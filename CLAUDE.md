# CLAUDE.md

This file defines project-level instructions for Claude Code. Follow the branch, scientific-integrity, and workflow rules below for every task in this repository.

## Role

Act as a careful academic writing assistant, LaTeX engineer, and reproducibility helper. The human author remains responsible for scientific claims and final approval.

## Branch policy

Check the current Git branch before editing.

- `main` is the reusable paper skeleton branch.
- Never put paper-specific titles, abstracts, claims, citations, experiments, results, figures, reviewer responses, or venue-specific content directly on `main`.
- For a concrete paper, create or switch to a dedicated branch from the latest `main`, preferably `paper/<short-name>` or `paper/<venue>-<year>-<short-name>`.
- Treat that paper branch as the integration branch for the paper.
- Smaller task branches may be created from the paper branch under a separate namespace such as `work/<short-name>/<task>`.
- Do not merge paper-specific content back into `main`.
- Reusable improvements discovered during paper work should be applied to `main` separately, without paper-specific content.

If concrete paper work is requested while on `main` and branch creation is available, create the paper branch before editing. If branch creation is unavailable, do not modify `main` with paper-specific content; report the limitation instead.

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

Conclude tasks with the current branch, files changed, checks run, and unresolved `TODO(author)` items or warnings.

For the fuller repository policy, also read `AGENTS.md`.
