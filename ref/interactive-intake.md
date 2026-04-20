# Interactive Intake Guide

Use this guide when the user gives a topic and the paper direction is still underspecified.

## Principle

Ask only the questions that change one of these:

- search keywords
- paper type
- output language
- argument structure
- evidence standard
- writing constraints

If a question would not affect the next step, do not ask it yet.

The interaction should feel like a guided discussion, not a template dump.

- prefer natural short questions
- ask in rounds
- after each round, summarize and narrow
- stop once the next action is clear

## Question Order

### Batch 1: paper type and scope

Use this first when the input is vague.

1. What kind of paper is this?
   - degree thesis
   - course paper or final assignment paper
   - technical report or technical document
   - journal paper
   - conference paper
   - survey/review
   - proposal
2. Should the final output be in Chinese or English?
3. What exact topic or subproblem should it focus on?
4. What output constraints matter most?
   - output language if not decided yet
   - approximate length
   - deadline
   - target venue, institution, or class requirement

The first batch should normally identify the paper type before deeper questions.

Recommended first-turn pattern:

1. ask paper type
2. ask output language
3. ask topic focus
4. ask one hard constraint

Example:

- "先确认一下，这篇是学位论文、课程结课论文、技术文档，还是期刊/会议论文？"
- "最终稿你希望我用中文写，还是英文写？"
- "这个主题里你最想聚焦哪一块？"
- "有没有字数、截止时间、课程要求或目标投稿方向？"

### Batch 2: user intention and contribution angle

Use this when the topic is known but the writing angle is still unclear.

1. Do you already have a tentative viewpoint, hypothesis, or preferred method?
2. Do you want the paper to emphasize theory, systems, experiments, or application?
3. Are there must-include ideas, datasets, papers, or keywords?

Ask this batch only after the paper type is already clear or mostly clear.

### Batch 3: type-specific follow-up

Pick only the branch that matches the user's paper type.

#### Degree thesis

Ask about:

1. degree level
2. institution or advisor requirements
3. expected chapter depth
4. whether original contribution, experiments, or implementation are required

Suggested natural prompts:

- "这是本科、硕士还是博士层面的学位论文？"
- "学校或导师对格式、章节、工作量有没有明确要求？"
- "你这篇需要体现原创研究，还是偏系统整理与分析？"

#### Course paper

Ask about:

1. course name and assignment requirement
2. target length
3. whether it should be a review, analysis, or proposal
4. whether formal novelty is required or a solid synthesis is enough

Suggested natural prompts:

- "这是哪门课的结课论文？老师有没有给 rubric 或题目边界？"
- "你更需要一篇扎实综述，还是围绕某个技术点做分析？"
- "大概字数和提交时间是多少？"

#### Technical report or technical document

Ask about:

1. target reader
2. practical purpose
3. system boundary or product boundary
4. whether formal academic citations are required

Suggested natural prompts:

- "这份文档是写给谁看的，研发团队、管理者，还是客户？"
- "它主要是为了方案论证、设计说明，还是技术调研汇总？"
- "需要学术化引用，还是工程文档风格即可？"

#### Journal or conference paper

Ask about:

1. target venue or venue family
2. main contribution claim
3. required experiments, benchmarks, or comparisons
4. submission deadline or urgency

Suggested natural prompts:

- "你打算按会议论文还是期刊论文的标准来写？有目标 venue 吗？"
- "你希望核心贡献落在方法、系统、实验，还是分析框架上？"
- "有没有必须补足的实验、benchmark 或对比基线？"

### Batch 4: boundary and exclusion

Use this before literature search if the topic could easily sprawl.

1. What should be excluded?
2. What depth is expected?
3. Should the paper stay conservative and evidence-driven, or can it include speculative discussion?

## When the User Is Unsure

Do not repeat the same question in abstract form. Instead:

- propose 2 or 3 candidate directions
- explain the tradeoff of each direction in one sentence
- ask the user to pick or modify one

Example:

- direction A: broad review, easier to complete, weaker novelty
- direction B: narrow technical comparison, stronger focus, needs sharper source selection
- direction C: proposal-style paper, more creative, requires explicit assumptions

If the user is unsure about paper type, offer a short explanation instead of just listing names.

Example:

- course paper: faster to finish, usually prioritizes understanding and synthesis
- journal or conference paper: requires sharper contribution and stronger evidence
- technical report: prioritizes engineering clarity and practical usefulness
- degree thesis: broader structure, stronger completeness and documentation requirements

If the user is unsure about output language, clarify by use case:

- Chinese: faster iteration with local teaching or internal writing contexts
- English: better fit for international venues, English-speaking reviewers, or publication-style drafts

If the user is unsure about topic focus, provide candidate angles derived from the topic instead of asking the same question again.

Example:

- angle A: broader background review
- angle B: narrow technical comparison
- angle C: problem-driven proposal or improvement path

## Intake Summary Format

After each batch, summarize using this structure:

- current topic:
- paper type:
- output language:
- why this type matters:
- likely focus:
- hard constraints:
- soft preferences:
- unknowns that still block progress:

## Stop Conditions

You can stop asking questions and move forward when:

- the topic boundary is clear enough to search
- the paper type is clear enough to choose structure
- the user constraints are clear enough to avoid major rework

If these are satisfied, stop interviewing and start working.

## Interaction Failure Modes to Avoid

- asking the user to answer too many questions in one turn
- asking for information that can be safely inferred later
- staying in interview mode after enough information is already available
- switching to drafting before the paper type and scope are clear
