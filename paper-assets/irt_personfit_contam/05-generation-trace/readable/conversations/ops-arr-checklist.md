# ops arr checklist

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 41
- **Recorded user turns:** 0
- **Tool calls:** 20
- **Original source:** `logs/chats/worker_ops_arr-checklist_20260523T030743.jsonl`
- **Structured JSON:** [`b49bdad8094a91f44caf.json`](../../sessions/b4/b49bdad8094a91f44caf.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

41 recorded events

### Tool call

_source line 1 · 2026-05-23T03:09:27.167007+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_arr-checklist_20260523T030743",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-23T03:09:27.168589+00:00_

paper/sections/experiments.tex
paper/sections/background.tex
paper/sections/sec_empirical.tex
paper/sections/sec_simulation.tex
paper/sections/sec_setup.tex
paper/sections/sec_ctrl_contam.tex
paper/sections/related_work.tex
paper/main.tex
paper/sections/method.tex
paper/sections/limitations.tex
paper/sections/abstract.tex
paper/sections/conclusion.tex
paper/sections/introduction.tex
paper/sections/results.tex
paper/sections/discussion.tex
paper/sections/appendix.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_arr-checklist_20260523T030743",
  "tool": "Glob",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-23T03:09:27.168900+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.bib",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_arr-checklist_20260523T030743",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.bib",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-23T03:09:27.169149+00:00_

paper/references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_arr-checklist_20260523T030743",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-23T03:09:27.169396+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.sty",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_arr-checklist_20260523T030743",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.sty",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-23T03:09:27.169620+00:00_

paper/acl.sty

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_arr-checklist_20260523T030743",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-23T03:09:27.169838+00:00_

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
  "session": "worker_ops_arr-checklist_20260523T030743",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-23T03:09:27.170085+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	\usepackage{graphicx}
9	\usepackage{booktabs}
10	\usepackage{amsmath}
11	\usepackage{amssymb}
12	\usepackage{multirow}
13	\usepackage{xcolor}
14	\usepackage{subcaption}
15	\usepackage{enumitem}
16	
17	\newcommand{\irtfit}{\textsc{IRT-FIT}}
18	
19	\graphicspath{{../figures/paper/}}
20	
21	\title{What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?}
22	
23	\author{Anonymous}
24	
25	\begin{document}
26	\maketitle
27	
28	\begin{abstract}
29	\input{sections/abstract}
30	\end{abstract}
31	
32	\input{sections/introduction}
33	\input{sections/related_work}
34	\input{sections/method}
35	\input{sections/results}
36	\input{sections/discussion}
37	\input{sections/conclusion}
38	
39	\input{sections/limitations}
40	
41	\section*{Reproducibility Statement}
42	Code and response data will be released upon acceptance.
43	Bootstrap confidence intervals use the percentile method with 10,000 resamples.
44	All three model families use clean baseline seeds 0--9 ($n{=}10$ per family).
45	Pre-calibrated 4PL item parameters are from the publicly available PSN-IRT item bank \citep{psnirt2026}.
46	
47	\bibliography{references}
48	
49	\appendix
50	\input{sections/appendix}
51	
52	\end{document}
53	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_arr-checklist_20260523T030743",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-23T03:09:27.170329+00:00_

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
  "session": "worker_ops_arr-checklist_20260523T030743",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/limitations.tex"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-23T03:09:27.170585+00:00_

1	\section*{Limitations}
2	
3	Our controlled experiments cover three model families (Qwen2.5-7B, Llama-3.1-8B, Mistral-7B) at the 7--8B scale with QLoRA fine-tuning; validation on larger models (13B, 70B), mixture-of-experts architectures, and full-parameter fine-tuning remains future work.
4	The $\theta$-shift absorption mechanism is confirmed within-model by fixed-$\theta$ analysis but its free-$\theta$ magnitude is highly seed-dependent (CV up to 60\%); cross-model comparisons require multi-seed replication not available for all families.
5	Our findings are scoped to SFT-based contamination and may not generalize to pretraining contamination, which operates through different learning dynamics.
6	The post-RL characterization is $N{=}1$ (Qwen only, GRPO algorithm, 15\% contamination on MMLU); generalization to other model families, RL methods (PPO, DPO), and contamination levels requires further validation.
7	LLMs systematically violate IRT assumptions of local independence and unidimensionality; while the $\Delta\ell_z^*$ design mitigates shared misfit through within-model differencing, the theoretical properties of this correction under severe model misfit remain an open question.
8	Our local dependence simulations employ testlet and Gaussian models that may not fully capture the dependency structures induced by attention mechanisms and sequential processing in LLMs; validating robustness under more realistic dependency structures remains an open question.
9	Most contamination conditions were trained as a single QLoRA run, though Qwen MMLU at 15\%/25\%/50\% was replicated with $n{=}3$ seeds (Appendix~\ref{app:reproducibility}).
10	Multi-seed validation shows stable free-$\theta$ effects at low/moderate contamination (CV${\leq}$25\%), while the high variance at 50\% (CV${=}$60\%) is resolved by $\theta$-anchoring (CV${=}$19\%).
11	Cross-condition consistency across 12 independent settings provides additional converging evidence.
12	Our lowest empirical contaminati
…[truncated 598 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_arr-checklist_20260523T030743",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-23T03:09:27.170852+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_arr-checklist_20260523T030743",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-23T03:09:27.171269+00:00_

1	% =============================================================================
2	% references.bib — IRT Person-Fit Contamination Detection Paper
3	% Cleaned: 2026-05-21 | 33 entries (orphan entries removed)
4	% =============================================================================
5	
6	% =============================================================================
7	% Person-Fit Statistics (Psychometrics)
8	% =============================================================================
9	
10	@article{hedges1981,
11	  author = {Hedges, Larry V.},
12	  title = {Distribution Theory for {Glass}'s Estimator of Effect Size and Related Estimators},
13	  journal = {Journal of Educational Statistics},
14	  volume = {6},
15	  number = {2},
16	  pages = {107--128},
17	  year = {1981},
18	}
19	
20	@article{drasgow1985,
21	  title = {Appropriateness Measurement with Polychotomous Item Response Models and Standardized Indices},
22	  author = {Drasgow, F. and Levine, M. V. and Williams, E. A.},
23	  journal = {British Journal of Mathematical and Statistical Psychology},
24	  year = {1985},
25	  volume = {38},
26	  number = {1},
27	  pages = {67--86},
28	  doi = {10.1111/j.2044-8317.1985.tb00817.x},
29	}
30	
31	@article{karabatsos2003,
32	  title = {Comparing the Aberrant Response Detection Performance of Thirty-Six Person-Fit Statistics},
33	  author = {Karabatsos, G.},
34	  journal = {Applied Measurement in Education},
35	  year = {2003},
36	  volume = {16},
37	  number = {4},
38	  pages = {277--298},
39	  doi = {10.1207/S15324818AME1604_2},
40	}
41	
42	@article{meijer2001,
43	  title = {Methodology Review: Evaluating Person Fit},
44	  author = {Meijer, R. R. and Sijtsma, K.},
45	  journal = {Applied Psychological Measurement},
46	  year = {2001},
47	  volume = {25},
48	  number = {2},
49	  pages = {107--135},
50	  doi = {10.1177/01466210122031957},
51	}
52	
53	@article{sinharay2017,
54	  title = {Which Statistic Should Be Used to Detect Item Preknowledge When the Set o
…[truncated 18260 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_arr-checklist_20260523T030743",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-23T03:09:27.171571+00:00_

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
  "session": "worker_ops_arr-checklist_20260523T030743",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/abstract.tex"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-23T03:09:27.171813+00:00_

1	Benchmark contamination in Large Language Models (LLMs) undermines evaluation validity, yet most detection methods require privileged access to training data, model internals, or output probabilities.
2	We present the first controlled characterization of IRT person-fit statistics for detecting SFT-stage contamination: the framework requires only binary response patterns from the target model---no access to weights, gradients, logits, or training data---combined with externally calibrated 4PL item parameters from a large-scale item bank; diagnostic $\theta$-anchoring additionally requires a clean baseline.
3	A contaminated LLM produces aberrant response patterns analogous to a test-taker with item preknowledge.
4	Using $\ell_z^*$ in a matched-difference design ($\Delta\ell_z^*$) across three 7--8B model families ($n{=}10$ clean baseline seeds per model family) on MMLU (14,042 items) and ARC-Challenge (295 items), we identify three behavior boundaries:
5	(1) model-specific $\theta$-shift dynamics, where contamination-induced ability inflation absorbs the person-fit signal; $\theta$-anchoring is necessary for reliable detection of high-ability models at high contamination (2.4$\times$ amplification, inter-seed CV reduced from 60\% to 19\%);
6	(2) a detection-diagnosis tradeoff where simpler statistics yield stronger detection but lack $\ell_z^*$'s diagnostic capabilities (seen/unseen decomposition, mechanistic $\theta$-shift analysis);
7	and (3, exploratory) ability-dependent non-monotonic dose-response under free-$\theta$ estimation, driven by $\theta$-shift absorption; $\theta$-anchored analysis reveals stable detection with a strong positive dose-response at higher contamination levels.
8	These findings establish when and why binary response patterns carry contamination information beyond aggregate accuracy.
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_arr-checklist_20260523T030743",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-23T03:09:27.172124+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_arr-checklist_20260523T030743",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/appendix.tex"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-23T03:09:27.172679+00:00_

1	\section{Simulation Validation}
2	\label{app:simulation}
3	
4	Under the null (no contamination), bootstrap $\ell_z^*$ tracks $\mathcal{N}(0,1)$: mean bias 0.041 and standard deviation 1.003 on MMLU.
5	Kolmogorov--Smirnov rejection rates vary with benchmark size: 8.3\% for MMLU and HellaSwag ($n > 10{,}000$), 50.0\% for GSM8K ($n = 1{,}319$), 58.3\% for ARC-C ($n = 295$), and 75.0\% for HumanEval ($n = 164$).
6	$\ell_z^*$ is well-calibrated for benchmarks with $n \geq 10{,}000$ items; smaller benchmarks show increasing finite-sample deviations from normality.
7	
8	Two-sided testing eliminates the inverted-U artifact: MMLU achieves 97.8\% power at 15\% contamination and sustains ${>}$93\% at all levels.
9	Power scales with $\sqrt{n}$, as predicted by the noncentrality parameter $\delta \propto \sqrt{n}$.
10	The empirical power function, derived via Gauss--Hermite quadrature ($K=30$) over the ability distribution, achieves $R^2 = 0.957$ against simulated values, with approximate minimum benchmark size of $n \geq 7{,}958$ items for 80\% power at 15\% contamination under MMLU item parameters.
11	
12	\section{4PL vs.\ 3PL Ablation Details}
13	\label{app:4pl_ablation}
14	
15	Table~\ref{tab:4pl_3pl_power} reports detection power (proportion of 2{,}000 simulation replicates rejecting $H_0$ at $\alpha{=}0.05$, two-sided) for 4PL and 3PL parameterizations across five benchmarks and seven contamination levels.
16	The 4PL model yields higher power than 3PL at every non-trivial contamination level on every benchmark.
17	The advantage is largest on MMLU and HellaSwag, where upper-asymptote ($d < 1$) violations are most prevalent, and smallest on ARC-Challenge and HumanEval, where limited item counts constrain power under both parameterizations.
18	
19	Power is non-monotonic at 75\% contamination under 4PL on four of five benchmarks (e.g., MMLU: $.952 \to .938$; GSM8K: $.846 \to .802$).
20	This reflects the $\theta$-shift boundary condition described in \S\ref{sec:inverted_u}: at
…[truncated 22148 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_arr-checklist_20260523T030743",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-23T03:09:27.173013+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "(github\\.com|gitlab\\.com|huggingface\\.co/[a-zA-Z]|\\.edu|\\.ac\\.|university|institute|acknowledge|funding|grant|supported by|thank)",
  "-i": "True",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_arr-checklist_20260523T030743",
  "tool": "Grep",
  "tool_args": {
    "pattern": "(github\\.com|gitlab\\.com|huggingface\\.co/[a-zA-Z]|\\.edu|\\.ac\\.|university|institute|acknowledge|funding|grant|supported by|thank)",
    "-i": "True",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-23T03:09:27.173263+00:00_

paper/acl_natbib.bst:208:% (thanks to 'ijvm' for suggested code here)
paper/acl_natbib.bst:1231:      % then don't print the URL (thanks to Joseph Wright
paper/acl_natbib.bst:1291:%   http://neal.ctstateu.edu/history/cite.html
paper/acl_natbib.bst:1292:%   http://www.cas.usf.edu/english/walker/mla.html
paper/acl.sty:4:%     https://github.com/acl-org/acl-style-files/
paper/acl.sty:127:\let\Thanks\thanks % \Thanks and \thanks used to be different, but keep this for backwards compatibility.
paper/acl.sty:144:   \@thanks
paper/acl.sty:149: \gdef\@thanks{}\gdef\@author{}\gdef\@title{}\let\thanks\relax}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_arr-checklist_20260523T030743",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-23T03:09:27.173497+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "(our (previous|prior|earlier|recent) (work|paper|study)|we (previously|earlier|recently) (showed|proposed|introduced|developed))",
  "-i": "True",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_arr-checklist_20260523T030743",
  "tool": "Grep",
  "tool_args": {
    "pattern": "(our (previous|prior|earlier|recent) (work|paper|study)|we (previously|earlier|recently) (showed|proposed|introduced|developed))",
    "-i": "True",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-23T03:09:27.173682+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_arr-checklist_20260523T030743",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-23T03:09:27.173864+00:00_

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
  "session": "worker_ops_arr-checklist_20260523T030743",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-23T03:09:27.174109+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Benchmark contamination, the unintended inclusion of evaluation data in training corpora, poses a growing threat to the integrity of large language model (LLM) evaluation \citep{dodge2021, magar2022, sainz2023}.
4	As training corpora and public benchmarks both expand, the probability of overlap increases structurally \citep{jacovi2023, chang2024survey}.
5	When contamination occurs, benchmark scores no longer reflect genuine capability, undermining the primary mechanism by which the community compares and selects models.
6	
7	A range of detection methods have been proposed, but all require some form of privileged access beyond the binary response record.
8	N-gram overlap methods need the training corpus \citep{dodge2021, magar2022}.
9	Membership inference approaches require token-level probabilities \citep{minkprob2024, deng2024}.
10	Probing methods rely on crafted prompts \citep{golchin2024, oren2024}.
11	Performance-based methods require multiple test variants or output logits \citep{constat2024, codec2026}.
12	These methods form a detection frontier ordered by information access.
13	No existing method operates using only binary response patterns, without model weights, gradients, logits, or training data---though, as we show, effective detection additionally requires externally calibrated item parameters.
14	
15	In this work, we focus on SFT-stage contamination---where benchmark answers are explicitly included in fine-tuning data---for three reasons.
16	First, controlled experiments require known ground-truth contamination sets, achievable through fine-tuning with specific benchmark items.
17	Second, SFT-stage contamination is increasingly relevant as fine-tuning-as-a-service platforms proliferate, creating new pathways for benchmark data to enter training mixtures.
18	Third, SFT provides a methodologically clean setting to characterize detection boundaries before extending to noisier pretraining scenarios.
19	
…[truncated 4615 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_arr-checklist_20260523T030743",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-23T03:09:27.174387+00:00_

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
  "session": "worker_ops_arr-checklist_20260523T030743",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-23T03:09:27.174674+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{IRT Person-Fit Framework}
5	\label{sec:framework}
6	
7	We adopt the four-parameter logistic (4PL) IRT model to characterize contamination-induced aberrance in LLM response patterns.
8	The 4PL model defines the probability that a model with ability $\theta$ answers item $i$ correctly:
9	\begin{equation}
10	  P_i(\theta) = c_i + (d_i - c_i)\,\frac{1}{1 + e^{-a_i(\theta - b_i)}}
11	  \label{eq:4pl}
12	\end{equation}
13	where $a_i$ is discrimination, $b_i$ difficulty, $c_i$ the lower asymptote (guessing), and $d_i$ the upper asymptote (slip).
14	Item parameters are pre-calibrated by PSN-IRT \citep{psnirt2026} from a large-scale leaderboard dataset; we use these external parameters rather than re-estimating from potentially contaminated data, since our MML-EM refit shows discrimination recovery degrades to $r_a{=}0.127$ on contaminated leaderboard data.
15	
16	Given item parameters and a binary response vector $\mathbf{x} = (x_1, \ldots, x_n)$, we compute the person-fit statistic $\ell_z^*$ \citep{snijders2001}, a standardized log-likelihood residual quantifying deviation between observed and expected response patterns.
17	The Snijders correction accounts for estimation uncertainty in $\hat{\theta}_{\text{MLE}}$, so that $\ell_z^* \sim \mathcal{N}(0,1)$ under the null \citep{drasgow1985, snijders2001}; \citet{magis2012} provide a detailed treatment of how response model selection and ability estimation affect $\ell_z^*$.
18	Large negative $\ell_z^*$ indicates aberrant responding (unexpected failures on easy items or unexpected successes on hard items); large positive values indicate over-consistent patterns.
19	
20	\subsection{$\Delta\ell_z^*$ Matched-Difference Design}
21	\label{sec:did}
22	
23	LLM response patterns systematically violate IRT assumptions of local independence and unidimensionality.
24	In our empirical data, 57 of 60 model-benchmark cells yield $|\ell_z^*| > 1.96$ even absent contamination, renderi
…[truncated 4353 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_arr-checklist_20260523T030743",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-23T03:09:27.174947+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_arr-checklist_20260523T030743",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/results.tex"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-23T03:09:27.175338+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	\subsection{Detection Signal Across Model Families}
5	\label{sec:detection}
6	
7	Table~\ref{tab:cohens_d} presents Cohen's $d$ effect sizes for $\ell_z^*$ across three model families and two benchmarks.
8	All confidence intervals exclude zero, confirming that $\Delta\ell_z^*$ reliably separates contaminated from clean models at both contamination levels.
9	
10	On MMLU, effect sizes range from $|d|{=}2.27$ (Llama at 15\%) to $|d|{=}7.44$ (Qwen at 25\%), with Qwen at 5\% ($|d|{=}4.15$) confirming detection at the lowest contamination level tested. Llama ($|d|{=}2.27$/$2.97$/$2.50$) and Mistral ($|d|{=}3.01$/$3.50$) show comparable magnitudes.
11	On ARC-C (295 items), Qwen yields $|d|{=}3.16$ at 15\% and $|d|{=}5.30$ at 50\%, demonstrating that detection remains feasible even on small benchmarks when contamination is sufficiently concentrated.
12	
13	Clean-model $\ell_z^*$ baselines diverge substantially across families: Qwen ${+}8.68$ ($\text{SD}{=}0.74$), Mistral ${+}4.02$ ($\text{SD}{=}2.05$), Llama ${+}0.29$ ($\text{SD}{=}1.45$), and ARC-C Qwen ${-}5.42$ ($\text{SD}{=}0.16$).
14	Absolute $\ell_z^*$ thresholds would produce contradictory results: Qwen's contaminated $\ell_z^*$ at 15\% (${+}3.85$) is still positive.
15	The $\Delta\ell_z^*$ design normalizes these divergent baselines: Cohen's $d$ yields comparable effect sizes ($|d|{=}2.27$--$7.44$) despite order-of-magnitude differences.
16	Figure~\ref{fig:heatmap} provides a visual summary.
17	
18	\begin{table}[t]
19	\centering
20	\caption{Cohen's $d$ for $\Delta\ell_z^*$ across model families ($n{=}10$ clean seeds). Single-seed conditions: percentile bootstrap 95\% CI (10,000 resamples) reflecting clean-seed variability. Qwen MMLU 15\%/25\%/50\%: multi-seed mean $\pm$ SD ($n{=}3$ independent contamination runs). All exclude zero.}
21	\label{tab:cohens_d}
22	\footnotesize
23	\resizebox{\columnwidth}{!}{%
24	\begin{tabular}{@{}llrrrr@{}}
25	\toprule
26	Model & Bench. & $
…[truncated 12642 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_arr-checklist_20260523T030743",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-23T03:09:27.175650+00:00_

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
  "session": "worker_ops_arr-checklist_20260523T030743",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/discussion.tex"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-23T03:09:27.175906+00:00_

1	\section{Discussion}\label{sec:discussion}
2	
3	Our findings reveal both the strengths and boundaries of IRT person-fit for contamination detection: $\ell_z^*$ reliably detects SFT-stage contamination across model families, but three boundary conditions constrain its practical utility.
4	
5	\paragraph{Characterization over tool.}
6	The detection-diagnosis tradeoff (\S\ref{sec:degradation}) shows that simpler statistics detect contamination more powerfully than $\ell_z^*$: accuracy $z$-scores yield $|d|$ values several-fold to over an order of magnitude larger, and HT generally exceeds $\ell_z^*$.
7	The value of the IRT framework lies not in detection power but in mechanistic understanding: the $\theta$-shift analysis reveals \emph{why} detection sensitivity varies across models and contamination levels, the seen/unseen decomposition identifies \emph{what fraction} of items are memorized, and the 4PL parameterization captures item-level ceiling effects that 3PL misattributes as aberrance.
8	These diagnostic capabilities are invisible to accuracy $z$-scores or HT.
9	Findings~1--2 are theoretically predictable from IRT principles; our contribution lies in quantifying these effects in the LLM setting, where the magnitude and boundary conditions are not derivable from theory alone.
10	
11	\paragraph{Practical implications.}
12	Two results have immediate consequences.
13	Free-$\theta$ estimation produces seed-dependent dose-response curves (CV up to 60\%); anchoring $\theta$ to a pre-contamination baseline stabilizes detection and amplifies the signal for models with substantial $\theta$-shift ($\Delta\theta > 0.2$).
14	The benchmark size boundary means $\ell_z^*$ is most informative for large benchmarks ($n > 7{,}000$ items for 80\% power at 15\% contamination); on small benchmarks like ARC-C (295 items), detection relies on concentrated contamination effects.
15	
16	\paragraph{Scope and calibration.}
17	Universal baseline misfit (57/60 cells flagged) confirms systemat
…[truncated 1257 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_arr-checklist_20260523T030743",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-23T03:09:27.176187+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_arr-checklist_20260523T030743",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-23T03:09:27.176440+00:00_

1	\section{Conclusion}\label{sec:conclusion}
2	
3	We characterized IRT person-fit statistics for LLM contamination detection across three 7--8B model families, establishing reliable SFT-stage detection while identifying boundary conditions: $\theta$-shift absorption necessitating $\theta$-anchored estimation for high-ability models, a detection-diagnosis tradeoff, and non-monotonic dose-response as a $\theta$-estimation artifact.
4	Future work should address pretraining-stage signatures and broader model scales.
5	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_arr-checklist_20260523T030743",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-23T03:09:27.176668+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_arr-checklist_20260523T030743",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-23T03:09:27.176938+00:00_

1	\section{Related Work}\label{sec:related_work}
2	
3	\paragraph{Benchmark contamination detection.}
4	Contamination detection methods span a wide range of information requirements.
5	Corpus-search methods match benchmark items directly against pretraining data \citep{dodge2021, magar2022}, but require full corpus access unavailable for closed models.
6	Membership inference attacks (MIA) use token-level log-probabilities to distinguish training from unseen examples \citep{minkprob2024, deng2024}.
7	Generation-based probes elicit benchmark content via prompting \citep{golchin2024, golchin2024quiz, oren2024}.
8	Performance-based methods compare accuracy on target and reference sets \citep{constat2024, pacost2024, codec2026}, requiring multiple evaluations or in-context learning passes.
9	\citet{zhou2023benchmark} and \citet{sainz2023} argue for systematic contamination measurement, \citet{jacovi2023} propose mitigation strategies, and \citet{bordt2025forget} show that contamination can be ``forgotten'' under sufficient continued training.
10	\citet{han2026quantifying} quantify contamination in psychometric evaluations of LLMs, demonstrating that memorization effects extend beyond standard benchmarks.
11	\citet{kattamuri2025radar} take a mechanistic interpretability approach, using activation patterns to distinguish recall-based from reasoning-based responses; our work instead operates purely on behavioral response patterns without access to model internals.
12	\citet{fu2025contamination} systematically evaluate detection method assumptions, finding that most methods degrade under realistic conditions; our work contributes a psychometric perspective to this ongoing evaluation.
13	
14	A critical limitation unites all token-level methods: \citet{wang2025fragility} show that RL post-training renders MIA-based detectors no better than random across 10 methods and 4 benchmarks, because RL reshapes token distributions while largely preserving binary correctness patterns.
15	
…[truncated 2840 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_arr-checklist_20260523T030743",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-23T03:09:27.177244+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "(\\\\begin\\{ack|\\\\section\\*?\\{Ack|\\\\section\\*?\\{Ethics|\\\\section\\*?\\{Ethical)",
  "-i": "True",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_arr-checklist_20260523T030743",
  "tool": "Grep",
  "tool_args": {
    "pattern": "(\\\\begin\\{ack|\\\\section\\*?\\{Ack|\\\\section\\*?\\{Ethics|\\\\section\\*?\\{Ethical)",
    "-i": "True",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper",
    "output_mode": "content",
    "glob": "*.tex"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-23T03:09:27.177500+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_arr-checklist_20260523T030743",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-23T03:09:27.177718+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/acl.sty",
  "limit": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_arr-checklist_20260523T030743",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/acl.sty",
    "limit": "20"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-23T03:09:27.177953+00:00_

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

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_arr-checklist_20260523T030743",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-23T03:09:27.178172+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "(url|howpublished).*\\{http",
  "-i": "True",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/references.bib",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_arr-checklist_20260523T030743",
  "tool": "Grep",
  "tool_args": {
    "pattern": "(url|howpublished).*\\{http",
    "-i": "True",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/references.bib",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-23T03:09:27.178413+00:00_

166:  url = {https://arxiv.org/abs/2511.04689},
196:  url = {https://arxiv.org/abs/2402.14992},
204:  url = {https://arxiv.org/abs/2505.15055},
233:  url = {https://arxiv.org/abs/2009.03300},
257:  url = {https://arxiv.org/abs/2510.27055},
265:  url = {https://arxiv.org/abs/2405.16281},
289:  url = {https://arxiv.org/abs/2308.08493},
320:  url = {https://arxiv.org/abs/2310.16789},
328:  url = {https://arxiv.org/abs/2310.17623},
336:  url = {https://arxiv.org/abs/2406.18326},
344:  url = {https://arxiv.org/abs/2311.01964},
352:  url = {https://arxiv.org/abs/2410.03249},
360:  url = {https://arxiv.org/abs/2510.07175},
368:  url = {https://arxiv.org/abs/2510.08931},
387:  url = {https://arxiv.org/abs/2410.18966},
407:  url = {https://arxiv.org/abs/2510.09259},
415:  url = {https://arxiv.org/abs/2510.02386},
423:  url = {https://arxiv.org/abs/2602.11792},

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_arr-checklist_20260523T030743",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-23T03:09:27.178660+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper && wc -l sections/abstract.tex sections/introduction.tex sections/related_work.tex sections/method.tex sections/results.tex sections/discussion.tex sections/conclusion.tex",
  "description": "Count lines in main body sections"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_arr-checklist_20260523T030743",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper && wc -l sections/abstract.tex sections/introduction.tex sections/related_work.tex sections/method.tex sections/results.tex sections/discussion.tex sections/conclusion.tex",
    "description": "Count lines in main body sections"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-23T03:09:27.178877+00:00_

    8 sections/abstract.tex
   53 sections/introduction.tex
   34 sections/related_work.tex
   64 sections/method.tex
  166 sections/results.tex
   21 sections/discussion.tex
    4 sections/conclusion.tex
  350 total

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_arr-checklist_20260523T030743",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 41 · 2026-05-23T03:09:27.179214+00:00_

```
ARR Submission Checklist:

- [x] 匿名化: PASS
  - \author{Anonymous} ✓
  - \usepackage[review]{acl} (启用匿名模式) ✓
  - 无作者姓名、机构名、个人 URL 泄露 ✓
  - 无 Acknowledgments 节 ✓
  - "Code and response data will be released upon acceptance" 无身份泄露 ✓

- [?] 页面限制: BORDERLINE (需编译确认)
  - 主文 (Abstract→Conclusion) 约 350 行 LaTeX + 3 表 + 2 图 (含 1 个 figure*)
  - 估算 ~7.5–8.1 页，卡在 8 页边界
  - Limitations 和 Reproducibility Statement 在 \bibliography 前，不计入限制 ✓
  - 建议编译 PDF 确认实际页数

- [x] 格式: PASS
  - \documentclass[11pt]{article} ✓
  - \usepackage[review]{acl} (ACL 官方模板) ✓
  - Review mode (非 final) ✓

- [x] Limitations: PASS (但偏长)
  - \section*{Limitations} 存在 ✓
  - 覆盖 ~8 个点 (模型规模、seed 依赖、SFT scope、post-RL N=1、IRT 假设违背、local dependence、参数依赖、无 MIA 对比)
  - 用户规则要求 "~3 个点，不需要很长"——当前 14 行偏长，不影响提交但可考虑精简

- [x] Ethics: PASS
  - 论文 PDF 中无 Ethics Statement (正确——ARR Responsible NLP Checklist 在 OpenReview form 中填写) ✓

- [x] Bib 身份泄露: PASS
  - 所有 URL 均为 arXiv 链接，无个人主页/GitHub ✓
  - 无 "our previous work" 或自引泄露 ✓
  - 33 条引用条目，无可识别身份信息 ✓
```

**需要行动的项**：
1. **编译 PDF 确认页数**——主文内容估算在 8 页边界，需确认不超页
2. **可选：精简 Limitations**——当前 14 行覆盖 ~8 个点，per 用户规则建议缩减到 ~3 个核心点

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_ops_arr-checklist_20260523T030743"
}
```

</details>

---
