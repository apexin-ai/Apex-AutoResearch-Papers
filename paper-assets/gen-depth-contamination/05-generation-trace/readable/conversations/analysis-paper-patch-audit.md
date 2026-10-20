# analysis paper patch audit

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 47
- **Recorded user turns:** 0
- **Tool calls:** 23
- **Original source:** `logs/chats/worker_analysis_paper_patch_audit_20260518T000144.jsonl`
- **Structured JSON:** [`371056f4f20b4423bd37.json`](../../sessions/37/371056f4f20b4423bd37.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

47 recorded events

### Tool call

_source line 1 · 2026-05-18T00:04:33.343224+00:00_

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
  "session": "worker_analysis_paper_patch_audit_20260518T000144",
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

_source line 2 · 2026-05-18T00:04:33.343609+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_patch_audit_20260518T000144",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-18T00:04:33.343830+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "gen-depth-contamination",
  "file": "paper_framing.md",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_patch_audit_20260518T000144",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "gen-depth-contamination",
    "file": "paper_framing.md",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-18T00:04:33.344182+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/paper_framing.md\", \"content\": \"# Paper Framing — gen-depth-contamination\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (ARR submission May 25, 2026)\\n- Fallback: EMNLP 2026 Findings\\n- Backup: AAAI 2027 (abstract July 25, paper August 1)\\n\\n## Canonical Experimental Condition\\n\\n**Continuation mode 是 cross-model 结论的基础。**\\n\\n> \\\"We evaluate both generation modes because real-world recursive contamination can arise from either. Our analysis reveals generation mode as a significant confound, leading us to recommend continuation mode as the canonical condition for cross-model comparisons.\\\"\\n\\n| Condition | Pythia↔OLMo | Qwen↔others | 论文定位 |\\n|-----------|-------------|-------------|---------|\\n| Continuation | 90-92% retention | 80-85% retention | **主实验条件** — cross-model claims 的基础 |\\n| Rewrite (instruction) | N/A | 61-63% retention | **upper bound with mode-specific confound** — 仅作 ablation |\\n\\n**原则**：\\n- C1' 的跨模型 claim 必须基于 continuation mode 数据\\n- Rewrite mode 的高 AUC (0.6957 vs cont 0.6114) 是 mode-specific signal amplification，不能作为泛化性证据\\n- mvp-001 (Qwen-rewrite) 定位为 \\\"pilot study demonstrating feasibility\\\"，后续用 continuation mode rigorously validate\\n- cont→rw 89% vs rw→cont 82% 不对称性 → continuation features 是 rewrite 的通用子集\\n\\n## Core Claims (2+1 结构, updated D049/D050)\\n\\n### Primary: C1' (K* Characterization — Domain-Dependent Bounded Saturation)\\n首次系统测量递归合成文本的 generational discrimination boundary K*，demonstrating that K* is low-bounded (≤3) and domain-dependent。\\n\\nDPI 理论证明有限 K*_theory 必然存在（信息论 impossibility boundary）；我们首次在受控实验中测量 K*_empirical，它提供 K*_theory 的保守下界。通过 8 model configurations（5 architecture families, 1B-8B）、3 source domains（C4, Wikipedia, arXiv）、4 decoding strategies 系统表征 K*_empirical 的行为，发现：\\n\\n- **K*∈{1,2,3} at θ=0.60**：K* 是有界的且域依赖的\\n- **Web text K*=2 是 dominant mode**（7/8 c
…[truncated 11935 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_patch_audit_20260518T000144",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-18T00:04:33.344371+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "gen-depth-contamination",
  "file": "memory.md",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_patch_audit_20260518T000144",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "gen-depth-contamination",
    "file": "memory.md",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-18T00:04:33.344580+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/memory.md\", \"content\": \"# Memory — gen-depth-contamination\\n\\n## 决策与经验\\n\\n### Wikipedia Scorer Confound Confirmed (2026-05-17)\\n- **发现**: Qwen-7B Wikipedia K*=2 是 Qwen-1.5B scorer 的 family bias artifact\\n- Pythia-1.4B scorer 下: 1v2 AUC=0.5870 (< θ=0.60) → K*=1\\n- Qwen-1.5B scorer 下: 1v2 AUC=0.6108 (barely > θ=0.60) → K*=2\\n- **机制**: Qwen scorer 对 Qwen 生成文本有 uniform +0.005~0.027 AUC inflation (family bias)\\n- **影响**: Wikipedia 可能统一为 K*=1（所有模型），等 exp_wiki_scorer_confound_1b5 确认\\n- C4/arXiv 不受影响: C4 已有 cross-scorer 验证(exp_022)；arXiv AUC 远超阈值\\n- **论文调整**: \\\"Qwen uniqueness on Wikipedia\\\" 需改为 \\\"scorer confound caveat\\\"，但核心 story (domain-dependent K*) 反而更 clean: arXiv(3)>C4(2)>Wikipedia(1)\\n\\n### Scorer Confound 预案 — 14B/32B 实验 (2026-05-17)\\n- **触发条件**: exp_14b_c4 或 exp_32b_c4 的 K*=1 时\\n- **操作**: 用 Qwen2.5-14B 作为 scorer（替代 1.5B）重新计算 surprisal features → 重跑 pairwise AUC\\n- **判断**: K* 变为 2 → scorer capacity confound confirmed；K* 仍为 1 → text-intrinsic one-wash\\n- **硬件**: RTX PRO 6000 96GB 装得下 14B scorer\\n- **代码**: run_pipeline.py 的 --scorer_path 已参数化，无需改代码\\n- **32B scorer**: 保守用 14B（14B vs 1.5B 已是 10x capacity gap），32B bf16 ~64GB 可能太紧\\n\\n### JSD Decay Rate λ 解释 K* 变异的机制 (2026-05-17)\\n- JSD 衰减存在两种截然不同的模式: sharp cliff (λ=2.9-6.3) vs gradual decay (λ=0.7-1.2)\\n- **λ 直接映射到 K***: C4 λ≈2.9 → K*=2, Wiki λ≈4.2 → K*=1-2, arXiv(non-OLMo) λ≈1.0 → K*=3\\n- Domain 内 λ 高度一致（C4 上 4 个模型 λ≈2.9），说明衰减速度主要由 domain structure 决定\\n- OLMo 是极端 outlier（cliff 47-50x），所有信息第一步坍塌 → 解释其跨域 K*=1\\n- Retrain-chain 无 cliff 模式（λ=0.285, cliff=1.31x），从根本上不同于 prompt-chain\\n- **论文意义**: 为 K* domain dependence 提供机制解释，不只是观察 K* 不同，而是量化信息坍塌速率\\n\\n### M002: Pipeline skip-if-exists 导致 data reuse bug (2026-05-17)\\n- exp_wiki_pythia 和 exp_wiki_olmo 共享 data_path `data/exp_023_wiki/`（exp-023 Qwen 的数据目录）\\n- run_pipeline.py 的 skip-if-exists 逻辑检测到 depth_*.
…[truncated 4907 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_patch_audit_20260518T000144",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-18T00:04:33.344790+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_patch_audit_20260518T000144",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/paper"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-18T00:04:33.344938+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_patch_audit_20260518T000144",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-18T00:04:33.345062+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/paper*/**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_patch_audit_20260518T000144",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/paper*/**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-18T00:04:33.345192+00:00_

artifacts/_project/paper/method.tex
artifacts/_project/paper/experiments_c1.tex
artifacts/exp_015_neural_probe/paper/neural_probe_analysis.tex
artifacts/exp-006/paper/c3_contingency_versions.tex
docs/paper/tables/tab_filtering_main.tex
docs/paper/tables/tab_alpha_sweep.tex
docs/paper/tables/tab_pairwise_significance.tex
docs/paper/tables/tab_crossscorer.tex
docs/paper/related_work.tex
docs/paper/appendix.tex
docs/paper/conclusion.tex
docs/paper/experiments_c3.tex
artifacts/_project/paper/theta_sensitivity_table.tex
docs/paper/method.tex
docs/paper/main.tex
docs/paper/introduction.tex
docs/paper/appendix_extended.tex
artifacts/_project/paper/tab_domain_model_kstar.tex
artifacts/_project/paper/tab_domain_model_kstar_full.tex
docs/paper/discussion.tex
docs/paper/experiments_c1.tex
docs/paper/tables/tab_domain_model_kstar_full.tex
docs/paper/tables/tab_domain_model_kstar.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_patch_audit_20260518T000144",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-18T00:04:33.345397+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_patch_audit_20260518T000144",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-18T00:04:33.345549+00:00_

artifacts/dream_reports/dream_20260512T200328/best/paper.tex
artifacts/dream_reports/dream_20260512T200328/median/paper.tex
artifacts/dream_reports/dream_20260512T200328/worst/paper.tex
artifacts/dream_reports/dream_20260513T080728/best/paper.tex
artifacts/dream_reports/dream_20260513T080728/median/paper.tex
artifacts/dream_reports/dream_20260513T080728/worst/paper.tex
artifacts/_project/paper/method.tex
artifacts/_project/paper/experiments_c1.tex
artifacts/exp_015_neural_probe/paper/neural_probe_analysis.tex
artifacts/drafts/neural_probe_analysis.tex
artifacts/c3_contingency_versions.tex
artifacts/exp-006/paper/c3_contingency_versions.tex
docs/paper/tables/tab_filtering_main.tex
docs/paper/tables/tab_alpha_sweep.tex
docs/paper/tables/tab_pairwise_significance.tex
docs/paper/tables/tab_crossscorer.tex
artifacts/dream_reports/dream_20260516T073047/best/paper.tex
artifacts/dream_reports/dream_20260516T073047/median/paper.tex
artifacts/dream_reports/dream_20260516T073047/worst/paper.tex
docs/paper/related_work.tex
docs/paper/appendix.tex
docs/paper/conclusion.tex
docs/paper/experiments_c3.tex
artifacts/_project/paper/theta_sensitivity_table.tex
artifacts/theta_sensitivity_table.tex
docs/paper/method.tex
docs/paper/main.tex
docs/paper/introduction.tex
docs/paper/appendix_extended.tex
artifacts/_project/paper/tab_domain_model_kstar.tex
artifacts/_project/paper/tab_domain_model_kstar_full.tex
docs/paper/discussion.tex
docs/paper/experiments_c1.tex
docs/paper/tables/tab_domain_model_kstar_full.tex
docs/paper/tables/tab_domain_model_kstar.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_patch_audit_20260518T000144",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-18T00:04:33.345701+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_patch_audit_20260518T000144",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-18T00:04:33.345928+00:00_

1	% EMNLP 2026 Main — ARR May 2026
2	% Generational Depth Contamination
3	\documentclass[11pt]{article}
4	\usepackage[review]{acl}
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{graphicx}
11	\usepackage{amsmath}
12	\usepackage{amssymb}
13	\usepackage{booktabs}
14	\usepackage{multirow}
15	\usepackage{enumitem}
16	\usepackage{subcaption}
17	\usepackage[section]{placeins}
18	
19	\newcommand{\Kstar}{{K^*}}
20	\newcommand{\Kempirical}{{K^*_{\text{empirical}}}}
21	\newcommand{\Ktheory}{{K^*_{\text{theory}}}}
22	\newcommand{\auc}{\text{AUC}}
23	\newcommand{\jsd}{\text{JSD}}
24	
25	\title{Generational Depth Estimation of Recursive Synthetic Text:\\Measuring the Discrimination Boundary}
26	
27	\author{Anonymous}
28	
29	\begin{document}
30	\maketitle
31	
32	% === Abstract ===
33	\begin{abstract}
34	Web-scale corpora are increasingly contaminated by recursive synthetic content, yet no method estimates a document's generational depth.
35	We measure the discrimination boundary $\Kempirical$ (the maximum depth at which adjacent generations remain distinguishable) using 15 statistical features and an OBD-LightGBM classifier.
36	Across 8 model configurations (5 architecture families, 1B--8B), 3 source domains, and 4 decoding strategies, $\Kempirical \in \{1, 2, 3\}$ at $\theta{=}0.60$ (Cohen's $h{\approx}0.20$): general web text yields $\Kempirical{=}2$ as the dominant mode (7/8 configurations), while structured academic text (arXiv) yields $\Kempirical{=}3$, validated across two architectures (Qwen-1.5B, Pythia-1.4B).
37	A single generation pass suffices to render general web text indistinguishable from deeper synthetic content, a \emph{one-wash laundering} effect.
38	Model-free statistical features enable 80--92\% cross-model transfer with scorer-invariant feature ordering ($\rho > 0.90$), and cross-scorer validation is consistent with $\Kempirical$ being governed by the generation proc
…[truncated 3722 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_patch_audit_20260518T000144",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-18T00:04:33.346109+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_patch_audit_20260518T000144",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-18T00:04:33.346270+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Web-scale text corpora are increasingly contaminated by synthetic content that has itself been generated from earlier synthetic content.
5	Estimates suggest that a substantial fraction of online text is machine-generated~\cite{sun2025aigt, spennemann2025quantifying}, and this share continues to rise.
6	When models train on the outputs of earlier models, the resulting multi-generational synthetic text degrades with each iteration: tail modes vanish, lexical diversity contracts, and surprisal distributions flatten~\cite{shumailov2024collapse, dohmatob2024model}.
7	This degradation arises in both \emph{retrain-chains} (iteratively training on model outputs) and \emph{prompt-chains} (recursively generating from previous outputs without retraining); we study the latter, which isolates generation-level information loss from training dynamics (Appendix~\ref{sec:extended_limitations}).
8	Yet the dominant paradigm treats all machine-generated text identically, discarding the generational depth dimension.
9	
10	This gap cuts across three communities: binary detectors~\cite{basani2026diveye, zhang2024minkpp} produce no depth estimate (Section~\ref{sec:binary_confidence}); membership inference~\cite{zawalski2026codec} addresses a different question; the model collapse literature~\cite{shumailov2024collapse, alemohammad2024selfconsuming, schaeffer2025position} provides no per-text tool; and data selection methods~\cite{xie2023dsir, tirumala2023d4, drayson2025} ignore recursive depth.
11	No existing method estimates how many rounds of recursive generation a text has undergone.
12	
13	The Data Processing Inequality guarantees that information degrades monotonically across generations, motivating a finite discrimination boundary $\Kstar$.
14	We empirically measure $\Kempirical$ (the maximum depth at which a classifier reliably distinguishes adjacent generations) using 15 statistical features and an Ordinal Binary Decompositio
…[truncated 1313 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_patch_audit_20260518T000144",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-18T00:04:33.346419+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_patch_audit_20260518T000144",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-18T00:04:33.346588+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\begin{figure*}[t]
5	\centering
6	\includegraphics[width=\textwidth]{figures/pipeline.pdf}
7	\caption{Generational depth estimation pipeline. Seed documents are recursively passed through a generation operator $G_\delta$ to produce a depth chain. Statistical features are fed to the OBD-LightGBM classifier for depth prediction.}
8	\label{fig:pipeline}
9	\end{figure*}
10	
11	\subsection{Problem Formulation}
12	\label{sec:formulation}
13	
14	A generation operator $G_\delta$ (LLM + decoding strategy $\delta$) produces successive generations $X \to Y_1 \to \cdots \to Y_K$, where $Y_k = G_\delta(Y_{k-1})$ and $Y_0 \triangleq X$ (Figure~\ref{fig:pipeline}).
15	This sequence forms a Markov chain.
16	By the Data Processing Inequality, $I(X; Y_1) \geq I(X; Y_2) \geq \cdots \geq 0$: the original signal degrades monotonically.
17	Together with Markov chain convergence, this guarantees a finite $\Ktheory$ beyond which adjacent generations are indistinguishable.
18	
19	We define the operational lower bound:
20	\begin{equation}
21	  \Kempirical = \max\{k \geq 1 : \auc_{k-1,k} > \theta\},
22	  \label{eq:kstar}
23	\end{equation}
24	where $\auc_{k-1,k}$ is the point-estimate pairwise AUC and $\theta = 0.60$ is a small-effect-size threshold (Cohen's $h \approx 0.20$\footnote{$h = 2\arcsin\!\sqrt{0.60} - 2\arcsin\!\sqrt{0.50} \approx 0.2014$, a ``small'' effect size by Cohen's (1988) convention.}; justified below).
25	Bootstrap 95\% CIs (1{,}000 resamples) provide uncertainty quantification: we verify that boundary-pair CI lower bounds exceed $\theta$ and non-boundary-pair CI upper bounds fall below $\theta$ (Section~\ref{sec:kstar_boundary}).
26	
27	\paragraph{Threshold justification.}
28	$\theta{=}0.60$ is supported by three independent lines of evidence.
29	First, it corresponds to Cohen's $h \approx 0.20$, a conventional small-effect-size boundary.
30	Second, a 10{,}000-iteration permutation test yields a 95th-percentile null of ${<}\,0.
…[truncated 4307 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_patch_audit_20260518T000144",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-18T00:04:33.346746+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_patch_audit_20260518T000144",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-18T00:04:33.346978+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We evaluate generational depth estimation on eight model configurations spanning five architecture families:
5	Pythia-1.4B, OLMo-1B, Qwen2.5-1.5B-Instruct (rewrite and continuation), Qwen2.5-1.5B (base), Qwen2.5-7B, LLaMA-3.1-8B, and Mistral-7B, all in continuation mode except where noted.
6	All experiments use the OBD-LightGBM classifier with the 15-dimensional feature set (Section~\ref{sec:method}), with 5{,}000 texts per depth level (generations 0--5).
7	
8	%% ====================================================================
9	\subsection{$\Kempirical \leq 2$ Across Model Configurations (C4)}
10	\label{sec:kstar_boundary}
11	
12	\begin{table*}[t]
13	\centering
14	\small
15	\caption{Pairwise $\auc$ for adjacent depth pairs with bootstrap 95\% CIs and permutation $p$-values for boundary rows.
16	$\Kempirical = 2$ requires 1v2 $\auc > \theta{=}0.60$ and 2v3 $\auc < \theta$; CIs quantify boundary uncertainty.
17	Extended results (all models) in Table~\ref{tab:kstar_ci_extended}.}
18	\label{tab:kstar_ci}
19	\begin{tabular}{lcccccccccc}
20	\toprule
21	 & \multicolumn{2}{c}{Qwen-rw} & \multicolumn{2}{c}{Pythia} & \multicolumn{2}{c}{OLMo} & \multicolumn{2}{c}{Qwen-cont} & \multicolumn{2}{c}{Qwen-7B\rlap{$^\ddagger$}} \\
22	\cmidrule(lr){2-3}\cmidrule(lr){4-5}\cmidrule(lr){6-7}\cmidrule(lr){8-9}\cmidrule(lr){10-11}
23	 & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI \\
24	\midrule
25	0v1 & .9956 & & .9932 & & .9970 & & .9971 & & .9638 & [.961,\,.967] \\
26	1v2 & .6955 & [.686,\,.704]\rlap{$^*$} & .6539 & [.645,\,.663]\rlap{$^*$} & .6145 & [.605,\,.625]\rlap{$^*$} & .6112 & [.602,\,.621]\rlap{$^*$} & .6168 & [.608,\,.626]\rlap{$^*$} \\
27	2v3 & .5893 & [.580,\,.599] & .5514 & [.542,\,.563] & .5496 & [.540,\,.560] & .5609 & [.551,\,.571] & .5492 & [.539,\,.559] \\
28	3v4 & .5435 & & .5152 & & .5091 & & .5409 & & .5276 & \\
29	4v5 & .5340 & & .5136 & & .5045 & & .5141 & &
…[truncated 11387 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_patch_audit_20260518T000144",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-18T00:04:33.347142+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c3.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_patch_audit_20260518T000144",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c3.tex"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-18T00:04:33.347317+00:00_

1	\section{Application: $\Kstar$-Aware Data Filtering}
2	\label{sec:filtering}
3	
4	$\Kempirical = 2$ makes a falsifiable prediction: binary curation should suffice, and graduated performance should converge toward binary as the decay steepness increases.
5	We compare six strategies on 30{,}000 documents (depths 0--5): (i)~\textbf{no-filter}, (ii)~\textbf{binary-ours} ($w = 1 - P(\text{synthetic})$ from 15D LightGBM), (iii)~\textbf{binary-Drayson}~\citep{drayson2025}, (iv)~\textbf{graduated} ($w = \exp(-\alpha \cdot \hat{d})$, $\alpha \in \{0.1,\ldots,0.9\}$), (v)~\textbf{surprisal} (retain above median), and (vi)~\textbf{DSIR}~\citep{xie2023dsir}.
6	We fine-tune Qwen2.5-1.5B-Instruct via LoRA (rank~8, $\alpha_{\text{LoRA}}{=}16$) for 3 epochs on MMLU and HellaSwag across 5 seeds (51 total runs; this 100\% synthetic setting is an upper bound~\cite{shumailov2024collapse, dohmatob2024model}).
7	
8	\begin{table}[t]
9	\centering
10	\small
11	\caption{Downstream task performance (MMLU, HellaSwag) under six data-filtering strategies. Binary-ours uses the 15D LightGBM depth classifier; Graduated applies exponentially decaying weights $w = \exp(-\alpha \hat{d})$. Mean $\pm$ std over 5 seeds. Full $\alpha$ sweep in Appendix~\ref{sec:extended_limitations}.}
12	\label{tab:tab_filtering_main}
13	\input{tables/tab_filtering_main}
14	\end{table}
15	
16	Binary-ours minimizes MMLU degradation most effectively (Table~\ref{tab:tab_filtering_main}), reducing the gap from $-$1.53\,pp (no-filter) to $-$0.77\,pp (${\sim}$50\% reduction; $p_{\text{corr}} < 0.05$ vs.\ all alternatives).
17	These effects are measured in a 100\% synthetic upper-bound setting; real-world contamination ratios are typically lower, and effect sizes would scale accordingly.
18	The strategy ordering is interpretable through $\Kempirical$: binary filtering exploits the one reliable boundary (0v1), while graduated strategies assign weights to depths 2--5 based on near-random classifier outputs, injecting noise.
19	G
…[truncated 807 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_patch_audit_20260518T000144",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-18T00:04:33.347478+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_patch_audit_20260518T000144",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-18T00:04:33.347704+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	\label{sec:why_kstar}
4	\label{sec:one_wash}
5	\label{sec:negative_graduated}
6	\label{sec:repr_dependence}
7	\label{sec:boundary_cases}
8	\label{sec:length_confound}
9	
10	\begin{figure}[t]
11	\centering
12	\includegraphics[width=\columnwidth]{figures/fig_jsd_decay.pdf}
13	\caption{Token-level JSD between adjacent depth pairs on log scale. Blue band: min-max range across 7 C4 models with $\Kempirical{=}2$; dashed purple: Mistral-7B ($\Kempirical{=}1$, cross-scorer validated); green: arXiv Pythia ($\Kempirical{=}3$); dotted red: retrain-chain ($\Kempirical{\geq}4$). C4 models exhibit a sharp cliff ($\lambda \approx 2.2$--$3.5$), while arXiv decays gradually ($\lambda \approx 1.0$) and retrain-chain shows no cliff ($\lambda = 0.285$).}
14	\label{fig:jsd_decay}
15	\end{figure}
16	
17	\paragraph{One-wash laundering (web text).}
18	For general web text, $\Kempirical{=}2$ reflects concentrated information loss: 0v1 is near-trivially separable ($\auc \geq 0.92$), 1v2 drops by ${\sim}$30\,pp, and 2v3 falls below $\theta$.
19	A single generation pass renders text indistinguishable from multiply recycled content, limiting depth-aware curation to a binary boundary.
20	Converging evidence supports a data-intrinsic interpretation: OBD achieves 96\% depth-0 recall but only 14--22\% for depths 2--4; frontier LLMs show 8--38\% (McNemar $p > 0.05$ vs.\ OBD; Table~\ref{tab:s3_llm_zeroshot}).
21	
22	\paragraph{JSD decay and the discrimination boundary.}
23	The token-level JSD between adjacent generations reveals two distinct decay regimes (Figure~\ref{fig:jsd_decay}).
24	For C4 web text, 0v1 JSD exceeds 1v2 by 6--56$\times$ across all 7 models with $\Kempirical{=}2$ (median cliff ratio ${\sim}$15$\times$), and subsequent pairs converge to a noise floor of ${\sim}$0.003--0.005.
25	Fitting $\jsd(k, k{+}1) \propto e^{-\lambda k}$ yields $\lambda \approx 2.2$--$3.5$ for C4 (mean ${\approx}\,2.9$), consistent with rapid mixing of $G_\delta
…[truncated 6926 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_patch_audit_20260518T000144",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-18T00:04:33.347921+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_patch_audit_20260518T000144",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-18T00:04:33.348072+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Model collapse and recursive degradation.}
5	Iterative training on model outputs causes tail-distribution degradation~\cite{shumailov2024collapse, alemohammad2024selfconsuming, dohmatob2024model, dohmatob2025strong}, diversity contraction~\cite{guo2024curious, padmakumar2024writing, briesch2023selfconsuming}, and predictable convergence~\cite{schaeffer2025position, kazdan2025collapse, gerstgrasser2024model}.
6	Our prompt-chain operates in the replace regime~\cite{kazdan2025collapse}, making $\Kempirical = 2$ a conservative lower bound.
7	This literature characterizes macro dynamics but provides no per-text depth estimation, the gap we address.
8	
9	\paragraph{Beyond binary detection.}
10	Binary detectors~\cite{mitchell2023detectgpt, bao2024fast, hans2024binoculars, basani2026diveye, zhang2024minkpp} achieve strong human-vs.-machine separation but produce no depth estimate.
11	Recent work extends beyond binary labels to collaboration degree~\cite{cheng2025beyond}, contamination hierarchies~\cite{mehta2025beyond}, and multigenerator benchmarks~\cite{wang2024semeval}; robustness concerns arise under paraphrasing~\cite{sadasivan2023detect, krishna2023paraphrasing} and cross-mode transfer~\cite{hao2025rewrite}; CoDeC~\cite{zawalski2026codec} addresses contamination via membership inference.
12	None estimates recursive generation depth.
13	
14	\paragraph{Data selection and curation.}
15	DSIR~\cite{xie2023dsir}, D4~\cite{tirumala2023d4}, and DoReMi~\cite{xie2023doremi} are depth-agnostic; Drayson et al.~\cite{drayson2025} combined binary detection with importance resampling, a special case when $\Kstar = 1$.
16	
17	\paragraph{Ordinal classification and probing.}
18	Our OBD classifier follows Frank \& Hall's~\cite{frank2001ordinal} binary decomposition; our neural probe extends probing~\cite{alain2017understanding, belinkov2022probing} to the discrimination boundary.
19	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_patch_audit_20260518T000144",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-18T00:04:33.348214+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_patch_audit_20260518T000144",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-18T00:04:33.348344+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We measure the generational depth discrimination boundary $\Kempirical$ for recursive synthetic text.
5	$\Kempirical \in \{1, 2, 3\}$ depends on source domain and model characteristics: general web text yields $\Kempirical{=}2$ across 7/8 configurations (5 families, 1B--8B; $p \leq 0.002$), with $\Kempirical{=}3$ for academic text, confirmed across architectures (Qwen-1.5B, Pythia-1.4B).
6	Model-free features enable 80--92\% cross-model transfer ($\rho > 0.90$), and under sufficient contamination, domain-appropriate $\Kempirical$ correctly predicts optimal curation granularity.
7	Future work includes scaling to 13B+, additional structured domains, and retrain-chain $\Kstar$ characterization.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_patch_audit_20260518T000144",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-18T00:04:33.348467+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_patch_audit_20260518T000144",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-18T00:04:33.348899+00:00_

1	\appendix
2	\section{Supplementary Figures}
3	
4	\begin{figure}[t]
5	\centering
6	\includegraphics[width=\columnwidth]{figures/fig_filtering_strategies.pdf}
7	\caption{Downstream performance of all filtering strategies (5 seeds, $\pm$1 std). Binary-ours (green) minimizes MMLU degradation; graduated $\alpha$ sweep shows monotonic convergence toward binary. Dashed line: base model (no fine-tuning).}
8	\label{fig:filtering_strategies}
9	\end{figure}
10	
11	\begin{figure}[t]
12	  \centering
13	  \includegraphics[width=\columnwidth]{figures/fig_s1_auc_decay_ci.pdf}
14	  \caption{Pairwise $\auc$ decay curves for five model-mode configurations with bootstrap 95\% confidence intervals. Error bars computed from 1{,}000 bootstrap resamples. The shaded region marks the $\Kempirical=2$ boundary where $\auc$ drops below $\theta=0.60$. This figure complements Figure~\ref{fig:auc_decay} in the main text by showing statistical uncertainty for each measurement point.}
15	  \label{fig:s1_auc_decay_ci}
16	\end{figure}
17	
18	\section{Supplementary Tables}
19	
20	%%% Feature ranking table (moved from main text)
21	\begin{table}[t]
22	\centering
23	\small
24	\caption{Top-3 features by single-feature $\auc$ ranking. Bold: shared across all continuation-mode models. Spearman $\rho$ (continuation pairs): Pythia--OLMo 0.95, Pythia--Qwen-cont 0.91, OLMo--Qwen-cont 0.85.}
25	\label{tab:top_features}
26	\begin{tabular}{cllll}
27	\toprule
28	Rank & Pythia & OLMo & Qwen-rw & Qwen-cont \\
29	\midrule
30	1 & \textbf{\texttt{surp\_d1\_std}} & \textbf{\texttt{surp\_std}} & \texttt{freq\_entropy} & \textbf{\texttt{surp\_d1\_std}} \\
31	2 & \textbf{\texttt{surp\_d2\_std}} & \textbf{\texttt{surp\_d1\_std}} & \textbf{\texttt{surp\_std}} & \textbf{\texttt{surp\_std}} \\
32	3 & \textbf{\texttt{surp\_std}} & \textbf{\texttt{surp\_d2\_std}} & \textbf{\texttt{surp\_d1\_std}} & \textbf{\texttt{surp\_d2\_std}} \\
33	\bottomrule
34	\end{tabular}
35	\end{table}
36	
37	%%% Table S1: Cross-Transfer Confusion Mat
…[truncated 25446 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_patch_audit_20260518T000144",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-18T00:04:33.349082+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_patch_audit_20260518T000144",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-18T00:04:33.349321+00:00_

1	\section{Extended Discussion}
2	\label{sec:extended_discussion}
3	
4	\subsection{Theoretical Implications of $\Kempirical = 2$}
5	
6	The DPI guarantees a finite $\Ktheory$; for general web text, $\Kempirical \leq 2$ across all 8 configurations (1B--8B, 5 families), while structured domains (arXiv) yield $\Kempirical{=}3$, aligning with model collapse convergence~\cite{shumailov2024collapse, dohmatob2024model, alemohammad2024selfconsuming}.
7	Decoding strategy modestly affects signal strength (1v2 $\auc \in [0.6866, 0.7039]$) but does not shift the boundary.
8	
9	\subsection{Cross-Model Transfer Implications}
10	
11	Cross-model classification retains 80--92\% accuracy with scorer-invariant feature rankings ($\rho > 0.90$), enabling single-classifier deployment across generators.
12	Absolute discriminability at the $\Kempirical$ boundary is scorer-sensitive: alternative scorers reduce Qwen-continuation $\Kempirical$ from 2 to 1, while rewrite-mode $\Kempirical = 2$ is preserved.
13	Model family similarity modulates transfer (Pythia$\leftrightarrow$OLMo: 90--92\% vs.\ Qwen-cont$\leftrightarrow$OLMo: 80--85\%).
14	
15	\begin{minipage}{\columnwidth}
16	\centering
17	\captionof{table}{Cross-scorer validation on Qwen-generated text. Alternative scorers (Pythia-1.4B, OLMo-1B) preserve feature ranking ($\rho > 0.90$) and rewrite-mode $\Kempirical = 2$, but reduce continuation-mode $\Kempirical$ from 2 to 1.}
18	\label{tab:crossscorer}
19	\resizebox{\columnwidth}{!}{\input{tables/tab_crossscorer}}
20	\end{minipage}
21	
22	\begin{table}[h]
23	\centering
24	\small
25	\caption{Three-way ANOVA (Generator $\times$ Scorer $\times$ Depth-Pair) on per-fold pairwise $\auc$ values. DV = per-fold AUC; $N{=}400$ (16 cells $\times$ 5 folds $\times$ 5 depth-pairs). The non-significant Scorer main effect is consistent with scorer independence of depth discrimination.}
26	\label{tab:anova_crossscorer}
27	\begin{tabular}{lrrrr}
28	\toprule
29	\textbf{Source} & \textbf{df} & $F$ & $p$ & $\et
…[truncated 14821 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_patch_audit_20260518T000144",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-18T00:04:33.349479+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/tables/tab_domain_model_kstar.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_patch_audit_20260518T000144",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/tables/tab_domain_model_kstar.tex"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-18T00:04:33.349621+00:00_

1	\begin{table}[t]
2	\centering
3	\caption{Generative depth $K^*$ across domains and models (scorer: Qwen2.5-1.5B, $\theta{=}0.60$). Bold values indicate the dominant mode per domain. $K^*$ is remarkably consistent within each domain: C4 yields $K^*{=}2$, arXiv yields $K^*{=}3$, and Wikipedia yields $K^*{=}1$, confirming that generative depth is domain-dependent and low-bounded.}
4	\label{tab:domain_model_kstar}
5	{\small
6	\begin{tabular}{llccc}
7	\toprule
8	\textbf{Model} & \textbf{Size} & \textbf{C4}~$K^*$ & \textbf{arXiv}~$K^*$ & \textbf{Wiki}~$K^*$ \\
9	\midrule
10	Qwen2.5       & 1.5B & \textbf{2} & \textbf{3} & \textbf{1}\textsuperscript{$\dagger$} \\
11	Qwen2.5       & 7B   & \textbf{2} & \textbf{3} & \textbf{1}\textsuperscript{$\dagger$} \\
12	Pythia        & 1.4B & \textbf{2} & \textbf{3} & \textbf{1} \\
13	LLaMA-3.1    & 8B   & \textbf{2} & \textbf{3} & \textbf{1} \\
14	Mistral       & 7B   & 1\textsuperscript{$\ddagger$} & \textbf{3} & \textbf{1} \\
15	OLMo          & 1B   & \textbf{2} & 1\textsuperscript{$*$} & \textbf{1} \\
16	\midrule
17	\textit{Dominant} & & \textbf{2} & \textbf{3} & \textbf{1} \\
18	\bottomrule
19	\end{tabular}
20	}
21	\vspace{2pt}
22	
23	{\footnotesize
24	\textsuperscript{$\dagger$}Scorer artifact: Qwen-1.5B scorer yields $K^*{=}2$; Pythia scorer yields $K^*{=}1$ (see \S\ref{sec:crossscorer}).\\
25	\textsuperscript{$\ddagger$}Domain-specific one-wash: AUC(1v2)${=}0.594{<}\theta$; arXiv rescues to $K^*{=}3$. Cross-scorer validated: Pythia-1.4B also yields $K^*{=}1$ (AUC${=}0.570$).\\
26	\textsuperscript{$*$}Capacity failure: OLMo-1B generates out-of-domain text on arXiv.
27	}
28	\end{table}
29	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_patch_audit_20260518T000144",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-18T00:04:33.349763+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/tables/tab_domain_model_kstar_full.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_patch_audit_20260518T000144",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/tables/tab_domain_model_kstar_full.tex"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-18T00:04:33.349930+00:00_

1	\begin{table*}[t]
2	\centering
3	\caption{Full generative depth results with AUC at the $K^*$ boundary (scorer: Qwen2.5-1.5B, $\theta{=}0.60$). AUC($k$v$k{+}1$) denotes the area under the ROC curve distinguishing generation $k$ from generation $k{+}1$. Bold indicates the dominant $K^*$ mode per domain. All AUC values computed on held-out test splits ($n{=}500$ per class).}
4	\label{tab:domain_model_kstar_full}
5	{\small
6	\begin{tabular}{llcccccc}
7	\toprule
8	& & \multicolumn{2}{c}{\textbf{C4}} & \multicolumn{2}{c}{\textbf{arXiv}} & \multicolumn{2}{c}{\textbf{Wikipedia}} \\
9	\cmidrule(lr){3-4} \cmidrule(lr){5-6} \cmidrule(lr){7-8}
10	\textbf{Model} & \textbf{Size} & $K^*$ & AUC(boundary) & $K^*$ & AUC(boundary) & $K^*$ & AUC(boundary) \\
11	\midrule
12	Qwen2.5       & 1.5B & \textbf{2} & 0.6262~(1v2) & \textbf{3} & 0.6427~(2v3) & \textbf{1}\textsuperscript{$\dagger$} & --- \\
13	Qwen2.5       & 7B   & \textbf{2} & 0.6178~(1v2) & \textbf{3} & 0.6255~(2v3) & \textbf{1}\textsuperscript{$\dagger$} & --- \\
14	Pythia        & 1.4B & \textbf{2} & 0.6539~(1v2) & \textbf{3} & 0.6544~(2v3) & \textbf{1} & --- \\
15	LLaMA-3.1    & 8B   & \textbf{2} & 0.6123~(1v2) & \textbf{3} & 0.6215~(2v3) & \textbf{1} & --- \\
16	Mistral       & 7B   & 1\textsuperscript{$\ddagger$} & 0.594~(1v2) & \textbf{3} & 0.6275~(2v3) & \textbf{1} & --- \\
17	OLMo          & 1B   & \textbf{2} & 0.6145~(1v2) & 1\textsuperscript{$*$} & --- & \textbf{1} & --- \\
18	\bottomrule
19	\end{tabular}
20	}
21	\vspace{2pt}
22	
23	{\footnotesize
24	\textsuperscript{$\dagger$}Scorer artifact: cross-scorer analysis (Appendix~\ref{app:crossscorer}) shows $K^*$ depends on scorer choice for Wiki with Qwen generators.\\
25	\textsuperscript{$\ddagger$}AUC(1v2)${=}0.594{<}\theta{=}0.60$: Mistral exhibits domain-specific one-wash on C4 web text. Cross-scorer validated: Pythia-1.4B also yields $K^*{=}1$ (AUC${=}0.570$).\\
26	\textsuperscript{$*$}Capacity failure: OLMo-1B produces out-of-domain text when prompted with arXi
…[truncated 35 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_patch_audit_20260518T000144",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-18T00:04:33.350074+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/tables/tab_crossscorer.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_patch_audit_20260518T000144",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/tables/tab_crossscorer.tex"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-18T00:04:33.350208+00:00_

1	{\small
2	\begin{tabular}{llcccc}
3	\toprule
4	\textbf{Scorer} & \textbf{Gen.\ Data} & $\boldsymbol{K^*}$ & \textbf{AUC(0v1)} & \textbf{AUC(1v2)} & \textbf{Spearman}~$\boldsymbol{\rho}$ \\
5	\midrule
6	% --- Qwen-RW block ---
7	Qwen-1.5B (self) & Qwen-RW & 2 & --- & 0.6955 & --- \\
8	Pythia-1.4B       & Qwen-RW & 2 & 0.9923 & 0.7012 & 0.906 \\
9	OLMo-1B           & Qwen-RW & 2 & 0.9918 & 0.6947 & 0.920 \\
10	\midrule
11	% --- Qwen-cont block ---
12	Qwen-1.5B (self) & Qwen-cont & 2 & --- & 0.6112 & --- \\
13	Pythia-1.4B       & Qwen-cont & \textcolor{red}{1\textsuperscript{$\dagger$}} & 0.9900 & \underline{0.5923} & 0.942 \\
14	OLMo-1B           & Qwen-cont & \textcolor{red}{1\textsuperscript{$\dagger$}} & 0.9890 & \underline{0.5858} & 0.902 \\
15	\midrule
16	% --- Qwen-7B cross-scale block ---
17	Qwen-1.5B        & Qwen-7B-cont & 2 & 0.9644 & 0.6178 & --- \\
18	\bottomrule
19	\end{tabular}
20	}
21	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_patch_audit_20260518T000144",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-18T00:04:33.350354+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/tables/tab_filtering_main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_patch_audit_20260518T000144",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/tables/tab_filtering_main.tex"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-18T00:04:33.350483+00:00_

1	\begin{tabular}{lcc}
2	\toprule
3	\textbf{Strategy} & \textbf{MMLU} & \textbf{HellaSwag} \\
4	\midrule
5	Base model (no training) & 0.6018 & 0.6821 \\
6	\midrule
7	Binary-ours ($\Kstar{=}2$) & \textbf{0.5941}$\pm$0.0008 & \textbf{0.6701}$\pm$0.0006 \\
8	Binary-Drayson & 0.5913$\pm$0.0009 & 0.6691$\pm$0.0004 \\
9	Surprisal & 0.5894$\pm$0.0009 & 0.6641$\pm$0.0006 \\
10	Graduated ($\alpha{=}0.9$) & 0.5892$\pm$0.0008 & 0.6701$\pm$0.0007 \\
11	DSIR & 0.5869$\pm$0.0003 & 0.6631$\pm$0.0007 \\
12	No filter & 0.5865$\pm$0.0010 & 0.6638$\pm$0.0008 \\
13	\bottomrule
14	\end{tabular}
15	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_patch_audit_20260518T000144",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-18T00:04:33.350616+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/",
  "description": "List artifacts directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_patch_audit_20260518T000144",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/",
    "description": "List artifacts directory"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-18T00:04:33.350745+00:00_

_project
bootstrap_ci_4model.json
borderline_bootstrap_ci.json
c3_contingency_versions.tex
c3_fallback_outline.md
discussion_outline.md
drafts
dream_reports
exp-004
exp-005
exp-006
exp-013
exp-019
exp-024
exp-D
exp005_4model_tau_matrix.json
exp006_analyze.py
exp006_continued_pretraining.py
exp006_evaluate.py
exp006_filtering_strategies.py
exp008_retrain_chain.py
exp012_binary_confidence.py
exp012_ppl_depth_correlation.py
exp016_bootstrap_ci.json
exp025_bootstrap_ci.json
exp026_feature_stability.json
exp_003_decoding_ablation
exp_006_graduated_filtering
exp_007_bootstrap_ci
exp_015_neural_probe
exp_016_base_vs_instruct
exp_019_mistral7b_depth
exp_019b_mistral_cross_scorer
exp_020_pythia_decoding
exp_022_cross_scorer_matrix
exp_023_wiki_domain
exp_024_arxiv_domain
exp_025_pythia_arxiv
exp_026
exp_026_feature_stability
exp_027
exp_B_14d_ablation.json
exp_C_permutation_10k.json
exp_D_obd_n500.json
exp_arXiv_qwen7b
exp_arXiv_qwen7b_analysis.md
exp_wiki_llama8b
exp_wiki_mistral7b
exp_wiki_qwen7b
exp_wiki_scorer_confound
fig2_auc_decay.pdf
fig2_auc_decay.png
fig3_transfer_heatmap.pdf
fig3_transfer_heatmap.png
figures
gen_pipeline_figure.py
gen_theta_sensitivity.py
gpu_optimization_report.txt
literature_positioning_notes.md
literature_scan_2025_2026.md
main.pdf
manifest.yaml
paper_consistency_audit.md
rebuttal
review_issues.yaml
review_reports
run_exp004_qwen7b_depth.py
run_exp006.sh
scripts
summary_auc_decay
theta_sensitivity_analysis.md
theta_sensitivity_table.csv
theta_sensitivity_table.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_patch_audit_20260518T000144",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-18T00:04:33.350938+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/paper_patch_audit.md",
  "content": "# Paper Comprehensive Patch Audit\n\n**Date**: 2026-05-18  \n**Context**: D060 scorer confound resolution, 5-model arXiv cross-validation, 6×3 Domain×Model matrix complete  \n**DDL**: EMNLP 2026 ARR May 25 (7 days)\n\n---\n\n## Summary of Current State\n\nThe paper is **largely up-to-date**. The D060 scorer confound, 6×3 matrix, Mistral case study, JSD decay, and Wikipedia resolution are all correctly reflected in the current `.tex` files. The main gaps are:\n\n1. Outdated arXiv description in Abstract/Conclusion (says \"two architectures\" instead of five)\n2. Missing LLaMA-8B and Mistral-7B data in extended CI table (shows \"---\")\n3. Scale validation (14B/32B) pending results not yet incorporated\n4. Minor wording updates to match paper_framing.md precision\n\n---\n\n## P0: Must Fix (factual errors or significant omissions)\n\n### 1. Abstract: arXiv cross-validation count outdated\n- **File**: `docs/paper/main.tex`, line 36\n- **Current**: `\"validated across two architectures (Qwen-1.5B, Pythia-1.4B)\"`\n- **Should be**: `\"validated across five models spanning four architecture families (1.4B--8B)\"`\n- **Reason**: paper_framing.md confirms 5-model cross-validation (Qwen-1.5B, Qwen-7B, Pythia-1.4B, LLaMA-8B, Mistral-7B). The \"two architectures\" is D055-era language.\n\n### 2. Conclusion: same outdated arXiv count\n- **File**: `docs/paper/conclusion.tex`, line 5\n- **Current**: `\"confirmed across architectures (Qwen-1.5B, Pythia-1.4B)\"`\n- **Should be**: `\"confirmed across five models (four architecture families, 1.4B--8B)\"`\n- **Reason**: Same as above.\n\n### 3. Limitations: arXiv scope description outdated\n- **File**: `docs/paper/main.tex`, line 68\n- **Current**: `\"arXiv $\\Kempirical{=}3$ is confirmed with two model families (Qwen-1.5B, Pythia-1.4B) but with reduced sample size ($n{=}2{,}200$ per model)\"`\n- **Should be**: `\"arXiv $\\Kempirical{=}3$ is confirmed with five models spanning four architecture families (Qwen-1.5B, Qwen-7B, Pythia-1.4B, LLaMA-8B, Mistral-7B; $n{=}2{,}200$ per model)\"`\n- **Reason**: 5-model validation completed (D055/D056/D057). Reduced sample size caveat still applies.\n\n### 4. Extended CI Table (Tab S2b): LLaMA-8B and Mistral-7B columns empty\n- **File**: `docs/paper/appendix.tex`, lines 93-115 (tab:kstar_ci_extended)\n- **Current**: LLaMA-8B column shows all \"---\"; Mistral-7B is not even present in the table\n- **Should be**: \n  - LLaMA-8B: 0v1=0.9225, 1v2=0.6123 [0.603, 0.622], 2v3~0.56, etc.\n  - Add Mistral-7B column: 0v1=~0.93, 1v2=0.5935 [0.584, 0.603], K*=1\n- **Reason**: These experiments completed (exp-018, exp-019). The main text references them but the extended table has placeholders.\n\n### 5. Pythia Decoding Table (Tab S10) entirely empty\n- **File**: `docs/paper/appendix.tex`, lines 405-424 (tab:s10_pythia_decoding)\n- **Current**: All cells show \"---\"\n- **Should be**: Fill with exp-020 results (greedy: repetition-collapsed 1v2~0.884; nuc p=0.9, T=0.7, T=1.2 values)\n- **Reason**: exp-020 completed. Caption references the data but cells are placeholders.\n\n### 6. Domain Ablation Table (Tab S12) entirely empty\n- **File**: `docs/paper/appendix.tex`, lines 449-469 (tab:s12_domain_ablation)\n- **Current**: All cells show \"---\"\n- **Should be**: Fill with Qwen-1.5B continuation data for C4/Wikipedia/arXiv from exp-023/exp-024\n- **Reason**: All domain experiments completed. The main-text tab:domain_kstar has the summary but this detailed table is unfilled.\n\n---\n\n## P1: Should Fix (strengthens narrative or fixes inconsistencies)\n\n### 7. Introduction contribution (b): still says \"two architectures\"\n- **File**: `docs/paper/introduction.tex`, line 21\n- **Current**: `\"consistent across model families\"`\n- **Should be**: `\"consistent across five models spanning four architecture families (1.4B--8B)\"`\n- **Reason**: The Introduction contribution list should match the Abstract and paper_framing.md precision. Current wording is vague but not wrong.\n\n### 8. Theta sensitivity table: missing arXiv entries for LLaMA/Mistral/Qwen-7B\n- **File**: `docs/paper/appendix_extended.tex`, lines 96-120 (tab:theta_sensitivity)\n- **Current**: Only shows arXiv rows for Qwen-1.5B-base and Pythia-1.4B\n- **Should be**: Add rows for LLaMA-8B, Mistral-7B, Qwen-7B on arXiv (all K*=3 at theta=0.60)\n- **Reason**: 5-model validation data available; showing only 2 is inconsistent with main text claim.\n\n### 9. experiments_c1.tex arXiv paragraph: claims \"five-model\" but body still leads with Qwen/Pythia\n- **File**: `docs/paper/experiments_c1.tex`, lines 123-128\n- **Current**: Correctly states 5-model validation and lists all models. Good.\n- **Note**: This section is already updated. No change needed.\n\n### 10. Method section experimental setup table (tab:setup): missing LLaMA-8B and Mistral-7B\n- **File**: `docs/paper/method.tex`, lines 56-73 (tab:setup)\n- **Current**: Lists only 6 configs (Qwen-rw, Qwen-cont, Qwen-base, Pythia, OLMo, Qwen-7B)\n- **Should be**: Add LLaMA-3.1-8B and Mistral-7B rows (both continuation mode, C4 5000 seeds)\n- **Reason**: Main text and abstract claim \"8 model configurations\" but setup table only shows 6. This is a factual mismatch the reviewer will notice.\n\n### 11. JSD decay figure: verify 7 models are shown\n- **File**: `docs/paper/discussion.tex`, line 13 (fig:jsd_decay caption)\n- **Current**: Caption says \"7 C4 models with K*=2\" and \"dashed purple: Mistral-7B\"\n- **Verify**: The figure file needs to include all 7 C4 models. If it was generated before LLaMA-8B data arrived, it may only show 5-6 models.\n- **Action**: Regenerate `figures/fig_jsd_decay.pdf` with all 7 C4 model curves + Mistral + arXiv + retrain-chain\n\n### 12. Scorer Sensitivity Table (Tab S13): mostly \"---\" entries\n- **File**: `docs/paper/appendix.tex`, lines 472-492 (tab:s13_scorer_sensitivity)\n- **Current**: Only Qwen-RW, Qwen-cont, Qwen-base have cross-scorer data. Pythia, OLMo, Qwen-7B, Mistral show \"---\"\n- **Should be**: exp-022 provides cross-scorer data for multiple generators. Fill what's available.\n- **Reason**: Partially filled table looks unfinished.\n\n### 13. Discussion \"Scorer sensitivity\" paragraph: mention Wikipedia resolution explicitly\n- **File**: `docs/paper/discussion.tex`, lines 66-68\n- **Current**: Already mentions Wikipedia scorer confound and recommends cross-family validation. Good.\n- **Note**: This section is already updated. No change needed.\n\n### 14. Scale validation (14B/32B) mention\n- **File**: `docs/paper/main.tex`, lines 68-70 (Limitations) and `conclusion.tex` line 7\n- **Current**: \"Scope: model scale ≤8B\"; Conclusion: \"Future work includes scaling to 13B+\"\n- **Should be**: If 14B/32B results arrive before submission, update Limitations scope and add one sentence to Discussion about scale. If not, current language is fine.\n- **Action**: Conditional on experiment completion before May 25.\n\n---\n\n## P2: Optional Improvements (polish)\n\n### 15. Abstract: add Wikipedia K*=1 to complete the domain hierarchy\n- **File**: `docs/paper/main.tex`, line 36\n- **Current**: Only mentions C4 K*=2 and arXiv K*=3\n- **Could add**: Brief mention of domain ordering: \"arXiv (K*=3) > C4 (K*=2) > Wikipedia (K*=1)\"\n- **Reason**: The clean three-level hierarchy is the headline finding post-D060. Space permitting, it strengthens the Abstract.\n\n### 16. Discussion: add explicit mention of \"two types of one-wash\"\n- **File**: `docs/paper/discussion.tex`, around lines 17-19 and 59-63\n- **Current**: Discusses Mistral domain-rescue and OLMo capacity failure separately\n- **Could add**: A sentence explicitly naming the distinction: \"One-wash arises from two distinct mechanisms: domain-dependent (Mistral, rescued by arXiv) and model-intrinsic (OLMo, K*=1 across all domains).\"\n- **Reason**: paper_framing.md emphasizes this as a key insight; the paper discusses it implicitly but never names the two-type taxonomy explicitly.\n\n### 17. Appendix extended discussion: lambda values could cite memory.md numbers\n- **File**: `docs/paper/discussion.tex`, lines 23-32\n- **Current**: Already mentions C4 lambda~2.9, arXiv lambda~1.0, Wikipedia lambda~3.1. Good.\n- **Note**: Numbers match memory.md. No change needed.\n\n### 18. Appendix Tab S12: caption says \"Qwen2.5-1.5B-Instruct, continuation mode\" but should reflect all 6 models\n- **File**: `docs/paper/appendix.tex`, line 453\n- **Current**: Caption scoped to single model\n- **Should be**: If filling with multi-model data, update caption accordingly. Or keep as single-model detail table and reference main-text tab:domain_kstar for full matrix.\n\n### 19. Ethics Statement: add Wikipedia and arXiv to data sources\n- **File**: `docs/paper/main.tex`, line 81\n- **Current**: \"Our experiments use the publicly available C4 corpus\"\n- **Should be**: \"Our experiments use publicly available corpora (C4, Wikipedia, arXiv abstracts)\"\n- **Reason**: Paper now uses 3 domains but Ethics only mentions C4.\n\n---\n\n## Priority Summary\n\n| Priority | Count | Items |\n|----------|-------|-------|\n| P0 (must fix) | 6 | #1, #2, #3, #4, #5, #6 |\n| P1 (should fix) | 8 | #7, #8, #10, #11, #12, #13, #14 (conditional) |\n| P2 (optional) | 5 | #15, #16, #17, #18, #19 |\n\n## Recommended Execution Order\n\n1. **First pass (P0, ~2h)**: Fix factual counts (#1, #2, #3, #7), add method table rows (#10), fill appendix data tables (#4, #5, #6)\n2. **Second pass (P1, ~2h)**: Update theta sensitivity table (#8), regenerate JSD figure (#11), fill scorer table (#12)\n3. **Third pass (P2, ~1h)**: Abstract domain hierarchy (#15), two-type one-wash (#16), Ethics (#19)\n4. **Conditional**: If 14B/32B results arrive, add to Discussion (#14)\n\n## Already Correct (no change needed)\n\n- experiments_c1.tex Section 4.5 (Cross-Domain Variation): correctly describes 5-model arXiv, 6-model Wikipedia, scorer confound, clean domain ordering\n- tab:domain_kstar (inline in experiments_c1.tex): 6×3 matrix with footnotes for scorer artifact, capacity failure, one-wash\n- tab:domain_model_kstar.tex and tab_domain_model_kstar_full.tex: correctly formatted with all 6 models\n- Discussion JSD paragraph: lambda values match memory.md\n- Discussion scorer sensitivity paragraph: correctly describes Wikipedia confound\n- appendix_extended.tex Wiki Domain section: correctly resolves the confound with detailed table\n- Dose-response section: complete with table and analysis\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_patch_audit_20260518T000144",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/paper_patch_audit.md",
    "content": "# Paper Comprehensive Patch Audit\n\n**Date**: 2026-05-18  \n**Context**: D060 scorer confound resolution, 5-model arXiv cross-validation, 6×3 Domain×Model matrix complete  \n**DDL**: EMNLP 2026 ARR May 25 (7 days)\n\n---\n\n## Summary of Current State\n\nThe paper is **largely up-to-date**. The D060 scorer confound, 6×3 matrix, Mistral case study, JSD decay, and Wikipedia resolution are all correctly reflected in the current `.tex` files. The main gaps are:\n\n1. Outdated arXiv description in Abstract/Conclusion (says \"two architectures\" instead of five)\n2. Missing LLaMA-8B and Mistral-7B data in extended CI table (shows \"---\")\n3. Scale validation (14B/32B) pending results not yet incorporated\n4. Minor wording updates to match paper_framing.md precision\n\n---\n\n## P0: Must Fix (factual errors or significant omissions)\n\n### 1. Abstract: arXiv cross-validation count outdated\n- **File**: `docs/paper/main.tex`, line 36\n- **Current**: `\"validated across two architectures (Qwen-1.5B, Pythia-1.4B)\"`\n- **Should be**: `\"validated across five models spanning four architecture families (1.4B--8B)\"`\n- **Reason**: paper_framing.md confirms 5-model cross-validation (Qwen-1.5B, Qwen-7B, Pythia-1.4B, LLaMA-8B, Mistral-7B). The \"two architectures\" is D055-era language.\n\n### 2. Conclusion: same outdated arXiv count\n- **File**: `docs/paper/conclusion.tex`, line 5\n- **Current**: `\"confirmed across architectures (Qwen-1.5B, Pythia-1.4B)\"`\n- **Should be**: `\"confirmed across five models (four architecture families, 1.4B--8B)\"`\n- **Reason**: Same as above.\n\n### 3. Limitations: arXiv scope description outdated\n- **File**: `docs/paper/main.tex`, line 68\n- **Current**: `\"arXiv $\\Kempirical{=}3$ is confirmed with two model families (Qwen-1.5B, Pythia-1.4B) but with reduced sample size ($n{=}2{,}200$ per model)\"`\n- **Should be**: `\"arXiv $\\Kempirical{=}3$ is confirmed with five models spanning four architecture families (Qwen-1.5B, Qwen-7B, Pythia-1.4B, LLaMA-8B, Mistral-7B; $n{=}2{,}200$ per model)\"`\n- **Reason**: 5-model validation completed (D055/D056/D057). Reduced sample size caveat still applies.\n\n### 4. Extended CI Table (Tab S2b): LLaMA-8B and Mistral-7B columns empty\n- **File**: `docs/paper/appendix.tex`, lines 93-115 (tab:kstar_ci_extended)\n- **Current**: LLaMA-8B column shows all \"---\"; Mistral-7B is not even present in the table\n- **Should be**: \n  - LLaMA-8B: 0v1=0.9225, 1v2=0.6123 [0.603, 0.622], 2v3~0.56, etc.\n  - Add Mistral-7B column: 0v1=~0.93, 1v2=0.5935 [0.584, 0.603], K*=1\n- **Reason**: These experiments completed (exp-018, exp-019). The main text references them but the extended table has placeholders.\n\n### 5. Pythia Decoding Table (Tab S10) entirely empty\n- **File**: `docs/paper/appendix.tex`, lines 405-424 (tab:s10_pythia_decoding)\n- **Current**: All cells show \"---\"\n- **Should be**: Fill with exp-020 results (greedy: repetition-collapsed 1v2~0.884; nuc p=0.9, T=0.7, T=1.2 values)\n- **Reason**: exp-020 completed. Caption references the data but cells are placeholders.\n\n### 6. Domain Ablation Table (Tab S12) entirely empty\n- **File**: `docs/paper/appendix.tex`, lines 449-469 (tab:s12_domain_ablation)\n- **Current**: All cells show \"---\"\n- **Should be**: Fill with Qwen-1.5B continuation data for C4/Wikipedia/arXiv from exp-023/exp-024\n- **Reason**: All domain experiments completed. The main-text tab:domain_kstar has the summary but this detailed table is unfilled.\n\n---\n\n## P1: Should Fix (strengthens narrative or fixes inconsistencies)\n\n### 7. Introduction contribution (b): still says \"two architectures\"\n- **File**: `docs/paper/introduction.tex`, line 21\n- **Current**: `\"consistent across model families\"`\n- **Should be**: `\"consistent across five models spanning four architecture families (1.4B--8B)\"`\n- **Reason**: The Introduction contribution list should match the Abstract and paper_framing.md precision. Current wording is vague but not wrong.\n\n### 8. Theta sensitivity table: missing arXiv entries for LLaMA/Mistral/Qwen-7B\n- **File**: `docs/paper/appendix_extended.tex`, lines 96-120 (tab:theta_sensitivity)\n- **Current**: Only shows arXiv rows for Qwen-1.5B-base and Pythia-1.4B\n- **Should be**: Add rows for LLaMA-8B, Mistral-7B, Qwen-7B on arXiv (all K*=3 at theta=0.60)\n- **Reason**: 5-model validation data available; showing only 2 is inconsistent with main text claim.\n\n### 9. experiments_c1.tex arXiv paragraph: claims \"five-model\" but body still leads with Qwen/Pythia\n- **File**: `docs/paper/experiments_c1.tex`, lines 123-128\n- **Current**: Correctly states 5-model validation and lists all models. Good.\n- **Note**: This section is already updated. No change needed.\n\n### 10. Method section experimental setup table (tab:setup): missing LLaMA-8B and Mistral-7B\n- **File**: `docs/paper/method.tex`, lines 56-73 (tab:setup)\n- **Current**: Lists only 6 configs (Qwen-rw, Qwen-cont, Qwen-base, Pythia, OLMo, Qwen-7B)\n- **Should be**: Add LLaMA-3.1-8B and Mistral-7B rows (both continuation mode, C4 5000 seeds)\n- **Reason**: Main text and abstract claim \"8 model configurations\" but setup table only shows 6. This is a factual mismatch the reviewer will notice.\n\n### 11. JSD decay figure: verify 7 models are shown\n- **File**: `docs/paper/discussion.tex`, line 13 (fig:jsd_decay caption)\n- **Current**: Caption says \"7 C4 models with K*=2\" and \"dashed purple: Mistral-7B\"\n- **Verify**: The figure file needs to include all 7 C4 models. If it was generated before LLaMA-8B data arrived, it may only show 5-6 models.\n- **Action**: Regenerate `figures/fig_jsd_decay.pdf` with all 7 C4 model curves + Mistral + arXiv + retrain-chain\n\n### 12. Scorer Sensitivity Table (Tab S13): mostly \"---\" entries\n- **File**: `docs/paper/appendix.tex`, lines 472-492 (tab:s13_scorer_sensitivity)\n- **Current**: Only Qwen-RW, Qwen-cont, Qwen-base have cross-scorer data. Pythia, OLMo, Qwen-7B, Mistral show \"---\"\n- **Should be**: exp-022 provides cross-scorer data for multiple generators. Fill what's available.\n- **Reason**: Partially filled table looks unfinished.\n\n### 13. Discussion \"Scorer sensitivity\" paragraph: mention Wikipedia resolution explicitly\n- **File**: `docs/paper/discussion.tex`, lines 66-68\n- **Current**: Already mentions Wikipedia scorer confound and recommends cross-family validation. Good.\n- **Note**: This section is already updated. No change needed.\n\n### 14. Scale validation (14B/32B) mention\n- **File**: `docs/paper/main.tex`, lines 68-70 (Limitations) and `conclusion.tex` line 7\n- **Current**: \"Scope: model scale ≤8B\"; Conclusion: \"Future work includes scaling to 13B+\"\n- **Should be**: If 14B/32B results arrive before submission, update Limitations scope and add one sentence to Discussion about scale. If not, current language is fine.\n- **Action**: Conditional on experiment completion before May 25.\n\n---\n\n## P2: Optional Improvements (polish)\n\n### 15. Abstract: add Wikipedia K*=1 to complete the domain hierarchy\n- **File**: `docs/paper/main.tex`, line 36\n- **Current**: Only mentions C4 K*=2 and arXiv K*=3\n- **Could add**: Brief mention of domain ordering: \"arXiv (K*=3) > C4 (K*=2) > Wikipedia (K*=1)\"\n- **Reason**: The clean three-level hierarchy is the headline finding post-D060. Space permitting, it strengthens the Abstract.\n\n### 16. Discussion: add explicit mention of \"two types of one-wash\"\n- **File**: `docs/paper/discussion.tex`, around lines 17-19 and 59-63\n- **Current**: Discusses Mistral domain-rescue and OLMo capacity failure separately\n- **Could add**: A sentence explicitly naming the distinction: \"One-wash arises from two distinct mechanisms: domain-dependent (Mistral, rescued by arXiv) and model-intrinsic (OLMo, K*=1 across all domains).\"\n- **Reason**: paper_framing.md emphasizes this as a key insight; the paper discusses it implicitly but never names the two-type taxonomy explicitly.\n\n### 17. Appendix extended discussion: lambda values could cite memory.md numbers\n- **File**: `docs/paper/discussion.tex`, lines 23-32\n- **Current**: Already mentions C4 lambda~2.9, arXiv lambda~1.0, Wikipedia lambda~3.1. Good.\n- **Note**: Numbers match memory.md. No change needed.\n\n### 18. Appendix Tab S12: caption says \"Qwen2.5-1.5B-Instruct, continuation mode\" but should reflect all 6 models\n- **File**: `docs/paper/appendix.tex`, line 453\n- **Current**: Caption scoped to single model\n- **Should be**: If filling with multi-model data, update caption accordingly. Or keep as single-model detail table and reference main-text tab:domain_kstar for full matrix.\n\n### 19. Ethics Statement: add Wikipedia and arXiv to data sources\n- **File**: `docs/paper/main.tex`, line 81\n- **Current**: \"Our experiments use the publicly available C4 corpus\"\n- **Should be**: \"Our experiments use publicly available corpora (C4, Wikipedia, arXiv abstracts)\"\n- **Reason**: Paper now uses 3 domains but Ethics only mentions C4.\n\n---\n\n## Priority Summary\n\n| Priority | Count | Items |\n|----------|-------|-------|\n| P0 (must fix) | 6 | #1, #2, #3, #4, #5, #6 |\n| P1 (should fix) | 8 | #7, #8, #10, #11, #12, #13, #14 (conditional) |\n| P2 (optional) | 5 | #15, #16, #17, #18, #19 |\n\n## Recommended Execution Order\n\n1. **First pass (P0, ~2h)**: Fix factual counts (#1, #2, #3, #7), add method table rows (#10), fill appendix data tables (#4, #5, #6)\n2. **Second pass (P1, ~2h)**: Update theta sensitivity table (#8), regenerate JSD figure (#11), fill scorer table (#12)\n3. **Third pass (P2, ~1h)**: Abstract domain hierarchy (#15), two-type one-wash (#16), Ethics (#19)\n4. **Conditional**: If 14B/32B results arrive, add to Discussion (#14)\n\n## Already Correct (no change needed)\n\n- experiments_c1.tex Section 4.5 (Cross-Domain Variation): correctly describes 5-model arXiv, 6-model Wikipedia, scorer confound, clean domain ordering\n- tab:domain_kstar (inline in experiments_c1.tex): 6×3 matrix with footnotes for scorer artifact, capacity failure, one-wash\n- tab:domain_model_kstar.tex and tab_domain_model_kstar_full.tex: correctly formatted with all 6 models\n- Discussion JSD paragraph: lambda values match memory.md\n- Discussion scorer sensitivity paragraph: correctly describes Wikipedia confound\n- appendix_extended.tex Wiki Domain section: correctly resolves the confound with detailed table\n- Dose-response section: complete with table and analysis\n"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-18T00:04:33.351328+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/paper_patch_audit.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_patch_audit_20260518T000144",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-18T00:04:33.351493+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "paper_patch_audit",
  "type": "report",
  "description": "Paper comprehensive patch audit - 逐章节修改清单 (6 P0 / 8 P1 / 5 P2 items)",
  "project": "gen-depth-contamination",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/paper_patch_audit.md",
  "tags": "['paper', 'audit', 'patch']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_patch_audit_20260518T000144",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "paper_patch_audit",
    "type": "report",
    "description": "Paper comprehensive patch audit - 逐章节修改清单 (6 P0 / 8 P1 / 5 P2 items)",
    "project": "gen-depth-contamination",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/paper_patch_audit.md",
    "tags": "['paper', 'audit', 'patch']"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-18T00:04:33.351657+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260518_ad3e64\", \"name\": \"paper_patch_audit\", \"type\": \"report\", \"description\": \"Paper comprehensive patch audit - 逐章节修改清单 (6 P0 / 8 P1 / 5 P2 items)\", \"path\": \"projects/gen-depth-contamination/artifacts/_project/report/paper_patch_audit.md\", \"url\": null, \"project\": \"gen-depth-contamination\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-18T00:04:20.926634+00:00\", \"tags\": [\"paper\", \"audit\", \"patch\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_patch_audit_20260518T000144",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 47 · 2026-05-18T00:04:33.351877+00:00_

审计完成。核心发现：

**论文整体已较新**，D060 scorer confound、6×3 matrix、Mistral case study、JSD decay 等关键内容在 `experiments_c1.tex` 和 `discussion.tex` 中已正确反映。

**6 个 P0 问题**（必须修）：
1. Abstract/Conclusion/Limitations 中 arXiv 仍写 "two architectures"，应更新为 "five models, four architecture families"
2. Method 的 setup table 只列 6 个模型配置，但全文 claim "8 configurations"
3. 三个 Appendix 数据表（extended CI、Pythia decoding、domain ablation）全是 "---" 占位符

**8 个 P1 问题**（应该改）：theta sensitivity table 缺 arXiv 新模型行、JSD figure 需确认包含全部 7 个模型、scorer sensitivity table 部分空缺等。

**5 个 P2 问题**（可选）：Abstract 加 domain hierarchy 三级排序、显式命名 two-type one-wash taxonomy、Ethics 补全数据源等。

建议执行顺序：先修 P0 factual counts + 填表（~2h），再补 P1 figure/table（~2h），最后 P2 polish（~1h）。14B/32B 结果到达后条件性更新。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_paper_patch_audit_20260518T000144"
}
```

</details>

---
