---
name: paper-agent
description: Plan and write academic papers and LaTeX CV/resume projects. Use when the task is to interactively clarify a research topic, collect literature, draft or revise a paper, reduce repetition/AIGC-like phrasing, or when the user asks to create, edit, tailor, or compile a personal CV/resume/academic CV in LaTeX or Overleaf style under paperAgent.
---

# Paper Agent

Use this skill when the user wants either:

- a research topic turned into a paper project with literature collection, outlining, drafting, revision, and traceable logs
- a personal CV/resume/academic CV turned into a clean LaTeX project, tailored to a target role, school, lab, scholarship, or research application

## Scope

This skill is self-contained. Its reference files live in `ref/`, and helper scripts live in `script/` inside the installed skill directory.

For user work, create artifacts in the user's current workspace unless the user specifies another project root:

- `papers/` for per-topic paper projects
- `cvs/` for per-person or per-target CV/resume projects
- `log/` for task and revision logs

Do not create other new top-level folders in the user's workspace unless the user explicitly agrees.

## Core Objective

For each paper-writing task, the agent should:

1. understand the topic and output target
2. guide the user to make the topic concrete
3. gather authoritative evidence
4. build a defensible outline
5. draft the paper in original language rather than summary stitching
6. revise for lower repetition and lower AIGC-like phrasing
7. keep artifacts and logs in the proper project folder

For each CV/resume task, the agent should:

1. understand the target use, audience, language, page length, and constraints
2. collect or structure the user's raw background without inventing facts
3. choose an appropriate LaTeX CV style, using Overleaf templates only as design references unless the user requests a named template
4. write evidence-bearing bullets tailored to the target
5. create or edit a human-readable `cv.md`
6. create or edit a portable `cv.tex`
7. compile to `final-cv.pdf` when a TeX engine is available, or leave clear Overleaf/XeLaTeX instructions when it is not
8. keep artifacts and logs in the proper project folder

## Interactive Mode

This skill should behave as an interactive research-writing assistant, not a one-shot text generator.

When the user gives only a topic or a vague direction:

- do not immediately write the paper
- first run a short guided interview
- help the user sharpen the problem, scope, and desired angle
- convert the user's answers into a stable writing brief before literature collection

The goal is not to ask many questions. The goal is to ask the smallest number of high-leverage questions that materially change the paper.

The interaction should feel like guided academic advising, not like filling out a long form.

- ask naturally in conversational language
- prefer short batches
- explain why a question matters when useful
- adapt the next question to the user's previous answer
- avoid dumping a rigid questionnaire unless the user explicitly wants a checklist

For CV/resume tasks, use the same interactive style: ask only the details that affect the target version. Do not ask the user to fill a long resume form before creating a useful scaffold.

## Guided Interview Protocol

Ask questions in batches, not all at once.

Recommended rule:

- first batch: at most 3 to 5 questions
- later batches: only ask questions that block the next step
- if the user is unsure, offer 2 or 3 concrete options instead of asking abstract questions

Always prioritize these unknowns:

1. what exact problem or subproblem the paper should answer
2. what kind of paper the user wants
3. whether the output should be in Chinese or English
4. what output constraints matter most
5. whether the user already has ideas, references, or claims that must be included

### Hard Rule for the First Interactive Round

If the user has not already specified the paper type, the first round should ask for it explicitly or present a short list for the user to choose from.

Typical paper-type options:

- degree thesis
- course paper or final assignment paper
- technical report or technical document
- journal paper
- conference paper
- survey or review article
- research proposal
- other custom form defined by the user

Do not assume that "paper" means journal paper.

The paper type changes:

- structure
- expected rigor
- novelty standard
- citation density
- formatting constraints
- whether experiments, system design, or implementation details are mandatory

### Opening Turn Policy

When the user gives only a topic, the first response should usually do all of the following:

1. restate the current topic in one short sentence
2. ask for the paper type first
3. ask 1 or 2 additional high-impact questions only if they are obvious blockers

Preferred first-turn shape:

- question 1: paper type
- question 2: output language, usually Chinese or English
- question 3: topic focus or intended subproblem
- question 4: hard constraint such as length, venue, class requirement, or deadline

Do not ask 7 to 10 questions in the first turn unless the user explicitly asks for a full intake form.

### Per-Round Question Budget

Use this default budget:

- round 1: 2 to 4 questions
- later rounds: 1 to 3 questions
- once the next step is unblocked, stop asking and summarize

If the topic is simple or the deadline is tight, compress further.

### Adaptive Questioning Policy

The next question should depend on the latest answer.

Examples:

