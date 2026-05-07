# paperAgent

版本：v0.4.0
状态：可用于“论文写作项目”和“LaTeX 简历/CV 项目”的版本。论文任务支持交互澄清、搜集资料、起草论文并导出 `docx`；简历任务支持生成 `cv.md`、`cv.tex`，并在本地 TeX 可用时导出 `final-cv.pdf`。
最后更新：2026-04-26

## 目标

`paperAgent` 面向科研论文写作，不应表现为一次性生成器，而应表现为可交互的研究写作助手。它的核心职责是：

- 根据用户主题先做必要的访谈式澄清
- 帮用户把模糊想法收敛成可执行的论文方向
- 基于高质量来源组织证据链
- 在证据和逻辑约束下形成论文草稿
- 通过改写和结构优化尽量降低 AIGC 痕迹与重复风险
- 生成可以直接交付用户的 `final-manuscript.docx`
- 对任务过程、关键决定和改稿过程进行记录

同时，`paperAgent` 支持个人简历/CV 创作，适合科研申请、实习申请、学术 CV、中文/英文/双语简历和 Overleaf/LaTeX 工作流。简历任务默认生成 `cv.md`、`cv.tex` 和可选的 `final-cv.pdf`；若用户提供本地头像图片路径，可复制为项目内 `profile-photo.*` 并在 LaTeX 页眉中引用。

## 目录约定

- `papers/`
  - 每次新的论文任务生成一个独立工程目录
  - 目录名建议：`YYYYMMDD-HHMMSS-topic-slug`
  - 工程内默认包含：`intake.md`、`brief.md`、`outline.md`、`draft.md`、`final-manuscript.docx`、`references.md`、`notes.md`
- `cvs/`
  - 每次新的 CV/Resume 任务生成一个独立工程目录
  - 目录名建议：`YYYYMMDD-HHMMSS-name-or-target-slug`
  - 工程内默认包含：`intake.md`、`brief.md`、`cv-data.md`、`cv.md`、`cv.tex`、`notes.md`
  - 若本机可用 XeLaTeX，则生成 `final-cv.pdf`
- `ref/`
  - 放置长期复用的参考资料
  - 包括：论文模板、引用规范、交互提问指引、来源优先级、质量检查表、LaTeX CV 指南
- `paper-agent/`
  - 自包含 Codex skill 包
  - 当前核心入口文件：`paper-agent/SKILL.md`
- `log/`
  - 放任务日志、改稿日志、决策记录
- `script/`
  - 放脚本
  - 例如：初始化论文工程、根据主题生成检索式、导出最终 `docx`、初始化 CV 工程、编译 LaTeX CV

## 交互式工作模式

默认采用“先澄清，再写作”的流程，不建议用户只给一个主题就直接起草全文。

推荐的交互原则：

- 第一轮优先确认论文类型
- 第一轮同步确认输出语言，默认可选中文或英文
- 每轮只问少量真正影响下一步的问题
- 问题应根据用户上轮回答动态变化
- 信息足够后立刻停止追问，转入提纲或写作
- 整体风格更像导师式访谈，而不是长表单

推荐流程：

1. 用户提供主题或大致方向
2. Agent 先优先确认论文类型和输出语言，再用少量高价值问题澄清目标、范围和硬约束
3. 将用户回答写入 `intake.md`
4. 从 `intake.md` 提炼出 `brief.md`
5. 根据 `brief.md` 组织检索与阅读
6. 先给出题目候选和提纲，再进入全文写作
7. 将当前可交付版本导出为 `final-manuscript.docx`
8. 记录日志并持续迭代

论文类型通常优先包括：

- 学位论文
- 课程结课论文
- 技术文档或技术报告
- 期刊论文
- 会议论文
- 综述论文
- 研究计划书

`paperAgent` 不应把所有主题都按同一种论文模板处理，而应根据论文类型动态追问。

输出语言默认支持：

- 中文
- 英文

`paperAgent` 应尽早固定输出语言，并保持 `draft.md` 与 `final-manuscript.docx` 的正文语言一致。

## LaTeX 简历/CV 工作模式

默认采用“先明确用途，再生成可编辑项目”的流程。第一轮优先确认目标用途、输出语言、篇幅、模板风格、是否需要头像、是否已有旧简历或项目/论文/获奖/技能素材。

