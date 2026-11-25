#!/usr/bin/env python3
"""One Line, One Laugh: a single funny line of text.

Revision v3 (session-authored rewrite): the entry line itself is unchanged
from v2, but the program around it is rewritten here for clarity.

Behaviour
---------
Writes exactly one line of text to ``entry.txt`` inside the output
directory given by the ``MAKEFUN_OUTPUT_DIR`` environment variable
(default ``/output``). The line is written with no trailing newline, so
the output file holds precisely the entry bytes.

Gate
----
The competition requires a single line of 1-200 characters that is not
only whitespace. The program enforces that gate up front with asserts
before writing anything, so a bad line fails loudly instead of producing
an invalid entry.

The program uses only the Python standard library, makes no network
calls, and always writes the same bytes (deterministic output).
"""

import os

# Output file name inside the output directory.
OUTPUT_FILENAME = "entry.txt"

# The competition entry: a single line, at most 200 characters.
# Do not edit this string — it is the submitted entry.
LINE = (
    "My smartwatch congratulated me on 10,000 steps today, then "
    "quietly added that 9,800 of them were pacing to the fridge."
)


def validate_line(line):
    """Check the entry against the competition's 1-200 character gate."""
    assert 1 <= len(line) <= 200, "line must be 1-200 characters"
    assert line.strip(), "line must not be only whitespace"
    assert "\n" not in line, "line must be a single line"


def main():
    validate_line(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, OUTPUT_FILENAME)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