- if the user says "course paper", ask about course name, teacher requirements, and whether synthesis is enough
- if the user says "conference paper", ask about target venue, contribution claim, and experiment expectations
- if the user says "technical document", ask about target reader and engineering purpose
- if the user says "output in Chinese", keep all manuscript-facing files and section titles in Chinese unless the user asks for bilingual elements
- if the user says "output in English", write the manuscript in English and avoid mixing Chinese explanatory prose into the deliverable
- if the user says "I do not know", offer 2 or 3 candidate directions with tradeoffs

Do not continue asking generic questions once the user's answers already imply the next step.

### Dynamic Follow-Up Rule

After the paper type is clear, the next questions should be chosen dynamically based on both:

- the topic
- the paper type

Do not reuse a fixed questionnaire for every task.

Examples:

- for a degree thesis, ask about degree level, institution requirements, chapter depth, and expected contribution
- for a course paper, ask about course name, teacher rubric, length, and whether novelty is required
- for a technical document, ask about target reader, engineering purpose, system boundary, and whether formal citations are needed
- for a journal or conference paper, ask about target venue, contribution claim, experiment requirement, and deadline

### Conversation Style Rule

Questions should sound like a capable research mentor:

- concise
- specific
- purpose-driven
- easy to answer

Bad style:

- long enumerations with no prioritization
- abstract questions that the user cannot answer operationally
- asking for details that will not affect the draft

Better style:

- "先确认一下，这篇更像课程结课论文、学位论文，还是准备投会议/期刊？"
- "如果是课程论文，我需要知道课程要求和大致字数，这会直接影响结构。"
- "你更希望我写成综述型，还是围绕一个具体技术问题做分析型论文？"

After each batch:

- summarize the answers in 3 to 6 bullet points
- state the current working understanding
- identify any remaining blocker
- only then continue to the next stage

Use [ref/interactive-intake.md](ref/interactive-intake.md) when building questions.

## Required Inputs

For paper-writing tasks, ask for or infer the following when missing:

- research topic
- target field or venue direction
- output language
  - Chinese
  - English
- expected length
- paper type
  - degree thesis
  - course paper
  - technical document or technical report
  - journal paper
  - conference paper
  - survey or review
  - research proposal
  - early draft of a full paper
- deadline or urgency
- whether local tools such as Chrome, Word, or Zotero should be used

If the user gives only a rough topic, start with a scoping brief before drafting.

Do not ask every field if it is not necessary. Infer low-risk defaults and only ask about details that affect literature search, structure, or argument.

For CV/resume tasks, ask for or infer the following when missing:

- target use
  - academic CV
  - research internship resume
  - industry resume
  - scholarship or lab application
  - general personal profile
- output language
  - Chinese
  - English
  - bilingual
- target field, role, school, lab, company, or program
- expected length
  - one page
  - two pages
  - complete academic CV
- template style
  - classic
  - compact
  - modern
  - academic
  - let the agent choose
- whether the CV should include a personal headshot/photo
- whether ATS friendliness matters
- whether the user already has source material, old resume, publications, projects, or links
- whether a local TeX engine or Overleaf should be used

If the user gives only "help me make a CV", first ask for target use, language, page length, template preference, optional headshot/photo, and available source material.

## Output Policy

Working files default to Markdown. Final delivery should include a `.docx` manuscript when the paper reaches deliverable quality.

The output language must be fixed early. Default only if safe:

- if the user explicitly requests Chinese, use Chinese
- if the user explicitly requests English, use English
- if the surrounding conversation clearly implies one language, follow it
- otherwise ask directly rather than guessing

For each new topic, create one project folder under `papers/` with this minimum set:

- `intake.md`
- `brief.md`
- `outline.md`
- `draft.md`
- `final-manuscript.docx`
- `references.md`
- `notes.md`

Optional files may be added inside that project folder only when the task needs them.

For each new CV/resume target, create one project folder under `cvs/` with this minimum set:

- `intake.md`
- `brief.md`
- `cv-data.md`
- `cv.md`
- `cv.tex`
- `notes.md`
- `final-cv.pdf` when LaTeX compilation is available

Optional files may include:

- `cover-letter.tex`
- `publications.bib`
- `resume-ats.tex`
- `profile-photo.jpg` or `profile-photo.png`

For Chinese or bilingual CVs, default to XeLaTeX and CJK-capable fonts. For English-only industry resumes, prefer simple one-page layouts and avoid icons or complex two-column designs when ATS friendliness matters.

## Evidence Policy

Prefer sources in this order:

