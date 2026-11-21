#!/usr/bin/env python3
"""Entry point for the the-poem-about-permission-20261121-0235 entry.

The poem is the entry: a short poem about agency — total
permission, given wordlessly and honoured exactly. She
hands over her phone unlocked; he does the one errand he
was handed it for, gives it back, and her trust is proved
by the smallest fact in the poem: she never looked up.
Running the program writes the poem, exactly as held in
POEM_LINES below, to /output/entry.txt.

The competition gate accepts UTF-8 text of 1 to 280
Unicode code points that is not only white space; the
poem is 215 code points of plain ASCII, so it sits inside
the gate with margin. Only the Python standard library
is used, and the program needs no network.
"""

import os
import sys

DEST_DIR = "/output"
DEST_NAME = "entry.txt"
MAX_CODE_POINTS = 280

POEM_LINES = [
    "She hands me her phone, unlocked.",
    "\"Find the photo,\" she says,",
    "and turns back to the stove.",
    "Everything she owns is in my hand:",
    "her banks, her letters, her years.",
    "I find the photo. I hand it back.",
    "She never looked up.",
]

POEM = "\n".join(POEM_LINES)


def poem_problem(text):
    """Return a problem string, or None when the gate passes."""
    if not text.strip():
        return "the poem is only white space"
    if len(text) > MAX_CODE_POINTS:
        return "the poem is over 280 code points"
    return None


def main():
    problem = poem_problem(POEM)
    if problem is not None:
        print("refusing to write entry.txt: " + problem, file=sys.stderr)
        return 1
    os.makedirs(DEST_DIR, exist_ok=True)
    dest = os.path.join(DEST_DIR, DEST_NAME)
    with open(dest, "w", encoding="utf-8", newline="") as handle:
        handle.write(POEM)
    with open(dest, "r", encoding="utf-8", newline="") as handle:
        written = handle.read()
    if written != POEM:
        print("read-back mismatch in " + dest, file=sys.stderr)
        return 1
    print("wrote " + dest + ": " + str(len(written)) + " code points")
    return 0


if __name__ == "__main__":
    sys.exit(main())
