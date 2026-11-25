"""One Line, One Laugh entry (02).

Writes a single original joke line to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output when the variable is unset).
Python 3.13, standard library only, deterministic, no network.
"""

import os

LINE = "I googled 'how to be spontaneous' and made a spreadsheet of the results."

# The gate requires 1-200 characters, a single line, valid UTF-8.
assert 1 <= len(LINE) <= 200, "entry line out of range"
assert "\n" not in LINE and "\r" not in LINE, "entry must be one line"
assert LINE.strip(), "entry must not be only whitespace"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
