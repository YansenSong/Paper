#!/usr/bin/env python3
"""Entry point for reproducible figure generation.

Replace this scaffold with code that reads recorded experiment outputs and
writes deterministic figure files into ../figures/. Do not hard-code paper
results here merely to match the manuscript.
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIGURES = ROOT / "figures"


def main() -> None:
    FIGURES.mkdir(parents=True, exist_ok=True)
    print(f"Figure directory ready: {FIGURES}")
    print("TODO(author): implement figure generation from recorded experiment data.")


if __name__ == "__main__":
    main()
