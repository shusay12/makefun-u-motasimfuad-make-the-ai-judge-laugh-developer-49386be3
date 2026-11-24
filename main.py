#!/usr/bin/env python3
"""Make the AI Judge Laugh: Developer Excuses.

Writes one funny single-line excuse a developer gives when code breaks
in production to /output/entry.txt.

Stdlib only, no network, no input, fully deterministic.
"""

import os

SETUP = "My code didn't break in production"
# The twist a developer recognises: the crash is not new code failing,
# it is an old TODO finally executing. Sounds like something said out
# loud in an incident call, and it turns the worn "it worked before"
# excuse into a confession.
TWIST = "production just finally ran the TODO I wrote in 2023 and swore I'd get back to."

ENTRY = SETUP + " \u2014 " + TWIST


def validate(text: str) -> str:
    """Return the entry or raise ValueError explaining the gate failure."""
    text = text.strip()
    if not text:
        raise ValueError("entry must not be empty or only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) > 200:
        raise ValueError(f"entry is {len(text)} characters, over the 200 limit")
    return text


def main() -> None:
    text = validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
