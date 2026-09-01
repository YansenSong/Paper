# AGENTS.md

## Purpose

This repository contains a reusable academic-paper skeleton written in LaTeX. Coding agents should act as careful LaTeX engineers and academic writing assistants. The human author owns all scientific judgments and final approval.

## Branch policy

Before editing, check the current Git branch.

- `main` is the reusable skeleton branch. It should contain only generic LaTeX structure, tooling, agent instructions, and conventions that are useful across papers.
- Never add paper-specific titles, abstracts, claims, citations, experiments, results, figures, reviewer responses, or venue-specific content directly to `main`.
- For work on a concrete paper, create or switch to a dedicated branch from the latest `main`, preferably named `paper/<short-name>` or `paper/<venue>-<year>-<short-name>`.
- Treat the dedicated paper branch as the integration branch for that paper.
- If smaller task branches are useful, create them from the paper branch under a separate namespace such as `work/<short-name>/<task>`.
- Do not merge paper-specific content back into `main`.
- If a concrete paper reveals a genuinely reusable scaffold improvement, apply that improvement to `main` separately without bringing paper-specific content with it.

If the environment permits branch creation and the user requests concrete paper work while on `main`, create the appropriate paper branch before editing. If branch creation is not permitted, do not put paper-specific content on `main`; report the limitation instead.

## Non-negotiable scientific-integrity rules

1. Never fabricate citations, papers, authors, venues, URLs, DOIs, datasets, numerical results, baselines, ablations, statistical tests, or qualitative findings.
2. Do not add a citation unless the reference is already present in `refs.bib` or its bibliographic metadata has been independently verified by the human author or an approved source.
3. Never change experimental numbers merely to improve the narrative.
4. Never claim significance, superiority, novelty, state of the art, robustness, causality, or generalization unless the evidence in the repository supports that claim.
5. When required evidence is missing, insert a clear `TODO(author)` comment instead of guessing.
6. Preserve the scientific meaning of equations, definitions, assumptions, and notation unless explicitly instructed to change them.

## Repository structure

- `main.tex`: paper entry point.
- `sections/`: major paper sections.
- `refs.bib`: verified bibliography entries.
- `figures/`: paper figures or generated figure outputs.
- `tables/`: reusable table fragments when needed.
- `scripts/`: reproducible helper scripts for figures, checks, and paper tooling.
- `notes/`: author notes, experiment notes, and reviewer feedback. Content here is not automatically paper-ready.

## Writing rules

- Prefer concise, precise academic prose.
- Preserve the author's technical terminology unless consistency requires a local correction.
- Define terminology before first use.
- Keep notation consistent across sections.
- Distinguish observations from interpretations and hypotheses.
- Avoid promotional language and unsupported adjectives.
- Do not silently remove caveats, limitations, negative results, or contradictory evidence.
- If a requested rewrite changes meaning, flag the change instead of silently applying it.

## LaTeX rules

- Keep major sections in `sections/*.tex` and include them from `main.tex`.
- Use `\label{}` and `\ref{}`/`\eqref{}` consistently.
- Use `\cite{}` only with valid keys from `refs.bib`.
- Prefer semantic LaTeX over manual spacing and formatting hacks.
- Use `booktabs` conventions for tables.
- Keep figures under `figures/` and scripts that generate them under `scripts/`.
- Do not edit generated LaTeX auxiliary files.
- Avoid adding packages unless they solve a concrete need and do not conflict with the target venue template.

## Required workflow after edits

1. Check the current Git branch and enforce the branch policy above.
2. Read the relevant surrounding sections before editing.
3. Make the smallest coherent change that satisfies the request.
4. Run `make` after LaTeX edits when a TeX toolchain is available.
5. Run `make check-refs` after citation edits.
6. Fix compilation errors introduced by the change.
7. Inspect warnings for undefined references/citations, duplicate labels, and severe overfull boxes.
8. Review `git diff` and summarize what changed, what was validated, and any unresolved TODOs.

## Editing boundaries

If the user restricts edits to particular files or sections, do not modify anything outside that scope unless necessary to keep the paper compiling. If an out-of-scope change is necessary, explain it clearly.

## Experiments and generated artifacts

If experiment code or results are later added to this repository:

- Treat raw recorded outputs as source data; do not hand-edit them to match prose.
- Prefer scripts that deterministically generate figures and tables from recorded results.
- Record configuration, seed, environment, and input paths when practical.
- Update paper claims only after reading the actual outputs.

## Completion report

At the end of a task, report:

- current branch;
- files changed;
- main substantive changes;
- commands/checks run and their outcomes;
- unresolved warnings or `TODO(author)` items.
