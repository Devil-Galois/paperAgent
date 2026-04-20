# paperAgent

版本：v0.3.0  
状态：可用于“用户给出研究主题后，Agent 先交互澄清，再搜集资料、起草论文，并导出最终 `docx` 交付稿”的版本。  
最后更新：2026-04-20

## 目标

`paperAgent` 面向科研论文写作，不应表现为一次性生成器，而应表现为可交互的研究写作助手。它的核心职责是：

- 根据用户主题先做必要的访谈式澄清
- 帮用户把模糊想法收敛成可执行的论文方向
- 基于高质量来源组织证据链
- 在证据和逻辑约束下形成论文草稿
- 通过改写和结构优化尽量降低 AIGC 痕迹与重复风险
- 生成可以直接交付用户的 `final-manuscript.docx`
- 对任务过程、关键决定和改稿过程进行记录

## 目录约定

- `papers/`
  - 每次新的论文任务生成一个独立工程目录
  - 目录名建议：`YYYYMMDD-HHMMSS-topic-slug`
  - 工程内默认包含：`intake.md`、`brief.md`、`outline.md`、`draft.md`、`final-manuscript.docx`、`references.md`、`notes.md`
- `ref/`
  - 放置长期复用的参考资料
  - 包括：论文模板、引用规范、交互提问指引、来源优先级、质量检查表
- `skills/`
  - 放置给 Agent 阅读的 skill
  - 当前核心入口文件：`SKILL.md`
- `log/`
  - 放任务日志、改稿日志、决策记录
- `script/`
  - 放脚本
  - 例如：初始化论文工程、根据主题生成检索式、导出最终 `docx`

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

## 工程边界

- 默认只使用当前已有一级目录：`papers`、`ref`、`skills`、`log`、`script`
- 如需新增目录，应先征询用户意见
- 中间工作文件优先使用 `md`
- 最终交付默认包含 `final-manuscript.docx`
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

- Skill 入口：[skills/SKILL.md](skills/SKILL.md)
- 交互提问指南：[ref/interactive-intake.md](ref/interactive-intake.md)
- 论文模板：[ref/paper-template.md](ref/paper-template.md)
- 引用规范：[ref/citation-style.md](ref/citation-style.md)
- 质量检查表：[ref/quality-checklist.md](ref/quality-checklist.md)
- 检索优先级：[ref/source-priority.md](ref/source-priority.md)
- DOCX 导出脚本：[script/export_final_docx.py](script/export_final_docx.py)

## 发布建议

如果需要将 `paperAgent` 公开发布：

- 保留 `skills/`、`ref/`、`script/`、`readme.md`
- 保留 `papers/` 目录本身，但不要公开其中真实论文工程内容
- `log/` 建议只保留模板，不保留具体用户任务记录
- 推荐配合 `.gitignore` 一起发布，避免后续把本地论文工程和缓存文件误提交
