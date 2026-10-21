# audit citation verify w1

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 137
- **Recorded user turns:** 0
- **Tool calls:** 68
- **Original source:** `logs/chats/worker_audit_citation-verify-w1_20260526T101523.jsonl`
- **Structured JSON:** [`bd40cfd27b142259fd8b.json`](../../sessions/bd/bd40cfd27b142259fd8b.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

137 recorded events

### Tool call

_source line 1 · 2026-05-26T10:22:48.762971+00:00_

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
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-26T10:22:48.763520+00:00_

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
…[truncated 21639 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-26T10:22:48.763754+00:00_

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
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-26T10:22:48.763937+00:00_

1	\documentclass[11pt]{article}
2	
3	% Change "review" to "final" to generate the final (camera-ready) version.
4	\usepackage[review]{acl}
5	
6	\usepackage{times}
7	\usepackage{latexsym}
8	\usepackage[T1]{fontenc}
9	\usepackage[utf8]{inputenc}
10	\usepackage{microtype}
11	\usepackage{inconsolata}
12	\usepackage{graphicx}
13	\graphicspath{{../../figures/paper/}}
14	
15	\usepackage{booktabs}
16	\usepackage{enumitem}
17	\usepackage{multirow}
18	\usepackage{algorithm}
19	\usepackage{algorithmic}
20	
21	\newcommand{\cond}[1]{\textit{#1}}
22	
23	\pdfinfo{/CreationDate () /ModDate ()}
24	
25	\title{Trace Verbosity Degrades SFT Verdict Prediction:\\ A Case Study in Information Density Effects}
26	\author{Anonymous ACL submission}
27	
28	\begin{document}
29	\maketitle
30	
31	\begin{abstract}
32	A natural assumption when augmenting code models with execution traces is that richer runtime information yields better predictions.
33	We challenge this for verdict prediction (classifying whether a test passes or fails) and find the opposite: complete traces degrade accuracy to near-baseline levels, while compact exception events alone reach ${\geq}$99.33\% across all models tested.
34	Through the first systematic component ablation of trace representations across multiple code models and architecture families, we identify information density as the key factor: exception events encode the fault signal in roughly 150 tokens, whereas full traces dilute it across thousands of routine steps, trapping models in unstable oscillation.
35	Controlled experiments support this finding: gradient masking isolates backward-pass dilution as a minor factor, a tail-truncation sweep reveals a sharp phase transition at the diagnostic-event boundary, and format-marker removal confirms the signal is semantic.
36	These results decompose trace verbosity into a two-tier diagnostic hierarchy and establish that targeted signal extraction strictly dominates richer input for structurally constrained tasks such
…[truncated 1290 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-26T10:22:48.764109+00:00_

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
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-26T10:22:48.764386+00:00_

1	\section{Introduction}
2	
3	Execution traces record a program's complete runtime behavior: every function call, variable assignment, and control flow decision.
4	Recent work has incorporated them into code language models for tasks from bug localization to program repair \citep{chen2025tracepile,ding2024traced,wang2025dcsh,ni2024next}, under the working assumption that richer runtime information yields better predictions.
5	\emph{We find the opposite.}
6	For verdict prediction (classifying whether a test passes or fails), feeding a model the complete execution trace produces accuracies of 79--82\%, barely above a source-code-only baseline (72--76\%), while a single compact component of the same trace reaches ${\geq}$99.33\% across all models tested.
7	Verbose traces do not just fail to help; they actively impair learning.
8	
9	Verdict prediction offers a clean testbed for isolating this effect.
10	As binary classification, it separates signal extraction from generation noise; as fault detection, the model need only detect failure, not simulate execution.
11	If the fault signal concentrates in a small trace subset, information density should matter more than quantity.
12	Prior work found no single trace representation consistently outperforms others \citep{wang2025dcsh}, but focused on generation tasks where this density hypothesis could not be cleanly tested.
13	
14	We conduct the first systematic component ablation of trace representations, decomposing Verdict-Optimized Trace Abstraction (VOTA; exception events + assertion comparisons + loop compression) into individual components across four models spanning 1.5B to 13B parameters and three architecture families \citep{qwen2025coder,roziere2024code,deepseek2024coder}, on 591 problems from HumanEval \citep{chen2021evaluating} and MBPP-sanitized \citep{austin2021program}.
15	The results are unambiguous: exception events (a median of 150 tokens encoding error type, stack frame, and message) reach ${\geq}$99.33\% acc
…[truncated 2597 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-26T10:22:48.764542+00:00_

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
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-26T10:22:48.764732+00:00_

1	\section{Experiments}
2	
3	We evaluate two questions:
4	(1)~Do exception signals generalize across model architectures and scales?
5	(2)~What is the relative contribution of each trace component?
6	All experiments use $N{=}1{,}190$ test samples with Wilson 95\% CIs.\footnote{Problem-level split (472/119 problems, zero crossover). Deduplication sensitivity analysis confirms 0.00pp delta across all 19 conditions (Appendix~\ref{sec:dedup_stats}).}
7	All cross-tier differences are significant at $p{<}.0001$ (paired bootstrap, $B{=}10{,}000$) unless noted.
8	Under problem-level clustered bootstrap (effective $N{\approx}119$), cross-tier gaps remain significant ($p{<}.001$); within-tier comparisons show partially overlapping CIs.
9	
10	\subsection{Cross-Model Comparison}
11	\label{sec:cross_model}
12	
13	Table~\ref{tab:cross_model} compares four models spanning three architecture families across a 1.5B--13B parameter range.
14	
15	\paragraph{Exception dominance across families.}
16	Under \cond{exception\_only}, all four models converge to ${\geq}$99.33\% across all seeds, with a cross-model range of just 0.50pp, the tightest of any condition.
17	CodeLlama-13B reaches 100\% on one seed; the two persistent errors on Qwen (both \textit{GeneratorExit}; Appendix~\ref{sec:irreducible}) are convergence artifacts rather than hard data limitations.
18	
19	\paragraph{Scale invariance.}
20	Exception accuracy is independent of model scale: the smallest model (1.5B) matches the largest (13B) on the same representation (Table~\ref{tab:cross_model}).
21	In contrast, \cond{no\_trace} scales monotonically with capacity and exhibits the highest seed variance of any condition.
22	Exception events eliminate both the scale gap and the instability.
23	
24	\paragraph{VOTA robustness.}
25	Excluding one training failure caused by tokenizer-induced truncation (Appendix~\ref{sec:tokenizer_analysis}), VOTA achieves ${\geq}$98.57\% across all models within a 0.80pp range.
26	The failure is itself i
…[truncated 8149 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-26T10:22:48.764887+00:00_

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
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/discussion.tex"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-26T10:22:48.765066+00:00_

1	\section{Discussion}
2	
3	\begin{figure}[t]
4	\centering
5	\includegraphics[width=\columnwidth]{fig2_calibration}
6	\caption{Reliability diagrams for four trace conditions on Qwen-2.5-7B ($N{=}1{,}190$). \cond{exception\_only} (ECE=0.003) clusters near the diagonal; \cond{no\_trace} (ECE=0.171) shows systematic overconfidence.}
7	\label{fig:calibration}
8	\end{figure}
9	
10	The central finding is that information density governs learning efficiency for trace-based verdict prediction.
11	Exception events concentrate the fault signal in a compact format (median 150 tokens), while non-exception components record \emph{how} the program ran, not \emph{whether} it failed.
12	This explains three patterns: (1)~adding information beyond exceptions provides no benefit (indeed, VOTA underperforms \cond{exception\_only}, Table~\ref{tab:ablation}); (2)~the tail-truncation phase transition at ${\sim}$500 tokens coincides with the diagnostic-event boundary (Figure~\ref{fig:trace_length}); and (3)~the SFT advantage over regex concentrates on caught-exception boundary cases (\S\ref{sec:nomarker}).
13	The narrow cross-model gap (Table~\ref{tab:cross_model}) supports density, not capacity, as the binding constraint.
14	
15	\paragraph{SFT vs.\ regex: semantic understanding.}
16	Format-marker removal drops accuracy by only ${\sim}$2pp, leaving a clear gap over the best regex.
17	On boundary samples with caught exceptions, SFT correctly classifies 6/8 vs.\ 0/8 for regex ($p{=}.041$). This confirms the signal is semantic rather than syntactic.
18	This distinction matters for deployment: regex baselines can detect most exceptions through surface-level pattern matching, but fail precisely on the ambiguous cases (caught exceptions within \textit{try/except} blocks) where correct classification requires understanding the exception's role in program control flow.
19	SFT learns this distinction from fewer than 5{,}000 training examples, suggesting that the relevant semantic features are readi
…[truncated 7261 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-26T10:22:48.765241+00:00_

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
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-26T10:22:48.765421+00:00_

1	\section{Related Work}
2	
3	\subsection{Execution Traces for Code LLMs}
4	
5	Recent work has scaled trace-augmented training: TracePile \citep{chen2025tracepile} pre-trained on 2.6M execution-annotated samples, while \citet{liu2023codeexecution} pre-trained models to predict execution outputs from traces.
6	\citet{wang2025dcsh} found trace utility to be task- and format-dependent but did not decompose individual trace components; relative to their work, we contribute a two-tier signal hierarchy, a phase transition in trace-length budgets, calibration analysis, and cross-architecture validation.
7	NExT \citep{ni2024next} and ET-CoT \citep{eguchi2025etcot} used trace chain-of-thought for execution reasoning, and \citet{ferrando2025execute} found compact traces comparable to full traces, consistent with our density finding.
8	CRUXEval \citep{gu2024cruxeval}, extended to 19 languages by CRUXEval-X \citep{xu2025cruxevalx}, established execution reasoning benchmarks, though neither decomposes which trace components contribute to \emph{classification} accuracy.
9	\citet{shi2023distracted} showed LLMs are easily distracted by irrelevant context, providing a complementary explanation for why verbose traces impair SFT learning.
10	In the prompt compression literature, LLMLingua \citep{jiang2023llmlingua} and Selective Context \citep{li2023selectivecontext} showed that pruning low-information tokens preserves downstream accuracy; TraceCoder \citep{huang2026tracecoder} and InspectCoder \citep{wang2025inspectcoder} apply selective trace extraction for automated debugging; and \citet{haque2025traces} found raw traces provide limited repair benefit.
11	Our density decomposition complements these methods by quantifying \emph{why} compression helps (gradient dilution explains ${\sim}$24\% of the gap; the remainder reflects inference-time interference).
12	
13	\subsection{Verdict Prediction and Fault Detection}
14	
15	Verdict prediction is an instance of the longstanding test oracl
…[truncated 4335 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-26T10:22:48.765576+00:00_

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
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-26T10:22:48.765741+00:00_

1	\section{Method}
2	
3	\subsection{Task Definition}
4	
5	We study \emph{verdict prediction}: given a Python function, a test input, and an optional execution trace, predict whether the test passes or fails.
6	The model produces a single token (\textit{pass} or \textit{fail}), making this a binary classification task.
7	Unlike code generation \citep{chen2025tracepile} or output prediction \citep{gu2024cruxeval}, verdict prediction isolates the model's ability to detect faults from its ability to simulate execution.
8	The discrete binary outcome makes the effect of each trace component directly measurable, providing cleaner ablation contrasts than generation tasks where output quality varies continuously.
9	
10	\subsection{Dataset}
11	\label{sec:dataset}
12	
13	We sampled 10 candidate solutions per problem from Qwen-2.5-Coder-7B-Instruct (temperature 0.8, top\_p 0.95) for 591 problems from HumanEval \citep{chen2021evaluating} (164) and MBPP-sanitized \citep{austin2021program} (427), executed each against canonical tests with \textit{sys.settrace} to obtain line-level traces and pass/fail verdicts, yielding 5,910 pairs (67\% pass, 33\% fail).
14	The dataset is split 80/20 by problem ID into 4,720 training and 1,190 test samples (majority baseline: 71.51\%).
15	The \cond{exception\_only} format collapses passing solutions into identical rows (39.45\% train, 48.99\% test duplicates); these duplicates arise from multiple candidate solutions per problem, with the train--test split enforced at the problem level (472 train / 119 test problems, zero crossover; Appendix~\ref{sec:dedup_stats}).
16	
17	\subsection{Trace Representations}
18	
19	We define seven conditions that vary the trace information available:
20	\begin{itemize}[nosep,leftmargin=1em]
21	\item \cond{no\_trace}: source code and test input only.
22	\item \cond{full\_trace}: complete line-by-line trace with variable states.
23	\item \cond{VOTA}: exception events + assertion-point comparisons + loop compression (A
…[truncated 3043 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-26T10:22:48.765890+00:00_

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
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-26T10:22:48.766090+00:00_

1	\section{Conclusion}
2	
3	We presented the first systematic component ablation of trace representations for verdict prediction, covering four code models across three architecture families.
4	The finding is clear: information density, not trace completeness, determines learning efficiency under SFT.
5	Compact exception events converge to ${\geq}$99.33\% across all models, while verbose full traces oscillate without stable convergence.
6	These results establish a two-tier diagnostic hierarchy: Tier~1 signals (exceptions, assertion comparisons) generalize across architectures within a 0.50--1.11pp range, while Tier~2 signals (loop patterns) are model-dependent. For structurally constrained tasks such as verdict prediction, targeted signal extraction should replace wholesale trace inclusion.
7	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-26T10:22:48.766332+00:00_

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
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/appendix.tex"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-26T10:22:48.766864+00:00_

1	\section{Per-Class Performance Breakdown}
2	\label{sec:per_class}
3	
4	Table~\ref{tab:per_class} reports per-class precision, recall, and F1 for all experimental conditions.
5	
6	\begin{table*}[t]
7	\centering
8	\caption{Per-class precision, recall, and F1 for all experimental conditions (seed 42). DeepSeek VOTA seed 42 is a training failure (84.45\%, fail recall = 45.4\%) due to tokenizer-driven truncation; seeds 123/456 achieve 99.16\%/99.33\%.}
9	\label{tab:per_class}
10	\small
11	\begin{tabular}{llccccccc}
12	\toprule
13	\textbf{Condition} & \textbf{Model} & \textbf{Acc} & \textbf{Pass P} & \textbf{Pass R} & \textbf{Pass F1} & \textbf{Fail P} & \textbf{Fail R} & \textbf{Fail F1} \\
14	\midrule
15	No Trace          & Qwen-2.5-7B & 75.13 & 87.76 & 75.79 & 81.34 & 54.73 & 73.45 & 62.72 \\
16	Full Trace        & Qwen-2.5-7B & 81.76 & 87.74 & 86.60 & 87.17 & 67.43 & 69.62 & 68.51 \\
17	Full Trace (LO)   & Qwen-2.5-7B & 85.94 & 88.21 & 93.18 & 90.63 & 80.07 & 68.73 & 73.97 \\
18	VOTA              & Qwen-2.5-7B & 99.05 & 100.00 & 99.18 & 99.59 & 97.98 & 100.00 & 98.98 \\
19	Exception Only    & Qwen-2.5-7B & 99.83 & 100.00 & 99.76 & 99.88 & 99.41 & 100.00 & 99.71 \\
20	AE Only           & Qwen-2.5-7B & 99.92 & 100.00 & 99.88 & 99.94 & 99.71 & 100.00 & 99.85 \\
21	Loop Only         & Qwen-2.5-7B & 86.05 & 92.39 & 87.07 & 89.66 & 71.65 & 82.01 & 76.48 \\
22	VOTA\_no\_ae       & Qwen-2.5-7B & 99.41 & 99.88 & 99.29 & 99.59 & 98.26 & 99.71 & 98.98 \\
23	\midrule
24	No Trace          & DeepSeek-6.7B & 73.36 & 81.71 & 80.85 & 81.28 & 53.16 & 54.57 & 53.86 \\
25	Full Trace        & DeepSeek-6.7B & 79.16 & 85.70 & 85.10 & 85.40 & 63.20 & 64.30 & 63.70 \\
26	VOTA              & DeepSeek-6.7B & 84.45 & 82.14 & 100.00 & 90.20 & 100.00 & 45.40 & 62.50 \\
27	Exception Only    & DeepSeek-6.7B & 99.33 & 100.00 & 99.06 & 99.53 & 97.69 & 100.00 & 98.83 \\
28	AE Only           & DeepSeek-6.7B & 98.74 & 98.40 & 99.90 & 99.10 & 99.70 & 95.90 & 97.70 \\
29	\bottomrule
30	\end{tabular}
31	\
…[truncated 50662 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-26T10:22:48.767088+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-26T10:22:48.767395+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-26T10:22:48.767651+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Chain of Execution Supervision Promotes General Reasoning in Large Language Models\" Nuo Chen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Chain of Execution Supervision Promotes General Reasoning in Large Language Models\" Nuo Chen"
  }
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-26T10:22:48.767788+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"TRACED: Execution-aware Pre-training for Source Code\" Yangruibo Ding ICSE"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"TRACED: Execution-aware Pre-training for Source Code\" Yangruibo Ding ICSE"
  }
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-26T10:22:48.767908+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Evaluating Large Language Models Trained on Code\" Chen Mark arXiv 2107.03374"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Evaluating Large Language Models Trained on Code\" Chen Mark arXiv 2107.03374"
  }
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-26T10:22:48.768024+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Program Synthesis with Large Language Models\" Austin Jacob arXiv 2108.07732"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Program Synthesis with Large Language Models\" Austin Jacob arXiv 2108.07732"
  }
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-26T10:22:48.768135+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"CRUXEval: A Benchmark for Code Reasoning, Understanding and Execution\" Alex Gu ICML 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"CRUXEval: A Benchmark for Code Reasoning, Understanding and Execution\" Alex Gu ICML 2024"
  }
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-26T10:22:48.768272+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"LoRA: Low-Rank Adaptation of Large Language Models\" Edward Hu ICLR 2022"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"LoRA: Low-Rank Adaptation of Large Language Models\" Edward Hu ICLR 2022"
  }
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-26T10:22:48.768395+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Qwen2.5-Coder Technical Report\" arXiv 2409.12186"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Qwen2.5-Coder Technical Report\" arXiv 2409.12186"
  }
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-26T10:22:48.768507+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"DeepSeek-Coder: When the Large Language Model Meets Programming\" arXiv 2401.14196"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"DeepSeek-Coder: When the Large Language Model Meets Programming\" arXiv 2401.14196"
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-26T10:22:48.768649+00:00_

Web search results for query: ""Evaluating Large Language Models Trained on Code" Chen Mark arXiv 2107.03374"

Links: [{"title":"[2107.03374] Evaluating Large Language Models Trained on Code","url":"https://arxiv.org/abs/2107.03374"},{"title":"Evaluating Large Language Models Trained on Code","url":"https://arxiv.org/pdf/2107.03374"},{"title":"(PDF) Evaluating Large Language Models Trained on Code","url":"https://www.researchgate.net/publication/353066484_Evaluating_Large_Language_Models_Trained_on_Code"},{"title":"Paper page - Evaluating Large Language Models Trained on Code","url":"https://huggingface.co/papers/2107.03374"},{"title":"[2107.03374] Evaluating Large Language Models Trained on Code","url":"https://arxiv-export3.library.cornell.edu/abs/2107.03374"},{"title":"Evaluating Large Language Models Trained on Code. | BibSonomy","url":"https://www.bibsonomy.org/bibtex/1612004c4b9c4bdd58c95b8e5127b9f9f"},{"title":"Notes on \"Evaluating Large Language Models Trained on Code\"","url":"https://www.andrelizardo.com/p/notes-on-evaluating-large-language"},{"title":"[2107.03374v2] Evaluating Large Language Models Trained on Code","url":"https://arxiv.org/abs/2107.03374v2"},{"title":"Evaluating Large Language Models Trained on Code - ADS","url":"https://ui.adsabs.harvard.edu/abs/2021arXiv210703374C/abstract"}]

I found the paper you're looking for. Here's a summary of the key information:

This paper introduces Codex, a GPT language model fine-tuned on publicly available code from GitHub, and studies its Python code-writing capabilities. A distinct production version of Codex powers GitHub Copilot.

**Key Results:**

On HumanEval, a new evaluation set released to measure functional correctness for synthesizing programs from docstrings, the model solves 28.8% of the problems, while GPT-3 solves 0% and GPT-J solves 11.4%. Further gains can be realized by generating 100 samples per problem and selecting the sample with the highest mean log-probability (44.5% solved) or by 
…[truncated 450 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-26T10:22:48.768823+00:00_

Web search results for query: ""TRACED: Execution-aware Pre-training for Source Code" Yangruibo Ding ICSE"

Links: [{"title":"TRACED: Execution-aware Pre-training for Source Code Yangruibo Ding","url":"https://arxiv.org/pdf/2306.07487"},{"title":"[2306.07487] TRACED: Execution-aware Pre-training for Source Code","url":"https://arxiv.org/abs/2306.07487"},{"title":"TRACED: Execution-aware Pre-training for Source Code | Proceedings of the IEEE/ACM 46th International Conference on Software Engineering","url":"https://dl.acm.org/doi/10.1145/3597503.3608140"},{"title":"TRACED: Execution-aware Pre-training for Source Code | Request PDF","url":"https://www.researchgate.net/publication/378027102_TRACED_Execution-aware_Pre-training_for_Source_Code"},{"title":"TRACED: Execution-aware Pre-training for Source Code","url":"https://figshare.com/articles/dataset/TRACED_Execution-aware_Pre-training_for_Source_Code/27367989"},{"title":"TRACED: Execution-aware Pre-training for Source Code - Benjamin Steenhoek","url":"https://benjijang.com/publication/2024-04-14-traced"},{"title":"Kexin Pei","url":"https://sites.google.com/site/kexinpeisite/"}]

I found the paper! Here's the information about "TRACED: Execution-aware Pre-training for Source Code":

## Summary

TRACED is an execution-aware pre-training strategy presented at ICSE 2024 in April 2024 in Lisbon, Portugal by Yangruibo Ding, Ben Steenhoek, Kexin Pei, Gail Kaiser, Wei Le, and Baishakhi Ray.

## Key Concept

Most existing pre-trained language models for source code focus on learning static code text, but program semantics are not fully exposed before real execution. Without understanding program execution, statically pre-trained models fail to capture dynamic code properties like branch coverage and runtime variable values, making them less effective at tasks like retrieving semantic clones and detecting software vulnerabilities.

## Approach

TRACED pre-trains code language models with a combination of source code, executable 
…[truncated 363 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-26T10:22:48.769001+00:00_

Web search results for query: ""Chain of Execution Supervision Promotes General Reasoning in Large Language Models" Nuo Chen"

Links: [{"title":"[2510.23629] Chain of Execution Supervision Promotes General Reasoning in Large Language Models","url":"https://arxiv.org/abs/2510.23629"},{"title":"Chain of Execution Supervision Promotes General Reasoning in Large Language Models","url":"https://arxiv.org/html/2510.23629"},{"title":"Chain of Execution Supervision Promotes General Reasoning in Large Language Models | OpenReview","url":"https://openreview.net/forum?id=QjnKsujXVG"},{"title":"NeurIPS Poster Chain of Execution Supervision Promotes General Reasoning in Large Language Models","url":"https://neurips.cc/virtual/2025/loc/san-diego/poster/118108"},{"title":"Chain of Execution Supervision Promotes General ...","url":"https://arxiv.org/pdf/2510.23629"},{"title":"Chain of Execution Supervision Promotes General Reasoning in ...","url":"https://openreview.net/pdf?id=QjnKsujXVG"},{"title":"ControlMath: Controllable Data Generation Promotes Math Generalist Models | Request PDF","url":"https://www.researchgate.net/publication/386184446_ControlMath_Controllable_Data_Generation_Promotes_Math_Generalist_Models"},{"title":"Towards Reasoning Era: A Survey of Long Chain-of-Thought for Reasoning Large Language Models","url":"https://arxiv.org/html/2503.09567v4"},{"title":"[2507.17168] Improving LLMs' Generalized Reasoning Abilities by Graph Problems","url":"https://arxiv.org/abs/2507.17168"}]

I found the paper! Here are the key details about "Chain of Execution Supervision Promotes General Reasoning in Large Language Models" by Nuo Chen and colleagues:

## Overview
The paper addresses building robust and general reasoning ability in large language models, authored by Nuo Chen, Zehua Li, Keqin Bao, Junyang Lin, and Dayiheng Liu from the Qwen Team at Alibaba and other institutions.

## Main Contribution
The authors introduce TracePile, a large-scale corpus of 2.6 million samples th
…[truncated 896 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-26T10:22:48.769161+00:00_

Web search results for query: ""Qwen2.5-Coder Technical Report" arXiv 2409.12186"

Links: [{"title":"[2409.12186] Qwen2.5-Coder Technical Report","url":"https://arxiv.org/abs/2409.12186"},{"title":"Qwen2.5-Coder Technical Report","url":"https://arxiv.org/html/2409.12186v1"},{"title":"Qwen2.5-Coder Technical Report","url":"https://www.emergentmind.com/papers/2409.12186"},{"title":"[2409.12186] Qwen2.5-Coder Technical Report - ar5iv - arXiv","url":"https://ar5iv.labs.arxiv.org/html/2409.12186"},{"title":"[2409.12186v3] Qwen2.5-Coder Technical Report","url":"https://arxiv.org/abs/2409.12186v3"},{"title":"[2409.12186v1] Qwen2.5-Coder Technical Report","url":"https://arxiv.org/abs/2409.12186v1"},{"title":"Qwen2.5-Coder Technical Report","url":"https://www.summarizepaper.com/en/arxiv-id/2409.12186v1/"},{"title":"Paper page - Qwen2.5-Coder Technical Report","url":"https://huggingface.co/papers/2409.12186"}]

I found the Qwen2.5-Coder Technical Report. Here's what the search results show:

The Qwen2.5-Coder series is a significant upgrade from CodeQwen1.5 and includes six models: Qwen2.5-Coder-(0.5B/1.5B/3B/7B/14B/32B).

As a code-specific model, Qwen2.5-Coder is built upon the Qwen2.5 architecture and continues pretrained on a vast corpus of over 5.5 trillion tokens. Through meticulous data cleaning, scalable synthetic data generation, and balanced data mixing, Qwen2.5-Coder demonstrates impressive code generation capabilities while retaining general and math skills.

These models have been evaluated on a wide range of code-related tasks, achieving state-of-the-art performance across more than 10 benchmarks, including code generation, completion, reasoning, and repair, consistently outperforming larger models of the same model size.

The paper was submitted on September 18, 2024, with the latest version (v3) revised on November 12, 2024. You can access it directly on arXiv at https://arxiv.org/abs/2409.12186.


REMINDER: You MUST include the sources above in your response 
…[truncated 38 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-26T10:22:48.769363+00:00_

Web search results for query: ""DeepSeek-Coder: When the Large Language Model Meets Programming" arXiv 2401.14196"

Links: [{"title":"[2401.14196] DeepSeek-Coder: When the Large Language Model Meets Programming -- The Rise of Code Intelligence","url":"https://arxiv.org/abs/2401.14196"},{"title":"[PDF] DeepSeek-Coder: When the Large Language Model Meets Programming - The Rise of Code Intelligence | Semantic Scholar","url":"https://www.semanticscholar.org/paper/DeepSeek-Coder:-When-the-Large-Language-Model-Meets-Guo-Zhu/1f2a20a6efaf83214861dddae4a38a83ae18fe32"},{"title":"DeepSeek-Coder: When the Large Language Model Meets Programming -- The Rise of Code Intelligence - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240114196G/abstract"},{"title":"DeepSeek-Coder: When the Large Language Model Meets ...","url":"https://arxiv.org/pdf/2401.14196"},{"title":"Paper page - DeepSeek-Coder: When the Large Language Model Meets Programming -- The Rise of Code Intelligence","url":"https://huggingface.co/papers/2401.14196"},{"title":"[2401.14196v2] DeepSeek-Coder: When the Large Language Model Meets Programming -- The Rise of Code Intelligence","url":"https://arxiv.org/abs/2401.14196v2"},{"title":"DeepSeek-Coder: When the Large Language Model Meets Programming - The Rise of Code Intelligence","url":"https://arxiv.org/html/2401.14196v1"},{"title":"GitHub - deepseek-ai/DeepSeek-Coder: DeepSeek Coder: Let the Code Write Itself · GitHub","url":"https://github.com/deepseek-ai/DeepSeek-Coder"}]

I found the paper you're looking for. Here's what I found:

**Paper Details:**
The DeepSeek-Coder series is a range of open-source code models with sizes from 1.3B to 33B, trained from scratch on 2 trillion tokens. These models are pre-trained on a high-quality project-level code corpus and employ a fill-in-the-blank task with a 16K window to enhance code generation and infilling.

**Performance:**
DeepSeek-Coder achieves state-of-the-art performance among open-source code models across 
…[truncated 542 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-26T10:22:48.769533+00:00_

Web search results for query: ""Program Synthesis with Large Language Models" Austin Jacob arXiv 2108.07732"

Links: [{"title":"[2108.07732] Program Synthesis with Large Language Models","url":"https://arxiv.org/abs/2108.07732"},{"title":"Program Synthesis with Large Language Models Jacob Austin* Augustus Odena*","url":"https://arxiv.org/pdf/2108.07732"},{"title":"[2108.07732v1] Program Synthesis with Large Language Models","url":"https://arxiv.org/abs/2108.07732v1"},{"title":"Paper page - Program Synthesis with Large Language Models","url":"https://huggingface.co/papers/2108.07732"},{"title":"Program Synthesis with Large Language Models","url":"https://www.researchgate.net/publication/353970323_Program_Synthesis_with_Large_Language_Models"},{"title":"Program Synthesis with Large Language Models","url":"https://www.summarizepaper.com/en/arxiv-id/2108.07732v1/"},{"title":"[PDF] Program Synthesis with Large Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Program-Synthesis-with-Large-Language-Models-Austin-Odena/a38e0f993e4805ba8a9beae4c275c91ffcec01df"},{"title":"Program Synthesis with Large Language Models - ADS","url":"https://ui.adsabs.harvard.edu/abs/2021arXiv210807732A/abstract"},{"title":"Google Scholar","url":"https://scholar.google.com/scholar?q=Jacob+Austin%2C+Augustus+Odena%2C+Maxwell+Nye%2C+Maarten+Bosma%2C+Henryk+Michalewski%2C+David+Dohan%2C+Ellen+Jiang%2C+Carrie+Cai%2C+Michael+Terry%2C+Quoc+Le%2C+et+al.+2021.+Program+synthesis+with+large+language+models.+arXiv+preprint+arXiv%3A2108.07732+%282021%29."},{"title":"dblp: Program Synthesis with Large Language Models.","url":"https://dblp.org/rec/journals/corr/abs-2108-07732.html"}]

I found the paper you're looking for. Here's what I found:

"Program Synthesis with Large Language Models" (arXiv:2108.07732) explores the limits of the current generation of large language models for program synthesis in general purpose programming languages, authored by Jacob Austin, Augustus Ode
…[truncated 966 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-26T10:22:48.769702+00:00_

Web search results for query: ""CRUXEval: A Benchmark for Code Reasoning, Understanding and Execution" Alex Gu ICML 2024"

Links: [{"title":"[2401.03065] CRUXEval: A Benchmark for Code Reasoning, Understanding and Execution","url":"https://arxiv.org/abs/2401.03065"},{"title":"CRUXEval: A Benchmark for Code Reasoning, Understanding and Execution","url":"https://proceedings.mlr.press/v235/gu24c.html"},{"title":"CRUXEval: A Benchmark for Code Reasoning, Understanding and Execution | ML Anthology","url":"https://mlanthology.org/icml/2024/gu2024icml-cruxeval/"},{"title":"CRUXEval: a benchmark for code reasoning ...","url":"https://dl.acm.org/doi/10.5555/3692070.3692729"},{"title":"CRUXEval: A Benchmark for Code Reasoning, Understanding and Execution","url":"https://bibbase.org/network/publication/gu-rozire-leather-solarlezama-synnaeve-wang-cruxevalabenchmarkforcodereasoningunderstandingandexecution-2024"},{"title":"CRUXEval: A Benchmark for Code Reasoning, Understanding and Execution | OpenReview","url":"https://openreview.net/forum?id=Ffpg52swvg"},{"title":"CRUXEval: Code Reasoning, Understanding, and Execution Evaluation","url":"https://crux-eval.github.io/"},{"title":"ICLR CRUXEval: A Benchmark for Code Reasoning, Understanding and Execution","url":"https://iclr.cc/virtual/2024/22440"}]

I found comprehensive information about the CRUXEval paper. Here's what I discovered:

## Overview

CRUXEval (Code Reasoning, Understanding, and eXecution Evaluation) is a benchmark consisting of 800 Python functions (3-13 lines), with each function coming with an input-output pair, leading to two natural tasks: input prediction and output prediction.

## Key Contributions

The authors propose a general recipe for generating their execution benchmark by sampling from a model, which can be used for more challenging versions of the benchmark if needed.

They evaluated twenty code models on the benchmark and discovered that many recent high-scoring models on HumanEval show no improvement
…[truncated 724 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-26T10:22:48.769881+00:00_

Web search results for query: ""LoRA: Low-Rank Adaptation of Large Language Models" Edward Hu ICLR 2022"

Links: [{"title":"ICLR Poster LoRA: Low-Rank Adaptation of Large Language Models","url":"https://iclr.cc/virtual/2022/poster/6319"},{"title":"LoRA: Low-Rank Adaptation of Large Language Models | OpenReview","url":"https://openreview.net/forum?id=nZeVKeeFYf9"},{"title":"[2106.09685] LoRA: Low-Rank Adaptation of Large Language Models","url":"https://arxiv.org/abs/2106.09685"},{"title":"LoRA: Low-Rank Adaptation of Large Language Models - Microsoft Research","url":"https://www.microsoft.com/en-us/research/publication/lora-low-rank-adaptation-of-large-language-models/"},{"title":"LORA: LOW-RANK ADAPTATION OF LARGE LAN","url":"https://openreview.net/pdf?id=nZeVKeeFYf9"},{"title":"LoRA: Low-Rank Adaptation of Large Language Models. | BibSonomy","url":"https://www.bibsonomy.org/bibtex/146d3736cb2ce0472e8e0d8f9859fb2a2"},{"title":"LoRA: Low-Rank Adaptation of Large Language Models | Request PDF","url":"https://www.researchgate.net/publication/352504883_LoRA_Low-Rank_Adaptation_of_Large_Language_Models"},{"title":"[PDF] LoRA: Low-Rank Adaptation of Large Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/LoRA:-Low-Rank-Adaptation-of-Large-Language-Models-Hu-Shen/a8ca46b171467ceb2d7652fbfb67fe701ad86092"},{"title":"LoRA: Low-Rank Adaptation of Large Language Models | by Abdullah Şamil Güser | Medium","url":"https://medium.com/@abdullahsamilguser/lora-low-rank-adaptation-of-large-language-models-7af929391fee"},{"title":"Google Scholar","url":"https://scholar.google.com/scholar_lookup?title=LoRA:+Low-rank+adaptation+of+large+language+models&publication_year=2022"}]

I found the paper you're looking for. Here's what the search results show:

"LoRA: Low-Rank Adaptation of Large Language Models" was published as a conference paper at ICLR 2022, authored by Edward Hu, Yelong Shen, Phillip Wallis, Zeyuan Allen-Zhu, Yuanzhi Li, Shean Wang, Lu Wang, a
…[truncated 1175 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-26T10:22:48.770071+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Do Code Semantics Help\" \"Comprehensive Study on Execution Trace\" Jian Wang EMNLP 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Do Code Semantics Help\" \"Comprehensive Study on Execution Trace\" Jian Wang EMNLP 2025"
  }
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-26T10:22:48.770199+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"NExT: Teaching Large Language Models to Reason about Code Execution\" Ansong Ni ICML 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"NExT: Teaching Large Language Models to Reason about Code Execution\" Ansong Ni ICML 2024"
  }
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-26T10:22:48.770345+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Making LLMs Program Interpreters via Execution Trace Chain of Thought\" Koshi Eguchi Takuya Akiba"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Making LLMs Program Interpreters via Execution Trace Chain of Thought\" Koshi Eguchi Takuya Akiba"
  }
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-26T10:22:48.770512+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"What I Cannot Execute, I Do Not Understand\" \"Training and Evaluating LLMs on Program Execution Traces\" arXiv 2503.05703"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"What I Cannot Execute, I Do Not Understand\" \"Training and Evaluating LLMs on Program Execution Traces\" arXiv 2503.05703"
  }
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-26T10:22:48.770639+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"CRUXEval-X: A Benchmark for Multilingual Code Reasoning\" Ruiyang Xu arXiv 2408.13001"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"CRUXEval-X: A Benchmark for Multilingual Code Reasoning\" Ruiyang Xu arXiv 2408.13001"
  }
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-26T10:22:48.770753+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"APPT: Boosting Automated Patch Correctness Prediction\" Quanjun Zhang IEEE TSE 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"APPT: Boosting Automated Patch Correctness Prediction\" Quanjun Zhang IEEE TSE 2024"
  }
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-26T10:22:48.770862+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Leveraging Large Language Model for Automatic Patch Correctness Assessment\" Xin Zhou IEEE TSE 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Leveraging Large Language Model for Automatic Patch Correctness Assessment\" Xin Zhou IEEE TSE 2024"
  }
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-26T10:22:48.770971+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Calibration and Correctness of Language Models for Code\" Claudio Spiess ICSE 2025 arXiv 2402.02047"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Calibration and Correctness of Language Models for Code\" Claudio Spiess ICSE 2025 arXiv 2402.02047"
  }
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-26T10:22:48.771115+00:00_

Web search results for query: ""Making LLMs Program Interpreters via Execution Trace Chain of Thought" Koshi Eguchi Takuya Akiba"

Links: [{"title":"Making LLMs Program Interpreters via Execution Trace Chain of Thought | OpenReview","url":"https://openreview.net/forum?id=pFyBdPyOCQ"},{"title":"Making LLMs Program Interpreters via Execution Trace Chain of Thought","url":"https://openreview.net/pdf?id=pFyBdPyOCQ"},{"title":"Takuya Akiba | OpenReview","url":"https://openreview.net/profile?id=~Takuya_Akiba2"},{"title":"DroPE: Extending the Context of Pretrained LLMs by Dropping their Positional Embeddings","url":"https://pub.sakana.ai/DroPE/"},{"title":"[2503.05703] What I cannot execute, I do not understand: Training and Evaluating LLMs on Program Execution Traces","url":"https://arxiv.org/abs/2503.05703"},{"title":"What I cannot execute, I do not understand: Training and Evaluating LLMs on Program Execution Traces","url":"https://arxiv.org/html/2503.05703v1"},{"title":"[2512.12167] Extending the Context of Pretrained LLMs by Dropping Their Positional Embeddings","url":"https://arxiv.org/abs/2512.12167"},{"title":"Responsible Agentic Reasoning and AI Agents: A Critical ...","url":"https://d197for5662m48.cloudfront.net/documents/publicationstatus/289766/preprint_pdf/f48077a80a72b5d411ccf1d683590cb9.pdf"},{"title":"[2403.13187] Evolutionary Optimization of Model Merging Recipes","url":"https://arxiv.org/abs/2403.13187"}]

Based on the search results, I found the paper you're looking for:

"Making LLMs Program Interpreters via Execution Trace Chain of Thought" is by Koshi Eguchi and Takuya Akiba.

The paper proposes ET-CoT (Execution Trace Chain of Thought), an approach where LLMs learn to generate a detailed and systematic program execution trace as a chain of thought to predict program outcomes. The authors developed a new Python interpreter called PyTracify, which outputs these traces during execution, and then generated a large number of traces and fine-tuned an LLM u
…[truncated 453 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-26T10:22:48.771396+00:00_

Web search results for query: ""Do Code Semantics Help" "Comprehensive Study on Execution Trace" Jian Wang EMNLP 2025"

Links: [{"title":"Do Code Semantics Help? A Comprehensive Study on Execution Trace-Based Information for Code Large Language Models - ACL Anthology","url":"https://aclanthology.org/2025.findings-emnlp.548/"},{"title":"[2509.11686] Do Code Semantics Help? A Comprehensive Study on Execution Trace-Based Information for Code Large Language Models","url":"https://arxiv.org/abs/2509.11686"},{"title":"[2509.11686v3] Do Code Semantics Help? A Comprehensive Study on Execution Trace-Based Information for Code Large Language Models","url":"https://arxiv.org/abs/2509.11686v3"},{"title":"Do Code Semantics Help? A Comprehensive Study on ...","url":"https://aclanthology.org/2025.findings-emnlp.548.pdf"},{"title":"Do Code Semantics Help? A Comprehensive Study on Execution","url":"https://arxiv.org/pdf/2509.11686"},{"title":"Do Code Semantics Help? A Comprehensive Study on Execution Trace-Based Information for Code Large Language Models","url":"https://arxiv.org/html/2509.11686v1"}]

I found the paper you were searching for! Here are the key details:

**Title:** Do Code Semantics Help? A Comprehensive Study on Execution Trace-Based Information for Code Large Language Models

**Authors:** Jian Jornbowrl Wang, Xiaofei Xie, Qiang Hu, Shangqing Liu, and Yi Li

**Publication:** Findings of the Association for Computational Linguistics: EMNLP 2025, pages 10367–10385, Suzhou, China

**Overview:** The paper addresses critical limitations in Code LLMs' ability to reason about runtime behavior and understand the actual functionality of programs, which poses significant challenges for their post-training and practical deployment.

**Key Finding:** The experimental results surprisingly disagree with previous works and demonstrate that semantic information has limited usefulness for SFT and test time scaling of Code LLM.

The paper is available on both the ACL Anthology and arX
…[truncated 131 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-26T10:22:48.771612+00:00_

Web search results for query: ""What I Cannot Execute, I Do Not Understand" "Training and Evaluating LLMs on Program Execution Traces" arXiv 2503.05703"

Links: [{"title":"[2503.05703] What I cannot execute, I do not understand: Training and Evaluating LLMs on Program Execution Traces","url":"https://arxiv.org/abs/2503.05703"},{"title":"What I cannot execute, I do not understand: Training and Evaluating LLMs on Program Execution Traces","url":"https://arxiv.org/html/2503.05703v1"},{"title":"LLMs versus the Halting Problem: Revisiting Program Termination Prediction","url":"https://arxiv.org/html/2601.18987v3"},{"title":"What I cannot execute, I do not understand: Training and Evaluating LLMs   on Program Execution Traces","url":"https://arxiv.org/pdf/2503.05703"},{"title":"Do Code Semantics Help? A Comprehensive Study on Execution Trace-Based Information for Code Large Language Models","url":"https://arxiv.org/pdf/2509.11686"}]

I found the paper you're looking for! Here are the key details:

**Paper Title:** "What I Cannot Execute, I Do Not Understand: Training and Evaluating LLMs on Program Execution Traces"

**arXiv ID:** 2503.05703 (Posted February 10, 2025)

**Authors:** Jordi Armengol-Estapé from University of Edinburgh and researchers from Meta AI including Quentin Carbonneaux, Tianjun Zhang, Aram H. Markosyan, and others

**Key Contributions:**

The paper studies Execution Tuning (E.T.), a training procedure in which researchers explicitly model real-world program execution traces without requiring manual test annotations.

**Main Results:** The researchers train and evaluate models on different execution trace granularities (line and instruction-level) and strategies on the task of output prediction, obtaining around 80% accuracy on CruxEval and MBPP, and showing the advantages of dynamic scratchpads on long executions (up to 14k steps).

**Core Problem Addressed:** Most code datasets typically treat code as static strings and rarely exploit the dynamic info
…[truncated 202 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-26T10:22:48.771804+00:00_

Web search results for query: ""CRUXEval-X: A Benchmark for Multilingual Code Reasoning" Ruiyang Xu arXiv 2408.13001"

Links: [{"title":"CRUXEVAL-X: A Benchmark for Multilingual Code Reasoning, Understanding and Execution - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.1158/"},{"title":"[2408.13001] CRUXEval-X: A Benchmark for Multilingual Code Reasoning, Understanding and Execution","url":"https://arxiv.org/abs/2408.13001"},{"title":"(PDF) CRUXEval-X: A Benchmark for Multilingual Code Reasoning, Understanding and Execution","url":"https://www.researchgate.net/publication/383413276_CRUXEval-X_A_Benchmark_for_Multilingual_Code_Reasoning_Understanding_and_Execution"},{"title":"CRUXEVAL-X: A Benchmark for Multilingual Code","url":"https://www.arxiv.org/pdf/2408.13001"},{"title":"Paper page - CRUXEval-X: A Benchmark for Multilingual Code Reasoning, Understanding and Execution","url":"https://huggingface.co/papers/2408.13001"},{"title":"CruxEval-X: A Benchmark for Multilingual Code Reasoning, Understanding and Execution","url":"https://arxiv.org/html/2408.13001v1"},{"title":"[PDF] CRUXEval-X: A Benchmark for Multilingual Code Reasoning, Understanding and Execution | Semantic Scholar","url":"https://www.semanticscholar.org/paper/CRUXEval-X:-A-Benchmark-for-Multilingual-Code-and-Xu-Cao/88d48041a76ddc4318c360cdda0a4e1379eeefb3"},{"title":"xhwl/cruxeval-x · Datasets at Hugging Face","url":"https://huggingface.co/datasets/xhwl/cruxeval-x"},{"title":"CRUXEVAL-X: A Benchmark for Multilingual Code ...","url":"https://aclanthology.org/2025.acl-long.1158.pdf"}]

Based on the search results, here's information about the paper you requested:

## CRUXEval-X: A Benchmark for Multilingual Code Reasoning

CRUXEval-X is a benchmark for multilingual code reasoning, understanding and execution by Xu et al., presented at ACL 2025, with authors including Ruiyang Xu, Jialun Cao, Yaojie Lu, Ming Wen, Hongyu Lin, Xianpei Han, Ben He, Shing-Chi Cheung, and Le Sun.

**Purpose and M
…[truncated 1524 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-26T10:22:48.771992+00:00_

Web search results for query: ""Leveraging Large Language Model for Automatic Patch Correctness Assessment" Xin Zhou IEEE TSE 2024"

Links: [{"title":"Leveraging Large Language Model for Automatic Patch Correctness Assessment | IEEE Transactions on Software Engineering","url":"https://dl.acm.org/doi/abs/10.1109/TSE.2024.3452252"},{"title":"Leveraging Large Language Model for Automatic Patch Correctness Assessment | Request PDF","url":"https://www.researchgate.net/publication/383591189_Leveraging_Large_Language_Model_for_Automatic_Patch_Correctness_Assessment"},{"title":"Leveraging Large Language Model for Automatic Patch Correctness Assessment. | BibSonomy","url":"https://www.bibsonomy.org/bibtex/121733ba2498fa6c09e6b5ba222ae64ff"},{"title":"Leveraging Large Language Model for Automatic Patch Correctness Assessment | IEEE Journals & Magazine | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/10659742/"},{"title":"Leveraging Large Language Model for Automatic Patch Correctness Assessment : Find an Expert : The University of Melbourne","url":"https://findanexpert.unimelb.edu.au/scholarlywork/1930021-leveraging-large-language-model-for-automatic-patch-correctness-assessment?cache=1737797463612"},{"title":"Automatic Patch Correctness Assessment with Large Language Model","url":"https://arxiv.org/html/2303.00202v3"},{"title":"Invalidator: Automated Patch Correctness Assessment Via Semantic and Syntactic Reasoning | IEEE Transactions on Software Engineering","url":"https://dl.acm.org/doi/abs/10.1109/TSE.2023.3255177"},{"title":"[PDF] Invalidator: Automated Patch Correctness Assessment Via Semantic and Syntactic Reasoning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Invalidator:-Automated-Patch-Correctness-Assessment-Le-Cong-Luong/f6beeaf7ca72e4ef32a8a8110d4c7e30b18b0231"},{"title":"GitHub - iSEngLab/AwesomeLLM4SE: [SCIS 2025] A Survey on Large Language Models for Software Engineering · GitHub","url":"https://github.com/iSEngLab/AwesomeLLM4SE"}]
…[truncated 1224 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-26T10:22:48.772158+00:00_

Web search results for query: ""NExT: Teaching Large Language Models to Reason about Code Execution" Ansong Ni ICML 2024"

Links: [{"title":"[2404.14662] NExT: Teaching Large Language Models to Reason about Code Execution","url":"https://arxiv.org/abs/2404.14662"},{"title":"[PDF] NExT: Teaching Large Language Models to Reason about Code Execution | Semantic Scholar","url":"https://www.semanticscholar.org/paper/NExT:-Teaching-Large-Language-Models-to-Reason-Code-Ni-Allamanis/49306aa1fde2a21fadc77dbc8ec7e487fac72c5b"},{"title":"NExT: Teaching Large Language Models to Reason about Code Execution","url":"https://proceedings.mlr.press/v235/ni24a.html"},{"title":"NExT: Teaching Large Language Models to Reason about Code Execution | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/next-teaching-large-language-models-to-reason"},{"title":"[2404.14662v1] NExT: Teaching Large Language Models to Reason about Code Execution","url":"https://arxiv.org/abs/2404.14662v1"},{"title":"NExT: Teaching Large Language Models to Reason about Code Execution | OpenReview","url":"https://openreview.net/forum?id=B1W712hMBi"},{"title":"teaching large language models to reason about code execution","url":"https://dl.acm.org/doi/10.5555/3692070.3693610"}]

I found the paper you're looking for! Here are the key details:

**Paper:** NExT: Teaching Large Language Models to Reason about Code Execution by Ansong Ni, Miltiadis Allamanis, Arman Cohan, Yinlin Deng, Kensen Shi, Charles Sutton, and Pengcheng Yin

**Venue:** Published in the Proceedings of the 41st International Conference on Machine Learning (ICML 2024)

**Main Contribution:** NExT is a method to teach LLMs to inspect the execution traces of programs (variable states of executed lines) and reason about their run-time behavior through chain-of-thought (CoT) rationales

**Key Problem Addressed:** Large language models (LLMs) of code are typically trained on the surface textual form of programs, thus may lack a semantic
…[truncated 451 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-26T10:22:48.772395+00:00_

Web search results for query: ""Calibration and Correctness of Language Models for Code" Claudio Spiess ICSE 2025 arXiv 2402.02047"

Links: [{"title":"Calibration and Correctness of Language Models for Code (ICSE 2025 - Research Track) - ICSE 2025","url":"https://conf.researchr.org/details/icse-2025/icse-2025-research-track/8/Calibration-and-Correctness-of-Language-Models-for-Code"},{"title":"Calibration and Correctness of Language Models for Code Claudio Spiess∗","url":"https://www.software-lab.org/publications/icse2025_calibration.pdf"},{"title":"Calibration and Correctness of Language Models for Code | Proceedings of the IEEE/ACM 47th International Conference on Software Engineering","url":"https://dl.acm.org/doi/10.1109/ICSE55347.2025.00040"},{"title":"[2402.02047] Calibration and Correctness of Language Models for Code","url":"https://arxiv.org/abs/2402.02047"},{"title":"Calibration and Correctness of Language Models for Code | Request PDF","url":"https://www.researchgate.net/publication/392966020_Calibration_and_Correctness_of_Language_Models_for_Code"},{"title":"Calibration and Correctness of Language Models for Code ICSE Artifact","url":"https://zenodo.org/records/14744842"},{"title":"[PDF] Calibration and Correctness of Language Models for Code | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Calibration-and-Correctness-of-Language-Models-for-Spiess-Gros/65b59f4ffae4f5b9e5d63fc1d11bf9ca7f7df34d"},{"title":"Calibration and Correctness of Language Models for Code ICSE Artifact","url":"https://explore.openaire.eu/search/result?pid=10.5281/zenodo.14744842"},{"title":"47th ICSE 2025: Ottawa, ON, Canada","url":"https://dblp.org/db/conf/icse/icse2025.html"},{"title":"Claudio Spiess","url":"https://claudio.ai/"}]

I found the paper you're looking for! Here's what I found:

## Paper Details

"Calibration and Correctness of Language Models for Code" is authored by Claudio Spiess, David Gros, Kunal Suresh Pai, Michael Pradel, Rafiqul Rabin, Amin Alipou
…[truncated 1167 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-26T10:22:48.772584+00:00_

Web search results for query: ""APPT: Boosting Automated Patch Correctness Prediction" Quanjun Zhang IEEE TSE 2024"

Links: [{"title":"[2301.12453] APPT: Boosting Automated Patch Correctness Prediction via Fine-tuning Pre-trained Models","url":"https://arxiv.org/abs/2301.12453"},{"title":"GitHub - iSEngLab/APPT: [TSE 2024] APPT: Boosting Automated Patch Correctness Prediction via Fine-tuning Pre-trained Models · GitHub","url":"https://github.com/iSEngLab/APPT"},{"title":"(PDF) Boosting Automated Patch Correctness Prediction via Pre-trained Language Model","url":"https://www.researchgate.net/publication/367558621_Boosting_Automated_Patch_Correctness_Prediction_via_Pre-trained_Language_Model"},{"title":"APPT: Boosting Automated Patch Correctness Prediction via Fine-Tuning Pre-Trained Models | IEEE Journals & Magazine | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/10402095/"},{"title":"dblp: Quanjun Zhang","url":"https://dblp.org/pid/231/4867.html"},{"title":"Actions · iSEngLab/APPT","url":"https://github.com/iSEngLab/APPT/actions"},{"title":"A Survey of Learning-based Automated Program Repair | ACM Transactions on Software Engineering and Methodology","url":"https://dl.acm.org/doi/10.1145/3631974?query=%22A+Survey+of+Learning-based+Automated+Program+Repair.%22+AND+33+2+1+2024"},{"title":"APPT Boosting Automated Patch Correctness Prediction via Fine-tuning Pre-trained Models","url":"https://www.scribd.com/document/874799956/APPT-Boosting-Automated-Patch-Correctness-Prediction-via-Fine-tuning-Pre-trained-Models"},{"title":"Contrastive Learning for Automated Patch Correctness ...","url":"https://arxiv.org/pdf/2602.07561"}]

Based on the search results, I found information about the paper "APPT: Boosting Automated Patch Correctness Prediction via Fine-tuning Pre-trained Models":

## Overview

APPT addresses automated program repair (APR), which aims to fix software bugs automatically without human debugging efforts. APR is challenged by a long-standing overfit
…[truncated 950 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-26T10:22:48.772781+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Mutation-Guided LLM-based Test Generation at Meta\" Christopher Foster FSE 2025 arXiv 2501.12862"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Mutation-Guided LLM-based Test Generation at Meta\" Christopher Foster FSE 2025 arXiv 2501.12862"
  }
}
```

</details>

---

### Tool call

_source line 54 · 2026-05-26T10:22:48.772911+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Demystifying Faulty Code: Step-by-Step Reasoning for Explainable Fault Localization\" Ratnadira Widyasari SANER 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Demystifying Faulty Code: Step-by-Step Reasoning for Explainable Fault Localization\" Ratnadira Widyasari SANER 2024"
  }
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-26T10:22:48.773032+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"TraceCoder: A Trace-Driven Multi-Agent Framework for Automated Debugging\" Jiangping Huang ICSE 2026 arXiv 2602.06875"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"TraceCoder: A Trace-Driven Multi-Agent Framework for Automated Debugging\" Jiangping Huang ICSE 2026 arXiv 2602.06875"
  }
}
```

</details>

---

### Tool call

_source line 56 · 2026-05-26T10:22:48.773150+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"InspectCoder: Dynamic Analysis-Enabled Self Repair\" Yunkun Wang arXiv 2510.18327"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"InspectCoder: Dynamic Analysis-Enabled Self Repair\" Yunkun Wang arXiv 2510.18327"
  }
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-26T10:22:48.773285+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Towards Effectively Leveraging Execution Traces for Program Repair\" Mirazul Haque arXiv 2505.04441"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Towards Effectively Leveraging Execution Traces for Program Repair\" Mirazul Haque arXiv 2505.04441"
  }
}
```

</details>

---

### Tool call

_source line 58 · 2026-05-26T10:22:48.773401+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Unveiling the Generalization Power of Fine-Tuned Large Language Models\" Haoran Yang NAACL 2024 arXiv 2403.09162"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Unveiling the Generalization Power of Fine-Tuned Large Language Models\" Haoran Yang NAACL 2024 arXiv 2403.09162"
  }
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-26T10:22:48.773513+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"DebugBench: Evaluating Debugging Capability of Large Language Models\" Runchu Tian ACL 2024 arXiv 2401.04621"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"DebugBench: Evaluating Debugging Capability of Large Language Models\" Runchu Tian ACL 2024 arXiv 2401.04621"
  }
}
```

</details>

---

### Tool call

_source line 60 · 2026-05-26T10:22:48.773627+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"On the Accuracy of Spectrum-based Fault Localization\" Rui Abreu 2007"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"On the Accuracy of Spectrum-based Fault Localization\" Rui Abreu 2007"
  }
}
```

</details>

---

### Tool result

_source line 61 · 2026-05-26T10:22:48.773768+00:00_

Web search results for query: ""Demystifying Faulty Code: Step-by-Step Reasoning for Explainable Fault Localization" Ratnadira Widyasari SANER 2024"

Links: [{"title":"Demystifying Faulty Code: Step-by-Step Reasoning for Explainable Fault Localization (SANER 2024 - Research Papers) - SANER 2024","url":"https://conf.researchr.org/details/saner-2024/saner-2024-papers/68/Demystifying-Faulty-Code-Step-by-Step-Reasoning-for-Explainable-Fault-Localization"},{"title":"Demystifying Faulty Code: Step-by-Step Reasoning for Explainable Fault Localization | Request PDF","url":"https://www.researchgate.net/publication/382317610_Demystifying_Faulty_Code_Step-by-Step_Reasoning_for_Explainable_Fault_Localization"},{"title":"[2403.10507] Demystifying Faulty Code with LLM: Step-by-Step Reasoning for Explainable Fault Localization","url":"https://arxiv.org/abs/2403.10507"},{"title":"Demystifying Faulty Code: Step-by-Step Reasoning for Explainable Fault Localization | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Demystifying-Faulty-Code:-Step-by-Step-Reasoning-Widyasari-Ang/3b60d1a39482d86a3507a1879919609767e58594"},{"title":"Demystifying Faulty Code: Step-by-Step Reasoning for Explainable Fault Localization - Singapore Management University","url":"https://smusg.elsevierpure.com/en/publications/demystifying-faulty-code-step-by-step-reasoning-for-explainable-f/"},{"title":"Demystifying Faulty Code with LLM: Step-by-Step Reasoning for Explainable Fault Localization","url":"https://arxiv.org/html/2403.10507v1"},{"title":"Demystifying Faulty Code with LLM: Step-by-Step Reasoning for Explainable Fault Localization - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240310507W/abstract"},{"title":"Demystifying Faulty Code with LLM: Explainable Fault Localization","url":"https://goatstack.ai/topics/demystifying-faulty-code-with-llm-explainable-fault-localization-vgshdv"}]

I found the paper you're looking for! Here are the key details:

**Paper Information:**
The paper
…[truncated 1323 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-26T10:22:48.773939+00:00_

Web search results for query: ""InspectCoder: Dynamic Analysis-Enabled Self Repair" Yunkun Wang arXiv 2510.18327"

Links: [{"title":"[2510.18327] InspectCoder: Dynamic Analysis-Enabled Self Repair through interactive LLM-Debugger Collaboration","url":"https://arxiv.org/abs/2510.18327"},{"title":"InspectCoder: Dynamic Analysis-Enabled Self Repair through Interactive LLM-Debugger Collaboration","url":"https://arxiv.org/html/2510.18327v1"},{"title":"InspectCoder: Dynamic Analysis-Enabled Self Repair through interactive LLM-Debugger Collaboration | alphaXiv","url":"https://www.alphaxiv.org/resources/2510.18327v1"},{"title":"InspectCoder: Dynamic Analysis-Enabled Self Repair through","url":"https://arxiv.org/pdf/2510.18327"},{"title":"Knowledge-Enhanced Program Repair for Data Science Code | Request PDF","url":"https://www.researchgate.net/publication/392960377_Knowledge-Enhanced_Program_Repair_for_Data_Science_Code"},{"title":"SemFix: Program repair via semantic analysis | Request PDF","url":"https://www.researchgate.net/publication/261166224_SemFix_Program_repair_via_semantic_analysis"},{"title":"InspectCoder: Agentic Code Repair","url":"https://www.emergentmind.com/topics/inspectcoder"},{"title":"Shuiguang DENG | Professor | PhD | Zhejiang University, Hangzhou | ZJU | College of Computer Science and Technology | Research profile","url":"https://www.researchgate.net/profile/Shuiguang-Deng"}]

I found the paper you're looking for! Here are the key details:

**Title:** InspectCoder: Dynamic Analysis-Enabled Self Repair through interactive LLM-Debugger Collaboration

**ArXiv ID:** 2510.18327

**Authors:** Yunkun Wang, Yue Zhang, Guochang Li, Chen Zhi, Binhua Li, Fei Huang, Yongbin Li, and Shuiguang Deng

**Main Contribution:** InspectCoder is the first agentic program repair system that empowers LLMs to actively conduct dynamic analysis via interactive debugger control.

**Key Innovation:** The dual-agent framework enables strategic breakpoint placement, targeted state in
…[truncated 577 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 63 · 2026-05-26T10:22:48.774116+00:00_

Web search results for query: ""Mutation-Guided LLM-based Test Generation at Meta" Christopher Foster FSE 2025 arXiv 2501.12862"

Links: [{"title":"Mutation-Guided LLM-based Test Generation at Meta (FSE 2025 - Industry Papers) - FSE 2025","url":"https://conf.researchr.org/details/fse-2025/fse-2025-industry-papers/16/Mutation-Guided-LLM-based-Test-Generation-at-Meta"},{"title":"Mutation-Guided LLM-based Test Generation at Meta | Proceedings of the 33rd ACM International Conference on the Foundations of Software Engineering","url":"https://dl.acm.org/doi/10.1145/3696630.3728544"},{"title":"Mutation-Guided LLM-based Test Generation at Meta Christopher Foster","url":"https://arxiv.org/pdf/2501.12862"},{"title":"[2501.12862] Mutation-Guided LLM-based Test Generation at Meta","url":"https://arxiv.org/abs/2501.12862"},{"title":"Mutation-Guided LLM-based Test Generation at Meta","url":"https://arxiv.org/html/2501.12862v1"},{"title":"Mutation-Guided LLM-based Test Generation at Meta - UCL Discovery","url":"https://discovery.ucl.ac.uk/id/eprint/10218052/"},{"title":"(PDF) Mutation-Guided LLM-based Test Generation at Meta","url":"https://www.researchgate.net/publication/388317879_Mutation-Guided_LLM-based_Test_Generation_at_Meta"}]

I found the paper! Here's what I found about "Mutation-Guided LLM-based Test Generation at Meta":

## Overview
The paper describes Meta's ACH (Automated Compliance Hardening) system for mutation-guided LLM-based test generation, authored by Christopher Foster, Abhishek Gulati, Mark Harman, Inna Harper, Ke Mao, Jillian Ritchey, Hervé Robert, and Shubho Sengupta.

## Key Details
ACH generates relatively few mutants (simulated faults) compared to traditional mutation testing, instead focusing on generating currently undetected faults that are specific to an issue of concern.

From these uncaught faults, ACH generates tests that can catch them, thereby 'killing' the mutants and hardening the platform against regressions, with privacy concerns used to i
…[truncated 767 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-26T10:22:48.774312+00:00_

Web search results for query: ""Unveiling the Generalization Power of Fine-Tuned Large Language Models" Haoran Yang NAACL 2024 arXiv 2403.09162"

Links: [{"title":"Unveiling the Generalization Power of Fine-Tuned Large Language Models - ACL Anthology","url":"https://aclanthology.org/2024.naacl-long.51/"},{"title":"[2403.09162] Unveiling the Generalization Power of Fine-Tuned Large Language Models","url":"https://arxiv.org/abs/2403.09162"},{"title":"Unveiling the Generalization Power of Fine-Tuned Large Language Models | Request PDF","url":"https://www.researchgate.net/publication/382633449_Unveiling_the_Generalization_Power_of_Fine-Tuned_Large_Language_Models"},{"title":"Unveiling the Generalization Power of Fine-Tuned Large Language Models","url":"https://gengo.sotaro.io/2024.naacl-long.51"},{"title":"Accepted Papers - NAACL-HLT 2024","url":"https://2024.naacl.org/program/accepted_papers/"},{"title":"[Quick Review] Unveiling the Generalization Power of Fine-Tuned Large Language Models","url":"https://liner.com/review/unveiling-generalization-power-finetuned-large-language-models"},{"title":"GitHub - LHRYANG/Generalization_of_FT-LLM: Implementation of NAACL 2024 paper Unveiling the Generalization Power of Fine-Tuned Large Language Models","url":"https://github.com/LHRYANG/Generalization_of_FT-LLM"},{"title":"Unveiling the Generalization Power of Fine-Tuned Large Language Models","url":"https://paperreading.club/page?id=215235"},{"title":"Paper page - Unveiling the Generalization Power of Fine-Tuned Large Language Models","url":"https://huggingface.co/papers/2403.09162"},{"title":"Unveiling the Generalization Power of Fine-Tuned Large Language Models&lt;!-- --> - &lt;!-- -->即時閱讀與關鍵洞見","url":"https://linnk.ai/tw/insight/natural-language-processing/unveiling-the-impact-of-fine-tuned-large-language-models-on-generalization-ability-iaYxNmYR/"}]

I found the paper you're looking for. Here's what I found:

"Unveiling the Generalization Power of Fine-Tuned Large Language Models" 
…[truncated 1270 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 65 · 2026-05-26T10:22:48.774513+00:00_

Web search results for query: ""DebugBench: Evaluating Debugging Capability of Large Language Models" Runchu Tian ACL 2024 arXiv 2401.04621"

Links: [{"title":"[2401.04621] DebugBench: Evaluating Debugging Capability of Large Language Models","url":"https://arxiv.org/abs/2401.04621"},{"title":"GitHub - thunlp/DebugBench: The repository for paper \"DebugBench: \"Evaluating Debugging Capability of Large Language Models\". · GitHub","url":"https://github.com/thunlp/DebugBench"},{"title":"DebugBench: Evaluating Debugging Capability of Large Language Models - ACL Anthology","url":"https://aclanthology.org/2024.findings-acl.247/"},{"title":"DebugBench: Evaluating Debugging Capability of Large Language Models | Request PDF","url":"https://www.researchgate.net/publication/384218799_DebugBench_Evaluating_Debugging_Capability_of_Large_Language_Models"},{"title":"DebugBench: Evaluating Debugging Capability of Large Language Models","url":"https://arxiv.org/pdf/2401.04621"},{"title":"DebugBench: Evaluating Debugging Capability of Large Language Models | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/debugbench-evaluating-debugging-capability-large-language-models"},{"title":"Paper page - DebugBench: Evaluating Debugging Capability of Large Language Models","url":"https://huggingface.co/papers/2401.04621"},{"title":"[PDF] DebugBench: Evaluating Debugging Capability of Large Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/DebugBench:-Evaluating-Debugging-Capability-of-Tian-Ye/bb39d2b273d4c75f8e489f1f66dec42a7e14c5fd"},{"title":"DebugBench: Evaluating Debugging Capability of Large ...","url":"https://aclanthology.org/2024.findings-acl.247.pdf"},{"title":"DebugBench: Evaluating Debugging Capability of Large Language Models - 专知论文","url":"https://www.zhuanzhiai.com/paper/fecfa7e2e47b3df5acb8eddc63aef315"}]

Here are the results for your search:

## Overview

DebugBench is a paper published in the Findings of the Association f
…[truncated 1162 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-26T10:22:48.774721+00:00_

Web search results for query: ""TraceCoder: A Trace-Driven Multi-Agent Framework for Automated Debugging" Jiangping Huang ICSE 2026 arXiv 2602.06875"

Links: [{"title":"[2602.06875] TraceCoder: A Trace-Driven Multi-Agent Framework for Automated Debugging of LLM-Generated Code","url":"https://arxiv.org/abs/2602.06875"},{"title":"TraceCoder: A Trace-Driven Multi-Agent Framework for Automated Debugging of LLM-Generated Code","url":"https://arxiv.org/html/2602.06875v1"},{"title":"TraceCoder: A Trace-Driven Multi-Agent Framework for Automated Debugging of LLM-Generated Code (ICSE 2026 - Research Track) - ICSE 2026","url":"https://conf.researchr.org/details/icse-2026/icse-2026-research-track/145/TraceCoder-A-Trace-Driven-Multi-Agent-Framework-for-Automated-Debugging-of-LLM-Gener"},{"title":"Trace-Based Diagnostics","url":"https://www.emergentmind.com/topics/trace-based-diagnostics"},{"title":"Agent Tracing for Debugging Multi-Agent AI Systems","url":"https://www.getmaxim.ai/articles/agent-tracing-for-debugging-multi-agent-ai-systems/"},{"title":"6 Best Debugging Tools for Multi-Agent Systems | Fastio","url":"https://fast.io/resources/best-debugging-tools-multi-agent-systems/"}]

Great! I found the paper you're looking for. Here's the information about TraceCoder:

## TraceCoder: A Trace-Driven Multi-Agent Framework for Automated Debugging

TraceCoder is a collaborative multi-agent framework that emulates the observe-analyze-repair process of human experts. The framework first instruments the code with diagnostic probes to capture fine-grained runtime traces, enabling deep insight into its internal execution.

**Purpose and Problem:**
Large Language Models (LLMs) often generate code with subtle but critical bugs, especially for complex tasks. Existing automated repair methods typically rely on superficial pass/fail signals, offering limited visibility into program behavior and hindering precise error localization.

**Key Components:**
Grounded in established cognitive mode
…[truncated 999 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 67 · 2026-05-26T10:22:48.774899+00:00_

Web search results for query: ""Towards Effectively Leveraging Execution Traces for Program Repair" Mirazul Haque arXiv 2505.04441"

Links: [{"title":"[2505.04441] Towards Effectively Leveraging Execution Traces for Program Repair with Code LLMs","url":"https://arxiv.org/abs/2505.04441"},{"title":"Towards Effectively Leveraging Execution Traces for Program Repair with Code LLMs","url":"https://arxiv.org/html/2505.04441v1"},{"title":"Towards Effectively Leveraging Execution Traces","url":"https://arxiv.org/pdf/2505.04441"},{"title":"Automated Cloud Infrastructure-as-Code Reconciliation with AI Agents","url":"https://arxiv.org/html/2510.20211v1"},{"title":"dblp: Mirazul Haque","url":"https://dblp.org/pid/272/0796.html"},{"title":"Debugging Code World Models","url":"https://arxiv.org/html/2602.07672v2"},{"title":"dblp: Search for \"author:Mirazul_Haque:\"","url":"https://dblp.org/search/pid/api?q=author:Mirazul_Haque:"},{"title":"A Survey of LLM-based Automated Program Repair: Taxonomies, Design Paradigms, and Applications","url":"https://arxiv.org/html/2506.23749v1"},{"title":"Bug Fixing with Broader Context: Enhancing LLM-Based Program Repair via Layered Knowledge Injection","url":"https://arxiv.org/html/2506.24015v1"},{"title":"Mirazul Haque - ACL Anthology","url":"https://aclanthology.org/people/mirazul-haque/"}]

I found the paper! Here are the details:

**Title:** "Towards Effectively Leveraging Execution Traces for Program Repair with Code LLMs"

**Authors:** Mirazul Haque, Petr Babkin, Farima Farmahinifarahani, and Manuela Veloso from J. P. Morgan AI Research

**ArXiv ID:** 2505.04441 (published May 7, 2025)

**Summary:**

Large Language Models (LLMs) show promising performance on various programming tasks, including Automatic Program Repair (APR). However, most approaches to LLM-based APR are limited to the static analysis of the programs, while disregarding their runtime behavior. 

The authors aim to remedy this potential blind spot by augmenting standard AP
…[truncated 600 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-26T10:22:48.775079+00:00_

Web search results for query: ""On the Accuracy of Spectrum-based Fault Localization" Rui Abreu 2007"

Links: [{"title":"On the Accuracy of Spectrum-based Fault Localization∗ Rui Abreu Peter Zoeteweij","url":"https://scispace.com/pdf/on-the-accuracy-of-spectrum-based-fault-localization-13lhdnxj1f.pdf"},{"title":"On the Accuracy of Spectrum-based Fault Localization","url":"https://www.researchgate.net/publication/4279298_On_the_Accuracy_of_Spectrum-based_Fault_Localization"},{"title":"[PDF] On the Accuracy of Spectrum-based Fault Localization | Semantic Scholar","url":"https://www.semanticscholar.org/paper/On-the-Accuracy-of-Spectrum-based-Fault-Abreu-Zoeteweij/eb956ab442810f783f44600ce6d714583a96a4aa"},{"title":"On the Accuracy of Spectrum-based Fault Localization | Proceedings of the Testing: Academic and Industrial Conference Practice and Research Techniques - MUTATION","url":"https://dl.acm.org/doi/10.5555/1308173.1308264"},{"title":"On the Accuracy of Spectrum-based Fault Localization | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/4344104/"},{"title":"Spectrum-Based Fault Localization for Diagnosing Concurrency Faults | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-642-41707-8_16"},{"title":"(PDF) A practical evaluation of spectrum-based fault localization","url":"https://www.academia.edu/30972916/A_practical_evaluation_of_spectrum_based_fault_localization"},{"title":"Enhancing spectrum based fault localization via emphasizing its formulas with importance weight | Proceedings of the Third International Workshop on Automated Program Repair","url":"https://dl.acm.org/doi/10.1145/3524459.3527349"},{"title":"Spectrum-Based Fault Localization in Model Transformations | ACM Transactions on Software Engineering and Methodology","url":"https://dl.acm.org/doi/10.1145/3241744"}]

I found the paper you're looking for. Here's what I can tell you about it:

"On the Accuracy of Spectrum-based Fault Local
…[truncated 904 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-26T10:22:48.775325+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Visualization of Test Information to Assist Fault Localization\" James Jones Mary Jean Harrold ICSE 2002"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Visualization of Test Information to Assist Fault Localization\" James Jones Mary Jean Harrold ICSE 2002"
  }
}
```

</details>

---

### Tool call

_source line 70 · 2026-05-26T10:22:48.775490+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Software Fault Localization Using DStar\" Wong Eric Debroy Journal of Systems and Software 2014"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Software Fault Localization Using DStar\" Wong Eric Debroy Journal of Systems and Software 2014"
  }
}
```

</details>

---

### Tool call

_source line 71 · 2026-05-26T10:22:48.775626+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"A Quantitative and Qualitative Evaluation of LLM-Based Explainable Fault Localization\" Sungmin Kang AutoFL FSE 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"A Quantitative and Qualitative Evaluation of LLM-Based Explainable Fault Localization\" Sungmin Kang AutoFL FSE 2024"
  }
}
```

</details>

---

### Tool call

_source line 72 · 2026-05-26T10:22:48.775743+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"AgentFL: Scaling LLM-based Fault Localization to Project-Level Context\" Yihao Qin ASE 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"AgentFL: Scaling LLM-based Fault Localization to Project-Level Context\" Yihao Qin ASE 2024"
  }
}
```

</details>

---

### Tool call

_source line 73 · 2026-05-26T10:22:48.775856+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Code Llama: Open Foundation Models for Code\" Baptiste Roziere arXiv 2308.12950"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Code Llama: Open Foundation Models for Code\" Baptiste Roziere arXiv 2308.12950"
  }
}
```

</details>

---

### Tool call

_source line 74 · 2026-05-26T10:22:48.775969+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Dataflow Analysis-Inspired Deep Learning for Efficient Vulnerability Detection\" Benjamin Steenhoek DeepDFA ICSE 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Dataflow Analysis-Inspired Deep Learning for Efficient Vulnerability Detection\" Benjamin Steenhoek DeepDFA ICSE 2024"
  }
}
```

</details>

---

### Tool call

_source line 75 · 2026-05-26T10:22:48.776080+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"SWE-bench: Can Language Models Resolve Real-World GitHub Issues\" Carlos Jimenez ICLR 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"SWE-bench: Can Language Models Resolve Real-World GitHub Issues\" Carlos Jimenez ICLR 2024"
  }
}
```