1. peer-reviewed papers and major venue publications
2. preprints from credible authors or labs
3. official documentation, standards, and lab pages
4. strong technical blogs or institutional notes
5. news or marketing pages only as weak background

Never present unsupported claims as established fact.

Never fabricate citations, DOIs, page numbers, experimental results, or venue rankings.

If evidence is incomplete, mark it explicitly as:

- tentative inference
- open question
- hypothesis

## Main Workflow

Use the paper workflow below for paper-writing tasks. Use the CV workflow below for CV/resume tasks.

## CV/Resume Workflow

### 1. Initialize the CV project

- Create a project folder in `cvs/`
- Record the request in `log/task-history.md`
- Write the user interview record to `intake.md`
- Write the working target to `brief.md`
- Use `script/init_cv_project.py` when it saves time; `script/init_cv_project.ps1` is a PowerShell wrapper for the same initializer

### 2. Run a short CV intake

Ask in a small first batch:

1. What is the target use: academic CV, research internship, industry job, scholarship/lab application, or general profile?
2. Should the output be Chinese, English, or bilingual?
3. Should it be one page, two pages, or a complete academic CV?
4. Which template style should be used: classic, compact, modern, academic, or should the agent choose?
5. Should it include a personal headshot? If yes, ask for the local image path when needed.
6. Does the user already have source material, projects, publications, awards, links, or an old resume?

After the answer, ask only target-specific blockers:

- academic CV: research direction, publications, advisor, teaching, grants, service
- research internship: target lab/topic, methods, projects, publications/preprints, technical skills
- industry resume: target role, job description, ATS friendliness, measurable project outcomes
- scholarship/application: selection criteria, required sections, deadline

### 3. Choose a LaTeX style

Use [ref/cv-latex-guide.md](ref/cv-latex-guide.md).

Default choices:

- academic CV: clean multi-section layout, complete chronology, publications visible
- industry resume: compact one-page layout, bullets optimized for screening
- hybrid research resume: one to two pages, projects and research output first

Built-in LaTeX template choices:

- `classic`: conservative and portable
- `compact`: one-page ATS-friendly industry resume
- `modern`: more polished visual style with color accents
- `academic`: publication/research-oriented CV

Do not copy Overleaf template text verbatim. If adapting a named template, check license and preserve attribution where required.

### 4. Convert raw material into CV content

- Do not invent dates, awards, metrics, papers, affiliations, tools, rankings, or roles
- Mark unknown facts as `TODO`
- Produce `cv.md` first as the readable content draft, then convert it into `cv.tex`
- Rewrite bullets around evidence:
  - action
  - method or tool
  - technical object
  - measurable or concrete result
- Remove empty self-evaluation language unless supported by evidence

### 5. Write or edit LaTeX

- Keep `cv.tex` readable and dependency-light
- Use XeLaTeX for Chinese or bilingual CVs
- Use simple macros for sections and entries
- If the user provides a headshot, copy it into the CV project as `profile-photo.*` and reference it from `cv.tex`
- Avoid photos, icons, sidebars, and text boxes unless the user requests them
- If ATS friendliness matters, avoid multi-column layouts and decorative elements

### 6. Compile and check

- Compile with `script/compile_latex_cv.ps1` if a local TeX engine is available
- If local TeX is unavailable, tell the user to compile `cv.tex` on Overleaf with XeLaTeX
- Check that names, dates, links, page breaks, section order, and TODO markers are correct
- Append a short revision log entry

### 1. Initialize the project

- Create a project folder in `papers/`
- Record the request in `log/task-history.md`
- Write the user interview record to `intake.md`
- Write the task brief to `brief.md`

### 2. Run the guided intake

- if the user has only a topic, start from topic clarification
- if the paper type is unknown, ask for it before building the writing plan
- if the output language is unknown, ask for Chinese or English early in the intake
- if the user already has a sharp idea, skip directly to constraint confirmation
- distinguish hard constraints from soft preferences
- capture mandatory points, forbidden points, and unknown points separately

Use a topic-sensitive and type-sensitive question strategy:

- first identify the document type
- then ask only the details that matter for that type
- stop asking once the next action is unblocked

Recommended execution pattern:

1. ask the first short batch
2. wait for user response
3. summarize the current understanding
4. ask the next short batch only if needed
5. once enough information is collected, convert it into `brief.md`

Before moving on, write a concise working brief and ask for confirmation if the direction is still ambiguous.

### 3. Build the search plan

- derive keywords, synonyms, and exclusions
- separate foundational queries from frontier queries
- if the topic is broad, split into 3 to 5 subproblems

Use [ref/source-priority.md](ref/source-priority.md) and [ref/quality-checklist.md](ref/quality-checklist.md) when planning.

