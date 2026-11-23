#!/usr/bin/env python3
"""Write the one-line office joke to /output/entry.txt.

Deterministic: the same bytes on every run, no randomness, no I/O
besides the single output file.
"""

import os

JOKE = (
    "I asked for a quiet day to focus, so my team booked a "
    "'Focus Time' meeting with twelve people and an agenda."
)


MIN_LEN = 1
MAX_LEN = 199


def validate_joke(text):
    """Check the joke against the competition gate (RULES.txt).

    Returns the text unchanged when every check passes, so the
    written bytes are exactly the JOKE constant.
    """
    assert text == text.strip(), "joke must not start or end with whitespace"
    assert MIN_LEN <= len(text) <= MAX_LEN, "joke must be 1-199 characters"
    assert "\n" not in text and "\r" not in text, "joke must be one line"
    assert text.encode("utf-8").decode("utf-8") == text, "joke must be valid UTF-8"
    return text


def main():
    text = validate_joke(JOKE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
