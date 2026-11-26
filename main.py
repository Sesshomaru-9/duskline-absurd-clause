#!/usr/bin/env python3
"""Duskline Absurd Clause — make.fun bounty u-donrulezz-the-absurd-clause-contest-035cc0f1.

Writes one absurd terms-of-service clause (a single English sentence,
no more than 200 characters) to $MAKEFUN_OUTPUT_DIR/entry.txt.
Deterministic, Python 3.13 standard library only, no network, no randomness.

Safety rules:
- Never writes into the repository directory: if the resolved output
  directory is the repo dir or inside it, refuse and exit 0.
- If MAKEFUN_OUTPUT_DIR is unset or empty, fall back to a fresh
  temporary directory outside the repo.
- Never raises: any failure exits 0 without writing anything.
"""

import os
import sys
import tempfile

ENTRY = "Upon your death, your account passes to your next of kin or, failing that, to a raccoon selected by us in our sole discretion."
# Joke idea: pure deadpan legal boilerplate — "upon your death", "passes
# to", "failing that", "in our sole discretion" — until the heir turns
# out to be a raccoon the company picked. One clean sentence, no setup,
# no explaining its own joke; the absurdity is a single concrete image
# (the raccoon) dropped into the driest possible register.
#
# Revision note: the first draft opened "In the event of your death, your
# account shall pass to ..." (141 chars). "Upon your death" and "passes
# to" say the same thing in fewer words and read more like real boilerplate,
# so the clause is now 126 characters with the joke untouched.

REPO_DIR = os.path.dirname(os.path.abspath(__file__))


def _is_in_repo(path):
    """True if path resolves to the repo dir or anywhere inside it."""
    try:
        resolved = os.path.realpath(path)
    except Exception:
        return True
    repo = os.path.realpath(REPO_DIR)
    return resolved == repo or resolved.startswith(repo + os.sep)


def main():
    try:
        if not 1 <= len(ENTRY) <= 200:
            return 0
        if not ENTRY.strip():
            return 0
        if "\n" in ENTRY or "\r" in ENTRY:
            return 0
        ENTRY.encode("utf-8")

        out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or ""
        if not out_dir:
            out_dir = tempfile.mkdtemp(prefix="duskline-absurd-clause-")
        if _is_in_repo(out_dir):
            return 0

        os.makedirs(out_dir, exist_ok=True)
        target = os.path.join(out_dir, "entry.txt")
        if _is_in_repo(target):
            return 0
        with open(target, "w", encoding="utf-8", newline="") as handle:
            handle.write(ENTRY)
        with open(target, "r", encoding="utf-8") as handle:
            back = handle.read()
        if back != ENTRY:
            try:
                os.remove(target)
            except Exception:
                pass
            return 0
    except Exception:
        return 0
    return 0


if __name__ == "__main__":
    sys.exit(main())
