# code 14b paper text update

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 31
- **Recorded user turns:** 0
- **Tool calls:** 15
- **Original source:** `logs/chats/worker_code_14b-paper-text-update_20260523T080501.jsonl`
- **Structured JSON:** [`77784cfdb39aeeed45cc.json`](../../sessions/77/77784cfdb39aeeed45cc.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

31 recorded events

### Tool call

_source line 1 · 2026-05-23T08:06:37.671836+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_14b-paper-text-update_20260523T080501",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/abstract.tex"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-23T08:06:37.672479+00:00_

1	\begin{abstract}
2	LLM-based program repair increasingly leverages test-time compute scaling, generating multiple candidate patches and selecting the best via a verifier. Execution-based verification is reliable but expensive; three execution-free alternatives have emerged: per-test binary classification (\cls{}), execution output generation (\cwm{}), and trajectory-level patch scoring (\traj{}). No prior work compares these formulations under matched conditions.
3	
4	We present the first systematic comparison across two representative code LLM families (Qwen3, DeepSeek-Coder), two complexity levels, and multiple seeds under ${\leq}$8B LoRA fine-tuning. At function level, \cls{} and \cwm{} are statistically equivalent across both families (TOST, 5 seeds): classification is not inherently easier than generation when outputs are short. \traj{} parity is model-dependent and not confirmed after multiple comparison correction. At repository level, a significant interaction ($z{=}-23.7$, DeepSeek-Coder) confirms this equivalence collapses: the \cls{}--\cwm{} gap widens to 18--26\pp{} across 2--3 seeds per model under our ${\leq}$8B LoRA protocol in variant-level evaluation, driven by format collapse in generation-based simulation. Gap magnitude depends on multiple confounds. At 14B (3 seeds), the function-level gap narrows to 0.43\pp{} (TOST $p{=}$[TOST\_P]), consistent with capacity-dependent convergence.
5	
6	Error complementarity and a failure mode taxonomy motivate future work on complexity-aware formulation routing, though simple heuristics capture $<$0.4\pp{} of oracle advantage.
7	\end{abstract}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_14b-paper-text-update_20260523T080501",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-23T08:06:37.672704+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_14b-paper-text-update_20260523T080501",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-23T08:06:37.672999+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We systematically compare \cls{}, \cwm{}, and \traj{} across two representative code LLM families, two complexity levels, and multiple seeds to characterize the formulation landscape for neural code verification.
5	
6	\subsection{Experimental Setup}
7	\label{sec:setup}
8	
9	\paragraph{Datasets.}
10	\emph{Function-level}: mutated variants from HumanEval~\cite{chen2021humaneval} and MBPP~\cite{austin2021mbpp} (five mutation types), labels verified by execution. 19,076 samples (train 15,290 / val 1,896 / test 1,890; pass:fail $\approx$ 52:48, majority baseline 51.75\%).
11	\emph{Repo-level}: per-test instances from SWE-bench Verified~\cite{chowdhury2024swebenchverified} mutants. ${\sim}$70K training samples; val ($n{=}9{,}335$) and test ($n{=}9{,}784$) have zero problem overlap (majority baseline 72.96\%). Val-based checkpoint selection follows standard practice~\cite{jimenez2024swebench} where validation loss is computable; runs using truncate preprocessing produce NaN validation loss because repo-level execution traces often exceed the 2,048-token sequence length limit; after truncation, many samples have all target tokens removed (labels entirely $-$100), producing degenerate loss---a formulation-inherent weakness that classification and trajectory formulations avoid by design. NaN loss defaults to the final epoch checkpoint (affects DeepSeek \cls{} s123, all \cwm{} runs, and Qwen3 \traj{} runs; see Appendix~\ref{app:hyperparams}).
12	
13	\paragraph{Models and training.}
14	We fine-tune Qwen3-4B and Qwen3-8B~\cite{qwen2025qwen3} with Low-Rank Adaptation (LoRA)~\cite{hu2022lora} (rank 16, 3 epochs) across five seeds. Seeds 42/123/456 use bfloat16; seeds 789/0 use NormalFloat 4-bit (NF4) quantization~\cite{dettmers2024qlora} to test robustness to precision reduction (function-level accuracy remains within seed noise across both precisions; see footnote in \S\ref{sec:equivalence}). As a cross-model consistency chec
…[truncated 19296 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_14b-paper-text-update_20260523T080501",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-23T08:06:37.673343+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_14b-paper-text-update_20260523T080501",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-23T08:06:37.673531+00:00_

1	\documentclass[11pt]{article}
2	
3	% ACL style (review mode for anonymous ARR submission)
4	\usepackage[review]{acl}
5	
6	% Fonts — Times Roman (required by ACL/ARR template)
7	\usepackage{times}
8	
9	% Math
10	\usepackage{amsmath}
11	\usepackage{amssymb}
12	
13	% Tables
14	\usepackage{booktabs}
15	\usepackage{multirow}
16	\usepackage{tabularx}
17	
18	% Graphics
19	\usepackage{graphicx}
20	\usepackage{xcolor}
21	\graphicspath{{../../artifacts/}}
22	
23	% Lists
24	\usepackage{enumitem}
25	
26	% Custom commands
27	\newcommand{\cls}{\textsc{Cls}}
28	\newcommand{\cwm}{\textsc{Cwm}}
29	\newcommand{\traj}{\textsc{Traj}}
30	\newcommand{\fone}{F\textsubscript{1}}
31	\newcommand{\pp}{\,\text{pp}}
32	\newcommand{\tbd}{\textsc{tbd}}
33	\newcommand{\placeholder}[1]{{\color{red}\texttt{[#1]}}}
34	
35	\title{A Systematic Comparison of Execution-Free Verification Formulations for Code Repair}
36	\author{Anonymous}
37	
38	\begin{document}
39	\maketitle
40	
41	\input{abstract}
42	
43	\input{introduction}
44	
45	\begin{figure*}[t]
46	\centering
47	\includegraphics[width=\textwidth]{figures/paper/fig1_reformulation.pdf}
48	\caption{Three verification formulations. \textbf{Left:} \cls{} predicts binary pass/fail per test (1 output token). \textbf{Center:} \cwm{} generates execution output, derives verdict by exact match ($O(L)$ tokens). \textbf{Right:} Trajectory-level scoring predicts patch-level resolved/unresolved (1 token, no per-test signal). Each formulation makes different tradeoffs between output complexity, diagnostic granularity, and inference cost.}
49	\label{fig:reformulation}
50	\end{figure*}
51	
52	\input{method}
53	
54	\input{experiments}
55	
56	\begin{figure}[t]
57	\centering
58	\includegraphics[width=\columnwidth]{figures/paper/figure2_v2.pdf}
59	\caption{Function-level accuracy scaling (4B--14B). CLS and CWM accuracy with shaded gap region. The \cls{}--\cwm{} gap follows an inverted-U trajectory: 1.32\pp{} at 4B, widening to 2.62\pp{} at 8B, then narrowing to 0.43\p
…[truncated 304 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_14b-paper-text-update_20260523T080501",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-23T08:06:37.673688+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_14b-paper-text-update_20260523T080501",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-23T08:06:37.673860+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We presented the first systematic comparison of three execution-free verification formulations (\cls{}, \cwm{}, \traj{}). At function level, \cls{} and \cwm{} are statistically equivalent (TOST $p{=}0.007$, 5 seeds); \traj{} equivalence is not confirmed after multiple comparison correction. Per-test classification achieves 217$\times$ higher throughput while providing diagnostic signal. Complementary errors (oracle: 90.63\%/95.83\%; single-seed) motivate complexity-aware routing. At repository level under ${\leq}$8B LoRA, divergence reaches 18--26\pp{} ($z{=}-23.7$, 2--3 seeds per model), with \cwm{} falling below majority baseline---consistent across families but dependent on multiple confounds (\S\ref{sec:threats}). Three failure modes (format collapse, decision collapse, aggregation penalty) are consistent across families. \cls{} is recommended primarily for its throughput advantage and diagnostic capability; the accuracy advantage over \traj{} is directional but underpowered ($n{=}48$, MDE${\approx}$25\pp{}; Appendix~\ref{app:power}). Primary statistical findings are established under ${\leq}$8B LoRA fine-tuning. 14B results (3 seeds) corroborate function-level convergence (gap 0.43\pp{}, TOST $p{=}$[TOST\_P]), consistent with capacity-dependent scaling; whether this extends to repo level remains open.
5	
6	Three directions follow: (1)~oracle gains motivate complexity-aware routing using the failure mode taxonomy as routing features; (2)~the semantic generation bottleneck (four interventions fail; Appendix~\ref{app:extended_analysis}(g)) suggests capacity scaling or execution trace pretraining~\cite{meta2025cwm} is needed---testing at 32B+ would resolve the primary open question; (3)~larger-scale evaluation of per-test diagnostics for downstream repair ($n{=}44$ in our pilot) would test whether \cls{}'s throughput advantage extends to repair pipelines.
7	
8	\section*{Limitations}
9	
10	Primary findings use ${\
…[truncated 560 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_14b-paper-text-update_20260523T080501",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-23T08:06:37.674078+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/abstract.tex",
  "old_string": "(TOST $p{=}$[TOST\\_P])",
  "new_string": "(TOST $p{=}0.0006$)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_14b-paper-text-update_20260523T080501",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/abstract.tex",
    "old_string": "(TOST $p{=}$[TOST\\_P])",
    "new_string": "(TOST $p{=}0.0006$)"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-23T08:06:37.674233+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/abstract.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_14b-paper-text-update_20260523T080501",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-23T08:06:37.674363+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex",
  "old_string": "\\textbf{89.93 $\\pm$ 0.80}",
  "new_string": "\\textbf{89.93 $\\pm$ 0.81}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_14b-paper-text-update_20260523T080501",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex",
    "old_string": "\\textbf{89.93 $\\pm$ 0.80}",
    "new_string": "\\textbf{89.93 $\\pm$ 0.81}"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-23T08:06:37.674551+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_14b-paper-text-update_20260523T080501",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-23T08:06:37.674679+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex",
  "old_string": "\\underline{89.50 $\\pm$ 0.67}",
  "new_string": "\\underline{89.50 $\\pm$ 0.65}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_14b-paper-text-update_20260523T080501",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex",
    "old_string": "\\underline{89.50 $\\pm$ 0.67}",
    "new_string": "\\underline{89.50 $\\pm$ 0.65}"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-23T08:06:37.674914+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_14b-paper-text-update_20260523T080501",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-23T08:06:37.675060+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex",
  "old_string": "89.93$\\pm$0.80\\% while \\cwm{} reaches 89.50$\\pm$0.67\\%, closing the gap from 2.62\\pp{} at 8B to 0.43\\pp{} (TOST $p{=}$[TOST\\_P])",
  "new_string": "89.93$\\pm$0.81\\% while \\cwm{} reaches 89.50$\\pm$0.65\\%, closing the gap from 2.62\\pp{} at 8B to 0.43\\pp{} (TOST $p{=}0.0006$)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_14b-paper-text-update_20260523T080501",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex",
    "old_string": "89.93$\\pm$0.80\\% while \\cwm{} reaches 89.50$\\pm$0.67\\%, closing the gap from 2.62\\pp{} at 8B to 0.43\\pp{} (TOST $p{=}$[TOST\\_P])",
    "new_string": "89.93$\\pm$0.81\\% while \\cwm{} reaches 89.50$\\pm$0.65\\%, closing the gap from 2.62\\pp{} at 8B to 0.43\\pp{} (TOST $p{=}0.0006$)"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-23T08:06:37.675266+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_14b-paper-text-update_20260523T080501",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-23T08:06:37.675437+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/conclusion.tex",
  "old_string": "TOST $p{=}$[TOST\\_P]",
  "new_string": "TOST $p{=}0.0006$"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_14b-paper-text-update_20260523T080501",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/conclusion.tex",
    "old_string": "TOST $p{=}$[TOST\\_P]",
    "new_string": "TOST $p{=}0.0006$"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-23T08:06:37.675592+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/conclusion.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_14b-paper-text-update_20260523T080501",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-23T08:06:37.675729+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "TOST_P|TOST\\\\\\_P",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_14b-paper-text-update_20260523T080501",
  "tool": "Grep",
  "tool_args": {
    "pattern": "TOST_P|TOST\\\\\\_P",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-23T08:06:37.675904+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_14b-paper-text-update_20260523T080501",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-23T08:06:37.676065+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\[GAP\\]|\\[TOST",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_14b-paper-text-update_20260523T080501",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\[GAP\\]|\\[TOST",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-23T08:06:37.676196+00:00_

docs/paper/main.aux:636:\@writefile{lof}{\contentsline {figure}{\numberline {2}{\ignorespaces Function-level accuracy scaling (4B--14B). CLS and CWM accuracy with shaded gap region. The \textsc  {Cls}{}--\textsc  {Cwm}{} gap follows an inverted-U trajectory: 1.32\,\text  {pp}{} at 4B, widening to 2.62\,\text  {pp}{} at 8B, then converging to near-zero ({\color  {red}[GAP]\,\text  {pp}{}}) at 14B (3 seeds).}}{7}{figure.caption.29}\protected@file@percent }
docs/paper/main.aux:637:\newlabel{fig:scaling_gap}{{2}{7}{Function-level accuracy scaling (4B--14B). CLS and CWM accuracy with shaded gap region. The \cls {}--\cwm {} gap follows an inverted-U trajectory: 1.32\pp {} at 4B, widening to 2.62\pp {} at 8B, then converging to near-zero ({\color {red}[GAP]\pp {}}) at 14B (3 seeds)}{figure.caption.29}{}}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_14b-paper-text-update_20260523T080501",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-23T08:06:37.676351+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "single.seed|exploratory",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper",
  "glob": "*.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_14b-paper-text-update_20260523T080501",
  "tool": "Grep",
  "tool_args": {
    "pattern": "single.seed|exploratory",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper",
    "glob": "*.tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-23T08:06:37.676480+00:00_

docs/paper/experiments.tex:117:Table~\ref{tab:repo_level} compares formulations at repository-level complexity. Variant-level comparisons ($n{=}48$) are exploratory due to limited seed coverage; the per-test interaction effect is statistically confirmed (see below). Checkpoints are val-selected where validation loss is computable (\S\ref{sec:setup}); the test set has zero problem overlap with validation.
docs/paper/experiments.tex:189:\paragraph{Error complementarity.} \cls{} and \cwm{} exhibit partially complementary errors. An oracle combination achieves 90.63\% (+2.80\pp{}; 95\% CI [89.3\%, 91.9\%]; single-seed) at function level and 95.83\% (+14.58\pp{}; $n{=}48$) at repo level. Simple routing heuristics capture $<$0.4\pp{} of the oracle gap; the complementarity is instance-specific, suggesting a learned router is needed (Appendix~\ref{app:oracle}).
docs/paper/conclusion.tex:4:[Omitted long matching line]
docs/paper/appendix.tex:364:[Omitted long matching line]
docs/paper/appendix.tex:560:[Omitted long matching line]
docs/paper/introduction.tex:15:\item \textbf{Error complementarity.} \cls{} and \cwm{} exhibit partially complementary error patterns at function level (oracle: 90.63\%, 95\% CI [89.3\%, 91.9\%]; single-seed); at repo level, oracle routing reaches 95.83\% variant accuracy (+14.58\pp{}; single-seed), the strongest practical argument for exploring formulation-level tradeoffs (\S\ref{sec:analysis}).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_14b-paper-text-update_20260523T080501",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-23T08:06:37.676654+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "single.seed|exploratory",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/appendix.tex",
  "output_mode": "content",
  "-n": "True",
  "context": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_14b-paper-text-update_20260523T080501",
  "tool": "Grep",
  "tool_args": {
    "pattern": "single.seed|exploratory",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/appendix.tex",
    "output_mode": "content",
    "-n": "True",
    "context": "1"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-23T08:06:37.676781+00:00_

363-\paragraph{(a) Error complementarity.}
364:[Omitted long matching line]
365-
--
559-\label{app:limitations}
560:[Omitted long matching line]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_14b-paper-text-update_20260523T080501",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-23T08:06:37.676976+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/appendix.tex",
  "offset": "363",
  "limit": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_14b-paper-text-update_20260523T080501",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/appendix.tex",
    "offset": "363",
    "limit": "3"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-23T08:06:37.677115+00:00_

363	\paragraph{(a) Error complementarity.}
364	\cls{} and \cwm{} are both FP-dominant at function level but at different rates, producing partial complementarity. Among \cls{} errors (seed 42), 56.5\% are false positives (PASS $\to$ FAIL); among \cwm{} errors, 70.3\% are false positives. Both formulations over-predict failure, but \cwm{}'s stronger FP bias means it incorrectly rejects passing tests that \cls{} correctly accepts. An oracle combination achieves 90.63\% accuracy (1713/1890 correct, 177 both-wrong; +2.80\pp{} over the best single formulation, \cls{} 87.83\%; single-seed estimate, seed 42). The complementarity arises from different \emph{degrees} of fail-bias rather than opposite error directions: \cwm{}'s generation bottleneck produces aggressive failure predictions, while \cls{}'s single-token output is more calibrated. Ensemble approaches exploiting this degree difference are a natural direction.
365	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_14b-paper-text-update_20260523T080501",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-23T08:06:37.677243+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/appendix.tex",
  "offset": "559",
  "limit": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_14b-paper-text-update_20260523T080501",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/appendix.tex",
    "offset": "559",
    "limit": "3"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-23T08:06:37.677377+00:00_

559	\label{app:limitations}
560	The same-size 4B comparison uses a single seed; \cls{} 4B seed 123 (val-best ckpt-800) achieves only 75.33\% test accuracy (+2.4\pp{} above majority baseline); val-best selection at an early checkpoint (step 800) amplifies the val-test distribution shift observed across all configurations. The \cwm{} 8B comparison uses 3 seeds per model. The validation and test sets have zero problem overlap but differ in mutation type composition (Table~\ref{tab:mutation_distribution}): \texttt{operator\_swap} shifts from 19.1\% (val) to 34.3\% (test), the largest single-type distribution mismatch (+15.2\pp{}). All repo-level results use val-selected checkpoints, and checkpoint selection variance could contribute to observed differences. Our training data is synthetically constructed from mutation operators rather than real developer patches. While mutation testing literature establishes that mutants are reasonable proxies for real faults in test effectiveness studies~\cite{andrews2005mutation,just2014mutants}, these findings concern mutation \emph{adequacy} (whether tests that kill mutants also detect real faults), not whether verifiers trained on mutants transfer to real patches. However, the coupling effect underlying these results supports \emph{relative ranking} validity: a domain shift from synthetic mutations to real bugs may affect absolute accuracy levels, but our core finding---that formulation choice matters at repo level but not function level---concerns relative performance ordering, which is expected to be preserved under distributional shifts that affect all formulations equally. The synthetic-to-real transfer gap for absolute accuracy remains untested. The \traj{} training configuration differs from \cls{}/\cwm{}: smaller training set (${\sim}$400 vs.\ ${\sim}$70K instances), different learning rate ($2{\times}10^{-4}$ vs.\ $5{\times}10^{-5}$), and variant-level evaluation ($n{=}48$ vs.\ per-test $n{=}9{,}784$). The function-level TOS
…[truncated 701 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_14b-paper-text-update_20260523T080501",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-23T08:06:37.677562+00:00_

Both appendix references are about oracle analysis (single-seed estimate) and 4B comparisons (single seed) — not about 14B. No changes needed there.

All edits are complete. Summary of changes:

- **abstract.tex**: `[TOST_P]` → `0.0006`
- **experiments.tex Table 2**: CLS 14B std `0.80` → `0.81`, CWM 14B std `0.67` → `0.65`
- **experiments.tex text (line 97)**: Same std updates + `[TOST_P]` → `0.0006`
- **conclusion.tex**: `[TOST_P]` → `0.0006`

The other items in the checklist (seed descriptions, footnote removal, figure caption, limitations wording) were already updated in prior commits — no stale 14B single-seed/exploratory language remains in any `.tex` source file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_code_14b-paper-text-update_20260523T080501"
}
```

</details>

---
