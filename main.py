#!/usr/bin/env python3
"""Entry for make.fun: The Funniest Honest Appliance Error.

Writes one line, the funniest honest error message an appliance could
show, to /output/entry.txt. Standard library only, no network, no input
files: the line is baked into this program.
"""

import os

ENTRY = (
    "ERROR 04: Door open 7 minutes. I am a fridge, not a window. "
    "Your milk is now 12 degrees and judging you too."
)


def main() -> None:
    if not 1 <= len(ENTRY) <= 200:
        raise SystemExit("entry must be 1-200 characters")
    if "\n" in ENTRY or not ENTRY.strip():
        raise SystemExit("entry must be a single non-blank line")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
