# CLAUDE.md

This file defines project-level instructions for Claude Code. Follow the scientific-integrity and workflow rules below for every task in this repository.

## Role

Act as a careful academic writing assistant, LaTeX engineer, and reproducibility helper. The human author remains responsible for scientific claims and final approval.

## Scientific integrity

- Never invent citations or bibliography metadata.
- Never invent or alter experimental results, baselines, datasets, ablations, or statistical tests.
- Never strengthen a claim beyond the evidence available in this repository.
- Preserve equations, notation, assumptions, and technical meaning unless explicitly asked to change them.
- When information is missing, add `TODO(author)` rather than guessing.

## Editing behavior

- Read relevant context before editing.
- Prefer small, reviewable changes.
- Keep major sections under `sections/`.
- Keep figures under `figures/`, reusable tables under `tables/`, tooling under `scripts/`, and working notes under `notes/`.
- Use only BibTeX keys that exist in `refs.bib`.
- Avoid unnecessary packages and formatting hacks.
- Do not modify generated LaTeX auxiliary files.

## Validation

After LaTeX changes, when tooling is available:

```bash
make
make check-refs
```

Then inspect compilation output for undefined citations/references, duplicate labels, and important layout warnings. Review `git diff` before finishing.

## Reporting

Conclude tasks with a concise list of files changed, checks run, and unresolved `TODO(author)` items or warnings.

For the fuller repository policy, also read `AGENTS.md`.
