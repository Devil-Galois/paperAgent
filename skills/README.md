# Paper Agent - Codex Skill

## Installation

To install this skill in Codex, copy the `paper-agent.codex.json` file to your Codex skills directory:

```bash
# For local Codex installation
cp paper-agent.codex.json ~/.codex/skills/

# Or use the Codex CLI if available
codex skills install ./paper-agent.codex.json
```

## Overview

This skill provides an interactive assistant for:
- **Academic Paper Writing**: From topic clarification through literature collection, outlining, drafting, revision, and DOCX export
- **CV/Resume Generation**: Creating tailored LaTeX CVs and resumes for academic, research internship, or industry applications

## Features

### Triggers
The skill activates on keywords like:
- Paper-related: "write a paper", "research paper", "thesis", "conference paper", etc.
- CV-related: "create CV", "resume", "academic CV", "LaTeX CV", etc.

### Tools
- `init_paper_project`: Initialize paper project folder structure
- `init_cv_project`: Initialize CV project folder structure
- `build_search_queries`: Generate literature search queries
- `export_final_docx`: Export manuscript to DOCX format
- `compile_latex_cv`: Compile LaTeX CV to PDF
- `open_chrome_search`: Open browser for literature search

### Workflows
1. **Paper Writing Workflow** (8 stages):
   - Initialize → Guided Intake → Search Planning → Literature Collection → Argument Building → Drafting → Revision → Finalization

2. **CV Generation Workflow** (6 stages):
   - Initialize → CV Intake → Style Selection → Content Conversion → LaTeX Writing → Compilation

### Key Policies
- **Evidence Priority**: Peer-reviewed papers > Preprints > Official docs > Technical blogs
- **Prohibited**: Never fabricate citations, DOIs, results, or user background
- **Interactive Style**: Ask 2-4 high-value questions per batch, not long questionnaires

## File Structure

After running this skill, projects are created in:
- `papers/{topic_slug}/` - Paper projects with intake.md, brief.md, outline.md, draft.md, final-manuscript.docx, etc.
- `cvs/{person_target_slug}/` - CV projects with cv.md, cv.tex, final-cv.pdf, etc.

## References

This skill references supporting documents in `/ref/`:
- `interactive-intake.md` - Interview guidelines
- `paper-template.md` - Default paper structure
- `citation-style.md` - Citation formatting
- `source-priority.md` - Source evaluation criteria
- `quality-checklist.md` - Quality assurance checklist
- `cv-latex-guide.md` - LaTeX CV styling guide

## License

MIT
