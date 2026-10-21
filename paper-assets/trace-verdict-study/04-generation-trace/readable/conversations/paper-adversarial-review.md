# paper adversarial review

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 49
- **Recorded user turns:** 0
- **Tool calls:** 24
- **Original source:** `logs/chats/worker_paper_adversarial-review_20260516T032646.jsonl`
- **Structured JSON:** [`349e44d3c1c73302a390.json`](../../sessions/34/349e44d3c1c73302a390.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

49 recorded events

### Tool call

_source line 1 · 2026-05-16T03:36:07.704879+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Read all paper files",
  "subagent_type": "Explore",
  "prompt": "Read ALL of the following files completely and return their full contents. This is for a paper review task — I need every detail.\n\nFiles to read:\n1. /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/main.tex\n2. /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/introduction.tex\n3. /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/method.tex\n4. /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/experiments.tex\n5. /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/discussion.tex\n6. /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/related_work.tex\n7. /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/conclusion.tex\n8. /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/appendix.tex\n9. /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/references.bib\n10. /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/paper_framing.md\n\nFor each file, return the COMPLETE content — do not summarize or truncate. I need to review every section, every table, every claim."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_adversarial-review_20260516T032646",
  "tool": "Agent",
  "tool_args": {
    "description": "Read all paper files",
    "subagent_type": "Explore",
    "prompt": "Read ALL of the following files completely and return their full contents. This is for a paper review task — I need every detail.\n\nFiles to read:\n1. /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/main.tex\n2. /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/introduction.tex\n3. /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/method.tex\n4. /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/experiments.tex\n5. /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/discussion.tex\n6. /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/related_work.tex\n7. /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/conclusion.tex\n8. /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/appendix.tex\n9. /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/references.bib\n10. /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/paper_framing.md\n\nFor each file, return the COMPLETE content — do not summarize or truncate. I need to review every section, every table, every claim."
  }
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-16T03:36:07.705344+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_adversarial-review_20260516T032646",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 3 · 2026-05-16T03:36:07.705547+00:00_

1	\documentclass[11pt,a4paper]{article}
2	\usepackage[review]{acl}
3	% \usepackage{acl}  % uncomment for camera-ready (remove [review])
4	\usepackage{times,latexsym}
5	\usepackage{amsmath,amssymb}
6	\usepackage{graphicx}
7	\graphicspath{{../../figures/paper/}}
8	\usepackage{booktabs}
9	\usepackage{multirow}
10	\usepackage{xcolor}
11	
12	\title{Exception Events Are All You Need: \\Cross-Model Fault Detection for Verdict Prediction}
13	\author{Anonymous ACL submission}
14	
15	\begin{document}
16	\maketitle
17	
18	\begin{abstract}
19	Execution traces are increasingly used to enhance code language models, but which trace components matter for downstream tasks remains poorly understood.
20	We present the first systematic component ablation of trace representations for \emph{verdict prediction}---classifying whether a test passes or fails---across two models (Qwen-2.5-Coder-7B and DeepSeek-Coder-6.7B).
21	Our key finding is that exception events alone achieve near-perfect accuracy on Qwen (99.83\% $\pm$ 0.00, 3 seeds) and are the most effective component on DeepSeek (2/3 seeds at 99.33\%; 1 outlier at 91.09\% from LoRA initialization sensitivity), while a multi-component representation (VOTA) degrades by 14.96pp on the weaker model, confounded by training-time trace truncation.
22	We decompose the gap between full traces and compressed representations into gradient dilution (26\%) and information overload (74\%), establishing that irrelevant trace content---not training signal quality---is the primary bottleneck.
23	Component ablation reveals a two-tier diagnostic hierarchy: Tier~1 signals (exception events, assertion points) individually achieve ${\geq}$99.8\% accuracy, while Tier~2 signals (loop compression) reach only 85.6\%.
24	These results reframe verdict prediction as fault detection, where the minimal sufficient signal is a compact exception event that transfers well across model families; training stability is a secondary factor for smaller models.
25	\end{abstra
…[truncated 236 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_adversarial-review_20260516T032646",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-16T03:36:07.705717+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_adversarial-review_20260516T032646",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-16T03:36:07.705862+00:00_

1	\section{Introduction}
2	
3	Execution traces---line-by-line records of a program's runtime behavior---have emerged as a promising input modality for code language models.
4	Recent work has explored trace-augmented training for code generation \citep{chen2025tracepile}, execution-aware pretraining \citep{ding2024traced}, trace-based code understanding \citep{wang2025dcsh}, and self-training on trace chain-of-thought \citep{ni2024next}.
5	Yet a fundamental question remains open: \emph{which components of an execution trace actually matter?}
6	
7	\citet{wang2025dcsh} found that no single trace representation consistently outperforms others on generation-oriented tasks, concluding that the utility of execution traces is task- and format-dependent.
8	However, their study focused on code generation and repair---tasks that require the model to simulate or reconstruct execution semantics.
9	\emph{Verdict prediction}---classifying whether a test passes or fails---is a fundamentally different task type: it is a fault detection problem, not a generation problem.
10	Whether the same trace components matter for fault detection as for generation is unknown.
11	
12	We present the first systematic study of what trace components drive verdict prediction performance.
13	Using 591 problems from HumanEval \citep{chen2021evaluating} and MBPP-sanitized \citep{austin2021program} with model-generated solutions and execution traces, we decompose a multi-component trace representation (VOTA: exception events + assertion-point comparisons + loop compression) into individual components and evaluate each in isolation across two models: Qwen-2.5-Coder-7B-Instruct and DeepSeek-Coder-6.7B-Instruct.
14	
15	Our results reveal a striking finding: \textbf{exception events alone achieve near-perfect verdict prediction on Qwen (99.83\% $\pm$ 0.00, 3 seeds) and are the most effective component on DeepSeek, with 2/3 seeds matching Qwen-level accuracy (99.33\%); the remaining seed (91.09\%) reflects LoRA
…[truncated 2822 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_adversarial-review_20260516T032646",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-16T03:36:07.706012+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_adversarial-review_20260516T032646",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-16T03:36:07.706195+00:00_

1	\section{Method}
2	
3	\subsection{Task Definition}
4	
5	We study \emph{verdict prediction}: given a Python function, a test input, and an optional execution trace, predict whether the test passes or fails.
6	The model produces a single token---\texttt{pass} or \texttt{fail}---making this a binary classification task.
7	Unlike code generation \citep{chen2025tracepile} or output prediction \citep{gu2024cruxeval}, verdict prediction isolates the model's ability to detect faults from its ability to simulate execution, providing a cleaner lens on what trace information actually contributes.
8	
9	\subsection{Dataset}
10	\label{sec:dataset}
11	
12	We sampled 10 candidate solutions per problem from Qwen-2.5-Coder-7B-Instruct (temperature 0.8, top\_p 0.95) for 591 problems from HumanEval \citep{chen2021evaluating} (164 problems) and MBPP-sanitized \citep{austin2021program} (427 problems), executed each solution against canonical test cases with \texttt{sys.settrace} to obtain line-level execution traces and pass/fail verdicts, yielding 5,910 trace--verdict pairs (67\% pass, 33\% fail).
13	The dataset is split 80/20 by problem ID into 4,720 training and 1,190 test samples; the test set majority-class baseline is 71.51\%.
14	
15	\paragraph{Deduplication statistics.}
16	Because multiple passing solutions to the same problem produce identical (input, output) pairs in the \texttt{exception\_only} format---correct executions raise no exceptions, so the trace content is the same regardless of the solution's internal logic---the dataset contains duplicate rows.
17	Table~\ref{tab:dedup} reports the duplication rates across formats.
18	Train--test input overlap is zero (split by problem ID), so no information leakage occurs.
19	The high duplication in \texttt{exception\_only} does not affect our experimental conclusions: after deduplication the training set still contains 2,858 unique samples and the test set 607, providing sufficient coverage for the 591-problem benchmark.
20	The \
…[truncated 5063 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_adversarial-review_20260516T032646",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-16T03:36:07.706394+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_adversarial-review_20260516T032646",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-16T03:36:07.706583+00:00_

1	\section{Experiments}
2	
3	We evaluate our trace preprocessing pipeline across two research questions:
4	(1)~Do Tier~1 exception signals generalize across models of different capability?
5	(2)~What is the relative contribution of each trace component to verdict prediction accuracy?
6	All experiments use our trace--verdict dataset (\S\ref{sec:dataset}) with $N{=}1{,}190$ test samples; accuracy is reported with Wilson 95\% confidence intervals unless stated otherwise.
7	Pairwise comparisons use paired bootstrap resampling ($B{=}10{,}000$, seed=42); all cross-condition differences reported below are significant at $p{<}0.0001$ unless noted otherwise.
8	
9	\subsection{Cross-Model Comparison}
10	\label{sec:cross_model}
11	
12	To test whether exception-based trace compression transfers across model families, we compare Qwen-2.5-7B-Instruct and DeepSeek-Coder-6.7B-Instruct under four input conditions: \texttt{exception\_only} (Tier~1 exception events), VOTA (exception + assertion-point + loop compression), \texttt{full\_trace} (complete execution trace), and \texttt{no\_trace} (source code only).
13	
14	\begin{table}[t]
15	\centering
16	\small
17	\begin{tabular}{lccc}
18	\toprule
19	\textbf{Condition} & \textbf{Qwen-2.5-7B} & \textbf{DeepSeek-6.7B} & \textbf{Gap} \\
20	\midrule
21	exception\_only & \textbf{99.83}\% & 99.33\%$^\dag$ & 0.50pp \\
22	VOTA & 99.41\% & 84.45\% & 14.96pp \\
23	VOTA\_no\_ae & 99.41\%$^\S$ & --- & --- \\
24	full\_trace & 81.76\% & 79.16\% & 2.60pp \\
25	no\_trace & 75.13\% & 73.36\% & 1.77pp \\
26	\midrule
27	Majority baseline & 71.51\% & 71.51\% & --- \\
28	\bottomrule
29	\end{tabular}
30	\caption{Cross-model accuracy ($N{=}1{,}190$). Qwen CIs: exception\_only [99.58, 100.00], VOTA [98.82, 99.83], full\_trace [79.70, 83.90], no\_trace [72.77, 77.48]; DeepSeek CIs: full\_trace [76.80, 81.30], VOTA [82.60, 86.40], no\_trace [70.80, 75.70]. $^\dag$DeepSeek \texttt{exception\_only} 3-seed results: 99.33\% (seeds 42, 456; CI [98.82, 99.75]) and 91.09
…[truncated 15713 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_adversarial-review_20260516T032646",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-16T03:36:07.706738+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_adversarial-review_20260516T032646",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/discussion.tex"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-16T03:36:07.706889+00:00_

1	\section{Discussion}
2	
3	\subsection{Why Exception Events Dominate}
4	
5	Verdict prediction is fundamentally a fault detection task: the model must determine whether execution deviated from expected behavior.
6	Exception events are the most explicit signal of such deviation---structured diagnostic moments that encode the nature and location of a fault.
7	Unlike loop compressions or assertion-point values, which require the model to integrate information across multiple trace elements, exception events provide a self-contained verdict cue.
8	This explains why \texttt{exception\_only} matches or exceeds VOTA: adding non-exception trace components dilutes the model's attention on the diagnostic signal rather than providing complementary information.
9	
10	We acknowledge that exception-based verdict prediction is, at its core, fault indicator presence detection: the model learns to map the presence or absence of a structured error message to a binary label, which is close to trivially solvable for any instruction-tuned LLM.
11	The Tier~1 accuracy of ${\geq}$99.8\% is therefore unsurprising in isolation.
12	The contribution of this finding lies not in demonstrating that a strong signal yields high accuracy, but in two less obvious results: (a)~adding more trace information---loop compressions, assertion-point values---actively \emph{hurts} performance (VOTA $<$ \texttt{exception\_only}, Table~\ref{tab:ablation}), quantifying an information density dilution effect that has not been previously measured; and (b)~this dilution is confounded by tokenizer-driven trace truncation on DeepSeek: the DeepSeek tokenizer produces longer sequences than Qwen for identical inputs, causing the majority of VOTA training samples to exceed the context window (\S\ref{sec:cross_model}); the verdict label is preserved, but the trace content is truncated, depriving the model of diagnostic information and contributing to the collapse of DeepSeek VOTA fail recall to 45.43\% (Table~\ref{tab:per
…[truncated 8182 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_adversarial-review_20260516T032646",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-16T03:36:07.707043+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_adversarial-review_20260516T032646",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-16T03:36:07.707176+00:00_

1	\section{Related Work}
2	
3	\paragraph{Execution Traces for Code LLMs.}
4	Several recent efforts have incorporated execution traces into code language model training.
5	TracePile \citep{chen2025tracepile} scaled trace-augmented training to 2.6M samples across multiple programming languages, demonstrating gains on code generation tasks.
6	\citet{wang2025dcsh} conducted a comprehensive study of execution trace-based information for code LLMs across synthesis, repair, and reasoning tasks, finding that trace-based semantic information has limited and inconsistent utility---a finding our work extends by showing that for \emph{verdict prediction}, exception events are a clear dominant signal.
7	NExT \citep{ni2024next} used self-training on execution trace chain-of-thought rationales, improving program repair on MBPP by 26.1\%.
8	ET-CoT \citep{eguchi2025etcot} introduced sub-line granularity traces via PyTracify, achieving 70.0\% on CRUXEval-O with SFT on Qwen2.5-7B.
9	\citet{jung2025execution} used debugger-extracted traces as grounded supervision for LLM reasoning, reducing overthinking while improving cross-domain transfer.
10	\citet{ferrando2025execute} compared regular, compact, and dynamic scratchpad strategies, finding that compact traces (recording only changed variables) perform comparably to full traces---directly supporting our finding that complete value information is redundant.
11	CRUXEval \citep{gu2024cruxeval} established benchmarks for code execution reasoning; CRUXEval-X \citep{xu2025cruxevalx} extended this to 19 programming languages.
12	A common limitation across these studies is that they focus on generation or output prediction tasks; none have decomposed which trace components contribute to \emph{classification} accuracy or tested cross-model generalization of trace signals.
13	
14	\paragraph{Code Verdict and Patch Classification.}
15	TRACED \citep{ding2024traced} showed that execution-aware pretraining improves vulnerability detection and clone d
…[truncated 2561 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_adversarial-review_20260516T032646",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-16T03:36:07.707385+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_adversarial-review_20260516T032646",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-16T03:36:07.707523+00:00_

1	\section{Conclusion}
2	
3	We presented the first systematic study of what execution trace components drive verdict prediction performance.
4	Through component ablation across two code LLMs, we established three findings:
5	
6	\textbf{(1) Exception signal transfer.}
7	Exception events alone achieve 99.83\% $\pm$ 0.00 on Qwen (3 seeds) and 99.33\% on 2/3 DeepSeek seeds, with one outlier at 91.09\% from LoRA initialization sensitivity.
8	Even the outlier exceeds VOTA (84.45\%) by 6.64pp, confirming exception events as the most effective component across models; training stability is a secondary factor for smaller models.
9	In contrast, the full VOTA representation degrades by 14.96pp on DeepSeek---a gap confounded by training-time trace truncation (the majority of DeepSeek VOTA samples exceed the context window; \S\ref{sec:cross_model}) and model capability differences, which cannot be disentangled in the current design.
10	
11	\textbf{(2) Information density decomposition.}
12	The 17.65pp gap between full traces and VOTA decomposes into gradient dilution (26\%, from training on irrelevant trace tokens) and information overload (74\%, from processing irrelevant trace lines at inference).
13	A trace length ablation confirms that input truncation is not the bottleneck: full-trace accuracy remains in a narrow 77--82\% band regardless of token budget (\S\ref{sec:trace_length}).
14	The primary bottleneck is trace content quality, not quantity or loss design.
15	
16	\textbf{(3) Two-tier diagnostic hierarchy.}
17	Tier~1 signals (exception events, assertion points) individually achieve ${\geq}$99.8\% accuracy, while Tier~2 signals (loop compression) reach 85.6\%.
18	Combining tiers in VOTA slightly degrades performance (99.41\%), confirming that additional trace components introduce noise rather than complementary signal.
19	
20	A cross-dataset evaluation on DebugBench (\S\ref{sec:debugbench}) confirms that the exception dominance ranking generalizes: \texttt{exception\_only
…[truncated 717 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_adversarial-review_20260516T032646",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-16T03:36:07.707668+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_adversarial-review_20260516T032646",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/appendix.tex"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-16T03:36:07.707831+00:00_

1	\section{Per-Class Performance Breakdown}
2	\label{sec:per_class}
3	
4	Table~\ref{tab:per_class} reports per-class precision, recall, and F1 for all experimental conditions.
5	
6	\begin{table*}[t]
7	\centering
8	\caption{Per-class precision, recall, and F1 for all experimental conditions (seed 42). DeepSeek VOTA achieves 100\% fail precision but only 45.43\% fail recall, indicating systematic bias toward predicting \texttt{pass}. DeepSeek \texttt{exception\_only} seed 42 achieves 100\% fail recall, but seed 123 drops to 70.5\% (see Table~\ref{tab:full_deepseek}).}
9	\label{tab:per_class}
10	\small
11	\begin{tabular}{llccccccc}
12	\toprule
13	\textbf{Condition} & \textbf{Model} & \textbf{Acc} & \textbf{Pass P} & \textbf{Pass R} & \textbf{Pass F1} & \textbf{Fail P} & \textbf{Fail R} & \textbf{Fail F1} \\
14	\midrule
15	No Trace          & Qwen-2.5-7B & 75.13 & 87.76 & 75.79 & 81.34 & 54.73 & 73.45 & 62.72 \\
16	Full Trace        & Qwen-2.5-7B & 81.76 & 87.74 & 86.60 & 87.17 & 67.43 & 69.62 & 68.51 \\
17	Full Trace (LO)   & Qwen-2.5-7B & 86.22 & 88.21 & 93.18 & 90.63 & 80.07 & 68.73 & 73.97 \\
18	VOTA              & Qwen-2.5-7B & 99.41 & 100.00 & 99.18 & 99.59 & 97.98 & 100.00 & 98.98 \\
19	Exception Only    & Qwen-2.5-7B & 99.83 & 100.00 & 99.76 & 99.88 & 99.41 & 100.00 & 99.71 \\
20	AE Only           & Qwen-2.5-7B & 99.92 & 100.00 & 99.88 & 99.94 & 99.71 & 100.00 & 99.85 \\
21	Loop Only         & Qwen-2.5-7B & 85.63 & 92.39 & 87.07 & 89.66 & 71.65 & 82.01 & 76.48 \\
22	VOTA$-$AE         & Qwen-2.5-7B & 99.41 & 99.88 & 99.29 & 99.59 & 98.26 & 99.71 & 98.98 \\
23	\midrule
24	No Trace          & DeepSeek-6.7B & 73.36 & 81.71 & 80.85 & 81.28 & 53.16 & 54.57 & 53.86 \\
25	Full Trace        & DeepSeek-6.7B & 79.16 & 85.70 & 85.10 & 85.40 & 63.20 & 64.30 & 63.70 \\
26	VOTA              & DeepSeek-6.7B & 84.45 & 82.14 & 100.00 & 90.20 & 100.00 & 45.43 & 62.47 \\
27	Exception Only    & DeepSeek-6.7B & 99.33 & 100.00 & 99.06 & 99.53 & 97.69 & 100.00 & 98.83 \\
28	\bottomrule
…[truncated 8786 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_adversarial-review_20260516T032646",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-16T03:36:07.707986+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_adversarial-review_20260516T032646",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-16T03:36:07.708138+00:00_

1	@inproceedings{chen2025tracepile,
2	  title={Chain of Execution Supervision Promotes General Reasoning in Large Language Models},
3	  author={Nuo Chen and Zehua Li and Keqin Bao and Junyang Lin and Dayiheng Liu},
4	  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
5	  year={2025},
6	  url={https://arxiv.org/abs/2510.23629},
7	}
8	
9	@inproceedings{ding2024traced,
10	  title={TRACED: Execution-aware Pre-training for Source Code},
11	  author={Yangruibo Ding and Ben Steenhoek and Kexin Pei and Gail Kaiser and Wei Le and Baishakhi Ray},
12	  booktitle={Proceedings of the 46th IEEE/ACM International Conference on Software Engineering (ICSE)},
13	  year={2024},
14	  doi={10.1145/3597503.3608140},
15	  url={https://arxiv.org/abs/2306.07487},
16	}
17	
18	@article{chen2021evaluating,
19	  title={Evaluating Large Language Models Trained on Code},
20	  author={Chen, Mark and Tworek, Jerry and Jun, Heewoo and Yuan, Qiming and Pinto, Henrique Ponde de Oliveira and Kaplan, Jared and Edwards, Harri and Burda, Yuri and Joseph, Nicholas and Brockman, Greg and others},
21	  journal={arXiv preprint arXiv:2107.03374},
22	  year={2021},
23	  url={https://arxiv.org/abs/2107.03374},
24	}
25	
26	@article{austin2021program,
27	  title={Program Synthesis with Large Language Models},
28	  author={Austin, Jacob and Odena, Augustus and Nye, Maxwell and Bosma, Maarten and Michalewski, Henryk and Dohan, David and Jiang, Ellen and Cai, Carrie and Terry, Michael and Le, Quoc and Sutton, Charles},
29	  journal={arXiv preprint arXiv:2108.07732},
30	  year={2021},
31	  url={https://arxiv.org/abs/2108.07732},
32	}
33	
34	@inproceedings{gu2024cruxeval,
35	  title={CRUXEval: A Benchmark for Code Reasoning, Understanding and Execution},
36	  author={Alex Gu and Baptiste Rozi{\`e}re and Hugh Leather and Armando Solar-Lezama and Gabriel Synnaeve and Sida I. Wang},
37	  booktitle={Proceedings of the 41st International Conference on Machine Learning (ICML)},
38	  year={2024},
39	  
…[truncated 9029 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_adversarial-review_20260516T032646",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-16T03:36:07.708311+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_adversarial-review_20260516T032646",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/paper_framing.md"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-16T03:36:07.708513+00:00_

1	# Paper Framing — trace-verdict-study
2	
3	> v3.0 — [UPDATED 2026-05-15] D030 CLOSED: DeepSeek VOTA 84.45% confirmed correct (confirmatory re-eval). **Critical narrative fix**: to_chat_text() preserves labels → VOTA 训练时 verdict label 未被截断 → 论文中 "label truncation/corruption" 措辞对 VOTA 不成立。正确叙事: trace INPUT content 被截断 (91.7% samples), 84.45% 反映 trace information loss。新增 D11: VOTA cross-model gap confounded by training-time truncation。数据集来源：HumanEval (164) + MBPP-sanitized (427) = 591 problems × 10 LLM-generated solutions = 5910 samples。
4	
5	## Target Venue
6	- Primary: EMNLP 2026 Main (ARR submission)
7	- Fallback: EMNLP 2026 Findings
8	- Deadline: ARR May 25, 2026
9	
10	## Core Insight
11	
12	Verdict prediction (pass/fail) is fundamentally a **fault detection** task. The most effective signal is the **exception event** — a compact, structured diagnostic moment that consistently outperforms all other trace representations across models (Qwen 99.83% ± 0.00 across 3 seeds; DeepSeek 91-99% depending on seed, but always > VOTA 84.45% and no_trace 73.36%). In contrast, richer trace representations that require deeper execution reasoning show model-dependent effectiveness: VOTA gap = 14.96pp, no_trace gap = 1.77pp. Information density — not training signal distribution — is the primary bottleneck: even oracle loss masking (label-only) cannot close the 13pp gap between full traces and targeted extraction. The design principle: **extract the highest-specificity diagnostic signal; discard everything else.** Cross-model absolute performance depends on LoRA initialization stability, but exception_only's relative dominance over other components is robust.
13	
14	VOTA's primary contribution is **fault indicator isolation** — automatically extracting exception events from noisy full traces — rather than generic trace compression. The "compression helps" narrative was a stepping stone; the real mechanism is diagnostic signal extraction.
15	
16	## Core Claims (3)
17	
18	### Claim 
…[truncated 29635 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_adversarial-review_20260516T032646",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-16T03:36:07.708726+00:00_

## **10. paper_framing.md (continued)**

```markdown
截断 bug 导致 82.6% 预测为 garbage tokens）。

### D9: LoRA initialization sensitivity as secondary bottleneck [NEW — D028]
DeepSeek exception_only seed42=99.83% vs seed123=91.43% (epoch1), 8.40pp gap。Qwen 3 seeds 完全一致。假说：exception signal 的 learnability 取决于 (1) signal 本身的结构简单性（cross-model robust）+ (2) LoRA 初始化是否落入能正确映射 exception→verdict 的 basin。Qwen-7B 可能因模型更强/LoRA landscape 更平滑而对初始化不敏感。DeepSeek-6.7B（CRUXEval-I 39% vs Qwen 56.5%）的 loss landscape 可能更 rugged，LoRA 初始化更易陷入 suboptimal basin（seed123 的 fail_recall 仅 70-72% 说明模型未学到 exception→fail 映射的关键部分）。**论文角度**: 这不是 negative result——它揭示了 trace SFT 的 practical consideration（training stability），可作为 contribution 的一部分。建议 Discussion 讨论 training stabilization 策略（warmup, lr schedule, LoRA rank 调整, multi-seed selection）。

### D10: Train loss ≈ but accuracy ≠ across seeds [NEW — D029]
DeepSeek exception_only seed456 (train_loss=0.1225) 与 seed123 (train_loss=0.122) 训练损失几乎相同，但 accuracy 差 8.2pp（99.33% vs 91.09%）。关键差异集中在 fail_recall（1.0 vs 0.705）——token-level loss 在所有 tokens 上平均，掩盖了 fail 类少数样本的 sample-level 分类能力差异。**Implication**: (1) 扩展 D1 (eval_loss vs accuracy decoupling) 到训练阶段：train_loss 同样不是 verdict task accuracy 的可靠代理指标；(2) 对 checkpoint selection 的实际建议更强：必须用 task-specific metric (accuracy/F1)，甚至 train_loss 收敛也不保证 task performance；(3) fail 类作为少数类（28.5%），其学习质量被平均 loss 稀释——这在 class-imbalanced 设置下是 general pattern，可推广到其他 verdict/detection 任务。

### D11: VOTA cross-model gap: training-time trace truncation as causal factor [NEW — D030 token analysis + group_analysis]
D030 token analysis 确认: `to_chat_text()` 保留 labels（verdict label 在训练时未被截断），但 91.7% 的 DeepSeek VOTA 训练样本的 **trace content** 从 mean 2626 tokens 被截断到 ~2048 tokens。

**Group analysis 提供因果证据**: 将测试集按训练截断状态分组（推理时无截断, max_length=16384），train-truncated 组 accuracy=83.04% vs train-intact 组 accuracy=100%, Fisher exact p≈0。**截断的因果方向可以 claim**: 训练时 trace 被截断导致模型学到的信息不完整 → 推理时即使看到完整 trace 也无法正确判断。模型能力差异是残余 confound（无法完全分离）。

**Implications**
…[truncated 4314 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_adversarial-review_20260516T032646",
  "tool": "Agent",
  "elapsed_ms": 3
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-16T03:36:07.708914+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_adversarial-review_20260516T032646",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-16T03:36:07.709062+00:00_

1	\documentclass[11pt,a4paper]{article}
2	\usepackage[review]{acl}
3	% \usepackage{acl}  % uncomment for camera-ready (remove [review])
4	\usepackage{times,latexsym}
5	\usepackage{amsmath,amssymb}
6	\usepackage{graphicx}
7	\graphicspath{{../../figures/paper/}}
8	\usepackage{booktabs}
9	\usepackage{multirow}
10	\usepackage{xcolor}
11	
12	\title{Exception Events Are All You Need: \\Cross-Model Fault Detection for Verdict Prediction}
13	\author{Anonymous ACL submission}
14	
15	\begin{document}
16	\maketitle
17	
18	\begin{abstract}
19	Execution traces are increasingly used to enhance code language models, but which trace components matter for downstream tasks remains poorly understood.
20	We present the first systematic component ablation of trace representations for \emph{verdict prediction}---classifying whether a test passes or fails---across two models (Qwen-2.5-Coder-7B and DeepSeek-Coder-6.7B).
21	Our key finding is that exception events alone achieve near-perfect accuracy on Qwen (99.83\% $\pm$ 0.00, 3 seeds) and are the most effective component on DeepSeek (2/3 seeds at 99.33\%; 1 outlier at 91.09\% from LoRA initialization sensitivity), while a multi-component representation (VOTA) degrades by 14.96pp on the weaker model, confounded by training-time trace truncation.
22	We decompose the gap between full traces and compressed representations into gradient dilution (26\%) and information overload (74\%), establishing that irrelevant trace content---not training signal quality---is the primary bottleneck.
23	Component ablation reveals a two-tier diagnostic hierarchy: Tier~1 signals (exception events, assertion points) individually achieve ${\geq}$99.8\% accuracy, while Tier~2 signals (loop compression) reach only 85.6\%.
24	These results reframe verdict prediction as fault detection, where the minimal sufficient signal is a compact exception event that transfers well across model families; training stability is a secondary factor for smaller models.
25	\end{abstra
…[truncated 236 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_adversarial-review_20260516T032646",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-16T03:36:07.709209+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_adversarial-review_20260516T032646",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-16T03:36:07.709387+00:00_

1	\section{Introduction}
2	
3	Execution traces---line-by-line records of a program's runtime behavior---have emerged as a promising input modality for code language models.
4	Recent work has explored trace-augmented training for code generation \citep{chen2025tracepile}, execution-aware pretraining \citep{ding2024traced}, trace-based code understanding \citep{wang2025dcsh}, and self-training on trace chain-of-thought \citep{ni2024next}.
5	Yet a fundamental question remains open: \emph{which components of an execution trace actually matter?}
6	
7	\citet{wang2025dcsh} found that no single trace representation consistently outperforms others on generation-oriented tasks, concluding that the utility of execution traces is task- and format-dependent.
8	However, their study focused on code generation and repair---tasks that require the model to simulate or reconstruct execution semantics.
9	\emph{Verdict prediction}---classifying whether a test passes or fails---is a fundamentally different task type: it is a fault detection problem, not a generation problem.
10	Whether the same trace components matter for fault detection as for generation is unknown.
11	
12	We present the first systematic study of what trace components drive verdict prediction performance.
13	Using 591 problems from HumanEval \citep{chen2021evaluating} and MBPP-sanitized \citep{austin2021program} with model-generated solutions and execution traces, we decompose a multi-component trace representation (VOTA: exception events + assertion-point comparisons + loop compression) into individual components and evaluate each in isolation across two models: Qwen-2.5-Coder-7B-Instruct and DeepSeek-Coder-6.7B-Instruct.
14	
15	Our results reveal a striking finding: \textbf{exception events alone achieve near-perfect verdict prediction on Qwen (99.83\% $\pm$ 0.00, 3 seeds) and are the most effective component on DeepSeek, with 2/3 seeds matching Qwen-level accuracy (99.33\%); the remaining seed (91.09\%) reflects LoRA
…[truncated 2822 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_adversarial-review_20260516T032646",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-16T03:36:07.709532+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_adversarial-review_20260516T032646",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-16T03:36:07.709703+00:00_

1	\section{Method}
2	
3	\subsection{Task Definition}
4	
5	We study \emph{verdict prediction}: given a Python function, a test input, and an optional execution trace, predict whether the test passes or fails.
6	The model produces a single token---\texttt{pass} or \texttt{fail}---making this a binary classification task.
7	Unlike code generation \citep{chen2025tracepile} or output prediction \citep{gu2024cruxeval}, verdict prediction isolates the model's ability to detect faults from its ability to simulate execution, providing a cleaner lens on what trace information actually contributes.
8	
9	\subsection{Dataset}
10	\label{sec:dataset}
11	
12	We sampled 10 candidate solutions per problem from Qwen-2.5-Coder-7B-Instruct (temperature 0.8, top\_p 0.95) for 591 problems from HumanEval \citep{chen2021evaluating} (164 problems) and MBPP-sanitized \citep{austin2021program} (427 problems), executed each solution against canonical test cases with \texttt{sys.settrace} to obtain line-level execution traces and pass/fail verdicts, yielding 5,910 trace--verdict pairs (67\% pass, 33\% fail).
13	The dataset is split 80/20 by problem ID into 4,720 training and 1,190 test samples; the test set majority-class baseline is 71.51\%.
14	
15	\paragraph{Deduplication statistics.}
16	Because multiple passing solutions to the same problem produce identical (input, output) pairs in the \texttt{exception\_only} format---correct executions raise no exceptions, so the trace content is the same regardless of the solution's internal logic---the dataset contains duplicate rows.
17	Table~\ref{tab:dedup} reports the duplication rates across formats.
18	Train--test input overlap is zero (split by problem ID), so no information leakage occurs.
19	The high duplication in \texttt{exception\_only} does not affect our experimental conclusions: after deduplication the training set still contains 2,858 unique samples and the test set 607, providing sufficient coverage for the 591-problem benchmark.
20	The \
…[truncated 5063 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_adversarial-review_20260516T032646",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-16T03:36:07.709853+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_adversarial-review_20260516T032646",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-16T03:36:07.710052+00:00_

1	\section{Experiments}
2	
3	We evaluate our trace preprocessing pipeline across two research questions:
4	(1)~Do Tier~1 exception signals generalize across models of different capability?
5	(2)~What is the relative contribution of each trace component to verdict prediction accuracy?
6	All experiments use our trace--verdict dataset (\S\ref{sec:dataset}) with $N{=}1{,}190$ test samples; accuracy is reported with Wilson 95\% confidence intervals unless stated otherwise.
7	Pairwise comparisons use paired bootstrap resampling ($B{=}10{,}000$, seed=42); all cross-condition differences reported below are significant at $p{<}0.0001$ unless noted otherwise.
8	
9	\subsection{Cross-Model Comparison}
10	\label{sec:cross_model}
11	
12	To test whether exception-based trace compression transfers across model families, we compare Qwen-2.5-7B-Instruct and DeepSeek-Coder-6.7B-Instruct under four input conditions: \texttt{exception\_only} (Tier~1 exception events), VOTA (exception + assertion-point + loop compression), \texttt{full\_trace} (complete execution trace), and \texttt{no\_trace} (source code only).
13	
14	\begin{table}[t]
15	\centering
16	\small
17	\begin{tabular}{lccc}
18	\toprule
19	\textbf{Condition} & \textbf{Qwen-2.5-7B} & \textbf{DeepSeek-6.7B} & \textbf{Gap} \\
20	\midrule
21	exception\_only & \textbf{99.83}\% & 99.33\%$^\dag$ & 0.50pp \\
22	VOTA & 99.41\% & 84.45\% & 14.96pp \\
23	VOTA\_no\_ae & 99.41\%$^\S$ & --- & --- \\
24	full\_trace & 81.76\% & 79.16\% & 2.60pp \\
25	no\_trace & 75.13\% & 73.36\% & 1.77pp \\
26	\midrule
27	Majority baseline & 71.51\% & 71.51\% & --- \\
28	\bottomrule
29	\end{tabular}
30	\caption{Cross-model accuracy ($N{=}1{,}190$). Qwen CIs: exception\_only [99.58, 100.00], VOTA [98.82, 99.83], full\_trace [79.70, 83.90], no\_trace [72.77, 77.48]; DeepSeek CIs: full\_trace [76.80, 81.30], VOTA [82.60, 86.40], no\_trace [70.80, 75.70]. $^\dag$DeepSeek \texttt{exception\_only} 3-seed results: 99.33\% (seeds 42, 456; CI [98.82, 99.75]) and 91.09
…[truncated 9257 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_adversarial-review_20260516T032646",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-16T03:36:07.710252+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_adversarial-review_20260516T032646",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/discussion.tex"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-16T03:36:07.710413+00:00_

1	\section{Discussion}
2	
3	Verdict prediction is fundamentally a fault detection task: the model must determine whether execution deviated from expected behavior.
4	Exception events are the most explicit signal of such deviation---structured diagnostic moments that encode the nature and location of a fault.
5	Unlike loop compressions or assertion-point values, which require the model to integrate information across multiple trace elements, exception events provide a self-contained verdict cue.
6	This explains why \texttt{exception\_only} matches or exceeds VOTA: adding non-exception trace components dilutes the model's attention on the diagnostic signal rather than providing complementary information.
7	
8	We acknowledge that exception-based verdict prediction is, at its core, fault indicator presence detection: the model learns to map the presence or absence of a structured error message to a binary label.
9	The Tier~1 accuracy of ${\geq}$99.8\% is therefore unsurprising in isolation.
10	The contribution lies in two less obvious results: (a)~adding more trace information actively \emph{hurts} performance (VOTA $<$ \texttt{exception\_only}, Table~\ref{tab:ablation}), quantifying an information density dilution effect that has not been previously measured; and (b)~this dilution is confounded by tokenizer-driven trace truncation on DeepSeek (\S\ref{sec:cross_model}), which causes the majority of VOTA training samples to exceed the context window, truncating diagnostic trace content while preserving the verdict label.
11	Additional analysis of cross-model robustness (Appendix~\ref{sec:robustness_analysis}), training dynamics (Appendix~\ref{sec:training_dynamics}), and irreducible errors (Appendix~\ref{sec:irreducible}) is provided.
12	
13	\subsection{Limitations}
14	
15	Our study has several limitations.
16	First, our primary experiments use a single dataset (591 problems from HumanEval and MBPP-sanitized); while a cross-dataset evaluation on DebugBench (\S\ref{sec:de
…[truncated 1411 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_adversarial-review_20260516T032646",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-16T03:36:07.710563+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_adversarial-review_20260516T032646",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-16T03:36:07.710712+00:00_

1	\section{Related Work}
2	
3	\paragraph{Execution Traces for Code LLMs.}
4	Several recent efforts have incorporated execution traces into code language model training.
5	TracePile \citep{chen2025tracepile} scaled trace-augmented training to 2.6M samples across multiple programming languages, demonstrating gains on code generation tasks.
6	\citet{wang2025dcsh} conducted a comprehensive study of execution trace-based information for code LLMs across synthesis, repair, and reasoning tasks, finding that trace-based semantic information has limited and inconsistent utility---a finding our work extends by showing that for \emph{verdict prediction}, exception events are a clear dominant signal.
7	NExT \citep{ni2024next} used self-training on execution trace chain-of-thought rationales, improving program repair on MBPP by 26.1\%.
8	ET-CoT \citep{eguchi2025etcot} introduced sub-line granularity traces via PyTracify, achieving 70.0\% on CRUXEval-O with SFT on Qwen2.5-7B.
9	\citet{jung2025execution} used debugger-extracted traces as grounded supervision for LLM reasoning, reducing overthinking while improving cross-domain transfer.
10	\citet{ferrando2025execute} compared regular, compact, and dynamic scratchpad strategies, finding that compact traces (recording only changed variables) perform comparably to full traces---directly supporting our finding that complete value information is redundant.
11	CRUXEval \citep{gu2024cruxeval} established benchmarks for code execution reasoning; CRUXEval-X \citep{xu2025cruxevalx} extended this to 19 programming languages.
12	A common limitation across these studies is that they focus on generation or output prediction tasks; none have decomposed which trace components contribute to \emph{classification} accuracy or tested cross-model generalization of trace signals.
13	
14	\paragraph{Code Verdict and Patch Classification.}
15	TRACED \citep{ding2024traced} showed that execution-aware pretraining improves vulnerability detection and clone d
…[truncated 2561 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_adversarial-review_20260516T032646",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-16T03:36:07.710856+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_adversarial-review_20260516T032646",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-16T03:36:07.710994+00:00_

1	\section{Conclusion}
2	
3	We presented the first systematic study of what execution trace components drive verdict prediction performance.
4	Through component ablation across two code LLMs, we established three findings:
5	
6	\textbf{(1) Exception signal transfer.}
7	Exception events alone achieve 99.83\% $\pm$ 0.00 on Qwen (3 seeds) and 99.33\% on 2/3 DeepSeek seeds, with one outlier at 91.09\% from LoRA initialization sensitivity.
8	Even the outlier exceeds VOTA (84.45\%) by 6.64pp, confirming exception events as the most effective component across models; training stability is a secondary factor for smaller models.
9	In contrast, the full VOTA representation degrades by 14.96pp on DeepSeek---a gap confounded by training-time trace truncation (the majority of DeepSeek VOTA samples exceed the context window; \S\ref{sec:cross_model}) and model capability differences, which cannot be disentangled in the current design.
10	
11	\textbf{(2) Information density decomposition.}
12	The 17.65pp gap between full traces and VOTA decomposes into gradient dilution (26\%, from training on irrelevant trace tokens) and information overload (74\%, from processing irrelevant trace lines at inference).
13	A trace length ablation confirms that input truncation is not the bottleneck: full-trace accuracy remains in a narrow 77--82\% band regardless of token budget (\S\ref{sec:trace_length}).
14	The primary bottleneck is trace content quality, not quantity or loss design.
15	
16	\textbf{(3) Two-tier diagnostic hierarchy.}
17	Tier~1 signals (exception events, assertion points) individually achieve ${\geq}$99.8\% accuracy, while Tier~2 signals (loop compression) reach 85.6\%.
18	Combining tiers in VOTA slightly degrades performance (99.41\%), confirming that additional trace components introduce noise rather than complementary signal.
19	
20	A cross-dataset evaluation on DebugBench (\S\ref{sec:debugbench}) confirms that the exception dominance ranking generalizes (\texttt{exception\_only
…[truncated 472 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_adversarial-review_20260516T032646",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-16T03:36:07.711131+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_adversarial-review_20260516T032646",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/appendix.tex"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-16T03:36:07.711411+00:00_

1	\section{Per-Class Performance Breakdown}
2	\label{sec:per_class}
3	
4	Table~\ref{tab:per_class} reports per-class precision, recall, and F1 for all experimental conditions.
5	
6	\begin{table*}[t]
7	\centering
8	\caption{Per-class precision, recall, and F1 for all experimental conditions (seed 42). DeepSeek VOTA achieves 100\% fail precision but only 45.43\% fail recall, indicating systematic bias toward predicting \texttt{pass}. DeepSeek \texttt{exception\_only} seed 42 achieves 100\% fail recall, but seed 123 drops to 70.5\% (see Table~\ref{tab:full_deepseek}).}
9	\label{tab:per_class}
10	\small
11	\begin{tabular}{llccccccc}
12	\toprule
13	\textbf{Condition} & \textbf{Model} & \textbf{Acc} & \textbf{Pass P} & \textbf{Pass R} & \textbf{Pass F1} & \textbf{Fail P} & \textbf{Fail R} & \textbf{Fail F1} \\
14	\midrule
15	No Trace          & Qwen-2.5-7B & 75.13 & 87.76 & 75.79 & 81.34 & 54.73 & 73.45 & 62.72 \\
16	Full Trace        & Qwen-2.5-7B & 81.76 & 87.74 & 86.60 & 87.17 & 67.43 & 69.62 & 68.51 \\
17	Full Trace (LO)   & Qwen-2.5-7B & 86.22 & 88.21 & 93.18 & 90.63 & 80.07 & 68.73 & 73.97 \\
18	VOTA              & Qwen-2.5-7B & 99.41 & 100.00 & 99.18 & 99.59 & 97.98 & 100.00 & 98.98 \\
19	Exception Only    & Qwen-2.5-7B & 99.83 & 100.00 & 99.76 & 99.88 & 99.41 & 100.00 & 99.71 \\
20	AE Only           & Qwen-2.5-7B & 99.92 & 100.00 & 99.88 & 99.94 & 99.71 & 100.00 & 99.85 \\
21	Loop Only         & Qwen-2.5-7B & 85.63 & 92.39 & 87.07 & 89.66 & 71.65 & 82.01 & 76.48 \\
22	VOTA$-$AE         & Qwen-2.5-7B & 99.41 & 99.88 & 99.29 & 99.59 & 98.26 & 99.71 & 98.98 \\
23	\midrule
24	No Trace          & DeepSeek-6.7B & 73.36 & 81.71 & 80.85 & 81.28 & 53.16 & 54.57 & 53.86 \\
25	Full Trace        & DeepSeek-6.7B & 79.16 & 85.70 & 85.10 & 85.40 & 63.20 & 64.30 & 63.70 \\
26	VOTA              & DeepSeek-6.7B & 84.45 & 82.14 & 100.00 & 90.20 & 100.00 & 45.43 & 62.47 \\
27	Exception Only    & DeepSeek-6.7B & 99.33 & 100.00 & 99.06 & 99.53 & 97.69 & 100.00 & 98.83 \\
28	\bottomrule
…[truncated 21389 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_adversarial-review_20260516T032646",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-16T03:36:07.711601+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/paper_framing.md",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_adversarial-review_20260516T032646",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/paper_framing.md",
    "limit": "200"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-16T03:36:07.711820+00:00_

1	# Paper Framing — trace-verdict-study
2	
3	> v3.0 — [UPDATED 2026-05-15] D030 CLOSED: DeepSeek VOTA 84.45% confirmed correct (confirmatory re-eval). **Critical narrative fix**: to_chat_text() preserves labels → VOTA 训练时 verdict label 未被截断 → 论文中 "label truncation/corruption" 措辞对 VOTA 不成立。正确叙事: trace INPUT content 被截断 (91.7% samples), 84.45% 反映 trace information loss。新增 D11: VOTA cross-model gap confounded by training-time truncation。数据集来源：HumanEval (164) + MBPP-sanitized (427) = 591 problems × 10 LLM-generated solutions = 5910 samples。
4	
5	## Target Venue
6	- Primary: EMNLP 2026 Main (ARR submission)
7	- Fallback: EMNLP 2026 Findings
8	- Deadline: ARR May 25, 2026
9	
10	## Core Insight
11	
12	Verdict prediction (pass/fail) is fundamentally a **fault detection** task. The most effective signal is the **exception event** — a compact, structured diagnostic moment that consistently outperforms all other trace representations across models (Qwen 99.83% ± 0.00 across 3 seeds; DeepSeek 91-99% depending on seed, but always > VOTA 84.45% and no_trace 73.36%). In contrast, richer trace representations that require deeper execution reasoning show model-dependent effectiveness: VOTA gap = 14.96pp, no_trace gap = 1.77pp. Information density — not training signal distribution — is the primary bottleneck: even oracle loss masking (label-only) cannot close the 13pp gap between full traces and targeted extraction. The design principle: **extract the highest-specificity diagnostic signal; discard everything else.** Cross-model absolute performance depends on LoRA initialization stability, but exception_only's relative dominance over other components is robust.
13	
14	VOTA's primary contribution is **fault indicator isolation** — automatically extracting exception events from noisy full traces — rather than generic trace compression. The "compression helps" narrative was a stepping stone; the real mechanism is diagnostic signal extraction.
15	
16	## Core Claims (3)
17	
18	### Claim 
…[truncated 16991 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_adversarial-review_20260516T032646",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-16T03:36:07.711997+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_adversarial-review_20260516T032646",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-16T03:36:07.712192+00:00_

1	@inproceedings{chen2025tracepile,
2	  title={Chain of Execution Supervision Promotes General Reasoning in Large Language Models},
3	  author={Nuo Chen and Zehua Li and Keqin Bao and Junyang Lin and Dayiheng Liu},
4	  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
5	  year={2025},
6	  url={https://arxiv.org/abs/2510.23629},
7	}
8	
9	@inproceedings{ding2024traced,
10	  title={TRACED: Execution-aware Pre-training for Source Code},
11	  author={Yangruibo Ding and Ben Steenhoek and Kexin Pei and Gail Kaiser and Wei Le and Baishakhi Ray},
12	  booktitle={Proceedings of the 46th IEEE/ACM International Conference on Software Engineering (ICSE)},
13	  year={2024},
14	  doi={10.1145/3597503.3608140},
15	  url={https://arxiv.org/abs/2306.07487},
16	}
17	
18	@article{chen2021evaluating,
19	  title={Evaluating Large Language Models Trained on Code},
20	  author={Chen, Mark and Tworek, Jerry and Jun, Heewoo and Yuan, Qiming and Pinto, Henrique Ponde de Oliveira and Kaplan, Jared and Edwards, Harri and Burda, Yuri and Joseph, Nicholas and Brockman, Greg and others},
21	  journal={arXiv preprint arXiv:2107.03374},
22	  year={2021},
23	  url={https://arxiv.org/abs/2107.03374},
24	}
25	
26	@article{austin2021program,
27	  title={Program Synthesis with Large Language Models},
28	  author={Austin, Jacob and Odena, Augustus and Nye, Maxwell and Bosma, Maarten and Michalewski, Henryk and Dohan, David and Jiang, Ellen and Cai, Carrie and Terry, Michael and Le, Quoc and Sutton, Charles},
29	  journal={arXiv preprint arXiv:2108.07732},
30	  year={2021},
31	  url={https://arxiv.org/abs/2108.07732},
32	}
33	
34	@inproceedings{gu2024cruxeval,
35	  title={CRUXEval: A Benchmark for Code Reasoning, Understanding and Execution},
36	  author={Alex Gu and Baptiste Rozi{\`e}re and Hugh Leather and Armando Solar-Lezama and Gabriel Synnaeve and Sida I. Wang},
37	  booktitle={Proceedings of the 41st International Conference on Machine Learning (ICML)},
38	  year={2024},
39	  
…[truncated 9029 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_adversarial-review_20260516T032646",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-16T03:36:07.712387+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__register_artifact",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_adversarial-review_20260516T032646",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__register_artifact",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-16T03:36:07.712515+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_adversarial-review_20260516T032646",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-16T03:36:07.712701+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/_project/report/adversarial_review_report.md",
  "content": "# Adversarial Review Report: EMNLP 2026 Simulation\n\n**Paper**: \"Exception Events Are All You Need: Cross-Model Fault Detection for Verdict Prediction\"\n\n**Simulated venue**: EMNLP 2026 Main Conference (ARR May cycle)\n\n---\n\n## Reviewer 1: Methodology Expert\n\n**Overall Assessment: Borderline**\n**Confidence: 4/5**\n\n### Strengths\n\n1. **Clean experimental decomposition.** The information density decomposition (gradient dilution 26% vs. information overload 74%) via the `full_trace_label_only` ablation is a well-designed causal intervention. This is the most methodologically novel contribution — it separates training signal quality from input signal quality in a way that is reusable by future work.\n\n2. **Transparent reporting of negative/messy results.** The paper does not hide the DeepSeek seed 123 outlier, the VOTA truncation confound, or the DebugBench ceiling effect. The irreducible error analysis (GeneratorExit) is a model of thoroughness.\n\n### Weaknesses (by severity)\n\n**W1 (Major): Insufficient seed coverage — most conditions have n=1 seed.**\nThe headline robustness claim rests on 3 seeds for `exception_only` only. All other conditions (VOTA, full_trace, label_only, ae_only, loop_only, no_trace) report a single seed (42). This is a critical gap: the entire Claim 2 (gradient dilution decomposition) and Claim 3 (two-tier hierarchy) hang on single-seed point estimates. The 86.22% for `label_only` could shift substantially with different seeds, invalidating the 26/74 ratio. At minimum, `ae_only`, `label_only`, and `loop_only` need 3-seed validation on Qwen to confirm the hierarchy is stable.\n\n**Recommendation**: Run 3 seeds for `label_only` and `ae_only` at minimum. If infeasible, add explicit caveats that the decomposition ratio is a point estimate from a single seed.\n\n**W2 (Major): Statistical testing is incomplete for key comparisons.**\n- The `exception_only` vs. `ae_only` comparison (99.83% vs. 99.92%, p=0.80) correctly reports non-significance, but **no effect size or equivalence test** is provided. Non-significance ≠ equivalence. A TOST equivalence test with a meaningful margin (e.g., 1pp) would substantiate the \"statistically indistinguishable\" claim.\n- The 26/74 decomposition has no uncertainty quantification on the ratio itself. Bootstrap the ratio directly (gap_gradient / gap_total) to get a CI on the percentage split.\n- DeepSeek `exception_only` 3-seed results (99.33, 99.33, 91.09) — reporting σ=4.76pp from n=3 is essentially uninformative. The distribution is bimodal, not normal; σ is a misleading summary statistic. Acknowledge the bimodality explicitly and avoid parametric summaries.\n\n**W3 (Moderate): The VOTA cross-model gap is acknowledged as confounded but then used for narrative support.**\nThe paper correctly states \"the two factors cannot be disentangled\" (model capability vs. truncation), but then uses the 14.96pp gap repeatedly to argue that \"richer representations are model-dependent.\" This is overclaiming from confounded evidence. The group analysis (intact 100% vs. truncated 83.04%) provides *directional* evidence but cannot estimate the truncation contribution because the groups differ in other ways (e.g., problem complexity correlates with trace length). The honest framing is: \"VOTA degrades on DeepSeek; truncation is a plausible contributor, but the magnitude of its effect is unknown.\"\n\n**W4 (Moderate): No cross-condition comparison on DeepSeek for ablation.**\nThe two-tier hierarchy (Claim 3) is established entirely on Qwen. DeepSeek only has 4 conditions (exception_only, VOTA, full_trace, no_trace) — no `ae_only`, `loop_only`, or `label_only`. The hierarchy could look different on a weaker model. This limits the \"cross-model\" framing.\n\n**W5 (Minor): Confidence intervals assume independent Bernoulli trials despite acknowledged duplication.**\nThe paper notes 48.99% test set duplication for `exception_only` but reports CIs assuming n=1190. The deduplicated CI (n=607) is mentioned in passing but all main tables use n=1190. This inflates precision. At minimum, report the deduplicated CI as the primary one, or use cluster-robust CIs where duplicates form clusters.\n\n---\n\n## Reviewer 2: Domain Expert / Skeptic\n\n**Overall Assessment: Weak Reject**\n**Confidence: 4/5**\n\n### Strengths\n\n1. **Practical design principle is clear and actionable.** \"Extract the highest-specificity diagnostic signal and discard everything else\" is a useful takeaway for practitioners building trace-augmented systems. The paper demonstrates that over-engineering trace representations can hurt.\n\n2. **Honest self-assessment of contribution scope.** The paper explicitly acknowledges (Introduction, para 4) that exception dominance is \"not itself surprising\" and locates the novelty in the decomposition and cross-model analysis.\n\n### Weaknesses (by severity)\n\n**W1 (Major): The task may be trivially solvable, undermining the significance of findings.**\n99.83% accuracy with a simple presence/absence signal raises a fundamental question: **is this task interesting enough to warrant a paper?** The `exception_only` representation effectively reduces verdict prediction to: \"does the trace contain `[ERROR]`?\" → fail; \"does it not?\" → pass. This is a regex, not a learned representation. The paper argues that the *decomposition* of why other representations fail is the contribution, but if the task is solvable by string matching, the decomposition explains something obvious: noisy inputs hurt classifiers more than clean inputs.\n\nThe irreducible error analysis confirms this — the only errors are where the representation *incorrectly* marks a pass as containing errors (GeneratorExit). The model has learned precisely the trivial rule.\n\n**Counter-argument the paper should address**: What is the accuracy of a zero-shot regex baseline (`grep -c \"[ERROR]\"`)? If it matches 99.83%, the entire SFT pipeline is unnecessary and the contribution collapses. The paper never reports this baseline.\n\n**W2 (Major): Extreme narrowness of evaluation scope.**\n- **2 models, both ~7B, both instruction-tuned**: No encoder models (e.g., CodeBERT for classification), no larger models (13B+, 70B), no API models. The \"cross-model\" framing overstates the diversity — both are decoder-only instruction-tuned code LLMs from the same generation.\n- **1 primary dataset (591 problems)**: HumanEval + MBPP are toy benchmarks with short, self-contained functions. Real verdict prediction involves multi-file projects, complex dependencies, flaky tests, environment-dependent failures, timeout errors without exceptions, assertion failures that don't raise exceptions, etc. The exception_only signal would likely fail catastrophically on assertion-based test frameworks (e.g., pytest where `assert x == y` raises `AssertionError` for both logic errors and expectation mismatches).\n- **DebugBench validation is weak**: 96.71% no_trace baseline → only 3.29pp headroom. This does not validate trace importance; it shows the dataset is too easy.\n- **Python only**: No evidence this transfers to statically-typed languages where exception semantics differ (e.g., Java checked exceptions, Rust panics, Go error returns).\n\n**W3 (Major): The \"fault detection reframing\" is a known perspective, not a novel contribution.**\nThe SE community has long understood that test verdict prediction is fault detection. FuseFL (cited in the paper) already uses structured fault signals including error messages. TRACED uses execution-aware features for vulnerability detection (a fault detection task). The paper's reframing adds terminology but not conceptual novelty.\n\n**W4 (Moderate): Solution generation creates a distribution confound.**\nAll 5,910 solutions were generated by Qwen-2.5-Coder-7B — the same model used for evaluation. This means:\n1. The failure modes in the dataset are Qwen-specific (the types of bugs Qwen makes).\n2. The exception patterns are also Qwen-specific.\n3. Evaluating Qwen on its own failure modes may inflate accuracy (the model \"recognizes\" its own error patterns).\nThe paper acknowledges this in Limitations but dismisses it (\"does not affect verdict prediction\"). This dismissal is unjustified — a model may be better at recognizing bugs it typically makes than bugs from a different distribution.\n\n**W5 (Moderate): Missing practical motivation.**\nWhen would you need ML-based verdict prediction? If you can execute the code (which you must, to get the trace), you already have the verdict. The paper never addresses this deployment scenario question. Possible answers (predicting verdicts for unseen tests, or for partial executions) are not discussed.\n\n---\n\n## Reviewer 3: Writing & Presentation Expert\n\n**Overall Assessment: Weak Accept**\n**Confidence: 3/5**\n\n### Strengths\n\n1. **Exceptionally well-structured paper.** The progression from single-model ablation → decomposition → cross-model validation → cross-dataset validation is logical and easy to follow. Each section answers a clear question.\n\n2. **Tables and figures are information-dense.** Table 1 (cross-model) and Table 2 (ablation) convey the core results efficiently. The trace overview figure (Fig 1) provides helpful visual context. CIs are consistently reported.\n\n### Weaknesses (by severity)\n\n**W1 (Major): The title overclaims.**\n\"Exception Events Are All You Need\" implies universality across tasks and settings. The paper demonstrates this for one task (verdict prediction), one language (Python), two very similar models, and one dataset family. A more accurate title: \"Exception Events Suffice for Verdict Prediction: A Component Ablation Study.\" The AIAYN allusion sets expectations the paper cannot meet.\n\n**W2 (Moderate): Claim 1 framing is convoluted and defensive.**\nThe abstract contains a 4-line sentence describing the DeepSeek seed results with parenthetical qualifications. The Claim 1 statement in the Introduction is 5 lines long with inline statistics. This defensiveness — trying to simultaneously claim robustness while acknowledging the outlier — produces confusing prose. Suggestion: lead with the clean Qwen result as the primary finding, then dedicate a separate paragraph to DeepSeek seed sensitivity as a nuanced secondary finding. Don't try to fit both into a single sentence.\n\n**W3 (Moderate): Overclaiming in several specific places.**\n- Abstract: \"the first systematic component ablation of trace representations for verdict prediction\" — this is likely true but unfalsifiable unless the authors have done an exhaustive literature survey. Consider \"a systematic\" instead.\n- §5.1: \"trace representations should match the model capability floor, not the ceiling\" — this design principle is asserted from a 2-model comparison where the \"floor\" model has a known truncation confound. The evidence doesn't support such a general principle.\n- Conclusion: \"These results reframe verdict prediction as fault detection\" — the reframing is a perspective shift, not a result. The results are accuracy numbers; the reframing is interpretation.\n\n**W4 (Moderate): Related work positioning is incomplete.**\n- No mention of **test outcome prediction** literature from SE (e.g., Bertolino et al.'s work on test case prioritization, or ML-based test flakiness detection). These communities have studied pass/fail prediction for decades.\n- No comparison with **simple ML baselines** (logistic regression on trace features, random forest on exception presence/absence). The paper only compares LLM-based approaches against each other, missing the opportunity to show when LLMs are actually needed.\n- The TRACED citation discusses execution-aware *pretraining* for encoder models — a fundamentally different setup (encoder vs. decoder, pretraining vs. SFT). The comparison is not apples-to-apples but the paper doesn't acknowledge this.\n\n**W5 (Minor): DebugBench results are over-interpreted.**\nThe paper says \"the component ranking is preserved\" on DebugBench but all three conditions are within 3.29pp at >96% accuracy. At these margins, the ranking is not meaningfully testable — CIs likely overlap for VOTA vs. exception_only (99.77% vs. 100%, $\\Delta$=0.23pp). The paper should state that DebugBench confirms the method does not degrade, rather than claiming it \"preserves the ranking.\"\n\n**W6 (Minor): Appendix is heavy; some content belongs in the main paper.**\nThe irreducible error analysis (GeneratorExit) is one of the paper's strongest methodological contributions but is relegated to the appendix. The training dynamics section (loss/accuracy decoupling) is interesting but tangential. Consider promoting the irreducible error analysis and demoting the training dynamics.\n\n---\n\n## Meta-Review: Consolidated Analysis\n\n### Top Weaknesses Flagged by Multiple Reviewers\n\n| # | Weakness | R1 | R2 | R3 | Severity |\n|---|----------|----|----|-----|----------|\n| 1 | **Task triviality / missing regex baseline** | — | W1 | — | Critical |\n| 2 | **Narrow evaluation scope** (2 models, 1 dataset, Python only) | W4 | W2 | W1 | Critical |\n| 3 | **Single-seed conditions** for non-headline results | W1 | — | — | Major |\n| 4 | **VOTA confound used for narrative despite acknowledged limitations** | W3 | — | W3 | Major |\n| 5 | **Overclaiming** (title, design principles, reframing language) | — | W3 | W1,W3 | Major |\n| 6 | **Missing practical motivation** for the task | — | W5 | — | Moderate |\n\n### Most Likely Rejection Reason\n\n**\"The task is too simple and the evaluation too narrow to constitute a sufficient contribution for EMNLP Main.\"**\n\nA skeptical AC would synthesize R2-W1 (task triviality) and R2-W2 (narrow scope) into: the paper demonstrates that a binary classification task with an obvious feature (exception presence) is solvable by that feature, across two similar models on toy benchmarks. The decomposition (Claim 2) and hierarchy (Claim 3) are interesting but rely on single-seed estimates and apply only to this narrow setting. The cross-model story is weakened by the truncation confound.\n\nFindings would be a more appropriate venue unless the evaluation scope is expanded.\n\n### Priority Repair Order (for EMNLP Main acceptance)\n\n**P0 — Must fix before submission (9 days):**\n\n1. **Add a regex/heuristic baseline.** Implement `has_error = \"[ERROR]\" in trace` and report its accuracy. If it matches 99.83%, pivot the framing to: \"SFT is unnecessary for exception-based verdict prediction; the contribution is the decomposition showing *why* simpler signals dominate.\" If it doesn't match (e.g., because the model handles edge cases like GeneratorExit differently), this becomes a strength.\n\n2. **Run 3 seeds for `label_only` and `ae_only` on Qwen.** These are cheap experiments (~2h each × 2 extra seeds = ~8h total). Without them, Claims 2 and 3 rest on single-seed point estimates, which any methodological reviewer will flag.\n\n3. **Soften the title.** \"Exception Events Suffice for Verdict Prediction\" or \"Exception Events Are the Dominant Signal for Verdict Prediction: A Cross-Model Trace Ablation Study.\"\n\n**P1 — Should fix:**\n\n4. **Add a practical motivation paragraph** in the Introduction. Explain *when* verdict prediction without execution is useful (e.g., predicting test outcomes for candidate patches before execution to save CI compute; predicting flakiness; handling partial executions).\n\n5. **Tighten the VOTA cross-model narrative.** Remove all instances where the 14.96pp gap is used to argue general model-dependence of rich representations. Instead, frame it as: \"VOTA performance on DeepSeek is confounded by training-time truncation; the clean cross-model comparison is on exception_only (0.50pp gap).\"\n\n6. **Report deduplicated CIs as primary** for `exception_only` results, or use cluster-robust standard errors.\n\n7. **Promote irreducible error analysis** to the main paper (even 1 paragraph in Discussion). This is one of the paper's strongest selling points.\n\n**P2 — Nice to have:**\n\n8. **Add one more model** (e.g., CodeLlama-7B or StarCoder2-7B) for `exception_only` to strengthen the \"cross-model\" claim. A single condition on a third model is ~2h of compute.\n\n9. **Add one non-ML baseline** (logistic regression on binary exception-presence feature) to demonstrate that SFT adds value beyond the trivial feature.\n\n10. **Acknowledge test outcome prediction literature** from SE in Related Work.\n\n11. **Run DeepSeek ablation** for at least `ae_only` to test whether the two-tier hierarchy holds cross-model.\n\n---\n\n## Predicted Outcome\n\n| Reviewer | Score | Likely disposition |\n|----------|-------|--------------------|\n| R1 (Methodology) | Borderline | Leans reject without multi-seed fixes |\n| R2 (Domain/Skeptic) | Weak Reject | Needs scope expansion or framing pivot |\n| R3 (Writing) | Weak Accept | Fixable with title change and tightening |\n| **Meta** | **Borderline → likely Findings** | Main needs P0 fixes + ideally P1 |\n\n**Bottom line**: The paper has a clean experimental design and honest reporting, but the task triviality concern and narrow scope are the primary threats. The P0 fixes (regex baseline, multi-seed, title) are feasible within 9 days and would shift the paper from \"likely Findings\" to \"competitive for Main.\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_adversarial-review_20260516T032646",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/_project/report/adversarial_review_report.md",
    "content": "# Adversarial Review Report: EMNLP 2026 Simulation\n\n**Paper**: \"Exception Events Are All You Need: Cross-Model Fault Detection for Verdict Prediction\"\n\n**Simulated venue**: EMNLP 2026 Main Conference (ARR May cycle)\n\n---\n\n## Reviewer 1: Methodology Expert\n\n**Overall Assessment: Borderline**\n**Confidence: 4/5**\n\n### Strengths\n\n1. **Clean experimental decomposition.** The information density decomposition (gradient dilution 26% vs. information overload 74%) via the `full_trace_label_only` ablation is a well-designed causal intervention. This is the most methodologically novel contribution — it separates training signal quality from input signal quality in a way that is reusable by future work.\n\n2. **Transparent reporting of negative/messy results.** The paper does not hide the DeepSeek seed 123 outlier, the VOTA truncation confound, or the DebugBench ceiling effect. The irreducible error analysis (GeneratorExit) is a model of thoroughness.\n\n### Weaknesses (by severity)\n\n**W1 (Major): Insufficient seed coverage — most conditions have n=1 seed.**\nThe headline robustness claim rests on 3 seeds for `exception_only` only. All other conditions (VOTA, full_trace, label_only, ae_only, loop_only, no_trace) report a single seed (42). This is a critical gap: the entire Claim 2 (gradient dilution decomposition) and Claim 3 (two-tier hierarchy) hang on single-seed point estimates. The 86.22% for `label_only` could shift substantially with different seeds, invalidating the 26/74 ratio. At minimum, `ae_only`, `label_only`, and `loop_only` need 3-seed validation on Qwen to confirm the hierarchy is stable.\n\n**Recommendation**: Run 3 seeds for `label_only` and `ae_only` at minimum. If infeasible, add explicit caveats that the decomposition ratio is a point estimate from a single seed.\n\n**W2 (Major): Statistical testing is incomplete for key comparisons.**\n- The `exception_only` vs. `ae_only` comparison (99.83% vs. 99.92%, p=0.80) correctly reports non-significance, but **no effect size or equivalence test** is provided. Non-significance ≠ equivalence. A TOST equivalence test with a meaningful margin (e.g., 1pp) would substantiate the \"statistically indistinguishable\" claim.\n- The 26/74 decomposition has no uncertainty quantification on the ratio itself. Bootstrap the ratio directly (gap_gradient / gap_total) to get a CI on the percentage split.\n- DeepSeek `exception_only` 3-seed results (99.33, 99.33, 91.09) — reporting σ=4.76pp from n=3 is essentially uninformative. The distribution is bimodal, not normal; σ is a misleading summary statistic. Acknowledge the bimodality explicitly and avoid parametric summaries.\n\n**W3 (Moderate): The VOTA cross-model gap is acknowledged as confounded but then used for narrative support.**\nThe paper correctly states \"the two factors cannot be disentangled\" (model capability vs. truncation), but then uses the 14.96pp gap repeatedly to argue that \"richer representations are model-dependent.\" This is overclaiming from confounded evidence. The group analysis (intact 100% vs. truncated 83.04%) provides *directional* evidence but cannot estimate the truncation contribution because the groups differ in other ways (e.g., problem complexity correlates with trace length). The honest framing is: \"VOTA degrades on DeepSeek; truncation is a plausible contributor, but the magnitude of its effect is unknown.\"\n\n**W4 (Moderate): No cross-condition comparison on DeepSeek for ablation.**\nThe two-tier hierarchy (Claim 3) is established entirely on Qwen. DeepSeek only has 4 conditions (exception_only, VOTA, full_trace, no_trace) — no `ae_only`, `loop_only`, or `label_only`. The hierarchy could look different on a weaker model. This limits the \"cross-model\" framing.\n\n**W5 (Minor): Confidence intervals assume independent Bernoulli trials despite acknowledged duplication.**\nThe paper notes 48.99% test set duplication for `exception_only` but reports CIs assuming n=1190. The deduplicated CI (n=607) is mentioned in passing but all main tables use n=1190. This inflates precision. At minimum, report the deduplicated CI as the primary one, or use cluster-robust CIs where duplicates form clusters.\n\n---\n\n## Reviewer 2: Domain Expert / Skeptic\n\n**Overall Assessment: Weak Reject**\n**Confidence: 4/5**\n\n### Strengths\n\n1. **Practical design principle is clear and actionable.** \"Extract the highest-specificity diagnostic signal and discard everything else\" is a useful takeaway for practitioners building trace-augmented systems. The paper demonstrates that over-engineering trace representations can hurt.\n\n2. **Honest self-assessment of contribution scope.** The paper explicitly acknowledges (Introduction, para 4) that exception dominance is \"not itself surprising\" and locates the novelty in the decomposition and cross-model analysis.\n\n### Weaknesses (by severity)\n\n**W1 (Major): The task may be trivially solvable, undermining the significance of findings.**\n99.83% accuracy with a simple presence/absence signal raises a fundamental question: **is this task interesting enough to warrant a paper?** The `exception_only` representation effectively reduces verdict prediction to: \"does the trace contain `[ERROR]`?\" → fail; \"does it not?\" → pass. This is a regex, not a learned representation. The paper argues that the *decomposition* of why other representations fail is the contribution, but if the task is solvable by string matching, the decomposition explains something obvious: noisy inputs hurt classifiers more than clean inputs.\n\nThe irreducible error analysis confirms this — the only errors are where the representation *incorrectly* marks a pass as containing errors (GeneratorExit). The model has learned precisely the trivial rule.\n\n**Counter-argument the paper should address**: What is the accuracy of a zero-shot regex baseline (`grep -c \"[ERROR]\"`)? If it matches 99.83%, the entire SFT pipeline is unnecessary and the contribution collapses. The paper never reports this baseline.\n\n**W2 (Major): Extreme narrowness of evaluation scope.**\n- **2 models, both ~7B, both instruction-tuned**: No encoder models (e.g., CodeBERT for classification), no larger models (13B+, 70B), no API models. The \"cross-model\" framing overstates the diversity — both are decoder-only instruction-tuned code LLMs from the same generation.\n- **1 primary dataset (591 problems)**: HumanEval + MBPP are toy benchmarks with short, self-contained functions. Real verdict prediction involves multi-file projects, complex dependencies, flaky tests, environment-dependent failures, timeout errors without exceptions, assertion failures that don't raise exceptions, etc. The exception_only signal would likely fail catastrophically on assertion-based test frameworks (e.g., pytest where `assert x == y` raises `AssertionError` for both logic errors and expectation mismatches).\n- **DebugBench validation is weak**: 96.71% no_trace baseline → only 3.29pp headroom. This does not validate trace importance; it shows the dataset is too easy.\n- **Python only**: No evidence this transfers to statically-typed languages where exception semantics differ (e.g., Java checked exceptions, Rust panics, Go error returns).\n\n**W3 (Major): The \"fault detection reframing\" is a known perspective, not a novel contribution.**\nThe SE community has long understood that test verdict prediction is fault detection. FuseFL (cited in the paper) already uses structured fault signals including error messages. TRACED uses execution-aware features for vulnerability detection (a fault detection task). The paper's reframing adds terminology but not conceptual novelty.\n\n**W4 (Moderate): Solution generation creates a distribution confound.**\nAll 5,910 solutions were generated by Qwen-2.5-Coder-7B — the same model used for evaluation. This means:\n1. The failure modes in the dataset are Qwen-specific (the types of bugs Qwen makes).\n2. The exception patterns are also Qwen-specific.\n3. Evaluating Qwen on its own failure modes may inflate accuracy (the model \"recognizes\" its own error patterns).\nThe paper acknowledges this in Limitations but dismisses it (\"does not affect verdict prediction\"). This dismissal is unjustified — a model may be better at recognizing bugs it typically makes than bugs from a different distribution.\n\n**W5 (Moderate): Missing practical motivation.**\nWhen would you need ML-based verdict prediction? If you can execute the code (which you must, to get the trace), you already have the verdict. The paper never addresses this deployment scenario question. Possible answers (predicting verdicts for unseen tests, or for partial executions) are not discussed.\n\n---\n\n## Reviewer 3: Writing & Presentation Expert\n\n**Overall Assessment: Weak Accept**\n**Confidence: 3/5**\n\n### Strengths\n\n1. **Exceptionally well-structured paper.** The progression from single-model ablation → decomposition → cross-model validation → cross-dataset validation is logical and easy to follow. Each section answers a clear question.\n\n2. **Tables and figures are information-dense.** Table 1 (cross-model) and Table 2 (ablation) convey the core results efficiently. The trace overview figure (Fig 1) provides helpful visual context. CIs are consistently reported.\n\n### Weaknesses (by severity)\n\n**W1 (Major): The title overclaims.**\n\"Exception Events Are All You Need\" implies universality across tasks and settings. The paper demonstrates this for one task (verdict prediction), one language (Python), two very similar models, and one dataset family. A more accurate title: \"Exception Events Suffice for Verdict Prediction: A Component Ablation Study.\" The AIAYN allusion sets expectations the paper cannot meet.\n\n**W2 (Moderate): Claim 1 framing is convoluted and defensive.**\nThe abstract contains a 4-line sentence describing the DeepSeek seed results with parenthetical qualifications. The Claim 1 statement in the Introduction is 5 lines long with inline statistics. This defensiveness — trying to simultaneously claim robustness while acknowledging the outlier — produces confusing prose. Suggestion: lead with the clean Qwen result as the primary finding, then dedicate a separate paragraph to DeepSeek seed sensitivity as a nuanced secondary finding. Don't try to fit both into a single sentence.\n\n**W3 (Moderate): Overclaiming in several specific places.**\n- Abstract: \"the first systematic component ablation of trace representations for verdict prediction\" — this is likely true but unfalsifiable unless the authors have done an exhaustive literature survey. Consider \"a systematic\" instead.\n- §5.1: \"trace representations should match the model capability floor, not the ceiling\" — this design principle is asserted from a 2-model comparison where the \"floor\" model has a known truncation confound. The evidence doesn't support such a general principle.\n- Conclusion: \"These results reframe verdict prediction as fault detection\" — the reframing is a perspective shift, not a result. The results are accuracy numbers; the reframing is interpretation.\n\n**W4 (Moderate): Related work positioning is incomplete.**\n- No mention of **test outcome prediction** literature from SE (e.g., Bertolino et al.'s work on test case prioritization, or ML-based test flakiness detection). These communities have studied pass/fail prediction for decades.\n- No comparison with **simple ML baselines** (logistic regression on trace features, random forest on exception presence/absence). The paper only compares LLM-based approaches against each other, missing the opportunity to show when LLMs are actually needed.\n- The TRACED citation discusses execution-aware *pretraining* for encoder models — a fundamentally different setup (encoder vs. decoder, pretraining vs. SFT). The comparison is not apples-to-apples but the paper doesn't acknowledge this.\n\n**W5 (Minor): DebugBench results are over-interpreted.**\nThe paper says \"the component ranking is preserved\" on DebugBench but all three conditions are within 3.29pp at >96% accuracy. At these margins, the ranking is not meaningfully testable — CIs likely overlap for VOTA vs. exception_only (99.77% vs. 100%, $\\Delta$=0.23pp). The paper should state that DebugBench confirms the method does not degrade, rather than claiming it \"preserves the ranking.\"\n\n**W6 (Minor): Appendix is heavy; some content belongs in the main paper.**\nThe irreducible error analysis (GeneratorExit) is one of the paper's strongest methodological contributions but is relegated to the appendix. The training dynamics section (loss/accuracy decoupling) is interesting but tangential. Consider promoting the irreducible error analysis and demoting the training dynamics.\n\n---\n\n## Meta-Review: Consolidated Analysis\n\n### Top Weaknesses Flagged by Multiple Reviewers\n\n| # | Weakness | R1 | R2 | R3 | Severity |\n|---|----------|----|----|-----|----------|\n| 1 | **Task triviality / missing regex baseline** | — | W1 | — | Critical |\n| 2 | **Narrow evaluation scope** (2 models, 1 dataset, Python only) | W4 | W2 | W1 | Critical |\n| 3 | **Single-seed conditions** for non-headline results | W1 | — | — | Major |\n| 4 | **VOTA confound used for narrative despite acknowledged limitations** | W3 | — | W3 | Major |\n| 5 | **Overclaiming** (title, design principles, reframing language) | — | W3 | W1,W3 | Major |\n| 6 | **Missing practical motivation** for the task | — | W5 | — | Moderate |\n\n### Most Likely Rejection Reason\n\n**\"The task is too simple and the evaluation too narrow to constitute a sufficient contribution for EMNLP Main.\"**\n\nA skeptical AC would synthesize R2-W1 (task triviality) and R2-W2 (narrow scope) into: the paper demonstrates that a binary classification task with an obvious feature (exception presence) is solvable by that feature, across two similar models on toy benchmarks. The decomposition (Claim 2) and hierarchy (Claim 3) are interesting but rely on single-seed estimates and apply only to this narrow setting. The cross-model story is weakened by the truncation confound.\n\nFindings would be a more appropriate venue unless the evaluation scope is expanded.\n\n### Priority Repair Order (for EMNLP Main acceptance)\n\n**P0 — Must fix before submission (9 days):**\n\n1. **Add a regex/heuristic baseline.** Implement `has_error = \"[ERROR]\" in trace` and report its accuracy. If it matches 99.83%, pivot the framing to: \"SFT is unnecessary for exception-based verdict prediction; the contribution is the decomposition showing *why* simpler signals dominate.\" If it doesn't match (e.g., because the model handles edge cases like GeneratorExit differently), this becomes a strength.\n\n2. **Run 3 seeds for `label_only` and `ae_only` on Qwen.** These are cheap experiments (~2h each × 2 extra seeds = ~8h total). Without them, Claims 2 and 3 rest on single-seed point estimates, which any methodological reviewer will flag.\n\n3. **Soften the title.** \"Exception Events Suffice for Verdict Prediction\" or \"Exception Events Are the Dominant Signal for Verdict Prediction: A Cross-Model Trace Ablation Study.\"\n\n**P1 — Should fix:**\n\n4. **Add a practical motivation paragraph** in the Introduction. Explain *when* verdict prediction without execution is useful (e.g., predicting test outcomes for candidate patches before execution to save CI compute; predicting flakiness; handling partial executions).\n\n5. **Tighten the VOTA cross-model narrative.** Remove all instances where the 14.96pp gap is used to argue general model-dependence of rich representations. Instead, frame it as: \"VOTA performance on DeepSeek is confounded by training-time truncation; the clean cross-model comparison is on exception_only (0.50pp gap).\"\n\n6. **Report deduplicated CIs as primary** for `exception_only` results, or use cluster-robust standard errors.\n\n7. **Promote irreducible error analysis** to the main paper (even 1 paragraph in Discussion). This is one of the paper's strongest selling points.\n\n**P2 — Nice to have:**\n\n8. **Add one more model** (e.g., CodeLlama-7B or StarCoder2-7B) for `exception_only` to strengthen the \"cross-model\" claim. A single condition on a third model is ~2h of compute.\n\n9. **Add one non-ML baseline** (logistic regression on binary exception-presence feature) to demonstrate that SFT adds value beyond the trivial feature.\n\n10. **Acknowledge test outcome prediction literature** from SE in Related Work.\n\n11. **Run DeepSeek ablation** for at least `ae_only` to test whether the two-tier hierarchy holds cross-model.\n\n---\n\n## Predicted Outcome\n\n| Reviewer | Score | Likely disposition |\n|----------|-------|--------------------|\n| R1 (Methodology) | Borderline | Leans reject without multi-seed fixes |\n| R2 (Domain/Skeptic) | Weak Reject | Needs scope expansion or framing pivot |\n| R3 (Writing) | Weak Accept | Fixable with title change and tightening |\n| **Meta** | **Borderline → likely Findings** | Main needs P0 fixes + ideally P1 |\n\n**Bottom line**: The paper has a clean experimental design and honest reporting, but the task triviality concern and narrow scope are the primary threats. The P0 fixes (regex baseline, multi-seed, title) are feasible within 9 days and would shift the paper from \"likely Findings\" to \"competitive for Main.\"\n"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-16T03:36:07.713054+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/_project/report/adversarial_review_report.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_adversarial-review_20260516T032646",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-16T03:36:07.713194+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "adversarial_review_report",
  "type": "report",
  "description": "Simulated EMNLP 2026 adversarial review with 3 reviewers (methodology, domain skeptic, writing), consolidated meta-review, and prioritized repair plan",
  "project": "trace-verdict-study",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/_project/report/adversarial_review_report.md",
  "tags": "['review', 'emnlp2026', 'adversarial']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_adversarial-review_20260516T032646",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "adversarial_review_report",
    "type": "report",
    "description": "Simulated EMNLP 2026 adversarial review with 3 reviewers (methodology, domain skeptic, writing), consolidated meta-review, and prioritized repair plan",
    "project": "trace-verdict-study",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/_project/report/adversarial_review_report.md",
    "tags": "['review', 'emnlp2026', 'adversarial']"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-16T03:36:07.713366+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260516_703492\", \"name\": \"adversarial_review_report\", \"type\": \"report\", \"description\": \"Simulated EMNLP 2026 adversarial review with 3 reviewers (methodology, domain skeptic, writing), consolidated meta-review, and prioritized repair plan\", \"path\": \"projects/trace-verdict-study/artifacts/_project/report/adversarial_review_report_703492.md\", \"url\": null, \"project\": \"trace-verdict-study\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-16T03:35:57.171762+00:00\", \"tags\": [\"review\", \"emnlp2026\", \"adversarial\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_adversarial-review_20260516T032646",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 49 · 2026-05-16T03:36:07.713538+00:00_

报告已保存并注册。核心结论：

**预测评分**: R1 Borderline / R2 Weak Reject / R3 Weak Accept → 整体 Borderline，可能进 Findings。

**最致命弱点**（3 个 reviewer 共识）:
1. **任务可能 trivially solvable** — 缺 regex baseline (`"[ERROR]" in trace`)。若 regex 达到 99.83%，整个 SFT pipeline 不必要。
2. **评估范围过窄** — 2 个极相似的 7B 模型，1 个数据集，仅 Python。
3. **非核心条件仅 1 个 seed** — Claims 2、3 的 label_only (86.22%) 和 ae_only (99.92%) 都是单 seed 点估计。

**9 天内必须修复的 P0**:
1. 加 regex/heuristic baseline（1 小时工作量）
2. `label_only` 和 `ae_only` 各跑 3 seeds（~8h GPU）
3. 改标题，去掉 "All You Need" 的过度 claim

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_adversarial-review_20260516T032646"
}
```

</details>

---
