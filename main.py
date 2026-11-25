#!/usr/bin/env python3
"""One Line, One Laugh: a single funny line of text.

The program writes a single line, at most 200 characters, to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output). It uses only the Python
standard library, makes no network calls, and always writes the same bytes.
"""

import os

LINE = (
    "My smartwatch congratulated me on 10,000 steps today, then "
    "quietly added that 9,800 of them were pacing to the fridge."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
    assert LINE.strip(), "line must not be only whitespace"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