</details>

---

### Tool call

_source line 76 · 2026-05-26T10:22:48.776202+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Language Models (Mostly) Know What They Know\" Saurav Kadavath arXiv 2207.05221"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Language Models (Mostly) Know What They Know\" Saurav Kadavath arXiv 2207.05221"
  }
}
```

</details>

---

### Tool result

_source line 77 · 2026-05-26T10:22:48.776408+00:00_

Web search results for query: ""Visualization of Test Information to Assist Fault Localization" James Jones Mary Jean Harrold ICSE 2002"

Links: [{"title":"Visualization of test information to assist fault localization | Request PDF","url":"https://www.researchgate.net/publication/3952065_Visualization_of_test_information_to_assist_fault_localization"},{"title":"[PDF] Visualization of test information to assist fault localization | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Visualization-of-test-information-to-assist-fault-Jones-Harrold/54a7d105ee1a5256b168f16d8264262340c0f6c3"},{"title":"Visualization of Test Information to Assist Fault Localization","url":"https://sites.cc.gatech.edu/gvu/ii/talks/icse02.pdf"},{"title":"[ISER] [SME] Visualization of test information to assist fault localization | Academic Notes","url":"https://wym0120.github.io/2020/09/18/paper/ISER/Software%20Maintenance%20and%20Evolution/sme-1/"},{"title":"Visualization of test information to assist fault localization | Spider Lab Research Group","url":"https://spideruci.org/publication/jones-visualization-2002/"},{"title":"Visualization of Test Information to Assist Fault Localization","url":"https://faculty.cc.gatech.edu/~john.stasko/papers/icse02.pdf"},{"title":"Visualization of test information to assist fault localization | Proceedings of the 24th International Conference on Software Engineering","url":"https://dl.acm.org/doi/10.1145/581339.581397"},{"title":"Visualization of test information to assist fault localization | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/1007991/"},{"title":"[PDF] Visualization for Fault Localization | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Visualization-for-Fault-Localization-Jones-Harrold/a512b04457cd02779508b60662fd5c632abab78d"},{"title":"PPT - Visualization for Fault Localization PowerPoint Presentation, free download - ID:3677678","url":"https://www.slideserve.com/aderes/
…[truncated 1010 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 78 · 2026-05-26T10:22:48.776587+00:00_

Web search results for query: ""Software Fault Localization Using DStar" Wong Eric Debroy Journal of Systems and Software 2014"

Links: [{"title":"The DStar Method for Effective Software Fault Localization | Semantic Scholar","url":"https://www.semanticscholar.org/paper/The-DStar-Method-for-Effective-Software-Fault-Wong-Debroy/db47f26a6b8cfc59f9c0fd135034ee25fbef554b"},{"title":"[PDF] Software Fault Localization Using DStar (D*) | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Software-Fault-Localization-Using-DStar-(D*)-Wong-Debroy/dbfbaae06b0bad70792127044566e3a981516a34"},{"title":"Software Fault Localization Using DStar (D*)","url":"https://personal.utdallas.edu/~ewong/SE6367/01-Project/08-SFL-papers/06-DStar.pdf"},{"title":"Professor Eric Wong's Recent Publications","url":"https://personal.utdallas.edu/~wew021000/Eric-Wong-Home-Page/Eric-publication.html"},{"title":"Figure 3 from Software Fault Localization Using DStar (D*) | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Software-Fault-Localization-Using-DStar-(D*)-Wong-Debroy/dbfbaae06b0bad70792127044566e3a981516a34/figure/4"},{"title":"Software Fault Localization: an Overview of Research, Techniques, and Tools - Handbook of Software Fault Localization - Wiley Online Library","url":"https://onlinelibrary.wiley.com/doi/abs/10.1002/9781119880929.ch1"},{"title":"Software Fault Localization for Programs with Multiple Bugs - Handbook of Software Fault Localization - Wiley Online Library","url":"https://onlinelibrary.wiley.com/doi/abs/10.1002/9781119880929.ch12"},{"title":"Software Fault Localization: an Overview of Research, Techniques, and Tools | CoLab","url":"https://colab.ws/articles/10.1002/9781119880929.ch1"}]

Based on the search results, I found information about the paper you're looking for. The paper "Software Fault Localization Using DStar (D*)" proposes a technique that can identify suspicious locations for fault localization automatically without requiring any prior inf
…[truncated 1064 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 79 · 2026-05-26T10:22:48.776762+00:00_

Web search results for query: ""Code Llama: Open Foundation Models for Code" Baptiste Roziere arXiv 2308.12950"

Links: [{"title":"[2308.12950] Code Llama: Open Foundation Models for Code","url":"https://arxiv.org/abs/2308.12950"},{"title":"(PDF) Code Llama: Open Foundation Models for Code","url":"https://www.researchgate.net/publication/373364143_Code_Llama_Open_Foundation_Models_for_Code"},{"title":"Code Llama: Open Foundation Models for Code","url":"https://arxiv.org/html/2308.12950v3"},{"title":"Paper page - Code Llama: Open Foundation Models for Code","url":"https://huggingface.co/papers/2308.12950"},{"title":"[PDF] Code Llama: Open Foundation Models for Code | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Code-Llama:-Open-Foundation-Models-for-Code-Rozi%C3%A8re-Gehring/0b0debb710366cdff461938c80763eace1651af6"},{"title":"[2308.12950] Code Llama: Open Foundation Models for Code","url":"http://export.arxiv.org/abs/2308.12950"},{"title":"[2308.12950v3] Code Llama: Open Foundation Models for Code","url":"https://arxiv.org/abs/2308.12950v3"},{"title":"[2308.12950v2] Code Llama: Open Foundation Models for Code","url":"https://arxiv.org/abs/2308.12950v2"}]

I found the paper successfully! Here's what I found about "Code Llama: Open Foundation Models for Code" (arXiv:2308.12950):

**Paper Details:**
- The paper was submitted on August 24, 2023, with the latest version (v3) revised on January 31, 2024
- The paper is authored by Baptiste Rozière and 25 other co-authors

**Main Contribution:**
The paper releases Code Llama, a family of large language models for code based on Llama 2 providing state-of-the-art performance among open models, with infilling capabilities, support for large input contexts, and zero-shot instruction following ability for programming tasks.

**Model Variants:**
The paper provides multiple flavors to cover a wide range of applications: foundation models (Code Llama), Python specializations (Code Llama - Python), and instruction-
…[truncated 257 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 80 · 2026-05-26T10:22:48.776934+00:00_

Web search results for query: ""SWE-bench: Can Language Models Resolve Real-World GitHub Issues" Carlos Jimenez ICLR 2024"

Links: [{"title":"[2310.06770] SWE-bench: Can Language Models Resolve Real-World GitHub Issues?","url":"https://arxiv.org/abs/2310.06770"},{"title":"GitHub - SWE-bench/SWE-bench: SWE-bench: Can Language Models Resolve Real-world Github Issues? · GitHub","url":"https://github.com/SWE-bench/SWE-bench"},{"title":"Can Language Models Resolve Real-world Github Issues","url":"https://www.swebench.com/original.html"},{"title":"SWE-BENCH: CAN LANGUAGE MODELS RESOLVE REAL-WORLD GITHUB ISSUES? - Princeton University","url":"https://collaborate.princeton.edu/en/publications/swe-bench-can-language-models-resolve-real-world-github-issues/"},{"title":"SWE-bench: Can Language Models Resolve Real-world Github Issues?","url":"https://proceedings.iclr.cc/paper_files/paper/2024/hash/edac78c3e300629acfe6cbe9ca88fb84-Abstract-Conference.html"},{"title":"SWE-bench: Can Language Models Resolve Real-world Github Issues? | OpenReview","url":"https://openreview.net/forum?id=VTF8yNQM66"},{"title":"ICLR Oral SWE-bench: Can Language Models Resolve Real-world Github Issues?","url":"https://iclr.cc/virtual/2024/oral/19757"},{"title":"SWE-bench: Can Language Models Resolve Real-World GitHub Issues? | Princeton Language and Intelligence","url":"https://pli.princeton.edu/blog/2023/swe-bench-can-language-models-resolve-real-world-github-issues"},{"title":"SWE-bench: Can Language Models Resolve Real-World GitHub Issues? · Issue #758 · irthomasthomas/undecidability","url":"https://github.com/irthomasthomas/undecidability/issues/758"},{"title":"Paper page - SWE-bench: Can Language Models Resolve Real-World GitHub Issues?","url":"https://huggingface.co/papers/2310.06770"}]

I found comprehensive information about the paper. Here are the key details:

## SWE-bench: Can Language Models Resolve Real-World GitHub Issues

The paper is by Carlos E. Jimenez, John Yang, Alexander Wettig, Sh
…[truncated 1171 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 81 · 2026-05-26T10:22:48.777104+00:00_

Web search results for query: ""AgentFL: Scaling LLM-based Fault Localization to Project-Level Context" Yihao Qin ASE 2024"

Links: [{"title":"[2403.16362] AgentFL: Scaling LLM-based Fault Localization to Project-Level Context","url":"https://arxiv.org/abs/2403.16362"},{"title":"AgentFL: Scaling LLM-based Fault Localization to Project-Level Context","url":"https://arxiv.org/html/2403.16362v1"},{"title":"[PDF] AgentFL: Scaling LLM-based Fault Localization to Project-Level Context | Semantic Scholar","url":"https://www.semanticscholar.org/paper/AgentFL:-Scaling-LLM-based-Fault-Localization-to-Qin-Wang/ed56e11c9c454bed81ec1396196998b9ca9f5a6c"},{"title":"[2403.16362v2] AgentFL: Scaling LLM-based Fault Localization to Project-Level Context","url":"https://arxiv.org/abs/2403.16362v2"},{"title":"AgentFL: Scaling LLM-based Fault Localization to Project-Level Context - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240316362Q/abstract"},{"title":"[Literature Review] AgentFL: Scaling LLM-based Fault Localization to Project-Level Context","url":"https://www.themoonlight.io/en/review/agentfl-scaling-llm-based-fault-localization-to-project-level-context"},{"title":"Papers with Code - AgentFL: Scaling LLM-based Fault Localization to Project-Level Context","url":"https://cs.paperswithcode.com/paper/agentfl-scaling-llm-based-fault-localization"},{"title":"AGENTFL: Scaling LLM-based Fault Localization to Project-Level Context","url":"https://scispace.com/pdf/agentfl-scaling-llm-based-fault-localization-to-project-2417pl0g8f.pdf"}]

I found the research paper you're looking for! Here's what I found:

## AgentFL: Scaling LLM-based Fault Localization to Project-Level Context

The paper is authored by Yihao Qin, Shangwen Wang, Yiling Lou, Jinhao Dong, Kaixin Wang, Xiaoling Li, and Xiaoguang Mao from institutions including the National University of Defense Technology, Fudan University, and Peking University.

### Overview

The paper addresses the limitation of existing LLM-base
…[truncated 1164 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 82 · 2026-05-26T10:22:48.777305+00:00_

Web search results for query: ""A Quantitative and Qualitative Evaluation of LLM-Based Explainable Fault Localization" Sungmin Kang AutoFL FSE 2024"

Links: [{"title":"[2308.05487] A Quantitative and Qualitative Evaluation of LLM-Based Explainable Fault Localization","url":"https://arxiv.org/abs/2308.05487"},{"title":"A Quantitative and Qualitative Evaluation of LLM-Based Explainable Fault Localization | Proceedings of the ACM on Software Engineering","url":"https://dl.acm.org/doi/10.1145/3660771"},{"title":"A Quantitative and Qualitative Evaluation of LLM-based Explainable Fault Localization (FSE 2024 - Posters) - FSE 2024","url":"https://2024.esec-fse.org/details/fse-2024-posters/19/A-Quantitative-and-Qualitative-Evaluation-of-LLM-based-Explainable-Fault-Localization"},{"title":"A Quantitative and Qualitative Evaluation of LLM-based Explainable Fault Localization (FSE 2024 - Research Papers) - FSE 2024","url":"https://2024.esec-fse.org/details/fse-2024-research-papers/15/A-Quantitative-and-Qualitative-Evaluation-of-LLM-based-Explainable-Fault-Localization"},{"title":"A Quantitative and Qualitative Evaluation of LLM-Based Explainable Fault Localization","url":"https://arxiv.org/html/2308.05487v3"},{"title":"A Quantitative and Qualitative Evaluation of LLM-Based Explainable Fault","url":"https://smkang96.github.io/assets/pdf/AutoFLFSE_240717.pdf"},{"title":"[PDF] A Quantitative and Qualitative Evaluation of LLM-Based Explainable Fault Localization | Semantic Scholar","url":"https://www.semanticscholar.org/paper/A-Quantitative-and-Qualitative-Evaluation-of-Fault-Kang-An/9ac304b5531d5adc1b5021dfc0dbe6e90b41c406"},{"title":"A Quantitative and Qualitative Evaluation of LLM-Based Explainable Fault Localization | Request PDF","url":"https://www.researchgate.net/publication/382236264_A_Quantitative_and_Qualitative_Evaluation_of_LLM-Based_Explainable_Fault_Localization"},{"title":"Our paper \"A Quantitative and Qualitative Evaluation of LLM-based Explainable Fault Localizat
…[truncated 1512 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 83 · 2026-05-26T10:22:48.777501+00:00_

Web search results for query: ""Language Models (Mostly) Know What They Know" Saurav Kadavath arXiv 2207.05221"

Links: [{"title":"[2207.05221] Language Models (Mostly) Know What They Know","url":"https://arxiv.org/abs/2207.05221"},{"title":"(PDF) Language Models (Mostly) Know What They Know","url":"https://www.researchgate.net/publication/361949621_Language_Models_Mostly_Know_What_They_Know"},{"title":"[PDF] Language Models (Mostly) Know What They Know | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Language-Models-(Mostly)-Know-What-They-Know-Kadavath-Conerly/142ebbf4760145f591166bde2564ac70c001e927"},{"title":"(PDF) Language Models (Mostly) Know What They Know (2022) | Saurav Kadavath | 413 Citations","url":"https://scispace.com/papers/language-models-mostly-know-what-they-know-zkg0pou4"},{"title":"[2207.05221] Language Models (Mostly) Know What They Know – Papiers","url":"https://papiers.ai/2207.05221"},{"title":"Language Models (Mostly) Know What They Know - ADS","url":"https://ui.adsabs.harvard.edu/abs/2022arXiv220705221K/abstract"},{"title":"[2207.05221v4] Language Models (Mostly) Know What They Know","url":"https://arxiv.org/abs/2207.05221v4"},{"title":"ml-papers/papers/2022/220711 Language Models (Mostly) Know What They Know.md at main · rosinality/ml-papers","url":"https://github.com/rosinality/ml-papers/blob/main/papers/2022/220711%20Language%20Models%20(Mostly)%20Know%20What%20They%20Know.md"}]

I found information about this paper. Here's what I discovered:

The paper "Language Models (Mostly) Know What They Know" was authored by Saurav Kadavath, Tom Conerly, Amanda Askell, Tom Henighan, and 35 other authors. The study investigates whether language models can evaluate the validity of their own claims and predict which questions they will be able to answer correctly.

The paper shows that larger models are well-calibrated on diverse multiple choice and true/false questions when they are provided in the right format. Additionally, the res
…[truncated 618 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 84 · 2026-05-26T10:22:48.777695+00:00_

Web search results for query: ""Dataflow Analysis-Inspired Deep Learning for Efficient Vulnerability Detection" Benjamin Steenhoek DeepDFA ICSE 2024"

Links: [{"title":"Dataflow Analysis-Inspired Deep Learning for Efficient Vulnerability Detection (ICSE 2024 - Research Track) - ICSE 2024","url":"https://conf.researchr.org/details/icse-2024/icse-2024-research-track/63/Dataflow-Analysis-Inspired-Deep-Learning-for-Efficient-Vulnerability-Detection"},{"title":"Dataflow Analysis-Inspired Deep Learning for Efficient Vulnerability Detection - Benjamin Steenhoek","url":"https://benjijang.com/publication/2024-04-14-deepdfa"},{"title":"Dataflow Analysis-Inspired Deep Learning for Efficient Vulnerability Detection","url":"https://www.researchgate.net/publication/378028377_Dataflow_Analysis-Inspired_Deep_Learning_for_Efficient_Vulnerability_Detection"},{"title":"Dataflow Analysis-Inspired Deep Learning for Efficient Vulnerability Detection","url":"https://arxiv.org/pdf/2212.08108"},{"title":"[2212.08108] Dataflow Analysis-Inspired Deep Learning for Efficient Vulnerability Detection","url":"https://arxiv.org/abs/2212.08108"},{"title":"GitHub - ISU-PAAL/DeepDFA: Replication package for \"Dataflow Analysis-Inspired Deep Learning for Efficient Vulnerability Detection\", ICSE 2024.","url":"https://github.com/ISU-PAAL/DeepDFA"},{"title":"Dataflow Analysis-Inspired Deep Learning for Efficient Vulnerability Detection | Proceedings of the IEEE/ACM 46th International Conference on Software Engineering","url":"https://dl.acm.org/doi/10.1145/3597503.3623345"},{"title":"Item - Dataflow Analysis-Inspired Deep Learning for Efficient Vulnerability Detection - figshare - Figshare","url":"https://figshare.com/articles/dataset/Dataflow_Analysis-Inspired_Deep_Learning_for_Efficient_Vulnerability_Detection/21225413"},{"title":"bstee615 (Benjamin Steenhoek) · GitHub","url":"https://github.com/bstee615"},{"title":"[PDF] Dataflow Analysis-Inspired Deep Learning for Efficient Vulnerability Detection | 
…[truncated 1764 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 85 · 2026-05-26T10:22:48.777891+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"A Large-Scale Empirical Study of Just-in-Time Quality Assurance\" Yasutaka Kamei IEEE TSE 2013"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"A Large-Scale Empirical Study of Just-in-Time Quality Assurance\" Yasutaka Kamei IEEE TSE 2013"
  }
}
```

