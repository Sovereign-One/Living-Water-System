import unittest
from datetime import date

from collector import FIELDS, daily_series, merge, read_csv, write_csv


class CollectorTest(unittest.TestCase):
    def test_daily_series_skips_incomplete_current_utc_day(self):
        payload = {"views": [
            {"timestamp": "2026-11-20T00:00:00Z", "count": 8, "uniques": 3},
            {"timestamp": "2026-11-21T00:00:00Z", "count": 90, "uniques": 7},
        ]}
        self.assertEqual(
            daily_series(payload, "views", date(2026, 11, 21)),
            {"2026-11-20": (8, 3)},
        )

    def test_backfills_upserts_preserves_old_dates_and_cumulatives(self):
        today = date(2026, 11, 21)
        rows = merge({}, {"2026-11-18": (2, 1), "2026-11-20": (4, 2)},
                     {"2026-11-19": (3, 1)}, today, "2026-11-21T06:23:00Z")
        self.assertEqual(len(rows), 3)
        self.assertEqual(rows["2026-11-20"]["archived_cumulative_views"], "6")
        self.assertEqual(rows["2026-11-20"]["archived_cumulative_clones"], "3")
        serialized = write_csv(rows)
        self.assertEqual(tuple(serialized.splitlines()[0].split(",")), FIELDS)
        existing = read_csv(serialized)
        updated = merge(existing, {"2026-11-20": (6, 2)}, {}, date(2026, 11, 22), "2026-11-22T06:23:00Z")
        self.assertEqual(updated["2026-11-18"]["views"], "2")
        self.assertEqual(updated["2026-11-20"]["views"], "6")
        self.assertEqual(updated["2026-11-21"]["views"], "0")
        self.assertEqual(updated["2026-11-21"]["archived_cumulative_views"], "8")

    def test_same_payload_rerun_does_not_change_csv(self):
        v = {"2026-11-20": (6, 4)}
        rows = merge({}, v, {}, date(2026, 11, 21), "2026-11-21T06:23:00Z")
        first = write_csv(rows)
        again = write_csv(merge(read_csv(first), v, {}, date(2026, 11, 21), "2026-11-21T12:00:00Z"))
        self.assertEqual(first, again)

    def test_reject_incorrect_existing_csv(self):
        with self.assertRaises(ValueError):
            read_csv("date,views\n2026-11-20,4\n")


if __name__ == "__main__":
    unittest.main()
