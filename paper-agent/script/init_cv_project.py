import argparse
import shutil
from datetime import datetime
from pathlib import Path


TEMPLATES = {
    "classic": {
        "label": "classic",
        "description": "clean academic/general CV, portable and conservative",
        "accent": "1F4E79",
        "margin": "1.35cm",
        "section_size": "large",
        "itemsep": "2pt",
        "topsep": "2pt",
        "header": "classic",
    },
    "compact": {
        "label": "compact",
        "description": "ATS-friendly one-page industry resume inspired by Jake/sb2nov style",
        "accent": "222222",
        "margin": "1.08cm",
        "section_size": "normalsize",
        "itemsep": "1pt",
        "topsep": "1pt",
        "header": "compact",
    },
    "modern": {
        "label": "modern",
        "description": "polished color-accent resume inspired by ModernCV/AltaCV visual language",
        "accent": "0E5484",
        "margin": "1.25cm",
        "section_size": "large",
        "itemsep": "1.8pt",
        "topsep": "2pt",
        "header": "modern",
    },
    "academic": {
        "label": "academic",
        "description": "research CV layout for publications, projects, teaching, and service",
        "accent": "4B2E83",
        "margin": "1.45cm",
        "section_size": "large",
        "itemsep": "2pt",
        "topsep": "2pt",
        "header": "classic",
    },
}


def safe_slug(raw: str) -> str:
    out = []
    last_dash = False
    for ch in raw.lower():
        if ch.isascii() and ch.isalnum():
            out.append(ch)
            last_dash = False
        elif not last_dash:
            out.append("-")
            last_dash = True
    return "".join(out).strip("-") or "cv-project"


def latex_escape(text: str) -> str:
    replacements = {
        "\\": r"\textbackslash{}",
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "_": r"\_",
        "{": r"\{",
        "}": r"\}",
        "~": r"\textasciitilde{}",
        "^": r"\textasciicircum{}",
    }
    return "".join(replacements.get(ch, ch) for ch in text)


def write(path: Path, content: str) -> None:
    path.write_text(content.strip() + "\n", encoding="utf-8")


def render_header(style: str, name: str, today: str, photo_file: str) -> str:
    escaped_name = latex_escape(name)
    if style == "compact":
        return rf"""
\newcommand{{\profilephoto}}{{{photo_file}}}
\newcommand{{\cvheader}}[5]{{
  \begin{{center}}
    {{\LARGE\sffamily\bfseries #1}}\\[-1pt]
    \small #2 \quad | \quad #3 \quad | \quad #4 \quad | \quad Updated: #5
  \end{{center}}
  \vspace{{-2pt}}
}}
"""
    if style == "modern":
        return rf"""
\newcommand{{\profilephoto}}{{{photo_file}}}
\newcommand{{\cvheader}}[5]{{
  \noindent\colorbox{{accent}}{{%
    \begin{{minipage}}{{0.98\textwidth}}
      \vspace{{5pt}}
      \color{{white}}
      {{\LARGE\sffamily\bfseries #1}}\hfill{{\small Updated: #5}}\\[2pt]
      \small #2 \quad | \quad #3 \quad | \quad #4
      \vspace{{5pt}}
    \end{{minipage}}%
  }}
  \hfill
  \ifthenelse{{\equal{{\profilephoto}}{{}}}}{{}}{{
    \begin{{minipage}}[t]{{0.18\textwidth}}
      \vspace{{-48pt}}\raggedleft\includegraphics[width=2.25cm,height=2.85cm,keepaspectratio]{{\profilephoto}}
    \end{{minipage}}
  }}
  \vspace{{7pt}}
}}
"""
    return rf"""
\newcommand{{\profilephoto}}{{{photo_file}}}
\newcommand{{\cvheader}}[5]{{
  \begin{{minipage}}[t]{{0.76\textwidth}}
  {{\LARGE\sffamily\bfseries #1}}\hfill{{\small Updated: #5}}\\[-1pt]
  \small #2 \quad | \quad #3 \quad | \quad #4
  \end{{minipage}}
  \hfill
  \ifthenelse{{\equal{{\profilephoto}}{{}}}}{{}}{{
    \begin{{minipage}}[t]{{0.18\textwidth}}
      \vspace{{-8pt}}\raggedleft\includegraphics[width=2.35cm,height=3.05cm,keepaspectratio]{{\profilephoto}}
    \end{{minipage}}
  }}
  \vspace{{6pt}}
}}
"""


