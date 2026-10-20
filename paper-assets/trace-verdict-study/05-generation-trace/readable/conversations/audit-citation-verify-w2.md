# audit citation verify w2

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 269
- **Recorded user turns:** 0
- **Tool calls:** 134
- **Original source:** `logs/chats/worker_audit_citation-verify-w2_20260526T101532.jsonl`
- **Structured JSON:** [`c4763a41a8567589574d.json`](../../sessions/c4/c4763a41a8567589574d.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

269 recorded events

### Tool call

_source line 1 · 2026-05-26T10:27:35.567352+00:00_

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
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-26T10:27:35.567838+00:00_

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
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-26T10:27:35.568029+00:00_

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
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-26T10:27:35.568190+00:00_

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
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-26T10:27:35.568398+00:00_

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
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-26T10:27:35.568563+00:00_

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
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-26T10:27:35.568709+00:00_

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
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-26T10:27:35.568893+00:00_

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
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-26T10:27:35.569047+00:00_

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
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/discussion.tex"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-26T10:27:35.569240+00:00_

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
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-26T10:27:35.569397+00:00_

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
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-26T10:27:35.569558+00:00_

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
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-26T10:27:35.569697+00:00_

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
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-26T10:27:35.569851+00:00_

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
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-26T10:27:35.569996+00:00_

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
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-26T10:27:35.570121+00:00_

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
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-26T10:27:35.570259+00:00_

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
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/appendix.tex"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-26T10:27:35.570687+00:00_

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
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-26T10:27:35.570910+00:00_

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
  "session": "worker_audit_citation-verify-w2_20260526T101532",
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

_source line 20 · 2026-05-26T10:27:35.571045+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-26T10:27:35.571262+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

````json
{
  "description": "Verify bib entries group 1 (1-12)",
  "prompt": "You are verifying academic paper references for correctness. For each bib entry below, use WebSearch to search for the paper title (in quotes) and verify:\na) Paper exists (MOST IMPORTANT)\nb) Author names (first and last author spelling)\nc) Year\nd) Title accuracy\ne) Venue correctness\nf) arXiv ID if present\n\nAlso check that each citation is used correctly in context (I provide the citation contexts).\n\n## Entries to verify (Group 1, alphabetical):\n\n**1. abreu2007accuracy**\n```\ntitle={On the Accuracy of Spectrum-based Fault Localization},\nauthor={Rui Abreu and Peter Zoeteweij and Arjan J.C. van Gemund},\njournal={Testing: Academic and Industrial Conference Practice and Research Techniques (MUTATION)},\nyear={2007},\ndoi={10.1109/TAIC.PART.2007.13},\n```\nContext: related_work.tex line 19: \"Spectrum-based fault localization (SBFL) ranks program elements by suspiciousness from test spectra \\citep{abreu2007accuracy,jones2002visualization,wong2014dstar}\"\n\n**2. appt2024**\n```\ntitle={APPT: Boosting Automated Patch Correctness Prediction via Fine-tuning Pre-trained Models},\nauthor={Quanjun Zhang and Chunrong Fang and Weisong Sun and Yan Liu and Tieke He and Xiaodong Hao and Zhenyu Chen},\njournal={IEEE Transactions on Software Engineering},\nyear={2024}, volume={50}, number={3},\n```\nContext: related_work.tex line 17: \"APPT \\citep{appt2024} (79.7%)\"\n\n**3. austin2021program**\n```\ntitle={Program Synthesis with Large Language Models},\nauthor={Austin, Jacob and Odena, Augustus and Nye, Maxwell and Bosma, Maarten and Michalewski, Henryk and Dohan, David and Jiang, Ellen and Cai, Carrie and Terry, Michael and Le, Quoc and Sutton, Charles},\njournal={arXiv preprint arXiv:2108.07732},\nyear={2021},\nurl={https://arxiv.org/abs/2108.07732},\n```\nContext: introduction.tex line 14: \"MBPP-sanitized \\citep{austin2021program}\"\nContext: method.tex line 13: \"MBPP-sanitized \\citep{austin2021program}\"\n\n**4. barr2015oracle**\n```\ntitle={The Oracle Problem in Software Testing: A Survey},\nauthor={Earl T. Barr and Mark Harman and Phil McMinn and Muzammil Shahbaz and Shin Yoo},\njournal={IEEE Transactions on Software Engineering},\nvolume={41}, number={5}, pages={507--525}, year={2015},\ndoi={10.1109/TSE.2014.2372785},\n```\nContext: related_work.tex line 15: \"Verdict prediction is an instance of the longstanding test oracle problem \\citep{barr2015oracle}.\"\n\n**5. bengio2009curriculum**\n```\ntitle={Curriculum Learning},\nauthor={Yoshua Bengio and Jérôme Louradour and Ronan Collobert and Jason Weston},\nbooktitle={Proceedings of the 26th Annual International Conference on Machine Learning (ICML)},\npages={41--48}, year={2009},\ndoi={10.1145/1553374.1553380},\n```\nContext: related_work.tex line 51: \"Curriculum learning \\citep{bengio2009curriculum}\"\n\n**6. bouzenia2025repairagent**\n```\ntitle={RepairAgent: An Autonomous, LLM-Based Agent for Program Repair},\nauthor={Islem Bouzenia and Premkumar Devanbu and Michael Pradel},\nbooktitle={Proceedings of the 47th IEEE/ACM International Conference on Software Engineering (ICSE)},\nyear={2025},\ndoi={10.1109/ICSE55347.2025.00157},\n```\nContext: related_work.tex line 20: \"RepairAgent \\citep{bouzenia2025repairagent}...all incorporate execution feedback in repair workflows\"\n\n**7. chen2021evaluating**\n```\ntitle={Evaluating Large Language Models Trained on Code},\nauthor={Chen, Mark and Tworek, Jerry and Jun, Heewoo and Yuan, Qiming and ...},\njournal={arXiv preprint arXiv:2107.03374},\nyear={2021},\nurl={https://arxiv.org/abs/2107.03374},\n```\nContext: introduction.tex line 14: \"HumanEval \\citep{chen2021evaluating}\"\nContext: method.tex line 13: \"HumanEval \\citep{chen2021evaluating}\"\n\n**8. chen2024selfdebug**\n```\ntitle={Teaching Large Language Models to Self-Debug},\nauthor={Xinyun Chen and Maxwell Lin and Nathanael Schärli and Denny Zhou},\nbooktitle={Proceedings of the 12th International Conference on Learning Representations (ICLR)},\nyear={2024},\n```\nContext: related_work.tex line 21: \"SelfDebug \\citep{chen2024selfdebug}...iteratively refine code using execution outcomes\"\n\n**9. chen2025tracepile**\n```\ntitle={Chain of Execution Supervision Promotes General Reasoning in Large Language Models},\nauthor={Nuo Chen and Zehua Li and Keqin Bao and Junyang Lin and Dayiheng Liu},\nbooktitle={Advances in Neural Information Processing Systems (NeurIPS)},\nyear={2025},\nurl={https://arxiv.org/abs/2510.23629},\n```\nContext: introduction.tex line 4: \"Recent work has incorporated them into code language models...citep{chen2025tracepile,...}\"\nContext: related_work.tex line 5: \"TracePile \\citep{chen2025tracepile} pre-trained on 2.6M execution-annotated samples\"\nContext: method.tex line 7: \"Unlike code generation \\citep{chen2025tracepile}\"\n\n**10. deepseek2024coder**\n```\ntitle={DeepSeek-Coder: When the Large Language Model Meets Programming -- The Rise of Code Intelligence},\nauthor={Daya Guo and Qihao Zhu and Dejian Yang and Zhenda Xie and Kai Dong and Wentao Zhang and Guanting Chen and Xiao Bi and Y. Wu and Y.K. Li and Fuli Luo and Yingfei Xiong and Wenfeng Liang},\njournal={arXiv preprint arXiv:2401.14196},\nyear={2024},\nurl={https://arxiv.org/abs/2401.14196},\n```\nContext: introduction.tex line 14, method.tex line 32: cited as one of the model families used.\n\n**11. ding2024traced**\n```\ntitle={TRACED: Execution-aware Pre-training for Source Code},\nauthor={Yangruibo Ding and Ben Steenhoek and Kexin Pei and Gail Kaiser and Wei Le and Baishakhi Ray},\nbooktitle={Proceedings of the 46th IEEE/ACM International Conference on Software Engineering (ICSE)},\nyear={2024},\ndoi={10.1145/3597503.3608140},\nurl={https://arxiv.org/abs/2306.07487},\n```\nContext: introduction.tex line 4: cited for incorporating traces into code LMs\nContext: related_work.tex line 16: \"TRACED \\citep{ding2024traced} showed execution-aware pretraining improves vulnerability detection\"\n\n**12. eguchi2025etcot**\n```\ntitle={Making LLMs Program Interpreters via Execution Trace Chain of Thought},\nauthor={Koshi Eguchi and Takuya Akiba},\nbooktitle={ICML 2025 Workshop on Programmatic Representations for Agent Learning (PRAL)},\nyear={2025},\n```\nContext: related_work.tex line 7: \"ET-CoT \\citep{eguchi2025etcot} used trace chain-of-thought for execution reasoning\"\n\n## Output format for each entry:\n```\n[key] Author(year) \"First 5 words of title...\"\n  Exists: ✓/✗  Authors: ✓/✗  Year: ✓/✗  Title: ✓/✗  Venue: ✓/✗  arXiv: ✓/✗/N/A\n  Citation context: [file:line] ✓/✗ — [explanation]\n  Issues: [if any]\n```\n\nSearch for each paper title using WebSearch with quotes around the title. Report your findings thoroughly.\n"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "Agent",
  "tool_args": {
    "description": "Verify bib entries group 1 (1-12)",
    "prompt": "You are verifying academic paper references for correctness. For each bib entry below, use WebSearch to search for the paper title (in quotes) and verify:\na) Paper exists (MOST IMPORTANT)\nb) Author names (first and last author spelling)\nc) Year\nd) Title accuracy\ne) Venue correctness\nf) arXiv ID if present\n\nAlso check that each citation is used correctly in context (I provide the citation contexts).\n\n## Entries to verify (Group 1, alphabetical):\n\n**1. abreu2007accuracy**\n```\ntitle={On the Accuracy of Spectrum-based Fault Localization},\nauthor={Rui Abreu and Peter Zoeteweij and Arjan J.C. van Gemund},\njournal={Testing: Academic and Industrial Conference Practice and Research Techniques (MUTATION)},\nyear={2007},\ndoi={10.1109/TAIC.PART.2007.13},\n```\nContext: related_work.tex line 19: \"Spectrum-based fault localization (SBFL) ranks program elements by suspiciousness from test spectra \\citep{abreu2007accuracy,jones2002visualization,wong2014dstar}\"\n\n**2. appt2024**\n```\ntitle={APPT: Boosting Automated Patch Correctness Prediction via Fine-tuning Pre-trained Models},\nauthor={Quanjun Zhang and Chunrong Fang and Weisong Sun and Yan Liu and Tieke He and Xiaodong Hao and Zhenyu Chen},\njournal={IEEE Transactions on Software Engineering},\nyear={2024}, volume={50}, number={3},\n```\nContext: related_work.tex line 17: \"APPT \\citep{appt2024} (79.7%)\"\n\n**3. austin2021program**\n```\ntitle={Program Synthesis with Large Language Models},\nauthor={Austin, Jacob and Odena, Augustus and Nye, Maxwell and Bosma, Maarten and Michalewski, Henryk and Dohan, David and Jiang, Ellen and Cai, Carrie and Terry, Michael and Le, Quoc and Sutton, Charles},\njournal={arXiv preprint arXiv:2108.07732},\nyear={2021},\nurl={https://arxiv.org/abs/2108.07732},\n```\nContext: introduction.tex line 14: \"MBPP-sanitized \\citep{austin2021program}\"\nContext: method.tex line 13: \"MBPP-sanitized \\citep{austin2021program}\"\n\n**4. barr2015oracle**\n```\ntitle={The Oracle Problem in Software Testing: A Survey},\nauthor={Earl T. Barr and Mark Harman and Phil McMinn and Muzammil Shahbaz and Shin Yoo},\njournal={IEEE Transactions on Software Engineering},\nvolume={41}, number={5}, pages={507--525}, year={2015},\ndoi={10.1109/TSE.2014.2372785},\n```\nContext: related_work.tex line 15: \"Verdict prediction is an instance of the longstanding test oracle problem \\citep{barr2015oracle}.\"\n\n**5. bengio2009curriculum**\n```\ntitle={Curriculum Learning},\nauthor={Yoshua Bengio and Jérôme Louradour and Ronan Collobert and Jason Weston},\nbooktitle={Proceedings of the 26th Annual International Conference on Machine Learning (ICML)},\npages={41--48}, year={2009},\ndoi={10.1145/1553374.1553380},\n```\nContext: related_work.tex line 51: \"Curriculum learning \\citep{bengio2009curriculum}\"\n\n**6. bouzenia2025repairagent**\n```\ntitle={RepairAgent: An Autonomous, LLM-Based Agent for Program Repair},\nauthor={Islem Bouzenia and Premkumar Devanbu and Michael Pradel},\nbooktitle={Proceedings of the 47th IEEE/ACM International Conference on Software Engineering (ICSE)},\nyear={2025},\ndoi={10.1109/ICSE55347.2025.00157},\n```\nContext: related_work.tex line 20: \"RepairAgent \\citep{bouzenia2025repairagent}...all incorporate execution feedback in repair workflows\"\n\n**7. chen2021evaluating**\n```\ntitle={Evaluating Large Language Models Trained on Code},\nauthor={Chen, Mark and Tworek, Jerry and Jun, Heewoo and Yuan, Qiming and ...},\njournal={arXiv preprint arXiv:2107.03374},\nyear={2021},\nurl={https://arxiv.org/abs/2107.03374},\n```\nContext: introduction.tex line 14: \"HumanEval \\citep{chen2021evaluating}\"\nContext: method.tex line 13: \"HumanEval \\citep{chen2021evaluating}\"\n\n**8. chen2024selfdebug**\n```\ntitle={Teaching Large Language Models to Self-Debug},\nauthor={Xinyun Chen and Maxwell Lin and Nathanael Schärli and Denny Zhou},\nbooktitle={Proceedings of the 12th International Conference on Learning Representations (ICLR)},\nyear={2024},\n```\nContext: related_work.tex line 21: \"SelfDebug \\citep{chen2024selfdebug}...iteratively refine code using execution outcomes\"\n\n**9. chen2025tracepile**\n```\ntitle={Chain of Execution Supervision Promotes General Reasoning in Large Language Models},\nauthor={Nuo Chen and Zehua Li and Keqin Bao and Junyang Lin and Dayiheng Liu},\nbooktitle={Advances in Neural Information Processing Systems (NeurIPS)},\nyear={2025},\nurl={https://arxiv.org/abs/2510.23629},\n```\nContext: introduction.tex line 4: \"Recent work has incorporated them into code language models...citep{chen2025tracepile,...}\"\nContext: related_work.tex line 5: \"TracePile \\citep{chen2025tracepile} pre-trained on 2.6M execution-annotated samples\"\nContext: method.tex line 7: \"Unlike code generation \\citep{chen2025tracepile}\"\n\n**10. deepseek2024coder**\n```\ntitle={DeepSeek-Coder: When the Large Language Model Meets Programming -- The Rise of Code Intelligence},\nauthor={Daya Guo and Qihao Zhu and Dejian Yang and Zhenda Xie and Kai Dong and Wentao Zhang and Guanting Chen and Xiao Bi and Y. Wu and Y.K. Li and Fuli Luo and Yingfei Xiong and Wenfeng Liang},\njournal={arXiv preprint arXiv:2401.14196},\nyear={2024},\nurl={https://arxiv.org/abs/2401.14196},\n```\nContext: introduction.tex line 14, method.tex line 32: cited as one of the model families used.\n\n**11. ding2024traced**\n```\ntitle={TRACED: Execution-aware Pre-training for Source Code},\nauthor={Yangruibo Ding and Ben Steenhoek and Kexin Pei and Gail Kaiser and Wei Le and Baishakhi Ray},\nbooktitle={Proceedings of the 46th IEEE/ACM International Conference on Software Engineering (ICSE)},\nyear={2024},\ndoi={10.1145/3597503.3608140},\nurl={https://arxiv.org/abs/2306.07487},\n```\nContext: introduction.tex line 4: cited for incorporating traces into code LMs\nContext: related_work.tex line 16: \"TRACED \\citep{ding2024traced} showed execution-aware pretraining improves vulnerability detection\"\n\n**12. eguchi2025etcot**\n```\ntitle={Making LLMs Program Interpreters via Execution Trace Chain of Thought},\nauthor={Koshi Eguchi and Takuya Akiba},\nbooktitle={ICML 2025 Workshop on Programmatic Representations for Agent Learning (PRAL)},\nyear={2025},\n```\nContext: related_work.tex line 7: \"ET-CoT \\citep{eguchi2025etcot} used trace chain-of-thought for execution reasoning\"\n\n## Output format for each entry:\n```\n[key] Author(year) \"First 5 words of title...\"\n  Exists: ✓/✗  Authors: ✓/✗  Year: ✓/✗  Title: ✓/✗  Venue: ✓/✗  arXiv: ✓/✗/N/A\n  Citation context: [file:line] ✓/✗ — [explanation]\n  Issues: [if any]\n```\n\nSearch for each paper title using WebSearch with quotes around the title. Report your findings thoroughly.\n"
  }
}
````

</details>

---

### Tool call

_source line 22 · 2026-05-26T10:27:35.571592+00:00_

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
  "session": "worker_audit_citation-verify-w2_20260526T101532",
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

_source line 23 · 2026-05-26T10:27:35.571730+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-26T10:27:35.571851+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"On the Accuracy of Spectrum-based Fault Localization\" Abreu Zoeteweij"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"On the Accuracy of Spectrum-based Fault Localization\" Abreu Zoeteweij"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-26T10:27:35.571984+00:00_

Web search results for query: ""On the Accuracy of Spectrum-based Fault Localization" Abreu Zoeteweij"

Links: [{"title":"On the Accuracy of Spectrum-based Fault Localization∗ Rui Abreu Peter Zoeteweij","url":"https://scispace.com/pdf/on-the-accuracy-of-spectrum-based-fault-localization-13lhdnxj1f.pdf"},{"title":"[PDF] On the Accuracy of Spectrum-based Fault Localization | Semantic Scholar","url":"https://www.semanticscholar.org/paper/On-the-Accuracy-of-Spectrum-based-Fault-Abreu-Zoeteweij/eb956ab442810f783f44600ce6d714583a96a4aa"},{"title":"A practical evaluation of spectrum-based fault localization - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0164121209001319"},{"title":"On the Accuracy of Spectrum-based Fault Localization","url":"https://www.researchgate.net/publication/4279298_On_the_Accuracy_of_Spectrum-based_Fault_Localization"},{"title":"Spectrum-Based Fault Localization for Diagnosing Concurrency Faults | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-642-41707-8_16"},{"title":"Enhancing spectrum based fault localization via emphasizing its formulas with importance weight | Proceedings of the Third International Workshop on Automated Program Repair","url":"https://dl.acm.org/doi/10.1145/3524459.3527349"},{"title":"On the analysis of spectrum based fault localization using hitting sets - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0164121218302231"},{"title":"SBEST: Spectrum-based fault localization without fault-triggering tests | Empirical Software Engineering | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10664-025-10761-8"},{"title":"(PDF) Spectrum-based Fault Localization: A Pair Scoring Approach","url":"https://www.academia.edu/90993270/Spectrum_based_Fault_Localization_A_Pair_Scoring_Approach"}]

I found the research paper you're looking for. "On the Accuracy of Spectrum-based Fault Localization" is authored by Rui Abreu, Peter Zo
…[truncated 914 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-26T10:27:35.572124+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"APPT: Boosting Automated Patch Correctness Prediction via Fine-tuning Pre-trained Models\" Zhang Fang"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"APPT: Boosting Automated Patch Correctness Prediction via Fine-tuning Pre-trained Models\" Zhang Fang"
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-26T10:27:35.572275+00:00_

Web search results for query: ""APPT: Boosting Automated Patch Correctness Prediction via Fine-tuning Pre-trained Models" Zhang Fang"

Links: [{"title":"[2301.12453] APPT: Boosting Automated Patch Correctness Prediction via Fine-tuning Pre-trained Models","url":"https://arxiv.org/abs/2301.12453"},{"title":"APPT: Boosting Automated Patch Correctness Prediction via Fine-Tuning Pre-Trained Models | IEEE Journals & Magazine | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/10402095/"},{"title":"APPT Boosting Automated Patch Correctness Prediction via Fine-tuning Pre-trained Models","url":"https://www.scribd.com/document/874799956/APPT-Boosting-Automated-Patch-Correctness-Prediction-via-Fine-tuning-Pre-trained-Models"},{"title":"(PDF) Boosting Automated Patch Correctness Prediction via Pre-trained Language Model","url":"https://www.researchgate.net/publication/367558621_Boosting_Automated_Patch_Correctness_Prediction_via_Pre-trained_Language_Model"},{"title":"GitHub - iSEngLab/APPT: [TSE 2024] APPT: Boosting Automated Patch Correctness Prediction via Fine-tuning Pre-trained Models · GitHub","url":"https://github.com/iSEngLab/APPT"},{"title":"[PDF] A Survey of Learning-based Automated Program Repair | Semantic Scholar","url":"https://www.semanticscholar.org/paper/A-Survey-of-Learning-based-Automated-Program-Repair-Zhang-Fang/1bf36d887a4317e8a25377504b102fff6f70029f"},{"title":"Table 1 from A Survey of Learning-based Automated Program Repair | Semantic Scholar","url":"https://www.semanticscholar.org/paper/A-Survey-of-Learning-based-Automated-Program-Repair-Zhang-Fang/1bf36d887a4317e8a25377504b102fff6f70029f/figure/1"},{"title":"IEEE TRANSACTIONS ON SOFTWARE ENGINEERING, VOL. XXX, NO. XXX, XXX 2022 1","url":"https://openreview.net/attachment?id=FzXGX0s8q7&name=pdf"}]

Based on the search results, I found information about this research paper:

APPT is a pre-trained model-based automated patch correctness assessment technique by both pre-training and fine-tuning. Th
…[truncated 1185 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-26T10:27:35.572428+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Program Synthesis with Large Language Models\" Austin Odena Nye arXiv 2108.07732"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Program Synthesis with Large Language Models\" Austin Odena Nye arXiv 2108.07732"
  }
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-26T10:27:35.572586+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

````json
{
  "description": "Verify bib entries group 2 (13-23)",
  "prompt": "You are verifying academic paper references for correctness. For each bib entry below, use WebSearch to search for the paper title (in quotes) and verify:\na) Paper exists (MOST IMPORTANT)\nb) Author names (first and last author spelling)\nc) Year\nd) Title accuracy\ne) Venue correctness\nf) arXiv ID if present\n\nAlso check that each citation is used correctly in context (I provide the citation contexts).\n\n## Entries to verify (Group 2):\n\n**13. ferrando2025execute**\n```\ntitle={What I Cannot Execute, I Do Not Understand: Training and Evaluating LLMs on Program Execution Traces},\nauthor={Jordi Armengol-Estape and Quentin Carbonneaux and Tianjun Zhang and Aram H. Markosyan and Volker Seeker and Chris Cummins and Melanie Kambadur and Michael F.P. O'Boyle and Sida Wang and Gabriel Synnaeve and Hugh Leather},\njournal={arXiv preprint arXiv:2503.05703},\nyear={2025},\nurl={https://arxiv.org/abs/2503.05703},\n```\nContext: related_work.tex line 7: \"\\citet{ferrando2025execute} found compact traces comparable to full traces, consistent with our density finding.\"\n\n**14. foster2025mutation**\n```\ntitle={Mutation-Guided LLM-based Test Generation at Meta},\nauthor={Christopher Foster and Abhishek Gulati and Mark Harman and Inna Harper and Ke Mao and Jillian Ritchey and Hervé Robert and Shubho Sengupta},\nbooktitle={Proceedings of the ACM International Conference on the Foundations of Software Engineering (FSE), Industry Track},\nyear={2025},\nurl={https://arxiv.org/abs/2501.12862},\n```\nContext: related_work.tex line 18: \"\\citet{foster2025mutation} demonstrated that structured fault signals (stack traces, mutation outcomes) improve localization\"\n\n**15. geng2024calibration**\n```\ntitle={A Survey of Confidence Estimation and Calibration in Large Language Models},\nauthor={Jiahui Geng and Fengyu Cai and Yuxia Wang and Heinz Koeppl and Preslav Nakov and Iryna Gurevych},\nbooktitle={Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL)},\nyear={2024},\nurl={https://aclanthology.org/2024.naacl-long.366},\n```\nContext: related_work.tex line 48: \"extended to LLMs \\citep{kadavath2022language,geng2024calibration}\"\n\n**16. gu2024cruxeval**\n```\ntitle={CRUXEval: A Benchmark for Code Reasoning, Understanding and Execution},\nauthor={Alex Gu and Baptiste Rozière and Hugh Leather and Armando Solar-Lezama and Gabriel Synnaeve and Sida I. Wang},\nbooktitle={Proceedings of the 41st International Conference on Machine Learning (ICML)},\nyear={2024},\nurl={https://arxiv.org/abs/2401.03065},\n```\nContext: related_work.tex line 8: \"CRUXEval \\citep{gu2024cruxeval}...established execution reasoning benchmarks\"\nContext: method.tex line 7: \"output prediction \\citep{gu2024cruxeval}\"\n\n**17. guo2017calibration**\n```\ntitle={On Calibration of Modern Neural Networks},\nauthor={Chuan Guo and Geoff Pleiss and Yu Sun and Kilian Q. Weinberger},\nbooktitle={Proceedings of the 34th International Conference on Machine Learning (ICML)},\npages={1321--1330}, year={2017},\n```\nContext: related_work.tex line 48: \"Neural network calibration \\citep{guo2017calibration}\"\n\n**18. haque2025traces**\n```\ntitle={Towards Effectively Leveraging Execution Traces for Program Repair with Code LLMs},\nauthor={Mirazul Haque and Petr Babkin and Farima Farmahinifarahani and Manuela Veloso},\nbooktitle={KnowledgeNLP Workshop at ACL 2025},\nyear={2025},\nurl={https://arxiv.org/abs/2505.04441},\n```\nContext: related_work.tex line 10: \"\\citet{haque2025traces} found raw traces provide limited repair benefit.\"\n\n**19. hoang2019deepjit**\n```\ntitle={DeepJIT: An End-to-End Deep Learning Framework for Just-in-Time Defect Prediction},\nauthor={Thong Hoang and Hoa Khanh Dam and Yasutaka Kamei and David Lo and Naoyasu Ubayashi},\nbooktitle={Proceedings of the 16th International Conference on Mining Software Repositories (MSR)},\npages={34--45}, year={2019},\ndoi={10.1109/MSR.2019.00016},\n```\nContext: related_work.tex line 50: \"Just-in-time defect prediction \\citep{kamei2013large,hoang2019deepjit,pornprasit2021jitline}\"\n\n**20. hoang2020cc2vec**\n```\ntitle={CC2Vec: Distributed Representations of Code Changes},\nauthor={Thong Hoang and Hong Jin Kang and Julia Lawall and David Lo},\nbooktitle={Proceedings of the ACM/IEEE 42nd International Conference on Software Engineering (ICSE)},\npages={518--529}, year={2020},\ndoi={10.1145/3377811.3380361},\n```\nContext: related_work.tex line 17: \"representation learning of code changes has progressed from CC2Vec \\citep{hoang2020cc2vec} to LLM4PatchCorrect\"\n\n**21. hu2022lora**\n```\ntitle={LoRA: Low-Rank Adaptation of Large Language Models},\nauthor={Edward J. Hu and Yelong Shen and Phillip Wallis and Zeyuan Allen-Zhu and Yuanzhi Li and Shean Wang and Lu Wang and Weizhu Chen},\nbooktitle={Proceedings of the 10th International Conference on Learning Representations (ICLR)},\nyear={2022},\nurl={https://arxiv.org/abs/2106.09685},\n```\nContext: method.tex line 33: \"Low-Rank Adaptation (LoRA) \\citep{hu2022lora}\"\nContext: appendix.tex line 38: \"LoRA \\citep{hu2022lora} applied to all linear layers\"\n\n**22. huang2026tracecoder**\n```\ntitle={TraceCoder: A Trace-Driven Multi-Agent Framework for Automated Debugging of LLM-Generated Code},\nauthor={Jiangping Huang and Wenguang Ye and Weisong Sun and Jian Zhang and Mingyue Zhang and Yang Liu},\nbooktitle={Proceedings of the 48th IEEE/ACM International Conference on Software Engineering (ICSE)},\nyear={2026},\nurl={https://arxiv.org/abs/2602.06875},\n```\nContext: related_work.tex line 10: \"TraceCoder \\citep{huang2026tracecoder}...apply selective trace extraction for automated debugging\"\n\n**23. jiang2023llmlingua**\n```\ntitle={LLMLingua: Compressing Prompts for Accelerated Inference of Large Language Models},\nauthor={Huiqiang Jiang and Qianhui Wu and Chin-Yew Lin and Yuqing Yang and Lili Qiu},\nbooktitle={Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\npages={13358--13376}, year={2023},\nurl={https://aclanthology.org/2023.emnlp-main.825},\n```\nContext: related_work.tex line 10: \"LLMLingua \\citep{jiang2023llmlingua}\"\nContext: discussion.tex line 66: \"LLMLingua \\citep{jiang2023llmlingua}...showed that pruning low-information tokens preserves downstream accuracy\"\n\n## Output format for each entry:\n```\n[key] Author(year) \"First 5 words of title...\"\n  Exists: ✓/✗  Authors: ✓/✗  Year: ✓/✗  Title: ✓/✗  Venue: ✓/✗  arXiv: ✓/✗/N/A\n  Citation context: [file:line] ✓/✗ — [explanation]\n  Issues: [if any]\n```\n\nSearch for each paper title using WebSearch with quotes around the title. Report your findings thoroughly.\n"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "Agent",
  "tool_args": {
    "description": "Verify bib entries group 2 (13-23)",
    "prompt": "You are verifying academic paper references for correctness. For each bib entry below, use WebSearch to search for the paper title (in quotes) and verify:\na) Paper exists (MOST IMPORTANT)\nb) Author names (first and last author spelling)\nc) Year\nd) Title accuracy\ne) Venue correctness\nf) arXiv ID if present\n\nAlso check that each citation is used correctly in context (I provide the citation contexts).\n\n## Entries to verify (Group 2):\n\n**13. ferrando2025execute**\n```\ntitle={What I Cannot Execute, I Do Not Understand: Training and Evaluating LLMs on Program Execution Traces},\nauthor={Jordi Armengol-Estape and Quentin Carbonneaux and Tianjun Zhang and Aram H. Markosyan and Volker Seeker and Chris Cummins and Melanie Kambadur and Michael F.P. O'Boyle and Sida Wang and Gabriel Synnaeve and Hugh Leather},\njournal={arXiv preprint arXiv:2503.05703},\nyear={2025},\nurl={https://arxiv.org/abs/2503.05703},\n```\nContext: related_work.tex line 7: \"\\citet{ferrando2025execute} found compact traces comparable to full traces, consistent with our density finding.\"\n\n**14. foster2025mutation**\n```\ntitle={Mutation-Guided LLM-based Test Generation at Meta},\nauthor={Christopher Foster and Abhishek Gulati and Mark Harman and Inna Harper and Ke Mao and Jillian Ritchey and Hervé Robert and Shubho Sengupta},\nbooktitle={Proceedings of the ACM International Conference on the Foundations of Software Engineering (FSE), Industry Track},\nyear={2025},\nurl={https://arxiv.org/abs/2501.12862},\n```\nContext: related_work.tex line 18: \"\\citet{foster2025mutation} demonstrated that structured fault signals (stack traces, mutation outcomes) improve localization\"\n\n**15. geng2024calibration**\n```\ntitle={A Survey of Confidence Estimation and Calibration in Large Language Models},\nauthor={Jiahui Geng and Fengyu Cai and Yuxia Wang and Heinz Koeppl and Preslav Nakov and Iryna Gurevych},\nbooktitle={Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL)},\nyear={2024},\nurl={https://aclanthology.org/2024.naacl-long.366},\n```\nContext: related_work.tex line 48: \"extended to LLMs \\citep{kadavath2022language,geng2024calibration}\"\n\n**16. gu2024cruxeval**\n```\ntitle={CRUXEval: A Benchmark for Code Reasoning, Understanding and Execution},\nauthor={Alex Gu and Baptiste Rozière and Hugh Leather and Armando Solar-Lezama and Gabriel Synnaeve and Sida I. Wang},\nbooktitle={Proceedings of the 41st International Conference on Machine Learning (ICML)},\nyear={2024},\nurl={https://arxiv.org/abs/2401.03065},\n```\nContext: related_work.tex line 8: \"CRUXEval \\citep{gu2024cruxeval}...established execution reasoning benchmarks\"\nContext: method.tex line 7: \"output prediction \\citep{gu2024cruxeval}\"\n\n**17. guo2017calibration**\n```\ntitle={On Calibration of Modern Neural Networks},\nauthor={Chuan Guo and Geoff Pleiss and Yu Sun and Kilian Q. Weinberger},\nbooktitle={Proceedings of the 34th International Conference on Machine Learning (ICML)},\npages={1321--1330}, year={2017},\n```\nContext: related_work.tex line 48: \"Neural network calibration \\citep{guo2017calibration}\"\n\n**18. haque2025traces**\n```\ntitle={Towards Effectively Leveraging Execution Traces for Program Repair with Code LLMs},\nauthor={Mirazul Haque and Petr Babkin and Farima Farmahinifarahani and Manuela Veloso},\nbooktitle={KnowledgeNLP Workshop at ACL 2025},\nyear={2025},\nurl={https://arxiv.org/abs/2505.04441},\n```\nContext: related_work.tex line 10: \"\\citet{haque2025traces} found raw traces provide limited repair benefit.\"\n\n**19. hoang2019deepjit**\n```\ntitle={DeepJIT: An End-to-End Deep Learning Framework for Just-in-Time Defect Prediction},\nauthor={Thong Hoang and Hoa Khanh Dam and Yasutaka Kamei and David Lo and Naoyasu Ubayashi},\nbooktitle={Proceedings of the 16th International Conference on Mining Software Repositories (MSR)},\npages={34--45}, year={2019},\ndoi={10.1109/MSR.2019.00016},\n```\nContext: related_work.tex line 50: \"Just-in-time defect prediction \\citep{kamei2013large,hoang2019deepjit,pornprasit2021jitline}\"\n\n**20. hoang2020cc2vec**\n```\ntitle={CC2Vec: Distributed Representations of Code Changes},\nauthor={Thong Hoang and Hong Jin Kang and Julia Lawall and David Lo},\nbooktitle={Proceedings of the ACM/IEEE 42nd International Conference on Software Engineering (ICSE)},\npages={518--529}, year={2020},\ndoi={10.1145/3377811.3380361},\n```\nContext: related_work.tex line 17: \"representation learning of code changes has progressed from CC2Vec \\citep{hoang2020cc2vec} to LLM4PatchCorrect\"\n\n**21. hu2022lora**\n```\ntitle={LoRA: Low-Rank Adaptation of Large Language Models},\nauthor={Edward J. Hu and Yelong Shen and Phillip Wallis and Zeyuan Allen-Zhu and Yuanzhi Li and Shean Wang and Lu Wang and Weizhu Chen},\nbooktitle={Proceedings of the 10th International Conference on Learning Representations (ICLR)},\nyear={2022},\nurl={https://arxiv.org/abs/2106.09685},\n```\nContext: method.tex line 33: \"Low-Rank Adaptation (LoRA) \\citep{hu2022lora}\"\nContext: appendix.tex line 38: \"LoRA \\citep{hu2022lora} applied to all linear layers\"\n\n**22. huang2026tracecoder**\n```\ntitle={TraceCoder: A Trace-Driven Multi-Agent Framework for Automated Debugging of LLM-Generated Code},\nauthor={Jiangping Huang and Wenguang Ye and Weisong Sun and Jian Zhang and Mingyue Zhang and Yang Liu},\nbooktitle={Proceedings of the 48th IEEE/ACM International Conference on Software Engineering (ICSE)},\nyear={2026},\nurl={https://arxiv.org/abs/2602.06875},\n```\nContext: related_work.tex line 10: \"TraceCoder \\citep{huang2026tracecoder}...apply selective trace extraction for automated debugging\"\n\n**23. jiang2023llmlingua**\n```\ntitle={LLMLingua: Compressing Prompts for Accelerated Inference of Large Language Models},\nauthor={Huiqiang Jiang and Qianhui Wu and Chin-Yew Lin and Yuqing Yang and Lili Qiu},\nbooktitle={Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\npages={13358--13376}, year={2023},\nurl={https://aclanthology.org/2023.emnlp-main.825},\n```\nContext: related_work.tex line 10: \"LLMLingua \\citep{jiang2023llmlingua}\"\nContext: discussion.tex line 66: \"LLMLingua \\citep{jiang2023llmlingua}...showed that pruning low-information tokens preserves downstream accuracy\"\n\n## Output format for each entry:\n```\n[key] Author(year) \"First 5 words of title...\"\n  Exists: ✓/✗  Authors: ✓/✗  Year: ✓/✗  Title: ✓/✗  Venue: ✓/✗  arXiv: ✓/✗/N/A\n  Citation context: [file:line] ✓/✗ — [explanation]\n  Issues: [if any]\n```\n\nSearch for each paper title using WebSearch with quotes around the title. Report your findings thoroughly.\n"
  }
}
````

</details>

---

### Tool result

_source line 30 · 2026-05-26T10:27:35.572973+00:00_

Web search results for query: ""Program Synthesis with Large Language Models" Austin Odena Nye arXiv 2108.07732"

Links: [{"title":"[2108.07732] Program Synthesis with Large Language Models","url":"https://arxiv.org/abs/2108.07732"},{"title":"Program Synthesis with Large Language Models Jacob Austin* Augustus Odena*","url":"https://arxiv.org/pdf/2108.07732"},{"title":"[PDF] Program Synthesis with Large Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Program-Synthesis-with-Large-Language-Models-Austin-Odena/a38e0f993e4805ba8a9beae4c275c91ffcec01df"},{"title":"Paper page - Program Synthesis with Large Language Models","url":"https://huggingface.co/papers/2108.07732"},{"title":"Program Synthesis with Large Language Models","url":"https://www.researchgate.net/publication/353970323_Program_Synthesis_with_Large_Language_Models"},{"title":"[2108.07732v1] Program Synthesis with Large Language Models","url":"https://arxiv.org/abs/2108.07732v1"},{"title":"Google Scholar","url":"https://scholar.google.com/scholar?q=Jacob+Austin%2C+Augustus+Odena%2C+Maxwell+Nye%2C+Maarten+Bosma%2C+Henryk+Michalewski%2C+David+Dohan%2C+Ellen+Jiang%2C+Carrie+Cai%2C+Michael+Terry%2C+Quoc+Le%2C+and+Charles+Sutton.+2021.+Program+Synthesis+with+Large+Language+Models.+arXiv%3A2108.07732+%5Bcs.PL%5D"},{"title":"Program Synthesis with Large Language Models","url":"https://www.summarizepaper.com/en/arxiv-id/2108.07732v1/"},{"title":"dblp: Program Synthesis with Large Language Models.","url":"https://dblp.org/rec/journals/corr/abs-2108-07732.html"},{"title":"Program Synthesis with Large Language Models - ADS","url":"https://ui.adsabs.harvard.edu/abs/2021arXiv210807732A/abstract"}]

I found the paper you're looking for. Here are the key details:

**Paper Title:** Program Synthesis with Large Language Models

**Authors:** Jacob Austin, Augustus Odena, Maxwell Nye, Maarten Bosma, Henryk Michalewski, David Dohan, Ellen Jiang, Carrie Cai, Michael Terry, Quoc Le, Charles Sutton


…[truncated 814 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-26T10:27:35.573132+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"The Oracle Problem in Software Testing: A Survey\" Barr Harman McMinn"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"The Oracle Problem in Software Testing: A Survey\" Barr Harman McMinn"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-26T10:27:35.573292+00:00_

Web search results for query: ""The Oracle Problem in Software Testing: A Survey" Barr Harman McMinn"

Links: [{"title":"[PDF] The Oracle Problem in Software Testing: A Survey | Semantic Scholar","url":"https://www.semanticscholar.org/paper/The-Oracle-Problem-in-Software-Testing:-A-Survey-Barr-Harman/0e17ab6c9d31a481c641f2b1760e09ea51ab76cc"},{"title":"(PDF) The Oracle Problem in Software Testing: A Survey","url":"https://www.researchgate.net/publication/276255185_The_Oracle_Problem_in_Software_Testing_A_Survey"},{"title":"The Oracle Problem in Software Testing: A Survey | IEEE Transactions on Software Engineering","url":"https://dl.acm.org/doi/10.1109/TSE.2014.2372785"},{"title":"(PDF) The Oracle Problem in Software Testing: A Survey","url":"https://www.academia.edu/24870121/The_Oracle_Problem_in_Software_Testing_A_Survey"},{"title":"1 The Oracle Problem in Software Testing: A Survey","url":"http://www0.cs.ucl.ac.uk/staff/m.harman/tse-oracle.pdf"},{"title":"The oracle problem in software testing: A survey - Korea Advanced Institute of Science and Technology","url":"https://pure.kaist.ac.kr/en/publications/the-oracle-problem-in-software-testing-a-survey/"},{"title":"The Oracle Problem in Software Testing: A Survey","url":"https://discovery.ucl.ac.uk/id/eprint/1471263/1/06963470.pdf"},{"title":"Figure 1 from The Oracle Problem in Software Testing: A Survey | Semantic Scholar","url":"https://www.semanticscholar.org/paper/The-Oracle-Problem-in-Software-Testing:-A-Survey-Barr-Harman/0e17ab6c9d31a481c641f2b1760e09ea51ab76cc/figure/0"},{"title":"DSpace at KOASAS: The Oracle Problem in Software Testing: A Survey","url":"https://koasas.kaist.ac.kr/handle/10203/204028"}]

I found comprehensive information about the paper "The Oracle Problem in Software Testing: A Survey" by Barr, Harman, and McMinn.

## Paper Details

The paper was published in IEEE Transactions on Software Engineering in 2015, volume 41, pages 507-525, by authors Earl T. Barr, Mark Harman, Phil McMinn, Muza
…[truncated 986 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-26T10:27:35.573445+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Curriculum Learning\" Bengio Louradour Collobert Weston ICML 2009"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Curriculum Learning\" Bengio Louradour Collobert Weston ICML 2009"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-26T10:27:35.573576+00:00_

Web search results for query: ""Curriculum Learning" Bengio Louradour Collobert Weston ICML 2009"

Links: [{"title":"Curriculum learning","url":"https://bibbase.org/network/publication/bengio-louradour-collobert-weston-curriculumlearning-2009"},{"title":"Curriculum learning | Proceedings of the 26th Annual International Conference on Machine Learning","url":"https://dl.acm.org/doi/10.1145/1553374.1553380"},{"title":"Curriculum Learning - Ronan Collobert","url":"https://ronan.collobert.com/pub/2009_curriculum_icml.pdf"},{"title":"[PDF] Curriculum learning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Curriculum-learning-Bengio-Louradour/8de174ab5419b9d3127695405efd079808e956e8"},{"title":"dblp: Curriculum learning.","url":"https://dblp.org/rec/conf/icml/BengioLCW09.html"},{"title":"Bengio, 2009 Curriculum Learning.pdf","url":"https://www.scribd.com/document/425393423/Bengio-2009-Curriculum-Learning-pdf"},{"title":"(PDF) Curriculum learning","url":"https://www.academia.edu/58928901/Curriculum_learning"},{"title":"Google Scholar","url":"https://scholar.google.com/scholar?q=Bengio%2C+Y.%2C+Louradour%2C+J.%2C+Collobert%2C+R.%2C+Weston%2C+J.%3A+Curriculum+learning.+In%3A+International+Conference+on+Machine+Learning+%28ICML%29+%282009%29"},{"title":"(PDF) Curriculum learning","url":"https://www.researchgate.net/publication/221344862_Curriculum_learning"},{"title":"ICML 2009","url":"https://icml.cc/Conferences/2009/abstracts.html"}]

## Search Results for "Curriculum Learning" Bengio et al. ICML 2009

I found comprehensive information about this influential paper. Here are the key details:

### Publication Details
The paper "Curriculum Learning" was authored by Bengio, Y., Louradour, J., Collobert, R., & Weston, J. and published in the Proceedings of the 26th Annual International Conference on Machine Learning (ICML '09) in Montreal, Quebec, Canada, 2009.

### Core Concept
The paper is based on the observation that humans and animals learn much better whe
…[truncated 1022 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-26T10:27:35.573718+00:00_

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
  "session": "worker_audit_citation-verify-w2_20260526T101532",
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

_source line 36 · 2026-05-26T10:27:35.573832+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-26T10:27:35.573943+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"What I Cannot Execute, I Do Not Understand: Training and Evaluating LLMs on Program Execution Traces\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"What I Cannot Execute, I Do Not Understand: Training and Evaluating LLMs on Program Execution Traces\""
  }
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-26T10:27:35.574054+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Mutation-Guided LLM-based Test Generation at Meta\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Mutation-Guided LLM-based Test Generation at Meta\""
  }
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-26T10:27:35.574164+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"A Survey of Confidence Estimation and Calibration in Large Language Models\" Geng"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"A Survey of Confidence Estimation and Calibration in Large Language Models\" Geng"
  }
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-26T10:27:35.574296+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"CRUXEval: A Benchmark for Code Reasoning, Understanding and Execution\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"CRUXEval: A Benchmark for Code Reasoning, Understanding and Execution\""
  }
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-26T10:27:35.574409+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"On Calibration of Modern Neural Networks\" Guo Pleiss Weinberger ICML 2017"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"On Calibration of Modern Neural Networks\" Guo Pleiss Weinberger ICML 2017"
  }
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-26T10:27:35.574517+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Towards Effectively Leveraging Execution Traces for Program Repair with Code LLMs\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Towards Effectively Leveraging Execution Traces for Program Repair with Code LLMs\""
  }
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-26T10:27:35.574638+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"DeepJIT: An End-to-End Deep Learning Framework for Just-in-Time Defect Prediction\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"DeepJIT: An End-to-End Deep Learning Framework for Just-in-Time Defect Prediction\""
  }
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-26T10:27:35.574804+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"CC2Vec: Distributed Representations of Code Changes\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"CC2Vec: Distributed Representations of Code Changes\""
  }
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-26T10:27:35.574978+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"LoRA: Low-Rank Adaptation of Large Language Models\" Hu Shen Wallis"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"LoRA: Low-Rank Adaptation of Large Language Models\" Hu Shen Wallis"
  }
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-26T10:27:35.575144+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"TraceCoder: A Trace-Driven Multi-Agent Framework for Automated Debugging of LLM-Generated Code\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"TraceCoder: A Trace-Driven Multi-Agent Framework for Automated Debugging of LLM-Generated Code\""
  }
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-26T10:27:35.575428+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"LLMLingua: Compressing Prompts for Accelerated Inference of Large Language Models\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"LLMLingua: Compressing Prompts for Accelerated Inference of Large Language Models\""
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-26T10:27:35.575629+00:00_

Web search results for query: ""Mutation-Guided LLM-based Test Generation at Meta""

Links: [{"title":"[2501.12862] Mutation-Guided LLM-based Test Generation at Meta","url":"https://arxiv.org/abs/2501.12862"},{"title":"Mutation-Guided LLM-based Test Generation at Meta | Proceedings of the 33rd ACM International Conference on the Foundations of Software Engineering","url":"https://dl.acm.org/doi/10.1145/3696630.3728544"},{"title":"Mutation-Guided LLM-based Test Generation at Meta (FSE 2025 - Industry Papers) - FSE 2025","url":"https://conf.researchr.org/details/fse-2025/fse-2025-industry-papers/16/Mutation-Guided-LLM-based-Test-Generation-at-Meta"},{"title":"Mutation-Guided LLM-based Test Generation at Meta","url":"https://arxiv.org/html/2501.12862v1"},{"title":"[Literature Review] Mutation-Guided LLM-based Test Generation at Meta","url":"https://www.themoonlight.io/en/review/mutation-guided-llm-based-test-generation-at-meta"},{"title":"(PDF) Mutation-Guided LLM-based Test Generation at Meta","url":"https://www.researchgate.net/publication/388317879_Mutation-Guided_LLM-based_Test_Generation_at_Meta"},{"title":"Paper page - Mutation-Guided LLM-based Test Generation at Meta","url":"https://huggingface.co/papers/2501.12862"},{"title":"Mutation-Guided LLM-based Test Generation at Meta - Paper Bytes | iHeart","url":"https://www.iheart.com/podcast/1333-paper-bytes-263964530/episode/mutation-guided-llm-based-test-generation-at-meta-265789478/"}]

Based on the search results, here's what I found about "Mutation-Guided LLM-based Test Generation at Meta":

This paper describes Meta's ACH system for mutation-guided LLM-based test generation. ACH stands for Automated Compliance Hardening.

**Key Features:**

ACH generates relatively few mutants (simulated faults) compared to traditional mutation testing, instead focusing on generating currently undetected faults that are specific to an issue of concern. From these currently uncaught faults, ACH generates tests that can catch the
…[truncated 786 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-26T10:27:35.575868+00:00_

Web search results for query: ""On Calibration of Modern Neural Networks" Guo Pleiss Weinberger ICML 2017"

Links: [{"title":"[1706.04599] On Calibration of Modern Neural Networks","url":"https://arxiv.org/abs/1706.04599"},{"title":"On Calibration of Modern Neural Networks","url":"https://proceedings.mlr.press/v70/guo17a/guo17a.pdf"},{"title":"On calibration of modern neural networks | Proceedings of the 34th International Conference on Machine Learning - Volume 70","url":"https://dl.acm.org/doi/10.5555/3305381.3305518"},{"title":"On Calibration of Modern Neural Networks Chuan Guo Kilian Q. Weinberger","url":"https://fernandoperezc.github.io/Advanced-Topics-in-Machine-Learning-and-Data-Science/Fluri.pdf"},{"title":"[PDF] On Calibration of Modern Neural Networks | Semantic Scholar","url":"https://www.semanticscholar.org/paper/On-Calibration-of-Modern-Neural-Networks-Guo-Pleiss/d65ce2b8300541414bfe51d03906fca72e93523c"},{"title":"Guo, C., Pleiss, G., Sun Y. and Weinberger, K.Q. (2017）On Calibration of Modern Neural Networks. Proceedings of the 34th International Conference on Machine Learning, Sydney, Vol. 70, 1321-1330. - References - Scientific Research Publishing","url":"https://www.scirp.org/(S(czeh4tfqyw2orz553k1w0r45))/reference/referencespapers?referenceid=3648829"},{"title":"Guo, C., Pleiss, G., Sun, Y. and Weinberger, K.Q. (2017) On Calibration of Modern Neural Networks. Proceedings of the 34th International Conference on Machine Learning, PMLR, Vol. 70, 1321-1330. - References - Scientific Research Publishing","url":"https://www.scirp.org/reference/referencespapers?referenceid=3534546"},{"title":"On Calibration of Modern Neural Networks | Request PDF","url":"https://www.researchgate.net/publication/317591245_On_Calibration_of_Modern_Neural_Networks"},{"title":"On Calibration of Modern Neural Networks","url":"https://github.com/vlgiitr/papers_we_read/blob/master/summaries/Calibration_of_Neural_Nets.md"},{"title":"Neural Network Calibration","url":"https://geo
…[truncated 1310 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-26T10:27:35.576100+00:00_

Web search results for query: ""CC2Vec: Distributed Representations of Code Changes""

Links: [{"title":"[2003.05620] CC2Vec: Distributed Representations of Code Changes","url":"https://arxiv.org/abs/2003.05620"},{"title":"CC2Vec: distributed representations of code changes","url":"https://dl.acm.org/doi/10.1145/3377811.3380361"},{"title":"GitHub - soarsmu/CC2Vec: Artifact website for the paper, CC2Vec: Distributed Representations of Code Changes","url":"https://github.com/soarsmu/CC2Vec"},{"title":"CC2Vec: Distributed Representations of Code Changes","url":"https://arxiv.org/pdf/2003.05620"},{"title":"[PDF] CC2Vec: Distributed Representations of Code Changes | Semantic Scholar","url":"https://www.semanticscholar.org/paper/CC2Vec:-Distributed-Representations-of-Code-Changes-Hoang-Kang/0dfe706526e5234338411489e1826b4060acc4e8"},{"title":"CC2Vec: Distributed Representations of Code Changes | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/9284081"},{"title":"CC2Vec: Distributed representations of code changes","url":"https://ink.library.smu.edu.sg/context/sis_research/article/6503/viewcontent/3377811.3380361.pdf"},{"title":"CC2Vec: Distributed Representations of Code Changes (ICSE 2020 - Technical Papers) - ICSE 2020","url":"https://2020.icse-conferences.org/details/icse-2020-papers/10/CC2Vec-Distributed-Representations-of-Code-Changes"}]

Based on the search results, here's what I found about CC2Vec:

CC2Vec is a neural network model that learns a representation of code changes guided by their accompanying log messages, which represent the semantic intent of the code changes.

**Key Technical Features:**

CC2Vec models the hierarchical structure of a code change with the help of the attention mechanism and uses multiple comparison functions to identify the differences between the removed and added code.

**Motivation:**

Existing work on software patches often use features specific to a single task and often rely on manually ide
…[truncated 731 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-26T10:27:35.576347+00:00_

Web search results for query: ""Towards Effectively Leveraging Execution Traces for Program Repair with Code LLMs""

Links: [{"title":"[2505.04441] Towards Effectively Leveraging Execution Traces for Program Repair with Code LLMs","url":"https://arxiv.org/abs/2505.04441"},{"title":"Towards Effectively Leveraging Execution Traces for Program Repair with Code LLMs","url":"https://arxiv.org/html/2505.04441v1"},{"title":"Towards Effectively Leveraging Execution Traces for ...","url":"https://aclanthology.org/2025.knowledgenlp-1.17.pdf"},{"title":"Debugging Code World Models","url":"https://arxiv.org/html/2602.07672v2"},{"title":"Bug Fixing with Broader Context: Enhancing LLM-Based Program Repair via Layered Knowledge Injection","url":"https://arxiv.org/html/2506.24015v1"},{"title":"Towards Effectively Leveraging Execution Traces","url":"https://arxiv.org/pdf/2505.04441"},{"title":"NExT: LLMs with Code Execution Reasoning","url":"https://www.emergentmind.com/papers/2404.14662"},{"title":"Petr Babkin's research works | Palo Alto Research Center and other places","url":"https://www.researchgate.net/scientific-contributions/Petr-Babkin-2224003926"}]

I found the paper! Here's what I found about "Towards Effectively Leveraging Execution Traces for Program Repair with Code LLMs":

## Overview

This paper was authored by Mirazul Haque, Petr Babkin, Farima Farmahinifarahani, and Manuela Veloso from J. P. Morgan AI Research. They evaluated their approach using the GPT family of models on three popular APR datasets.

## Main Focus

Most approaches to LLM-based Automatic Program Repair (APR) are limited to the static analysis of the programs while disregarding their runtime behavior, and the authors aimed to remedy this by augmenting standard APR prompts with program execution traces.

## Key Findings

The findings suggest that simply incorporating execution traces into the prompt provides a limited performance improvement over trace-free baselines, in only 2 out of 6 tested datas
…[truncated 687 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-26T10:27:35.576580+00:00_

Web search results for query: ""What I Cannot Execute, I Do Not Understand: Training and Evaluating LLMs on Program Execution Traces""

Links: [{"title":"[2503.05703] What I cannot execute, I do not understand: Training and Evaluating LLMs on Program Execution Traces","url":"https://arxiv.org/abs/2503.05703"},{"title":"What I cannot execute, I do not understand: Training and Evaluating LLMs on Program Execution Traces","url":"https://arxiv.org/html/2503.05703v1"},{"title":"LLMs versus the Halting Problem: Revisiting Program Termination Prediction","url":"https://arxiv.org/html/2601.18987v3"},{"title":"Making LLMs Program Interpreters via Execution Trace Chain of Thought","url":"https://openreview.net/pdf?id=pFyBdPyOCQ"},{"title":"Towards Effectively Leveraging Execution Traces for Program Repair with Code LLMs","url":"https://arxiv.org/html/2505.04441"},{"title":"Why LLMs Can Explain Algorithms They Cannot Execute | by Zheng Zhang | Medium","url":"https://medium.com/@zzhang_29583/why-llms-can-explain-algorithms-they-cannot-execute-46d60d0546c2"}]

Based on the search results, here's what I found about the paper "What I Cannot Execute, I Do Not Understand: Training and Evaluating LLMs on Program Execution Traces":

## Paper Overview

This paper by Jordi Armengol-Estapé and 10 other authors addresses code generation and understanding capabilities for large language models. 

## Main Contribution

The paper studies Execution Tuning (E.T.), a training procedure that explicitly models real-world program execution traces without requiring manual test annotations. The work addresses the issue that standard code datasets typically treat code as static strings and rarely exploit the dynamic information about their execution.

## Methodology and Results

The researchers trained and evaluated models on different execution trace granularities (line and instruction-level) on the task of output prediction, obtaining around 80% accuracy on CruxEval and MBPP, and demonstrated the a
…[truncated 252 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-26T10:27:35.576795+00:00_

Web search results for query: ""A Survey of Confidence Estimation and Calibration in Large Language Models" Geng"

Links: [{"title":"[2311.08298] A Survey of Confidence Estimation and Calibration in Large Language Models","url":"https://arxiv.org/abs/2311.08298"},{"title":"A Survey of Confidence Estimation and Calibration in Large Language Models - ACL Anthology","url":"https://aclanthology.org/2024.naacl-long.366/"},{"title":"[PDF] A Survey of Confidence Estimation and Calibration in Large Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/A-Survey-of-Confidence-Estimation-and-Calibration-Geng-Cai/6aa6003c7d7b3d275ae981aa6200014968c32430"},{"title":"A Survey of Confidence Estimation and Calibration in Large Language Models","url":"https://www.researchgate.net/publication/382633391_A_Survey_of_Confidence_Estimation_and_Calibration_in_Large_Language_Models"},{"title":"A Survey of Confidence Estimation and Calibration in Large Language Models | alphaXiv","url":"https://www.alphaxiv.org/overview/2311.08298v2"},{"title":"[2311.08298v2] A Survey of Confidence Estimation and Calibration in Large Language Models","url":"https://arxiv.org/abs/2311.08298v2"},{"title":"A Survey of Confidence Estimation and Calibration in Large Language Models","url":"https://arxiv.org/html/2311.08298v2"},{"title":"A Survey of Confidence Estimation and Calibration ...","url":"https://lingo.iitgn.ac.in/nlpexplorer/paper/2024.naacl-long.366"}]

I found the survey paper you were looking for. Here are the key details:

**Title:** A Survey of Confidence Estimation and Calibration in Large Language Models

**Authors:** Jiahui Geng, Fengyu Cai, Yuxia Wang, Heinz Koeppl, Preslav Nakov, and Iryna Gurevych

**Publication:** Published in the Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL) in June 2024 in Mexico City

**Overview:** Despite their impressive performance, Large Language Models can be unrel
…[truncated 738 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-26T10:27:35.577015+00:00_

Web search results for query: ""LoRA: Low-Rank Adaptation of Large Language Models" Hu Shen Wallis"

Links: [{"title":"[2106.09685] LoRA: Low-Rank Adaptation of Large Language Models","url":"https://arxiv.org/abs/2106.09685"},{"title":"[PDF] LoRA: Low-Rank Adaptation of Large Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/LoRA:-Low-Rank-Adaptation-of-Large-Language-Models-Hu-Shen/a8ca46b171467ceb2d7652fbfb67fe701ad86092"},{"title":"LORA: LOW-RANK ADAPTATION OF LARGE LAN","url":"https://openreview.net/pdf?id=nZeVKeeFYf9"},{"title":"GitHub - microsoft/LoRA: Code for loralib, an implementation of \"LoRA: Low-Rank Adaptation of Large Language Models\" · GitHub","url":"https://github.com/microsoft/LoRA"},{"title":"LORA: LOW-RANK ADAPTATION OF LARGE LAN- GUAGE MODELS Edward Hu∗ Yelong Shen∗","url":"https://arxiv.org/pdf/2106.09685"},{"title":"LoRA: Low-Rank Adaptation of Large Language Models Edward Hu∗ Yelong Shen∗","url":"https://arxiv.org/pdf/2106.09685v1/1000"},{"title":"LoRA: Low-Rank Adaptation of Large Language Models | BibSonomy","url":"https://www.bibsonomy.org/bibtex/5fa57783e2dbd09410e0ddfbdf0efce7"},{"title":"LoRA: Low-Rank Adaptation of Large Language Models","url":"https://www.byhand.ai/p/lora-low-rank-adaptation-of-large"},{"title":"LoRA: Low-Rank Adaptation of Large Language Models - Microsoft Research","url":"https://www.microsoft.com/en-us/research/publication/lora-low-rank-adaptation-of-large-language-models/"}]

I found the paper you're looking for! Here are the key details:

**Paper:** LoRA: Low-Rank Adaptation of Large Language Models by Edward J. Hu, Yelong Shen, Phillip Wallis, Zeyuan Allen-Zhu, Yuanzhi Li, Shean Wang, Lu Wang, and Weizhu Chen

**Main Contribution:** The paper proposes Low-Rank Adaptation (LoRA), which freezes the pre-trained model weights and injects trainable rank decomposition matrices into each layer of the Transformer architecture, greatly reducing the number of trainable parameters for downst
…[truncated 660 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 55 · 2026-05-26T10:27:35.577253+00:00_

Web search results for query: ""CRUXEval: A Benchmark for Code Reasoning, Understanding and Execution""

Links: [{"title":"[2401.03065] CRUXEval: A Benchmark for Code Reasoning, Understanding and Execution","url":"https://arxiv.org/abs/2401.03065"},{"title":"CRUXEval: Code Reasoning, Understanding, and Execution Evaluation","url":"https://crux-eval.github.io/"},{"title":"CRUXEval: a benchmark for code reasoning ...","url":"https://dl.acm.org/doi/10.5555/3692070.3692729"},{"title":"GitHub - facebookresearch/cruxeval: CRUXEval: Code Reasoning, Understanding, and Execution Evaluation · GitHub","url":"https://github.com/facebookresearch/cruxeval"},{"title":"CRUXEval: A Benchmark for Code Reasoning, Understanding and Execution","url":"https://proceedings.mlr.press/v235/gu24c.html"},{"title":"CRUXEval: A Benchmark for Code Reasoning, Understanding and Execution Alex Gu⋆","url":"https://arxiv.org/pdf/2401.03065"},{"title":"[2408.13001] CRUXEval-X: A Benchmark for Multilingual Code Reasoning, Understanding and Execution","url":"https://arxiv.org/abs/2408.13001"},{"title":"CRUXEval: A Benchmark for Code Reasoning, Understanding and Execution","url":"https://openreview.net/pdf?id=S33IFOa8Yl"},{"title":"CRUXEval: A Benchmark for Code Reasoning, Understanding and Execution | OpenReview","url":"https://openreview.net/forum?id=Ffpg52swvg"},{"title":"[PDF] CRUXEval: A Benchmark for Code Reasoning, Understanding and Execution | Semantic Scholar","url":"https://www.semanticscholar.org/paper/CRUXEval:-A-Benchmark-for-Code-Reasoning,-and-Gu-Rozi%C3%A8re/4701914bc77dedef9e0a001687277103fb3ddfc6"}]

Based on the search results, here's what I found about CRUXEval:

CRUXEval (Code Reasoning, Understanding, and eXecution Evaluation) is a benchmark consisting of 800 Python functions (3-13 lines), with each function coming with an input-output pair that leads to two natural tasks: input prediction and output prediction.

The benchmark was designed to better evaluate the code reasoning aspect
…[truncated 898 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-26T10:27:35.577494+00:00_

Web search results for query: ""LLMLingua: Compressing Prompts for Accelerated Inference of Large Language Models""

Links: [{"title":"[2310.05736] LLMLingua: Compressing Prompts for Accelerated Inference of Large Language Models","url":"https://arxiv.org/abs/2310.05736"},{"title":"LLMLingua: Compressing Prompts for Accelerated Inference of Large Language Models","url":"https://llmlingua.com/llmlingua.html"},{"title":"LLMLingua: Compressing Prompts for Accelerated Inference of Large Language Models - ACL Anthology","url":"https://aclanthology.org/2023.emnlp-main.825/"},{"title":"LLMLingua: Compressing Prompts for Accelerated Inference of Large Language Models","url":"https://arxiv.org/html/2310.05736v2"},{"title":"LLMLingua: Compressing Prompts for Accelerated Inference of Large Language Models - Microsoft Research","url":"https://www.microsoft.com/en-us/research/publication/llmlingua-compressing-prompts-for-accelerated-inference-of-large-language-models/"},{"title":"LLMLingua: Compressing Prompts for Accelerated Inference of Large Language Models - Summary","url":"https://portkey.ai/blog/llmlingua-compressing-prompts-for-accelerated-inference-of-large-language-models-summary/"}]

I found comprehensive information about LLMLingua. Here's what the search results show:

## Overview

LLMLingua is a coarse-to-fine prompt compression method that involves a budget controller to maintain semantic integrity under high compression ratios, a token-level iterative compression algorithm to better model the interdependence between compressed contents, and an instruction tuning based method for distribution alignment between language models.

## Problem It Addresses

With advancements in technologies such as chain-of-thought (CoT) prompting and in-context learning (ICL), the prompts fed to LLMs are becoming increasingly lengthy, even exceeding tens of thousands of tokens. LLMLingua was developed to accelerate model inference and reduce costs in this context.

## Key Components

T
…[truncated 627 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 57 · 2026-05-26T10:27:35.577734+00:00_

Web search results for query: ""TraceCoder: A Trace-Driven Multi-Agent Framework for Automated Debugging of LLM-Generated Code""

Links: [{"title":"[2602.06875] TraceCoder: A Trace-Driven Multi-Agent Framework for Automated Debugging of LLM-Generated Code","url":"https://arxiv.org/abs/2602.06875"},{"title":"TraceCoder: A Trace-Driven Multi-Agent Framework for Automated Debugging of LLM-Generated Code","url":"https://arxiv.org/html/2602.06875"},{"title":"TraceCoder: A Trace-Driven Multi-Agent Framework for Automated Debugging of LLM-Generated Code (ICSE 2026 - Research Track) - ICSE 2026","url":"https://conf.researchr.org/details/icse-2026/icse-2026-research-track/145/TraceCoder-A-Trace-Driven-Multi-Agent-Framework-for-Automated-Debugging-of-LLM-Gener"},{"title":"Envisioning Intelligent Requirements Engineering via Knowledge-Guided Multi-Agent Collaboration | Request PDF","url":"https://www.researchgate.net/publication/400199860_Envisioning_Intelligent_Requirements_Engineering_via_Knowledge-Guided_Multi-Agent_Collaboration"},{"title":"Trace-Based Diagnostics","url":"https://www.emergentmind.com/topics/trace-based-diagnostics"},{"title":"LLM-Based Agentic Systems for Software Engineering:","url":"https://arxiv.org/pdf/2601.09822"},{"title":"Best LLM tracing tools for multi-agent systems (2026 review) - Articles - Braintrust","url":"https://www.braintrust.dev/articles/best-llm-tracing-tools-2026"},{"title":"Trae Agent: LLM-Based Automated Code Issue Resolution","url":"https://www.emergentmind.com/topics/trae-agent"},{"title":"Token-Level Execution Traces: Debugging LLM Agents by Inspecting Their Stepwise Computational Graphs | by Pablo jusue | Medium","url":"https://medium.com/@pablojusue/token-level-execution-traces-debugging-llm-agents-by-inspecting-their-stepwise-computational-c14beef0dfba"}]

I found several results about TraceCoder. Here's what the research reveals:

## Overview

TraceCoder is a collaborative multi-agent framework that emulates the observe-analyze
…[truncated 1407 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-26T10:27:35.577973+00:00_

Web search results for query: ""DeepJIT: An End-to-End Deep Learning Framework for Just-in-Time Defect Prediction""

Links: [{"title":"DeepJIT: An End-to-End Deep Learning Framework for Just-in-Time Defect Prediction | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/abstract/document/8816772/"},{"title":"[PDF] DeepJIT: An End-to-End Deep Learning Framework for Just-in-Time Defect Prediction | Semantic Scholar","url":"https://www.semanticscholar.org/paper/DeepJIT:-An-End-to-End-Deep-Learning-Framework-for-Hoang-Dam/952fe2400f4b1a33fa45aa1aefaa856235e13c0c"},{"title":"DeepJIT: an end-to-end deep learning framework for just-in ...","url":"https://ink.library.smu.edu.sg/cgi/viewcontent.cgi?article=5489&context=sis_research"},{"title":"DeepJIT: An End-to-End Deep Learning Framework for Just-in-Time Defect Prediction | Request PDF","url":"https://www.researchgate.net/publication/335498581_DeepJIT_An_End-to-End_Deep_Learning_Framework_for_Just-in-Time_Defect_Prediction"},{"title":"DeepJIT: an end-to-end deep learning framework for just-in ...","url":"https://dl.acm.org/doi/10.1109/msr.2019.00016"},{"title":"[PDF] Deep Learning for Just-in-Time Defect Prediction | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Deep-Learning-for-Just-in-Time-Defect-Prediction-Yang-Lo/e4be4ba1d428bc89f63662ae7b0db097fa83d651"},{"title":"DeepJIT: an end-to-end deep learning framework for just-in-time defect prediction - CORE Reader","url":"https://core.ac.uk/reader/275589720"},{"title":"(PDF) JIT-CF: Integrating contrastive learning with feature fusion for enhanced just-in-time defect prediction","url":"https://www.academia.edu/128114529/JIT_CF_Integrating_contrastive_learning_with_feature_fusion_for_enhanced_just_in_time_defect_prediction"}]

Based on the search results, here's what I found about DeepJIT:

## Overview

DeepJIT is an end-to-end deep learning framework that automatically extracts features from commit messages and code changes and us
…[truncated 1133 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-26T10:27:35.578193+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2503.05703 \"Jordi Armengol-Estape\" authors Meta FAIR"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2503.05703 \"Jordi Armengol-Estape\" authors Meta FAIR"
  }
}
```

</details>

---

### Tool call

_source line 60 · 2026-05-26T10:27:35.578388+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Mutation-Guided LLM-based Test Generation at Meta\" FSE 2025 authors \"Christopher Foster\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Mutation-Guided LLM-based Test Generation at Meta\" FSE 2025 authors \"Christopher Foster\""
  }
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-26T10:27:35.578520+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Towards Effectively Leveraging Execution Traces\" \"KnowledgeNLP\" ACL 2025 workshop venue"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Towards Effectively Leveraging Execution Traces\" \"KnowledgeNLP\" ACL 2025 workshop venue"
  }
}
```

</details>

---

### Tool call

_source line 62 · 2026-05-26T10:27:35.578643+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CRUXEval ICML 2024 \"Alex Gu\" \"Baptiste Rozière\" authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CRUXEval ICML 2024 \"Alex Gu\" \"Baptiste Rozière\" authors"
  }
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-26T10:27:35.578764+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "TraceCoder ICSE 2026 \"Jiangping Huang\" authors list"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "tool_args": {
    "query": "TraceCoder ICSE 2026 \"Jiangping Huang\" authors list"
  }
}
```

</details>

---

### Tool call

_source line 64 · 2026-05-26T10:27:35.578996+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CC2Vec ICSE 2020 \"Thong Hoang\" \"Hong Jin Kang\" \"Julia Lawall\" \"David Lo\" authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CC2Vec ICSE 2020 \"Thong Hoang\" \"Hong Jin Kang\" \"Julia Lawall\" \"David Lo\" authors"
  }
}
```

</details>

---

### Tool result

_source line 65 · 2026-05-26T10:27:35.579175+00:00_

Web search results for query: "CRUXEval ICML 2024 "Alex Gu" "Baptiste Rozière" authors"

Links: [{"title":"Alex Gu - CRUXEval: Code Reasoning, Understanding, and Execution Evaluation","url":"https://icml.cc/media/icml-2024/Slides/34526.pdf"},{"title":"CRUXEval: A Benchmark for Code Reasoning, Understanding and Execution | ML Anthology","url":"https://mlanthology.org/icml/2024/gu2024icml-cruxeval/"},{"title":"dblp: Baptiste Rozière","url":"https://dblp.org/pid/178/8263.html"},{"title":"CRUXEval: A Benchmark for Code Reasoning, Understanding and Execution","url":"https://bibbase.org/network/publication/gu-rozire-leather-solarlezama-synnaeve-wang-cruxevalabenchmarkforcodereasoningunderstandingandexecution-2024"},{"title":"CRUXEval: A Benchmark for Code Reasoning, Understanding and Execution","url":"https://proceedings.mlr.press/v235/gu24c.html"},{"title":"ICLR CRUXEval: A Benchmark for Code Reasoning, Understanding and Execution","url":"https://iclr.cc/virtual/2024/22440"},{"title":"CRUXEval | Proceedings of the 41st International Conference on Machine Learning","url":"https://dl.acm.org/doi/10.5555/3692070.3692729"},{"title":"[PDF] CRUXEval: A Benchmark for Code Reasoning, Understanding and Execution | Semantic Scholar","url":"https://www.semanticscholar.org/paper/CRUXEval:-A-Benchmark-for-Code-Reasoning,-and-Gu-Rozi%C3%A8re/4701914bc77dedef9e0a001687277103fb3ddfc6"},{"title":"GitHub - facebookresearch/cruxeval: CRUXEval: Code Reasoning, Understanding, and Execution Evaluation · GitHub","url":"https://github.com/facebookresearch/cruxeval"},{"title":"[2401.03065] CRUXEval: A Benchmark for Code Reasoning, Understanding and Execution","url":"https://arxiv.org/abs/2401.03065"}]

Based on the search results, I found information about the CRUXEval paper presented at ICML 2024:

The authors of CRUXEval at ICML 2024 are Alex Gu, Baptiste Rozière, Hugh James Leather, Armando Solar-Lezama, Gabriel Synnaeve, and Sida Wang.

CRUXEval is a benchmark consisting of 800 Python functi
…[truncated 243 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-26T10:27:35.579676+00:00_

Web search results for query: "arxiv 2503.05703 "Jordi Armengol-Estape" authors Meta FAIR"

Links: [{"title":"What I cannot execute, I do not understand: Training and Evaluating LLMs on Program Execution Traces","url":"https://arxiv.org/html/2503.05703"},{"title":"[2503.05703] What I cannot execute, I do not understand: Training and Evaluating LLMs on Program Execution Traces","url":"https://arxiv.org/abs/2503.05703"},{"title":"Jordi Armengol-Estapé","url":"https://scholar.google.com/citations?user=CiHoJfcAAAAJ&hl=en"},{"title":"Jordi Armengol-Estape - Research Scientist, FAIR @ Meta","url":"https://uk.linkedin.com/in/jordiae"},{"title":"dblp: Jordi Armengol-Estapé","url":"https://dblp.org/pid/263/2700.html"},{"title":"Machine Learning Mar 2025","url":"https://www.arxiv.org/list/cs.LG/2025-03?skip=500&show=2000"},{"title":"Jordi Armengol - Estape","url":"https://aclanthology.org/people/jordi-armengol-estape/"},{"title":"Jordi Armengol-Estapé","url":"https://openreview.net/profile?id=~Jordi_Armengol-Estap%C3%A91"}]

Based on the search results, here's information about arxiv paper 2503.05703:

**Title:** "What I cannot execute, I do not understand: Training and Evaluating LLMs on Program Execution Traces"

**Authors:** Jordi Armengol-Estapé, Quentin Carbonneaux, Tianjun Zhang, Aram H. Markosyan, Volker Seeker, Chris Cummins, Melanie Kambadur, Michael F.P. O'Boyle, Sida Wang, Gabriel Synnaeve, and Hugh James Leather

**Affiliations:** One author is from University of Edinburgh, while others are from Meta AI, with work done while interning at FAIR, Meta AI

**Main Contribution:** The paper studies Execution Tuning (E.T.), a training procedure in which they explicitly model real-world program execution traces without requiring manual test annotations

**Results:** They trained and evaluated models on different execution trace granularities (line and instruction-level) and strategies on the task of output prediction, obtaining around 80% accuracy on CruxEval and MBPP, an
…[truncated 187 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 67 · 2026-05-26T10:27:35.579931+00:00_

Web search results for query: ""Mutation-Guided LLM-based Test Generation at Meta" FSE 2025 authors "Christopher Foster""

Links: [{"title":"Mutation-Guided LLM-based Test Generation at Meta (FSE 2025 - Industry Papers) - FSE 2025","url":"https://conf.researchr.org/details/fse-2025/fse-2025-industry-papers/16/Mutation-Guided-LLM-based-Test-Generation-at-Meta"},{"title":"Mutation-Guided LLM-based Test Generation at Meta | Proceedings of the 33rd ACM International Conference on the Foundations of Software Engineering","url":"https://dl.acm.org/doi/10.1145/3696630.3728544"},{"title":"Mutation-Guided LLM-based Test Generation at Meta Christopher Foster","url":"https://arxiv.org/pdf/2501.12862"},{"title":"[2501.12862] Mutation-Guided LLM-based Test Generation at Meta","url":"https://arxiv.org/abs/2501.12862"},{"title":"Paper page - Mutation-Guided LLM-based Test Generation at Meta","url":"https://huggingface.co/papers/2501.12862"},{"title":"Mutation-Guided LLM-based Test Generation at Meta - UCL Discovery","url":"https://discovery.ucl.ac.uk/id/eprint/10218052/"},{"title":"Mutation-Guided LLM-based Test Generation at Meta","url":"https://arxiv.org/html/2501.12862v1"}]

Based on the search results, I found comprehensive information about this paper:

## Paper Overview

"Mutation-Guided LLM-based Test Generation at Meta" describes Meta's ACH (Automated Compliance Hardening) system for mutation-guided LLM-based test generation.

## Authors

The authors are Christopher Foster, Abhishek Gulati, Mark Harman, Inna Harper, Ke Mao, Jillian Ritchey, Hervé Robert, and Shubho Sengupta.

## Key Contributions

ACH generates relatively few mutants (simulated faults) compared to traditional mutation testing, and instead focuses on generating currently undetected faults that are specific to an issue of concern. From these uncaught faults, ACH generates tests that can catch them, thereby 'killing' the mutants and consequently hardening the platform against regressions.

## Results

ACH was
…[truncated 537 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-26T10:27:35.580360+00:00_

Web search results for query: "CC2Vec ICSE 2020 "Thong Hoang" "Hong Jin Kang" "Julia Lawall" "David Lo" authors"

Links: [{"title":"CC2Vec: Distributed Representations of Code Changes (ICSE 2020 - Technical Papers) - ICSE 2020","url":"https://conf.researchr.org/details/icse-2020/icse-2020-papers/10/CC2Vec-Distributed-Representations-of-Code-Changes"},{"title":"[PDF] CC2Vec: Distributed Representations of Code Changes | Semantic Scholar","url":"https://www.semanticscholar.org/paper/CC2Vec:-Distributed-Representations-of-Code-Changes-Hoang-Kang/0dfe706526e5234338411489e1826b4060acc4e8"},{"title":"Publications | Thong Hoang (James)","url":"https://hvdthong.github.io/publications/"},{"title":"Julia Lawall","url":"https://who.paris.inria.fr/Julia.Lawall/"},{"title":"CC2Vec: distributed representations of code changes | Request PDF","url":"https://www.researchgate.net/publication/346022771_CC2Vec_distributed_representations_of_code_changes"},{"title":"CC2Vec: Distributed Representations of Code Changes","url":"https://arxiv.org/pdf/2003.05620"},{"title":"Pretrained models and data for CC2Vec","url":"https://zenodo.org/records/3965149"},{"title":"dblp: BibTeX records: Julia Lawall","url":"https://dblp.org/pid/l/JuliaLLawall.html?view=bibtex&param=0"},{"title":"CC2Vec | Proceedings of the ACM/IEEE 42nd International Conference on Software Engineering","url":"https://dl.acm.org/doi/10.1145/3377811.3380361"}]

I found the paper! Here are the results:

CC2Vec was published at ICSE 2020 with authors Thong Hoang, Hong Jin Kang, Julia Lawall, and David Lo.

CC2Vec is a neural network model that learns the representation of code changes guided by their accompanying log messages, which represent the semantic intent of the code changes. The paper was published in the 2020 IEEE/ACM 42nd International Conference on Software Engineering (ICSE), pages 518-529.

The paper has been well-received, with 147 citations and highly influential citations status according to Semantic Scholar.


R
…[truncated 99 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-26T10:27:35.580556+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

````json
{
  "description": "Verify bib entries group 3 (24-34)",
  "prompt": "You are verifying academic paper references for correctness. For each bib entry below, use WebSearch to search for the paper title (in quotes) and verify:\na) Paper exists (MOST IMPORTANT)\nb) Author names (first and last author spelling)\nc) Year\nd) Title accuracy\ne) Venue correctness\nf) arXiv ID if present\n\nAlso check that each citation is used correctly in context (I provide the citation contexts).\n\n## Entries to verify (Group 3):\n\n**24. jimenez2024swebench**\n```\ntitle={SWE-bench: Can Language Models Resolve Real-World GitHub Issues?},\nauthor={Carlos E. Jimenez and John Yang and Alexander Wettig and Shunyu Yao and Kexin Pei and Ofir Press and Karthik R. Narasimhan},\nbooktitle={Proceedings of the 12th International Conference on Learning Representations (ICLR)},\nyear={2024},\nurl={https://openreview.net/forum?id=VTF8yNQM66},\n```\nContext: related_work.tex line 20: \"in the SWE-bench ecosystem \\citep{jimenez2024swebench}, these agents rely on test verdict signals to guide patch selection\"\n\n**25. jones2002visualization**\n```\ntitle={Visualization of Test Information to Assist Fault Localization},\nauthor={James A. Jones and Mary Jean Harrold and John Stasko},\nbooktitle={Proceedings of the 24th International Conference on Software Engineering (ICSE)},\nyear={2002},\ndoi={10.1145/581339.581397},\n```\nContext: related_work.tex line 19: \"SBFL ranks program elements by suspiciousness from test spectra \\citep{abreu2007accuracy,jones2002visualization,wong2014dstar}\"\n\n**26. kadavath2022language**\n```\ntitle={Language Models (Mostly) Know What They Know},\nauthor={Saurav Kadavath and Tom Conerly and Amanda Askell and Tom Henighan and Dawn Drain and Ethan Perez and Nicholas Schiefer and Zac Hatfield-Dodds and Nova DasSarma and Eli Tran-Johnson and Scott Johnston and Sheer El-Showk and Andy Jones and Nelson Elhage and Tristan Hume and Anna Chen and Yuntao Bai and Sam Bowman and Stanislav Fort and Deep Ganguli and Danny Hernandez and Josh Jacobson and Jackson Kernion and Shauna Kravec and Liane Lovitt and Kamal Ndousse and Catherine Olsson and Sam Ringer and Dario Amodei and Tom Brown and Jack Clark and Nicholas Joseph and Ben Mann and Sam McCandlish and Chris Olah and Jared Kaplan},\njournal={arXiv preprint arXiv:2207.05221},\nyear={2022},\n```\nContext: related_work.tex line 48: \"extended to LLMs \\citep{kadavath2022language,geng2024calibration}\"\n\n**27. kamei2013large**\n```\ntitle={A Large-Scale Empirical Study of Just-in-Time Quality Assurance},\nauthor={Yasutaka Kamei and Emad Shihab and Bram Adams and Ahmed E. Hassan and Audris Mockus and Anand Sinha and Naoyasu Ubayashi},\njournal={IEEE Transactions on Software Engineering},\nvolume={39}, number={6}, pages={757--773}, year={2013},\ndoi={10.1109/TSE.2012.70},\n```\nContext: related_work.tex line 50: \"Just-in-time defect prediction \\citep{kamei2013large,hoang2019deepjit,pornprasit2021jitline}\"\n\n**28. kang2024autofl**\n```\ntitle={A Quantitative and Qualitative Evaluation of LLM-Based Explainable Fault Localization},\nauthor={Sungmin Kang and Gabin An and Shin Yoo},\nbooktitle={Proceedings of the ACM on Software Engineering (FSE)},\nyear={2024},\ndoi={10.1145/3660771},\nurl={https://arxiv.org/abs/2308.05487},\n```\nContext: related_work.tex line 19: \"recent LLM-based approaches such as AutoFL \\citep{kang2024autofl} and AgentFL \\citep{qin2024agentfl} share our insight that anomalous execution events carry the strongest diagnostic signal.\"\n\n**29. li2023selectivecontext**\n```\ntitle={Compressing Context to Enhance Inference Efficiency of Large Language Models},\nauthor={Yucheng Li and Bo Dong and Frank Guerin and Chenghua Lin},\nbooktitle={Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\nyear={2023},\nurl={https://aclanthology.org/2023.emnlp-main.391},\n```\nContext: related_work.tex line 10: \"Selective Context \\citep{li2023selectivecontext}\"\nContext: discussion.tex line 66: \"Selective Context \\citep{li2023selectivecontext} showed that pruning low-information tokens preserves downstream accuracy\"\n\n**30. liu2023codeexecution**\n```\ntitle={Code Execution with Pre-trained Language Models},\nauthor={Chenxiao Liu and Shuai Lu and Weizhu Chen and Daxin Jiang and Alexey Svyatkovskiy and Shengyu Fu and Neel Sundaresan and Nan Duan},\nbooktitle={Findings of the Association for Computational Linguistics: ACL 2023},\npages={4984--4999}, year={2023},\ndoi={10.18653/v1/2023.findings-acl.308},\n```\nContext: related_work.tex line 5: \"\\citet{liu2023codeexecution} pre-trained models to predict execution outputs from traces.\"\n\n**31. ni2024next**\n```\ntitle={NExT: Teaching Large Language Models to Reason about Code Execution},\nauthor={Ansong Ni and Miltiadis Allamanis and Arman Cohan and Yinlin Deng and Kensen Shi and Charles Sutton and Pengcheng Yin},\nbooktitle={Proceedings of the 41st International Conference on Machine Learning (ICML)},\nyear={2024},\nurl={https://arxiv.org/abs/2404.14662},\n```\nContext: introduction.tex line 4: \"citep{...ni2024next}\"\nContext: related_work.tex line 7: \"NExT \\citep{ni2024next}...used trace chain-of-thought for execution reasoning\"\n\n**32. papadakis2019mutation**\n```\ntitle={Mutation Testing Advances: An Analysis and Survey},\nauthor={Mike Papadakis and Marinos Kintis and Jie Zhang and Yue Jia and Yves Le Traon and Mark Harman},\njournal={Advances in Computers},\nvolume={112}, pages={275--378}, year={2019},\ndoi={10.1016/bs.adcom.2018.03.015},\n```\nContext: related_work.tex line 18: \"the equivalent-mutant problem \\citep{papadakis2019mutation} poses an analogous classification challenge\"\n\n**33. pornprasit2021jitline**\n```\ntitle={JITLine: A Simpler, Better, Faster, Finer-grained Just-In-Time Defect Prediction},\nauthor={Chanathip Pornprasit and Chakkrit Tantithamthavorn},\nbooktitle={Proceedings of the 18th International Conference on Mining Software Repositories (MSR)},\npages={369--379}, year={2021},\ndoi={10.1109/MSR52588.2021.00049},\n```\nContext: related_work.tex line 50: \"Just-in-time defect prediction \\citep{kamei2013large,hoang2019deepjit,pornprasit2021jitline}\"\n\n**34. qin2024agentfl**\n```\ntitle={AgentFL: Scaling LLM-based Fault Localization to Project-Level Context},\nauthor={Yihao Qin and Shangwen Wang and Yiling Lou and Jinhao Dong and Kaixin Wang and Xiaoling Li and Xiaoguang Mao},\nbooktitle={Proceedings of the 39th IEEE/ACM International Conference on Automated Software Engineering (ASE)},\nyear={2024},\nurl={https://arxiv.org/abs/2403.16362},\n```\nContext: related_work.tex line 19: \"AgentFL \\citep{qin2024agentfl} share our insight that anomalous execution events carry the strongest diagnostic signal.\"\n\n## Output format for each entry:\n```\n[key] Author(year) \"First 5 words of title...\"\n  Exists: ✓/✗  Authors: ✓/✗  Year: ✓/✗  Title: ✓/✗  Venue: ✓/✗  arXiv: ✓/✗/N/A\n  Citation context: [file:line] ✓/✗ — [explanation]\n  Issues: [if any]\n```\n\nSearch for each paper title using WebSearch with quotes around the title. Report your findings thoroughly.\n"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "Agent",
  "tool_args": {
    "description": "Verify bib entries group 3 (24-34)",
    "prompt": "You are verifying academic paper references for correctness. For each bib entry below, use WebSearch to search for the paper title (in quotes) and verify:\na) Paper exists (MOST IMPORTANT)\nb) Author names (first and last author spelling)\nc) Year\nd) Title accuracy\ne) Venue correctness\nf) arXiv ID if present\n\nAlso check that each citation is used correctly in context (I provide the citation contexts).\n\n## Entries to verify (Group 3):\n\n**24. jimenez2024swebench**\n```\ntitle={SWE-bench: Can Language Models Resolve Real-World GitHub Issues?},\nauthor={Carlos E. Jimenez and John Yang and Alexander Wettig and Shunyu Yao and Kexin Pei and Ofir Press and Karthik R. Narasimhan},\nbooktitle={Proceedings of the 12th International Conference on Learning Representations (ICLR)},\nyear={2024},\nurl={https://openreview.net/forum?id=VTF8yNQM66},\n```\nContext: related_work.tex line 20: \"in the SWE-bench ecosystem \\citep{jimenez2024swebench}, these agents rely on test verdict signals to guide patch selection\"\n\n**25. jones2002visualization**\n```\ntitle={Visualization of Test Information to Assist Fault Localization},\nauthor={James A. Jones and Mary Jean Harrold and John Stasko},\nbooktitle={Proceedings of the 24th International Conference on Software Engineering (ICSE)},\nyear={2002},\ndoi={10.1145/581339.581397},\n```\nContext: related_work.tex line 19: \"SBFL ranks program elements by suspiciousness from test spectra \\citep{abreu2007accuracy,jones2002visualization,wong2014dstar}\"\n\n**26. kadavath2022language**\n```\ntitle={Language Models (Mostly) Know What They Know},\nauthor={Saurav Kadavath and Tom Conerly and Amanda Askell and Tom Henighan and Dawn Drain and Ethan Perez and Nicholas Schiefer and Zac Hatfield-Dodds and Nova DasSarma and Eli Tran-Johnson and Scott Johnston and Sheer El-Showk and Andy Jones and Nelson Elhage and Tristan Hume and Anna Chen and Yuntao Bai and Sam Bowman and Stanislav Fort and Deep Ganguli and Danny Hernandez and Josh Jacobson and Jackson Kernion and Shauna Kravec and Liane Lovitt and Kamal Ndousse and Catherine Olsson and Sam Ringer and Dario Amodei and Tom Brown and Jack Clark and Nicholas Joseph and Ben Mann and Sam McCandlish and Chris Olah and Jared Kaplan},\njournal={arXiv preprint arXiv:2207.05221},\nyear={2022},\n```\nContext: related_work.tex line 48: \"extended to LLMs \\citep{kadavath2022language,geng2024calibration}\"\n\n**27. kamei2013large**\n```\ntitle={A Large-Scale Empirical Study of Just-in-Time Quality Assurance},\nauthor={Yasutaka Kamei and Emad Shihab and Bram Adams and Ahmed E. Hassan and Audris Mockus and Anand Sinha and Naoyasu Ubayashi},\njournal={IEEE Transactions on Software Engineering},\nvolume={39}, number={6}, pages={757--773}, year={2013},\ndoi={10.1109/TSE.2012.70},\n```\nContext: related_work.tex line 50: \"Just-in-time defect prediction \\citep{kamei2013large,hoang2019deepjit,pornprasit2021jitline}\"\n\n**28. kang2024autofl**\n```\ntitle={A Quantitative and Qualitative Evaluation of LLM-Based Explainable Fault Localization},\nauthor={Sungmin Kang and Gabin An and Shin Yoo},\nbooktitle={Proceedings of the ACM on Software Engineering (FSE)},\nyear={2024},\ndoi={10.1145/3660771},\nurl={https://arxiv.org/abs/2308.05487},\n```\nContext: related_work.tex line 19: \"recent LLM-based approaches such as AutoFL \\citep{kang2024autofl} and AgentFL \\citep{qin2024agentfl} share our insight that anomalous execution events carry the strongest diagnostic signal.\"\n\n**29. li2023selectivecontext**\n```\ntitle={Compressing Context to Enhance Inference Efficiency of Large Language Models},\nauthor={Yucheng Li and Bo Dong and Frank Guerin and Chenghua Lin},\nbooktitle={Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\nyear={2023},\nurl={https://aclanthology.org/2023.emnlp-main.391},\n```\nContext: related_work.tex line 10: \"Selective Context \\citep{li2023selectivecontext}\"\nContext: discussion.tex line 66: \"Selective Context \\citep{li2023selectivecontext} showed that pruning low-information tokens preserves downstream accuracy\"\n\n**30. liu2023codeexecution**\n```\ntitle={Code Execution with Pre-trained Language Models},\nauthor={Chenxiao Liu and Shuai Lu and Weizhu Chen and Daxin Jiang and Alexey Svyatkovskiy and Shengyu Fu and Neel Sundaresan and Nan Duan},\nbooktitle={Findings of the Association for Computational Linguistics: ACL 2023},\npages={4984--4999}, year={2023},\ndoi={10.18653/v1/2023.findings-acl.308},\n```\nContext: related_work.tex line 5: \"\\citet{liu2023codeexecution} pre-trained models to predict execution outputs from traces.\"\n\n**31. ni2024next**\n```\ntitle={NExT: Teaching Large Language Models to Reason about Code Execution},\nauthor={Ansong Ni and Miltiadis Allamanis and Arman Cohan and Yinlin Deng and Kensen Shi and Charles Sutton and Pengcheng Yin},\nbooktitle={Proceedings of the 41st International Conference on Machine Learning (ICML)},\nyear={2024},\nurl={https://arxiv.org/abs/2404.14662},\n```\nContext: introduction.tex line 4: \"citep{...ni2024next}\"\nContext: related_work.tex line 7: \"NExT \\citep{ni2024next}...used trace chain-of-thought for execution reasoning\"\n\n**32. papadakis2019mutation**\n```\ntitle={Mutation Testing Advances: An Analysis and Survey},\nauthor={Mike Papadakis and Marinos Kintis and Jie Zhang and Yue Jia and Yves Le Traon and Mark Harman},\njournal={Advances in Computers},\nvolume={112}, pages={275--378}, year={2019},\ndoi={10.1016/bs.adcom.2018.03.015},\n```\nContext: related_work.tex line 18: \"the equivalent-mutant problem \\citep{papadakis2019mutation} poses an analogous classification challenge\"\n\n**33. pornprasit2021jitline**\n```\ntitle={JITLine: A Simpler, Better, Faster, Finer-grained Just-In-Time Defect Prediction},\nauthor={Chanathip Pornprasit and Chakkrit Tantithamthavorn},\nbooktitle={Proceedings of the 18th International Conference on Mining Software Repositories (MSR)},\npages={369--379}, year={2021},\ndoi={10.1109/MSR52588.2021.00049},\n```\nContext: related_work.tex line 50: \"Just-in-time defect prediction \\citep{kamei2013large,hoang2019deepjit,pornprasit2021jitline}\"\n\n**34. qin2024agentfl**\n```\ntitle={AgentFL: Scaling LLM-based Fault Localization to Project-Level Context},\nauthor={Yihao Qin and Shangwen Wang and Yiling Lou and Jinhao Dong and Kaixin Wang and Xiaoling Li and Xiaoguang Mao},\nbooktitle={Proceedings of the 39th IEEE/ACM International Conference on Automated Software Engineering (ASE)},\nyear={2024},\nurl={https://arxiv.org/abs/2403.16362},\n```\nContext: related_work.tex line 19: \"AgentFL \\citep{qin2024agentfl} share our insight that anomalous execution events carry the strongest diagnostic signal.\"\n\n## Output format for each entry:\n```\n[key] Author(year) \"First 5 words of title...\"\n  Exists: ✓/✗  Authors: ✓/✗  Year: ✓/✗  Title: ✓/✗  Venue: ✓/✗  arXiv: ✓/✗/N/A\n  Citation context: [file:line] ✓/✗ — [explanation]\n  Issues: [if any]\n```\n\nSearch for each paper title using WebSearch with quotes around the title. Report your findings thoroughly.\n"
  }
}
````

</details>

---

### Tool result

_source line 70 · 2026-05-26T10:27:35.580841+00:00_

Web search results for query: "TraceCoder ICSE 2026 "Jiangping Huang" authors list"

Links: [{"title":"Envisioning Intelligent Requirements Engineering via Knowledge-Guided Multi-Agent Collaboration | Request PDF","url":"https://www.researchgate.net/publication/400199860_Envisioning_Intelligent_Requirements_Engineering_via_Knowledge-Guided_Multi-Agent_Collaboration"},{"title":"Dongming Jin - Homepage","url":"https://jdm4pku.github.io/"},{"title":"ICSE 2026 - Journal-first Papers - ICSE 2026","url":"https://conf.researchr.org/track/icse-2026/icse-2026-journal-first-papers"},{"title":"ICSE 2026 - Research Track - ICSE 2026","url":"https://conf.researchr.org/track/icse-2026/icse-2026-research-track"},{"title":"80+ \"Jiangping Huang\" profiles","url":"https://www.linkedin.com/pub/dir/Jiangping/Huang"},{"title":"7 \"Huang Jianping\" profiles","url":"https://www.linkedin.com/pub/dir/Huang/Jianping"},{"title":"ICSE 2026 - Demonstrations - conf.researchr.org","url":"https://conf.researchr.org/track/icse-2026/icse-2026-demonstrations"},{"title":"ICSE 2026, Research Track","url":"https://icse2026.hotcrp.com/"}]

Based on the search results, TraceCoder is a Trace-Driven Multi-Agent Framework for Automated Debugging of LLM-Generated Code with authors Jiangping Huang, Wenguang Ye, Weisong Sun, and Yang Liu. The paper was listed as a preprint available in February 2026.

However, I should note that while this appears to be related work, the search results don't specifically confirm that TraceCoder is appearing at ICSE 2026. The paper is listed as a preprint, and it may have been submitted to ICSE 2026, but I cannot definitively confirm its acceptance or presence in the official ICSE 2026 program from these search results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 71 · 2026-05-26T10:27:35.581005+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"RepairAgent: An Autonomous, LLM-Based Agent for Program Repair\" Bouzenia Devanbu Pradel"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"RepairAgent: An Autonomous, LLM-Based Agent for Program Repair\" Bouzenia Devanbu Pradel"
  }
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-26T10:27:35.581256+00:00_

Web search results for query: ""RepairAgent: An Autonomous, LLM-Based Agent for Program Repair" Bouzenia Devanbu Pradel"

Links: [{"title":"[2403.17134] RepairAgent: An Autonomous, LLM-Based Agent for Program Repair","url":"https://arxiv.org/abs/2403.17134"},{"title":"RepairAgent: An Autonomous, LLM-Based Agent for Program Repair Islem Bouzenia","url":"https://arxiv.org/pdf/2403.17134"},{"title":"[Literature Review] RepairAgent: An Autonomous, LLM-Based Agent for Program Repair","url":"https://www.themoonlight.io/en/review/repairagent-an-autonomous-llm-based-agent-for-program-repair"},{"title":"RepairAgent: An Autonomous, LLM-Based Agent for Program Repair","url":"https://arxiv.org/html/2403.17134v1"},{"title":"GitHub - sola-st/RepairAgent: RepairAgent is an autonomous LLM-based agent for software repair. · GitHub","url":"https://github.com/sola-st/RepairAgent"},{"title":"RepairAgent: An Autonomous, LLM-Based Agent for Program Repair | ELLIS Unit Stuttgart","url":"https://ellis-stuttgart.eu/publications/icse2025-RepairAgent/"},{"title":"RepairAgent: An Autonomous, LLM-Based Agent for Program Repair | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/repairagent-autonomous-llm-based-agent-program-repair"},{"title":"RepairAgent: An Autonomous, LLM-Based Agent for Program Repair Islem Bouzenia","url":"https://jespereggers.com/wp-content/uploads/2024/10/Bouzenia-et-al.-2024-RepairAgent-An-Autonomous-LLM-Based-Agent-for-Pr-1.pdf"},{"title":"RepairAgent: An Autonomous, LLM-Based Agent for Program Repair | Request PDF","url":"https://www.researchgate.net/publication/392956389_RepairAgent_An_Autonomous_LLM-Based_Agent_for_Program_Repair"}]

I found the paper you're looking for! Here's a summary of the key information:

"RepairAgent" is the first work to address the program repair challenge through an autonomous agent based on a large language model (LLM). The authors are Islem Bouzenia, Premkumar Devanbu, and Michael Pradel.

**Key Features:**

RepairA
…[truncated 1078 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 73 · 2026-05-26T10:27:35.581416+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Evaluating Large Language Models Trained on Code\" Chen Tworek arXiv 2107.03374"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Evaluating Large Language Models Trained on Code\" Chen Tworek arXiv 2107.03374"
  }
}
```

</details>

---

### Tool result

_source line 74 · 2026-05-26T10:27:35.581550+00:00_

Web search results for query: ""Evaluating Large Language Models Trained on Code" Chen Tworek arXiv 2107.03374"

Links: [{"title":"[2107.03374] Evaluating Large Language Models Trained on Code","url":"https://arxiv.org/abs/2107.03374"},{"title":"Evaluating Large Language Models Trained on Code","url":"https://arxiv.org/pdf/2107.03374"},{"title":"[PDF] Evaluating Large Language Models Trained on Code | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Evaluating-Large-Language-Models-Trained-on-Code-Chen-Tworek/acbdbf49f9bc3f151b93d9ca9a06009f4f6eb269"},{"title":"Paper page - Evaluating Large Language Models Trained on Code","url":"https://huggingface.co/papers/2107.03374"},{"title":"Evaluating Large Language Models Trained on Code. | BibSonomy","url":"https://www.bibsonomy.org/bibtex/1612004c4b9c4bdd58c95b8e5127b9f9f"},{"title":"(PDF) Evaluating Large Language Models Trained on Code","url":"https://www.researchgate.net/publication/353066484_Evaluating_Large_Language_Models_Trained_on_Code"},{"title":"[2107.03374v2] Evaluating Large Language Models Trained on Code","url":"https://arxiv.org/abs/2107.03374v2"},{"title":"CodeMixBench: Evaluating Large Language Models on Code Generation with Code-Mixed Prompts","url":"https://arxiv.org/html/2505.05063v1"},{"title":"(PDF) Evaluating Large Language Models Trained on Code","url":"https://www.academia.edu/94807952/Evaluating_Large_Language_Models_Trained_on_Code"}]

I found the paper you're looking for! Here are the key details:

**Paper:** "Evaluating Large Language Models Trained on Code" by Mark Chen, Jerry Tworek, and many co-authors

**ArXiv ID:** 2107.03374

**Published:** July 14, 2021

**Main Contribution:**
The paper introduces Codex, a GPT language model fine-tuned on publicly available code from GitHub, studying its Python code-writing capabilities. A distinct production version of Codex powers GitHub Copilot.

**Key Results:**
On HumanEval, a new evaluation set released to measure functional correctn
…[truncated 702 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 75 · 2026-05-26T10:27:35.581701+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Teaching Large Language Models to Self-Debug\" Xinyun Chen Maxwell Lin Schärli Denny Zhou ICLR 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Teaching Large Language Models to Self-Debug\" Xinyun Chen Maxwell Lin Schärli Denny Zhou ICLR 2024"
  }
}
```

</details>

---

### Tool result

_source line 76 · 2026-05-26T10:27:35.581835+00:00_

Web search results for query: ""Teaching Large Language Models to Self-Debug" Xinyun Chen Maxwell Lin Schärli Denny Zhou ICLR 2024"

Links: [{"title":"[2304.05128] Teaching Large Language Models to Self-Debug","url":"https://arxiv.org/abs/2304.05128"},{"title":"TEACHING LARGE LANGUAGE MODELS TO SELF- DEBUG","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/2460396f2d0d421885997dd1612ac56b-Paper-Conference.pdf"},{"title":"[PDF] Teaching Large Language Models to Self-Debug | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Teaching-Large-Language-Models-to-Self-Debug-Chen-Lin/9e3c493fb09dcd61bb05e8c5659f23327b7b6340"},{"title":"Teaching Large Language Models to Self-Debug Xinyun Chen Google Research","url":"https://arxiv.org/pdf/2304.05128v1"},{"title":"[2304.05128v1] Teaching Large Language Models to Self-Debug","url":"https://arxiv.org/abs/2304.05128v1"},{"title":"[2304.05128v2] Teaching Large Language Models to Self-Debug","url":"https://arxiv.org/abs/2304.05128v2"},{"title":"[Quick Review] Teaching Large Language Models to Self-Debug","url":"https://liner.com/review/teaching-large-language-models-to-selfdebug"},{"title":"Large Language Model Guided Self-Debugging Code Generation","url":"https://arxiv.org/html/2502.02928v2"}]

I found the paper you're looking for. Here's what I found:

## "Teaching Large Language Models to Self-Debug"

**Paper Details:**
- Authors: Xinyun Chen, Maxwell Lin, Nathanael Schärli, Denny Zhou
- The paper was published at ICLR 2024 (originally submitted to arXiv in April 2023)

**Key Contribution:**
The paper proposes Self-Debugging, which teaches a large language model to debug its predicted program via few-shot demonstrations.

**Main Finding:**
Self-Debugging can teach the large language model to perform rubber duck debugging; i.e., without any human feedback on the code correctness or error messages, the model is able to identify its mistakes by investigating the execution results and explaining the generate
…[truncated 585 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 77 · 2026-05-26T10:27:35.581976+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Chain of Execution Supervision Promotes General Reasoning\" Nuo Chen Zehua Li NeurIPS 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Chain of Execution Supervision Promotes General Reasoning\" Nuo Chen Zehua Li NeurIPS 2025"
  }
}
```

</details>

---

### Tool result

_source line 78 · 2026-05-26T10:27:35.582102+00:00_

Web search results for query: ""Towards Effectively Leveraging Execution Traces" "KnowledgeNLP" ACL 2025 workshop venue"

Links: [{"title":"Towards Effectively Leveraging Execution Traces for ...","url":"https://aclanthology.org/2025.knowledgenlp-1.17.pdf"},{"title":"KnowledgeNLP’25 2025 The 4th International Workshop on Knowledge-Augmented","url":"https://aclanthology.org/2025.knowledgenlp-1.0.pdf"},{"title":"Workshop on Knowledge Augmented Methods for NLP (2025) - ACL Anthology","url":"https://aclanthology.org/events/knowledgenlp-2025/"},{"title":"[2505.04441] Towards Effectively Leveraging Execution Traces for Program Repair with Code LLMs","url":"https://arxiv.org/abs/2505.04441"},{"title":"Towards Effectively Leveraging Execution Traces for Program Repair with Code LLMs","url":"https://arxiv.org/html/2505.04441v1"},{"title":"Leveraging Domain Knowledge at Inference Time for LLM Translation: Retrieval versus Generation - ACL Anthology","url":"https://aclanthology.org/2025.knowledgenlp-1.7/"}]

Based on the web search results, I found the information about the paper and its workshop venue:

"Towards Effectively Leveraging Execution Traces for Program Repair with Code LLMs" is by Mirazul Haque, Petr Babkin, Farima Farmahinifarahani and Manuela Veloso.

The paper was presented at KnowledgeNLP'25 (the 4th International Workshop on Knowledge-Augmented Methods for Natural Language Processing), held in conjunction with NAACL 2025 on May 3rd, 2025 in New Mexico, USA.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool call

_source line 79 · 2026-05-26T10:27:35.582263+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2503.05703 \"Armengol-Estapé\" OR \"Armengol-Estape\" first author name spelling"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2503.05703 \"Armengol-Estapé\" OR \"Armengol-Estape\" first author name spelling"
  }
}
```

</details>

---

### Tool call

_source line 80 · 2026-05-26T10:27:35.582396+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"KnowledgeNLP Workshop\" NAACL 2025 OR ACL 2025 workshop"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"KnowledgeNLP Workshop\" NAACL 2025 OR ACL 2025 workshop"
  }
}
```

</details>

---

### Tool call

_source line 81 · 2026-05-26T10:27:35.582512+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2602.06875 TraceCoder authors \"Jian Zhang\" \"Mingyue Zhang\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2602.06875 TraceCoder authors \"Jian Zhang\" \"Mingyue Zhang\""
  }
}
```

</details>

---

### Tool call

_source line 82 · 2026-05-26T10:27:35.582624+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CRUXEval authors \"Sida I. Wang\" OR \"Sida Wang\" ICML 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CRUXEval authors \"Sida I. Wang\" OR \"Sida Wang\" ICML 2024"
  }
}
```

</details>

---

### Tool result

_source line 83 · 2026-05-26T10:27:35.582742+00:00_

Web search results for query: "arxiv 2503.05703 "Armengol-Estapé" OR "Armengol-Estape" first author name spelling"

Links: [{"title":"[2503.05703] What I cannot execute, I do not understand: Training and Evaluating LLMs on Program Execution Traces","url":"https://arxiv.org/abs/2503.05703"},{"title":"dblp: Jordi Armengol-Estapé","url":"https://dblp.org/pid/263/2700.html"},{"title":"Jordi Armengol-Estapé","url":"https://scholar.google.com/citations?user=CiHoJfcAAAAJ&hl=en"},{"title":"Jordi Armengol-Estapé","url":"https://openreview.net/profile?id=~Jordi_Armengol-Estap%C3%A91"},{"title":"Jordi Armengol-Estapé | IEEE Xplore Author Details","url":"https://ieeexplore.ieee.org/author/354093766232960"},{"title":"Jordi Armengol-Estapé","url":"https://orcid.org/0000-0001-8893-6185"},{"title":"Jordi Armengol-Estapé - ACL Anthology","url":"https://aclanthology.org/people/jordi-armengol-estape/"},{"title":"Papers with Code - Jordi Armengol-Estapé","url":"https://paperswithcode.com/author/jordi-armengol-estape"},{"title":"Jordi Armengol-Estape - Research Scientist, FAIR @ Meta","url":"https://uk.linkedin.com/in/jordiae"}]

Based on the search results, the first author of arxiv paper 2503.05703 is Jordi Armengol-Estapé. The correct spelling is **Armengol-Estapé** (with an accent on the final 'e'), as confirmed by multiple academic sources including the arXiv page, DBLP, Google Scholar, and the ACL Anthology.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 84 · 2026-05-26T10:27:35.582886+00:00_

Web search results for query: ""KnowledgeNLP Workshop" NAACL 2025 OR ACL 2025 workshop"

Links: [{"title":"Welcome to KnowledgeNLP-NAACL'25!","url":"https://knowledge-nlp.github.io/naacl2025/"},{"title":"Knowledge-Augmented Methods for NLP Workshop at NAACL 2025 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/knowledge-augmented-methods-nlp-workshop-naacl-2025"},{"title":"Workshop on Knowledge Augmented Methods for NLP (2025) - ACL Anthology","url":"https://aclanthology.org/events/knowledgenlp-2025/"},{"title":"KnowledgeNLP’25 2025 The 4th International Workshop on Knowledge-Augmented","url":"https://aclanthology.org/2025.knowledgenlp-1.0.pdf"},{"title":"NAACL 2025 Workshop KnowledgeNLP | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FNAACL%2F2025%2FWorkshop%2FKnowledgeNLP"},{"title":"Joint Call for Workshops Proposals - NAACL-HLT 2025","url":"https://2025.naacl.org/calls/workshops/"},{"title":"KnowledgeNLP Workshop @NAACL 2025 (@knowledgenlp) / X","url":"https://x.com/knowledgenlp?lang=en"},{"title":"Joint Call for Workshops for NAACL/ACL/EMNLP 2025 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-workshops-naaclaclemnlp-2025"}]

I found information about the KnowledgeNLP Workshop. Here are the key details:

## KnowledgeNLP Workshop at NAACL 2025

This workshop is the 4th edition of the workshop focusing on knowledge-driven NLP, aiming to highlight the importance of the application of knowledge in NLP methods, and to explore its role in large language models (LLMs).

**Date and Location:**
KnowledgeNLP will take place on May 3rd, 2025, allowing for both virtual and in-person attendance in New Mexico, USA.

**Important Dates:**
Workshop Paper Due Date: Feb 14, 2025; Notification of acceptance: Mar 7, 2025; Camera-ready papers due: Mar 14, 2025; Workshop date: May 3, 2025.

**Background:**
The first workshop on knowledge-augmented methods for NLP was held at AAAI 2023. The third workshop on knowledge-augm
…[truncated 382 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 85 · 2026-05-26T10:27:35.583027+00:00_

Web search results for query: "arxiv 2602.06875 TraceCoder authors "Jian Zhang" "Mingyue Zhang""

Links: [{"title":"[2602.06875] TraceCoder: A Trace-Driven Multi-Agent Framework for Automated Debugging of LLM-Generated Code","url":"https://arxiv.org/abs/2602.06875"},{"title":"TraceCoder: A Trace-Driven Multi-Agent Framework for Automated Debugging of LLM-Generated Code","url":"https://arxiv.org/html/2602.06875"},{"title":"[2510.15267] TraceCoder: Towards Traceable ICD Coding via Multi-Source Knowledge Integration","url":"https://arxiv.org/abs/2510.15267"},{"title":"Computer Science","url":"https://arxiv.org/list/cs/recent?skip=543&show=2000"},{"title":"Computer Vision and Pattern Recognition Mar 2025","url":"https://arxiv.org/list/cs.CV/2025-03?skip=1200&show=2000"},{"title":"[2602.15763] GLM-5: from Vibe Coding to Agentic Engineering","url":"https://arxiv.org/abs/2602.15763"},{"title":"Computer Vision and Pattern Recognition Feb 2024","url":"https://arxiv.org/list/cs.CV/2024-02?skip=125&show=2000"}]

Based on the search results, I found information about arxiv paper 2602.06875 on TraceCoder:

The paper is titled "TraceCoder: A Trace-Driven Multi-Agent Framework for Automated Debugging of LLM-Generated Code" and has authors including Jiangping Huang, Wenguang Ye, Weisong Sun, Jian Zhang, Mingyue Zhang, and Yang Liu.

Jian Zhang is affiliated with Beihang University in Beijing, China, and Mingyue Zhang is affiliated with Southwest University in Chongqing, China.

The paper presents TraceCoder, a collaborative multi-agent framework that emulates the observe-analyze-repair process of human experts. The framework instruments code with diagnostic probes to capture fine-grained runtime traces, and then conducts causal analysis on these traces to accurately identify the root cause of failures.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 86 · 2026-05-26T10:27:35.583170+00:00_

Web search results for query: "CRUXEval authors "Sida I. Wang" OR "Sida Wang" ICML 2024"

Links: [{"title":"CRUXEval: A Benchmark for Code Reasoning, Understanding and Execution | ML Anthology","url":"https://mlanthology.org/icml/2024/gu2024icml-cruxeval/"},{"title":"ICLR CRUXEval: A Benchmark for Code Reasoning, Understanding and Execution","url":"https://iclr.cc/virtual/2024/22440"},{"title":"CRUXEval: A Benchmark for Code Reasoning, Understanding and Execution","url":"https://proceedings.mlr.press/v235/gu24c.html"},{"title":"GitHub - facebookresearch/cruxeval: CRUXEval: Code Reasoning, Understanding, and Execution Evaluation · GitHub","url":"https://github.com/facebookresearch/cruxeval"},{"title":"ICML Poster CRUXEval: A Benchmark for Code Reasoning, Understanding and Execution","url":"https://icml.cc/virtual/2024/poster/34526"},{"title":"[PDF] CRUXEval: A Benchmark for Code Reasoning, Understanding and Execution | Semantic Scholar","url":"https://www.semanticscholar.org/paper/CRUXEval:-A-Benchmark-for-Code-Reasoning,-and-Gu-Rozi%C3%A8re/4701914bc77dedef9e0a001687277103fb3ddfc6"},{"title":"dblp: ICML 2024","url":"https://dblp.org/db/conf/icml/icml2024.html"},{"title":"ICML 2024 Reviewers","url":"https://icml.cc/Conferences/2024/Reviewers"},{"title":"CRUXEval: A Benchmark for Code Reasoning, Understanding and Execution | OpenReview","url":"https://openreview.net/forum?id=Ffpg52swvg"}]

Based on the search results, I found information about the CRUXEval paper and its authors at ICML 2024:

The CRUXEval paper was authored by Alex Gu, Baptiste Roziere, Hugh James Leather, Armando Solar-Lezama, Gabriel Synnaeve, and Sida Wang, and was published at ICML 2024. The author is credited as "Sida I. Wang" in some citations.

The paper presents Code Reasoning, Understanding, and eXecution Evaluation (CRUXEval), a benchmark consisting of 800 Python functions (3-13 lines), with each function coming with an input-output pair for two natural tasks: input prediction and output pre
…[truncated 111 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 87 · 2026-05-26T10:27:35.583547+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2503.05703 \"What I cannot execute\" author \"Ferrando\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2503.05703 \"What I cannot execute\" author \"Ferrando\""
  }
}
```

</details>

---

### Tool call

_source line 88 · 2026-05-26T10:27:35.583792+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "DeepJIT MSR 2019 authors \"Thong Hoang\" \"Hoa Khanh Dam\" \"Yasutaka Kamei\" pages"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "tool_args": {
    "query": "DeepJIT MSR 2019 authors \"Thong Hoang\" \"Hoa Khanh Dam\" \"Yasutaka Kamei\" pages"
  }
}
```

</details>

---

### Tool result

_source line 89 · 2026-05-26T10:27:35.583969+00:00_

Web search results for query: "DeepJIT MSR 2019 authors "Thong Hoang" "Hoa Khanh Dam" "Yasutaka Kamei" pages"

Links: [{"title":"[PDF] DeepJIT: An End-to-End Deep Learning Framework for Just-in-Time Defect Prediction | Semantic Scholar","url":"https://www.semanticscholar.org/paper/DeepJIT:-An-End-to-End-Deep-Learning-Framework-for-Hoang-Dam/952fe2400f4b1a33fa45aa1aefaa856235e13c0c"},{"title":"DeepJIT | Proceedings of the 16th International Conference on Mining Software Repositories","url":"https://dl.acm.org/doi/10.1109/msr.2019.00016"},{"title":"POSL Research Group","url":"https://posl.ait.kyushu-u.ac.jp/papers_jp.html"},{"title":"dblp: Khanh Hoa Dam","url":"https://dblp.org/pid/75/4194.html"},{"title":"DeepJIT: An End-to-End Deep Learning Framework for Just-in-Time Defect Prediction | Request PDF","url":"https://www.researchgate.net/publication/335498581_DeepJIT_An_End-to-End_Deep_Learning_Framework_for_Just-in-Time_Defect_Prediction"},{"title":"DeepJIT: An end-to-end deep learning framework for just-in-time defect prediction","url":"https://zenodo.org/records/3965246"},{"title":"Hoa Khanh Dam","url":"https://www.researchgate.net/profile/Hoa-Dam"},{"title":"An empirical study of token-based micro commits | Empirical Software Engineering | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10664-024-10527-8"},{"title":"(PDF) Towards Effective AI-Powered Agile Project Management","url":"https://www.researchgate.net/publication/335361278_Towards_Effective_AI-Powered_Agile_Project_Management"},{"title":"[1812.10578] Towards effective AI-powered agile project management","url":"https://arxiv.org/abs/1812.10578"}]

Based on the search results, here is the information about the DeepJIT paper at MSR 2019:

**Title:** DeepJIT: An End-to-End Deep Learning Framework for Just-in-Time Defect Prediction

**Authors:** Thong Hoang, Hoa Khanh Dam, Yasutaka Kamei, David Lo, Naoyasu Ubayashi

**Conference:** 2019 IEEE/ACM 16th International Conference on Mining 
…[truncated 164 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 90 · 2026-05-26T10:27:35.584155+00:00_

Web search results for query: "arxiv 2503.05703 "What I cannot execute" author "Ferrando""

Links: [{"title":"[2503.05703] What I cannot execute, I do not understand: Training and Evaluating LLMs on Program Execution Traces","url":"https://arxiv.org/abs/2503.05703"},{"title":"What I cannot execute, I do not understand: Training and Evaluating LLMs on Program Execution Traces","url":"https://arxiv.org/html/2503.05703"},{"title":"Computer Science","url":"https://www.arxiv.org/list/cs/recent?skip=1057&show=1000"},{"title":"Machine Learning Mar 2025","url":"https://www.arxiv.org/list/cs.LG/2025-03?skip=500&show=2000"},{"title":"A Modern Introduction to Cardano and Ferrari Formulas in the Algebraic   Equations","url":"https://arxiv.org/pdf/quant-ph/0311102"},{"title":"Fermionic state discrimination by local operations and classical   communication","url":"https://arxiv.org/pdf/2002.10197"},{"title":"The Feynman problem and Fermionic entanglement: Fermionic theory versus   qubit theory","url":"https://arxiv.org/pdf/1403.2674"}]

I found the paper! The arXiv paper 2503.05703 is titled "What I cannot execute, I do not understand: Training and Evaluating LLMs on Program Execution Traces".

However, I should note that based on the search results, the authors listed include Jordi Armengol-Estapé, Quentin Carbonneaux, Tianjun Zhang, Aram H. Markosyan, Volker Seeker, Chris Cummins, Melanie Kambadur, Michael F.P. O'Boyle, Sida Wang, Gabriel Synnaeve, and Hugh James Leather. I did not find an author named "Ferrando" listed for this paper in the search results. It's possible there may be a different paper you're looking for, or the author information in your query may differ from what appears on arXiv.

The paper studies Execution Tuning (E.T.), a training procedure in which they explicitly model real-world program execution traces without requiring manual test annotations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 91 · 2026-05-26T10:27:35.584554+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "LoRA ICLR 2022 \"10th International Conference on Learning Representations\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "tool_args": {
    "query": "LoRA ICLR 2022 \"10th International Conference on Learning Representations\""
  }
}
```

</details>

---

### Tool call

_source line 92 · 2026-05-26T10:27:35.584744+00:00_

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
  "session": "worker_audit_citation-verify-w2_20260526T101532",
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

_source line 93 · 2026-05-26T10:27:35.584903+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 94 · 2026-05-26T10:27:35.585040+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"SWE-bench: Can Language Models Resolve Real-World GitHub Issues?\" Jimenez ICLR 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"SWE-bench: Can Language Models Resolve Real-World GitHub Issues?\" Jimenez ICLR 2024"
  }
}
```

</details>

---

### Tool result

_source line 95 · 2026-05-26T10:27:35.585197+00:00_

Web search results for query: ""SWE-bench: Can Language Models Resolve Real-World GitHub Issues?" Jimenez ICLR 2024"

Links: [{"title":"[2310.06770] SWE-bench: Can Language Models Resolve Real-World GitHub Issues?","url":"https://arxiv.org/abs/2310.06770"},{"title":"GitHub - SWE-bench/SWE-bench: SWE-bench: Can Language Models Resolve Real-world Github Issues? · GitHub","url":"https://github.com/SWE-bench/SWE-bench"},{"title":"Can Language Models Resolve Real-world Github Issues","url":"https://www.swebench.com/original.html"},{"title":"SWE-BENCH: CAN LANGUAGE MODELS RESOLVE ...","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/edac78c3e300629acfe6cbe9ca88fb84-Paper-Conference.pdf"},{"title":"SWE-Bench: Can Language Models Resolve Real-World ...","url":"https://arxiv.org/pdf/2310.06770"},{"title":"SWE-BENCH: CAN LANGUAGE MODELS RESOLVE REAL-WORLD GITHUB ISSUES? - Princeton University","url":"https://collaborate.princeton.edu/en/publications/swe-bench-can-language-models-resolve-real-world-github-issues/"},{"title":"SWE-bench: Can Language Models Resolve Real-world Github Issues?","url":"https://proceedings.iclr.cc/paper_files/paper/2024/hash/edac78c3e300629acfe6cbe9ca88fb84-Abstract-Conference.html"},{"title":"SWE-bench: Can Language Models Resolve Real-world Github Issues? | OpenReview","url":"https://openreview.net/forum?id=VTF8yNQM66"},{"title":"SWE-BENCH: CAN LANGUAGE MODELS RESOLVE ...","url":"https://openreview.net/pdf?id=VTF8yNQM66"},{"title":"ICLR Oral SWE-bench: Can Language Models Resolve Real-world Github Issues?","url":"https://iclr.cc/virtual/2024/oral/19757"}]

I found the paper you're looking for! Here are the key details about the SWE-bench paper:

## Paper Overview

The paper "SWE-bench: Can Language Models Resolve Real-world Github Issues?" was authored by Carlos E Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press, and Karthik R Narasimhan, and was published at The Twelfth International Conference on Learning Repr
…[truncated 940 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 96 · 2026-05-26T10:27:35.585432+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Visualization of Test Information to Assist Fault Localization\" Jones Harrold Stasko ICSE 2002"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Visualization of Test Information to Assist Fault Localization\" Jones Harrold Stasko ICSE 2002"
  }
}
```

</details>

---

### Tool result

_source line 97 · 2026-05-26T10:27:35.585615+00:00_

Web search results for query: ""Visualization of Test Information to Assist Fault Localization" Jones Harrold Stasko ICSE 2002"

Links: [{"title":"Visualization of test information to assist fault localization | Request PDF","url":"https://www.researchgate.net/publication/3952065_Visualization_of_test_information_to_assist_fault_localization"},{"title":"Visualization of Test Information to Assist Fault Localization","url":"https://faculty.cc.gatech.edu/~stasko/papers/icse02.pdf"},{"title":"[PDF] Visualization of test information to assist fault localization | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Visualization-of-test-information-to-assist-fault-Jones-Harrold/54a7d105ee1a5256b168f16d8264262340c0f6c3"},{"title":"Visualization of Test Information to Assist Fault Localization","url":"https://sites.cc.gatech.edu/gvu/ii/talks/icse02.pdf"},{"title":"Visualization of test information to assist fault localization | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/1007991/"},{"title":"[ISER] [SME] Visualization of test information to assist fault localization | Academic Notes","url":"https://wym0120.github.io/2020/09/18/paper/ISER/Software%20Maintenance%20and%20Evolution/sme-1/"},{"title":"Visualization of test information to assist fault localization | Spider Lab Research Group","url":"https://spideruci.org/publication/jones-visualization-2002/"},{"title":"Visualization of test information to assist fault localization | Proceedings of the 24th International Conference on Software Engineering","url":"https://dl.acm.org/doi/10.1145/581339.581397"},{"title":"Effective fault localization using probabilistic and grouping approach | International Journal of System Assurance Engineering and Management | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s13198-024-02479-5"},{"title":"Interactive Fault Localization Using Test Information | Journal of Computer Science and Technology | Springer Nature 
…[truncated 1426 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 98 · 2026-05-26T10:27:35.585785+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Language Models (Mostly) Know What They Know\" Kadavath 2022 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Language Models (Mostly) Know What They Know\" Kadavath 2022 arXiv"
  }
}
```

</details>

---

### Tool result

_source line 99 · 2026-05-26T10:27:35.585979+00:00_

Web search results for query: ""Language Models (Mostly) Know What They Know" Kadavath 2022 arXiv"

Links: [{"title":"[2207.05221] Language Models (Mostly) Know What They Know","url":"https://arxiv.org/abs/2207.05221"},{"title":"(PDF) Language Models (Mostly) Know What They Know","url":"https://www.researchgate.net/publication/361949621_Language_Models_Mostly_Know_What_They_Know"},{"title":"[PDF] Language Models (Mostly) Know What They Know | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Language-Models-(Mostly)-Know-What-They-Know-Kadavath-Conerly/142ebbf4760145f591166bde2564ac70c001e927"},{"title":"Language Models (Mostly) Know What They Know","url":"https://bibbase.org/network/publication/kadavath-conerly-askell-henighan-drain-perez-schiefer-hatfielddodds-etal-languagemodelsmostlyknowwhattheyknow-2022"},{"title":"(PDF) Language Models (Mostly) Know What They Know (2022) | Saurav Kadavath | 413 Citations","url":"https://scispace.com/papers/language-models-mostly-know-what-they-know-zkg0pou4"},{"title":"Language Models (Mostly) Know What They Know - ADS","url":"https://ui.adsabs.harvard.edu/abs/2022arXiv220705221K/abstract"},{"title":"ml-papers/papers/2022/220711 Language Models (Mostly) Know What They Know.md at main · rosinality/ml-papers","url":"https://github.com/rosinality/ml-papers/blob/main/papers/2022/220711%20Language%20Models%20(Mostly)%20Know%20What%20They%20Know.md"},{"title":"[2207.05221] Language Models (Mostly) Know What They Know – Papiers","url":"https://papiers.ai/2207.05221"}]

I found the paper you're looking for! Here are the details:

**Title:** Language Models (Mostly) Know What They Know

**Authors:** Saurav Kadavath, Tom Conerly, Amanda Askell, Tom Henighan, Dawn Drain, Ethan Perez, Nicholas Schiefer, Zac Hatfield-Dodds, Nova DasSarma, Eli Tran-Johnson, Scott Johnston, Sheer El-Showk, Andy Jones, Nelson Elhage, Tristan Hume, Anna Chen, Yuntao Bai, Sam Bowman, Stanislav Fort, Deep Ganguli, Danny Hernandez, Josh Jacobson, Jac
…[truncated 763 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 100 · 2026-05-26T10:27:35.586141+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"A Large-Scale Empirical Study of Just-in-Time Quality Assurance\" Kamei Shihab Adams Hassan 2013"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"A Large-Scale Empirical Study of Just-in-Time Quality Assurance\" Kamei Shihab Adams Hassan 2013"
  }
}
```

</details>

---

### Tool call

_source line 101 · 2026-05-26T10:27:35.586346+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

````json
{
  "description": "Verify bib entries group 4 (35-46)",
  "prompt": "You are verifying academic paper references for correctness. For each bib entry below, use WebSearch to search for the paper title (in quotes) and verify:\na) Paper exists (MOST IMPORTANT)\nb) Author names (first and last author spelling)\nc) Year\nd) Title accuracy\ne) Venue correctness\nf) arXiv ID if present\n\nAlso check that each citation is used correctly in context (I provide the citation contexts).\n\n## Entries to verify (Group 4):\n\n**35. qwen2025coder**\n```\ntitle={Qwen2.5-Coder Technical Report},\nauthor={Qwen Team},\njournal={arXiv preprint arXiv:2409.12186},\nyear={2024},\nurl={https://arxiv.org/abs/2409.12186},\n```\nContext: introduction.tex line 14, method.tex line 32: cited as one of the model families used (Qwen-2.5-Coder-7B/1.5B-Instruct).\n\n**36. roziere2024code**\n```\ntitle={Code Llama: Open Foundation Models for Code},\nauthor={Baptiste Rozière and Jonas Gehring and Fabian Gloeckle and Sten Sootla and Itai Gat and Xiaoqing Ellen Tan and Yossi Adi and Jingyu Liu and Rémi Lacroix and Tal Remez and Jérémy Rapin and Artyom Kozhevnikov and Ivan Evtimov and Joanna Bitton and Manish Bhatt and Cristian Canton Ferrer and Aaron Grattafiori and Wenhan Xiong and Alexandre Défossez and Jade Copet and Faisal Azhar and Hugo Touvron and Louis Martin and Nicolas Usunier and Thomas Scialom and Gabriel Synnaeve},\njournal={arXiv preprint arXiv:2308.12950},\nyear={2023},\n```\nContext: introduction.tex line 14, method.tex line 32: cited as CodeLlama-13B-Instruct model family.\n\n**37. sachdeva2024dataefficient**\n```\ntitle={How to Train Data-Efficient LLMs},\nauthor={Noveen Sachdeva and Benjamin Coleman and Wang-Cheng Kang and Jianmo Ni and Lichan Hong and Ed H. Chi and James Caverlee and Julian McAuley and Derek Zhiyuan Cheng},\njournal={arXiv preprint arXiv:2402.09668},\nyear={2024},\nurl={https://arxiv.org/abs/2402.09668},\n```\nContext: related_work.tex line 51: \"data selection methods \\citep{sachdeva2024dataefficient,xie2023doremi} demonstrate that data quality and ordering improve convergence\"\n\n**38. shi2023distracted**\n```\ntitle={Large Language Models Can Be Easily Distracted by Irrelevant Context},\nauthor={Freda Shi and Xinyun Chen and Kanishka Misra and Nathan Scales and David Dohan and Ed Chi and Nathanael Schärli and Denny Zhou},\nbooktitle={Proceedings of the 40th International Conference on Machine Learning (ICML)},\nyear={2023},\n```\nContext: related_work.tex line 9: \"\\citet{shi2023distracted} showed LLMs are easily distracted by irrelevant context, providing a complementary explanation for why verbose traces impair SFT learning.\"\n\n**39. shinn2023reflexion**\n```\ntitle={Reflexion: Language Agents with Verbal Reinforcement Learning},\nauthor={Noah Shinn and Federico Cassano and Edward Berman and Ashwin Gopinath and Karthik Narasimhan and Shunyu Yao},\nbooktitle={Advances in Neural Information Processing Systems (NeurIPS)},\nyear={2023},\n```\nContext: related_work.tex line 21: \"Reflexion \\citep{shinn2023reflexion} iteratively refine code using execution outcomes.\"\n\n**40. spiess2025calibration**\n```\ntitle={Calibration and Correctness of Language Models for Code},\nauthor={Claudio Spiess and David Gros and others},\nbooktitle={Proceedings of the 47th IEEE/ACM International Conference on Software Engineering (ICSE)},\nyear={2025},\nurl={https://arxiv.org/abs/2402.02047},\n```\nContext: related_work.tex line 48: \"\\citet{spiess2025calibration} specifically addressed calibration for code models.\"\nContext: appendix.tex line 546: \"\\citep{spiess2025calibration}\"\n\n**41. steenhoek2024deepdfa**\n```\ntitle={Dataflow Analysis-Inspired Deep Learning for Efficient Vulnerability Detection},\nauthor={Benjamin Steenhoek and Hongyang Gao and Wei Le},\nbooktitle={Proceedings of the 46th IEEE/ACM International Conference on Software Engineering (ICSE)},\nyear={2024},\ndoi={10.1145/3597503.3623345},\n```\nContext: related_work.tex line 16: \"DeepDFA \\citep{steenhoek2024deepdfa}...combined classical program analysis with deep learning for defect detection.\"\n\n**42. swayamdipta2020cartography**\n```\ntitle={Dataset Cartography: Mapping and Diagnosing Datasets with Training Dynamics},\nauthor={Swabha Swayamdipta and Roy Schwartz and Nicholas Lourie and Yizhong Wang and Hannaneh Hajishirzi and Noah A. Smith and Yejin Choi},\nbooktitle={Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\npages={9275--9293}, year={2020},\ndoi={10.18653/v1/2020.emnlp-main.746},\n```\nContext: related_work.tex line 51: \"dataset cartography via training dynamics \\citep{swayamdipta2020cartography}\"\n\n**43. tian2020patchcorrectness**\n```\ntitle={Evaluating Representation Learning of Code Changes for Predicting Patch Correctness in Program Repair},\nauthor={Haoye Tian and Kui Liu and Abdoul Kader Kaboré and Anil Koyuncu and Li Li and Jacques Klein and Tegawendé F. Bissyandé},\nbooktitle={Proceedings of the 35th IEEE/ACM International Conference on Automated Software Engineering (ASE)},\npages={981--992}, year={2020},\ndoi={10.1145/3324884.3416532},\n```\nContext: related_work.tex line 17: \"\\citet{tian2020patchcorrectness} evaluated change representations for predicting repair correctness.\"\n\n**44. tian2024debugbench**\n```\ntitle={DebugBench: Evaluating Debugging Capability of Large Language Models},\nauthor={Runchu Tian and Yining Ye and Yujia Qin and Xin Cong and Yankai Lin and Yinxu Pan and Yesai Wu and Haotian Hui and Weichuan Liu and Zhiyuan Liu and Maosong Sun},\nbooktitle={Findings of the Association for Computational Linguistics: ACL 2024},\nyear={2024},\nurl={https://arxiv.org/abs/2401.04621},\n```\nContext: experiments.tex line 126: \"DebugBench \\citep{tian2024debugbench} ($N{=}426$) preserves the component ranking\"\nContext: appendix.tex line 616: cited in cross-dataset generalization section.\n\n**45. wang2025dcsh**\n```\ntitle={Do Code Semantics Help? A Comprehensive Study on Execution Trace-Based Information for Code Large Language Models},\nauthor={Jian Wang and Xiaofei Xie and Qiang Hu and Shangqing Liu and Yi Li},\nbooktitle={Findings of the Association for Computational Linguistics: EMNLP 2025},\nyear={2025},\nurl={https://arxiv.org/abs/2509.11686},\n```\nContext: introduction.tex line 4, 12: cited for incorporating traces and for finding no single trace representation consistently outperforms.\nContext: related_work.tex line 6: \"\\citet{wang2025dcsh} found trace utility to be task- and format-dependent\"\n\n**46. wang2025inspectcoder**\n```\ntitle={InspectCoder: Dynamic Analysis-Enabled Self Repair through Interactive LLM-Debugger Collaboration},\nauthor={Yunkun Wang and Yue Zhang and Guochang Li and Chen Zhi and Binhua Li and Fei Huang and Yongbin Li and Shuiguang Deng},\njournal={arXiv preprint arXiv:2510.18327},\nyear={2025},\nurl={https://arxiv.org/abs/2510.18327},\n```\nContext: related_work.tex line 10: \"InspectCoder \\citep{wang2025inspectcoder} apply selective trace extraction for automated debugging\"\n\n## Output format for each entry:\n```\n[key] Author(year) \"First 5 words of title...\"\n  Exists: ✓/✗  Authors: ✓/✗  Year: ✓/✗  Title: ✓/✗  Venue: ✓/✗  arXiv: ✓/✗/N/A\n  Citation context: [file:line] ✓/✗ — [explanation]\n  Issues: [if any]\n```\n\nSearch for each paper title using WebSearch with quotes around the title. Report your findings thoroughly.\n"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "Agent",
  "tool_args": {
    "description": "Verify bib entries group 4 (35-46)",
    "prompt": "You are verifying academic paper references for correctness. For each bib entry below, use WebSearch to search for the paper title (in quotes) and verify:\na) Paper exists (MOST IMPORTANT)\nb) Author names (first and last author spelling)\nc) Year\nd) Title accuracy\ne) Venue correctness\nf) arXiv ID if present\n\nAlso check that each citation is used correctly in context (I provide the citation contexts).\n\n## Entries to verify (Group 4):\n\n**35. qwen2025coder**\n```\ntitle={Qwen2.5-Coder Technical Report},\nauthor={Qwen Team},\njournal={arXiv preprint arXiv:2409.12186},\nyear={2024},\nurl={https://arxiv.org/abs/2409.12186},\n```\nContext: introduction.tex line 14, method.tex line 32: cited as one of the model families used (Qwen-2.5-Coder-7B/1.5B-Instruct).\n\n**36. roziere2024code**\n```\ntitle={Code Llama: Open Foundation Models for Code},\nauthor={Baptiste Rozière and Jonas Gehring and Fabian Gloeckle and Sten Sootla and Itai Gat and Xiaoqing Ellen Tan and Yossi Adi and Jingyu Liu and Rémi Lacroix and Tal Remez and Jérémy Rapin and Artyom Kozhevnikov and Ivan Evtimov and Joanna Bitton and Manish Bhatt and Cristian Canton Ferrer and Aaron Grattafiori and Wenhan Xiong and Alexandre Défossez and Jade Copet and Faisal Azhar and Hugo Touvron and Louis Martin and Nicolas Usunier and Thomas Scialom and Gabriel Synnaeve},\njournal={arXiv preprint arXiv:2308.12950},\nyear={2023},\n```\nContext: introduction.tex line 14, method.tex line 32: cited as CodeLlama-13B-Instruct model family.\n\n**37. sachdeva2024dataefficient**\n```\ntitle={How to Train Data-Efficient LLMs},\nauthor={Noveen Sachdeva and Benjamin Coleman and Wang-Cheng Kang and Jianmo Ni and Lichan Hong and Ed H. Chi and James Caverlee and Julian McAuley and Derek Zhiyuan Cheng},\njournal={arXiv preprint arXiv:2402.09668},\nyear={2024},\nurl={https://arxiv.org/abs/2402.09668},\n```\nContext: related_work.tex line 51: \"data selection methods \\citep{sachdeva2024dataefficient,xie2023doremi} demonstrate that data quality and ordering improve convergence\"\n\n**38. shi2023distracted**\n```\ntitle={Large Language Models Can Be Easily Distracted by Irrelevant Context},\nauthor={Freda Shi and Xinyun Chen and Kanishka Misra and Nathan Scales and David Dohan and Ed Chi and Nathanael Schärli and Denny Zhou},\nbooktitle={Proceedings of the 40th International Conference on Machine Learning (ICML)},\nyear={2023},\n```\nContext: related_work.tex line 9: \"\\citet{shi2023distracted} showed LLMs are easily distracted by irrelevant context, providing a complementary explanation for why verbose traces impair SFT learning.\"\n\n**39. shinn2023reflexion**\n```\ntitle={Reflexion: Language Agents with Verbal Reinforcement Learning},\nauthor={Noah Shinn and Federico Cassano and Edward Berman and Ashwin Gopinath and Karthik Narasimhan and Shunyu Yao},\nbooktitle={Advances in Neural Information Processing Systems (NeurIPS)},\nyear={2023},\n```\nContext: related_work.tex line 21: \"Reflexion \\citep{shinn2023reflexion} iteratively refine code using execution outcomes.\"\n\n**40. spiess2025calibration**\n```\ntitle={Calibration and Correctness of Language Models for Code},\nauthor={Claudio Spiess and David Gros and others},\nbooktitle={Proceedings of the 47th IEEE/ACM International Conference on Software Engineering (ICSE)},\nyear={2025},\nurl={https://arxiv.org/abs/2402.02047},\n```\nContext: related_work.tex line 48: \"\\citet{spiess2025calibration} specifically addressed calibration for code models.\"\nContext: appendix.tex line 546: \"\\citep{spiess2025calibration}\"\n\n**41. steenhoek2024deepdfa**\n```\ntitle={Dataflow Analysis-Inspired Deep Learning for Efficient Vulnerability Detection},\nauthor={Benjamin Steenhoek and Hongyang Gao and Wei Le},\nbooktitle={Proceedings of the 46th IEEE/ACM International Conference on Software Engineering (ICSE)},\nyear={2024},\ndoi={10.1145/3597503.3623345},\n```\nContext: related_work.tex line 16: \"DeepDFA \\citep{steenhoek2024deepdfa}...combined classical program analysis with deep learning for defect detection.\"\n\n**42. swayamdipta2020cartography**\n```\ntitle={Dataset Cartography: Mapping and Diagnosing Datasets with Training Dynamics},\nauthor={Swabha Swayamdipta and Roy Schwartz and Nicholas Lourie and Yizhong Wang and Hannaneh Hajishirzi and Noah A. Smith and Yejin Choi},\nbooktitle={Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\npages={9275--9293}, year={2020},\ndoi={10.18653/v1/2020.emnlp-main.746},\n```\nContext: related_work.tex line 51: \"dataset cartography via training dynamics \\citep{swayamdipta2020cartography}\"\n\n**43. tian2020patchcorrectness**\n```\ntitle={Evaluating Representation Learning of Code Changes for Predicting Patch Correctness in Program Repair},\nauthor={Haoye Tian and Kui Liu and Abdoul Kader Kaboré and Anil Koyuncu and Li Li and Jacques Klein and Tegawendé F. Bissyandé},\nbooktitle={Proceedings of the 35th IEEE/ACM International Conference on Automated Software Engineering (ASE)},\npages={981--992}, year={2020},\ndoi={10.1145/3324884.3416532},\n```\nContext: related_work.tex line 17: \"\\citet{tian2020patchcorrectness} evaluated change representations for predicting repair correctness.\"\n\n**44. tian2024debugbench**\n```\ntitle={DebugBench: Evaluating Debugging Capability of Large Language Models},\nauthor={Runchu Tian and Yining Ye and Yujia Qin and Xin Cong and Yankai Lin and Yinxu Pan and Yesai Wu and Haotian Hui and Weichuan Liu and Zhiyuan Liu and Maosong Sun},\nbooktitle={Findings of the Association for Computational Linguistics: ACL 2024},\nyear={2024},\nurl={https://arxiv.org/abs/2401.04621},\n```\nContext: experiments.tex line 126: \"DebugBench \\citep{tian2024debugbench} ($N{=}426$) preserves the component ranking\"\nContext: appendix.tex line 616: cited in cross-dataset generalization section.\n\n**45. wang2025dcsh**\n```\ntitle={Do Code Semantics Help? A Comprehensive Study on Execution Trace-Based Information for Code Large Language Models},\nauthor={Jian Wang and Xiaofei Xie and Qiang Hu and Shangqing Liu and Yi Li},\nbooktitle={Findings of the Association for Computational Linguistics: EMNLP 2025},\nyear={2025},\nurl={https://arxiv.org/abs/2509.11686},\n```\nContext: introduction.tex line 4, 12: cited for incorporating traces and for finding no single trace representation consistently outperforms.\nContext: related_work.tex line 6: \"\\citet{wang2025dcsh} found trace utility to be task- and format-dependent\"\n\n**46. wang2025inspectcoder**\n```\ntitle={InspectCoder: Dynamic Analysis-Enabled Self Repair through Interactive LLM-Debugger Collaboration},\nauthor={Yunkun Wang and Yue Zhang and Guochang Li and Chen Zhi and Binhua Li and Fei Huang and Yongbin Li and Shuiguang Deng},\njournal={arXiv preprint arXiv:2510.18327},\nyear={2025},\nurl={https://arxiv.org/abs/2510.18327},\n```\nContext: related_work.tex line 10: \"InspectCoder \\citep{wang2025inspectcoder} apply selective trace extraction for automated debugging\"\n\n## Output format for each entry:\n```\n[key] Author(year) \"First 5 words of title...\"\n  Exists: ✓/✗  Authors: ✓/✗  Year: ✓/✗  Title: ✓/✗  Venue: ✓/✗  arXiv: ✓/✗/N/A\n  Citation context: [file:line] ✓/✗ — [explanation]\n  Issues: [if any]\n```\n\nSearch for each paper title using WebSearch with quotes around the title. Report your findings thoroughly.\n"
  }
}
````

</details>

---

### Tool result

_source line 102 · 2026-05-26T10:27:35.586721+00:00_

Web search results for query: ""Chain of Execution Supervision Promotes General Reasoning" Nuo Chen Zehua Li NeurIPS 2025"

Links: [{"title":"Chain of Execution Supervision Promotes General Reasoning in Large Language Models | OpenReview","url":"https://openreview.net/forum?id=QjnKsujXVG"},{"title":"NeurIPS Poster Chain of Execution Supervision Promotes General Reasoning in Large Language Models","url":"https://neurips.cc/virtual/2025/loc/san-diego/poster/118108"},{"title":"Chain of Execution Supervision Promotes General ...","url":"https://neurips.cc/media/neurips-2025/Slides/118108_wlRR5Wc.pdf"},{"title":"[2510.23629] Chain of Execution Supervision Promotes General Reasoning in Large Language Models","url":"https://arxiv.org/abs/2510.23629"},{"title":"Chain of Execution Supervision Promotes General Reasoning in Large Language Models","url":"https://arxiv.org/html/2510.23629"},{"title":"Nuo Chen | OpenReview","url":"https://openreview.net/profile?id=%7ENuo_Chen1"},{"title":"Zehua Li | OpenReview","url":"https://openreview.net/profile?id=~Zehua_Li2"},{"title":"NeurIPS 2025 Friday 12/5","url":"https://neurips.cc/virtual/2025/day/12/5"}]

I found the paper! Here are the search results for "Chain of Execution Supervision Promotes General Reasoning" by Nuo Chen, Zehua Li, and colleagues at NeurIPS 2025:

## Paper Overview

The paper addresses building robust and general reasoning ability in large language models by using code as a rich training source, given its inherent logical structure and diverse reasoning paradigms such as divide-and-conquer, topological ordering, and enumeration.

## Key Contribution

The authors introduce TracePile, a large-scale corpus of 2.6 million samples that transforms code execution into explicit, step-by-step chain-of-thought-style rationales, which they call Chain of Execution (CoE). The corpus spans domains including mathematics, classical algorithms and algorithmic competition, and is enriched with variable-tracing questions and code r
…[truncated 759 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "elapsed_ms": 4
}
```

</details>

---

### Tool call

_source line 103 · 2026-05-26T10:27:35.586893+00:00_

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
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"DeepSeek-Coder: When the Large Language Model Meets Programming\" arXiv 2401.14196"
  }
}
```

</details>

---

### Tool result

_source line 104 · 2026-05-26T10:27:35.587044+00:00_

Web search results for query: ""DeepSeek-Coder: When the Large Language Model Meets Programming" arXiv 2401.14196"

Links: [{"title":"[2401.14196] DeepSeek-Coder: When the Large Language Model Meets Programming -- The Rise of Code Intelligence","url":"https://arxiv.org/abs/2401.14196"},{"title":"DeepSeek-Coder: When the Large Language Model Meets ...","url":"https://arxiv.org/pdf/2401.14196"},{"title":"[PDF] DeepSeek-Coder: When the Large Language Model Meets Programming - The Rise of Code Intelligence | Semantic Scholar","url":"https://www.semanticscholar.org/paper/DeepSeek-Coder:-When-the-Large-Language-Model-Meets-Guo-Zhu/1f2a20a6efaf83214861dddae4a38a83ae18fe32"},{"title":"[2401.14196] DeepSeek-Coder: When the Large Language Model Meets Programming - The Rise of Code Intelligence","url":"https://ar5iv.labs.arxiv.org/html/2401.14196"},{"title":"GitHub - deepseek-ai/DeepSeek-Coder: DeepSeek Coder: Let the Code Write Itself · GitHub","url":"https://github.com/deepseek-ai/DeepSeek-Coder"},{"title":"[2401.14196v2] DeepSeek-Coder: When the Large Language Model Meets Programming -- The Rise of Code Intelligence","url":"https://arxiv.org/abs/2401.14196v2"},{"title":"Paper page - DeepSeek-Coder: When the Large Language Model Meets Programming -- The Rise of Code Intelligence","url":"https://huggingface.co/papers/2401.14196"},{"title":"Open-Source Code Language Models: DeepSeek, Qwen, and Beyond","url":"https://blog.premai.io/open-source-code-language-models-deepseek-qwen-and-beyond/"}]

I found the paper! Here's information about the arXiv paper "DeepSeek-Coder: When the Large Language Model Meets Programming" (arXiv 2401.14196):

## Overview

The DeepSeek-Coder series is a range of open-source code models with sizes from 1.3B to 33B, trained from scratch on 2 trillion tokens. These models are pre-trained on a high-quality project-level code corpus and employ a fill-in-the-blank task with a 16K window to enhance code generation and infilling.

## Performance

DeepSeek-Co
…[truncated 911 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 105 · 2026-05-26T10:27:35.587201+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"TRACED: Execution-aware Pre-training for Source Code\" Ding Steenhoek Pei Kaiser ICSE 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"TRACED: Execution-aware Pre-training for Source Code\" Ding Steenhoek Pei Kaiser ICSE 2024"
  }
}
```

</details>

---

### Tool result

_source line 106 · 2026-05-26T10:27:35.587476+00:00_

Web search results for query: ""TRACED: Execution-aware Pre-training for Source Code" Ding Steenhoek Pei Kaiser ICSE 2024"

Links: [{"title":"TRACED: Execution-aware Pre-training for Source Code Yangruibo Ding","url":"https://arxiv.org/pdf/2306.07487"},{"title":"TRACED: Execution-aware Pre-training for Source Code - Benjamin Steenhoek","url":"https://benjijang.com/publication/2024-04-14-traced"},{"title":"[2306.07487] TRACED: Execution-aware Pre-training for Source Code","url":"https://arxiv.org/abs/2306.07487"},{"title":"TRACED: Execution-aware Pre-training for Source Code | Request PDF","url":"https://www.researchgate.net/publication/378027102_TRACED_Execution-aware_Pre-training_for_Source_Code"},{"title":"TRACED: Execution-aware Pre-training for Source Code | Proceedings of the IEEE/ACM 46th International Conference on Software Engineering","url":"https://dl.acm.org/doi/10.1145/3597503.3608140"},{"title":"TRACED: Execution-aware Pre-training for Source Code | Proceedings of the IEEE/ACM 46th International Conference on Software Engineering","url":"https://doi.org/10.1145/3597503.3608140"},{"title":"TRACED: Execution-aware Pre-training for Source Code","url":"https://figshare.com/articles/dataset/TRACED_Execution-aware_Pre-training_for_Source_Code/27367989"},{"title":"TRACED: Execution-aware Pre-training for Source Code","url":"https://arxiv.org/html/2306.07487"}]

I found the paper you're looking for! Here's the information about TRACED:

**TRACED: Execution-aware Pre-training for Source Code** is a paper by Yangruibo Ding, Benjamin Steenhoek, Kexin Pei, Gail Kaiser, Wei Le, and Baishakhi Ray, published in 2024 at the IEEE/ACM 46th International Conference on Software Engineering (ICSE '24) in April 14–20, 2024, in Lisbon, Portugal.

**Overview:**

The paper introduces TRACED, an execution-aware pre-training strategy for source code to close the gap between the static nature of language models and the dynamic characteristics of programs.

**Key Contribution:**

T
…[truncated 860 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 107 · 2026-05-26T10:27:35.587636+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Making LLMs Program Interpreters via Execution Trace Chain of Thought\" Eguchi Akiba ICML 2025 PRAL workshop"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Making LLMs Program Interpreters via Execution Trace Chain of Thought\" Eguchi Akiba ICML 2025 PRAL workshop"
  }
}
```

</details>

---

### Tool result

_source line 108 · 2026-05-26T10:27:35.587776+00:00_

Web search results for query: "LoRA ICLR 2022 "10th International Conference on Learning Representations""

Links: [{"title":"2022 International Conference on Learning Representations (ICLR2022) | IEEE Information Theory Society","url":"https://www.itsoc.org/event/10th-international-conference-learning-representations-iclr"},{"title":"State of Representation Learning — ICLR 2022 | by Georgian | Georgian Impact Blog | Medium","url":"https://medium.com/georgian-impact-blog/state-of-representation-learning-iclr-2022-2645dc5a4f49"},{"title":"ICLR 2022 : The Tenth International Conference on Learning Representations","url":"http://www.wikicfp.com/cfp/servlet/event.showcfp?eventid=137564"},{"title":"Published as a conference paper at ICLR 2022","url":"https://openreview.net/pdf?id=nZeVKeeFYf9"},{"title":"2022 Conference","url":"https://iclr.cc/Conferences/2022"},{"title":"dblp: ICLR","url":"https://dblp.org/db/conf/iclr/index.html"},{"title":"LoRA: Low-Rank Adaptation of Large Language Models | OpenReview","url":"https://openreview.net/forum?id=nZeVKeeFYf9"},{"title":"ICLR 2022 - Naver Labs Europe","url":"https://europe.naverlabs.com/updates/tenth-international-conference-on-learning-representations-iclr-2022/"}]

Based on the search results, I found relevant information about your query:

## ICLR 2022 Conference

The 10th International Conference on Learning Representations (ICLR) took place virtually from April 25 to 29, 2022.

## LoRA at ICLR 2022

LoRA (Low-Rank Adaptation) was published as a poster at ICLR 2022, and it appears to be a significant contribution to the field. The paper proposes a Low-Rank Adaptation (LoRA) approach based on the hypothesis that the change in weights during model adaptation has a low "intrinsic rank".

Compared to GPT-3 175B fine-tuned with Adam, LoRA can reduce the number of trainable parameters by a factor of 10,000 and the GPU memory requirement by a factor of 3. LoRA performs on-par or better than fine-tuning in model quality on RoBER
…[truncated 328 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool result

_source line 109 · 2026-05-26T10:27:35.587937+00:00_

Web search results for query: ""A Large-Scale Empirical Study of Just-in-Time Quality Assurance" Kamei Shihab Adams Hassan 2013"

Links: [{"title":"(PDF) A Large-Scale Empirical Study of Just-in-Time Quality Assurance","url":"https://www.researchgate.net/publication/260648765_A_Large-Scale_Empirical_Study_of_Just-in-Time_Quality_Assurance"},{"title":"[PDF] A large-scale empirical study of just-in-time quality assurance | Semantic Scholar","url":"https://www.semanticscholar.org/paper/A-large-scale-empirical-study-of-just-in-time-Kamei-Shihab/04eb410c0a59fc08a4648af43f7de323cc7d06c2"},{"title":"A Large-Scale Empirical Study of Just-in-Time Quality Assurance","url":"https://posl.ait.kyushu-u.ac.jp/~kamei/publications/Kamei_TSE2013.pdf"},{"title":"A large-scale empirical study of just-in-time quality assurance - PolyPublie","url":"https://publications.polymtl.ca/13693/"},{"title":"A large-scale empirical study of just-in-time quality assurance - Kyushu University Pure Portal Site","url":"https://kyushu-u.elsevierpure.com/en/publications/a-large-scale-empirical-study-of-just-in-time-quality-assurance/"},{"title":"Publications - POSL: Y. Kamei, E. Shihab, B. Adams, A. E. Hassan, A. Mockus, A. Sinha, and N. Ubayashi, A Large-Scale Empirical Study of Just-In-Time Quality Assurance, 2013.","url":"https://posl.ait.kyushu-u.ac.jp/pman3/pman3.cgi?D=322"},{"title":"A Large-Scale Empirical Study of Just-in-Time Quality Assurance","url":"https://repository.usthb.dz/xmlui/handle/123456789/9054"},{"title":"(PDF) A large-scale empirical study of just-in-time quality assurance","url":"https://www.academia.edu/30808766/A_large-scale_empirical_study_of_just-in-time_quality_assurance"},{"title":"An Empirical Study on Data Sampling for Just-in-Time Defect Prediction | Artificial Intelligence and Security","url":"https://dl.acm.org/doi/10.1007/978-3-030-78612-0_5"}]

I found the paper you're looking for. Here are the key details:

"A Large-Scale Empirical Study of Just-in-Time Quality Assu
…[truncated 949 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 110 · 2026-05-26T10:27:35.588089+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"A Quantitative and Qualitative Evaluation of LLM-Based Explainable Fault Localization\" Kang An Yoo AutoFL 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"A Quantitative and Qualitative Evaluation of LLM-Based Explainable Fault Localization\" Kang An Yoo AutoFL 2024"
  }
}
```

</details>

---

### Tool result

_source line 111 · 2026-05-26T10:27:35.588246+00:00_

Web search results for query: ""A Quantitative and Qualitative Evaluation of LLM-Based Explainable Fault Localization" Kang An Yoo AutoFL 2024"

Links: [{"title":"A Quantitative and Qualitative Evaluation of LLM-Based Explainable Fault Localization | Proceedings of the ACM on Software Engineering","url":"https://dl.acm.org/doi/10.1145/3660771"},{"title":"[2308.05487] A Quantitative and Qualitative Evaluation of LLM-Based Explainable Fault Localization","url":"https://arxiv.org/abs/2308.05487"},{"title":"A Quantitative and Qualitative Evaluation of LLM-based Explainable Fault Localization (FSE 2024 - Posters) - FSE 2024","url":"https://2024.esec-fse.org/details/fse-2024-posters/19/A-Quantitative-and-Qualitative-Evaluation-of-LLM-based-Explainable-Fault-Localization"},{"title":"A Quantitative and Qualitative Evaluation of LLM-based Explainable Fault Localization (FSE 2024 - Research Papers) - FSE 2024","url":"https://2024.esec-fse.org/details/fse-2024-research-papers/15/A-Quantitative-and-Qualitative-Evaluation-of-LLM-based-Explainable-Fault-Localization"},{"title":"[PDF] A Quantitative and Qualitative Evaluation of LLM-Based Explainable Fault Localization | Semantic Scholar","url":"https://www.semanticscholar.org/paper/A-Quantitative-and-Qualitative-Evaluation-of-Fault-Kang-An/9ac304b5531d5adc1b5021dfc0dbe6e90b41c406"},{"title":"A Quantitative and Qualitative Evaluation of LLM-Based ...","url":"https://coinse.github.io/publications/pdfs/Kang2024ay.pdf"},{"title":"A Quantitative and Qualitative Evaluation of LLM-Based Explainable Fault Localization | Request PDF","url":"https://www.researchgate.net/publication/382236264_A_Quantitative_and_Qualitative_Evaluation_of_LLM-Based_Explainable_Fault_Localization"},{"title":"A Quantitative and Qualitative Evaluation of LLM-Based Explainable Fault Localization","url":"https://arxiv.org/html/2308.05487v3"},{"title":"A Quantitative and Qualitative Evaluation of LLM-Based Explainable Fault","url":"https://smkang96.github.io/assets
…[truncated 1461 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 112 · 2026-05-26T10:27:35.588402+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Compressing Context to Enhance Inference Efficiency of Large Language Models\" Li Dong Guerin Lin EMNLP 2023 Selective Context"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Compressing Context to Enhance Inference Efficiency of Large Language Models\" Li Dong Guerin Lin EMNLP 2023 Selective Context"
  }
}
```

</details>

---

### Tool result

_source line 113 · 2026-05-26T10:27:35.588546+00:00_

Web search results for query: ""Compressing Context to Enhance Inference Efficiency of Large Language Models" Li Dong Guerin Lin EMNLP 2023 Selective Context"

Links: [{"title":"Compressing Context to Enhance Inference Efficiency of Large Language Models - ACL Anthology","url":"https://aclanthology.org/2023.emnlp-main.391/"},{"title":"Compressing Context to Enhance Inference Efficiency of Large Language Models - Research Explorer The University of Manchester","url":"https://research.manchester.ac.uk/en/publications/compressing-context-to-enhance-inference-efficiency-of-large-lang/"},{"title":"[2310.06201] Compressing Context to Enhance Inference Efficiency of Large Language Models","url":"https://arxiv.org/abs/2310.06201"},{"title":"Compressing Context to Enhance Inference Efficiency of Large Language Models | OpenReview","url":"https://openreview.net/forum?id=cjbdRN8Yxy"},{"title":"Compressing Context to Enhance Inference Efficiency of Large Language Models","url":"https://www.researchgate.net/publication/376401484_Compressing_Context_to_Enhance_Inference_Efficiency_of_Large_Language_Models"},{"title":"selective-context · PyPI","url":"https://pypi.org/project/selective-context/"},{"title":"GitHub - liyucheng09/Selective_Context: Compress your input to ChatGPT or other LLMs, to let them process 2x more content and save 40% memory and GPU time. · GitHub","url":"https://github.com/liyucheng09/Selective_Context"},{"title":"[PDF] Compressing Context to Enhance Inference Efficiency of Large Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Compressing-Context-to-Enhance-Inference-Efficiency-Li-Dong/b12541867632737e826b7b01c7fbe1c4222d8655"}]

I found the paper you're looking for. Here are the key details:

## Paper Information

The paper "Compressing Context to Enhance Inference Efficiency of Large Language Models" was authored by Yucheng Li, Bo Dong, Frank Guerin, and Chenghua Lin, and it was published in the Proceedings of the 2023 Confer
…[truncated 1223 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 114 · 2026-05-26T10:27:35.588697+00:00_

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
  "session": "worker_audit_citation-verify-w2_20260526T101532",
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

_source line 115 · 2026-05-26T10:27:35.588820+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 116 · 2026-05-26T10:27:35.588938+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Qwen2.5-Coder Technical Report\" arXiv 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Qwen2.5-Coder Technical Report\" arXiv 2024"
  }
}
```

</details>

---

### Tool result

_source line 117 · 2026-05-26T10:27:35.589064+00:00_

Web search results for query: ""Qwen2.5-Coder Technical Report" arXiv 2024"

Links: [{"title":"[2409.12186] Qwen2.5-Coder Technical Report","url":"https://arxiv.org/abs/2409.12186"},{"title":"2025-01-06 Qwen2.5 Technical Report Qwen Team https://huggingface.co/Qwen","url":"https://arxiv.org/pdf/2412.15115"},{"title":"Technical Report Qwen2.5-Coder Technical Report Binyuan Hui* Jian Yang*","url":"https://arxiv.org/pdf/2409.12186"},{"title":"Qwen2.5-Coder Technical Report","url":"https://arxiv.org/html/2409.12186v2"},{"title":"[2409.12186v3] Qwen2.5-Coder Technical Report","url":"https://arxiv.org/abs/2409.12186v3"},{"title":"Qwen2.5-Coder Technical Report | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/qwen25-coder-technical-report"},{"title":"Qwen2.5 Technical Report - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv241215115Q/abstract"},{"title":"Paper page - Qwen2.5-Coder Technical Report","url":"https://huggingface.co/papers/2409.12186"}]

I found the Qwen2.5-Coder Technical Report on arXiv. Here are the key details:

**Paper Information:**
- The paper was submitted on September 18, 2024 (arXiv:2409.12186)
- It introduces the Qwen2.5-Coder series, a significant upgrade from its predecessor, CodeQwen1.5

**Model Details:**
- The series includes six models: Qwen2.5-Coder-(0.5B/1.5B/3B/7B/14B/32B)
- As a code-specific model, Qwen2.5-Coder is built upon the Qwen2.5 architecture and continues pretrained on a vast corpus of over 5.5 trillion tokens

**Key Capabilities:**
- Through meticulous data cleaning, scalable synthetic data generation, and balanced data mixing, Qwen2.5-Coder demonstrates impressive code generation capabilities while retaining general and math skills
- The models have been evaluated on a wide range of code-related tasks, achieving state-of-the-art (SOTA) performance across more than 10 benchmarks, including code generation, completion, reasoning, and repair, consistently outperforming larger models of the same mode
…[truncated 177 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 118 · 2026-05-26T10:27:35.589213+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Code Llama: Open Foundation Models for Code\" Rozière arXiv 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Code Llama: Open Foundation Models for Code\" Rozière arXiv 2023"
  }
}
```

</details>

---

### Tool result

_source line 119 · 2026-05-26T10:27:35.589375+00:00_

Web search results for query: ""Code Llama: Open Foundation Models for Code" Rozière arXiv 2023"

Links: [{"title":"[2308.12950] Code Llama: Open Foundation Models for Code","url":"https://arxiv.org/abs/2308.12950"},{"title":"Code Llama: Open Foundation Models for Code","url":"https://arxiv.org/html/2308.12950v3"},{"title":"[PDF] Code Llama: Open Foundation Models for Code | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Code-Llama:-Open-Foundation-Models-for-Code-Rozi%C3%A8re-Gehring/0b0debb710366cdff461938c80763eace1651af6"},{"title":"GitHub - sadkowsk/codellama-Aug.2023: Learn about \"Code Llama: Open Foundation Models for Code\" (24 Aug. 2023) by Meta AI. · GitHub","url":"https://github.com/sadkowsk/codellama-Aug.2023"},{"title":"Paper page - Code Llama: Open Foundation Models for Code","url":"https://huggingface.co/papers/2308.12950"},{"title":"[2308.12950v3] Code Llama: Open Foundation Models for Code","url":"https://arxiv.org/abs/2308.12950v3"},{"title":"[2308.12950v2] Code Llama: Open Foundation Models for Code","url":"https://arxiv.org/abs/2308.12950v2"},{"title":"[2308.12950] Code Llama: Open Foundation Models for Code","url":"http://export.arxiv.org/abs/2308.12950"},{"title":"(PDF) Code Llama: Open Foundation Models for Code","url":"https://www.researchgate.net/publication/373364143_Code_Llama_Open_Foundation_Models_for_Code"}]

I found the paper you're looking for. Here are the key details:

**Title:** Code Llama: Open Foundation Models for Code

**Authors:** Baptiste Rozière, Jonas Gehring, Fabian Gloeckle, Sten Sootla, Itai Gat, Xiaoqing Ellen Tan, Yossi Adi, Jingyu Liu, Romain Sauvestre, Tal Remez, Jérémy Rapin, Artyom Kozhevnikov, Ivan Evtimov, Joanna Bitton, Manish Bhatt, Cristian Canton Ferrer, Aaron Grattafiori, Wenhan Xiong, Alexandre Défossez, Jade Copet, Faisal Azhar, Hugo Touvron, Louis Martin, Nicolas Usunier, Thomas Scialom, Gabriel Synnaeve

**Publication Date:** Submitted on 24 Aug 2023 (v1), revised 25 Aug 2023 (v2), lates
…[truncated 496 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 120 · 2026-05-26T10:27:35.589520+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"How to Train Data-Efficient LLMs\" Sachdeva arXiv 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"How to Train Data-Efficient LLMs\" Sachdeva arXiv 2024"
  }
}
```

</details>

---

### Tool call

_source line 121 · 2026-05-26T10:27:35.589654+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Code Execution with Pre-trained Language Models\" Chenxiao Liu Shuai Lu ACL 2023 Findings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Code Execution with Pre-trained Language Models\" Chenxiao Liu Shuai Lu ACL 2023 Findings"
  }
}
```

</details>

---

### Tool call

_source line 122 · 2026-05-26T10:27:35.589808+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

````json
{
  "description": "Verify bib entries group 5 (47-57)",
  "prompt": "You are verifying academic paper references for correctness. For each bib entry below, use WebSearch to search for the paper title (in quotes) and verify:\na) Paper exists (MOST IMPORTANT)\nb) Author names (first and last author spelling)\nc) Year\nd) Title accuracy\ne) Venue correctness\nf) arXiv ID if present\n\nAlso check that each citation is used correctly in context (I provide the citation contexts).\n\n## Entries to verify (Group 5):\n\n**47. wang2025openhands**\n```\ntitle={OpenHands: An Open Platform for AI Software Developers as Generalist Agents},\nauthor={Xingyao Wang and Boxuan Li and Yufan Song and Frank F. Xu and Xiangru Tang and Mingchen Zhuge and Jiayi Pan and Yueqi Song and Bowen Li and Jaskirat Singh and Hoang Tran and Fuqiang Li and Ren Ma and Mingzhang Zheng and Bill Qian and Daniel Shao and Niklas Muennighoff and Yizhe Zhang and Binyuan Hui and Junyang Lin and Robert Brennan and Hao Peng and Heng Ji and Graham Neubig},\nbooktitle={Proceedings of the 13th International Conference on Learning Representations (ICLR)},\nyear={2025},\nurl={https://arxiv.org/abs/2407.16741},\n```\nContext: related_work.tex line 20: \"OpenHands \\citep{wang2025openhands} all incorporate execution feedback in repair workflows\"\n\n**48. widyasari2024fusefl**\n```\ntitle={Demystifying Faulty Code: Step-by-Step Reasoning for Explainable Fault Localization},\nauthor={Ratnadira Widyasari and Jia Wei Ang and Truong Giang Nguyen and Neil Sharma and David Lo},\nbooktitle={Proceedings of the IEEE International Conference on Software Analysis, Evolution and Reengineering (SANER)},\nyear={2024},\n```\nContext: related_work.tex line 18: \"FuseFL \\citep{widyasari2024fusefl}...demonstrated that structured fault signals improve localization\"\n\n**49. wong2014dstar**\n```\ntitle={Software Fault Localization Using DStar (D*)},\nauthor={W. Eric Wong and Vidroha Debroy and Ruizhi Gao and Yihao Li},\njournal={Journal of Systems and Software},\nvolume={91}, pages={44--58}, year={2014},\ndoi={10.1016/j.jss.2013.12.020},\n```\nContext: related_work.tex line 19: \"SBFL ranks program elements by suspiciousness from test spectra \\citep{abreu2007accuracy,jones2002visualization,wong2014dstar}\"\n\n**50. xia2024agentless**\n```\ntitle={Agentless: Demystifying LLM-based Software Engineering Agents},\nauthor={Chunqiu Steven Xia and Yinlin Deng and Soren Dunn and Lingming Zhang},\njournal={arXiv preprint arXiv:2407.01489},\nyear={2024},\nurl={https://arxiv.org/abs/2407.01489},\n```\nContext: related_work.tex line 20: \"Agentless \\citep{xia2024agentless}...incorporate execution feedback in repair workflows\"\n\n**51. xie2023doremi**\n```\ntitle={DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining},\nauthor={Sang Michael Xie and Hieu Pham and Xuanyi Dong and Nan Du and Hanxiao Liu and Yifeng Lu and Percy Liang and Quoc V. Le and Tengyu Ma and Adams Wei Yu},\nbooktitle={Advances in Neural Information Processing Systems (NeurIPS)},\nyear={2023},\nurl={https://arxiv.org/abs/2305.10429},\n```\nContext: related_work.tex line 51: \"data selection methods \\citep{sachdeva2024dataefficient,xie2023doremi}\"\n\n**52. xu2025cruxevalx**\n```\ntitle={CRUXEval-X: A Benchmark for Multilingual Code Reasoning, Understanding and Execution},\nauthor={Ruiyang Xu and others},\nbooktitle={Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (ACL)},\nyear={2025},\nurl={https://arxiv.org/abs/2408.13001},\n```\nContext: related_work.tex line 8: \"CRUXEval-X \\citep{xu2025cruxevalx}, established execution reasoning benchmarks\"\n\n**53. yadavally2024slicing**\n```\ntitle={A Learning-Based Approach to Static Program Slicing},\nauthor={Aashish Yadavally and Yi Li and Shaohua Wang and Tien N. Nguyen},\nbooktitle={Proceedings of the ACM on Programming Languages (OOPSLA)},\nyear={2024},\ndoi={10.1145/3649814},\n```\nContext: related_work.tex line 16: \"learned program slicing \\citep{yadavally2024slicing} combined classical program analysis with deep learning for defect detection.\"\n\n**54. yang2024generalization**\n```\ntitle={Unveiling the Generalization Power of Fine-Tuned Large Language Models},\nauthor={Haoran Yang and Yumeng Zhang and Jiaqi Xu and Hongyuan Lu and Pheng Ann Heng and Wai Lam},\nbooktitle={Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL)},\nyear={2024},\nurl={https://arxiv.org/abs/2403.09162},\n```\nContext: related_work.tex line 52: \"\\citet{yang2024generalization} further showed that fine-tuned LLMs generalize better on concise inputs\"\nContext: appendix.tex line 655: \"confounded by tokenizer efficiency and base model differences \\citep{yang2024generalization}\"\n\n**55. yang2024sweagent**\n```\ntitle={SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering},\nauthor={John Yang and Carlos E. Jimenez and Alexander Wettig and Kilian Lieret and Shunyu Yao and Karthik Narasimhan and Ofir Press},\nbooktitle={Advances in Neural Information Processing Systems (NeurIPS)},\nyear={2024},\nurl={https://arxiv.org/abs/2405.15793},\n```\nContext: related_work.tex line 20: \"SWE-agent \\citep{yang2024sweagent}...incorporate execution feedback in repair workflows\"\n\n**56. zhong2024ldb**\n```\ntitle={LDB: A Large Language Model Debugger via Verifying Runtime Execution Step by Step},\nauthor={Li Zhong and Zilong Wang and Jingbo Shang},\nbooktitle={Findings of the Association for Computational Linguistics: ACL 2024},\nyear={2024},\n```\nContext: related_work.tex line 21: \"LDB \\citep{zhong2024ldb} applies segment-level trace verification for debugging\"\n\n**57. zhou2024llm4patch**\n```\ntitle={Leveraging Large Language Model for Automatic Patch Correctness Assessment},\nauthor={Xin Zhou and Bowen Xu and Kisub Kim and DongGyun Han and Hung Huu Nguyen and Thanh Le-Cong and Junda He and Bach Le and David Lo},\njournal={IEEE Transactions on Software Engineering},\nyear={2024}, volume={50}, number={11},\n```\nContext: related_work.tex line 17: \"LLM4PatchCorrect \\citep{zhou2024llm4patch} (84.4%)\"\n\n## Output format for each entry:\n```\n[key] Author(year) \"First 5 words of title...\"\n  Exists: ✓/✗  Authors: ✓/✗  Year: ✓/✗  Title: ✓/✗  Venue: ✓/✗  arXiv: ✓/✗/N/A\n  Citation context: [file:line] ✓/✗ — [explanation]\n  Issues: [if any]\n```\n\nSearch for each paper title using WebSearch with quotes around the title. Report your findings thoroughly.\n"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "Agent",
  "tool_args": {
    "description": "Verify bib entries group 5 (47-57)",
    "prompt": "You are verifying academic paper references for correctness. For each bib entry below, use WebSearch to search for the paper title (in quotes) and verify:\na) Paper exists (MOST IMPORTANT)\nb) Author names (first and last author spelling)\nc) Year\nd) Title accuracy\ne) Venue correctness\nf) arXiv ID if present\n\nAlso check that each citation is used correctly in context (I provide the citation contexts).\n\n## Entries to verify (Group 5):\n\n**47. wang2025openhands**\n```\ntitle={OpenHands: An Open Platform for AI Software Developers as Generalist Agents},\nauthor={Xingyao Wang and Boxuan Li and Yufan Song and Frank F. Xu and Xiangru Tang and Mingchen Zhuge and Jiayi Pan and Yueqi Song and Bowen Li and Jaskirat Singh and Hoang Tran and Fuqiang Li and Ren Ma and Mingzhang Zheng and Bill Qian and Daniel Shao and Niklas Muennighoff and Yizhe Zhang and Binyuan Hui and Junyang Lin and Robert Brennan and Hao Peng and Heng Ji and Graham Neubig},\nbooktitle={Proceedings of the 13th International Conference on Learning Representations (ICLR)},\nyear={2025},\nurl={https://arxiv.org/abs/2407.16741},\n```\nContext: related_work.tex line 20: \"OpenHands \\citep{wang2025openhands} all incorporate execution feedback in repair workflows\"\n\n**48. widyasari2024fusefl**\n```\ntitle={Demystifying Faulty Code: Step-by-Step Reasoning for Explainable Fault Localization},\nauthor={Ratnadira Widyasari and Jia Wei Ang and Truong Giang Nguyen and Neil Sharma and David Lo},\nbooktitle={Proceedings of the IEEE International Conference on Software Analysis, Evolution and Reengineering (SANER)},\nyear={2024},\n```\nContext: related_work.tex line 18: \"FuseFL \\citep{widyasari2024fusefl}...demonstrated that structured fault signals improve localization\"\n\n**49. wong2014dstar**\n```\ntitle={Software Fault Localization Using DStar (D*)},\nauthor={W. Eric Wong and Vidroha Debroy and Ruizhi Gao and Yihao Li},\njournal={Journal of Systems and Software},\nvolume={91}, pages={44--58}, year={2014},\ndoi={10.1016/j.jss.2013.12.020},\n```\nContext: related_work.tex line 19: \"SBFL ranks program elements by suspiciousness from test spectra \\citep{abreu2007accuracy,jones2002visualization,wong2014dstar}\"\n\n**50. xia2024agentless**\n```\ntitle={Agentless: Demystifying LLM-based Software Engineering Agents},\nauthor={Chunqiu Steven Xia and Yinlin Deng and Soren Dunn and Lingming Zhang},\njournal={arXiv preprint arXiv:2407.01489},\nyear={2024},\nurl={https://arxiv.org/abs/2407.01489},\n```\nContext: related_work.tex line 20: \"Agentless \\citep{xia2024agentless}...incorporate execution feedback in repair workflows\"\n\n**51. xie2023doremi**\n```\ntitle={DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining},\nauthor={Sang Michael Xie and Hieu Pham and Xuanyi Dong and Nan Du and Hanxiao Liu and Yifeng Lu and Percy Liang and Quoc V. Le and Tengyu Ma and Adams Wei Yu},\nbooktitle={Advances in Neural Information Processing Systems (NeurIPS)},\nyear={2023},\nurl={https://arxiv.org/abs/2305.10429},\n```\nContext: related_work.tex line 51: \"data selection methods \\citep{sachdeva2024dataefficient,xie2023doremi}\"\n\n**52. xu2025cruxevalx**\n```\ntitle={CRUXEval-X: A Benchmark for Multilingual Code Reasoning, Understanding and Execution},\nauthor={Ruiyang Xu and others},\nbooktitle={Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (ACL)},\nyear={2025},\nurl={https://arxiv.org/abs/2408.13001},\n```\nContext: related_work.tex line 8: \"CRUXEval-X \\citep{xu2025cruxevalx}, established execution reasoning benchmarks\"\n\n**53. yadavally2024slicing**\n```\ntitle={A Learning-Based Approach to Static Program Slicing},\nauthor={Aashish Yadavally and Yi Li and Shaohua Wang and Tien N. Nguyen},\nbooktitle={Proceedings of the ACM on Programming Languages (OOPSLA)},\nyear={2024},\ndoi={10.1145/3649814},\n```\nContext: related_work.tex line 16: \"learned program slicing \\citep{yadavally2024slicing} combined classical program analysis with deep learning for defect detection.\"\n\n**54. yang2024generalization**\n```\ntitle={Unveiling the Generalization Power of Fine-Tuned Large Language Models},\nauthor={Haoran Yang and Yumeng Zhang and Jiaqi Xu and Hongyuan Lu and Pheng Ann Heng and Wai Lam},\nbooktitle={Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL)},\nyear={2024},\nurl={https://arxiv.org/abs/2403.09162},\n```\nContext: related_work.tex line 52: \"\\citet{yang2024generalization} further showed that fine-tuned LLMs generalize better on concise inputs\"\nContext: appendix.tex line 655: \"confounded by tokenizer efficiency and base model differences \\citep{yang2024generalization}\"\n\n**55. yang2024sweagent**\n```\ntitle={SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering},\nauthor={John Yang and Carlos E. Jimenez and Alexander Wettig and Kilian Lieret and Shunyu Yao and Karthik Narasimhan and Ofir Press},\nbooktitle={Advances in Neural Information Processing Systems (NeurIPS)},\nyear={2024},\nurl={https://arxiv.org/abs/2405.15793},\n```\nContext: related_work.tex line 20: \"SWE-agent \\citep{yang2024sweagent}...incorporate execution feedback in repair workflows\"\n\n**56. zhong2024ldb**\n```\ntitle={LDB: A Large Language Model Debugger via Verifying Runtime Execution Step by Step},\nauthor={Li Zhong and Zilong Wang and Jingbo Shang},\nbooktitle={Findings of the Association for Computational Linguistics: ACL 2024},\nyear={2024},\n```\nContext: related_work.tex line 21: \"LDB \\citep{zhong2024ldb} applies segment-level trace verification for debugging\"\n\n**57. zhou2024llm4patch**\n```\ntitle={Leveraging Large Language Model for Automatic Patch Correctness Assessment},\nauthor={Xin Zhou and Bowen Xu and Kisub Kim and DongGyun Han and Hung Huu Nguyen and Thanh Le-Cong and Junda He and Bach Le and David Lo},\njournal={IEEE Transactions on Software Engineering},\nyear={2024}, volume={50}, number={11},\n```\nContext: related_work.tex line 17: \"LLM4PatchCorrect \\citep{zhou2024llm4patch} (84.4%)\"\n\n## Output format for each entry:\n```\n[key] Author(year) \"First 5 words of title...\"\n  Exists: ✓/✗  Authors: ✓/✗  Year: ✓/✗  Title: ✓/✗  Venue: ✓/✗  arXiv: ✓/✗/N/A\n  Citation context: [file:line] ✓/✗ — [explanation]\n  Issues: [if any]\n```\n\nSearch for each paper title using WebSearch with quotes around the title. Report your findings thoroughly.\n"
  }
}
````

</details>

---

### Tool result

_source line 123 · 2026-05-26T10:27:35.590086+00:00_

Web search results for query: ""How to Train Data-Efficient LLMs" Sachdeva arXiv 2024"

Links: [{"title":"[2402.09668] How to Train Data-Efficient LLMs","url":"https://arxiv.org/abs/2402.09668"},{"title":"[PDF] How to Train Data-Efficient LLMs | Semantic Scholar","url":"https://www.semanticscholar.org/paper/How-to-Train-Data-Efficient-LLMs-Sachdeva-Coleman/31b2918acc77682b5a499da1aa111f34e76d9603"},{"title":"Federated Data-Efficient Instruction Tuning for Large Language Models","url":"https://arxiv.org/html/2410.10926v2"},{"title":"Preference Curriculum: LLMs Should Always Be Pretrained on Their Preferred Data","url":"https://arxiv.org/html/2501.13126v1"},{"title":"Beyond Random Sampling: Efficient Language Model Pretraining via Curriculum Learning","url":"https://arxiv.org/html/2506.11300v1"},{"title":"FisherSFT: Data-Efficient Supervised Fine-Tuning of Language Models Using Information Gain","url":"https://arxiv.org/html/2505.14826v1"},{"title":"Multi-Agent Collaborative Data Selection for Efficient LLM Pretraining","url":"https://arxiv.org/html/2410.08102v1"},{"title":"How to Train Data-Efficient LLMs","url":"https://arxiv.org/pdf/2402.09668"},{"title":"GitHub - susumuota/nano-askllm: Unofficial implementation of the Ask-LLM paper 'How to Train Data-Efficient LLMs', arXiv:2402.09668. · GitHub","url":"https://github.com/susumuota/nano-askllm"}]

I found the paper you're looking for! Here's what I found about "How to Train Data-Efficient LLMs" by Sachdeva et al. (2024):

## Paper Overview

The paper seeks to understand the tradeoffs associated with data selection routines based on (i) expensive-to-compute data-quality estimates, and (ii) maximization of coverage and diversity-based measures in the feature space.

## Key Contributions

The paper proposes two main techniques:

1. **Ask-LLM**: This technique leverages the zero-shot reasoning capabilities of instruction-tuned LLMs to directly assess the quality of a training example.

2. **Density Sampling**: This meth
…[truncated 866 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 124 · 2026-05-26T10:27:35.590270+00:00_

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
  "session": "worker_audit_citation-verify-w2_20260526T101532",
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

_source line 125 · 2026-05-26T10:27:35.590410+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 126 · 2026-05-26T10:27:35.590547+00:00_

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
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Large Language Models Can Be Easily Distracted by Irrelevant Context\" Freda Shi ICML 2023"
  }
}
```

</details>

---

### Tool result

_source line 127 · 2026-05-26T10:27:35.590688+00:00_

Web search results for query: ""Making LLMs Program Interpreters via Execution Trace Chain of Thought" Eguchi Akiba ICML 2025 PRAL workshop"

Links: [{"title":"Making LLMs Program Interpreters via Execution Trace Chain of Thought | OpenReview","url":"https://openreview.net/forum?id=pFyBdPyOCQ"},{"title":"Making LLMs Program Interpreters via Execution Trace Chain of Thought","url":"https://openreview.net/pdf?id=pFyBdPyOCQ"},{"title":"Takuya Akiba | OpenReview","url":"https://openreview.net/profile?id=~Takuya_Akiba2"},{"title":"ICML Poster Revisiting Chain-of-Thought in Code Generation: Do Language Models Need to Learn Reasoning before Coding?","url":"https://icml.cc/virtual/2025/poster/43621"},{"title":"ICML 2025 Papers","url":"https://icml.cc/virtual/2025/papers.html"},{"title":"ICML Poster RLEF: Grounding Code LLMs in Execution Feedback with Reinforcement Learning","url":"https://icml.cc/virtual/2025/poster/45358"},{"title":"Accepted papers | FoRLM @ NeurIPS'25","url":"https://reasoning-workshop.github.io/accepted/"},{"title":"Track: Poster Session 5 East","url":"https://icml.cc/virtual/2025/session/50267"},{"title":"Track: Poster Session 4 West","url":"https://icml.cc/virtual/2025/session/50260"}]

I found the paper you're looking for! Here's what I found about it:

"Making LLMs Program Interpreters via Execution Trace Chain of Thought" was published at the ICML 2025 Workshop PRAL, authored by Koshi Eguchi and Takuya Akiba from Sakana AI.

The paper proposes ET-CoT (Execution Trace Chain of Thought), an approach where LLMs learn to generate a detailed and systematic program execution trace as a chain of thought to predict program outcomes.

The authors developed a new Python interpreter called PyTracify which outputs execution traces, generated a large number of traces, and fine-tuned an LLM using them, allowing the LLMs to execute Python programs consistently by generating the trace as a CoT. Their fine-tuned model outperforms other models of comparable size on c
…[truncated 255 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool call

_source line 128 · 2026-05-26T10:27:35.590927+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"OpenHands: An Open Platform for AI Software Developers as Generalist Agents\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"OpenHands: An Open Platform for AI Software Developers as Generalist Agents\""
  }
}
```

</details>

---

### Tool result

_source line 129 · 2026-05-26T10:27:35.591138+00:00_

Web search results for query: ""Code Execution with Pre-trained Language Models" Chenxiao Liu Shuai Lu ACL 2023 Findings"

Links: [{"title":"Code Execution with Pre-trained Language Models - ACL Anthology","url":"https://aclanthology.org/2023.findings-acl.308/"},{"title":"Code Execution with Pre-trained Language Models","url":"https://aclanthology.org/2023.findings-acl.308.pdf"},{"title":"[2305.05383] Code Execution with Pre-trained Language Models","url":"https://arxiv.org/abs/2305.05383"},{"title":"Code Execution with Pre-trained Language Models | Request PDF","url":"https://www.researchgate.net/publication/372915950_Code_Execution_with_Pre-trained_Language_Models"},{"title":"Code Execution with Pre-trained Language Models - Microsoft Research","url":"https://www.microsoft.com/en-us/research/publication/code-execution-with-pre-trained-language-models/"},{"title":"Shuai Lu - ACL Anthology","url":"https://aclanthology.org/people/shuai-lu/"},{"title":"Findings - ACL 2023","url":"https://2023.aclweb.org/program/accepted_findings/"},{"title":"Papers with Code - Code Execution with Pre-trained Language Models","url":"https://paperswithcode.com/paper/code-execution-with-pre-trained-language"},{"title":"Code Execution with Pre-trained Language Models","url":"https://arxiv.org/pdf/2305.05383"},{"title":"Paper page - Code Execution with Pre-trained Language Models","url":"https://huggingface.co/papers/2305.05383"}]

I found the paper you're looking for! Here's what I found:

"Code Execution with Pre-trained Language Models" by Chenxiao Liu, Shuai Lu, Weizhu Chen, Daxin Jiang, Alexey Svyatkovskiy, Shengyu Fu, Neel Sundaresan, and Nan Duan was published in Findings of ACL 2023.

The paper addresses how most pre-trained models for code intelligence ignore the execution trace and only rely on source code and syntactic structures. The authors developed a mutation-based data augmentation technique to create a large-scale Python dataset for code execution, and presented CodeExecut
…[truncated 563 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 130 · 2026-05-26T10:27:35.591434+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "APPT IEEE TSE 2024 volume 50 number 3 Quanjun Zhang patch correctness"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "tool_args": {
    "query": "APPT IEEE TSE 2024 volume 50 number 3 Quanjun Zhang patch correctness"
  }
}
```

</details>

---

### Tool call

_source line 131 · 2026-05-26T10:27:35.591655+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"NExT: Teaching Large Language Models to Reason about Code Execution\" Ansong Ni Allamanis ICML 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"NExT: Teaching Large Language Models to Reason about Code Execution\" Ansong Ni Allamanis ICML 2024"
  }
}
```

</details>

---

### Tool result

_source line 132 · 2026-05-26T10:27:35.591871+00:00_

Web search results for query: ""Large Language Models Can Be Easily Distracted by Irrelevant Context" Freda Shi ICML 2023"

Links: [{"title":"Large Language Models Can Be Easily Distracted by Irrelevant Context","url":"https://proceedings.mlr.press/v202/shi23a.html"},{"title":"[2302.00093] Large Language Models Can Be Easily Distracted by Irrelevant Context","url":"https://arxiv.org/abs/2302.00093"},{"title":"Large language models can be easily distracted by irrelevant context | Proceedings of the 40th International Conference on Machine Learning","url":"https://dl.acm.org/doi/10.5555/3618408.3619699"},{"title":"Large Language Models Can Be Easily Distracted by Irrelevant Context","url":"https://openreview.net/pdf?id=JSZmoN03Op"},{"title":"Large Language Models Can Be Easily Distracted by Irrelevant Context. | BibSonomy","url":"https://www.bibsonomy.org/bibtex/7a5e56e46d0a590ba4f0fe0b2e3d532d"},{"title":"[Quick Review] Large Language Models Can Be Easily Distracted by Irrelevant Context","url":"https://liner.com/review/large-language-models-can-be-easily-distracted-by-irrelevant-context"},{"title":"[PDF] Large Language Models Can Be Easily Distracted by Irrelevant Context | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Large-Language-Models-Can-Be-Easily-Distracted-by-Shi-Chen/3d68522abfadfc8ee6b7ec9edaaf91f1b2f38e5e"},{"title":"(PDF) Large Language Models Can Be Easily Distracted by Irrelevant Context","url":"https://www.researchgate.net/publication/367961918_Large_Language_Models_Can_Be_Easily_Distracted_by_Irrelevant_Context"},{"title":"Large Language Models Can Be Easily Distracted by Irrelevant Context | OpenReview","url":"https://openreview.net/forum?id=JSZmoN03Op"},{"title":"ml-papers/papers/2023/230131 Large Language Models Can Be Easily Distracted by Irrelevant Context.md at main · rosinality/ml-papers","url":"https://github.com/rosinality/ml-papers/blob/main/papers/2023/230131%20Large%20Language%20Models%20Can%20Be%20Easily%20Distracted%20
…[truncated 1310 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 133 · 2026-05-26T10:27:35.592255+00:00_

Now I have all the information needed. Here are my verification results:

---

```
[ferrando2025execute] Armengol-Estapé(2025) "What I Cannot Execute, I..."
  Exists: ✓  Authors: ✓  Year: ✓  Title: ✓  Venue: ✓  arXiv: ✓
  Citation context: [related_work.tex:7] ✓ — Paper studies compact vs full execution traces for output prediction; "density finding" is a reasonable characterization.
  Issues:
    1. BIB KEY MISMATCH: The key is "ferrando2025execute" but no author named "Ferrando" exists on this paper. The first author is Jordi Armengol-Estapé. The key should be something like "armengolestape2025execute".
    2. MINOR TITLE CASING: The arXiv listing uses lowercase "cannot" → "What I cannot execute, I do not understand" while the bib uses "Cannot". This is a stylistic choice and acceptable in BibTeX.
    3. AUTHOR NAME: The bib has "Jordi Armengol-Estape" but the correct spelling is "Jordi Armengol-Estapé" (with accent on final 'e'). Non-ASCII may need LaTeX encoding: "Armengol-Estap{\'e}".
```

```
[foster2025mutation] Foster(2025) "Mutation-Guided LLM-based Test Generation..."
  Exists: ✓  Authors: ✓  Year: ✓  Title: ✓  Venue: ✓  arXiv: ✓ (2501.12862)
  Citation context: [related_work.tex:18] ✓ — Paper uses mutation outcomes (structured fault signals) to guide test generation; characterizing it as improving localization is a reasonable interpretation.
  Issues:
    1. VENUE DETAIL: The bib says "Proceedings of the ACM International Conference on the Foundations of Software Engineering (FSE), Industry Track". The official venue is "Proceedings of the 33rd ACM International Conference on the Foundations of Software Engineering" (FSE 2025). Adding "33rd" would be more precise. The conference was held in Trondheim, Norway, June 2025.
```

```
[geng2024calibration] Geng(2024) "A Survey of Confidence Estimation..."
  Exists: ✓  Authors: ✓  Year: ✓  Title: ✓  Venue: ✓  arXiv: ✓ (2311.08298)
  Citation context: [related_work.tex:48] ✓ — Paper is a comprehensive survey on L
…[truncated 4931 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "Agent",
  "elapsed_ms": 19
}
```

</details>

---

### Tool result

_source line 134 · 2026-05-26T10:27:35.592531+00:00_

Web search results for query: ""OpenHands: An Open Platform for AI Software Developers as Generalist Agents""

Links: [{"title":"[2407.16741] OpenHands: An Open Platform for AI Software Developers as Generalist Agents","url":"https://arxiv.org/abs/2407.16741"},{"title":"OpenHands: An Open Platform for AI Software Developers as Generalist Agents | OpenReview","url":"https://openreview.net/forum?id=OJd3ayDDoF"},{"title":"OpenHands: An Open Platform for AI Software Developers as Generalist Agents","url":"https://arxiv.org/html/2407.16741v3"},{"title":"OpenHands - An Open Platform for AI Software Developers as Generalist Agents | Boxuan Li","url":"https://www.li-boxuan.com/project/openhands/"},{"title":"OPENHANDS: AN OPEN PLATFORM FOR AI SOFTWARE ...","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/a4b6ad6b48850c0c331d1259fc66a69c-Paper-Conference.pdf"},{"title":"OpenHands: An Open Platform for AI Software Developers as Generalist Agents - ADS","url":"https://ui.adsabs.harvard.edu/abs/arXiv:2407.16741"},{"title":"[PDF] OpenHands: An Open Platform for AI Software Developers as Generalist Agents | Semantic Scholar","url":"https://www.semanticscholar.org/paper/OpenHands:-An-Open-Platform-for-AI-Software-as-Wang-Li/1d07e5b6f978cf69c0186f3d5f434fa92d471e46"},{"title":"Redefining Dev Workflows: Exploring OpenHands — An Open-Source AI Developer Agent | by Niar | Medium","url":"https://medium.com/@niarsdet/redefining-dev-workflows-exploring-openhands-an-open-source-ai-developer-agent-4d579c6e5f40"},{"title":"OpenHands | The Open Platform for Cloud Coding Agents","url":"https://www.openhands.dev/"},{"title":"OPENHANDS: AN OPEN PLATFORM FOR AI SOFTWARE DEVELOPERS AS GENERALIST AGENTS - Illinois Experts","url":"https://experts.illinois.edu/en/publications/openhands-an-open-platform-for-ai-software-developers-as-generali/"}]

Based on the search results, here's a summary of OpenHands:

## Overview

OpenHands is a platform for the development of powerful and flexible 
…[truncated 1395 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 135 · 2026-05-26T10:27:35.592781+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Reflexion: Language Agents with Verbal Reinforcement Learning\" Shinn NeurIPS 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Reflexion: Language Agents with Verbal Reinforcement Learning\" Shinn NeurIPS 2023"
  }
}
```

</details>

---

### Tool call

_source line 136 · 2026-05-26T10:27:35.592984+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Demystifying Faulty Code: Step-by-Step Reasoning for Explainable Fault Localization\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Demystifying Faulty Code: Step-by-Step Reasoning for Explainable Fault Localization\""
  }
}
```

</details>

---

### Tool result

_source line 137 · 2026-05-26T10:27:35.593184+00:00_

Web search results for query: ""NExT: Teaching Large Language Models to Reason about Code Execution" Ansong Ni Allamanis ICML 2024"

Links: [{"title":"[2404.14662] NExT: Teaching Large Language Models to Reason about Code Execution","url":"https://arxiv.org/abs/2404.14662"},{"title":"[PDF] NExT: Teaching Large Language Models to Reason about Code Execution | Semantic Scholar","url":"https://www.semanticscholar.org/paper/NExT:-Teaching-Large-Language-Models-to-Reason-Code-Ni-Allamanis/49306aa1fde2a21fadc77dbc8ec7e487fac72c5b"},{"title":"NExT: Teaching Large Language Models to Reason about Code Execution","url":"https://proceedings.mlr.press/v235/ni24a.html"},{"title":"NExT: Teaching Large Language Models to Reason about Code Execution | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/next-teaching-large-language-models-to-reason"},{"title":"[2404.14662v1] NExT: Teaching Large Language Models to Reason about Code Execution","url":"https://arxiv.org/abs/2404.14662v1"},{"title":"teaching large language models to reason about code execution","url":"https://dl.acm.org/doi/10.5555/3692070.3693610"},{"title":"NExT: Teaching Large Language Models to Reason about Code Execution · Miltos Allamanis","url":"https://miltos.allamanis.com/publications/2024next/"},{"title":"NExT: Teaching Large Language Models to Reason about ...","url":"https://www.emergentmind.com/papers/2404.14662"},{"title":"NExT: Teaching Large Language Models to Reason about Code Execution | OpenReview","url":"https://openreview.net/forum?id=B1W712hMBi"}]

I found the paper you were looking for. Here's what I found:

The paper "NExT: Teaching Large Language Models to Reason about Code Execution" was published by Ansong Ni, Miltiadis Allamanis, Arman Cohan, Yinlin Deng, Kensen Shi, Charles Sutton, and Pengcheng Yin in the Proceedings of the 41st International Conference on Machine Learning in 2024.

The paper addresses the issue that large language models (LLMs) of code are typically tra
…[truncated 677 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 138 · 2026-05-26T10:27:35.593449+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Mutation Testing Advances: An Analysis and Survey\" Papadakis Kintis Zhang Jia Le Traon Harman 2019"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Mutation Testing Advances: An Analysis and Survey\" Papadakis Kintis Zhang Jia Le Traon Harman 2019"
  }
}
```

</details>

---

### Tool result

_source line 139 · 2026-05-26T10:27:35.593646+00:00_

Web search results for query: "APPT IEEE TSE 2024 volume 50 number 3 Quanjun Zhang patch correctness"

Links: [{"title":"Leveraging Large Language Model for Automatic Patch Correctness Assessment | IEEE Transactions on Software Engineering","url":"https://dl.acm.org/doi/abs/10.1109/TSE.2024.3452252"},{"title":"A Survey of Learning-based Automated Program Repair | ACM Transactions on Software Engineering and Methodology","url":"https://dl.acm.org/doi/10.1145/3631974?query=%22A+Survey+of+Learning-based+Automated+Program+Repair.%22+AND+33+2+1+2024"},{"title":"GitHub - iSEngLab/APPT: [TSE 2024] APPT: Boosting Automated Patch Correctness Prediction via Fine-tuning Pre-trained Models · GitHub","url":"https://github.com/iSEngLab/APPT"},{"title":"A Systematic Literature Review on Large Language Models for Automated Program Repair | ACM Transactions on Software Engineering and Methodology","url":"https://dl.acm.org/doi/10.1145/3799693"},{"title":"Invalidator: Automated Patch Correctness Assessment Via Semantic and Syntactic Reasoning | IEEE Transactions on Software Engineering","url":"https://dl.acm.org/doi/abs/10.1109/TSE.2023.3255177"},{"title":"IEEE TRANSACTIONS ON SOFTWARE ENGINEERING, VOL. 50, NO. 4, APRIL 2024 911","url":"https://web.eecs.umich.edu/~movaghar/Testing%20LLMs%20Survey%202024.pdf"}]

Based on the search results, I found relevant information about your query. APPT is a paper published in IEEE Transactions on Software Engineering (TSE) in 2024 that focuses on boosting automated patch correctness prediction via fine-tuning pre-trained models.

The search results show that Quanjun Zhang and colleagues have published work on boosting automated patch correctness prediction via pre-trained language models in 2023, and this appears to be related to or an extension of the 2024 TSE publication on APPT.

The results indicate that the research addresses the problem of patch overfitting, where a generated patch can be incorrect although it passes all tests. The APPT ap
…[truncated 236 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 140 · 2026-05-26T10:27:35.593854+00:00_

Web search results for query: ""Reflexion: Language Agents with Verbal Reinforcement Learning" Shinn NeurIPS 2023"

Links: [{"title":"[2303.11366] Reflexion: Language Agents with Verbal Reinforcement Learning","url":"https://arxiv.org/abs/2303.11366"},{"title":"NeurIPS Poster Reflexion: language agents with verbal reinforcement learning","url":"https://neurips.cc/virtual/2023/poster/70114"},{"title":"GitHub - noahshinn/reflexion: [NeurIPS 2023] Reflexion: Language Agents with Verbal Reinforcement Learning · GitHub","url":"https://github.com/noahshinn/reflexion"},{"title":"Reflexion: Language Agents with Verbal Reinforcement Learning Noah Shinn","url":"https://proceedings.neurips.cc/paper_files/paper/2023/file/1b44b878bb782e6954cd888628510e90-Paper-Conference.pdf"},{"title":"Reflexion: Language Agents with Verbal Reinforcement Learning","url":"https://arxiv.org/html/2303.11366"},{"title":"Reflexion: language agents with verbal reinforcement learning | OpenReview","url":"https://openreview.net/forum?id=vAElhFcKW6"},{"title":"Reflexion: Language Agents with Verbal Reinforcement Learning - Princeton University","url":"https://collaborate.princeton.edu/en/publications/reflexion-language-agents-with-verbal-reinforcement-learning-2/"},{"title":"GitHub - noahshinn/reflexion: [NeurIPS 2023] Reflexion: Language Agents with Verbal Reinforcement Learning","url":"https://github.com/noahshinn/reflexion/tree/main"},{"title":"Reflexion: Language Agents with Verbal Reinforcement Learning Noah Shinn","url":"https://openreview.net/pdf?id=vAElhFcKW6"}]

I found comprehensive information about the paper "Reflexion: Language Agents with Verbal Reinforcement Learning" by Noah Shinn and colleagues.

## Overview

Reflexion is a novel framework to reinforce language agents not by updating weights, but instead through linguistic feedback. Reflexion agents verbally reflect on task feedback signals, then maintain their own reflective text in an episodic memory buffer to induce better decision-m
…[truncated 1227 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 141 · 2026-05-26T10:27:35.594026+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "APPT patch correctness IEEE Xplore TSE volume issue pages 2024",
  "allowed_domains": "['ieeexplore.ieee.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "tool_args": {
    "query": "APPT patch correctness IEEE Xplore TSE volume issue pages 2024",
    "allowed_domains": "['ieeexplore.ieee.org']"
  }
}
```

</details>

---

### Tool result

_source line 142 · 2026-05-26T10:27:35.594170+00:00_

Web search results for query: ""Demystifying Faulty Code: Step-by-Step Reasoning for Explainable Fault Localization""

Links: [{"title":"[2403.10507] Demystifying Faulty Code with LLM: Step-by-Step Reasoning for Explainable Fault Localization","url":"https://arxiv.org/abs/2403.10507"},{"title":"Demystifying Faulty Code: Step-by-Step Reasoning for Explainable Fault Localization | Request PDF","url":"https://www.researchgate.net/publication/382317610_Demystifying_Faulty_Code_Step-by-Step_Reasoning_for_Explainable_Fault_Localization"},{"title":"Demystifying Faulty Code: Step-by-Step Reasoning for Explainable Fault Localization | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/10589899/"},{"title":"Demystifying Faulty Code: Step-by-Step Reasoning for Explainable Fault Localization","url":"https://figshare.com/s/bce02cb607a6c30043ad"},{"title":"Demystifying Faulty Code with LLM: Step-by-Step Reasoning for Explainable Fault Localization","url":"https://arxiv.org/html/2403.10507v1"},{"title":"Demystifying Faulty Code: Step-by-Step Reasoning for Explainable Fault Localization - Singapore Management University","url":"https://smusg.elsevierpure.com/en/publications/demystifying-faulty-code-step-by-step-reasoning-for-explainable-f/"},{"title":"[Literature Review] Demystifying Faulty Code with LLM: Step-by-Step Reasoning for Explainable Fault Localization","url":"https://www.themoonlight.io/en/review/demystifying-faulty-code-with-llm-step-by-step-reasoning-for-explainable-fault-localization"}]

I found the paper for you! Here's what I found:

## Overview

Fault localization is a critical process that involves identifying specific program elements responsible for program failures. Manually pinpointing these elements, such as classes, methods, or statements, which are associated with a fault is laborious and time-consuming.

## The FuseFL Approach

The study investigates step-by-step reasoning for explainable fault localization and explores 
…[truncated 1150 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 143 · 2026-05-26T10:27:35.594372+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Calibration and Correctness of Language Models for Code\" Spiess ICSE 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Calibration and Correctness of Language Models for Code\" Spiess ICSE 2025"
  }
}
```

</details>

---

### Tool call

_source line 144 · 2026-05-26T10:27:35.594517+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Software Fault Localization Using DStar\" Wong Debroy Gao Li"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Software Fault Localization Using DStar\" Wong Debroy Gao Li"
  }
}
```

</details>

---

### Tool result

_source line 145 · 2026-05-26T10:27:35.594650+00:00_

Web search results for query: ""Mutation Testing Advances: An Analysis and Survey" Papadakis Kintis Zhang Jia Le Traon Harman 2019"

Links: [{"title":"Mutation Testing Advances: An Analysis and Survey | Request PDF","url":"https://www.researchgate.net/publication/325014033_Mutation_Testing_Advances_An_Analysis_and_Survey"},{"title":"[PDF] Chapter Six - Mutation Testing Advances: An Analysis and Survey | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Chapter-Six-Mutation-Testing-Advances:-An-Analysis-Papadakis-Kintis/d461ab9482b7fb5eadd7e6cd2c6dffced8ede8b8"},{"title":"Mutation Testing Advances: An Analysis and Survey - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0065245818300305"},{"title":"Mutation testing advances: An analysis and survey (chapter 6)","url":"https://alastairreid.github.io/RelatedWork/papers/papadakis:advances:2019/"},{"title":"dblp: Chapter Six - Mutation Testing Advances: An Analysis and Survey.","url":"https://dblp.org/rec/journals/ac/PapadakisK00TH19.html"},{"title":"Mutation Testing Advances: An Analysis and Survey","url":"https://scite.ai/reports/mutation-testing-advances-an-analysis-ZGEyL6y"},{"title":"Mutation Testing Advances: An Analysis and Survey","url":"https://mutationtesting.uni.lu/survey.pdf"},{"title":"Google Scholar","url":"https://scholar.google.com/scholar?q=Mike+Papadakis%2C+Marinos+Kintis%2C+Jie+Zhang%2C+Yue+Jia%2C+Yves+Le+Traon%2C+and+Mark+Harman.+2019.+Mutation+Testing+Advances%3A+An+Analysis+and+Survey.+ACM+Computing+Surveys+%28CSUR%29+51%2C+5+%282019%29%2C+1--33."},{"title":"Quantitative Metrics for Mutation Testing","url":"https://www.scitepress.org/Papers/2019/78418/78418.pdf"}]

Based on the search results, I found the publication you're looking for:

**"Chapter Six - Mutation Testing Advances: An Analysis and Survey"** by Mike Papadakis, Marinos Kintis, Jie Zhang, Yue Jia, Yves Le Traon, and Mark Harman.

The paper was published in Advances in Computers, Volume 112, pages
…[truncated 788 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 146 · 2026-05-26T10:27:35.594810+00:00_

Web search results for query: "APPT patch correctness IEEE Xplore TSE volume issue pages 2024"

Links: [{"title":"APPT: Boosting Automated Patch Correctness Prediction via Fine-Tuning Pre-Trained Models | IEEE Journals & Magazine | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/10402095/"},{"title":"Automated Patch Correctness Assessment: How Far are We? | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/9286063"},{"title":"On Reliability of Patch Correctness Assessment | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/8812054"},{"title":"Invalidator: Automated Patch Correctness Assessment Via Semantic and Syntactic Reasoning | IEEE Journals & Magazine | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/10066209/"},{"title":"Identifying Patch Correctness in Test-Based Program Repair | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/8453152"},{"title":"Leveraging Large Language Model for Automatic Patch Correctness Assessment | IEEE Journals & Magazine | IEEE Xplore","url":"https://ieeexplore.ieee.org/abstract/document/10659742/"},{"title":"Improving Patch Correctness Analysis via Random Testing and Large Language Models | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/10638611/;jsessionid=AF15DD3989EAD87F4A4DF07651D7FCCF"},{"title":"Peft: Multiline Complex Patch Correctness Assessment Based on Fine-Tuning Large Language Model with “Golden Data” | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/11173468/"},{"title":"Evaluating Representation Learning of Code Changes for Predicting Patch Correctness in Program Repair | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/abstract/document/9286101/"},{"title":"Boosting Patch Correctness Checking via Combining Code-Edit Embeddings as Additional What-to-Change Information | IEEE Conferenc
…[truncated 809 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 147 · 2026-05-26T10:27:35.594966+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"JITLine: A Simpler, Better, Faster, Finer-grained Just-In-Time Defect Prediction\" Pornprasit Tantithamthavorn MSR 2021"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"JITLine: A Simpler, Better, Faster, Finer-grained Just-In-Time Defect Prediction\" Pornprasit Tantithamthavorn MSR 2021"
  }
}
```

</details>

---

### Tool call

_source line 148 · 2026-05-26T10:27:35.595106+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "TRACED ICSE 2024 \"Ben Steenhoek\" OR \"Benjamin Steenhoek\" Yangruibo Ding"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "tool_args": {
    "query": "TRACED ICSE 2024 \"Ben Steenhoek\" OR \"Benjamin Steenhoek\" Yangruibo Ding"
  }
}
```

</details>

---

### Tool result

_source line 149 · 2026-05-26T10:27:35.595284+00:00_

Web search results for query: ""Calibration and Correctness of Language Models for Code" Spiess ICSE 2025"

Links: [{"title":"Calibration and Correctness of Language Models for Code (ICSE 2025 - Research Track) - ICSE 2025","url":"https://conf.researchr.org/details/icse-2025/icse-2025-research-track/8/Calibration-and-Correctness-of-Language-Models-for-Code"},{"title":"Calibration and Correctness of Language Models for Code Claudio Spiess∗","url":"https://www.software-lab.org/publications/icse2025_calibration.pdf"},{"title":"Calibration and Correctness of Language Models for Code | Proceedings of the IEEE/ACM 47th International Conference on Software Engineering","url":"https://dl.acm.org/doi/10.1109/ICSE55347.2025.00040"},{"title":"Calibration and Correctness of Language Models for Code ICSE Artifact","url":"https://zenodo.org/records/14744842"},{"title":"Calibration and Correctness of Language Models for Code ICSE Artifact","url":"https://explore.openaire.eu/search/result?pid=10.5281/zenodo.14744842"},{"title":"[PDF] Calibration and Correctness of Language Models for Code | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Calibration-and-Correctness-of-Language-Models-for-Spiess-Gros/65b59f4ffae4f5b9e5d63fc1d11bf9ca7f7df34d"},{"title":"[2402.02047] Calibration and Correctness of Language Models for Code","url":"https://arxiv.org/abs/2402.02047"},{"title":"47th ICSE 2025: Ottawa, ON, Canada","url":"https://dblp.org/db/conf/icse/icse2025.html"},{"title":"Calibration and Correctness of Language Models for Code | Request PDF","url":"https://www.researchgate.net/publication/392966020_Calibration_and_Correctness_of_Language_Models_for_Code"}]

I found the paper you're looking for. Here's what I found:

## "Calibration and Correctness of Language Models for Code" by Spiess et al. at ICSE 2025

The paper is authored by Claudio Spiess, David Gros, Kunal Suresh Pai, Michael Pradel, Rafiqul Rabin, Amin Alipour, Susmit Jha, Prem Devanbu, and Toufique Ahmed, and w
…[truncated 1220 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 150 · 2026-05-26T10:27:35.595480+00:00_

Web search results for query: ""Software Fault Localization Using DStar" Wong Debroy Gao Li"

Links: [{"title":"The DStar Method for Effective Software Fault Localization | Semantic Scholar","url":"https://www.semanticscholar.org/paper/The-DStar-Method-for-Effective-Software-Fault-Wong-Debroy/db47f26a6b8cfc59f9c0fd135034ee25fbef554b"},{"title":"[PDF] Software Fault Localization Using DStar (D*) | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Software-Fault-Localization-Using-DStar-(D*)-Wong-Debroy/dbfbaae06b0bad70792127044566e3a981516a34"},{"title":"Figure 3 from Software Fault Localization Using DStar (D*) | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Software-Fault-Localization-Using-DStar-(D*)-Wong-Debroy/dbfbaae06b0bad70792127044566e3a981516a34/figure/4"},{"title":"Software Fault Localization: an Overview of Research, Techniques, and Tools - Handbook of Software Fault Localization - Wiley Online Library","url":"https://onlinelibrary.wiley.com/doi/10.1002/9781119880929.ch1"},{"title":"Software Fault Localization Using DStar (D*)","url":"https://personal.utdallas.edu/~ewong/SE6367/01-Project/08-SFL-papers/06-DStar.pdf"},{"title":"Google Scholar","url":"https://scholar.google.com/scholar_lookup?doi=10.1109/TR.2013.2285319"},{"title":"Spectrum‐Based Techniques for Software Fault Localization - Handbook of Software Fault Localization - Wiley Online Library","url":"https://onlinelibrary.wiley.com/doi/10.1002/9781119880929.ch4"},{"title":"The DStar Method for Effective Software Fault Localization | Request PDF","url":"https://www.researchgate.net/publication/260524645_The_DStar_Method_for_Effective_Software_Fault_Localization"}]

Based on the search results, I found relevant information about the research on "Software Fault Localization Using DStar":

The paper "Software Fault Localization Using DStar (D*)" was authored by W.E. Wong, Debroy V., Li Y., and Gao R., and was presented at the Sixth International Conference on Software Sec
…[truncated 803 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 151 · 2026-05-26T10:27:35.595643+00:00_

Web search results for query: ""JITLine: A Simpler, Better, Faster, Finer-grained Just-In-Time Defect Prediction" Pornprasit Tantithamthavorn MSR 2021"

Links: [{"title":"JITLine: A Simpler, Better, Faster, Finer-grained Just-In-Time Defect Prediction | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/9463103/"},{"title":"JITLine: a simpler, better, faster, finer-grained Just-In-Time defect prediction - Monash University","url":"https://research.monash.edu/en/publications/jitline-a-simpler-better-faster-finer-grained-just-in-time-defect/"},{"title":"(PDF) JITLine: A Simpler, Better, Faster, Finer-grained Just-In-Time Defect Prediction","url":"https://www.researchgate.net/publication/350061459_JITLine_A_Simpler_Better_Faster_Finer-grained_Just-In-Time_Defect_Prediction"},{"title":"[2103.07068] JITLine: A Simpler, Better, Faster, Finer-grained Just-In-Time Defect Prediction","url":"https://arxiv.org/abs/2103.07068"},{"title":"JITLine: A Simpler, Better, Faster, Finer-grained Just-In-Time Defect Prediction - ADS","url":"https://ui.adsabs.harvard.edu/abs/2021arXiv210307068P/abstract"},{"title":"JITLine: A Simpler, Better, Faster, Finer-grained Just-In-Time Defect Prediction | DeepAI","url":"https://deepai.org/publication/jitline-a-simpler-better-faster-finer-grained-just-in-time-defect-prediction"},{"title":"Papers with Code - JITLine: A Simpler, Better, Faster, Finer-grained Just-In-Time Defect Prediction","url":"https://cs.paperswithcode.com/paper/jitline-a-simpler-better-faster-finer-grained"}]

I found the research paper you're looking for. Here's information about it:

## JITLine: A Simpler, Better, Faster, Finer-grained Just-In-Time Defect Prediction

**Authors:** Chanathip Pornprasit and Chakkrit Tantithamthavorn

**Conference:** MSR 2021 (IEEE/ACM 18th International Conference on Mining Software Repositories)

### Overview
JITLine is a Just-In-Time defect prediction approach for predicting defect-introducing commits and iden
…[truncated 881 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 152 · 2026-05-26T10:27:35.595794+00:00_

Web search results for query: "TRACED ICSE 2024 "Ben Steenhoek" OR "Benjamin Steenhoek" Yangruibo Ding"

Links: [{"title":"Curriculum Vitae - Benjamin Steenhoek","url":"https://benjijang.com/cv/"},{"title":"dblp: ICSE 2024","url":"https://dblp.org/db/conf/icse/icse2024.html"},{"title":"Publications - Benjamin Steenhoek","url":"https://benjijang.com/publications/"},{"title":"Benjamin Steenhoek - Research Intern - Microsoft","url":"https://www.linkedin.com/in/ben-steenhoek/"},{"title":"Benjamin Steenhoek - ICSE 2024 - Conferences - Researchr","url":"https://conf.researchr.org/profile/icse-2024/benjaminsteenhoek"},{"title":"TRACED: Execution-aware Pre-training for Source Code | Proceedings of the IEEE/ACM 46th International Conference on Software Engineering","url":"https://dl.acm.org/doi/10.1145/3597503.3608140"},{"title":"dblp: Kexin Pei","url":"https://dblp.uni-trier.de/pid/145/6061.html"},{"title":"Gail E. Kaiser's CV","url":"http://www.cs.columbia.edu/~kaiser/vita.html"}]

Based on the search results, I found information about the TRACED paper presented at ICSE 2024:

TRACED: Execution-aware Pre-training for Source Code is authored by Yangruibo Ding, Benjamin Steenhoek, Kexin Pei, Gail E. Kaiser, Wei Le, and Baishakhi Ray. 

The paper was presented at the 2024 IEEE/ACM 46th International Conference on Software Engineering (ICSE '24) on April 14–20, 2024, in Lisbon, Portugal.

TRACED is an execution-aware pre-training strategy for source code wherein code language models are pre-trained with a combination of source code, executable inputs, and corresponding execution traces.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 153 · 2026-05-26T10:27:35.595948+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Dataflow Analysis-Inspired Deep Learning for Efficient Vulnerability Detection\" Steenhoek ICSE 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Dataflow Analysis-Inspired Deep Learning for Efficient Vulnerability Detection\" Steenhoek ICSE 2024"
  }
}
```

</details>

---

### Tool call

_source line 154 · 2026-05-26T10:27:35.596083+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Agentless: Demystifying LLM-based Software Engineering Agents\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Agentless: Demystifying LLM-based Software Engineering Agents\""
  }
}
```

</details>

---

### Tool call

_source line 155 · 2026-05-26T10:27:35.596212+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"AgentFL: Scaling LLM-based Fault Localization to Project-Level Context\" Qin Shangwen Wang ASE 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"AgentFL: Scaling LLM-based Fault Localization to Project-Level Context\" Qin Shangwen Wang ASE 2024"
  }
}
```

</details>

---

### Tool call

_source line 156 · 2026-05-26T10:27:35.596366+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "RepairAgent ICSE 2025 \"47th\" OR \"46th\" Bouzenia doi"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "tool_args": {
    "query": "RepairAgent ICSE 2025 \"47th\" OR \"46th\" Bouzenia doi"
  }
}
```

</details>

---

### Tool result

_source line 157 · 2026-05-26T10:27:35.596500+00:00_

Web search results for query: ""Agentless: Demystifying LLM-based Software Engineering Agents""

Links: [{"title":"[2407.01489] Agentless: Demystifying LLM-based Software Engineering Agents","url":"https://arxiv.org/abs/2407.01489"},{"title":"AGENTLESS : Demystifying LLM-based Software Engineering Agents","url":"https://arxiv.org/pdf/2407.01489"},{"title":"Paper page - Agentless: Demystifying LLM-based Software Engineering Agents","url":"https://huggingface.co/papers/2407.01489"},{"title":"(PDF) Agentless: Demystifying LLM-based Software Engineering Agents","url":"https://www.researchgate.net/publication/381911059_Agentless_Demystifying_LLM-based_Software_Engineering_Agents"},{"title":"[2407.01489v2] Agentless: Demystifying LLM-based Software Engineering Agents","url":"https://arxiv.org/abs/2407.01489v2"},{"title":"[2407.01489v1] Agentless: Demystifying LLM-based Software Engineering Agents","url":"https://arxiv.org/abs/2407.01489v1"},{"title":"Agentless: Demystifying LLM-based Software Engineering Agents | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/agentless-demystifying-llm-based-software-engineering-agents"}]

I found results for "Agentless: Demystifying LLM-based Software Engineering Agents." Here's what I found:

## Overview

This is a paper by Chunqiu Steven Xia, Yinlin Deng, Soren Dunn, and Lingming Zhang from the University of Illinois Urbana-Champaign that discusses how recent advancements in large language models have advanced the automation of software development tasks, including code synthesis, program repair, and test generation.

## The Agentless Approach

The paper presents Agentless – an agentless approach to automatically resolve software development issues, following a simple three phase process: localization, repair, and patch validation. Unlike verbose and complex agent-based approaches, Agentless employs a simplistic two-phase process of localization followed by repair, without letting the LLM decide future actions 
…[truncated 529 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 158 · 2026-05-26T10:27:35.596659+00:00_

Web search results for query: "RepairAgent ICSE 2025 "47th" OR "46th" Bouzenia doi"

Links: [{"title":"RepairAgent: An Autonomous, LLM-Based Agent for Program Repair Islem Bouzenia","url":"https://software-lab.org/publications/icse2025_RepairAgent.pdf"},{"title":"GitHub - sola-st/RepairAgent: RepairAgent is an autonomous LLM-based agent for software repair. · GitHub","url":"https://github.com/sola-st/RepairAgent"},{"title":"dblp: Islem Bouzenia","url":"https://dblp.org/pid/324/8017.html"},{"title":"RepairAgent: An Autonomous, LLM-Based Agent for Program Repair | ELLIS Unit Stuttgart","url":"https://ellis-stuttgart.eu/publications/icse2025-RepairAgent/"},{"title":"Islem Bouzenia - Software Lab - Department of Computer Science - University of Stuttgart","url":"https://software-lab.org/people/Islem_Bouzenia.html"},{"title":"RepairAgent: An Autonomous, LLM-Based Agent for Program Repair (ICSE 2025 - Research Track) - ICSE 2025","url":"https://conf.researchr.org/details/icse-2025/icse-2025-research-track/160/RepairAgent-An-Autonomous-LLM-Based-Agent-for-Program-Repair"},{"title":"AgentStepper: Interactive Debugging of Software Development Agents","url":"https://arxiv.org/html/2602.06593v1"},{"title":"RepairAgent: An Autonomous, LLM-Based Agent for Program Repair | Request PDF","url":"https://www.researchgate.net/publication/392956389_RepairAgent_An_Autonomous_LLM-Based_Agent_for_Program_Repair"},{"title":"RepairAgent: An Autonomous, LLM-Based Agent for Program Repair | Proceedings of the IEEE/ACM 47th International Conference on Software Engineering","url":"https://dl.acm.org/doi/10.1109/ICSE55347.2025.00157"},{"title":"dblp: RepairAgent (code + data). - Version 2","url":"https://dblp.org/rec/data/11/BouzeniaDP25.html"}]

Based on the search results, I found the information about RepairAgent at ICSE 2025:

RepairAgent: An Autonomous, LLM-Based Agent for Program Repair was published by Islem Bouzenia and Michael Pradel in the Proceedings of the 47th International Conferen
…[truncated 386 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 159 · 2026-05-26T10:27:35.596818+00:00_

Web search results for query: ""Dataflow Analysis-Inspired Deep Learning for Efficient Vulnerability Detection" Steenhoek ICSE 2024"

Links: [{"title":"Dataflow Analysis-Inspired Deep Learning for Efficient Vulnerability Detection (ICSE 2024 - Research Track) - ICSE 2024","url":"https://conf.researchr.org/details/icse-2024/icse-2024-research-track/63/Dataflow-Analysis-Inspired-Deep-Learning-for-Efficient-Vulnerability-Detection"},{"title":"GitHub - ISU-PAAL/DeepDFA: Replication package for \"Dataflow Analysis-Inspired Deep Learning for Efficient Vulnerability Detection\", ICSE 2024.","url":"https://github.com/ISU-PAAL/DeepDFA"},{"title":"Dataflow Analysis-Inspired Deep Learning for Efficient Vulnerability Detection - Benjamin Steenhoek","url":"https://benjijang.com/publication/2024-04-14-deepdfa"},{"title":"Dataflow Analysis-Inspired Deep Learning for Efficient Vulnerability Detection","url":"https://arxiv.org/pdf/2212.08108"},{"title":"Dataflow Analysis-Inspired Deep Learning for Efficient Vulnerability Detection","url":"https://www.researchgate.net/publication/378028377_Dataflow_Analysis-Inspired_Deep_Learning_for_Efficient_Vulnerability_Detection"},{"title":"Dataflow Analysis-Inspired Deep Learning for Efficient Vulnerability Detection | Proceedings of the IEEE/ACM 46th International Conference on Software Engineering","url":"https://dl.acm.org/doi/10.1145/3597503.3623345"},{"title":"Item - Dataflow Analysis-Inspired Deep Learning for Efficient Vulnerability Detection - figshare - Figshare","url":"https://figshare.com/articles/dataset/Dataflow_Analysis-Inspired_Deep_Learning_for_Efficient_Vulnerability_Detection/21225413"},{"title":"bstee615 (Benjamin Steenhoek) · GitHub","url":"https://github.com/bstee615"},{"title":"[2212.08108] Dataflow Analysis-Inspired Deep Learning for Efficient Vulnerability Detection","url":"https://arxiv.org/abs/2212.08108"},{"title":"[PDF] Dataflow Analysis-Inspired Deep Learning for Efficient Vulnerability Detection | Semantic Scholar"
…[truncated 1778 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 160 · 2026-05-26T10:27:35.596976+00:00_

Web search results for query: ""AgentFL: Scaling LLM-based Fault Localization to Project-Level Context" Qin Shangwen Wang ASE 2024"

Links: [{"title":"[2403.16362] AgentFL: Scaling LLM-based Fault Localization to Project-Level Context","url":"https://arxiv.org/abs/2403.16362"},{"title":"AgentFL: Scaling LLM-based Fault Localization to Project-Level Context","url":"https://arxiv.org/html/2403.16362v1"},{"title":"[Literature Review] AgentFL: Scaling LLM-based Fault Localization to Project-Level Context","url":"https://www.themoonlight.io/en/review/agentfl-scaling-llm-based-fault-localization-to-project-level-context"},{"title":"AGENTFL: Scaling LLM-based Fault Localization to Project-Level Context","url":"https://scispace.com/pdf/agentfl-scaling-llm-based-fault-localization-to-project-2417pl0g8f.pdf"},{"title":"AgentFL: Scaling LLM-based Fault Localization to Project-Level Context - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240316362Q/abstract"},{"title":"[PDF] AgentFL: Scaling LLM-based Fault Localization to Project-Level Context | Semantic Scholar","url":"https://www.semanticscholar.org/paper/AgentFL:-Scaling-LLM-based-Fault-Localization-to-Qin-Wang/ed56e11c9c454bed81ec1396196998b9ca9f5a6c"},{"title":"[2403.16362v2] AgentFL: Scaling LLM-based Fault Localization to Project-Level Context","url":"https://arxiv.org/abs/2403.16362v2"},{"title":"AgentFL: Scaling LLM-based Fault Localization to Project-Level Context","url":"https://www.emergentmind.com/papers/2403.16362"}]

I found the paper you're looking for! Here's what I found about it:

## AgentFL: Scaling LLM-based Fault Localization to Project-Level Context

**Overview:**
AgentFL is a multi-agent system based on ChatGPT for automated fault localization. The work addresses a key limitation of existing LLM-based fault localization, which remains on localizing bugs within a small code scope (i.e., a method or a class), which struggles to diagnose bugs for a large code scope (i.e., an entire software system
…[truncated 1201 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 161 · 2026-05-26T10:27:35.597132+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "DeepSeek-Coder arXiv 2401.14196 full author list \"Daya Guo\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "tool_args": {
    "query": "DeepSeek-Coder arXiv 2401.14196 full author list \"Daya Guo\""
  }
}
```

</details>

---

### Tool call

_source line 162 · 2026-05-26T10:27:35.597286+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining\""
  }
}
```

</details>

---

### Tool call

_source line 163 · 2026-05-26T10:27:35.597424+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Dataset Cartography: Mapping and Diagnosing Datasets with Training Dynamics\" Swayamdipta EMNLP 2020"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Dataset Cartography: Mapping and Diagnosing Datasets with Training Dynamics\" Swayamdipta EMNLP 2020"
  }
}
```

</details>

---

### Tool call

_source line 164 · 2026-05-26T10:27:35.597554+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "AgentFL Qin Wang Yoo \"ASE 2024\" OR \"Automated Software Engineering\" venue conference"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "tool_args": {
    "query": "AgentFL Qin Wang Yoo \"ASE 2024\" OR \"Automated Software Engineering\" venue conference"
  }
}
```

</details>

---

### Tool result

_source line 165 · 2026-05-26T10:27:35.597691+00:00_

Web search results for query: "DeepSeek-Coder arXiv 2401.14196 full author list "Daya Guo""

Links: [{"title":"[2401.14196] DeepSeek-Coder: When the Large Language Model Meets Programming -- The Rise of Code Intelligence","url":"https://arxiv.org/abs/2401.14196"},{"title":"DeepSeek-Coder: When the Large Language Model Meets ...","url":"https://arxiv.org/pdf/2401.14196"},{"title":"[PDF] DeepSeek-Coder: When the Large Language Model Meets Programming - The Rise of Code Intelligence | Semantic Scholar","url":"https://www.semanticscholar.org/paper/DeepSeek-Coder:-When-the-Large-Language-Model-Meets-Guo-Zhu/1f2a20a6efaf83214861dddae4a38a83ae18fe32"},{"title":"GitHub - deepseek-ai/DeepSeek-Coder: DeepSeek Coder: Let the Code Write Itself · GitHub","url":"https://github.com/deepseek-ai/DeepSeek-Coder"},{"title":"Paper page - DeepSeek-Coder: When the Large Language Model Meets Programming -- The Rise of Code Intelligence","url":"https://huggingface.co/papers/2401.14196"},{"title":"[2401.14196v2] DeepSeek-Coder: When the Large Language Model Meets Programming -- The Rise of Code Intelligence","url":"https://arxiv.org/abs/2401.14196v2"},{"title":"dblp: DeepSeek-Coder: When the Large Language Model Meets Programming - The Rise of Code Intelligence.","url":"https://dblp.org/rec/journals/corr/abs-2401-14196.html"},{"title":"DeepSeek vs. ChatGPT: prospects and challenges","url":"https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2025.1576992/pdf"},{"title":"DeepSeek-Coder: When the Large Language Model Meets Programming - The Rise of Code Intelligence","url":"https://arxiv.org/html/2401.14196v1"},{"title":"DeepSeek in Action: LLM Deployment, Fine-Tuning, and Application","url":"https://www.researchgate.net/publication/396135336_DeepSeek_in_Action_LLM_Deployment_Fine-Tuning_and_Application"}]

Based on the search results, the full author list for arXiv paper 2401.14196 "DeepSeek-Coder: When the Large Language Model Meets Programming - The Rise of Co
…[truncated 341 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 166 · 2026-05-26T10:27:35.597848+00:00_

Web search results for query: "AgentFL Qin Wang Yoo "ASE 2024" OR "Automated Software Engineering" venue conference"

Links: [{"title":"[PDF] AgentFL: Scaling LLM-based Fault Localization to Project-Level Context | Semantic Scholar","url":"https://www.semanticscholar.org/paper/AgentFL:-Scaling-LLM-based-Fault-Localization-to-Qin-Wang/ed56e11c9c454bed81ec1396196998b9ca9f5a6c"},{"title":"AgentFL: Scaling LLM-based Fault Localization to Project-Level Context - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240316362Q/abstract"},{"title":"ASE 2024 Contributors - ASE 2024","url":"https://conf.researchr.org/people-index/ase-2024"},{"title":"ASE 2024 - Industry Showcase - conf.researchr.org","url":"https://conf.researchr.org/track/ase-2024/ase-2024-industry-showcase"},{"title":"ASE 2024 - Research Papers - conf.researchr.org","url":"https://conf.researchr.org/track/ase-2024/ase-2024-research"},{"title":"39th ASE 2024: Sacramento, CA, USA","url":"https://dblp.org/db/conf/kbse/ase2024.html"},{"title":"Kingdom 4: Return of the Great General Full Cast & Crew - MyDramaList","url":"https://mydramalist.com/761269-kingdom-4/cast"},{"title":"ASE 2024 - The New Ideas and Emerging Results (NIER) Track - ASE 2024","url":"https://conf.researchr.org/track/ase-2024/ase-2024-nier-track"},{"title":"China 2024 – GC Powerlist","url":"https://www.legal500.com/gc-powerlist/china-2024/"},{"title":"Qianxiang Wang - ASE 2024 - Conferences - Researchr","url":"https://conf.researchr.org/profile/ase-2024/qianxiangwang"}]

Based on the search results, I found information about AgentFL:

AgentFL is a multi-agent system based on ChatGPT for automated fault localization. It models the fault localization task as a three-step process involving comprehension, navigation, and confirmation, with agents utilizing different tools to handle specific tasks.

The paper was authored by Yihao Qin and Shangwen Wang, among other authors (note: the search query mentioned "Qin Wang Yoo," but the actual authors 
…[truncated 531 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 167 · 2026-05-26T10:27:35.598008+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"On the Accuracy of Spectrum-based Fault Localization\" 2007 \"TAIC-PART\" OR \"MUTATION\" venue conference proceedings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"On the Accuracy of Spectrum-based Fault Localization\" 2007 \"TAIC-PART\" OR \"MUTATION\" venue conference proceedings"
  }
}
```

</details>

---

### Tool call

_source line 168 · 2026-05-26T10:27:35.598143+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "AgentFL \"Scaling LLM-based Fault Localization\" accepted ASE conference proceedings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "tool_args": {
    "query": "AgentFL \"Scaling LLM-based Fault Localization\" accepted ASE conference proceedings"
  }
}
```

</details>

---

### Tool result

_source line 169 · 2026-05-26T10:27:35.598293+00:00_

Web search results for query: ""DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining""

Links: [{"title":"[2305.10429] DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining","url":"https://arxiv.org/abs/2305.10429"},{"title":"DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining | OpenReview","url":"https://openreview.net/forum?id=lXuByUeHhd"},{"title":"DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining","url":"https://proceedings.neurips.cc/paper_files/paper/2023/file/dcba6be91359358c2355cd920da3fcbd-Paper-Conference.pdf"},{"title":"NeurIPS Poster DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining","url":"https://neurips.cc/virtual/2023/poster/70588"},{"title":"[2305.10429v4] DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining","url":"https://arxiv.org/abs/2305.10429v4"},{"title":"DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining","url":"https://dmlr.ai/assets/accepted-papers/15/CameraReady/ICML_workshop_DoReMi%20(5)%20(1).pdf"},{"title":"Paper page - DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining","url":"https://huggingface.co/papers/2305.10429"}]

I found information about the DoReMi paper. Here are the key details:

## Overview

DoReMi (Domain Reweighting with Minimax Optimization) addresses how the mixture proportions of pretraining data domains (e.g., Wikipedia, books, web text) greatly affect language model performance. It works by training a small proxy model using group distributionally robust optimization (Group DRO) over domains to produce domain weights without knowledge of downstream tasks.

## Methodology

The method then resamples a dataset with these domain weights and trains a larger, full-sized model. In experiments, DoReMi was used on a 280M-parameter proxy model to set the domain weights for training an 8B-parameter model (30x larger) more efficiently.

## Results

DoReMi improves average few-shot dow
…[truncated 453 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 170 · 2026-05-26T10:27:35.598450+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"CRUXEval-X: A Benchmark for Multilingual Code Reasoning, Understanding and Execution\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"CRUXEval-X: A Benchmark for Multilingual Code Reasoning, Understanding and Execution\""
  }
}
```

</details>

---

### Tool result

_source line 171 · 2026-05-26T10:27:35.598586+00:00_

Web search results for query: ""Dataset Cartography: Mapping and Diagnosing Datasets with Training Dynamics" Swayamdipta EMNLP 2020"

Links: [{"title":"Dataset Cartography: Mapping and Diagnosing Datasets with Training Dynamics - ACL Anthology","url":"https://aclanthology.org/2020.emnlp-main.746/"},{"title":"GitHub - allenai/cartography: Dataset Cartography: Mapping and Diagnosing Datasets with Training Dynamics · GitHub","url":"https://github.com/allenai/cartography"},{"title":"[PDF] Dataset Cartography: Mapping and Diagnosing Datasets with Training Dynamics | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Dataset-Cartography:-Mapping-and-Diagnosing-with-Swayamdipta-Schwartz/ee5fff85d3ec62698eddba162f054b7e73670b2a"},{"title":"Dataset Cartography: Mapping and Diagnosing Datasets with Training Dynamics | Request PDF","url":"https://www.researchgate.net/publication/347237029_Dataset_Cartography_Mapping_and_Diagnosing_Datasets_with_Training_Dynamics"},{"title":"[2009.10795] Dataset Cartography: Mapping and Diagnosing Datasets with Training Dynamics","url":"https://arxiv.org/abs/2009.10795"},{"title":"Dataset Cartography: Mapping and Diagnosing Datasets with Training Dynamics | Paper to HTML | Allen Institute for AI","url":"https://a11y2.apps.allenai.org/paper?id=ee5fff85d3ec62698eddba162f054b7e73670b2a"},{"title":"GitHub - allenai/cartography: Dataset Cartography: Mapping and Diagnosing Datasets with Training Dynamics","url":"https://github.com/allenai/cartography/tree/main"},{"title":"Dataset cartography: Mapping and diagnosing datasets with training dynamics","url":"https://www.mendeley.com/catalogue/5ef551f0-f6e4-3329-a092-e574463bf2b6/"},{"title":"Dataset Cartography: Mapping and Diagnosing Datasets with Training Dynamics | Home","url":"https://schwartz-lab-huji.github.io/publication/datamaps/"}]

I found comprehensive information about this paper. Here are the key details:

## Publication Details

"Dataset Cartography: Mapping and Diagnosing Datas
…[truncated 1354 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 172 · 2026-05-26T10:27:35.598740+00:00_

Web search results for query: "AgentFL "Scaling LLM-based Fault Localization" accepted ASE conference proceedings"

Links: [{"title":"[2403.16362] AgentFL: Scaling LLM-based Fault Localization to Project-Level Context","url":"https://arxiv.org/abs/2403.16362"},{"title":"[PDF] AgentFL: Scaling LLM-based Fault Localization to Project-Level Context | Semantic Scholar","url":"https://www.semanticscholar.org/paper/AgentFL:-Scaling-LLM-based-Fault-Localization-to-Qin-Wang/ed56e11c9c454bed81ec1396196998b9ca9f5a6c"},{"title":"AgentFL: Scaling LLM-based Fault Localization to Project-Level Context","url":"https://arxiv.org/html/2403.16362v1"},{"title":"AGENTFL: Scaling LLM-based Fault Localization to Project-Level Context","url":"https://scispace.com/pdf/agentfl-scaling-llm-based-fault-localization-to-project-2417pl0g8f.pdf"},{"title":"[Literature Review] AgentFL: Scaling LLM-based Fault Localization to Project-Level Context","url":"https://www.themoonlight.io/en/review/agentfl-scaling-llm-based-fault-localization-to-project-level-context"},{"title":"[2403.16362v2] AgentFL: Scaling LLM-based Fault Localization to Project-Level Context","url":"https://arxiv.org/abs/2403.16362v2"},{"title":"Online repository for Paper \"AgentFL: Scaling LLM-based Fault Localization to Project-Level Context\"","url":"https://zenodo.org/records/16938304"},{"title":"AgentFL: Scaling LLM-based Fault Localization to Project-Level Context - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240316362Q/abstract"},{"title":"AgentFL: Scaling LLM-based Fault Localization to Project-Level Context","url":"https://www.emergentmind.com/papers/2403.16362"}]

Based on the search results, I found information about AgentFL and "Scaling LLM-based Fault Localization." However, the search results indicate that this paper is available on arXiv (paper 2403.16362), but I don't see confirmation of acceptance to the ASE conference proceedings in these results.

The search results show that AgentFL is a multi-agent s
…[truncated 745 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 173 · 2026-05-26T10:27:35.598898+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Evaluating Representation Learning of Code Changes for Predicting Patch Correctness in Program Repair\" Tian ASE 2020"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Evaluating Representation Learning of Code Changes for Predicting Patch Correctness in Program Repair\" Tian ASE 2020"
  }
}
```

</details>

---

### Tool result

_source line 174 · 2026-05-26T10:27:35.599031+00:00_

Web search results for query: ""On the Accuracy of Spectrum-based Fault Localization" 2007 "TAIC-PART" OR "MUTATION" venue conference proceedings"

Links: [{"title":"On the Accuracy of Spectrum-based Fault Localization","url":"https://www.researchgate.net/publication/4279298_On_the_Accuracy_of_Spectrum-based_Fault_Localization"},{"title":"[PDF] On the Accuracy of Spectrum-based Fault Localization | Semantic Scholar","url":"https://www.semanticscholar.org/paper/On-the-Accuracy-of-Spectrum-based-Fault-Abreu-Zoeteweij/eb956ab442810f783f44600ce6d714583a96a4aa"},{"title":"On the Accuracy of Spectrum-based Fault Localization | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/4344104/"},{"title":"Spectrum-Based Fault Localization for Diagnosing Concurrency Faults | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-642-41707-8_16"},{"title":"On the Accuracy of Spectrum-based Fault Localization | Proceedings of the Testing: Academic and Industrial Conference Practice and Research Techniques - MUTATION","url":"https://dl.acm.org/doi/10.5555/1308173.1308264"},{"title":"Spectrum-Based Fault Localization in Model Transformations | ACM Transactions on Software Engineering and Methodology","url":"https://dl.acm.org/doi/10.1145/3241744"},{"title":"On the Accuracy of Spectrum-based Fault Localization","url":"https://scispace.com/pdf/on-the-accuracy-of-spectrum-based-fault-localization-13lhdnxj1f.pdf"},{"title":"Enhancing spectrum based fault localization via emphasizing its formulas with importance weight | Proceedings of the Third International Workshop on Automated Program Repair","url":"https://dl.acm.org/doi/10.1145/3524459.3527349"},{"title":"A practical evaluation of spectrum-based fault localization - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0164121209001319"}]

I found the paper you're looking for! Here are the search results:

"On the Accuracy of Spectrum-based Fault Localiz
…[truncated 1050 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 175 · 2026-05-26T10:27:35.599180+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:dblp.org AgentFL Qin Wang fault localization"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:dblp.org AgentFL Qin Wang fault localization"
  }
}
```

</details>

---

### Tool result

_source line 176 · 2026-05-26T10:27:35.599363+00:00_

Web search results for query: ""CRUXEval-X: A Benchmark for Multilingual Code Reasoning, Understanding and Execution""

Links: [{"title":"CRUXEVAL-X: A Benchmark for Multilingual Code Reasoning, Understanding and Execution - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.1158/"},{"title":"[2408.13001] CRUXEval-X: A Benchmark for Multilingual Code Reasoning, Understanding and Execution","url":"https://arxiv.org/abs/2408.13001"},{"title":"(PDF) CRUXEval-X: A Benchmark for Multilingual Code Reasoning, Understanding and Execution","url":"https://www.researchgate.net/publication/383413276_CRUXEval-X_A_Benchmark_for_Multilingual_Code_Reasoning_Understanding_and_Execution"},{"title":"CRUXEval-X: A Benchmark for Multilingual Code Reasoning, Understanding and Execution - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240813001X/abstract"},{"title":"CruxEval-X: A Benchmark for Multilingual Code Reasoning, Understanding and Execution","url":"https://arxiv.org/html/2408.13001v2"},{"title":"Paper page - CRUXEval-X: A Benchmark for Multilingual Code Reasoning, Understanding and Execution","url":"https://huggingface.co/papers/2408.13001"},{"title":"[PDF] CRUXEval-X: A Benchmark for Multilingual Code Reasoning, Understanding and Execution | Semantic Scholar","url":"https://www.semanticscholar.org/paper/CRUXEval-X:-A-Benchmark-for-Multilingual-Code-and-Xu-Cao/88d48041a76ddc4318c360cdda0a4e1379eeefb3"},{"title":"CRUXEval-X: A Benchmark for Multilingual Code Reasoning, Understanding and Execution | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/cruxeval-x-benchmark-multilingual-code-reasoning-understanding"}]

I found detailed information about CRUXEval-X. Here's what the research shows:

## Overview

CRUXEval-X is a multi-lingual code reasoning benchmark that contains 19 programming languages. It comprises at least 600 subjects for each language, along with 19K content-consistent tests in total.

## Motivation

There is an unignorable pr
…[truncated 1382 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 177 · 2026-05-26T10:27:35.599534+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "chen2025tracepile TracePile authors \"Keqin Bao\" \"Junyang Lin\" \"Dayiheng Liu\" affiliations"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "tool_args": {
    "query": "chen2025tracepile TracePile authors \"Keqin Bao\" \"Junyang Lin\" \"Dayiheng Liu\" affiliations"
  }
}
```

</details>

---

### Tool call

_source line 178 · 2026-05-26T10:27:35.599669+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"A Learning-Based Approach to Static Program Slicing\" Yadavally"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"A Learning-Based Approach to Static Program Slicing\" Yadavally"
  }
}
```

</details>

---

### Tool result

_source line 179 · 2026-05-26T10:27:35.599803+00:00_

Web search results for query: ""Evaluating Representation Learning of Code Changes for Predicting Patch Correctness in Program Repair" Tian ASE 2020"

Links: [{"title":"Evaluating representation learning of code changes for predicting patch correctness in program repair | Proceedings of the 35th IEEE/ACM International Conference on Automated Software Engineering","url":"https://dl.acm.org/doi/10.1145/3324884.3416532"},{"title":"Evaluating Representation Learning of Code Changes for ...","url":"https://kui-liu.github.io/papers/tian2020evaluating.pdf"},{"title":"[PDF] Evaluating Representation Learning of Code Changes for Predicting Patch Correctness in Program Repair | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Evaluating-Representation-Learning-of-Code-Changes-Tian-Liu/521b813aeb71162fe74ad09da4a2bbbcd9919b70"},{"title":"Evaluating representation learning of code changes for predicting patch correctness in program repair - Monash University","url":"https://research.monash.edu/en/publications/evaluating-representation-learning-of-code-changes-for-predicting/"},{"title":"[2008.02944] Evaluating Representation Learning of Code Changes for Predicting Patch Correctness in Program Repair","url":"https://ar5iv.labs.arxiv.org/html/2008.02944"},{"title":"[2008.02944] Evaluating Representation Learning of Code Changes for Predicting Patch Correctness in Program Repair","url":"https://arxiv-export1.library.cornell.edu/abs/2008.02944"}]

I found the paper you're looking for! Here are the details:

**Paper Title:** "Evaluating Representation Learning of Code Changes for Predicting Patch Correctness in Program Repair"

**Authors:** Haoye Tian, Kui Liu, Abdoul Kader Kaboreé, Anil Koyuncu, Li Li, Jacques Klein, Tegawendé F. Bissyandé

**Conference:** 35th IEEE/ACM International Conference on Automated Software Engineering (ASE '20), September 21–25, 2020, Virtual Event, Australia

**Main Focus:** The paper studies the benefit of learning code representations to 
…[truncated 598 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 180 · 2026-05-26T10:27:35.599954+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"DebugBench: Evaluating Debugging Capability of Large Language Models\" Tian ACL 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"DebugBench: Evaluating Debugging Capability of Large Language Models\" Tian ACL 2024"
  }
}
```

</details>

---

### Tool result

_source line 181 · 2026-05-26T10:27:35.600088+00:00_

Web search results for query: "site:dblp.org AgentFL Qin Wang fault localization"

Links: [{"title":"dblp: Qin Wang (disambiguation)","url":"https://dblp.org/pid/35/1647.html"},{"title":"dblp: Liwei Zheng","url":"https://dblp.org/pid/04/4077.html"},{"title":"dblp: Ruixin Wang (disambiguation)","url":"https://dblp.org/pid/169/2205.html"},{"title":"dblp: Ziyuan Wang","url":"https://dblp.org/pers/w/Wang:Ziyuan.html"},{"title":"dblp: Peiyu Liu 0003","url":"https://dblp.org/pid/85/670-3.html"},{"title":"dblp: Zhipeng Wang 0009","url":"https://dblp.org/pid/56/5818-9.html"},{"title":"dblp: Zhiying Wu","url":"https://dblp.org/pid/36/10644.html"},{"title":"dblp: Xuebin Qin","url":"https://dblp.org/pid/142/6561.html"}]

The search results returned papers from DBLP with various authors named "Qin Wang" and other researchers working on fault localization, but did not return any specific results for "AgentFL" by Qin Wang. The results show various papers on fault localization topics by different authors, but nothing matching the specific "AgentFL" project you're looking for from the DBLP site.

It's possible that:
1. The paper/project may be listed under a different name on DBLP
2. It may be a very recent publication not yet indexed by DBLP
3. The specific combination of these terms may not have matches in DBLP's current database

Would you like me to try a different search query, or search more broadly for "AgentFL" without the site restriction?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 182 · 2026-05-26T10:27:35.600245+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "dblp AgentFL Yihao Qin 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "tool_args": {
    "query": "dblp AgentFL Yihao Qin 2024"
  }
}
```

</details>

---

### Tool result

_source line 183 · 2026-05-26T10:27:35.600381+00:00_

Web search results for query: ""A Learning-Based Approach to Static Program Slicing" Yadavally"

Links: [{"title":"A Learning-Based Approach to Static Program Slicing | Proceedings of the ACM on Programming Languages","url":"https://dl.acm.org/doi/10.1145/3649814"},{"title":"A Learning-Based Approach to Static Program Slicing | Request PDF","url":"https://www.researchgate.net/publication/380202230_A_Learning-Based_Approach_to_Static_Program_Slicing"},{"title":"A Learning-Based Approach to Static Program Slicing (SPLASH 2024 - OOPSLA 2024) - SPLASH 2024","url":"https://2024.splashcon.org/details/splash-2024-oopsla/4/A-Learning-Based-Approach-to-Static-Program-Slicing"},{"title":"A Learning-Based Approach to Static Program Slicing","url":"https://dl.acm.org/doi/pdf/10.1145/3649814"},{"title":"[OOPSLA24] A Learning-Based Approach to Static Program Slicing - YouTube","url":"https://www.youtube.com/watch?v=JhFDjtNkRi8"},{"title":"SliceT5: Static Program Slicing using Language Models with Copy Mechanism and Constrained Decoding","url":"https://arxiv.org/html/2509.17338v1"}]

I found results for "A Learning-Based Approach to Static Program Slicing" by Yadavally. Here's what I found:

The paper is authored by Aashish Yadavally, Yi Li, Shaohua Wang, and Tien N. Nguyen, and was published in Proceedings of the ACM on Programming Languages, Vol. 8, OOPSLA1, Article 97 (April 2024).

The paper addresses the fact that traditional program slicing techniques are crucial for early bug detection and debugging, but their inability to handle incomplete code hinders their real-world applicability. 

The authors present NS-Slicer, a novel learning-based approach that predicts static program slices for both complete and partial code. The tool leverages a pre-trained language model to exploit its understanding of fine-grained variable-statement dependencies within source code.

The paper was presented at SPLASH 2024 - OOPSLA 2024, and an artifact was made available in April 2024.


REMINDE
…[truncated 93 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 184 · 2026-05-26T10:27:35.600547+00:00_

Web search results for query: ""DebugBench: Evaluating Debugging Capability of Large Language Models" Tian ACL 2024"

Links: [{"title":"DebugBench: Evaluating Debugging Capability of Large Language Models - ACL Anthology","url":"https://aclanthology.org/2024.findings-acl.247/"},{"title":"[2401.04621] DebugBench: Evaluating Debugging Capability of Large Language Models","url":"https://arxiv.org/abs/2401.04621"},{"title":"GitHub - thunlp/DebugBench: The repository for paper \"DebugBench: \"Evaluating Debugging Capability of Large Language Models\". · GitHub","url":"https://github.com/thunlp/DebugBench"},{"title":"DebugBench: Evaluating Debugging Capability of Large ...","url":"https://aclanthology.org/2024.findings-acl.247.pdf"},{"title":"DebugBench: Evaluating Debugging Capability of Large Language Models [Quick Review]","url":"https://liner.com/review/debugbench-evaluating-debugging-capability-large-language-models"},{"title":"DebugBench: Evaluating Debugging Capability of Large Language Models | Request PDF","url":"https://www.researchgate.net/publication/384218799_DebugBench_Evaluating_Debugging_Capability_of_Large_Language_Models"},{"title":"[PDF] DebugBench: Evaluating Debugging Capability of Large Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/DebugBench:-Evaluating-Debugging-Capability-of-Tian-Ye/bb39d2b273d4c75f8e489f1f66dec42a7e14c5fd"},{"title":"DebugBench: Evaluating Debugging Capability of Large Language Models","url":"https://openreview.net/pdf/f3e7b01b7edc2ac558a684981bd38c590ff89cb3.pdf"},{"title":"Paper page - DebugBench: Evaluating Debugging Capability of Large Language Models","url":"https://huggingface.co/papers/2401.04621"}]

I found the paper you're looking for! Here's the information:

## DebugBench: Evaluating Debugging Capability of Large Language Models

The paper "DebugBench: Evaluating Debugging Capability of Large Language Models" was authored by Runchu Tian, Yining Ye, Yujia Qin, Xin Cong, Yankai Lin, Yin
…[truncated 1319 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 185 · 2026-05-26T10:27:35.600702+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Unveiling the Generalization Power of Fine-Tuned Large Language Models\" Yang Zhang Xu Lu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Unveiling the Generalization Power of Fine-Tuned Large Language Models\" Yang Zhang Xu Lu"
  }
}
```

</details>

---

### Tool call

_source line 186 · 2026-05-26T10:27:35.600834+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Do Code Semantics Help? A Comprehensive Study on Execution Trace-Based Information\" Wang EMNLP 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Do Code Semantics Help? A Comprehensive Study on Execution Trace-Based Information\" Wang EMNLP 2025"
  }
}
```

</details>

---

### Tool result

_source line 187 · 2026-05-26T10:27:35.600957+00:00_

Web search results for query: "dblp AgentFL Yihao Qin 2024"

Links: [{"title":"[PDF] AgentFL: Scaling LLM-based Fault Localization to Project-Level Context | Semantic Scholar","url":"https://www.semanticscholar.org/paper/AgentFL:-Scaling-LLM-based-Fault-Localization-to-Qin-Wang/ed56e11c9c454bed81ec1396196998b9ca9f5a6c"},{"title":"dblp: FG 2024","url":"https://dblp.org/db/conf/fgr/fg2024.html"},{"title":"dblp: AAAI 2024","url":"https://dblp.org/db/conf/aaai/aaai2024.html"},{"title":"dblp: IPSN 2024","url":"https://dblp.org/db/conf/ipsn/ipsn2024.html"},{"title":"dblp: ACL 2024","url":"https://dblp.org/db/conf/acl/acl2024f.html"},{"title":"dblp: Qin Tao","url":"https://dblp.org/pid/146/0560.html"},{"title":"dblp: MM 2024","url":"https://dblp.org/db/conf/mm/mm2024.html"}]

Based on the search results, I found information about the AgentFL paper by Yihao Qin and colleagues from 2024:

AgentFL is titled "Scaling LLM-based Fault Localization to Project-Level Context" and was authored by Yihao Qin, Shangwen Wang, Yiling Lou, Jinhao Dong, Kaixin Wang, Xiaoling Li, and Xiaoguang Mao. The paper was published on arXiv on March 25, 2024 with identifier abs/2403.16362.

AgentFL is a multi-agent system based on ChatGPT for automated fault localization, which outperforms other LLM-based approaches and exhibits complementarity to state-of-the-art learning-based techniques.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 188 · 2026-05-26T10:27:35.601103+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "AgentFL Yihao Qin Shangwen Wang venue published \"39th\" OR \"ASE\" OR \"ICSE\" OR \"FSE\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "tool_args": {
    "query": "AgentFL Yihao Qin Shangwen Wang venue published \"39th\" OR \"ASE\" OR \"ICSE\" OR \"FSE\""
  }
}
```

</details>

---

### Tool result

_source line 189 · 2026-05-26T10:27:35.601252+00:00_

Web search results for query: ""Unveiling the Generalization Power of Fine-Tuned Large Language Models" Yang Zhang Xu Lu"

Links: [{"title":"[2403.09162] Unveiling the Generalization Power of Fine-Tuned Large Language Models","url":"https://arxiv.org/abs/2403.09162"},{"title":"Unveiling the Generalization Power of Fine-Tuned Large Language Models - ACL Anthology","url":"https://aclanthology.org/2024.naacl-long.51/"},{"title":"[PDF] Unveiling the Generalization Power of Fine-Tuned Large Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Unveiling-the-Generalization-Power-of-Fine-Tuned-Yang-Zhang/6edf144fb397afde80d9acf9472dfaffd22c8072"},{"title":"Unveiling the Generalization Power of Fine-Tuned Large Language Models","url":"https://bibbase.org/network/publication/yang-zhang-xu-lu-heng-lam-unveilingthegeneralizationpoweroffinetunedlargelanguagemodels-2024"},{"title":"Unveiling the Generalization Power of Fine-Tuned Large Language Models","url":"https://arxiv.org/html/2403.09162v1"},{"title":"Paper page - Unveiling the Generalization Power of Fine-Tuned Large Language Models","url":"https://huggingface.co/papers/2403.09162"},{"title":"Unveiling the Generalization Power of Fine-Tuned Large ...","url":"https://aclanthology.org/2024.naacl-long.51.pdf"},{"title":"[Quick Review] Unveiling the Generalization Power of Fine-Tuned Large Language Models","url":"https://liner.com/review/unveiling-generalization-power-finetuned-large-language-models"},{"title":"Unveiling the Generalization Power of Fine-Tuned Large Language Models","url":"https://paperreading.club/page?id=215235"}]

Based on the search results, I found the paper you're looking for:

## Paper Details

"Unveiling the Generalization Power of Fine-Tuned Large Language Models" is authored by Haoran Yang, Yumeng Zhang, Jiaqi Xu, Hongyuan Lu, Pheng-Ann Heng, and Wai Lam.

## Overview

While Large Language Models (LLMs) have demonstrated exceptional multitasking abilities, fine-tuning these 
…[truncated 911 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 190 · 2026-05-26T10:27:35.601412+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering\""
  }
}
```

</details>

---

### Tool result

_source line 191 · 2026-05-26T10:27:35.601547+00:00_

Web search results for query: ""Do Code Semantics Help? A Comprehensive Study on Execution Trace-Based Information" Wang EMNLP 2025"

Links: [{"title":"Do Code Semantics Help? A Comprehensive Study on Execution Trace-Based Information for Code Large Language Models - ACL Anthology","url":"https://aclanthology.org/2025.findings-emnlp.548/"},{"title":"[2509.11686] Do Code Semantics Help? A Comprehensive Study on Execution Trace-Based Information for Code Large Language Models","url":"https://arxiv.org/abs/2509.11686"},{"title":"[2509.11686v3] Do Code Semantics Help? A Comprehensive Study on Execution Trace-Based Information for Code Large Language Models","url":"https://arxiv.org/abs/2509.11686v3"},{"title":"Do Code Semantics Help? A Comprehensive Study on ...","url":"https://aclanthology.org/2025.findings-emnlp.548.pdf"},{"title":"Do Code Semantics Help? A Comprehensive Study on Execution","url":"https://arxiv.org/pdf/2509.11686"},{"title":"Do Code Semantics Help? A Comprehensive Study on Execution Trace-Based Information for Code Large Language Models","url":"https://arxiv.org/html/2509.11686v1"}]

I found the paper! Here are the key details:

## Paper Information

"Do Code Semantics Help? A Comprehensive Study on Execution Trace-Based Information for Code Large Language Models" was published in Findings of the Association for Computational Linguistics: EMNLP 2025 (pages 10367–10385, Suzhou, China).

The authors are Jian Jornbowrl Wang, Xiaofei Xie, Qiang Hu, Shangqing Liu, and Yi Li.

## Overview

The paper addresses critical limitations in Code Large Language Models' ability to reason about runtime behavior and understand the actual functionality of programs, which poses significant challenges for their post-training and practical deployment.

Code LLMs encounter two principal issues: (1) a lack of proficiency in reasoning about program execution behavior, as they struggle to interpret what programs actually do during runtime, and (2) the inconsistent and fragment
…[truncated 764 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 192 · 2026-05-26T10:27:35.601724+00:00_

Web search results for query: "chen2025tracepile TracePile authors "Keqin Bao" "Junyang Lin" "Dayiheng Liu" affiliations"

Links: [{"title":"[PDF] CoRT: Code-integrated Reasoning within Thinking | Semantic Scholar","url":"https://www.semanticscholar.org/paper/CoRT:-Code-integrated-Reasoning-within-Thinking-Li-Tang/eff086f0a6d66b6514322c6832f2469d057f33e3"},{"title":"HellaSwag-Pro: A Large-Scale Bilingual Benchmark for Evaluating the Robustness of LLMs in Commonsense Reasoning - ACL Anthology","url":"https://aclanthology.org/2025.findings-acl.472/"},{"title":"Keqin Bao","url":"https://www.catalyzex.com/author/Keqin%20Bao"},{"title":"Home - Dayiheng Liu","url":"https://liudayiheng.github.io/"},{"title":"Keqin Chen","url":"https://www.catalyzex.com/author/Keqin%20Chen"},{"title":"Tianyi Tang / 唐天一 @ Qwen Team","url":"https://steventang1998.github.io/"},{"title":"GitHub - QwenLM/Qwen3-VL-Embedding · GitHub","url":"https://github.com/QwenLM/Qwen3-VL-Embedding"},{"title":"[PDF] Qwen3-VL Technical Report | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Qwen3-VL-Technical-Report-Bai-Cai/15538df854dd33351dfb5cefd7e8f3340c8936c3"}]

I can see results for papers involving these authors, but I didn't find specific information about "TracePile" in the initial search. Let me search more specifically for TracePile.

Links: [{"title":"GitHub - BeyonderXX/TRACE: TRACE: A Comprehensive Benchmark for Continual Learning in Large Language Models · GitHub","url":"https://github.com/BeyonderXX/TRACE"},{"title":"Towards Effective Author Name Disambiguation by Hybrid Attention","url":"https://jcst.ict.ac.cn/fileup/1000-9000/PDF/JCST-2024-4-12-2070-929.pdf"},{"title":"The Pile (dataset) - Wikipedia","url":"https://en.wikipedia.org/wiki/The_Pile_(dataset)"},{"title":"Authors author affiliations","url":"https://www.cambridge.org/core/services/authors/author-affiliations"},{"title":"GitHub - martenlienen/icml-neurips-iclr-dataset: Papers, authors and author affiliations from ICM
…[truncated 5209 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 193 · 2026-05-26T10:27:35.601877+00:00_

Web search results for query: "AgentFL Yihao Qin Shangwen Wang venue published "39th" OR "ASE" OR "ICSE" OR "FSE""

Links: [{"title":"Fault Localization from the Semantic Code Search Perspective | ACM Transactions on Software Engineering and Methodology","url":"https://dl.acm.org/doi/10.1145/3757915"},{"title":"Publications - Shangwen Wang / Assistant Professor","url":"https://shangwenwang.github.io/publications/"},{"title":"dblp: Shangwen Wang","url":"https://dblp.org/pid/219/1645.html"},{"title":"About me - Shangwen Wang / Assistant Professor","url":"https://shangwenwang.github.io/"},{"title":"Shangwen Wang - ASE 2024","url":"https://conf.researchr.org/profile/ase-2024/shangwenwang"},{"title":"Shangwen Wang - ICSE 2023","url":"https://conf.researchr.org/profile/icse-2023/shangwenwang"},{"title":"Shangwen Wang - ICSE 2020","url":"https://2020.icse-conferences.org/profile/shangwenwang"},{"title":"Shangwen Wang - ASE 2025 - conf.researchr.org","url":"https://conf.researchr.org/profile/ase-2025/shangwenwang"},{"title":"Shangwen Wang - ESEC/FSE 2022","url":"https://2022.esec-fse.org/profile/shangwenwang"}]

Based on the search results, I found information about AgentFL by Yihao Qin and Shangwen Wang:

AgentFL: Scaling LLM-based Fault Localization to Project-Level Context was published on arXiv in 2024 (arXiv:2403.16362).

However, the search results don't show that AgentFL was published at one of the specific venues you mentioned (39th ASE, ICSE, or FSE). A different work on LLM-based fault localization by this research group was accepted by ASE 2025, but that appears to be a separate paper from AgentFL.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 194 · 2026-05-26T10:27:35.602024+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"InspectCoder: Dynamic Analysis-Enabled Self Repair through Interactive LLM-Debugger Collaboration\" Wang arXiv 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"InspectCoder: Dynamic Analysis-Enabled Self Repair through Interactive LLM-Debugger Collaboration\" Wang arXiv 2025"
  }
}
```

</details>

---

### Tool call

_source line 195 · 2026-05-26T10:27:35.602153+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:shangwenwang.github.io AgentFL"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:shangwenwang.github.io AgentFL"
  }
}
```

</details>

---

### Tool call

_source line 196 · 2026-05-26T10:27:35.602305+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "TRACED ICSE 2024 ACM \"Yangruibo Ding\" \"Ben Steenhoek\" author list proceedings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "tool_args": {
    "query": "TRACED ICSE 2024 ACM \"Yangruibo Ding\" \"Ben Steenhoek\" author list proceedings"
  }
}
```

</details>

---

### Tool result

_source line 197 · 2026-05-26T10:27:35.602442+00:00_

Web search results for query: "site:shangwenwang.github.io AgentFL"

Links: [{"title":"About me - Shangwen Wang / Assistant Professor","url":"https://shangwenwang.github.io/"},{"title":"Publications - Shangwen Wang / Assistant Professor","url":"https://shangwenwang.github.io/publications/"},{"title":"ShangwenWang (Shangwen Wang) · GitHub","url":"https://github.com/ShangwenWang"},{"title":"Github","url":"https://shangwenwang.github.io/files/ISSTA-24.pdf"},{"title":"Fine-Grained Code-Comment Semantic Interaction Analysis Mingyang Geng","url":"https://shangwenwang.github.io/files/ICPC-22.pdf"},{"title":"CCT5: A Code-Change-Oriented Pre-Trained Model Bo Lin linbo19@nudt.edu.cn","url":"https://shangwenwang.github.io/files/FSE-23B.pdf"},{"title":"Automated Patch Correctness Assessment: How Far are We? Shangwen Wang∗","url":"https://shangwenwang.github.io/files/ASE-20.pdf"},{"title":"Shangdong Yang (杨尚东) - Homepage - Homepage","url":"https://shangdongyang.github.io/"},{"title":"Shangwen Wang - ICSE 2020","url":"https://2020.icse-conferences.org/profile/shangwenwang"},{"title":"Natural Language to Code: How Far Are We? Shangwen Wang","url":"https://shangwenwang.github.io/files/FSE-23A.pdf"}]

The search results show information about Shangwen Wang's academic website and publications, but they do not contain any specific results related to "AgentFL." The search query with the `site:` operator was designed to find content specifically on shangwenwang.github.io that mentions "AgentFL," but no such results were returned.

The search results indicate that Shangwen Wang is an Assistant Professor at National University of Defense Technology who focuses on program repair, software testing, program comprehension, mining software repositories, and AI4SE, but there is no mention of a project or topic called "AgentFL" on the accessible pages of his website.

If you're looking for information about AgentFL, it may not be publicly available on this particular website, or it might be foun
…[truncated 129 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 198 · 2026-05-26T10:27:35.602601+00:00_

Web search results for query: ""SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering""

Links: [{"title":"[2405.15793] SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering","url":"https://arxiv.org/abs/2405.15793"},{"title":"SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering | OpenReview","url":"https://openreview.net/forum?id=mXpq6ut8J3"},{"title":"SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering","url":"https://arxiv.org/pdf/2405.15793"},{"title":"NeurIPS Poster SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering","url":"https://neurips.cc/virtual/2024/poster/93753"},{"title":"SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering - Princeton University","url":"https://collaborate.princeton.edu/en/publications/swe-agent-agent-computer-interfaces-enable-automated-software-eng/"},{"title":"[PDF] SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering | Semantic Scholar","url":"https://www.semanticscholar.org/paper/SWE-agent:-Agent-Computer-Interfaces-Enable-Yang-Jimenez/1c3c531fc0fbe79f97f367ed3648de8467caeeaa"},{"title":"(PDF) SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering","url":"https://www.researchgate.net/publication/380907343_SWE-agent_Agent-Computer_Interfaces_Enable_Automated_Software_Engineering"}]

I found comprehensive information about SWE-agent. Here are the key findings:

## Overview

SWE-agent is a system that facilitates language model agents to autonomously use computers to solve software engineering tasks. The paper was authored by John Yang and 6 other authors, and was published in 2024 in the Advances in Neural Information Processing Systems, Volume 37.

## Key Concept: Agent-Computer Interfaces

The research posits that language model agents represent a new category of end users with their own needs and abilities, and would benefit from specially-built interfaces t
…[truncated 806 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 199 · 2026-05-26T10:27:35.602755+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"AgentFL\" \"ASE\" OR \"Automated Software Engineering\" Qin 2024 accepted proceedings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"AgentFL\" \"ASE\" OR \"Automated Software Engineering\" Qin 2024 accepted proceedings"
  }
}
```

</details>

---

### Tool call

_source line 200 · 2026-05-26T10:27:35.602886+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"LDB: A Large Language Model Debugger via Verifying Runtime Execution Step by Step\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"LDB: A Large Language Model Debugger via Verifying Runtime Execution Step by Step\""
  }
}
```

</details>

---

### Tool result

_source line 201 · 2026-05-26T10:27:35.603018+00:00_

Web search results for query: "TRACED ICSE 2024 ACM "Yangruibo Ding" "Ben Steenhoek" author list proceedings"

Links: [{"title":"TRACED: Execution-aware Pre-training for Source Code - Benjamin Steenhoek","url":"https://benjijang.com/publication/2024-04-14-traced"},{"title":"dblp: ICSE 2024","url":"https://dblp.org/db/conf/icse/icse2024.html"},{"title":"Curriculum Vitae - Benjamin Steenhoek","url":"https://benjijang.com/cv/"},{"title":"TRACED: Execution-aware Pre-training for Source Code | Proceedings of the IEEE/ACM 46th International Conference on Software Engineering","url":"https://dl.acm.org/doi/10.1145/3597503.3608140"},{"title":"Gail E. Kaiser's CV","url":"http://www.cs.columbia.edu/~kaiser/vita.html"},{"title":"[2306.07487] TRACED: Execution-aware Pre-training for Source Code","url":"https://arxiv.org/abs/2306.07487"},{"title":"Yangruibo Ding - ASE 2024 - Conferences - Researchr","url":"https://conf.researchr.org/profile/ase-2024/yangruiboding"},{"title":"Yangruibo Ding - ICSE 2026 - conf.researchr.org","url":"https://conf.researchr.org/profile/icse-2026/yangruiboding"},{"title":"Yangruibo Ding - ICSE 2025 - Conferences","url":"https://conf.researchr.org/profile/icse-2025/yangruiboding"}]

Based on the web search results, here is the information about the TRACED paper at ICSE 2024:

**Paper Title:** TRACED: Execution-aware Pre-training for Source Code

**Complete Author List:** Yangruibo Ding, Benjamin Steenhoek, Kexin Pei, Gail Kaiser, Wei Le, Baishakhi Ray

**Publication Details:** Proceedings of the 46th IEEE/ACM International Conference on Software Engineering (ICSE '24), April 14–20, 2024, Lisbon, Portugal

**DOI:** https://doi.org/10.1145/3597503.3608140


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 202 · 2026-05-26T10:27:35.603172+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:dl.acm.org \"TRACED\" \"3597503.3608140\" author"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:dl.acm.org \"TRACED\" \"3597503.3608140\" author"
  }
}
```

</details>

---

### Tool result

_source line 203 · 2026-05-26T10:27:35.603357+00:00_

Web search results for query: ""InspectCoder: Dynamic Analysis-Enabled Self Repair through Interactive LLM-Debugger Collaboration" Wang arXiv 2025"

Links: [{"title":"[2510.18327] InspectCoder: Dynamic Analysis-Enabled Self Repair through interactive LLM-Debugger Collaboration","url":"https://arxiv.org/abs/2510.18327"},{"title":"InspectCoder: Dynamic Analysis-Enabled Self Repair through Interactive LLM-Debugger Collaboration","url":"https://arxiv.org/html/2510.18327v1"},{"title":"InspectCoder: Dynamic Analysis-Enabled Self Repair through interactive LLM-Debugger Collaboration | alphaXiv","url":"https://www.alphaxiv.org/resources/2510.18327v1"},{"title":"InspectCoder: Dynamic Analysis-Enabled Self Repair through","url":"https://arxiv.org/pdf/2510.18327"},{"title":"[Literature Review] InspectCoder: Dynamic Analysis-Enabled Self Repair through interactive LLM-Debugger Collaboration","url":"https://www.themoonlight.io/en/review/inspectcoder-dynamic-analysis-enabled-self-repair-through-interactive-llm-debugger-collaboration"},{"title":"InspectCoder: Agentic Code Repair","url":"https://www.emergentmind.com/topics/inspectcoder"},{"title":"InspectWare: LLM-Enabled Debugger Middleware","url":"https://www.emergentmind.com/topics/inspectware"}]

I found the paper you're looking for! Here are the key details:

**Paper Title:** InspectCoder: Dynamic Analysis-Enabled Self Repair through interactive LLM-Debugger Collaboration

**Authors:** Yunkun Wang, Yue Zhang, Guochang Li, Chen Zhi, Binhua Li, Fei Huang, Yongbin Li, and Shuiguang Deng

**Publication:** arXiv paper 2510.18327, published October 21, 2025

**Overview:**
InspectCoder is the first agentic program repair system that empowers LLMs to actively conduct dynamic analysis via interactive debugger control, with a dual-agent framework enabling strategic breakpoint placement, targeted state inspection, and incremental runtime experimentation within stateful debugger sessions.

**Key Results:**
InspectCoder achieves 5.10%-60.3
…[truncated 535 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 204 · 2026-05-26T10:27:35.603528+00:00_

Web search results for query: ""AgentFL" "ASE" OR "Automated Software Engineering" Qin 2024 accepted proceedings"

Links: [{"title":"2024 39th IEEE/ACM International Conference on Automated Software Engineering ASE","url":"https://www.aconf.org/conf_185997.html"},{"title":"ASE: Automated Software Engineering 2027 2026 2025 .. ...","url":"http://www.wikicfp.com/cfp/program?id=233"},{"title":"ASE 2024 - conf.researchr.org","url":"https://conf.researchr.org/home/ase-2024"},{"title":"[2405.15793] SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering","url":"https://arxiv.org/abs/2405.15793"},{"title":"ASE 2024 - Research Papers - conf.researchr.org","url":"https://conf.researchr.org/track/ase-2024/ase-2024-research"},{"title":"(PDF) SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering","url":"https://www.researchgate.net/publication/380907343_SWE-agent_Agent-Computer_Interfaces_Enable_Automated_Software_Engineering"},{"title":"NeurIPS Poster SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering","url":"https://neurips.cc/virtual/2024/poster/93753"},{"title":"ASE 2024 - Industry Showcase - conf.researchr.org","url":"https://conf.researchr.org/track/ase-2024/ase-2024-industry-showcase"},{"title":"ASE: Automated Software Engineering","url":"https://dl.acm.org/doi/proceedings/10.1145/3691620"}]

The search results show information about ASE 2024 (the 39th IEEE/ACM International Conference on Automated Software Engineering), but they don't contain specific results for a paper called "AgentFL" by Qin in the 2024 proceedings. Let me try a more specific search.

Links: [{"title":"[PDF] AgentFL: Scaling LLM-based Fault Localization to Project-Level Context | Semantic Scholar","url":"https://www.semanticscholar.org/paper/AgentFL:-Scaling-LLM-based-Fault-Localization-to-Qin-Wang/ed56e11c9c454bed81ec1396196998b9ca9f5a6c"},{"title":"[2403.16362] AgentFL: Scaling LLM-based Fault Localization to Project-Level Context","ur
…[truncated 1887 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 205 · 2026-05-26T10:27:35.603684+00:00_

Web search results for query: "site:dl.acm.org "TRACED" "3597503.3608140" author"

Links: [{"title":"TRACED: Execution-aware Pre-training for Source Code | Proceedings of the IEEE/ACM 46th International Conference on Software Engineering","url":"https://dl.acm.org/doi/10.1145/3597503.3608140"},{"title":"Software trace cache | ACM International Conference on Supercomputing 25th Anniversary Volume","url":"https://dl.acm.org/doi/10.1145/2591635.2667175"},{"title":"X-trace | Proceedings of the 4th USENIX conference on Networked systems design & implementation","url":"https://dl.acm.org/citation.cfm?id=1973450"},{"title":"TRACE: Trajectory-Aware Comprehensive Evaluation for Deep Research Agents | Proceedings of the ACM Web Conference 2026","url":"https://dl.acm.org/doi/10.1145/3774904.3792738"},{"title":"TraceDiag: Adaptive, Interpretable, and Efficient Root Cause Analysis on Large-Scale Microservice Systems | Proceedings of the 31st ACM Joint European Software Engineering Conference and Symposium on the Foundations of Software Engineering","url":"https://dl.acm.org/doi/10.1145/3611643.3613864"},{"title":"Trace-based Multi-Dimensional Root Cause Localization of Performance Issues in Microservice Systems | Proceedings of the IEEE/ACM 46th International Conference on Software Engineering","url":"https://dl.acm.org/doi/10.1145/3597503.3639088"},{"title":"Introducing the open trace format (OTF) | Proceedings of the 6th international conference on Computational Science - Volume Part II","url":"https://dl.acm.org/doi/10.1007/11758525_71"},{"title":". . Latest updates: hps://dl.acm.org/doi/10.1145/3729351 . . RESEARCH-ARTICLE","url":"https://dl.acm.org/doi/pdf/10.1145/3729351"}]

Based on the search results, I found the paper you're looking for. The authors of TRACED are Yangruibo Ding, Benjamin Steenhoek, Kexin Pei, Gail Kaiser, Wei Le, and Baishakhi Ray. The paper is titled "TRACED: Execution-aware Pre-training for Source Code" and was published in the Proceedings of the IEE
…[truncated 174 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 206 · 2026-05-26T10:27:35.603843+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arXiv 2409.12186 Qwen2.5-Coder authors list"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arXiv 2409.12186 Qwen2.5-Coder authors list"
  }
}
```

</details>

---

### Tool result

_source line 207 · 2026-05-26T10:27:35.604026+00:00_

Web search results for query: ""LDB: A Large Language Model Debugger via Verifying Runtime Execution Step by Step""

Links: [{"title":"GitHub - FloridSleeves/LLMDebugger: LDB: A Large Language Model Debugger via Verifying Runtime Execution Step by Step (ACL'24) · GitHub","url":"https://github.com/FloridSleeves/LLMDebugger"},{"title":"LDB: A Large Language Model Debugger via Verifying Runtime Execution Step by Step","url":"https://arxiv.org/html/2402.16906v1"},{"title":"Debug like a Human: A Large Language Model Debugger via Verifying Runtime Execution Step by Step","url":"https://arxiv.org/html/2402.16906v5"},{"title":"[2402.16906v3] LDB: A Large Language Model Debugger via Verifying Runtime Execution Step-by-step","url":"https://arxiv.org/abs/2402.16906v3"},{"title":"LDB: A Large Language Model Debugger Via Verifying Runtime Execution Step by Step | PDF | Software Bug | Debugging","url":"https://www.scribd.com/document/880943078/2402-16906v1"},{"title":"LDB: A Large Language Model Debugger via Verifying Runtime Execution Step-by-step | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/ldb-large-language-model-debugger-via-verifying"},{"title":"[AI Read] LDB: A Large Language Model Debugger via Verifying Runtime Execution Step-by-step","url":"https://www.arxivpaperai.com/papers/computer-science/ldb:-a-large-language-model-debugger-via-verifying-runtime-execution-step-by-step-240216906.html"},{"title":"Paper page - LDB: A Large Language Model Debugger via Verifying Runtime Execution Step-by-step","url":"https://huggingface.co/papers/2402.16906"}]

Based on the search results, here's what I found about LDB:

## Overview

LDB (Large Language Model Debugger) is a novel debugging framework that enables LLMs to refine their generated programs with runtime execution information. It was presented at ACL 2024.

## How It Works

LDB imitates how human developers debug programs by segmenting programs into basic blocks and tracking the values of intermedia
…[truncated 1048 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 208 · 2026-05-26T10:27:35.604187+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:dl.acm.org \"AgentFL\" 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:dl.acm.org \"AgentFL\" 2024"
  }
}
```

</details>

---

### Tool call

_source line 209 · 2026-05-26T10:27:35.604386+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Leveraging Large Language Model for Automatic Patch Correctness Assessment\" Zhou Xu Kim"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Leveraging Large Language Model for Automatic Patch Correctness Assessment\" Zhou Xu Kim"
  }
}
```

</details>

---

### Tool result

_source line 210 · 2026-05-26T10:27:35.604531+00:00_

Web search results for query: "arXiv 2409.12186 Qwen2.5-Coder authors list"

Links: [{"title":"[2409.12186] Qwen2.5-Coder Technical Report","url":"https://arxiv.org/abs/2409.12186"},{"title":"Qwen2.5-Coder Technical Report","url":"https://arxiv.org/html/2409.12186v1"},{"title":"[2409.12186v1] Qwen2.5-Coder Technical Report","url":"https://arxiv.org/abs/2409.12186v1"},{"title":"[2409.12186v3] Qwen2.5-Coder Technical Report","url":"https://arxiv.org/abs/2409.12186v3"},{"title":"Paper page - Qwen2.5-Coder Technical Report","url":"https://huggingface.co/papers/2409.12186"},{"title":"Qwen2.5-Coder Series: Powerful, Diverse, Practical. | Qwen","url":"https://qwenlm.github.io/blog/qwen2.5-coder-family/"},{"title":"Qwen2.5-Coder Technical Report | Request PDF","url":"https://www.researchgate.net/publication/384115782_Qwen25-Coder_Technical_Report"},{"title":"GitHub - huggingface/Qwen2.5-Coder: Qwen2.5-Coder is the code version of Qwen2.5, the large language model series developed by Qwen team, Alibaba Cloud. · GitHub","url":"https://github.com/huggingface/Qwen2.5-Coder"},{"title":"Qwen/Qwen2.5-Coder-1.5B · Hugging Face","url":"https://huggingface.co/Qwen/Qwen2.5-Coder-1.5B"}]

Based on the search results, here is the complete authors list for arXiv paper 2409.12186 (Qwen2.5-Coder Technical Report):

Binyuan Hui, Jian Yang, Zeyu Cui, Jiaxi Yang, Dayiheng Liu, Lei Zhang, Tianyu Liu, Jiajun Zhang, Bowen Yu, Keming Lu, Kai Dang, Yang Fan, Yichang Zhang, An Yang, Rui Men, Fei Huang, Bo Zheng, Yibo Miao, Shanghaoran Quan, Yunlong Feng, Xingzhang Ren, Xuancheng Ren, Jingren Zhou, and Junyang Lin.

The paper was last revised on November 12, 2024 (version 3).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 211 · 2026-05-26T10:27:35.604686+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Calibration and Correctness of Language Models for Code\" Spiess Gros full author list arXiv 2402.02047"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Calibration and Correctness of Language Models for Code\" Spiess Gros full author list arXiv 2402.02047"
  }
}
```

</details>

---

### Tool result

_source line 212 · 2026-05-26T10:27:35.604822+00:00_

Web search results for query: "site:dl.acm.org "AgentFL" 2024"

Links: [{"title":"LLM-Based Multi-Agent Systems for Software Engineering: Literature Review, Vision, and the Road Ahead | ACM Transactions on Software Engineering and Methodology","url":"https://dl.acm.org/doi/10.1145/3712003"},{"title":"Visibility into AI Agents | Proceedings of the 2024 ACM Conference on Fairness, Accountability, and Transparency","url":"https://dl.acm.org/doi/10.1145/3630106.3658948"},{"title":"Proceedings of the 23rd International Conference on Autonomous Agents and Multiagent Systems | ACM Conferences","url":"https://dl.acm.org/doi/proceedings/10.5555/3635637?tocHeading=heading1"},{"title":"Agent3D-Zero: An Agent for Zero-Shot 3D Understanding | Computer Vision – ECCV 2024","url":"https://dl.acm.org/doi/10.1007/978-3-031-72655-2_11"},{"title":"A Survey of Multi-AI Agent Collaboration: Theories, Technologies and Applications | Proceedings of the 2nd Guangdong-Hong Kong-Macao Greater Bay Area International Conference on Digital Economy and Artificial Intelligence","url":"https://dl.acm.org/doi/10.1145/3745238.3745531"},{"title":"AutoAgents | Proceedings of the Thirty-Third International Joint Conference on Artificial Intelligence","url":"https://dl.acm.org/doi/10.24963/ijcai.2024/3"},{"title":"Proceedings of the 24th International Conference on Autonomous Agents and Multiagent Systems | ACM Conferences","url":"https://dl.acm.org/doi/proceedings/10.5555/3709347"},{"title":"Proceedings of the 2024 3rd International Conference on Frontiers of Artificial Intelligence and Machine Learning | ACM Other conferences","url":"https://dl.acm.org/doi/proceedings/10.1145/3653644"},{"title":"The Role of AI Agents in the Reconfiguration of Interdisciplinary Educational Design: An Examination of Applied Practices and Outcomes | Proceedings of the 2024 9th International Conference on Distance Education and Learning","url":"https://dl.acm.org/doi/10.1145/3675812.3675833"}]

Based on the search results,
…[truncated 618 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 213 · 2026-05-26T10:27:35.604975+00:00_

Web search results for query: ""Leveraging Large Language Model for Automatic Patch Correctness Assessment" Zhou Xu Kim"

Links: [{"title":"Automatic Patch Correctness Assessment with Large Language Model","url":"https://arxiv.org/html/2303.00202v3"},{"title":"Leveraging Large Language Model for Automatic Patch Correctness Assessment | IEEE Transactions on Software Engineering","url":"https://dl.acm.org/doi/abs/10.1109/TSE.2024.3452252"},{"title":"Leveraging Large Language Model for Automatic Patch Correctness Assessment | IEEE Journals & Magazine | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/10659742/"},{"title":"Leveraging Large Language Model for Automatic Patch Correctness Assessment : Find an Expert : The University of Melbourne","url":"https://findanexpert.unimelb.edu.au/scholarlywork/1930021-leveraging-large-language-model-for-automatic-patch-correctness-assessment?cache=1737797463612"},{"title":"Leveraging Large Language Model for Automatic Patch Correctness Assessment | Request PDF","url":"https://www.researchgate.net/publication/383591189_Leveraging_Large_Language_Model_for_Automatic_Patch_Correctness_Assessment"},{"title":"Leveraging Large Language Model for Automatic Patch Correctness Assessment. | BibSonomy","url":"https://www.bibsonomy.org/bibtex/121733ba2498fa6c09e6b5ba222ae64ff"},{"title":"Leveraging Large Language Model for Automatic Patch Correctness Assessment - Peeref","url":"https://www.peeref.com/works/84586982/comments"}]

Based on the search results, I found the research you're looking for:

The paper "Leveraging Large Language Model for Automatic Patch Correctness Assessment" was authored by Xin Zhou, Bowen Xu, Kisub Kim, DongGyun Han, Hung Huu Nguyen, Thanh Le-Cong, Junda He, Bach Le, and David Lo, and was published in IEEE Transactions on Software Engineering in 2024.

The paper addresses the overfitting problem in Automated Program Repair (APR) techniques, where a generated patch can be incorrect although it passes all tests.
…[truncated 482 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 214 · 2026-05-26T10:27:35.605123+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "dblp.org \"ase2024\" AgentFL OR \"Yihao Qin\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "tool_args": {
    "query": "dblp.org \"ase2024\" AgentFL OR \"Yihao Qin\""
  }
}
```

</details>

---

### Tool call

_source line 215 · 2026-05-26T10:27:35.605273+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Wong Debroy Gao Li \"DStar\" \"Journal of Systems and Software\" 2014"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Wong Debroy Gao Li \"DStar\" \"Journal of Systems and Software\" 2014"
  }
}
```

</details>

---

### Tool result

_source line 216 · 2026-05-26T10:27:35.605410+00:00_

Web search results for query: "Wong Debroy Gao Li "DStar" "Journal of Systems and Software" 2014"

Links: [{"title":"[PDF] Software Fault Localization Using DStar (D*) | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Software-Fault-Localization-Using-DStar-(D*)-Wong-Debroy/dbfbaae06b0bad70792127044566e3a981516a34"},{"title":"The DStar Method for Effective Software Fault Localization | Semantic Scholar","url":"https://www.semanticscholar.org/paper/The-DStar-Method-for-Effective-Software-Fault-Wong-Debroy/db47f26a6b8cfc59f9c0fd135034ee25fbef554b"},{"title":"Professor Eric Wong's Recent Publications","url":"https://personal.utdallas.edu/~wew021000/Eric-Wong-Home-Page/Eric-publication.html"},{"title":"Effective software fault localization using predicted execution results | Software Quality Journal","url":"https://link.springer.com/article/10.1007/s11219-015-9295-1"},{"title":"Inforence: effective fault localization based on information-theoretic analysis and statistical causal inference | Frontiers of Computer Science | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11704-017-6512-z"},{"title":"[PDF] A Survey on Software Fault Localization | Semantic Scholar","url":"https://www.semanticscholar.org/paper/A-Survey-on-Software-Fault-Localization-Wong-Gao/4667536a1f2175c7b7bfe6113e4b316e64d35136"},{"title":"Figure 3 from Software Fault Localization Using DStar (D*) | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Software-Fault-Localization-Using-DStar-(D*)-Wong-Debroy/dbfbaae06b0bad70792127044566e3a981516a34/figure/4"},{"title":"Figure 5 from A family of code coverage-based heuristics for effective fault localization | Semantic Scholar","url":"https://www.semanticscholar.org/paper/A-family-of-code-coverage-based-heuristics-for-Wong-Debroy/b89e89bc57e5da88acbcdf0ef77722aa0d9afa76/figure/8"},{"title":"dblp: W. Eric Wong","url":"https://dblp.org/pid/w/WEricWong.html"}]

Based on the search results, I found information 
…[truncated 885 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 217 · 2026-05-26T10:27:35.605558+00:00_

Web search results for query: ""Calibration and Correctness of Language Models for Code" Spiess Gros full author list arXiv 2402.02047"

Links: [{"title":"[2402.02047] Calibration and Correctness of Language Models for Code","url":"https://arxiv.org/abs/2402.02047"},{"title":"Calibration and Correctness of Language Models for Code Claudio Spiess∗","url":"https://arxiv.org/pdf/2402.02047"},{"title":"Calibration and Correctness of Language Models for Code","url":"https://arxiv.org/html/2402.02047v3"},{"title":"Calibration and Correctness of Language Models for Code ICSE Artifact","url":"https://zenodo.org/records/14744842"},{"title":"Calibration and Correctness of Language Models for Code (ICSE 2025 - Research Track) - ICSE 2025","url":"https://conf.researchr.org/details/icse-2025/icse-2025-research-track/8/Calibration-and-Correctness-of-Language-Models-for-Code"},{"title":"Calibration and Correctness of Language Models for Code. | BibSonomy","url":"https://www.bibsonomy.org/bibtex/1f01e738a923b639d48c884eb35dfae8f"},{"title":"Precision or Peril: Evaluating Code Quality from Quantized Large Language Models","url":"https://arxiv.org/html/2411.10656v1"},{"title":"Calibration and Correctness of Language Models for Code | Proceedings of the IEEE/ACM 47th International Conference on Software Engineering","url":"https://dl.acm.org/doi/10.1109/ICSE55347.2025.00040"},{"title":"A Survey of Calibration Process for Black-Box LLMs","url":"https://arxiv.org/html/2412.12767v1"}]

Based on the search results, here is the full author list for the paper "Calibration and Correctness of Language Models for Code" (arXiv 2402.02047):

The authors are: Claudio Spiess, David Gros, Kunal Suresh Pai, Michael Pradel, Md Rafiqul Islam Rabin, Amin Alipour, Susmit Jha, Prem Devanbu, and Toufique Ahmed.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 218 · 2026-05-26T10:27:35.605709+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Wong Debroy Gao Li \"Software Fault Localization Using DStar\" \"Journal of Systems and Software\" volume 91"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Wong Debroy Gao Li \"Software Fault Localization Using DStar\" \"Journal of Systems and Software\" volume 91"
  }
}
```

</details>

---

### Tool result

_source line 219 · 2026-05-26T10:27:35.605834+00:00_

Web search results for query: "dblp.org "ase2024" AgentFL OR "Yihao Qin""

Links: [{"title":"[PDF] AgentFL: Scaling LLM-based Fault Localization to Project-Level Context | Semantic Scholar","url":"https://www.semanticscholar.org/paper/AgentFL:-Scaling-LLM-based-Fault-Localization-to-Qin-Wang/ed56e11c9c454bed81ec1396196998b9ca9f5a6c"},{"title":"dblp: ASE 2025","url":"https://dblp.org/db/conf/kbse/ase2025.html"},{"title":"dblp: Yihao Huang 0001","url":"https://dblp.org/pid/255/5085.html"},{"title":"dblp: ACL 2024","url":"https://dblp.org/db/conf/acl/acl2024-1.html"},{"title":"dblp: Yihao Liu (disambiguation)","url":"https://dblp.org/pid/200/6534.html"},{"title":"dblp: Shuang Cheng","url":"https://dblp.org/pid/157/0909.html"}]

Based on the search results, I found relevant information about AgentFL and Yihao Qin:

AgentFL is a multi-agent system based on ChatGPT for automated fault localization, authored by Yihao Qin, Shangwen Wang, and others, which outperforms other LLM-based approaches and exhibits complementarity to state-of-the-art learning-based techniques.

However, regarding ASE 2024 specifically, the search results did not return information about that conference proceedings. I found a reference to Yihao Qin publishing work titled "Let the Code Speak: Incorporating Program Dynamic State for Better Method-Level Fault Localization" in ASE 2025.

The search results indicate that AgentFL was published in 2024 (with ArXiv reference abs/2403.16362), but I did not find a specific DBLP entry for ASE 2024 with AgentFL in these results. You may want to visit DBLP directly or search for the specific ASE 2024 proceedings page for more complete information.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 220 · 2026-05-26T10:27:35.605979+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arXiv 2308.12950 \"Code Llama\" full author list Roziere"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arXiv 2308.12950 \"Code Llama\" full author list Roziere"
  }
}
```

</details>

---

### Tool call

_source line 221 · 2026-05-26T10:27:35.606111+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "SWE-bench \"Real-World\" OR \"Real-world\" ICLR 2024 official title Jimenez"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "tool_args": {
    "query": "SWE-bench \"Real-World\" OR \"Real-world\" ICLR 2024 official title Jimenez"
  }
}
```

</details>

---

### Tool result

_source line 222 · 2026-05-26T10:27:35.606254+00:00_

Web search results for query: "SWE-bench "Real-World" OR "Real-world" ICLR 2024 official title Jimenez"

Links: [{"title":"GitHub - SWE-bench/SWE-bench: SWE-bench: Can Language Models Resolve Real-world Github Issues? · GitHub","url":"https://github.com/SWE-bench/SWE-bench"},{"title":"Published as a conference paper at ICLR 2024 SWE-BENCH:","url":"https://arxiv.org/pdf/2310.06770"},{"title":"[2310.06770] SWE-bench: Can Language Models Resolve Real-World GitHub Issues?","url":"https://arxiv.org/abs/2310.06770"},{"title":"SWE-bench: Can Language Models Resolve Real-world Github Issues?","url":"https://proceedings.iclr.cc/paper_files/paper/2024/hash/edac78c3e300629acfe6cbe9ca88fb84-Abstract-Conference.html"},{"title":"ICLR Oral SWE-bench: Can Language Models Resolve Real-world Github Issues?","url":"https://iclr.cc/virtual/2024/oral/19757"},{"title":"GitHub - METR/SWE-bench-fork: [ICLR 2024] SWE-bench: Can Language Models Resolve Real-world Github Issues? · GitHub","url":"https://github.com/METR/SWE-bench-fork"},{"title":"SWE-BENCH: CAN LANGUAGE MODELS RESOLVE REAL-WORLD GITHUB ISSUES? - Princeton University","url":"https://collaborate.princeton.edu/en/publications/swe-bench-can-language-models-resolve-real-world-github-issues/"},{"title":"SWE-bench Citations","url":"https://www.swebench.com/citations.html"}]

Based on the search results, the official title of the paper is "SWE-bench: Can Language Models Resolve Real-world Github Issues?" This paper was published as a conference paper at ICLR 2024 by Carlos E Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press, and Karthik R Narasimhan.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 223 · 2026-05-26T10:27:35.606409+00:00_

Web search results for query: "arXiv 2308.12950 "Code Llama" full author list Roziere"

Links: [{"title":"[2308.12950] Code Llama: Open Foundation Models for Code","url":"https://arxiv.org/abs/2308.12950"},{"title":"[2308.12950] Code Llama: Open Foundation Models for Code","url":"http://export.arxiv.org/abs/2308.12950"},{"title":"Paper page - Code Llama: Open Foundation Models for Code","url":"https://huggingface.co/papers/2308.12950"},{"title":"Code Llama: Open Foundation Models for Code","url":"https://arxiv.org/pdf/2308.12950"},{"title":"[2308.12950v2] Code Llama: Open Foundation Models for Code","url":"https://arxiv.org/abs/2308.12950v2"},{"title":"[2308.12950v3] Code Llama: Open Foundation Models for Code","url":"https://arxiv.org/abs/2308.12950v3"},{"title":"(PDF) Code Llama: Open Foundation Models for Code","url":"https://www.researchgate.net/publication/373364143_Code_Llama_Open_Foundation_Models_for_Code"},{"title":"[PDF] Code Llama: Open Foundation Models for Code | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Code-Llama:-Open-Foundation-Models-for-Code-Rozi%C3%A8re-Gehring/0b0debb710366cdff461938c80763eace1651af6"},{"title":"Computation and Language Aug 2023","url":"http://arxiv.org/list/cs.CL/2023-08?skip=475&show=10"}]

The full author list for arXiv paper 2308.12950 "Code Llama: Open Foundation Models for Code" is: Baptiste Rozière, Jonas Gehring, Fabian Gloeckle, Sten Sootla, Itai Gat, Xiaoqing Ellen Tan, Yossi Adi, Jingyu Liu, Romain Sauvestre, Tal Remez, Jérémy Rapin, Artyom Kozhevnikov, Ivan Evtimov, Joanna Bitton, Manish Bhatt, Cristian Canton Ferrer, Aaron Grattafiori, Wenhan Xiong, Alexandre Défossez, Jade Copet, Faisal Azhar, Hugo Touvron, Louis Martin, Nicolas Usunier, Thomas Scialom, and Gabriel Synnaeve.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 224 · 2026-05-26T10:27:35.606548+00:00_

Web search results for query: "Wong Debroy Gao Li "Software Fault Localization Using DStar" "Journal of Systems and Software" volume 91"

Links: [{"title":"The DStar Method for Effective Software Fault Localization | Semantic Scholar","url":"https://www.semanticscholar.org/paper/The-DStar-Method-for-Effective-Software-Fault-Wong-Debroy/db47f26a6b8cfc59f9c0fd135034ee25fbef554b"},{"title":"[PDF] Software Fault Localization Using DStar (D*) | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Software-Fault-Localization-Using-DStar-(D*)-Wong-Debroy/dbfbaae06b0bad70792127044566e3a981516a34"},{"title":"Software Fault Localization Using DStar (D*)","url":"https://personal.utdallas.edu/~ewong/SE6367/01-Project/08-SFL-papers/06-DStar.pdf"},{"title":"Emerging Aspects of Software Fault Localization - Handbook of Software Fault Localization - Wiley Online Library","url":"https://onlinelibrary.wiley.com/doi/10.1002/9781119880929.ch13"},{"title":"Google Scholar","url":"https://scholar.google.com/scholar_lookup?doi=10.1109/TR.2013.2285319"},{"title":"Software Fault Localization: an Overview of Research, Techniques, and Tools - Handbook of Software Fault Localization - Wiley Online Library","url":"https://onlinelibrary.wiley.com/doi/10.1002/9781119880929.ch1"},{"title":"[PDF] A Survey on Software Fault Localization | Semantic Scholar","url":"https://www.semanticscholar.org/paper/A-Survey-on-Software-Fault-Localization-Wong-Gao/be0ed514aa9afa080e2fbc51a88d21543580179d"},{"title":"Figure 3 from Software Fault Localization Using DStar (D*) | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Software-Fault-Localization-Using-DStar-(D*)-Wong-Debroy/dbfbaae06b0bad70792127044566e3a981516a34/figure/4"}]

Based on the search results, I found information related to your query about Wong, Debroy, Gao, and Li's work on DStar (D*) for software fault localization.

The search results show that W. Eric Wong, Vidroha Debroy, Yihao Li, and Ruizhi Gao from the Department of
…[truncated 999 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 225 · 2026-05-26T10:27:35.606704+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2308.12950 code llama \"Rémi Lacroix\" OR \"Romain Sauvestre\" authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2308.12950 code llama \"Rémi Lacroix\" OR \"Romain Sauvestre\" authors"
  }
}
```

</details>

---

### Tool call

_source line 226 · 2026-05-26T10:27:35.606887+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "wong2014dstar doi \"10.1016/j.jss.2013.12.020\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "tool_args": {
    "query": "wong2014dstar doi \"10.1016/j.jss.2013.12.020\""
  }
}
```

</details>

---

### Tool result

_source line 227 · 2026-05-26T10:27:35.607242+00:00_

I now have all the information needed. Let me compile the verification report.

Here are the verification results for all 12 entries:

---

```
[abreu2007accuracy] Abreu(2007) "On the Accuracy of Spectrum-based..."
  Exists: ✓  Authors: ✓  Year: ✓  Title: ✓  Venue: ✓  arXiv: N/A
  Citation context: [related_work.tex:19] ✓ — Correctly cited as foundational SBFL work
  Issues: None. Venue is listed as "Testing: Academic and Industrial Conference Practice and Research Techniques (MUTATION)" which matches the official TAICPART-MUTATION 2007 proceedings. Note: the bib uses `journal=` but this is a conference paper; should use `booktitle=`. Minor formatting issue only.
```

```
[appt2024] Zhang(2024) "APPT: Boosting Automated Patch Correctness..."
  Exists: ✓  Authors: ✓  Year: ✓  Title: ✓  Venue: ✓  arXiv: N/A
  Citation context: [related_work.tex:17] ✓ — 79.7% accuracy claim matches the paper's reported results on Defects4J
  Issues: None. Published in IEEE TSE 2024, vol 50. The IEEE Xplore record (10402095) confirms the details. Title casing differs slightly between arXiv ("Pre-trained") and IEEE ("Pre-Trained") but this is cosmetic.
```

```
[austin2021program] Austin(2021) "Program Synthesis with Large Language..."
  Exists: ✓  Authors: ✓  Year: ✓  Title: ✓  Venue: ✓  arXiv: ✓ (2108.07732)
  Citation context: [introduction.tex:14] ✓ — MBPP-sanitized is indeed introduced in this paper
  Citation context: [method.tex:13] ✓ — Same correct usage
  Issues: None. This paper introduced the MBPP benchmark. arXiv ID correct.
```

```
[barr2015oracle] Barr(2015) "The Oracle Problem in Software Testing..."
  Exists: ✓  Authors: ✓  Year: ✓  Title: ✓  Venue: ✓  arXiv: N/A
  Citation context: [related_work.tex:15] ✓ — Verdict prediction as instance of oracle problem is a correct characterization
  Issues: None. IEEE TSE vol 41, no 5, pp 507-525, 2015 all confirmed. DOI correct.
```

```
[bengio2009curriculum] Bengio(2009) "Curriculum Learning"
  Exists: ✓  Authors: ✓  Year: ✓  Tit
…[truncated 4112 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "Agent",
  "elapsed_ms": 35
}
```

</details>

---

### Tool call

_source line 228 · 2026-05-26T10:27:35.607535+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"A Quantitative and Qualitative Evaluation of LLM-Based Explainable Fault Localization\" venue \"Proceedings of the ACM on Software Engineering\" OR \"FSE\" Kang"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"A Quantitative and Qualitative Evaluation of LLM-Based Explainable Fault Localization\" venue \"Proceedings of the ACM on Software Engineering\" OR \"FSE\" Kang"
  }
}
```

</details>

---

### Tool result

_source line 229 · 2026-05-26T10:27:35.607838+00:00_

Web search results for query: "arxiv 2308.12950 code llama "Rémi Lacroix" OR "Romain Sauvestre" authors"

Links: [{"title":"[2308.12950] Code Llama: Open Foundation Models for Code","url":"https://arxiv.org/abs/2308.12950"},{"title":"[2308.12950] Code Llama: Open Foundation Models for Code","url":"https://ar5iv.labs.arxiv.org/html/2308.12950"},{"title":"[2308.12950] Code Llama: Open Foundation Models for Code","url":"http://export.arxiv.org/abs/2308.12950"},{"title":"Paper page - Code Llama: Open Foundation Models for Code","url":"https://huggingface.co/papers/2308.12950"},{"title":"[2308.12950v3] Code Llama: Open Foundation Models for Code","url":"https://arxiv.org/abs/2308.12950v3"},{"title":"[PDF] Code Llama: Open Foundation Models for Code | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Code-Llama:-Open-Foundation-Models-for-Code-Rozi%C3%A8re-Gehring/0b0debb710366cdff461938c80763eace1651af6"},{"title":"[2308.12950v2] Code Llama: Open Foundation Models for Code","url":"https://arxiv.org/abs/2308.12950v2"},{"title":"(PDF) Code Llama: Open Foundation Models for Code","url":"https://www.researchgate.net/publication/373364143_Code_Llama_Open_Foundation_Models_for_Code"}]

Based on the search results, I found the paper you're looking for. The arxiv paper 2308.12950 is titled "Code Llama: Open Foundation Models for Code" and one of the authors listed is Romain Sauvestre. 

The paper was submitted on August 24, 2023, and the most recent version (v3) was updated on January 31, 2024. However, based on the search results, I did not find "Rémi Lacroix" listed as an author on this paper. The authors of the paper include Baptiste Rozière, Jonas Gehring, Fabian Gloeckle, Sten Sootla, Itai Gat, Xiaoqing Ellen Tan, Yossi Adi, Jingyu Liu, Romain Sauvestre, Tal Remez, Jérémy Rapin, Artyom Kozhevnikov, Ivan Evtimov, Joanna Bitton, Manish Bhatt, Cristian Canton Ferrer, Aaron Grattafiori, Wenhan Xiong, Alexandre Défossez, Jade Copet, Faisal Azhar, Hugo Touvron, Louis
…[truncated 166 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 230 · 2026-05-26T10:27:35.608094+00:00_

Web search results for query: "wong2014dstar doi "10.1016/j.jss.2013.12.020""

Links: [{"title":"DOI Name 10.1016 Values","url":"https://doi.org/10.1016"},{"title":"All-trans-retinoic acid counteract the tumor-stimulating effect of hepatectomy and increases survival of rats bearing liver metastases - PubMed","url":"https://pubmed.ncbi.nlm.nih.gov/24439134/"},{"title":"All-trans-retinoic acid counteract the tumor-stimulating effect of hepatectomy and increases survival of rats bearing liver metastases - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0022480413021987"},{"title":"Cellular and synaptic specializations for sub-millisecond ...","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12127432/"},{"title":"Design of a Superelastic Alloy Uniting Large Functional Response and Exceptional Cyclic Stability - Dang - Advanced Functional Materials - Wiley Online Library","url":"https://advanced.onlinelibrary.wiley.com/doi/abs/10.1002/adfm.202520629"},{"title":"ScienceDirect.com | Science, health and medical journals, full text articles and books.","url":"https://www.sciencedirect.com/science/article/pii/S0099239914008991"},{"title":"Wenbo Wu (0000-0002-7642-9773)","url":"https://orcid.org/0000-0002-7642-9773"},{"title":"Missed Opportunities to Diagnose and Treat Tertiary Hyperparathyroidism After Transplant - PubMed","url":"https://pubmed.ncbi.nlm.nih.gov/36857809/"},{"title":"DaaS: Cloud-based mobile Web service discovery: Pervasive and Mobile Computing: Vol 13, No null","url":"https://dl.acm.org/doi/abs/10.1016/j.pmcj.2013.10.015"},{"title":"The Persistence of Sex Bias in High-Impact Clinical Research","url":"https://pubmed.ncbi.nlm.nih.gov/35687931/"}]

Based on the search results, the DOI 10.1016/j.jss.2013.12.020 refers to an article published in 2014, May 1. However, the search results don't contain information about a publication with the author "wong2014dstar" associated with this DOI.

The article with this DOI is titled "All-trans-r
…[truncated 587 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 231 · 2026-05-26T10:27:35.608361+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Software Fault Localization Using DStar\" \"Journal of Systems and Software\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Software Fault Localization Using DStar\" \"Journal of Systems and Software\""
  }
}
```

</details>

---

### Tool call

_source line 232 · 2026-05-26T10:27:35.608569+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2509.11686 \"Do Code Semantics Help\" authors \"Jian Wang\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2509.11686 \"Do Code Semantics Help\" authors \"Jian Wang\""
  }
}
```

</details>

---

### Tool result

_source line 233 · 2026-05-26T10:27:35.608762+00:00_

Web search results for query: "arxiv 2509.11686 "Do Code Semantics Help" authors "Jian Wang""

Links: [{"title":"[2509.11686] Do Code Semantics Help? A Comprehensive Study on Execution Trace-Based Information for Code Large Language Models","url":"https://arxiv.org/abs/2509.11686"},{"title":"[2509.11686v3] Do Code Semantics Help? A Comprehensive Study on Execution Trace-Based Information for Code Large Language Models","url":"https://arxiv.org/abs/2509.11686v3"},{"title":"Do Code Semantics Help? A Comprehensive Study on Execution","url":"https://arxiv.org/pdf/2509.11686"},{"title":"Do Code Semantics Help? A Comprehensive Study on Execution Trace-Based Information for Code Large Language Models","url":"https://arxiv.org/html/2509.11686"},{"title":"Computation and Language 2025","url":"https://arxiv.org/list/cs.CL/2025?skip=12600&show=50"},{"title":"Are Large Language Models Robust in Understanding Code Against Semantics-Preserving Mutations?","url":"https://arxiv.org/html/2505.10443v3"}]

I found the paper you're looking for. Here are the key details:

**Paper Title:** Do Code Semantics Help? A Comprehensive Study on Execution Trace-Based Information for Code Large Language Models

**Authors:** Jian Wang, Xiaofei Xie, Qiang Hu, Shangqing Liu, Yi Li

**Affiliations:** Jian Wang and Yi Li are from Nanyang Technological University, Singapore; Xiaofei Xie is from Singapore Management University; Qiang Hu is from Tianjin University, China; and Shangqing Liu is from the State Key Laboratory for Novel Software Technology, Nanjing University, China

**Key Focus:** The paper addresses critical limitations in Code LLMs' ability to reason about runtime behavior and understand program functionality, specifically examining the lack of proficiency in reasoning about program execution behavior and the inconsistent representation of semantic information like execution traces

**Submission Details:** The paper was submitted on September 15, 2025 (v1) and last revised on September 24,
…[truncated 182 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 234 · 2026-05-26T10:27:35.608986+00:00_

Web search results for query: ""Software Fault Localization Using DStar" "Journal of Systems and Software""

Links: [{"title":"The DStar Method for Effective Software Fault Localization | IEEE Journals & Magazine | IEEE Xplore","url":"https://ieeexplore.ieee.org/abstract/document/6651713/"},{"title":"Software Fault Localization Using DStar (D*) | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/6258291"},{"title":"The DStar Method for Effective Software Fault Localization | Request PDF","url":"https://www.researchgate.net/publication/260524645_The_DStar_Method_for_Effective_Software_Fault_Localization"},{"title":"Software Fault Localization Using DStar (D*)","url":"https://personal.utdallas.edu/~ewong/SE6367/01-Project/08-SFL-papers/06-DStar.pdf"},{"title":"[PDF] Software Fault Localization Using DStar (D*) | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Software-Fault-Localization-Using-DStar-(D*)-Wong-Debroy/dbfbaae06b0bad70792127044566e3a981516a34"},{"title":"The DStar Method for Effective Software Fault Localization | Semantic Scholar","url":"https://www.semanticscholar.org/paper/The-DStar-Method-for-Effective-Software-Fault-Wong-Debroy/db47f26a6b8cfc59f9c0fd135034ee25fbef554b"},{"title":"Figure 3 from Software Fault Localization Using DStar (D*) | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Software-Fault-Localization-Using-DStar-(D*)-Wong-Debroy/dbfbaae06b0bad70792127044566e3a981516a34/figure/4"},{"title":"Software Fault Localization for Programs with Multiple Bugs - Handbook of Software Fault Localization - Wiley Online Library","url":"https://onlinelibrary.wiley.com/doi/abs/10.1002/9781119880929.ch12"},{"title":" Abstract— Fault localization is considered one of the most","url":"https://jcoms.fesb.unist.hr/pdfs/402.pdf"}]

I've found research related to Software Fault Localization Using DStar. Here are the key findings:

DStar (D*) is a technique with origins rooted in similarity coef
…[truncated 1160 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 235 · 2026-05-26T10:27:35.609238+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Do Code Semantics Help\" wang ACL Anthology EMNLP 2025 findings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Do Code Semantics Help\" wang ACL Anthology EMNLP 2025 findings"
  }
}
```

</details>

---

### Tool result

_source line 236 · 2026-05-26T10:27:35.609455+00:00_

Web search results for query: ""A Quantitative and Qualitative Evaluation of LLM-Based Explainable Fault Localization" venue "Proceedings of the ACM on Software Engineering" OR "FSE" Kang"

Links: [{"title":"A Quantitative and Qualitative Evaluation of LLM-Based Explainable Fault Localization | Proceedings of the ACM on Software Engineering","url":"https://dl.acm.org/doi/10.1145/3660771"},{"title":"[2308.05487] A Quantitative and Qualitative Evaluation of LLM-Based Explainable Fault Localization","url":"https://arxiv.org/abs/2308.05487"},{"title":"A Quantitative and Qualitative Evaluation of LLM-Based Explainable Fault Localization | Request PDF","url":"https://www.researchgate.net/publication/382236264_A_Quantitative_and_Qualitative_Evaluation_of_LLM-Based_Explainable_Fault_Localization"},{"title":"[PDF] A Quantitative and Qualitative Evaluation of LLM-Based Explainable Fault Localization | Semantic Scholar","url":"https://www.semanticscholar.org/paper/A-Quantitative-and-Qualitative-Evaluation-of-Fault-Kang-An/9ac304b5531d5adc1b5021dfc0dbe6e90b41c406"},{"title":"A Quantitative and Qualitative Evaluation of LLM-Based Explainable Fault Localization","url":"https://arxiv.org/html/2308.05487v3"},{"title":"A Quantitative and Qualitative Evaluation of LLM-based Explainable Fault Localization (FSE 2024 - Research Papers) - FSE 2024","url":"https://2024.esec-fse.org/details/fse-2024-research-papers/15/A-Quantitative-and-Qualitative-Evaluation-of-LLM-based-Explainable-Fault-Localization"},{"title":"A Quantitative and Qualitative Evaluation of LLM-based Explainable Fault Localization (FSE 2024 - Posters) - FSE 2024","url":"https://2024.esec-fse.org/details/fse-2024-posters/19/A-Quantitative-and-Qualitative-Evaluation-of-LLM-based-Explainable-Fault-Localization"},{"title":"Our paper \"A Quantitative and Qualitative Evaluation of LLM-based Explainable Fault Localization\" has been accepted to FSE 2024","url":"https://coinse.github.io/2024/04/24/AutoFL-FSE-2024.html"}]

Based o
…[truncated 887 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 237 · 2026-05-26T10:27:35.609664+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CRUXEval-X authors \"Ruiyang Xu\" ACL 2025 full author list"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CRUXEval-X authors \"Ruiyang Xu\" ACL 2025 full author list"
  }
}
```

</details>

---

### Tool call

_source line 238 · 2026-05-26T10:27:35.609810+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Mutation Testing Advances\" Papadakis \"Advances in Computers\" volume 112 2019"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Mutation Testing Advances\" Papadakis \"Advances in Computers\" volume 112 2019"
  }
}
```

</details>

---

### Tool result

_source line 239 · 2026-05-26T10:27:35.609945+00:00_

Web search results for query: ""Do Code Semantics Help" wang ACL Anthology EMNLP 2025 findings"

Links: [{"title":"Do Code Semantics Help? A Comprehensive Study on Execution Trace-Based Information for Code Large Language Models - ACL Anthology","url":"https://aclanthology.org/2025.findings-emnlp.548/"},{"title":"Do Code Semantics Help? A Comprehensive Study on ...","url":"https://aclanthology.org/2025.findings-emnlp.548.pdf"},{"title":"Few-Shot Semantic Parsing with Language Models Trained On Code","url":"https://arxiv.org/pdf/2112.08696"},{"title":"Emergent Representations of Program Semantics in Language Models Trained   on Programs","url":"https://arxiv.org/pdf/2305.11169"},{"title":"CodeQueries: A Dataset of Semantic Queries over Code","url":"https://arxiv.org/pdf/2209.08372"},{"title":"Leveraging Code to Improve In-context Learning for Semantic Parsing","url":"https://arxiv.org/pdf/2311.09519"},{"title":"Grammar-Based Code Representation: Is It a Worthy Pursuit for LLMs?","url":"https://arxiv.org/pdf/2503.05507"}]

I found the paper you're looking for! "Do Code Semantics Help? A Comprehensive Study on Execution Trace-Based Information for Code Large Language Models" is published in the Findings of the Association for Computational Linguistics: EMNLP 2025.

The paper is authored by Jian Wang, Xiaofei Xie, Qiang Hu, Shangqing Liu, and Yi Li. 

The paper addresses critical limitations in Code LLMs' ability to reason about runtime behavior and understand the actual functionality of programs, which poses significant challenges for their post-training and practical deployment. The research appears to investigate whether incorporating execution trace-based semantic information can help improve Code LLMs' understanding and capabilities.

You can access the full paper at: https://aclanthology.org/2025.findings-emnlp.548/


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 240 · 2026-05-26T10:27:35.610097+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Evaluating Representation Learning of Code Changes\" Tian 2020 ASE full author Kaboré OR Kaboreé"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Evaluating Representation Learning of Code Changes\" Tian 2020 ASE full author Kaboré OR Kaboreé"
  }
}
```

</details>

---

### Tool result

_source line 241 · 2026-05-26T10:27:35.610248+00:00_

Web search results for query: "CRUXEval-X authors "Ruiyang Xu" ACL 2025 full author list"

Links: [{"title":"CRUXEVAL-X: A Benchmark for Multilingual Code ...","url":"https://aclanthology.org/2025.acl-long.1158.pdf"},{"title":"CRUXEVAL-X: A Benchmark for Multilingual Code Reasoning, Understanding and Execution - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.1158/"},{"title":"dblp: Ruiyang Xu","url":"https://dblp.org/pid/172/5569.html"},{"title":"[2408.13001] CRUXEval-X: A Benchmark for Multilingual Code Reasoning, Understanding and Execution","url":"https://arxiv.org/abs/2408.13001"},{"title":"CRUXEval-X: A Benchmark for Multilingual Code Reasoning, Understanding and Execution","url":"https://arxiv.org/pdf/2408.13001"},{"title":"Ruiyang Xu - ACL Anthology","url":"https://aclanthology.org/people/ruiyang-xu/"},{"title":"[PDF] CRUXEval-X: A Benchmark for Multilingual Code Reasoning, Understanding and Execution | Semantic Scholar","url":"https://www.semanticscholar.org/paper/CRUXEval-X:-A-Benchmark-for-Multilingual-Code-and-Xu-Cao/88d48041a76ddc4318c360cdda0a4e1379eeefb3"},{"title":"(PDF) CRUXEval-X: A Benchmark for Multilingual Code Reasoning, Understanding and Execution","url":"https://www.researchgate.net/publication/383413276_CRUXEval-X_A_Benchmark_for_Multilingual_Code_Reasoning_Understanding_and_Execution"}]

Based on the search results, here is the full author list for the CRUXEval-X paper accepted at ACL 2025:

The authors of "CRUXEVAL-X: A Benchmark for Multilingual Code Reasoning, Understanding and Execution" are: Ruiyang Xu, Jialun Cao, Yaojie Lu, Ming Wen, Hongyu Lin, Xianpei Han, Ben He, Shing-Chi Cheung, and Le Sun.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 242 · 2026-05-26T10:27:35.610419+00:00_

Web search results for query: ""Mutation Testing Advances" Papadakis "Advances in Computers" volume 112 2019"

Links: [{"title":"Advances in Computers, Volume 112 - 1st Edition | Elsevier Shop","url":"https://shop.elsevier.com/books/advances-in-computers/memon/978-0-12-815121-1"},{"title":"dblp: Chapter Six - Mutation Testing Advances: An Analysis and Survey.","url":"https://dblp.org/rec/journals/ac/PapadakisK00TH19.html"},{"title":"Mutation Testing Advances: An Analysis and Survey | Request PDF","url":"https://www.researchgate.net/publication/325014033_Mutation_Testing_Advances_An_Analysis_and_Survey"},{"title":"A Survey on Mutation Testing | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-031-78946-5_20"},{"title":"ORBilu: Detailed Reference","url":"https://orbilu.uni.lu/handle/10993/54578"},{"title":"Mutation Testing Advances: An Analysis and Survey - ScienceDirect","url":"https://www.sciencedirect.com/science/chapter/bookseries/abs/pii/S0065245818300305"},{"title":"Keeping Mutation Test Suites Consistent and Relevant with Long-Standing Mutants","url":"https://discovery.ucl.ac.uk/id/eprint/10184856/1/3611643.3613089.pdf"},{"title":"Mutation Testing Advances: An Analysis and Survey","url":"https://scite.ai/reports/mutation-testing-advances-an-analysis-ZGEyL6y"},{"title":"Mutant Reduction Evaluation: What is There and What is Missing? | ACM Transactions on Software Engineering and Methodology","url":"https://dl.acm.org/doi/10.1145/3522578"}]

The search has successfully found information about the publication you requested. Here are the key details:

The article "Mutation Testing Advances: An Analysis and Survey" was authored by Mike Papadakis, Marinos Kintis, Jie Zhang, Yue Jia, Yves Le Traon and Mark Harman. It appears as Chapter Six in Advances in Computers, volume 112, pages 275-378, published in 2019.

The chapter covers how mutation testing realizes the idea of using artificial defects to support testing activities, and is typical
…[truncated 425 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 243 · 2026-05-26T10:27:35.610572+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Agentless Xia Deng Dunn Zhang NeurIPS 2024 venue"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Agentless Xia Deng Dunn Zhang NeurIPS 2024 venue"
  }
}
```

</details>

---

### Tool call

_source line 244 · 2026-05-26T10:27:35.610703+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "NExT ICML 2024 \"Ansong Ni\" \"Miltiadis Allamanis\" \"Arman Cohan\" authors proceedings machine learning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "tool_args": {
    "query": "NExT ICML 2024 \"Ansong Ni\" \"Miltiadis Allamanis\" \"Arman Cohan\" authors proceedings machine learning"
  }
}
```

</details>

---

### Tool result

_source line 245 · 2026-05-26T10:27:35.610838+00:00_

Web search results for query: ""Evaluating Representation Learning of Code Changes" Tian 2020 ASE full author Kaboré OR Kaboreé"

Links: [{"title":"Evaluating Representation Learning of Code Changes for ...","url":"https://kui-liu.github.io/papers/tian2020evaluating.pdf"},{"title":"Evaluating representation learning of code changes for predicting patch correctness in program repair - Monash University","url":"https://research.monash.edu/en/publications/evaluating-representation-learning-of-code-changes-for-predicting/"},{"title":"Evaluating representation learning of code changes for predicting patch correctness in program repair | Proceedings of the 35th IEEE/ACM International Conference on Automated Software Engineering","url":"https://dl.acm.org/doi/10.1145/3324884.3416532"},{"title":"[PDF] Evaluating Representation Learning of Code Changes for Predicting Patch Correctness in Program Repair | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Evaluating-Representation-Learning-of-Code-Changes-Tian-Liu/521b813aeb71162fe74ad09da4a2bbbcd9919b70"},{"title":"Evaluating Representation Learning of Code Changes for Predicting Patch Correctness in Program Repair | Request PDF","url":"https://www.researchgate.net/publication/343546393_Evaluating_Representation_Learning_of_Code_Changes_for_Predicting_Patch_Correctness_in_Program_Repair"},{"title":"Table 1 from Evaluating Representation Learning of Code Changes for Predicting Patch Correctness in Program Repair | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Evaluating-Representation-Learning-of-Code-Changes-Tian-Liu/67bc0ca2d6d5490e70efa0101ecc1c04d2ecfb1d/figure/0"},{"title":"Learning to represent code changes | Empirical Software Engineering | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10664-025-10763-6"},{"title":"[2008.02944] Evaluating Representation Learning of Code Changes for Predicting Patch Correctness in Program Repair","url":"https://ar5iv.labs.arxiv.org/
…[truncated 669 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 246 · 2026-05-26T10:27:35.610987+00:00_

Web search results for query: "Agentless Xia Deng Dunn Zhang NeurIPS 2024 venue"

Links: [{"title":"[PDF] Demystifying LLM-Based Software Engineering Agents | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Demystifying-LLM-Based-Software-Engineering-Agents-Xia-Deng/d712280b0d51ff648eb2091c619bc55a2e1164fa"},{"title":"Welcome to Soren Dunn’s Homepage","url":"https://sorendunn.github.io/"},{"title":"(PDF) Agentless: Demystifying LLM-based Software Engineering Agents","url":"https://www.researchgate.net/publication/381911059_Agentless_Demystifying_LLM-based_Software_Engineering_Agents"},{"title":"38th NeurIPS 2024: Vancouver, BC, Canada","url":"https://dblp.org/db/conf/nips/neurips2024.html"},{"title":"Google at NeurIPS 2024","url":"https://research.google/conferences-and-events/google-at-neurips-2024/"},{"title":"NeurIPS 2024 Daily Schedule","url":"https://neurips.cc/virtual/2024/daily-schedule/?date=2024-12-15"},{"title":"Strong Northwestern Presence at the 2024 NeurIPS Conference | News & Events | Computer Science | Northwestern Engineering","url":"https://www.mccormick.northwestern.edu/computer-science/news-events/news/articles/2024/strong-northwestern-presence-at-the-2024-neurips-conference.html"}]

Based on the search results, I found relevant information about the Agentless paper by Xia, Deng, Dunn, and Zhang:

NeurIPS 2024 took place in Vancouver, BC, Canada. 

However, it's important to note that based on the search results, the Agentless paper by Chun Xia, Yinlin Deng, Soren Dunn, and Lingming Zhang was published in the Proceedings of the ACM on Software Engineering in 2025, rather than being presented at NeurIPS 2024. The paper appears to have been initially shared in July 2024 but was published in a different venue.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 247 · 2026-05-26T10:27:35.611136+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"How to Train Data-Efficient LLMs\" Sachdeva venue conference publication 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"How to Train Data-Efficient LLMs\" Sachdeva venue conference publication 2024"
  }
}
```

</details>

---

### Tool call

_source line 248 · 2026-05-26T10:27:35.611327+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Agentless Xia Deng Dunn Zhang \"FSE\" OR \"ICSE\" OR \"ASE\" 2025 published venue"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Agentless Xia Deng Dunn Zhang \"FSE\" OR \"ICSE\" OR \"ASE\" 2025 published venue"
  }
}
```

</details>

---

### Tool result

_source line 249 · 2026-05-26T10:27:35.611502+00:00_

Web search results for query: "NExT ICML 2024 "Ansong Ni" "Miltiadis Allamanis" "Arman Cohan" authors proceedings machine learning"

Links: [{"title":"dblp: Miltiadis Allamanis","url":"https://dblp.org/pid/121/4943.html"},{"title":"[PDF] NExT: Teaching Large Language Models to Reason about Code Execution | Semantic Scholar","url":"https://www.semanticscholar.org/paper/NExT:-Teaching-Large-Language-Models-to-Reason-Code-Ni-Allamanis/49306aa1fde2a21fadc77dbc8ec7e487fac72c5b"},{"title":"dblp: Ansong Ni","url":"https://dblp.org/pid/202/1480.html"},{"title":"NExT: Teaching Large Language Models to Reason about Code Execution","url":"https://proceedings.mlr.press/v235/ni24a.html"},{"title":"dblp: Pengcheng Yin","url":"https://dblp.org/pid/130/7385.html"},{"title":"[2404.14662] NExT: Teaching Large Language Models to Reason about Code Execution","url":"https://arxiv.org/abs/2404.14662"},{"title":"dblp: Kensen Shi","url":"https://dblp.org/pid/135/8307.html"},{"title":"dblp: BibTeX records: Charles Sutton","url":"https://dblp.uni-trier.de/pid/59/5879.html?view=bibtex"},{"title":"Ansong’s Page","url":"https://niansong1996.github.io/"}]

Based on the search results, I found the paper you're looking for:

**NExT: Teaching Large Language Models to Reason about Code Execution** by Ansong Ni, Miltiadis Allamanis, Arman Cohan, Yinlin Deng, Kensen Shi, Charles Sutton, and Pengcheng Yin was published in the Proceedings of the 41st International Conference on Machine Learning (ICML 2024), pages 37929-37956.

The paper addresses how a fundamental skill among human developers is the ability to understand and reason about program execution, while large language models (LLMs) of code typically trained on the surface textual form of programs may lack semantic understanding of how programs execute at run-time.

The paper is available through multiple sources including the official PMLR proceedings, arXiv (2404.14662), and academic databases like DBLP and Semantic Scholar.


REMINDER: You MU
…[truncated 84 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 250 · 2026-05-26T10:27:35.611662+00:00_

Web search results for query: ""How to Train Data-Efficient LLMs" Sachdeva venue conference publication 2024"

Links: [{"title":"[2402.09668] How to Train Data-Efficient LLMs","url":"https://arxiv.org/abs/2402.09668"},{"title":"[PDF] How to Train Data-Efficient LLMs | Semantic Scholar","url":"https://www.semanticscholar.org/paper/How-to-Train-Data-Efficient-LLMs-Sachdeva-Coleman/31b2918acc77682b5a499da1aa111f34e76d9603"},{"title":"How to Train Data-Efficient LLMs","url":"https://www.linkedin.com/pulse/how-train-data-efficient-llms-vlad-bogolin-fai5e"},{"title":"How to Train Data-Efficient LLMs - Vlad Bogolin","url":"https://vladbogo.com/blog/2024/02/19/how-to-train.html"},{"title":"GitHub - susumuota/nano-askllm: Unofficial implementation of the Ask-LLM paper 'How to Train Data-Efficient LLMs', arXiv:2402.09668. · GitHub","url":"https://github.com/susumuota/nano-askllm"},{"title":"How to train data-efficient LLMs | OpenReview","url":"https://openreview.net/forum?id=yKUbw7q1IA"},{"title":"Federated Data-Efficient Instruction Tuning for Large Language Models","url":"https://arxiv.org/html/2410.10926v2"},{"title":"Beyond Random Sampling: Efficient Language Model Pretraining via Curriculum Learning","url":"https://arxiv.org/html/2506.11300v1"},{"title":"Towards Data-efficient Machine Learning Systems","url":"https://escholarship.org/uc/item/8nb955b8"},{"title":"A Survey on Efficient Large Language Model Training: From Data-centric Perspectives","url":"https://arxiv.org/pdf/2510.25817"}]

Based on the search results, here's what I found about "How to Train Data-Efficient LLMs" by Sachdeva:

## Publication Details

The paper is by Noveen Sachdeva and was published on February 15, 2024. The full author list includes Noveen Sachdeva, Benjamin Coleman, Wang-Cheng Kang, Jianmo Ni, Lichan Hong, Ed H. Chi, James Caverlee, Julian McAuley, and Derek Zhiyuan Cheng.

## Publication Venue

The paper appears to have been published on **arXiv** (arXiv:2402.09668). The search results s
…[truncated 908 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 251 · 2026-05-26T10:27:35.611811+00:00_

Web search results for query: "Agentless Xia Deng Dunn Zhang "FSE" OR "ICSE" OR "ASE" 2025 published venue"

Links: [{"title":"ALMAS: an Autonomous LLM-based Multi-Agent Software Engineering Framework","url":"https://arxiv.org/pdf/2510.03463"},{"title":"The Design Space of LLM-Based AI Coding Assistants: An Analysis of 90 Systems","url":"https://lau.ucsd.edu/pubs/2025_analysis-of-90-genai-coding-tools_VLHCC.pdf"},{"title":"Lingming Zhang's Homepage","url":"https://lingming.cs.illinois.edu/publication.html"},{"title":"Distinguished Paper Award","url":"https://www2.sigsoft.org/awards/distinguishedpaper/"},{"title":"Demystifying LLM-Based Software Engineering Agents","url":"https://lingming.cs.illinois.edu/publications/fse2025.pdf"},{"title":"Zishuo Ding's Homepage - Homepage","url":"https://personal.hkust-gz.edu.cn/ding/"}]

Based on the search results, the paper "Agentless: Demystifying LLM-based Software Engineering Agents" by C. S. Xia, Y. Deng, S. Dunn, and L. Zhang was published in Proceedings of the 2025 ACM SIGSOFT International Symposium on the Foundations of Software Engineering (FSE '25) in 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 252 · 2026-05-26T10:27:35.611954+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "LDB debugger Zhong Wang Shang ACL 2024 Findings venue"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "tool_args": {
    "query": "LDB debugger Zhong Wang Shang ACL 2024 Findings venue"
  }
}
```

</details>

---

### Tool result

_source line 253 · 2026-05-26T10:27:35.612080+00:00_

Web search results for query: "LDB debugger Zhong Wang Shang ACL 2024 Findings venue"

Links: [{"title":"Debug like a Human: A Large Language Model Debugger via Verifying Runtime Execution Step by Step - ACL Anthology","url":"https://aclanthology.org/2024.findings-acl.49/"},{"title":"[PDF] Debug like a Human: A Large Language Model Debugger via Verifying Runtime Execution Step by Step | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Debug-like-a-Human:-A-Large-Language-Model-Debugger-Zhong-Wang/c6c584ea3983627329eebff7c78951938b227351"},{"title":"Findings of the Association for Computational Linguistics: ACL 2024 - ACL Anthology","url":"https://aclanthology.org/volumes/2024.findings-acl/"},{"title":"fly51fly on X: \"[CL] LDB: A Large Language Model Debugger via Verifying Runtime Execution Step-by-step L Zhong, Z Wang, J Shang [University of California, San Diego] (2024) https://t.co/9iDi9Bmg5m - The paper proposes LDB, a novel debugging framework that enables LLMs to refine their generated https://t.co/GLFYfvRu5p\" / X","url":"https://x.com/fly51fly/status/1764275980502433834"},{"title":"dblp: ACL 2024","url":"https://dblp.org/db/conf/acl/acl2024f.html"},{"title":"Accepted Findings Papers - ACL 2024","url":"https://2024.aclweb.org/program/finding_papers/"}]

Based on the search results, I found the paper you're looking for:

The paper "Debug like a Human: A Large Language Model Debugger via Verifying Runtime Execution Step by Step" was authored by Li Zhong, Zilong Wang, and Jingbo Shang and published in the Findings of the Association for Computational Linguistics: ACL 2024.

The paper introduces LDB, a novel debugging framework that enables LLMs to refine their generated programs using runtime execution information. LDB consistently enhances baseline performance by up to 9.8% across the HumanEval, MBPP, and TransCoder benchmarks, achieving new state-of-the-art performance in code debugging for various LLM selections.


REMINDER: You MUST include the
…[truncated 70 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 254 · 2026-05-26T10:27:35.612257+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "LDB Zhong Wang Shang title \"Debug like a Human\" OR \"LDB: A Large Language Model Debugger\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "tool_args": {
    "query": "LDB Zhong Wang Shang title \"Debug like a Human\" OR \"LDB: A Large Language Model Debugger\""
  }
}
```

</details>

---

### Tool result

_source line 255 · 2026-05-26T10:27:35.612404+00:00_

Web search results for query: "LDB Zhong Wang Shang title "Debug like a Human" OR "LDB: A Large Language Model Debugger""

Links: [{"title":"[2402.16906] Debug like a Human: A Large Language Model Debugger via Verifying Runtime Execution Step-by-step","url":"https://arxiv.org/abs/2402.16906"},{"title":"GitHub - FloridSleeves/LLMDebugger: LDB: A Large Language Model Debugger via Verifying Runtime Execution Step by Step (ACL'24) · GitHub","url":"https://github.com/FloridSleeves/LLMDebugger"},{"title":"Debug like a Human: A Large Language Model Debugger via Verifying Runtime Execution Step by Step - ACL Anthology","url":"https://aclanthology.org/2024.findings-acl.49/"},{"title":"[PDF] Debug like a Human: A Large Language Model Debugger via Verifying Runtime Execution Step by Step | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Debug-like-a-Human:-A-Large-Language-Model-Debugger-Zhong-Wang/c6c584ea3983627329eebff7c78951938b227351"},{"title":"Debug like a Human: A Large Language Model Debugger via Verifying Runtime Execution Step by Step","url":"https://arxiv.org/html/2402.16906v5"},{"title":"Debug like a Human: A Large Language Model Debugger via Verifying","url":"https://arxiv.org/pdf/2402.16906"},{"title":"LDB: A Large Language Model Debugger via Verifying Runtime Execution Step by Step","url":"https://arxiv.org/html/2402.16906v2"},{"title":"fly51fly on X: \"[CL] LDB: A Large Language Model Debugger via Verifying Runtime Execution Step-by-step L Zhong, Z Wang, J Shang [University of California, San Diego] (2024) https://t.co/9iDi9Bmg5m - The paper proposes LDB, a novel debugging framework that enables LLMs to refine their generated https://t.co/GLFYfvRu5p\" / X","url":"https://x.com/fly51fly/status/1764275980502433834"},{"title":"Québec.AI on X: \"Debug like a Human: A Large Language Model Debugger via Verifying Runtime Execution Step-by-step Li Zhong, Zilong Wang, Jingbo Shang : https://t.co/40qY1751cQ #ArtificialIntelligence #DeepLearning #MachineLe
…[truncated 1658 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 256 · 2026-05-26T10:27:35.612556+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Software Fault Localization Using DStar\" IEEE conference 2012 proceedings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Software Fault Localization Using DStar\" IEEE conference 2012 proceedings"
  }
}
```

</details>

---

### Tool result

_source line 257 · 2026-05-26T10:27:35.612776+00:00_

Now I have all the information needed to compile the verification report. Here are my findings:

---

```
[jimenez2024swebench] Jimenez(2024) "SWE-bench: Can Language Models..."
  Exists: ✓  Authors: ✓  Year: ✓  Title: ✗  Venue: ✓  arXiv: N/A
  Citation context: [related_work.tex:20] ✓ — correctly cites the SWE-bench benchmark ecosystem
  Issues:
    - Title mismatch: bib has "Real-World GitHub Issues" (capital W, "GitHub"),
      but the official ICLR proceedings title is "Real-world Github Issues"
      (lowercase w, "Github"). arXiv abstract uses "Real-World GitHub Issues"
      but the published/camera-ready version at proceedings.iclr.cc uses
      "Real-world Github Issues". Recommend matching the proceedings version.
```

```
[jones2002visualization] Jones(2002) "Visualization of Test Information..."
  Exists: ✓  Authors: ✓  Year: ✓  Title: ✓  Venue: ✓  arXiv: N/A
  Citation context: [related_work.tex:19] ✓ — correctly cited alongside other SBFL works (Abreu, Wong) for spectrum-based fault localization
  Issues: None. All metadata verified correct. DOI 10.1145/581339.581397 confirmed.
```

```
[kadavath2022language] Kadavath(2022) "Language Models (Mostly) Know..."
  Exists: ✓  Authors: ✓  Year: ✓  Title: ✓  Venue: ✓  arXiv: ✓
  Citation context: [related_work.tex:48] ✓ — correctly cited for LLM self-calibration/self-knowledge
  Issues: None. arXiv ID 2207.05221 confirmed. Note: this paper was never
    formally published at a peer-reviewed venue; "arXiv preprint" is the
    correct venue designation.
```

```
[kamei2013large] Kamei(2013) "A Large-Scale Empirical Study..."
  Exists: ✓  Authors: ✓  Year: ✓  Title: ✓  Venue: ✓  arXiv: N/A
  Citation context: [related_work.tex:50] ✓ — correctly cited as foundational JIT defect prediction work
  Issues: None. IEEE TSE vol. 39 no. 6 pp. 757-773, DOI 10.1109/TSE.2012.70
    all confirmed correct.
```

```
[kang2024autofl] Kang(2024) "A Quantitative and Qualitative..."
  Exists: ✓  Authors: ✓  Year: ✓  Title: ✓  Ven
…[truncated 4345 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "Agent",
  "elapsed_ms": 32
}
```

</details>

---

### Tool result

_source line 258 · 2026-05-26T10:27:35.612950+00:00_

Web search results for query: ""Software Fault Localization Using DStar" IEEE conference 2012 proceedings"

Links: [{"title":"Software Fault Localization Using DStar (D*) | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/6258291"},{"title":"The DStar Method for Effective Software Fault Localization | IEEE Journals & Magazine | IEEE Xplore","url":"https://ieeexplore.ieee.org/abstract/document/6651713/"},{"title":"Figure 3 from Software Fault Localization Using DStar (D*) | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Software-Fault-Localization-Using-DStar-(D*)-Wong-Debroy/dbfbaae06b0bad70792127044566e3a981516a34/figure/4"},{"title":"The DStar Method for Effective Software Fault Localization | Semantic Scholar","url":"https://www.semanticscholar.org/paper/The-DStar-Method-for-Effective-Software-Fault-Wong-Debroy/db47f26a6b8cfc59f9c0fd135034ee25fbef554b"},{"title":"[PDF] Software Fault Localization Using DStar (D*) | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Software-Fault-Localization-Using-DStar-(D*)-Wong-Debroy/dbfbaae06b0bad70792127044566e3a981516a34"},{"title":"Software Fault Localization Using DStar (D*)","url":"https://personal.utdallas.edu/~ewong/SE6367/01-Project/08-SFL-papers/06-DStar.pdf"},{"title":"Spectrum‐Based Techniques for Software Fault Localization - Handbook of Software Fault Localization - Wiley Online Library","url":"https://onlinelibrary.wiley.com/doi/10.1002/9781119880929.ch4"},{"title":"Software Fault Localization through Aggregation-Based Neural Ranking for Static and Dynamic Features Selection - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC8587821/"}]

Based on the web search results, I found the paper you're looking for:

**Paper Details:**

The paper "Software Fault Localization Using DStar (D*)" by Wong, W.E., Debroy, V., Li, Y., and Gao, R. was published in the Proceedings of the 2012 IEEE Sixth International Conference on Software Security and Reliabil
…[truncated 705 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 259 · 2026-05-26T10:27:35.613109+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"The DStar method for effective software fault localization\" Wong IEEE Transactions Reliability 2014 journal volume pages"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"The DStar method for effective software fault localization\" Wong IEEE Transactions Reliability 2014 journal volume pages"
  }
}
```

</details>

---

### Tool result

_source line 260 · 2026-05-26T10:27:35.613365+00:00_

Here is my complete verification report for all 12 references:

---

```
[qwen2025coder] Qwen Team (2024) "Qwen2.5-Coder Technical Report..."
  Exists: ✓  Authors: ✓*  Year: ✓  Title: ✓  Venue: ✓  arXiv: ✓
  Citation context: [introduction.tex:14, method.tex:32] ✓ — correctly cited as model family used in experiments
  Issues:
    * The bib uses "author={Qwen Team}" which is acceptable shorthand, but the actual paper
      lists individual authors (Binyuan Hui, Jian Yang, Zeyu Cui, et al.). Either form is
      fine for citation; some venues prefer the full list.
    * The bib key "qwen2025coder" suggests 2025, but year={2024} in the entry is correct
      (arXiv submitted Sep 2024). Minor inconsistency in the key name only — not a real error.
```

```
[roziere2024code] Rozière et al. (2023) "Code Llama: Open Foundation..."
  Exists: ✓  Authors: ✗  Year: ✓  Title: ✓  Venue: ✓  arXiv: ✓
  Citation context: [introduction.tex:14, method.tex:32] ✓ — correctly cited as CodeLlama-13B-Instruct model family
  Issues:
    * AUTHOR ERROR: The bib entry lists "Rémi Lacroix" as an author, but the actual paper
      has "Romain Sauvestre" in that position. "Rémi Lacroix" does not appear in the author
      list of arXiv:2308.12950. Must be corrected.
    * The bib key says "roziere2024code" but year={2023}. The key year is cosmetic only, not
      a real error; year=2023 is correct (submitted Aug 2023).
```

```
[sachdeva2024dataefficient] Sachdeva et al. (2024) "How to Train Data-Efficient..."
  Exists: ✓  Authors: ✓  Year: ✓  Title: ✓  Venue: ✓  arXiv: ✓
  Citation context: [related_work.tex:51] ✓ — correctly cited for data selection methods
    improving convergence
  Issues: None. All metadata matches. The paper is an arXiv preprint (also on OpenReview),
    and the bib correctly lists it as "arXiv preprint."
```

```
[shi2023distracted] Shi et al. (2023) "Large Language Models Can Be..."
  Exists: ✓  Authors: ✓  Year: ✓  Title: ✓  Venue: ✓  arXiv: N/A
  Citation context: [r
…[truncated 5320 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "Agent",
  "elapsed_ms": 27
}
```

</details>

---

### Tool result

_source line 261 · 2026-05-26T10:27:35.613548+00:00_

Web search results for query: ""The DStar method for effective software fault localization" Wong IEEE Transactions Reliability 2014 journal volume pages"

Links: [{"title":"The DStar Method for Effective Software Fault Localization | Request PDF","url":"https://www.researchgate.net/publication/260524645_The_DStar_Method_for_Effective_Software_Fault_Localization"},{"title":"The DStar Method for Effective Software Fault Localization | IEEE Journals & Magazine | IEEE Xplore","url":"https://ieeexplore.ieee.org/abstract/document/6651713/"},{"title":"The DStar Method for Effective Software Fault Localization | Semantic Scholar","url":"https://www.semanticscholar.org/paper/The-DStar-Method-for-Effective-Software-Fault-Wong-Debroy/db47f26a6b8cfc59f9c0fd135034ee25fbef554b"},{"title":"[PDF] Software Fault Localization Using DStar (D*) | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Software-Fault-Localization-Using-DStar-(D*)-Wong-Debroy/dbfbaae06b0bad70792127044566e3a981516a34"},{"title":"Spectrum‐Based Techniques for Software Fault Localization - Handbook of Software Fault Localization - Wiley Online Library","url":"https://onlinelibrary.wiley.com/doi/10.1002/9781119880929.ch4"},{"title":"Software Fault Localization for Programs with Multiple Bugs - Handbook of Software Fault Localization - Wiley Online Library","url":"https://onlinelibrary.wiley.com/doi/10.1002/9781119880929.ch12"},{"title":"Software Fault Localization Using DStar (D*)","url":"https://personal.utdallas.edu/~ewong/SE6367/01-Project/08-SFL-papers/06-DStar.pdf"},{"title":"Figure 3 from Software Fault Localization Using DStar (D*) | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Software-Fault-Localization-Using-DStar-(D*)-Wong-Debroy/dbfbaae06b0bad70792127044566e3a981516a34/figure/4"},{"title":"Inforence: effective fault localization based on information-theoretic analysis and statistical causal inference | Frontiers of Computer Science | Springer Nature Link","url":"https://l
…[truncated 722 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 262 · 2026-05-26T10:27:35.613712+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "widyasari \"FuseFL\" SANER 2024 title \"with LLM\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "tool_args": {
    "query": "widyasari \"FuseFL\" SANER 2024 title \"with LLM\""
  }
}
```

</details>

---

### Tool result

_source line 263 · 2026-05-26T10:27:35.613847+00:00_

Web search results for query: "widyasari "FuseFL" SANER 2024 title "with LLM""

Links: [{"title":"Identifying Root Causes of Null Pointer Exceptions with Logical Inferences","url":"https://arxiv.org/html/2412.01005"},{"title":"Advancing Software Development with Generative AI: Hands-On with LLM Agents (SANER 2024 - Workshops and Tutorials Track ) - SANER 2024","url":"https://conf.researchr.org/details/saner-2024/saner-2024-workshops-and-tutorials-track-/26/Advancing-Software-Development-with-Generative-AI-Hands-On-with-LLM-Agents"},{"title":"SANER 2024 - Workshops and Tutorials Track - SANER 2024","url":"https://conf.researchr.org/track/saner-2024/saner-2024-workshops-and-tutorials-track-"},{"title":"Ratnadira Widyasari - Singapore Management University | LinkedIn","url":"https://www.linkedin.com/in/ratnadira-widyasari/"},{"title":"Navigating Confidentiality in Test Automation: A Case Study in LLM Driven Test Data Generation (SANER 2024 - Industrial Track) - SANER 2024","url":"https://conf.researchr.org/details/saner-2024/saner-2024-industrial-track/101/Navigating-Confidentiality-in-Test-Automation-A-Case-Study-in-LLM-Driven-Test-Data-G"},{"title":"Is This You, LLM? Recognizing AI-written Programs with Multilingual Code Stylometry (SANER 2025 - Research Papers) - SANER 2025","url":"https://conf.researchr.org/details/saner-2025/saner-2025-papers/36/Is-This-You-LLM-Recognizing-AI-written-Programs-with-Multilingual-Code-Stylometry"},{"title":"News","url":"https://soarsmu.github.io/allnews.html"},{"title":"Ratnadira Widyasari","url":"https://ratnadiraw.github.io/"}]

Based on the search results, I found references to FuseFL, a paper by Widyasari et al. (2024) related to fault localization with LLM. The search results show that Ratnadira Widyasari authored "Demystifying Faulty Code: Step-by-Step Reasoning for Explainable Fault Localization" published at SANER (the 31st IEEE International Conference on Software Analysis, Evolution, and Reengineering).

However, the search
…[truncated 569 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 264 · 2026-05-26T10:27:35.613999+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Widyasari \"Demystifying Faulty Code\" arXiv title exact \"with LLM\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Widyasari \"Demystifying Faulty Code\" arXiv title exact \"with LLM\""
  }
}
```

</details>

---

### Tool result

_source line 265 · 2026-05-26T10:27:35.614129+00:00_

Web search results for query: "Widyasari "Demystifying Faulty Code" arXiv title exact "with LLM""

Links: [{"title":"[2403.10507] Demystifying Faulty Code with LLM: Step-by-Step Reasoning for Explainable Fault Localization","url":"https://arxiv.org/abs/2403.10507"},{"title":"Demystifying Faulty Code with LLM: Step-by-Step Reasoning for Explainable Fault Localization","url":"https://arxiv.org/html/2403.10507v1"},{"title":"Demystifying Faulty Code with LLM: Step-by-Step","url":"https://arxiv.org/pdf/2403.10507"},{"title":"Demystifying Faulty Code with LLM: Step-by-Step Reasoning for Explainable Fault Localization - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240310507W/abstract"},{"title":"Demystifying Faulty Code with LLM: Explainable Fault Localization","url":"https://goatstack.ai/topics/demystifying-faulty-code-with-llm-explainable-fault-localization-vgshdv"},{"title":"GitHub - iSEngLab/AwesomeLLM4SE: [SCIS 2025] A Survey on Large Language Models for Software Engineering · GitHub","url":"https://github.com/iSEngLab/AwesomeLLM4SE"}]

I found the paper you were looking for! "Demystifying Faulty Code with LLM: Step-by-Step Reasoning for Explainable Fault Localization" is by Ratnadira Widyasari and 4 other authors, published on arXiv on March 15, 2024 (arXiv ID: 2403.10507).

The study investigates step-by-step reasoning for explainable fault localization and explores the potential of Large Language Models in assisting developers in reasoning about code. The researchers proposed FuseFL, which utilizes spectrum-based fault localization results along with other information to improve fault localization.

You can access the paper at: https://arxiv.org/abs/2403.10507


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 266 · 2026-05-26T10:27:35.614300+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Leveraging Large Language Model for Automatic Patch Correctness Assessment\" IEEE TSE volume 50 number 11 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Leveraging Large Language Model for Automatic Patch Correctness Assessment\" IEEE TSE volume 50 number 11 2024"
  }
}
```

</details>

---

### Tool result

_source line 267 · 2026-05-26T10:27:35.614442+00:00_

Web search results for query: ""Leveraging Large Language Model for Automatic Patch Correctness Assessment" IEEE TSE volume 50 number 11 2024"

Links: [{"title":"Leveraging Large Language Model for Automatic Patch Correctness Assessment | IEEE Transactions on Software Engineering","url":"https://dl.acm.org/doi/10.1109/TSE.2024.3452252"},{"title":"Leveraging Large Language Model for Automatic Patch Correctness Assessment. | BibSonomy","url":"https://www.bibsonomy.org/bibtex/121733ba2498fa6c09e6b5ba222ae64ff"},{"title":"Leveraging Large Language Model for Automatic Patch Correctness Assessment | IEEE Journals & Magazine | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/10659742/"},{"title":"Leveraging Large Language Model for Automatic Patch Correctness Assessment : Find an Expert : The University of Melbourne","url":"https://findanexpert.unimelb.edu.au/scholarlywork/1930021-leveraging-large-language-model-for-automatic-patch-correctness-assessment?cache=1737797463612"},{"title":"GitHub - iSEngLab/AwesomeLLM4APR: [TOSEM 2026]A Systematic Literature Review on Large Language Models for Automated Program Repair · GitHub","url":"https://github.com/iSEngLab/AwesomeLLM4APR"},{"title":"Invalidator: Automated Patch Correctness Assessment Via Semantic and Syntactic Reasoning | IEEE Transactions on Software Engineering","url":"https://dl.acm.org/doi/abs/10.1109/TSE.2023.3255177"},{"title":"Leveraging Large Language Model for Automatic Patch Correctness Assessment | Request PDF","url":"https://www.researchgate.net/publication/383591189_Leveraging_Large_Language_Model_for_Automatic_Patch_Correctness_Assessment"},{"title":"GitHub - iSEngLab/AwesomeLLM4SE: [SCIS 2025] A Survey on Large Language Models for Software Engineering · GitHub","url":"https://github.com/iSEngLab/AwesomeLLM4SE"},{"title":"Leveraging Large Language Model for Automatic Patch Correctness Assessment - Peeref","url":"https://www.peeref.com/works/84586982/comments"}]

I found the paper you're looking for.
…[truncated 1227 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 268 · 2026-05-26T10:27:35.614681+00:00_

Now I have all the information needed. Here is my comprehensive verification report:

---

```
[wang2025openhands] Wang et al.(2025) "OpenHands: An Open Platform for..."
  Exists: ✓  Authors: ✓  Year: ✓  Title: ✓  Venue: ✓  arXiv: ✓
  Citation context: [related_work.tex:20] ✓ — OpenHands does incorporate execution feedback; appropriate citation in repair workflows context.
  Issues: None.
```

```
[widyasari2024fusefl] Widyasari et al.(2024) "Demystifying Faulty Code: Step-by-Step..."
  Exists: ✓  Authors: ✓  Year: ✓  Title: ✗  Venue: ✓  arXiv: N/A
  Citation context: [related_work.tex:18] ✓ — FuseFL is the system proposed in this paper; context about structured fault signals improving localization is accurate.
  Issues:
    - TITLE MISMATCH: The bib entry has "Demystifying Faulty Code: Step-by-Step Reasoning for Explainable Fault Localization" but the actual title is "Demystifying Faulty Code **with LLM**: Step-by-Step Reasoning for Explainable Fault Localization". The phrase "with LLM" is missing from the title. The arXiv version (2403.10507) and the IEEE published version on IEEE Xplore both include "with LLM" in the title.
```

```
[wong2014dstar] Wong et al.(2014) "Software Fault Localization Using DStar..."
  Exists: ✓  Authors: ✓  Year: ✓/⚠  Title: ✓/⚠  Venue: ✗  arXiv: N/A
  Citation context: [related_work.tex:19] ✓ — DStar is a core SBFL technique; appropriate citation alongside other SBFL methods.
  Issues:
    - VENUE MISMATCH: The bib entry lists "Journal of Systems and Software" but the DStar paper was published in two forms:
      (1) Conference: "Software Fault Localization Using DStar (D*)" at IEEE SERE 2012.
      (2) Journal: "The DStar Method for Effective Software Fault Localization" in IEEE Transactions on Reliability, Vol. 63(1), pp. 290-308, 2014.
      Neither venue is "Journal of Systems and Software". The 2014 journal version is in IEEE Transactions on Reliability, not JSS.
    - TITLE: If citing the 2014 journal version, the title should b
…[truncated 5683 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-w2_20260526T101532",
  "tool": "Agent",
  "elapsed_ms": 24
}
```

</details>

---

### Assistant

_source line 269 · 2026-05-26T10:27:35.614985+00:00_

全部 5 组验证完成。汇总报告如下：

---

## 引用验证报告（Worker 2/3）

### 逐条验证结果

```
[abreu2007accuracy] Abreu(2007) "On the Accuracy of Spectrum-based..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: N/A
  引用位置: [related_work.tex:19] ✓ — SBFL 基础工作
  问题: 格式小问题：应用 booktitle= 而非 journal=（这是会议论文）

[appt2024] Zhang(2024) "APPT: Boosting Automated Patch Correctness..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: N/A
  引用位置: [related_work.tex:17] ✓ — 79.7% 准确率与论文报告一致
  问题: 无

[austin2021program] Austin(2021) "Program Synthesis with Large Language..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: ✓
  引用位置: [introduction.tex:14] ✓ [method.tex:13] ✓ — MBPP 来源正确
  问题: 无

[barr2015oracle] Barr(2015) "The Oracle Problem in Software Testing..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: N/A
  引用位置: [related_work.tex:15] ✓ — 正确引用 test oracle 综述
  问题: 无

[bengio2009curriculum] Bengio(2009) "Curriculum Learning"
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: N/A
  引用位置: [related_work.tex:51] ✓
  问题: 无

[bouzenia2025repairagent] Bouzenia(2025) "RepairAgent: An Autonomous, LLM-Based..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: N/A
  引用位置: [related_work.tex:20] ✓
  问题: 无

[chen2021evaluating] Chen(2021) "Evaluating Large Language Models Trained..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: ✓
  引用位置: [introduction.tex:14] ✓ [method.tex:13] ✓ — HumanEval 来源正确
  问题: 无

[chen2024selfdebug] Chen(2024) "Teaching Large Language Models to Self-Debug"
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: N/A
  引用位置: [related_work.tex:21] ✓
  问题: 无

[chen2025tracepile] Chen(2025) "Chain of Execution Supervision Promotes..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: ✓
  引用位置: [introduction.tex:4] ✓ [related_work.tex:5] ✓ [method.tex:7] ✓
  问题: 无

[deepseek2024coder] Guo(2024) "DeepSeek-Coder: When the Large Language..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: ✓
  引用位置: [introduction.tex:14] ✓ [method.tex:32] ✓
  问题: 无

[ding2024traced] Ding(2024) "TRACED: Execution-aware Pre-training..."
  存在: ✓  作者: ✗  年份: ✓  标题: ✓  Venue: ✓  arXiv: ✓
  引用位置: [introduction.tex:4] ✓ [related_work.tex:16] ✓
  问题: 作者 "Ben Steenhoek" 在 ACM 官方记录中为 "Benjamin Steenhoek"

[eguchi2025etcot] Eguchi(2025) "Making LLMs Program Interpreters via..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: N/A
  引用位置: [related_work.tex:7] ✓
  问题: 无

[ferrando2025execute] Armengol-Estapé(2025) "What I Cannot Execute, I..."
  存在: ✓  作者: ✗  年份: ✓  标题: ✓  Venue: ✓  arXiv: ✓
  引用位置: [related_work.tex:7] ✓
  问题: ⚠ bib key 含 "ferrando" 但无此姓作者（第一作者是 Armengol-Estapé）；
        作者名缺 accent："Estape" 应为 "Estap{\'e}"

[foster2025mutation] Foster(2025) "Mutation-Guided LLM-based Test Generation..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: ✓
  引用位置: [related_work.tex:18] ✓
  问题: 无（venue 可补 "33rd" 但非错误）

[geng2024calibration] Geng(2024) "A Survey of Confidence Estimation..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: ✓
  引用位置: [related_work.tex:48] ✓
  问题: 无

[gu2024cruxeval] Gu(2024) "CRUXEval: A Benchmark for Code..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: ✓
  引用位置: [related_work.tex:8] ✓ [method.tex:7] ✓
  问题: 无

[guo2017calibration] Guo(2017) "On Calibration of Modern Neural..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: N/A
  引用位置: [related_work.tex:48] ✓
  问题: 无

[haque2025traces] Haque(2025) "Towards Effectively Leveraging Execution..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✗  arXiv: ✓
  引用位置: [related_work.tex:10] ✓
  问题: ⚠ Venue 错误：应为 "KnowledgeNLP Workshop at NAACL 2025"，非 "ACL 2025"

[hoang2019deepjit] Hoang(2019) "DeepJIT: An End-to-End Deep Learning..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: N/A
  引用位置: [related_work.tex:50] ✓
  问题: 无

[hoang2020cc2vec] Hoang(2020) "CC2Vec: Distributed Representations of..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: N/A
  引用位置: [related_work.tex:17] ✓
  问题: 无

[hu2022lora] Hu(2022) "LoRA: Low-Rank Adaptation of Large..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: ✓
  引用位置: [method.tex:33] ✓ [appendix.tex:38] ✓
  问题: 无

[huang2026tracecoder] Huang(2026) "TraceCoder: A Trace-Driven Multi-Agent..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: ✓
  引用位置: [related_work.tex:10] ✓
  问题: 无

[jiang2023llmlingua] Jiang(2023) "LLMLingua: Compressing Prompts for..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: ✓
  引用位置: [related_work.tex:10] ✓ [discussion.tex:66] ✓
  问题: 无

[jimenez2024swebench] Jimenez(2024) "SWE-bench: Can Language Models..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: N/A
  引用位置: [related_work.tex:20] ✓
  问题: 标题大小写微小差异（"Real-World GitHub" vs proceedings 版 "Real-world Github"），非重大问题

[jones2002visualization] Jones(2002) "Visualization of Test Information..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: N/A
  引用位置: [related_work.tex:19] ✓
  问题: 无

[kadavath2022language] Kadavath(2022) "Language Models (Mostly) Know..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: ✓
  引用位置: [related_work.tex:48] ✓
  问题: 无

[kamei2013large] Kamei(2013) "A Large-Scale Empirical Study..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: N/A
  引用位置: [related_work.tex:50] ✓
  问题: 无

[kang2024autofl] Kang(2024) "A Quantitative and Qualitative Evaluation..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: ✓
  引用位置: [related_work.tex:19] ✓
  问题: 无

[li2023selectivecontext] Li(2023) "Compressing Context to Enhance..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: N/A
  引用位置: [related_work.tex:10] ✓ [discussion.tex:66] ✓
  问题: 无

[liu2023codeexecution] Liu(2023) "Code Execution with Pre-trained..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: N/A
  引用位置: [related_work.tex:5] ✓
  问题: 无

[ni2024next] Ni(2024) "NExT: Teaching Large Language Models..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: ✓
  引用位置: [introduction.tex:4] ✓ [related_work.tex:7] ✓
  问题: 无

[papadakis2019mutation] Papadakis(2019) "Mutation Testing Advances: An..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: N/A
  引用位置: [related_work.tex:18] ✓
  问题: 无

[pornprasit2021jitline] Pornprasit(2021) "JITLine: A Simpler, Better..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: N/A
  引用位置: [related_work.tex:50] ✓
  问题: 无

[qin2024agentfl] Qin(2024) "AgentFL: Scaling LLM-based Fault..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✗  arXiv: ✓
  引用位置: [related_work.tex:19] ✓
  问题: ⚠ Venue 未确认为 ASE 2024——DBLP/ACM DL 搜不到该论文在 ASE 2024 的记录，可能仅为 arXiv 预印本

[qwen2025coder] Qwen Team(2024) "Qwen2.5-Coder Technical Report..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: ✓
  引用位置: [introduction.tex:14] ✓ [method.tex:32] ✓
  问题: bib key "qwen2025coder" 与 year={2024} 不一致（cosmetic）

[roziere2024code] Rozière(2023) "Code Llama: Open Foundation Models..."
  存在: ✓  作者: ✗  年份: ✓  标题: ✓  Venue: ✓  arXiv: ✓
  引用位置: [introduction.tex:14] ✓ [method.tex:32] ✓
  问题: ⚠ 作者列表中 "Rémi Lacroix" 可能不在该论文作者中（需二次确认，26 位作者的长列表）

[sachdeva2024dataefficient] Sachdeva(2024) "How to Train Data-Efficient..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: ✓
  引用位置: [related_work.tex:51] ✓
  问题: 无

[shi2023distracted] Shi(2023) "Large Language Models Can Be Easily..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: N/A
  引用位置: [related_work.tex:9] ✓
  问题: 无

[shinn2023reflexion] Shinn(2023) "Reflexion: Language Agents with..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: N/A
  引用位置: [related_work.tex:21] ✓
  问题: 无

[spiess2025calibration] Spiess(2025) "Calibration and Correctness of..."
  存在: ✓  作者: ✗  年份: ✓  标题: ✓  Venue: ✓  arXiv: ✓
  引用位置: [related_work.tex:48] ✓ [appendix.tex:546] ✓
  问题: "and others" 不是标准 BibTeX 用法；应列出全部 9 位作者

[steenhoek2024deepdfa] Steenhoek(2024) "Dataflow Analysis-Inspired Deep..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: N/A
  引用位置: [related_work.tex:16] ✓
  问题: 无

[swayamdipta2020cartography] Swayamdipta(2020) "Dataset Cartography: Mapping and..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: N/A
  引用位置: [related_work.tex:51] ✓
  问题: 无

[tian2020patchcorrectness] Tian(2020) "Evaluating Representation Learning of..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: N/A
  引用位置: [related_work.tex:17] ✓
  问题: 无

[tian2024debugbench] Tian(2024) "DebugBench: Evaluating Debugging..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: ✓
  引用位置: [experiments.tex:126] ✓ [appendix.tex:616] ✓
  问题: 无

[wang2025dcsh] Wang(2025) "Do Code Semantics Help? A..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: ✓
  引用位置: [introduction.tex:4,12] ✓ [related_work.tex:6] ✓
  问题: 无

[wang2025inspectcoder] Wang(2025) "InspectCoder: Dynamic Analysis-Enabled..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: ✓
  引用位置: [related_work.tex:10] ✓
  问题: 无

[wang2025openhands] Wang(2025) "OpenHands: An Open Platform for..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: ✓
  引用位置: [related_work.tex:20] ✓
  问题: 无

[widyasari2024fusefl] Widyasari(2024) "Demystifying Faulty Code: Step-by-Step..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✗  Venue: ✓  arXiv: N/A
  引用位置: [related_work.tex:18] ✓
  问题: ⚠ 标题缺 "with LLM"——应为 "Demystifying Faulty Code with LLM: Step-by-Step Reasoning for Explainable Fault Localization"

[wong2014dstar] Wong(2014) "Software Fault Localization Using DStar..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✗  Venue: ✗  arXiv: N/A
  引用位置: [related_work.tex:19] ✓
  问题: ✗✗ 严重错误——
    (1) Venue 错：bib 写 "Journal of Systems and Software"，实际 2014 期刊版发表在 IEEE Transactions on Reliability (Vol.63, No.1, pp.290-308)
    (2) 标题错：2014 期刊版标题为 "The DStar Method for Effective Software Fault Localization"
    (3) Volume/pages 错：bib 写 vol.91 pp.44-58，应为 vol.63 pp.290-308
    (4) DOI 错：10.1016/j.jss.2013.12.020 指向无关论文，正确 DOI 为 10.1109/TR.2013.2285319

[xia2024agentless] Xia(2024) "Agentless: Demystifying LLM-based..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: ✓
  引用位置: [related_work.tex:20] ✓
  问题: 已正式发表于 FSE 2025，建议更新 venue（当前 arXiv 标注不算错）

[xie2023doremi] Xie(2023) "DoReMi: Optimizing Data Mixtures..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: ✓
  引用位置: [related_work.tex:51] ✓
  问题: 无

[xu2025cruxevalx] Xu(2025) "CRUXEval-X: A Benchmark for Multilingual..."
  存在: ✓  作者: ✗  年份: ✓  标题: ✓  Venue: ✓  arXiv: ✓
  引用位置: [related_work.tex:8] ✓
  问题: "and others" 应展开为完整作者列表（共 9 位作者）

[yadavally2024slicing] Yadavally(2024) "A Learning-Based Approach to Static..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: N/A
  引用位置: [related_work.tex:16] ✓
  问题: 无

[yang2024generalization] Yang(2024) "Unveiling the Generalization Power..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: ✓
  引用位置: [related_work.tex:52] ✓ [appendix.tex:655] ✓
  问题: 无

[yang2024sweagent] Yang(2024) "SWE-agent: Agent-Computer Interfaces..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: ✓
  引用位置: [related_work.tex:20] ✓
  问题: 无

[zhong2024ldb] Zhong(2024) "LDB: A Large Language Model Debugger..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✗  Venue: ✓  arXiv: N/A
  引用位置: [related_work.tex:21] ✓
  问题: ⚠ 正式发表版标题为 "Debug like a Human: A Large Language Model Debugger via Verifying Runtime Execution Step by Step"，bib 中用了旧标题 "LDB: ..."

[zhou2024llm4patch] Zhou(2024) "Leveraging Large Language Model for..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: N/A
  引用位置: [related_work.tex:17] ✓
  问题: 无
```

---

### 汇总

**总计：57 条**
**幻觉引用（HALLUCINATED）：0 条** — 全部论文真实存在
**错误引用（MISATTRIBUTION）：0 条** — 所有引用上下文使用正确

**问题数：10 条**

| 严重程度 | Key | 问题类型 | 说明 |
|---------|-----|---------|------|
| **严重** | `wong2014dstar` | Venue/标题/DOI/页码全错 | venue 应为 IEEE Trans. Reliability，标题/vol/pages/DOI 均不对 |
| **中** | `haque2025traces` | Venue 错误 | "ACL 2025" 应为 "NAACL 2025" |
| **中** | `qin2024agentfl` | Venue 未确认 | 未在 ASE 2024 proceedings 中找到，可能仅为 arXiv 预印本 |
| **中** | `widyasari2024fusefl` | 标题不完整 | 缺 "with LLM" |
| **中** | `zhong2024ldb` | 标题过时 | 正式版标题以 "Debug like a Human:" 开头 |
| **低** | `ferrando2025execute` | bib key 不匹配 + 作者缺 accent | key 含 "ferrando" 但无此姓作者；"Estape" 缺 accent |
| **低** | `ding2024traced` | 作者名 | "Ben" 应为 "Benjamin" Steenhoek |
| **低** | `spiess2025calibration` | 作者不完整 | "and others" 非标准 BibTeX，应列全部 9 人 |
| **低** | `xu2025cruxevalx` | 作者不完整 | "and others" 应展开为全部 9 位作者 |
| **低** | `roziere2024code` | 作者存疑 | "Rémi Lacroix" 可能不在 Code Llama 作者列表中（需二次确认） |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_audit_citation-verify-w2_20260526T101532"
}
```

</details>

---
