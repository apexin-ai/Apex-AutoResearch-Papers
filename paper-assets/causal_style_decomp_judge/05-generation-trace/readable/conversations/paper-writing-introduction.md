# paper writing introduction

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 21
- **Recorded user turns:** 0
- **Tool calls:** 10
- **Original source:** `logs/chats/worker_paper_writing_introduction_20260520T232613.jsonl`
- **Structured JSON:** [`7e10d5db84c2460ebcf5.json`](../../sessions/7e/7e10d5db84c2460ebcf5.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

21 recorded events

### Tool call

_source line 1 · 2026-05-20T23:30:49.199225+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260520T232613",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-20T23:30:49.200222+00:00_

1	---
2	name: paper-writing-norms
3	description: 顶会级别论文写作风格规范——章节写法（Abstract/Intro/Related Work）、去 AI 风格、视觉密度、叙事哲学。Paper Agent 和 Worker 写论文章节时必须加载。
4	allowed-tools: [Read, Write, Edit, Glob, Grep]
5	scope: global
6	version: 2
7	priority: 9
8	tags:
9	  - writing
10	  - paper
11	  - style
12	  - norms
13	roles:
14	  - agent
15	  - worker
16	  - paper_agent
17	---
18	
19	# 论文写作风格规范
20	
21	> 核心哲学：**论文是一个有说服力的故事，不是实验报告。** 审稿人在几十秒内判断论文价值——如果 Abstract 和 Introduction 读起来像实验日志，论文就已经失败了。
22	
23	---
24	
25	## 一、总体写作哲学
26	
27	### 1.1 故事驱动，不是数据堆砌
28	
29	- 论文必须以"故事线"为核心展开：问题 → 洞察 → 方法 → 验证
30	- 禁止大量实验数据堆砌——每个数字出现必须服务于叙事推进
31	- 附录内容必须在正文中有明确引用且融入叙事，禁止简单堆砌
32	- 如果附录数据对核心叙事有重大影响，根据附录数据调整论文 framing
33	
34	### 1.2 主线统一性
35	
36	- 当 idea 在研究过程中发生变化后，**必须重审全文逻辑**
37	- 常见问题：Introduction 讲的故事 A，Method 做的是故事 B，Results 又在讲故事 C
38	- 修复方式：从最终实验结论反推，重写 Introduction 的问题定义和动机
39	- 每次 idea 调整后检查：Abstract → Introduction → Method → Results → Discussion → Conclusion 是否形成一条连贯主线
40	
41	### 1.3 专有名词必须有定义
42	
43	- 首次出现的专有名词/缩写必须给出完整定义和解释
44	- Abstract 中使用的缩写也必须在 Abstract 内定义（如 LLM = Large Language Model）
45	- 不能假设读者知道你自己定义的术语——论文从来没解释过的概念不能直接使用
46	- 通用规则：如果一个非标准术语第一次出现时没有括号定义，就是写作 bug
47	
48	### 1.4 写作前必读同类优秀论文
49	
50	- 每个章节动笔前，找 **2-3 篇目标会议近 1-2 年的高分论文**作为风格参考——同类问题或同类方法皆可
51	- 重点学：
52	  - Abstract 怎么用最少篇幅讲完故事
53	  - Introduction 怎么从大问题切入到具体贡献
54	  - Related Work 怎么 positioning 自己（不是 survey）
55	  - Table/Figure 怎么压缩信息密度
56	- **不是抄袭**，是学习同行的故事节奏和审美——不同子领域叙事节奏差异很大
57	- 实操：Paper Agent 可以从 `literature_map.yaml` 中挑 `role=foundation` 或 `role=direct-competitor` 的论文，把 `{title, venue, year, abstract}` 附在 Worker 的 task_prompt 中作为概念参考；如需学习写作风格本身，让 Worker 通过 WebSearch 取得论文链接并 fetch 全文
58	
59	---
60	
61	## 二、Abstract 写作规范
62	
63	### 2.1 四个必答问题（150-250 words）
64	
65	Abstract 必须在很短的篇幅内清楚回答：
66	1. **研究什么问题** — 1-2 句话交代背景和痛点
67	2. **为什么重要** — 现有方法的不足（不用写太多）
68	3. **本文提出什么** — 核心贡献的关键机制（简要，不堆砌细节）
69	4. **结果说明什么** — 用具体实验结论支撑贡献
70	
71	### 2.2 禁忌
72	
73	- **禁止堆砌数据**：Abstract 不是 Results 的缩写。最多引用 2-3 个关键数字，要服务于 claim
74	- **
…[truncated 5709 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260520T232613",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-20T23:30:49.200718+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260520T232613",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-20T23:30:49.201564+00:00_

1	---
2	name: latex-paper
3	description: ML 顶会论文 LaTeX 写作全流程——Claim-Evidence 方法论、引用防幻觉、顶会模板速查、投稿工程链、会议转投。写论文/投稿时参考。
4	scope: global
5	tags:
6	- latex
7	- paper-writing
8	- academic
9	- citation
10	- submission
11	version: 1
12	roles:
13	- agent
14	- worker
15	---
16	
17	# LaTeX 论文写作全流程
18	
19	ML/AI 顶会论文从草稿到投稿的完整指南。整合 Orchestra Research、VibeSkills、claim2evidence 三方最佳实践。
20	
21	---
22	
23	## 1. 工作模式
24	
25	开始前选择模式：
26	
27	| 模式 | 说明 | 适用 |
28	|------|------|------|
29	| **Build** | 从实验笔记/结果/代码生成论文 | 新稿 |
30	| **Improve** | 改写已有章节，强化论证 | 修改稿 |
31	| **Audit** | 输出风险列表 + 缺失证据 + 修复建议 | 投前检查 |
32	
33	---
34	
35	## 2. Claim-Evidence 方法论
36	
37	**核心原则：论文是一个有中心贡献的故事，不是实验的堆砌。**
38	
39	### 2.1 一句话贡献
40	
41	在写任何内容之前，必须能用一句话说清贡献。如果不能，说明还没准备好写论文。
42	
43	### 2.2 Claim-Evidence Map
44	
45	为每个 contribution 建立 claim→evidence 映射表：
46	
47	| Contribution | Claim | Evidence | Table/Figure |
48	|-------------|-------|----------|-------------|
49	| C1: 方法 X 在 Y 上 SOTA | 比所有 baseline 高 ≥2% | 5-seed 平均，p<0.05 | Table 1 |
50	| C2: 消融证明 Z 是关键 | 去掉 Z 后掉 >5% | 消融实验 | Table 2 |
51	| C3: 计算效率 | 比 baseline 快 3× | FLOPs + wall-clock | Figure 3 |
52	
53	**没有直接证据支撑的 claim 必须删除或降级为 discussion。**
54	
55	### 2.3 章节起草顺序
56	
57	```
58	1. Introduction + Experiments（先确定 claim 和 evidence）
59	2. Method（评估问题稳定后再写细节）
60	3. Related Work
61	4. Abstract + Title（核心 claim 定型后最后写）
62	```
63	
64	### 2.4 Quality Gates
65	
66	投稿前必须通过：
67	- [ ] 前两段出现显式 novelty 声明
68	- [ ] 每个 contribution 有可验证的 evidence
69	- [ ] Abstract / Intro / Conclusion 的 claim 一致
70	- [ ] Limitations 真实且技术性诚实
71	- [ ] 审稿人两分钟内能识别 delta
72	
73	---
74	
75	## 3. 引用防幻觉（CRITICAL）
76	
77	**AI 生成引用有 ~40% 错误率。绝对禁止凭记忆写 BibTeX。**
78	
79	### 3.1 黄金法则
80	
81	```
82	IF 无法程序化获取引用:
83	    → 标记 [CITATION NEEDED] 或 \cite{PLACEHOLDER_verify}
84	    → 明确告知用户
85	    → 绝不编造看似合理的引用
86	```
87	
88	### 3.2 五步验证流程
89	
90	```
91	1. SEARCH  → Semantic Scholar API 搜索关键词
92	2. VERIFY  → 至少 2 个来源确认论文存在（S2 + arXiv/CrossRef）
93	3. RETRIEVE → 通过 DOI 获取 BibTeX（程序化，非记忆）
94	4. CHECK   → 确认
…[truncated 7201 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260520T232613",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-20T23:30:49.202195+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/skills/projects/causal_style_decomp_judge/distilled-writing.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260520T232613",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/skills/projects/causal_style_decomp_judge/distilled-writing.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-20T23:30:49.225724+00:00_

1	---
2	name: LLM Judge Style Bias — Writing Patterns
3	description: 从8篇深度精读论文蒸馏的叙事策略、图表设计共识、投稿编排经验
4	type: writing
5	source_papers: 8 deep-read (ICLR/ICML/arXiv 2025-2026)
6	---
7	
8	## 叙事类型分布
9	
10	突破局限型（3/8）最主流：SOS-Bench、Preference Leakage、CASSE。模式="大家都在用X，但X有个被忽视的致命问题"。化繁为简型（2/8）：LC-AlpacaEval、RATE。模式="复杂问题有个优雅的简单解"。统一框架型（2/8）：FairJudge、Soumik。跨界迁移型（1/8）：Counterfactual Rhetorical。**置信度：高。**
11	
12	## 开篇钩子模式
13	
14	**"普遍实践+隐藏风险"钩子**（5/8，主流）：从社区公认的实践（LLM-judge评估/style prompting/合成数据训练）切入，然后揭示隐藏的系统性问题。代表：SOS-Bench"PO方法爆炸增长，都依赖LLM-judge，但judge偏好=对齐吗？"；CASSE"Style prompting无处不在，但没人验证feature独立性假设"。
15	
16	**"具体失败案例"钩子**（1/8）：Figure 1直接展示两个judge判断翻转的案例（FairJudge）。视觉冲击力强但需要有好的失败例子。
17	
18	**可模仿策略**：第一句话锚定社区常识，第二句话用"but"转折引出被忽视的问题。LC-AlpacaEval和SOS-Bench都用此结构。
19	
20	## Intro结构共识
21	
22	**4段结构**（5/8主流）：P1=问题背景 → P2=现有方法局限/Gap → P3=本文方案 → P4=贡献列表。**贡献条数**：3-4条（4条更常见，4/8），名词短语标签开头（Soumik/FairJudge/CASSE/Counterfactual Rhetorical），从概念→方法→验证递进。置信度：高。
23	
24	## Figure 1设计
25	
26	**problem_illustration**（4/8最主流）：对比布局展示"旧方法vs新视角"或"失败案例"。设计元素共识：左右对比布局（4/8）、颜色编码区分类型（5/8）、真实数据/案例（3/8）。
27	
28	**method_overview**（2/8）：多阶段pipeline流程图。适合方法论贡献型论文。
29	
30	**teaser_result**（1/8）：开篇即亮核心数字（LC-AlpacaEval的柱状图）。高风险高收益——数字必须够震撼。
31	
32	**可模仿**：SOS-Bench的Figure 1用概念对比图建立分析框架，后续逐一击破；Preference Leakage用taxonomy流程图一张图定义整个问题空间。置信度：高。
33	
34	## 结果图表共识
35	
36	**主结果图**：line_plot（4/8）和bar_chart（5/8）并列主流。因果效应趋势用line_plot+CI band（RATE, Counterfactual Rhetorical）；多方法比较用grouped bar（Soumik, Preference Leakage）。**Gain突出手法**：置信区间/带（4/8）、直接数值标注（3/8）、颜色对比（4/8）。
37	
38	**交互/矩阵数据**：heatmap（CASSE的12×12矩阵，LC-AlpacaEval的模型对预测）。适合展示dense pairwise关系。
39	
40	**Scatter用于Pareto frontier**（Soumik: cost vs accuracy）或相关性展示（SOS-Bench: style R=0.999）。
41	
42	## 主结果表编排
43	
44	**行轴=methods，列轴=datasets×metrics**（6/8）。行按类别分组（by_category 5/8）：先frontier模型再mid-tier再开源，或先existing再proposed。列按dataset分组（grouped_by_dataset）。
45	
46	**Baseline数量**：3-9个（中位5-6）。**高亮策略**：significance markers（*†）+ bootstrap CIs（3/8）> bold_best（2/8）> color co
…[truncated 849 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260520T232613",
  "tool": "Read",
  "elapsed_ms": 23
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-20T23:30:49.226195+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/dream_reports/dream_20260520T211832/best/paper.tex",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260520T232613",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/dream_reports/dream_20260520T211832/best/paper.tex",
    "limit": "80"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-20T23:30:49.226549+00:00_

1	\documentclass[11pt,a4paper]{article}
2	\usepackage[utf8]{inputenc}
3	\usepackage[T1]{fontenc}
4	\usepackage{times}
5	\usepackage{graphicx}
6	\usepackage{amsmath,amssymb}
7	\usepackage{booktabs}
8	\usepackage{multirow}
9	\usepackage{xcolor}
10	\usepackage[margin=2.5cm]{geometry}
11	\usepackage{hyperref}
12	\usepackage{cleveref}
13	\usepackage{natbib}
14	\bibliographystyle{plainnat}
15	
16	\newcommand{\cmark}{\checkmark}
17	
18	\title{Causal Style Decomposition Reveals Systematic Style Bias\\in LLM-as-Judge That Likert Scoring Misses}
19	
20	\author{Anonymous}
21	\date{}
22	
23	\begin{document}
24	\maketitle
25	
26	% ============================================================
27	% ABSTRACT
28	% ============================================================
29	\begin{abstract}
30	LLM-as-judge has become critical infrastructure for NLP evaluation and alignment training, yet recent work shows style bias dominates other judge biases.
31	Existing analyses treat style as a monolithic dimension or rely on correlational evidence.
32	We introduce \textbf{Causal Style Decomposition (CSD)}, a black-box, post-hoc framework that generates binary style counterfactuals, verifies content preservation via NLI and BERTScore, and measures causal style bias through position-controlled pairwise comparison.
33	Across 3 judges (GPT-4o, Claude-Sonnet, Gemini-Flash), 3 benchmarks (LLMBar, AlpacaEval, MT-Bench), and 3 style axes (formality, tone, register), CSD detects significant style premiums (mean win rate 66.3\%, $p<0.05$ in 7--9 of 9 judge$\times$benchmark cells for formality).
34	We uncover a systematic \emph{measurement gap}: standard Likert pointwise scoring fails to detect any of these biases (0/9 significant), while pairwise comparison succeeds (7/9 significant)---implying that prior Likert-based studies may systematically underestimate style bias severity.
35	Style bias is axis-dependent: formality (68.4\%) $>$ register (66.3\%) $>$ tone (63.4\%), with lighter models (Gemini-Flas
…[truncated 4015 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260520T232613",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-20T23:30:49.226871+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260520T232613",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-20T23:30:49.227114+00:00_

docs/paper/main.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260520T232613",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-20T23:30:49.257372+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/ 2>/dev/null || echo \"DIR_NOT_FOUND\"",
  "description": "Check if sections directory exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260520T232613",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/ 2>/dev/null || echo \"DIR_NOT_FOUND\"",
    "description": "Check if sections directory exists"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-20T23:30:49.290029+00:00_

total 8
drwxr-xr-x 2 ubuntu ubuntu 4096 May 20 23:23 .
drwxr-xr-x 3 ubuntu ubuntu 4096 May 20 23:23 ..

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260520T232613",
  "tool": "Bash",
  "elapsed_ms": 60
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-20T23:30:49.290332+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260520T232613",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-20T23:30:49.290561+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{inconsolata}
11	\usepackage{graphicx}
12	\usepackage{booktabs}
13	\usepackage{amsmath,amssymb}
14	\usepackage{xcolor}
15	\usepackage{subcaption}
16	
17	\title{Causal Style Decomposition Reveals the Likert Blindspot:\\Standard Scoring Underestimates Style Bias in LLM Judges}
18	
19	\author{Anonymous}
20	
21	\begin{document}
22	\maketitle
23	
24	\input{sections/abstract}
25	
26	\input{sections/introduction}
27	
28	% \input{sections/related_work}
29	
30	% \input{sections/method}
31	
32	% \input{sections/experiments}
33	
34	% \input{sections/conclusion}
35	
36	\section*{Limitations}
37	
38	% TODO: Add limitations section
39	
40	\bibliography{references}
41	
42	\end{document}
43	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260520T232613",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-20T23:30:49.291020+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/introduction.tex",
  "content": "\\section{Introduction}\n\nLarge Language Model (LLM) judges have become central infrastructure for NLP evaluation and preference-based alignment training.\nSystems such as AlpacaEval, MT-Bench, and Chatbot Arena rely on LLM judges to score and rank model outputs, and the resulting leaderboards guide both academic research and industry deployment.\nReinforcement Learning from Human Feedback (RLHF) and Direct Preference Optimization (DPO) pipelines consume judge-generated preferences as reward signals that shape model behavior during alignment.\nThe reliability of these judgments carries direct consequences: it determines which models the community considers superior and which response patterns are reinforced.\nAs automated judges increasingly mediate both evaluation and training, any systematic bias in their assessments propagates through the entire model development pipeline.\n\nRecent work has converged on a striking finding: \\emph{style bias} is the dominant source of unreliability in LLM judges, far outweighing other documented biases such as position or verbosity preference.\n\\citet{murugadoss2025sos} show that style features alone explain judge scores with $R = 0.999$, far exceeding the explanatory power of content features.\n\\citet{li2026preference} demonstrate that 76--92\\% of observed preference signals originate from surface-level style cues rather than substantive quality differences.\n\\citet{soumik2026judging} report bias scores of 0.76--0.92 across five different judges.\nDespite this consensus on severity, existing approaches share four critical gaps: (1)~they treat style as a single dimension, typically reducing it to response length; (2)~they rely on correlational analyses that cannot establish causal direction; (3)~population-level corrections such as length-controlled AlpacaEval \\citep{dubois2025lc} cannot diagnose per-instance bias; and (4)~no existing method provides black-box, post-hoc, per-axis causal detection.\nRecent multi-feature frameworks such as CASSE \\citep{casse2026concise} and FairJudge \\citep{wang2026fairjudge} begin to decompose style into finer dimensions, but neither provides causal identification of per-axis effects.\nA further methodological concern compounds these limitations: standard Likert pointwise scoring (integer scales from 1 to 10) exhibits a ceiling effect that masks real bias.\nOn our data, 64\\% of counterfactual pairs receive identical Likert scores ($\\Delta = 0$), and this integer ceiling effect leaves Likert insensitive to style interventions that pairwise comparison readily detects.\n\nWe propose Causal Style Decomposition (CSD), a framework that addresses all four gaps.\nDrawing on causal inference methods for text \\citep{veitch2020adapting}, CSD operates in three stages: binary style counterfactual generation along a single axis (e.g., formal vs.\\ casual), content preservation verification through Natural Language Inference (NLI) entailment and BERTScore filtering, and causal bias measurement via position-controlled pairwise comparison.\nBecause CSD requires no access to judge internals and applies post-hoc to any black-box judge, it complements existing population-level approaches and provides finer-grained, per-instance diagnostics.\nOur experiments reveal what we term the \\emph{Likert Blindspot}: on the same formality data, Likert scoring yields a corrected Average Treatment Effect (ATE) of $+0.102$ (Cohen's $d = 0.104$, $p = 0.332$, $n = 88$), a non-significant result, while pairwise comparison shows a formal win rate of 69.1\\% (Wilson CI: $[55.97\\%, 79.72\\%]$, sign test $p = 0.006$, $n = 55$ consistent pairs).\nFigure~\\ref{fig:likert_blindspot} illustrates this divergence.\nUnlike LC-AlpacaEval \\citep{dubois2025lc}, which applies a single population-level length regression, CSD decomposes bias along multiple axes with per-instance causal intervention.\n\nOur contributions are as follows:\n\\begin{itemize}\n    \\item \\textbf{A black-box causal framework} for detecting per-axis style bias in LLM judges through binary counterfactual generation and position-controlled pairwise comparison (Section~\\ref{sec:method}).\n    \\item \\textbf{The Likert Blindspot phenomenon:} empirical evidence that standard pointwise scoring systematically fails to detect style biases that pairwise comparison reveals, with formality bias undetectable by Likert ($p = 0.332$) but significant under pairwise measurement (69.1\\%, $p = 0.006$) (Section~\\ref{sec:experiments}, Figure~\\ref{fig:likert_blindspot}).\n    \\item \\textbf{Evidence of axis-dependent bias:} \\textit{[to be updated with full experimental results across multiple judges and style axes]}.\n    \\item \\textbf{Practical implications for evaluation methodology:} style bias audits should employ pairwise comparison rather than Likert scoring, and bias must be assessed per axis rather than as a single ``style'' factor (Section~\\ref{sec:discussion}).\n\\end{itemize}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260520T232613",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/introduction.tex",
    "content": "\\section{Introduction}\n\nLarge Language Model (LLM) judges have become central infrastructure for NLP evaluation and preference-based alignment training.\nSystems such as AlpacaEval, MT-Bench, and Chatbot Arena rely on LLM judges to score and rank model outputs, and the resulting leaderboards guide both academic research and industry deployment.\nReinforcement Learning from Human Feedback (RLHF) and Direct Preference Optimization (DPO) pipelines consume judge-generated preferences as reward signals that shape model behavior during alignment.\nThe reliability of these judgments carries direct consequences: it determines which models the community considers superior and which response patterns are reinforced.\nAs automated judges increasingly mediate both evaluation and training, any systematic bias in their assessments propagates through the entire model development pipeline.\n\nRecent work has converged on a striking finding: \\emph{style bias} is the dominant source of unreliability in LLM judges, far outweighing other documented biases such as position or verbosity preference.\n\\citet{murugadoss2025sos} show that style features alone explain judge scores with $R = 0.999$, far exceeding the explanatory power of content features.\n\\citet{li2026preference} demonstrate that 76--92\\% of observed preference signals originate from surface-level style cues rather than substantive quality differences.\n\\citet{soumik2026judging} report bias scores of 0.76--0.92 across five different judges.\nDespite this consensus on severity, existing approaches share four critical gaps: (1)~they treat style as a single dimension, typically reducing it to response length; (2)~they rely on correlational analyses that cannot establish causal direction; (3)~population-level corrections such as length-controlled AlpacaEval \\citep{dubois2025lc} cannot diagnose per-instance bias; and (4)~no existing method provides black-box, post-hoc, per-axis causal detection.\nRecent multi-feature frameworks such as CASSE \\citep{casse2026concise} and FairJudge \\citep{wang2026fairjudge} begin to decompose style into finer dimensions, but neither provides causal identification of per-axis effects.\nA further methodological concern compounds these limitations: standard Likert pointwise scoring (integer scales from 1 to 10) exhibits a ceiling effect that masks real bias.\nOn our data, 64\\% of counterfactual pairs receive identical Likert scores ($\\Delta = 0$), and this integer ceiling effect leaves Likert insensitive to style interventions that pairwise comparison readily detects.\n\nWe propose Causal Style Decomposition (CSD), a framework that addresses all four gaps.\nDrawing on causal inference methods for text \\citep{veitch2020adapting}, CSD operates in three stages: binary style counterfactual generation along a single axis (e.g., formal vs.\\ casual), content preservation verification through Natural Language Inference (NLI) entailment and BERTScore filtering, and causal bias measurement via position-controlled pairwise comparison.\nBecause CSD requires no access to judge internals and applies post-hoc to any black-box judge, it complements existing population-level approaches and provides finer-grained, per-instance diagnostics.\nOur experiments reveal what we term the \\emph{Likert Blindspot}: on the same formality data, Likert scoring yields a corrected Average Treatment Effect (ATE) of $+0.102$ (Cohen's $d = 0.104$, $p = 0.332$, $n = 88$), a non-significant result, while pairwise comparison shows a formal win rate of 69.1\\% (Wilson CI: $[55.97\\%, 79.72\\%]$, sign test $p = 0.006$, $n = 55$ consistent pairs).\nFigure~\\ref{fig:likert_blindspot} illustrates this divergence.\nUnlike LC-AlpacaEval \\citep{dubois2025lc}, which applies a single population-level length regression, CSD decomposes bias along multiple axes with per-instance causal intervention.\n\nOur contributions are as follows:\n\\begin{itemize}\n    \\item \\textbf{A black-box causal framework} for detecting per-axis style bias in LLM judges through binary counterfactual generation and position-controlled pairwise comparison (Section~\\ref{sec:method}).\n    \\item \\textbf{The Likert Blindspot phenomenon:} empirical evidence that standard pointwise scoring systematically fails to detect style biases that pairwise comparison reveals, with formality bias undetectable by Likert ($p = 0.332$) but significant under pairwise measurement (69.1\\%, $p = 0.006$) (Section~\\ref{sec:experiments}, Figure~\\ref{fig:likert_blindspot}).\n    \\item \\textbf{Evidence of axis-dependent bias:} \\textit{[to be updated with full experimental results across multiple judges and style axes]}.\n    \\item \\textbf{Practical implications for evaluation methodology:} style bias audits should employ pairwise comparison rather than Likert scoring, and bias must be assessed per axis rather than as a single ``style'' factor (Section~\\ref{sec:discussion}).\n\\end{itemize}\n"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-20T23:30:49.291355+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/introduction.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260520T232613",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-20T23:30:49.291579+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__register_artifact",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260520T232613",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__register_artifact",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-20T23:30:49.291763+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260520T232613",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-20T23:30:49.291940+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "introduction_section_v1",
  "type": "paper",
  "description": "Introduction section (v1) for EMNLP 2026 submission. 4-paragraph structure: LLM judge infrastructure → style bias dominance + 4 gaps + Likert ceiling → CSD framework + Likert Blindspot data → contributions list. ~650 words, ACL template.",
  "project": "causal_style_decomp_judge",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/introduction.tex",
  "tags": "['paper', 'introduction', 'v1', 'emnlp2026']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260520T232613",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "introduction_section_v1",
    "type": "paper",
    "description": "Introduction section (v1) for EMNLP 2026 submission. 4-paragraph structure: LLM judge infrastructure → style bias dominance + 4 gaps + Likert ceiling → CSD framework + Likert Blindspot data → contributions list. ~650 words, ACL template.",
    "project": "causal_style_decomp_judge",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/introduction.tex",
    "tags": "['paper', 'introduction', 'v1', 'emnlp2026']"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-20T23:30:49.292165+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260520_64eb98\", \"name\": \"introduction_section_v1\", \"type\": \"paper\", \"description\": \"Introduction section (v1) for EMNLP 2026 submission. 4-paragraph structure: LLM judge infrastructure → style bias dominance + 4 gaps + Likert ceiling → CSD framework + Likert Blindspot data → contributions list. ~650 words, ACL template.\", \"path\": \"projects/causal_style_decomp_judge/artifacts/_project/paper/introduction.tex\", \"url\": null, \"project\": \"causal_style_decomp_judge\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-20T23:30:32.549155+00:00\", \"tags\": [\"paper\", \"introduction\", \"v1\", \"emnlp2026\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260520T232613",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-20T23:30:49.292452+00:00_

Introduction 已写入 `docs/paper/sections/introduction.tex`。

**结构概览：**
- **P1** (5句): LLM judge 作为评估+对齐核心基础设施，bias 传播风险
- **P2** (8句): style bias 主宰地位 (SOS-Bench R=0.999, Preference Leakage 76-92%, Soumik 0.76-0.92) → 4个gap → CASSE/FairJudge仍无因果识别 → Likert整数天花板效应 (64% Δ=0)
- **P3** (6句): CSD三阶段机制 → Likert Blindspot命名 (Likert ATE=+0.102, p=0.332 vs Pairwise 69.1%, p=0.006) → 与LC-AlpacaEval对比
- **P4**: 4条contributions (框架/Blindspot现象/axis-dependent placeholder/实践意义)

**引用使用：** murugadoss2025sos, li2026preference, soumik2026judging, dubois2025lc (×2), casse2026concise, wang2026fairjudge, veitch2020adapting

**Contribution 3** 保留 placeholder 待实验数据填充。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_writing_introduction_20260520T232613"
}
```

</details>

---
