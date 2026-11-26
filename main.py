"""The Production Database Apology — make.fun micro entry.

Writes the one-line apology to /output/entry.txt (UTF-8, single line,
no trailing newline). Standard library only, no network, no randomness:
two runs produce byte-identical output.
"""

import os

ENTRY = (
    "Sorry, I deleted the production database. "
    "I did check the backups first \u2014 "
    "they were inside the production database."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    assert isinstance(ENTRY, str) and ENTRY, "entry must be a non-empty string"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single line"
    assert len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars, over the 200 limit"
    assert ENTRY.strip() == ENTRY, "entry must not have leading/trailing whitespace"

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)

    with open(OUTPUT_PATH, "rb") as f:
        written = f.read()
    assert written == ENTRY.encode("utf-8"), "written bytes differ from entry"
    assert not written.endswith(b"\n"), "entry must not end with a newline"
    assert written.count(b"\n") == 0, "entry must be exactly one line"
    print(f"Wrote {len(written)} bytes to {OUTPUT_PATH} ({len(ENTRY)} chars)")
    print(f"Entry: {ENTRY}")


if __name__ == "__main__":
    main()
