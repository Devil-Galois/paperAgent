# paperAgent

`paperAgent` 是一个面向 Agent 的交互式论文写作工程脚手架。它不是“一次性生成整篇文章”的简单文本工具，而是把论文写作拆成更真实的工作流：先根据用户主题做澄清，再收集资料、组织提纲、撰写草稿、修改润色，最后导出 `docx` 交付稿。

它适合这样的场景：用户先给出一个主题，Agent 不急着直接开写，而是先判断论文类型、确认输出语言、追问少量真正影响写作的问题，然后再进入正式写作流程。

## 它能做什么

- 把一个粗略主题转成结构化论文工程
- 优先确认论文类型，而不是默认所有任务都按同一种模板处理
- 支持中文或英文输出
- 在起草前先保存用户回答，形成 `intake.md`
- 分离提纲、笔记、参考资料、正文草稿和最终交付稿
- 导出最终的 `final-manuscript.docx`
- 把可复用的写作规则、模板、脚本和参考材料沉淀在工程外层

## 适用场景

`paperAgent` 适合以下类型的写作任务：

- 课程结课论文
- 学位论文早期草稿
- 技术报告或技术文档
- 综述/调研类论文
- 期刊或会议论文准备稿
- 研究计划书

如果用户目前只有一个模糊主题，还需要 Agent 帮忙一起澄清方向，那么这个项目尤其合适。

## 核心工作流

1. 用户给出主题。
2. Agent 先确认论文类型。
3. Agent 再确认输出语言是中文还是英文。
4. Agent 根据前一轮回答，只问下一步真正需要的问题。
5. 用户回答被写入 `intake.md`。
6. Agent 从 `intake.md` 提炼出 `brief.md`，再生成提纲和正文草稿。
7. 最终导出 `final-manuscript.docx`。

整个交互应当是短轮次、动态追问、像讨论而不是像填表。

## 最小使用示例

下面是一个最小交互示例：

### 用户输入

```text
请帮我写一篇关于“人工智能时代集成电路人才发展机遇”的论文。
```

### Agent 第一轮追问

```text
先确认 3 件事：

1. 这篇是什么类型？
学位论文、课程结课论文、技术报告、期刊论文、会议论文，还是综述？

2. 最终稿用中文还是英文？

3. 你更希望我聚焦哪一块？
比如就业机会、继续深造、产业趋势，或者贴合你个人背景来写。
```

### 用户补充

```text
课程结课论文，中文，最好贴合我自己的专业背景写，字数 2000 左右。
```

### Agent 后续动作

- 把这些信息写入 `intake.md`
- 进一步确认专业背景和格式要求
- 生成 `brief.md`
- 输出提纲
- 写出 `draft.md`
- 导出 `final-manuscript.docx`

这个例子体现的核心不是“Agent 会写论文”，而是“Agent 会先把需求问清楚，再写论文”。

## 项目结构

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

## 关键文件

- [skills/SKILL.md](skills/SKILL.md)：Agent 的核心行为约定
- [ref/interactive-intake.md](ref/interactive-intake.md)：交互式 intake 的规则
- [ref/paper-template.md](ref/paper-template.md)：默认论文结构模板
- [script/init_paper_project.ps1](script/init_paper_project.ps1)：初始化新论文工程
- [script/export_final_docx.py](script/export_final_docx.py)：导出最终 `docx`

## 默认论文工程结构

每次论文任务，通常会在 `papers/` 下生成一个新目录，包含：

- `intake.md`
- `brief.md`
- `outline.md`
- `draft.md`
- `references.md`
- `notes.md`
- `final-manuscript.docx`

## 设计原则

- 先问清楚，再开始写
- 不默认论文类型
- 不默认输出语言
- 尽量让证据可追溯
- 原始笔记与最终正文分离
- 修改阶段主动降低重复、减少模板化 AI 语气
- 默认不把真实论文内容放进公开仓库

## 仓库边界

这个仓库公开的是“可复用脚手架”，不是具体论文内容。

- `papers/` 目录只保留空目录占位
- 真实论文工程不应提交到仓库
- `log/` 应优先保留模板，而不是用户真实任务记录
- `.gitignore` 已默认忽略论文工程内容和 Python 缓存文件

## 当前限制

- 默认 `docx` 导出路径是 Python 生成的 OpenXML 文件，不以 Word COM 自动化为主
- 当前导出更偏向结构和可读性，还不是完全精修的学术排版
- 最终稿质量依然高度依赖前期 intake 质量和资料选择质量

## 推荐后续扩展

如果要继续增强 `paperAgent`，比较自然的下一步包括：

- 增加更完整的 Word 排版能力，如封面、页码、悬挂缩进参考文献
- 连接 Zotero 或其他本地文献管理工具
- 增加面向不同期刊/会议的模板
- 增加更强的降重与去模板化改写规则