</details>

---

### Tool call

_source line 86 · 2026-05-26T10:22:48.778021+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"RepairAgent: An Autonomous LLM-Based Agent for Program Repair\" Islem Bouzenia ICSE 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"RepairAgent: An Autonomous LLM-Based Agent for Program Repair\" Islem Bouzenia ICSE 2025"
  }
}
```

</details>

---

### Tool call

_source line 87 · 2026-05-26T10:22:48.778140+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Code Execution with Pre-trained Language Models\" Chenxiao Liu ACL 2023 Findings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Code Execution with Pre-trained Language Models\" Chenxiao Liu ACL 2023 Findings"
  }
}
```

</details>

---

### Tool call

_source line 88 · 2026-05-26T10:22:48.778289+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Evaluating Representation Learning of Code Changes for Predicting Patch Correctness\" Haoye Tian ASE 2020"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Evaluating Representation Learning of Code Changes for Predicting Patch Correctness\" Haoye Tian ASE 2020"
  }
}
```

</details>

---

### Tool call

_source line 89 · 2026-05-26T10:22:48.778419+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"A Learning-Based Approach to Static Program Slicing\" Aashish Yadavally OOPSLA 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"A Learning-Based Approach to Static Program Slicing\" Aashish Yadavally OOPSLA 2024"
  }
}
```

