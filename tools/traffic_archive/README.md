# Private, daily GitHub traffic archive

This collector archives **Living-Water-System** daily GitHub traffic counts to a **separate private repository**. The public source repository contains only code, never visitor statistics or credentials.

The scheduled GitHub Actions job runs daily at 06:23 UTC and collects completed UTC days for page views, unique visitors per day, repository clones, and unique cloners per day. GitHub exposes approximately the previous 14 days of traffic; the script backfills available days on its first run, then refreshes overlapping days without creating duplicate date rows.

**Destination:** `data/daily_traffic.csv` on the `main` branch of the PRIVATE repository `Sovereign-One/living-water-traffic-private`.

## One-time setup (account owner)

1. Create a GitHub repository named **`living-water-traffic-private`**, owned by **`Sovereign-One`**. Select **Private**, and **Add a README** to initialize its default `main` branch. Confirm it is private. The connected assistant cannot create a private repository or save GitHub Actions secrets.
2. Create a **fine-grained personal access token** restricted to **only** `Sovereign-One/Living-Water-System`, granting **Administration: Read-only**. In the PUBLIC source repository, go to **Settings → Secrets and variables → Actions → New repository secret**. Store that token under the name **`TRAFFIC_READ_TOKEN`**.
3. Create a **second fine-grained token** restricted to **only** `Sovereign-One/living-water-traffic-private`, granting **Contents: Read and write**. In the PUBLIC source repository, store it as another Actions repository secret named **`ARCHIVE_WRITE_TOKEN`**.
4. In `Living-Water-System`, go to **Actions → Archive repository traffic privately → Run workflow** to test. Then verify the private CSV appears in the private repository.

**Keep both tokens secret.** Do not paste them into chat, Issues, source code, or documentation. Token expiry or permission changes may interrupt collection. The workflow intentionally skips collection if either token has not been configured.

## CSV columns

`date_utc,views,unique_visitors_per_day,clones,unique_cloners_per_day,archived_cumulative_views,archived_cumulative_clones,last_observed_utc`

- The **cumulative views and clones** cover archived dates only, **not** the repository's full lifetime.
- GitHub's **daily unique** visitor/cloner counts cannot be summed to calculate lifetime unique people.
- The collector updates any day where GitHub revises its reported totals. It never duplicates a date.
- GitHub may include your own views and some automated clone activity. Traffic numbers do not prove people read or used the designs.
- It collects aggregate numbers only, not identities or IP addresses.
- It does **not** write stats into the publicly visible Living-Water-System repository or its Actions logs.
- If a scheduled workflow is delayed or skips, GitHub's limited lookback means some data can eventually be lost. Check workflow runs periodically.

The collector uses Python's standard library and the [GitHub traffic API](https://docs.github.com/en/rest/metrics/traffic). The private CSV can be downloaded or charted later.
