# paper writing method

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 0
- **Tool calls:** 5
- **Original source:** `logs/chats/worker_paper_writing_method_20260522T145638.jsonl`
- **Structured JSON:** [`f77c7b46218edc283a8b.json`](../../sessions/f7/f77c7b46218edc283a8b.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

11 recorded events

### Tool call

_source line 1 · 2026-05-22T14:58:16.356880+00:00_

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
  "session": "worker_paper_writing_method_20260522T145638",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-22T14:58:16.357662+00:00_

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
  "session": "worker_paper_writing_method_20260522T145638",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-22T14:58:16.357898+00:00_

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
  "session": "worker_paper_writing_method_20260522T145638",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-22T14:58:16.358277+00:00_

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
  "session": "worker_paper_writing_method_20260522T145638",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-22T14:58:16.358458+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260522T145638",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-22T14:58:16.358664+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Models.}
8	We probe two instruction-tuned models with comparable parameter counts but distinct architectures: Llama-3.1-8B-Instruct (32 layers, hidden dimension 4096) \citep{grattafiori2024llama} and Qwen3-8B (36 layers, hidden dimension 4096) \citep{yang2024qwen25}.
9	
10	\paragraph{Dataset.}
11	We use ConflictQA \citep{xie2024adaptive}, a benchmark of context-parametric knowledge conflicts where a provided context contradicts the model's parametric knowledge.
12	After verifying that each model can correctly answer the parametric-knowledge question without context, we retain 1{,}368 samples for Llama (1{,}096 train / 272 test) and 966 samples for Qwen (773 train / 193 test), split 80/20 with stratification.
13	
14	\paragraph{Translation.}
15	We translate all English contexts and questions into Chinese using a Qwen3-8B translation pipeline (EN$\to$ZH), with quality validated by COMET \citep{rei2020comet} back-translation scores.
16	
17	\paragraph{Probing.}
18	For each layer $l$, we train a logistic regression probe on the last-token residual stream representation $\mathbf{h}_l$, with binary labels indicating whether the model chose the contextual or parametric answer.
19	We report balanced accuracy to account for class imbalance.
20	All confidence intervals (CIs) are computed via bootstrap resampling with paired differences for asymmetry estimation.
21	
22	\paragraph{Non-conflict baseline.}
23	To test whether cross-lingual transfer patterns are specific to knowledge conflicts, we run the same probing pipeline on XNLI \citep{conneau2018xnli}, classifying entailment versus contradiction.
24	
25	\subsection{Within-Language Conflict Detection}
26	\label{sec:within_lang}
27	
28	Table~\ref{tab:main_results} reports balanced accuracy for all probe transfer directions.
29	Both models encode linearly detectable conflict signals in their residual streams.
…[truncated 9669 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260522T145638",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-22T14:58:16.358882+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/sections/",
  "description": "List paper sections directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260522T145638",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/sections/",
    "description": "List paper sections directory"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-22T14:58:16.359025+00:00_

experiments.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260522T145638",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-22T14:58:16.359179+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/sections/method.tex",
  "content": "\\section{Method}\n\\label{sec:method}\n\nFigure~\\ref{fig:pipeline} illustrates the complete pipeline, from data construction through probing and steering.\nWe first formalize the task (\\S\\ref{sec:task}), then describe data construction (\\S\\ref{sec:data}), activation extraction (\\S\\ref{sec:extraction}), the probing framework (\\S\\ref{sec:probing}), cross-lingual transfer protocol (\\S\\ref{sec:transfer}), confound exclusion (\\S\\ref{sec:confound_method}), and representation steering (\\S\\ref{sec:steering_method}).\n\n\\subsection{Task Formulation}\n\\label{sec:task}\n\nGiven an input $x = (c, q)$ consisting of a context passage $c$ and a question $q$, the model produces an answer $a$ that is either \\emph{contextual} (derived from $c$) or \\emph{parametric} (derived from the model's pre-trained knowledge).\nWhen $c$ contradicts the model's parametric knowledge, the choice between these two answer sources constitutes a knowledge conflict.\nLet $\\mathbf{h}_l \\in \\mathbb{R}^d$ denote the residual stream representation at layer $l$ for the last input token.\nOur goal is to train a logistic regression probe $f_\\theta(\\mathbf{h}_l)$ that predicts a binary label $y \\in \\{\\text{contextual}, \\text{parametric}\\}$ from $\\mathbf{h}_l$, and to examine whether the learned probe direction transfers across languages and causally influences model behavior.\n\n\\subsection{Data Construction}\n\\label{sec:data}\n\n\\paragraph{Source dataset.}\nWe build on ConflictQA \\citep{xie2024adaptive}, a benchmark that pairs each question with a context passage that contradicts the model's parametric knowledge.\nEach sample contains a question, a parametric answer (ground truth from the model's training data), and a context-based answer (the contradicting information in the passage).\n\n\\paragraph{Parametric knowledge verification.}\nNot all samples in ConflictQA produce genuine conflicts for a given model: if the model cannot answer the question correctly without context, there is no parametric knowledge to conflict with.\nWe filter samples by first querying each model without context and retaining only those where the model produces the correct parametric answer.\nThis verification step yields 1{,}368 samples for Llama-3.1-8B-Instruct \\citep{grattafiori2024llama} and 966 for Qwen3-8B \\citep{yang2024qwen25}.\nWe split each set 80/20 with stratification by label, producing 1{,}096 train / 272 test for Llama and 773 train / 193 test for Qwen.\n\n\\paragraph{Translation.}\nTo study cross-lingual transfer, we translate all English contexts and questions into Chinese (EN$\\to$ZH) using a Qwen3-8B translation pipeline.\nWe validate translation quality with COMET \\citep{rei2020comet} back-translation scores: each Chinese translation is back-translated to English, and the COMET score between the original and back-translated English text serves as a quality measure.\nThis score is later used for confound analysis (\\S\\ref{sec:confound_method}).\n\n\\subsection{Activation Extraction}\n\\label{sec:extraction}\n\nFor each model, we construct two language versions of every input: an English version (EN context + EN question) and a Chinese version (ZH context + ZH question).\nWe pass each version through the model and extract the last-token residual stream representation $\\mathbf{h}_l \\in \\mathbb{R}^d$ at every layer $l \\in \\{0, \\ldots, L-1\\}$, where $L$ is the total number of layers (32 for Llama, 36 for Qwen) and $d = 4096$ for both models.\nThe last token is chosen because autoregressive models aggregate information into the final position before generating the next token \\citep{belinkov2022probing}.\nWe then record the model's predicted answer for each input and assign the binary label $y$: contextual if the model chose the context-based answer, parametric otherwise.\n\n\\subsection{Probing Framework}\n\\label{sec:probing}\n\nAt each layer $l$, we train a logistic regression classifier with $L_2$ regularization on the extracted representations $\\{\\mathbf{h}_l^{(i)}, y^{(i)}\\}_{i=1}^{N_\\text{train}}$ \\citep{belinkov2022probing, hewitt2019designing}.\nThe probe $f_\\theta(\\mathbf{h}_l) = \\sigma(\\mathbf{w}_l^\\top \\mathbf{h}_l + b_l)$ outputs the probability of the contextual class, where $\\mathbf{w}_l \\in \\mathbb{R}^d$ is the weight vector and $b_l$ is the bias.\nWe evaluate with balanced accuracy (the macro-average of per-class recall) to account for class imbalance.\nWe report the peak-layer accuracy, defined as the maximum balanced accuracy across all layers, as the primary metric for each probe transfer direction.\n\nConfidence intervals (CIs) are estimated via bootstrap resampling \\citep{ulmer2022deep}.\nFor each bootstrap iteration, we resample the test set with replacement, compute balanced accuracy, and derive 95\\% CIs from the empirical distribution.\nFor asymmetry estimation, we use paired bootstrap differences (described in \\S\\ref{sec:transfer}).\n\n\\subsection{Cross-Lingual Transfer Protocol}\n\\label{sec:transfer}\n\nWe evaluate probes in four transfer directions: EN$\\to$EN (train and test on English activations), ZH$\\to$ZH (train and test on Chinese), EN$\\to$ZH (train on English, test on Chinese), and ZH$\\to$EN (train on Chinese, test on English).\nThe within-language directions (EN$\\to$EN, ZH$\\to$ZH) establish upper bounds, while the cross-lingual directions test whether conflict representations share structure across languages.\n\nTo quantify the directional asymmetry between the two cross-lingual directions, we define:\n\\begin{equation}\n\\Delta_{\\text{asym}} = \\text{acc}(\\text{ZH}{\\to}\\text{EN}) - \\text{acc}(\\text{EN}{\\to}\\text{ZH})\n\\label{eq:asymmetry}\n\\end{equation}\nA positive $\\Delta_{\\text{asym}}$ indicates that Chinese-trained probes transfer to English more readily than the reverse.\nWe compute $\\Delta_{\\text{asym}}$ via paired bootstrap: in each iteration, the same resampled test indices are used for both directions, and the paired difference eliminates sample-level variance.\nWe report the mean and 95\\% CI of the bootstrap distribution.\n\n\\subsection{Confound Exclusion}\n\\label{sec:confound_method}\n\nCross-lingual probe transfer could reflect artifacts of translation quality or lexical overlap rather than shared representations.\nWe design two controls to exclude these confounds.\n\n\\paragraph{COMET tercile ablation.}\nWe stratify test samples into terciles by their COMET back-translation score (high, medium, low quality) and compare probe accuracy across strata.\nIf translation quality drove transfer, high-quality translations would yield higher probe accuracy.\nWe test this with Fisher's exact test on the accuracy difference between the top and bottom terciles.\n\n\\paragraph{Token overlap analysis.}\nDespite the large typographic distance between English and Chinese, some tokens (numbers, proper nouns, punctuation) may be shared after subword tokenization.\nWe compute the per-sample Jaccard similarity between the English and Chinese token sets and test for correlation with probe accuracy via Pearson's $r$.\nA positive correlation would suggest that shared tokens, rather than shared representations, drive transfer.\n\n\\paragraph{Non-conflict baseline.}\nTo test whether cross-lingual transfer asymmetry is specific to knowledge conflicts, we apply the same probing pipeline to XNLI \\citep{conneau2018xnli}, classifying entailment versus contradiction.\nIf the asymmetry pattern ($\\Delta_{\\text{asym}} > 0$) also appears in a non-conflict task, it reflects a general cross-lingual property rather than a conflict-specific phenomenon.\n\n\\subsection{Representation Steering}\n\\label{sec:steering_method}\n\nProbing establishes that conflict signals are linearly detectable, but detection does not imply causal relevance \\citep{hewitt2019designing}.\nWe test the causal role of the probe direction by injecting it into the model's forward pass during inference, following the inference-time intervention framework of \\citet{li2023iti} and \\citet{zou2023representation}.\n\n\\paragraph{Intervention procedure.}\nLet $\\mathbf{w}_{\\text{probe}}$ denote the weight vector of the logistic regression probe trained at a target layer $l$.\nDuring inference, we modify the last-token residual stream at layer $l$:\n\\begin{equation}\n\\mathbf{h}'_l = \\mathbf{h}_l + \\alpha \\cdot \\mathbf{w}_{\\text{probe}}\n\\label{eq:steering}\n\\end{equation}\nwhere $\\alpha \\in \\mathbb{R}$ is the steering magnitude.\nPositive $\\alpha$ pushes the representation toward the contextual direction; negative $\\alpha$ pushes toward the parametric direction.\n\n\\paragraph{Control condition.}\nWe replace $\\mathbf{w}_{\\text{probe}}$ with a random unit vector $\\mathbf{w}_{\\text{random}}$ of equal norm, injected with the same $\\alpha$.\nThis controls for the possibility that any perturbation of sufficient magnitude could alter model behavior.\n\n\\paragraph{Evaluation.}\nWe measure the flip rate: the fraction of test samples that switch answer category (parametric $\\leftrightarrow$ contextual) after intervention.\nWe compare steering and control flip rates with Fisher's exact test, applying Bonferroni correction for multiple comparisons across layers and $\\alpha$ values.\nWe test at three layers spanning different depths: L13 (41\\% depth), L18 (56\\% depth), and L28 (88\\% depth, the probing accuracy peak).\nThe steering magnitude $\\alpha$ is swept over $\\{-20, -10, -5, +2, +5, +10, +20\\}$ to characterize the effective range.\nIf the probe direction is causally relevant, the steering flip rate should significantly exceed the control, and the direction of flips (parametric-to-contextual vs.\\ contextual-to-parametric) should be consistent with the sign of $\\alpha$.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260522T145638",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/sections/method.tex",
    "content": "\\section{Method}\n\\label{sec:method}\n\nFigure~\\ref{fig:pipeline} illustrates the complete pipeline, from data construction through probing and steering.\nWe first formalize the task (\\S\\ref{sec:task}), then describe data construction (\\S\\ref{sec:data}), activation extraction (\\S\\ref{sec:extraction}), the probing framework (\\S\\ref{sec:probing}), cross-lingual transfer protocol (\\S\\ref{sec:transfer}), confound exclusion (\\S\\ref{sec:confound_method}), and representation steering (\\S\\ref{sec:steering_method}).\n\n\\subsection{Task Formulation}\n\\label{sec:task}\n\nGiven an input $x = (c, q)$ consisting of a context passage $c$ and a question $q$, the model produces an answer $a$ that is either \\emph{contextual} (derived from $c$) or \\emph{parametric} (derived from the model's pre-trained knowledge).\nWhen $c$ contradicts the model's parametric knowledge, the choice between these two answer sources constitutes a knowledge conflict.\nLet $\\mathbf{h}_l \\in \\mathbb{R}^d$ denote the residual stream representation at layer $l$ for the last input token.\nOur goal is to train a logistic regression probe $f_\\theta(\\mathbf{h}_l)$ that predicts a binary label $y \\in \\{\\text{contextual}, \\text{parametric}\\}$ from $\\mathbf{h}_l$, and to examine whether the learned probe direction transfers across languages and causally influences model behavior.\n\n\\subsection{Data Construction}\n\\label{sec:data}\n\n\\paragraph{Source dataset.}\nWe build on ConflictQA \\citep{xie2024adaptive}, a benchmark that pairs each question with a context passage that contradicts the model's parametric knowledge.\nEach sample contains a question, a parametric answer (ground truth from the model's training data), and a context-based answer (the contradicting information in the passage).\n\n\\paragraph{Parametric knowledge verification.}\nNot all samples in ConflictQA produce genuine conflicts for a given model: if the model cannot answer the question correctly without context, there is no parametric knowledge to conflict with.\nWe filter samples by first querying each model without context and retaining only those where the model produces the correct parametric answer.\nThis verification step yields 1{,}368 samples for Llama-3.1-8B-Instruct \\citep{grattafiori2024llama} and 966 for Qwen3-8B \\citep{yang2024qwen25}.\nWe split each set 80/20 with stratification by label, producing 1{,}096 train / 272 test for Llama and 773 train / 193 test for Qwen.\n\n\\paragraph{Translation.}\nTo study cross-lingual transfer, we translate all English contexts and questions into Chinese (EN$\\to$ZH) using a Qwen3-8B translation pipeline.\nWe validate translation quality with COMET \\citep{rei2020comet} back-translation scores: each Chinese translation is back-translated to English, and the COMET score between the original and back-translated English text serves as a quality measure.\nThis score is later used for confound analysis (\\S\\ref{sec:confound_method}).\n\n\\subsection{Activation Extraction}\n\\label{sec:extraction}\n\nFor each model, we construct two language versions of every input: an English version (EN context + EN question) and a Chinese version (ZH context + ZH question).\nWe pass each version through the model and extract the last-token residual stream representation $\\mathbf{h}_l \\in \\mathbb{R}^d$ at every layer $l \\in \\{0, \\ldots, L-1\\}$, where $L$ is the total number of layers (32 for Llama, 36 for Qwen) and $d = 4096$ for both models.\nThe last token is chosen because autoregressive models aggregate information into the final position before generating the next token \\citep{belinkov2022probing}.\nWe then record the model's predicted answer for each input and assign the binary label $y$: contextual if the model chose the context-based answer, parametric otherwise.\n\n\\subsection{Probing Framework}\n\\label{sec:probing}\n\nAt each layer $l$, we train a logistic regression classifier with $L_2$ regularization on the extracted representations $\\{\\mathbf{h}_l^{(i)}, y^{(i)}\\}_{i=1}^{N_\\text{train}}$ \\citep{belinkov2022probing, hewitt2019designing}.\nThe probe $f_\\theta(\\mathbf{h}_l) = \\sigma(\\mathbf{w}_l^\\top \\mathbf{h}_l + b_l)$ outputs the probability of the contextual class, where $\\mathbf{w}_l \\in \\mathbb{R}^d$ is the weight vector and $b_l$ is the bias.\nWe evaluate with balanced accuracy (the macro-average of per-class recall) to account for class imbalance.\nWe report the peak-layer accuracy, defined as the maximum balanced accuracy across all layers, as the primary metric for each probe transfer direction.\n\nConfidence intervals (CIs) are estimated via bootstrap resampling \\citep{ulmer2022deep}.\nFor each bootstrap iteration, we resample the test set with replacement, compute balanced accuracy, and derive 95\\% CIs from the empirical distribution.\nFor asymmetry estimation, we use paired bootstrap differences (described in \\S\\ref{sec:transfer}).\n\n\\subsection{Cross-Lingual Transfer Protocol}\n\\label{sec:transfer}\n\nWe evaluate probes in four transfer directions: EN$\\to$EN (train and test on English activations), ZH$\\to$ZH (train and test on Chinese), EN$\\to$ZH (train on English, test on Chinese), and ZH$\\to$EN (train on Chinese, test on English).\nThe within-language directions (EN$\\to$EN, ZH$\\to$ZH) establish upper bounds, while the cross-lingual directions test whether conflict representations share structure across languages.\n\nTo quantify the directional asymmetry between the two cross-lingual directions, we define:\n\\begin{equation}\n\\Delta_{\\text{asym}} = \\text{acc}(\\text{ZH}{\\to}\\text{EN}) - \\text{acc}(\\text{EN}{\\to}\\text{ZH})\n\\label{eq:asymmetry}\n\\end{equation}\nA positive $\\Delta_{\\text{asym}}$ indicates that Chinese-trained probes transfer to English more readily than the reverse.\nWe compute $\\Delta_{\\text{asym}}$ via paired bootstrap: in each iteration, the same resampled test indices are used for both directions, and the paired difference eliminates sample-level variance.\nWe report the mean and 95\\% CI of the bootstrap distribution.\n\n\\subsection{Confound Exclusion}\n\\label{sec:confound_method}\n\nCross-lingual probe transfer could reflect artifacts of translation quality or lexical overlap rather than shared representations.\nWe design two controls to exclude these confounds.\n\n\\paragraph{COMET tercile ablation.}\nWe stratify test samples into terciles by their COMET back-translation score (high, medium, low quality) and compare probe accuracy across strata.\nIf translation quality drove transfer, high-quality translations would yield higher probe accuracy.\nWe test this with Fisher's exact test on the accuracy difference between the top and bottom terciles.\n\n\\paragraph{Token overlap analysis.}\nDespite the large typographic distance between English and Chinese, some tokens (numbers, proper nouns, punctuation) may be shared after subword tokenization.\nWe compute the per-sample Jaccard similarity between the English and Chinese token sets and test for correlation with probe accuracy via Pearson's $r$.\nA positive correlation would suggest that shared tokens, rather than shared representations, drive transfer.\n\n\\paragraph{Non-conflict baseline.}\nTo test whether cross-lingual transfer asymmetry is specific to knowledge conflicts, we apply the same probing pipeline to XNLI \\citep{conneau2018xnli}, classifying entailment versus contradiction.\nIf the asymmetry pattern ($\\Delta_{\\text{asym}} > 0$) also appears in a non-conflict task, it reflects a general cross-lingual property rather than a conflict-specific phenomenon.\n\n\\subsection{Representation Steering}\n\\label{sec:steering_method}\n\nProbing establishes that conflict signals are linearly detectable, but detection does not imply causal relevance \\citep{hewitt2019designing}.\nWe test the causal role of the probe direction by injecting it into the model's forward pass during inference, following the inference-time intervention framework of \\citet{li2023iti} and \\citet{zou2023representation}.\n\n\\paragraph{Intervention procedure.}\nLet $\\mathbf{w}_{\\text{probe}}$ denote the weight vector of the logistic regression probe trained at a target layer $l$.\nDuring inference, we modify the last-token residual stream at layer $l$:\n\\begin{equation}\n\\mathbf{h}'_l = \\mathbf{h}_l + \\alpha \\cdot \\mathbf{w}_{\\text{probe}}\n\\label{eq:steering}\n\\end{equation}\nwhere $\\alpha \\in \\mathbb{R}$ is the steering magnitude.\nPositive $\\alpha$ pushes the representation toward the contextual direction; negative $\\alpha$ pushes toward the parametric direction.\n\n\\paragraph{Control condition.}\nWe replace $\\mathbf{w}_{\\text{probe}}$ with a random unit vector $\\mathbf{w}_{\\text{random}}$ of equal norm, injected with the same $\\alpha$.\nThis controls for the possibility that any perturbation of sufficient magnitude could alter model behavior.\n\n\\paragraph{Evaluation.}\nWe measure the flip rate: the fraction of test samples that switch answer category (parametric $\\leftrightarrow$ contextual) after intervention.\nWe compare steering and control flip rates with Fisher's exact test, applying Bonferroni correction for multiple comparisons across layers and $\\alpha$ values.\nWe test at three layers spanning different depths: L13 (41\\% depth), L18 (56\\% depth), and L28 (88\\% depth, the probing accuracy peak).\nThe steering magnitude $\\alpha$ is swept over $\\{-20, -10, -5, +2, +5, +10, +20\\}$ to characterize the effective range.\nIf the probe direction is causally relevant, the steering flip rate should significantly exceed the control, and the direction of flips (parametric-to-contextual vs.\\ contextual-to-parametric) should be consistent with the sign of $\\alpha$.\n"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-22T14:58:16.359402+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/sections/method.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260522T145638",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-22T14:58:16.359560+00:00_

Method section written to `method.tex`. Key design choices:

- All symbols ($\mathbf{h}_l$, $f_\theta$, $\mathbf{w}_{\text{probe}}$, $\Delta_{\text{asym}}$, $\alpha$) defined at first use, consistent with Experiments section notation
- Citations use `\citep{}` with the specified bib keys; `\citet{}` only for inline author references (Li et al., Zou et al.)
- No em-dash, no -ing phrase endings, no banned transition words
- ~1200 words, 7 subsections matching the outline
- Figure~\ref{fig:pipeline} referenced in the opening sentence
- Equations numbered for cross-referencing (Eq.~\ref{eq:asymmetry}, Eq.~\ref{eq:steering})
- Layer/depth conventions match Experiments (L13/41%, L18/56%, L28/88%)
- Data splits match exactly (1,368/966, 80/20 stratified)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_writing_method_20260522T145638"
}
```

</details>

---