def render_cv_tex(name: str, today: str, photo_file: str, template: str) -> str:
    cfg = TEMPLATES[template]
    section_size = cfg["section_size"]
    section_rule = r"[\titlerule]" if template != "modern" else r""
    section_color = "accent" if template != "compact" else "black"
    header = render_header(cfg["header"], name, today, photo_file)
    escaped_name = latex_escape(name)

    return rf"""
\documentclass[10pt,a4paper]{{article}}

\usepackage[margin={cfg["margin"]}]{{geometry}}
\usepackage{{iftex}}
\usepackage{{xcolor}}
\usepackage{{enumitem}}
\usepackage{{tabularx}}
\usepackage{{graphicx}}
\usepackage[hidelinks]{{hyperref}}
\usepackage{{titlesec}}
\usepackage{{array}}
\usepackage{{ifthen}}

\ifXeTeX
  \usepackage{{fontspec}}
  \usepackage{{xeCJK}}
  \IfFontExistsTF{{Times New Roman}}{{\setmainfont{{Times New Roman}}}}{{\setmainfont{{TeX Gyre Termes}}}}
  \IfFontExistsTF{{Arial}}{{\setsansfont{{Arial}}}}{{\setsansfont{{TeX Gyre Heros}}}}
  \IfFontExistsTF{{Noto Serif CJK SC}}{{\setCJKmainfont{{Noto Serif CJK SC}}}}{{\setCJKmainfont{{SimSun}}}}
  \IfFontExistsTF{{Noto Sans CJK SC}}{{\setCJKsansfont{{Noto Sans CJK SC}}}}{{\setCJKsansfont{{SimHei}}}}
\else
  \errmessage{{This CV template requires XeLaTeX. Compile with xelatex.}}
\fi

\definecolor{{accent}}{{HTML}}{{{cfg["accent"]}}}
\pagestyle{{empty}}
\setlength{{\parindent}}{{0pt}}
\setlength{{\parskip}}{{0pt}}
\setlist[itemize]{{leftmargin=1.15em, itemsep={cfg["itemsep"]}, topsep={cfg["topsep"]}}}

\titleformat{{\section}}
  {{\{section_size}\sffamily\bfseries\color{{{section_color}}}}}
  {{}}{{0pt}}{{}}{section_rule}
\titlespacing*{{\section}}{{0pt}}{{7pt}}{{4pt}}

{header}
\newcommand{{\entry}}[4]{{
  \textbf{{#1}}\hfill #2\\
  \textit{{#3}}\hfill \textit{{#4}}\\[-2pt]
}}

\newcommand{{\projectentry}}[3]{{
  \textbf{{#1}}\hfill #2\\[-2pt]
  #3
}}

\begin{{document}}

\cvheader{{{escaped_name}}}{{email@example.com}}{{+86-000-0000-0000}}{{GitHub / Website / LinkedIn}}{{{today}}}

\section*{{研究方向 / Profile}}
面向目标岗位或申请方向，写 1--2 句高度具体的定位。避免空泛自我评价；说明研究领域、核心技能和可验证成果。

\section*{{教育经历 / Education}}
\entry{{学校名称}}{{城市，国家}}{{学位，专业}}{{起止年月}}
\begin{{itemize}}
  \item 导师 / GPA / 排名 / 相关课程：TODO
  \item 与目标方向相关的训练：TODO
\end{{itemize}}

\section*{{研究经历 / Research Experience}}
\entry{{课题组或机构}}{{城市，国家}}{{研究助理 / 学生研究者}}{{起止年月}}
\begin{{itemize}}
  \item 围绕 TODO 问题，使用 TODO 方法，完成 TODO 实验或系统，实现 TODO 结果。
  \item 将工具、数据集、仿真平台、芯片工艺、模型或指标写清楚；不要写未验证的夸张结论。
\end{{itemize}}

\section*{{项目经历 / Projects}}
\projectentry{{项目名称}}{{起止年月}}{{技术栈 / 方法：TODO}}
\begin{{itemize}}
  \item 动作 + 方法 + 对象 + 结果。例如：构建 TODO，用 TODO 指标评估，在 TODO 场景下改善 TODO。
  \item 如果没有量化结果，写清楚可交付物：代码、报告、实验平台、论文、海报、开源仓库。
\end{{itemize}}

\section*{{论文与成果 / Publications}}
\begin{{itemize}}
  \item 作者. 题名. 会议/期刊/预印本, 年份. DOI/URL.（没有正式发表则标注 manuscript / preprint / under review）
\end{{itemize}}

\section*{{技能 / Skills}}
\begin{{tabularx}}{{\textwidth}}{{>{{\bfseries}}p{{2.6cm}}X}}
编程 & Python, C/C++, MATLAB, TODO \\
工具 & Git, Linux, LaTeX, TODO \\
专业 & 计算机体系结构, AI/ML, 模拟集成电路, TODO \\
语言 & 中文, 英文, TODO \\
\end{{tabularx}}

\section*{{荣誉与服务 / Honors and Service}}
\begin{{itemize}}
  \item 奖项或服务经历，年份。只写可验证事实。
\end{{itemize}}

\end{{document}}
"""