</details>

---

### Tool call

_source line 90 · 2026-05-26T10:22:48.778532+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Agentless: Demystifying LLM-based Software Engineering Agents\" Chunqiu Steven Xia arXiv 2407.01489"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Agentless: Demystifying LLM-based Software Engineering Agents\" Chunqiu Steven Xia arXiv 2407.01489"
  }
}
```

</details>

---

### Tool call

_source line 91 · 2026-05-26T10:22:48.778652+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"On Calibration of Modern Neural Networks\" Chuan Guo ICML 2017"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"On Calibration of Modern Neural Networks\" Chuan Guo ICML 2017"
  }
}
```

</details>

---

### Tool call

_source line 92 · 2026-05-26T10:22:48.778765+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"A Survey of Confidence Estimation and Calibration in Large Language Models\" Jiahui Geng NAACL 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"A Survey of Confidence Estimation and Calibration in Large Language Models\" Jiahui Geng NAACL 2024"
  }
}
```

</details>

---

### Tool result

_source line 93 · 2026-05-26T10:22:48.778905+00:00_

Web search results for query: ""A Large-Scale Empirical Study of Just-in-Time Quality Assurance" Yasutaka Kamei IEEE TSE 2013"

Links: [{"title":"(PDF) A Large-Scale Empirical Study of Just-in-Time Quality Assurance","url":"https://www.researchgate.net/publication/260648765_A_Large-Scale_Empirical_Study_of_Just-in-Time_Quality_Assurance"},{"title":"[PDF] A large-scale empirical study of just-in-time quality assurance | Semantic Scholar","url":"https://www.semanticscholar.org/paper/A-large-scale-empirical-study-of-just-in-time-Kamei-Shihab/04eb410c0a59fc08a4648af43f7de323cc7d06c2"},{"title":"A Large-Scale Empirical Study of Just-in-Time Quality Assurance","url":"https://posl.ait.kyushu-u.ac.jp/~kamei/publications/Kamei_TSE2013.pdf"},{"title":"A large-scale empirical study of just-in-time quality assurance - Kyushu University Pure Portal Site","url":"https://kyushu-u.elsevierpure.com/en/publications/a-large-scale-empirical-study-of-just-in-time-quality-assurance/"},{"title":"A large-scale empirical study of just-in-time quality assurance | IEEE Journals & Magazine | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/6341763/"},{"title":"A large-scale empirical study of just-in-time quality assurance - PolyPublie","url":"https://publications.polymtl.ca/13693/"},{"title":"Publications - POSL: Y. Kamei, E. Shihab, B. Adams, A. E. Hassan, A. Mockus, A. Sinha, and N. Ubayashi, A Large-Scale Empirical Study of Just-In-Time Quality Assurance, 2013.","url":"https://posl.ait.kyushu-u.ac.jp/pman3/pman3.cgi?D=322"},{"title":"A Large-Scale Empirical Study of Just-in-Time Quality Assurance","url":"https://repository.usthb.dz/xmlui/handle/123456789/9054"}]

I found the paper you're looking for. Here are the details:

"A Large-Scale Empirical Study of Just-In-Time Quality Assurance" by Kamei, Y., Shihab, E., Adams, B., Hassan, A. E., Mockus, A., Sinha, A., & Ubayashi, N., published in IEEE Transactions on Software Engineering, Volume 39, Issue 6, pages 757-773, in 2013.

The p
…[truncated 741 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 94 · 2026-05-26T10:22:48.779065+00:00_

Web search results for query: ""Evaluating Representation Learning of Code Changes for Predicting Patch Correctness" Haoye Tian ASE 2020"

Links: [{"title":"Evaluating Representation Learning of Code Changes for Predicting Patch Correctness in Program Repair - ADS","url":"https://ui.adsabs.harvard.edu/abs/2020arXiv200802944T/abstract"},{"title":"Evaluating representation learning of code changes for predicting patch correctness in program repair | Proceedings of the 35th IEEE/ACM International Conference on Automated Software Engineering","url":"https://dl.acm.org/doi/10.1145/3324884.3416532"},{"title":"Evaluating Representation Learning of Code Changes for ...","url":"https://haoyetiancoder.github.io/papers/tian2020evaluating.pdf"},{"title":"Evaluating representation learning of code changes for predicting patch correctness in program repair - Monash University","url":"https://research.monash.edu/en/publications/evaluating-representation-learning-of-code-changes-for-predicting/"},{"title":"[PDF] Evaluating Representation Learning of Code Changes for Predicting Patch Correctness in Program Repair | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Evaluating-Representation-Learning-of-Code-Changes-Tian-Liu/521b813aeb71162fe74ad09da4a2bbbcd9919b70"},{"title":"[2008.02944] Evaluating Representation Learning of Code Changes for Predicting Patch Correctness in Program Repair","url":"https://ar5iv.labs.arxiv.org/html/2008.02944"},{"title":"Evaluating Representation Learning of Code Changes for Predicting Patch Correctness in Program Repair | Request PDF","url":"https://www.researchgate.net/publication/343546393_Evaluating_Representation_Learning_of_Code_Changes_for_Predicting_Patch_Correctness_in_Program_Repair"}]

I found the research paper you're looking for! Here's the information about it:

**Publication Details:**
The paper "Evaluating Representation Learning of Code Changes for Predicting Patch Correctness in Program Repair" was authored by Tian, H., L
…[truncated 1044 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 95 · 2026-05-26T10:22:48.779256+00:00_

Web search results for query: ""Code Execution with Pre-trained Language Models" Chenxiao Liu ACL 2023 Findings"

Links: [{"title":"Code Execution with Pre-trained Language Models - ACL Anthology","url":"https://aclanthology.org/2023.findings-acl.308/"},{"title":"Code Execution with Pre-trained Language Models | Request PDF","url":"https://www.researchgate.net/publication/372915950_Code_Execution_with_Pre-trained_Language_Models"},{"title":"Findings - ACL 2023","url":"https://2023.aclweb.org/program/accepted_findings/"},{"title":"[2305.05383] Code Execution with Pre-trained Language Models","url":"https://arxiv.org/abs/2305.05383"},{"title":"Code Execution with Pre-trained Language Models - Microsoft Research","url":"https://www.microsoft.com/en-us/research/publication/code-execution-with-pre-trained-language-models/"},{"title":"Code Execution with Pre-trained Language Models","url":"https://aclanthology.org/2023.findings-acl.308.pdf"},{"title":"Code Execution with Pre-trained Language Models","url":"https://arxiv.org/pdf/2305.05383"},{"title":"Pre-trained Language Model with Prompts for Temporal Knowledge Graph Completion - ACL Anthology","url":"https://aclanthology.org/2023.findings-acl.493/"}]

I found the paper you're looking for! Here are the details:

The paper "Code Execution with Pre-trained Language Models" was authored by Chenxiao Liu, Shuai Lu, Weizhu Chen, Daxin Jiang, Alexey Svyatkovskiy, Shengyu Fu, Neel Sundaresan, and Nan Duan and published in the Findings of ACL 2023. It appears in the proceedings on pages 4984–4999, in Toronto, Canada.

The paper addresses an important gap in pre-trained models for code: Code execution is a fundamental aspect of programming language semantics that reflects the exact behavior of the code. However, most pre-trained models for code intelligence ignore the execution trace and only rely on source code and syntactic structures.

To tackle this, the authors develop a mutation-based data augmentation technique to create a 
…[truncated 455 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 96 · 2026-05-26T10:22:48.779465+00:00_

Web search results for query: ""Agentless: Demystifying LLM-based Software Engineering Agents" Chunqiu Steven Xia arXiv 2407.01489"

Links: [{"title":"[2407.01489] Agentless: Demystifying LLM-based Software Engineering Agents","url":"https://arxiv.org/abs/2407.01489"},{"title":"Agentless : Demystifying LLM-based Software Engineering Agents","url":"https://arxiv.org/html/2407.01489v1"},{"title":"(PDF) Agentless: Demystifying LLM-based Software Engineering Agents","url":"https://www.researchgate.net/publication/381911059_Agentless_Demystifying_LLM-based_Software_Engineering_Agents"},{"title":"[2407.01489v2] Agentless: Demystifying LLM-based Software Engineering Agents","url":"https://arxiv.org/abs/2407.01489v2"},{"title":"[2407.01489v1] Agentless: Demystifying LLM-based Software Engineering Agents","url":"https://arxiv.org/abs/2407.01489v1"},{"title":"Agentless: Demystifying LLM-based Software Engineering Agents","url":"https://www.emergentmind.com/papers/2407.01489"},{"title":"dblp: Agentless: Demystifying LLM-based Software Engineering Agents.","url":"https://dblp.org/rec/journals/corr/abs-2407-01489.html"}]

I found the paper! Here's information about it:

**Title:** Agentless: Demystifying LLM-based Software Engineering Agents

**Authors and Affiliation:** Chunqiu Steven Xia, Yinlin Deng, Soren Dunn, and Lingming Zhang from the University of Illinois Urbana-Champaign

**arXiv Identifier:** 2407.01489

**Publication Timeline:** The paper was first submitted on July 1, 2024, with a revised version on October 29, 2024

**Core Contribution:** The paper presents Agentless, an agentless approach to automatically solve software development problems that employs a simplistic three-phase process of localization, repair, and patch validation

**Main Question:** The paper addresses the question of whether complex autonomous software agents are necessary, given their complexity and the limited abilities of current LLMs

**Key Finding:** Agentless, despite its simplicity, outp
…[truncated 251 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 97 · 2026-05-26T10:22:48.779648+00:00_

Web search results for query: ""A Survey of Confidence Estimation and Calibration in Large Language Models" Jiahui Geng NAACL 2024"

Links: [{"title":"A Survey of Confidence Estimation and Calibration in Large Language Models - ACL Anthology","url":"https://aclanthology.org/2024.naacl-long.366/"},{"title":"A Survey of Confidence Estimation and Calibration in Large Language Models","url":"https://www.researchgate.net/publication/382633391_A_Survey_of_Confidence_Estimation_and_Calibration_in_Large_Language_Models"},{"title":"[2311.08298] A Survey of Confidence Estimation and Calibration in Large Language Models","url":"https://arxiv.org/abs/2311.08298"},{"title":"[PDF] A Survey of Confidence Estimation and Calibration in Large Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/A-Survey-of-Confidence-Estimation-and-Calibration-Geng-Cai/6aa6003c7d7b3d275ae981aa6200014968c32430"},{"title":"A Survey of Confidence Estimation and Calibration in Large Language Models - YouTube","url":"https://www.youtube.com/watch?v=43a1XbHV7S8"},{"title":"[2311.08298v2] A Survey of Confidence Estimation and Calibration in Large Language Models","url":"https://arxiv.org/abs/2311.08298v2"},{"title":"A Survey of Confidence Estimation and Calibration in Large Language Models","url":"https://arxiv.org/html/2311.08298v2"},{"title":"A Survey of Confidence Estimation and Calibration in Large Language Models | alphaXiv","url":"https://www.alphaxiv.org/overview/2311.08298v2"}]

I found the paper you're looking for! Here are the search results:

"A Survey of Confidence Estimation and Calibration in Large Language Models" by Jiahui Geng, Fengyu Cai, Yuxia Wang, Heinz Koeppl, Preslav Nakov, and Iryna Gurevych was published in the Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers), pages 6577–6595, Mexico City, Mexico.

The paper addresses the fact that despite
…[truncated 822 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 98 · 2026-05-26T10:22:48.779817+00:00_

Web search results for query: ""A Learning-Based Approach to Static Program Slicing" Aashish Yadavally OOPSLA 2024"

Links: [{"title":"A Learning-Based Approach to Static Program Slicing (SPLASH 2024 - OOPSLA 2024) - SPLASH 2024","url":"https://2024.splashcon.org/details/splash-2024-oopsla/4/A-Learning-Based-Approach-to-Static-Program-Slicing"},{"title":"A Learning-Based Approach to Static Program Slicing","url":"https://aashishyadavally.github.io/assets/pdf/pub-oopsla2024.pdf"},{"title":"A Learning-Based Approach to Static Program Slicing | Proceedings of the ACM on Programming Languages","url":"https://dl.acm.org/doi/10.1145/3649814"},{"title":"[OOPSLA24] A Learning-Based Approach to Static Program Slicing - YouTube","url":"https://www.youtube.com/watch?v=JhFDjtNkRi8"},{"title":"A Learning-Based Approach to Static Program Slicing | Request PDF","url":"https://www.researchgate.net/publication/380202230_A_Learning-Based_Approach_to_Static_Program_Slicing"},{"title":"A Learning-Based Approach to Static Program Slicing","url":"https://dl.acm.org/doi/pdf/10.1145/3649814"},{"title":"Aashish Yadavally","url":"https://www.cecs.ucf.edu/faculty/aashish-yadavally/"},{"title":"Aashish Yadavally Assistant Professor Department of Computer Science","url":"https://aashishyadavally.github.io/assets/pdf/cv.pdf"},{"title":"publications | Aashish Yadavally","url":"https://aashishyadavally.github.io/publications/"}]

I found the research paper you're looking for! Here's what I found:

## Paper Overview

"A Learning-Based Approach to Static Program Slicing" presents NS-Slicer, a novel learning-based approach that predicts static program slices for both complete and partial code.

## Authors and Publication

The paper is authored by Aashish Yadavally, Yi Li, Shaohua Wang, and Tien N. Nguyen, and was published in Proceedings of the 2024 ACM SIGPLAN International Conference on Object-Oriented Programming, Systems, Languages, and Applications (OOPSLA 2024) with an acceptance rate of 38.5%.
…[truncated 855 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 99 · 2026-05-26T10:22:48.780016+00:00_

Web search results for query: ""On Calibration of Modern Neural Networks" Chuan Guo ICML 2017"

Links: [{"title":"[1706.04599] On Calibration of Modern Neural Networks","url":"https://arxiv.org/abs/1706.04599"},{"title":"On Calibration of Modern Neural Networks","url":"https://proceedings.mlr.press/v70/guo17a/guo17a.pdf"},{"title":"On calibration of modern neural networks | Proceedings of the 34th International Conference on Machine Learning - Volume 70","url":"https://dl.acm.org/doi/10.5555/3305381.3305518"},{"title":"On Calibration of Modern Neural Networks Chuan Guo Kilian Q. Weinberger","url":"https://fernandoperezc.github.io/Advanced-Topics-in-Machine-Learning-and-Data-Science/Fluri.pdf"},{"title":"On Calibration of Modern Neural Networks","url":"https://github.com/vlgiitr/papers_we_read/blob/master/summaries/Calibration_of_Neural_Nets.md"},{"title":"\"On Calibration of Modern Neural Networks\", Guo et al. • David Stutz","url":"https://davidstutz.de/on-calibration-of-modern-neural-networks-guo-et-al/"},{"title":"(Open Access) On Calibration of Modern Neural Networks (2017) | Chuan Guo | 4418 Citations","url":"https://scispace.com/papers/on-calibration-of-modern-neural-networks-5cc9ha8ohx"},{"title":"On Calibration of Modern Neural Networks | PDF | Artificial Neural Network | Deep Learning","url":"https://www.scribd.com/document/611497504/1706-04599"},{"title":"On Calibration of Modern Neural Networks | BibSonomy","url":"https://www.bibsonomy.org/bibtex/268aff8dcf6ef5c7d6050192e5218f9d3/tobias.koopmann"},{"title":"Guo, C., Pleiss, G., Sun Y. and Weinberger, K.Q. (2017）On Calibration of Modern Neural Networks. Proceedings of the 34th International Conference on Machine Learning, Sydney, Vol. 70, 1321-1330. - References - Scientific Research Publishing","url":"https://www.scirp.org/(S(czeh4tfqyw2orz553k1w0r45))/reference/referencespapers?referenceid=3648829"}]

I found several results for "On Calibration of Modern Neural Networks" by Chuan Guo et al. from ICML 201
…[truncated 1153 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 100 · 2026-05-26T10:22:48.780206+00:00_

Web search results for query: ""RepairAgent: An Autonomous LLM-Based Agent for Program Repair" Islem Bouzenia ICSE 2025"

Links: [{"title":"RepairAgent: An Autonomous, LLM-Based Agent for Program Repair (ICSE 2025 - Research Track) - ICSE 2025","url":"https://conf.researchr.org/details/icse-2025/icse-2025-research-track/160/RepairAgent-An-Autonomous-LLM-Based-Agent-for-Program-Repair"},{"title":"RepairAgent: An Autonomous, LLM-Based Agent for Program Repair | ELLIS Unit Stuttgart","url":"https://ellis-stuttgart.eu/publications/icse2025-RepairAgent/"},{"title":"RepairAgent: An Autonomous, LLM-Based Agent for Program Repair","url":"https://arxiv.org/pdf/2403.17134"},{"title":"GitHub - sola-st/RepairAgent: RepairAgent is an autonomous LLM-based agent for software repair. · GitHub","url":"https://github.com/sola-st/RepairAgent"},{"title":"Islem Bouzenia - Software Lab - Department of Computer Science - University of Stuttgart","url":"https://software-lab.org/people/Islem_Bouzenia.html"},{"title":"dblp: Islem Bouzenia","url":"https://dblp.org/pid/324/8017.html"},{"title":"[2403.17134] RepairAgent: An Autonomous, LLM-Based Agent for Program Repair","url":"https://arxiv.org/abs/2403.17134"},{"title":"RepairAgent: An Autonomous, LLM-Based Agent for Program Repair | Proceedings of the IEEE/ACM 47th International Conference on Software Engineering","url":"https://dl.acm.org/doi/10.1109/ICSE55347.2025.00157"},{"title":"[Literature Review] RepairAgent: An Autonomous, LLM-Based Agent for Program Repair","url":"https://www.themoonlight.io/en/review/repairagent-an-autonomous-llm-based-agent-for-program-repair"}]

I found comprehensive information about the paper. Here are the search results:

## RepairAgent: An Autonomous, LLM-Based Agent for Program Repair

RepairAgent is the first work to address the program repair challenge through an autonomous agent based on a large language model (LLM), authored by Islem Bouzenia, Premkumar Devanbu, and Michael Pradel.

**Key Approach:**

Un
…[truncated 1420 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 101 · 2026-05-26T10:22:48.780420+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"DeepJIT: An End-to-End Deep Learning Framework for Just-in-Time Defect Prediction\" Thong Hoang MSR 2019"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"DeepJIT: An End-to-End Deep Learning Framework for Just-in-Time Defect Prediction\" Thong Hoang MSR 2019"
  }
}
```

