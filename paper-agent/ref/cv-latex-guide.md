# CV and Resume LaTeX Guide

Use this reference when a user asks for a CV, resume, academic CV, researcher profile, internship resume, job resume, or LaTeX/Overleaf resume editing task.

## Template Families

Use Overleaf templates as design references, not as text to copy wholesale.

- Academic CV templates: best for students, researchers, PhD applications, postdoc applications, faculty applications, and publication-heavy profiles. Common structure: contact, research interests, education, research experience, publications, teaching, awards, service, skills.
- Clean academic CV with modular sections and BibLaTeX: best when publications are numerous and should be maintained separately.
- Jake's Resume style: best for industry, internship, software/hardware engineering, and one-page recruiting use. Common structure: education, experience, projects, skills, honors.
- Awesome CV / highly designed templates: visually polished but often depend on custom classes, icons, and fonts. Use only when presentation is more important than portability.

Prefer an original, dependency-light template unless the user explicitly asks to adapt a named template and its license allows it.

## Built-In Template Choices

`init_cv_project.py` supports these original, dependency-light template styles:

- `classic`: conservative academic/general CV; good default when the user does not care about visual styling.
- `compact`: ATS-friendly one-page industry resume; inspired by Jake's Resume / sb2nov-style density, but implemented from scratch.
- `modern`: color-accented polished resume; inspired by ModernCV/AltaCV/Awesome CV visual language, but avoids custom classes and icon dependencies.
- `academic`: research CV layout for publications, teaching, service, and research projects.

Selection rule:

- industry job or ATS concern: use `compact`
- academic CV or publication-heavy profile: use `academic`
- Chinese campus recruitment or user asks for a nicer visual style: use `modern`
- unclear target or maximum portability: use `classic`

## Template Selection

Choose the layout based on purpose:

- Academic CV: allow 2+ pages, chronological completeness, publications and research outputs have high priority.
- Research internship or PhD application resume: 1 to 2 pages, highlight research projects, methods, publications/preprints, skills, and recommendation-relevant achievements.
- Industry resume: usually 1 page, project/experience bullets must show action, method, result, and measurable impact where available.
- Chinese resume: use XeLaTeX with CJK fonts, avoid decorative icons unless requested, keep section names direct.
- English resume: concise bullets, no long self-evaluation paragraph, avoid inflated adjectives.
- Bilingual CV: avoid duplicating every bullet in two languages unless required; prefer bilingual section headings or a separate English version.

## Intake Questions

Ask only the questions that change the CV:

1. target use: academic application, industry job, internship, scholarship, funding, lab application, or general profile
2. language: Chinese, English, or bilingual
3. length: one page, two pages, or complete academic CV
4. template preference: classic, compact, modern, academic, or let the agent choose
5. target field or role
6. available raw material: existing resume, education, projects, publications, awards, skills, links
7. constraints: photo, GPA, ranking, publication format, target country, ATS friendliness, deadline
8. optional headshot: whether the user wants to include a personal photo and whether they can provide a local image path

If the user is unsure, offer:

- academic CV: comprehensive, stronger for research applications
- industry resume: compact, stronger for recruiter screening
- hybrid research resume: one to two pages, useful for research internships and graduate applications

## Content Rules

- Do not invent degrees, awards, publications, roles, dates, metrics, rankings, or affiliations.
- Mark uncertain content as TODO or ask the user to confirm.
- Convert weak descriptions into evidence-bearing bullets.
- Prefer `Action + technical method + object + result` for experience bullets.
- For research bullets, include problem, method, experiment/artifact, and contribution.
- For hardware/architecture/ML/CAD work, make tools, benchmarks, datasets, PDKs, simulators, and metrics explicit when known.
- Remove empty claims such as "hard-working", "strong learning ability", and "responsible" unless backed by evidence.
- Include a headshot only if the target context expects or permits it. For ATS-oriented or US/UK industry resumes, usually avoid photos. For Chinese campus recruitment, scholarships, or institution-specific forms, a clean ID-style photo can be acceptable when the user requests it.

## LaTeX Rules

- Default to `cv.tex` compiled with XeLaTeX.
- Use a dependency-light article template, `geometry`, `enumitem`, `hyperref`, `xcolor`, `tabularx`, `fontspec`, `xeCJK`, and `graphicx` when a photo is used.
- For Chinese or bilingual output, require XeLaTeX and use CJK fonts with fallbacks.
- Keep source editable: define simple macros for sections and entries, but avoid deeply nested custom commands.
- Avoid photos, icons, colored sidebars, and dense two-column layouts unless the user asks for them.
- If the target is ATS screening, avoid icons, text boxes, images, and multi-column content.

## File Conventions

Each CV project should live under `paperAgent/cvs/YYYYMMDD-HHMMSS-slug/` and contain:

- `intake.md`: user goals, target use, constraints, missing fields
- `brief.md`: final working direction
- `cv-data.md`: structured source material and TODOs
- `cv.md`: human-readable CV/resume content draft
- `cv.tex`: LaTeX source
- `final-cv.pdf`: compiled deliverable when a TeX engine is available
- `notes.md`: revision notes and fit-to-role strategy

Optional files:

- `cover-letter.tex` if the user requests a cover letter
- `publications.bib` for publication-heavy academic CVs
- `resume-ats.tex` for a one-page ATS-friendly variant
- `profile-photo.jpg` or `profile-photo.png` when the user provides a headshot

## Overleaf References

- Overleaf CV and resumes category: https://www.overleaf.com/latex/templates?q=cv
- Academic CV Template by Sara Venkatraman: https://www.overleaf.com/latex/templates/academic-cv-template/vqghvksnqdhv
- Academic CV Template by Dubasi Pavan Kumar: https://www.overleaf.com/latex/templates/academic-cv-template/gmyytjmdbvdm
- Clean Academic CV Template by Matthew R. DeVerna: https://www.overleaf.com/latex/templates/clean-academic-cv-template/tjpjkzmvztwn
- Jake's Resume: https://www.overleaf.com/latex/templates/jakes-resume/syzfjbzwjncs
- Software Engineer Resume by sb2nov: https://www.overleaf.com/latex/templates/software-engineer-resume/gqxmqsvsbdjf
- ModernCV and Cover Letter: https://www.overleaf.com/latex/templates/moderncv-and-cover-letter-template/sttkgjcysttn
- AltaCV: https://github.com/liantze/AltaCV
- Awesome CV: https://github.com/posquit0/Awesome-CV
- moderncv: https://github.com/moderncv/moderncv
- sb2nov resume: https://github.com/sb2nov/resume

When a GitHub template is used directly rather than as inspiration, check its current license, keep required attribution, and copy only what the license permits.
