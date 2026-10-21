# paper emnlp format precheck

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 57
- **Recorded user turns:** 0
- **Tool calls:** 28
- **Original source:** `logs/chats/worker_paper_emnlp-format-precheck_20260520T193016.jsonl`
- **Structured JSON:** [`c140640511e824e3219e.json`](../../sessions/c1/c140640511e824e3219e.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

57 recorded events

### Tool call

_source line 1 · 2026-05-20T19:33:52.990372+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__read_project_file",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_emnlp-format-precheck_20260520T193016",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__read_project_file",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-20T19:33:52.990707+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_emnlp-format-precheck_20260520T193016",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-20T19:33:52.990893+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "find /root/contamcal-irt-calibration/ -name \"*.tex\" -o -name \"*.bib\" -o -name \"*.sty\" -o -name \"*.cls\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_emnlp-format-precheck_20260520T193016",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "find /root/contamcal-irt-calibration/ -name \"*.tex\" -o -name \"*.bib\" -o -name \"*.sty\" -o -name \"*.cls\""
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-20T19:33:52.991031+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_emnlp-format-precheck_20260520T193016",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-20T19:33:52.991166+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.94}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_emnlp-format-precheck_20260520T193016",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-20T19:33:52.991329+00:00_

artifacts/dream_reports/dream_20260513T155040/best/paper.tex
artifacts/dream_reports/dream_20260513T155040/median/paper.tex
artifacts/dream_reports/dream_20260513T155040/worst/paper.tex
artifacts/_project/paper/related_work.tex
artifacts/dream_reports/dream_20260513T171200/best/paper.tex
artifacts/dream_reports/dream_20260513T171200/median/paper.tex
artifacts/dream_reports/dream_20260513T171200/worst/paper.tex
artifacts/_project/paper/fisher_info_appendix.tex
artifacts/fisher_info_derivation/fisher_info_appendix.tex
artifacts/dream_reports/dream_20260514T171536/best/paper.tex
artifacts/dream_reports/dream_20260514T171536/median/paper.tex
artifacts/dream_reports/dream_20260514T171536/worst/paper.tex
artifacts/dream_reports/dream_20260514T185145/best/paper.tex
artifacts/dream_reports/dream_20260514T185145/median/paper.tex
artifacts/dream_reports/dream_20260514T185145/worst/paper.tex
artifacts/dream_reports/dream_20260515T052337/best/paper.tex
artifacts/dream_reports/dream_20260515T052337/median/paper.tex
artifacts/dream_reports/dream_20260515T052337/worst/paper.tex
artifacts/dream_reports/dream_20260516T104822/best/paper.tex
artifacts/dream_reports/dream_20260516T104822/median/paper.tex
artifacts/dream_reports/dream_20260516T104822/worst/paper.tex
artifacts/dream_reports/dream_20260516T155748/best/paper.tex
artifacts/dream_reports/dream_20260516T155748/median/paper.tex
artifacts/dream_reports/dream_20260516T155748/worst/paper.tex
artifacts/_project/paper/results.tex
artifacts/_project/paper/related_work_04a735.tex
artifacts/_project/paper/discussion.tex
artifacts/_project/paper/abstract.tex
artifacts/paper_draft/experiments.tex
artifacts/_project/paper/introduction.tex
artifacts/paper_draft/abstract.tex
artifacts/paper_draft/conclusion.tex
artifacts/paper_draft/discussion.tex
artifacts/paper_draft/introduction.tex
artifacts/paper_draft/main.tex
artifacts/paper_draft/method.tex
artifacts/paper_draft/related_work.tex
artifacts/paper_draft/results.tex
artifacts/paper_dra
…[truncated 448 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_emnlp-format-precheck_20260520T193016",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-20T19:33:52.991485+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_emnlp-format-precheck_20260520T193016",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.bib",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-20T19:33:52.991616+00:00_

artifacts/dream_reports/dream_20260513T155040/best/references.bib
artifacts/dream_reports/dream_20260514T185145/median/references.bib
artifacts/bib_rebuild_2025plus.bib
artifacts/bib_rebuild_2024_classics.bib
artifacts/_project/paper/references.bib
artifacts/paper_draft/references.bib
docs/paper/references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_emnlp-format-precheck_20260520T193016",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-20T19:33:52.991769+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_emnlp-format-precheck_20260520T193016",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-20T19:33:52.991901+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review,hyperref]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage{amsmath}
6	\usepackage{amssymb}
7	\usepackage{graphicx}
8	\usepackage{booktabs}
9	\usepackage{multirow}
10	\usepackage{xcolor}
11	\usepackage{subcaption}
12	\usepackage{algorithm}
13	\usepackage{algpseudocode}
14	\usepackage{float}
15	
16	\title{Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families}
17	
18	\author{Anonymous}
19	
20	\begin{document}
21	\maketitle
22	
23	\begin{abstract}
24	\input{abstract}
25	\end{abstract}
26	
27	\input{introduction}
28	\input{related_work}
29	\input{method}
30	\input{experimental_setup}
31	\input{results}
32	\input{conclusion}
33	
34	\input{limitations}
35	\input{ethics}
36	
37	\bibliography{references}
38	
39	\input{appendix}
40	
41	\end{document}
42	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_emnlp-format-precheck_20260520T193016",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-20T19:33:52.992027+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_emnlp-format-precheck_20260520T193016",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/abstract.tex"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-20T19:33:52.992157+00:00_

1	Benchmark contamination is widely assumed to inflate language model scores, yet the actual effect has never been systematically measured across model families. We perform controlled SFT injection at five dosage levels into five models spanning four independent families (7B--14.7B parameters) and discover that contamination produces not one effect but qualitatively different dose-response patterns---from immunity ($\pm$0.5pp) through monotonic benefit ($+$3.8pp) to catastrophic collapse ($-$9 to $-$13pp across seeds). Contamination vulnerability concentrates in the 65--70\% MMLU baseline band; models at extreme baselines show limited sensitivity. Counter-intuitively, the 14B Qwen model is 3$\times$ more fragile than 7B. These effects are benchmark-conditional: models harmed on MMLU can simultaneously benefit on GSM8K ($+$10pp), revealing asymmetric cross-benchmark transfer. Profiles are robust on MMLU (4/5 families $\geq$99.6\% bootstrap stability); ARC-Challenge shows directional agreement for 4/5 families but lower stability due to its smaller item pool (1{,}172 vs.\ 14{,}042 items). We further characterize contamination detection signal failure: Min-K\%++ exhibits directional reversal at small scales (Cohen's $d = -1.55$ to $-1.98$), actively misleading practitioners. Simulation studies establish that IRT-based contamination diagnosis requires ensemble sizes ($J \geq 50$) above current practice. Our findings demonstrate that ``contamination equals inflation'' is a gross oversimplification; model-specific dose-response profiling is necessary for reliable benchmark interpretation.
2	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_emnlp-format-precheck_20260520T193016",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-20T19:33:52.992287+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_emnlp-format-precheck_20260520T193016",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-20T19:33:52.992534+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Benchmark scores drive model selection and research priorities for large language models, yet training data contamination is pervasive: trillion-token web crawls routinely ingest benchmark items \citep{oren2024proving}, and practitioners cannot determine how much of a reported score reflects genuine capability versus memorization \citep{hendrycks2021mmlu,chang2025benchmarking}. Despite twenty mitigation strategies \citep{sun2025emperor}, contamination-free benchmarks \citep{white2024livebench}, and dynamic regeneration \citep{dong_2024_cdd}, a fundamental question remains: what is the actual effect of contamination on aggregate scores? The implicit assumption is uniform inflation, but this has never been tested across model families.
4	
5	We perform controlled SFT injection (LoRA, five dosage levels) into five models spanning four independent families from four labs (Alibaba, Microsoft, Allen AI, Google) and discover qualitatively different dose-response patterns---from immunity (Phi-4 14.7B, $\pm$0.5pp on MMLU) to catastrophic collapse (Qwen-14B, $-$9 to $-$13pp across seeds). Contamination vulnerability concentrates in the 65--70\% MMLU baseline band: below it, models benefit (OLMo-2 $+$3.2pp, Gemma-2 $+$3.8pp); above it, they are harmed or immune. Counter-intuitively, the 14B model is 3$\times$ more fragile than 7B. Using ContamCal, a two-stage pipeline combining multi-signal item filtering with contamination-augmented IRT (2PL+$\gamma_k$), we provide the statistical machinery for this characterization.
6	
7	Our contributions:
8	\begin{enumerate}
9	    \item \textbf{Dose-response taxonomy with cross-seed and cross-benchmark validation.} Controlled injection across four families reveals qualitatively different dose-response patterns; contamination vulnerability concentrates in the 65--70\% MMLU baseline band, while models at extreme baselines show limited sensitivity. Cross-benchmark transfer to GSM8K reveals t
…[truncated 1156 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_emnlp-format-precheck_20260520T193016",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-20T19:33:52.992693+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_emnlp-format-precheck_20260520T193016",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-20T19:33:52.992890+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	ContamCal operates in two stages: Stage~1 estimates per-item contamination exposure from multiple detection signals via training-free fusion; Stage~2 embeds these scores in a contamination-augmented IRT model to produce calibrated ability estimates with credible intervals.
5	
6	\subsection{Problem Formulation}
7	\label{sec:formulation}
8	
9	Let $y_{ijk} \in \{0,1\}$ denote the binary response of model~$j$ ($j=1,\ldots,J$) to item~$i$ ($i=1,\ldots,I_k$) on benchmark~$k$. Standard IRT assumes $P(y_{ijk}=1) = f(\theta_j, \boldsymbol{\xi}_i)$ where $\theta_j$ is latent ability and $\boldsymbol{\xi}_i$ collects item parameters. When training corpora contain benchmark items, the observed ability $\hat{\theta}_j$ confounds genuine capability with memorization.
10	
11	Our goal is to estimate $\theta_j^{\text{clean}}$, the ability each model would exhibit absent contamination, and to diagnose contamination effects at domain granularity. We adapt item compromise IRT \citep{eckerly_2017_item_compromise,sinharay_2017_preknowledge} and explanatory IRT \citep{deboeck_2004_explanatory_irt} for LLM evaluation: replacing binary leakage indicators with continuous exposure scores $e_{ij} \in [0,1]$, fitting per-benchmark models to handle the shared item pool \citep{sanmartin_2009_irt}, and recovering clean ability via counterfactual inference (setting $e_{ij}=0$).
12	
13	\subsection{Stage 1: Multi-Signal Exposure Mapping}
14	\label{sec:stage1}
15	
16	For each model~$j$ and item~$i$, we consider four candidate detection signals. \textbf{S1}~(Embedding similarity): cosine similarity between the item embedding and its nearest neighbor in the SFT training corpus. \textbf{S2}~(Min-K\%++): a membership inference statistic based on token-level surprisal \citep{zhang_2024_minkpp}. \textbf{S3}~(ConStat): the accuracy gap between original and paraphrased item variants \citep{dekoninck2024constat}. \textbf{S4}~(Self-Critique): negative entropy of mode
…[truncated 9017 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_emnlp-format-precheck_20260520T193016",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-20T19:33:52.993044+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_emnlp-format-precheck_20260520T193016",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-20T19:33:52.993185+00:00_

1	\section{Related Work}\label{sec:related_work}
2	
3	\paragraph{Contamination detection and mitigation.}
4	Detection methods flag contaminated items via token-level surprisal \citep{shi_2023_minkprob,zhang_2024_minkpp}, accuracy gaps on paraphrases \citep{dekoninck2024constat}, kernel divergence \citep{choi_2025_kds}, completion probes \citep{dong_2024_cdd}, and parallel test sets \citep{zhang_2024_gsm1k}; see \citet{chen2025benchmarking,singh2024evaluation} for surveys. Concurrent work by \citet{tao2025detecting} targets RL-trained models via entropy collapse. These methods perform binary classification without quantifying effect sizes. On mitigation, \citet{sun2025emperor} find none of twenty approaches reliably restores clean performance; DCR \citep{xu2025dcr} estimates decontaminated scores but without uncertainty quantification. ContamCal consumes detection signals as inputs and produces calibrated ability with credible intervals.
5	
6	\paragraph{IRT for LLM evaluation.}
7	Item Response Theory \citep{lord_1980_irt,hambleton_1991_irt} has gained traction for LLM evaluation: TinyBenchmarks \citep{polo_2024_tinybenchmarks} for efficient evaluation, Growing Pains \citep{habba_2025_growing_pains} for large-scale validation, HiBayES \citep{luettgau_2025_hibayes} for hierarchical Bayesian inference; see \citet{lalor_2024_irt_nlp} for a tutorial. Most directly related, \citet{han2026quantifying} apply psychometric DIF to quantify contamination on item parameters, using group-based binary indicators on naturally contaminated models. ContamCal differs by introducing continuous exposure covariates ($\gamma_k$) from multiple detection signals, operating on controlled-injection data with known ground truth, and providing domain-level decomposition. Our $\gamma$ parameter is formally an instance of explanatory DIF \citep{deboeck_2004_explanatory_irt,eckerly_2017_item_compromise}: the contamination covariate differentially affects response probability, analogous to item comp
…[truncated 259 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_emnlp-format-precheck_20260520T193016",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-20T19:33:52.993362+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/experimental_setup.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_emnlp-format-precheck_20260520T193016",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/experimental_setup.tex"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-20T19:33:52.993536+00:00_

1	\section{Experimental Setup}
2	\label{sec:experiments}
3	
4	\subsection{Controlled SFT Injection}
5	\label{sec:injection}
6	
7	We construct a controlled contamination testbed spanning four independent model families from four labs, trained on independent corpora with distinct pre-training recipes: Qwen2.5 \citep{qwen2024qwen25} (0.5B, 1.5B, 3B, 7B, 14B), Phi-4 \citep{abdin2024phi4} (14.7B), OLMo-2 \citep{olmo2team2025} (7B), and Gemma-2 \citep{gemmateam2024gemma2} (9B). All models are fine-tuned with a unified LoRA configuration \citep{hu2022lora} ($r=16$, $\alpha=32$, lr$=5\times10^{-5}$, bf16) on a general-purpose SFT corpus into which benchmark items are injected at five dosage levels: d000 (0\%, clean control), d005 (5\%), d025 (25\%), d050 (50\%), and d100 (100\%). Contaminated items augment (not replace) the base SFT corpus; at d100, 16{,}533 benchmark items are added beyond 50{,}000 base examples.
8	
9	Qwen2.5 serves as the primary within-family series (five scale points, 0.5B--14B). Models at $\leq$3B are trained with two seeds at four dosage levels; 7B and 14B at all five dosages. The three cross-family models are each trained at five dosages with a single seed, serving as consistency checks rather than independent confirmatory analyses. This yields over 50 checkpoints spanning eight sizes across four families. We exclude 0.5B from MC IRT due to position bias (A-option rate: 46\% at d000 to 98\% at d100; \S\ref{sec:signal_failure}).
10	
11	\subsection{Benchmarks, Domains, and Evaluation}
12	\label{sec:benchmarks}
13	
14	We evaluate on three benchmarks spanning distinct cognitive demands and response formats.
15	
16	\textbf{MMLU} \citep{hendrycks2021mmlu} (5-shot): 14,042 multiple-choice items across 57 subjects, grouped into 8 cognitive domains (Math, Science, CS \& Engineering, Medical, Humanities, Social Sciences, Business \& Law, Other). This stratification reveals within-benchmark heterogeneity that aggregate scoring obscures (\S\ref{sec:results}).
17
…[truncated 1364 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_emnlp-format-precheck_20260520T193016",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-20T19:33:52.993686+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_emnlp-format-precheck_20260520T193016",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/results.tex"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-20T19:33:52.993951+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	Cross-family results (\S\ref{sec:taxonomy}) use seed$=$42 data across five models from four independent families. Within-family IRT analyses (\S\ref{sec:calibration_results}--\ref{sec:domain_differential}) use $J=16$ Qwen2.5 models (8$\times$1.5B + 8$\times$3B); domain-level contamination estimates $\gamma_d$ (\S\ref{sec:domain_differential}) are reported at $J=16$ in the text and $J=13$ in Figure~\ref{fig:domain_gamma}.
5	
6	\subsection{Dose-Response Patterns}
7	\label{sec:taxonomy}
8	
9	\begin{table}[t]
10	\centering
11	\caption{Observed dose-response patterns under controlled SFT injection (seed$=$42, MMLU). $\Delta$acc: d000$\to$d100 change (95\% CI from item-level paired bootstrap, $B=10{,}000$). Stab.: bootstrap classification stability. Classifications are robust to threshold hyperparameter choice (180/180 model--seed--combination pairs across 30 $(\tau,\sigma)$ combinations; Appendix~\ref{sec:classification_sensitivity}).}
12	\label{tab:taxonomy}
13	\footnotesize
14	\begin{tabular}{llccccc}
15	\toprule
16	Pattern & Model & Baseline & $\Delta$acc & 95\% CI & Peak & Stab. \\
17	\midrule
18	Immune & Phi-4 14.7B & 76.4\% & $\pm$0.5pp & [$-$0.60, $+$0.26] & negl. & 100\% \\
19	Collapse & Qwen-14B & 69.4\% & $-$9.4 to $-$12.7pp & [$-$12.74, $-$9.0] & --- & 100\% \\
20	V-recovery & Qwen-7B & 66.1\% & $-$1.8pp & [$-$2.36, $-$1.22] & $-$3.1\textsuperscript{d025} & 99.6\% \\
21	Benefit & Gemma-2 9B & 61.9\% & $+$3.8pp & [$+$3.18, $+$4.33] & mono. & 76.6\% \\
22	Benefit & OLMo-2 7B & 53.8\% & $+$3.2pp\textsuperscript{$\dagger$} & [$+$2.73, $+$3.71] & sat.\textsuperscript{d050} & 100\% \\
23	\bottomrule
24	\multicolumn{7}{l}{\scriptsize $^{\dagger}$Seed-sensitive: s42 $+$3.2pp, s123 $-$0.6pp, s0 $+$1.4pp; cross-seed CI crosses zero ($p=0.039$). See \S\ref{sec:cross_seed}.}
25	\end{tabular}
26	\end{table}
27	
28	Applying Algorithm~\ref{alg:profile-classification} to seed$=$42 accuracy trajectories yields qualitatively differ
…[truncated 13902 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_emnlp-format-precheck_20260520T193016",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-20T19:33:52.994136+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_emnlp-format-precheck_20260520T193016",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-20T19:33:52.994280+00:00_

1	\section{Discussion and Conclusion}\label{sec:conclusion}
2	
3	We systematically profiled how SFT-injected contamination affects benchmark scores across model families and scales. Three findings emerge.
4	
5	\paragraph{Diverse patterns, not uniform inflation.}
6	The ``contamination inflates scores'' assumption is a gross oversimplification. Controlled injection reveals qualitatively different dose-response patterns: contamination vulnerability concentrates in the 65--70\% MMLU baseline band, while models at extreme baselines show limited sensitivity. Item-level DiD analysis (\S\ref{sec:memorization_test}) shows these patterns arise from global capability modulation, not item-specific memorization---challenging the premise of overlap-based detection methods. Contamination \emph{direction} is consistent across benchmarks; \emph{shape} varies with benchmark properties (Appendix~\ref{sec:arc_cross_benchmark}), implying model-\emph{and}-benchmark-specific profiling is necessary. Cross-seed analysis (\S\ref{sec:cross_seed}) shows effect direction is reproducible but magnitude is seed-sensitive; conflicting contamination findings in the literature may partly reflect unreported seed variance.
7	
8	\paragraph{Why bigger $\neq$ more robust.}
9	Qwen-14B ($-$9 to $-$13pp across seeds) is 3$\times$ more fragile than Qwen-7B ($-$2 to $-$3pp): SFT injection disrupts more specialized representations that smaller models have not yet developed. Organizations fine-tuning frontier models on mixed-quality data face greater capability degradation risk.
10	
11	\paragraph{Diagnostic value beyond aggregate calibration.}
12	Domain analysis reveals heterogeneity masked by aggregate scores (Social Sciences $P(\gamma_d\!<\!0) = 99.7\%$). The IRT framework captures both family-level patterns and domain-level decomposition. Pretraining contamination may produce qualitatively different effects \citep{schaeffer2026causally}; scaling to 70B+ is a natural next step.
13	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_emnlp-format-precheck_20260520T193016",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-20T19:33:52.994559+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_emnlp-format-precheck_20260520T193016",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/limitations.tex"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-20T19:33:52.994722+00:00_

1	\section*{Limitations}
2	\label{sec:limitations}
3	
4	We identify ten limitations that bound the scope of our conclusions.
5	
6	\paragraph{Scale ceiling.}
7	All experiments use models at or below 14.7B parameters. Larger models (70B+) may exhibit qualitatively different contamination dynamics where SFT injection is absorbed without producing measurable signal divergence.
8	
9	\paragraph{Seed sensitivity.}
10	Cross-seed analysis (\S\ref{sec:cross_seed}) confirms that effect \emph{direction} is reproducible across three seeds, but magnitude and dose-response shape exhibit seed-dependent variability. OLMo-2's cross-seed CI crosses zero ($p=0.039$), rendering its benefit classification borderline. Practitioners should report multi-seed CIs rather than single-seed point estimates.
11	
12	\paragraph{SFT ecological validity.}
13	We use LoRA-based SFT injection exclusively in AUGMENT mode (contaminated items appended to, not replacing, base SFT data). Pretraining-stage leakage, which occurs during large-scale web crawl ingestion, may produce qualitatively different contamination signatures. The position bias at 0.5B (A-option rate escalating from 46\% to 98\% with dosage) is likely SFT-specific. Generalization to pretraining contamination requires further validation.
14	
15	\paragraph{ARC-Challenge bootstrap stability.}
16	ARC-Challenge contains only 1{,}172 items (vs.\ 14{,}042 for MMLU), resulting in substantially lower bootstrap profile stability: OLMo-2 53.3\%, Gemma-2 62.7\% (vs.\ $\geq$76.6\% on MMLU). Gemma-2's ARC $\Delta$acc 95\% CI crosses zero, and Qwen-14B exhibits a different pattern (V-recovery) on ARC than on MMLU (Collapse). Cross-benchmark consistency claims should be interpreted as directional agreement, not pattern-level replication.
17	
18	\paragraph{Signal coverage.}
19	S1 (embedding similarity) requires training corpus access, unavailable for closed-source models. For API-only models, only S2 and S4 are applicable, and both show poor discrimination b
…[truncated 2298 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_emnlp-format-precheck_20260520T193016",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-20T19:33:52.994873+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/ethics.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_emnlp-format-precheck_20260520T193016",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/ethics.tex"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-20T19:33:52.995001+00:00_

1	\section*{Ethics Statement}
2	
3	All experiments use publicly available, open-weight language models (Qwen2.5, Phi-4, OLMo-2, and Gemma-2) under their respective licenses. Contamination injection is performed via standard supervised fine-tuning on existing public benchmark items; no new data collection involving human subjects is conducted. All evaluation benchmarks (MMLU, ARC-Challenge, GSM8K) are publicly released datasets. This work does not involve private user data, personally identifiable information, or human annotation.
4	
5	We acknowledge a dual-use risk: the contamination injection protocol we describe could be used to deliberately inflate benchmark scores. We mitigate this by focusing on detection and measurement rather than injection optimization, and by releasing detection signals rather than injection recipes. Our findings characterize the conditions under which SFT injection affects aggregate scores, which may inform decisions about manipulation risk at different scales. The measurement framework is intended to improve evaluation transparency, not to enable gaming.
6	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_emnlp-format-precheck_20260520T193016",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-20T19:33:52.995127+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_emnlp-format-precheck_20260520T193016",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/appendix.tex"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-20T19:33:52.995419+00:00_

1	\appendix
2	
3	\section{ARC-Challenge Cross-Benchmark Analysis}
4	\label{sec:arc_cross_benchmark}
5	
6	ARC-Challenge (25-shot, 1{,}172 items) patterns under s42 are directionally consistent with MMLU for four of five models: OLMo-2 benefits ($+$3.9pp), Qwen-7B ($-$2.9pp) and Qwen-14B ($-$3.4pp) are harmed, Phi-4 remains immune ($+$0.6pp). Gemma-2 ARC under s42 exhibits a 16pp oscillation artifact not reproduced under s123, indicating a seed-specific evaluation instability rather than a systematic pattern. Under s123, Gemma-2 benefits on ARC ($+$2.73pp, d000$=$80.1\%$\to$d100$=$82.9\%), consistent with MMLU Benefit ($+$3.8pp). Bootstrap stability is substantially lower than MMLU (OLMo-2: 53.3\%, Gemma-2: 62.7\%) due to the smaller item pool (1{,}172 vs.\ 14{,}042).
7	
8	\paragraph{Cross-seed ARC consistency.}
9	Phi-4 is the strongest anchor with $n\!=\!3$ on both benchmarks: ARC mean $\Delta = +0.66$pp (SD$=$0.18pp; s0 $+$0.51, s42 $+$0.60, s123 $+$0.86; BCa 95\% CI [$+$0.51, $+$0.77]), MMLU mean $\Delta = +0.73$pp---cross-benchmark agreement within 0.07pp. While statistically detectable on ARC (CI excludes zero, unlike MMLU CI [$-$0.17, $+$1.39]), the effect ($+$0.66pp) is too small to meaningfully inflate benchmark scores, consistent with the Immune classification. Qwen-7B's net ARC harm is cross-seed stable ($-$2.9pp at s42, $-$2.4pp at s123), though d005 V-dip severity is seed-dependent ($-$1.8pp vs.\ $-$4.7pp). Under s123, extreme patterns remain benchmark-invariant: Qwen-14B suffers harm on both MMLU ($-$12.7pp) and ARC ($-$3.2pp). OLMo-2 achieves $n\!=\!3$ on ARC: mean $\Delta = +3.44$pp (SD$=$0.52pp; s0 $+$3.50, s42 $+$3.92, s123 $+$2.90). Despite being the most seed-sensitive family on MMLU (SD$=$1.9pp), OLMo-2 is remarkably stable on ARC (SD$=$0.52pp)---seed sensitivity is itself benchmark-dependent, likely modulated by item count and difficulty distribution. Using multi-seed MMLU means ($+$1.4pp), direction is consistently positive on both benchmarks, il
…[truncated 21448 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_emnlp-format-precheck_20260520T193016",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-20T19:33:52.995598+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_emnlp-format-precheck_20260520T193016",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-20T19:33:52.995866+00:00_

1	% ============================================================
2	% Literature Map Entries (keys from literature_map.yaml ids)
3	% ============================================================
4	
5	@inproceedings{carlini_2021_extracting,
6	  author    = {Carlini, Nicholas and Tramer, Florian and Wallace, Eric and Jagielski, Matthew and Herbert-Voss, Ariel and Lee, Katherine and Roberts, Adam and Brown, Tom and Song, Dawn and Erlingsson, Ulfar and Oprea, Alina and Raffel, Colin},
7	  title     = {Extracting Training Data from Large Language Models},
8	  booktitle = {Proceedings of the 30th USENIX Security Symposium},
9	  year      = {2021},
10	  url       = {https://arxiv.org/abs/2012.07805}
11	}
12	
13	@inproceedings{choi_2025_kds,
14	  author    = {Choi, Hyeong Kyu and Khanov, Maxim and Wei, Hongxin and Li, Yixuan},
15	  title     = {How Contaminated Is Your Benchmark? Measuring Dataset Leakage in Large Language Models with Kernel Divergence},
16	  booktitle = {Proceedings of the 42nd International Conference on Machine Learning (ICML)},
17	  year      = {2025},
18	  url       = {https://arxiv.org/abs/2502.00678}
19	}
20	
21	@inproceedings{cormack_2009_rrf,
22	  author    = {Cormack, Gordon V. and Clarke, Charles L. A. and Buettcher, Stefan},
23	  title     = {Reciprocal Rank Fusion Outperforms {Condorcet} and Individual Rank Learning Methods},
24	  booktitle = {Proceedings of the 32nd International ACM SIGIR Conference on Research and Development in Information Retrieval},
25	  pages     = {758--759},
26	  year      = {2009},
27	  publisher = {ACM},
28	  url       = {https://dl.acm.org/doi/10.1145/1571941.1572114}
29	}
30	
31	@book{deboeck_2004_explanatory_irt,
32	  author    = {De Boeck, Paul and Wilson, Mark},
33	  title     = {Explanatory Item Response Models: A Generalized Linear and Nonlinear Approach},
34	  publisher = {Springer},
35	  year      = {2004},
36	  address   = {New York},
37	  url       = {https://link.springer.com/book/10.1007/978-1-4757-3990-9}
…[truncated 26494 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_emnlp-format-precheck_20260520T193016",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-20T19:33:52.996092+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "docs/paper/figures/**",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_emnlp-format-precheck_20260520T193016",
  "tool": "Glob",
  "tool_args": {
    "pattern": "docs/paper/figures/**",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-20T19:33:52.996229+00:00_

docs/paper/figures/fig_signal_heatmap.pdf
docs/paper/figures/fig_identifiability_heatmap.pdf
docs/paper/figures/fig_domain_gamma.pdf
docs/paper/figures/fig_dose_response.pdf
docs/paper/figures/arc_dose_response.pdf
docs/paper/figures/baseline_vs_effect.pdf
docs/paper/figures/fig_arc_dose_response.pdf
docs/paper/figures/fig_baseline_vs_effect.pdf
docs/paper/figures/fig_treated_untreated.pdf
docs/paper/figures/fig_did_dose_response.pdf

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_emnlp-format-precheck_20260520T193016",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-20T19:33:52.996372+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper && cat abstract.tex | wc -w",
  "description": "Count abstract word count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_emnlp-format-precheck_20260520T193016",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper && cat abstract.tex | wc -w",
    "description": "Count abstract word count"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-20T19:33:52.996503+00:00_

201

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_emnlp-format-precheck_20260520T193016",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-20T19:33:52.996666+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "docs/paper/*.sty",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_emnlp-format-precheck_20260520T193016",
  "tool": "Glob",
  "tool_args": {
    "pattern": "docs/paper/*.sty",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-20T19:33:52.996787+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_emnlp-format-precheck_20260520T193016",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-20T19:33:52.996899+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "docs/paper/*.cls",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_emnlp-format-precheck_20260520T193016",
  "tool": "Glob",
  "tool_args": {
    "pattern": "docs/paper/*.cls",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-20T19:33:52.997011+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_emnlp-format-precheck_20260520T193016",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-20T19:33:52.997160+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "(\\\\todo|\\\\fixme|\\\\textcolor|TODO|FIXME|XXX|HACK|TBD|\\\\comment)",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_emnlp-format-precheck_20260520T193016",
  "tool": "Grep",
  "tool_args": {
    "pattern": "(\\\\todo|\\\\fixme|\\\\textcolor|TODO|FIXME|XXX|HACK|TBD|\\\\comment)",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-20T19:33:52.997281+00:00_

acl_natbib.bst:226:            { "XXX" }
results.tex:87:Gemma-2 & 2 & $+$ & $+$ & --- & [$-$11.8, $+$17.1]\textsuperscript{$t$} & Benefit & \checkmark & TBD\textsuperscript{a} \\

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_emnlp-format-precheck_20260520T193016",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-20T19:33:52.997443+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "docs/paper/*.bst",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_emnlp-format-precheck_20260520T193016",
  "tool": "Glob",
  "tool_args": {
    "pattern": "docs/paper/*.bst",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-20T19:33:52.997560+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_emnlp-format-precheck_20260520T193016",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-20T19:33:52.997671+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\aclfinalcopy",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_emnlp-format-precheck_20260520T193016",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\aclfinalcopy",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-20T19:33:52.997780+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_emnlp-format-precheck_20260520T193016",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-20T19:33:52.997918+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/{acl,acl_natbib}.{sty,bst,cls}",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_emnlp-format-precheck_20260520T193016",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/{acl,acl_natbib}.{sty,bst,cls}",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-20T19:33:52.998033+00:00_

acl.sty
acl_natbib.bst

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_emnlp-format-precheck_20260520T193016",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-20T19:33:52.998153+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "head -30 /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/acl.sty",
  "description": "Check ACL style file version"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_emnlp-format-precheck_20260520T193016",
  "tool": "Bash",
  "tool_args": {
    "command": "head -30 /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/acl.sty",
    "description": "Check ACL style file version"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-20T19:33:52.998262+00:00_

Exit code 1
head: cannot open '/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/acl.sty' for reading: No such file or directory

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_emnlp-format-precheck_20260520T193016",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-20T19:33:52.998393+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/acl.sty",
  "limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_emnlp-format-precheck_20260520T193016",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/acl.sty",
    "limit": "30"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-20T19:33:52.998503+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_emnlp-format-precheck_20260520T193016",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-20T19:33:52.998613+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration -name \"acl.sty\" -o -name \"acl_natbib.bst\" 2>/dev/null",
  "description": "Find ACL template files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_emnlp-format-precheck_20260520T193016",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration -name \"acl.sty\" -o -name \"acl_natbib.bst\" 2>/dev/null",
    "description": "Find ACL template files"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-20T19:33:52.998725+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/acl_natbib.bst
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/acl.sty

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_emnlp-format-precheck_20260520T193016",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-20T19:33:52.998834+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/acl.sty",
  "limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_emnlp-format-precheck_20260520T193016",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/acl.sty",
    "limit": "30"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-20T19:33:52.998958+00:00_

1	% This is the LaTex style file for *ACL.
2	% The official sources can be found at
3	%
4	%     https://github.com/acl-org/acl-style-files/
5	%
6	% This package is activated by adding
7	%
8	%    \usepackage{acl}
9	%
10	% to your LaTeX file. When submitting your paper for review, add the "review" option:
11	%
12	%    \usepackage[review]{acl}
13	
14	\newif\ifacl@finalcopy
15	\newif\ifacl@anonymize
16	\newif\ifacl@linenumbers
17	\newif\ifacl@pagenumbers
18	\DeclareOption{final}{\acl@finalcopytrue\acl@anonymizefalse\acl@linenumbersfalse\acl@pagenumbersfalse}
19	\DeclareOption{review}{\acl@finalcopyfalse\acl@anonymizetrue\acl@linenumberstrue\acl@pagenumberstrue}
20	\DeclareOption{preprint}{\acl@finalcopytrue\acl@anonymizefalse\acl@linenumbersfalse\acl@pagenumberstrue}
21	\ExecuteOptions{final} % final copy is the default
22	
23	% include hyperref, unless user specifies nohyperref option like this:
24	% \usepackage[nohyperref]{acl}
25	\newif\ifacl@hyperref
26	\DeclareOption{hyperref}{\acl@hyperreftrue}
27	\DeclareOption{nohyperref}{\acl@hyperreffalse}
28	\ExecuteOptions{hyperref} % default is to use hyperref
29	\ProcessOptions\relax
30	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_emnlp-format-precheck_20260520T193016",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 57 · 2026-05-20T19:33:52.999169+00:00_

所有文件已读取完毕。以下是格式预检报告。

---

## EMNLP 2026 (ARR) 格式预检报告

### FAIL

| # | 项目 | 详情 |
|---|------|------|
| F1 | **主文极可能超 8 页** | 主文（Introduction → Discussion/Conclusion）包含 7 个 section、Algorithm 1（35 行伪代码）、5 个 table（Tab 1–5）、2 个 figure。ACL 双栏格式下保守估计 10–11 页。必须编译验证并裁剪。 |
| F2 | **正文残留 "TBD"** | `results.tex:87` — Table 3 Gemma-2 Pattern 列写的是 `TBD\textsuperscript{a}`，脚注 "Classifier fix in progress"。未完成内容不能提交。 |

### WARNING

| # | 项目 | 详情 |
|---|------|------|
| W1 | **acl.sty 版本未标注** | `docs/paper/acl.sty` 无版本日期。ARR 2026 submission cycle 可能要求最新模板，需到 [acl-org/acl-style-files](https://github.com/acl-org/acl-style-files/) 核对。 |
| W2 | **Bib arXiv 格式不一致** | `abdin2024phi4`、`olmo2team2025`、`gemmateam2024gemma2` 用 `journal = {arXiv preprint arXiv:XXXX}` 而非标准 `eprint` 字段。其他 arXiv 条目用的是 `eprint` + `archiveprefix`。应统一。 |
| W3 | **arXiv-only 条目可能已有正式版本** | `zhang_2024_gsm1k`（2024）、`kadavath2022`（2022）、`white2024livebench`（2024）、`clark2018arc`（2018）等长期 arXiv 条目，需查验是否已正式发表并更新 venue/pages。 |
| W4 | **`zhang_2024_gsm1k` 条目类型错误** | 用了 `@inproceedings` + `booktitle = {arXiv preprint}`，arXiv 论文应为 `@article` + `journal`。 |
| W5 | **多个 `@inproceedings` 缺 pages 字段** | `dekoninck2024constat`、`oren2024proving`、`hendrycks2021mmlu`、`hu2022lora` 等。已有 proceedings 的条目应补充页码。 |
| W6 | **`\usepackage[review,hyperref]{acl}`** | `hyperref` 是 acl.sty 默认选项，冗余但无害。 |

### PASS

| # | 项目 | 详情 |
|---|------|------|
| P1 | **匿名提交** | `\author{Anonymous}`，无 acknowledgments，无 `\thanks`，无去匿名化自引。 |
| P2 | **`[review]` 模式** | 已启用行号 + 匿名化。未出现 `\aclfinalcopy`。 |
| P3 | **Abstract 长度** | 201 words ≤ 250。 |
| P4 | **Limitations section** | 充分：10 个 limitation 段落，覆盖 scale ceiling / seed sensitivity / ecological validity / signal coverage / ensemble size / position bias / model misfit / linearity / prompt format。 |
| P5 | **Ethics Statement** | 存在，讨论了 dual-use risk 和 mitigation。 |
| P6 | **图文件完整** | 主文引用的 `fig_dose_response.pdf`、`fig_treated_untreated.pdf` 及 appendix 全部 8 个 figure 文件均存在于 `docs/paper/figures/`。 |
| P7 | **Table/Figure caption** | 所有 table 和 figure 均有 caption 且被正文引用。 |
| P8 | **编号连续** | 主文 Table 1–5、Figure 1–2，Appendix Table 6–12、Figure 3–8，连续无缺。 |
| P9 | **Section 结构** | Introduction → Related Work → Method → Experimental Setup → Results → Discussion/Conclusion → Limitations* → Ethics* → References → Appendix。符合 ARR 规范。 |
| P10 | **引用风格** | ACL natbib (`\citep`/`\citet`/`\citealp`) 一致使用。 |

---

### 修复建议

**F1 (超页数)** — 最高优先级。可行方案：
- 将 Algorithm 1 移入 Appendix（节省 ~0.7 页）
- 将 Table 3 (cross-seed) 或 Table 4 (DiD) 移入 Appendix，正文仅保留文字总结
- 压缩 §5.1–5.6 中描述性文字（当前结果段落较冗长）
- Figure 2 (treated_untreated) 可移入 Appendix，用一句话引用
- 需编译后逐页裁剪至严格 8 页

**F2 (TBD)** — `results.tex:87` Gemma-2 Pattern 列和脚注 `a` 需要填入实际分类结果或删除该列。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_emnlp-format-precheck_20260520T193016"
}
```

</details>

---
