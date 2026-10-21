# paper intro related work

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 29
- **Recorded user turns:** 0
- **Tool calls:** 14
- **Original source:** `logs/chats/worker_paper_intro-related-work_20260515T233142.jsonl`
- **Structured JSON:** [`4001597f5370a93886b4.json`](../../sessions/40/4001597f5370a93886b4.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

29 recorded events

### Tool call

_source line 1 · 2026-05-15T23:39:26.616266+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper/ 2>/dev/null; echo \"---\"; ls /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/ 2>/dev/null",
  "description": "Check existing paper and artifacts directories"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_intro-related-work_20260515T233142",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper/ 2>/dev/null; echo \"---\"; ls /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/ 2>/dev/null",
    "description": "Check existing paper and artifacts directories"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-15T23:39:26.616623+00:00_

total 344
drwxr-xr-x 3 ubuntu ubuntu   4096 May 15 22:30 .
drwxr-xr-x 4 ubuntu ubuntu   4096 May 15 05:23 ..
-rw-r--r-- 1 ubuntu ubuntu  11615 May 15 20:19 acl.sty
-rw-r--r-- 1 ubuntu ubuntu  45186 May 15 20:19 acl_natbib.bst
-rw-r--r-- 1 ubuntu ubuntu  15429 May 15 22:17 main.aux
-rw-r--r-- 1 ubuntu ubuntu   6506 May 15 22:17 main.bbl
-rw-r--r-- 1 ubuntu ubuntu   1463 May 15 22:17 main.blg
-rw-r--r-- 1 ubuntu ubuntu  27225 May 15 22:17 main.log
-rw-r--r-- 1 ubuntu ubuntu   1276 May 15 22:17 main.out
-rw-r--r-- 1 ubuntu ubuntu 192299 May 15 22:17 main.pdf
-rw-r--r-- 1 ubuntu ubuntu   1554 May 15 21:49 main.tex
-rw-r--r-- 1 ubuntu ubuntu  10897 May 15 22:30 method.tex
-rw-r--r-- 1 ubuntu ubuntu   6034 May 15 21:48 references.bib
drwxr-xr-x 2 ubuntu ubuntu   4096 May 15 22:20 sections
---
_project
adaptive_fix_seed42
all_success_summary.md
analyze_tau_sweep.py
bstar_distribution_analysis.md
data_generation
detector
drayson_comparison.md
dream_reports
ess_only_analysis_template.md
ess_only_implementation.md
ess_only_seed42
evaluation
experiment_setup_draft.md
experiment_status_summary.md
experiment_summary.md
experiment_summary_table.md
full_experiment_data.md
grid_b5_0_seed123
grid_eval_source_audit.md
interim_mvp_analysis.md
literature_diff_drayson.md
literature_notes.md
literature_scan_results.md
literature_tau_sensitivity.md
manifest.yaml
method_section_draft.md
mvp_analysis_draft.md
mvp_analysis_summary.md
new_scripts_manifest.md
nmin1_seed42
novelty_drayson_analysis.md
paper_tables.md
q1_ess_equivalence_analysis.md
related_work_notes.md
review_issues.yaml
run_mvp.sh
seed42_diagnostic.md
table1_data.md
tau_095_seed42
tau_09_seed42
tau_b_strength.pdf
tau_b_strength.png
tau_derivation_check.md
tau_fix_changelog.md
tau_ppl_curve.pdf
tau_ppl_curve.png
tau_sweep.pdf
tau_sweep.png
tau_sweep_commands.md
tau_sweep_curve_dummy.pdf
tau_sweep_curve_dummy.png
tau_sweep_improvement_dummy.pdf
tau_sweep_improvement_dummy.png
tau_sweep_readiness.md
tau_theory_analysis.md
tau_theo
…[truncated 74 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_intro-related-work_20260515T233142",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T23:39:26.616807+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__save_project_file",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_intro-related-work_20260515T233142",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__save_project_file",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-15T23:39:26.617013+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_intro-related-work_20260515T233142",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-15T23:39:26.617200+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_intro-related-work_20260515T233142",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-15T23:39:26.617380+00:00_

1	% References for Minimum Intervention Reweighting paper
2	% Note: entries to be verified via verify_references before final submission
3	
4	@article{drayson2025detection,
5	  title={Machine-Generated Text Detection Prevents Language Model Collapse},
6	  author={Drayson, George and Yilmaz, Emine and Lampos, Vasileios},
7	  journal={arXiv preprint arXiv:2502.15654},
8	  year={2025}
9	}
10	
11	@article{he2025golden,
12	  title={Golden Ratio Weighting Prevents Model Collapse},
13	  author={He, Hengzhi and Xu, Shirong and Cheng, Guang},
14	  journal={arXiv preprint arXiv:2502.18049},
15	  year={2025}
16	}
17	
18	@article{wang2026survive,
19	  title={Can Generative Artificial Intelligence Survive Data Contamination? Theoretical Guarantees under Contaminated Recursive Training},
20	  author={Wang, Kevin and Niu, Hongqian and Li, Didong},
21	  journal={arXiv preprint arXiv:2602.16065},
22	  year={2026}
23	}
24	
25	@article{shumailov2024model,
26	  title={{AI} Models Collapse When Trained on Recursively Generated Data},
27	  author={Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Papernot, Nicolas and Anderson, Ross and Gal, Yarin},
28	  journal={Nature},
29	  volume={631},
30	  pages={755--759},
31	  year={2024}
32	}
33	
34	@inproceedings{dohmatob2025strong,
35	  title={Strong Model Collapse},
36	  author={Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia},
37	  booktitle={ICLR},
38	  year={2025}
39	}
40	
41	@article{vehtari2024psis,
42	  title={Pareto Smoothed Importance Sampling},
43	  author={Vehtari, Aki and Simpson, Daniel and Gelman, Andrew and Yao, Yuling and Gabry, Jonah},
44	  journal={JMLR},
45	  year={2024}
46	}
47	
48	@inproceedings{sow2025dynamic,
49	  title={Dynamic Loss-Based Sample Reweighting for Improved Large Language Model Pretraining},
50	  author={Sow, Daouda and Woisetschl{\"a}ger, Herbert and Bulusu, Saikiran and Wang, Shiqiang and Jacobsen, Hans-Arno and Liang, Yingbin},
51	  booktitle={ICLR},
52	  year={2025}
53	
…[truncated 4590 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_intro-related-work_20260515T233142",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-15T23:39:26.617542+00:00_

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
  "session": "worker_paper_intro-related-work_20260515T233142",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-15T23:39:26.617690+00:00_

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
  "session": "worker_paper_intro-related-work_20260515T233142",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-15T23:39:26.617833+00:00_

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
  "session": "worker_paper_intro-related-work_20260515T233142",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-15T23:39:26.618101+00:00_

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
  "session": "worker_paper_intro-related-work_20260515T233142",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-15T23:39:26.618260+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "provenance_weight_training",
  "file": "paper_framing.md",
  "max_chars": "12000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_intro-related-work_20260515T233142",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "provenance_weight_training",
    "file": "paper_framing.md",
    "max_chars": "12000"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-15T23:39:26.618496+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper_framing.md\", \"content\": \"# Paper Framing — provenance_weight_training\\n\\n> 状态: STABLE (D023 dual-constraint + D029 ESS-only resolved + D035 τ sweep complete)\\n> 最后更新: 2026-05-15 21:30 UTC\\n> 投稿目标: EMNLP 2026 ARR May 25\\n\\n## Core Insight\\n\\nWeb 语料预训练面临合成数据污染问题（20-60%，来源未知），Drayson et al. (EMNLP 2025) 提出 w=(1-q)^b detect-and-reweight 框架，但 b 需要 per-model validation-based grid search（GPT-2/SmolLM ≤360M 用 b=10，SmolLM 1.7B 用 b=1）。\\n\\n我们提出 **dual-constrained adaptive b***：per-batch 从 q-score 分布推导最优 b*，同时满足两个约束：\\n- **α_eff(b) ≥ τ** — 质量下界：确保加权后有效真实率达到收敛理论要求的阈值（\\\"至少做够清洁\\\"）\\n- **ESS(b) ≥ n_min** — 稳定上界：确保有效样本量不低于 Kish 阈值（\\\"不要清洁过头\\\"）\\n\\nb* = inf{b ≥ 0 : α_eff(b) ≥ τ} subject to ESS(b) ≥ n_min — **最小干预准则**：在保证质量的前提下，使用最少的 downweighting。\\n\\n**关键洞察**：α_eff(b) 单调递增、ESS(b) 单调递减。α_eff 给出 b 的下界 b_τ（需至少这么多清洁），ESS 给出 b 的上界 b_ESS（最多这么多清洁）。当 b_τ < b_ESS（~40% reweighted batches），α_eff 是 binding constraint，b* 远小于 ESS 上界（mean 1.67 vs 4.15）——方法选择保守干预而非最大干预。\\n\\n实现路径：**直接 loss reweighting**（gradient 层面连续加权），vs Drayson 的 SIR resampling（离散重采样）。\\n\\n### α_eff(b) 的角色（D023 修正定论）\\n\\n**D021 证明 α_eff(b) 严格单调递增**（dα_eff/db = Cov_w(x, ln x) ≥ 0）——这是正确的。\\n\\n**D021 的错误推论**：\\\"因此 α_eff 优化等价于 ESS 阈值化\\\"——这假设优化目标是 max α_eff(b) s.t. ESS ≥ n_min。但实际优化是 **inf{b : α_eff(b) ≥ τ}**——最小满足质量阈值的 b。单调性恰恰保证了 b_τ 的**存在性和唯一性**。\\n\\n**Q1 实证（Reviewer 独立核实）**：\\n- 51,913 micro-batches 中，49.9% clean (b*=0), 20.2% α_eff binding, 30.0% ESS binding\\n- 在需 reweighting 的 batch 中：40.1% α_eff binding, 59.9% ESS binding\\n- α_eff binding 时 b*=1.67，ESS-only 方法会选 b*=4.15（2.5× 更激进）\\n- α_eff binding 时 ESS=2.60（vs n_min=2.0，有 30% 余量）\\n\\n**论文呈现**：α_eff 是方法的核心组件（非仅 motivation），提供质量阈值约束。Figure: 双轴图展示 α_eff(b) 和 ESS(b) 曲线 + b_τ 和 b_ESS 标注。\\n\\n**τ 的定位（D025 定论 + D035 τ sweep 完整数据更新）**：收敛理论 (arXiv 2602.16065) 中 α = m₁/(m₁+m₂) 是已知设计参数，推导依赖已知比例。τ **不能声称有 propor
…[truncated 10140 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_intro-related-work_20260515T233142",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-15T23:39:26.618688+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper/sections/",
  "description": "List existing section files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_intro-related-work_20260515T233142",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper/sections/",
    "description": "List existing section files"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-15T23:39:26.618823+00:00_

total 44
drwxr-xr-x 2 ubuntu ubuntu  4096 May 15 22:20 .
drwxr-xr-x 3 ubuntu ubuntu  4096 May 15 22:30 ..
-rw-r--r-- 1 ubuntu ubuntu     0 May 15 20:19 abstract.tex
-rw-r--r-- 1 ubuntu ubuntu     0 May 15 20:19 appendix.tex
-rw-r--r-- 1 ubuntu ubuntu  2434 May 15 22:20 conclusion.tex
-rw-r--r-- 1 ubuntu ubuntu     0 May 15 20:19 discussion.tex
-rw-r--r-- 1 ubuntu ubuntu  3137 May 15 22:17 experiments.tex
-rw-r--r-- 1 ubuntu ubuntu  4831 May 15 22:16 introduction.tex
-rw-r--r-- 1 ubuntu ubuntu     0 May 15 20:19 limitations.tex
-rw-r--r-- 1 ubuntu ubuntu 10939 May 15 21:29 method.tex
-rw-r--r-- 1 ubuntu ubuntu  5760 May 15 22:17 related_work.tex
-rw-r--r-- 1 ubuntu ubuntu     0 May 15 20:19 results.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_intro-related-work_20260515T233142",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-15T23:39:26.618976+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "provenance_weight_training",
  "file": "literature_map.yaml",
  "max_chars": "12000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_intro-related-work_20260515T233142",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "provenance_weight_training",
    "file": "literature_map.yaml",
    "max_chars": "12000"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-15T23:39:26.619245+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/literature_map.yaml\", \"content\": \"# Literature Map for provenance_weight_training\\n# 研究方向：基于收敛理论的自适应污染重加权\\n# 核心公式：w=(1-q)^b，q 为检测器合成概率，b* 为理论最优权重指数\\n# 更新日期：2026-05-15（文献扫描：补充 Wang et al. + 4 方向新文献 + 修正 2 处错误）\\n\\n# ============================================================\\n# Category: direct-competitor\\n# 同主题/同方法的论文\\n# ============================================================\\n\\n- id: drayson_2025_detection_collapse\\n  title: \\\"Machine-Generated Text Detection Prevents Language Model Collapse\\\"\\n  authors: \\\"George Drayson, Emine Yilmaz, Vasileios Lampos\\\"\\n  venue: \\\"EMNLP 2025\\\"\\n  year: 2025\\n  arxiv_id: \\\"2502.15654\\\"\\n  url: \\\"https://arxiv.org/abs/2502.15654\\\"\\n  github: \\\"https://github.com/GeorgeDrayson/model_collapse\\\"\\n  category: direct-competitor\\n  role: \\\"使用同一公式 w=(1-q)^b 进行重加权，但 b 为验证集 empirical 选取，训练中固定\\\"\\n  method_summary: >\\n    Detect-and-reweight 防止递归训练 model collapse。检测器为 ModernBERT 150M\\n    (MAGE fine-tune, in-domain AUC=0.986, OOD AUC=0.943)。权重公式 wⱼ=(1-q(xⱼ))^b / Σₗ(1-q(xₗ))^b，\\n    通过 SIR 按权重重采样训练数据。b 通过 WikiText-2 验证集上 1 代递归训练后评估选取\\n    (GPT-2/SmolLM 135M/360M 用 b=10, SmolLM 1.7B 用 b=1)，训练全程固定。\\n    实验覆盖 4 个模型 (GPT-2 124M, SmolLM 135M/360M/1.7B)、10 代递归训练、6 种解码策略。\\n    结果 PPL 降低 0.85%–25.65%，diversity 提升 3.44%–14.62%。\\n  key_findings: \\\"验证 detect-and-reweight 有效防止 model collapse 且优于纯人类数据训练；b 值对模型规模敏感（小模型 b=10，大模型 b=1）\\\"\\n  differentiation:\\n    b_selection: \\\"Drayson: 验证集 empirical grid search, per-model 固定 | 我们: α_eff(b) + ESS 约束, per-batch 自适应\\\"\\n    contamination_setting: \\\"Drayson: 不假设已知比例（原文明确声明），但实验为控制设置 | 我们: 未知比例（batch 统计量在线估计）\\\"\\n    detector: \\\"Drayson: ModernBERT 150M (AUC=0.986) | 我们: TF-IDF+LR (AUC=0.939)，证明轻量检测器即可\\\"\\n    theory: \\\"Drayson: 无 b 选取理论（SIR 启发式） | 我们: 收敛理论 motivated α_eff(b) 推导\\\"\\n    traini
…[truncated 11597 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_intro-related-work_20260515T233142",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-15T23:39:26.619437+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_intro-related-work_20260515T233142",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper/sections/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-15T23:39:26.619598+00:00_

1	Web pretraining corpora are increasingly contaminated by machine-generated text, with recent estimates placing the synthetic fraction between 20\% and 60\%.
2	This poses a fundamental threat to model quality: \citet{shumailov2024model} demonstrate that training on recursively generated data leads to irreversible model collapse, and \citet{dohmatob2025strong} prove under scaling-law regimes that even a vanishingly small synthetic fraction suffices to trigger degradation, ruling out data scaling as a remedy.
3	As synthetic content becomes ubiquitous, \emph{contamination-aware training}---strategies that explicitly account for data provenance during optimization---is necessary for maintaining pretraining quality.
4	
5	A natural mitigation is detect-and-reweight: assign each sample a weight $w(x) = (1 - q(x))^b$ based on a detector's estimated synthetic probability $q(x)$, where larger $b$ downweights suspected synthetic text more aggressively \citep{drayson2025detection}.
6	However, the exponent $b$ is a sensitive per-model hyperparameter whose optimal value varies by an order of magnitude across scales: $b = 1$ for SmolLM-1.7B versus $b = 10$ for GPT-2 124M.
7	Selecting $b$ requires a clean validation set and grid search costing up to $6{\times}$ the base training budget.
8	The practical question is immediate: \emph{how should $b$ be chosen without validation data?}
9	
10	We propose a \emph{dual-constraint framework} that derives the exponent adaptively per batch from two diagnostics computed on the detector scores alone.
11	The effective real proportion $\aeff(b)$ measures the weighted fraction of gradient signal attributable to real data and imposes a \emph{quality floor}: $\aeff(b) \geq \tau$---at least enough cleaning.
12	Kish's effective sample size $\mathrm{ESS}(b)$ \citep{vehtari2024psis} quantifies weight concentration and imposes a \emph{stability ceiling}: $\mathrm{ESS}(b) \geq \nmin$---not so much cleaning that gradient signal degrades.
13	A key structura
…[truncated 2927 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_intro-related-work_20260515T233142",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-15T23:39:26.619748+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_intro-related-work_20260515T233142",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper/sections/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-15T23:39:26.619921+00:00_

1	\paragraph{Synthetic Contamination and Model Collapse.}
2	Training on recursively generated data leads to irreversible quality degradation---\emph{model collapse}~\citep{shumailov2024model}.
3	\citet{alemohammad2024mad} formalize this as Model Autophagy Disorder, showing that quality or diversity inevitably degrades without fresh real data, even when original training data is retained.
4	More critically, \citet{dohmatob2025strong} prove under scaling-law regimes that even a vanishingly small synthetic fraction (e.g., $1/1000$) suffices to trigger collapse, ruling out data scaling as a remedy.
5	Independent estimates suggest that synthetic content now constitutes 20--60\% of web corpora, making this threat increasingly urgent.
6	These results motivate \emph{contamination-aware} training strategies that explicitly account for synthetic provenance rather than treating all tokens equally.
7	
8	\paragraph{Detection and Filtering of Machine-Generated Text.}
9	Given the severity of contamination, a natural response is to detect and remove synthetic content.
10	DetectGPT~\citep{mitchell2023detectgpt} performs zero-shot detection via probability curvature, while Min-$k$\% Prob~\citep{shi2024minkprob} uses the average log-probability of the lowest-$k$\% tokens as a reference-free signal.
11	Both produce continuous confidence scores suitable as input to reweighting frameworks such as ours.
12	On the mitigation side, \citet{feng2025beyond} prove that even an imperfect verifier prevents collapse, but apply hard binary filtering that discards borderline samples.
13	\citet{guo2025escaping} similarly rely on verification-based selection.
14	Hard filtering requires a precision--recall threshold; soft reweighting avoids this trade-off by assigning continuous weights.
15	
16	Most directly related to our work, \citet{drayson2025detection} propose $w_j = (1{-}q_j)^b$ for collapse prevention via detect-and-reweight, where $q_j$ is the detector's synthetic probability.
17	We adopt the s
…[truncated 3880 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_intro-related-work_20260515T233142",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-15T23:39:26.620340+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper/introduction.tex",
  "content": "% Introduction for \"Minimum Intervention Reweighting: Adaptive Exponent Selection\n% for Contamination-Aware Pretraining\"\n% Generated: 2026-05-15\n% Framing: STABLE (D023 dual-constraint + D029 ESS-only + D035 tau sweep)\n\n\\section{Introduction}\n\\label{sec:intro}\n\nWeb pretraining corpora are increasingly contaminated by machine-generated text, with recent estimates placing the synthetic fraction between 20\\% and 60\\% \\citep{cheng2025contamination}.\nThis poses a fundamental threat to model quality: \\cite{shumailov2024model} demonstrate that training on recursively generated data leads to irreversible model collapse, and \\cite{dohmatob2025strong} prove under scaling-law regimes that even a vanishingly small synthetic fraction suffices to trigger degradation, ruling out data scaling as a remedy.\nAs synthetic content becomes ubiquitous, \\emph{contamination-aware training}---strategies that explicitly account for data provenance during optimization---is necessary for maintaining pretraining quality.\n\nA natural mitigation is detect-and-reweight: assign each sample a weight $w(x) = (1 - q(x))^b$ based on a detector's estimated synthetic probability $q(x)$, where larger $b$ downweights suspected synthetic text more aggressively \\citep{drayson2025detection}.\nHowever, the exponent $b$ is a sensitive per-model hyperparameter whose optimal value varies by an order of magnitude across model scales---$b = 1$ for SmolLM-1.7B versus $b = 10$ for GPT-2 124M---and selecting it requires a clean validation set and grid search costing up to $6{\\times}$ the base training budget.\nThe practical question is: \\emph{given per-sample detector scores $q(x)$, how should $b$ be chosen without validation?}\n\nWe propose a \\emph{dual-constraint framework} that derives the exponent adaptively per batch from two diagnostics computed on the detector scores alone.\nThe effective real proportion $\\aeff(b)$ measures the weighted fraction of gradient signal from real data and imposes a \\emph{quality floor}: $\\aeff(b) \\geq \\tau$---at least enough cleaning.\nKish's effective sample size $\\mathrm{ESS}(b)$ \\citep{vehtari2024psis} quantifies weight concentration and imposes a \\emph{stability ceiling}: $\\mathrm{ESS}(b) \\geq \\nmin$---not so much cleaning that gradient estimates degrade.\nA key structural insight makes this tractable: $\\aeff$ is strictly increasing in $b$ while $\\mathrm{ESS}$ is strictly decreasing, so the quality constraint yields a unique lower bound $\\btau$ and the stability constraint a unique upper bound $\\bess$.\nWe adopt a \\emph{minimum intervention principle}:\n\\begin{equation*}\n  \\bstar = \\inf\\{b \\geq 0 : \\aeff(b) \\geq \\tau\\} \\quad \\text{subject to} \\quad \\mathrm{ESS}(\\bstar) \\geq \\nmin,\n\\end{equation*}\nthe smallest exponent satisfying the quality floor.\nThis is deliberately conservative: apply enough decontamination to meet the quality target, but no more, preserving the largest possible effective sample size.\nIn practice, batches fall into three regimes---already clean ($\\bstar{=}0$), quality-binding ($\\bstar{=}\\btau$), and stability-binding ($\\bstar{=}\\bess$)---allowing the framework to handle heterogeneous contamination naturally.\nUnlike the discrete sampling-importance-resampling of \\cite{drayson2025detection}, we implement reweighting through direct loss scaling with continuous gradient contributions.\n\nWe evaluate on continued pretraining of Qwen3-0.6B on 132M FineWeb \\citep{penedo2024fineweb} tokens with 40\\% synthetic contamination (\\S\\ref{sec:experiments}).\nAdaptive $\\bstar$ with default hyperparameters ($\\tau{=}0.8$, $\\nmin{=}2$) matches the grid-search-optimal fixed $b$ within seed variance (PPL $17.650 {\\pm} 0.007$ vs.\\ $17.646 {\\pm} 0.007$ across three seeds) at zero validation cost.\nIt outperforms both uniform training (PPL $17.69$) and ESS-only maximum intervention (PPL $17.73$), confirming that minimum intervention is superior to maximum intervention.\nA lightweight TF-IDF + logistic regression detector (AUC\\,=\\,0.939) suffices for effective reweighting, and the quality threshold $\\tau$ admits a wide safe range of $[0.5, 0.8]$ within which all tested values improve over uniform training.\n\nOur contributions are:\n\\begin{enumerate}[nosep,leftmargin=*]\n  \\item A dual-constraint framework for adaptive $\\bstar$ selection with minimum intervention semantics, providing validation-free per-batch exponent derivation from batch-level diagnostics (\\S\\ref{sec:method}).\n  \\item Empirical evidence that adaptive $\\bstar$ matches grid-search-optimal performance within seed variance at zero validation cost, and that minimum intervention (dual-constraint) outperforms maximum intervention (ESS-only) (\\S\\ref{sec:results}).\n  \\item Evidence that a lightweight TF-IDF + logistic regression detector suffices for effective reweighting (\\S\\ref{sec:results}).\n\\end{enumerate}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_intro-related-work_20260515T233142",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper/introduction.tex",
    "content": "% Introduction for \"Minimum Intervention Reweighting: Adaptive Exponent Selection\n% for Contamination-Aware Pretraining\"\n% Generated: 2026-05-15\n% Framing: STABLE (D023 dual-constraint + D029 ESS-only + D035 tau sweep)\n\n\\section{Introduction}\n\\label{sec:intro}\n\nWeb pretraining corpora are increasingly contaminated by machine-generated text, with recent estimates placing the synthetic fraction between 20\\% and 60\\% \\citep{cheng2025contamination}.\nThis poses a fundamental threat to model quality: \\cite{shumailov2024model} demonstrate that training on recursively generated data leads to irreversible model collapse, and \\cite{dohmatob2025strong} prove under scaling-law regimes that even a vanishingly small synthetic fraction suffices to trigger degradation, ruling out data scaling as a remedy.\nAs synthetic content becomes ubiquitous, \\emph{contamination-aware training}---strategies that explicitly account for data provenance during optimization---is necessary for maintaining pretraining quality.\n\nA natural mitigation is detect-and-reweight: assign each sample a weight $w(x) = (1 - q(x))^b$ based on a detector's estimated synthetic probability $q(x)$, where larger $b$ downweights suspected synthetic text more aggressively \\citep{drayson2025detection}.\nHowever, the exponent $b$ is a sensitive per-model hyperparameter whose optimal value varies by an order of magnitude across model scales---$b = 1$ for SmolLM-1.7B versus $b = 10$ for GPT-2 124M---and selecting it requires a clean validation set and grid search costing up to $6{\\times}$ the base training budget.\nThe practical question is: \\emph{given per-sample detector scores $q(x)$, how should $b$ be chosen without validation?}\n\nWe propose a \\emph{dual-constraint framework} that derives the exponent adaptively per batch from two diagnostics computed on the detector scores alone.\nThe effective real proportion $\\aeff(b)$ measures the weighted fraction of gradient signal from real data and imposes a \\emph{quality floor}: $\\aeff(b) \\geq \\tau$---at least enough cleaning.\nKish's effective sample size $\\mathrm{ESS}(b)$ \\citep{vehtari2024psis} quantifies weight concentration and imposes a \\emph{stability ceiling}: $\\mathrm{ESS}(b) \\geq \\nmin$---not so much cleaning that gradient estimates degrade.\nA key structural insight makes this tractable: $\\aeff$ is strictly increasing in $b$ while $\\mathrm{ESS}$ is strictly decreasing, so the quality constraint yields a unique lower bound $\\btau$ and the stability constraint a unique upper bound $\\bess$.\nWe adopt a \\emph{minimum intervention principle}:\n\\begin{equation*}\n  \\bstar = \\inf\\{b \\geq 0 : \\aeff(b) \\geq \\tau\\} \\quad \\text{subject to} \\quad \\mathrm{ESS}(\\bstar) \\geq \\nmin,\n\\end{equation*}\nthe smallest exponent satisfying the quality floor.\nThis is deliberately conservative: apply enough decontamination to meet the quality target, but no more, preserving the largest possible effective sample size.\nIn practice, batches fall into three regimes---already clean ($\\bstar{=}0$), quality-binding ($\\bstar{=}\\btau$), and stability-binding ($\\bstar{=}\\bess$)---allowing the framework to handle heterogeneous contamination naturally.\nUnlike the discrete sampling-importance-resampling of \\cite{drayson2025detection}, we implement reweighting through direct loss scaling with continuous gradient contributions.\n\nWe evaluate on continued pretraining of Qwen3-0.6B on 132M FineWeb \\citep{penedo2024fineweb} tokens with 40\\% synthetic contamination (\\S\\ref{sec:experiments}).\nAdaptive $\\bstar$ with default hyperparameters ($\\tau{=}0.8$, $\\nmin{=}2$) matches the grid-search-optimal fixed $b$ within seed variance (PPL $17.650 {\\pm} 0.007$ vs.\\ $17.646 {\\pm} 0.007$ across three seeds) at zero validation cost.\nIt outperforms both uniform training (PPL $17.69$) and ESS-only maximum intervention (PPL $17.73$), confirming that minimum intervention is superior to maximum intervention.\nA lightweight TF-IDF + logistic regression detector (AUC\\,=\\,0.939) suffices for effective reweighting, and the quality threshold $\\tau$ admits a wide safe range of $[0.5, 0.8]$ within which all tested values improve over uniform training.\n\nOur contributions are:\n\\begin{enumerate}[nosep,leftmargin=*]\n  \\item A dual-constraint framework for adaptive $\\bstar$ selection with minimum intervention semantics, providing validation-free per-batch exponent derivation from batch-level diagnostics (\\S\\ref{sec:method}).\n  \\item Empirical evidence that adaptive $\\bstar$ matches grid-search-optimal performance within seed variance at zero validation cost, and that minimum intervention (dual-constraint) outperforms maximum intervention (ESS-only) (\\S\\ref{sec:results}).\n  \\item Evidence that a lightweight TF-IDF + logistic regression detector suffices for effective reweighting (\\S\\ref{sec:results}).\n\\end{enumerate}\n"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-15T23:39:26.620557+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper/introduction.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_intro-related-work_20260515T233142",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-15T23:39:26.620706+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper/related_work.tex",
  "content": "% Related Work for \"Minimum Intervention Reweighting: Adaptive Exponent Selection\n% for Contamination-Aware Pretraining\"\n% Generated: 2026-05-15\n% Framing: STABLE (D023 dual-constraint + D029 ESS-only + D035 tau sweep)\n\n\\section{Related Work}\n\\label{sec:related}\n\n\\paragraph{Synthetic Contamination and Model Collapse.}\nTraining on recursively generated data leads to irreversible quality degradation---\\emph{model collapse} \\citep{shumailov2024model}.\n\\cite{alemohammad2024mad} formalize this as Model Autophagy Disorder, showing that quality or diversity inevitably degrades without fresh real data, even when original training data is retained.\nMore critically, \\cite{dohmatob2025strong} prove under scaling-law regimes that even a vanishingly small synthetic fraction (e.g., $1/1000$) suffices to trigger collapse, ruling out data scaling as a remedy.\nWith synthetic content now estimated at 20--60\\% of web corpora \\citep{cheng2025contamination}, these results motivate contamination-aware training strategies that explicitly account for data provenance rather than treating all tokens equally.\n\n\\paragraph{Detect and Reweight.}\nA natural response to contamination is to detect and remove synthetic content.\nDetectGPT \\citep{mitchell2023detectgpt} performs zero-shot detection via probability curvature, while Min-$k$\\% Prob \\citep{shi2024minkprob} uses the average log-probability of the lowest-$k$\\% tokens as a reference-free signal; both produce continuous confidence scores suitable as input to reweighting frameworks.\n\\cite{feng2025beyond} prove that even an imperfect verifier prevents collapse, but apply hard binary filtering that discards borderline samples; \\cite{guo2025escaping} similarly rely on verification-based selection.\nSoft reweighting avoids the precision--recall threshold inherent in hard filtering by assigning continuous weights.\n\nMost directly related to our work, \\cite{drayson2025detection} propose $w_j = (1{-}q_j)^b$ for collapse prevention via detect-and-reweight, where $q_j$ is a detector's synthetic probability.\nWe adopt the same weighting formula but differ in several fundamental ways.\n\\textbf{(i)}~Drayson et al.\\ select $b$ via validation-set grid search and fix it throughout training; different model scales require different values ($b{=}10$ for ${\\leq}360$M parameters, $b{=}1$ for 1.7B), making the choice per-model and expensive.\nOur $\\bstar$ is derived per-batch from dual constraints ($\\aeff \\geq \\tau$, $\\mathrm{ESS} \\geq \\nmin$) at zero validation cost, following a minimum intervention principle that selects the smallest sufficient exponent.\n\\textbf{(ii)}~Their SIR resampling discretizes the weight distribution; we apply direct loss reweighting with continuous gradient contributions.\n\\textbf{(iii)}~They employ a ModernBERT-150M detector (AUC\\,=\\,0.986) on WikiText-2 (${\\sim}$2M tokens); we show that a lightweight TF-IDF+LR detector (AUC\\,=\\,0.939) suffices on FineWeb-scale data (132M+ tokens).\n\n\\paragraph{Data Mixing and Reweighting.}\nA parallel line of work optimizes data composition without targeting synthetic contamination.\nAt the \\emph{domain} level, DoReMi \\citep{xie2023doremi} learns mixture weights via Group DRO with a proxy model, DSIR \\citep{xie2023dsir} performs importance resampling with $n$-gram features, \\cite{ye2025mixing} discover predictable functional forms relating mixing ratios to performance, and AIOLI \\citep{chen2025aioli} unifies these into an online adaptive framework.\nThese methods operate at the domain level and do not address instance-level contamination within a domain.\nAt the \\emph{instance} level, SoftDedup \\citep{he2024softdedup} downweights high-frequency samples via $n$-gram commonness, and \\cite{sow2025dynamic} derive sample weights from per-sample loss with convergence guarantees.\nOur reweighting differs from all of these in being driven by \\emph{provenance}---detector scores estimating human vs.\\ machine origin---rather than loss, frequency, or domain membership.\n\n\\paragraph{Theoretical Foundations.}\n\\cite{he2025golden} derive the optimal real-data weight under known mixture proportions, finding the golden-ratio reciprocal (${\\approx}0.62$) optimal when both sources are equally sized; their result requires the contamination ratio, unavailable in web-scale settings.\n\\cite{wang2026survive} prove that contaminated recursive training converges at a rate governed by the effective real-data fraction $\\alpha$, providing the theoretical motivation for our quality threshold: ensuring $\\aeff(b) \\geq \\tau$ guarantees a convergence-rate lower bound.\nWe operationalize this without the known-proportion assumption, estimating $\\aeff$ from batch-level statistics online.\nFor the stability constraint, we build on Kish's effective sample size and the Pareto-smoothed importance sampling framework of \\cite{vehtari2024psis}.\n\\cite{kimura2024iw} provide a broader treatment of importance weighting under distribution shift, within which our provenance-based reweighting can be viewed as covariate-shift correction where the covariate is synthetic origin probability.\n\n\\smallskip\n\\noindent\\textbf{Summary.}\nNo existing method provides principled per-batch exponent selection without validation.\nDrayson et al.\\ use the same $w{=}(1{-}q)^b$ formula but require per-model grid search; Golden Ratio weighting requires known mixture proportions; DoReMi and DSIR operate at the domain level rather than instance-level contamination.\nOur dual-constraint framework fills this gap by deriving the minimum intervention $\\bstar$ from batch-level diagnostics alone.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_intro-related-work_20260515T233142",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper/related_work.tex",
    "content": "% Related Work for \"Minimum Intervention Reweighting: Adaptive Exponent Selection\n% for Contamination-Aware Pretraining\"\n% Generated: 2026-05-15\n% Framing: STABLE (D023 dual-constraint + D029 ESS-only + D035 tau sweep)\n\n\\section{Related Work}\n\\label{sec:related}\n\n\\paragraph{Synthetic Contamination and Model Collapse.}\nTraining on recursively generated data leads to irreversible quality degradation---\\emph{model collapse} \\citep{shumailov2024model}.\n\\cite{alemohammad2024mad} formalize this as Model Autophagy Disorder, showing that quality or diversity inevitably degrades without fresh real data, even when original training data is retained.\nMore critically, \\cite{dohmatob2025strong} prove under scaling-law regimes that even a vanishingly small synthetic fraction (e.g., $1/1000$) suffices to trigger collapse, ruling out data scaling as a remedy.\nWith synthetic content now estimated at 20--60\\% of web corpora \\citep{cheng2025contamination}, these results motivate contamination-aware training strategies that explicitly account for data provenance rather than treating all tokens equally.\n\n\\paragraph{Detect and Reweight.}\nA natural response to contamination is to detect and remove synthetic content.\nDetectGPT \\citep{mitchell2023detectgpt} performs zero-shot detection via probability curvature, while Min-$k$\\% Prob \\citep{shi2024minkprob} uses the average log-probability of the lowest-$k$\\% tokens as a reference-free signal; both produce continuous confidence scores suitable as input to reweighting frameworks.\n\\cite{feng2025beyond} prove that even an imperfect verifier prevents collapse, but apply hard binary filtering that discards borderline samples; \\cite{guo2025escaping} similarly rely on verification-based selection.\nSoft reweighting avoids the precision--recall threshold inherent in hard filtering by assigning continuous weights.\n\nMost directly related to our work, \\cite{drayson2025detection} propose $w_j = (1{-}q_j)^b$ for collapse prevention via detect-and-reweight, where $q_j$ is a detector's synthetic probability.\nWe adopt the same weighting formula but differ in several fundamental ways.\n\\textbf{(i)}~Drayson et al.\\ select $b$ via validation-set grid search and fix it throughout training; different model scales require different values ($b{=}10$ for ${\\leq}360$M parameters, $b{=}1$ for 1.7B), making the choice per-model and expensive.\nOur $\\bstar$ is derived per-batch from dual constraints ($\\aeff \\geq \\tau$, $\\mathrm{ESS} \\geq \\nmin$) at zero validation cost, following a minimum intervention principle that selects the smallest sufficient exponent.\n\\textbf{(ii)}~Their SIR resampling discretizes the weight distribution; we apply direct loss reweighting with continuous gradient contributions.\n\\textbf{(iii)}~They employ a ModernBERT-150M detector (AUC\\,=\\,0.986) on WikiText-2 (${\\sim}$2M tokens); we show that a lightweight TF-IDF+LR detector (AUC\\,=\\,0.939) suffices on FineWeb-scale data (132M+ tokens).\n\n\\paragraph{Data Mixing and Reweighting.}\nA parallel line of work optimizes data composition without targeting synthetic contamination.\nAt the \\emph{domain} level, DoReMi \\citep{xie2023doremi} learns mixture weights via Group DRO with a proxy model, DSIR \\citep{xie2023dsir} performs importance resampling with $n$-gram features, \\cite{ye2025mixing} discover predictable functional forms relating mixing ratios to performance, and AIOLI \\citep{chen2025aioli} unifies these into an online adaptive framework.\nThese methods operate at the domain level and do not address instance-level contamination within a domain.\nAt the \\emph{instance} level, SoftDedup \\citep{he2024softdedup} downweights high-frequency samples via $n$-gram commonness, and \\cite{sow2025dynamic} derive sample weights from per-sample loss with convergence guarantees.\nOur reweighting differs from all of these in being driven by \\emph{provenance}---detector scores estimating human vs.\\ machine origin---rather than loss, frequency, or domain membership.\n\n\\paragraph{Theoretical Foundations.}\n\\cite{he2025golden} derive the optimal real-data weight under known mixture proportions, finding the golden-ratio reciprocal (${\\approx}0.62$) optimal when both sources are equally sized; their result requires the contamination ratio, unavailable in web-scale settings.\n\\cite{wang2026survive} prove that contaminated recursive training converges at a rate governed by the effective real-data fraction $\\alpha$, providing the theoretical motivation for our quality threshold: ensuring $\\aeff(b) \\geq \\tau$ guarantees a convergence-rate lower bound.\nWe operationalize this without the known-proportion assumption, estimating $\\aeff$ from batch-level statistics online.\nFor the stability constraint, we build on Kish's effective sample size and the Pareto-smoothed importance sampling framework of \\cite{vehtari2024psis}.\n\\cite{kimura2024iw} provide a broader treatment of importance weighting under distribution shift, within which our provenance-based reweighting can be viewed as covariate-shift correction where the covariate is synthetic origin probability.\n\n\\smallskip\n\\noindent\\textbf{Summary.}\nNo existing method provides principled per-batch exponent selection without validation.\nDrayson et al.\\ use the same $w{=}(1{-}q)^b$ formula but require per-model grid search; Golden Ratio weighting requires known mixture proportions; DoReMi and DSIR operate at the domain level rather than instance-level contamination.\nOur dual-constraint framework fills this gap by deriving the minimum intervention $\\bstar$ from batch-level diagnostics alone.\n"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-15T23:39:26.620923+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper/related_work.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_intro-related-work_20260515T233142",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-15T23:39:26.621097+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "introduction_tex",
  "type": "paper",
  "description": "Introduction section draft for EMNLP 2026 submission. Covers contamination motivation, dual-constraint framework, minimum intervention principle, key results (adaptive matches grid-best within seed variance, min > max intervention), and 3 contributions.",
  "project": "provenance_weight_training",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper/introduction.tex",
  "tags": "['paper', 'introduction', 'emnlp2026']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_intro-related-work_20260515T233142",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "introduction_tex",
    "type": "paper",
    "description": "Introduction section draft for EMNLP 2026 submission. Covers contamination motivation, dual-constraint framework, minimum intervention principle, key results (adaptive matches grid-best within seed variance, min > max intervention), and 3 contributions.",
    "project": "provenance_weight_training",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper/introduction.tex",
    "tags": "['paper', 'introduction', 'emnlp2026']"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-15T23:39:26.621272+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260515_c6a67f\", \"name\": \"introduction_tex\", \"type\": \"paper\", \"description\": \"Introduction section draft for EMNLP 2026 submission. Covers contamination motivation, dual-constraint framework, minimum intervention principle, key results (adaptive matches grid-best within seed variance, min > max intervention), and 3 contributions.\", \"path\": \"projects/provenance_weight_training/artifacts/_project/paper/introduction_c6a67f.tex\", \"url\": null, \"project\": \"provenance_weight_training\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-15T23:39:08.961160+00:00\", \"tags\": [\"paper\", \"introduction\", \"emnlp2026\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_intro-related-work_20260515T233142",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-15T23:39:26.621408+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "related_work_tex",
  "type": "paper",
  "description": "Related Work section draft for EMNLP 2026 submission. Four groups: Synthetic Contamination/Collapse, Detect and Reweight (Drayson as closest prior work), Data Mixing/Reweighting, Theoretical Foundations. 20 citations total.",
  "project": "provenance_weight_training",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper/related_work.tex",
  "tags": "['paper', 'related_work', 'emnlp2026']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_intro-related-work_20260515T233142",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "related_work_tex",
    "type": "paper",
    "description": "Related Work section draft for EMNLP 2026 submission. Four groups: Synthetic Contamination/Collapse, Detect and Reweight (Drayson as closest prior work), Data Mixing/Reweighting, Theoretical Foundations. 20 citations total.",
    "project": "provenance_weight_training",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper/related_work.tex",
    "tags": "['paper', 'related_work', 'emnlp2026']"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-15T23:39:26.621554+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260515_0b6096\", \"name\": \"related_work_tex\", \"type\": \"paper\", \"description\": \"Related Work section draft for EMNLP 2026 submission. Four groups: Synthetic Contamination/Collapse, Detect and Reweight (Drayson as closest prior work), Data Mixing/Reweighting, Theoretical Foundations. 20 citations total.\", \"path\": \"projects/provenance_weight_training/artifacts/_project/paper/related_work_0b6096.tex\", \"url\": null, \"project\": \"provenance_weight_training\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-15T23:39:11.538211+00:00\", \"tags\": [\"paper\", \"related_work\", \"emnlp2026\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_intro-related-work_20260515T233142",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 29 · 2026-05-15T23:39:26.621736+00:00_

两个文件已完成并注册。

**Introduction** (`paper/introduction.tex`):
- 5 段 + 3 条 contributions，约 1 页
- 开篇：20-60% 污染 + strong collapse 动机
- 中段：Drayson 的 b 需 per-model grid search → 提出 dual-constraint adaptive b*
- 核心公式：b* = inf{b : α_eff(b) ≥ τ} s.t. ESS(b*) ≥ n_min
- 结果：adaptive PPL 17.650±0.007 vs grid-best 17.646±0.007（within seed variance），优于 uniform (17.69) 和 ESS-only (17.73)
- Contributions: (1) dual-constraint framework, (2) matches grid-best + min > max intervention, (3) lightweight detector sufficiency

**Related Work** (`paper/related_work.tex`):
- 4 组 + Summary，约 1 页，20 篇引用
- Group 1: Collapse 动机 (Shumailov, Alemohammad, Dohmatob, Cheng)
- Group 2: Detect-and-reweight，Drayson 作为 closest prior work，3 点差异化 (b 选择/SIR vs loss reweight/检测器规模)
- Group 3: Data mixing (DoReMi, DSIR, Ye, AIOLI) + instance-level (SoftDedup, Sow)，区分 provenance-based vs loss/frequency/domain
- Group 4: 理论基础 (Golden Ratio, Wang convergence, PSIS, IW survey)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_intro-related-work_20260515T233142"
}
```

</details>

---
