# paper method section

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 19
- **Recorded user turns:** 0
- **Tool calls:** 9
- **Original source:** `logs/chats/worker_paper_method-section_20260515T233110.jsonl`
- **Structured JSON:** [`310bd1d7813b0ff9ca68.json`](../../sessions/31/310bd1d7813b0ff9ca68.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

19 recorded events

### Tool call

_source line 1 · 2026-05-15T23:38:00.719528+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__read_project_file",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_method-section_20260515T233110",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__read_project_file",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-15T23:38:00.720021+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_method-section_20260515T233110",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T23:38:00.720299+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "provenance_weight_training",
  "file": "paper_framing.md",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_method-section_20260515T233110",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "provenance_weight_training",
    "file": "paper_framing.md",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-15T23:38:00.720697+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper_framing.md\", \"content\": \"# Paper Framing — provenance_weight_training\\n\\n> 状态: STABLE (D023 dual-constraint + D029 ESS-only resolved + D035 τ sweep complete)\\n> 最后更新: 2026-05-15 21:30 UTC\\n> 投稿目标: EMNLP 2026 ARR May 25\\n\\n## Core Insight\\n\\nWeb 语料预训练面临合成数据污染问题（20-60%，来源未知），Drayson et al. (EMNLP 2025) 提出 w=(1-q)^b detect-and-reweight 框架，但 b 需要 per-model validation-based grid search（GPT-2/SmolLM ≤360M 用 b=10，SmolLM 1.7B 用 b=1）。\\n\\n我们提出 **dual-constrained adaptive b***：per-batch 从 q-score 分布推导最优 b*，同时满足两个约束：\\n- **α_eff(b) ≥ τ** — 质量下界：确保加权后有效真实率达到收敛理论要求的阈值（\\\"至少做够清洁\\\"）\\n- **ESS(b) ≥ n_min** — 稳定上界：确保有效样本量不低于 Kish 阈值（\\\"不要清洁过头\\\"）\\n\\nb* = inf{b ≥ 0 : α_eff(b) ≥ τ} subject to ESS(b) ≥ n_min — **最小干预准则**：在保证质量的前提下，使用最少的 downweighting。\\n\\n**关键洞察**：α_eff(b) 单调递增、ESS(b) 单调递减。α_eff 给出 b 的下界 b_τ（需至少这么多清洁），ESS 给出 b 的上界 b_ESS（最多这么多清洁）。当 b_τ < b_ESS（~40% reweighted batches），α_eff 是 binding constraint，b* 远小于 ESS 上界（mean 1.67 vs 4.15）——方法选择保守干预而非最大干预。\\n\\n实现路径：**直接 loss reweighting**（gradient 层面连续加权），vs Drayson 的 SIR resampling（离散重采样）。\\n\\n### α_eff(b) 的角色（D023 修正定论）\\n\\n**D021 证明 α_eff(b) 严格单调递增**（dα_eff/db = Cov_w(x, ln x) ≥ 0）——这是正确的。\\n\\n**D021 的错误推论**：\\\"因此 α_eff 优化等价于 ESS 阈值化\\\"——这假设优化目标是 max α_eff(b) s.t. ESS ≥ n_min。但实际优化是 **inf{b : α_eff(b) ≥ τ}**——最小满足质量阈值的 b。单调性恰恰保证了 b_τ 的**存在性和唯一性**。\\n\\n**Q1 实证（Reviewer 独立核实）**：\\n- 51,913 micro-batches 中，49.9% clean (b*=0), 20.2% α_eff binding, 30.0% ESS binding\\n- 在需 reweighting 的 batch 中：40.1% α_eff binding, 59.9% ESS binding\\n- α_eff binding 时 b*=1.67，ESS-only 方法会选 b*=4.15（2.5× 更激进）\\n- α_eff binding 时 ESS=2.60（vs n_min=2.0，有 30% 余量）\\n\\n**论文呈现**：α_eff 是方法的核心组件（非仅 motivation），提供质量阈值约束。Figure: 双轴图展示 α_eff(b) 和 ESS(b) 曲线 + b_τ 和 b_ESS 标注。\\n\\n**τ 的定位（D025 定论 + D035 τ sweep 完整数据更新）**：收敛理论 (arXiv 2602.16065) 中 α = m₁/(m₁+m₂) 是已知设计参数，推导依赖已知比例。τ **不能声称有 propor
…[truncated 10140 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_method-section_20260515T233110",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-15T23:38:00.721003+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "provenance_weight_training",
  "file": "writing_plan.yaml",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_method-section_20260515T233110",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "provenance_weight_training",
    "file": "writing_plan.yaml",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-15T23:38:00.721573+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/writing_plan.yaml\", \"content\": \"# Writing Plan — provenance_weight_training\\n# Generated: 2026-05-15\\n# Contract for downstream writing Workers\\n\\nvenue: EMNLP 2026 ARR May 25\\ndeadline: 2026-05-25\\npage_limit: 8 (+ unlimited appendix)\\n\\ntitle: \\\"Minimum Intervention Reweighting: Adaptive Exponent Selection for Contamination-Aware Pretraining\\\"\\n# 备选:\\n# - \\\"Dual-Constrained Adaptive Reweighting for Pretraining on Contaminated Web Corpora\\\"\\n# - \\\"How Much to Downweight? Principled Exponent Selection for Contamination-Aware Pretraining\\\"\\n\\nabstract_outline:\\n  - sentence_1: \\\"Web pretraining corpora contain 20–60% machine-generated text of unknown provenance, and naive training on such mixtures degrades model quality (model collapse).\\\"\\n  - sentence_2: \\\"Existing detect-and-reweight methods (Drayson et al., 2025) require per-model validation-based grid search over the weighting exponent b, which is expensive and fragile.\\\"\\n  - sentence_3: \\\"We propose a dual-constrained adaptive b* that jointly enforces a quality lower bound (α_eff ≥ τ) and a stability upper bound (ESS ≥ n_min), yielding the minimum intervention—the smallest b that achieves sufficient cleaning per batch, with zero validation cost.\\\"\\n  - sentence_4: \\\"On FineWeb with Qwen3-0.6B, adaptive b* matches grid-search-optimal performance within seed variance while eliminating 6× search cost, and outperforms both uniform training and the max-intervention (ESS-only) baseline.\\\"\\n\\n# ============================================================\\n# SECTIONS\\n# ============================================================\\n\\nsections:\\n\\n  introduction:\\n    target_pages: 1.0\\n    key_points:\\n      - \\\"Web corpora contamination is pervasive (20–60%) and growing; strong model collapse occurs even at low contamina
…[truncated 20970 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_method-section_20260515T233110",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-15T23:38:00.721835+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper/**/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_method-section_20260515T233110",
  "tool": "Glob",
  "tool_args": {
    "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper/**/*.tex"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-15T23:38:00.722065+00:00_

paper/sections/abstract.tex
paper/sections/results.tex
paper/sections/discussion.tex
paper/sections/limitations.tex
paper/sections/appendix.tex
paper/sections/method.tex
paper/main.tex
paper/sections/introduction.tex
paper/sections/related_work.tex
paper/sections/experiments.tex
paper/sections/conclusion.tex
paper/method.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_method-section_20260515T233110",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-15T23:38:00.722312+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_method-section_20260515T233110",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper/sections/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-15T23:38:00.722660+00:00_

1	% Method section — do not add \section{Method} here (already in main.tex)
2	
3	\subsection{Problem Setup}
4	\label{sec:problem_setup}
5	
6	Let $\mathcal{D} = \{x_1, \dots, x_N\}$ denote a pretraining corpus drawn from a mixture of human-written text $\mathcal{D}_{\text{real}}$ and machine-generated text $\mathcal{D}_{\text{synth}}$, with unknown mixing proportion.
7	A pretrained detector assigns each sample a synthetic probability $q(x) \in [0,1]$, where higher values indicate greater likelihood of machine origin.
8	Following \citet{drayson2025detection}, we define the sample weight as
9	\begin{equation}
10	  w(x) = (1 - q(x))^b, \quad b \geq 0,
11	  \label{eq:weight}
12	\end{equation}
13	where $b$ controls the strength of downweighting: $b=0$ recovers uniform training, while large $b$ aggressively suppresses samples with high $q(x)$.
14	
15	\citet{drayson2025detection} treat $b$ as a hyperparameter selected via per-model validation grid search.
16	This is costly---their reported optima range from $b=1$ (SmolLM-1.7B) to $b=10$ (GPT-2 124M)---and requires a clean validation set that may not be available at web scale.
17	We seek instead to \emph{derive} $b$ per batch from the detector scores alone, without validation.
18	
19	\subsection{Dual-Constraint Framework}
20	\label{sec:dual_constraint}
21	
22	We introduce two batch-level diagnostics that together determine the operating point for $b$.
23	
24	\paragraph{Effective real proportion.}
25	Given a batch $\{x_1, \dots, x_B\}$ with binary provenance labels $r_i \in \{0,1\}$ (available from the detector at training time via thresholding or, more generally, as soft labels), the \emph{effective real proportion} under exponent $b$ is
26	\begin{equation}
27	  \aeff(b) \;=\; \frac{\sum_{i=1}^{B} w_i(b) \cdot r_i}{\sum_{i=1}^{B} w_i(b)},
28	  \label{eq:alpha_eff}
29	\end{equation}
30	where $w_i(b) = (1 - q_i)^b$.
31	Intuitively, $\aeff$ measures the fraction of effective gradient signal attributable to real data after rewei
…[truncated 9517 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_method-section_20260515T233110",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-15T23:38:00.722954+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_method-section_20260515T233110",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-15T23:38:00.723197+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	\usepackage{graphicx}
9	\usepackage{amsmath}
10	\usepackage{amssymb}
11	\usepackage{amsthm}
12	\usepackage{algorithm}
13	\usepackage{algorithmic}
14	\usepackage{booktabs}
15	\usepackage{multirow}
16	\usepackage{xcolor}
17	\usepackage{enumitem}
18	\usepackage{hyperref}
19	
20	\newtheorem{proposition}{Proposition}
21	\newtheorem{definition}{Definition}
22	
23	\newcommand{\bstar}{b^*}
24	\newcommand{\aeff}{\alpha_{\mathrm{eff}}}
25	\newcommand{\nmin}{n_{\min}}
26	\newcommand{\btau}{b_{\tau}}
27	\newcommand{\bess}{b_{\mathrm{ESS}}}
28	
29	\title{Minimum Intervention Reweighting: Adaptive Exponent Selection\\for Contamination-Aware Pretraining}
30	
31	\author{Anonymous}
32	
33	\begin{document}
34	\maketitle
35	
36	\begin{abstract}
37	\input{sections/abstract}
38	\end{abstract}
39	
40	\section{Introduction}
41	\label{sec:intro}
42	\input{sections/introduction}
43	
44	\section{Related Work}
45	\label{sec:related}
46	\input{sections/related_work}
47	
48	\section{Method}
49	\label{sec:method}
50	\input{sections/method}
51	
52	\section{Experimental Setup}
53	\label{sec:experiments}
54	\input{sections/experiments}
55	
56	\section{Results}
57	\label{sec:results}
58	\input{sections/results}
59	
60	\section{Discussion}
61	\label{sec:discussion}
62	\input{sections/discussion}
63	
64	\section{Conclusion}
65	\label{sec:conclusion}
66	\input{sections/conclusion}
67	
68	\section*{Limitations}
69	\label{sec:limitations}
70	\input{sections/limitations}
71	
72	\bibliography{references}
73	\bibliographystyle{acl_natbib}
74	
75	\appendix
76	\input{sections/appendix}
77	
78	\end{document}
79	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_method-section_20260515T233110",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-15T23:38:00.723440+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_method-section_20260515T233110",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-15T23:38:00.723790+00:00_

1	
2	\section{Method}
3	\label{sec:method}
4	
5	\subsection{Problem Setup}
6	\label{sec:problem-setup}
7	
8	Consider a pretraining corpus $\mathcal{D} = \{x_1, \ldots, x_N\}$ comprising an unknown mixture of human-authored text $\mathcal{D}_{\mathrm{real}}$ and machine-generated text $\mathcal{D}_{\mathrm{synth}}$, with contamination rate $\rho = |\mathcal{D}_{\mathrm{synth}}| / |\mathcal{D}|$ unknown to the practitioner. A pretrained contamination detector assigns each sample a synthetic probability $q(x_i) \in [0, 1]$.
9	
10	Following \cite{drayson2025detection}, we define per-sample weights as
11	\begin{equation}
12	    w_b(x_i) = (1 - q(x_i))^b, \quad b \geq 0,
13	    \label{eq:weight}
14	\end{equation}
15	where $b = 0$ recovers uniform weighting and increasing $b$ progressively downweights samples with high synthetic probability. The weighted pretraining objective is
16	\begin{equation}
17	    \mathcal{L}(b) = \frac{1}{\sum_j w_b(x_j)} \sum_{i} w_b(x_i) \, \ell(x_i; \theta),
18	    \label{eq:loss}
19	\end{equation}
20	where $\ell(x_i; \theta)$ is the per-sample language modeling loss.
21	
22	\cite{drayson2025detection} treat $b$ as a hyperparameter selected via validation-based grid search, requiring separate training runs for each candidate value. Their optimal $b$ varies across model families (e.g., $b{=}10$ for GPT-2 and SmolLM $\leq$360M vs.\ $b{=}1$ for SmolLM 1.7B), making per-model tuning unavoidable. We instead derive $b$ adaptively per batch from the detector scores alone, requiring no validation set and no grid search.
23	
24	\subsection{Dual-Constraint Framework}
25	\label{sec:dual-constraint}
26	
27	The exponent $b$ controls a fundamental trade-off: stronger downweighting (higher $b$) removes more synthetic influence but also discards effective training signal. We formalize this trade-off through two per-batch statistics.
28	
29	\paragraph{Effective real proportion.} For a batch $\mathcal{B} = \{x_1, \ldots, x_B\}$ with weights $w_i = w_b(x_i)$, we 
…[truncated 9341 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_method-section_20260515T233110",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-15T23:38:00.724527+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper/method.tex",
  "content": "% Method section for \"Minimum Intervention Reweighting\" (EMNLP 2026)\n% Generated: 2026-05-15\n% Based on: paper_framing.md (STABLE, D023/D029/D035)\n% Requires macros: \\bstar, \\aeff, \\nmin, \\btau, \\bess (defined in main.tex preamble)\n\n\\section{Method}\n\\label{sec:method}\n\n\\subsection{Problem Setup}\n\\label{sec:problem-setup}\n\nLet $\\mathcal{D} = \\{x_1, \\ldots, x_N\\}$ denote a pretraining corpus comprising human-written text $\\mathcal{D}_{\\mathrm{real}}$ and machine-generated text $\\mathcal{D}_{\\mathrm{synth}}$, with unknown contamination rate $\\rho = |\\mathcal{D}_{\\mathrm{synth}}| / |\\mathcal{D}|$.\nA pretrained detector assigns each sample a synthetic probability $q(x_i) \\in [0, 1]$.\nFollowing \\citet{drayson_2025_detection_collapse}, we define per-sample weights\n\\begin{equation}\n  w_b(x_i) = (1 - q(x_i))^b, \\quad b \\geq 0,\n  \\label{eq:weight}\n\\end{equation}\nwhere $b = 0$ recovers uniform weighting and increasing $b$ progressively downweights high-$q$ samples.\nThe weighted training objective is\n\\begin{equation}\n  \\mathcal{L}(b) = \\frac{\\sum_{i} w_b(x_i) \\, \\ell(x_i; \\theta)}{\\sum_{j} w_b(x_j)},\n  \\label{eq:loss}\n\\end{equation}\nwhere $\\ell(x_i; \\theta)$ is the per-sample language modeling loss.\n\n\\citet{drayson_2025_detection_collapse} treat $b$ as a hyperparameter selected via validation-based grid search, with reported optima ranging from $b{=}1$ (SmolLM-1.7B) to $b{=}10$ (GPT-2 124M), making per-model tuning unavoidable.\nWe instead derive $b$ adaptively per batch from the detector scores alone, requiring no validation set.\n\n\\subsection{Dual-Constraint Framework}\n\\label{sec:dual-constraint}\n\nHigher $b$ removes more synthetic influence but also discards effective training signal.\nWe formalize this trade-off through two per-batch statistics.\n\n\\paragraph{Effective real proportion.}\nFor a batch $\\mathcal{B} = \\{x_1, \\ldots, x_B\\}$ with weights $w_i(b) = (1 - q_i)^b$, we define\n\\begin{equation}\n  \\aeff(b) = \\frac{\\sum_{i \\in \\mathcal{B}} w_i(b) \\cdot \\mathbf{1}[x_i \\in \\mathcal{D}_{\\mathrm{real}}]}{\\sum_{i \\in \\mathcal{B}} w_i(b)},\n  \\label{eq:alpha_eff}\n\\end{equation}\nmeasuring the effective fraction of real data after reweighting.\nSince true provenance labels are unavailable at training time, we use the detector's hard prediction $\\mathbf{1}[q(x_i) < 0.5]$ as a proxy; all theoretical properties below hold for this approximation.\n\n\\paragraph{Effective sample size.}\nKish's effective sample size \\citep{vehtari_2024_psis} quantifies weight concentration:\n\\begin{equation}\n  \\mathrm{ESS}(b) = \\frac{\\left(\\sum_{i \\in \\mathcal{B}} w_i(b)\\right)^2}{\\sum_{i \\in \\mathcal{B}} w_i^2(b)}.\n  \\label{eq:ess}\n\\end{equation}\n$\\mathrm{ESS}(0) = B$ under uniform weights, decreasing toward $1$ as $b \\to \\infty$ for any batch containing synthetic samples.\n\n\\begin{proposition}[Monotonicity]\n\\label{prop:monotonicity}\nFor any batch containing both real and synthetic samples with non-identical $q$-scores:\n\\begin{enumerate}[leftmargin=*,nosep]\n  \\item $\\aeff(b)$ is strictly increasing in $b$.\n  \\item $\\mathrm{ESS}(b)$ is strictly decreasing in $b$.\n\\end{enumerate}\n\\end{proposition}\n\n\\begin{proof}[Proof sketch]\nFor (1), differentiating Eq.~\\eqref{eq:alpha_eff} using $\\frac{dw_i}{db} = w_i \\ln(1 {-} q_i)$ yields\n\\begin{equation}\n  \\frac{d\\aeff}{db} = \\aeff(1 {-} \\aeff) \\!\\left( \\mathbb{E}_w[\\ln(1{-}q) \\mid \\mathrm{real}] - \\mathbb{E}_w[\\ln(1{-}q) \\mid \\mathrm{synth}] \\right)\\!,\n  \\label{eq:dalpha}\n\\end{equation}\nwhere $\\mathbb{E}_w$ denotes expectation under the normalized weight distribution.\nSince real samples have lower $q$-scores, $\\ln(1{-}q)$ is strictly less negative for real than synthetic samples, making the parenthesized difference positive.\nFor (2), increasing $b$ multiplies each weight by $(1{-}q_i)^{\\Delta b}$, a factor varying across samples, which concentrates the normalized weight distribution and strictly increases $\\sum_i \\tilde{w}_i^2$, hence decreasing ESS.\nFull proofs appear in Appendix~\\ref{app:proofs}.\n\\end{proof}\n\nProposition~\\ref{prop:monotonicity} establishes that quality and sample efficiency move in opposite directions as $b$ increases, motivating two complementary constraints.\n\n\\paragraph{Quality lower bound.}\nWe require $\\aeff(b) \\geq \\tau$ for a threshold $\\tau \\in (0, 1)$.\nBy strict monotonicity, this defines a unique lower bound\n\\begin{equation}\n  \\btau = \\inf\\{b \\geq 0 : \\aeff(b) \\geq \\tau\\}\n  \\label{eq:b_tau}\n\\end{equation}\non the exponent---the minimum intervention needed to achieve quality $\\tau$.\n\\citet{wang_2026_survive_contamination} show that pretraining convergence rate scales with effective real data fraction, providing theoretical motivation for maintaining $\\aeff$ above a threshold.\n\n\\paragraph{Stability upper bound.}\nWe require $\\mathrm{ESS}(b) \\geq \\nmin$ for a floor $\\nmin \\geq 1$.\nBy strict monotonicity, this defines a unique upper bound\n\\begin{equation}\n  \\bess = \\sup\\{b \\geq 0 : \\mathrm{ESS}(b) \\geq \\nmin\\}\n  \\label{eq:b_ess}\n\\end{equation}\nbeyond which gradient estimates become unreliable due to weight concentration.\n\n\\paragraph{Minimum intervention principle.}\nWe select\n\\begin{equation}\n  \\bstar = \\begin{cases}\n    0 & \\text{if } \\aeff(0) \\geq \\tau \\\\\n    \\btau & \\text{if } \\btau \\leq \\bess \\\\\n    \\bess & \\text{if } \\btau > \\bess\n  \\end{cases}\n  \\label{eq:bstar}\n\\end{equation}\nyielding three regimes:\n(1)~\\textbf{Already clean} ($\\aeff(0) \\geq \\tau$): the unweighted batch meets quality $\\tau$; set $\\bstar = 0$.\n(2)~\\textbf{$\\aeff$-binding} ($\\btau \\leq \\bess$): the quality constraint determines $\\bstar = \\btau$, applying the \\emph{minimum} intervention to reach $\\tau$, with ESS margin remaining.\n(3)~\\textbf{ESS-binding} ($\\btau > \\bess$): quality $\\tau$ is infeasible under the stability constraint; $\\bstar = \\bess$ applies the maximum stable intervention.\n\nThe key insight is that when the feasible region $[\\btau, \\bess]$ is non-empty, the method selects its \\emph{left} endpoint---downweighting no more than necessary.\nThis contrasts with an ESS-only strategy that selects $\\bess$ (the right endpoint), maximizing cleaning at the cost of discarding useful gradient signal from borderline samples.\nIn our experiments (\\S\\ref{sec:results}), 40.1\\% of reweighted batches are $\\aeff$-binding, where mean $\\bstar = 1.67$ compared to $4.15$ under ESS-only---a $2.5\\times$ less aggressive exponent that retains $\\mathrm{ESS} = 2.60$, well above the floor $\\nmin = 2$.\n\n\\subsection{Algorithm}\n\\label{sec:algorithm}\n\nAlgorithm~\\ref{alg:solver} solves for $\\bstar$ via bisection on $\\aeff$, exploiting monotonicity (Proposition~\\ref{prop:monotonicity}) to guarantee convergence.\n\n\\begin{algorithm}[t]\n\\caption{Per-batch adaptive exponent solver}\n\\label{alg:solver}\n\\begin{algorithmic}[1]\n\\REQUIRE Batch scores $\\{q_1, \\ldots, q_B\\}$, threshold $\\tau$, ESS floor $\\nmin$, tolerance $\\varepsilon$, cap $b_{\\max}$\n\\ENSURE Optimal exponent $\\bstar$\n\\IF{$\\aeff(0) \\geq \\tau$}\n  \\STATE \\textbf{return} $\\bstar = 0$ \\hfill $\\triangleright$ Already clean\n\\ENDIF\n\\STATE $b_{\\mathrm{lo}} \\leftarrow 0,\\; b_{\\mathrm{hi}} \\leftarrow b_{\\max}$ \\hfill $\\triangleright$ Bisect for $\\btau$\n\\WHILE{$b_{\\mathrm{hi}} - b_{\\mathrm{lo}} > \\varepsilon$}\n  \\STATE $b_{\\mathrm{mid}} \\leftarrow (b_{\\mathrm{lo}} + b_{\\mathrm{hi}}) / 2$\n  \\IF{$\\aeff(b_{\\mathrm{mid}}) < \\tau$}\n    \\STATE $b_{\\mathrm{lo}} \\leftarrow b_{\\mathrm{mid}}$\n  \\ELSE\n    \\STATE $b_{\\mathrm{hi}} \\leftarrow b_{\\mathrm{mid}}$\n  \\ENDIF\n\\ENDWHILE\n\\STATE $\\btau \\leftarrow b_{\\mathrm{hi}}$\n\\IF{$\\mathrm{ESS}(\\btau) \\geq \\nmin$}\n  \\STATE \\textbf{return} $\\bstar = \\btau$ \\hfill $\\triangleright$ $\\aeff$-binding\n\\ELSE\n  \\STATE Find $\\bess = \\sup\\{b : \\mathrm{ESS}(b) \\geq \\nmin\\}$ via bisection\n  \\STATE \\textbf{return} $\\bstar = \\bess$ \\hfill $\\triangleright$ ESS-binding\n\\ENDIF\n\\end{algorithmic}\n\\end{algorithm}\n\n\\paragraph{Implementation.}\nWe apply $\\bstar$ through loss reweighting: each sample's loss is scaled by its normalized weight $\\bar{w}_i = w_{\\bstar}(x_i) / \\sum_j w_{\\bstar}(x_j)$, yielding continuous gradient contributions from all samples including those with intermediate $q$-scores.\nThis contrasts with the sampling-importance-resampling (SIR) approach of \\citet{drayson_2025_detection_collapse}, which discretely resamples a subset of the batch, introducing additional variance and discarding partial information from borderline samples.\n\n\\paragraph{Computational cost.}\nEach evaluation of $\\aeff$ or ESS costs $O(B)$ for batch size $B$.\nBisection requires $O(\\log(b_{\\max} / \\varepsilon))$ iterations, giving total per-batch overhead $O(B \\log(b_{\\max} / \\varepsilon))$---negligible compared to the $O(BHD)$ cost of transformer forward and backward passes with hidden dimension $H$ and depth $D$.\nWith $b_{\\max} = 20$ and $\\varepsilon = 0.01$, this amounts to ${\\sim}11$ iterations per batch.\n\n\\subsection{Hyperparameters}\n\\label{sec:hyperparameters}\n\nThe framework replaces the single sensitive exponent $b$ with two hyperparameters, $\\tau$ and $\\nmin$, both admitting principled defaults that transfer across settings without per-model tuning.\n\n\\paragraph{Quality threshold $\\tau$.}\n\\citet{wang_2026_survive_contamination} establish that pretraining convergence rate scales with effective real data proportion, motivating a quality threshold.\nHowever, their analysis assumes known mixture proportions; since we do not assume known $\\rho$, $\\tau$ is an empirical hyperparameter with theoretical motivation rather than a theoretically derived quantity.\nWe evaluate $\\tau \\in \\{0.5, 0.6, 0.7, 0.8, 0.9, 0.95\\}$ at $\\rho = 0.4$ (\\S\\ref{sec:results}).\nAll values in $[0.5, 0.8]$ improve over uniform training, with PPL spanning only $0.035$ across this range (17.688 at $\\tau{=}0.5$ to 17.653 at $\\tau{=}0.8$).\nWe adopt $\\tau = 0.8$ as the default.\nThe sensitivity is asymmetric: under-cleaning ($\\tau < 0.8$) yields mild degradation, while over-cleaning ($\\tau > 0.8$) causes sharper regression as $\\bstar$ inflates (mean $\\bstar = 2.36$ at $\\tau{=}0.9$ vs.\\ $1.40$ at $\\tau{=}0.8$), excessively suppressing borderline samples whose gradient signal remains useful.\n\n\\paragraph{ESS floor $\\nmin$.}\nThe stability constraint prevents gradient instability from weight concentration.\nAt $\\nmin = 1$ (effectively unconstrained), $\\bstar$ inflates to mean $7.20$ with 46.7\\% of batches exceeding $\\bstar = 2$, yielding PPL~$= 17.789$---worse than uniform ($17.694$) by $+0.095$, confirming that unconstrained downweighting is harmful.\nAt $\\nmin \\geq B$, the constraint forces $\\bstar = 0$ for all batches, recovering uniform training.\nWe use $\\nmin = 2$ (half the batch size for $B = 4$), which yields consistent improvement across three seeds (\\S\\ref{sec:results}).\n\n\\paragraph{Comparison with fixed $b$.}\nBoth $\\tau$ and $\\nmin$ admit wide effective ranges ($\\tau \\in [0.5, 0.8]$, $\\nmin \\in \\{2, 3\\}$) and can be set once without per-model adjustment.\nIn contrast, the fixed $b$ of \\citet{drayson_2025_detection_collapse} spans an order of magnitude across model scales and requires a clean validation set plus grid search costing up to $6{\\times}$ the training budget.\nOur adaptive $\\bstar$ eliminates this cost entirely.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_method-section_20260515T233110",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper/method.tex",
    "content": "% Method section for \"Minimum Intervention Reweighting\" (EMNLP 2026)\n% Generated: 2026-05-15\n% Based on: paper_framing.md (STABLE, D023/D029/D035)\n% Requires macros: \\bstar, \\aeff, \\nmin, \\btau, \\bess (defined in main.tex preamble)\n\n\\section{Method}\n\\label{sec:method}\n\n\\subsection{Problem Setup}\n\\label{sec:problem-setup}\n\nLet $\\mathcal{D} = \\{x_1, \\ldots, x_N\\}$ denote a pretraining corpus comprising human-written text $\\mathcal{D}_{\\mathrm{real}}$ and machine-generated text $\\mathcal{D}_{\\mathrm{synth}}$, with unknown contamination rate $\\rho = |\\mathcal{D}_{\\mathrm{synth}}| / |\\mathcal{D}|$.\nA pretrained detector assigns each sample a synthetic probability $q(x_i) \\in [0, 1]$.\nFollowing \\citet{drayson_2025_detection_collapse}, we define per-sample weights\n\\begin{equation}\n  w_b(x_i) = (1 - q(x_i))^b, \\quad b \\geq 0,\n  \\label{eq:weight}\n\\end{equation}\nwhere $b = 0$ recovers uniform weighting and increasing $b$ progressively downweights high-$q$ samples.\nThe weighted training objective is\n\\begin{equation}\n  \\mathcal{L}(b) = \\frac{\\sum_{i} w_b(x_i) \\, \\ell(x_i; \\theta)}{\\sum_{j} w_b(x_j)},\n  \\label{eq:loss}\n\\end{equation}\nwhere $\\ell(x_i; \\theta)$ is the per-sample language modeling loss.\n\n\\citet{drayson_2025_detection_collapse} treat $b$ as a hyperparameter selected via validation-based grid search, with reported optima ranging from $b{=}1$ (SmolLM-1.7B) to $b{=}10$ (GPT-2 124M), making per-model tuning unavoidable.\nWe instead derive $b$ adaptively per batch from the detector scores alone, requiring no validation set.\n\n\\subsection{Dual-Constraint Framework}\n\\label{sec:dual-constraint}\n\nHigher $b$ removes more synthetic influence but also discards effective training signal.\nWe formalize this trade-off through two per-batch statistics.\n\n\\paragraph{Effective real proportion.}\nFor a batch $\\mathcal{B} = \\{x_1, \\ldots, x_B\\}$ with weights $w_i(b) = (1 - q_i)^b$, we define\n\\begin{equation}\n  \\aeff(b) = \\frac{\\sum_{i \\in \\mathcal{B}} w_i(b) \\cdot \\mathbf{1}[x_i \\in \\mathcal{D}_{\\mathrm{real}}]}{\\sum_{i \\in \\mathcal{B}} w_i(b)},\n  \\label{eq:alpha_eff}\n\\end{equation}\nmeasuring the effective fraction of real data after reweighting.\nSince true provenance labels are unavailable at training time, we use the detector's hard prediction $\\mathbf{1}[q(x_i) < 0.5]$ as a proxy; all theoretical properties below hold for this approximation.\n\n\\paragraph{Effective sample size.}\nKish's effective sample size \\citep{vehtari_2024_psis} quantifies weight concentration:\n\\begin{equation}\n  \\mathrm{ESS}(b) = \\frac{\\left(\\sum_{i \\in \\mathcal{B}} w_i(b)\\right)^2}{\\sum_{i \\in \\mathcal{B}} w_i^2(b)}.\n  \\label{eq:ess}\n\\end{equation}\n$\\mathrm{ESS}(0) = B$ under uniform weights, decreasing toward $1$ as $b \\to \\infty$ for any batch containing synthetic samples.\n\n\\begin{proposition}[Monotonicity]\n\\label{prop:monotonicity}\nFor any batch containing both real and synthetic samples with non-identical $q$-scores:\n\\begin{enumerate}[leftmargin=*,nosep]\n  \\item $\\aeff(b)$ is strictly increasing in $b$.\n  \\item $\\mathrm{ESS}(b)$ is strictly decreasing in $b$.\n\\end{enumerate}\n\\end{proposition}\n\n\\begin{proof}[Proof sketch]\nFor (1), differentiating Eq.~\\eqref{eq:alpha_eff} using $\\frac{dw_i}{db} = w_i \\ln(1 {-} q_i)$ yields\n\\begin{equation}\n  \\frac{d\\aeff}{db} = \\aeff(1 {-} \\aeff) \\!\\left( \\mathbb{E}_w[\\ln(1{-}q) \\mid \\mathrm{real}] - \\mathbb{E}_w[\\ln(1{-}q) \\mid \\mathrm{synth}] \\right)\\!,\n  \\label{eq:dalpha}\n\\end{equation}\nwhere $\\mathbb{E}_w$ denotes expectation under the normalized weight distribution.\nSince real samples have lower $q$-scores, $\\ln(1{-}q)$ is strictly less negative for real than synthetic samples, making the parenthesized difference positive.\nFor (2), increasing $b$ multiplies each weight by $(1{-}q_i)^{\\Delta b}$, a factor varying across samples, which concentrates the normalized weight distribution and strictly increases $\\sum_i \\tilde{w}_i^2$, hence decreasing ESS.\nFull proofs appear in Appendix~\\ref{app:proofs}.\n\\end{proof}\n\nProposition~\\ref{prop:monotonicity} establishes that quality and sample efficiency move in opposite directions as $b$ increases, motivating two complementary constraints.\n\n\\paragraph{Quality lower bound.}\nWe require $\\aeff(b) \\geq \\tau$ for a threshold $\\tau \\in (0, 1)$.\nBy strict monotonicity, this defines a unique lower bound\n\\begin{equation}\n  \\btau = \\inf\\{b \\geq 0 : \\aeff(b) \\geq \\tau\\}\n  \\label{eq:b_tau}\n\\end{equation}\non the exponent---the minimum intervention needed to achieve quality $\\tau$.\n\\citet{wang_2026_survive_contamination} show that pretraining convergence rate scales with effective real data fraction, providing theoretical motivation for maintaining $\\aeff$ above a threshold.\n\n\\paragraph{Stability upper bound.}\nWe require $\\mathrm{ESS}(b) \\geq \\nmin$ for a floor $\\nmin \\geq 1$.\nBy strict monotonicity, this defines a unique upper bound\n\\begin{equation}\n  \\bess = \\sup\\{b \\geq 0 : \\mathrm{ESS}(b) \\geq \\nmin\\}\n  \\label{eq:b_ess}\n\\end{equation}\nbeyond which gradient estimates become unreliable due to weight concentration.\n\n\\paragraph{Minimum intervention principle.}\nWe select\n\\begin{equation}\n  \\bstar = \\begin{cases}\n    0 & \\text{if } \\aeff(0) \\geq \\tau \\\\\n    \\btau & \\text{if } \\btau \\leq \\bess \\\\\n    \\bess & \\text{if } \\btau > \\bess\n  \\end{cases}\n  \\label{eq:bstar}\n\\end{equation}\nyielding three regimes:\n(1)~\\textbf{Already clean} ($\\aeff(0) \\geq \\tau$): the unweighted batch meets quality $\\tau$; set $\\bstar = 0$.\n(2)~\\textbf{$\\aeff$-binding} ($\\btau \\leq \\bess$): the quality constraint determines $\\bstar = \\btau$, applying the \\emph{minimum} intervention to reach $\\tau$, with ESS margin remaining.\n(3)~\\textbf{ESS-binding} ($\\btau > \\bess$): quality $\\tau$ is infeasible under the stability constraint; $\\bstar = \\bess$ applies the maximum stable intervention.\n\nThe key insight is that when the feasible region $[\\btau, \\bess]$ is non-empty, the method selects its \\emph{left} endpoint---downweighting no more than necessary.\nThis contrasts with an ESS-only strategy that selects $\\bess$ (the right endpoint), maximizing cleaning at the cost of discarding useful gradient signal from borderline samples.\nIn our experiments (\\S\\ref{sec:results}), 40.1\\% of reweighted batches are $\\aeff$-binding, where mean $\\bstar = 1.67$ compared to $4.15$ under ESS-only---a $2.5\\times$ less aggressive exponent that retains $\\mathrm{ESS} = 2.60$, well above the floor $\\nmin = 2$.\n\n\\subsection{Algorithm}\n\\label{sec:algorithm}\n\nAlgorithm~\\ref{alg:solver} solves for $\\bstar$ via bisection on $\\aeff$, exploiting monotonicity (Proposition~\\ref{prop:monotonicity}) to guarantee convergence.\n\n\\begin{algorithm}[t]\n\\caption{Per-batch adaptive exponent solver}\n\\label{alg:solver}\n\\begin{algorithmic}[1]\n\\REQUIRE Batch scores $\\{q_1, \\ldots, q_B\\}$, threshold $\\tau$, ESS floor $\\nmin$, tolerance $\\varepsilon$, cap $b_{\\max}$\n\\ENSURE Optimal exponent $\\bstar$\n\\IF{$\\aeff(0) \\geq \\tau$}\n  \\STATE \\textbf{return} $\\bstar = 0$ \\hfill $\\triangleright$ Already clean\n\\ENDIF\n\\STATE $b_{\\mathrm{lo}} \\leftarrow 0,\\; b_{\\mathrm{hi}} \\leftarrow b_{\\max}$ \\hfill $\\triangleright$ Bisect for $\\btau$\n\\WHILE{$b_{\\mathrm{hi}} - b_{\\mathrm{lo}} > \\varepsilon$}\n  \\STATE $b_{\\mathrm{mid}} \\leftarrow (b_{\\mathrm{lo}} + b_{\\mathrm{hi}}) / 2$\n  \\IF{$\\aeff(b_{\\mathrm{mid}}) < \\tau$}\n    \\STATE $b_{\\mathrm{lo}} \\leftarrow b_{\\mathrm{mid}}$\n  \\ELSE\n    \\STATE $b_{\\mathrm{hi}} \\leftarrow b_{\\mathrm{mid}}$\n  \\ENDIF\n\\ENDWHILE\n\\STATE $\\btau \\leftarrow b_{\\mathrm{hi}}$\n\\IF{$\\mathrm{ESS}(\\btau) \\geq \\nmin$}\n  \\STATE \\textbf{return} $\\bstar = \\btau$ \\hfill $\\triangleright$ $\\aeff$-binding\n\\ELSE\n  \\STATE Find $\\bess = \\sup\\{b : \\mathrm{ESS}(b) \\geq \\nmin\\}$ via bisection\n  \\STATE \\textbf{return} $\\bstar = \\bess$ \\hfill $\\triangleright$ ESS-binding\n\\ENDIF\n\\end{algorithmic}\n\\end{algorithm}\n\n\\paragraph{Implementation.}\nWe apply $\\bstar$ through loss reweighting: each sample's loss is scaled by its normalized weight $\\bar{w}_i = w_{\\bstar}(x_i) / \\sum_j w_{\\bstar}(x_j)$, yielding continuous gradient contributions from all samples including those with intermediate $q$-scores.\nThis contrasts with the sampling-importance-resampling (SIR) approach of \\citet{drayson_2025_detection_collapse}, which discretely resamples a subset of the batch, introducing additional variance and discarding partial information from borderline samples.\n\n\\paragraph{Computational cost.}\nEach evaluation of $\\aeff$ or ESS costs $O(B)$ for batch size $B$.\nBisection requires $O(\\log(b_{\\max} / \\varepsilon))$ iterations, giving total per-batch overhead $O(B \\log(b_{\\max} / \\varepsilon))$---negligible compared to the $O(BHD)$ cost of transformer forward and backward passes with hidden dimension $H$ and depth $D$.\nWith $b_{\\max} = 20$ and $\\varepsilon = 0.01$, this amounts to ${\\sim}11$ iterations per batch.\n\n\\subsection{Hyperparameters}\n\\label{sec:hyperparameters}\n\nThe framework replaces the single sensitive exponent $b$ with two hyperparameters, $\\tau$ and $\\nmin$, both admitting principled defaults that transfer across settings without per-model tuning.\n\n\\paragraph{Quality threshold $\\tau$.}\n\\citet{wang_2026_survive_contamination} establish that pretraining convergence rate scales with effective real data proportion, motivating a quality threshold.\nHowever, their analysis assumes known mixture proportions; since we do not assume known $\\rho$, $\\tau$ is an empirical hyperparameter with theoretical motivation rather than a theoretically derived quantity.\nWe evaluate $\\tau \\in \\{0.5, 0.6, 0.7, 0.8, 0.9, 0.95\\}$ at $\\rho = 0.4$ (\\S\\ref{sec:results}).\nAll values in $[0.5, 0.8]$ improve over uniform training, with PPL spanning only $0.035$ across this range (17.688 at $\\tau{=}0.5$ to 17.653 at $\\tau{=}0.8$).\nWe adopt $\\tau = 0.8$ as the default.\nThe sensitivity is asymmetric: under-cleaning ($\\tau < 0.8$) yields mild degradation, while over-cleaning ($\\tau > 0.8$) causes sharper regression as $\\bstar$ inflates (mean $\\bstar = 2.36$ at $\\tau{=}0.9$ vs.\\ $1.40$ at $\\tau{=}0.8$), excessively suppressing borderline samples whose gradient signal remains useful.\n\n\\paragraph{ESS floor $\\nmin$.}\nThe stability constraint prevents gradient instability from weight concentration.\nAt $\\nmin = 1$ (effectively unconstrained), $\\bstar$ inflates to mean $7.20$ with 46.7\\% of batches exceeding $\\bstar = 2$, yielding PPL~$= 17.789$---worse than uniform ($17.694$) by $+0.095$, confirming that unconstrained downweighting is harmful.\nAt $\\nmin \\geq B$, the constraint forces $\\bstar = 0$ for all batches, recovering uniform training.\nWe use $\\nmin = 2$ (half the batch size for $B = 4$), which yields consistent improvement across three seeds (\\S\\ref{sec:results}).\n\n\\paragraph{Comparison with fixed $b$.}\nBoth $\\tau$ and $\\nmin$ admit wide effective ranges ($\\tau \\in [0.5, 0.8]$, $\\nmin \\in \\{2, 3\\}$) and can be set once without per-model adjustment.\nIn contrast, the fixed $b$ of \\citet{drayson_2025_detection_collapse} spans an order of magnitude across model scales and requires a clean validation set plus grid search costing up to $6{\\times}$ the training budget.\nOur adaptive $\\bstar$ eliminates this cost entirely.\n"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-15T23:38:00.725290+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper/method.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_method-section_20260515T233110",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-15T23:38:00.725588+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "method_section_draft_v1",
  "type": "paper",
  "description": "Method section (Section 3) initial draft for EMNLP 2026 paper. Covers Problem Setup, Dual-Constraint Framework (α_eff + ESS monotonicity, Proposition 1, minimum intervention principle), Algorithm (bisection solver), and Hyperparameters (τ, n_min). ~2.5 target pages. Based on paper_framing.md STABLE version (D023/D029/D035).",
  "project": "provenance_weight_training",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper/method.tex",
  "tags": "['paper', 'method', 'draft', 'emnlp2026']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_method-section_20260515T233110",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "method_section_draft_v1",
    "type": "paper",
    "description": "Method section (Section 3) initial draft for EMNLP 2026 paper. Covers Problem Setup, Dual-Constraint Framework (α_eff + ESS monotonicity, Proposition 1, minimum intervention principle), Algorithm (bisection solver), and Hyperparameters (τ, n_min). ~2.5 target pages. Based on paper_framing.md STABLE version (D023/D029/D035).",
    "project": "provenance_weight_training",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper/method.tex",
    "tags": "['paper', 'method', 'draft', 'emnlp2026']"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-15T23:38:00.725878+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260515_3f5a58\", \"name\": \"method_section_draft_v1\", \"type\": \"paper\", \"description\": \"Method section (Section 3) initial draft for EMNLP 2026 paper. Covers Problem Setup, Dual-Constraint Framework (α_eff + ESS monotonicity, Proposition 1, minimum intervention principle), Algorithm (bisection solver), and Hyperparameters (τ, n_min). ~2.5 target pages. Based on paper_framing.md STABLE version (D023/D029/D035).\", \"path\": \"projects/provenance_weight_training/artifacts/_project/paper/method_3f5a58.tex\", \"url\": null, \"project\": \"provenance_weight_training\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-15T23:37:43.883269+00:00\", \"tags\": [\"paper\", \"method\", \"draft\", \"emnlp2026\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_method-section_20260515T233110",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-15T23:38:00.726175+00:00_

已写入 `paper/method.tex` 并注册为 artifact `art_20260515_3f5a58`。

**内容结构**（4 subsections，目标 2.5 页）：

- **3.1 Problem Setup** — 语料 D、检测器 q(x)、权重公式 w=(1-q)^b（共享自 Drayson）、加权损失方程、b 自适应推导的动机
- **3.2 Dual-Constraint Framework** — α_eff 和 ESS 定义（含 proxy 说明）、Proposition 1（单调性，条件期望形式的证明 sketch）、质量下界 b_τ + 稳定上界 b_ESS、分段定义的 b*（Eq.8）、三种 regime + 实证统计（引用 §5）
- **3.3 Algorithm** — Algorithm 1（bisection solver，algorithmic 环境）、loss reweighting vs SIR 实现、O(B log(b_max/ε)) 复杂度
- **3.4 Hyperparameters** — τ（理论 motivation + [0.5,0.8] safe range + 非对称敏感性）、n_min（boundary behavior + default=2）、与 fixed b 的对比

**相对于两个先前版本的改进**：
- 统一使用 main.tex 宏（`\bstar`, `\aeff`, `\btau`, `\bess`, `\nmin`）
- 证明使用更严谨的条件期望分解形式
- 算法伪代码与 `algorithmic` 包兼容（大写命令）
- 引用 key 按 writing_plan 规范（`drayson_2025_detection_collapse` 等）
- 所有定量 claim 引用 §5

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_method-section_20260515T233110"
}
```

</details>

---