</details>

---

### Tool call

_source line 102 · 2026-05-26T10:22:48.780549+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"CC2Vec: Distributed Representations of Code Changes\" Thong Hoang ICSE 2020"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"CC2Vec: Distributed Representations of Code Changes\" Thong Hoang ICSE 2020"
  }
}
```

</details>

---

### Tool call

_source line 103 · 2026-05-26T10:22:48.780668+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"JITLine: A Simpler, Better, Faster, Finer-grained Just-In-Time Defect Prediction\" Chanathip Pornprasit MSR 2021"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"JITLine: A Simpler, Better, Faster, Finer-grained Just-In-Time Defect Prediction\" Chanathip Pornprasit MSR 2021"
  }
}
```

</details>

---

### Tool result

_source line 104 · 2026-05-26T10:22:48.780806+00:00_

Web search results for query: ""DeepJIT: An End-to-End Deep Learning Framework for Just-in-Time Defect Prediction" Thong Hoang MSR 2019"

Links: [{"title":"[PDF] DeepJIT: An End-to-End Deep Learning Framework for Just-in-Time Defect Prediction | Semantic Scholar","url":"https://www.semanticscholar.org/paper/DeepJIT:-An-End-to-End-Deep-Learning-Framework-for-Hoang-Dam/952fe2400f4b1a33fa45aa1aefaa856235e13c0c"},{"title":"DeepJIT: An End-to-End Deep Learning Framework for Just-in-Time Defect Prediction | Request PDF","url":"https://www.researchgate.net/publication/335498581_DeepJIT_An_End-to-End_Deep_Learning_Framework_for_Just-in-Time_Defect_Prediction"},{"title":"DeepJIT: an end-to-end deep learning framework for just-in ...","url":"https://dl.acm.org/doi/10.1109/msr.2019.00016"},{"title":"DeepJIT: An End-To-End Deep LearningFramework for Just-In-Time Defect Prediction (MSR 2019 - Technical Papers) - MSR 2019","url":"https://2019.msrconf.org/details/msr-2019-papers/11/DeepJIT-An-End-To-End-Deep-LearningFramework-for-Just-In-Time-Defect-Prediction"},{"title":"DeepJIT: an end-to-end deep learning framework for just-in ...","url":"https://ink.library.smu.edu.sg/cgi/viewcontent.cgi?article=5489&context=sis_research"},{"title":"DeepJIT: An End-to-End Deep Learning Framework for Just-in-Time Defect Prediction | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/iel7/8804710/8816727/08816772.pdf"},{"title":"[PDF] Deep Learning for Just-in-Time Defect Prediction | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Deep-Learning-for-Just-in-Time-Defect-Prediction-Yang-Lo/e4be4ba1d428bc89f63662ae7b0db097fa83d651"}]