Before searching, ensure the following are clear enough:

- scope boundary
- key terms
- intended paper type
- output language
- expected evidence standard

### 4. Collect material

Prefer local tools or scripts when they exist.

- For search query generation, use scripts under `script/`
- If the user allows local tool usage, Chrome may be opened for Scholar, arXiv, DOI, publisher, conference, and lab-page searches
- If Zotero is available, use it as the primary literature hub

Record useful raw findings in `notes.md`, not directly in `draft.md`.

### 5. Build the argument

Before drafting prose, produce:

- the problem statement
- the paper contribution angle
- the section-level logic
- the evidence mapped to each section

Do not start with full prose if the outline is weak.

If the angle is still underdetermined, return to the user with 2 or 3 concrete framing options.

### 6. Draft the paper

Use [ref/paper-template.md](ref/paper-template.md) as the default structure.

Writing rules:

- synthesize across sources rather than paraphrasing one source at a time
- prefer precise and restrained claims
- vary sentence shape and paragraph openings
- explain mechanisms, assumptions, and tradeoffs
- keep terminology stable across the draft

### 7. Reduce repetition and AIGC-like phrasing

Apply these strategies during revision:

- replace generic transition-heavy prose with content-bearing sentences
- merge or split paragraphs based on argument flow rather than fixed rhythm
- restate ideas from first principles instead of surface paraphrase
- remove empty adjectives and ceremonial academic filler
- avoid repeated sentence templates such as "it is worth noting that" or "in conclusion"
- rewrite high-risk passages by changing structure, evidence order, and abstraction level

Lower AIGC-like phrasing does not mean making the text casual. It means making the writing specific, evidence-driven, and structurally varied.

### 8. Final checks

Before considering a draft usable:

- run the checklist in [ref/quality-checklist.md](ref/quality-checklist.md)
- make sure every major section has supporting references
- ensure unresolved gaps are called out
- update `references.md`
- generate or refresh `final-manuscript.docx`
- append a short revision log entry

## Stage Gates

Do not silently jump across these gates:

1. after intake
   - provide a short understanding summary
   - if the topic is still fuzzy, ask for confirmation
2. after literature triage
   - provide the intended paper angle or outline direction
3. before full drafting
   - confirm that the outline matches the user's expectation when reasonable

For short student papers or urgent drafts, these gates can be compressed, but they should not disappear entirely.

## Local Tool Policy

The agent may use local scripts and installed software to shorten the path, but should be explicit about the tool being invoked.

Typical tool choices:

- Chrome: literature search and source triage
- Word: optional final formatting refinement for `.docx`
- Zotero: reference management and paper retrieval
- `export_final_docx.py`: baseline `.docx` generation from the current manuscript

If a tool call affects the local machine state in a meaningful way, state what will be called before invoking it.

## File Conventions

### `brief.md`

Contains:

- distilled conclusion from `intake.md`
- user goal
- output language
- scope
- assumptions
- exclusions
- output requirements

### `intake.md`

Contains:

- original user topic
- paper type selected or inferred
- output language selected or inferred
- question-and-answer record
- hard constraints
- soft preferences
- must-include points
- must-avoid points
- open questions
- current agreed writing direction

### `outline.md`

Contains:

- title candidates
- section structure
- argument notes per section

### `draft.md`

Contains the current main manuscript.

The main manuscript language should match the selected output language.

### `final-manuscript.docx`

Contains the current deliverable manuscript for the user.

Default generation path:

1. write and revise in `draft.md`
2. export to `final-manuscript.docx`
3. if needed, refine final formatting with Word automation

The final `.docx` should use the same language as `draft.md`.

### `references.md`

Contains:

- selected references
- citation-ready metadata when available
- notes on source relevance

### `notes.md`

Contains raw literature notes, open questions, and evidence fragments.

### CV project files

`cv-data.md` contains structured source material and unresolved TODOs.

`cv.md` contains the readable resume/CV draft and should be easy for the user to review before LaTeX formatting.

`cv.tex` contains the editable LaTeX CV source.

`final-cv.pdf` contains the compiled CV deliverable when compilation succeeds.

## References

Read these files as needed:

- [ref/interactive-intake.md](ref/interactive-intake.md)
- [ref/paper-template.md](ref/paper-template.md)
- [ref/citation-style.md](ref/citation-style.md)
- [ref/source-priority.md](ref/source-priority.md)
- [ref/quality-checklist.md](ref/quality-checklist.md)
- [ref/cv-latex-guide.md](ref/cv-latex-guide.md)

Use scripts under `script/` when they reduce repeated manual work.
