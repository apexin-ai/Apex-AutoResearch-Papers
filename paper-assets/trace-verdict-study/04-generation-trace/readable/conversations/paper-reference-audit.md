# paper reference audit

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 37
- **Recorded user turns:** 0
- **Tool calls:** 18
- **Original source:** `logs/chats/worker_paper_reference-audit_20260516T045759.jsonl`
- **Structured JSON:** [`dced24f195774b1623a4.json`](../../sessions/dc/dced24f195774b1623a4.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

37 recorded events

### Tool call

_source line 1 · 2026-05-16T05:02:38.567482+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.{tex,bib}",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference-audit_20260516T045759",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.{tex,bib}",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-16T05:02:38.567821+00:00_

docs/paper/related_work.tex
docs/paper/references.bib
docs/paper/conclusion.tex
docs/paper/introduction.tex
docs/paper/method.tex
docs/paper/discussion.tex
docs/paper/main.tex
docs/paper/arr_checklist.tex
docs/paper/experiments.tex
docs/paper/appendix.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference-audit_20260516T045759",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-16T05:02:38.567979+00:00_

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
  "session": "worker_paper_reference-audit_20260516T045759",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-16T05:02:38.568141+00:00_

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
…[truncated 2492 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference-audit_20260516T045759",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-16T05:02:38.568336+00:00_

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
  "session": "worker_paper_reference-audit_20260516T045759",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-16T05:02:38.568536+00:00_

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
  "session": "worker_paper_reference-audit_20260516T045759",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-16T05:02:38.568693+00:00_

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
  "session": "worker_paper_reference-audit_20260516T045759",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-16T05:02:38.568847+00:00_

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
15	Our results reveal that \textbf{exception events alone achieve near-perfect verdict prediction on Qwen (99.83\% $\pm$ 0.00, 3 seeds) and are the most effective component on DeepSeek (2/3 seeds at 99.33\%; 1 outlier at 91.09\% from LoRA initialization sensitivity).}
16	Even the outlier outperfor
…[truncated 1748 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference-audit_20260516T045759",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-16T05:02:38.568996+00:00_

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
  "session": "worker_paper_reference-audit_20260516T045759",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-16T05:02:38.569156+00:00_

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
15	The \texttt{exception\_only} format collapses multiple passing solutions into identical rows (39.45\% train, 48.99\% test duplicates) because correct executions produce no exception events; train--test input overlap is zero (no leakage).
16	Full deduplication statistics are in Appendix~\ref{sec:dedup_stats}.
17	
18	\subsection{Trace Representations}
19	
20	We define seven input conditions that systematically vary the trace information available to the model (Figure~\ref{fig:trace_overview}):
21	
22	\begin{itemize}
23	\item \texttt{no\_trace}: Source code and test input only; no execution information.
24	\item \texttt{full\_trace}: Complete line-by-line execution trace recording variable states at each step.
25	\item \texttt{VOTA} (Verdict-Oriented Tr
…[truncated 3493 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference-audit_20260516T045759",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-16T05:02:38.569345+00:00_

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
  "session": "worker_paper_reference-audit_20260516T045759",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-16T05:02:38.569549+00:00_

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
…[truncated 10560 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference-audit_20260516T045759",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-16T05:02:38.569701+00:00_

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
  "session": "worker_paper_reference-audit_20260516T045759",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/discussion.tex"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-16T05:02:38.569842+00:00_

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
11	A regex baseline analysis sharpens this point: the strongest legitimate regex (exception type pattern-matching) achieves 93.61\%, while a format-marker heuristic reaches 99.33\% by exploiting a data formatting artifact rather than exception semantics (Appendix~\ref{sec:regex_baselines}).
12	The 6.22pp gap between regex and SFT concentrates on boundary samples where exceptions are raised but caught by \texttt{try/except}---SFT correctly classifies 6/8,
…[truncated 915 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference-audit_20260516T045759",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-16T05:02:38.569980+00:00_

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
  "session": "worker_paper_reference-audit_20260516T045759",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-16T05:02:38.570127+00:00_

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
  "session": "worker_paper_reference-audit_20260516T045759",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-16T05:02:38.570321+00:00_

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
  "session": "worker_paper_reference-audit_20260516T045759",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-16T05:02:38.570470+00:00_

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
  "session": "worker_paper_reference-audit_20260516T045759",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-16T05:02:38.570617+00:00_

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
  "session": "worker_paper_reference-audit_20260516T045759",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/appendix.tex"
  }
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-16T05:02:38.570738+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/arr_checklist.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference-audit_20260516T045759",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/arr_checklist.tex"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-16T05:02:38.570893+00:00_

1	\documentclass[11pt,a4paper]{article}
2	\usepackage[review]{acl}
3	\usepackage{times,latexsym}
4	\usepackage{booktabs}
5	
6	\title{ARR Reproducibility Checklist\\(Supplementary Material)}
7	\author{Anonymous ACL submission}
8	
9	\begin{document}
10	\maketitle
11	
12	\section*{Responsible NLP Research Checklist}
13	
14	\subsection*{A. Limitations and Risks}
15	
16	\begin{enumerate}
17	\item \textbf{Did you discuss the limitations of your work?} \\
18	\textit{Yes.} A dedicated Limitations section discusses: single-dataset scope, single model scale (7B), seed-dependent variance on DeepSeek, the invalidated full\_trace run, generator--evaluator overlap, and task scope limited to verdict prediction.
19	
20	\item \textbf{Did you discuss any potential risks of your work?} \\
21	\textit{Yes.} The Ethics Statement notes that the work uses public benchmarks, involves no human subjects, and has minimal environmental impact. Verdict prediction is a developer-facing tool with no direct end-user impact.
22	\end{enumerate}
23	
24	\subsection*{B. Did you use or create scientific artifacts?}
25	
26	\begin{enumerate}
27	\item \textbf{Did you cite the creators of artifacts you used?} \\
28	\textit{Yes.} HumanEval \cite{chen2021evaluating}, MBPP-sanitized \cite{austin2021program}, DebugBench \cite{tian2024debugbench}, Qwen-2.5-Coder-7B-Instruct \cite{qwen2025coder}, DeepSeek-Coder-6.7B-Instruct \cite{deepseek2024coder}, LoRA \cite{hu2022lora}, and TRL SFTTrainer are all cited.
29	
30	\item \textbf{Did you discuss the license or terms for use and/or distribution of any artifacts?} \\
31	\textit{Partial.} All base models and datasets are publicly available. HumanEval is released under MIT license; MBPP under CC-BY-4.0; DebugBench under MIT. Model licenses: Qwen-2.5-Coder under Apache 2.0; DeepSeek-Coder under the DeepSeek License.
32	
33	\item \textbf{Did you discuss if your use of existing artifacts was consistent with their intended use?} \\
34	\textit{Yes.} HumanEval and MBPP are st
…[truncated 3773 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference-audit_20260516T045759",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-16T05:02:38.571207+00:00_

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
…[truncated 28570 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference-audit_20260516T045759",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-16T05:02:38.571519+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\cite[pt]?\\{[^}]+\\}",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference-audit_20260516T045759",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\cite[pt]?\\{[^}]+\\}",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-16T05:02:38.571702+00:00_

docs/paper/related_work.tex:5:TracePile \citep{chen2025tracepile} scaled trace-augmented training to 2.6M samples across multiple programming languages, demonstrating gains on code generation tasks.
docs/paper/related_work.tex:6:\citet{wang2025dcsh} conducted a comprehensive study of execution trace-based information for code LLMs across synthesis, repair, and reasoning tasks, finding that trace-based semantic information has limited and inconsistent utility---a finding our work extends by showing that for \emph{verdict prediction}, exception events are a clear dominant signal.
docs/paper/related_work.tex:7:NExT \citep{ni2024next} used self-training on execution trace chain-of-thought rationales, improving program repair on MBPP by 26.1\%.
docs/paper/related_work.tex:8:ET-CoT \citep{eguchi2025etcot} introduced sub-line granularity traces via PyTracify, achieving 70.0\% on CRUXEval-O with SFT on Qwen2.5-7B.
docs/paper/related_work.tex:9:\citet{jung2025execution} used debugger-extracted traces as grounded supervision for LLM reasoning, reducing overthinking while improving cross-domain transfer.
docs/paper/related_work.tex:10:\citet{ferrando2025execute} compared regular, compact, and dynamic scratchpad strategies, finding that compact traces (recording only changed variables) perform comparably to full traces---directly supporting our finding that complete value information is redundant.
docs/paper/related_work.tex:11:CRUXEval \citep{gu2024cruxeval} established benchmarks for code execution reasoning; CRUXEval-X \citep{xu2025cruxevalx} extended this to 19 programming languages.
docs/paper/related_work.tex:15:TRACED \citep{ding2024traced} showed that execution-aware pretraining improves vulnerability detection and clone detection, using encoder-based models with trace-augmented objectives.
docs/paper/related_work.tex:16:In automated patch correctness prediction, APPT \citep{appt2024} fine-tuned pre-trained models with BERT+LSTM achieving 79.7\% accuracy on Defects4J pa
…[truncated 6215 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference-audit_20260516T045759",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-16T05:02:38.571857+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\label\\{[^}]+\\}",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference-audit_20260516T045759",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\label\\{[^}]+\\}",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-16T05:02:38.571996+00:00_

docs/paper/experiments.tex:10:\label{sec:cross_model}
docs/paper/experiments.tex:31:\label{tab:cross_model}
docs/paper/experiments.tex:57:\label{fig:cross_model_gap}
docs/paper/experiments.tex:61:\label{sec:ablation}
docs/paper/experiments.tex:87:\label{tab:ablation}
docs/paper/experiments.tex:101:\label{sec:density}
docs/paper/experiments.tex:119:\label{tab:density}
docs/paper/experiments.tex:126:\label{sec:trace_length}
docs/paper/experiments.tex:133:\label{sec:calibration}
docs/paper/experiments.tex:139:\label{sec:debugbench}
docs/paper/method.tex:10:\label{sec:dataset}
docs/paper/method.tex:38:\label{fig:trace_overview}
docs/paper/appendix.tex:2:\label{sec:per_class}
docs/paper/appendix.tex:9:\label{tab:per_class}
docs/paper/appendix.tex:34:\label{sec:training_details}
docs/paper/appendix.tex:42:\label{tab:hyperparams}
docs/paper/appendix.tex:81:\label{tab:train_time}
docs/paper/appendix.tex:103:\label{sec:vota_examples}
docs/paper/appendix.tex:161:\label{sec:full_results}
docs/paper/appendix.tex:168:\label{tab:full_qwen}
docs/paper/appendix.tex:191:\label{tab:full_deepseek}
docs/paper/appendix.tex:212:\label{sec:irreducible}
docs/paper/appendix.tex:233:\label{sec:trace_length_full}
docs/paper/appendix.tex:251:\label{tab:trace_length}
docs/paper/appendix.tex:258:\label{fig:trace_length}
docs/paper/appendix.tex:293:\label{tab:trace_length_pairwise}
docs/paper/appendix.tex:314:\label{sec:calibration_full}
docs/paper/appendix.tex:333:\label{tab:calibration}
docs/paper/appendix.tex:346:\label{fig:calibration}
docs/paper/appendix.tex:351:\label{sec:debugbench_full}
docs/paper/appendix.tex:371:\label{tab:debugbench}
docs/paper/appendix.tex:386:\label{sec:robustness_analysis}
docs/paper/appendix.tex:399:\label{sec:training_dynamics}
docs/paper/appendix.tex:415:\label{sec:dedup_stats}
docs/paper/appendix.tex:436:\label{tab:dedup}
docs/paper/appendix.tex:441:\label{sec:regex_baselines}
docs/paper/appendix.tex:463:\label{tab:regex}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference-audit_20260516T045759",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-16T05:02:38.572127+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\ref\\{[^}]+\\}",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference-audit_20260516T045759",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\ref\\{[^}]+\\}",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-16T05:02:38.572319+00:00_

docs/paper/discussion.tex:10:[Omitted long matching line]
docs/paper/discussion.tex:11:A regex baseline analysis sharpens this point: the strongest legitimate regex (exception type pattern-matching) achieves 93.61\%, while a format-marker heuristic reaches 99.33\% by exploiting a data formatting artifact rather than exception semantics (Appendix~\ref{sec:regex_baselines}).
docs/paper/discussion.tex:14:Training dynamics further illustrate the complexity beneath surface-level metrics: on DeepSeek, two seeds converge to nearly identical final training losses (0.122 vs.\ 0.123) yet differ by 8.24pp in accuracy, demonstrating that token-level loss can mask fundamental differences in sample-level classification ability (Appendix~\ref{sec:training_dynamics}).
docs/paper/discussion.tex:15:The \texttt{exception\_only} 0.50pp cross-model gap---unaffected by truncation since inputs average ${\sim}$200 tokens---provides a clean measure of model capability differences, suggesting a design principle: trace representations should match the model capability floor, not the ceiling (Appendix~\ref{sec:robustness_analysis}).
docs/paper/discussion.tex:16:Additional analysis of irreducible errors is in Appendix~\ref{sec:irreducible}.
docs/paper/experiments.tex:6:All experiments use our trace--verdict dataset (\S\ref{sec:dataset}) with $N{=}1{,}190$ test samples; accuracy is reported with Wilson 95\% confidence intervals unless stated otherwise.
docs/paper/experiments.tex:34:Table~\ref{tab:cross_model} reveals a striking asymmetry.
docs/paper/experiments.tex:36:Even the outlier seed outperforms VOTA (84.45\%) by 6.64pp, confirming exception events as the most effective component across models (Figure~\ref{fig:cross_model_gap}).
docs/paper/experiments.tex:43:Per-class analysis (Appendix~\ref{sec:per_class}) reveals the mechanism: DeepSeek VOTA achieves 100\% fail precision but only 45.43\% fail recall, systematically defaulting to \texttt{pass}---in contrast to Qwen VOTA, which achieves 10
…[truncated 9555 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference-audit_20260516T045759",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-16T05:02:38.572495+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/appendix.tex",
  "offset": "470"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference-audit_20260516T045759",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/appendix.tex",
    "offset": "470"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-16T05:02:38.572620+00:00_

&lt;system-reminder>Warning: the file exists but is shorter than the provided offset (470). The file has 470 lines.&lt;/system-reminder>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference-audit_20260516T045759",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-16T05:02:38.572774+00:00_

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
  "session": "worker_paper_reference-audit_20260516T045759",
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

_source line 32 · 2026-05-16T05:02:38.572896+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference-audit_20260516T045759",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-16T05:02:38.573051+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/reference_audit_report.md",
  "content": "# Paper Audit Report: trace-verdict-study\n\n**Date**: 2026-05-16  \n**Scope**: Citation integrity, data consistency, cross-references, ARR compliance, formatting\n\n---\n\n## 1. Citation Audit\n\n### 1.1 Cross-Check Results\n\n| Check | Result |\n|-------|--------|\n| Cited keys in .tex files | 28 unique keys |\n| Bib entries in references.bib | 28 entries |\n| Cited but missing from bib | **0** |\n| In bib but never cited | **0** |\n\n**Status: PASS** — perfect 1:1 match between citations and bib entries.\n\n### 1.2 Bib Entry Completeness\n\nAll 28 entries have title, author, year, and venue (booktitle/journal). Issues:\n\n| Entry | Issue | Severity |\n|-------|-------|----------|\n| `xu2025cruxevalx` | Author field: \"Ruiyang Xu and others\" (truncated) | Minor |\n| `spiess2025calibration` | Author field: \"Claudio Spiess and David Gros and others\" (truncated) | Minor |\n| `foster2025mutation` | Author field: \"Christopher Foster and others\" (truncated) | Minor |\n| `appt2024` | Missing pages field (TSE journal) | Minor |\n| `zhou2024llm4patch` | Missing pages field (TSE journal) | Minor |\n| `eguchi2025etcot` | Missing URL (workshop paper, no preprint link) | Minor |\n| `widyasari2024fusefl` | Missing URL/DOI/pages | Minor |\n| `yadavally2024ndslicer` | Missing URL/DOI/pages | Minor |\n\n### 1.3 Bib Key Naming Issues (non-functional)\n\n- `ferrando2025execute`: First author is Armengol-Estape, not Ferrando. Key is misleading but does not affect compilation.\n- `qwen2025coder`: Entry has `year={2024}` but key says \"2025\". ArXiv paper is from Sept 2024. No functional impact.\n\n---\n\n## 2. Data Consistency\n\n### 2.1 VOTA_no_ae Accuracy: 99.41% vs Registry 99.40%\n\nThe task flags that the registry value is 99.40% (from 99.405% raw). The paper consistently uses **99.41%** in all locations:\n- Table 1 (experiments.tex): 99.41%§\n- Table 2 (experiments.tex): 99.41%\n- Text (experiments.tex line 93): \"VOTA_no_ae = VOTA = 99.41%\"\n- Table full_qwen (appendix.tex): 99.41\n\n**Assessment**: 99.405 → 99.41% is correct under round-half-up convention. If the registry uses round-half-even (banker's rounding), 99.405 → 99.40%. **Recommend verifying the raw value and picking one convention consistently.** Paper is internally consistent at 99.41%.\n\n### 2.2 Decimal Place Consistency\n\nAll tables use 2-decimal format consistently. However, the **abstract** and **conclusion** use 1-decimal \"85.6%\" for loop_only, while Table 2 reports \"85.63%\".\n\n| Location | Value |\n|----------|-------|\n| Abstract | \"85.6%\" |\n| Introduction (line 26) | \"85.6%\" |\n| Conclusion (line 17) | \"85.6%\" |\n| Table 2 (tab:ablation) | \"85.63%\" |\n\n**Severity**: Low. Rounding in prose summaries is acceptable but introduces minor inconsistency.\n\n### 2.3 All Other Numbers\n\nCross-checked all repeated values (99.83%, 99.33%, 91.09%, 84.45%, 14.96pp, 81.76%, 75.13%, 6.64pp, 93.61%, etc.) — all consistent across locations.\n\n---\n\n## 3. Cross-Reference Audit\n\n### 3.1 Label/Ref Match\n\n| Check | Count |\n|-------|-------|\n| Labels defined | 33 |\n| All \\ref{} targets have matching \\label{} | **Yes** |\n| Dangling refs (ref without label) | **0** |\n\n### 3.2 Orphaned Labels (defined but never referenced)\n\n| Label | Location | Notes |\n|-------|----------|-------|\n| `sec:vota_examples` | appendix.tex:103 | Never \\ref'd from any file |\n| `sec:full_results` | appendix.tex:161 | Never \\ref'd from any file |\n\n**Severity**: Low. Appendix sections don't strictly need cross-references, but adding a pointer from the main text (e.g., \"Full per-seed results in Appendix~\\ref{sec:full_results}\") would improve navigability.\n\n### 3.3 Table/Figure Numbering\n\nLaTeX auto-numbers; sequence is correct:\n- Main text: Tables 1–3, Figures 1–2\n- Appendix: Tables 4–14, Figures 3–4\n\nNo gaps or duplicates.\n\n---\n\n## 4. ARR Compliance\n\n| Requirement | Status |\n|-------------|--------|\n| `[review]` mode (anonymous) | PASS — `\\usepackage[review]{acl}` |\n| Author anonymized | PASS — \"Anonymous ACL submission\" |\n| Limitations section | PASS — comprehensive, 6 limitations |\n| Ethics Statement | PASS — public data, no human subjects, minimal compute |\n| No de-anonymization leaks | PASS — no GitHub URLs, author names, lab names, or affiliations |\n| ARR checklist (arr_checklist.tex) | PASS — all sections A–F complete |\n| Code/data release language | PASS — \"upon acceptance\" phrasing |\n\n---\n\n## 5. Format Issues\n\n### 5.1 Table Caption Placement (CRITICAL)\n\n**ACL style requires table captions ABOVE the table body.**\n\n| File | Tables | Caption Position | Correct? |\n|------|--------|-----------------|----------|\n| experiments.tex | Tables 1, 2, 3 | **Below** (`\\caption` after `\\end{tabular}`) | NO |\n| appendix.tex | Tables 4–14 | Above (`\\caption` before `\\begin{tabular}`) | YES |\n\n**Fix required**: Move `\\caption{...}\\label{...}` to before `\\begin{tabular}` in experiments.tex for all three tables.\n\n### 5.2 Figure Caption Placement\n\nAll figures have captions below — correct per convention. PASS.\n\n### 5.3 Condition Name Formatting Inconsistency\n\n| Condition | Canonical Form | Deviant Form | Location |\n|-----------|---------------|--------------|----------|\n| VOTA_no_ae | `\\texttt{VOTA\\_no\\_ae}` | `VOTA$-$AE` | appendix.tex per_class table (line 22) |\n| full_trace_label_only | `\\texttt{full\\_trace\\_label\\_only}` | `label\\_only` (no \\texttt{}) | experiments.tex Table 3 |\n| full_trace_label_only | `\\texttt{full\\_trace\\_label\\_only}` | `Full Trace (LO)` | appendix.tex per_class table (line 17) |\n\n### 5.4 Appendix Label Format\n\nAll appendix labels use consistent `sec:snake_case` / `tab:snake_case` / `fig:snake_case` format. PASS.\n\n---\n\n## 6. Critical Issues (Must Fix)\n\n1. **Table caption placement in experiments.tex** — Tables 1–3 have captions below the table body. ACL requires captions above. Move `\\caption` + `\\label` before `\\begin{tabular}` for each.\n\n## 7. Recommended Fixes (Should Fix)\n\n2. **VOTA_no_ae naming in per_class table** — Change \"VOTA$-$AE\" to `\\texttt{VOTA\\_no\\_ae}` for consistency (appendix.tex line 22).\n3. **label_only naming in Table 3** — Add `\\texttt{}` around `label\\_only` in experiments.tex Table 3.\n4. **\"Full Trace (LO)\" in per_class table** — Standardize to `\\texttt{full\\_trace\\_label\\_only}` or at minimum `\\texttt{label\\_only}` (appendix.tex line 17).\n5. **85.6% vs 85.63%** — Either use 85.63% everywhere, or add \"(rounded)\" qualification in abstract/conclusion.\n\n## 8. Optional Improvements\n\n6. Add cross-references to orphaned appendix sections (`sec:vota_examples`, `sec:full_results`).\n7. Complete truncated author lists in bib entries (xu2025cruxevalx, spiess2025calibration, foster2025mutation).\n8. Add pages field to journal entries (appt2024, zhou2024llm4patch).\n9. Add URL/DOI to widyasari2024fusefl and yadavally2024ndslicer.\n10. Verify VOTA_no_ae raw value rounding convention (99.405 → 99.41% or 99.40%).\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference-audit_20260516T045759",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/reference_audit_report.md",
    "content": "# Paper Audit Report: trace-verdict-study\n\n**Date**: 2026-05-16  \n**Scope**: Citation integrity, data consistency, cross-references, ARR compliance, formatting\n\n---\n\n## 1. Citation Audit\n\n### 1.1 Cross-Check Results\n\n| Check | Result |\n|-------|--------|\n| Cited keys in .tex files | 28 unique keys |\n| Bib entries in references.bib | 28 entries |\n| Cited but missing from bib | **0** |\n| In bib but never cited | **0** |\n\n**Status: PASS** — perfect 1:1 match between citations and bib entries.\n\n### 1.2 Bib Entry Completeness\n\nAll 28 entries have title, author, year, and venue (booktitle/journal). Issues:\n\n| Entry | Issue | Severity |\n|-------|-------|----------|\n| `xu2025cruxevalx` | Author field: \"Ruiyang Xu and others\" (truncated) | Minor |\n| `spiess2025calibration` | Author field: \"Claudio Spiess and David Gros and others\" (truncated) | Minor |\n| `foster2025mutation` | Author field: \"Christopher Foster and others\" (truncated) | Minor |\n| `appt2024` | Missing pages field (TSE journal) | Minor |\n| `zhou2024llm4patch` | Missing pages field (TSE journal) | Minor |\n| `eguchi2025etcot` | Missing URL (workshop paper, no preprint link) | Minor |\n| `widyasari2024fusefl` | Missing URL/DOI/pages | Minor |\n| `yadavally2024ndslicer` | Missing URL/DOI/pages | Minor |\n\n### 1.3 Bib Key Naming Issues (non-functional)\n\n- `ferrando2025execute`: First author is Armengol-Estape, not Ferrando. Key is misleading but does not affect compilation.\n- `qwen2025coder`: Entry has `year={2024}` but key says \"2025\". ArXiv paper is from Sept 2024. No functional impact.\n\n---\n\n## 2. Data Consistency\n\n### 2.1 VOTA_no_ae Accuracy: 99.41% vs Registry 99.40%\n\nThe task flags that the registry value is 99.40% (from 99.405% raw). The paper consistently uses **99.41%** in all locations:\n- Table 1 (experiments.tex): 99.41%§\n- Table 2 (experiments.tex): 99.41%\n- Text (experiments.tex line 93): \"VOTA_no_ae = VOTA = 99.41%\"\n- Table full_qwen (appendix.tex): 99.41\n\n**Assessment**: 99.405 → 99.41% is correct under round-half-up convention. If the registry uses round-half-even (banker's rounding), 99.405 → 99.40%. **Recommend verifying the raw value and picking one convention consistently.** Paper is internally consistent at 99.41%.\n\n### 2.2 Decimal Place Consistency\n\nAll tables use 2-decimal format consistently. However, the **abstract** and **conclusion** use 1-decimal \"85.6%\" for loop_only, while Table 2 reports \"85.63%\".\n\n| Location | Value |\n|----------|-------|\n| Abstract | \"85.6%\" |\n| Introduction (line 26) | \"85.6%\" |\n| Conclusion (line 17) | \"85.6%\" |\n| Table 2 (tab:ablation) | \"85.63%\" |\n\n**Severity**: Low. Rounding in prose summaries is acceptable but introduces minor inconsistency.\n\n### 2.3 All Other Numbers\n\nCross-checked all repeated values (99.83%, 99.33%, 91.09%, 84.45%, 14.96pp, 81.76%, 75.13%, 6.64pp, 93.61%, etc.) — all consistent across locations.\n\n---\n\n## 3. Cross-Reference Audit\n\n### 3.1 Label/Ref Match\n\n| Check | Count |\n|-------|-------|\n| Labels defined | 33 |\n| All \\ref{} targets have matching \\label{} | **Yes** |\n| Dangling refs (ref without label) | **0** |\n\n### 3.2 Orphaned Labels (defined but never referenced)\n\n| Label | Location | Notes |\n|-------|----------|-------|\n| `sec:vota_examples` | appendix.tex:103 | Never \\ref'd from any file |\n| `sec:full_results` | appendix.tex:161 | Never \\ref'd from any file |\n\n**Severity**: Low. Appendix sections don't strictly need cross-references, but adding a pointer from the main text (e.g., \"Full per-seed results in Appendix~\\ref{sec:full_results}\") would improve navigability.\n\n### 3.3 Table/Figure Numbering\n\nLaTeX auto-numbers; sequence is correct:\n- Main text: Tables 1–3, Figures 1–2\n- Appendix: Tables 4–14, Figures 3–4\n\nNo gaps or duplicates.\n\n---\n\n## 4. ARR Compliance\n\n| Requirement | Status |\n|-------------|--------|\n| `[review]` mode (anonymous) | PASS — `\\usepackage[review]{acl}` |\n| Author anonymized | PASS — \"Anonymous ACL submission\" |\n| Limitations section | PASS — comprehensive, 6 limitations |\n| Ethics Statement | PASS — public data, no human subjects, minimal compute |\n| No de-anonymization leaks | PASS — no GitHub URLs, author names, lab names, or affiliations |\n| ARR checklist (arr_checklist.tex) | PASS — all sections A–F complete |\n| Code/data release language | PASS — \"upon acceptance\" phrasing |\n\n---\n\n## 5. Format Issues\n\n### 5.1 Table Caption Placement (CRITICAL)\n\n**ACL style requires table captions ABOVE the table body.**\n\n| File | Tables | Caption Position | Correct? |\n|------|--------|-----------------|----------|\n| experiments.tex | Tables 1, 2, 3 | **Below** (`\\caption` after `\\end{tabular}`) | NO |\n| appendix.tex | Tables 4–14 | Above (`\\caption` before `\\begin{tabular}`) | YES |\n\n**Fix required**: Move `\\caption{...}\\label{...}` to before `\\begin{tabular}` in experiments.tex for all three tables.\n\n### 5.2 Figure Caption Placement\n\nAll figures have captions below — correct per convention. PASS.\n\n### 5.3 Condition Name Formatting Inconsistency\n\n| Condition | Canonical Form | Deviant Form | Location |\n|-----------|---------------|--------------|----------|\n| VOTA_no_ae | `\\texttt{VOTA\\_no\\_ae}` | `VOTA$-$AE` | appendix.tex per_class table (line 22) |\n| full_trace_label_only | `\\texttt{full\\_trace\\_label\\_only}` | `label\\_only` (no \\texttt{}) | experiments.tex Table 3 |\n| full_trace_label_only | `\\texttt{full\\_trace\\_label\\_only}` | `Full Trace (LO)` | appendix.tex per_class table (line 17) |\n\n### 5.4 Appendix Label Format\n\nAll appendix labels use consistent `sec:snake_case` / `tab:snake_case` / `fig:snake_case` format. PASS.\n\n---\n\n## 6. Critical Issues (Must Fix)\n\n1. **Table caption placement in experiments.tex** — Tables 1–3 have captions below the table body. ACL requires captions above. Move `\\caption` + `\\label` before `\\begin{tabular}` for each.\n\n## 7. Recommended Fixes (Should Fix)\n\n2. **VOTA_no_ae naming in per_class table** — Change \"VOTA$-$AE\" to `\\texttt{VOTA\\_no\\_ae}` for consistency (appendix.tex line 22).\n3. **label_only naming in Table 3** — Add `\\texttt{}` around `label\\_only` in experiments.tex Table 3.\n4. **\"Full Trace (LO)\" in per_class table** — Standardize to `\\texttt{full\\_trace\\_label\\_only}` or at minimum `\\texttt{label\\_only}` (appendix.tex line 17).\n5. **85.6% vs 85.63%** — Either use 85.63% everywhere, or add \"(rounded)\" qualification in abstract/conclusion.\n\n## 8. Optional Improvements\n\n6. Add cross-references to orphaned appendix sections (`sec:vota_examples`, `sec:full_results`).\n7. Complete truncated author lists in bib entries (xu2025cruxevalx, spiess2025calibration, foster2025mutation).\n8. Add pages field to journal entries (appt2024, zhou2024llm4patch).\n9. Add URL/DOI to widyasari2024fusefl and yadavally2024ndslicer.\n10. Verify VOTA_no_ae raw value rounding convention (99.405 → 99.41% or 99.40%).\n"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-16T05:02:38.573328+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/reference_audit_report.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference-audit_20260516T045759",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-16T05:02:38.573496+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "reference_audit_report",
  "type": "report",
  "description": "论文引用审计+完整性检查报告：引用交叉验证、数据一致性、交叉引用、ARR合规、格式规范",
  "project": "trace-verdict-study",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/reference_audit_report.md",
  "tags": "['paper', 'audit', 'citation', 'ARR']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference-audit_20260516T045759",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "reference_audit_report",
    "type": "report",
    "description": "论文引用审计+完整性检查报告：引用交叉验证、数据一致性、交叉引用、ARR合规、格式规范",
    "project": "trace-verdict-study",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/reference_audit_report.md",
    "tags": "['paper', 'audit', 'citation', 'ARR']"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-16T05:02:38.573655+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260516_afa09d\", \"name\": \"reference_audit_report\", \"type\": \"report\", \"description\": \"论文引用审计+完整性检查报告：引用交叉验证、数据一致性、交叉引用、ARR合规、格式规范\", \"path\": \"projects/trace-verdict-study/artifacts/_project/report/reference_audit_report_afa09d.md\", \"url\": null, \"project\": \"trace-verdict-study\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-16T05:02:25.327646+00:00\", \"tags\": [\"paper\", \"audit\", \"citation\", \"ARR\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference-audit_20260516T045759",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 37 · 2026-05-16T05:02:38.573829+00:00_

审计完成。核心结论：

**引用完整性**: 28 个 cite key 与 bib 完全 1:1 匹配，无遗漏无冗余。

**Critical 问题 (1个)**: experiments.tex 的 Tables 1–3 caption 放在表格下方，ACL 要求在上方。需要把 `\caption`+`\label` 移到 `\begin{tabular}` 之前。

**Should Fix (4个)**:
- per_class 表中 "VOTA$-$AE" 应改为 `\texttt{VOTA\_no\_ae}`
- Table 3 中 `label\_only` 缺 `\texttt{}`
- per_class 表中 "Full Trace (LO)" 命名不统一
- Abstract/conclusion 中 "85.6%" 与 Table 2 的 "85.63%" 不一致

**ARR 合规**: 全部通过（匿名、limitations、ethics、checklist 完整、无去匿名化泄露）。

**数据一致性**: VOTA_no_ae 99.41% 全文一致；需确认 registry 99.40% 的 rounding convention 差异是否需要对齐。

完整报告已写入 `artifacts/reference_audit_report.md`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_reference-audit_20260516T045759"
}
```

</details>

---
