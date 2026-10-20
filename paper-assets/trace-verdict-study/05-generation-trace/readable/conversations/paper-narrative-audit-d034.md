# paper narrative audit d034

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 37
- **Recorded user turns:** 0
- **Tool calls:** 18
- **Original source:** `logs/chats/worker_paper_narrative_audit_d034_20260516T012026.jsonl`
- **Structured JSON:** [`0b93664246fffcb3ed81.json`](../../sessions/0b/0b93664246fffcb3ed81.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

37 recorded events

### Tool call

_source line 1 · 2026-05-16T01:21:58.678735+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_narrative_audit_d034_20260516T012026",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-16T01:21:58.679151+00:00_

artifacts/dream_reports/dream_20260515T013018/best/paper.tex
artifacts/dream_reports/dream_20260515T013018/median/paper.tex
artifacts/dream_reports/dream_20260515T013018/worst/paper.tex
artifacts/dream_reports/dream_20260515T084908/best/paper.tex
artifacts/dream_reports/dream_20260515T084908/median/paper.tex
artifacts/dream_reports/dream_20260515T084908/worst/paper.tex
artifacts/_project/paper/related_work.tex
artifacts/_project/paper/experiments.tex
artifacts/per_class_breakdown.tex
artifacts/_project/paper/section3_experimental_setup_d4f1e8.tex
artifacts/_project/paper/section3_experimental_setup.tex
docs/paper/related_work.tex
docs/paper/method.tex
docs/paper/introduction.tex
docs/paper/main.tex
docs/paper/conclusion.tex
artifacts/_project/paper/main_results_tables.tex
artifacts/paper_tables/main_results_tables.tex
docs/paper/experiments.tex
docs/paper/discussion.tex
docs/paper/appendix.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_narrative_audit_d034_20260516T012026",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-16T01:21:58.679364+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/paper/**",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_narrative_audit_d034_20260516T012026",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/paper/**",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-16T01:21:58.679512+00:00_

artifacts/_project/paper/related_work.tex
artifacts/_project/paper/paper_framing_draft_v2.md
figures/paper/fig1_trace_overview.pdf
figures/paper/fig1_trace_overview.png
figures/paper/fig3_cross_model_gap.pdf
figures/paper/fig3_cross_model_gap.png
figures/paper/gen_fig2_calibration.py
figures/paper/fig2_calibration.pdf
figures/paper/fig2_calibration.png
docs/paper/acl.sty
docs/paper/acl_natbib.bst
artifacts/_project/paper/experiments.tex
artifacts/_project/paper/main.pdf
artifacts/_project/paper/section3_experimental_setup_d4f1e8.tex
artifacts/_project/paper/section3_experimental_setup.tex
docs/paper/references.bib
docs/paper/related_work.tex
docs/paper/method.tex
docs/paper/main.blg
docs/paper/main.bbl
docs/paper/main.fls
docs/paper/main.fdb_latexmk
docs/paper/introduction.tex
docs/paper/main.tex
docs/paper/conclusion.tex
artifacts/_project/paper/main_results_tables.tex
docs/paper/main.aux
docs/paper/main.out
docs/paper/main.log
docs/paper/main.pdf
docs/paper/experiments.tex
docs/paper/discussion.tex
docs/paper/appendix.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_narrative_audit_d034_20260516T012026",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-16T01:21:58.679662+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "truncat|label corruption",
  "-i": "True",
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
  "session": "worker_paper_narrative_audit_d034_20260516T012026",
  "tool": "Grep",
  "tool_args": {
    "pattern": "truncat|label corruption",
    "-i": "True",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-16T01:21:58.679819+00:00_

docs/paper/experiments.tex:39:The VOTA training framework preserves the verdict label but truncates the trace content (input), so the model trains with incomplete diagnostic information for the vast majority of the dataset.
docs/paper/experiments.tex:40:The 14.96pp gap thus reflects both model capability differences and training-time trace truncation; the two factors cannot be disentangled in the current design.
docs/paper/experiments.tex:41:However, a post-hoc group analysis provides directional evidence: partitioning DeepSeek VOTA test samples by whether their training-set counterparts exceeded the context window, intact samples ($N{=}99$) achieve 100\% accuracy while truncated samples ($N{=}1{,}091$) achieve 83.04\% (95\% CI [80.75\%, 85.24\%]; Fisher exact $p{<}0.001$), with all 185 errors concentrated in the fail class of the truncated group (fail recall $=$ 31.23\%).
docs/paper/experiments.tex:42:In contrast, the \texttt{exception\_only} condition is unaffected by truncation because exception-based inputs are short enough to fit within the context window for both tokenizers, making its cross-model comparison clean.
docs/paper/experiments.tex:109:This two-factor decomposition is consistent across models: the VOTA cross-model gap (14.96pp, Table~\ref{tab:cross_model}) is confounded by training-time trace truncation on DeepSeek (\S\ref{sec:cross_model}), which amplifies information overload by removing diagnostic trace content from the majority of training samples.
docs/paper/main.tex:21:Our key finding is that exception events alone achieve near-perfect accuracy on Qwen (99.83\% $\pm$ 0.00, 3 seeds) and are the most effective component on DeepSeek (2/3 seeds at 99.33\%; 1 outlier at 91.09\% from LoRA initialization sensitivity), while a multi-component representation (VOTA) degrades by 14.96pp on the weaker model, confounded by training-time trace truncation.
docs/paper/conclusion.tex:9:In contrast, the full VOTA representation degrades by 14.96pp on DeepSeek---
…[truncated 2787 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_narrative_audit_d034_20260516T012026",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-16T01:21:58.679977+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "truncat|label corruption",
  "-i": "True",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/_project/paper",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_narrative_audit_d034_20260516T012026",
  "tool": "Grep",
  "tool_args": {
    "pattern": "truncat|label corruption",
    "-i": "True",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/_project/paper",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-16T01:21:58.680110+00:00_

artifacts/_project/paper/section3_experimental_setup.tex:32:For models with limited context, traces are tokenized and truncated to fit a 2{,}048-token window.
artifacts/_project/paper/section3_experimental_setup.tex:33:We apply chat-template-aware truncation that reserves token budget for the verdict label at the sequence end, preventing the label from being right-truncated during tokenization---a failure mode that causes complete training collapse (Appendix~\ref{app:truncation}).
artifacts/_project/paper/section3_experimental_setup.tex:94:\texttt{full\_trace} & $\mathbf{x} + t$, truncated to 2048 tokens \\
artifacts/_project/paper/section3_experimental_setup_d4f1e8.tex:32:For models with limited context, traces are tokenized and truncated to fit a 2{,}048-token window.
artifacts/_project/paper/section3_experimental_setup_d4f1e8.tex:33:We apply chat-template-aware truncation that reserves token budget for the verdict label at the sequence end, preventing the label from being right-truncated during tokenization---a failure mode that causes complete training collapse (Appendix~\ref{app:truncation}).
artifacts/_project/paper/section3_experimental_setup_d4f1e8.tex:94:\texttt{full\_trace} & $\mathbf{x} + t$, truncated to 2048 tokens \\
artifacts/_project/paper/experiments.tex:28:[Omitted long matching line]
artifacts/_project/paper/main_results_tables.tex:83:VOTA gap partly attributable to training-time trace content truncation
artifacts/_project/paper/main_results_tables.tex:84:(91.7\% of samples truncated to ${\sim}$2048 tokens; labels preserved).
artifacts/_project/paper/main_results_tables.tex:85:Full trace v3 uses label-preserving truncation (v1 collapsed due to label truncation).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_narrative_audit_d034_20260516T012026",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-16T01:21:58.680279+00:00_

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
  "session": "worker_paper_narrative_audit_d034_20260516T012026",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/appendix.tex"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-16T01:21:58.680499+00:00_

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
…[truncated 8700 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_narrative_audit_d034_20260516T012026",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-16T01:21:58.680666+00:00_

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
  "session": "worker_paper_narrative_audit_d034_20260516T012026",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/discussion.tex"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-16T01:21:58.680847+00:00_

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
…[truncated 7761 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_narrative_audit_d034_20260516T012026",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-16T01:21:58.681034+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "Table 10|tab:truncat|app:truncat|label truncat",
  "-i": "True",
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
  "session": "worker_paper_narrative_audit_d034_20260516T012026",
  "tool": "Grep",
  "tool_args": {
    "pattern": "Table 10|tab:truncat|app:truncat|label truncat",
    "-i": "True",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-16T01:21:58.681161+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_narrative_audit_d034_20260516T012026",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-16T01:21:58.681296+00:00_

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
  "session": "worker_paper_narrative_audit_d034_20260516T012026",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-16T01:21:58.681471+00:00_

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
  "session": "worker_paper_narrative_audit_d034_20260516T012026",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-16T01:21:58.681611+00:00_

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
  "session": "worker_paper_narrative_audit_d034_20260516T012026",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-16T01:21:58.681765+00:00_

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
  "session": "worker_paper_narrative_audit_d034_20260516T012026",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-16T01:21:58.681930+00:00_

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
  "session": "worker_paper_narrative_audit_d034_20260516T012026",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-16T01:21:58.682141+00:00_

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
…[truncated 10190 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_narrative_audit_d034_20260516T012026",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-16T01:21:58.682394+00:00_

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
  "session": "worker_paper_narrative_audit_d034_20260516T012026",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-16T01:21:58.682551+00:00_

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
13	The primary bottleneck is trace content selection, not loss design.
14	
15	\textbf{(3) Two-tier diagnostic hierarchy.}
16	Tier~1 signals (exception events, assertion points) individually achieve ${\geq}$99.8\% accuracy, while Tier~2 signals (loop compression) reach 85.6\%.
17	Combining tiers in VOTA slightly degrades performance (99.41\%), confirming that additional trace components introduce noise rather than complementary signal.
18	
19	These results yield a practical design principle: for verdict prediction, extract the highest-specificity diagnostic signal and discard everything else.
20	Future work should test whether exception dominance extends to other datasets (DebugBench, LiveCodeBench), model scales, and classification tasks beyond verdict prediction.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_narrative_audit_d034_20260516T012026",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-16T01:21:58.682687+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/_project/paper/main_results_tables.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_narrative_audit_d034_20260516T012026",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/_project/paper/main_results_tables.tex"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-16T01:21:58.682887+00:00_

1	% =============================================================================
2	% Paper Tables for trace-verdict-study
3	% EMNLP 2026 Main — ARR May 25
4	% Generated from experiment registry (2026-05-16)
5	% =============================================================================
6	
7	% Required packages (add to preamble):
8	% \usepackage{booktabs}
9	% \usepackage{multirow}
10	
11	
12	% =============================================================================
13	% TABLE 1: Qwen-2.5-Coder-7B Main Results
14	% =============================================================================
15	
16	\begin{table*}[t]
17	\centering
18	\small
19	\begin{tabular}{@{}llcccc@{}}
20	\toprule
21	& \textbf{Condition} & \textbf{Acc.\,(\%)} & \textbf{Pass\,$F_1$} & \textbf{Fail\,$F_1$} & \textbf{95\% CI} \\
22	\midrule
23	\multirow{2}{*}{\textit{Baselines}}
24	& Majority (pass)           & 71.51 & ---   & ---   & --- \\
25	& No trace                  & 75.13 & 81.3  & 62.7  & [72.8, 77.5] \\
26	\midrule
27	\multirow{2}{*}{\textit{Full trace}}
28	& Standard                  & 81.76 & 87.2  & 68.5  & [79.7, 83.9] \\
29	& Label-only loss            & 86.22 & 90.6  & 74.0  & [84.4, 88.1] \\
30	\midrule
31	\multirow{3}{*}{\textit{Components}}
32	& Loop only (Tier\,2)       & 85.63 & 89.7  & 76.5  & [83.5, 87.6] \\
33	& Exception only (Tier\,1)  & \textbf{99.83} & \textbf{99.9}  & \textbf{99.7}  & [99.6, 100] \\
34	& A/E only (Tier\,1)        & 99.92 & 99.9$^\dagger$  & 99.9$^\dagger$ & [99.8, 100] \\
35	\midrule
36	\multirow{2}{*}{\textit{VOTA}}
37	& VOTA ($-$A/E)             & 99.41 & 99.6  & 98.9  & [98.9, 99.8] \\
38	& VOTA (full)               & 99.41 & 99.4  & 98.6  & [98.8, 99.8] \\
39	\bottomrule
40	\end{tabular}
41	\caption{
42	Verdict prediction results on Qwen-2.5-Coder-7B-Instruct (seed\,=\,42, $n$\,=\,1190).
43	\textit{Label-only loss}: full trace input with gradient computed only on verdict tokens (oracle loss masking).
44	\textit{A/E}: actual/expected assertion-p
…[truncated 5709 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_narrative_audit_d034_20260516T012026",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-16T01:21:58.683076+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/_project/paper/section3_experimental_setup.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_narrative_audit_d034_20260516T012026",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/_project/paper/section3_experimental_setup.tex"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-16T01:21:58.683296+00:00_

1	\section{Experimental Setup}
2	\label{sec:setup}
3	
4	\subsection{Task Definition}
5	\label{sec:task}
6	
7	We study \emph{verdict prediction}: given a code snippet $c$, a test input $i$, and an expected output $o_{\text{exp}}$, predict whether executing $c$ on $i$ produces $o_{\text{exp}}$.
8	Let $\mathbf{x} = (c, i, o_{\text{exp}})$ denote the static context and $t$ the full execution trace obtained by running $c(i)$.
9	Each experimental condition defines a trace preprocessing function $f$ such that the model receives $(\mathbf{x}, f(t))$ and generates a verdict $\hat{y} \in \{\text{pass}, \text{fail}\}$.
10	
11	We formulate verdict prediction as supervised fine-tuning (SFT) in an instruction-tuned chat format.
12	The model generates a single token---\texttt{pass} or \texttt{fail}---as its response, which constitutes a single token in both the Qwen and DeepSeek tokenizers used in our experiments.
13	This setup differs fundamentally from code generation: the output space is $O(1)$, so all task-relevant information must be extracted from the input representation.
14	The trace preprocessing function $f$ is therefore the primary design variable.
15	
16	\subsection{Dataset}
17	\label{sec:dataset}
18	
19	We use the verdict prediction dataset constructed by \cite{placeholder_WangEMNLP2025} from CRUXEval \citep{placeholder_GuICML2024}, a benchmark of 800 standalone Python functions designed for execution reasoning evaluation.
20	\cite{placeholder_WangEMNLP2025} paired each function with multiple test cases and collected line-by-line execution traces via a Python tracer, recording every executed line, variable assignment, function call, and exception event.
21	This produced 5{,}910 labeled examples, each containing the source code, test input, expected output, ground-truth verdict, and full execution trace.
22	
23	We split the data into 4{,}720 training and 1{,}190 test examples.
24	The test set is pass-dominant: 71.51\% of samples have verdict \emph{pass}, establishing a
…[truncated 5729 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_narrative_audit_d034_20260516T012026",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-16T01:21:58.683473+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "app:truncat|label.truncat",
  "-i": "True",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "output_mode": "content",
  "-n": "True",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_narrative_audit_d034_20260516T012026",
  "tool": "Grep",
  "tool_args": {
    "pattern": "app:truncat|label.truncat",
    "-i": "True",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
    "output_mode": "content",
    "-n": "True",
    "glob": "*.tex"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-16T01:21:58.683609+00:00_

artifacts/paper_tables/main_results_tables.tex:85:Full trace v3 uses label-preserving truncation (v1 collapsed due to label truncation).
artifacts/_project/paper/section3_experimental_setup.tex:33:We apply chat-template-aware truncation that reserves token budget for the verdict label at the sequence end, preventing the label from being right-truncated during tokenization---a failure mode that causes complete training collapse (Appendix~\ref{app:truncation}).
artifacts/_project/paper/section3_experimental_setup_d4f1e8.tex:33:We apply chat-template-aware truncation that reserves token budget for the verdict label at the sequence end, preventing the label from being right-truncated during tokenization---a failure mode that causes complete training collapse (Appendix~\ref{app:truncation}).
artifacts/_project/paper/main_results_tables.tex:85:Full trace v3 uses label-preserving truncation (v1 collapsed due to label truncation).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_narrative_audit_d034_20260516T012026",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-16T01:21:58.683757+00:00_

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
  "session": "worker_paper_narrative_audit_d034_20260516T012026",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-16T01:21:58.683895+00:00_

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
  "session": "worker_paper_narrative_audit_d034_20260516T012026",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-16T01:21:58.684056+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "truncat",
  "-i": "True",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/related_work.tex",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_narrative_audit_d034_20260516T012026",
  "tool": "Grep",
  "tool_args": {
    "pattern": "truncat",
    "-i": "True",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/related_work.tex",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-16T01:21:58.684176+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_narrative_audit_d034_20260516T012026",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-16T01:21:58.684503+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/method.tex",
  "offset": "75",
  "limit": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_narrative_audit_d034_20260516T012026",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/method.tex",
    "offset": "75",
    "limit": "5"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-16T01:21:58.685008+00:00_

75	All conditions use identical training configurations to ensure fair comparison.
76	We apply LoRA \citep{hu2022lora} (rank=16, $\alpha$=32, dropout=0.05) to all linear layers and train for 3 epochs with batch size 4, gradient accumulation 8 (effective batch size 32), learning rate $2 \times 10^{-4}$ with linear warmup and linear decay, warmup ratio 0.1, and weight decay 0.01.
77	The maximum sequence length is 2,048 tokens; input sequences exceeding this limit are truncated from the input content while preserving the complete verdict label.
78	Training wall-clock time ranges from 0.5 to 2.5 hours per condition on a single GPU, depending on trace format verbosity.
79	The primary seed is 42; seed robustness is evaluated with seeds 123 and 456 for the \texttt{exception\_only} condition.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_narrative_audit_d034_20260516T012026",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-16T01:21:58.685237+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "app:truncation",
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
  "session": "worker_paper_narrative_audit_d034_20260516T012026",
  "tool": "Grep",
  "tool_args": {
    "pattern": "app:truncation",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-16T01:21:58.685412+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_narrative_audit_d034_20260516T012026",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 37 · 2026-05-16T01:21:58.685611+00:00_

`Appendix~\ref{app:truncation}` 只存在于 artifacts 版本（未编译），编译版 `docs/paper/method.tex` 没有这个引用。编译论文无悬空引用问题。

## 最终判定

**编译论文（docs/paper/）叙事一致性全部通过。** 具体结论：

1. **所有描述 VOTA 跨模型 gap（84.45% vs 99.41%）的地方**：全部使用 "trace truncation" / "trace content truncation" / "truncates the trace content"，verdict label 被明确说明是 preserved。✅

2. **描述 DeepSeek full_trace v1 坍塌（28.5%）的地方**（discussion.tex:60）：使用 "truncating the verdict label"，正确描述旧 bug。✅

3. **通用截断说明**（method.tex:32, 77）：使用中性措辞 "truncated to fit" / "truncated from the input content while preserving the complete verdict label"，精确无歧义。✅

4. **artifacts/main_results_tables.tex:85**："v1 collapsed due to label truncation"——这是 v1 旧 bug 的正确描述。✅

**无需修改任何文件。D034 叙事一致性终审通过 ✅**

关于任务提到的 "appendix Table 10 标题 label truncation bug 措辞"：当前编译论文的 appendix 中不存在 Table 10 或包含 "label truncation bug" 的标题。该问题可能已在之前的 audit 中修复，或指的是 artifacts 版本中的 `main_results_tables.tex:85`（"v1 collapsed due to label truncation"），该处描述 v1 旧 bug，措辞正确。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_narrative_audit_d034_20260516T012026"
}
```

</details>

---
