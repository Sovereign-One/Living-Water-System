#!/usr/bin/env python3
"""Archive GitHub traffic into a separate PRIVATE GitHub repository.

Uses only the Python standard library. Nothing is written to the public
source repository. All timestamps and daily buckets use UTC.
"""
from __future__ import annotations

import base64
import csv
import io
import json
import os
import sys
from datetime import date, datetime, timedelta, timezone
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen

API_ROOT = "https://api.github.com"
API_VERSION = "2022-11-28"
DESTINATION_PATH = "data/daily_traffic.csv"
FIELDS = (
    "date_utc", "views", "unique_visitors_per_day", "clones",
    "unique_cloners_per_day", "archived_cumulative_views",
    "archived_cumulative_clones", "last_observed_utc",
)
COUNT_FIELDS = ("views", "unique_visitors_per_day", "clones", "unique_cloners_per_day")


def required_env(name: str) -> str:
    value = os.environ.get(name, "").strip()
    if not value:
        raise ValueError(f"Missing required configuration: {name}")
    return value


def validate_repo(name: str) -> str:
    parts = name.split("/")
    if len(parts) != 2 or any(not p or p in (".", "..") for p in parts):
        raise ValueError("Repository must be in owner/name format")
    return "/".join(quote(part, safe="-_.") for part in parts)


def api(method: str, path: str, token: str, data: dict | None = None, allow_404: bool = False):
    url = API_ROOT + path
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": "Bearer " + token,
        "X-GitHub-Api-Version": API_VERSION,
        "User-Agent": "living-water-traffic-archive",
    }
    body = None
    if data is not None:
        headers["Content-Type"] = "application/json; charset=utf-8"
        body = json.dumps(data).encode("utf-8")
    try:
        with urlopen(Request(url, data=body, method=method, headers=headers), timeout=30) as response:
            return json.loads(response.read().decode("utf-8"))
    except HTTPError as exc:
        if allow_404 and exc.code == 404:
            return None
        raise RuntimeError(f"GitHub API returned HTTP {exc.code} for {method} {path}") from exc
    except URLError as exc:
        raise RuntimeError(f"GitHub API unavailable while accessing {path}: {exc.reason}") from exc


def daily_series(payload: dict, key: str, today: date) -> dict[str, tuple[int, int]]:
    result = {}
    for item in payload.get(key, []):
        timestamp = item["timestamp"].replace("Z", "+00:00")
        day = datetime.fromisoformat(timestamp).astimezone(timezone.utc).date()
        if day >= today:
            continue
        count, uniques = int(item["count"]), int(item["uniques"])
        if count < 0 or uniques < 0:
            raise ValueError("GitHub reported a negative count")
        result[day.isoformat()] = (count, uniques)
    return result


def read_csv(content: str) -> dict[str, dict]:
    if not content.strip():
        return {}
    reader = csv.DictReader(io.StringIO(content))
    if tuple(reader.fieldnames or ()) != FIELDS:
        raise ValueError("Private CSV has an unexpected header; refusing to overwrite it")
    result = {}
    for row in reader:
        day = date.fromisoformat(row["date_utc"])
        if day.isoformat() in result:
            raise ValueError("Duplicate dates in private CSV; refusing to overwrite it")
        for field in COUNT_FIELDS:
            if not row[field].isdigit():
                raise ValueError(f"Invalid count in CSV: {field}")
        result[day.isoformat()] = row
    return result


def merge(rows: dict[str, dict], views: dict[str, tuple[int, int]],
          clones: dict[str, tuple[int, int]], today: date, sampled: str) -> dict[str, dict]:
    """Upsert GitHub's overlapping 14-day buckets, keeping one row per UTC day."""
    all_days = set(views) | set(clones)
    first_day = date.fromisoformat(min(all_days)) if all_days else today - timedelta(days=1)
    day = first_day
    while day < today:
        key = day.isoformat()
        view_count, unique_views = views.get(key, (0, 0))
        clone_count, unique_clones = clones.get(key, (0, 0))
        candidate = {
            "date_utc": key,
            "views": str(view_count),
            "unique_visitors_per_day": str(unique_views),
            "clones": str(clone_count),
            "unique_cloners_per_day": str(unique_clones),
        }
        previous = rows.get(key)
        if previous is None or any(previous[field] != candidate[field] for field in COUNT_FIELDS):
            candidate["last_observed_utc"] = sampled
            rows[key] = candidate
        day += timedelta(days=1)

    view_total = clone_total = 0
    for key in sorted(rows):
        record = rows[key]
        view_total += int(record["views"])
        clone_total += int(record["clones"])
        record["archived_cumulative_views"] = str(view_total)
        record["archived_cumulative_clones"] = str(clone_total)
    return rows


def write_csv(rows: dict[str, dict]) -> str:
    buffer = io.StringIO(newline="")
    writer = csv.DictWriter(buffer, fieldnames=FIELDS, lineterminator="\n")
    writer.writeheader()
    for day in sorted(rows):
        writer.writerow(rows[day])
    return buffer.getvalue()


def main() -> None:
    source = validate_repo(required_env("SOURCE_REPO"))
    archive = validate_repo(required_env("ARCHIVE_REPO"))
    read_token = required_env("TRAFFIC_READ_TOKEN")
    write_token = required_env("ARCHIVE_WRITE_TOKEN")
    if source == archive:
        raise ValueError("Archive repository must be different from the public source repository")

    utc_now = datetime.now(timezone.utc)
    sampled = utc_now.isoformat(timespec="seconds").replace("+00:00", "Z")
    today = utc_now.date()
    views_payload = api("GET", f"/repos/{source}/traffic/views?per=day", read_token)
    clones_payload = api("GET", f"/repos/{source}/traffic/clones?per=day", read_token)
    views = daily_series(views_payload, "views", today)
    clones = daily_series(clones_payload, "clones", today)

    path = f"/repos/{archive}/contents/{DESTINATION_PATH}"
    old_file = api("GET", path, write_token, allow_404=True)
    if old_file is None:
        old_text, sha = "", None
    else:
        if old_file.get("type") != "file" or old_file.get("encoding") != "base64":
            raise ValueError("Private archive CSV is not a regular base64-encoded file")
        sha = old_file["sha"]
        old_text = base64.b64decode(old_file["content"]).decode("utf-8")

    rows = merge(read_csv(old_text), views, clones, today, sampled)
    new_text = write_csv(rows)
    if old_text == new_text:
        print(f"No traffic changes to archive. Existing UTC days: {len(rows)}.")
        return
    payload = {
        "message": f"Archive GitHub traffic through {today - timedelta(days=1):%Y-%m-%d} UTC",
        "content": base64.b64encode(new_text.encode("utf-8")).decode("ascii"),
        "branch": "main",
    }
    if sha:
        payload["sha"] = sha
    api("PUT", path, write_token, payload)
    print(f"Archived {len(rows)} UTC daily rows in private repository {archive}.")
    print("Note: summing daily unique visitors does NOT count unique people across the archive.")


if __name__ == "__main__":
    try:
        main()
    except (ValueError, RuntimeError) as error:
        print(f"Traffic archive not updated: {error}", file=sys.stderr)
        sys.exit(1)
