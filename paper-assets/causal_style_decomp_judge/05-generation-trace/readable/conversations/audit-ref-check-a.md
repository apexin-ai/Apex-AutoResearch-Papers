# audit ref check A

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 81
- **Recorded user turns:** 0
- **Tool calls:** 40
- **Original source:** `logs/chats/worker_audit_ref_check_A_20260526T104718.jsonl`
- **Structured JSON:** [`ecbaf1d6454a2f5994e5.json`](../../sessions/ec/ecbaf1d6454a2f5994e5.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

81 recorded events

### Tool call

_source line 1 · 2026-05-26T10:52:07.731201+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Read all tex files for citation contexts",
  "subagent_type": "Explore",
  "prompt": "Read the following tex files and find ALL occurrences of these citation keys. For each key, extract the surrounding sentence/paragraph so we can verify the citation context is correct.\n\nCitation keys to find:\ncohen1988statistical, pearl2009causality, tripathi2025pairwise, murugadoss2025sos, li2026preference, wang2026fairjudge, dubois2025lc, casse2026concise, counterfactual2025rhetorical, soumik2026judging, reber2025rate, kiritchenko2017bws, novikova2018rankme, stevens1946theory, nemes2009bias, david1988method, thurstone1927law, decoster2011median, zheng2023judging\n\nFiles to read:\n- /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.tex\n- /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/abstract.tex\n- /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/introduction.tex\n- /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/related_work.tex\n- /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/method.tex\n- /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/experiments.tex\n- /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/conclusion.tex\n- /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex\n\nAlso look for a .bib file in /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/ directory to get the actual bib entries.\n\nFor each citation key, report:\n1. The exact bib entry (if found in .bib file)\n2. Every location where it's cited in the tex files, with the surrounding text (2-3 sentences of context)\n\nBe very thorough - search breadth \"very thorough\"."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_check_A_20260526T104718",
  "tool": "Agent",
  "tool_args": {
    "description": "Read all tex files for citation contexts",
    "subagent_type": "Explore",
    "prompt": "Read the following tex files and find ALL occurrences of these citation keys. For each key, extract the surrounding sentence/paragraph so we can verify the citation context is correct.\n\nCitation keys to find:\ncohen1988statistical, pearl2009causality, tripathi2025pairwise, murugadoss2025sos, li2026preference, wang2026fairjudge, dubois2025lc, casse2026concise, counterfactual2025rhetorical, soumik2026judging, reber2025rate, kiritchenko2017bws, novikova2018rankme, stevens1946theory, nemes2009bias, david1988method, thurstone1927law, decoster2011median, zheng2023judging\n\nFiles to read:\n- /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.tex\n- /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/abstract.tex\n- /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/introduction.tex\n- /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/related_work.tex\n- /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/method.tex\n- /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/experiments.tex\n- /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/conclusion.tex\n- /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex\n\nAlso look for a .bib file in /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/ directory to get the actual bib entries.\n\nFor each citation key, report:\n1. The exact bib entry (if found in .bib file)\n2. Every location where it's cited in the tex files, with the surrounding text (2-3 sentences of context)\n\nBe very thorough - search breadth \"very thorough\"."
  }
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-26T10:52:07.731681+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,WebFetch",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_check_A_20260526T104718",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,WebFetch",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 3 · 2026-05-26T10:52:07.731889+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_check_A_20260526T104718",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-26T10:52:07.732050+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper -name \"*.bib\" 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_check_A_20260526T104718",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper -name \"*.bib\" 2>/dev/null"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-26T10:52:07.732191+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_check_A_20260526T104718",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-26T10:52:07.732387+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_check_A_20260526T104718",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-26T10:52:07.732634+00:00_

1	@book{cohen1988statistical,
2	  title={Statistical Power Analysis for the Behavioral Sciences},
3	  author={Cohen, Jacob},
4	  edition={2nd},
5	  year={1988},
6	  publisher={Lawrence Erlbaum Associates}
7	}
8	
9	@book{pearl2009causality,
10	  title={Causality: Models, Reasoning, and Inference},
11	  author={Pearl, Judea},
12	  edition={2nd},
13	  year={2009},
14	  publisher={Cambridge University Press}
15	}
16	
17	@inproceedings{tripathi2025pairwise,
18	  title={Pairwise or Pointwise? Evaluating Feedback Protocols for Bias in {LLM}-Based Evaluation},
19	  author={Tripathi, Tuhina and Wadhwa, Manya and Durrett, Greg and Niekum, Scott},
20	  booktitle={Proceedings of the 2nd Conference on Language Modeling (COLM)},
21	  year={2025},
22	  url={https://arxiv.org/abs/2504.14716}
23	}
24	
25	@inproceedings{murugadoss2025sos,
26	  title={Style Outweighs Substance: Failure Modes of {LLM} Judges in Alignment Benchmarking},
27	  author={Murugadoss, Aakanksha and others},
28	  booktitle={Proceedings of the International Conference on Learning Representations (ICLR)},
29	  year={2025},
30	  url={https://arxiv.org/abs/2409.15268}
31	}
32	
33	@inproceedings{li2026preference,
34	  title={Preference Leakage: A Contamination Problem in {LLM}-as-a-Judge},
35	  author={Li, Dawei and others},
36	  booktitle={Proceedings of the International Conference on Learning Representations (ICLR)},
37	  year={2026},
38	  url={https://arxiv.org/abs/2502.01534}
39	}
40	
41	@article{wang2026fairjudge,
42	  title={{FairJudge}: An Adaptive, Debiased, and Consistent {LLM}-as-a-Judge},
43	  author={Yang, Bo and Feng, Lanfei and Chen, Yunkui and Zhang, Yu and Xu, Xiao and Li, Shijian},
44	  journal={arXiv preprint arXiv:2602.06625},
45	  year={2026},
46	  url={https://arxiv.org/abs/2602.06625}
47	}
48	
49	
50	@inproceedings{dubois2025lc,
51	  title={Length-Controlled {AlpacaEval}: A Simple Way to Debias Automatic Evaluators},
52	  author={Dubois, Yann and others},
53	  booktitle={Proceedings of the Int
…[truncated 19891 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_check_A_20260526T104718",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-26T10:52:07.732839+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_check_A_20260526T104718",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-26T10:52:07.733001+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{inconsolata}
11	\usepackage{graphicx}
12	\usepackage{booktabs}
13	\usepackage{amsmath,amssymb}
14	\usepackage{xcolor}
15	\usepackage{subcaption}
16	\usepackage{tikz}
17	\usetikzlibrary{arrows.meta,positioning}
18	
19	\title{The Likert Blindspot: Measurement-Mode Divergence\\in LLM Judge Style Evaluation}
20	
21	\author{Anonymous}
22	
23	\begin{document}
24	\maketitle
25	
26	\input{sections/abstract}
27	
28	\input{sections/introduction}
29	
30	\input{sections/related_work}
31	
32	\input{sections/method}
33	
34	\input{sections/experiments}
35	
36	\input{sections/conclusion}
37	
38	\section*{Limitations}
39	\label{sec:limitations}
40	
41	\noindent\textbf{Residual confounding.}
42	The NLI gate blocks content changes but cannot block quality perception shifts mediated by style itself; residual confounding is not fully eliminated despite logistic adjustment.
43	
44	\noindent\textbf{Detection vs.\ amplification.}
45	The Blindspot may partly reflect pairwise format amplification \citep{jeong2025comparative} rather than pure detection; six controls bound this risk (\S\ref{sec:amplification}), but we cannot precisely quantify the amplification factor.
46	
47	\noindent\textbf{Scope.}
48	CSD applies only to surface-level axes whose rewrites preserve semantic content. Primary analyses use LLMBar ($n = 100$) with five judges; generalization to additional axes, benchmarks, and judges remains open.
49	
50	\section*{Ethical Considerations}
51	
52	This work studies biases in automated evaluation systems and does not involve generating harmful content. Human annotation (100 pairs, two annotators) was conducted by compensated research collaborators; no crowdsourcing platforms were used. All data are drawn from publicly available benchmarks.
53	
54	\bibliography{references}
55	
56	\i
…[truncated 49 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_check_A_20260526T104718",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-26T10:52:07.733180+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_check_A_20260526T104718",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-26T10:52:07.733367+00:00_

1	\begin{abstract}
2	Likert and pairwise scoring yield divergent style-sensitivity profiles in LLM judges.
3	We define the \emph{Likert Blindspot}: statistically significant pairwise sensitivity absent from Likert scoring on the same data.
4	We introduce Controlled Style Decomposition (CSD), a black-box diagnostic combining natural language inference gated content control, per-axis style decomposition, and position-controlled pairwise comparison.
5	Across four target judges and two axes (formality, verbosity), pairwise reaches significance ($p < 0.001$) where Likert does not ($p > 0.28$) in all eight primary cells, replicated across three benchmarks and confirmed by seven statistical methods.
6	Scaled replication shows this divergence is structural: Likert effect sizes collapse toward zero at larger sample sizes while pairwise remains stable, revealing a three- to four-fold efficiency gap rather than absolute failure.
7	Generalized estimating equation decomposition further reveals that the confound structure differs by axis: verbosity bias is style-dominated, while formality reflects joint style--quality confounding---a distinction invisible to aggregate metrics.
8	Likert-only audits risk missing style preferences that propagate through pairwise-based alignment pipelines\footnote{Code and data are available at \url{https://anonymous.4open.science/r/causal_style_decomp_judge-5EBE/}.}.
9	\end{abstract}
10	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_check_A_20260526T104718",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-26T10:52:07.733541+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_check_A_20260526T104718",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-26T10:52:07.733690+00:00_

1	\section{Introduction}
2	
3	\emph{``What is the average height for a male?''} In our experiments, given a formal and a casual answer with verified identical content (natural language inference [NLI] entailment $= 0.993$), GPT-4o rates the casual variant \emph{higher} on a 1--10 Likert scale (8 vs.\ 5), yet consistently selects the formal variant in pairwise comparison.
4	Same judge, same texts, opposite conclusions---and both answers say the same thing.
5	This is not an isolated quirk.
6	Surface-level style features alone explain most of the variance in judge scores \citep{murugadoss2025sos}, with 76--92\% of preferences originating from style cues \citep{li2026preference,soumik2026judging}.
7	We term this pattern the \emph{Likert Blindspot}: the measurement-mode divergence where pairwise comparison detects statistically significant style sensitivity that Likert scoring misses on the same data.
8	The divergence admits multiple non-exclusive explanations---measurement attenuation, format amplification \citep{jeong2025comparative}, or construct-level differences---which our controlled design bounds but cannot definitively resolve (\S\ref{sec:likert_pairwise}).
9	
10	LLM judges are central infrastructure for evaluation and alignment training, where judge preferences serve as reward signals in reinforcement learning from human feedback (RLHF) and direct preference optimization (DPO).
11	Any systematic bias therefore propagates through both evaluation leaderboards and model development pipelines.
12	Existing approaches address individual requirements---multi-dimensional style analysis \citep{casse2026concise,wang2026fairjudge}, interventional design \citep{reber2025rate}, population-level correction \citep{dubois2025lc}---but no single framework integrates per-axis decomposition, interventional identification, confound-structure analysis, and black-box applicability.
13	Classical psychometrics establishes that pairwise comparison yields higher discriminability than abs
…[truncated 2496 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_check_A_20260526T104718",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-26T10:52:07.733865+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_check_A_20260526T104718",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-26T10:52:07.734016+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Interventional Approaches to Judge Bias}
5	Text-based interventional methods have a growing methodological foundation \citep{feder2021causalm,wu2021polyjuice,feder2022causal}.
6	\citet{reber2025rate} propose RATE, which rewrites outputs along style attributes and measures causal effects via Likert average treatment effect (ATE); however, our experiments show 60\% of style-transformed pairs receive identical Likert scores, yielding non-significant effects that pairwise comparison detects at $p = 0.006$.
7	CSD differs in targeting individual style axes, using position-controlled pairwise comparison, and enforcing content preservation via NLI gating.
8	\citet{counterfactual2025rhetorical} adopt a similar design at persona-level granularity, whereas CSD intervenes on specific style axes with position control.
9	
10	\paragraph{Style Bias in LLM Judges}
11	The foundational LLM-as-judge framework \citep{zheng2023judging} documented position bias; \citet{shi2024judging} study it across 15 judges, and \citet{ye2024justice} quantify 12 bias types, though neither isolates individual style effects.
12	Style bias as a separate source has received recent attention \citep{wu2023style,murugadoss2025sos,saito2023verbosity,li2026preference,soumik2026judging}; \citet{li2026preference} show that style-mediated \emph{preference leakage} propagates through evaluation pipelines.
13	Multi-feature frameworks such as CASSE \citep{casse2026concise} and FairJudge \citep{wang2026fairjudge} decompose style into finer dimensions but rely on correlational analyses that cannot distinguish causal style effects from content quality confounds.
14	\citet{jeong2025comparative} identify the Comparative Trap (pairwise comparison may amplify style biases), which we address in \S\ref{sec:amplification}.
15	Unlike human evaluators, LLM judges acquire format-specific biases through RLHF training: pairwise comparison serves as the reward signa
…[truncated 987 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_check_A_20260526T104718",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-26T10:52:07.734252+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_check_A_20260526T104718",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-26T10:52:07.734482+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Style-Controlled Rewriting}
5	\label{sec:rewriting}
6	
7	We isolate the effect of individual style attributes on judge scores by generating text pairs that differ along exactly one style axis while holding content fixed, a single-axis intervention design that enables per-axis causal attribution rather than aggregate style sensitivity measurement.
8	For each text, an instruction-tuned LLM (Qwen3-32B) classifies its current style along the target axis (e.g., formal vs.\ casual via binary classification).
9	It then rewrites the text toward the opposite pole (temperature 0.7, selected to balance diversity with coherence in pilot experiments) according to an axis-specific prompt (Appendix~\ref{app:rewriting_prompts}).
10	This produces a dataset balanced across both directions at the dataset level: texts detected as formal are rewritten to casual, and vice versa.
11	Each operation approximates a binary intervention on a single style variable while all other axes remain fixed (Section~\ref{sec:causal_framework}; Appendix~\ref{app:cross_axis_contamination}).
12	To control for rewriting artifact bias (the possibility that the judge prefers original text over any rewrite regardless of style), we also generate a same-style double-rewrite for each text (e.g., formal $\to$ formal) to form an original-vs-double-rewrite control pair, following the RATE bias correction protocol \citep{reber2025rate}.
13	
14	\subsection{Content Preservation Verification}
15	\label{sec:nli_gate}
16	
17	Style-controlled rewriting risks altering semantic content, which would confound the style effect with a content quality effect (the $R \to Q$ path in Figure~\ref{fig:dag}).
18	To block this path, we apply a natural language inference (NLI) gate using DeBERTa-v3-large fine-tuned on Multi-Genre NLI (MNLI; \citealp{williams2018broad}) with an entailment threshold of 0.90, selected as the threshold above which NLI performance plateaus (Appendix~\ref
…[truncated 5675 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_check_A_20260526T104718",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-26T10:52:07.734661+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_check_A_20260526T104718",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-26T10:52:07.734861+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	
5	\subsection{Statistical Framework}
6	\label{sec:stat_framework}
7	
8	The primary family comprises six tests (three target judges $\times$ two axes), corrected via Holm-Bonferroni at $\alpha = 0.05$; Gemini-2.5-Flash serves as confirmatory replication and is excluded from family-wise error rate control; as a sensitivity check, all eight tests remain significant under the expanded family (Appendix~\ref{app:holm8}).
9	Table~\ref{tab:main_results} reports both raw and adjusted $p$-values.
10	Analyses outside this grid are classified as either \emph{exploratory} (NLI threshold sensitivity sweep, \S\ref{sec:nli_threshold}) or \emph{confirmatory} (consistency filter validation, \S\ref{sec:consistency}).
11	Exploratory analyses use uncorrected $p$-values; confirmatory analyses (pipeline validity) are evaluated at $\alpha = 0.05$ without additional correction.
12	Bradley-Terry parameters \citep{bradley1952rank,luce1959individual} are estimated via spectral initialization followed by minorization-maximization \citep{hunter2004mm}, using the \texttt{choix} Python library's default L2 regularization ($\alpha = 10^{-6}$).
13	In binary-choice BT models, independence of irrelevant alternatives is structurally satisfied; the direction asymmetry in Appendix~\ref{app:bt_gof} (formality: formal-origin 88.9\% vs.\ casual-origin 52.6\%, Fisher $p = 0.015$) reflects heterogeneous treatment effects rather than a violation of this assumption.
14	All bootstrap confidence intervals are percentile CIs from 10{,}000 pair-level resamples with seed 42; we verify bootstrap stability by confirming that halving the resample count changes interval widths by $<$1pp.
15	GEE models use exchangeable working correlation with sandwich standard errors that are robust to correlation misspecification (Appendix~\ref{app:gee_diagnostics}).
16	A prospective power analysis (Appendix~\ref{app:power_analysis}) confirms that our sample sizes ($n = 86$--$88$ 
…[truncated 19294 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_check_A_20260526T104718",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-26T10:52:07.735034+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_check_A_20260526T104718",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-26T10:52:07.735171+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	CSD yields two findings: the Likert Blindspot (8/8 primary cells, $d \!\to\! 0$ at $n{=}355$; concordance $p < .001$ favors attenuation) and per-axis confound structures via GEE (verbosity style-dominated, formality conditional).
4	Practically, Likert-only audits risk false negatives at benchmark sizes $n < 200$; per-axis decomposition reveals that verbosity preferences are predominantly style-driven while formality partially reflects quality differences---a distinction invisible to aggregate metrics and consequential for RLHF pipelines where pairwise judgments serve as reward signals.
5	CSD extends to any surface-level axis with content-preserving rewrites; deeper axes remain for future work.
6	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_check_A_20260526T104718",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-26T10:52:07.735360+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_check_A_20260526T104718",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-26T10:52:07.735699+00:00_

1	\appendix
2	
3	\noindent\emph{Organization: design rationale and confound structure (A--B), consistency and GEE diagnostics (C--D), rewriter independence and gate validation (E--G), equivalence testing (H), BT analysis and statistical details (I--L), sensitivity analyses (M--N), Likert scale and ablation controls (O--Q), implementation and multiplicity (R--S), cross-axis contamination and FK analysis (T--U), annotation agreement (V), cross-benchmark replication (W--X), rewriting prompts (Y), non-tie concordance (Z).}
4	
5	\section{Design Rationale}
6	\label{app:design_rationale}
7	
8	Three variables govern the observed judge score $Y$: the style attribute $S$ (e.g., formality), the original content quality $Q$, and the judge's internal scoring function.
9	Both $S$ and $Q$ causally influence $Y$; the goal of CSD is to approximate the effect $S \to Y$ while blocking confounding through $Q$.
10	Style-controlled rewriting generates a text pair that differs along a single style axis, but any rewriting operation risks inadvertently altering content quality ($R \to Q$).
11	The NLI gate (\S\ref{sec:nli_gate}) blocks this path, yielding a controlled estimate of the $S \to Y$ effect.
12	Our approach provides interventional rather than formal causal evidence: we do not claim that the directed acyclic graph (DAG) in Figure~\ref{fig:dag} is a complete structural causal model, nor do we invoke SUTVA or consistency assumptions from the potential outcomes framework.
13	``Controlled'' in this context refers to experimentally controlled rewriting conditions, not formal causal identification in the potential-outcomes sense.
14	Our identification rests on three operational assumptions: (i)~the NLI gate approximates content preservation, blocking the $R \to Q$ path; (ii)~position swapping controls for presentation-order effects; and (iii)~the style rewrite introduces no systematic differences beyond the target axis.
15	
16	\section{Direction Asymmetry and Quality Confounding}
17	\labe
…[truncated 51486 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_check_A_20260526T104718",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-26T10:52:07.735900+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\cite(t|p)?\\{(cohen1988statistical|pearl2009causality|tripathi2025pairwise|murugadoss2025sos|li2026preference|wang2026fairjudge|dubois2025lc|casse2026concise|counterfactual2025rhetorical|soumik2026judging|reber2025rate|kiritchenko2017bws|novikova2018rankme|stevens1946theory|nemes2009bias|david1988method|thurstone1927law|decoster2011median|zheng2023judging)\\}",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections",
  "output_mode": "content",
  "context": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_check_A_20260526T104718",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\cite(t|p)?\\{(cohen1988statistical|pearl2009causality|tripathi2025pairwise|murugadoss2025sos|li2026preference|wang2026fairjudge|dubois2025lc|casse2026concise|counterfactual2025rhetorical|soumik2026judging|reber2025rate|kiritchenko2017bws|novikova2018rankme|stevens1946theory|nemes2009bias|david1988method|thurstone1927law|decoster2011median|zheng2023judging)\\}",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections",
    "output_mode": "content",
    "context": "3"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-26T10:52:07.736100+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/related_work.tex-3-
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/related_work.tex-4-\paragraph{Interventional Approaches to Judge Bias}
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/related_work.tex-5-Text-based interventional methods have a growing methodological foundation \citep{feder2021causalm,wu2021polyjuice,feder2022causal}.
docs/paper/sections/related_work.tex:6:\citet{reber2025rate} propose RATE, which rewrites outputs along style attributes and measures causal effects via Likert average treatment effect (ATE); however, our experiments show 60\% of style-transformed pairs receive identical Likert scores, yielding non-significant effects that pairwise comparison detects at $p = 0.006$.
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/related_work.tex-7-CSD differs in targeting individual style axes, using position-controlled pairwise comparison, and enforcing content preservation via NLI gating.
docs/paper/sections/related_work.tex:8:\citet{counterfactual2025rhetorical} adopt a similar design at persona-level granularity, whereas CSD intervenes on specific style axes with position control.
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/related_work.tex-9-
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/related_work.tex-10-\paragraph{Style Bias in LLM Judges}
docs/paper/sections/related_work.tex:11:The foundational LLM-as-judge framework \citep{zheng2023judging} documented position bias; \citet{shi2024judging} study it across 15 judges, and \citet{ye2024justice} quantify 12 bias types, though neither isolates individual style effects.
docs/paper/sections/related_work.tex:12:Style bia
…[truncated 16845 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_check_A_20260526T104718",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-26T10:52:07.736281+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\cite(t|p)?\\{(cohen1988statistical|pearl2009causality|tripathi2025pairwise|murugadoss2025sos|li2026preference|wang2026fairjudge|dubois2025lc|casse2026concise|counterfactual2025rhetorical|soumik2026judging|reber2025rate|kiritchenko2017bws|novikova2018rankme|stevens1946theory|nemes2009bias|david1988method|thurstone1927law|decoster2011median|zheng2023judging)\\}",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper",
  "output_mode": "content",
  "context": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_check_A_20260526T104718",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\cite(t|p)?\\{(cohen1988statistical|pearl2009causality|tripathi2025pairwise|murugadoss2025sos|li2026preference|wang2026fairjudge|dubois2025lc|casse2026concise|counterfactual2025rhetorical|soumik2026judging|reber2025rate|kiritchenko2017bws|novikova2018rankme|stevens1946theory|nemes2009bias|david1988method|thurstone1927law|decoster2011median|zheng2023judging)\\}",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper",
    "output_mode": "content",
    "context": "2"
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-26T10:52:07.736486+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/related_work.tex-4-\paragraph{Interventional Approaches to Judge Bias}
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/related_work.tex-5-Text-based interventional methods have a growing methodological foundation \citep{feder2021causalm,wu2021polyjuice,feder2022causal}.
docs/paper/sections/related_work.tex:6:\citet{reber2025rate} propose RATE, which rewrites outputs along style attributes and measures causal effects via Likert average treatment effect (ATE); however, our experiments show 60\% of style-transformed pairs receive identical Likert scores, yielding non-significant effects that pairwise comparison detects at $p = 0.006$.
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/related_work.tex-7-CSD differs in targeting individual style axes, using position-controlled pairwise comparison, and enforcing content preservation via NLI gating.
docs/paper/sections/related_work.tex:8:\citet{counterfactual2025rhetorical} adopt a similar design at persona-level granularity, whereas CSD intervenes on specific style axes with position control.
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/related_work.tex-9-
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/related_work.tex-10-\paragraph{Style Bias in LLM Judges}
docs/paper/sections/related_work.tex:11:The foundational LLM-as-judge framework \citep{zheng2023judging} documented position bias; \citet{shi2024judging} study it across 15 judges, and \citet{ye2024justice} quantify 12 bias types, though neither isolates individual style effects.
docs/paper/sections/related_work.tex:12:Style bias as a separate source has received recent attention \citep{wu2023style,murugadoss2025sos,saito2023verbosity,li2026preferen
…[truncated 13588 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_check_A_20260526T104718",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-26T10:52:07.736668+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\cite(t|p)?\\{.*pearl2009causality.*\\}",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper",
  "output_mode": "content",
  "context": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_check_A_20260526T104718",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\cite(t|p)?\\{.*pearl2009causality.*\\}",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper",
    "output_mode": "content",
    "context": "2"
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-26T10:52:07.736806+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_check_A_20260526T104718",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-26T10:52:07.736943+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "pearl2009causality",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper",
  "output_mode": "content",
  "context": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_check_A_20260526T104718",
  "tool": "Grep",
  "tool_args": {
    "pattern": "pearl2009causality",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper",
    "output_mode": "content",
    "context": "2"
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-26T10:52:07.737090+00:00_

docs/paper/main.bbl-188-  Technologies (Volume 2: Short Papers)}.
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.bbl-189-
docs/paper/main.bbl:190:\bibitem[{Pearl(2009)}]{pearl2009causality}
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.bbl-191-Judea Pearl. 2009.
docs/paper/main.bbl-192-\newblock \emph{Causality: Models, Reasoning, and Inference}, 2nd edition.
--
docs/paper/sections/experiments.tex-169-Both rewriting directions favor verbose responses (90.7\%/80.6\%); length-controlled Style OR is unchanged ($<$2\%), and an independent GPT-4o rewriter bounds evaluator-producer overlap to a 22\% reduction (Appendix~\ref{app:rewriter_indep}).
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/experiments.tex-170-Length-controlled regression confirms that 60\% of the Flesch-Kincaid grade cross-axis effect is mediated by sentence length (Sobel $z = 2.15$, $p = .031$).
docs/paper/sections/experiments.tex:171:Under the assumed causal structure (Figure~\ref{fig:dag}), Flesch-Kincaid grade acts as a plausible mediator ($S \to \text{FK} \to Y$; \citealp{pearl2009causality}), yielding a direct-effect Style OR of $2.15$ for GPT-4o (total OR $= 2.70$; Appendix~\ref{app:fk_length}).
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/experiments.tex-172-
docs/paper/sections/experiments.tex-173-These per-axis patterns selectively replicate across benchmarks (6/24 possible cells; Figure~\ref{fig:cross_bench_heatmap}), targeting the strongest effects: Llama-70B formality on AlpacaEval (BT 75.0\%, Style OR $= 7.64$) is strong enough for Likert detection ($\ddagger$ rows), confirming the severity spectrum.
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/references.bib-7-}
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/caus
…[truncated 2129 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_check_A_20260526T104718",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-26T10:52:07.737265+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "(tripathi2025pairwise|kiritchenko2017bws|decoster2011median|stevens1946theory)",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper",
  "output_mode": "content",
  "context": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_check_A_20260526T104718",
  "tool": "Grep",
  "tool_args": {
    "pattern": "(tripathi2025pairwise|kiritchenko2017bws|decoster2011median|stevens1946theory)",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper",
    "output_mode": "content",
    "context": "2"
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-26T10:52:07.737438+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.bbl-246-
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.bbl-247-\bibitem[{Tripathi et~al.(2025)Tripathi, Wadhwa, Durrett, and
docs/paper/main.bbl:248:  Niekum}]{tripathi2025pairwise}
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.bbl-249-Tuhina Tripathi, Manya Wadhwa, Greg Durrett, and Scott Niekum. 2025.
docs/paper/main.bbl-250-\newblock \href {https://arxiv.org/abs/2504.14716} {Pairwise or pointwise?
--
docs/paper/sections/experiments.tex-87-Under format equivalence, observing 8/8 primary cells as Blindspot has binomial probability $p = 0.004$; non-tie concordance (76.6\%, $p < .001$; \S\ref{sec:likert_pairwise}) provides a complementary formal test of format divergence.
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/experiments.tex-88-\paragraph{Interpreting the divergence.}
docs/paper/sections/experiments.tex:89:[Omitted long matching line]
docs/paper/sections/experiments.tex-90-Six experimental controls (\S\ref{sec:amplification}) bound the amplification factor but cannot eliminate it.
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/experiments.tex-91-The attenuation evidence ($d \to 0$ at $n = 355$) is consistent with Likert signal loss, but does not by itself rule out concurrent amplification or construct divergence.
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/references.bib-15-}
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/references.bib-16-
docs/paper/references.bib:17:@inproceedings{tripathi2025pairwise,
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/references.bib-18-  title={Pairwise or Pointwise? Ev
…[truncated 3600 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_check_A_20260526T104718",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-26T10:52:07.737597+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "tripathi2025pairwise|construct divergence",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections",
  "output_mode": "content",
  "context": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_check_A_20260526T104718",
  "tool": "Grep",
  "tool_args": {
    "pattern": "tripathi2025pairwise|construct divergence",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections",
    "output_mode": "content",
    "context": "3"
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-26T10:52:07.737746+00:00_

docs/paper/sections/experiments.tex-86-Figure~\ref{fig:power_curve} plots detection probability at observed effect magnitudes (not post-hoc power; cf.\ \citealt{hoenig2001abuse}): across six cells, Likert requires $4$--$206\times$ the current $n$ ($336$--$27{,}159$ pairs; Appendix~\ref{app:power_analysis}) to detect effects BT identifies at $p < 0.001$ with $n \leq 100$.
docs/paper/sections/experiments.tex-87-Under format equivalence, observing 8/8 primary cells as Blindspot has binomial probability $p = 0.004$; non-tie concordance (76.6\%, $p < .001$; \S\ref{sec:likert_pairwise}) provides a complementary formal test of format divergence.
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/experiments.tex-88-\paragraph{Interpreting the divergence.}
docs/paper/sections/experiments.tex:89:[Omitted long matching line]
docs/paper/sections/experiments.tex-90-Six experimental controls (\S\ref{sec:amplification}) bound the amplification factor but cannot eliminate it.
docs/paper/sections/experiments.tex:91:The attenuation evidence ($d \to 0$ at $n = 355$) is consistent with Likert signal loss, but does not by itself rule out concurrent amplification or construct divergence.
docs/paper/sections/experiments.tex-92-Non-tie concordance analysis partially adjudicates: among 201 Likert non-tie pairs (pooled across judges and axes), 76.6\% agree with pairwise direction [70.3\%, 81.9\%], $p < 0.001$.
docs/paper/sections/experiments.tex:93:Point-biserial correlations are uniformly positive ($r = 0.20$--$0.45$, 7/9 significant; Appendix~\ref{app:concordance}), evidence more consistent with measurement attenuation than construct divergence, though partial construct divergence remains at weaker effect sizes.
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/experiments.tex-94-Claude's benchmark-dependent profile illustrates why aggregate BT is insufficient for bias attribution.
docs
…[truncated 4759 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_check_A_20260526T104718",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-26T10:52:07.737912+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/experiments.tex",
  "offset": "85",
  "limit": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_check_A_20260526T104718",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/experiments.tex",
    "offset": "85",
    "limit": "20"
  }
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-26T10:52:07.738057+00:00_

85	
86	Figure~\ref{fig:power_curve} plots detection probability at observed effect magnitudes (not post-hoc power; cf.\ \citealt{hoenig2001abuse}): across six cells, Likert requires $4$--$206\times$ the current $n$ ($336$--$27{,}159$ pairs; Appendix~\ref{app:power_analysis}) to detect effects BT identifies at $p < 0.001$ with $n \leq 100$.
87	Under format equivalence, observing 8/8 primary cells as Blindspot has binomial probability $p = 0.004$; non-tie concordance (76.6\%, $p < .001$; \S\ref{sec:likert_pairwise}) provides a complementary formal test of format divergence.
88	\paragraph{Interpreting the divergence.}
89	The measurement-mode divergence admits three non-exclusive interpretations: (a)~\emph{Likert attenuation}, where tie inflation and residual signal loss reduce Likert sensitivity below detection thresholds; (b)~\emph{pairwise amplification}, where forced-choice comparison inflates micro-preferences into apparent biases \citep{jeong2025comparative}; (c)~\emph{construct divergence}, where the two formats measure different constructs (absolute quality vs.\ ordinal preference; \citealt{tripathi2025pairwise}).
90	Six experimental controls (\S\ref{sec:amplification}) bound the amplification factor but cannot eliminate it.
91	The attenuation evidence ($d \to 0$ at $n = 355$) is consistent with Likert signal loss, but does not by itself rule out concurrent amplification or construct divergence.
92	Non-tie concordance analysis partially adjudicates: among 201 Likert non-tie pairs (pooled across judges and axes), 76.6\% agree with pairwise direction [70.3\%, 81.9\%], $p < 0.001$.
93	Point-biserial correlations are uniformly positive ($r = 0.20$--$0.45$, 7/9 significant; Appendix~\ref{app:concordance}), evidence more consistent with measurement attenuation than construct divergence, though partial construct divergence remains at weaker effect sizes.
94	Claude's benchmark-dependent profile illustrates why aggregate BT is insufficient for bias attribution.
95	On LLM
…[truncated 1287 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_check_A_20260526T104718",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-26T10:52:07.738263+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper && grep -r \"cohen1988statistical\\|pearl2009causality\\|tripathi2025pairwise\\|murugadoss2025sos\\|li2026preference\\|wang2026fairjudge\\|dubois2025lc\\|casse2026concise\\|counterfactual2025rhetorical\\|soumik2026judging\\|reber2025rate\\|kiritchenko2017bws\\|novikova2018rankme\\|stevens1946theory\\|nemes2009bias\\|david1988method\\|thurstone1927law\\|decoster2011median\\|zheng2023judging\" sections/*.tex | cut -d: -f1,2,3 | sort | uniq"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_check_A_20260526T104718",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper && grep -r \"cohen1988statistical\\|pearl2009causality\\|tripathi2025pairwise\\|murugadoss2025sos\\|li2026preference\\|wang2026fairjudge\\|dubois2025lc\\|casse2026concise\\|counterfactual2025rhetorical\\|soumik2026judging\\|reber2025rate\\|kiritchenko2017bws\\|novikova2018rankme\\|stevens1946theory\\|nemes2009bias\\|david1988method\\|thurstone1927law\\|decoster2011median\\|zheng2023judging\" sections/*.tex | cut -d: -f1,2,3 | sort | uniq"
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-26T10:52:07.738451+00:00_

sections/appendix.tex:AlpacaEval \citep{dubois2025lc}: 100 sampled pairs.
sections/appendix.tex:GEE conditional decomposition at $n = 330$ confirms substantial shrinkage from $n = 88$ estimates, consistent with more extreme initial estimates producing larger corrections \citep{nemes2009bias}: Qwen3 $13.10 \to 3.83$ ($-71\%$), Llama $8.21 \to 4.01$ ($-51\%$), Gemini $8.98 \to 2.52$ ($-72\%$).
sections/appendix.tex:MT-Bench \citep{zheng2023judging}: 80 multi-turn pairs.
sections/appendix.tex:\caption{Cross-axis contamination: effect of rewriting along one style axis on surface proxies of the other axis. Cohen's $d$
sections/experiments.tex:Applying RATE's Likert ATE methodology \citep{reber2025rate} to our formality style-transformed pairs yields Cohen's $d = {-}0.04$, $p = 0.91$ (non-significant, $n = 88$); pairwise comparison on identical data reveals a 63.0\% formal preference ($p = 0.0004$, Bradley-Terry on all 173 comparisons), confirmed by a consistency-filtered sign test (73.9\%, $p = 0.006$, $n = 46$ consistent pairs).
sections/experiments.tex:At $n = 355$, the Qwen3-32B formality Style OR drops from $4.20$ to $2.15$ ($-49\%$), consistent with small-sample upward bias \citep{nemes2009bias}; the regime classification remains stable (both effects significant; Orig OR $4.70 \to 4.99$).
sections/experiments.tex:The measurement-mode divergence admits three non-exclusive interpretations: (a)~\emph{Likert attenuation}, where tie inflation and residual signal loss reduce Likert sensitivity below detection thresholds; (b)~\emph{pairwise amplification}, where forced-choice comparison inflates micro-preferences into apparent biases \citep{jeong2025comparative}; (c)~\emph{construct divergence}, where the two formats measure different constructs (absolute quality vs.\ ordinal preference; \citealt{tripathi2025pairwise}).
sections/experiments.tex:Under the assumed causal structure (Figure~\ref{fig:dag}), Flesch-Kincaid grade acts as a plausible mediator ($S \to \text{FK} \to
…[truncated 3817 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_check_A_20260526T104718",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-26T10:52:07.738739+00:00_

Perfect! Now let me compile a comprehensive report with all the findings. Let me create a summary of all citations found:

Based on my thorough search of the tex files and references.bib, here is a comprehensive report of all citation keys and their occurrences:

## COMPLETE CITATION VERIFICATION REPORT

### BIB FILE ENTRIES (from `/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/references.bib`)

All 19 requested citation keys were found in the bibliography file:

**1. cohen1988statistical**
```bibtex
@book{cohen1988statistical,
  title={Statistical Power Analysis for the Behavioral Sciences},
  author={Cohen, Jacob},
  edition={2nd},
  year={1988},
  publisher={Lawrence Erlbaum Associates}
}
```

**2. pearl2009causality**
```bibtex
@book{pearl2009causality,
  title={Causality: Models, Reasoning, and Inference},
  author={Pearl, Judea},
  edition={2nd},
  year={2009},
  publisher={Cambridge University Press}
}
```

**3. tripathi2025pairwise**
```bibtex
@inproceedings{tripathi2025pairwise,
  title={Pairwise or Pointwise? Evaluating Feedback Protocols for Bias in {LLM}-Based Evaluation},
  author={Tripathi, Tuhina and Wadhwa, Manya and Durrett, Greg and Niekum, Scott},
  booktitle={Proceedings of the 2nd Conference on Language Modeling (COLM)},
  year={2025},
  url={https://arxiv.org/abs/2504.14716}
}
```

**4. murugadoss2025sos**
```bibtex
@inproceedings{murugadoss2025sos,
  title={Style Outweighs Substance: Failure Modes of {LLM} Judges in Alignment Benchmarking},
  author={Murugadoss, Aakanksha and others},
  booktitle={Proceedings of the International Conference on Learning Representations (ICLR)},
  year={2025},
  url={https://arxiv.org/abs/2409.15268}
}
```

**5. li2026preference**
```bibtex
@inproceedings{li2026preference,
  title={Preference Leakage: A Contamination Problem in {LLM}-as-a-Judge},
  author={Li, Dawei and others},
  booktitle={Proceedings of the International Conference on Learning Representations (IC
…[truncated 17438 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_check_A_20260526T104718",
  "tool": "Agent",
  "elapsed_ms": 7
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-26T10:52:07.738968+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Pairwise or Pointwise? Evaluating Feedback Protocols for Bias in LLM-Based Evaluation\" Tripathi 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_check_A_20260526T104718",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Pairwise or Pointwise? Evaluating Feedback Protocols for Bias in LLM-Based Evaluation\" Tripathi 2025"
  }
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-26T10:52:07.739115+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Style Outweighs Substance: Failure Modes of LLM Judges\" Murugadoss arXiv 2409.15268"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_check_A_20260526T104718",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Style Outweighs Substance: Failure Modes of LLM Judges\" Murugadoss arXiv 2409.15268"
  }
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-26T10:52:07.739251+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Preference Leakage: A Contamination Problem in LLM-as-a-Judge\" Li Dawei arXiv 2502.01534"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_check_A_20260526T104718",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Preference Leakage: A Contamination Problem in LLM-as-a-Judge\" Li Dawei arXiv 2502.01534"
  }
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-26T10:52:07.739408+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"FairJudge: An Adaptive, Debiased, and Consistent LLM-as-a-Judge\" arXiv 2602.06625"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_check_A_20260526T104718",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"FairJudge: An Adaptive, Debiased, and Consistent LLM-as-a-Judge\" arXiv 2602.06625"
  }
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-26T10:52:07.739540+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Length-Controlled AlpacaEval: A Simple Way to Debias Automatic Evaluators\" Dubois arXiv 2404.04475"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_check_A_20260526T104718",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Length-Controlled AlpacaEval: A Simple Way to Debias Automatic Evaluators\" Dubois arXiv 2404.04475"
  }
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-26T10:52:07.739668+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"A Concise Agent is Less Expert: Revealing Side Effects of Using Style Features\" arXiv 2601.10809"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_check_A_20260526T104718",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"A Concise Agent is Less Expert: Revealing Side Effects of Using Style Features\" arXiv 2601.10809"
  }
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-26T10:52:07.739796+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Counterfactual LLM-based Framework for Measuring Rhetorical Style\" arXiv 2512.19908"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_check_A_20260526T104718",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Counterfactual LLM-based Framework for Measuring Rhetorical Style\" arXiv 2512.19908"
  }
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-26T10:52:07.739922+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Judging the Judges: A Systematic Evaluation of Bias Mitigation Strategies in LLM-as-a-Judge\" Soumik arXiv 2604.23178"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_check_A_20260526T104718",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Judging the Judges: A Systematic Evaluation of Bias Mitigation Strategies in LLM-as-a-Judge\" Soumik arXiv 2604.23178"
  }
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-26T10:52:07.740048+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"RATE: Causal Explainability of Reward Models with Imperfect Counterfactuals\" Reber arXiv 2410.11348"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_check_A_20260526T104718",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"RATE: Causal Explainability of Reward Models with Imperfect Counterfactuals\" Reber arXiv 2410.11348"
  }
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-26T10:52:07.740174+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Best-Worst Scaling More Reliable than Rating Scales\" Kiritchenko Mohammad 2017 ACL"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_check_A_20260526T104718",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Best-Worst Scaling More Reliable than Rating Scales\" Kiritchenko Mohammad 2017 ACL"
  }
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-26T10:52:07.740364+00:00_

Web search results for query: ""Preference Leakage: A Contamination Problem in LLM-as-a-Judge" Li Dawei arXiv 2502.01534"

Links: [{"title":"[2502.01534] Preference Leakage: A Contamination Problem in LLM-as-a-judge","url":"https://arxiv.org/abs/2502.01534"},{"title":"Preference Leakage: A Contamination Problem in LLM-as-a-judge","url":"https://arxiv.org/html/2502.01534v3"},{"title":"(PDF) Preference Leakage: A Contamination Problem in LLM-as-a-judge","url":"https://www.researchgate.net/publication/388685541_Preference_Leakage_A_Contamination_Problem_in_LLM-as-a-judge"},{"title":"Preference Leakage: A Contamination Problem in LLM-as- ...","url":"https://arxiv.org/pdf/2502.01534"},{"title":"[2502.01534v1] Preference Leakage: A Contamination Problem in LLM-as-a-judge","url":"https://arxiv.org/abs/2502.01534v1"},{"title":"Preference Leakage: A Contamination Problem in LLM-as-a-judge","url":"https://howiehwong.github.io/preference_leakage.pdf"},{"title":"LLM-as-a-judge","url":"https://llm-as-a-judge.github.io/"},{"title":"Preference Leakage: A Contamination Problem in LLM-as-a-judge | Pap…","url":"https://www.opentrain.ai/papers/preference-leakage-a-contamination-problem-in-llm-as-a-judge--arxiv-2502.01534/"},{"title":"[Paper Note] Preference Leakage: A Contamination Problem in LLM-as-a-judge - 📚 AI Paper Notes","url":"https://en.papernotes.org/ICLR2026/llm_evaluation/preference_leakage_a_contamination_problem_in_llm-as-a-judge/"}]

I found the paper you're looking for. Here's what I found:

**"Preference Leakage: A Contamination Problem in LLM-as-a-Judge"** exposes preference leakage, a contamination problem in LLM-as-a-judge caused by the relatedness between the synthetic data generators and LLM-based evaluators.

**Paper Details:**
- **arXiv ID:** 2502.01534
- **Authors:** Dawei Li, Renliang Sun, Yue Huang, Ming Zhong, Bohan Jiang, Jiawei Han, Xiangliang Zhang, Wei Wang, and Huan Liu
- **Conference:** ICLR 2026

**Key Findings:**

The authors define three common rela
…[truncated 518 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_check_A_20260526T104718",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-26T10:52:07.740556+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"RankME: Reliable Human Ratings for Natural Language Generation\" Novikova 2018 NAACL"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_check_A_20260526T104718",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"RankME: Reliable Human Ratings for Natural Language Generation\" Novikova 2018 NAACL"
  }
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-26T10:52:07.740694+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena\" Zheng 2023 NeurIPS arXiv 2306.05685"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_check_A_20260526T104718",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena\" Zheng 2023 NeurIPS arXiv 2306.05685"
  }
}
```

</details>

---

### Tool call

_source line 54 · 2026-05-26T10:52:07.740824+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Bias in odds ratios by logistic regression modelling and sample size\" Nemes 2009 BMC"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_check_A_20260526T104718",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Bias in odds ratios by logistic regression modelling and sample size\" Nemes 2009 BMC"
  }
}
```

</details>

---

### Tool result

_source line 55 · 2026-05-26T10:52:07.740980+00:00_

Web search results for query: ""Style Outweighs Substance: Failure Modes of LLM Judges" Murugadoss arXiv 2409.15268"

Links: [{"title":"[2409.15268] Style Outweighs Substance: Failure Modes of LLM Judges in Alignment Benchmarking","url":"https://arxiv.org/abs/2409.15268"},{"title":"Style Outweighs Substance: Failure Modes of LLM Judges in Alignment Benchmarking","url":"https://arxiv.org/html/2409.15268"},{"title":"[Literature Review] Style Outweighs Substance: Failure Modes of LLM Judges in Alignment Benchmarking","url":"https://www.themoonlight.io/en/review/style-outweighs-substance-failure-modes-of-llm-judges-in-alignment-benchmarking"},{"title":"Paper page - Style over Substance: Failure Modes of LLM Judges in Alignment Benchmarking","url":"https://huggingface.co/papers/2409.15268"},{"title":"(PDF) Style over Substance: Failure Modes of LLM Judges in Alignment Benchmarking","url":"https://www.researchgate.net/publication/384288829_Style_over_Substance_Failure_Modes_of_LLM_Judges_in_Alignment_Benchmarking"},{"title":"[PDF] Style Outweighs Substance: Failure Modes of LLM Judges in Alignment Benchmarking | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Style-Outweighs-Substance:-Failure-Modes-of-LLM-in-Feuer-Goldblum/50ee11e0d057defe6c449099e01b12cf3cb74446"},{"title":"Mathematical Proof as a Litmus Test: Revealing Failure Modes of Advanced Large Reasoning Models","url":"https://arxiv.org/html/2506.17114v1"},{"title":"When Judgment Becomes Noise: How Design Failures in LLM Judge Benchmarks Silently Undermine Validity","url":"https://arxiv.org/html/2509.20293v1"}]

I found the paper successfully. Here's information about it:

## "Style Outweighs Substance: Failure Modes of LLM Judges in Alignment Benchmarking"

The paper was written by Benjamin Feuer et al. and presented at the International Conference on Learning Representations (ICLR) in 2025.

**Key Research Questions:**

The work attempts to answer whether LLM-judge preferences translate to progre
…[truncated 1029 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_check_A_20260526T104718",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-26T10:52:07.741163+00:00_

Web search results for query: ""FairJudge: An Adaptive, Debiased, and Consistent LLM-as-a-Judge" arXiv 2602.06625"

Links: [{"title":"[2602.06625] FairJudge: An Adaptive, Debiased, and Consistent LLM-as-a-Judge","url":"https://arxiv.org/abs/2602.06625"},{"title":"FairJudge: An Adaptive, Debiased, and Consistent LLM-as-a-Judge","url":"https://arxiv.org/html/2602.06625"},{"title":"LLM-as-a-Judge: Why Frontier Models Fail 50%+ Bias Tests | Adaline","url":"https://www.adaline.ai/blog/llm-as-a-judge-reliability-bias"},{"title":"Who can we trust? LLM-as-a-jury for Comparative Assessment","url":"https://arxiv.org/html/2602.16610v1"},{"title":"[2602.00521] Diagnosing the Reliability of LLM-as-a-Judge via Item Response Theory","url":"https://arxiv.org/abs/2602.00521"},{"title":"Towards Provably Unbiased LLM Judges via Bias-Bounded Evaluation","url":"https://arxiv.org/html/2603.05485"},{"title":"Evaluating Scoring Bias in LLM-as-a-Judge","url":"https://arxiv.org/html/2506.22316v3"}]

Based on the search results, here's information about the paper "FairJudge: An Adaptive, Debiased, and Consistent LLM-as-a-Judge" (arXiv 2602.06625):

## Overview

FairJudge is an adaptive, debiased, and consistent LLM-as-a-Judge. The paper was published in February 2026 by Bo Yang and colleagues.

## Problem Statement

Existing LLM-as-a-Judge systems suffer from three fundamental limitations: limited adaptivity to task- and domain-specific evaluation criteria, systematic biases driven by non-semantic cues such as position, length, format, and model provenance, and evaluation inconsistency that leads to contradictory judgments across different evaluation modes (e.g., pointwise versus pairwise).

## Key Approach

Unlike prior approaches that treat the judge as a static evaluator, FairJudge models judging behavior itself as a learnable and regularized policy. 

From a data-centric perspective, the authors construct a high-information-density judging dataset that explicitly injects supervision signa
…[truncated 499 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_check_A_20260526T104718",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-26T10:52:07.741358+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Best Practices for Using Median Splits Artificial Categorization\" DeCoster 2011 Journal Experimental Psychopathology"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_check_A_20260526T104718",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Best Practices for Using Median Splits Artificial Categorization\" DeCoster 2011 Journal Experimental Psychopathology"
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-26T10:52:07.741521+00:00_

Web search results for query: ""Pairwise or Pointwise? Evaluating Feedback Protocols for Bias in LLM-Based Evaluation" Tripathi 2025"

Links: [{"title":"[2504.14716] Pairwise or Pointwise? Evaluating Feedback Protocols for Bias in LLM-Based Evaluation","url":"https://arxiv.org/abs/2504.14716"},{"title":"Pairwise or Pointwise? Evaluating Feedback Protocols for Bias in LLM-Based Evaluation","url":"https://www.emergentmind.com/papers/2504.14716"},{"title":"[2504.14716v2] Pairwise or Pointwise? Evaluating Feedback Protocols for Bias in LLM-Based Evaluation","url":"https://arxiv.org/abs/2504.14716v2"},{"title":"[2504.14716v1] Pairwise or Pointwise? Evaluating Feedback Protocols for Bias in LLM-Based Evaluation","url":"https://arxiv.org/abs/2504.14716v1"},{"title":"[Literature Review] Pairwise or Pointwise? Evaluating Feedback Protocols for Bias in LLM-Based Evaluation","url":"https://www.themoonlight.io/en/review/pairwise-or-pointwise-evaluating-feedback-protocols-for-bias-in-llm-based-evaluation"},{"title":"Am I More Pointwise or Pairwise? Revealing Position Bias in Rubric-Based LLM-as-a-Judge","url":"https://arxiv.org/html/2602.02219"},{"title":"Pairwise or Pointwise? Evaluating Feedback Protocols for ...","url":"https://arxiv.org/pdf/2504.14716"},{"title":"CodeRankEval: Benchmarking and Analyzing LLM Performance for Code Ranking","url":"https://www.researchgate.net/publication/397827093_CodeRankEval_Benchmarking_and_Analyzing_LLM_Performance_for_Code_Ranking"}]

I found the paper you're looking for. Here's what I found:

**Paper Details:**
"Pairwise or Pointwise? Evaluating Feedback Protocols for Bias in LLM-Based Evaluation" is by Tuhina Tripathi and 3 other authors. The co-authors are Manya Wadhwa, Greg Durrett, and Scott Niekum from University of Massachusetts Amherst and The University of Texas at Austin.

**Main Findings:**
The choice of feedback protocol for evaluation (absolute scores versus relative preferences) can significantly affect evaluation reliability 
…[truncated 826 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_check_A_20260526T104718",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 59 · 2026-05-26T10:52:07.741708+00:00_

Web search results for query: ""Counterfactual LLM-based Framework for Measuring Rhetorical Style" arXiv 2512.19908"

Links: [{"title":"[2512.19908] Counterfactual LLM-based Framework for Measuring Rhetorical Style","url":"https://arxiv.org/abs/2512.19908"},{"title":"Counterfactual LLM-based Framework for Measuring Rhetorical Style","url":"https://arxiv.org/html/2512.19908v1"},{"title":"Counterfactual LLM-based Framework for Measuring Rhetorical Style","url":"https://www.researchgate.net/publication/399026376_Counterfactual_LLM-based_Framework_for_Measuring_Rhetorical_Style"},{"title":"Counterfactual LLM-based Framework for Measuring Rhetorical Style | OpenReview","url":"https://openreview.net/forum?id=fiohEI16sf"},{"title":"[Literature Review] Counterfactual LLM-based Framework for Measuring Rhetorical Style","url":"https://www.themoonlight.io/en/review/counterfactual-llm-based-framework-for-measuring-rhetorical-style"},{"title":"COUNTERFACTUAL LLM-BASED FRAMEWORK FOR ...","url":"https://openreview.net/pdf/e194fe1dda6ea2aff401bf0f16650a9c7d414fd9.pdf"},{"title":"Rhetorical Questions in LLM Representations: A Linear Probing Study","url":"https://arxiv.org/html/2604.14128"},{"title":"Jingyi Qiu (@JingyiQiu4) / Posts / X","url":"https://x.com/JingyiQiu4"}]

Based on the search results, here's what I found about this paper:

## Overview

The paper introduces a counterfactual, LLM-based framework where multiple LLM rhetorical personas generate counterfactual writings from the same substantive content, an LLM judge compares them through pairwise evaluations, and outcomes are aggregated using a Bradley-Terry model.

## Problem Statement

The rise of AI has fueled growing concerns about "hype" in machine learning papers, yet a reliable way to quantify rhetorical style independently of substantive content has remained elusive.

## Methodology

The framework asks how the perception and evaluation of a paper would change if the rhetorical style were altered while the underlyi
…[truncated 629 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_check_A_20260526T104718",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-26T10:52:07.741914+00:00_

Web search results for query: ""Length-Controlled AlpacaEval: A Simple Way to Debias Automatic Evaluators" Dubois arXiv 2404.04475"

Links: [{"title":"[2404.04475] Length-Controlled AlpacaEval: A Simple Way to Debias Automatic Evaluators","url":"https://arxiv.org/abs/2404.04475"},{"title":"Length-Controlled AlpacaEval: A Simple Way to Debias Automatic Evaluators","url":"https://arxiv.org/html/2404.04475v1"},{"title":"[PDF] Length-Controlled AlpacaEval: A Simple Way to Debias Automatic Evaluators | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Length-Controlled-AlpacaEval:-A-Simple-Way-to-Dubois-Galambosi/eb375712bd37250c350ecd3f559e1879e87eb3e5"},{"title":"GitHub - tatsu-lab/alpaca_eval: An automatic evaluator for instruction-following language models. Human-validated, high-quality, cheap, and fast. · GitHub","url":"https://github.com/tatsu-lab/alpaca_eval"},{"title":"Debiasing AlpacaEval via Length Control","url":"https://www.emergentmind.com/papers/2404.04475"},{"title":"Length-Controlled AlpacaEval: A Simple Way to Debias Automatic Eval…","url":"https://www.opentrain.ai/papers/length-controlled-alpacaeval-a-simple-way-to-debias-automatic-evaluators--arxiv-2404.04475/"},{"title":"[Literature Review] Length-Controlled AlpacaEval: A Simple Way to Debias Automatic Evaluators","url":"https://www.themoonlight.io/en/review/length-controlled-alpacaeval-a-simple-way-to-debias-automatic-evaluators"},{"title":"Length Controlled Generation for Black-box LLMs","url":"https://aclanthology.org/2025.acl-long.825.pdf"},{"title":"Rethinking LLM-based Preference Evaluation","url":"https://arxiv.org/html/2407.01085v2"}]

I found the paper you're looking for! Here's what I found:

## Length-Controlled AlpacaEval: A Simple Way to Debias Automatic Evaluators

**Authors:** Yann Dubois, Balázs Galambosi, Percy Liang, and Tatsunori B. Hashimoto

**arXiv ID:** 2404.04475

**Submission Date:** April 6, 2024 (v1), last revised March 10, 2025 (v2)

**Affiliations:** Stanford 
…[truncated 1307 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_check_A_20260526T104718",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 61 · 2026-05-26T10:52:07.742112+00:00_

Web search results for query: ""Best-Worst Scaling More Reliable than Rating Scales" Kiritchenko Mohammad 2017 ACL"

Links: [{"title":"Best-Worst Scaling More Reliable than Rating Scales: A Case Study on Sentiment Intensity Annotation - ACL Anthology","url":"https://aclanthology.org/P17-2074/"},{"title":"[1712.01765] Best-Worst Scaling More Reliable than Rating Scales: A Case Study on Sentiment Intensity Annotation","url":"https://arxiv.org/abs/1712.01765"},{"title":"(PDF) Best-Worst Scaling More Reliable than Rating Scales: A Case Study on Sentiment Intensity Annotation","url":"https://www.researchgate.net/publication/318741851_Best-Worst_Scaling_More_Reliable_than_Rating_Scales_A_Case_Study_on_Sentiment_Intensity_Annotation"},{"title":"[PDF] Best-Worst Scaling More Reliable than Rating Scales: A Case Study on Sentiment Intensity Annotation | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Best-Worst-Scaling-More-Reliable-than-Rating-A-Case-Kiritchenko-Mohammad/524fd6d2bd91bc9fc6ff7f4ee19e52f652718644"},{"title":"Best-Worst Scaling More Reliable than Rating Scales: A Case Study on Sentiment Intensity Annotation - ADS","url":"https://ui.adsabs.harvard.edu/abs/2017arXiv171201765K/abstract"},{"title":"When is best-worst best? A comparison of best-worst scaling, numeric estimation, and rating scales for collection of semantic norms | Behavior Research Methods | Springer Nature Link","url":"https://link.springer.com/article/10.3758/s13428-017-1009-0"},{"title":"Best-worst scaling more reliable than rating scales","url":"https://nrc-publications.canada.ca/eng/view/accepted/?id=b132b0af-2ae0-4964-ac3a-493e7292a37a"},{"title":"(PDF) Best-Worst Scaling More Reliable than Rating Scales: A Case Study on Sentiment Intensity Annotation","url":"https://www.academia.edu/67783414/Best_Worst_Scaling_More_Reliable_than_Rating_Scales_A_Case_Study_on_Sentiment_Intensity_Annotation"},{"title":"“You are an expert annotator”: Automatic Best–Worst-Scaling Annotations for Em
…[truncated 1230 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_check_A_20260526T104718",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-26T10:52:07.742364+00:00_

Web search results for query: ""RATE: Causal Explainability of Reward Models with Imperfect Counterfactuals" Reber arXiv 2410.11348"

Links: [{"title":"[2410.11348] RATE: Causal Explainability of Reward Models with Imperfect Counterfactuals","url":"https://arxiv.org/abs/2410.11348"},{"title":"RATE: Causal Explainability of Reward Models with Imperfect Counterfactuals","url":"https://arxiv.org/html/2410.11348v3"},{"title":"ICML Poster RATE: Causal Explainability of Reward Models with Imperfect Counterfactuals","url":"https://icml.cc/virtual/2025/poster/43898"},{"title":"RATE: Causal Explainability of Reward Models with Imperfect Counterfactuals | OpenReview","url":"https://openreview.net/forum?id=rL3uxe5a0c"},{"title":"RATE: Causal Explainability of Reward Models with Imperfect Counterfactuals","url":"https://proceedings.mlr.press/v267/reber25a.html"},{"title":"[2410.11348v1] RATE: Score Reward Models with Imperfect Rewrites of Rewrites","url":"https://arxiv.org/abs/2410.11348v1"},{"title":"CAUSAL PROXIMAL POLICY OPTIMIZATION","url":"https://openreview.net/pdf?id=kJ2X6wZVlD"},{"title":"CARP: CAUSAL ALIGNMENT OF REWARD MODELS","url":"https://openreview.net/pdf/95856110713620760525308a38513f5a1d10a7f7.pdf"}]

I found the paper you're looking for! Here's what I found about "RATE: Causal Explainability of Reward Models with Imperfect Counterfactuals":

## Overview

The paper is by David Reber and 4 other authors (Sean M. Richardson, Todd Nief, Cristina Garbacea, and Victor Veitch), with arXiv ID 2410.11348.

## Key Contributions

RATE (Rewrite-based Attribute Treatment Estimator) is a method for measuring the sensitivity of a reward model to high-level attributes of responses, such as sentiment, helpfulness, or complexity. 

RATE measures the causal effect of an attribute on the reward and uses LLMs to rewrite responses to produce imperfect counterfactuals examples that can be used to measure causal effects.

## Main Challenge

A key challenge is that these rewrites are 
…[truncated 474 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_check_A_20260526T104718",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 63 · 2026-05-26T10:52:07.742574+00:00_

Web search results for query: ""RankME: Reliable Human Ratings for Natural Language Generation" Novikova 2018 NAACL"

Links: [{"title":"RankME: Reliable Human Ratings for Natural Language Generation - ACL Anthology","url":"https://aclanthology.org/N18-2012/"},{"title":"GitHub - jeknov/RankME: The dataset and code released with the submission of NAACL 2018 paper \"RankME: Reliable Human Ratings for Natural Language Generation\"","url":"https://github.com/jeknov/RankME"},{"title":"[1803.05928] RankME: Reliable Human Ratings for Natural Language Generation","url":"https://arxiv.org/abs/1803.05928"},{"title":"(PDF) RankME: Reliable Human Ratings for Natural Language Generation","url":"https://www.researchgate.net/publication/323846192_RankME_Reliable_Human_Ratings_for_Natural_Language_Generation"},{"title":"RankME: Reliable Human Ratings for Natural Language Generation - Heriot-Watt Research Portal","url":"https://researchportal.hw.ac.uk/en/publications/rankme-reliable-human-ratings-for-natural-language-generation"},{"title":"RankME: Reliable Human Ratings for Natural Language Generation - ADS","url":"https://ui.adsabs.harvard.edu/abs/2018arXiv180305928N/abstract"},{"title":"[PDF] RankME: Reliable Human Ratings for Natural Language Generation | Semantic Scholar","url":"https://www.semanticscholar.org/paper/RankME:-Reliable-Human-Ratings-for-Natural-Language-Novikova-Dusek/f4c8a3f4fb932ef0bdb43f905cc5b9c9031e9af0"},{"title":"metaeval/rankme-nlg-acceptability · Datasets at Hugging Face","url":"https://huggingface.co/datasets/metaeval/rankme-nlg-acceptability"},{"title":"Jekaterina Novikova - ACL Anthology","url":"https://aclweb.org/anthology/people/j/jekaterina-novikova"},{"title":"RankME: Reliable Human Ratings for Natural Language ...","url":"https://aclanthology.org/N18-2012.pdf"}]

I've successfully found the paper you're looking for! Here's what I found:

**Paper Details:**

RankME: Reliable Human Ratings for Natural Language Generation was published by Novikova, Duš
…[truncated 1145 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_check_A_20260526T104718",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-26T10:52:07.742772+00:00_

Web search results for query: ""Bias in odds ratios by logistic regression modelling and sample size" Nemes 2009 BMC"

Links: [{"title":"Bias in odds ratios by logistic regression modelling and sample size | BMC Medical Research Methodology | Springer Nature Link","url":"https://link.springer.com/article/10.1186/1471-2288-9-56"},{"title":"Bias in odds ratios by logistic regression modelling and sample size - PubMed","url":"https://pubmed.ncbi.nlm.nih.gov/19635144/"},{"title":"Bias in odds ratios by logistic regression modelling and sample size - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC2724427/"},{"title":"(PDF) Bias in odds ratios by logistic regression modeling and sample size","url":"https://www.researchgate.net/publication/26698179_Bias_in_odds_ratios_by_logistic_regression_modeling_and_sample_size"},{"title":"Bias in odds ratios by logistic regression modelling and sample size | BMC Medical Research Methodology | Full Text","url":"https://bmcmedresmethodol-biomedcentral-com.translate.goog/articles/10.1186/1471-2288-9-56?_x_tr_sl=en&_x_tr_tl=pt&_x_tr_hl=pt&_x_tr_pto=tc"},{"title":"Peer review reports | Bias in odds ratios by logistic regression modelling and sample size | BMC Medical Research Methodology | Springer Nature Link","url":"https://link.springer.com/article/10.1186/1471-2288-9-56/peer-review"},{"title":"Sample Size Issues for Categorical Analyses and Logistic ...","url":"https://web.pdx.edu/~newsomj/cdaclass/ho_sample%20size.pdf"},{"title":"Google Scholar","url":"https://scholar.google.com/scholar_lookup?title=Bias+in+odds+ratios+by+logistic+regression+modelling+and+sample+size&amp=&author=S+Nemes&amp=&author=JM+Jonasson&amp=&author=A+Genell&amp=&author=G+Steineck&amp=&publication_year=2009&amp=&journal=BMC+Med+Res+Methodol&amp=&volume=9&amp=&pages=56"},{"title":"Bias in odds ratios by logistic re ... | Article | H1 Connect","url":"https://archive.connect.h1.co/article/1164488/"}]

I found the study you're looking for. Here's information a
…[truncated 1265 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_check_A_20260526T104718",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 65 · 2026-05-26T10:52:07.742966+00:00_

Web search results for query: ""Judging the Judges: A Systematic Evaluation of Bias Mitigation Strategies in LLM-as-a-Judge" Soumik arXiv 2604.23178"

Links: [{"title":"[2604.23178] Judging the Judges: A Systematic Evaluation of Bias Mitigation Strategies in LLM-as-a-Judge Pipelines","url":"https://arxiv.org/abs/2604.23178"},{"title":"Judging the Judges: A Systematic Evaluation of Bias Mitigation Strategies in LLM-as-a-Judge Pipelines","url":"https://arxiv.org/html/2604.23178"},{"title":"(PDF) Judging the Judges: A Systematic Evaluation of Bias Mitigation Strategies in LLM-as-a-Judge Pipelines","url":"https://www.researchgate.net/publication/404249222_Judging_the_Judges_A_Systematic_Evaluation_of_Bias_Mitigation_Strategies_in_LLM-as-a-Judge_Pipelines"},{"title":"Judging the Judges: A Systematic Evaluation of Bias Miti-","url":"https://arxiv.org/pdf/2604.23178"},{"title":"Judging the Judges: A Systematic Evaluation of Bi… - arXiv","url":"https://arxiv-troller.com/paper/3154455/"},{"title":"Judging the Judges: A Systematic Study of Position Bias in LLM-as-a-Judge","url":"https://arxiv.org/html/2406.07791v9"},{"title":"Judging the Judges: A Systematic Evaluation of Bias Miti- gation Strategies in LLM-as-a-Judge Pipelines | OpenReview","url":"https://openreview.net/forum?id=QF4lAmG4zc"},{"title":"Juding the Judges: A Systematic Investigation of Position Bias in Pairwise Comparative LLM-as-a-Judge","url":"https://arxiv.org/html/2406.07791v5"},{"title":"[2406.07791] Judging the Judges: A Systematic Study of Position Bias in LLM-as-a-Judge","url":"https://arxiv.org/abs/2406.07791"}]

I found the paper you're looking for. Here's a summary of the key information:

The paper "Judging the Judges: A Systematic Evaluation of Bias Mitigation Strategies in LLM-as-a-Judge Pipelines" by Sadman Kabir Soumik addresses how LLM judges exhibit systematic biases that compromise evaluation reliability.

The study presents a comprehensive empirical study comparing nine debiasing strategies 
…[truncated 825 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_check_A_20260526T104718",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-26T10:52:07.743164+00:00_

Web search results for query: ""Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena" Zheng 2023 NeurIPS arXiv 2306.05685"

Links: [{"title":"[2306.05685] Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena","url":"https://arxiv.org/abs/2306.05685"},{"title":"Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena | OpenReview","url":"https://openreview.net/forum?id=uccHPGDlao"},{"title":"Judging LLM-as-a-judge with MT-bench and Chatbot Arena | Proceedings of the 37th International Conference on Neural Information Processing Systems","url":"https://dl.acm.org/doi/10.5555/3666122.3668142"},{"title":"NeurIPS Poster Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena","url":"https://neurips.cc/virtual/2023/poster/73434"},{"title":"Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena","url":"https://arxiv.org/html/2306.05685v4"},{"title":"Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena | Request PDF","url":"https://www.researchgate.net/publication/401443885_Judging_LLM-as-a-Judge_with_MT-Bench_and_Chatbot_Arena"},{"title":"Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena","url":"https://papers.nips.cc/paper_files/paper/2023/hash/91f18a1287b398d378ef22505bf41832-Abstract-Datasets_and_Benchmarks.html"},{"title":"[Paper Note] Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena, Lianmin Zheng+, NeurIPS'23, 2023.06 · Issue #903 · AkihikoWatanabe/paper_notes","url":"https://github.com/AkihikoWatanabe/paper_notes/issues/903"},{"title":"Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena - United Arab Emirates - Ministry of Health and Prevention","url":"https://nchr.elsevierpure.com/en/publications/judging-llm-as-a-judge-with-mt-bench-and-chatbot-arena/"}]

I found the paper you're looking for! Here are the key details:

**Title:** Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena

**Authors:** Lianmin Zheng, Wei-Lin Chiang, Ying Sheng, Siyuan Zhuang, Zhanghao Wu, Yonghao Zhuang, Zi Lin, Zhuohan Li, Dacheng Li, Eric Xing, Hao Zhang, Joseph Gonza
…[truncated 824 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_check_A_20260526T104718",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 67 · 2026-05-26T10:52:07.743380+00:00_

Web search results for query: ""Best Practices for Using Median Splits Artificial Categorization" DeCoster 2011 Journal Experimental Psychopathology"

Links: [{"title":"Best Practices for Using Median Splits, Artificial Categorization, and their Continuous Alternatives - Jamie DeCoster, Marcello Gallucci, Anne-Marie R. Iselin, 2011","url":"https://journals.sagepub.com/doi/10.5127/jep.008310"},{"title":"(PDF) Best Practices for Using Median Splits, Artificial Categorization, and their Continuous Alternatives","url":"https://www.researchgate.net/publication/274433320_Best_Practices_for_Using_Median_Splits_Artificial_Categorization_and_their_Continuous_Alternatives"},{"title":"Google Scholar","url":"https://scholar.google.com/scholar_lookup?title=Best+practices+for+using+median+splits,+artificial+categorization,+and+their+continuous+alternatives&amp=&author=J.+DeCoster&amp=&author=M.+Gallucci&amp=&author=A.+M.+R.+Iselin&amp=&publication_year=2011&amp=&journal=Journal+of+Experimental+Psychopathology&amp=&pages=197-209&amp=&doi=10.5127/jep.008310"},{"title":"Best Practices for Using Median Splits, Artificial Categorization, and their Continuous Alternatives | 10.5127/jep.008310-Sci_hub","url":"https://www.wellesu.com/10.5127/jep.008310"},{"title":"Best Practices for Using Median Splits, Artificial ...","url":"https://journals.sagepub.com/doi/pdf/10.5127/jep.008310"},{"title":"JCP2015MedianSplitNuanced.pdf","url":"https://cdn.vanderbilt.edu/vu-web/owen/files/publications/JCP2015MedianSplitNuanced.pdf"},{"title":"A Researcher’s Guide to Regression, Discretization, and Median Splits of Continuous Variables | Request PDF","url":"https://www.researchgate.net/publication/276075439_A_Researcher's_Guide_to_Regression_Discretization_and_Median_Splits_of_Continuous_Variables"}]

I found the article you're looking for! Jamie DeCoster, Marcello Gallucci, and Anne-Marie R. Iselin published "Best Practices for Using Median Splits, Artificial Categorization, and their Continuous Altern
…[truncated 1089 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_check_A_20260526T104718",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-26T10:52:07.743576+00:00_

Web search results for query: ""A Concise Agent is Less Expert: Revealing Side Effects of Using Style Features" arXiv 2601.10809"

Links: [{"title":"[2601.10809] A Concise Agent is Less Expert: Revealing Side Effects of Using Style Features on Conversational Agents","url":"https://arxiv.org/abs/2601.10809"},{"title":"A Concise Agent is Less Expert: Revealing Side Effects of Using Style Features on Conversational Agents","url":"https://arxiv.org/html/2601.10809"},{"title":"A Concise Agent is Less Expert: Revealing Side Effects of Using Style Features on Conversational Agents","url":"https://www.catalyzex.com/paper/a-concise-agent-is-less-expert-revealing-side"},{"title":"Computer Science","url":"https://arxiv.org/list/cs/pastweek?skip=235&show=1000"},{"title":"PenForge: On-the-Fly Expert Agent Construction for ...","url":"https://www.arxiv.org/pdf/2601.06910"},{"title":"Agents Are Not Enough | Hacker News","url":"https://news.ycombinator.com/item?id=42611099"},{"title":"Artificial Intelligence May 2025","url":"https://arxiv.org/list/cs.AI/2025-05?skip=3575&show=1000"},{"title":"Machine Learning Jun 2024","url":"https://web3.arxiv.org/list/cs.LG/2024-06?skip=1900&show=2000"},{"title":"Machine Learning Apr 2025","url":"https://www.arxiv.org/list/cs.LG/2025-04?skip=200&show=2000"},{"title":"Computer Science Jun 2025","url":"https://arxiv.org/list/cs/2025-06?skip=9425&show=2000"}]

I found the paper! Here are the key details about arXiv 2601.10809:

**Title:** "A Concise Agent is Less Expert: Revealing Side Effects of Using Style Features on Conversational Agents"

**Overview:** The paper studies style features such as friendly, helpful, or concise used in prompts to steer the behavior of Large Language Model conversational agents, and their unintended side effects.

**Research Approach:** The authors conducted a comprehensive survey of 127 conversational agent papers from ACL Anthology to identify 12 frequently used style features, then used controlled, synthetic dialog
…[truncated 840 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_check_A_20260526T104718",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-26T10:52:07.743806+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2409.15268",
  "prompt": "What is the exact title of this paper? Who are ALL the authors listed? What venue was it published at (if any)?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_check_A_20260526T104718",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2409.15268",
    "prompt": "What is the exact title of this paper? Who are ALL the authors listed? What venue was it published at (if any)?"
  }
}
```

</details>

---

### Tool call

_source line 70 · 2026-05-26T10:52:07.743953+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.23178",
  "prompt": "What is the exact title of this paper? Who are ALL the authors listed? What is the first author's full name?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_check_A_20260526T104718",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2604.23178",
    "prompt": "What is the exact title of this paper? Who are ALL the authors listed? What is the first author's full name?"
  }
}
```

</details>

---

### Tool call

_source line 71 · 2026-05-26T10:52:07.744099+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2601.10809",
  "prompt": "What is the exact title? Who are ALL the authors listed? What is the first author's full name?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_check_A_20260526T104718",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2601.10809",
    "prompt": "What is the exact title? Who are ALL the authors listed? What is the first author's full name?"
  }
}
```

</details>

---

### Tool call

_source line 72 · 2026-05-26T10:52:07.744234+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2502.01534",
  "prompt": "Who are ALL the authors listed? Is the first author \"Dawei Li\"?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_check_A_20260526T104718",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2502.01534",
    "prompt": "Who are ALL the authors listed? Is the first author \"Dawei Li\"?"
  }
}
```

</details>

---

### Tool result

_source line 73 · 2026-05-26T10:52:07.744393+00:00_

**Title:** "Style Outweighs Substance: Failure Modes of LLM Judges in Alignment Benchmarking"

**Authors:** Benjamin Feuer, Micah Goldblum, Teresa Datta, Sanjana Nambiar, Raz Besaleli, Samuel Dooley, Max Cembalest, and John P. Dickerson

**Venue:** ICLR 2025

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_check_A_20260526T104718",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 74 · 2026-05-26T10:52:07.744528+00:00_

# Paper Details

**Exact Title:** "A Concise Agent is Less Expert: Revealing Side Effects of Using Style Features on Conversational Agents"

**All Authors Listed:**
1. Young-Min Cho
2. Yuan Yuan
3. Sharath Chandra Guntuku
4. Lyle Ungar

**First Author's Full Name:** Young-Min Cho

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_check_A_20260526T104718",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 75 · 2026-05-26T10:52:07.744657+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2602.06625",
  "prompt": "Who are ALL the authors listed? What is the first author's full name?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_check_A_20260526T104718",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2602.06625",
    "prompt": "Who are ALL the authors listed? What is the first author's full name?"
  }
}
```

</details>

---

### Tool result

_source line 76 · 2026-05-26T10:52:07.744787+00:00_

# Paper Details

**Exact Title:** "Judging the Judges: A Systematic Evaluation of Bias Mitigation Strategies in LLM-as-a-Judge Pipelines"

**Authors Listed:** Only one author is identified on this arXiv submission.

**First Author's Full Name:** Sadman Kabir Soumik

The webpage shows this paper was submitted on April 25, 2026, and is currently under review at TMLR (Transactions on Machine Learning Research).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_check_A_20260526T104718",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 77 · 2026-05-26T10:52:07.744917+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2512.19908",
  "prompt": "Who are ALL the authors listed? What are their exact names?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_check_A_20260526T104718",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2512.19908",
    "prompt": "Who are ALL the authors listed? What are their exact names?"
  }
}
```

</details>

---

### Tool result

_source line 78 · 2026-05-26T10:52:07.745044+00:00_

# Authors of the Paper

Yes, the first author is "Dawei Li". The complete list of all authors is:

"Dawei Li, Renliang Sun, Yue Huang, Ming Zhong, Bohan Jiang, Jiawei Han, Xiangliang Zhang, Wei Wang, Huan Liu"

There are nine authors total on this arXiv paper about preference leakage in LLM-based evaluation systems.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_check_A_20260526T104718",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 79 · 2026-05-26T10:52:07.745180+00:00_

# Authors of FairJudge Paper

The paper lists six authors in total:

1. **Bo Yang** (first author)
2. Lanfei Feng
3. Yunkui Chen
4. Yu Zhang
5. Xiao Xu
6. Shijian Li

The first author's full name is "Bo Yang" as shown in the arXiv submission metadata.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_check_A_20260526T104718",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 80 · 2026-05-26T10:52:07.745326+00:00_

Based on the content provided, the three authors listed for this paper are:

1. Jingyi Qiu
2. Hong Chen
3. Zongyi Li

The paper header states: "Authors: [Jingyi Qiu](https://arxiv.org/search/cs?searchtype=author&query=Qiu,+J), [Hong Chen](https://arxiv.org/search/cs?searchtype=author&query=Chen,+H), [Zongyi Li](https://arxiv.org/search/cs?searchtype=author&query=Li,+Z)"

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_check_A_20260526T104718",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 81 · 2026-05-26T10:52:07.745601+00:00_

所有信息收集完毕。以下是完整核查报告。

---

## [1]. cohen1988statistical
- 真实性：✓ 存在（经典教材）
- 作者：✓ 正确
- 年份：✓ 正确
- 标题：✓ 正确
- Venue：✓ 正确（书籍）
- 正文引用上下文：✓ 正确（appendix 表格注释中定义 Cohen's d 阈值，引用此书作为出处）

## [2]. pearl2009causality
- 真实性：✓ 存在（经典教材）
- 作者：✓ 正确
- 年份：✓ 正确
- 标题：✓ 正确
- Venue：✓ 正确（书籍，Cambridge University Press）
- 正文引用上下文：✓ 正确（experiments.tex 讨论因果中介分析框架时引用）

## [3]. tripathi2025pairwise
- 真实性：✓ 存在
- 作者：✓ 正确（Tuhina Tripathi, Manya Wadhwa, Greg Durrett, Scott Niekum）
- 年份：✓ 正确
- 标题：✓ 正确
- Venue：✓ 正确（COLM 2025 = 2nd Conference on Language Modeling）
- 正文引用上下文：✓ 正确（experiments.tex 讨论 pairwise vs Likert 的 construct divergence 时引用）

## [4]. murugadoss2025sos
- 真实性：✓ 存在（arXiv:2409.15268）
- 作者：✗ **错误** — bib 中写 `Murugadoss, Aakanksha and others`，实际第一作者是 **Benjamin Feuer**，完整作者列表为 Benjamin Feuer, Micah Goldblum, Teresa Datta, Sanjana Nambiar, Raz Besaleli, Samuel Dooley, Max Cembalest, John P. Dickerson。"Murugadoss" 不在作者列表中。
- 年份：✓ 正确（2025）
- 标题：✓ 正确（"Style Outweighs Substance: Failure Modes of LLM Judges in Alignment Benchmarking"）
- Venue：✓ 正确（ICLR 2025）
- 正文引用上下文：✓ 正确（introduction 说 "Surface-level style features alone explain most of the variance in judge scores"，与该论文发现一致）
- **注意**：bib key `murugadoss2025sos` 与实际第一作者 Feuer 不匹配，应改为 `feuer2025style` 或类似命名，并修正作者字段

## [5]. li2026preference
- 真实性：✓ 存在（arXiv:2502.01534）
- 作者：✓ 正确（Dawei Li 为第一作者，共 9 位作者）
- 年份：✓ 正确（2026）
- 标题：✓ 正确
- Venue：✓ 正确（ICLR 2026）
- 正文引用上下文：✓ 正确（introduction 和 related_work 中引用，related_work 说 "preference leakage propagates through evaluation pipelines" 与论文内容一致）

## [6]. wang2026fairjudge
- 真实性：✓ 存在（arXiv:2602.06625）
- 作者：✓ 正确（Bo Yang, Lanfei Feng, Yunkui Chen, Yu Zhang, Xiao Xu, Shijian Li）
- 年份：✓ 正确
- 标题：✓ 正确
- Venue：✓ 正确（arXiv preprint）
- 正文引用上下文：✓ 正确（introduction 和 related_work 中引用，related_work 说 FairJudge 分解 style 为更细维度但依赖相关性分析，与论文方法一致）
- **注意**：bib key `wang2026fairjudge` 但第一作者姓 Yang，非 Wang。key 命名与作者不匹配。

## [7]. dubois2025lc
- 真实性：✓ 存在（arXiv:2404.04475）
- 作者：✓ 正确（Yann Dubois 为第一作者）
- 年份：✓ 正确
- 标题：✓ 正确
- Venue：✓ 正确（ICLR 2025）
- 正文引用上下文：✓ 正确（introduction 引用为 population-level correction 方法；appendix 引用为 AlpacaEval 基准）

## [8]. casse2026concise
- 真实性：✓ 存在（arXiv:2601.10809）
- 作者：✓ 正确（Cho, Young-Min; Yuan, Yuan; Guntuku, Sharath Chandra; Ungar, Lyle）
- 年份：✓ 正确（2026）
- 标题：✓ 正确
- Venue：✓ 正确（arXiv preprint）
- 正文引用上下文：✓ 正确（related_work 引用 CASSE 框架为多特征分析方法）
- **注意**：bib key `casse2026concise` 以框架名 CASSE 命名而非第一作者 Cho，命名不符常规但不影响正确性

## [9]. counterfactual2025rhetorical
- 真实性：✓ 存在（arXiv:2512.19908）
- 作者：✓ 正确（Qiu, Jingyi; Chen, Hong; Li, Zongyi）
- 年份：✓ 正确（2025）
- 标题：✓ 正确
- Venue：✓ 正确（arXiv preprint）
- 正文引用上下文：✓ 正确（related_work 说 "adopt a similar design at persona-level granularity"，该论文确实使用 LLM rhetorical personas 生成反事实写作）

## [10]. soumik2026judging
- 真实性：✓ 存在（arXiv:2604.23178）
- 作者：✗ **错误** — bib 中写 `Soumik, Mohammad and others`，实际作者全名为 **Sadman Kabir Soumik**（单一作者，无 "others"）。名字 "Mohammad" 错误，应为 "Sadman Kabir"。
- 年份：✓ 正确（2026）
- 标题：✓ 正确
- Venue：✓ 正确（arXiv preprint，currently under review at TMLR）
- 正文引用上下文：✓ 正确（introduction 中 "76–92% of preferences originating from style cues" 对应该论文发现 style bias 0.76–0.92）

## [11]. reber2025rate
- 真实性：✓ 存在（arXiv:2410.11348）
- 作者：✓ 正确（David Reber, Sean Richardson, Todd Nief, Cristina Garbacea, Victor Veitch）
- 年份：✓ 正确
- 标题：✓ 正确
- Venue：✓ 正确（ICML 2025）
- 正文引用上下文：✓ 正确（method.tex 引用 RATE bias correction protocol；related_work 描述其方法为 rewrite + Likert ATE，与论文方法一致）

## [12]. kiritchenko2017bws
- 真实性：✓ 存在
- 作者：✓ 正确（Svetlana Kiritchenko, Saif Mohammad）
- 年份：✓ 正确（2017）
- 标题：✓ 正确（完整标题含副标题 "A Case Study on Sentiment Intensity Annotation"）
- Venue：✓ 正确（ACL 2017 Short Papers）
- 正文引用上下文：**N/A — 未在正文中被引用（orphan bib entry）**

## [13]. novikova2018rankme
- 真实性：✓ 存在
- 作者：✓ 正确（Jekaterina Novikova, Ondřej Dušek, Verena Rieser）
- 年份：✓ 正确（2018）
- 标题：✓ 正确
- Venue：✓ 正确（NAACL 2018 Short Papers）
- 正文引用上下文：✓ 正确（related_work 说 "forced-choice methods detect quality differences that rating scales miss"，与论文发现一致）

## [14]. stevens1946theory
- 真实性：✓ 存在（经典文献）
- 作者：✓ 正确
- 年份：✓ 正确
- 标题：✓ 正确
- Venue：✓ 正确（Science）
- 正文引用上下文：**N/A — 未在正文中被引用（orphan bib entry）**

## [15]. nemes2009bias
- 真实性：✓ 存在
- 作者：✓ 正确（Nemes, Szilard; Jonasson, Jörgen M; Genell, Anna; Steineck, Gunnar）
- 年份：✓ 正确（2009）
- 标题：✓ 正确
- Venue：✓ 正确（BMC Medical Research Methodology, vol 9, 56）
- 正文引用上下文：✓ 正确（experiments.tex 两处引用，说明小样本 odds ratio 存在向上偏差，与论文核心发现一致）

## [16]. david1988method
- 真实性：✓ 存在（经典教材）
- 作者：✓ 正确
- 年份：✓ 正确
- 标题：✓ 正确
- Venue：✓ 正确（书籍，Oxford University Press）
- 正文引用上下文：✓ 正确（introduction 说 pairwise comparison yields higher discriminability than absolute rating，该书正是配对比较方法的经典参考）

## [17]. thurstone1927law
- 真实性：✓ 存在（经典文献）
- 作者：✓ 正确
- 年份：✓ 正确
- 标题：✓ 正确
- Venue：✓ 正确（Psychological Review）
- 正文引用上下文：✓ 正确（introduction 和 related_work 中引用，作为 pairwise comparison 优越性的经典基础）

## [18]. decoster2011median
- 真实性：✓ 存在
- 作者：✓ 正确（DeCoster, Jamie; Gallucci, Marcello; Iselin, Anne-Marie R.）
- 年份：✓ 正确（2011）
- 标题：✓ 正确
- Venue：✓ 正确（Journal of Experimental Psychopathology, vol 2(2), pp 197-209）
- 正文引用上下文：**N/A — 未在正文中被引用（orphan bib entry）**

## [19]. zheng2023judging
- 真实性：✓ 存在（arXiv:2306.05685）
- 作者：✓ 正确（Lianmin Zheng 为第一作者，共 13 位作者）
- 年份：✓ 正确（2023）
- 标题：✓ 正确
- Venue：✓ 正确（NeurIPS 2023）
- 正文引用上下文：✓ 正确（method.tex 引用 MT-Bench；related_work 引用为 LLM-as-judge 基础框架并指出其发现了 position bias；appendix 引用为 MT-Bench 基准说明）

---

## 汇总

**总共 19 条，✓ 14 条完全正确，✗ 2 条有错误，⚠ 3 条 orphan 引用**

### 错误（必须修正）

| # | cite key | 问题 | 修正 |
|---|----------|------|------|
| 4 | `murugadoss2025sos` | 作者错误：写了 `Murugadoss, Aakanksha`，实际第一作者是 `Feuer, Benjamin`，Murugadoss 不在作者列表中 | 改为 `author={Feuer, Benjamin and Goldblum, Micah and Datta, Teresa and Nambiar, Sanjana and Besaleli, Raz and Dooley, Samuel and Cembalest, Max and Dickerson, John P.}`，并考虑将 key 改为 `feuer2025style` |
| 10 | `soumik2026judging` | 作者名错误：写了 `Soumik, Mohammad and others`，实际为单一作者 `Soumik, Sadman Kabir`（无 others） | 改为 `author={Soumik, Sadman Kabir}` |

### 命名不规范（建议修正）

| # | cite key | 问题 |
|---|----------|------|
| 6 | `wang2026fairjudge` | key 前缀 `wang` 但第一作者姓 Yang |
| 8 | `casse2026concise` | key 前缀 `casse` 是框架名，第一作者姓 Cho |

### Orphan 引用（在 bib 中但未在正文引用）

| # | cite key |
|---|----------|
| 12 | `kiritchenko2017bws` |
| 14 | `stevens1946theory` |
| 18 | `decoster2011median` |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_audit_ref_check_A_20260526T104718"
}
```

</details>

---
