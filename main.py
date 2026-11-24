#!/usr/bin/env python3
"""Demo -- the one word my ex would use to describe me.

For the make.fun bounty "One Word From Your Ex". The program drops a
single word into /output/entry.txt and does nothing else. It uses only
the standard library, opens no other files, and never touches the
network, so a second run writes byte-for-byte the same file.
"""

import os
import sys

WORD = "Demo"
LIMIT = 24


def check_word(word):
    """Refuse anything that is not one plain word within the gate."""
    if not isinstance(word, str):
        raise TypeError("word must be text, got %s" % type(word).__name__)
    if word == "":
        raise ValueError("word must not be empty")
    if len(word) > LIMIT:
        raise ValueError("word is %d chars, limit is %d" % (len(word), LIMIT))
    if word.strip() != word:
        raise ValueError("word must not start or end with whitespace")
    if len(word.split()) != 1:
        raise ValueError("word must be a single token, no spaces inside")
    if not word.isalpha():
        raise ValueError("word must be letters only")
    if not word.isascii():
        raise ValueError("word must be plain ASCII letters")
    for letter in word:
        if ord(letter) < 0x20 or ord(letter) == 0x7F:
            raise ValueError("word must not hold control characters")
    word.encode("utf-8")
    return word


def save_word(word, folder):
    """Write the word to entry.txt through a staging file, then confirm."""
    word = check_word(word)
    os.makedirs(folder, exist_ok=True)
    target = os.path.join(folder, "entry.txt")
    staged = target + ".staging"
    payload = word.encode("utf-8")
    with open(staged, "wb") as handle:
        handle.write(payload)
        handle.flush()
        os.fsync(handle.fileno())
    os.replace(staged, target)
    folder_fd = os.open(folder, os.O_RDONLY)
    try:
        os.fsync(folder_fd)
    finally:
        os.close(folder_fd)
    with open(target, "rb") as handle:
        stored = handle.read()
    if stored != payload:
        raise ValueError("entry.txt does not match the word")
    return len(word)


def main():
    folder = os.environ.get("OUTPUT_DIR", "/output")
    size = save_word(WORD, folder)
    print("entry.txt holds %d characters" % size)
    return 0


if __name__ == "__main__":
    sys.exit(main())