内置模板风格：

- `classic`：保守、干净、通用
- `compact`：一页工业求职/ATS 友好
- `modern`：更美观的颜色强调版
- `academic`：科研/论文/学术成果导向

写作原则：

- 不编造学历、奖项、论文、项目结果、日期、排名或量化指标
- 优先将经历改写为“动作 + 方法/工具 + 对象 + 结果”的证据型 bullet
- 中文或双语简历默认使用 XeLaTeX
- 若面向 ATS 筛选或欧美工业求职，默认避免头像、图标、侧栏和复杂双栏布局
- 若用户提供头像，复制到 CV 工程目录并在 `cv.tex` 中引用
- 模板设计参考 Overleaf 和 GitHub 开源简历模板，但默认生成原创、轻依赖、易编译的 LaTeX 源码

## 工程边界

- 默认只使用当前已有一级目录：`papers`、`cvs`、`ref`、`paper-agent`、`log`、`script`
- 如需新增目录，应先征询用户意见
- 中间工作文件优先使用 `md`
- 论文最终交付默认包含 `final-manuscript.docx`；CV 最终交付默认包含 `cv.md`、`cv.tex`，本地 TeX 可用时包含 `final-cv.pdf`
- 若后续用户明确要求，可再用 Word 做最终排版增强

## 来源优先级

优先级从高到低：

1. 顶会、顶刊、正式出版论文
2. arXiv 预印本与作者主页版本
3. 官方技术文档、标准文档、实验室主页
4. 高质量技术博客、学术机构公开资料
5. 新闻媒体与营销材料

默认避免把新闻媒体内容当作主要技术依据。

## 写作约束

- 不编造引用，不伪造数据，不捏造实验
- 关键论断尽量回溯到具体文献或可审查推理
- 不把多个摘要直接拼接为正文
- 不追求空泛学术腔，优先追求逻辑闭环、术语准确和结构清楚
- 对高重复风险段落必须改写，优先重构论证顺序和表达层次

## 当前关键文件

- Skill 入口：[paper-agent/SKILL.md](paper-agent/SKILL.md)
- 交互提问指南：[ref/interactive-intake.md](ref/interactive-intake.md)
- 论文模板：[ref/paper-template.md](ref/paper-template.md)
- 引用规范：[ref/citation-style.md](ref/citation-style.md)
- 质量检查表：[ref/quality-checklist.md](ref/quality-checklist.md)
- 检索优先级：[ref/source-priority.md](ref/source-priority.md)
- LaTeX CV 指南：[ref/cv-latex-guide.md](ref/cv-latex-guide.md)
- DOCX 导出脚本：[script/export_final_docx.py](script/export_final_docx.py)
- CV 初始化脚本：[script/init_cv_project.py](script/init_cv_project.py)
- CV 初始化 PowerShell 包装器：[script/init_cv_project.ps1](script/init_cv_project.ps1)
- CV 编译脚本：[script/compile_latex_cv.ps1](script/compile_latex_cv.ps1)

## 发布建议

如果需要将 `paperAgent` 公开发布：

- 保留 `paper-agent/`、`ref/`、`script/`、`readme.md`
- 保留 `papers/` 与 `cvs/` 目录本身，但不要公开其中真实论文工程、简历内容或头像图片
- `log/` 建议只保留模板，不保留具体用户任务记录
- 推荐配合 `.gitignore` 一起发布，避免后续把本地论文工程和缓存文件误提交

## Codex Skill 安装

`paperAgent` 已打包为自包含的 Codex skill，位于 `paper-agent/` 目录。

### 安装步骤

**Windows:**
```powershell
# 复制 paper-agent 目录到 Codex skills 目录
Copy-Item -Recurse .\paper-agent $env:USERPROFILE\.codex\skills\
```

**macOS / Linux:**
```bash
# 复制 paper-agent 目录到 Codex skills 目录
cp -r ./paper-agent ~/.codex/skills/
```

### 验证安装

确保以下结构存在：
```
~/.codex/skills/paper-agent/SKILL.md
~/.codex/skills/paper-agent/ref/
~/.codex/skills/paper-agent/script/
```

详细安装说明请参阅 [paper-agent/README.md](paper-agent/README.md)。