def build_project(
    name: str,
    target: str,
    language: str,
    photo_path: str,
    slug: str,
    base_dir: str,
    template: str,
) -> Path:
    script_dir = Path(__file__).resolve().parent
    root = Path(base_dir)
    if not root.is_absolute():
        root = (script_dir / root).resolve()

    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    project_slug = slug or safe_slug(name)
    target_dir = root / f"{timestamp}-{project_slug}"
    target_dir.mkdir(parents=True, exist_ok=True)

    today = datetime.now().strftime("%Y-%m-%d")
    photo_file = ""
    if photo_path:
        src = Path(photo_path).expanduser().resolve()
        ext = src.suffix or ".jpg"
        photo_file = f"profile-photo{ext}"
        shutil.copy2(src, target_dir / photo_file)

    template_info = TEMPLATES[template]

    intake = f"""
# CV Intake

- Name: {name}
- Target: {target}
- Language: {language}
- Template: {template}
- Photo: {photo_file}
- Created: {today}

## Goal

## Target Role or Application

## Hard Constraints

## Soft Preferences

## Missing Information

## User Source Material
"""

    brief = f"""
# CV Brief

- Name: {name}
- Target: {target}
- Language: {language}
- Template: {template} ({template_info["description"]})
- Markdown: cv.md
- LaTeX: cv.tex
- PDF: final-cv.pdf when XeLaTeX is available
- Photo: {photo_file}

## Working Direction

Use a clean, dependency-light LaTeX CV. Keep claims evidence-based and leave TODO markers for missing facts.
"""

    cv_data = """
# CV Data

## Contact

- Email:
- Phone:
- Location:
- Website:
- GitHub:
- LinkedIn:

## Education

- Institution:
  - Degree:
  - Major:
  - Dates:
  - GPA/Rank:
  - Advisor:

## Research or Work Experience

- Organization:
  - Role:
  - Dates:
  - Bullets:

## Projects

- Project:
  - Context:
  - Methods/Tools:
  - Results:

## Publications

- TODO

## Awards

- TODO

## Skills

- Programming:
- Tools:
- Research:
- Languages:
"""

    cv_md = f"""
# {name}

- Email: email@example.com
- Phone: +86-000-0000-0000
- Location: TODO
- Links: GitHub / Website / LinkedIn
- Template: {template}
- Photo: {photo_file}

## 研究方向 / Profile

面向目标岗位或申请方向，写 1--2 句高度具体的定位。避免空泛自我评价；说明研究领域、核心技能和可验证成果。

## 教育经历 / Education

**学校名称**，学位，专业，起止年月

- 导师 / GPA / 排名 / 相关课程：TODO
- 与目标方向相关的训练：TODO

## 研究经历 / Research Experience

**课题组或机构**，研究助理 / 学生研究者，起止年月

- 围绕 TODO 问题，使用 TODO 方法，完成 TODO 实验或系统，实现 TODO 结果。
- 将工具、数据集、仿真平台、芯片工艺、模型或指标写清楚；不要写未验证的夸张结论。

## 项目经历 / Projects

**项目名称**，起止年月

- 技术栈 / 方法：TODO
- 动作 + 方法 + 对象 + 结果。例如：构建 TODO，用 TODO 指标评估，在 TODO 场景下改善 TODO。

## 论文与成果 / Publications

- 作者. 题名. 会议/期刊/预印本, 年份. DOI/URL.

## 技能 / Skills

- 编程：Python, C/C++, MATLAB, TODO
- 工具：Git, Linux, LaTeX, TODO
- 专业：计算机体系结构, AI/ML, 模拟集成电路, TODO
- 语言：中文, 英文, TODO

## 荣誉与服务 / Honors and Service

- 奖项或服务经历，年份。只写可验证事实。
"""

    notes = f"""
# CV Notes

## Fit Strategy

## Template

- Selected template: {template}
- Template intent: {template_info["description"]}
- External inspirations are recorded in `ref/cv-latex-guide.md`; generated source is original and dependency-light.

## Revision Notes

## TODO

- Replace placeholders in cv.md and cv.tex with verified facts.
- Confirm target use, page length, template style, headshot policy, and whether ATS friendliness matters.
"""

    cv_tex = render_cv_tex(name=name, today=today, photo_file=photo_file, template=template)

    files = {
        "intake.md": intake,
        "brief.md": brief,
        "cv-data.md": cv_data,
        "cv.md": cv_md,
        "notes.md": notes,
        "cv.tex": cv_tex,
    }
    for name_, content in files.items():
        write(target_dir / name_, content)

    return target_dir


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", default="Your Name")
    parser.add_argument("--target", default="academic")
    parser.add_argument("--language", choices=["zh", "en", "bilingual"], default="zh")
    parser.add_argument("--template", choices=sorted(TEMPLATES), default="classic")
    parser.add_argument("--photo-path", default="")
    parser.add_argument("--slug", default="")
    parser.add_argument("--base-dir", default="../cvs")
    args = parser.parse_args()
    path = build_project(
        name=args.name,
        target=args.target,
        language=args.language,
        photo_path=args.photo_path,
        slug=args.slug,
        base_dir=args.base_dir,
        template=args.template,
    )
    print(path)


if __name__ == "__main__":
    main()
