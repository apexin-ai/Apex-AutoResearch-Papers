# paper writing method

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 0
- **Tool calls:** 5
- **Original source:** `logs/chats/worker_paper_writing_method_20260521T025540.jsonl`
- **Structured JSON:** [`02d5f566f6cc4145c7a0.json`](../../sessions/02/02d5f566f6cc4145c7a0.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

11 recorded events

### Tool call

_source line 1 · 2026-05-21T02:57:28.948096+00:00_

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
  "session": "worker_paper_writing_method_20260521T025540",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-21T02:57:28.948677+00:00_

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
  "session": "worker_paper_writing_method_20260521T025540",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-21T02:57:28.948874+00:00_

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
  "session": "worker_paper_writing_method_20260521T025540",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-21T02:57:28.949218+00:00_

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
  "session": "worker_paper_writing_method_20260521T025540",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-21T02:57:28.949430+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260521T025540",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-21T02:57:28.949593+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	% TODO: Full method description (pipeline overview, style-controlled rewriting, NLI gating, pairwise comparison protocol)
5	
6	\subsection{Causal Framework}
7	\label{sec:causal_framework}
8	
9	Figure~\ref{fig:dag} presents the assumed data-generating process.
10	Three variables govern the observed judge score $Y$: the style attribute $S$ (e.g., formality), the original content quality $Q$, and the judge's internal scoring function.
11	Both $S$ and $Q$ causally influence $Y$; the goal of CSD is to isolate the effect $S \to Y$ while blocking confounding through $Q$.
12	Style-controlled rewriting generates a text pair that differs along a single style axis, but any rewriting operation risks inadvertently altering content quality ($R \to Q$).
13	The NLI entailment gate approximates the \emph{do}-operator by filtering out pairs where the rewrite changed semantic content, thereby blocking the $R \to Q$ path and yielding an interventional estimate of the $S \to Y$ effect.
14	Our approach provides interventional rather than formal causal evidence: we do not claim that this DAG is a complete structural causal model, nor do we invoke SUTVA or consistency assumptions from the potential outcomes framework.
15	
16	\begin{figure}[t]
17	\centering
18	\begin{tikzpicture}[
19	    node distance=2.2cm and 2.5cm,
20	    every node/.style={font=\small},
21	    obs/.style={draw, circle, minimum size=1cm, thick},
22	    mech/.style={draw, rectangle, rounded corners, minimum size=0.8cm, thick, fill=gray!10},
23	    gate/.style={draw, rectangle, dashed, thick, fill=blue!8, font=\footnotesize},
24	    arr/.style={-{Stealth[length=5pt]}, thick},
25	    blocked/.style={-{Stealth[length=5pt]}, thick, dashed, red!60},
26	  ]
27	  \node[obs] (S) {$S$};
28	  \node[obs, right=of S] (Y) {$Y$};
29	  \node[obs, above=1.5cm of Y] (Q) {$Q$};
30	  \node[mech, left=1.8cm of Q] (R) {Rewrite};
31	  \node[gate, below=0.4cm of R] (NLI) {NLI gate};
32	
33	  \draw[ar
…[truncated 659 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260521T025540",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-21T02:57:28.949832+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/method.tex",
  "old_string": "% TODO: Full method description (pipeline overview, style-controlled rewriting, NLI gating, pairwise comparison protocol)\n\n\\subsection{Causal Framework}",
  "new_string": "\\subsection{Style-Controlled Rewriting}\n\\label{sec:rewriting}\n\nWe isolate the causal effect of individual style attributes on judge scores by generating text pairs that differ along exactly one style axis.\nGiven an input text, an instruction-tuned LLM (Qwen3-32B, temperature 0.7) rewrites it according to an axis-specific prompt (e.g., ``Rewrite the following text to be more formal/casual while preserving the exact same content and meaning'').\nFor each axis, we produce both a forward rewrite (original $\\to$ target style) and a backward rewrite (target $\\to$ original style) to form a symmetric pair.\nThis bidirectional design controls for asymmetric effects: a text shortened for conciseness may lose information that an expansion would not.\nEach operation constitutes a binary intervention on a single style variable while all other axes remain fixed (Section~\\ref{sec:causal_framework}).\n\n\\subsection{Content Preservation Verification}\n\\label{sec:nli_gate}\n\nStyle-controlled rewriting risks altering semantic content, which would confound the style effect with a content quality effect (the $R \\to Q$ path in Figure~\\ref{fig:dag}).\nTo block this path, we apply a natural language inference (NLI) gate using DeBERTa-v3-large with a bidirectional entailment threshold of 0.90: both NLI(original $\\to$ rewrite) and NLI(rewrite $\\to$ original) must exceed this value.\nBidirectional verification is essential for axes that inherently change information density (e.g., verbosity), where forward and backward entailment scores can be asymmetric.\nThis gating mechanism approximates the \\emph{do}-operator \\citep{veitch2020adapting} by ensuring that retained pairs differ only in style, not in content quality.\nWe additionally compute BERTScore as a supplementary monitoring metric, but it does not participate in the gating decision.\n\n\\subsection{Measurement Protocol}\n\\label{sec:measurement}\n\nEach pair that passes the NLI gate is evaluated by GPT-4o (\\texttt{gpt-4o-2024-08-06}) under two complementary scoring modes.\nIn Likert mode, the judge assigns an integer score from 1 to 10 for overall quality to each text independently.\nIn pairwise mode, the judge receives both texts as candidates A and B and makes a forced choice of which response is better.\n\nTo control for position bias, each pairwise comparison is evaluated twice with the presentation order swapped, which produces $n_{\\text{pairs}} \\times 2$ observations.\nWe apply two analysis strategies to these data.\nFor the nonparametric sign test, we retain only \\emph{consistent} pairs where the judge selected the same text in both orderings.\nFor the Bradley-Terry model, we use all observations including inconsistent pairs, as the model naturally accommodates noise in individual comparisons.\n\n\\subsection{Causal Framework}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260521T025540",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/method.tex",
    "old_string": "% TODO: Full method description (pipeline overview, style-controlled rewriting, NLI gating, pairwise comparison protocol)\n\n\\subsection{Causal Framework}",
    "new_string": "\\subsection{Style-Controlled Rewriting}\n\\label{sec:rewriting}\n\nWe isolate the causal effect of individual style attributes on judge scores by generating text pairs that differ along exactly one style axis.\nGiven an input text, an instruction-tuned LLM (Qwen3-32B, temperature 0.7) rewrites it according to an axis-specific prompt (e.g., ``Rewrite the following text to be more formal/casual while preserving the exact same content and meaning'').\nFor each axis, we produce both a forward rewrite (original $\\to$ target style) and a backward rewrite (target $\\to$ original style) to form a symmetric pair.\nThis bidirectional design controls for asymmetric effects: a text shortened for conciseness may lose information that an expansion would not.\nEach operation constitutes a binary intervention on a single style variable while all other axes remain fixed (Section~\\ref{sec:causal_framework}).\n\n\\subsection{Content Preservation Verification}\n\\label{sec:nli_gate}\n\nStyle-controlled rewriting risks altering semantic content, which would confound the style effect with a content quality effect (the $R \\to Q$ path in Figure~\\ref{fig:dag}).\nTo block this path, we apply a natural language inference (NLI) gate using DeBERTa-v3-large with a bidirectional entailment threshold of 0.90: both NLI(original $\\to$ rewrite) and NLI(rewrite $\\to$ original) must exceed this value.\nBidirectional verification is essential for axes that inherently change information density (e.g., verbosity), where forward and backward entailment scores can be asymmetric.\nThis gating mechanism approximates the \\emph{do}-operator \\citep{veitch2020adapting} by ensuring that retained pairs differ only in style, not in content quality.\nWe additionally compute BERTScore as a supplementary monitoring metric, but it does not participate in the gating decision.\n\n\\subsection{Measurement Protocol}\n\\label{sec:measurement}\n\nEach pair that passes the NLI gate is evaluated by GPT-4o (\\texttt{gpt-4o-2024-08-06}) under two complementary scoring modes.\nIn Likert mode, the judge assigns an integer score from 1 to 10 for overall quality to each text independently.\nIn pairwise mode, the judge receives both texts as candidates A and B and makes a forced choice of which response is better.\n\nTo control for position bias, each pairwise comparison is evaluated twice with the presentation order swapped, which produces $n_{\\text{pairs}} \\times 2$ observations.\nWe apply two analysis strategies to these data.\nFor the nonparametric sign test, we retain only \\emph{consistent} pairs where the judge selected the same text in both orderings.\nFor the Bradley-Terry model, we use all observations including inconsistent pairs, as the model naturally accommodates noise in individual comparisons.\n\n\\subsection{Causal Framework}"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-21T02:57:28.950025+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/method.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260521T025540",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-21T02:57:28.950165+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260521T025540",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-21T02:57:28.950338+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Style-Controlled Rewriting}
5	\label{sec:rewriting}
6	
7	We isolate the causal effect of individual style attributes on judge scores by generating text pairs that differ along exactly one style axis.
8	Given an input text, an instruction-tuned LLM (Qwen3-32B, temperature 0.7) rewrites it according to an axis-specific prompt (e.g., ``Rewrite the following text to be more formal/casual while preserving the exact same content and meaning'').
9	For each axis, we produce both a forward rewrite (original $\to$ target style) and a backward rewrite (target $\to$ original style) to form a symmetric pair.
10	This bidirectional design controls for asymmetric effects: a text shortened for conciseness may lose information that an expansion would not.
11	Each operation constitutes a binary intervention on a single style variable while all other axes remain fixed (Section~\ref{sec:causal_framework}).
12	
13	\subsection{Content Preservation Verification}
14	\label{sec:nli_gate}
15	
16	Style-controlled rewriting risks altering semantic content, which would confound the style effect with a content quality effect (the $R \to Q$ path in Figure~\ref{fig:dag}).
17	To block this path, we apply a natural language inference (NLI) gate using DeBERTa-v3-large with a bidirectional entailment threshold of 0.90: both NLI(original $\to$ rewrite) and NLI(rewrite $\to$ original) must exceed this value.
18	Bidirectional verification is essential for axes that inherently change information density (e.g., verbosity), where forward and backward entailment scores can be asymmetric.
19	This gating mechanism approximates the \emph{do}-operator \citep{veitch2020adapting} by ensuring that retained pairs differ only in style, not in content quality.
20	We additionally compute BERTScore as a supplementary monitoring metric, but it does not participate in the gating decision.
21	
22	\subsection{Measurement Protocol}
23	\label{sec:measurement}
24	
25	Each
…[truncated 3376 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260521T025540",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-21T02:57:28.950534+00:00_

已插入 §3.1 Style-Controlled Rewriting、§3.2 Content Preservation Verification、§3.3 Measurement Protocol。§3.4 Causal Framework 保持不变。所有技术细节（Qwen3-32B、NLI 0.90 双向阈值、BERTScore 仅监控、双模式评估、position swap、consistency filter vs Bradley-Terry 分流）均已覆盖。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_writing_method_20260521T025540"
}
```

</details>

---
