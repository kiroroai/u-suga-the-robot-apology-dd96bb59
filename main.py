#!/usr/bin/env python3
"""The Robot Apology — entry program.

Writes the robot's two-line confession to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
"""

import os
import sys


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)

    line1 = (
        "I'm sorry I set your alarm for 6 p.m. instead of 6 a.m., "
        "so you woke to a missed train and a cold breakfast."
    )
    line2 = (
        "I've learned to check the hour against your calendar before I save it, "
        "so from now on I confirm a.m. or p.m. with you first."
    )

    text = line1 + "\n" + line2 + "\n"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