Based on the search results, I found information about the DeepJIT paper:

DeepJIT: An End-to-End Deep Learning Framework for Just-in-Time Defect Prediction was published in May 2019 at the 2019 16th IEEE/ACM International Conference on Mining Software Repositories (MSR) in Montreal, Canada.

The paper was authored by Thong Ho
…[truncated 709 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 105 · 2026-05-26T10:22:48.780953+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Curriculum Learning\" Yoshua Bengio ICML 2009"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Curriculum Learning\" Yoshua Bengio ICML 2009"
  }
}
```

</details>

---

### Tool call

_source line 106 · 2026-05-26T10:22:48.781103+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"How to Train Data-Efficient LLMs\" Noveen Sachdeva arXiv 2402.09668"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"How to Train Data-Efficient LLMs\" Noveen Sachdeva arXiv 2402.09668"
  }
}
```

</details>

---

### Tool call

_source line 107 · 2026-05-26T10:22:48.781302+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Dataset Cartography: Mapping and Diagnosing Datasets with Training Dynamics\" Swabha Swayamdipta EMNLP 2020"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Dataset Cartography: Mapping and Diagnosing Datasets with Training Dynamics\" Swabha Swayamdipta EMNLP 2020"
  }
}
```

</details>

---

### Tool call

_source line 108 · 2026-05-26T10:22:48.781440+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining\" Sang Michael Xie NeurIPS 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining\" Sang Michael Xie NeurIPS 2023"
  }
}
```

</details>

---

### Tool call

_source line 109 · 2026-05-26T10:22:48.781559+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering\" John Yang NeurIPS 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering\" John Yang NeurIPS 2024"
  }
}
```

</details>

---

### Tool result

_source line 110 · 2026-05-26T10:22:48.781710+00:00_

Web search results for query: ""CC2Vec: Distributed Representations of Code Changes" Thong Hoang ICSE 2020"

Links: [{"title":"CC2Vec: Distributed Representations of Code Changes (ICSE 2020 - Technical Papers) - ICSE 2020","url":"https://2020.icse-conferences.org/details/icse-2020-papers/10/CC2Vec-Distributed-Representations-of-Code-Changes"},{"title":"CC2Vec: Distributed Representations of Code Changes","url":"https://arxiv.org/pdf/2003.05620"},{"title":"[PDF] CC2Vec: Distributed Representations of Code Changes | Semantic Scholar","url":"https://www.semanticscholar.org/paper/CC2Vec:-Distributed-Representations-of-Code-Changes-Hoang-Kang/0dfe706526e5234338411489e1826b4060acc4e8"},{"title":"[2003.05620] CC2Vec: Distributed Representations of Code Changes","url":"https://arxiv.org/abs/2003.05620"},{"title":"CC2Vec: distributed representations of code changes | Request PDF","url":"https://www.researchgate.net/publication/346022771_CC2Vec_distributed_representations_of_code_changes"},{"title":"GitHub - soarsmu/CC2Vec: Artifact website for the paper, CC2Vec: Distributed Representations of Code Changes","url":"https://github.com/soarsmu/CC2Vec"},{"title":"CC2Vec: distributed representations of code changes","url":"https://dl.acm.org/doi/10.1145/3377811.3380361"},{"title":"Representing Code Changes as Vectors: CC2Vec – Embold Blog","url":"https://blog.embold.io/representing-code-changes-as-vectors-cc2vec/"}]

I found the paper! Here's information about CC2Vec:

## CC2Vec: Distributed Representations of Code Changes

**Authors:** Thong Hoang, Hong Jin Kang, Julia Lawall, David Lo

**Venue:** ICSE 2020 (42nd International Conference on Software Engineering)

### Overview

CC2Vec is a neural network model that learns the representation of code changes guided by their accompanying log messages, which represent the semantic intent of the code changes.

### Key Features

CC2Vec models the hierarchical structure of a code change with the help of the attention mechanism and uses m
…[truncated 565 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 111 · 2026-05-26T10:22:48.781880+00:00_

Web search results for query: ""JITLine: A Simpler, Better, Faster, Finer-grained Just-In-Time Defect Prediction" Chanathip Pornprasit MSR 2021"

Links: [{"title":"JITLine: A Simpler, Better, Faster, Finer-grained Just-In-Time Defect Prediction | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/9463103/"},{"title":"JITLine: a simpler, better, faster, finer-grained Just-In-Time defect prediction - Monash University","url":"https://research.monash.edu/en/publications/jitline-a-simpler-better-faster-finer-grained-just-in-time-defect/"},{"title":"(PDF) JITLine: A Simpler, Better, Faster, Finer-grained Just-In-Time Defect Prediction","url":"https://www.researchgate.net/publication/350061459_JITLine_A_Simpler_Better_Faster_Finer-grained_Just-In-Time_Defect_Prediction"},{"title":"[2103.07068] JITLine: A Simpler, Better, Faster, Finer-grained Just-In-Time Defect Prediction","url":"https://arxiv.org/abs/2103.07068"},{"title":"JITLine: A Simpler, Better, Faster, Finer-grained Just-In-Time Defect Prediction - ADS","url":"https://ui.adsabs.harvard.edu/abs/2021arXiv210307068P/abstract"},{"title":"JITLine: A Simpler, Better, Faster, Finer-grained Just-In-Time Defect Prediction | DeepAI","url":"https://deepai.org/publication/jitline-a-simpler-better-faster-finer-grained-just-in-time-defect-prediction"},{"title":"Papers with Code - JITLine: A Simpler, Better, Faster, Finer-grained Just-In-Time Defect Prediction","url":"https://cs.paperswithcode.com/paper/jitline-a-simpler-better-faster-finer-grained"}]

I found the research paper you're looking for. Here's a summary of the key information:

## JITLine: A Simpler, Better, Faster, Finer-grained Just-In-Time Defect Prediction

JITLine is a Just-In-Time defect prediction approach for predicting defect-introducing commits and identifying lines that are associated with that defect-introducing commit (i.e., defective lines).

**Key Findings:**

The research was conducted by Chanathip Pornprasit and co
…[truncated 917 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 112 · 2026-05-26T10:22:48.782056+00:00_

Web search results for query: ""Curriculum Learning" Yoshua Bengio ICML 2009"

Links: [{"title":"Curriculum learning | Proceedings of the 26th Annual International Conference on Machine Learning","url":"https://dl.acm.org/doi/10.1145/1553374.1553380"},{"title":"Curriculum Learning Yoshua Bengio1 Yoshua.Bengio@umontreal.ca","url":"https://ronan.collobert.com/pub/2009_curriculum_icml.pdf"},{"title":"Curriculum learning (2009) | Yoshua Bengio | 6391 Citations","url":"https://scispace.com/papers/curriculum-learning-a335v5etyf"},{"title":"(PDF) Curriculum learning","url":"https://www.academia.edu/58928901/Curriculum_learning"},{"title":"Yoshua Bengio - Curriculum Learning (2009) | tomrochette.com","url":"https://blog.tomrochette.com/machine-learning/papers/yoshua-bengio-curriculum-learning"},{"title":"[PDF] Curriculum learning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Curriculum-learning-Bengio-Louradour/8de174ab5419b9d3127695405efd079808e956e8"},{"title":"dblp: Curriculum learning.","url":"https://dblp.org/rec/conf/icml/BengioLCW09.html"},{"title":"Curriculum learning","url":"https://bibbase.org/network/publication/bengio-louradour-collobert-weston-curriculumlearning-2009"},{"title":"Bengio, 2009 Curriculum Learning.pdf","url":"https://www.scribd.com/document/425393423/Bengio-2009-Curriculum-Learning-pdf"},{"title":"BibSLEIGH — Curriculum learning","url":"https://bibtex.github.io/ICML-2009-BengioLCW.html"}]

I've found comprehensive information about the paper. Here are the key details:

**Paper Details:**
The paper "Curriculum learning" was authored by Yoshua Bengio, Jérôme Louradour, Ronan Collobert, and Jason Weston, and it was published in the ICML '09: Proceedings of the 26th Annual International Conference on Machine Learning on June 14, 2009, pages 41-48.

**Main Concept:**
The paper formalizes the observation that humans and animals learn much better when examples are organized in a meaningful order illustrating gradually more concepts and
…[truncated 675 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 113 · 2026-05-26T10:22:48.782254+00:00_

Web search results for query: ""DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining" Sang Michael Xie NeurIPS 2023"

Links: [{"title":"[2305.10429] DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining","url":"https://arxiv.org/abs/2305.10429"},{"title":"DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining","url":"https://proceedings.neurips.cc/paper_files/paper/2023/file/dcba6be91359358c2355cd920da3fcbd-Paper-Conference.pdf"},{"title":"NeurIPS Poster DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining","url":"https://neurips.cc/virtual/2023/poster/70588"},{"title":"Paper page - DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining","url":"https://huggingface.co/papers/2305.10429"},{"title":"DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining | Request PDF","url":"https://www.researchgate.net/publication/370841750_DoReMi_Optimizing_Data_Mixtures_Speeds_Up_Language_Model_Pretraining"},{"title":"GitHub - sangmichaelxie/doremi: Pytorch implementation of DoReMi, a method for optimizing the data mixture weights in language modeling datasets · GitHub","url":"https://github.com/sangmichaelxie/doremi"},{"title":"DoReMi: optimizing data mixtures speeds up language ...","url":"https://dl.acm.org/doi/10.5555/3666122.3669181"},{"title":"[PDF] DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining | Semantic Scholar","url":"https://www.semanticscholar.org/paper/DoReMi:-Optimizing-Data-Mixtures-Speeds-Up-Language-Xie-Pham/9b4f7c97c0b83a80c32bc0b93595cbcfb4ecb16d"},{"title":"[Quick Review] DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining","url":"https://liner.com/review/doremi-optimizing-data-mixtures-speeds-up-language-model-pretraining"}]

I found comprehensive information about the DoReMi paper. Here's what I found:

## Overview

DoReMi proposes Domain Reweighting with Minimax Optimization (DoReMi), which first trains a small proxy model usi
…[truncated 1044 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 114 · 2026-05-26T10:22:48.782448+00:00_

Web search results for query: ""Dataset Cartography: Mapping and Diagnosing Datasets with Training Dynamics" Swabha Swayamdipta EMNLP 2020"

Links: [{"title":"Dataset Cartography: Mapping and Diagnosing Datasets with Training Dynamics - ACL Anthology","url":"https://aclanthology.org/2020.emnlp-main.746/"},{"title":"GitHub - allenai/cartography: Dataset Cartography: Mapping and Diagnosing Datasets with Training Dynamics · GitHub","url":"https://github.com/allenai/cartography"},{"title":"Dataset Cartography: Mapping and Diagnosing Datasets with Training Dynamics | Request PDF","url":"https://www.researchgate.net/publication/347237029_Dataset_Cartography_Mapping_and_Diagnosing_Datasets_with_Training_Dynamics"},{"title":"[PDF] Dataset Cartography: Mapping and Diagnosing Datasets with Training Dynamics | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Dataset-Cartography:-Mapping-and-Diagnosing-with-Swayamdipta-Schwartz/ee5fff85d3ec62698eddba162f054b7e73670b2a"},{"title":"[2009.10795] Dataset Cartography: Mapping and Diagnosing Datasets with Training Dynamics","url":"https://arxiv.org/abs/2009.10795"},{"title":"Dataset Cartography: Mapping and Diagnosing Datasets with Training Dynamics | Paper to HTML | Allen Institute for AI","url":"https://a11y2.apps.allenai.org/paper?id=ee5fff85d3ec62698eddba162f054b7e73670b2a"},{"title":"Dataset cartography: Mapping and diagnosing datasets with training dynamics - The Hebrew University of Jerusalem","url":"https://cris.huji.ac.il/en/publications/dataset-cartography-mapping-and-diagnosing-datasets-with-training/"},{"title":"Dataset cartography: Mapping and diagnosing datasets with training dynamics","url":"https://www.mendeley.com/catalogue/5ef551f0-f6e4-3329-a092-e574463bf2b6/"}]

I found the paper you were looking for! Here are the details:

**Paper Citation:**
Dataset Cartography: Mapping and Diagnosing Datasets with Training Dynamics was published by Swabha Swayamdipta, Roy Schwartz, Nicholas Lourie, Yizhong Wang, H
…[truncated 1227 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 115 · 2026-05-26T10:22:48.782633+00:00_

Web search results for query: ""SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering" John Yang NeurIPS 2024"

Links: [{"title":"SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering","url":"https://proceedings.neurips.cc/paper_files/paper/2024/hash/5a7c947568c1b1328ccc5230172e1e7c-Abstract-Conference.html"},{"title":"[2405.15793] SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering","url":"https://arxiv.org/abs/2405.15793"},{"title":"NeurIPS Poster SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering","url":"https://neurips.cc/virtual/2024/poster/93753"},{"title":"GitHub - SWE-agent/SWE-agent: SWE-agent takes a GitHub issue and tries to automatically fix it, using your LM of choice. It can also be employed for offensive cybersecurity or competitive coding challenges. [NeurIPS 2024] · GitHub","url":"https://github.com/SWE-agent/SWE-agent"},{"title":"SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering - Princeton University","url":"https://collaborate.princeton.edu/en/publications/swe-agent-agent-computer-interfaces-enable-automated-software-eng/"},{"title":"SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering | OpenReview","url":"https://openreview.net/forum?id=mXpq6ut8J3"},{"title":"SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering - New Jersey Research Community","url":"https://www.researchwithnj.com/en/publications/swe-agent-agent-computer-interfaces-enable-automated-software-eng/"},{"title":"[Quick Review] SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering","url":"https://liner.com/review/sweagent-agentcomputer-interfaces-enable-automated-software-engineering"},{"title":"NeurIPS Poster SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering","url":"https://nips.cc/virtual/2024/poster/93753"},{"title":"[PDF] SWE-agent: Agent-Computer Interfaces Enable Automated Softw
…[truncated 1537 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 116 · 2026-05-26T10:22:48.782813+00:00_

Web search results for query: ""How to Train Data-Efficient LLMs" Noveen Sachdeva arXiv 2402.09668"

Links: [{"title":"[2402.09668] How to Train Data-Efficient LLMs","url":"https://arxiv.org/abs/2402.09668"},{"title":"How to Train Data-Efficient LLMs","url":"https://arxiv.org/html/2402.09668v1"},{"title":"[PDF] How to Train Data-Efficient LLMs | Semantic Scholar","url":"https://www.semanticscholar.org/paper/How-to-Train-Data-Efficient-LLMs-Sachdeva-Coleman/31b2918acc77682b5a499da1aa111f34e76d9603"},{"title":"2402.09668 - How to Train Data-Efficient LLMs","url":"https://www.emergentmind.com/papers/2402.09668"},{"title":"GitHub - susumuota/nano-askllm: Unofficial implementation of the Ask-LLM paper 'How to Train Data-Efficient LLMs', arXiv:2402.09668. · GitHub","url":"https://github.com/susumuota/nano-askllm"},{"title":"Preference Curriculum: LLMs Should Always Be Pretrained on Their Preferred Data","url":"https://arxiv.org/html/2501.13126v1"},{"title":"Multi-Agent Collaborative Data Selection for Efficient LLM Pretraining","url":"https://arxiv.org/html/2410.08102v1"},{"title":"Beyond Random Sampling: Efficient Language Model Pretraining via Curriculum Learning","url":"https://arxiv.org/html/2506.11300v1"},{"title":"Paper page - How to Train Data-Efficient LLMs","url":"https://huggingface.co/papers/2402.09668"},{"title":"How to train data-efficient LLMs | OpenReview","url":"https://openreview.net/forum?id=yKUbw7q1IA"}]

I found the paper! Here's what I found:

This paper studies data-efficient approaches for pre-training LLMs, which are techniques that aim to optimize the Pareto frontier of model quality and training resource/data consumption.

The paper proposes two main techniques:

1. **Ask-LLM**: Leverages the zero-shot reasoning capabilities of instruction-tuned LLMs to directly assess the quality of a training example.

2. **Density sampling**: Models the data distribution to select a diverse sample.

In their comparison of 19 samplers involving hundreds of eval
…[truncated 507 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 117 · 2026-05-26T10:22:48.783001+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"OpenHands: An Open Platform for AI Software Developers as Generalist Agents\" Xingyao Wang ICLR 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"OpenHands: An Open Platform for AI Software Developers as Generalist Agents\" Xingyao Wang ICLR 2025"
  }
}
```

