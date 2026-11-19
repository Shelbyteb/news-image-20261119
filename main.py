#!/usr/bin/env python3
"""Entry for make.fun news-image-20261119.

Writes the front-page image of Thursday 19 November 2026's world news
to $MAKEFUN_OUTPUT_DIR/entry.png (or /output/entry.png by default).

The image is drawn once, ahead of time, and shipped in this repository;
the program only copies it, so both graded runs write identical bytes.
Standard library only; no network.
"""
import os
import shutil
import sys


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    if not os.path.isfile(src):
        print("entry.png missing from repository", file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(src, os.path.join(out_dir, "entry.png"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
