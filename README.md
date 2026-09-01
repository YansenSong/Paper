# Paper

Agent-friendly LaTeX research paper repository for use with Codex, Claude Code, and other coding agents.

## Repository model

This repository uses `main` as a reusable paper skeleton, not as a concrete paper project.

- `main` contains only generic LaTeX structure, tooling, agent instructions, and reusable conventions.
- Each concrete paper starts from the latest `main` and lives on its own long-lived branch.
- Paper-specific titles, abstracts, claims, citations, figures, experiments, results, and venue formatting belong only on the paper branch.
- Do not merge paper-specific content back into `main`.
- Improvements that are genuinely reusable across papers should be applied to `main` separately from the paper-specific work.

Recommended branch naming:

```text
paper/<short-name>
paper/<venue>-<year>-<short-name>
```

Example:

```bash
git switch main
git pull
git switch -c paper/icml-2027-my-method
```

If a paper needs smaller task branches for collaboration, branch them from the paper branch using a separate namespace, for example:

```text
work/my-method/introduction
work/my-method/experiments
work/my-method/reviewer-response
```

The paper branch is then the integration branch for that specific paper, while `main` remains clean and reusable.

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

1. Check the current Git branch before editing.
2. If on `main`, only make reusable scaffold/tooling changes. For a concrete paper, create or switch to its paper branch first.
3. Read `AGENTS.md` or `CLAUDE.md` before editing.
4. Read the whole paper before making structural changes.
5. Never fabricate citations, results, datasets, baselines, or statistics.
6. Make focused edits.
7. Compile with `make` after LaTeX changes.
8. Review `git diff` before committing.

The human author remains responsible for scientific claims and final approval.
