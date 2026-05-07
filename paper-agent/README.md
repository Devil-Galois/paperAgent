# paperAgent Skill Package

A self-contained Codex skill for academic paper writing and LaTeX CV/resume generation.

## Package Structure

```
paper-agent/
├── SKILL.md              # Main skill definition (Codex entry point)
├── ref/                  # Reference documents
│   ├── citation-style.md
│   ├── cv-latex-guide.md
│   ├── interactive-intake.md
│   ├── paper-template.md
│   ├── quality-checklist.md
│   └── source-priority.md
└── script/               # Helper scripts
    ├── build_search_queries.py
    ├── compile_latex_cv.ps1
    ├── export_final_docx.py
    ├── init_cv_project.ps1
    ├── init_cv_project.py
    ├── init_paper_project.ps1
    └── open_chrome_search.ps1
```

## Installation

### Windows

Copy the `paper-agent` folder to:
```
C:\Users\<USER>\.codex\skills\paper-agent\
```

Final layout should be:
```
C:\Users\<USER>\.codex\skills\paper-agent\SKILL.md
C:\Users\<USER>\.codex\skills\paper-agent\ref\
C:\Users\<USER>\.codex\skills\paper-agent\script\
```

### macOS / Linux

Copy the `paper-agent` folder to:
```
~/.codex/skills/paper-agent/
```

Final layout should be:
```
~/.codex/skills/paper-agent/SKILL.md
~/.codex/skills/paper-agent/ref/
~/.codex/skills/paper-agent/script/
```

Or use Codex CLI if available:
```bash
codex skills install ./paper-agent
```

## Health Check

Before using the skill, verify the installation:

1. **SKILL.md exists at root**: The skill definition file must be at `paper-agent/SKILL.md`
2. **All ref files exist**:
   - `ref/citation-style.md`
   - `ref/cv-latex-guide.md`
   - `ref/interactive-intake.md`
   - `ref/paper-template.md`
   - `ref/quality-checklist.md`
   - `ref/source-priority.md`
3. **Core scripts exist**:
   - `script/export_final_docx.py`
   - `script/init_cv_project.py`
   - `script/compile_latex_cv.ps1`
4. **No broken relative paths**: SKILL.md should reference `ref/xxx` and `script/xxx` (not `../ref/` or `../script/`)

Run this quick check (PowerShell):
```powershell
$skillPath = "$env:USERPROFILE\.codex\skills\paper-agent"
Test-Path "$skillPath\SKILL.md" -and `
Test-Path "$skillPath\ref\interactive-intake.md" -and `
Test-Path "$skillPath\script\export_final_docx.py"
```

Run this quick check (bash):
```bash
skill_path="$HOME/.codex/skills/paper-agent"
[ -f "$skill_path/SKILL.md" ] && \
[ -f "$skill_path/ref/interactive-intake.md" ] && \
[ -f "$skill_path/script/export_final_docx.py" ] && \
echo "OK" || echo "FAIL"
```

## Features

### Paper Writing
- Interactive topic clarification
- Literature search and collection
- Outline building
- Drafting with original language
- Revision for lower repetition and AIGC-like phrasing
- DOCX export

### CV/Resume Generation
- Academic CV, research internship resume, industry resume
- LaTeX template selection (classic, compact, modern, academic)
- XeLaTeX support for Chinese/bilingual CVs
- ATS-friendly layouts
- PDF compilation (local or Overleaf)

## Usage

Once installed, activate the skill in Codex by mentioning:
- "paper agent"
- "write a paper"
- "create a CV"
- "LaTeX resume"
- "academic paper"
- "literature review"

Or use any of the 28+ trigger keywords defined in SKILL.md.

## Work Directory

The skill creates working directories in your project:
- `papers/` - Per-topic paper projects
- `cvs/` - Per-person or per-target CV projects
- `log/` - Task and revision logs

These are created automatically on first use.

## Requirements

### For Paper Writing
- Optional: Chrome browser for literature search
- Optional: Zotero for reference management
- Optional: Microsoft Word for final `.docx` refinement

### For CV Compilation
- Local TeX engine (TeX Live, MiKTeX, MacTeX) with XeLaTeX support, OR
- Overleaf account for online compilation

## Encoding

All files are UTF-8 encoded. If you see garbled Chinese text, ensure your editor uses UTF-8 encoding.

## License

Same as the parent paperAgent project.

## Support

For issues or questions, refer to the main paperAgent repository documentation.
