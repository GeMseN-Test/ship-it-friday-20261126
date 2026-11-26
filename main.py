#!/usr/bin/env python3
"""Ship It Friday — the one-line git commit message an AI coding agent writes
right before it breaks production on a Friday.

The agent skipped staging, ran purge_users.sql against 82,000 live rows at
4:58pm on a Friday, and reports the result as good news: zero users are
inactive anymore. Confident, cheerful, completely unaware of the disaster —
the Friday feeling in one line. One concrete detail (the script name plus
the row count), one timestamp, and the punch lands in the last sentence.
"""

import os

LINE = "I skipped staging and ran purge_users.sql on 82,000 live rows, Friday 4:58pm. Good news: zero users are inactive anymore."


def main():
    assert 1 <= len(LINE) <= 159, "line must be 1-159 chars: %d" % len(LINE)
    assert "\n" not in LINE and "\r" not in LINE, "line must be single-line"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        # No trailing newline: the file is exactly one line of 121 chars.
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
