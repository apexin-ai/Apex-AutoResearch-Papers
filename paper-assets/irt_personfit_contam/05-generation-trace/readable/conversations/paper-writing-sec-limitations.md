# paper writing sec limitations

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 43
- **Recorded user turns:** 0
- **Tool calls:** 21
- **Original source:** `logs/chats/worker_paper_writing_sec_limitations_20260520T235421.jsonl`
- **Structured JSON:** [`dcde897f9092c6d29aa9.json`](../../sessions/dc/dcde897f9092c6d29aa9.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

43 recorded events

### Tool call

_source line 1 · 2026-05-20T23:56:14.577528+00:00_

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
  "session": "worker_paper_writing_sec_limitations_20260520T235421",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-20T23:56:14.578085+00:00_

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
  "session": "worker_paper_writing_sec_limitations_20260520T235421",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-20T23:56:14.578281+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Explore paper sections context",
  "prompt": "I need to understand the current state of a paper in /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/. \n\n1. List all files in the paper/sections/ directory\n2. Read the main paper .tex file to understand the structure\n3. Read the introduction and method sections to understand the paper's contributions and approach\n4. Read the results/experiments section to understand what was actually done\n5. Check if there's an existing limitations.tex file\n\nFocus on understanding: what are the main contributions, what methods were used, what datasets, what models, and what results were obtained. Report back key details I'll need for writing a Limitations section."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_sec_limitations_20260520T235421",
  "tool": "Agent",
  "tool_args": {
    "subagent_type": "Explore",
    "description": "Explore paper sections context",
    "prompt": "I need to understand the current state of a paper in /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/. \n\n1. List all files in the paper/sections/ directory\n2. Read the main paper .tex file to understand the structure\n3. Read the introduction and method sections to understand the paper's contributions and approach\n4. Read the results/experiments section to understand what was actually done\n5. Check if there's an existing limitations.tex file\n\nFocus on understanding: what are the main contributions, what methods were used, what datasets, what models, and what results were obtained. Report back key details I'll need for writing a Limitations section."
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-20T23:56:14.578482+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper -type f -name \"*.tex\" | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_sec_limitations_20260520T235421",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper -type f -name \"*.tex\" | head -20"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-20T23:56:14.578620+00:00_

/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/sec_simulation.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/appendix.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/sec_setup.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/background.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/sec_empirical.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/limitations.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/sec_ctrl_contam.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/discussion.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/experiments.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/main.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_sec_limitations_20260520T235421",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-20T23:56:14.578762+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_sec_limitations_20260520T235421",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-20T23:56:14.578881+00:00_

total 72
drwxr-xr-x 2 ubuntu ubuntu 4096 May 20 23:37 .
drwxr-xr-x 3 ubuntu ubuntu 4096 May 20 22:49 ..
-rw-r--r-- 1 ubuntu ubuntu   11 May 20 22:24 abstract.tex
-rw-r--r-- 1 ubuntu ubuntu   11 May 20 22:24 appendix.tex
-rw-r--r-- 1 ubuntu ubuntu 4696 May 20 23:00 background.tex
-rw-r--r-- 1 ubuntu ubuntu   13 May 20 22:24 conclusion.tex
-rw-r--r-- 1 ubuntu ubuntu 1655 May 20 23:37 discussion.tex
-rw-r--r-- 1 ubuntu ubuntu  170 May 20 22:36 experiments.tex
-rw-r--r-- 1 ubuntu ubuntu 5510 May 20 23:33 introduction.tex
-rw-r--r-- 1 ubuntu ubuntu   14 May 20 22:24 limitations.tex
-rw-r--r-- 1 ubuntu ubuntu 6724 May 20 22:53 method.tex
-rw-r--r-- 1 ubuntu ubuntu 2944 May 20 22:55 sec_ctrl_contam.tex
-rw-r--r-- 1 ubuntu ubuntu 2781 May 20 22:49 sec_empirical.tex
-rw-r--r-- 1 ubuntu ubuntu 1287 May 20 22:49 sec_setup.tex
-rw-r--r-- 1 ubuntu ubuntu 2150 May 20 22:52 sec_simulation.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_sec_limitations_20260520T235421",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-20T23:56:14.579017+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_sec_limitations_20260520T235421",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-20T23:56:14.579142+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	\usepackage{inconsolata}
9	\usepackage{graphicx}
10	\usepackage{booktabs}
11	\usepackage{amsmath}
12	\usepackage{amssymb}
13	\usepackage{multirow}
14	\usepackage{xcolor}
15	\usepackage{subcaption}
16	
17	\graphicspath{{../figures/paper/}}
18	
19	\title{Detecting Benchmark Contamination in Large Language Models \\
20	via Item Response Theory Person-Fit Statistics}
21	
22	\author{Anonymous}
23	
24	\begin{document}
25	\maketitle
26	
27	\begin{abstract}
28	\input{sections/abstract}
29	\end{abstract}
30	
31	\input{sections/introduction}
32	\input{sections/background}
33	\input{sections/method}
34	\input{sections/experiments}
35	\input{sections/discussion}
36	
37	\section*{Limitations}
38	\input{sections/limitations}
39	
40	\bibliography{references}
41	
42	\appendix
43	\input{sections/appendix}
44	
45	\end{document}
46	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_sec_limitations_20260520T235421",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-20T23:56:14.579272+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_sec_limitations_20260520T235421",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-20T23:56:14.579426+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Benchmark contamination, the unintended inclusion of evaluation data in training corpora, poses a growing threat to the integrity of large language model (LLM) evaluation \citep{dodge2021, magar2022, sainz2023}.
4	As training corpora and public benchmarks both expand, the probability of overlap increases structurally: any model trained on broad web-crawled data may have encountered evaluation items during pretraining or fine-tuning \citep{jacovi2023, chang2024survey}.
5	When contamination occurs, benchmark scores no longer reflect genuine capability, undermining the primary mechanism by which the community compares and selects models.
6	
7	A range of detection methods have been proposed, but all require some form of privileged access beyond the binary response record.
8	N-gram overlap methods need the training corpus itself \citep{dodge2021, magar2022}.
9	Membership inference approaches such as Min-K\%++ require token-level probabilities \citep{minkprob2024, deng2024}.
10	Time Travel probing relies on crafted prompts that elicit memorized completions \citep{golchin2024, oren2024}.
11	Performance-based methods compare results across original and rephrased test variants \citep{constat2024}, and in-context learning approaches require output logits \citep{codec2026}.
12	These methods form a detection frontier ordered by information access: training data, model weights, logits, token probabilities, rephrased retests, and finally binary patterns.
13	No existing method operates at the bottom of this frontier.
14	We ask: \emph{what can be detected from binary response patterns alone?}
15	
16	The need for minimal-information detection grows more pressing as models evolve.
17	\citet{wang2025fragility} show that all ten log-probability-based detection methods they evaluate perform at chance level on reasoning models trained with reinforcement learning (RL).
18	RL fine-tuning reshapes internal token distributions while prese
…[truncated 3627 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_sec_limitations_20260520T235421",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-20T23:56:14.579582+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_sec_limitations_20260520T235421",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-20T23:56:14.579728+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{The \textsc{IRT-Fit} Framework}
5	\label{sec:framework}
6	
7	Our method takes as input a binary response matrix $\mathbf{X} \in \{0,1\}^{M \times n}$, where $M$ models answer $n$ benchmark items, together with pre-calibrated four-parameter logistic (4PL) item parameters from PSN-IRT \citep{psnirt2026}.
8	The 4PL model defines the probability that a model with ability $\theta$ answers item $i$ correctly:
9	\begin{equation}
10	  P_i(\theta) = c_i + (d_i - c_i)\,\frac{1}{1 + e^{-a_i(\theta - b_i)}}
11	  \label{eq:4pl}
12	\end{equation}
13	where $a_i$ is discrimination, $b_i$ is difficulty, $c_i$ is a lower asymptote (guessing), and $d_i$ is an upper asymptote (slip).
14	
15	The framework proceeds in three steps.
16	\textbf{Step~1}: Estimate each model's ability $\hat{\theta}$ via maximum likelihood on each benchmark separately.
17	\textbf{Step~2}: Compute the person-fit statistic $\ell_z^*$ \citep{snijders2001}, a standardized likelihood residual that quantifies how well a model's item-level response pattern conforms to the IRT model given $\hat{\theta}$.
18	The statistic extends the original $\ell_z$ \citep{drasgow1985} by correcting for estimation uncertainty in $\hat{\theta}$, so that $\ell_z^* \sim \mathcal{N}(0,1)$ under the null hypothesis.
19	\textbf{Step~3}: For within-model contamination detection, compute $\Delta\ell_z^* = \ell_z^*(\text{target}) - \ell_z^*(\text{reference})$ between a target benchmark and a reference benchmark from the same model.
20	The entire procedure is unsupervised: it requires no training data, no labeled contamination examples, and no access to pretraining corpora.
21	
22	\paragraph{Validity under assumption violations.}
23	IRT assumes local independence and unidimensionality, conditions that LLM benchmarks violate.
24	When these assumptions fail, $\ell_z^*$ can exhibit systematic bias: all models may appear aberrant even without contamination, because inter-item dependencies in
…[truncated 4946 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_sec_limitations_20260520T235421",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-20T23:56:14.579874+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/background.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_sec_limitations_20260520T235421",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/background.tex"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-20T23:56:14.580041+00:00_

1	\section{Background and Related Work}\label{sec:background}
2	
3	\subsection{IRT and Person-Fit Statistics}\label{sec:irt_background}
4	
5	Item Response Theory (IRT) models the probability that an examinee answers a test item correctly as a function of the examinee's latent ability $\theta$ and item-level parameters \citep{lord1980, embretson2000}.
6	The four-parameter logistic (4PL) model, formalized in \S\ref{sec:framework} (Eq.~\ref{eq:4pl}), extends the classical three-parameter model \citep{birnbaum1968} with an upper asymptote $d$ that captures the probability of error even at high ability \citep{barton1981}.
7	This parameter matters for LLMs: \citet{psnirt2026} find that 46\% of MMLU items have $d < 0.95$, meaning ceiling effects are pervasive and a model without the $d$ parameter systematically misestimates item characteristics.
8	
9	Given calibrated item parameters, person-fit statistics measure whether an examinee's \emph{pattern} of correct and incorrect responses is consistent with the IRT model at the estimated ability level.
10	The key intuition is that a test-taker with ability $\theta$ should get hard items wrong and easy items right at rates the model predicts; systematic deviations signal aberrant behavior.
11	\citet{drasgow1985} introduced $\ell_z$, a standardized log-likelihood residual that aggregates per-item deviations into a single score.
12	\citet{snijders2001} corrected the variance of $\ell_z$ for uncertainty in the estimated $\hat{\theta}$, yielding $\ell_z^*$ with the property that $\ell_z^* \sim \mathcal{N}(0,1)$ under the null hypothesis of model-consistent responding.
13	Negative values indicate \emph{aberrant} patterns (unexpected errors on easy items or unexpected successes on hard items), while positive values indicate \emph{over-consistent} patterns (responses too predictable given the model).
14	We defer the formal definition to \S\ref{sec:framework}.
15	
16	In psychometrics, person-fit statistics have a long history in detecti
…[truncated 2804 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_sec_limitations_20260520T235421",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-20T23:56:14.580198+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_sec_limitations_20260520T235421",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-20T23:56:14.580333+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\input{sections/sec_setup}
5	\input{sections/sec_simulation}
6	\input{sections/sec_ctrl_contam}
7	\input{sections/sec_empirical}
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_sec_limitations_20260520T235421",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-20T23:56:14.580459+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/sec_ctrl_contam.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_sec_limitations_20260520T235421",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/sec_ctrl_contam.tex"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-20T23:56:14.580586+00:00_

1	\subsection{Controlled Contamination}
2	\label{sec:ctrl_contam}
3	
4	We validate $\ell_z^*$ on MMLU with ground-truth contamination.
5	Three clean seeds yield $\ell_z^*$ values of $s_1{=}8.01$, $s_2{=}5.94$, $s_3{=}8.08$ (mean$\,{=}\,7.35\pm1.21$); $s_2$ is ${\sim}26\%$ lower than $s_1$/$s_3$, attributable to seed-specific training dynamics (Appendix~\ref{app:seed_sensitivity}).
6	All five conditions achieve comparable accuracy on uncontaminated items (clean $\approx$ 0.679), while contaminated models show overall accuracy gains (0.731 at 15\%, 0.764 at 50\%).
7	
8	\paragraph{Finding 1: Detection signal.}
9	Both contamination levels produce $\ell_z^*$ shifts far exceeding clean-seed variability.
10	At 15\% contamination, $|\text{Cohen's}\;d|{=}3.58$; at 50\%, $|d|{=}1.56$ (ddof$\,{=}\,1$, $n{=}3$ clean seeds).
11	The contamination signal exceeds the clean-clean $\Delta\ell_z^*$ noise floor (0.70) by a factor of 6.2$\times$.
12	
13	\paragraph{Finding 2: Free-$\theta$ non-monotonicity.}
14	Under free-$\theta$ estimation, dose-response is non-monotonic: $\Delta\ell_z^*{=}{-}4.34$ at 15\% versus ${-}1.90$ at 50\%.
15	The 50\% condition produces a \emph{weaker} signal than 15\% because contamination inflates $\hat{\theta}_{\text{MLE}}$, which absorbs part of the aberrance into a higher ability estimate ($\Delta\theta{=}0.29$ at 15\%, $0.47$ at 50\%).
16	
17	\paragraph{Finding 3: Fixed $\theta$ restores monotonicity.}
18	Anchoring at the pre-contamination baseline ($\theta_{\text{fixed}}{=}{-}0.0966$, mean of $n{=}3$ clean $\hat{\theta}$ estimates) restores monotonic dose-response: $\Delta\ell_{z,\text{fixed}}^*{=}2.68$ (15\%) and $8.36$ (50\%), a ratio of 3.12 (Figure~\ref{fig:ctrl_contam}, right panel).
19	
20	\paragraph{Finding 4: Memorization fingerprint.}
21	Splitting by seen/unseen items reveals a characteristic fingerprint: at 15\% contamination, memorized items yield $\ell_z^*{\approx}0$ (consistent with the model's inflated $\hat{\theta}$), while unseen items p
…[truncated 1034 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_sec_limitations_20260520T235421",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-20T23:56:14.580734+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/sec_empirical.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_sec_limitations_20260520T235421",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/sec_empirical.tex"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-20T23:56:14.580860+00:00_

1	\subsection{Empirical Findings}
2	\label{sec:empirical}
3	
4	We apply $\ell_z^*$ to 12 models across five benchmarks (60 model-benchmark cells).
5	After Benjamini--Hochberg FDR correction ($\alpha=0.05$), 57 of 60 cells are flagged as significant.
6	The three unflagged cells (Yi-Lightning$\times$ARC-C, 360GPT2-Pro$\times$HumanEval, Yi-Lightning$\times$HumanEval) all involve small benchmarks ($n \leq 295$), consistent with the power analysis in \S\ref{sec:simulation}.
7	By contrast, an accuracy $z$-score baseline flags only 4 of 60 cells: $\ell_z^*$ captures 14$\times$ more anomalies by exploiting response-pattern structure that accuracy aggregation discards.
8	This near-universal misfit indicates that real LLM response patterns systematically deviate from 4PL IRT predictions, regardless of architecture or training paradigm.
9	
10	\paragraph{12-model case study.}
11	Figure~\ref{fig:heatmap} presents the $\ell_z^*$ heatmap across 12 models and five benchmarks.
12	93.3\% of flagged cells exhibit positive $\ell_z^*$ (over-consistency): models answer too many hard items correctly relative to their estimated ability.
13	Gemini-1.5-Flash on MMLU represents an extreme case: 100\% accuracy (14{,}042/14{,}042 items correct), $\hat{\theta}=0.78$, and $\ell_z^*{=}{+}34.75$, with 50 of 57 MMLU subjects flagged individually.
14	Ward hierarchical clustering on the $\ell_z^*$ profile matrix reveals heterogeneous contamination typologies; Gemini-1.5-Flash isolates as a distinct outlier, while other models form clusters that correspond to selective versus uniform misfit.
15	Ten of 12 models are flagged on all five benchmarks simultaneously.
16	
17	\paragraph{IRT parameter estimation gap.}
18	Refitting 3PL parameters via MML-EM on the v1 leaderboard ($N{=}178$ models) recovers difficulty moderately ($r_b = 0.663$) but fails on discrimination ($r_a = 0.127$).
19	Classical IRT calibration requires sample sizes that current leaderboards cannot provide; neural calibration methods such a
…[truncated 859 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_sec_limitations_20260520T235421",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-20T23:56:14.581000+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/sec_setup.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_sec_limitations_20260520T235421",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/sec_setup.tex"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-20T23:56:14.581118+00:00_

1	\subsection{Experimental Setup}
2	\label{sec:setup}
3	
4	We evaluate on five benchmarks that span knowledge, reasoning, and code generation: MMLU \citep{hendrycks2021mmlu} (14,042 items), HellaSwag \citep{zellers2019hellaswag} (10,042), GSM8K \citep{cobbe2021gsm8k} (1,319), ARC-Challenge \citep{clark2018arc} (295), and HumanEval \citep{chen2021humaneval} (164).
5	All item parameters follow the four-parameter logistic (4PL) IRT model, calibrated by \citet{psnirt2026} from a large-scale leaderboard dataset.
6	
7	\paragraph{Empirical data.}
8	We obtain per-item binary response vectors for 12 models from the PSN-IRT v2 leaderboard dataset \citep{psnirt2026}, covering open-weight and proprietary models across capability tiers.
9	
10	\paragraph{Controlled contamination.}
11	We fine-tune Qwen2.5-7B-Instruct with QLoRA (rank\,=\,16, $\alpha$\,=\,32) under five conditions: three clean runs (seeds 42, 123, 456) and two contaminated runs where 15\% and 50\% of MMLU evaluation items are included in the supervised fine-tuning (SFT) training data.
12	
13	\paragraph{Simulation.}
14	For each benchmark, we generate 2{,}000 response-vector replicates per condition across 11 contamination levels (0\%, 3\%, 5\%, 10\%, 15\%, 25\%, 50\%, 60\%, 75\%, 90\%, 100\%), sampling responses under the calibrated 4PL parameters.
15	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_sec_limitations_20260520T235421",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-20T23:56:14.581252+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/sec_simulation.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_sec_limitations_20260520T235421",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/sec_simulation.tex"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-20T23:56:14.581397+00:00_

1	\subsection{Simulation Validation}
2	\label{sec:simulation}
3	
4	\paragraph{Null calibration.}
5	Under the null (no contamination), bootstrap $lz^*$ tracks $\mathcal{N}(0,1)$: mean bias 0.041 and standard deviation 1.003 on MMLU.
6	Kolmogorov--Smirnov rejection rates vary with benchmark size: 8.3\% for MMLU and HellaSwag ($n > 10{,}000$), 50.0\% for GSM8K ($n = 1{,}319$), 58.3\% for ARC-C ($n = 295$), and 75.0\% for HumanEval ($n = 164$).
7	$lz^*$ is well-calibrated for benchmarks with $n \geq 10{,}000$ items; smaller benchmarks show increasing finite-sample deviations from normality.
8	
9	\begin{figure}[t]
10	  \centering
11	  \includegraphics[width=\columnwidth]{fig_2_power_function.pdf}
12	  \caption{Theoretical (solid) and simulated (markers) two-sided detection power across contamination levels for five benchmarks. Power scales with $\sqrt{n}$. At contamination above 50\%, mean $lz^*$ crosses zero and shifts from negative to positive anomaly, which produces a brief power dip.}
13	  \label{fig:power}
14	\end{figure}
15	
16	\paragraph{Detection power.}
17	Two-sided testing eliminates the inverted-U artifact: MMLU achieves 97.8\% power at 15\% contamination and sustains ${>}$93\% at all levels (93.6\% at 75\%, 95.2\% at 90\%, 100\% at full contamination).
18	Power scales with $\sqrt{n}$, as predicted by the noncentrality parameter $\delta \propto \sqrt{n}$.
19	Figure~\ref{fig:power} overlays theoretical and simulated power curves; the closed-form power function, derived via Gauss--Hermite quadrature ($K=30$) over the ability distribution with the \citet{snijders2001} variance formula, achieves $R^2 = 0.9572$.
20	Practitioners can determine detection feasibility from a benchmark's item count alone.
21	
22	\paragraph{Model comparison.}
23	The 4PL model yields a mean $+$27.3pp power gain over 3PL on MMLU, $+$26.1pp on HellaSwag, and $+$20.3pp on GSM8K, as 46\% of MMLU items exhibit upper asymptote $d < 0.95$ (Appendix~\ref{app:4pl_ablation}).
24	Against supervised 
…[truncated 216 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_sec_limitations_20260520T235421",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-20T23:56:14.581541+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_sec_limitations_20260520T235421",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/limitations.tex"
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-20T23:56:14.581650+00:00_

1	% limitations
2	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_sec_limitations_20260520T235421",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-20T23:56:14.581772+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_sec_limitations_20260520T235421",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/discussion.tex"
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-20T23:56:14.581887+00:00_

1	\section{Discussion}\label{sec:discussion}
2	
3	The simulation study confirms that $\ell_z^*$ is well-calibrated under the bootstrap null (mean bias 0.041, std 1.003), yet 57 of 60 model-benchmark cells exhibit 4PL misfit in real data. This gap is not an artifact of miscalibration. LLM response patterns genuinely violate IRT assumptions such as local independence and unidimensionality, producing systematic positive $\ell_z^*$ (over-consistency) across models. The $\Delta\ell_z^*$ design turns this universal misfit into a feature: because the bias is shared across benchmarks, within-model differencing cancels it, isolating contamination-specific aberrance.
4	
5	This design enables practical deployment. PSN-IRT v1 provides over 13K per-item binary response vectors publicly~\citep{psnirt2026}, and binary response data are routinely recorded on leaderboards, so retrospective audits require no new data collection.
6	
7	Two scope boundaries deserve emphasis. First, our controlled validation uses a single model family (Qwen2.5-7B) with QLoRA (rank=16), which limits memorization capacity; the observed 38\% memorization fraction likely represents a conservative lower bound, and full fine-tuning would produce stronger signals. Second, $\Delta\ell_z^*$ targets SFT-stage contamination and leaderboard gaming rather than incidental pretraining exposure.
8	
9	Future work includes multi-family controlled contamination, large-scale leaderboard audits pending estimation advances for RL-era models~\citep{zhang2026rlvr}, and post-RL validation. The $\ell_z^*$ statistic is structurally invariant to RL distributional changes; empirical verification is future work.
10	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_sec_limitations_20260520T235421",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-20T23:56:14.582015+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_sec_limitations_20260520T235421",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/abstract.tex"
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-20T23:56:14.582122+00:00_

1	% abstract
2	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_sec_limitations_20260520T235421",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-20T23:56:14.582239+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/ | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_sec_limitations_20260520T235421",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/ | head -20"
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-20T23:56:14.582372+00:00_

total 296
drwxr-xr-x 13 ubuntu ubuntu  4096 May 20 23:53 .
drwxrwxr-x  5 ubuntu ubuntu  4096 May 20 07:09 ..
drwxr-xr-x  3 ubuntu ubuntu  4096 May 20 07:09 .claude
drwxr-xr-x  6 ubuntu ubuntu  4096 May 20 07:34 .venv
-rw-r--r--  1 ubuntu ubuntu 14170 May 20 23:53 AGENTS.md
-rw-r--r--  1 ubuntu ubuntu     0 May 20 07:12 ROADMAP.lock
-rw-------  1 ubuntu ubuntu  4431 May 20 23:22 ROADMAP.md
-rw-r--r--  1 ubuntu ubuntu    91 May 20 19:43 _last_visual_review.json
drwxr-xr-x 42 ubuntu ubuntu  4096 May 20 20:07 artifacts
drwxr-xr-x  2 ubuntu ubuntu 16384 May 20 23:18 checkpoints
-rw-r--r--  1 ubuntu ubuntu     0 May 20 07:13 decisions.lock
-rw-------  1 ubuntu ubuntu 17564 May 20 23:13 decisions.yaml
drwxr-xr-x  2 ubuntu ubuntu  4096 May 20 11:43 distill_tmp
drwxr-xr-x  4 ubuntu ubuntu  4096 May 20 07:40 docs
-rwxr-xr-x  1 ubuntu ubuntu     0 May 20 07:40 dream_registry.lock
-rw-------  1 ubuntu ubuntu  3128 May 20 19:47 dream_registry.yaml
-rw-r--r--  1 ubuntu ubuntu  3133 May 20 19:47 dream_registry.yaml.bak
-rw-r--r--  1 ubuntu ubuntu  8637 May 20 13:04 experiment_plan.yaml
drwxr-xr-x  2 ubuntu ubuntu  4096 May 20 13:29 experiments

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_sec_limitations_20260520T235421",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-20T23:56:14.582580+00:00_

Now I have a comprehensive understanding of the paper. Let me compile my findings:

## Paper Analysis Summary

I've thoroughly reviewed the paper structure and content. Here's a comprehensive summary of the key details you'll need for writing a Limitations section:

### **Paper Overview**
**Title:** "Detecting Benchmark Contamination in Large Language Models via Item Response Theory Person-Fit Statistics"

**Main Contribution:** IRT-FIT, a framework that detects benchmark contamination in LLMs using only binary response patterns (correct/incorrect), without requiring access to training data, model weights, logits, or other privileged information.

---

### **Main Contributions** (from Introduction)
1. **IRT-FIT Framework** - A person-fit analysis method requiring only binary responses and pre-calibrated item parameters, with validation showing |Cohen's d| = 3.58 at 15% contamination
2. **Power Function** - A closed-form power function (R² = 0.957) linking benchmark size to detection sensitivity; shows 80% power at 15% contamination requires ≥7,958 items
3. **Empirical Findings** - Universal 4PL model misfit (57/60 cells flagged), inadequacy of accuracy-based detection (only 4/60 cells), and identification of the θ-shift boundary condition

---

### **Core Methods & Technical Details**

**IRT Model:** Four-parameter logistic (4PL) model with:
- Discrimination (a_i), Difficulty (b_i), Lower asymptote/Guessing (c_i), Upper asymptote/Slip (d_i)
- Pre-calibrated parameters from PSN-IRT (cited as psnirt2026)
- Person-fit statistic: ℓ_z* (standardized likelihood residual)

**Detection Approach:**
- Estimate model ability θ via maximum likelihood
- Compute ℓ_z* quantifying response pattern conformance
- For within-model detection: Δℓ_z* = ℓ_z*(target) - ℓ_z*(reference) acts as difference-in-differences estimator
- Significance via nonparametric bootstrap (not asymptotic N(0,1) reference)

**Key Innovation - θ-Shift Analysis:**
- Free-θ estimation produces non-monotonic dose
…[truncated 3882 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_sec_limitations_20260520T235421",
  "tool": "Agent",
  "elapsed_ms": 4
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-20T23:56:14.582778+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "label\\{eq:power",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_sec_limitations_20260520T235421",
  "tool": "Grep",
  "tool_args": {
    "pattern": "label\\{eq:power",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-20T23:56:14.582901+00:00_

paper/sections/method.tex:58:  \label{eq:power}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_sec_limitations_20260520T235421",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-20T23:56:14.583030+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/limitations.tex",
  "content": "\\section*{Limitations}\n\nOur controlled contamination experiments use a single model family (Qwen2.5-7B-Instruct) with QLoRA fine-tuning at rank 16. The limited adapter capacity means observed memorization rates (38\\% of injected items at 15\\% contamination) likely represent a conservative lower bound; full-parameter fine-tuning would permit greater memorization and produce stronger $\\ell_z^*$ signals. Validating this expectation across multiple model families and scales remains future work.\n\nThe framework relies on pre-calibrated item parameters from PSN-IRT rather than self-calibrated parameters. Our MML-EM refit experiment reveals that discrimination recovery degrades substantially ($r_a = 0.127$) when calibrating on current leaderboard data where most models exhibit contamination-driven misfit. Until neural IRT or alternative calibration methods can handle contaminated respondent pools, the framework depends on externally maintained parameter banks.\n\nAll controlled experiments target SFT-stage contamination. While $\\ell_z^*$ is structurally invariant to post-hoc distributional changes from reinforcement learning, empirical validation on post-RL models is deferred to future work.\n\nDetection power varies with benchmark size. On ARC-Challenge (295 items), Cohen's $d = 0.45$ at 15\\% contamination, well below the $d = 3.58$ observed on MMLU (14,042 items). The closed-form power function (Equation~\\ref{eq:power}) predicts that 80\\% power at 15\\% contamination requires $\\geq$7,958 items, placing small benchmarks below reliable detection thresholds.\n\nFinally, because LLM response patterns universally violate classical IRT assumptions, absolute $\\ell_z^*$ values cannot be interpreted against standard normal thresholds. Our framework addresses this through the $\\Delta\\ell_z^*$ difference-in-differences design, but this requires a clean reference condition for each benchmark.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_sec_limitations_20260520T235421",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/limitations.tex",
    "content": "\\section*{Limitations}\n\nOur controlled contamination experiments use a single model family (Qwen2.5-7B-Instruct) with QLoRA fine-tuning at rank 16. The limited adapter capacity means observed memorization rates (38\\% of injected items at 15\\% contamination) likely represent a conservative lower bound; full-parameter fine-tuning would permit greater memorization and produce stronger $\\ell_z^*$ signals. Validating this expectation across multiple model families and scales remains future work.\n\nThe framework relies on pre-calibrated item parameters from PSN-IRT rather than self-calibrated parameters. Our MML-EM refit experiment reveals that discrimination recovery degrades substantially ($r_a = 0.127$) when calibrating on current leaderboard data where most models exhibit contamination-driven misfit. Until neural IRT or alternative calibration methods can handle contaminated respondent pools, the framework depends on externally maintained parameter banks.\n\nAll controlled experiments target SFT-stage contamination. While $\\ell_z^*$ is structurally invariant to post-hoc distributional changes from reinforcement learning, empirical validation on post-RL models is deferred to future work.\n\nDetection power varies with benchmark size. On ARC-Challenge (295 items), Cohen's $d = 0.45$ at 15\\% contamination, well below the $d = 3.58$ observed on MMLU (14,042 items). The closed-form power function (Equation~\\ref{eq:power}) predicts that 80\\% power at 15\\% contamination requires $\\geq$7,958 items, placing small benchmarks below reliable detection thresholds.\n\nFinally, because LLM response patterns universally violate classical IRT assumptions, absolute $\\ell_z^*$ values cannot be interpreted against standard normal thresholds. Our framework addresses this through the $\\Delta\\ell_z^*$ difference-in-differences design, but this requires a clean reference condition for each benchmark.\n"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-20T23:56:14.583163+00:00_

&lt;tool_use_error>File has not been read yet. Read it first before writing to it.&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_sec_limitations_20260520T235421",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-20T23:56:14.583275+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_sec_limitations_20260520T235421",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/limitations.tex"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-20T23:56:14.583407+00:00_

1	% limitations
2	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_sec_limitations_20260520T235421",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-20T23:56:14.583524+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/limitations.tex",
  "content": "\\section*{Limitations}\n\nOur controlled contamination experiments use a single model family (Qwen2.5-7B-Instruct) with QLoRA fine-tuning at rank 16. The limited adapter capacity means observed memorization rates (38\\% of injected items at 15\\% contamination) likely represent a conservative lower bound; full-parameter fine-tuning would permit greater memorization and produce stronger $\\ell_z^*$ signals. Validating this expectation across multiple model families and scales remains future work.\n\nThe framework relies on pre-calibrated item parameters from PSN-IRT rather than self-calibrated parameters. Our MML-EM refit experiment reveals that discrimination recovery degrades substantially ($r_a = 0.127$) when calibrating on current leaderboard data where most models exhibit contamination-driven misfit. Until neural IRT or alternative calibration methods can handle contaminated respondent pools, the framework depends on externally maintained parameter banks.\n\nAll controlled experiments target SFT-stage contamination. While $\\ell_z^*$ is structurally invariant to post-hoc distributional changes from reinforcement learning, empirical validation on post-RL models is deferred to future work.\n\nDetection power varies with benchmark size. On ARC-Challenge (295 items), Cohen's $d = 0.45$ at 15\\% contamination, well below the $d = 3.58$ observed on MMLU (14,042 items). The closed-form power function (Equation~\\ref{eq:power}) predicts that 80\\% power at 15\\% contamination requires $\\geq$7,958 items, placing small benchmarks below reliable detection thresholds.\n\nFinally, because LLM response patterns universally violate classical IRT assumptions, absolute $\\ell_z^*$ values cannot be interpreted against standard normal thresholds. Our framework addresses this through the $\\Delta\\ell_z^*$ difference-in-differences design, but this requires a clean reference condition for each benchmark.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_sec_limitations_20260520T235421",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/limitations.tex",
    "content": "\\section*{Limitations}\n\nOur controlled contamination experiments use a single model family (Qwen2.5-7B-Instruct) with QLoRA fine-tuning at rank 16. The limited adapter capacity means observed memorization rates (38\\% of injected items at 15\\% contamination) likely represent a conservative lower bound; full-parameter fine-tuning would permit greater memorization and produce stronger $\\ell_z^*$ signals. Validating this expectation across multiple model families and scales remains future work.\n\nThe framework relies on pre-calibrated item parameters from PSN-IRT rather than self-calibrated parameters. Our MML-EM refit experiment reveals that discrimination recovery degrades substantially ($r_a = 0.127$) when calibrating on current leaderboard data where most models exhibit contamination-driven misfit. Until neural IRT or alternative calibration methods can handle contaminated respondent pools, the framework depends on externally maintained parameter banks.\n\nAll controlled experiments target SFT-stage contamination. While $\\ell_z^*$ is structurally invariant to post-hoc distributional changes from reinforcement learning, empirical validation on post-RL models is deferred to future work.\n\nDetection power varies with benchmark size. On ARC-Challenge (295 items), Cohen's $d = 0.45$ at 15\\% contamination, well below the $d = 3.58$ observed on MMLU (14,042 items). The closed-form power function (Equation~\\ref{eq:power}) predicts that 80\\% power at 15\\% contamination requires $\\geq$7,958 items, placing small benchmarks below reliable detection thresholds.\n\nFinally, because LLM response patterns universally violate classical IRT assumptions, absolute $\\ell_z^*$ values cannot be interpreted against standard normal thresholds. Our framework addresses this through the $\\Delta\\ell_z^*$ difference-in-differences design, but this requires a clean reference condition for each benchmark.\n"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-20T23:56:14.583669+00:00_

The file /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/limitations.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_sec_limitations_20260520T235421",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 43 · 2026-05-20T23:56:14.583823+00:00_

Limitations section written (~240 words). Covers all 6 outlined elements:

1. **Single model family** (Qwen2.5-7B) + QLoRA conservative framing (UC-3: rank-16 limits memorization → 38% is lower bound → full FT would be stronger)
2. **PSN-IRT dependency** + MML-EM refit failure ($r_a = 0.127$) → neural IRT needed for self-calibration
3. **SFT-only** contamination; post-RL deferred
4. **Power vs. benchmark size** (ARC-C $d = 0.45$, need ≥7,958 items for 80% power)
5. **Universal misfit** → absolute $\ell_z^*$ thresholds inapplicable → $\Delta\ell_z^*$ design required
6. **MML-EM discrimination recovery failure** → external parameter bank dependency

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_writing_sec_limitations_20260520T235421"
}
```

</details>

---