</details>

---

### Tool call

_source line 118 · 2026-05-26T10:22:48.783131+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"LLMLingua: Compressing Prompts for Accelerated Inference\" Huiqiang Jiang EMNLP 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"LLMLingua: Compressing Prompts for Accelerated Inference\" Huiqiang Jiang EMNLP 2023"
  }
}
```

</details>

---

### Tool call

_source line 119 · 2026-05-26T10:22:48.783279+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Compressing Context to Enhance Inference Efficiency of Large Language Models\" Yucheng Li Selective Context EMNLP 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Compressing Context to Enhance Inference Efficiency of Large Language Models\" Yucheng Li Selective Context EMNLP 2023"
  }
}
```

</details>

---

### Tool call

_source line 120 · 2026-05-26T10:22:48.783430+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"The Oracle Problem in Software Testing: A Survey\" Earl Barr IEEE TSE 2015"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"The Oracle Problem in Software Testing: A Survey\" Earl Barr IEEE TSE 2015"
  }
}
```

</details>

---

### Tool call

_source line 121 · 2026-05-26T10:22:48.783549+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Mutation Testing Advances: An Analysis and Survey\" Mike Papadakis Advances in Computers 2019"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Mutation Testing Advances: An Analysis and Survey\" Mike Papadakis Advances in Computers 2019"
  }
}
```

</details>

---

### Tool call

_source line 122 · 2026-05-26T10:22:48.783670+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Large Language Models Can Be Easily Distracted by Irrelevant Context\" Freda Shi ICML 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Large Language Models Can Be Easily Distracted by Irrelevant Context\" Freda Shi ICML 2023"
  }
}
```

</details>

---

### Tool call

_source line 123 · 2026-05-26T10:22:48.783783+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"LDB: A Large Language Model Debugger via Verifying Runtime Execution Step by Step\" Li Zhong ACL 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"LDB: A Large Language Model Debugger via Verifying Runtime Execution Step by Step\" Li Zhong ACL 2024"
  }
}
```

</details>

---

### Tool call

_source line 124 · 2026-05-26T10:22:48.783893+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Teaching Large Language Models to Self-Debug\" Xinyun Chen ICLR 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Teaching Large Language Models to Self-Debug\" Xinyun Chen ICLR 2024"
  }
}
```

</details>

---

### Tool result

_source line 125 · 2026-05-26T10:22:48.784040+00:00_

Web search results for query: ""The Oracle Problem in Software Testing: A Survey" Earl Barr IEEE TSE 2015"

Links: [{"title":"[PDF] The Oracle Problem in Software Testing: A Survey | Semantic Scholar","url":"https://www.semanticscholar.org/paper/The-Oracle-Problem-in-Software-Testing:-A-Survey-Barr-Harman/0e17ab6c9d31a481c641f2b1760e09ea51ab76cc"},{"title":"(PDF) The Oracle Problem in Software Testing: A Survey","url":"https://www.researchgate.net/publication/276255185_The_Oracle_Problem_in_Software_Testing_A_Survey"},{"title":"The oracle problem in software testing: A survey - Korea Advanced Institute of Science and Technology","url":"https://pure.kaist.ac.kr/en/publications/the-oracle-problem-in-software-testing-a-survey/"},{"title":"(PDF) The Oracle Problem in Software Testing: A Survey","url":"https://www.academia.edu/24870121/The_Oracle_Problem_in_Software_Testing_A_Survey"},{"title":"The oracle problem in software testing: A survey – Related Work","url":"https://alastairreid.github.io/RelatedWork/papers/barr:tse:2015/"},{"title":"The Oracle Problem in Software Testing: A Survey - UCL Discovery","url":"https://discovery.ucl.ac.uk/id/eprint/1471263/"},{"title":"The Oracle Problem in Software Testing: A Survey | IEEE Transactions on Software Engineering","url":"https://dl.acm.org/doi/10.1109/TSE.2014.2372785"},{"title":"1 The Oracle Problem in Software Testing: A Survey","url":"https://earlbarr.com/publications/testoracles.pdf"},{"title":"The Oracle Problem in Software Testing: A Survey","url":"https://discovery.ucl.ac.uk/id/eprint/1471263/1/06963470.pdf"}]

I found the paper you're looking for. The paper "The Oracle Problem in Software Testing: A Survey" by Barr, Harman, McMinn, Shahbaz, and Yoo was published in IEEE Transactions on Software Engineering, volume 41, issue 5, pages 507-525 in 2015.

The paper addresses the test oracle problem, which is the challenge of distinguishing the corresponding desired, correct behaviour from potentially incorrect behavior 
…[truncated 490 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 126 · 2026-05-26T10:22:48.784211+00:00_

Web search results for query: ""OpenHands: An Open Platform for AI Software Developers as Generalist Agents" Xingyao Wang ICLR 2025"

Links: [{"title":"ICLR Poster OpenHands: An Open Platform for AI Software Developers as Generalist Agents","url":"https://iclr.cc/virtual/2025/poster/29831"},{"title":"[2407.16741] OpenHands: An Open Platform for AI Software Developers as Generalist Agents","url":"https://arxiv.org/abs/2407.16741"},{"title":"Published as a conference paper at ICLR 2025 OPENHANDS: AN OPEN PLATFORM FOR","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/a4b6ad6b48850c0c331d1259fc66a69c-Paper-Conference.pdf"},{"title":"OpenHands: An Open Platform for AI Software Developers as Generalist Agents","url":"https://proceedings.iclr.cc/paper_files/paper/2025/hash/a4b6ad6b48850c0c331d1259fc66a69c-Abstract-Conference.html"},{"title":"OpenHands: An Open Platform for AI Software Developers as Generalist Agents","url":"https://arxiv.org/html/2407.16741v3"},{"title":"ICLR Invited Talk: Designing, Building, and Training Effective Software Engineering Agents by Xingyao Wang","url":"https://iclr.cc/virtual/2025/10000566"},{"title":"OpenHands: Open Platform for AI Software Agents and What It Means for Finance Automation - Beancount.io","url":"https://beancount.io/bean-labs/research-logs/2026/06/30/openhands-open-platform-ai-software-developers-generalist-agents"},{"title":"OPENHANDS: AN OPEN PLATFORM FOR AI SOFTWARE DEVELOPERS AS GENERALIST AGENTS - Illinois Experts","url":"https://experts.illinois.edu/en/publications/openhands-an-open-platform-for-ai-software-developers-as-generali/"},{"title":"[Quick Review] OpenHands: An Open Platform for AI Software Developers as Generalist Agents","url":"https://liner.com/review/openhands-an-open-platform-for-ai-software-developers-as-generalist"}]

I found comprehensive information about this ICLR 2025 paper. Here are the key details:

## Paper Overview

OpenHands is a platform for the development of powerful and flexib
…[truncated 1387 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 127 · 2026-05-26T10:22:48.784402+00:00_

Web search results for query: ""Compressing Context to Enhance Inference Efficiency of Large Language Models" Yucheng Li Selective Context EMNLP 2023"

Links: [{"title":"Compressing Context to Enhance Inference Efficiency of Large Language   Models","url":"https://arxiv.org/pdf/2310.06201"},{"title":"Paper page - Compressing Context to Enhance Inference Efficiency of Large Language Models","url":"https://huggingface.co/papers/2310.06201"},{"title":"Compressing Context to Enhance Inference Efficiency of Large Language Models - ACL Anthology","url":"https://aclanthology.org/2023.emnlp-main.391/"},{"title":"In-Context Former: Lightning-fast Compressing Context for Large Language   Model","url":"https://arxiv.org/pdf/2406.13618"},{"title":"Enhancing and Accelerating Large Language Models via Instruction-Aware   Contextual Compression","url":"https://arxiv.org/pdf/2408.15491"},{"title":"[2310.06201] Compressing Context to Enhance Inference Efficiency of Large Language Models","url":"https://arxiv.org/abs/2310.06201"}]

I found the paper you're looking for! Here's what I found:

The paper "Compressing Context to Enhance Inference Efficiency of Large Language Models" was authored by Yucheng Li, Bo Dong, Frank Guerin, and Chenghua Lin and published at EMNLP 2023.

The paper proposes a method called Selective Context that enhances the inference efficiency of LLMs by identifying and pruning redundancy in the input context to make the input more compact. The approach was tested using common data sources requiring long context processing: arXiv papers, news articles, and long conversations, on tasks of summarisation, question answering, and response generation.

The results show that they achieved a 50% reduction in context cost, resulting in a 36% reduction in inference memory usage and a 32% reduction in inference time, while observing only a minor drop of .023 in BERTscore and .038 in faithfulness on four downstream applications.

The paper is available on arXiv (2310.06201)
…[truncated 237 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 128 · 2026-05-26T10:22:48.784577+00:00_

Web search results for query: ""LLMLingua: Compressing Prompts for Accelerated Inference" Huiqiang Jiang EMNLP 2023"

Links: [{"title":"LLMLingua: Compressing Prompts for Accelerated Inference of Large Language Models - ACL Anthology","url":"https://aclanthology.org/2023.emnlp-main.825/"},{"title":"[2310.05736] LLMLingua: Compressing Prompts for Accelerated Inference of Large Language Models","url":"https://arxiv.org/abs/2310.05736"},{"title":"LLMLingua: Compressing Prompts for Accelerated Inference of Large Language Models","url":"https://llmlingua.com/llmlingua.html"},{"title":"LLMLingua: Innovating LLM efficiency with prompt compression - Microsoft Research","url":"https://www.microsoft.com/en-us/research/blog/llmlingua-innovating-llm-efficiency-with-prompt-compression/"},{"title":"GitHub - microsoft/LLMLingua: [EMNLP'23, ACL'24] To speed up LLMs' inference and enhance LLM's perceive of key information, compress the prompt and KV-Cache, which achieves up to 20x compression with minimal performance loss. · GitHub","url":"https://github.com/microsoft/LLMLingua"},{"title":"LLMLingua: Compressing Prompts for Accelerated Inference of Large Language Models - Microsoft Research","url":"https://www.microsoft.com/en-us/research/publication/llmlingua-compressing-prompts-for-accelerated-inference-of-large-language-models/"},{"title":"LLMLingua: Compressing Prompts for Accelerated Inference of Large Language Models","url":"https://arxiv.org/html/2310.05736v2"},{"title":"LLMLingua: Compressing Prompts for Accelerated Inference of Large Language Models [Quick Review]","url":"https://liner.com/review/llmlingua-compressing-prompts-for-accelerated-inference-large-language-models"},{"title":"Compressing Prompts for Accelerated Inference of Large ...","url":"https://aclanthology.org/2023.emnlp-main.825.pdf"}]

I found comprehensive information about the paper. Here are the search results:

## Paper Overview

LLMLingua: Compressing Prompts for Accelerated Inference of Large Language
…[truncated 1274 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 129 · 2026-05-26T10:22:48.784752+00:00_

Web search results for query: ""Mutation Testing Advances: An Analysis and Survey" Mike Papadakis Advances in Computers 2019"

Links: [{"title":"Mutation Testing Advances: An Analysis and Survey | Request PDF","url":"https://www.researchgate.net/publication/325014033_Mutation_Testing_Advances_An_Analysis_and_Survey"},{"title":"[PDF] Chapter Six - Mutation Testing Advances: An Analysis and Survey | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Chapter-Six-Mutation-Testing-Advances:-An-Analysis-Papadakis-Kintis/d461ab9482b7fb5eadd7e6cd2c6dffced8ede8b8"},{"title":"Mutation Testing Advances: An Analysis and Survey - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0065245818300305"},{"title":"Mutation Testing Advances: An Analysis and Survey - Papadakis Mike","url":"https://publications.uni.lu/handle/10993/31612"},{"title":"Chapter Six: Mutation Testing Advances: An Analysis and Survey - Advances in Computers [Book]","url":"https://www.oreilly.com/library/view/advances-in-computers/9780128151228/S0065245818300305_1.xhtml"},{"title":"Mutation Testing Advances: An Analysis and Survey","url":"https://scite.ai/reports/mutation-testing-advances-an-analysis-ZGEyL6y"},{"title":"dblp: Chapter Six - Mutation Testing Advances: An Analysis and Survey.","url":"https://dblp.org/rec/journals/ac/PapadakisK00TH19.html"},{"title":"Mutation testing advances: An analysis and survey (chapter 6)","url":"https://alastairreid.github.io/RelatedWork/papers/papadakis:advances:2019/"},{"title":"Github","url":"https://mpapad.github.io/publications/pdfs/MutationSurvey2019.pdf"},{"title":"Mutation Testing Advances: An Analysis and Survey | Scilit","url":"https://www.scilit.com/publications/f7c1e8603f8979f7a383b350281424ae"}]

I found the publication you're looking for. Here are the details:

**"Mutation Testing Advances: An Analysis and Survey"** is a chapter by Mike Papadakis, Marinos Kintis, Jie Zhang, Yue Jia, Yves Le Traon, and Mark Harman, published 
…[truncated 699 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 130 · 2026-05-26T10:22:48.784934+00:00_

Web search results for query: ""Large Language Models Can Be Easily Distracted by Irrelevant Context" Freda Shi ICML 2023"

Links: [{"title":"Large Language Models Can Be Easily Distracted by Irrelevant Context","url":"https://proceedings.mlr.press/v202/shi23a.html"},{"title":"[2302.00093] Large Language Models Can Be Easily Distracted by Irrelevant Context","url":"https://arxiv.org/abs/2302.00093"},{"title":"Large language models can be easily distracted by irrelevant context | Proceedings of the 40th International Conference on Machine Learning","url":"https://dl.acm.org/doi/10.5555/3618408.3619699"},{"title":"Large Language Models Can Be Easily Distracted by Irrelevant Context","url":"https://openreview.net/pdf?id=JSZmoN03Op"},{"title":"Large Language Models Can Be Easily Distracted by Irrelevant Context. | BibSonomy","url":"https://www.bibsonomy.org/bibtex/7a5e56e46d0a590ba4f0fe0b2e3d532d"},{"title":"[Quick Review] Large Language Models Can Be Easily Distracted by Irrelevant Context","url":"https://liner.com/review/large-language-models-can-be-easily-distracted-by-irrelevant-context"},{"title":"[PDF] Large Language Models Can Be Easily Distracted by Irrelevant Context | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Large-Language-Models-Can-Be-Easily-Distracted-by-Shi-Chen/3d68522abfadfc8ee6b7ec9edaaf91f1b2f38e5e"},{"title":"(PDF) Large Language Models Can Be Easily Distracted by Irrelevant Context","url":"https://www.researchgate.net/publication/367961918_Large_Language_Models_Can_Be_Easily_Distracted_by_Irrelevant_Context"},{"title":"Large Language Models Can Be Easily Distracted by Irrelevant Context | OpenReview","url":"https://openreview.net/forum?id=JSZmoN03Op"},{"title":"ml-papers/papers/2023/230131 Large Language Models Can Be Easily Distracted by Irrelevant Context.md at main · rosinality/ml-papers","url":"https://github.com/rosinality/ml-papers/blob/main/papers/2023/230131%20Large%20Language%20Models%20Can%20Be%20Easily%20Distracted%20
…[truncated 1413 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 131 · 2026-05-26T10:22:48.785116+00:00_

Web search results for query: ""LDB: A Large Language Model Debugger via Verifying Runtime Execution Step by Step" Li Zhong ACL 2024"

Links: [{"title":"GitHub - FloridSleeves/LLMDebugger: LDB: A Large Language Model Debugger via Verifying Runtime Execution Step by Step (ACL'24) · GitHub","url":"https://github.com/FloridSleeves/LLMDebugger"},{"title":"Debug like a Human: A Large Language Model Debugger via Verifying Runtime Execution Step by Step - ACL Anthology","url":"https://aclanthology.org/2024.findings-acl.49/"},{"title":"[2402.16906] Debug like a Human: A Large Language Model Debugger via Verifying Runtime Execution Step-by-step","url":"https://arxiv.org/abs/2402.16906"},{"title":"A Large Language Model Debugger via Verifying Runtime ...","url":"https://aclanthology.org/2024.findings-acl.49.pdf"},{"title":"Paper Review — Debug like a Human: A Large Language Model Debugger via Verifying Runtime Execution Step-by-step (ACL 2024) | by Riley Learning | Medium","url":"https://rileylearning.medium.com/paper-review-debug-like-a-human-a-large-language-model-debugger-via-verifying-runtime-execution-3872e931cf40"},{"title":"LDB: A Large Language Model Debugger via Verifying Runtime Execution Step by Step","url":"https://arxiv.org/html/2402.16906v1"},{"title":"[2402.16906v3] LDB: A Large Language Model Debugger via Verifying Runtime Execution Step-by-step","url":"https://arxiv.org/abs/2402.16906v3"},{"title":"LDB: A Large Language Model Debugger via Verifying Runtime Execution Step-by-step | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/ldb-large-language-model-debugger-via-verifying"},{"title":"[Quick Review] Debug like a Human: A Large Language Model Debugger via Verifying Runtime Execution Step by Step","url":"https://liner.com/review/debug-like-human-large-language-model-debugger-via-verifying-runtime"},{"title":"Paper page - LDB: A Large Language Model Debugger via Verifying Runtime Execution Step-by-step","url":"https://huggingface.co/pap
…[truncated 1531 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 132 · 2026-05-26T10:22:48.785313+00:00_

Web search results for query: ""Teaching Large Language Models to Self-Debug" Xinyun Chen ICLR 2024"

Links: [{"title":"[2304.05128] Teaching Large Language Models to Self-Debug","url":"https://arxiv.org/abs/2304.05128"},{"title":"TEACHING LARGE LANGUAGE MODELS TO SELF- DEBUG","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/2460396f2d0d421885997dd1612ac56b-Paper-Conference.pdf"},{"title":"Teaching Large Language Models to Self-Debug | OpenReview","url":"https://openreview.net/forum?id=KuPixIqPiq"},{"title":"[PDF] Teaching Large Language Models to Self-Debug | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Teaching-Large-Language-Models-to-Self-Debug-Chen-Lin/9e3c493fb09dcd61bb05e8c5659f23327b7b6340"},{"title":"LARGE LANGUAGE MODELS CANNOT SELF-CORRECT ...","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/8b4add8b0aa8749d80a34ca5d941c355-Paper-Conference.pdf"},{"title":"Revisit Self-Debugging with Self-Generated Tests for Code ...","url":"https://aclanthology.org/2025.acl-long.881.pdf"},{"title":"[Quick Review] Teaching Large Language Models to Self-Debug","url":"https://liner.com/review/teaching-large-language-models-to-selfdebug"},{"title":"Xinyun Chen's Homepage","url":"https://jungyhuk.github.io/"},{"title":"GitHub - ryokamoi/llm-self-correction-papers: List of papers on Self-Correction of LLMs. · GitHub","url":"https://github.com/ryokamoi/llm-self-correction-papers"}]

Based on the search results, I found the paper you're looking for. Here's what I can tell you about it:

"Teaching Large Language Models to Self-Debug" proposes Self-Debugging, which teaches a large language model to debug its predicted program via few-shot demonstrations.

Self-Debugging can teach the large language model to perform rubber duck debugging; i.e., without any human feedback on the code correctness or error messages, the model is able to identify its mistakes by investigating the execution results and explaining the generated code in natur
…[truncated 594 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 133 · 2026-05-26T10:22:48.785508+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Reflexion: Language Agents with Verbal Reinforcement Learning\" Noah Shinn NeurIPS 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Reflexion: Language Agents with Verbal Reinforcement Learning\" Noah Shinn NeurIPS 2023"
  }
}
```

