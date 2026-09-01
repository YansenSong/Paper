#!/usr/bin/env python3
"""Check that citation keys used by LaTeX files exist in refs.bib.

This intentionally uses only the Python standard library so it can run in a
minimal paper-writing environment. It is a lightweight guard, not a full TeX
or BibTeX parser.
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BIB = ROOT / "refs.bib"

CITE_RE = re.compile(r"\\cite\w*\s*(?:\[[^\]]*\]\s*)*\{([^}]*)\}")
BIB_KEY_RE = re.compile(r"@\w+\s*\{\s*([^,\s]+)\s*,", re.IGNORECASE)


def strip_comments(text: str) -> str:
    lines = []
    for line in text.splitlines():
        match = re.search(r"(?<!\\)%", line)
        if match:
            line = line[: match.start()]
        lines.append(line)
    return "\n".join(lines)


def citation_keys() -> set[str]:
    keys: set[str] = set()
    for path in ROOT.rglob("*.tex"):
        text = strip_comments(path.read_text(encoding="utf-8"))
        for group in CITE_RE.findall(text):
            keys.update(key.strip() for key in group.split(",") if key.strip())
    return keys


def bibliography_keys() -> set[str]:
    if not BIB.exists():
        return set()
    return set(BIB_KEY_RE.findall(BIB.read_text(encoding="utf-8")))


def main() -> int:
    cited = citation_keys()
    available = bibliography_keys()
    missing = sorted(cited - available)

    if missing:
        print("Missing BibTeX keys:")
        for key in missing:
            print(f"  - {key}")
        return 1

    print(f"Citation check passed: {len(cited)} cited key(s), {len(available)} BibTeX entrie(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
