# paper writing abstract

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 0
- **Tool calls:** 5
- **Original source:** `logs/chats/worker_paper_writing_abstract_20260519T200353.jsonl`
- **Structured JSON:** [`d580bdc0895f3111fc53.json`](../../sessions/d5/d580bdc0895f3111fc53.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

11 recorded events

### Tool call

_source line 1 · 2026-05-19T20:05:02.500272+00:00_

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
  "session": "worker_paper_writing_abstract_20260519T200353",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-19T20:05:02.500873+00:00_

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
  "session": "worker_paper_writing_abstract_20260519T200353",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-19T20:05:02.501078+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_abstract_20260519T200353",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-19T20:05:02.501269+00:00_

1	\section{Introduction}
2	
3	When attention layers are added to three different recurrent architectures, their LAMBADA performance becomes near-identical: cross-architecture standard deviation drops from 0.024 to 0.005, a 79\% reduction. Yet this aggregate convergence hides an asymmetry at the per-example level. The three architectures reach similar overall accuracy by helping and hurting almost entirely different examples, with pairwise Jaccard similarity below 0.10. Two models can agree on a benchmark score while disagreeing on which inputs they get right. This tension between aggregate agreement and per-example disagreement arises in the context of a rapid architectural shift toward hybrid recurrent-attention models, which interleave attention layers within linear recurrent backbones. Jamba \citep{lieber2024jamba} combines Mamba layers with Transformer blocks; Griffin \citep{de2024griffin} mixes gated linear recurrences with local attention; RWKV-6 \citep{peng2024eagle} integrates matrix-valued states with attention-like mechanisms; RecurrentGemma \citep{botev2024recurrentgemma} pairs linear recurrences with sliding-window attention. These systems now serve as production-grade alternatives to pure Transformers, and the practical question of how much attention to include is typically answered by comparing aggregate benchmark numbers. \citet{wang2025hybrid} provide a controlled model zoo spanning three recurrent architectures, five attention ratios, and two parameter scales, which enables systematic study of how attention allocation affects these hybrid designs.
4	
5	Most evaluations of hybrid architectures compare aggregate benchmark scores and report that a given attention ratio achieves a certain accuracy averaged across tasks or averaged across architectures. This practice can mask substantial per-example behavioral diversity. \citet{damour2022underspecification} showed that models with equivalent held-out performance can disagree on individual predictions, a 
…[truncated 5586 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_abstract_20260519T200353",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-19T20:05:02.501423+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/experiments.tex",
  "limit": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_abstract_20260519T200353",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/experiments.tex",
    "limit": "20"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-19T20:05:02.501671+00:00_

1	\section{Experiments}\label{sec:experiments}
2	
3	We analyze how attention affects cross-architecture performance variance using models from the hybrid recurrent model zoo of \citet{wang2025hybrid}. Our analysis spans three architectures (GatedDeltaNet, RetNet, HGRN2), five attention ratios (0\% pure recurrent, 4\%, 7.7\%, 14.3\%, 25\%), and two scales (340M and 1.3B parameters). In the h$k$-1 notation used throughout, one attention layer is interleaved per every $k{+}1$ layers; h3-1 denotes 25\% attention. All models within each scale share identical training data and hyperparameters; they differ only in architecture and attention configuration. We evaluate on 10 benchmarks spanning retrieval, comprehension, reasoning, and mixed task categories, plus one supplementary benchmark (COPA, $n = 100$).
4	
5	\subsection{Task-Specific Convergence}\label{ssec:task_convergence}
6	
7	We first ask whether adding attention layers reduces performance differences between architectures, and whether any such reduction is uniform across tasks. For each benchmark, we compute the cross-architecture standard deviation ($\sigma$) at each attention ratio and measure the Spearman rank correlation ($\rho$) between attention ratio and $\sigma$ across the five configurations.
8	
9	Table~\ref{tab:convergence} reports results for all benchmarks at 1.3B scale. LAMBADA is the only benchmark exhibiting monotonic convergence: $\rho = -1.0$ (exact permutation test, $p = .017$, two-tailed, $n = 5$, 120 permutations). Cross-architecture $\sigma$ drops from 0.024 to 0.005, a 79\% reduction. The 95\% BCa percentile bootstrap confidence interval for $\rho$ is $[-1.0, -0.7]$ (10{,}000 resamples), which excludes zero. After Bonferroni correction for six pre-registered benchmarks, the adjusted $p = .100$ does not survive strict Bonferroni correction at $\alpha = 0.05$. We therefore treat the confidence interval, rather than the corrected $p$-value, as the primary evidence for the LAMBADA convergence effe
…[truncated 1802 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_abstract_20260519T200353",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-19T20:05:02.501874+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_abstract_20260519T200353",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-19T20:05:02.502034+00:00_

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
13	\usepackage{amsmath}
14	\usepackage{multirow}
15	\usepackage{xcolor}
16	
17	\title{Aggregate Convergence, Per-Example Divergence: Decoupled Effects of Attention in Hybrid Recurrent Architectures}
18	
19	\author{Anonymous}
20	
21	\begin{document}
22	\maketitle
23	
24	\begin{abstract}
25	% TODO: Step 4 - abstract (last in writing order)
26	\end{abstract}
27	
28	\input{sections/introduction}
29	
30	\input{sections/related_work}
31	
32	\input{sections/method}
33	
34	\input{sections/experiments}
35	
36	\input{sections/conclusion}
37	
38	\section*{Limitations}
39	
40	Our analysis has several limitations that constrain the scope of its conclusions.
41	
42	\paragraph{Statistical power.} With only $n = 5$ attention ratios, the minimum achievable two-tailed $p$-value under an exact permutation test is approximately 0.008. This ceiling limits our ability to detect weak convergence effects and contributes to the Bonferroni-adjusted $p = .100$ for LAMBADA not reaching conventional significance. We report confidence intervals as primary evidence to partially address this constraint.
43	
44	\paragraph{Per-example scope.} Our per-example decomposition is limited to LAMBADA, the only benchmark with statistically supported convergence. Extending helped/hurt analysis to benchmarks without convergence would not test the central claim, but examining per-example effects on tasks with moderate but non-significant convergence (e.g., ARC-Easy, MMLU) could reveal whether the decoupling pattern generalizes.
45	
46	\paragraph{Scale coverage.} We compare two scale points (340M and 1.3B parameters). The contrast between complete convergence at 1.3B and partial convergence at 340M is a binary observation, not a scaling law. Inte
…[truncated 1253 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_abstract_20260519T200353",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-19T20:05:02.502248+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/main.tex",
  "old_string": "\\begin{abstract}\n% TODO: Step 4 - abstract (last in writing order)\n\\end{abstract}",
  "new_string": "\\begin{abstract}\nHybrid recurrent architectures that interleave attention layers with linear recurrence are increasingly standard, yet how attention affects per-example behavior across different recurrent backbones remains poorly quantified. We conduct a systematic analysis using the controlled model zoo of \\citet{wang2025hybrid}: three architectures (GatedDeltaNet, RetNet, HGRN2) at five attention ratios and two scales (340M and 1.3B parameters), evaluated on 10 benchmarks with 5{,}153 per-example comparisons on LAMBADA. Of the 10 benchmarks, only LAMBADA exhibits cross-architecture convergence ($\\rho = -1.0$, BCa 95\\% CI $[-1.0, -0.7]$; cross-architecture standard deviation drops 79\\%). The Bonferroni-adjusted $p = .100$ does not survive strict correction; the confidence interval serves as primary evidence. This convergence is complete at 1.3B but partial and non-monotonic at 340M; sufficient scale appears necessary for full equalization. Despite aggregate convergence, per-example helped and hurt sets are nearly disjoint across architectures (Jaccard similarity $< 0.10$), and this overlap saturates at minimal (4\\%) attention. Aggregate performance equalizes progressively, while per-example specificity is fixed from the earliest attention allocation. These results quantify underspecification in hybrid architecture design: aggregate equivalence does not imply per-example behavioral interchangeability.\n\\end{abstract}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_abstract_20260519T200353",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/main.tex",
    "old_string": "\\begin{abstract}\n% TODO: Step 4 - abstract (last in writing order)\n\\end{abstract}",
    "new_string": "\\begin{abstract}\nHybrid recurrent architectures that interleave attention layers with linear recurrence are increasingly standard, yet how attention affects per-example behavior across different recurrent backbones remains poorly quantified. We conduct a systematic analysis using the controlled model zoo of \\citet{wang2025hybrid}: three architectures (GatedDeltaNet, RetNet, HGRN2) at five attention ratios and two scales (340M and 1.3B parameters), evaluated on 10 benchmarks with 5{,}153 per-example comparisons on LAMBADA. Of the 10 benchmarks, only LAMBADA exhibits cross-architecture convergence ($\\rho = -1.0$, BCa 95\\% CI $[-1.0, -0.7]$; cross-architecture standard deviation drops 79\\%). The Bonferroni-adjusted $p = .100$ does not survive strict correction; the confidence interval serves as primary evidence. This convergence is complete at 1.3B but partial and non-monotonic at 340M; sufficient scale appears necessary for full equalization. Despite aggregate convergence, per-example helped and hurt sets are nearly disjoint across architectures (Jaccard similarity $< 0.10$), and this overlap saturates at minimal (4\\%) attention. Aggregate performance equalizes progressively, while per-example specificity is fixed from the earliest attention allocation. These results quantify underspecification in hybrid architecture design: aggregate equivalence does not imply per-example behavioral interchangeability.\n\\end{abstract}"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-19T20:05:02.502424+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/main.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_abstract_20260519T200353",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-19T20:05:02.502582+00:00_

Abstract 已写入 `main.tex`。180 words，四段结构完整：问题定位 → 方法 → 三项发现（含全部关键数字）→ 启示。无禁用词，无 em-dash，无 -ing 结尾短语。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_writing_abstract_20260519T200353"
}
```

</details>

---
