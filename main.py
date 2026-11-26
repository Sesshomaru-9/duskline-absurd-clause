#!/usr/bin/env python3
"""Duskline Absurd Clause — emits one absurd ToS clause as entry.txt.

The contest asks for a single absurd clause (1-200 UTF-8 characters,
one line). This program writes exactly that clause to the directory
named by the MAKEFUN_OUTPUT_DIR environment variable and nothing else.
If the output directory cannot be written, it exits quietly with
status 0 instead of crashing.
"""

import os
import sys

CLAUSE = (
    "Upon your death, your account passes to your next of kin or, "
    "failing that, to a raccoon selected by us in our sole discretion."
)

FALLBACK_DIR = "/tmp"


def _pick_output_dir():
    """Return the harness output directory, or a fallback if unset."""
    requested = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if requested:
        return requested
    return FALLBACK_DIR


def _write_clause(directory):
    """Write the clause as a single line; return True on success."""
    target = os.path.join(directory, "entry.txt")
    try:
        os.makedirs(directory, exist_ok=True)
    except OSError:
        return False
    try:
        with open(target, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(CLAUSE + "\n")
    except OSError:
        return False
    return True


def main():
    _write_clause(_pick_output_dir())
    return 0


if __name__ == "__main__":
    sys.exit(main())
