# paper writing related work

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 31
- **Recorded user turns:** 0
- **Tool calls:** 15
- **Original source:** `logs/chats/worker_paper_writing_related_work_20260521T051915.jsonl`
- **Structured JSON:** [`8a1dbeebb17397239332.json`](../../sessions/8a/8a1dbeebb17397239332.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

31 recorded events

### Tool call

_source line 1 · 2026-05-21T05:21:38.105025+00:00_

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
  "session": "worker_paper_writing_related_work_20260521T051915",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-21T05:21:38.106005+00:00_

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
  "session": "worker_paper_writing_related_work_20260521T051915",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-21T05:21:38.106272+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260521T051915",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.bib",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-21T05:21:38.106437+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260521T051915",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-21T05:21:38.106571+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/related_work*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260521T051915",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/related_work*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-21T05:21:38.106705+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260521T051915",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-21T05:21:38.106898+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260521T051915",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.bib",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-21T05:21:38.107063+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260521T051915",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-21T05:21:38.107191+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260521T051915",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-21T05:21:38.107316+00:00_

docs/paper/theory.tex
docs/paper/experiments.tex
docs/paper/method.tex
docs/paper/introduction.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260521T051915",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-21T05:21:38.107438+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260521T051915",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.bib",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-21T05:21:38.107558+00:00_

artifacts/dream_reports/dream_20260521T032758/median/references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260521T051915",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-21T05:21:38.107681+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/introduction.tex",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260521T051915",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/introduction.tex",
    "limit": "80"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-21T05:21:38.108019+00:00_

1	\section{Introduction}
2	\label{sec:intro}
3	
4	Large language models (LLMs) now routinely replace human annotators in computational social science (CSS), producing labels for sentiment, hate speech, stance, and political discourse at costs orders of magnitude below manual coding~\cite{gilardi2023chatgpt,tornberg2024chatgpt,ziems2024nlp}.
5	Yet these annotations are not uniformly accurate.
6	\citet{ashwin2025bias} document that LLM misclassification rates vary by up to 5$\times$ across demographic subgroups defined by refugee status, gender, and education level.
7	When such annotations serve as effect modifiers in heterogeneous treatment effect (HTE) analysis, subgroup-specific errors propagate directly into conditional average treatment effect (CATE) estimates.
8	The resulting bias is not random noise that averages out; it is structured by the same demographic axes that define the research question.
9	Standard correction procedures, which estimate a single confusion matrix and apply its inverse uniformly, cannot account for this heterogeneity.
10	
11	This problem matters because HTE analysis is the primary tool for understanding how treatment effects vary across populations.
12	Subgroup CATEs inform resource allocation decisions: which communities benefit most from policy interventions, where health programs should be targeted, and how educational reforms affect different student groups.
13	Biased CATE estimates can reverse the sign of apparent treatment heterogeneity, leading practitioners to conclude that an intervention harms a subgroup it actually helps, or to allocate resources away from the communities that benefit most.
14	The failure mode is subtle: a researcher who responsibly corrects for annotation noise using a pooled confusion matrix may introduce more bias than doing nothing, precisely in the low-error subgroups where the original labels were most trustworthy.
15	The problem grows in proportion to LLM adoption.
16	As automated annotation pipelines r
…[truncated 4974 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260521T051915",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-21T05:21:38.108234+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/dream_reports/dream_20260521T032758/median/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260521T051915",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/dream_reports/dream_20260521T032758/median/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-21T05:21:38.108439+00:00_

1	@article{angelopoulos2023,
2	  title={Prediction-Powered Inference},
3	  author={Angelopoulos, Anastasios N and Bates, Stephen and Cand{\`e}s, Emmanuel J and Jordan, Michael I and Lei, Lihua},
4	  journal={Science},
5	  volume={382},
6	  number={6671},
7	  pages={669--674},
8	  year={2023}
9	}
10	
11	@inproceedings{egami2024,
12	  title={Using Imperfect Surrogates for Downstream Inference: Design-Based Supervised Learning for Social Science Applications of Large Language Models},
13	  author={Egami, Naoki and Hinck, Musashi and Stewart, Brandon and Wei, Hanying},
14	  booktitle={Advances in Neural Information Processing Systems},
15	  year={2024}
16	}
17	
18	@article{sui2026,
19	  title={Prediction-Powered Conditional Inference},
20	  author={Sui, Yizhou and others},
21	  journal={arXiv preprint},
22	  year={2026}
23	}
24	
25	@article{mozer2026,
26	  title={Arm-Specific Rectifiers for Treatment Effect Estimation under Differential Prediction Error},
27	  author={Mozer, Reagan},
28	  journal={arXiv preprint},
29	  year={2026}
30	}
31	
32	@article{ashwin2025,
33	  title={Heterogeneous Misclassification in LLM Annotations across Demographic Subgroups},
34	  author={Ashwin, Aditya and others},
35	  journal={arXiv preprint},
36	  year={2025}
37	}
38	
39	@article{gilardi2023,
40	  title={{ChatGPT} Outperforms Crowd Workers for Text-Annotation Tasks},
41	  author={Gilardi, Fabrizio and Alizadeh, Meysam and Kubli, Maël},
42	  journal={Proceedings of the National Academy of Sciences},
43	  volume={120},
44	  number={30},
45	  year={2023}
46	}
47	
48	@article{tornberg2024,
49	  title={{ChatGPT-4} Outperforms Experts and Crowd Workers in Annotating Political {Twitter} Messages with Zero-Shot Learning},
50	  author={Törnberg, Petter},
51	  journal={arXiv preprint arXiv:2304.06588},
52	  year={2024}
53	}
54	
55	@article{ziems2024,
56	  title={Can Large Language Models Transform Computational Social Science?},
57	  author={Ziems, Caleb and Held, William and Shaikh, Omar and Che
…[truncated 4151 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260521T051915",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-21T05:21:38.108593+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/theory.tex",
  "limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260521T051915",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/theory.tex",
    "limit": "30"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-21T05:21:38.108744+00:00_

1	% Requires preamble: \usepackage{amsthm,amsmath,amssymb}
2	% and: \newtheorem{theorem}{Theorem}
3	%      \newtheorem{corollary}[theorem]{Corollary}
4	%      \newtheorem{proposition}[theorem]{Proposition}
5	
6	\section{Bias Decomposition: When Debiasing Hurts}
7	\label{sec:theory}
8	
9	We formalize the bias that global misclassification correction introduces when subgroup error rates are heterogeneous.
10	Consider estimating the conditional average treatment effect (CATE) $\tau(z) = \mathbb{E}[Y(1) - Y(0) \mid Z = z]$, where $Z \in \{0, 1\}$ is a binary effect modifier observed only through a noisy annotation $\hat{Z}$.
11	The population consists of $K$ subgroups $S \in \{1, \ldots, K\}$ with weights $w_s = P(S{=}s)$, each characterized by a $2 \times 2$ confusion matrix $C_s$ with symmetric error rate $\pi_s = P(\hat{Z} \neq Z \mid S{=}s)$.
12	Standard practice estimates a single confusion matrix $\bar{C} = \sum_s w_s C_s$ from expert annotations and applies its inverse uniformly to all observations, with pooled error rate $\bar{\pi} = \sum_s w_s \pi_s$.
13	We show that when error rates vary across subgroups, this global procedure introduces a bias with an exact product form.
14	
15	We state four assumptions maintained throughout.
16	%
17	\begin{itemize}
18	\item[\textbf{(A1)}] \textit{Conditional independence:} misclassification depends only on the true label $Z$ and subgroup $S$, not on potential outcomes $Y(0), Y(1)$.
19	\item[\textbf{(A2)}] \textit{Symmetric misclassification:} $P(\hat{Z}{=}1 \mid Z{=}0, S{=}s) = P(\hat{Z}{=}0 \mid Z{=}1, S{=}s) = \pi_s$ for all $s$.
20	\item[\textbf{(A3)}] \textit{Balanced effect modifier:} $P(Z{=}0) = P(Z{=}1) = 0.5$. This simplifies the exposition; we discuss relaxation below.
21	\item[\textbf{(A4)}] \textit{Non-degeneracy:} $\pi_s \neq 0.5$ for all $s$, ensuring each $C_s$ is invertible.
22	\end{itemize}
23	
24	Under (A2)--(A3), the Bayesian mixing matrix $M_s$ (entries $M_s[\hat{z}, z] = P(Z{=}z \mid \hat{Z}{=}\hat{z}, S{
…[truncated 307 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260521T051915",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-21T05:21:38.109056+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\cite",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper",
  "output_mode": "content",
  "head_limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260521T051915",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\cite",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper",
    "output_mode": "content",
    "head_limit": "50"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-21T05:21:38.109230+00:00_

docs/paper/experiments.tex:20:To test EC-HTE under realistic conditions, we construct a semi-synthetic DGP from the TweetEval sentiment corpus~\cite{barbieri2020tweeteval}, sampling $N{=}5000$ tweets per run from a pool of 57{,}899.
docs/paper/experiments.tex:24:We set subgroup-specific misclassification rates $\pi_{S0}{=}0.05$, $\pi_{S1}{=}0.10$, $\pi_{S2}{=}0.15$, $\pi_{S3}{=}0.25$ in the extreme regime, reflecting empirical evidence that hashtag-heavy text degrades LLM classifier accuracy~\cite{ashwin2025bias}.
docs/paper/experiments.tex:32:We compare: (1) \textit{Naive} (no correction), (2) \textit{Global} (pooled confusion matrix), (3) \textit{Stratified MLE} (per-subgroup MLE without pooling), (4) \textit{HB EC-HTE} (our hierarchical Bayes estimator), (5) \textit{PPCI}~\cite{sui2026ppci}, and (6) \textit{EC-HTE+PPCI} (our combined method).
docs/paper/experiments.tex:33:For the CausalForest estimator~\cite{wager2018causal}, we also compare naive, global, and EC-HTE variants.
docs/paper/experiments.tex:63:When the downstream estimator is a CausalForest~\cite{wager2018causal} rather than difference-in-means, the bias mechanism operates with amplified magnitude.
docs/paper/experiments.tex:137:Prediction-Powered Conditional Inference~\cite{sui2026ppci} (PPCI) correct outcome-level prediction error using a small gold-standard sample but assume correct covariate labels.
docs/paper/experiments.tex:145:The two corrections are complementary rather than redundant: EC-HTE handles the structured $M^{-1}$ inversion for covariate error, while PPCI handles residual outcome-level bias through its debiasing estimator~\cite{sui2026ppci}.
docs/paper/method.tex:38:For heterogeneous treatment effect estimation, we feed corrected covariates into CausalForestDML~\cite{wager2018causal} with honest splitting.
docs/paper/method.tex:56:PPCI~\cite{sui2026ppci} corrects residual outcome bias using a debiasing estimator but assumes correct covariate labels.
docs/paper/introduction.tex:4:Lar
…[truncated 1535 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260521T051915",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-21T05:21:38.109416+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/",
  "description": "List paper directory contents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260521T051915",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/",
    "description": "List paper directory contents"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-21T05:21:38.109549+00:00_

experiments.tex
introduction.tex
method.tex
theory.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260521T051915",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-21T05:21:38.109688+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/related_work.tex",
  "content": "\\section{Related Work}\n\\label{sec:related}\n\n\\paragraph{Measurement error in regression and causal models.}\nThe classical measurement error literature establishes that naive regression with mismeasured covariates yields attenuated coefficient estimates, and that correction via estimated error models can amplify mean squared error when the error structure is misspecified~\\cite{fuller1987measurement,carroll2006measurement}.\nBayesian treatments model the measurement process jointly with the outcome, requiring informative priors when identification is weak~\\cite{gustafson2003measurement}.\nNonparametric identification results show that repeated measurements or instrumental variables can recover the true distribution without parametric assumptions on the error mechanism~\\cite{hu2008nonparametric}.\nA recurring theme is that correction helps only when the error model is well-specified; misspecified correction can perform worse than ignoring the error entirely.\nWe formalize this principle for a specific causal estimand: Theorem~\\ref{thm:bias_identity} gives an exact identity for CATE bias under global correction with heterogeneous misclassification rates, and derives the condition under which global correction amplifies rather than reduces bias.\n\n\\paragraph{Bayesian annotation models.}\n\\citet{dawid1979maximum} introduced confusion matrix estimation for multiple annotators via EM, enabling label aggregation that accounts for annotator reliability.\nExtensions incorporate item difficulty~\\cite{passonneau2014benefits}, learned annotator competence~\\cite{hovy2013learning}, and hierarchical priors that share information across annotators with varying expertise~\\cite{paun2018comparing}.\nThese models target label quality for classification tasks.\nOur hierarchical confusion matrix estimator (Section~\\ref{sec:method}) adapts this architecture to causal inference: the estimated subgroup-stratified matrices feed into CATE correction rather than label aggregation, and the prior structure is tied to the subgroup dimension that defines treatment effect heterogeneity.\n\n\\paragraph{Heterogeneous treatment effect estimation.}\nCausal forests recursively partition the covariate space to estimate conditional treatment effects with valid confidence intervals~\\cite{athey2016recursive,wager2018causal}.\nDouble/debiased machine learning provides Neyman-orthogonal moment conditions that yield root-$n$ consistent estimates robust to slow first-stage convergence~\\cite{chernozhukov2018dml}.\nDoubly-robust CATE estimators achieve minimax rates under flexible nuisance estimation~\\cite{kennedy2023dr}, and meta-learners unify several approaches within a common framework~\\cite{kunzel2019metalearners}.\nThese methods all assume that the covariates defining heterogeneity are observed without error.\nWhen the effect modifier is misclassified, the heterogeneity structure itself is distorted: observations are assigned to wrong subgroups, and the resulting CATE estimates conflate effects across groups.\nEC-HTE provides upstream correction that restores valid inputs to any of these downstream estimators (Section~\\ref{sec:method}).\n\n\\paragraph{LLMs as annotators.}\nLLMs now match or exceed crowd-worker accuracy on many text classification tasks~\\cite{gilardi2023chatgpt,tornberg2024chatgpt}, and surveys document their expanding role across computational social science~\\cite{ziems2024nlp,pangakis2023automated}.\nHowever, error rates are not uniform.\n\\citet{ashwin2025bias} show that misclassification varies by up to $5\\times$ across demographic subgroups defined by refugee status, gender, and education.\nThis heterogeneity is precisely the failure mode we address: when subgroup-varying LLM errors feed into HTE analysis, they distort the very contrasts that define the research question.\nPrior work documents these error patterns but provides no correction mechanism for downstream causal estimands.\n\n\\paragraph{Prediction-powered and design-based correction.}\nPrediction-Powered Inference (PPI) constructs valid confidence intervals for population parameters by combining a large set of ML predictions with a small gold-standard sample~\\cite{angelopoulos2023ppi}, with extensions to cross-prediction and active sampling~\\cite{zrnic2024cross}.\nDesign-based Supervised Learning (DSL) achieves similar goals through a survey-sampling framework~\\cite{egami2024dsl}.\n\\citet{mozer2026ppi} extend PPI to arm-specific correction for average treatment effects under differential prediction error.\nPPCI~\\cite{sui2026ppci} targets conditional estimands but corrects outcome-side prediction error ($\\hat{Y}$ given true $Z$), not covariate-side misclassification.\nForestIV~\\cite{bu2023forestiv} instruments for ML-predicted covariates in regression forests but targets the outcome model rather than the heterogeneity structure.\n\\citet{grimmer2022text} and \\citet{audinet2025benchmarking} provide broader methodological guidance for text-as-data pipelines without specific correction for causal heterogeneity.\nAll of these methods address either population-level correction or outcome-side error; none corrects the case where the mismeasured variable is the effect modifier whose levels index the CATE function.\n\n\\citet{imai2010causal} study misclassification of the \\textit{treatment variable}, where errors change which arm a unit is assigned to.\nTheir setting requires instrumental variables or partial identification bounds because treatment misclassification directly compromises the identification of average effects.\nOur problem is structurally distinct: the treatment is observed correctly, but the \\textit{effect modifier} that defines subgroups is misclassified.\nThis does not threaten ATE identification but distorts the heterogeneity structure, a bias that admits exact correction through subgroup-stratified confusion matrices rather than bounds.\nThe two problems share surface similarity (both involve misclassification in causal inference) but differ in which dimension is corrupted, what estimand is affected, and what correction is feasible.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260521T051915",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/related_work.tex",
    "content": "\\section{Related Work}\n\\label{sec:related}\n\n\\paragraph{Measurement error in regression and causal models.}\nThe classical measurement error literature establishes that naive regression with mismeasured covariates yields attenuated coefficient estimates, and that correction via estimated error models can amplify mean squared error when the error structure is misspecified~\\cite{fuller1987measurement,carroll2006measurement}.\nBayesian treatments model the measurement process jointly with the outcome, requiring informative priors when identification is weak~\\cite{gustafson2003measurement}.\nNonparametric identification results show that repeated measurements or instrumental variables can recover the true distribution without parametric assumptions on the error mechanism~\\cite{hu2008nonparametric}.\nA recurring theme is that correction helps only when the error model is well-specified; misspecified correction can perform worse than ignoring the error entirely.\nWe formalize this principle for a specific causal estimand: Theorem~\\ref{thm:bias_identity} gives an exact identity for CATE bias under global correction with heterogeneous misclassification rates, and derives the condition under which global correction amplifies rather than reduces bias.\n\n\\paragraph{Bayesian annotation models.}\n\\citet{dawid1979maximum} introduced confusion matrix estimation for multiple annotators via EM, enabling label aggregation that accounts for annotator reliability.\nExtensions incorporate item difficulty~\\cite{passonneau2014benefits}, learned annotator competence~\\cite{hovy2013learning}, and hierarchical priors that share information across annotators with varying expertise~\\cite{paun2018comparing}.\nThese models target label quality for classification tasks.\nOur hierarchical confusion matrix estimator (Section~\\ref{sec:method}) adapts this architecture to causal inference: the estimated subgroup-stratified matrices feed into CATE correction rather than label aggregation, and the prior structure is tied to the subgroup dimension that defines treatment effect heterogeneity.\n\n\\paragraph{Heterogeneous treatment effect estimation.}\nCausal forests recursively partition the covariate space to estimate conditional treatment effects with valid confidence intervals~\\cite{athey2016recursive,wager2018causal}.\nDouble/debiased machine learning provides Neyman-orthogonal moment conditions that yield root-$n$ consistent estimates robust to slow first-stage convergence~\\cite{chernozhukov2018dml}.\nDoubly-robust CATE estimators achieve minimax rates under flexible nuisance estimation~\\cite{kennedy2023dr}, and meta-learners unify several approaches within a common framework~\\cite{kunzel2019metalearners}.\nThese methods all assume that the covariates defining heterogeneity are observed without error.\nWhen the effect modifier is misclassified, the heterogeneity structure itself is distorted: observations are assigned to wrong subgroups, and the resulting CATE estimates conflate effects across groups.\nEC-HTE provides upstream correction that restores valid inputs to any of these downstream estimators (Section~\\ref{sec:method}).\n\n\\paragraph{LLMs as annotators.}\nLLMs now match or exceed crowd-worker accuracy on many text classification tasks~\\cite{gilardi2023chatgpt,tornberg2024chatgpt}, and surveys document their expanding role across computational social science~\\cite{ziems2024nlp,pangakis2023automated}.\nHowever, error rates are not uniform.\n\\citet{ashwin2025bias} show that misclassification varies by up to $5\\times$ across demographic subgroups defined by refugee status, gender, and education.\nThis heterogeneity is precisely the failure mode we address: when subgroup-varying LLM errors feed into HTE analysis, they distort the very contrasts that define the research question.\nPrior work documents these error patterns but provides no correction mechanism for downstream causal estimands.\n\n\\paragraph{Prediction-powered and design-based correction.}\nPrediction-Powered Inference (PPI) constructs valid confidence intervals for population parameters by combining a large set of ML predictions with a small gold-standard sample~\\cite{angelopoulos2023ppi}, with extensions to cross-prediction and active sampling~\\cite{zrnic2024cross}.\nDesign-based Supervised Learning (DSL) achieves similar goals through a survey-sampling framework~\\cite{egami2024dsl}.\n\\citet{mozer2026ppi} extend PPI to arm-specific correction for average treatment effects under differential prediction error.\nPPCI~\\cite{sui2026ppci} targets conditional estimands but corrects outcome-side prediction error ($\\hat{Y}$ given true $Z$), not covariate-side misclassification.\nForestIV~\\cite{bu2023forestiv} instruments for ML-predicted covariates in regression forests but targets the outcome model rather than the heterogeneity structure.\n\\citet{grimmer2022text} and \\citet{audinet2025benchmarking} provide broader methodological guidance for text-as-data pipelines without specific correction for causal heterogeneity.\nAll of these methods address either population-level correction or outcome-side error; none corrects the case where the mismeasured variable is the effect modifier whose levels index the CATE function.\n\n\\citet{imai2010causal} study misclassification of the \\textit{treatment variable}, where errors change which arm a unit is assigned to.\nTheir setting requires instrumental variables or partial identification bounds because treatment misclassification directly compromises the identification of average effects.\nOur problem is structurally distinct: the treatment is observed correctly, but the \\textit{effect modifier} that defines subgroups is misclassified.\nThis does not threaten ATE identification but distorts the heterogeneity structure, a bias that admits exact correction through subgroup-stratified confusion matrices rather than bounds.\nThe two problems share surface similarity (both involve misclassification in causal inference) but differ in which dimension is corrupted, what estimand is affected, and what correction is feasible.\n"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-21T05:21:38.109948+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/related_work.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260521T051915",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-21T05:21:38.110124+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "wc -w /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/related_work.tex",
  "description": "Count words in related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260521T051915",
  "tool": "Bash",
  "tool_args": {
    "command": "wc -w /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/related_work.tex",
    "description": "Count words in related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-21T05:21:38.110257+00:00_

678 /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/related_work.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260521T051915",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-21T05:21:38.110387+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -n \"—\\|–\" /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/related_work.tex",
  "description": "Check for em-dashes and en-dashes"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260521T051915",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -n \"—\\|–\" /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/related_work.tex",
    "description": "Check for em-dashes and en-dashes"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-21T05:21:38.110514+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260521T051915",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-21T05:21:38.110635+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -n \"ing\\.\" /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/related_work.tex | grep -v \"\\\\\\\\cite\\|label\\|section\\|sampling\\|splitting\"",
  "description": "Check for -ing phrase sentence endings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260521T051915",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -n \"ing\\.\" /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/related_work.tex | grep -v \"\\\\\\\\cite\\|label\\|section\\|sampling\\|splitting\"",
    "description": "Check for -ing phrase sentence endings"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-21T05:21:38.110755+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260521T051915",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-21T05:21:38.110972+00:00_

678 words (includes LaTeX commands; prose is ~600). No em-dashes, no en-dashes, no -ing phrase endings.

Written to `/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/related_work.tex`. Five clusters as specified, with a dedicated Imai & Yamamoto paragraph distinguishing treatment-variable misclassification from effect-modifier misclassification. Cross-references to `Theorem~\ref{thm:bias_identity}` and `Section~\ref{sec:method}` included.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_writing_related_work_20260521T051915"
}
```

</details>

---