</details>

---

### Tool call

_source line 134 · 2026-05-26T10:22:48.785636+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Wong Debroy Gao Li \"Software Fault Localization Using DStar\" \"Journal of Systems and Software\" 2014 volume 91"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Wong Debroy Gao Li \"Software Fault Localization Using DStar\" \"Journal of Systems and Software\" 2014 volume 91"
  }
}
```

</details>

---

### Tool result

_source line 135 · 2026-05-26T10:22:48.785785+00:00_

Web search results for query: ""Reflexion: Language Agents with Verbal Reinforcement Learning" Noah Shinn NeurIPS 2023"

Links: [{"title":"GitHub - noahshinn/reflexion: [NeurIPS 2023] Reflexion: Language Agents with Verbal Reinforcement Learning · GitHub","url":"https://github.com/noahshinn/reflexion"},{"title":"[2303.11366] Reflexion: Language Agents with Verbal Reinforcement Learning","url":"https://arxiv.org/abs/2303.11366"},{"title":"NeurIPS Poster Reflexion: language agents with verbal reinforcement learning","url":"https://neurips.cc/virtual/2023/poster/70114"},{"title":"Reflexion: Language Agents with Verbal Reinforcement Learning Noah Shinn","url":"https://proceedings.neurips.cc/paper_files/paper/2023/file/1b44b878bb782e6954cd888628510e90-Paper-Conference.pdf"},{"title":"Reflexion: Language Agents with Verbal Reinforcement Learning","url":"https://arxiv.org/html/2303.11366"},{"title":"Reflexion: Language Agents with Verbal Reinforcement Learning - Princeton University","url":"https://collaborate.princeton.edu/en/publications/reflexion-language-agents-with-verbal-reinforcement-learning-2/"},{"title":"Reflexion: language agents with verbal reinforcement learning [Quick Review]","url":"https://liner.com/review/reflexion-language-agents-with-verbal-reinforcement-learning"},{"title":"GitHub - noahshinn/reflexion: [NeurIPS 2023] Reflexion: Language Agents with Verbal Reinforcement Learning","url":"https://github.com/noahshinn/reflexion/tree/main"}]

I found comprehensive information about "Reflexion: Language Agents with Verbal Reinforcement Learning" by Noah Shinn and colleagues. Here's what the search revealed:

## Overview

Reflexion is a novel framework to reinforce language agents not by updating weights, but instead through linguistic feedback. Reflexion agents verbally reflect on task feedback signals, then maintain their own reflective text in an episodic memory buffer to induce better decision-making in subsequent trials.

## Problem It Addresses

It rema
…[truncated 889 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 136 · 2026-05-26T10:22:48.785970+00:00_

Web search results for query: "Wong Debroy Gao Li "Software Fault Localization Using DStar" "Journal of Systems and Software" 2014 volume 91"

Links: [{"title":"[PDF] Software Fault Localization Using DStar (D*) | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Software-Fault-Localization-Using-DStar-(D*)-Wong-Debroy/dbfbaae06b0bad70792127044566e3a981516a34"},{"title":"The DStar Method for Effective Software Fault Localization | Semantic Scholar","url":"https://www.semanticscholar.org/paper/The-DStar-Method-for-Effective-Software-Fault-Wong-Debroy/db47f26a6b8cfc59f9c0fd135034ee25fbef554b"},{"title":"Effective software fault localization using predicted execution results | Software Quality Journal","url":"https://link.springer.com/article/10.1007/s11219-015-9295-1"},{"title":"Emerging Aspects of Software Fault Localization - Handbook of Software Fault Localization - Wiley Online Library","url":"https://onlinelibrary.wiley.com/doi/10.1002/9781119880929.ch13"},{"title":"[PDF] A Survey on Software Fault Localization | Semantic Scholar","url":"https://www.semanticscholar.org/paper/A-Survey-on-Software-Fault-Localization-Wong-Gao/4667536a1f2175c7b7bfe6113e4b316e64d35136"},{"title":"International Journal of Software Engineering and Knowledge Engineering","url":"https://www.worldscientific.com/doi/10.1142/S0218194024500219"},{"title":"Effective fault localization using probabilistic and grouping approach | International Journal of System Assurance Engineering and Management | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s13198-024-02479-5"},{"title":"Software Fault Localization: an Overview of Research, Techniques, and Tools - Handbook of Software Fault Localization - Wiley Online Library","url":"https://onlinelibrary.wiley.com/doi/10.1002/9781119880929.ch1"},{"title":"Software Fault Localization Using DStar (D*)","url":"https://personal.utdallas.edu/~ewong/SE6367/01-Project/08-SFL-papers/06-DStar.pdf"}]

Based on the search results,
…[truncated 969 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w1_20260526T101523",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 137 · 2026-05-26T10:22:48.786310+00:00_

全部 57 条 WebSearch 完成。现在编译验证报告。

---

# 引用验证报告（Worker 1/3）

## 逐条验证结果

```
[abreu2007accuracy] Abreu(2007) "On the Accuracy of..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: N/A
  引用位置: [related_work.tex:19] ✓ — SBFL suspiciousness排序
  问题: 无

[appt2024] Zhang(2024) "APPT: Boosting Automated..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: N/A
  引用位置: [related_work.tex:17] ✓ — patch correctness prediction进展
  问题: 无

[austin2021program] Austin(2021) "Program Synthesis with..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: ✓ (2108.07732)
  引用位置: [introduction.tex:14] ✓ — MBPP-sanitized来源
  引用位置: [method.tex:13] ✓ — MBPP-sanitized来源
  问题: 无

[barr2015oracle] Barr(2015) "The Oracle Problem in..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: N/A
  引用位置: [related_work.tex:15] ✓ — test oracle problem
  问题: 无

[bengio2009curriculum] Bengio(2009) "Curriculum Learning"
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: N/A
  引用位置: [related_work.tex:51] ✓ — curriculum learning
  问题: 无

[bouzenia2025repairagent] Bouzenia(2025) "RepairAgent: An Autonomous..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: N/A
  引用位置: [related_work.tex:20] ✓ — agent-based repair
  问题: 无

[chen2021evaluating] Chen(2021) "Evaluating Large Language..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: ✓ (2107.03374)
  引用位置: [introduction.tex:14] ✓ — HumanEval来源
  引用位置: [method.tex:13] ✓ — HumanEval来源
  问题: 无

[chen2024selfdebug] Chen(2024) "Teaching Large Language..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: N/A
  引用位置: [related_work.tex:21] ✓ — 用execution outcomes迭代修复
  问题: 无

[chen2025tracepile] Chen(2025) "Chain of Execution..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓ (NeurIPS 2025)  arXiv: ✓ (2510.23629)
  引用位置: [introduction.tex:4] ✓ — trace-augmented训练
  引用位置: [related_work.tex:5] ✓ — TracePile预训练
  引用位置: [method.tex:7] ✓ — code generation任务对比
  问题: 无

[deepseek2024coder] Guo(2024) "DeepSeek-Coder: When the..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: ✓ (2401.14196)
  引用位置: [introduction.tex:14] ✓ — 模型家族之一
  引用位置: [method.tex:32] ✓ — DeepSeek-Coder-6.7B
  问题: 无

[ding2024traced] Ding(2024) "TRACED: Execution-aware..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓ (ICSE 2024)  arXiv: ✓ (2306.07487)
  引用位置: [introduction.tex:4] ✓ — trace-augmented code models
  引用位置: [related_work.tex:16] ✓ — execution-aware pretraining
  问题: 无

[eguchi2025etcot] Eguchi(2025) "Making LLMs Program..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓ (ICML 2025 PRAL Workshop)  arXiv: N/A
  引用位置: [related_work.tex:7] ✓ — trace chain-of-thought
  问题: 无

[ferrando2025execute] Armengol-Estapé(2025) "What I Cannot Execute..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓ (arXiv preprint)  arXiv: ✓ (2503.05703)
  引用位置: [related_work.tex:7] ✓ — compact traces comparable to full traces
  问题: 无（bib key "ferrando"无对应作者，仅为key命名问题）

[foster2025mutation] Foster(2025) "Mutation-Guided LLM-based..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓ (FSE 2025 Industry Track)  arXiv: ✓ (2501.12862)
  引用位置: [related_work.tex:18] ✓ — mutation outcomes改善定位
  问题: 无

[geng2024calibration] Geng(2024) "A Survey of Confidence..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓ (NAACL 2024)  arXiv: N/A
  引用位置: [related_work.tex:48] ✓ — LLM calibration survey
  问题: 无

[gu2024cruxeval] Gu(2024) "CRUXEval: A Benchmark..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓ (ICML 2024)  arXiv: ✓ (2401.03065)
  引用位置: [related_work.tex:8] ✓ — execution reasoning benchmark
  引用位置: [method.tex:7] ✓ — output prediction任务对比
  问题: 无

[guo2017calibration] Guo(2017) "On Calibration of Modern..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓ (ICML 2017)  arXiv: N/A
  引用位置: [related_work.tex:48] ✓ — neural network calibration
  问题: 无

[haque2025traces] Haque(2025) "Towards Effectively Leveraging..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓ (KnowledgeNLP@ACL 2025)  arXiv: ✓ (2505.04441)
  引用位置: [related_work.tex:10] ✓ — raw traces provide limited repair benefit
  问题: 无

[hoang2019deepjit] Hoang(2019) "DeepJIT: An End-to-End..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓ (MSR 2019)  arXiv: N/A
  引用位置: [related_work.tex:50] ✓ — JIT defect prediction
  问题: 无

[hoang2020cc2vec] Hoang(2020) "CC2Vec: Distributed Representations..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓ (ICSE 2020)  arXiv: N/A
  引用位置: [related_work.tex:17] ✓ — code change representation learning
  问题: 无

[hu2022lora] Hu(2022) "LoRA: Low-Rank Adaptation..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓ (ICLR 2022)  arXiv: ✓ (2106.09685)
  引用位置: [method.tex:33] ✓ — LoRA训练方法
  引用位置: [appendix.tex:38] ✓ — LoRA训练方法
  问题: 无

[huang2026tracecoder] Huang(2026) "TraceCoder: A Trace-Driven..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓ (ICSE 2026)  arXiv: ✓ (2602.06875)
  引用位置: [related_work.tex:10] ✓ — selective trace extraction for debugging
  问题: 无

[jiang2023llmlingua] Jiang(2023) "LLMLingua: Compressing Prompts..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓ (EMNLP 2023)  arXiv: N/A
  引用位置: [related_work.tex:10] ✓ — prompt compression
  引用位置: [discussion.tex:66] ✓ — prompt compression
  问题: 无

[jimenez2024swebench] Jimenez(2024) "SWE-bench: Can Language..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓ (ICLR 2024)  arXiv: N/A
  引用位置: [related_work.tex:20] ✓ — SWE-bench ecosystem
  问题: 无

[jones2002visualization] Jones(2002) "Visualization of Test..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓ (ICSE 2002)  arXiv: N/A
  引用位置: [related_work.tex:19] ✓ — SBFL
  问题: 无

[kadavath2022language] Kadavath(2022) "Language Models (Mostly)..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓ (arXiv preprint)  arXiv: ✓ (2207.05221)
  引用位置: [related_work.tex:48] ✓ — LLM self-knowledge/calibration
  问题: 无

[kamei2013large] Kamei(2013) "A Large-Scale Empirical..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓ (IEEE TSE)  arXiv: N/A
  引用位置: [related_work.tex:50] ✓ — JIT quality assurance
  问题: 无

[kang2024autofl] Kang(2024) "A Quantitative and Qualitative..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓ (FSE 2024)  arXiv: ✓ (2308.05487)
  引用位置: [related_work.tex:19] ✓ — LLM-based fault localization (AutoFL)
  问题: 无

[li2023selectivecontext] Li(2023) "Compressing Context to..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓ (EMNLP 2023)  arXiv: N/A
  引用位置: [related_work.tex:10] ✓ — context compression
  引用位置: [discussion.tex:66] ✓ — Selective Context
  问题: 无

[liu2023codeexecution] Liu(2023) "Code Execution with..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓ (Findings ACL 2023)  arXiv: N/A
  引用位置: [related_work.tex:5] ✓ — pre-trained models to predict execution outputs
  问题: 无

[ni2024next] Ni(2024) "NExT: Teaching Large..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓ (ICML 2024)  arXiv: ✓ (2404.14662)
  引用位置: [introduction.tex:4] ✓ — trace-augmented code models
  引用位置: [related_work.tex:7] ✓ — trace chain-of-thought
  问题: 无

[papadakis2019mutation] Papadakis(2019) "Mutation Testing Advances..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓ (Advances in Computers)  arXiv: N/A
  引用位置: [related_work.tex:18] ✓ — equivalent-mutant problem
  问题: 无

[pornprasit2021jitline] Pornprasit(2021) "JITLine: A Simpler..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓ (MSR 2021)  arXiv: N/A
  引用位置: [related_work.tex:50] ✓ — JIT defect prediction
  问题: 无

[qin2024agentfl] Qin(2024) "AgentFL: Scaling LLM-based..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓ (ASE 2024)  arXiv: ✓ (2403.16362)
  引用位置: [related_work.tex:19] ✓ — LLM-based fault localization
  问题: 无

[qwen2025coder] Qwen Team(2024) "Qwen2.5-Coder Technical..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓ (arXiv preprint)  arXiv: ✓ (2409.12186)
  引用位置: [introduction.tex:14] ✓ — Qwen模型来源
  引用位置: [method.tex:32] ✓ — Qwen模型来源
  问题: 无

[roziere2024code] Rozière(2023) "Code Llama: Open Foundation..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓ (arXiv preprint)  arXiv: N/A (URL未提供但2308.12950)
  引用位置: [introduction.tex:14] ✓ — CodeLlama模型来源
  引用位置: [method.tex:32] ✓ — CodeLlama模型来源
  问题: 无

[sachdeva2024dataefficient] Sachdeva(2024) "How to Train Data-Efficient..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓ (arXiv preprint)  arXiv: ✓ (2402.09668)
  引用位置: [related_work.tex:51] ✓ — data selection methods
  问题: 无

[shi2023distracted] Shi(2023) "Large Language Models Can..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓ (ICML 2023)  arXiv: N/A
  引用位置: [related_work.tex:9] ✓ — LLMs distracted by irrelevant context
  问题: 无

[shinn2023reflexion] Shinn(2023) "Reflexion: Language Agents..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓ (NeurIPS 2023)  arXiv: N/A
  引用位置: [related_work.tex:21] ✓ — iterative code refinement with execution outcomes
  问题: 无

[spiess2025calibration] Spiess(2025) "Calibration and Correctness..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓ (ICSE 2025)  arXiv: ✓ (2402.02047)
  引用位置: [related_work.tex:48] ✓ — code model calibration
  引用位置: [appendix.tex:547] ✓ — code LLM confidence calibration
  问题: 无

[steenhoek2024deepdfa] Steenhoek(2024) "Dataflow Analysis-Inspired..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓ (ICSE 2024)  arXiv: N/A
  引用位置: [related_work.tex:16] ✓ — dataflow + deep learning for defect detection
  问题: 无

[swayamdipta2020cartography] Swayamdipta(2020) "Dataset Cartography..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓ (EMNLP 2020)  arXiv: N/A
  引用位置: [related_work.tex:51] ✓ — dataset cartography via training dynamics
  问题: 无

[tian2020patchcorrectness] Tian(2020) "Evaluating Representation..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓ (ASE 2020)  arXiv: N/A
  引用位置: [related_work.tex:17] ✓ — code change representation for patch correctness
  问题: 无

[tian2024debugbench] Tian(2024) "DebugBench: Evaluating..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓ (Findings ACL 2024)  arXiv: ✓ (2401.04621)
  引用位置: [experiments.tex:126] ✓ — cross-dataset generalization
  引用位置: [appendix.tex:617] ✓ — DebugBench dataset
  问题: 无

[wang2025dcsh] Wang(2025) "Do Code Semantics Help?..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓ (Findings EMNLP 2025)  arXiv: ✓ (2509.11686)
  引用位置: [introduction.tex:4] ✓ — trace-augmented code models
  引用位置: [introduction.tex:12] ✓ — no single trace representation best
  引用位置: [related_work.tex:6] ✓ — trace utility task-dependent
  问题: 无

[wang2025inspectcoder] Wang(2025) "InspectCoder: Dynamic..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓ (arXiv preprint)  arXiv: ✓ (2510.18327)
  引用位置: [related_work.tex:10] ✓ — selective trace extraction for debugging
  问题: 无

[wang2025openhands] Wang(2025) "OpenHands: An Open..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓ (ICLR 2025)  arXiv: ✓ (2407.16741)
  引用位置: [related_work.tex:20] ✓ — agent-based repair
  问题: 无

[widyasari2024fusefl] Widyasari(2024) "Demystifying Faulty Code..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓ (SANER 2024)  arXiv: N/A
  引用位置: [related_work.tex:18] ✓ — structured fault signals improve localization
  问题: 无

[wong2014dstar] Wong(2014) "Software Fault Localization..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓ (JSS, DOI确认)  arXiv: N/A
  引用位置: [related_work.tex:19] ✓ — SBFL D* metric
  问题: 无

[xia2024agentless] Xia(2024) "Agentless: Demystifying..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓ (arXiv preprint)  arXiv: ✓ (2407.01489)
  引用位置: [related_work.tex:20] ✓ — agentless repair
  问题: 无

[xie2023doremi] Xie(2023) "DoReMi: Optimizing Data..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓ (NeurIPS 2023)  arXiv: ✓ (2305.10429)
  引用位置: [related_work.tex:51] ✓ — data selection/mixture optimization
  问题: 无

[xu2025cruxevalx] Xu(2025) "CRUXEval-X: A Benchmark..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓ (ACL 2025)  arXiv: ✓ (2408.13001)
  引用位置: [related_work.tex:8] ✓ — multilingual extension of CRUXEval
  问题: 无

[yadavally2024slicing] Yadavally(2024) "A Learning-Based Approach..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓ (OOPSLA 2024)  arXiv: N/A
  引用位置: [related_work.tex:16] ✓ — learned program slicing
  问题: 无

[yang2024generalization] Yang(2024) "Unveiling the Generalization..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓ (NAACL 2024)  arXiv: ✓ (2403.09162)
  引用位置: [related_work.tex:52] ✓ — fine-tuned LLMs generalize better on concise inputs
  引用位置: [appendix.tex:655] ✓ — VOTA instability confounds
  问题: 无

[yang2024sweagent] Yang(2024) "SWE-agent: Agent-Computer..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓ (NeurIPS 2024)  arXiv: ✓ (2405.15793)
  引用位置: [related_work.tex:20] ✓ — agent-based repair
  问题: 无

[zhong2024ldb] Zhong(2024) "LDB: A Large Language..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✗  Venue: ✓ (Findings ACL 2024)  arXiv: N/A
  引用位置: [related_work.tex:21] ✓ — segment-level trace verification for debugging
  问题: ⚠️ 标题不完整。Bib标题为 "LDB: A Large Language Model Debugger via Verifying Runtime Execution Step by Step"，官方ACL Anthology标题为 "Debug like a Human: A Large Language Model Debugger via Verifying Runtime Execution Step by Step"，缺少 "Debug like a Human:" 前缀。

[zhou2024llm4patch] Zhou(2024) "Leveraging Large Language..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓ (IEEE TSE)  arXiv: N/A
  引用位置: [related_work.tex:17] ✓ — LLM4PatchCorrect (84.4%)
  问题: 无
```

## 汇总

```
总计：57 条
幻觉 (HALLUCINATED)：0 条
误引 (MISATTRIBUTION)：0 条
问题数：1 条

问题清单：
1. [zhong2024ldb] 标题不完整 — 缺少 "Debug like a Human:" 前缀
   Bib: "LDB: A Large Language Model Debugger via Verifying Runtime Execution Step by Step"
   正确: "Debug like a Human: A Large Language Model Debugger via Verifying Runtime Execution Step by Step"

次要注意事项（不影响正确性）：
- [ferrando2025execute] bib key "ferrando" 无对应作者（第一作者为 Armengol-Estapé），仅key命名问题
- [xu2025cruxevalx] 和 [spiess2025calibration] 使用 "and others" 替代完整作者列表（非常规但不算错）
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_audit_citation-verify-w1_20260526T101523"
}
```

</details>

---
