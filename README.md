# Paper

Agent-friendly LaTeX research paper repository for use with Codex, Claude Code, and other coding agents.

## Structure

```text
.
├── main.tex
├── refs.bib
├── AGENTS.md
├── CLAUDE.md
├── Makefile
├── sections/
├── figures/
├── tables/
├── scripts/
└── notes/
```

## Build

Install a TeX distribution with `latexmk`, then run:

```bash
make
```

Clean generated files with:

```bash
make clean
```

Check citation keys with:

```bash
make check-refs
```

## Agent workflow

1. Read `AGENTS.md` or `CLAUDE.md` before editing.
2. Read the whole paper before making structural changes.
3. Never fabricate citations, results, datasets, baselines, or statistics.
4. Make focused edits.
5. Compile with `make` after LaTeX changes.
6. Review `git diff` before committing.

The human author remains responsible for scientific claims and final approval.
