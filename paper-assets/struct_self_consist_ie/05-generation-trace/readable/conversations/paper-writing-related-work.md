# paper writing related work

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 15
- **Recorded user turns:** 0
- **Tool calls:** 7
- **Original source:** `logs/chats/worker_paper_writing_related_work_20260514T202951.jsonl`
- **Structured JSON:** [`17b5d9e9214892f5ddc9.json`](../../sessions/17/17b5d9e9214892f5ddc9.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

15 recorded events

### Tool call

_source line 1 · 2026-05-14T20:31:30.668756+00:00_

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
  "session": "worker_paper_writing_related_work_20260514T202951",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-14T20:31:30.669440+00:00_

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
  "session": "worker_paper_writing_related_work_20260514T202951",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-14T20:31:30.669659+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260514T202951",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-14T20:31:30.669848+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Self-consistency---sampling multiple outputs and aggregating them---has become a powerful strategy for improving language model reasoning.
4	On discrete-answer tasks such as arithmetic and commonsense QA, majority voting over chain-of-thought samples yields large gains: +18 percentage points on GSM8K \cite{wang2023selfconsistency}.
5	More broadly, test-time compute scaling through repeated sampling and selection has emerged as a complementary axis to model scaling, offering substantial quality improvements at inference time \cite{snell2024scaling, brown2024monkeys}.
6	These results rest on a shared assumption: that among $N$ stochastic samples, a selection mechanism can identify better outputs.
7	For tasks with a single correct answer, this assumption holds naturally---the majority vote is the selector.
8	But information extraction (IE) poses a fundamentally different challenge.
9	The output is not a single token or number; it is a \textit{set} of entities or relations with internal dependencies, where two samples may extract overlapping but non-identical structures.
10	There is no obvious majority to vote on, partial agreement is the norm rather than the exception, and the space of valid outputs is combinatorially large.
11	Can self-consistency still provide useful signal in this structured setting?
12	
13	Prior work on confidence estimation for LLM-based IE has conflated two distinct objectives.
14	\textit{Quality estimation} asks which inputs the model handles reliably---a ranking over instances.
15	\textit{Sample selection} asks which of $N$ candidate outputs is best for a given input---a ranking over samples.
16	These require fundamentally different signal properties: the former benefits from instance-level aggregation across all $N$ samples, while the latter demands per-sample discrimination.
17	Existing evaluations rarely separate the two.
18	Self-consistency methods designed for discrete answers \cite{wan
…[truncated 4392 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260514T202951",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-14T20:31:30.670014+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260514T202951",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-14T20:31:30.670255+00:00_

1	\section{Method}\label{sec:method}
2	
3	We present a framework for evaluating confidence signals in test-time scaling for information extraction.
4	This section formalizes the problem (\S\ref{sec:formulation}), defines five confidence signals spanning three families (\S\ref{sec:signals}), and introduces the evaluation protocol (\S\ref{sec:evaluation}).
5	
6	\subsection{Problem Formulation}\label{sec:formulation}
7	
8	Given a language model $\mathcal{M}$ and an input instance $x$, we independently sample $N$ structured outputs $\{y_1, \ldots, y_N\}$ at temperature $T > 0$.
9	Each $y_i$ is a structured extraction result---an entity set for NER or a relation set for RE---produced via constrained decoding \cite{willard2023guided} to ensure valid output structure.
10	Our goal is to define a confidence signal $c$ that serves two purposes: (a) \textit{quality estimation}---predicting which instances the model handles reliably, and (b) \textit{sample selection}---identifying the best output among the $N$ candidates.
11	
12	A key distinction underlies this framework.
13	A \textbf{per-sample signal} scores each $y_i$ independently, $c_{\text{ps}}: (x, y_i) \to \mathbb{R}$, enabling direct ranking of the $N$ candidates.
14	An \textbf{instance-level signal} aggregates over all $N$ samples, $c_{\text{il}}: (x, \{y_i\}_{i=1}^N) \to \mathbb{R}$, producing a single score per input.
15	Instance-level signals can estimate overall prediction reliability but do not inherently rank individual samples.
16	This asymmetry---between predicting \textit{which inputs} are easy and selecting \textit{which output} is best---is central to the correlation-selection gap we investigate.
17	
18	Table~\ref{tab:notation} summarizes our notation.
19	
20	\begin{table}[h]
21	\centering
22	\small
23	\begin{tabular}{cl}
24	\toprule
25	Symbol & Meaning \\
26	\midrule
27	$\mathcal{M}$ & Language model \\
28	$x$ & Input instance \\
29	$y_i$ & $i$-th stochastic sample \\
30	$N$ & Number of samples \\
31	$T$ &
…[truncated 6724 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260514T202951",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-14T20:31:30.670478+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/",
  "description": "List paper sections directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260514T202951",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/",
    "description": "List paper sections directory"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-14T20:31:30.670610+00:00_

total 48
drwxr-xr-x 2 ubuntu ubuntu  4096 May 14 20:28 .
drwxr-xr-x 4 ubuntu ubuntu  4096 May 14 19:51 ..
-rw-r--r-- 1 ubuntu ubuntu 18603 May 14 20:28 experiments.tex
-rw-r--r-- 1 ubuntu ubuntu  6245 May 14 20:10 introduction.tex
-rw-r--r-- 1 ubuntu ubuntu  8336 May 14 19:41 method.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260514T202951",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-14T20:31:30.670754+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex",
  "content": "\\section{Related Work}\\label{sec:related}\n\nOur work connects three research threads: self-consistency and test-time scaling methods developed for reasoning tasks, confidence estimation for structured information extraction, and broader uncertainty quantification for language models.\n\n\\subsection{Self-Consistency and Test-Time Scaling}\n\n\\paragraph{Self-consistency for discrete and free-form tasks.}\nSelf-consistency decoding \\cite{wang2023selfconsistency} improves chain-of-thought reasoning by sampling multiple rationales and selecting the most frequent answer via majority vote.\nThis paradigm assumes a discrete answer space where outputs can be grouped by equivalence and counted---an assumption that holds for arithmetic, commonsense QA, and similar tasks but breaks for set-valued structured outputs.\n\\citet{chen2024usc} extend self-consistency to free-form text generation by replacing exact matching with LLM-based semantic comparison, while SelfCheckGPT \\cite{manakul2023selfcheckgpt} leverages cross-sample consistency to detect hallucinations in open-ended generation.\n\\citet{thirukovalluru2024atomic} decompose long-form outputs into atomic sub-claims and measure per-claim consistency, moving beyond whole-output comparison.\nThese methods operate on text-level equivalence or entailment; our work instead compares \\textit{structured sets} of entities and relations, requiring set-theoretic similarity measures that account for partial overlap, type constraints, and span-level matching.\n\n\\paragraph{Test-time scaling and sample selection.}\nA growing body of work studies how to allocate additional compute at inference time.\n\\citet{snell2024scaling} characterize the scaling laws governing test-time compute, showing that repeated sampling with effective selection can substitute for model scaling.\n\\citet{brown2024monkeys} demonstrate that best-of-$N$ sampling with large $N$ yields substantial gains across diverse tasks.\nSeveral recent methods aim to improve selection without trained reward models.\nCISC \\cite{taubenfeld2025cisc} combines confidence scores with majority voting, weighting each sample's contribution to the consensus.\nSelf-Certainty \\cite{kang2025selfcertainty} uses KL divergence between a sample's token distribution and the prior to select high-quality outputs, demonstrating that reward-free selection is viable for mathematical reasoning.\nReASC \\cite{kim2026reasc} adaptively adjusts the number of samples based on estimated difficulty, while \\citet{wang2025rankedvoting} replace plurality voting with ranked aggregation, and \\citet{oh2025latentsc} perform consistency estimation in latent space rather than output space.\n\nAll of these methods target reasoning and QA tasks with discrete or near-discrete answer spaces.\nOur work is, to our knowledge, the first to extend self-consistency to set-valued structured outputs in IE, and the first to identify the correlation-selection gap: strong quality estimation ($\\rho{=}0.50$) coexists with selection failure (no gain over greedy on NER).\nIn direct dialogue with \\citet{kang2025selfcertainty}, who show that reward-free selection succeeds for reasoning, our results demonstrate that this success does not transfer to structured extraction, where the combinatorial output space and instance-level nature of consistency signals preclude effective per-sample discrimination.\n\n\\subsection{Consistency and Confidence for Structured IE}\n\nThe most directly relevant prior work is \\citet{nedellec2026consistency}, who study consistency--accuracy correlations in hard-prompted LLMs for NER and relation extraction on plant-health data.\nTheir findings corroborate our quality-estimation results: higher inter-sample consistency predicts higher extraction accuracy.\nHowever, three key limitations motivate our work.\nFirst, they rely on surface-level string matching and explicitly acknowledge that their approach ``overlooks semantically consistent outputs''---precisely the gap our Soft Jaccard signal addresses through type-aware bipartite matching with span overlap.\nSecond, they do not study best-of-$N$ selection, leaving the quality-estimation-to-selection transfer question unexamined.\nThird, their evaluation covers a single domain with hard-prompted (temperature-zero) generation and no comparison across signal families.\nOur work extends their analysis to multi-domain benchmarks, temperature-based sampling, and a systematic five-signal comparison that reveals when structural signals outperform surface alternatives and vice versa.\n\nCoCoA \\cite{vashurin2025cocoa} proposes a minimum Bayes risk framework that fuses model confidence with inter-sample consistency for uncertainty quantification on QA, summarization, and translation.\nTheir confidence-consistency ensemble parallels our analysis of signal combinations, but they do not address structured extraction, where the unit of comparison shifts from text sequences to entity and relation sets.\n\nOur evaluation setting---LLMs performing IE as a generation task---builds on a line of work establishing generative approaches to entity and relation extraction.\nUniNER \\cite{zhou2024uniner} and GoLLIE \\cite{sainz2024gollie} train universal IE models via instruction tuning; \\citet{wadhwa2023revisiting} and InstructUIE \\cite{wang2023instructuie} demonstrate that instruction-following LLMs can perform extraction zero-shot or with minimal supervision; GenIE \\cite{josifoski2022genie} and CodeIE \\cite{li2023codeie} frame IE as constrained sequence generation.\nWe adopt constrained decoding \\cite{willard2023guided} following this paradigm and study confidence estimation as an orthogonal dimension: given that LLMs generate structured outputs, how reliably can we estimate extraction quality from multiple samples?\n\n\\subsection{Uncertainty Estimation and Calibration}\n\n\\paragraph{Confidence and uncertainty for LLMs.}\nSeveral surveys chart the landscape of confidence estimation \\cite{geng2024confidence}, selective abstention \\cite{wen2025know}, uncertainty quantification \\cite{xia2025survey}, and their intersection with calibration \\cite{hobelsberger2025systematic}.\nOur work bridges confidence estimation and selective prediction: we use confidence signals not only to rank instances by reliability but also to attempt best-of-$N$ selection, revealing that these two objectives impose different requirements on the underlying signal.\n\nSemantic uncertainty \\cite{kuhn2023semantic} clusters generations by meaning rather than surface form and estimates uncertainty from cluster statistics.\n\\citet{kossen2024semantic} distill semantic entropy into lightweight probes, and P(True) \\cite{kadavath2022language} directly queries the model for its confidence.\nThese approaches measure uncertainty over the model's belief distribution; our structural signals instead measure agreement over output \\textit{structure}, comparing extracted entity sets rather than semantic content of free-form text.\n\n\\paragraph{Calibration and ensembles.}\nModern neural networks are often miscalibrated \\cite{guo2017calibration}, and calibration techniques for pre-trained language models \\cite{desai2020calibration} aim to align predicted probabilities with empirical accuracy.\nOur reliability diagrams assess whether confidence signals are calibrated for IE, extending calibration analysis beyond classification to structured prediction.\nDeep ensembles \\cite{lakshminarayanan2017ensembles} and MC-dropout \\cite{gal2016dropout} obtain uncertainty from model variation, requiring multiple forward passes through different model parameters.\nOur multi-sample approach is conceptually related---we also use variation across stochastic outputs---but requires no model modification or access to internal parameters beyond token log-probabilities, operating entirely post-hoc on generated outputs.\n\n\\paragraph{Uncertainty for token-level and span-level NER.}\nPrior work on NER uncertainty operates within discriminative, pre-LLM paradigms: \\citet{xiao2019uncertainty} study Bayesian inference for sequence labeling, \\citet{shelmanov2021active} leverage uncertainty for active learning in NER, and \\citet{zhang2023ener} estimate entity-level uncertainty from span probabilities.\nThese methods assume access to per-token classification logits from a discriminative model.\nIn the generative LLM setting we study, entity boundaries are implicit in the decoded text and uncertainty must be estimated from the generation process itself.\n\n\\paragraph{Related paradigms.}\nConformal prediction \\cite{fisch2021conformal, angelopoulos2021conformal} provides distribution-free coverage guarantees but targets prediction sets rather than quality ranking.\nTrained verifiers \\cite{cobbe2021verifiers, lightman2024verify} and reward models \\cite{wang2024mathshepherd} learn to score outputs from labeled data; we focus on unsupervised signals that require no additional training.\nSelective prediction \\cite{geifman2017selective} and confidence-based IE filtering \\cite{culotta2004confidence} establish the broader framework of abstaining when uncertain; our contribution is characterizing which confidence signals support this objective for generative IE and where the quality-estimation-to-selection transfer breaks down.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260514T202951",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex",
    "content": "\\section{Related Work}\\label{sec:related}\n\nOur work connects three research threads: self-consistency and test-time scaling methods developed for reasoning tasks, confidence estimation for structured information extraction, and broader uncertainty quantification for language models.\n\n\\subsection{Self-Consistency and Test-Time Scaling}\n\n\\paragraph{Self-consistency for discrete and free-form tasks.}\nSelf-consistency decoding \\cite{wang2023selfconsistency} improves chain-of-thought reasoning by sampling multiple rationales and selecting the most frequent answer via majority vote.\nThis paradigm assumes a discrete answer space where outputs can be grouped by equivalence and counted---an assumption that holds for arithmetic, commonsense QA, and similar tasks but breaks for set-valued structured outputs.\n\\citet{chen2024usc} extend self-consistency to free-form text generation by replacing exact matching with LLM-based semantic comparison, while SelfCheckGPT \\cite{manakul2023selfcheckgpt} leverages cross-sample consistency to detect hallucinations in open-ended generation.\n\\citet{thirukovalluru2024atomic} decompose long-form outputs into atomic sub-claims and measure per-claim consistency, moving beyond whole-output comparison.\nThese methods operate on text-level equivalence or entailment; our work instead compares \\textit{structured sets} of entities and relations, requiring set-theoretic similarity measures that account for partial overlap, type constraints, and span-level matching.\n\n\\paragraph{Test-time scaling and sample selection.}\nA growing body of work studies how to allocate additional compute at inference time.\n\\citet{snell2024scaling} characterize the scaling laws governing test-time compute, showing that repeated sampling with effective selection can substitute for model scaling.\n\\citet{brown2024monkeys} demonstrate that best-of-$N$ sampling with large $N$ yields substantial gains across diverse tasks.\nSeveral recent methods aim to improve selection without trained reward models.\nCISC \\cite{taubenfeld2025cisc} combines confidence scores with majority voting, weighting each sample's contribution to the consensus.\nSelf-Certainty \\cite{kang2025selfcertainty} uses KL divergence between a sample's token distribution and the prior to select high-quality outputs, demonstrating that reward-free selection is viable for mathematical reasoning.\nReASC \\cite{kim2026reasc} adaptively adjusts the number of samples based on estimated difficulty, while \\citet{wang2025rankedvoting} replace plurality voting with ranked aggregation, and \\citet{oh2025latentsc} perform consistency estimation in latent space rather than output space.\n\nAll of these methods target reasoning and QA tasks with discrete or near-discrete answer spaces.\nOur work is, to our knowledge, the first to extend self-consistency to set-valued structured outputs in IE, and the first to identify the correlation-selection gap: strong quality estimation ($\\rho{=}0.50$) coexists with selection failure (no gain over greedy on NER).\nIn direct dialogue with \\citet{kang2025selfcertainty}, who show that reward-free selection succeeds for reasoning, our results demonstrate that this success does not transfer to structured extraction, where the combinatorial output space and instance-level nature of consistency signals preclude effective per-sample discrimination.\n\n\\subsection{Consistency and Confidence for Structured IE}\n\nThe most directly relevant prior work is \\citet{nedellec2026consistency}, who study consistency--accuracy correlations in hard-prompted LLMs for NER and relation extraction on plant-health data.\nTheir findings corroborate our quality-estimation results: higher inter-sample consistency predicts higher extraction accuracy.\nHowever, three key limitations motivate our work.\nFirst, they rely on surface-level string matching and explicitly acknowledge that their approach ``overlooks semantically consistent outputs''---precisely the gap our Soft Jaccard signal addresses through type-aware bipartite matching with span overlap.\nSecond, they do not study best-of-$N$ selection, leaving the quality-estimation-to-selection transfer question unexamined.\nThird, their evaluation covers a single domain with hard-prompted (temperature-zero) generation and no comparison across signal families.\nOur work extends their analysis to multi-domain benchmarks, temperature-based sampling, and a systematic five-signal comparison that reveals when structural signals outperform surface alternatives and vice versa.\n\nCoCoA \\cite{vashurin2025cocoa} proposes a minimum Bayes risk framework that fuses model confidence with inter-sample consistency for uncertainty quantification on QA, summarization, and translation.\nTheir confidence-consistency ensemble parallels our analysis of signal combinations, but they do not address structured extraction, where the unit of comparison shifts from text sequences to entity and relation sets.\n\nOur evaluation setting---LLMs performing IE as a generation task---builds on a line of work establishing generative approaches to entity and relation extraction.\nUniNER \\cite{zhou2024uniner} and GoLLIE \\cite{sainz2024gollie} train universal IE models via instruction tuning; \\citet{wadhwa2023revisiting} and InstructUIE \\cite{wang2023instructuie} demonstrate that instruction-following LLMs can perform extraction zero-shot or with minimal supervision; GenIE \\cite{josifoski2022genie} and CodeIE \\cite{li2023codeie} frame IE as constrained sequence generation.\nWe adopt constrained decoding \\cite{willard2023guided} following this paradigm and study confidence estimation as an orthogonal dimension: given that LLMs generate structured outputs, how reliably can we estimate extraction quality from multiple samples?\n\n\\subsection{Uncertainty Estimation and Calibration}\n\n\\paragraph{Confidence and uncertainty for LLMs.}\nSeveral surveys chart the landscape of confidence estimation \\cite{geng2024confidence}, selective abstention \\cite{wen2025know}, uncertainty quantification \\cite{xia2025survey}, and their intersection with calibration \\cite{hobelsberger2025systematic}.\nOur work bridges confidence estimation and selective prediction: we use confidence signals not only to rank instances by reliability but also to attempt best-of-$N$ selection, revealing that these two objectives impose different requirements on the underlying signal.\n\nSemantic uncertainty \\cite{kuhn2023semantic} clusters generations by meaning rather than surface form and estimates uncertainty from cluster statistics.\n\\citet{kossen2024semantic} distill semantic entropy into lightweight probes, and P(True) \\cite{kadavath2022language} directly queries the model for its confidence.\nThese approaches measure uncertainty over the model's belief distribution; our structural signals instead measure agreement over output \\textit{structure}, comparing extracted entity sets rather than semantic content of free-form text.\n\n\\paragraph{Calibration and ensembles.}\nModern neural networks are often miscalibrated \\cite{guo2017calibration}, and calibration techniques for pre-trained language models \\cite{desai2020calibration} aim to align predicted probabilities with empirical accuracy.\nOur reliability diagrams assess whether confidence signals are calibrated for IE, extending calibration analysis beyond classification to structured prediction.\nDeep ensembles \\cite{lakshminarayanan2017ensembles} and MC-dropout \\cite{gal2016dropout} obtain uncertainty from model variation, requiring multiple forward passes through different model parameters.\nOur multi-sample approach is conceptually related---we also use variation across stochastic outputs---but requires no model modification or access to internal parameters beyond token log-probabilities, operating entirely post-hoc on generated outputs.\n\n\\paragraph{Uncertainty for token-level and span-level NER.}\nPrior work on NER uncertainty operates within discriminative, pre-LLM paradigms: \\citet{xiao2019uncertainty} study Bayesian inference for sequence labeling, \\citet{shelmanov2021active} leverage uncertainty for active learning in NER, and \\citet{zhang2023ener} estimate entity-level uncertainty from span probabilities.\nThese methods assume access to per-token classification logits from a discriminative model.\nIn the generative LLM setting we study, entity boundaries are implicit in the decoded text and uncertainty must be estimated from the generation process itself.\n\n\\paragraph{Related paradigms.}\nConformal prediction \\cite{fisch2021conformal, angelopoulos2021conformal} provides distribution-free coverage guarantees but targets prediction sets rather than quality ranking.\nTrained verifiers \\cite{cobbe2021verifiers, lightman2024verify} and reward models \\cite{wang2024mathshepherd} learn to score outputs from labeled data; we focus on unsupervised signals that require no additional training.\nSelective prediction \\cite{geifman2017selective} and confidence-based IE filtering \\cite{culotta2004confidence} establish the broader framework of abstaining when uncertain; our contribution is characterizing which confidence signals support this objective for generative IE and where the quality-estimation-to-selection transfer breaks down.\n"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-14T20:31:30.670971+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260514T202951",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-14T20:31:30.671105+00:00_

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
  "session": "worker_paper_writing_related_work_20260514T202951",
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

_source line 12 · 2026-05-14T20:31:30.671250+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260514T202951",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-14T20:31:30.671371+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "related_work.tex",
  "type": "paper",
  "description": "Related Work section (§4) for struct_self_consist_ie paper, covering self-consistency/TTS, consistency for structured IE, and uncertainty estimation.",
  "project": "struct_self_consist_ie",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex",
  "tags": "['paper', 'related-work', 'latex']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260514T202951",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "related_work.tex",
    "type": "paper",
    "description": "Related Work section (§4) for struct_self_consist_ie paper, covering self-consistency/TTS, consistency for structured IE, and uncertainty estimation.",
    "project": "struct_self_consist_ie",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex",
    "tags": "['paper', 'related-work', 'latex']"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-14T20:31:30.671533+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260514_b4a7d5\", \"name\": \"related_work.tex\", \"type\": \"paper\", \"description\": \"Related Work section (§4) for struct_self_consist_ie paper, covering self-consistency/TTS, consistency for structured IE, and uncertainty estimation.\", \"path\": \"projects/struct_self_consist_ie/artifacts/_project/paper/related_work.tex\", \"url\": null, \"project\": \"struct_self_consist_ie\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-14T20:31:17.193532+00:00\", \"tags\": [\"paper\", \"related-work\", \"latex\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260514T202951",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-14T20:31:30.671702+00:00_

Related Work 章节已写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex`。

结构概要：
- **§4.1 Self-Consistency and Test-Time Scaling** (~450 words): 从 SC-CoT/USC/SelfCheckGPT 等基础方法到 CISC/Self-Certainty/ReASC 等 TTS 选择方法，明确定位我们是首个将 SC 扩展到 set-valued IE 输出的工作，并与 Kang et al. 2026 形成直接学术对话（reward-free selection 在 reasoning 上成功但在 structured IE 上失败）。
- **§4.2 Consistency and Confidence for Structured IE** (~350 words): 以 Nédellec & Xia 2026 为最直接 competitor，逐点区分（surface matching vs. SJ、无 BoN 选择、单域单信号）；CoCoA 的 confidence+consistency 融合作为并行参照；generative IE 方法（UniNER/GoLLIE/CodeIE 等）定义 evaluation setting。
- **§4.3 Uncertainty Estimation and Calibration** (~400 words): 覆盖 surveys、semantic uncertainty、calibration、ensembles/MC-dropout、token/span NER uncertainty、conformal prediction、verifiers、selective prediction，每类 1-2 句定位 + 与我们的区别。

所有 citation keys 均来自指定的 references.bib 列表，无虚构引用。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_writing_related_work_20260514T202951"
}
```

</details>

---
