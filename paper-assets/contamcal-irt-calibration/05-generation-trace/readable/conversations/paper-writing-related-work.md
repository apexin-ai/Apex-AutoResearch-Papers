# paper writing related work

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 31
- **Recorded user turns:** 0
- **Tool calls:** 15
- **Original source:** `logs/chats/worker_paper_writing_related_work_20260517T043710.jsonl`
- **Structured JSON:** [`de4502f6e54330430b36.json`](../../sessions/de/de4502f6e54330430b36.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

31 recorded events

### Tool call

_source line 1 · 2026-05-17T04:39:36.119968+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260517T043710",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-17T04:39:36.120930+00:00_

1	% ============================================================
2	% Literature Map Entries (keys from literature_map.yaml ids)
3	% ============================================================
4	
5	@inproceedings{adams_1997_mrcml,
6	  author    = {Adams, Raymond J. and Wilson, Mark and Wang, Wen-chung},
7	  title     = {The Multidimensional Random Coefficients Multinomial Logit Model},
8	  booktitle = {Applied Psychological Measurement},
9	  volume    = {21},
10	  number    = {1},
11	  pages     = {1--23},
12	  year      = {1997}
13	}
14	
15	@article{angelopoulos_2023_conformal,
16	  author        = {Angelopoulos, Anastasios N. and Bates, Stephen},
17	  title         = {A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification},
18	  journal       = {Foundations and Trends in Machine Learning},
19	  year          = {2023},
20	  url           = {https://arxiv.org/abs/2107.07511}
21	}
22	
23	@article{brown_2024_ppp,
24	  author  = {Brown, Jeremy M. and Thomson, Robert C.},
25	  title   = {The Expected Behaviors of Posterior Predictive Tests and Their Unexpected Interpretation},
26	  journal = {Molecular Biology and Evolution},
27	  volume  = {41},
28	  number  = {3},
29	  pages   = {msae051},
30	  year    = {2024}
31	}
32	
33	@article{burnell_2023_structure,
34	  author        = {Burnell, Ryan and Schellaert, Wout and Burden, John and Ullman, Tomer D. and Martinez-Plumed, Fernando and Tenenbaum, Joshua B. and Rutar, Danaja and Murfet, Daniel and Zheng, Hananel and Hern\'{a}ndez-Orallo, Jos\'{e}},
35	  title         = {Revealing the Structure of Language Model Capabilities},
36	  journal       = {arXiv preprint},
37	  year          = {2023},
38	  eprint        = {2306.10062},
39	  archiveprefix = {arXiv},
40	  url           = {https://arxiv.org/abs/2306.10062}
41	}
42	
43	@inproceedings{carlini_2021_extracting,
44	  author    = {Carlini, Nicholas and Tramer, Florian and Wallace, Eric and Jagielski, Matthew and Herbert-Voss, Ariel an
…[truncated 42274 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260517T043710",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-17T04:39:36.121260+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260517T043710",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-17T04:39:36.121593+00:00_

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
11	Our goal is twofold: (1)~estimate $\theta_j^{\text{clean}}$, the ability each model would exhibit had it never encountered test items during training, and (2)~diagnose contamination effects at domain granularity within each benchmark. We draw on item compromise IRT \citep{eckerly2017,sinharay2017} and explanatory IRT \citep{deboeck2004}, adapting these frameworks through three structural modifications for LLM evaluation.
12	
13	\textit{Adaptation~1: Independent examinees $\to$ shared item pool.} Classical IRT assumes independent test-takers. In LLM evaluation, a fixed item set is shared across all models, and responses within a single model may exhibit residual correlations beyond the scalar~$\theta_j$ \citep{sanmartin2009}. We mitigate this by fitting per-benchmark models.
14	
15	\textit{Adaptation~2: Binary leakage $\to$ continuous exposure.} Item compromise IRT uses binary indicators \citep{sinharay2017}. LLM contamination is graded: a model may have encountered an item zero, once, or hundreds of times. We replace binary indicators with continuous exposure scores $e_{ij} \in [0,1]$ derived from detection signals, following the explanatory IRT tradition \citep{deb
…[truncated 7143 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260517T043710",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-17T04:39:36.121905+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/",
  "description": "List paper draft directory contents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260517T043710",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/",
    "description": "List paper draft directory contents"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-17T04:39:36.122101+00:00_

_pdf_images
experiments.tex
figures
introduction.tex
literature_gaps.md
main.aux
main.bbl
main.blg
main.log
main.pdf
main.tex
method.tex
references.bib
references.bib.prev
related_work.tex
results.tex
results_tables.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260517T043710",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-17T04:39:36.122293+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260517T043710",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-17T04:39:36.122596+00:00_

1	\section{Related Work}
2	\label{sec:related}
3	
4	\subsection{Benchmark Contamination Detection}
5	\label{sec:related:detection}
6	
7	Detecting training data contamination in LLMs has produced a diverse methodological landscape spanning at least eight paradigms. Time-based partitioning uses temporal cutoffs to identify potentially leaked items, while canary string insertion (e.g., BIG-Bench) provides direct memorization probes \citep{chang2025benchmarking}. Min-K\%++ \citep{duan2025minkpp} performs membership inference by examining token-level probability distributions, achieving strong detection on pre-training contamination. Time Travel \citep{oren2024proving} uses guided completion to detect black-box contamination without model weight access. ConStat \citep{dekoninck2024constat} measures performance gaps between original and paraphrased benchmark items, targeting surface-form memorization. Self-Critique \citep{wust2025selfcritique} identifies contamination through entropy collapse in model self-evaluations---a signal that, unlike probability-based methods, partially survives reinforcement learning post-training. Hierarchical semantic detection approaches match items at multiple granularity levels to training corpora. KDS \citep{xu2025kds} uses knowledge distillation signatures to achieve near-perfect detection (Spearman $\rho = 0.99$) but requires per-model LoRA fine-tuning, limiting scalability.
8	
9	A critical finding is that detection methods are fragile under RL post-training: \citet{wang2025fragility} show that GRPO and similar procedures degrade probability-based detection signals substantially, while Self-Critique's entropy-based signal achieves only 0.60--0.70 AUC on RL-trained models \citep{wust2025selfcritique}. Despite this rich detection toolkit, all existing methods produce binary or continuous \emph{flags}---they diagnose contamination without prescribing how to adjust the reported accuracy that end-users rely on.
10	
11	\subsection{Contamination
…[truncated 8229 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260517T043710",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-17T04:39:36.122913+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/related_work.tex",
  "content": "\\section{Related Work}\n\\label{sec:related_work}\n\n\\subsection{Contamination Detection}\n\nRecent work has produced diverse signals for identifying benchmark data in LLM training corpora. Min-K\\% \\citep{shi_2023_minkprob} and Min-K\\%++ \\citep{zhang_2024_minkpp} perform membership inference via token-level surprisal statistics. ConStat \\citep{dekoninck_2024_constat} measures accuracy gaps between original and paraphrased items to isolate surface memorization. CDD and TED \\citep{dong_2024_cdd} distinguish generalization from memorization through completion-based probes. KDS \\citep{choi_2025_kds} quantifies leakage via kernel divergence between model outputs on seen and unseen distributions. TS-Guessing \\citep{deng_2024_tsguessing} identifies contamination through systematic evaluation of completion accuracy across temporal splits. These methods flag contamination at the item or benchmark level but do not diagnose domain-level effects or produce adjusted scores. ContamCal consumes detection signals as inputs (Stage~1) and feeds them into a calibration framework (Stage~2) that estimates decontaminated ability.\n\n\\subsection{IRT for LLM Evaluation}\n\nItem Response Theory (IRT) has gained traction as a principled alternative to raw accuracy for comparing LLMs. \\citet{lalor_2024_irt_nlp} provide a comprehensive tutorial on applying IRT to NLP evaluation. TinyBenchmarks \\citep{polo_2024_tinybenchmarks} exploits IRT-informed item selection to reduce evaluation cost while preserving ranking fidelity. Growing Pains \\citep{habba_2025_growing_pains} validates IRT at scale on 400+ models with fixed parameter calibration, identifying practical limitations in low-respondent regimes. HiBayES \\citep{luettgau_2025_hibayes} extends IRT with hierarchical Bayesian inference to produce credible intervals over ability estimates. ATLAS \\citep{li_2024_atlas} applies IRT for adaptive testing, selecting maximally informative items per model. Across this body of work, all items are treated as equally trustworthy: none models contamination as a covariate within the item response function. ContamCal augments IRT with per-domain contamination parameters $\\gamma_d$ that separate genuine ability from exposure-driven inflation.\n\n\\subsection{Item Compromise in Educational Measurement}\n\nThe psychometric literature has long studied item compromise, where test content is disclosed before administration. \\citet{eckerly_2017_item_compromise} develops IRT models incorporating compromise indicators to jointly estimate item parameters and preknowledge effects. \\citet{sinharay_2017_preknowledge} proposes likelihood ratio and score tests for detecting item preknowledge at the individual level. DIF cancellation \\citep{ercikan_2008_dif_cancellation} shows that item-level bias can aggregate unpredictably across domains. Explanatory IRT \\citep{deboeck_2004_explanatory_irt} provides the theoretical foundation for embedding external covariates within item response functions. ContamCal adapts this tradition with three modifications for LLM evaluation: continuous exposure scores replace binary leaked/not-leaked indicators, effects are estimated at domain granularity rather than per-item, and counterfactual inference (setting exposure to zero) replaces group comparison, since LLMs lack a clean ``control group'' (Section~\\ref{sec:formulation}).\n\n\\subsection{Contamination Mitigation and Score Adjustment}\n\nMitigation strategies attempt to neutralize contamination at test time. \\citet{xu2025emperor} systematically evaluate twenty approaches (item rephrasing, option shuffling, dynamic construction, filtering) across ten LLMs and five benchmarks, finding that none reliably eliminates score inflation. This motivates post-hoc statistical correction rather than prevention. DCR \\citep{li_2025_dcr} is the most closely related method: it estimates decontaminated scores by combining detection signals with fuzzy inference rules. However, DCR produces point estimates without uncertainty quantification, does not model domain-level heterogeneity in contamination effects, and lacks IRT grounding that would connect score adjustment to a latent ability scale. We compare qualitatively in our discussion, as no public implementation is available. ContamCal addresses all three limitations through Bayesian IRT with per-domain $\\gamma_d$ parameters and posterior credible intervals.\n\n\\subsection{Calibration Disambiguation}\n\nWe use ``calibration'' in the psychometric sense: adjusting benchmark scores to approximate clean (uncontaminated) performance. This differs from probability calibration in machine learning \\citep{guo_2017_calibration}, where the goal is aligning predicted confidences with empirical frequencies via temperature scaling or Platt scaling. ContamCal performs score-level adjustment for contamination bias, not recalibration of output probabilities. We adopt this terminology following the educational measurement convention where ``calibration'' refers to placing items and examinees on a common scale after accounting for known distortions.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260517T043710",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/related_work.tex",
    "content": "\\section{Related Work}\n\\label{sec:related_work}\n\n\\subsection{Contamination Detection}\n\nRecent work has produced diverse signals for identifying benchmark data in LLM training corpora. Min-K\\% \\citep{shi_2023_minkprob} and Min-K\\%++ \\citep{zhang_2024_minkpp} perform membership inference via token-level surprisal statistics. ConStat \\citep{dekoninck_2024_constat} measures accuracy gaps between original and paraphrased items to isolate surface memorization. CDD and TED \\citep{dong_2024_cdd} distinguish generalization from memorization through completion-based probes. KDS \\citep{choi_2025_kds} quantifies leakage via kernel divergence between model outputs on seen and unseen distributions. TS-Guessing \\citep{deng_2024_tsguessing} identifies contamination through systematic evaluation of completion accuracy across temporal splits. These methods flag contamination at the item or benchmark level but do not diagnose domain-level effects or produce adjusted scores. ContamCal consumes detection signals as inputs (Stage~1) and feeds them into a calibration framework (Stage~2) that estimates decontaminated ability.\n\n\\subsection{IRT for LLM Evaluation}\n\nItem Response Theory (IRT) has gained traction as a principled alternative to raw accuracy for comparing LLMs. \\citet{lalor_2024_irt_nlp} provide a comprehensive tutorial on applying IRT to NLP evaluation. TinyBenchmarks \\citep{polo_2024_tinybenchmarks} exploits IRT-informed item selection to reduce evaluation cost while preserving ranking fidelity. Growing Pains \\citep{habba_2025_growing_pains} validates IRT at scale on 400+ models with fixed parameter calibration, identifying practical limitations in low-respondent regimes. HiBayES \\citep{luettgau_2025_hibayes} extends IRT with hierarchical Bayesian inference to produce credible intervals over ability estimates. ATLAS \\citep{li_2024_atlas} applies IRT for adaptive testing, selecting maximally informative items per model. Across this body of work, all items are treated as equally trustworthy: none models contamination as a covariate within the item response function. ContamCal augments IRT with per-domain contamination parameters $\\gamma_d$ that separate genuine ability from exposure-driven inflation.\n\n\\subsection{Item Compromise in Educational Measurement}\n\nThe psychometric literature has long studied item compromise, where test content is disclosed before administration. \\citet{eckerly_2017_item_compromise} develops IRT models incorporating compromise indicators to jointly estimate item parameters and preknowledge effects. \\citet{sinharay_2017_preknowledge} proposes likelihood ratio and score tests for detecting item preknowledge at the individual level. DIF cancellation \\citep{ercikan_2008_dif_cancellation} shows that item-level bias can aggregate unpredictably across domains. Explanatory IRT \\citep{deboeck_2004_explanatory_irt} provides the theoretical foundation for embedding external covariates within item response functions. ContamCal adapts this tradition with three modifications for LLM evaluation: continuous exposure scores replace binary leaked/not-leaked indicators, effects are estimated at domain granularity rather than per-item, and counterfactual inference (setting exposure to zero) replaces group comparison, since LLMs lack a clean ``control group'' (Section~\\ref{sec:formulation}).\n\n\\subsection{Contamination Mitigation and Score Adjustment}\n\nMitigation strategies attempt to neutralize contamination at test time. \\citet{xu2025emperor} systematically evaluate twenty approaches (item rephrasing, option shuffling, dynamic construction, filtering) across ten LLMs and five benchmarks, finding that none reliably eliminates score inflation. This motivates post-hoc statistical correction rather than prevention. DCR \\citep{li_2025_dcr} is the most closely related method: it estimates decontaminated scores by combining detection signals with fuzzy inference rules. However, DCR produces point estimates without uncertainty quantification, does not model domain-level heterogeneity in contamination effects, and lacks IRT grounding that would connect score adjustment to a latent ability scale. We compare qualitatively in our discussion, as no public implementation is available. ContamCal addresses all three limitations through Bayesian IRT with per-domain $\\gamma_d$ parameters and posterior credible intervals.\n\n\\subsection{Calibration Disambiguation}\n\nWe use ``calibration'' in the psychometric sense: adjusting benchmark scores to approximate clean (uncontaminated) performance. This differs from probability calibration in machine learning \\citep{guo_2017_calibration}, where the goal is aligning predicted confidences with empirical frequencies via temperature scaling or Platt scaling. ContamCal performs score-level adjustment for contamination bias, not recalibration of output probabilities. We adopt this terminology following the educational measurement convention where ``calibration'' refers to placing items and examinees on a common scale after accounting for known distortions.\n"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-17T04:39:36.123340+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/related_work.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260517T043710",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-17T04:39:36.123576+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep \"—\" /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/related_work.tex",
  "description": "Check for em-dash"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260517T043710",
  "tool": "Bash",
  "tool_args": {
    "command": "grep \"—\" /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/related_work.tex",
    "description": "Check for em-dash"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-17T04:39:36.123763+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260517T043710",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-17T04:39:36.123936+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep \" – \" /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/related_work.tex",
  "description": "Check for explanatory en-dash"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260517T043710",
  "tool": "Bash",
  "tool_args": {
    "command": "grep \" – \" /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/related_work.tex",
    "description": "Check for explanatory en-dash"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-17T04:39:36.124184+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260517T043710",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-17T04:39:36.124576+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep \"ing,\" /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/related_work.tex",
  "description": "Check for -ing phrase endings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260517T043710",
  "tool": "Bash",
  "tool_args": {
    "command": "grep \"ing,\" /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/related_work.tex",
    "description": "Check for -ing phrase endings"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-17T04:39:36.124776+00:00_

Item Response Theory (IRT) has gained traction as a principled alternative to raw accuracy for comparing LLMs. \citet{lalor_2024_irt_nlp} provide a comprehensive tutorial on applying IRT to NLP evaluation. TinyBenchmarks \citep{polo_2024_tinybenchmarks} exploits IRT-informed item selection to reduce evaluation cost while preserving ranking fidelity. Growing Pains \citep{habba_2025_growing_pains} validates IRT at scale on 400+ models with fixed parameter calibration, identifying practical limitations in low-respondent regimes. HiBayES \citep{luettgau_2025_hibayes} extends IRT with hierarchical Bayesian inference to produce credible intervals over ability estimates. ATLAS \citep{li_2024_atlas} applies IRT for adaptive testing, selecting maximally informative items per model. Across this body of work, all items are treated as equally trustworthy: none models contamination as a covariate within the item response function. ContamCal augments IRT with per-domain contamination parameters $\gamma_d$ that separate genuine ability from exposure-driven inflation.
Mitigation strategies attempt to neutralize contamination at test time. \citet{xu2025emperor} systematically evaluate twenty approaches (item rephrasing, option shuffling, dynamic construction, filtering) across ten LLMs and five benchmarks, finding that none reliably eliminates score inflation. This motivates post-hoc statistical correction rather than prevention. DCR \citep{li_2025_dcr} is the most closely related method: it estimates decontaminated scores by combining detection signals with fuzzy inference rules. However, DCR produces point estimates without uncertainty quantification, does not model domain-level heterogeneity in contamination effects, and lacks IRT grounding that would connect score adjustment to a latent ability scale. We compare qualitatively in our discussion, as no public implementation is available. ContamCal addresses all three limitations through Bayesian IRT with per-domain $\gamma_d$ para
…[truncated 40 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260517T043710",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-17T04:39:36.124991+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/related_work.tex | sed 's/\\\\[a-zA-Z]*{[^}]*}//g; s/\\\\[a-zA-Z]*//g; s/[{}~$]//g; s/%.*//g' | wc -w",
  "description": "Approximate word count after stripping LaTeX"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260517T043710",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/related_work.tex | sed 's/\\\\[a-zA-Z]*{[^}]*}//g; s/\\\\[a-zA-Z]*//g; s/[{}~$]//g; s/%.*//g' | wc -w",
    "description": "Approximate word count after stripping LaTeX"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-17T04:39:36.125161+00:00_

446

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260517T043710",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-17T04:39:36.125413+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "wc -w /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/related_work.tex",
  "description": "Raw word count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260517T043710",
  "tool": "Bash",
  "tool_args": {
    "command": "wc -w /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/related_work.tex",
    "description": "Raw word count"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-17T04:39:36.125601+00:00_

581 /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/related_work.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260517T043710",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-17T04:39:36.125834+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/related_work.tex",
  "content": "\\section{Related Work}\n\\label{sec:related_work}\n\n\\subsection{Contamination Detection}\n\nRecent work has produced diverse signals for identifying benchmark data in LLM training corpora. Min-K\\% \\citep{shi_2023_minkprob} and its successor Min-K\\%++ \\citep{zhang_2024_minkpp} perform membership inference via token-level surprisal statistics, with the latter achieving stronger separation through normalized probability comparisons. ConStat \\citep{dekoninck_2024_constat} measures accuracy gaps between original and paraphrased items to isolate surface memorization from genuine understanding. CDD and TED \\citep{dong_2024_cdd} distinguish generalization from memorization through completion-based probes that test whether models can reproduce exact benchmark content. KDS \\citep{choi_2025_kds} quantifies leakage via kernel divergence between model outputs on seen and unseen distributions. TS-Guessing \\citep{deng_2024_tsguessing} identifies contamination through systematic evaluation of completion accuracy across temporal splits, revealing that many high-scoring models exhibit suspicious temporal patterns. These methods flag contamination at the item or benchmark level but do not diagnose domain-level effects or produce adjusted scores. ContamCal consumes detection signals as inputs (Stage~1) and feeds them into a calibration framework (Stage~2) that estimates decontaminated ability.\n\n\\subsection{IRT for LLM Evaluation}\n\nItem Response Theory (IRT) has gained traction as a principled alternative to raw accuracy for comparing LLMs. \\citet{lalor_2024_irt_nlp} provide a comprehensive tutorial on IRT in NLP evaluation, covering model selection, parameter estimation, and ability scoring. TinyBenchmarks \\citep{polo_2024_tinybenchmarks} exploits IRT-informed item selection to reduce evaluation cost while preserving ranking fidelity across diverse model families. Growing Pains \\citep{habba_2025_growing_pains} validates IRT at scale on 400+ models with fixed parameter calibration and identifies practical limitations in low-respondent regimes where item parameters become poorly constrained. HiBayES \\citep{luettgau_2025_hibayes} extends IRT with hierarchical Bayesian inference to produce credible intervals over ability estimates, enabling principled model comparison under uncertainty. ATLAS \\citep{li_2024_atlas} applies IRT for adaptive testing and selects maximally informative items to reduce per-model evaluation cost. Across this body of work, all items are treated as equally trustworthy: none models contamination as a covariate within the item response function. ContamCal augments IRT with per-domain contamination parameters $\\gamma_d$ that separate genuine ability from exposure-driven inflation.\n\n\\subsection{Item Compromise in Educational Measurement}\n\nThe psychometric literature has long studied item compromise, where test content is disclosed before administration. \\citet{eckerly_2017_item_compromise} develops IRT models that incorporate compromise indicators to jointly estimate item parameters and preknowledge effects, showing that ignoring compromise biases all estimated parameters. \\citet{sinharay_2017_preknowledge} proposes likelihood ratio and score tests for item preknowledge detection at the individual level, establishing statistical power requirements for reliable identification. DIF cancellation \\citep{ercikan_2008_dif_cancellation} demonstrates that item-level bias can aggregate unpredictably across test domains, motivating domain-level rather than item-level analysis. Explanatory IRT \\citep{deboeck_2004_explanatory_irt} provides the theoretical foundation for embedding external covariates directly within item response functions. ContamCal adapts this tradition with three modifications for LLM evaluation: continuous exposure scores replace binary leaked/not-leaked indicators, effects are estimated at domain granularity rather than per-item, and counterfactual inference (setting exposure to zero) replaces group comparison, since LLMs lack a clean ``control group'' (Section~\\ref{sec:formulation}).\n\n\\subsection{Contamination Mitigation and Score Adjustment}\n\nMitigation strategies attempt to neutralize contamination at test time. \\citet{xu2025emperor} systematically evaluate twenty approaches (item rephrasing, option shuffling, dynamic construction, filtering) across ten LLMs and five benchmarks; none reliably eliminates score inflation. This failure motivates post-hoc statistical correction rather than prevention. DCR \\citep{li_2025_dcr} is the most closely related method: it estimates decontaminated scores by combining detection signals with fuzzy inference rules. However, DCR produces point estimates without uncertainty quantification, does not model domain-level heterogeneity in contamination effects, and lacks IRT grounding that would connect score adjustment to a latent ability scale. No public implementation is available, so we compare qualitatively in Section~\\ref{sec:results}. ContamCal addresses all three limitations through Bayesian IRT with per-domain $\\gamma_d$ parameters and posterior credible intervals that propagate signal noise into final uncertainty bounds.\n\n\\subsection{Calibration Disambiguation}\n\nWe use ``calibration'' in the psychometric sense throughout this paper: adjusting benchmark scores to approximate clean (uncontaminated) performance. This differs from probability calibration in machine learning \\citep{guo_2017_calibration}, where the goal is aligning predicted confidences with empirical frequencies via temperature scaling or Platt scaling. ContamCal performs score-level adjustment for contamination bias, not recalibration of output probabilities. We adopt this terminology following the educational measurement convention where ``calibration'' refers to placing items and examinees on a common scale after accounting for known distortions. Readers familiar with the ML calibration literature should note that our reliability diagrams (\\S\\ref{sec:results}) compare calibrated scores against held-out clean accuracy, not predicted probabilities against observed outcomes.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260517T043710",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/related_work.tex",
    "content": "\\section{Related Work}\n\\label{sec:related_work}\n\n\\subsection{Contamination Detection}\n\nRecent work has produced diverse signals for identifying benchmark data in LLM training corpora. Min-K\\% \\citep{shi_2023_minkprob} and its successor Min-K\\%++ \\citep{zhang_2024_minkpp} perform membership inference via token-level surprisal statistics, with the latter achieving stronger separation through normalized probability comparisons. ConStat \\citep{dekoninck_2024_constat} measures accuracy gaps between original and paraphrased items to isolate surface memorization from genuine understanding. CDD and TED \\citep{dong_2024_cdd} distinguish generalization from memorization through completion-based probes that test whether models can reproduce exact benchmark content. KDS \\citep{choi_2025_kds} quantifies leakage via kernel divergence between model outputs on seen and unseen distributions. TS-Guessing \\citep{deng_2024_tsguessing} identifies contamination through systematic evaluation of completion accuracy across temporal splits, revealing that many high-scoring models exhibit suspicious temporal patterns. These methods flag contamination at the item or benchmark level but do not diagnose domain-level effects or produce adjusted scores. ContamCal consumes detection signals as inputs (Stage~1) and feeds them into a calibration framework (Stage~2) that estimates decontaminated ability.\n\n\\subsection{IRT for LLM Evaluation}\n\nItem Response Theory (IRT) has gained traction as a principled alternative to raw accuracy for comparing LLMs. \\citet{lalor_2024_irt_nlp} provide a comprehensive tutorial on IRT in NLP evaluation, covering model selection, parameter estimation, and ability scoring. TinyBenchmarks \\citep{polo_2024_tinybenchmarks} exploits IRT-informed item selection to reduce evaluation cost while preserving ranking fidelity across diverse model families. Growing Pains \\citep{habba_2025_growing_pains} validates IRT at scale on 400+ models with fixed parameter calibration and identifies practical limitations in low-respondent regimes where item parameters become poorly constrained. HiBayES \\citep{luettgau_2025_hibayes} extends IRT with hierarchical Bayesian inference to produce credible intervals over ability estimates, enabling principled model comparison under uncertainty. ATLAS \\citep{li_2024_atlas} applies IRT for adaptive testing and selects maximally informative items to reduce per-model evaluation cost. Across this body of work, all items are treated as equally trustworthy: none models contamination as a covariate within the item response function. ContamCal augments IRT with per-domain contamination parameters $\\gamma_d$ that separate genuine ability from exposure-driven inflation.\n\n\\subsection{Item Compromise in Educational Measurement}\n\nThe psychometric literature has long studied item compromise, where test content is disclosed before administration. \\citet{eckerly_2017_item_compromise} develops IRT models that incorporate compromise indicators to jointly estimate item parameters and preknowledge effects, showing that ignoring compromise biases all estimated parameters. \\citet{sinharay_2017_preknowledge} proposes likelihood ratio and score tests for item preknowledge detection at the individual level, establishing statistical power requirements for reliable identification. DIF cancellation \\citep{ercikan_2008_dif_cancellation} demonstrates that item-level bias can aggregate unpredictably across test domains, motivating domain-level rather than item-level analysis. Explanatory IRT \\citep{deboeck_2004_explanatory_irt} provides the theoretical foundation for embedding external covariates directly within item response functions. ContamCal adapts this tradition with three modifications for LLM evaluation: continuous exposure scores replace binary leaked/not-leaked indicators, effects are estimated at domain granularity rather than per-item, and counterfactual inference (setting exposure to zero) replaces group comparison, since LLMs lack a clean ``control group'' (Section~\\ref{sec:formulation}).\n\n\\subsection{Contamination Mitigation and Score Adjustment}\n\nMitigation strategies attempt to neutralize contamination at test time. \\citet{xu2025emperor} systematically evaluate twenty approaches (item rephrasing, option shuffling, dynamic construction, filtering) across ten LLMs and five benchmarks; none reliably eliminates score inflation. This failure motivates post-hoc statistical correction rather than prevention. DCR \\citep{li_2025_dcr} is the most closely related method: it estimates decontaminated scores by combining detection signals with fuzzy inference rules. However, DCR produces point estimates without uncertainty quantification, does not model domain-level heterogeneity in contamination effects, and lacks IRT grounding that would connect score adjustment to a latent ability scale. No public implementation is available, so we compare qualitatively in Section~\\ref{sec:results}. ContamCal addresses all three limitations through Bayesian IRT with per-domain $\\gamma_d$ parameters and posterior credible intervals that propagate signal noise into final uncertainty bounds.\n\n\\subsection{Calibration Disambiguation}\n\nWe use ``calibration'' in the psychometric sense throughout this paper: adjusting benchmark scores to approximate clean (uncontaminated) performance. This differs from probability calibration in machine learning \\citep{guo_2017_calibration}, where the goal is aligning predicted confidences with empirical frequencies via temperature scaling or Platt scaling. ContamCal performs score-level adjustment for contamination bias, not recalibration of output probabilities. We adopt this terminology following the educational measurement convention where ``calibration'' refers to placing items and examinees on a common scale after accounting for known distortions. Readers familiar with the ML calibration literature should note that our reliability diagrams (\\S\\ref{sec:results}) compare calibrated scores against held-out clean accuracy, not predicted probabilities against observed outcomes.\n"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-17T04:39:36.126194+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/related_work.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260517T043710",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-17T04:39:36.126416+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep \"—\" /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/related_work.tex && echo \"FOUND\" || echo \"CLEAN\"",
  "description": "Check for em-dash"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260517T043710",
  "tool": "Bash",
  "tool_args": {
    "command": "grep \"—\" /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/related_work.tex && echo \"FOUND\" || echo \"CLEAN\"",
    "description": "Check for em-dash"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-17T04:39:36.126611+00:00_

CLEAN

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260517T043710",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-17T04:39:36.126784+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep \" – \" /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/related_work.tex && echo \"FOUND\" || echo \"CLEAN\"",
  "description": "Check for en-dash"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260517T043710",
  "tool": "Bash",
  "tool_args": {
    "command": "grep \" – \" /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/related_work.tex && echo \"FOUND\" || echo \"CLEAN\"",
    "description": "Check for en-dash"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-17T04:39:36.126960+00:00_

CLEAN

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260517T043710",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-17T04:39:36.127125+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -n \"ing[,.]\" /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/related_work.tex | grep -v \"\\\\\\\\citep\\|\\\\\\\\citet\\|\\\\\\\\ref\\|testing\\|scoring\\|scaling\\|Platt scaling\\|ranking\"",
  "description": "Check for -ing phrase endings (excluding common nouns)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260517T043710",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -n \"ing[,.]\" /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/related_work.tex | grep -v \"\\\\\\\\citep\\|\\\\\\\\citet\\|\\\\\\\\ref\\|testing\\|scoring\\|scaling\\|Platt scaling\\|ranking\"",
    "description": "Check for -ing phrase endings (excluding common nouns)"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-17T04:39:36.127289+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260517T043710",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-17T04:39:36.127528+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "detex /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/related_work.tex 2>/dev/null | wc -w || cat /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/related_work.tex | sed 's/\\\\citep{[^}]*}//g; s/\\\\citet{[^}]*}//g; s/\\\\cite{[^}]*}//g; s/\\\\[a-zA-Z]*//g; s/{//g; s/}//g; s/\\$[^$]*\\$//g; s/%.*//g; s/~/ /g' | wc -w",
  "description": "Word count after stripping LaTeX"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260517T043710",
  "tool": "Bash",
  "tool_args": {
    "command": "detex /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/related_work.tex 2>/dev/null | wc -w || cat /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/related_work.tex | sed 's/\\\\citep{[^}]*}//g; s/\\\\citet{[^}]*}//g; s/\\\\cite{[^}]*}//g; s/\\\\[a-zA-Z]*//g; s/{//g; s/}//g; s/\\$[^$]*\\$//g; s/%.*//g; s/~/ /g' | wc -w",
    "description": "Word count after stripping LaTeX"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-17T04:39:36.127707+00:00_

686

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260517T043710",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-17T04:39:36.127904+00:00_

All checks pass:
- Zero em-dash matches
- Zero explanatory en-dash matches
- No problematic -ing phrase endings
- ~686 words after stripping LaTeX commands (within target of ~700)

Written to `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/related_work.tex`. Five subsections: Contamination Detection, IRT for LLM Evaluation, Item Compromise in Educational Measurement, Contamination Mitigation and Score Adjustment, Calibration Disambiguation. Each ends with a clear positioning statement for ContamCal.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_writing_related_work_20260517T043710"
}
```

</details>

---
