# paper patch ablation significance

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 25
- **Recorded user turns:** 0
- **Tool calls:** 12
- **Original source:** `logs/chats/worker_paper_patch_ablation_significance_20260516T043905.jsonl`
- **Structured JSON:** [`ec8b8b9ff1c265cefabd.json`](../../sessions/ec/ec8b8b9ff1c265cefabd.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

25 recorded events

### Tool call

_source line 1 · 2026-05-16T04:44:29.344320+00:00_

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
  "session": "worker_paper_patch_ablation_significance_20260516T043905",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-16T04:44:29.344830+00:00_

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
…[truncated 10378 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_patch_ablation_significance_20260516T043905",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-16T04:44:29.345045+00:00_

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
  "session": "worker_paper_patch_ablation_significance_20260516T043905",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/appendix.tex"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-16T04:44:29.345414+00:00_

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
…[truncated 25116 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_patch_ablation_significance_20260516T043905",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-16T04:44:29.345615+00:00_

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
  "session": "worker_paper_patch_ablation_significance_20260516T043905",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-16T04:44:29.345780+00:00_

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
  "session": "worker_paper_patch_ablation_significance_20260516T043905",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-16T04:44:29.346195+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/experiments.tex",
  "old_string": "\tAll four conditions fall within a 5pp range (77.2\\%--81.8\\%) with broadly overlapping CIs and a non-monotonic trend (Appendix~\\ref{sec:trace_length_full}), confirming that trace content quality---not quantity---is the bottleneck.\n\tEven with unlimited tokens, the model cannot extract the diagnostic signal that VOTA's targeted compression provides, reinforcing the information density interpretation (\\S\\ref{sec:density}).",
  "new_string": "\tAccuracy spans a narrow 5pp range (77.2\\%--81.8\\%) but the trend is non-monotonic: increasing from 512 to 1024 tokens \\emph{decreases} accuracy by 3.19pp ($p{=}0.002$, paired bootstrap), and 1024 tokens is not significantly better than no trace at all ($p{=}0.078$).\n\tOnly the no-limit condition (81.76\\%) significantly exceeds 1024 tokens ($p{<}0.001$), yet remains 18pp below VOTA (Figure~\\ref{fig:trace_length}, Appendix~\\ref{sec:trace_length_full}), confirming that trace content quality---not quantity---is the bottleneck and reinforcing the information density interpretation (\\S\\ref{sec:density})."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_patch_ablation_significance_20260516T043905",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/experiments.tex",
    "old_string": "\tAll four conditions fall within a 5pp range (77.2\\%--81.8\\%) with broadly overlapping CIs and a non-monotonic trend (Appendix~\\ref{sec:trace_length_full}), confirming that trace content quality---not quantity---is the bottleneck.\n\tEven with unlimited tokens, the model cannot extract the diagnostic signal that VOTA's targeted compression provides, reinforcing the information density interpretation (\\S\\ref{sec:density}).",
    "new_string": "\tAccuracy spans a narrow 5pp range (77.2\\%--81.8\\%) but the trend is non-monotonic: increasing from 512 to 1024 tokens \\emph{decreases} accuracy by 3.19pp ($p{=}0.002$, paired bootstrap), and 1024 tokens is not significantly better than no trace at all ($p{=}0.078$).\n\tOnly the no-limit condition (81.76\\%) significantly exceeds 1024 tokens ($p{<}0.001$), yet remains 18pp below VOTA (Figure~\\ref{fig:trace_length}, Appendix~\\ref{sec:trace_length_full}), confirming that trace content quality---not quantity---is the bottleneck and reinforcing the information density interpretation (\\S\\ref{sec:density})."
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-16T04:44:29.346404+00:00_

&lt;tool_use_error>String to replace not found in file.
String: 	All four conditions fall within a 5pp range (77.2\%--81.8\%) with broadly overlapping CIs and a non-monotonic trend (Appendix~\ref{sec:trace_length_full}), confirming that trace content quality---not quantity---is the bottleneck.
	Even with unlimited tokens, the model cannot extract the diagnostic signal that VOTA's targeted compression provides, reinforcing the information density interpretation (\S\ref{sec:density}).&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_patch_ablation_significance_20260516T043905",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-16T04:44:29.346550+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/experiments.tex",
  "offset": "127",
  "limit": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_patch_ablation_significance_20260516T043905",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/experiments.tex",
    "offset": "127",
    "limit": "5"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-16T04:44:29.346679+00:00_

127	
128	To test whether the \texttt{full\_trace} performance gap is driven by input truncation, we vary the maximum trace token budget (256, 512, 1024, no limit) on Qwen-2.5-7B (seed=42).
129	All four conditions fall within a 5pp range (77.2\%--81.8\%) with broadly overlapping CIs and a non-monotonic trend (Appendix~\ref{sec:trace_length_full}), confirming that trace content quality---not quantity---is the bottleneck.
130	Even with unlimited tokens, the model cannot extract the diagnostic signal that VOTA's targeted compression provides, reinforcing the information density interpretation (\S\ref{sec:density}).
131	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_patch_ablation_significance_20260516T043905",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-16T04:44:29.346805+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/experiments.tex",
  "old_string": "All four conditions fall within a 5pp range (77.2\\%--81.8\\%) with broadly overlapping CIs and a non-monotonic trend (Appendix~\\ref{sec:trace_length_full}), confirming that trace content quality---not quantity---is the bottleneck.\nEven with unlimited tokens, the model cannot extract the diagnostic signal that VOTA's targeted compression provides, reinforcing the information density interpretation (\\S\\ref{sec:density}).",
  "new_string": "Accuracy spans a narrow 5pp range (77.2\\%--81.8\\%) but the trend is non-monotonic: increasing from 512 to 1024 tokens \\emph{decreases} accuracy by 3.19pp ($p{=}0.002$, paired bootstrap), and 1024 tokens is not significantly better than no trace at all ($p{=}0.078$).\nOnly the no-limit condition (81.76\\%) significantly exceeds 1024 tokens ($p{<}0.001$), yet remains 18pp below VOTA (Figure~\\ref{fig:trace_length}, Appendix~\\ref{sec:trace_length_full}), confirming that trace content quality---not quantity---is the bottleneck and reinforcing the information density interpretation (\\S\\ref{sec:density})."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_patch_ablation_significance_20260516T043905",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/experiments.tex",
    "old_string": "All four conditions fall within a 5pp range (77.2\\%--81.8\\%) with broadly overlapping CIs and a non-monotonic trend (Appendix~\\ref{sec:trace_length_full}), confirming that trace content quality---not quantity---is the bottleneck.\nEven with unlimited tokens, the model cannot extract the diagnostic signal that VOTA's targeted compression provides, reinforcing the information density interpretation (\\S\\ref{sec:density}).",
    "new_string": "Accuracy spans a narrow 5pp range (77.2\\%--81.8\\%) but the trend is non-monotonic: increasing from 512 to 1024 tokens \\emph{decreases} accuracy by 3.19pp ($p{=}0.002$, paired bootstrap), and 1024 tokens is not significantly better than no trace at all ($p{=}0.078$).\nOnly the no-limit condition (81.76\\%) significantly exceeds 1024 tokens ($p{<}0.001$), yet remains 18pp below VOTA (Figure~\\ref{fig:trace_length}, Appendix~\\ref{sec:trace_length_full}), confirming that trace content quality---not quantity---is the bottleneck and reinforcing the information density interpretation (\\S\\ref{sec:density})."
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-16T04:44:29.346989+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/experiments.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_patch_ablation_significance_20260516T043905",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-16T04:44:29.347130+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/appendix.tex",
  "old_string": "\\caption{Trace length ablation on Qwen-2.5-7B ($N{=}1{,}190$, seed=42). All four conditions fall within a 5pp range (77.2\\%--81.8\\%) with broadly overlapping confidence intervals, indicating no significant effect of trace length on full-trace accuracy.}",
  "new_string": "\\caption{Trace length ablation on Qwen-2.5-7B ($N{=}1{,}190$, seed=42). Per-condition bootstrap 95\\% CIs ($B{=}10{,}000$). All four conditions fall within a 5pp range (77.2\\%--81.8\\%), but pairwise bootstrap tests reveal significant differences between specific pairs (Table~\\ref{tab:trace_length_pairwise}).}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_patch_ablation_significance_20260516T043905",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/appendix.tex",
    "old_string": "\\caption{Trace length ablation on Qwen-2.5-7B ($N{=}1{,}190$, seed=42). All four conditions fall within a 5pp range (77.2\\%--81.8\\%) with broadly overlapping confidence intervals, indicating no significant effect of trace length on full-trace accuracy.}",
    "new_string": "\\caption{Trace length ablation on Qwen-2.5-7B ($N{=}1{,}190$, seed=42). Per-condition bootstrap 95\\% CIs ($B{=}10{,}000$). All four conditions fall within a 5pp range (77.2\\%--81.8\\%), but pairwise bootstrap tests reveal significant differences between specific pairs (Table~\\ref{tab:trace_length_pairwise}).}"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-16T04:44:29.347358+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/appendix.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_patch_ablation_significance_20260516T043905",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-16T04:44:29.347510+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/appendix.tex",
  "old_string": "As shown in Table~\\ref{tab:trace_length} and Figure~\\ref{fig:trace_length}, all four trace length conditions fall within a 5pp range (77.2\\%--81.8\\%) with broadly overlapping confidence intervals.\nThe trend is non-monotonic (1024 tokens yields the lowest accuracy at 77.23\\%), and no condition approaches the VOTA (99.41\\%) or \\texttt{exception\\_only} (99.83\\%) baselines.\nThis suggests that input truncation alone does not explain the full-trace performance gap: even with unlimited trace tokens, the model cannot extract the diagnostic signal that VOTA's targeted compression provides.\nThe result reinforces the information density interpretation (\\S\\ref{sec:density}): the gap between full traces and VOTA is driven by the \\emph{content} of the trace (irrelevant lines diluting the diagnostic signal), not its \\emph{length}.\nIn contrast, VOTA's compressed representation concentrates the diagnostic signal into fewer tokens, making it sensitive to truncation when those tokens are removed (\\S\\ref{sec:cross_model}).",
  "new_string": "As shown in Table~\\ref{tab:trace_length} and Figure~\\ref{fig:trace_length}, all four trace length conditions fall within a 5pp range (77.2\\%--81.8\\%).\nTo quantify the reliability of the observed differences, Table~\\ref{tab:trace_length_pairwise} reports paired bootstrap comparisons ($B{=}10{,}000$, seed=42) across all condition pairs.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llccc}\n\\toprule\n& \\textbf{Comparison} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} & \\textbf{$p$-value} \\\\\n\\midrule\n\\multirow{4}{*}{\\rotatebox{90}{\\scriptsize Budget}}\n& 512 vs.\\ 256           & $+$1.60  & [$-$0.34, $+$3.53]   & 0.117 \\\\\n& 1024 vs.\\ 512          & $-$3.19  & [$-$5.29, $-$1.09]   & 0.002** \\\\\n& no\\_limit vs.\\ 1024    & $+$4.54  & [$+$2.52, $+$6.55]   & ${<}$0.001*** \\\\\n& no\\_limit vs.\\ 256     & $+$2.94  & [$+$0.84, $+$5.04]   & 0.006** \\\\\n\\midrule\n\\multirow{4}{*}{\\rotatebox{90}{\\scriptsize vs.\\ no\\_trace}}\n& 256 $-$ no\\_trace       & $+$3.70  & [$+$1.43, $+$6.05]   & 0.002** \\\\\n& 512 $-$ no\\_trace       & $+$5.29  & [$+$3.03, $+$7.56]   & ${<}$0.001*** \\\\\n& 1024 $-$ no\\_trace      & $+$2.10  & [$-$0.17, $+$4.37]   & 0.078 \\\\\n& no\\_limit $-$ no\\_trace & $+$6.64  & [$+$4.37, $+$8.99]   & ${<}$0.001*** \\\\\n\\midrule\n\\multirow{4}{*}{\\rotatebox{90}{\\scriptsize vs.\\ exc.}}\n& 256 $-$ exc\\_only       & $-$21.01 & [$-$23.45, $-$18.74] & ${<}$0.001*** \\\\\n& 512 $-$ exc\\_only       & $-$19.41 & [$-$21.76, $-$17.14] & ${<}$0.001*** \\\\\n& 1024 $-$ exc\\_only      & $-$22.61 & [$-$25.04, $-$20.25] & ${<}$0.001*** \\\\\n& no\\_limit $-$ exc\\_only & $-$18.07 & [$-$20.34, $-$15.88] & ${<}$0.001*** \\\\\n\\bottomrule\n\\end{tabular}%\n}\n\\caption{Pairwise paired bootstrap comparisons for trace length ablation ($B{=}10{,}000$, seed=42). $\\Delta$ = accuracy difference between the two conditions (first $-$ second in the budget group; condition $-$ baseline in the other groups). **$p{<}0.01$; ***$p{<}0.001$.}\n\\label{tab:trace_length_pairwise}\n\\end{table}\n\n\\paragraph{Non-monotonic pattern.}\nThe trend across trace budgets is non-monotonic: 512 tokens (80.42\\%) slightly outperforms 256 tokens (78.82\\%), but doubling to 1024 tokens \\emph{decreases} accuracy to 77.23\\%---a statistically significant 3.19pp drop ($p{=}0.002$, 95\\% CI [$-$5.29, $-$1.09]).\nThe no-limit condition (81.76\\%) recovers and significantly exceeds 1024 tokens ($p{<}0.001$), but 1024 tokens is not significantly better than the \\texttt{no\\_trace} baseline (75.13\\%; $\\Delta{=}{+}2.10$pp, $p{=}0.078$, 95\\% CI [$-$0.17, $+$4.37]).\nThis means that truncating traces to an intermediate length can be \\emph{worse} than providing no trace at all---the 1024-token budget retains enough irrelevant content to mislead the model while discarding diagnostic events that might appear late in the trace.\n\n\\paragraph{Comparison to baselines.}\nAll four trace budget conditions significantly exceed \\texttt{no\\_trace} except 1024 tokens ($p{=}0.078$), confirming that raw trace content provides some signal but unreliably so.\nThe gap to \\texttt{exception\\_only} (99.83\\%) is massive for every budget condition (18--23pp, all $p{<}0.001$), underscoring that even unlimited raw traces cannot substitute for targeted signal extraction.\nThe best full-trace condition (no\\_limit, 81.76\\%) still lags \\texttt{exception\\_only} by 18.07pp (95\\% CI [$-$20.34, $-$15.88]).\n\n\\paragraph{Interpretation.}\nThese results rule out input truncation as the primary explanation for the full-trace performance gap: even with unlimited tokens, the model cannot extract the diagnostic signal that VOTA's targeted compression provides.\nThe non-monotonic dip at 1024 tokens is consistent with a ``worst-of-both-worlds'' regime where the model receives enough noisy context to dilute the signal but not enough to compensate through broader coverage.\nThe result reinforces the information density interpretation (\\S\\ref{sec:density}): the gap between full traces and VOTA is driven by the \\emph{content} of the trace (irrelevant lines diluting the diagnostic signal), not its \\emph{length}.\nIn contrast, VOTA's compressed representation concentrates the diagnostic signal into fewer tokens, making it sensitive to truncation when those tokens are removed (\\S\\ref{sec:cross_model})."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_patch_ablation_significance_20260516T043905",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/appendix.tex",
    "old_string": "As shown in Table~\\ref{tab:trace_length} and Figure~\\ref{fig:trace_length}, all four trace length conditions fall within a 5pp range (77.2\\%--81.8\\%) with broadly overlapping confidence intervals.\nThe trend is non-monotonic (1024 tokens yields the lowest accuracy at 77.23\\%), and no condition approaches the VOTA (99.41\\%) or \\texttt{exception\\_only} (99.83\\%) baselines.\nThis suggests that input truncation alone does not explain the full-trace performance gap: even with unlimited trace tokens, the model cannot extract the diagnostic signal that VOTA's targeted compression provides.\nThe result reinforces the information density interpretation (\\S\\ref{sec:density}): the gap between full traces and VOTA is driven by the \\emph{content} of the trace (irrelevant lines diluting the diagnostic signal), not its \\emph{length}.\nIn contrast, VOTA's compressed representation concentrates the diagnostic signal into fewer tokens, making it sensitive to truncation when those tokens are removed (\\S\\ref{sec:cross_model}).",
    "new_string": "As shown in Table~\\ref{tab:trace_length} and Figure~\\ref{fig:trace_length}, all four trace length conditions fall within a 5pp range (77.2\\%--81.8\\%).\nTo quantify the reliability of the observed differences, Table~\\ref{tab:trace_length_pairwise} reports paired bootstrap comparisons ($B{=}10{,}000$, seed=42) across all condition pairs.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llccc}\n\\toprule\n& \\textbf{Comparison} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} & \\textbf{$p$-value} \\\\\n\\midrule\n\\multirow{4}{*}{\\rotatebox{90}{\\scriptsize Budget}}\n& 512 vs.\\ 256           & $+$1.60  & [$-$0.34, $+$3.53]   & 0.117 \\\\\n& 1024 vs.\\ 512          & $-$3.19  & [$-$5.29, $-$1.09]   & 0.002** \\\\\n& no\\_limit vs.\\ 1024    & $+$4.54  & [$+$2.52, $+$6.55]   & ${<}$0.001*** \\\\\n& no\\_limit vs.\\ 256     & $+$2.94  & [$+$0.84, $+$5.04]   & 0.006** \\\\\n\\midrule\n\\multirow{4}{*}{\\rotatebox{90}{\\scriptsize vs.\\ no\\_trace}}\n& 256 $-$ no\\_trace       & $+$3.70  & [$+$1.43, $+$6.05]   & 0.002** \\\\\n& 512 $-$ no\\_trace       & $+$5.29  & [$+$3.03, $+$7.56]   & ${<}$0.001*** \\\\\n& 1024 $-$ no\\_trace      & $+$2.10  & [$-$0.17, $+$4.37]   & 0.078 \\\\\n& no\\_limit $-$ no\\_trace & $+$6.64  & [$+$4.37, $+$8.99]   & ${<}$0.001*** \\\\\n\\midrule\n\\multirow{4}{*}{\\rotatebox{90}{\\scriptsize vs.\\ exc.}}\n& 256 $-$ exc\\_only       & $-$21.01 & [$-$23.45, $-$18.74] & ${<}$0.001*** \\\\\n& 512 $-$ exc\\_only       & $-$19.41 & [$-$21.76, $-$17.14] & ${<}$0.001*** \\\\\n& 1024 $-$ exc\\_only      & $-$22.61 & [$-$25.04, $-$20.25] & ${<}$0.001*** \\\\\n& no\\_limit $-$ exc\\_only & $-$18.07 & [$-$20.34, $-$15.88] & ${<}$0.001*** \\\\\n\\bottomrule\n\\end{tabular}%\n}\n\\caption{Pairwise paired bootstrap comparisons for trace length ablation ($B{=}10{,}000$, seed=42). $\\Delta$ = accuracy difference between the two conditions (first $-$ second in the budget group; condition $-$ baseline in the other groups). **$p{<}0.01$; ***$p{<}0.001$.}\n\\label{tab:trace_length_pairwise}\n\\end{table}\n\n\\paragraph{Non-monotonic pattern.}\nThe trend across trace budgets is non-monotonic: 512 tokens (80.42\\%) slightly outperforms 256 tokens (78.82\\%), but doubling to 1024 tokens \\emph{decreases} accuracy to 77.23\\%---a statistically significant 3.19pp drop ($p{=}0.002$, 95\\% CI [$-$5.29, $-$1.09]).\nThe no-limit condition (81.76\\%) recovers and significantly exceeds 1024 tokens ($p{<}0.001$), but 1024 tokens is not significantly better than the \\texttt{no\\_trace} baseline (75.13\\%; $\\Delta{=}{+}2.10$pp, $p{=}0.078$, 95\\% CI [$-$0.17, $+$4.37]).\nThis means that truncating traces to an intermediate length can be \\emph{worse} than providing no trace at all---the 1024-token budget retains enough irrelevant content to mislead the model while discarding diagnostic events that might appear late in the trace.\n\n\\paragraph{Comparison to baselines.}\nAll four trace budget conditions significantly exceed \\texttt{no\\_trace} except 1024 tokens ($p{=}0.078$), confirming that raw trace content provides some signal but unreliably so.\nThe gap to \\texttt{exception\\_only} (99.83\\%) is massive for every budget condition (18--23pp, all $p{<}0.001$), underscoring that even unlimited raw traces cannot substitute for targeted signal extraction.\nThe best full-trace condition (no\\_limit, 81.76\\%) still lags \\texttt{exception\\_only} by 18.07pp (95\\% CI [$-$20.34, $-$15.88]).\n\n\\paragraph{Interpretation.}\nThese results rule out input truncation as the primary explanation for the full-trace performance gap: even with unlimited tokens, the model cannot extract the diagnostic signal that VOTA's targeted compression provides.\nThe non-monotonic dip at 1024 tokens is consistent with a ``worst-of-both-worlds'' regime where the model receives enough noisy context to dilute the signal but not enough to compensate through broader coverage.\nThe result reinforces the information density interpretation (\\S\\ref{sec:density}): the gap between full traces and VOTA is driven by the \\emph{content} of the trace (irrelevant lines diluting the diagnostic signal), not its \\emph{length}.\nIn contrast, VOTA's compressed representation concentrates the diagnostic signal into fewer tokens, making it sensitive to truncation when those tokens are removed (\\S\\ref{sec:cross_model})."
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-16T04:44:29.347797+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/appendix.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_patch_ablation_significance_20260516T043905",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-16T04:44:29.347944+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/experiments.tex",
  "offset": "125",
  "limit": "8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_patch_ablation_significance_20260516T043905",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/experiments.tex",
    "offset": "125",
    "limit": "8"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-16T04:44:29.348080+00:00_

125	\subsection{Trace Length Ablation}
126	\label{sec:trace_length}
127	
128	To test whether the \texttt{full\_trace} performance gap is driven by input truncation, we vary the maximum trace token budget (256, 512, 1024, no limit) on Qwen-2.5-7B (seed=42).
129	Accuracy spans a narrow 5pp range (77.2\%--81.8\%) but the trend is non-monotonic: increasing from 512 to 1024 tokens \emph{decreases} accuracy by 3.19pp ($p{=}0.002$, paired bootstrap), and 1024 tokens is not significantly better than no trace at all ($p{=}0.078$).
130	Only the no-limit condition (81.76\%) significantly exceeds 1024 tokens ($p{<}0.001$), yet remains 18pp below VOTA (Figure~\ref{fig:trace_length}, Appendix~\ref{sec:trace_length_full}), confirming that trace content quality---not quantity---is the bottleneck and reinforcing the information density interpretation (\S\ref{sec:density}).
131	
132	\subsection{Calibration Analysis}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_patch_ablation_significance_20260516T043905",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-16T04:44:29.348206+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/appendix.tex",
  "offset": "232",
  "limit": "75"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_patch_ablation_significance_20260516T043905",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/appendix.tex",
    "offset": "232",
    "limit": "75"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-16T04:44:29.348383+00:00_

232	\section{Trace Length Ablation}
233	\label{sec:trace_length_full}
234	
235	To test whether the \texttt{full\_trace} performance gap is caused by input truncation at training time, we vary the maximum trace token budget on Qwen-2.5-7B (seed=42) while keeping all other hyperparameters fixed.
236	
237	\begin{table}[t]
238	\centering
239	\small
240	\begin{tabular}{lcc}
241	\toprule
242	\textbf{Max Trace Tokens} & \textbf{Acc (\%)} & \textbf{95\% CI} \\
243	\midrule
244	256  & 78.82 & [76.4, 81.0] \\
245	512  & 80.42 & [78.2, 82.6] \\
246	1024 & 77.23 & [74.9, 79.6] \\
247	no\_limit ($\infty$) & 81.76 & [79.7, 83.9] \\
248	\bottomrule
249	\end{tabular}
250	\caption{Trace length ablation on Qwen-2.5-7B ($N{=}1{,}190$, seed=42). Per-condition bootstrap 95\% CIs ($B{=}10{,}000$). All four conditions fall within a 5pp range (77.2\%--81.8\%), but pairwise bootstrap tests reveal significant differences between specific pairs (Table~\ref{tab:trace_length_pairwise}).}
251	\label{tab:trace_length}
252	\end{table}
253	
254	\begin{figure}[t]
255	\centering
256	\includegraphics[width=\columnwidth]{fig4_trace_length}
257	\caption{Full-trace accuracy as a function of maximum trace token budget (Qwen-2.5-7B, $N{=}1{,}190$). Dashed lines show \texttt{exception\_only} (99.83\%), \texttt{no\_trace} (75.13\%), and majority-class (71.51\%) baselines. Accuracy remains in a narrow band regardless of trace length, confirming that trace content quality---not quantity---is the bottleneck.}
258	\label{fig:trace_length}
259	\end{figure}
260	
261	As shown in Table~\ref{tab:trace_length} and Figure~\ref{fig:trace_length}, all four trace length conditions fall within a 5pp range (77.2\%--81.8\%).
262	To quantify the reliability of the observed differences, Table~\ref{tab:trace_length_pairwise} reports paired bootstrap comparisons ($B{=}10{,}000$, seed=42) across all condition pairs.
263	
264	\begin{table}[t]
265	\centering
266	\small
267	\resizebox{\columnwidth}{!}{%
268	\begin{tabular}{llccc}
26
…[truncated 3096 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_patch_ablation_significance_20260516T043905",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-16T04:44:29.348526+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/appendix.tex",
  "offset": "306",
  "limit": "15"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_patch_ablation_significance_20260516T043905",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/appendix.tex",
    "offset": "306",
    "limit": "15"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-16T04:44:29.348658+00:00_

306	\paragraph{Interpretation.}
307	These results rule out input truncation as the primary explanation for the full-trace performance gap: even with unlimited tokens, the model cannot extract the diagnostic signal that VOTA's targeted compression provides.
308	The non-monotonic dip at 1024 tokens is consistent with a ``worst-of-both-worlds'' regime where the model receives enough noisy context to dilute the signal but not enough to compensate through broader coverage.
309	The result reinforces the information density interpretation (\S\ref{sec:density}): the gap between full traces and VOTA is driven by the \emph{content} of the trace (irrelevant lines diluting the diagnostic signal), not its \emph{length}.
310	In contrast, VOTA's compressed representation concentrates the diagnostic signal into fewer tokens, making it sensitive to truncation when those tokens are removed (\S\ref{sec:cross_model}).
311	
312	%% ============================================================
313	\section{Calibration Analysis}
314	\label{sec:calibration_full}
315	
316	Beyond accuracy, we evaluate whether trace conditions affect prediction calibration, motivated by recent findings that code LLM confidence is often poorly calibrated \citep{spiess2025calibration}.
317	
318	\begin{table}[t]
319	\centering
320	\small

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_patch_ablation_significance_20260516T043905",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-16T04:44:29.348798+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "multirow",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/main.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_patch_ablation_significance_20260516T043905",
  "tool": "Grep",
  "tool_args": {
    "pattern": "multirow",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/main.tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-16T04:44:29.348912+00:00_

9:\usepackage{multirow}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_patch_ablation_significance_20260516T043905",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-16T04:44:29.349067+00:00_

`multirow` is already loaded. Both edits are complete:

**experiments.tex §4.4** (line 129-130): Replaced the vague "broadly overlapping CIs" description with specific bootstrap results — the 512→1024 significant drop (p=0.002), the 1024 vs no_trace non-significance (p=0.078), and the no_limit vs 1024 significance (p<0.001). Added Figure cross-reference.

**appendix.tex trace_length_full** (lines 261-310): 
- Updated the per-condition table caption to reference bootstrap CIs and the new pairwise table
- Added a 12-row pairwise bootstrap comparison table (Table `trace_length_pairwise`) organized in three groups: adjacent budgets, vs no_trace, vs exception_only
- Replaced the old discussion with three structured paragraphs: non-monotonic pattern analysis (with the "worst-of-both-worlds" interpretation for the 1024 dip), baseline comparisons, and interpretation — all backed by specific p-values and CIs from the bootstrap results

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_patch_ablation_significance_20260516T043905"
}
```

</details>

---
