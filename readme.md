# paperAgent

`paperAgent` is an interactive paper-writing project scaffold for agents. It is designed for workflows where a user first gives a topic, the agent then asks targeted clarification questions, and only after that starts literature collection, outlining, drafting, revision, and final `docx` delivery.

This project is not meant to be a one-shot text generator. Its intended behavior is closer to a research-writing assistant that can narrow the topic, identify the paper type, lock the output language, collect evidence, and write a paper project step by step.

## What It Does

- turns a rough topic into a structured paper project
- asks for paper type first instead of assuming every request is the same
- supports Chinese or English output
- stores user answers in an intake artifact before drafting
- separates outline, notes, references, draft, and final deliverable
- exports a final `final-manuscript.docx`
- keeps reusable writing rules, prompts, and references outside the paper workspace

## Intended Use

`paperAgent` is useful when you want an agent to help with tasks such as:

- course papers
- degree-thesis early drafts
- technical reports
- survey or review papers
- journal or conference-paper preparation
- proposal-style academic writing

It is especially useful when the user only has a topic at first and needs the agent to guide the clarification process.

## Core Workflow

1. The user gives a topic.
2. The agent asks for the paper type.
3. The agent asks whether the output should be in Chinese or English.
4. The agent asks only the next few questions that actually matter.
5. The answers are written into `intake.md`.
6. The agent derives `brief.md`, then builds the outline and draft.
7. The final deliverable is exported as `final-manuscript.docx`.

The intended interaction style is short-round, adaptive, and discussion-like rather than a long rigid form.

## Project Structure

```text
paperAgent/
├─ skills/
│  └─ SKILL.md
├─ ref/
│  ├─ interactive-intake.md
│  ├─ paper-template.md
│  ├─ citation-style.md
│  ├─ source-priority.md
│  └─ quality-checklist.md
├─ script/
│  ├─ init_paper_project.ps1
│  ├─ build_search_queries.py
│  ├─ export_final_docx.py
│  └─ open_chrome_search.ps1
├─ log/
│  ├─ task-history.md
│  └─ revision-log.md
├─ papers/
│  └─ .gitkeep
└─ readme.md
```

## Key Files

- [skills/SKILL.md](skills/SKILL.md): main agent behavior contract
- [ref/interactive-intake.md](ref/interactive-intake.md): how the intake dialogue should work
- [ref/paper-template.md](ref/paper-template.md): default manuscript structure
- [script/init_paper_project.ps1](script/init_paper_project.ps1): create a new paper project folder
- [script/export_final_docx.py](script/export_final_docx.py): export the manuscript to `docx`

## Default Paper Project Layout

Each paper task is expected to generate a new folder under `papers/` with files such as:

- `intake.md`
- `brief.md`
- `outline.md`
- `draft.md`
- `references.md`
- `notes.md`
- `final-manuscript.docx`

## Design Principles

- ask before drafting
- do not assume paper type
- do not assume output language
- keep evidence traceable
- separate raw notes from the final manuscript
- reduce repetitive, generic AI-sounding prose during revision
- keep real paper content out of the public project by default

## Repository Policy

This repository is meant to publish the reusable project scaffold only.

- `papers/` is kept as an empty tracked directory
- real user paper projects should not be committed
- `log/` should keep templates rather than private task records
- `.gitignore` already excludes paper-project contents and Python cache files

## Current Limits

- Word COM automation is not the default path; `docx` export currently uses a Python-based OpenXML generator
- the default export focuses on structure and readability, not on fully polished academic typography
- the quality of the final manuscript still depends on the quality of the interactive intake and source selection

## Recommended Next Steps

If you want to extend `paperAgent`, common next steps are:

- add richer Word styling such as a cover page, page numbers, and hanging-indent references
- connect Zotero or a local reference manager
- add venue-specific templates
- add stronger revision heuristics for lowering repetition and AI-like phrasing

