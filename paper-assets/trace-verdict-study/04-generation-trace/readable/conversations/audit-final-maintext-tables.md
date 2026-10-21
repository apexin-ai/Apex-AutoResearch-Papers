# audit final maintext tables

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 55
- **Recorded user turns:** 0
- **Tool calls:** 27
- **Original source:** `logs/chats/worker_audit_final-maintext-tables_20260523T191655.jsonl`
- **Structured JSON:** [`f69900c745133c6262cb.json`](../../sessions/f6/f69900c745133c6262cb.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

55 recorded events

### Tool call

_source line 1 · 2026-05-23T19:33:00.183465+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_final-maintext-tables_20260523T191655",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/paper"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-23T19:33:00.183864+00:00_

&lt;tool_use_error>Directory does not exist: /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/paper. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study.&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_final-maintext-tables_20260523T191655",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-23T19:33:00.184053+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_final-maintext-tables_20260523T191655",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_registry",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-23T19:33:00.184203+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_final-maintext-tables_20260523T191655",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-23T19:33:00.184519+00:00_

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
  "session": "worker_audit_final-maintext-tables_20260523T191655",
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

_source line 6 · 2026-05-23T19:33:00.184726+00:00_

artifacts/dream_reports/dream_20260515T013018/best/paper.tex
artifacts/dream_reports/dream_20260515T013018/median/paper.tex
artifacts/dream_reports/dream_20260515T013018/worst/paper.tex
artifacts/dream_reports/dream_20260515T084908/best/paper.tex
artifacts/dream_reports/dream_20260515T084908/median/paper.tex
artifacts/dream_reports/dream_20260515T084908/worst/paper.tex
artifacts/per_class_breakdown.tex
artifacts/_project/paper/section3_experimental_setup_d4f1e8.tex
artifacts/_project/paper/section3_experimental_setup.tex
artifacts/_project/paper/ethics_statement.tex
artifacts/_project/paper/ethics_statement_77cf5f.tex
artifacts/_project/paper/main_results_tables.tex
artifacts/_project/paper/main_results_tables_d8c8b6.tex
artifacts/paper_tables/main_results_tables.tex
artifacts/dream_reports/dream_20260516T105259/best/paper.tex
artifacts/dream_reports/dream_20260516T105259/median/paper.tex
artifacts/dream_reports/dream_20260516T105259/worst/paper.tex
artifacts/dream_reports/dream_20260516T155731/best/paper.tex
artifacts/dream_reports/dream_20260516T155731/median/paper.tex
artifacts/dream_reports/dream_20260516T155731/worst/paper.tex
artifacts/dream_reports/dream_20260518T113804/best/paper.tex
artifacts/dream_reports/dream_20260518T113804/median/paper.tex
artifacts/dream_reports/dream_20260518T113804/worst/paper.tex
artifacts/dream_reports/dream_20260518T125926/best/paper.tex
artifacts/dream_reports/dream_20260518T125926/median/paper.tex
artifacts/dream_reports/dream_20260518T125926/worst/paper.tex
artifacts/_project/paper/main.tex
artifacts/_project/paper/introduction.tex
artifacts/_project/paper/method.tex
artifacts/_project/paper/discussion.tex
artifacts/_project/paper/conclusion.tex
artifacts/_project/paper/appendix.tex
artifacts/_project/paper/arr_checklist.tex
artifacts/_project/paper/experiments.tex
artifacts/_project/paper/related_work.tex
artifacts/discussion.tex
artifacts/main.tex
artifacts/related_work.tex
docs/paper/arr_checklist.tex
docs/paper/introductio
…[truncated 178 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_final-maintext-tables_20260523T191655",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-23T19:33:00.184878+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "trace-verdict-study",
  "limit": "0",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_final-maintext-tables_20260523T191655",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "trace-verdict-study",
    "limit": "0",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-23T19:33:00.186583+00:00_

Error: result (351,844 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study/d5f32b76-3066-49a9-b711-4657d91efad8/tool-results/mcp-agent-ml-research-read_registry-1779563834793.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study/d5f32b76-3066-49a9-b711-4657d91efad8/tool-results/mcp-agent-ml-research-read_registry-1779563834793.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study/d5f32b76-3066-49a9-b711-4657d91efad8/tool-results/mcp-agent-ml-research-read_registry-1779563834793.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_final-maintext-tables_20260523T191655",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-23T19:33:00.186887+00:00_

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
  "session": "worker_audit_final-maintext-tables_20260523T191655",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-23T19:33:00.187356+00:00_

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
11	\usepackage{algorithm}
12	\usepackage{algorithmic}
13	
14	\title{Complete Execution Traces Degrade SFT-Based Verdict Prediction: \\A Diagnostic Signal Analysis}
15	\author{Anonymous ACL submission}
16	
17	\begin{document}
18	\maketitle
19	
20	\begin{abstract}
21	Complete execution traces contain all information needed for verdict prediction (classifying whether a test passes or fails), yet they actively impair SFT learning.
22	Across four code-specialized models (1.5B--13B, three architecture families), complete traces achieve only 77--82\% while compact exception events reach ${\geq}$99.33\%.
23	A regex exploiting format markers matches this ceiling, but marker removal collapses it to 28.49\% while SFT retains 97.65\%; cross-dataset transfer shows SFT acquires diagnostic patterns beyond format matching.
24	Gradient masking attributes ${\leq}$4\% of the 18--23pp gap to gradient dilution; content quality at inference explains the majority, though forward-pass attention remains an unquantified residual.
25	With compact exception input, SFT on a 7B model surpasses GPT-4o by 12pp, whereas the ranking reverses without trace information---input density dominates model scale.
26	An empirical two-tier signal hierarchy holds across families, yielding a practical strategy: extract exception events first; when unavailable, tail-truncated traces (${\geq}$512 tokens) provide a viable fallback.
27	\end{abstract}
28	
29	\input{introduction}
30	\input{method}
31	\input{experiments}
32	\input{discussion}
33	\input{related_work}
34	\input{conclusion}
35	
36	\section*{Limitations}
37	
38	All experiments use Python-only benchmarks (HumanEval, MBPP-sanitized
…[truncated 478 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_final-maintext-tables_20260523T191655",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-23T19:33:00.187553+00:00_

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
  "session": "worker_audit_final-maintext-tables_20260523T191655",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-23T19:33:00.187720+00:00_

1	\section{Introduction}
2	
3	Execution traces (line-by-line records of a program's runtime behavior) have emerged as a promising input modality for code language models \citep{chen2025tracepile,ding2024traced,wang2025dcsh,ni2024next}.
4	The intuition is straightforward: more execution information should help the model make better predictions.
5	Yet for verdict prediction (classifying whether a test passes or fails), this intuition is wrong.
6	Complete traces \emph{actively degrade} accuracy compared to compact exception events, despite containing strictly more information.
7	
8	Prior work found trace utility to be task-dependent \citep{wang2025dcsh}, but focused on generation-oriented tasks where output noise confounds the analysis.
9	Verdict prediction offers a cleaner testbed: as binary classification, it isolates the learning signal from generation noise, and controlled component ablation directly measures how trace content affects SFT learning.
10	This approach aligns with recent *ACL precedent: CRUXEval \citep{gu2024cruxeval} uses execution prediction to probe code reasoning, and NExT \citep{ni2024next} uses trace-augmented chain-of-thought for program repair.
11	
12	We present a systematic component ablation of trace representations for verdict prediction.
13	Using 591 problems from HumanEval \citep{chen2021evaluating} and MBPP-sanitized \citep{austin2021program}, we evaluate four models across three architecture families and 1.5B to 13B parameters: Qwen-2.5-Coder-7B/1.5B-Instruct \citep{qwen2024coder}, CodeLlama-13B-Instruct \citep{roziere2024code}, and DeepSeek-Coder-6.7B-Instruct \citep{deepseek2024coder}.
14	
15	The central result: complete traces (77--82\%) barely improve over source code alone, while compact exception events achieve near-perfect accuracy (${\geq}$99\%) across all four models, an 18--23pp gap (\S\ref{sec:cross_model}).
16	A simple regex exploiting a format marker matches this ceiling, so the interesting question is not why exceptions hel
…[truncated 2263 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_final-maintext-tables_20260523T191655",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-23T19:33:00.187864+00:00_

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
  "session": "worker_audit_final-maintext-tables_20260523T191655",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-23T19:33:00.188036+00:00_

1	\section{Method}
2	
3	\subsection{Task Definition and Diagnostic Signal Metrics}
4	
5	We study \emph{verdict prediction}: given a Python function, a test input, and an optional execution trace, predict whether the test passes or fails.
6	The model produces a single token (\texttt{pass} or \texttt{fail}), making this a binary classification task.
7	Unlike code generation \citep{chen2025tracepile} or output prediction \citep{gu2024cruxeval}, verdict prediction isolates the model's ability to detect faults from its ability to simulate execution, providing cleaner ablation contrasts than generation tasks.
8	
9	To quantify signal quality without circular reference to model accuracy, we define the \emph{diagnostic token ratio} $d = n_{\text{diag}} / n_{\text{total}}$, where $n_{\text{diag}}$ counts tokens matching exception or assertion patterns.
10	This model-free metric correlates with accuracy at Pearson $r{=}0.949$ ($p{=}0.014$, $N{=}5$, df=3; treat as descriptive), but captures only the \emph{explicit} diagnostic pathway; tail-truncated conditions achieve 93--98\% with $d {\approx} 0$, indicating a second, implicit signal channel operating through terminal execution state (\S\ref{sec:density}).
11	
12	\subsection{Dataset}
13	\label{sec:dataset}
14	
15	We sampled 10 candidate solutions per problem from Qwen-2.5-Coder-7B-Instruct (temperature 0.8, top\_p 0.95) for 591 problems from HumanEval \citep{chen2021evaluating} (164) and MBPP-sanitized \citep{austin2021program} (427), executed each against canonical tests with \texttt{sys.settrace} to obtain line-level traces and pass/fail verdicts, yielding 5,910 pairs (67\% pass, 33\% fail).
16	The dataset is split 80/20 by problem ID into 4,720 training and 1,190 test samples (majority baseline: 71.51\%).
17	The \texttt{exception\_only} format collapses passing solutions into identical rows (39.45\% train, 48.99\% test duplicates); these duplicates arise from multiple candidate solutions per problem, with the train--test sp
…[truncated 3243 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_final-maintext-tables_20260523T191655",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-23T19:33:00.188192+00:00_

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
  "session": "worker_audit_final-maintext-tables_20260523T191655",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-23T19:33:00.188461+00:00_

1	\section{Experiments}
2	
3	We evaluate across two research questions:
4	(1)~Why do complete traces degrade SFT verdict accuracy despite containing all diagnostic information?
5	(2)~Which trace components carry the verdict signal, and how does their density affect learning?
6	All experiments use $N{=}1{,}190$ test samples; accuracy is reported with Wilson 95\% CIs.\footnote{Problem-level partition (472 train / 119 test, zero crossover; \S\ref{sec:dataset}). \texttt{exception\_only} duplicates (48.99\% test; Appendix~\ref{sec:dedup_stats}) arise from within-problem variants; deduplication yields negligible ($<$0.1pp) delta.}
7	Pairwise comparisons use paired bootstrap resampling ($B{=}10{,}000$, seed=42); all differences are significant at $p{<}.0001$ unless noted.
8	Under problem-level clustered bootstrap ($n_\text{eff}{=}119$), all cross-tier gaps remain significant ($p{<}.001$); 3 of 80 within-tier pairwise comparisons lose significance after Holm--Bonferroni correction.
9	
10	\subsection{Cross-Model Comparison}
11	\label{sec:cross_model}
12	
13	Table~\ref{tab:cross_model} compares four models spanning an 8.7$\times$ parameter range (1.5B--13B) and three architecture families under key conditions; single-seed entries are marked with $^\dag$.
14	Regex B5 (99.33\%) exploits the \texttt{[No exception data in trace]} format marker, providing a non-learned baseline; its collapse to 28.49\% under marker removal (\S\ref{sec:nomarker}) shows the SFT advantage is not format-driven.
15	
16	\begin{table}[t]
17	\centering
18	\caption{Cross-model verdict accuracy (\%, $N{=}1{,}190$) across four models (1.5B--13B) and three architecture families. Multi-seed entries report mean$\pm$std over 2--3 seeds; $^\dag$ = single seed (seed 42). Bold: best per model. Full per-seed breakdowns in Appendix~\ref{sec:full_results}; per-class metrics in Appendix~\ref{sec:per_class}.}
19	\label{tab:cross_model}
20	\small
21	\resizebox{\columnwidth}{!}{%
22	\begin{tabular}{lcccc}
23	\toprule
24	\
…[truncated 17670 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_final-maintext-tables_20260523T191655",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-23T19:33:00.188767+00:00_

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
  "session": "worker_audit_final-maintext-tables_20260523T191655",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/discussion.tex"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-23T19:33:00.188961+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{A descriptive two-pathway framework.}
5	The results suggest two independent signal pathways and a dilution mechanism that together explain why complete traces degrade SFT learning.
6	
7	\paragraph{Explicit pathway: diagnostic tokens.}
8	The diagnostic token ratio $d$ (\S2.1) correlates strongly with accuracy across five conditions, and all four models achieve near-perfect accuracy under \texttt{exception\_only} (Table~\ref{tab:cross_model}).
9	\texttt{ae\_only}, a strict superset, slightly underperforms (Table~\ref{tab:ablation}), indicating that additional content introduces noise even within exception events.
10	
11	\paragraph{Implicit pathway: terminal execution state.}
12	Tail-truncated traces achieve 93--98\% accuracy (Table~\ref{tab:tail_cross_model}) despite $d {\approx} 0$.
13	At ${\geq}$512 tokens (Figure~\ref{fig:budget_curve}), tail truncation captures \texttt{[Line~X]} variable values at final execution steps, which implicitly encode verdict direction; below 384 tokens, the globals module dump consumes the entire budget, yielding near-\texttt{no\_trace} performance.
14	
15	\paragraph{Diagnostic signal dilution in complete traces.}
16	Both pathways' signals exist in full traces but are buried under thousands of intermediate tokens.
17	Controlled gradient masking (\S\ref{sec:density}) attributes ${\leq}$4\% of the gap to gradient dilution, assigning the majority to content quality at inference: diagnostic tokens are too sparse for the model to reliably extract from verbose input.
18	Training dynamics (Appendix~\ref{sec:training_dynamics}) corroborate this: \texttt{exception\_only} converges within 50 steps while \texttt{full\_trace} oscillates without convergence.
19	
20	\paragraph{Why SFT over regex?}
21	The contribution is the diagnostic decomposition, not a prediction system; nonetheless, SFT dominates regex on every axis beyond raw accuracy.
22	SFT retains 97.65\% under marker removal whil
…[truncated 869 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_final-maintext-tables_20260523T191655",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-23T19:33:00.189117+00:00_

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
  "session": "worker_audit_final-maintext-tables_20260523T191655",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-23T19:33:00.189446+00:00_

1	\section{Conclusion}
2	
3	Across four code-specialized models (1.5B--13B), compact exception events (${\geq}$99.33\%) outperform complete traces (77--82\%) by 18--23pp; gradient masking (${\leq}$4\% dilution), cross-dataset transfer (99.4--100\%), and marker-removal robustness show that diagnostic density, not information quantity, drives SFT learning.
4	Practitioners should extract exception events first; tail-truncated traces (${\geq}$512 tokens) recover 93--98\% as fallback.
5	Whether models beyond 13B can overcome signal dilution in complete traces, and whether these findings extend to languages without Python's structured exception hierarchy, remain open questions.
6	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_final-maintext-tables_20260523T191655",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-23T19:33:00.189812+00:00_

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
  "session": "worker_audit_final-maintext-tables_20260523T191655",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/appendix.tex"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-23T19:33:00.190728+00:00_

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
…[truncated 53688 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_final-maintext-tables_20260523T191655",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-23T19:33:00.190961+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Parse registry JSON for audit",
  "prompt": "I need you to parse a large JSON registry file and extract all experiment metrics for a paper data audit.\n\nThe file is at: /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study/d5f32b76-3066-49a9-b711-4657d91efad8/tool-results/mcp-agent-ml-research-read_registry-1779563834793.txt\n\nIt's JSON with schema: {result: string} — the `result` field is itself a JSON string that needs to be parsed.\n\nPlease use Python to:\n1. Load the file, parse the outer JSON, then parse the inner `result` string\n2. For each experiment, extract: exp_id, status, metrics (especially accuracy, mean, std, seeds, ECE, Brier, CI, etc.), and any tags/labels\n3. Group experiments by their type/condition (e.g., exception_only, full_trace, ae_only, VOTA, loop_only, no_trace, regex, majority, ablation, density/gradient masking, cross-dataset, nomarker, SFT, etc.)\n\nOutput a comprehensive structured summary with ALL numeric metrics for every experiment. I need exact numbers - don't round or summarize. Include exp_id for each.\n\nFocus especially on:\n- Table 1 experiments (cross_model): exception_only, ae_only, VOTA, loop_only, full_trace, no_trace for models GPT-4o, Claude-3.5, Gemini-2.0, DeepSeek-V3\n- Table 2 experiments (ablation): different conditions with accuracy, CI, tier\n- Table 3 experiments (density decomposition): exception_only, gradient masking, full_trace, label-only\n- Regex baseline and Majority baseline numbers\n- Any nomarker experiments\n- Any cross-dataset experiments\n- ECE and Brier score values\n\nWrite the output to /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/_audit_registry_extract.txt so I can read it.",
  "model": "sonnet"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_final-maintext-tables_20260523T191655",
  "tool": "Agent",
  "tool_args": {
    "description": "Parse registry JSON for audit",
    "prompt": "I need you to parse a large JSON registry file and extract all experiment metrics for a paper data audit.\n\nThe file is at: /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study/d5f32b76-3066-49a9-b711-4657d91efad8/tool-results/mcp-agent-ml-research-read_registry-1779563834793.txt\n\nIt's JSON with schema: {result: string} — the `result` field is itself a JSON string that needs to be parsed.\n\nPlease use Python to:\n1. Load the file, parse the outer JSON, then parse the inner `result` string\n2. For each experiment, extract: exp_id, status, metrics (especially accuracy, mean, std, seeds, ECE, Brier, CI, etc.), and any tags/labels\n3. Group experiments by their type/condition (e.g., exception_only, full_trace, ae_only, VOTA, loop_only, no_trace, regex, majority, ablation, density/gradient masking, cross-dataset, nomarker, SFT, etc.)\n\nOutput a comprehensive structured summary with ALL numeric metrics for every experiment. I need exact numbers - don't round or summarize. Include exp_id for each.\n\nFocus especially on:\n- Table 1 experiments (cross_model): exception_only, ae_only, VOTA, loop_only, full_trace, no_trace for models GPT-4o, Claude-3.5, Gemini-2.0, DeepSeek-V3\n- Table 2 experiments (ablation): different conditions with accuracy, CI, tier\n- Table 3 experiments (density decomposition): exception_only, gradient masking, full_trace, label-only\n- Regex baseline and Majority baseline numbers\n- Any nomarker experiments\n- Any cross-dataset experiments\n- ECE and Brier score values\n\nWrite the output to /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/_audit_registry_extract.txt so I can read it.",
    "model": "sonnet"
  }
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-23T19:33:00.191154+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study/d5f32b76-3066-49a9-b711-4657d91efad8/tool-results/mcp-agent-ml-research-read_registry-1779563834793.txt 2>/dev/null && echo \"FILE_EXISTS\" || echo \"FILE_NOT_FOUND\"",
  "description": "Check if the target file exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_final-maintext-tables_20260523T191655",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study/d5f32b76-3066-49a9-b711-4657d91efad8/tool-results/mcp-agent-ml-research-read_registry-1779563834793.txt 2>/dev/null && echo \"FILE_EXISTS\" || echo \"FILE_NOT_FOUND\"",
    "description": "Check if the target file exists"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-23T19:33:00.191390+00:00_

/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study/d5f32b76-3066-49a9-b711-4657d91efad8/tool-results/mcp-agent-ml-research-read_registry-1779563834793.txt
FILE_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_final-maintext-tables_20260523T191655",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-23T19:33:00.191538+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nfilepath = \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study/d5f32b76-3066-49a9-b711-4657d91efad8/tool-results/mcp-agent-ml-research-read_registry-1779563834793.txt\"\n\nwith open(filepath, 'r') as f:\n    outer = json.load(f)\n\nprint(\"Outer keys:\", list(outer.keys()))\nresult_str = outer.get('result', '')\nprint(\"Result type:\", type(result_str))\nprint(\"Result length:\", len(result_str))\nprint(\"First 500 chars:\", result_str[:500])\nPYEOF\n",
  "description": "Parse outer JSON and inspect inner result"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_final-maintext-tables_20260523T191655",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 << 'PYEOF'\nimport json\n\nfilepath = \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study/d5f32b76-3066-49a9-b711-4657d91efad8/tool-results/mcp-agent-ml-research-read_registry-1779563834793.txt\"\n\nwith open(filepath, 'r') as f:\n    outer = json.load(f)\n\nprint(\"Outer keys:\", list(outer.keys()))\nresult_str = outer.get('result', '')\nprint(\"Result type:\", type(result_str))\nprint(\"Result length:\", len(result_str))\nprint(\"First 500 chars:\", result_str[:500])\nPYEOF\n",
    "description": "Parse outer JSON and inspect inner result"
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-23T19:33:00.191669+00:00_

Outer keys: ['result']
Result type: &lt;class 'str'>
Result length: 329949
First 500 chars: {"success": true, "data": {"experiments": {"deepseek_gradient_masking_seed123": {"status": "DONE", "retry_count": 0, "created_at": "2026-05-23T09:51:05.056Z", "updated_at": "2026-05-23T13:45:23.758Z", "hypothesis": "DeepSeek-6.7B gradient masking multi-seed validation (seed 123): 99.8% gradient masking should achieve ≥98.5% accuracy, confirming dilution bound stability. Derived from deepseek_gradient_masking_seed42 (99.33%, dilution 0.06%).", "parent": "deepseek_gradient_masking_seed42", "spec":

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_final-maintext-tables_20260523T191655",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-23T19:33:00.191812+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\nimport os\n\nfilepath = \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study/d5f32b76-3066-49a9-b711-4657d91efad8/tool-results/mcp-agent-ml-research-read_registry-1779563834793.txt\"\n\nwith open(filepath, 'r') as f:\n    outer = json.load(f)\n\nresult_str = outer['result']\ninner = json.loads(result_str)\n\nprint(\"Inner keys:\", list(inner.keys()))\ndata = inner.get('data', {})\nprint(\"Data keys:\", list(data.keys()))\nexperiments = data.get('experiments', {})\nprint(\"Total experiments:\", len(experiments))\nprint(\"\\nAll experiment IDs:\")\nfor eid in sorted(experiments.keys()):\n    print(\" -\", eid)\nPYEOF\n",
  "description": "Parse inner JSON and list all experiment IDs"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_final-maintext-tables_20260523T191655",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 << 'PYEOF'\nimport json\nimport os\n\nfilepath = \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study/d5f32b76-3066-49a9-b711-4657d91efad8/tool-results/mcp-agent-ml-research-read_registry-1779563834793.txt\"\n\nwith open(filepath, 'r') as f:\n    outer = json.load(f)\n\nresult_str = outer['result']\ninner = json.loads(result_str)\n\nprint(\"Inner keys:\", list(inner.keys()))\ndata = inner.get('data', {})\nprint(\"Data keys:\", list(data.keys()))\nexperiments = data.get('experiments', {})\nprint(\"Total experiments:\", len(experiments))\nprint(\"\\nAll experiment IDs:\")\nfor eid in sorted(experiments.keys()):\n    print(\" -\", eid)\nPYEOF\n",
    "description": "Parse inner JSON and list all experiment IDs"
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-23T19:33:00.191959+00:00_

Inner keys: ['success', 'data', 'error', 'metadata']
Data keys: ['experiments', 'count', 'total', 'baseline']
Total experiments: 188

All experiment IDs:
 - ae_only_seed123
 - ae_only_seed456
 - attention_gradient_analysis
 - calibration_analysis_seed42
 - codellama13b_ae_only_seed123
 - codellama13b_ae_only_seed42
 - codellama13b_exception_only_seed123
 - codellama13b_exception_only_seed42
 - codellama13b_exception_only_seed456
 - codellama13b_full_trace_head2048_seed42
 - codellama13b_full_trace_tail1024_seed42
 - codellama13b_full_trace_tail1024_seed42_v2
 - codellama13b_full_trace_tail1024_seed42_v3
 - codellama13b_full_trace_tail2048_seed42
 - codellama13b_full_trace_tail2048_seed42_v2
 - codellama13b_full_trace_tail2048_seed42_v3
 - codellama13b_full_trace_tail256_seed42
 - codellama13b_full_trace_tail384_seed42
 - codellama13b_full_trace_tail512_seed123
 - codellama13b_full_trace_tail512_seed42
 - codellama13b_full_trace_tail512_seed456
 - codellama13b_label_only_seed123_v2
 - codellama13b_label_only_seed42
 - codellama13b_label_only_seed42_v2
 - codellama13b_loop_only_seed123
 - codellama13b_loop_only_seed42
 - codellama13b_loop_only_seed456
 - codellama13b_no_trace_seed42
 - codellama13b_nomarker_seed42
 - codellama13b_vota_seed123
 - codellama13b_vota_seed42
 - codellama_exception_only_seed42
 - codellama_gradient_masking_seed42
 - codellama_no_trace_seed42
 - codellama_vota_seed42
 - cross_dataset_batch
 - cross_he2mbpp_exception_only_seed42
 - cross_he2mbpp_no_trace_seed42
 - cross_mbpp2he_exception_only_seed42
 - cross_mbpp2he_no_trace_seed42
 - cross_model_calibration
 - cross_model_calibration_eval
 - debugbench_exception_bug_fix
 - debugbench_exception_only_seed42
 - debugbench_no_trace_seed42
 - debugbench_vota_seed42
 - deepseek_ae_only_seed123
 - deepseek_ae_only_seed42
 - deepseek_exception_only_seed123
 - deepseek_exception_only_seed123_v2
 - deepseek_exception_only_seed42
 - deepseek_exception_only_seed456
 - deepseek_full_trace_head2048_seed42
…[truncated 4062 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_final-maintext-tables_20260523T191655",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-23T19:33:00.192115+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nfilepath = \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study/d5f32b76-3066-49a9-b711-4657d91efad8/tool-results/mcp-agent-ml-research-read_registry-1779563834793.txt\"\n\nwith open(filepath, 'r') as f:\n    outer = json.load(f)\n\ninner = json.loads(outer['result'])\nexperiments = inner['data']['experiments']\nbaseline = inner['data'].get('baseline', {})\n\n# Inspect a few experiments to understand schema\nsample_ids = list(experiments.keys())[:3]\nfor eid in sample_ids:\n    print(f\"\\n=== {eid} ===\")\n    exp = experiments[eid]\n    print(json.dumps(exp, indent=2)[:2000])\n    print(\"...\")\nPYEOF\n",
  "description": "Inspect a few experiment schemas to understand field structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_final-maintext-tables_20260523T191655",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 << 'PYEOF'\nimport json\n\nfilepath = \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study/d5f32b76-3066-49a9-b711-4657d91efad8/tool-results/mcp-agent-ml-research-read_registry-1779563834793.txt\"\n\nwith open(filepath, 'r') as f:\n    outer = json.load(f)\n\ninner = json.loads(outer['result'])\nexperiments = inner['data']['experiments']\nbaseline = inner['data'].get('baseline', {})\n\n# Inspect a few experiments to understand schema\nsample_ids = list(experiments.keys())[:3]\nfor eid in sample_ids:\n    print(f\"\\n=== {eid} ===\")\n    exp = experiments[eid]\n    print(json.dumps(exp, indent=2)[:2000])\n    print(\"...\")\nPYEOF\n",
    "description": "Inspect a few experiment schemas to understand field structure"
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-23T19:33:00.192285+00:00_

=== deepseek_gradient_masking_seed123 ===
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-23T09:51:05.056Z",
  "updated_at": "2026-05-23T13:45:23.758Z",
  "hypothesis": "DeepSeek-6.7B gradient masking multi-seed validation (seed 123): 99.8% gradient masking should achieve \u226598.5% accuracy, confirming dilution bound stability. Derived from deepseek_gradient_masking_seed42 (99.33%, dilution 0.06%).",
  "parent": "deepseek_gradient_masking_seed42",
  "spec": {
    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/trace-verdict-study && python train/train_sft.py --condition exception_only --model_path deepseek-coder-6.7b-instruct --gradient_mask_ratio 0.998 --gradient_checkpointing --seed 123\"",
    "server": "westd-11235",
    "gpu": [
      "cuda:0"
    ],
    "pid": "874893",
    "log_path": "~/runs/trace-verdict-study/deepseek_gradient_masking_seed123.log",
    "data_path": "/root/trace-verdict-study/data/exception_only_train.jsonl",
    "data_count": 4720,
    "model_name": "deepseek-ai/deepseek-coder-6.7b-instruct",
    "seed": 123,
    "checkpoint_source": "trained_from_scratch",
    "eval_data": "/root/trace-verdict-study/data/exception_only_test.jsonl",
    "checkpoint_path": "/root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_gradient_masking_seed123/final/"
  },
  "metrics": {
    "accuracy": 0.9395,
    "pass_precision": 0.924,
    "pass_recall": 0.998,
    "pass_f1": 0.959,
    "fail_precision": 0.993,
    "fail_recall": 0.794,
    "fail_f1": 0.882
  },
  "conclusion": "negative",
  "completed_at": "2026-05-23T13:45:23.758Z"
}
...

=== codellama_gradient_masking_seed42 ===
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-23T08:52:00.476Z",
  "updated_at": "2026-05-23T11:40:38.570Z",
  "hypothesis": "Cross-architecture gradient masking validation: CodeLlama-13B exception_only with 99.8% gradient masking should achieve \u226598.5% accuracy (vs baseline 99.89
…[truncated 2945 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_final-maintext-tables_20260523T191655",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-23T19:33:00.192451+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nfilepath = \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study/d5f32b76-3066-49a9-b711-4657d91efad8/tool-results/mcp-agent-ml-research-read_registry-1779563834793.txt\"\n\nwith open(filepath, 'r') as f:\n    outer = json.load(f)\n\ninner = json.loads(outer['result'])\nexperiments = inner['data']['experiments']\nbaseline = inner['data'].get('baseline', {})\n\n# Check baseline structure\nprint(\"=== BASELINE ===\")\nprint(json.dumps(baseline, indent=2)[:3000])\nPYEOF\n",
  "description": "Check baseline data structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_final-maintext-tables_20260523T191655",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 << 'PYEOF'\nimport json\n\nfilepath = \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study/d5f32b76-3066-49a9-b711-4657d91efad8/tool-results/mcp-agent-ml-research-read_registry-1779563834793.txt\"\n\nwith open(filepath, 'r') as f:\n    outer = json.load(f)\n\ninner = json.loads(outer['result'])\nexperiments = inner['data']['experiments']\nbaseline = inner['data'].get('baseline', {})\n\n# Check baseline structure\nprint(\"=== BASELINE ===\")\nprint(json.dumps(baseline, indent=2)[:3000])\nPYEOF\n",
    "description": "Check baseline data structure"
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-23T19:33:00.192585+00:00_

=== BASELINE ===
null

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_final-maintext-tables_20260523T191655",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-23T19:33:00.192715+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nfilepath = \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study/d5f32b76-3066-49a9-b711-4657d91efad8/tool-results/mcp-agent-ml-research-read_registry-1779563834793.txt\"\n\nwith open(filepath, 'r') as f:\n    outer = json.load(f)\n\ninner = json.loads(outer['result'])\nexperiments = inner['data']['experiments']\n\n# Look at cross_model, regex, majority, calibration, ablation, density/cross-dataset key experiments\nkey_ids = [\n    'cross_model_calibration', 'cross_model_calibration_eval',\n    'regex_baseline_analysis', 'regex_nomarker_baseline',\n    'majority_baseline' if 'majority_baseline' in experiments else None,\n    'calibration_analysis_seed42',\n    'cross_dataset_batch',\n    'cross_he2mbpp_exception_only_seed42', 'cross_he2mbpp_no_trace_seed42',\n    'cross_mbpp2he_exception_only_seed42', 'cross_mbpp2he_no_trace_seed42',\n    'nomarker_cross_he2mbpp_exception_only',\n]\n\nfor eid in key_ids:\n    if eid and eid in experiments:\n        print(f\"\\n=== {eid} ===\")\n        print(json.dumps(experiments[eid], indent=2))\nPYEOF\n",
  "description": "Inspect key cross_model, regex, calibration, cross_dataset experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_final-maintext-tables_20260523T191655",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 << 'PYEOF'\nimport json\n\nfilepath = \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study/d5f32b76-3066-49a9-b711-4657d91efad8/tool-results/mcp-agent-ml-research-read_registry-1779563834793.txt\"\n\nwith open(filepath, 'r') as f:\n    outer = json.load(f)\n\ninner = json.loads(outer['result'])\nexperiments = inner['data']['experiments']\n\n# Look at cross_model, regex, majority, calibration, ablation, density/cross-dataset key experiments\nkey_ids = [\n    'cross_model_calibration', 'cross_model_calibration_eval',\n    'regex_baseline_analysis', 'regex_nomarker_baseline',\n    'majority_baseline' if 'majority_baseline' in experiments else None,\n    'calibration_analysis_seed42',\n    'cross_dataset_batch',\n    'cross_he2mbpp_exception_only_seed42', 'cross_he2mbpp_no_trace_seed42',\n    'cross_mbpp2he_exception_only_seed42', 'cross_mbpp2he_no_trace_seed42',\n    'nomarker_cross_he2mbpp_exception_only',\n]\n\nfor eid in key_ids:\n    if eid and eid in experiments:\n        print(f\"\\n=== {eid} ===\")\n        print(json.dumps(experiments[eid], indent=2))\nPYEOF\n",
    "description": "Inspect key cross_model, regex, calibration, cross_dataset experiments"
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-23T19:33:00.192903+00:00_

=== cross_model_calibration ===
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-21T06:14:12.232Z",
  "updated_at": "2026-05-21T06:14:57.965Z",
  "hypothesis": "Calibration quality (ECE and Brier Score) of exception_only fine-tuned models is universally strong across different model architectures and sizes, not specific to Qwen-7B.",
  "spec": {
    "command": "bash eval/run_cross_model_calibration.sh",
    "server": "westd-11235",
    "data_path": "/root/autodl-tmp/trace-verdict-study-data/exception_only_test.jsonl",
    "data_count": 1190,
    "model_name": "Qwen-7B/Qwen-1.5B/CodeLlama-13B/DeepSeek-6.7B",
    "seed": 42,
    "checkpoint_source": "exception_only checkpoints for all 4 models",
    "eval_data": "exception_only_test.jsonl (1190 samples)",
    "checkpoint_path": "/root/autodl-tmp/trace-verdict-study-checkpoints/cross_model_calibration/",
    "log_path": "/root/autodl-tmp/trace-verdict-study-checkpoints/cross_model_calibration/calibration.log"
  },
  "conclusion": "success",
  "completed_at": "2026-05-21T06:14:57.965Z"
}

=== cross_model_calibration_eval ===
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-19T21:40:43.958Z",
  "updated_at": "2026-05-19T21:41:10.724Z",
  "hypothesis": "4 \u6a21\u578b \u00d7 exception_only \u7684 ECE/Brier \u5e94\u4e00\u81f4\u6027\u4f4e\uff08ECE < 0.01\uff09\uff0c\u9a8c\u8bc1 calibration quality \u8de8\u6a21\u578b universal",
  "conclusion": "success",
  "metrics": {
    "qwen_7b": {
      "ece": 0.0027,
      "mce": 0.8355,
      "brier": 0.0013,
      "accuracy": 0.9983
    },
    "qwen_1_5b": {
      "ece": 0.002,
      "mce": 0.7549,
      "brier": 0.0013,
      "accuracy": 0.9983
    },
    "codellama_13b": {
      "ece": 0.002,
      "mce": 0.0411,
      "brier": 0.0013,
      "accuracy": 0.9983
    },
    "deepseek_6_7b": {
      "ece": 0.0064,
      "mce": 0.7756,
      "brier": 0.0061,
      "accuracy": 0.9933
    }
  },
  "spec": {
    "checkpoint_path": "/root/autodl-tmp/trac
…[truncated 12408 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_final-maintext-tables_20260523T191655",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-23T19:33:00.193066+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nfilepath = \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study/d5f32b76-3066-49a9-b711-4657d91efad8/tool-results/mcp-agent-ml-research-read_registry-1779563834793.txt\"\n\nwith open(filepath, 'r') as f:\n    outer = json.load(f)\n\ninner = json.loads(outer['result'])\nexperiments = inner['data']['experiments']\n\n# Look at main table experiments: exception_only, full_trace, no_trace, vota, ae_only, loop_only for Qwen-7B (the base)\nmain_ids = [\n    'exception_only_seed123', 'exception_only_seed456',\n    'full_trace_seed123', 'full_trace_seed42', 'full_trace_seed42_v2', 'full_trace_seed42_v5', 'full_trace_seed456',\n    'no_trace_seed42', 'no_trace_seed123', 'no_trace_seed456',\n    'no_trace_seed42_v2', 'no_trace_seed42_v3', 'no_trace_seed42_v4', 'no_trace_seed42_v5',\n    'vota_seed42', 'vota_seed123', 'vota_seed456',\n    'vota_seed42_v2', 'vota_seed42_v3', 'vota_seed42_v4', 'vota_seed42_v5',\n    'vota_seed456_v2',\n    'ae_only_seed123', 'ae_only_seed456',\n    'loop_only_seed123', 'loop_only_seed456',\n    'label_only_seed123', 'label_only_seed456',\n]\n\nfor eid in main_ids:\n    if eid in experiments:\n        exp = experiments[eid]\n        print(f\"\\n=== {eid} ===\")\n        print(f\"  status: {exp.get('status')}\")\n        print(f\"  metrics: {json.dumps(exp.get('metrics', {}))}\")\n        print(f\"  conclusion: {exp.get('conclusion')}\")\n        tags = exp.get('tags', exp.get('labels', exp.get('tag', exp.get('label', None))))\n        if tags:\n            print(f\"  tags: {tags}\")\nPYEOF\n",
  "description": "Inspect main Qwen-7B table experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_final-maintext-tables_20260523T191655",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 << 'PYEOF'\nimport json\n\nfilepath = \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study/d5f32b76-3066-49a9-b711-4657d91efad8/tool-results/mcp-agent-ml-research-read_registry-1779563834793.txt\"\n\nwith open(filepath, 'r') as f:\n    outer = json.load(f)\n\ninner = json.loads(outer['result'])\nexperiments = inner['data']['experiments']\n\n# Look at main table experiments: exception_only, full_trace, no_trace, vota, ae_only, loop_only for Qwen-7B (the base)\nmain_ids = [\n    'exception_only_seed123', 'exception_only_seed456',\n    'full_trace_seed123', 'full_trace_seed42', 'full_trace_seed42_v2', 'full_trace_seed42_v5', 'full_trace_seed456',\n    'no_trace_seed42', 'no_trace_seed123', 'no_trace_seed456',\n    'no_trace_seed42_v2', 'no_trace_seed42_v3', 'no_trace_seed42_v4', 'no_trace_seed42_v5',\n    'vota_seed42', 'vota_seed123', 'vota_seed456',\n    'vota_seed42_v2', 'vota_seed42_v3', 'vota_seed42_v4', 'vota_seed42_v5',\n    'vota_seed456_v2',\n    'ae_only_seed123', 'ae_only_seed456',\n    'loop_only_seed123', 'loop_only_seed456',\n    'label_only_seed123', 'label_only_seed456',\n]\n\nfor eid in main_ids:\n    if eid in experiments:\n        exp = experiments[eid]\n        print(f\"\\n=== {eid} ===\")\n        print(f\"  status: {exp.get('status')}\")\n        print(f\"  metrics: {json.dumps(exp.get('metrics', {}))}\")\n        print(f\"  conclusion: {exp.get('conclusion')}\")\n        tags = exp.get('tags', exp.get('labels', exp.get('tag', exp.get('label', None))))\n        if tags:\n            print(f\"  tags: {tags}\")\nPYEOF\n",
    "description": "Inspect main Qwen-7B table experiments"
  }
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-23T19:33:00.193258+00:00_

=== exception_only_seed123 ===
  status: DONE
  metrics: {"accuracy": 0.9983, "accuracy_ci": [0.9958, 1], "majority_baseline": 0.7151, "lift": 0.2832, "n": 1190, "pass_precision": 1, "pass_recall": 0.9976, "pass_f1": 0.9988, "fail_precision": 0.9941, "fail_recall": 1, "fail_f1": 0.9971, "train_loss": 0.1096, "train_runtime_sec": 7507, "epochs": 3, "seed_comparison": {"seed42_accuracy": 0.9983, "seed456_accuracy": 0.9983, "seed123_accuracy": 0.9983, "max_diff": 0, "note": "identical accuracy to 4 decimal places across all 3 seeds (42/456/123); each has exactly 2/1190 errors; exception_only fully seed-robust"}}
  conclusion: success

=== exception_only_seed456 ===
  status: DONE
  metrics: {"accuracy": 0.9983, "accuracy_ci": [0.9958, 1], "majority_baseline": 0.7151, "lift": 0.2832, "n": 1190, "pass_precision": 1, "pass_recall": 0.9976, "pass_f1": 0.9988, "fail_precision": 0.9941, "fail_recall": 1, "fail_f1": 0.9971, "vs_seed42": {"seed42_accuracy": 0.9983, "seed456_accuracy": 0.9983, "diff": 0, "note": "identical accuracy to 4 decimal places; no predictions.jsonl for paired bootstrap"}, "train_loss": 0.1087, "eval_loss": 0.4629, "train_runtime_sec": 4541, "epochs": 3}
  conclusion: success

=== full_trace_seed123 ===
  status: DONE
  metrics: {"accuracy": 0.7958, "majority_baseline": 0.7151, "lift": 0.0807, "n": 1190, "pass_precision": 0.8753, "pass_recall": 0.8331, "pass_f1": 0.8537, "fail_precision": 0.6263, "fail_recall": 0.7021, "fail_f1": 0.662, "accuracy_ci_lower": 0.7714, "accuracy_ci_upper": 0.8202, "lift_ci_lower": 0.0504, "lift_ci_upper": 0.1143, "train_loss": 0.0416, "eval_loss": 0.0842, "wall_clock_seconds": 7844, "epoch_level": {"epoch_2_eval_loss": 0.0761, "epoch_3_eval_loss": 0.0842}}
  conclusion: success

=== full_trace_seed42 ===
  status: DONE
  metrics: {"train_loss": 0.037, "eval_loss": 0.084, "eval_mean_token_accuracy": 0.984, "accuracy": 0.284, "majority_baseline": 0.7151, "lift": -0.431, "pass_precision": 0.88, "pass_recall": 0.08, "pass_f1": 0
…[truncated 7000 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_final-maintext-tables_20260523T191655",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-23T19:33:00.193432+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nfilepath = \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study/d5f32b76-3066-49a9-b711-4657d91efad8/tool-results/mcp-agent-ml-research-read_registry-1779563834793.txt\"\n\nwith open(filepath, 'r') as f:\n    outer = json.load(f)\n\ninner = json.loads(outer['result'])\nexperiments = inner['data']['experiments']\n\n# Look at Qwen-7B seed42 canonical: exception_only, full_trace, no_trace, vota, ae_only, loop_only\n# Also check VOTA multi-component ablation experiments\nvota_ablation = ['vota_ae_only_seed42', 'vota_exception_only_seed42', 'vota_exception_only_seed42_v2',\n                 'vota_loop_only_seed42', 'vota_no_ae_seed42',\n                 'exc_message_only_seed42', 'exc_stacktrace_only_seed42', 'exc_type_only_seed42',\n                 'exception_only_padded2048_seed42', 'full_trace_label_only_seed42']\n\nfor eid in vota_ablation:\n    if eid in experiments:\n        exp = experiments[eid]\n        print(f\"\\n=== {eid} ===\")\n        print(f\"  status: {exp.get('status')}\")\n        print(f\"  hypothesis: {exp.get('hypothesis', '')[:200]}\")\n        print(f\"  metrics: {json.dumps(exp.get('metrics', {}))}\")\n        print(f\"  conclusion: {exp.get('conclusion')}\")\nPYEOF\n",
  "description": "Inspect VOTA ablation and exception sub-component experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_final-maintext-tables_20260523T191655",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 << 'PYEOF'\nimport json\n\nfilepath = \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study/d5f32b76-3066-49a9-b711-4657d91efad8/tool-results/mcp-agent-ml-research-read_registry-1779563834793.txt\"\n\nwith open(filepath, 'r') as f:\n    outer = json.load(f)\n\ninner = json.loads(outer['result'])\nexperiments = inner['data']['experiments']\n\n# Look at Qwen-7B seed42 canonical: exception_only, full_trace, no_trace, vota, ae_only, loop_only\n# Also check VOTA multi-component ablation experiments\nvota_ablation = ['vota_ae_only_seed42', 'vota_exception_only_seed42', 'vota_exception_only_seed42_v2',\n                 'vota_loop_only_seed42', 'vota_no_ae_seed42',\n                 'exc_message_only_seed42', 'exc_stacktrace_only_seed42', 'exc_type_only_seed42',\n                 'exception_only_padded2048_seed42', 'full_trace_label_only_seed42']\n\nfor eid in vota_ablation:\n    if eid in experiments:\n        exp = experiments[eid]\n        print(f\"\\n=== {eid} ===\")\n        print(f\"  status: {exp.get('status')}\")\n        print(f\"  hypothesis: {exp.get('hypothesis', '')[:200]}\")\n        print(f\"  metrics: {json.dumps(exp.get('metrics', {}))}\")\n        print(f\"  conclusion: {exp.get('conclusion')}\")\nPYEOF\n",
    "description": "Inspect VOTA ablation and exception sub-component experiments"
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-23T19:33:00.193592+00:00_

=== vota_ae_only_seed42 ===
  status: DONE
  hypothesis: VOTA component ablation: ae_only condition — only actual/expected values, no exception/loop compression (plan_003 sub-a)
  metrics: {"accuracy": 0.9992, "accuracy_ci": [0.9975, 1], "bootstrap_pairwise": {"ae_only_vs_no_trace": {"diff": 0.2479, "ci": [0.2235, 0.2731], "p_value": 0, "significant": true}, "ae_only_vs_exception_only": {"diff": 0.0008, "ci": [-0.0017, 0.0034], "p_value": 0.8002, "significant": false}, "ae_only_vs_vota": {"diff": 0.005, "ci": [0.0017, 0.0092], "p_value": 0.0046, "significant": true}}, "config": {"n_bootstrap": 10000, "seed": 42, "method": "paired_bootstrap"}}
  conclusion: success

=== vota_exception_only_seed42 ===
  status: DONE
  hypothesis: VOTA component ablation: exception_only condition — only exception summaries, no actual/expected or loop compression. Tests if [ERROR] events are the primary driver of VOTA's 99.2% accuracy (plan_003 
  metrics: {}
  conclusion: failed

=== vota_exception_only_seed42_v2 ===
  status: DONE
  hypothesis: VOTA component ablation: exception_only condition — retry with --gradient_checkpointing (v1 OOM at step 8). Tests if [ERROR] events are the primary driver of VOTA's 99.2% accuracy (plan_003 sub-b)
  metrics: {"accuracy": 0.9983, "majority_baseline": 0.7151, "lift": 0.2832, "n": 1190, "pass_precision": 1, "pass_recall": 0.998, "pass_f1": 0.999, "fail_precision": 0.994, "fail_recall": 1, "fail_f1": 0.997, "lift_vs_notrace": 0.2471, "lift_vs_notrace_ci_lower": 0.2227, "lift_vs_notrace_ci_upper": 0.2714, "lift_vs_fulltrace": 0.1807, "lift_vs_fulltrace_ci_lower": 0.1588, "lift_vs_fulltrace_ci_upper": 0.2034, "lift_vs_vota": 0.0067, "lift_vs_vota_ci_lower": 0.0017, "lift_vs_vota_ci_upper": 0.0126, "lift_vs_vota_pvalue": 0.01}
  conclusion: success

=== vota_loop_only_seed42 ===
  status: DONE
  hypothesis: VOTA component ablation: loop_only condition — only loop compression summaries, no actual/expected or exception. Tests loop behavioral pattern con
…[truncated 3773 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_final-maintext-tables_20260523T191655",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-23T19:33:00.193752+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nfilepath = \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study/d5f32b76-3066-49a9-b711-4657d91efad8/tool-results/mcp-agent-ml-research-read_registry-1779563834793.txt\"\n\nwith open(filepath, 'r') as f:\n    outer = json.load(f)\n\ninner = json.loads(outer['result'])\nexperiments = inner['data']['experiments']\n\n# Qwen-7B main ablation seed42 canonical\nqwen7b_main = [\n    'qwen7b_full_trace_seed123', 'qwen7b_full_trace_seed456', 'qwen7b_full_trace_seed456_v2',\n    'qwen7b_vota_seed123', 'qwen7b_vota_seed456',\n    'qwen7b_full_trace_label_only_seed123', 'qwen7b_full_trace_label_only_seed456',\n    'gradient_masking_qwen7b_seed42', 'gradient_masking_qwen7b_seed123', 'gradient_masking_qwen7b_seed456',\n    'qwen7b_full_trace_tail512_seed123', 'qwen7b_full_trace_tail512_seed42', 'qwen7b_full_trace_tail512_seed456',\n    'qwen7b_full_trace_head2048_seed42', 'qwen7b_full_trace_tail384_seed42',\n    'qwen7b_exception_only_dynamics_seed42', 'qwen7b_full_trace_dynamics_seed42',\n]\n\nfor eid in qwen7b_main:\n    if eid in experiments:\n        exp = experiments[eid]\n        print(f\"\\n=== {eid} ===\")\n        print(f\"  status: {exp.get('status')}\")\n        print(f\"  hypothesis: {exp.get('hypothesis', '')[:150]}\")\n        print(f\"  metrics: {json.dumps(exp.get('metrics', {}))}\")\n        print(f\"  conclusion: {exp.get('conclusion')}\")\nPYEOF\n",
  "description": "Inspect Qwen-7B supplementary experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_final-maintext-tables_20260523T191655",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 << 'PYEOF'\nimport json\n\nfilepath = \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study/d5f32b76-3066-49a9-b711-4657d91efad8/tool-results/mcp-agent-ml-research-read_registry-1779563834793.txt\"\n\nwith open(filepath, 'r') as f:\n    outer = json.load(f)\n\ninner = json.loads(outer['result'])\nexperiments = inner['data']['experiments']\n\n# Qwen-7B main ablation seed42 canonical\nqwen7b_main = [\n    'qwen7b_full_trace_seed123', 'qwen7b_full_trace_seed456', 'qwen7b_full_trace_seed456_v2',\n    'qwen7b_vota_seed123', 'qwen7b_vota_seed456',\n    'qwen7b_full_trace_label_only_seed123', 'qwen7b_full_trace_label_only_seed456',\n    'gradient_masking_qwen7b_seed42', 'gradient_masking_qwen7b_seed123', 'gradient_masking_qwen7b_seed456',\n    'qwen7b_full_trace_tail512_seed123', 'qwen7b_full_trace_tail512_seed42', 'qwen7b_full_trace_tail512_seed456',\n    'qwen7b_full_trace_head2048_seed42', 'qwen7b_full_trace_tail384_seed42',\n    'qwen7b_exception_only_dynamics_seed42', 'qwen7b_full_trace_dynamics_seed42',\n]\n\nfor eid in qwen7b_main:\n    if eid in experiments:\n        exp = experiments[eid]\n        print(f\"\\n=== {eid} ===\")\n        print(f\"  status: {exp.get('status')}\")\n        print(f\"  hypothesis: {exp.get('hypothesis', '')[:150]}\")\n        print(f\"  metrics: {json.dumps(exp.get('metrics', {}))}\")\n        print(f\"  conclusion: {exp.get('conclusion')}\")\nPYEOF\n",
    "description": "Inspect Qwen-7B supplementary experiments"
  }
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-23T19:33:00.193918+00:00_

=== qwen7b_full_trace_seed123 ===
  status: DONE
  hypothesis: Qwen-7B full_trace seed123 应在 ~81% 附近（与 seed42=81.76% 一致），为 MF-3 multi-seed 要求补齐 full_trace 方差估计。full_trace 是 C2 "more info hurts" claim 的锚点，单 seed 在 
  metrics: {"accuracy": 0.802, "ci_lower": 0.778, "ci_upper": 0.825, "majority_baseline": 0.715, "lift_pp": 8.7, "pass_precision": 0.88, "pass_recall": 0.84, "pass_f1": 0.86, "fail_precision": 0.64, "fail_recall": 0.7, "fail_f1": 0.67, "train_loss": 0.0415, "eval_loss": 0.0827}
  conclusion: success

=== qwen7b_full_trace_seed456 ===
  status: DONE
  hypothesis: Qwen-7B full_trace seed456 应在 ~81% 附近（与 seed42=81.76% 一致），为 MF-3 multi-seed 要求补齐 full_trace 方差估计。3-seed mean 将替换 Table 2 中的单 seed 值。
  metrics: {}
  conclusion: failed

=== qwen7b_full_trace_seed456_v2 ===
  status: DONE
  hypothesis: Qwen-7B full_trace seed456 应在 ~81% 附近（与 seed42=81.76%, seed123=80.20% 一致），为 MF-3 multi-seed 要求补齐 full_trace 方差估计。3-seed mean 将替换 Table 2 中的占位符。
  metrics: {"accuracy": 0.8235, "ci_lower": 0.8017, "ci_upper": 0.8454, "majority_baseline": 0.7151, "lift_pp": 10.84, "pass_precision": 0.8885, "pass_recall": 0.8613, "pass_f1": 0.8747, "fail_precision": 0.6767, "fail_recall": 0.7286, "fail_f1": 0.7017, "train_loss": 0.0416, "eval_loss": 0.0794}
  conclusion: success

=== qwen7b_vota_seed123 ===
  status: DONE
  hypothesis: Qwen-7B VOTA seed123 应在 84-92% 范围（与 vota_seed42_v4 一致），为 N5 reviewer concern 提供 VOTA 条件的方差估计
  metrics: {"accuracy": 0.9866, "accuracy_ci_lower": 0.979, "accuracy_ci_upper": 0.9925, "majority_baseline": 0.7151, "lift": 0.2714, "n": 1190, "pass_precision": 1, "pass_recall": 0.9812, "pass_f1": 0.9905, "fail_precision": 0.9549, "fail_recall": 1, "fail_f1": 0.9769, "train_loss": 0.0499, "eval_loss": 0.0864}
  conclusion: success

=== qwen7b_vota_seed456 ===
  status: DONE
  hypothesis: Qwen-7B VOTA seed456 应在 84-92% 范围（与 vota_seed42_v4 一致），为 N5 reviewer concern 提供 VOTA 条件的方差估计
  metrics: {"accuracy": 0.9908, "accuracy_ci_lower": 0.9849, "accuracy_ci_upper": 0.
…[truncated 5642 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_final-maintext-tables_20260523T191655",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-23T19:33:00.194083+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nfilepath = \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study/d5f32b76-3066-49a9-b711-4657d91efad8/tool-results/mcp-agent-ml-research-read_registry-1779563834793.txt\"\n\nwith open(filepath, 'r') as f:\n    outer = json.load(f)\n\ninner = json.loads(outer['result'])\nexperiments = inner['data']['experiments']\n\n# DeepSeek and Qwen-1.5B and CodeLlama cross-model experiments\ncross_model_ids = [\n    'deepseek_exception_only_seed42', 'deepseek_exception_only_seed123', 'deepseek_exception_only_seed123_v2',\n    'deepseek_exception_only_seed456',\n    'deepseek_full_trace_seed42', 'deepseek_full_trace_seed42_v2', 'deepseek_full_trace_seed42_v3',\n    'deepseek_full_trace_tail512_seed42', 'deepseek_full_trace_tail512_seed123', 'deepseek_full_trace_tail512_seed123_v2', \n    'deepseek_full_trace_tail512_seed456',\n    'deepseek_no_trace_seed42', 'deepseek_no_trace_seed123',\n    'deepseek_vota_seed42', 'deepseek_vota_seed123', 'deepseek_vota_seed456',\n    'deepseek_ae_only_seed42', 'deepseek_ae_only_seed123',\n    'deepseek_loop_only_seed42', 'deepseek_loop_only_seed123', 'deepseek_loop_only_seed456',\n    'deepseek_label_only_seed42',\n    # CodeLlama\n    'codellama13b_exception_only_seed42', 'codellama13b_exception_only_seed123', 'codellama13b_exception_only_seed456',\n    'codellama13b_full_trace_tail512_seed42', 'codellama13b_full_trace_tail512_seed123', 'codellama13b_full_trace_tail512_seed456',\n    'codellama13b_full_trace_tail1024_seed42', 'codellama13b_full_trace_tail2048_seed42',\n    'codellama13b_no_trace_seed42',\n    'codellama13b_vota_seed42', 'codellama13b_vota_seed123',\n    'codellama13b_ae_only_seed42', 'codellama13b_ae_only_seed123',\n    'codellama13b_loop_only_seed42', 'codellama13b_loop_only_seed123', 'codellama13b_loop_only_seed456',\n    'codellama13b_label_only_seed42', 'codellama13b_label_only_seed42_v2', 'codellama13b_label_only_seed123_v2',\n    # Qwen-1.5B\n    'qwen15b_exception_only_seed42', 'qwen15b_exception_only_seed123', 'qwen15b_exception_only_seed123_v2',\n    'qwen15b_exception_only_seed456',\n    'qwen15b_full_trace_seed42',\n    'qwen15b_full_trace_tail512_seed42', 'qwen15b_full_trace_tail512_seed123', 'qwen15b_full_trace_tail512_seed456',\n    'qwen15b_no_trace_seed42', 'qwen15b_no_trace_seed123', 'qwen15b_no_trace_seed456',\n    'qwen15b_vota_seed42', 'qwen15b_vota_seed123',\n    'qwen15b_ae_only_seed42', 'qwen15b_ae_only_seed123',\n    'qwen15b_loop_only_seed42', 'qwen15b_loop_only_seed123', 'qwen15b_loop_only_seed456',\n    'qwen15b_label_only_seed42', 'qwen15b_label_only_seed42_v2', 'qwen15b_label_only_seed123_v2', 'qwen15b_label_only_seed456_v2',\n]\n\nfor eid in cross_model_ids:\n    if eid in experiments:\n        exp = experiments[eid]\n        print(f\"\\n=== {eid} ===\")\n        print(f\"  status: {exp.get('status')}\")\n        m = exp.get('metrics', {})\n        # Only print key metrics\n        key_metrics = {k: v for k, v in m.items() if k in [\n            'accuracy', 'accuracy_ci', 'accuracy_ci_lower', 'accuracy_ci_upper', 'ci_lower', 'ci_upper', 'ci_95',\n            'majority_baseline', 'lift', 'n', 'pass_f1', 'fail_f1', 'seed_comparison', 'mean_accuracy', 'std'\n        ]}\n        print(f\"  key_metrics: {json.dumps(key_metrics)}\")\n        print(f\"  conclusion: {exp.get('conclusion')}\")\nPYEOF\n",
  "description": "Extract metrics for cross-model experiments (DeepSeek, Qwen-1.5B, CodeLlama)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_final-maintext-tables_20260523T191655",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 << 'PYEOF'\nimport json\n\nfilepath = \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study/d5f32b76-3066-49a9-b711-4657d91efad8/tool-results/mcp-agent-ml-research-read_registry-1779563834793.txt\"\n\nwith open(filepath, 'r') as f:\n    outer = json.load(f)\n\ninner = json.loads(outer['result'])\nexperiments = inner['data']['experiments']\n\n# DeepSeek and Qwen-1.5B and CodeLlama cross-model experiments\ncross_model_ids = [\n    'deepseek_exception_only_seed42', 'deepseek_exception_only_seed123', 'deepseek_exception_only_seed123_v2',\n    'deepseek_exception_only_seed456',\n    'deepseek_full_trace_seed42', 'deepseek_full_trace_seed42_v2', 'deepseek_full_trace_seed42_v3',\n    'deepseek_full_trace_tail512_seed42', 'deepseek_full_trace_tail512_seed123', 'deepseek_full_trace_tail512_seed123_v2', \n    'deepseek_full_trace_tail512_seed456',\n    'deepseek_no_trace_seed42', 'deepseek_no_trace_seed123',\n    'deepseek_vota_seed42', 'deepseek_vota_seed123', 'deepseek_vota_seed456',\n    'deepseek_ae_only_seed42', 'deepseek_ae_only_seed123',\n    'deepseek_loop_only_seed42', 'deepseek_loop_only_seed123', 'deepseek_loop_only_seed456',\n    'deepseek_label_only_seed42',\n    # CodeLlama\n    'codellama13b_exception_only_seed42', 'codellama13b_exception_only_seed123', 'codellama13b_exception_only_seed456',\n    'codellama13b_full_trace_tail512_seed42', 'codellama13b_full_trace_tail512_seed123', 'codellama13b_full_trace_tail512_seed456',\n    'codellama13b_full_trace_tail1024_seed42', 'codellama13b_full_trace_tail2048_seed42',\n    'codellama13b_no_trace_seed42',\n    'codellama13b_vota_seed42', 'codellama13b_vota_seed123',\n    'codellama13b_ae_only_seed42', 'codellama13b_ae_only_seed123',\n    'codellama13b_loop_only_seed42', 'codellama13b_loop_only_seed123', 'codellama13b_loop_only_seed456',\n    'codellama13b_label_only_seed42', 'codellama13b_label_only_seed42_v2', 'codellama13b_label_only_seed123_v2',\n    # Qwen-1.5B\n    'qwen15b_exception_only_seed42', 'qwen15b_exception_only_seed123', 'qwen15b_exception_only_seed123_v2',\n    'qwen15b_exception_only_seed456',\n    'qwen15b_full_trace_seed42',\n    'qwen15b_full_trace_tail512_seed42', 'qwen15b_full_trace_tail512_seed123', 'qwen15b_full_trace_tail512_seed456',\n    'qwen15b_no_trace_seed42', 'qwen15b_no_trace_seed123', 'qwen15b_no_trace_seed456',\n    'qwen15b_vota_seed42', 'qwen15b_vota_seed123',\n    'qwen15b_ae_only_seed42', 'qwen15b_ae_only_seed123',\n    'qwen15b_loop_only_seed42', 'qwen15b_loop_only_seed123', 'qwen15b_loop_only_seed456',\n    'qwen15b_label_only_seed42', 'qwen15b_label_only_seed42_v2', 'qwen15b_label_only_seed123_v2', 'qwen15b_label_only_seed456_v2',\n]\n\nfor eid in cross_model_ids:\n    if eid in experiments:\n        exp = experiments[eid]\n        print(f\"\\n=== {eid} ===\")\n        print(f\"  status: {exp.get('status')}\")\n        m = exp.get('metrics', {})\n        # Only print key metrics\n        key_metrics = {k: v for k, v in m.items() if k in [\n            'accuracy', 'accuracy_ci', 'accuracy_ci_lower', 'accuracy_ci_upper', 'ci_lower', 'ci_upper', 'ci_95',\n            'majority_baseline', 'lift', 'n', 'pass_f1', 'fail_f1', 'seed_comparison', 'mean_accuracy', 'std'\n        ]}\n        print(f\"  key_metrics: {json.dumps(key_metrics)}\")\n        print(f\"  conclusion: {exp.get('conclusion')}\")\nPYEOF\n",
    "description": "Extract metrics for cross-model experiments (DeepSeek, Qwen-1.5B, CodeLlama)"
  }
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-23T19:33:00.194301+00:00_

=== deepseek_exception_only_seed42 ===
  status: DONE
  key_metrics: {"accuracy": 0.9933, "majority_baseline": 0.7151, "lift": 0.2782, "n": 1190, "pass_f1": 0.9953, "fail_f1": 0.9883}
  conclusion: success

=== deepseek_exception_only_seed123 ===
  status: DONE
  key_metrics: {}
  conclusion: killed

=== deepseek_exception_only_seed123_v2 ===
  status: DONE
  key_metrics: {"accuracy": 0.995}
  conclusion: success

=== deepseek_exception_only_seed456 ===
  status: DONE
  key_metrics: {"accuracy": 0.9933, "majority_baseline": 0.7151, "lift": 0.2782, "n": 1190, "pass_f1": 0.9953, "fail_f1": 0.9883, "accuracy_ci": [0.9882, 0.9975], "seed_comparison": {"seed42_accuracy": 0.9933, "seed456_accuracy": 0.9933, "seed123_accuracy": 0.9109, "note": "seed42 and seed456 identical (99.33%); seed123 outlier (91.09%). 2/3 seeds robust."}}
  conclusion: success

=== deepseek_full_trace_seed42 ===
  status: DONE
  key_metrics: {"majority_baseline": 0.7151, "n": 1190}
  conclusion: negative

=== deepseek_full_trace_seed42_v2 ===
  status: DONE
  key_metrics: {}
  conclusion: killed

=== deepseek_full_trace_seed42_v3 ===
  status: DONE
  key_metrics: {"accuracy": 0.7916, "majority_baseline": 0.7151, "lift": 0.0765, "n": 1190, "pass_f1": 0.854, "fail_f1": 0.637, "accuracy_ci": [0.768, 0.813]}
  conclusion: success

=== deepseek_full_trace_tail512_seed42 ===
  status: DONE
  key_metrics: {"accuracy": 0.939, "accuracy_ci_lower": 0.926, "accuracy_ci_upper": 0.953, "majority_baseline": 0.715, "pass_f1": 0.96, "fail_f1": 0.9}
  conclusion: success

=== deepseek_full_trace_tail512_seed123 ===
  status: DONE
  key_metrics: {"seed_comparison": {"seed42_accuracy": 0.9361, "seed123_accuracy": "N/A - OOM crash"}}
  conclusion: failed

=== deepseek_full_trace_tail512_seed123_v2 ===
  status: DONE
  key_metrics: {"accuracy": 0.9504, "majority_baseline": 0.7151, "lift": 0.2353, "n": 1190, "pass_f1": 0.9649, "fail_f1": 0.9154, "accuracy_ci": [0.9387, 0.963]}
  conclusion: success

=== deepseek_full_tra
…[truncated 11273 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_final-maintext-tables_20260523T191655",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-23T19:33:00.194476+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nfilepath = \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study/d5f32b76-3066-49a9-b711-4657d91efad8/tool-results/mcp-agent-ml-research-read_registry-1779563834793.txt\"\n\nwith open(filepath, 'r') as f:\n    outer = json.load(f)\n\ninner = json.loads(outer['result'])\nexperiments = inner['data']['experiments']\n\n# nomarker experiments, ablation density/trace length, debugbench, fewshot, attention analysis\nremaining_ids = [\n    'exception_only_nomarker_seed42', 'exception_only_nomarker_seed123', 'exception_only_nomarker_seed456',\n    'codellama13b_nomarker_seed42', 'qwen15b_nomarker_seed42',\n    # trace length ablations (Qwen-7B)\n    'full_trace_256tok_seed42', 'full_trace_512tok_seed42', 'full_trace_1024tok_seed42', 'full_trace_2048tok_seed42',\n    'full_trace_tail256_seed42', 'full_trace_tail_256_seed42', 'full_trace_tail_512_seed42', 'full_trace_tail_1024_seed42',\n    'full_trace_tail_seed42', 'full_trace_tail256_seed42',\n    'deepseek_full_trace_tail256_seed42', 'deepseek_full_trace_tail384_seed42', \n    'deepseek_full_trace_tail1024_seed42', 'deepseek_full_trace_tail2048_seed42', 'deepseek_full_trace_head2048_seed42',\n    'codellama13b_full_trace_tail256_seed42', 'codellama13b_full_trace_tail384_seed42',\n    'codellama13b_full_trace_tail2048_seed42', 'codellama13b_full_trace_tail2048_seed42_v2', 'codellama13b_full_trace_tail2048_seed42_v3',\n    'codellama13b_full_trace_tail1024_seed42', 'codellama13b_full_trace_tail1024_seed42_v2', 'codellama13b_full_trace_tail1024_seed42_v3',\n    'codellama13b_full_trace_head2048_seed42',\n    'qwen15b_full_trace_tail256_seed42', 'qwen15b_full_trace_tail384_seed42',\n    'qwen15b_full_trace_tail1024_seed42', 'qwen15b_full_trace_tail2048_seed42', 'qwen15b_full_trace_head2048_seed42',\n    # debugbench, fewshot\n    'debugbench_exception_only_seed42', 'debugbench_no_trace_seed42', 'debugbench_vota_seed42', 'debugbench_exception_bug_fix',\n    'fewshot_gpt4o_exception_only_0shot', 'fewshot_gpt4o_exception_only_3shot', 'fewshot_gpt4o_no_trace_0shot',\n    'fewshot_gpt41_exception_only_0shot', 'fewshot_gpt41_exception_only_3shot', 'fewshot_gpt41_no_trace_0shot',\n    'fewshot_qwen7b_exception_only',\n    # attention / misc\n    'attention_gradient_analysis',\n    'zeroshot_codellama13b_exception_only', 'zeroshot_deepseek7b_exception_only',\n    'zeroshot_qwen15b_exception_only', 'zeroshot_qwen7b_exception_only',\n    'qwen1.5b_exception_only_seed42', 'qwen1.5b_full_trace_seed42', 'qwen1.5b_no_trace_seed42', 'qwen1.5b_vota_seed42',\n    'codellama_exception_only_seed42', 'codellama_no_trace_seed42', 'codellama_vota_seed42',\n    'eval_missing_predictions_batch', 'eval_missing_predictions_batch_v2',\n]\n\nfor eid in remaining_ids:\n    if eid in experiments:\n        exp = experiments[eid]\n        print(f\"\\n=== {eid} ===\")\n        print(f\"  status: {exp.get('status')}\")\n        print(f\"  hypothesis: {exp.get('hypothesis', '')[:150]}\")\n        print(f\"  metrics: {json.dumps(exp.get('metrics', {}))}\")\n        print(f\"  conclusion: {exp.get('conclusion')}\")\nPYEOF\n",
  "description": "Extract remaining experiments including nomarker, trace length, fewshot, debugbench"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_final-maintext-tables_20260523T191655",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 << 'PYEOF'\nimport json\n\nfilepath = \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study/d5f32b76-3066-49a9-b711-4657d91efad8/tool-results/mcp-agent-ml-research-read_registry-1779563834793.txt\"\n\nwith open(filepath, 'r') as f:\n    outer = json.load(f)\n\ninner = json.loads(outer['result'])\nexperiments = inner['data']['experiments']\n\n# nomarker experiments, ablation density/trace length, debugbench, fewshot, attention analysis\nremaining_ids = [\n    'exception_only_nomarker_seed42', 'exception_only_nomarker_seed123', 'exception_only_nomarker_seed456',\n    'codellama13b_nomarker_seed42', 'qwen15b_nomarker_seed42',\n    # trace length ablations (Qwen-7B)\n    'full_trace_256tok_seed42', 'full_trace_512tok_seed42', 'full_trace_1024tok_seed42', 'full_trace_2048tok_seed42',\n    'full_trace_tail256_seed42', 'full_trace_tail_256_seed42', 'full_trace_tail_512_seed42', 'full_trace_tail_1024_seed42',\n    'full_trace_tail_seed42', 'full_trace_tail256_seed42',\n    'deepseek_full_trace_tail256_seed42', 'deepseek_full_trace_tail384_seed42', \n    'deepseek_full_trace_tail1024_seed42', 'deepseek_full_trace_tail2048_seed42', 'deepseek_full_trace_head2048_seed42',\n    'codellama13b_full_trace_tail256_seed42', 'codellama13b_full_trace_tail384_seed42',\n    'codellama13b_full_trace_tail2048_seed42', 'codellama13b_full_trace_tail2048_seed42_v2', 'codellama13b_full_trace_tail2048_seed42_v3',\n    'codellama13b_full_trace_tail1024_seed42', 'codellama13b_full_trace_tail1024_seed42_v2', 'codellama13b_full_trace_tail1024_seed42_v3',\n    'codellama13b_full_trace_head2048_seed42',\n    'qwen15b_full_trace_tail256_seed42', 'qwen15b_full_trace_tail384_seed42',\n    'qwen15b_full_trace_tail1024_seed42', 'qwen15b_full_trace_tail2048_seed42', 'qwen15b_full_trace_head2048_seed42',\n    # debugbench, fewshot\n    'debugbench_exception_only_seed42', 'debugbench_no_trace_seed42', 'debugbench_vota_seed42', 'debugbench_exception_bug_fix',\n    'fewshot_gpt4o_exception_only_0shot', 'fewshot_gpt4o_exception_only_3shot', 'fewshot_gpt4o_no_trace_0shot',\n    'fewshot_gpt41_exception_only_0shot', 'fewshot_gpt41_exception_only_3shot', 'fewshot_gpt41_no_trace_0shot',\n    'fewshot_qwen7b_exception_only',\n    # attention / misc\n    'attention_gradient_analysis',\n    'zeroshot_codellama13b_exception_only', 'zeroshot_deepseek7b_exception_only',\n    'zeroshot_qwen15b_exception_only', 'zeroshot_qwen7b_exception_only',\n    'qwen1.5b_exception_only_seed42', 'qwen1.5b_full_trace_seed42', 'qwen1.5b_no_trace_seed42', 'qwen1.5b_vota_seed42',\n    'codellama_exception_only_seed42', 'codellama_no_trace_seed42', 'codellama_vota_seed42',\n    'eval_missing_predictions_batch', 'eval_missing_predictions_batch_v2',\n]\n\nfor eid in remaining_ids:\n    if eid in experiments:\n        exp = experiments[eid]\n        print(f\"\\n=== {eid} ===\")\n        print(f\"  status: {exp.get('status')}\")\n        print(f\"  hypothesis: {exp.get('hypothesis', '')[:150]}\")\n        print(f\"  metrics: {json.dumps(exp.get('metrics', {}))}\")\n        print(f\"  conclusion: {exp.get('conclusion')}\")\nPYEOF\n",
    "description": "Extract remaining experiments including nomarker, trace length, fewshot, debugbench"
  }
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-23T19:33:00.194724+00:00_

=== exception_only_nomarker_seed42 ===
  status: DONE
  hypothesis: Format marker ablation: removing [No exception data in trace] and [ERROR] prefix markers reduces accuracy by ~2pp, isolating semantic content contribu
  metrics: {"accuracy": 0.9655, "n": 1190, "accuracy_ci": [0.955, 0.976]}
  conclusion: success

=== exception_only_nomarker_seed123 ===
  status: DONE
  hypothesis: Seed robustness of nomarker ablation: format marker contribution (~2pp) is consistent across random seeds, not an artifact of specific LoRA initializa
  metrics: {"accuracy": 0.9832, "n": 1190, "ci_95": [0.9756, 0.9899], "pass_f1": 0.9882, "fail_f1": 0.9705, "pass_precision": 0.9882, "pass_recall": 0.9882, "fail_precision": 0.9705, "fail_recall": 0.9705, "lift_over_majority": 0.2681}
  conclusion: success

=== exception_only_nomarker_seed456 ===
  status: DONE
  hypothesis: Seed robustness of nomarker ablation: format marker contribution (~2pp) is consistent across random seeds, not an artifact of specific LoRA initializa
  metrics: {"accuracy": 0.9807, "n": 1190, "errors": 23, "ci_95": [0.9712, 0.9871], "pass_f1": 0.9865, "fail_f1": 0.9658, "pass_precision": 0.9836, "pass_recall": 0.9894, "fail_precision": 0.9731, "fail_recall": 0.9587, "lift_over_majority": 0.266}
  conclusion: success

=== codellama13b_nomarker_seed42 ===
  status: DONE
  hypothesis: Cross-architecture marker contribution: format markers ([No exception data in trace], [ERROR] prefix) contribute ~2pp on CodeLlama-13B as on Qwen fami
  metrics: {}
  conclusion: killed

=== qwen15b_nomarker_seed42 ===
  status: DONE
  hypothesis: Cross-scale nomarker validation: format marker contribution (~2pp at 7B) is consistent at 1.5B, confirming markers provide a small but architecture-an
  metrics: {"accuracy": 0.978, "n": 1190, "accuracy_ci": [0.97, 0.986], "majority_baseline": 0.715, "lift": 0.263, "pass_precision": 0.97, "pass_recall": 1, "pass_f1": 0.98, "fail_precision": 1, "fail_recall": 0.92, "fail_f1": 0.96}
  conclusion: s
…[truncated 21634 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_final-maintext-tables_20260523T191655",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-23T19:33:00.195340+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nfilepath = \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study/d5f32b76-3066-49a9-b711-4657d91efad8/tool-results/mcp-agent-ml-research-read_registry-1779563834793.txt\"\n\nwith open(filepath, 'r') as f:\n    outer = json.load(f)\n\ninner = json.loads(outer['result'])\nexperiments = inner['data']['experiments']\n\n# Check remaining experiments I haven't fully covered\nremaining = [\n    'deepseek_full_trace_tail256_seed42', 'deepseek_full_trace_tail384_seed42',\n    'codellama13b_full_trace_tail256_seed42', 'codellama13b_full_trace_tail384_seed42',\n    'codellama13b_full_trace_tail512_seed42',\n    'vota_exception_only_seed42_v2',  # already got\n    # check for seed42 canonical Qwen-7B experiments I may have missed\n    'full_trace_seed42', 'no_trace_seed42_v4', 'no_trace_seed42_v5',\n    # exception_only seed42 canonical\n]\n\n# also let's check all Qwen-7B VOTA seed42 canonical\ncanonical_qwen7b = {\n    'exception_only': 'exception_only_seed123',  # seed42 has same accuracy, use seed123 \n    'full_trace': 'full_trace_seed123',  # canonical 3-seed\n    'no_trace': 'no_trace_seed42_v5',  # canonical\n    'vota': 'vota_seed42_v4',  # canonical\n    'ae_only': 'ae_only_seed456',  # has comparison\n    'loop_only': 'loop_only_seed456',  # has comparison\n    'label_only': 'full_trace_label_only_seed42',\n}\n\n# Also look at the exception_only seed42 canonical\neid = 'exception_only_seed123'\nexp = experiments.get(eid, {})\nprint(f\"=== exception_only_seed123 (canonical Qwen-7B) ===\")\nprint(json.dumps(exp.get('metrics', {}), indent=2))\n\n# And check if there's a canonical seed42 for exception_only Qwen-7B\nprint(\"\\n\\nSearching for Qwen-7B exception_only seed42 canonical...\")\nfor eid in ['exception_only_seed42', 'vota_exception_only_seed42_v2']:\n    if eid in experiments:\n        exp = experiments[eid]\n        print(f\"\\n=== {eid} ===\")\n        print(json.dumps(exp.get('metrics', {}), indent=2))\n        print(f\"  conclusion: {exp.get('conclusion')}\")\nPYEOF\n",
  "description": "Check Qwen-7B canonical experiment metrics"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_final-maintext-tables_20260523T191655",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 << 'PYEOF'\nimport json\n\nfilepath = \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study/d5f32b76-3066-49a9-b711-4657d91efad8/tool-results/mcp-agent-ml-research-read_registry-1779563834793.txt\"\n\nwith open(filepath, 'r') as f:\n    outer = json.load(f)\n\ninner = json.loads(outer['result'])\nexperiments = inner['data']['experiments']\n\n# Check remaining experiments I haven't fully covered\nremaining = [\n    'deepseek_full_trace_tail256_seed42', 'deepseek_full_trace_tail384_seed42',\n    'codellama13b_full_trace_tail256_seed42', 'codellama13b_full_trace_tail384_seed42',\n    'codellama13b_full_trace_tail512_seed42',\n    'vota_exception_only_seed42_v2',  # already got\n    # check for seed42 canonical Qwen-7B experiments I may have missed\n    'full_trace_seed42', 'no_trace_seed42_v4', 'no_trace_seed42_v5',\n    # exception_only seed42 canonical\n]\n\n# also let's check all Qwen-7B VOTA seed42 canonical\ncanonical_qwen7b = {\n    'exception_only': 'exception_only_seed123',  # seed42 has same accuracy, use seed123 \n    'full_trace': 'full_trace_seed123',  # canonical 3-seed\n    'no_trace': 'no_trace_seed42_v5',  # canonical\n    'vota': 'vota_seed42_v4',  # canonical\n    'ae_only': 'ae_only_seed456',  # has comparison\n    'loop_only': 'loop_only_seed456',  # has comparison\n    'label_only': 'full_trace_label_only_seed42',\n}\n\n# Also look at the exception_only seed42 canonical\neid = 'exception_only_seed123'\nexp = experiments.get(eid, {})\nprint(f\"=== exception_only_seed123 (canonical Qwen-7B) ===\")\nprint(json.dumps(exp.get('metrics', {}), indent=2))\n\n# And check if there's a canonical seed42 for exception_only Qwen-7B\nprint(\"\\n\\nSearching for Qwen-7B exception_only seed42 canonical...\")\nfor eid in ['exception_only_seed42', 'vota_exception_only_seed42_v2']:\n    if eid in experiments:\n        exp = experiments[eid]\n        print(f\"\\n=== {eid} ===\")\n        print(json.dumps(exp.get('metrics', {}), indent=2))\n        print(f\"  conclusion: {exp.get('conclusion')}\")\nPYEOF\n",
    "description": "Check Qwen-7B canonical experiment metrics"
  }
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-23T19:33:00.195530+00:00_

=== exception_only_seed123 (canonical Qwen-7B) ===
{
  "accuracy": 0.9983,
  "accuracy_ci": [
    0.9958,
    1
  ],
  "majority_baseline": 0.7151,
  "lift": 0.2832,
  "n": 1190,
  "pass_precision": 1,
  "pass_recall": 0.9976,
  "pass_f1": 0.9988,
  "fail_precision": 0.9941,
  "fail_recall": 1,
  "fail_f1": 0.9971,
  "train_loss": 0.1096,
  "train_runtime_sec": 7507,
  "epochs": 3,
  "seed_comparison": {
    "seed42_accuracy": 0.9983,
    "seed456_accuracy": 0.9983,
    "seed123_accuracy": 0.9983,
    "max_diff": 0,
    "note": "identical accuracy to 4 decimal places across all 3 seeds (42/456/123); each has exactly 2/1190 errors; exception_only fully seed-robust"
  }
}


Searching for Qwen-7B exception_only seed42 canonical...

=== vota_exception_only_seed42_v2 ===
{
  "accuracy": 0.9983,
  "majority_baseline": 0.7151,
  "lift": 0.2832,
  "n": 1190,
  "pass_precision": 1,
  "pass_recall": 0.998,
  "pass_f1": 0.999,
  "fail_precision": 0.994,
  "fail_recall": 1,
  "fail_f1": 0.997,
  "lift_vs_notrace": 0.2471,
  "lift_vs_notrace_ci_lower": 0.2227,
  "lift_vs_notrace_ci_upper": 0.2714,
  "lift_vs_fulltrace": 0.1807,
  "lift_vs_fulltrace_ci_lower": 0.1588,
  "lift_vs_fulltrace_ci_upper": 0.2034,
  "lift_vs_vota": 0.0067,
  "lift_vs_vota_ci_lower": 0.0017,
  "lift_vs_vota_ci_upper": 0.0126,
  "lift_vs_vota_pvalue": 0.01
}
  conclusion: success

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_final-maintext-tables_20260523T191655",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-23T19:33:00.195804+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nfilepath = \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study/d5f32b76-3066-49a9-b711-4657d91efad8/tool-results/mcp-agent-ml-research-read_registry-1779563834793.txt\"\n\nwith open(filepath, 'r') as f:\n    outer = json.load(f)\n\ninner = json.loads(outer['result'])\nexperiments = inner['data']['experiments']\n\noutput_path = \"/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/_audit_registry_extract.txt\"\n\nlines = []\nlines.append(\"=\" * 100)\nlines.append(\"REGISTRY AUDIT EXTRACT — trace-verdict-study\")\nlines.append(\"Generated from: mcp-agent-ml-research-read_registry-1779563834793.txt\")\nlines.append(f\"Total experiments in registry: {len(experiments)}\")\nlines.append(\"=\" * 100)\nlines.append(\"\")\n\n# ============================================================================================\n# SECTION 1: TABLE 1 — MAIN CONDITION RESULTS (Qwen-7B canonical, all seeds)\n# ============================================================================================\nlines.append(\"=\" * 100)\nlines.append(\"SECTION 1: TABLE 1 CANDIDATES — Main SFT Conditions (Qwen2.5-Coder-7B-Instruct, n=1190)\")\nlines.append(\"=\" * 100)\nlines.append(\"\")\n\n# --- exception_only (Qwen-7B) ---\nlines.append(\"--- exception_only (Qwen-7B) ---\")\nlines.append(\"  Seed 42 accuracy: 0.9983 (from seed_comparison in exception_only_seed123)\")\nlines.append(\"  Seed 123 accuracy: 0.9983  | exp_id: exception_only_seed123\")\nlines.append(\"    accuracy_ci: [0.9958, 1.0]\")\nlines.append(\"    pass_precision: 1.0000  pass_recall: 0.9976  pass_f1: 0.9988\")\nlines.append(\"    fail_precision: 0.9941  fail_recall: 1.0000  fail_f1: 0.9971\")\nlines.append(\"    majority_baseline: 0.7151  lift: 0.2832  n: 1190\")\nlines.append(\"  Seed 456 accuracy: 0.9983  | exp_id: exception_only_seed456\")\nlines.append(\"    accuracy_ci: [0.9958, 1.0]  eval_loss: 0.4629  train_loss: 0.1087\")\nlines.append(\"  MEAN across 3 seeds: 0.9983 ± 0.0000 (all identical, max_diff=0)\")\nlines.append(\"  NOTE: each seed has exactly 2/1190 errors\")\nlines.append(\"\")\n\n# --- full_trace (Qwen-7B) ---\nlines.append(\"--- full_trace (Qwen-7B) ---\")\nlines.append(\"  Seed 123 accuracy: 0.7958  | exp_id: full_trace_seed123\")\nlines.append(\"    accuracy_ci_lower: 0.7714  accuracy_ci_upper: 0.8202\")\nlines.append(\"    pass_precision: 0.8753  pass_recall: 0.8331  pass_f1: 0.8537\")\nlines.append(\"    fail_precision: 0.6263  fail_recall: 0.7021  fail_f1: 0.6620\")\nlines.append(\"    majority_baseline: 0.7151  lift: 0.0807  n: 1190\")\nlines.append(\"  Seed 42 (v5) accuracy: 0.8176  | exp_id: full_trace_seed42_v5\")\nlines.append(\"    accuracy_ci_lower: 0.797  accuracy_ci_upper: 0.839\")\nlines.append(\"    pass_precision: 0.8774  pass_recall: 0.8660  pass_f1: 0.8717\")\nlines.append(\"    fail_precision: 0.6743  fail_recall: 0.6962  fail_f1: 0.6851\")\nlines.append(\"    lift: 0.1025  lift_vs_notrace: 0.0664  (CI: [0.0437, 0.0899])\")\nlines.append(\"    epoch_level: epoch1=0.8303 epoch2=0.7630 epoch3=0.8176 (non-monotonic)\")\nlines.append(\"  Seed 456 accuracy: 0.8050  | exp_id: full_trace_seed456\")\nlines.append(\"    accuracy_ci_lower: 0.7824  accuracy_ci_upper: 0.8269\")\nlines.append(\"    pass_f1: 0.8637  fail_f1: 0.6578\")\nlines.append(\"    lift: 0.0899\")\nlines.append(\"  Seed 123 (qwen7b_full_trace_seed123) accuracy: 0.8020  | exp_id: qwen7b_full_trace_seed123\")\nlines.append(\"    ci_lower: 0.778  ci_upper: 0.825  lift_pp: 8.7\")\nlines.append(\"  Seed 456 (v2) accuracy: 0.8235  | exp_id: qwen7b_full_trace_seed456_v2\")\nlines.append(\"    ci_lower: 0.8017  ci_upper: 0.8454  lift_pp: 10.84\")\nlines.append(\"  3-SEED MEAN (seed42=0.8176, seed123=0.8020, seed456=0.8235): ~0.814\")\nlines.append(\"\")\n\n# --- no_trace (Qwen-7B) ---\nlines.append(\"--- no_trace (Qwen-7B) ---\")\nlines.append(\"  Seed 42 (v4/v5) accuracy: 0.7513  | exp_id: no_trace_seed42_v5\")\nlines.append(\"    accuracy_ci_lower: 0.7277  accuracy_ci_upper: 0.7748\")\nlines.append(\"    pass_precision: 0.8776  pass_recall: 0.7579  pass_f1: 0.8134\")\nlines.append(\"    fail_precision: 0.5473  fail_recall: 0.7345  fail_f1: 0.6272\")\nlines.append(\"    majority_baseline: 0.7151  lift: 0.0361  (CI: [0.0042, 0.0706])\")\nlines.append(\"    epoch_level: epoch1=0.7429 epoch2=0.7630 epoch3=0.7513\")\nlines.append(\"  Seed 123 accuracy: 0.7908  | exp_id: no_trace_seed123\")\nlines.append(\"    pass_f1: 0.8523  fail_f1: 0.6581  n: 1190\")\nlines.append(\"  Seed 456 accuracy: 0.7504  | exp_id: no_trace_seed456\")\nlines.append(\"    accuracy_ci: [0.7235, 0.7748]  pass_f1: 0.8119  fail_f1: 0.6292\")\nlines.append(\"  3-SEED MEAN (seed42=0.7513, seed123=0.7908, seed456=0.7504): ~0.764\")\nlines.append(\"\")\n\n# --- VOTA (Qwen-7B) ---\nlines.append(\"--- VOTA (Qwen-7B) ---\")\nlines.append(\"  Seed 42 (v4) accuracy: 0.9563  | exp_id: vota_seed42_v4  [canonical v4]\")\nlines.append(\"    lift: 0.2412  lift_vs_notrace: 0.2050  (CI: [0.177, 0.234])\")\nlines.append(\"    pass_precision: 0.9440  pass_recall: 0.9980  pass_f1: 0.9700\")\nlines.append(\"    fail_precision: 0.9930  fail_recall: 0.8530  fail_f1: 0.9170\")\nlines.append(\"  Seed 42 (v5) accuracy: 0.9941  | exp_id: vota_seed42_v5  [note: diff script]\")\nlines.append(\"    pass_precision: 1.0000  pass_recall: 0.9918  pass_f1: 0.9959\")\nlines.append(\"    fail_precision: 0.9798  fail_recall: 1.0000  fail_f1: 0.9898  n: 1190\")\nlines.append(\"  Seed 123 accuracy: 0.9866  | exp_id: qwen7b_vota_seed123\")\nlines.append(\"    accuracy_ci_lower: 0.9790  accuracy_ci_upper: 0.9925  lift: 0.2714\")\nlines.append(\"    pass_f1: 0.9905  fail_f1: 0.9769\")\nlines.append(\"  Seed 456 accuracy: 0.9908  | exp_id: qwen7b_vota_seed456\")\nlines.append(\"    accuracy_ci_lower: 0.9849  accuracy_ci_upper: 0.9958  lift: 0.2756\")\nlines.append(\"    pass_f1: 0.9935  fail_f1: 0.9840\")\nlines.append(\"  Seed 456 v2 accuracy: 0.9908  | exp_id: vota_seed456_v2\")\nlines.append(\"    ci_95: [0.985, 0.996]  pass_f1: 0.9930  fail_f1: 0.9840\")\nlines.append(\"  3-SEED MEAN (seed42=0.9941, seed123=0.9866, seed456=0.9908): ~0.991\")\nlines.append(\"    [using v5 for seed42; note v4 gives 0.9563 — version discrepancy]\")\nlines.append(\"\")\n\n# --- ae_only (Qwen-7B) ---\nlines.append(\"--- ae_only (Qwen-7B) ---\")\nlines.append(\"  Seed 42 accuracy: 0.9992  | exp_id: vota_ae_only_seed42\")\nlines.append(\"    accuracy_ci: [0.9975, 1.0000]\")\nlines.append(\"    bootstrap vs no_trace: diff=0.2479 CI=[0.2235, 0.2731] p=0\")\nlines.append(\"    bootstrap vs exception_only: diff=0.0008 CI=[-0.0017, 0.0034] p=0.8002 (n.s.)\")\nlines.append(\"    bootstrap vs vota: diff=0.0050 CI=[0.0017, 0.0092] p=0.0046\")\nlines.append(\"  Seed 123 accuracy: 0.9908  | exp_id: ae_only_seed123\")\nlines.append(\"    pass_recall: 0.987  fail_recall: 1.0  n: 1190  lift: 0.2757\")\nlines.append(\"  Seed 456 accuracy: 0.9992  | exp_id: ae_only_seed456\")\nlines.append(\"    lift: 0.2841  n: 1190\")\nlines.append(\"    seed_comparison: seed42=0.9992 seed123=0.9908 seed456=0.9992 → mean=0.9964 ± 0.0049\")\nlines.append(\"  3-SEED MEAN: 0.9964 ± 0.0049\")\nlines.append(\"\")\n\n# --- loop_only (Qwen-7B) ---\nlines.append(\"--- loop_only (Qwen-7B) ---\")\nlines.append(\"  Seed 42 accuracy: 0.8563  | exp_id: vota_loop_only_seed42\")\nlines.append(\"    accuracy_ci: [0.8353, 0.8756]  lift: 0.1412\")\nlines.append(\"    pass_precision: 0.9239  pass_recall: 0.8707  pass_f1: 0.8966\")\nlines.append(\"    fail_precision: 0.7165  fail_recall: 0.8201  fail_f1: 0.7648\")\nlines.append(\"    bootstrap vs vota: diff=-0.1378 CI=[-0.1571, -0.1185] (sig)\")\nlines.append(\"  Seed 123 accuracy: 0.8588  | exp_id: loop_only_seed123\")\nlines.append(\"    accuracy_ci: [0.8403, 0.8773]  lift: 0.1437\")\nlines.append(\"    pass_f1: 0.8999  fail_f1: 0.7607\")\nlines.append(\"  Seed 456 accuracy: 0.8664  | exp_id: loop_only_seed456\")\nlines.append(\"    accuracy_ci: [0.8470, 0.8840]\")\nlines.append(\"    pass_f1: 0.9053  fail_f1: 0.7732\")\nlines.append(\"    seed_comparison: seed42=0.8563 seed123=0.8588 seed456=0.8664 → mean=0.8605 ± 0.0053\")\nlines.append(\"  3-SEED MEAN: 0.8605 ± 0.0053\")\nlines.append(\"\")\n\n# --- label_only / full_trace_label_only (Qwen-7B) ---\nlines.append(\"--- label_only / full_trace_label_only_loss (Qwen-7B) ---\")\nlines.append(\"  Seed 42 (full_trace, label_only_loss) accuracy: 0.8622  | exp_id: full_trace_label_only_seed42\")\nlines.append(\"    accuracy_ci_lower: 0.8437  accuracy_ci_upper: 0.8807  lift: 0.1471\")\nlines.append(\"    pass_f1: 0.9063  fail_f1: 0.7397  n: 1190\")\nlines.append(\"    lift_vs_notrace: 0.1109  CI: [0.0849, 0.1370]\")\nlines.append(\"    lift_vs_standard_fulltrace: 0.0445  CI: [0.0235, 0.0655]  p=0\")\nlines.append(\"  Seed 123 accuracy: 0.8689  | exp_id: qwen7b_full_trace_label_only_seed123\")\nlines.append(\"    accuracy_ci: [0.8496, 0.8874]  pass_f1: 0.9121  fail_f1: 0.7426  lift: 0.1538\")\nlines.append(\"  Seed 456 accuracy: 0.8470  | exp_id: qwen7b_full_trace_label_only_seed456\")\nlines.append(\"    accuracy_ci: [0.827, 0.866]  pass_f1: 0.9000  fail_f1: 0.7100  lift: 0.1319\")\nlines.append(\"  NOTE: standalone label_only seeds (no trace at all):\")\nlines.append(\"    label_only_seed123 accuracy: 0.8706  pass_f1: 0.915  fail_f1: 0.729\")\nlines.append(\"    label_only_seed456 accuracy: 0.8590  pass_f1: 0.905  fail_f1: 0.727\")\nlines.append(\"\")\n\nlines.append(\"\")\nlines.append(\"=\" * 100)\nlines.append(\"SECTION 2: CROSS-MODEL TABLE — All 4 Models × Main Conditions\")\nlines.append(\"=\" * 100)\nlines.append(\"\")\n\n# --- DeepSeek-Coder-6.7B ---\nlines.append(\"--- DeepSeek-Coder-6.7B ---\")\nlines.append(\"\")\nlines.append(\"  exception_only:\")\nlines.append(\"    Seed 42  accuracy: 0.9933  | exp_id: deepseek_exception_only_seed42\")\nlines.append(\"      pass_f1: 0.9953  fail_f1: 0.9883  n: 1190  lift: 0.2782\")\nlines.append(\"    Seed 123 accuracy: 0.9950  | exp_id: deepseek_exception_only_seed123_v2\")\nlines.append(\"    Seed 456 accuracy: 0.9933  | exp_id: deepseek_exception_only_seed456\")\nlines.append(\"      accuracy_ci: [0.9882, 0.9975]\")\nlines.append(\"      seed_comparison: seed42=0.9933 seed456=0.9933 seed123=0.9109 (outlier)\")\nlines.append(\"      NOTE: seed123 v1 was OOM-crash; seed123_v2 = 0.9950 (canonical)\")\nlines.append(\"    3-SEED MEAN (using v2 for seed123): ~0.994\")\nlines.append(\"\")\nlines.append(\"  full_trace:\")\nlines.append(\"    Seed 42 (v3) accuracy: 0.7916  | exp_id: deepseek_full_trace_seed42_v3\")\nlines.append(\"      accuracy_ci: [0.768, 0.813]  lift: 0.0765\")\nlines.append(\"      pass_f1: 0.854  fail_f1: 0.637  n: 1190\")\nlines.append(\"    (v1, v2 = killed/negative)\")\nlines.append(\"\")\nlines.append(\"  no_trace:\")\nlines.append(\"    Seed 42 accuracy: 0.7336  | exp_id: deepseek_no_trace_seed42\")\nlines.append(\"      accuracy_ci: [0.708, 0.757]  lift: 0.0185\")\nlines.append(\"      pass_f1: 0.8130  fail_f1: 0.5390  n: 1190\")\nlines.append(\"\")\nlines.append(\"  VOTA:\")\nlines.append(\"    Seed 42 accuracy: 0.8445  | exp_id: deepseek_vota_seed42  [early canonical]\")\nlines.append(\"      accuracy_ci: [0.826, 0.864]  lift: 0.1294\")\nlines.append(\"      pass_f1: 0.9020  fail_f1: 0.6250\")\nlines.append(\"    Seed 123 accuracy: 0.9916  | exp_id: deepseek_vota_seed123\")\nlines.append(\"      accuracy_ci_lower: 0.9857  accuracy_ci_upper: 0.9966\")\nlines.append(\"    Seed 456 accuracy: 0.9933  | exp_id: deepseek_vota_seed456\")\nlines.append(\"    NOTE: large seed variance — seed42 may be from different pipeline version\")\nlines.append(\"\")\nlines.append(\"  ae_only:\")\nlines.append(\"    Seed 42 accuracy: 0.9874  | exp_id: deepseek_ae_only_seed42\")\nlines.append(\"      accuracy_ci: [0.9807, 0.9933]  pass_f1: 0.9910  fail_f1: 0.9770\")\nlines.append(\"    Seed 123 accuracy: 0.9832  | exp_id: deepseek_ae_only_seed123\")\nlines.append(\"\")\nlines.append(\"  loop_only:\")\nlines.append(\"    Seed 42 accuracy: 0.8126  | exp_id: deepseek_loop_only_seed42\")\nlines.append(\"      accuracy_ci: [0.7908, 0.8345]\")\nlines.append(\"    Seed 123 accuracy: 0.8126  | exp_id: deepseek_loop_only_seed123\")\nlines.append(\"      accuracy_ci: [0.792, 0.834]\")\nlines.append(\"    Seed 456 accuracy: 0.784   | exp_id: deepseek_loop_only_seed456\")\nlines.append(\"      fail_f1: 0.63  majority_baseline: 0.715\")\nlines.append(\"\")\nlines.append(\"  label_only (full_trace_label_only_loss):\")\nlines.append(\"    Seed 42 accuracy: 0.285   | exp_id: deepseek_label_only_seed42  [COLLAPSED]\")\nlines.append(\"      accuracy_ci: [0.261, 0.308]  lift: -0.430\")\nlines.append(\"      pass_f1: 0.0  fail_f1: 0.44\")\nlines.append(\"\")\n\n# --- CodeLlama-13B ---\nlines.append(\"--- CodeLlama-13B ---\")\nlines.append(\"\")\nlines.append(\"  exception_only:\")\nlines.append(\"    Seed 42  accuracy: 0.9983  | exp_id: codellama13b_exception_only_seed42\")\nlines.append(\"      accuracy_ci: [0.9958, 1.000]  pass_f1: 0.9988  fail_f1: 0.9971\")\nlines.append(\"    Seed 123 accuracy: 1.0000  | exp_id: codellama13b_exception_only_seed123\")\nlines.append(\"      pass_f1: 1.0  fail_f1: 1.0  n: 1190\")\nlines.append(\"    Seed 456 accuracy: 0.9983  | exp_id: codellama13b_exception_only_seed456\")\nlines.append(\"      pass_f1: 0.9988  fail_f1: 0.9971  n: 1190\")\nlines.append(\"    3-SEED MEAN: 0.9989\")\nlines.append(\"\")\nlines.append(\"  full_trace (canonical tail512, label_only_loss):\")\nlines.append(\"    Seed 42  accuracy: 0.9824  | exp_id: codellama13b_full_trace_tail512_seed42\")\nlines.append(\"      accuracy_ci: [0.9748, 0.9899]  lift: 0.2672  pass_f1: 0.9878  fail_f1: 0.9680\")\nlines.append(\"    Seed 123 accuracy: 0.9824  | exp_id: codellama13b_full_trace_tail512_seed123\")\nlines.append(\"      accuracy_ci: [0.9748, 0.9899]\")\nlines.append(\"    Seed 456 accuracy: 0.9824  | exp_id: codellama13b_full_trace_tail512_seed456\")\nlines.append(\"      NOTE: all 3 seeds identical at 0.9824\")\nlines.append(\"    NOTE: full-seq loss at tail2048 collapsed (0.296); label_only_loss v3 at tail1024 = 0.9824 epoch1\")\nlines.append(\"\")\nlines.append(\"  no_trace:\")\nlines.append(\"    Seed 42 accuracy: 0.7650  | exp_id: codellama13b_no_trace_seed42\")\nlines.append(\"      accuracy_ci: [0.738, 0.787]  lift: 0.050\")\nlines.append(\"      pass_f1: 0.840  fail_f1: 0.590  n: 1190\")\nlines.append(\"\")\nlines.append(\"  VOTA:\")\nlines.append(\"    Seed 42  accuracy: 0.9857  | exp_id: codellama13b_vota_seed42\")\nlines.append(\"      accuracy_ci: [0.9790, 0.9916]  pass_f1: 0.9900  fail_f1: 0.9748\")\nlines.append(\"    Seed 123 accuracy: 0.9891  | exp_id: codellama13b_vota_seed123\")\nlines.append(\"      accuracy_ci: [0.9832, 0.9941]  pass_f1: 0.9924  fail_f1: 0.9809  n: 1190  lift: 0.2739\")\nlines.append(\"\")\nlines.append(\"  ae_only:\")\nlines.append(\"    Seed 42  accuracy: 0.9908  | exp_id: codellama13b_ae_only_seed42\")\nlines.append(\"      accuracy_ci: [0.9849, 0.9958]  pass_f1: 0.9935  fail_f1: 0.9840\")\nlines.append(\"    Seed 123 accuracy: 0.9908  | exp_id: codellama13b_ae_only_seed123\")\nlines.append(\"      accuracy_ci: [0.9849, 0.9958]  pass_f1: 0.9930  fail_f1: 0.9840\")\nlines.append(\"\")\nlines.append(\"  loop_only:\")\nlines.append(\"    Seed 42  accuracy: 0.7706  | exp_id: codellama13b_loop_only_seed42\")\nlines.append(\"      accuracy_ci: [0.7487, 0.7941]  lift: 0.0555  pass_f1: 0.820  fail_f1: 0.670\")\nlines.append(\"    Seed 123 accuracy: 0.7605  | exp_id: codellama13b_loop_only_seed123\")\nlines.append(\"      accuracy_ci: [0.7387, 0.7857]  pass_f1: 0.8078  fail_f1: 0.6823  lift: 0.0454\")\nlines.append(\"    Seed 456 accuracy: 0.7908  | exp_id: codellama13b_loop_only_seed456\")\nlines.append(\"      pass_f1: 0.843  fail_f1: 0.688  n: 1190  lift: 0.0757\")\nlines.append(\"\")\nlines.append(\"  label_only (full_trace_label_only_loss):\")\nlines.append(\"    Seed 42 (v2) accuracy: 0.2849  | exp_id: codellama13b_label_only_seed42_v2  [COLLAPSED]\")\nlines.append(\"      accuracy_ci: [0.2613, 0.3084]  pass_f1: 0.0  fail_f1: 0.4434\")\nlines.append(\"    Seed 123 (v2) accuracy: 'collapsed' | exp_id: codellama13b_label_only_seed123_v2\")\nlines.append(\"\")\n\n# --- Qwen-1.5B ---\nlines.append(\"--- Qwen2.5-Coder-1.5B ---\")\nlines.append(\"\")\nlines.append(\"  exception_only:\")\nlines.append(\"    Seed 42  accuracy: 0.9983  | exp_id: qwen15b_exception_only_seed42\")\nlines.append(\"      accuracy_ci: [0.9958, 1.000]  lift: 0.283  pass_f1: 0.9988  fail_f1: 0.9971\")\nlines.append(\"    Seed 123 accuracy: 0.9983  | exp_id: qwen15b_exception_only_seed123_v2\")\nlines.append(\"      accuracy_ci: [0.9958, 1.000]\")\nlines.append(\"    Seed 456 accuracy: 0.9983  | exp_id: qwen15b_exception_only_seed456\")\nlines.append(\"      seed_comparison: all 3 seeds identical — fully seed-robust\")\nlines.append(\"    3-SEED MEAN: 0.9983 ± 0.0000\")\nlines.append(\"\")\nlines.append(\"  full_trace:\")\nlines.append(\"    Seed 42 (full_trace, no trunc) accuracy: 0.7706  | exp_id: qwen15b_full_trace_seed42\")\nlines.append(\"    Seed 42 (tail512) accuracy: 0.956   | exp_id: qwen15b_full_trace_tail512_seed42\")\nlines.append(\"      accuracy_ci: [0.945, 0.968]  pass_f1: 0.970  fail_f1: 0.920\")\nlines.append(\"    Seed 123 (tail512) accuracy: 0.9765  | exp_id: qwen15b_full_trace_tail512_seed123\")\nlines.append(\"      accuracy_ci: [0.9681, 0.9849]  lift: 0.2613\")\nlines.append(\"    Seed 456 (tail512) accuracy: 0.9672  | exp_id: qwen15b_full_trace_tail512_seed456\")\nlines.append(\"      accuracy_ci: [0.9563, 0.9773]  lift: 0.2521\")\nlines.append(\"\")\nlines.append(\"  no_trace:\")\nlines.append(\"    Seed 42  accuracy: 0.6731  | exp_id: qwen15b_no_trace_seed42\")\nlines.append(\"      pass_f1: 0.7527  fail_f1: 0.518  n: 1190\")\nlines.append(\"    Seed 123 accuracy: 0.7588  | exp_id: qwen15b_no_trace_seed123\")\nlines.append(\"      accuracy_ci: [0.7328, 0.7824]  lift: 0.0437\")\nlines.append(\"      pass_f1: 0.8323  fail_f1: 0.571\")\nlines.append(\"    Seed 456 accuracy: 0.7387  | exp_id: qwen15b_no_trace_seed456\")\nlines.append(\"      pass_f1: 0.8195  fail_f1: 0.5266\")\nlines.append(\"\")\nlines.append(\"  VOTA:\")\nlines.append(\"    Seed 42  accuracy: 0.9958  | exp_id: qwen15b_vota_seed42\")\nlines.append(\"      pass_f1: 0.9971  fail_f1: 0.9926  n: 1190\")\nlines.append(\"    Seed 123 accuracy: 0.9950  | exp_id: qwen15b_vota_seed123\")\nlines.append(\"      ci_95: [0.9908, 0.9983]  pass_f1: 0.9965  fail_f1: 0.9912\")\nlines.append(\"\")\nlines.append(\"  ae_only:\")\nlines.append(\"    Seed 42  accuracy: 0.9908  | exp_id: qwen15b_ae_only_seed42\")\nlines.append(\"      accuracy_ci: [0.9849, 0.9958]  lift: 0.2756  pass_f1: 0.9935  fail_f1: 0.9840\")\nlines.append(\"    Seed 123 accuracy: 0.9857  | exp_id: qwen15b_ae_only_seed123\")\nlines.append(\"      majority_baseline: 0.715  fail_f1: 0.975\")\nlines.append(\"\")\nlines.append(\"  loop_only:\")\nlines.append(\"    Seed 42  accuracy: 0.7832  | exp_id: qwen15b_loop_only_seed42\")\nlines.append(\"      pass_f1: 0.8526  fail_f1: 0.5905\")\nlines.append(\"    Seed 123 accuracy: 0.8109  | exp_id: qwen15b_loop_only_seed123\")\nlines.append(\"      pass_f1: 0.8737  fail_f1: 0.6244\")\nlines.append(\"    Seed 456 accuracy: 0.7920  | exp_id: qwen15b_loop_only_seed456\")\nlines.append(\"      ci_95: [0.768, 0.813]  majority_baseline: 0.715\")\nlines.append(\"\")\nlines.append(\"  label_only (full_trace_label_only_loss):\")\nlines.append(\"    Seed 42 (v2) accuracy: 0.7890  | exp_id: qwen15b_label_only_seed42_v2\")\nlines.append(\"      accuracy_ci: [0.766, 0.812]  pass_f1: 0.860  fail_f1: 0.570\")\nlines.append(\"    Seed 123 (v2) accuracy: 0.8134  | exp_id: qwen15b_label_only_seed123_v2\")\nlines.append(\"      accuracy_ci: [0.7924, 0.8345]  pass_f1: 0.878  fail_f1: 0.602\")\nlines.append(\"    Seed 456 (v2) accuracy: 0.8252  | exp_id: qwen15b_label_only_seed456_v2\")\nlines.append(\"      pass_f1: 0.885  fail_f1: 0.639\")\nlines.append(\"\")\n\nlines.append(\"\")\nlines.append(\"=\" * 100)\nlines.append(\"SECTION 3: TABLE 2 — ABLATION CONDITIONS (Qwen-7B, seed42 canonical)\")\nlines.append(\"=\" * 100)\nlines.append(\"\")\n\nlines.append(\"--- Ablation: VOTA component decomposition ---\")\nlines.append(\"  ae_only (Qwen-7B seed42) accuracy: 0.9992  CI:[0.9975, 1.0]  | exp_id: vota_ae_only_seed42\")\nlines.append(\"  exception_only (Qwen-7B) accuracy: 0.9983  CI:[0.9958, 1.0]  | exp_id: vota_exception_only_seed42_v2\")\nlines.append(\"  loop_only (Qwen-7B seed42) accuracy: 0.8563  CI:[0.8353, 0.8756]  | exp_id: vota_loop_only_seed42\")\nlines.append(\"  VOTA-no-ae (Qwen-7B seed42) accuracy: 0.9940  CI:[0.989, 0.998]  | exp_id: vota_no_ae_seed42\")\nlines.append(\"    lift_vs_notrace: 0.2430  CI:[0.218, 0.268]\")\nlines.append(\"\")\nlines.append(\"--- Ablation: Exception sub-component ---\")\nlines.append(\"  exc_message_only_seed42: accuracy=0.9950 CI:[0.991, 0.998] | exp_id: exc_message_only_seed42\")\nlines.append(\"    pass_f1: 0.9960  fail_f1: 0.9910  n: 1190\")\nlines.append(\"  exc_stacktrace_only_seed42: accuracy=0.9980 CI:[0.996, 1.0] | exp_id: exc_stacktrace_only_seed42\")\nlines.append(\"    pass_f1: 0.9990  fail_f1: 0.9970  n: 1190\")\nlines.append(\"  exc_type_only_seed42: no metrics (None conclusion)\")\nlines.append(\"\")\nlines.append(\"--- Ablation: full_trace with label_only_loss ---\")\nlines.append(\"  full_trace_label_only_seed42: accuracy=0.8622 CI:[0.8437, 0.8807] | exp_id: full_trace_label_only_seed42\")\nlines.append(\"    lift_vs_notrace: 0.1109 CI:[0.0849, 0.1370]\")\nlines.append(\"    lift_vs_standard_fulltrace: +0.0445 CI:[0.0235, 0.0655] p=0\")\nlines.append(\"    pass_f1: 0.9063  fail_f1: 0.7397\")\nlines.append(\"\")\nlines.append(\"--- Ablation: nomarker (Qwen-7B) ---\")\nlines.append(\"  Seed 42  accuracy: 0.9655  CI:[0.955, 0.976] | exp_id: exception_only_nomarker_seed42\")\nlines.append(\"  Seed 123 accuracy: 0.9832  CI:[0.9756, 0.9899] | exp_id: exception_only_nomarker_seed123\")\nlines.append(\"    pass_f1: 0.9882  fail_f1: 0.9705  lift_over_majority: 0.2681\")\nlines.append(\"  Seed 456 accuracy: 0.9807  CI:[0.9712, 0.9871] | exp_id: exception_only_nomarker_seed456\")\nlines.append(\"    errors: 23  pass_f1: 0.9865  fail_f1: 0.9658  lift_over_majority: 0.2660\")\nlines.append(\"  NOTE: vs exception_only (0.9983), marker contributes ~1.5-3.3pp\")\nlines.append(\"\")\nlines.append(\"--- Ablation: nomarker (Qwen-1.5B) ---\")\nlines.append(\"  qwen15b_nomarker_seed42: accuracy=0.9780 CI:[0.970, 0.986]  | exp_id: qwen15b_nomarker_seed42\")\nlines.append(\"    majority_baseline: 0.715  lift: 0.263\")\nlines.append(\"    pass_precision: 0.970  pass_recall: 1.0  pass_f1: 0.980\")\nlines.append(\"    fail_precision: 1.0    fail_recall: 0.92  fail_f1: 0.960\")\nlines.append(\"\")\nlines.append(\"--- Ablation: exception_only padded to 2048 tokens ---\")\nlines.append(\"  exception_only_padded2048_seed42: accuracy=0.9983  | exp_id: exception_only_padded2048_seed42\")\nlines.append(\"    (identical to unpadded — padding does not degrade accuracy)\")\nlines.append(\"\")\n\nlines.append(\"\")\nlines.append(\"=\" * 100)\nlines.append(\"SECTION 4: TABLE 3 — DENSITY DECOMPOSITION (gradient masking, tail truncation)\")\nlines.append(\"=\" * 100)\nlines.append(\"\")\n\nlines.append(\"--- Gradient Masking (99.8% masked, exception_only) ---\")\nlines.append(\"  Qwen-7B Seed 42 accuracy: 0.9933 CI:[0.9882, 0.9975] | exp_id: gradient_masking_qwen7b_seed42\")\nlines.append(\"    NOTE: metrics empty (None conclusion) — see seed123/456 for canonical\")\nlines.append(\"  Qwen-7B Seed 123 accuracy: 0.9933 CI:[0.9882, 0.9975] | exp_id: gradient_masking_qwen7b_seed123\")\nlines.append(\"    pass_f1: 0.9953  fail_f1: 0.9883  lift: 0.2782  train_loss: 1.6031  eval_loss: 0.0381\")\nlines.append(\"  Qwen-7B Seed 456 accuracy: 0.9933 CI:[0.9882, 0.9975] | exp_id: gradient_masking_qwen7b_seed456\")\nlines.append(\"    (identical to seed123)\")\nlines.append(\"  3-SEED MEAN: 0.9933 ± 0.0000  dilution_pct: N/A (vs baseline 0.9983 → dilution ~0.5%)\")\nlines.append(\"\")\nlines.append(\"  DeepSeek-6.7B Seed 42 accuracy: 0.9933 CI:[0.9882, 0.9975] | exp_id: deepseek_gradient_masking_seed42\")\nlines.append(\"    dilution_pct: N/A  baseline_accuracy: 99.39%  lift: 0.278  eval_loss: 0.0529\")\nlines.append(\"    majority_baseline: 0.715\")\nlines.append(\"  DeepSeek-6.7B Seed 123 accuracy: 0.9395 | exp_id: deepseek_gradient_masking_seed123\")\nlines.append(\"    pass_precision: 0.924  pass_recall: 0.998  pass_f1: 0.959\")\nlines.append(\"    fail_precision: 0.993  fail_recall: 0.794  fail_f1: 0.882\")\nlines.append(\"    conclusion: negative (fell below 98.5% threshold)\")\nlines.append(\"\")\nlines.append(\"  CodeLlama-13B Seed 42 accuracy: 1.0000 | exp_id: codellama_gradient_masking_seed42\")\nlines.append(\"    accuracy_ci_lower: 1.0  accuracy_ci_upper: 1.0\")\nlines.append(\"    eval_loss: 0.0625  dilution_pct: -0.11  pass_f1: 1.0  fail_f1: 1.0  n_test: 1190\")\nlines.append(\"    baseline_accuracy: 99.89%\")\nlines.append(\"\")\n\nlines.append(\"--- Tail Truncation Budget Curve (Qwen-7B) ---\")\nlines.append(\"  tail-256 (full_trace_tail_256_seed42):  accuracy=0.7748  CI:[0.7496, 0.7975]  pass_f1: 0.8333  fail_f1: 0.6528\")\nlines.append(\"  tail-384 (qwen7b_full_trace_tail384_seed42): accuracy=0.798  CI:[0.776, 0.821]  pass_f1: 0.85  fail_f1: 0.68\")\nlines.append(\"  tail-512 (full_trace_tail_512_seed42):  accuracy=0.9360  CI:[0.922, 0.950]   pass_f1: 0.950  fail_f1: 0.890\")\nlines.append(\"  tail-512 Seed 123 (qwen7b_full_trace_tail512_seed123): accuracy=0.9597 CI:[0.9487, 0.9706]\")\nlines.append(\"  tail-512 Seed 456 (qwen7b_full_trace_tail512_seed456): accuracy=0.9765 CI:[0.9681, 0.9849]\")\nlines.append(\"  tail-1024 (full_trace_tail_1024_seed42): accuracy=0.9647  CI:[0.9546, 0.9748]  pass_f1: 0.9753  fail_f1: 0.9381\")\nlines.append(\"  tail-2048 (full_trace_tail_seed42):     accuracy=0.9730  CI:[0.964, 0.982]    pass_f1: 0.980  fail_f1: 0.950\")\nlines.append(\"  head-2048 (qwen7b_full_trace_head2048_seed42): accuracy=0.8160 (epoch1 best)\")\nlines.append(\"    pass_f1_epoch1: 0.87  fail_f1_epoch1: 0.686\")\nlines.append(\"\")\nlines.append(\"--- Tail Truncation Budget Curve (DeepSeek-6.7B) ---\")\nlines.append(\"  tail-256 (deepseek_full_trace_tail256_seed42):  accuracy=0.7639  CI:[0.7403, 0.7874]  pass_f1: 0.8424  fail_f1: 0.5293\")\nlines.append(\"  tail-384 (deepseek_full_trace_tail384_seed42):  accuracy=0.8070  CI:[0.786, 0.829]    pass_f1: 0.87  fail_f1: 0.60\")\nlines.append(\"  tail-512 (deepseek_full_trace_tail512_seed42):  accuracy=0.9390  CI:[0.926, 0.953]    pass_f1: 0.960  fail_f1: 0.900\")\nlines.append(\"  tail-512 Seed 123 (v2): accuracy=0.9504  CI:[0.9387, 0.9630]\")\nlines.append(\"  tail-512 Seed 456: accuracy=0.9605  CI:[0.9496, 0.9714]\")\nlines.append(\"  tail-1024 (deepseek_full_trace_tail1024_seed42): accuracy=0.9647 CI:[0.9538, 0.9748]  pass_f1: 0.976  fail_f1: 0.936\")\nlines.append(\"  tail-2048 (deepseek_full_trace_tail2048_seed42): accuracy=0.9496 CI:[0.937, 0.962]    pass_f1: 0.965  fail_f1: 0.913\")\nlines.append(\"  head-2048 (deepseek_full_trace_head2048_seed42): accuracy=0.7870 CI:[0.765, 0.810]    pass_f1: 0.850  fail_f1: 0.620\")\nlines.append(\"\")\nlines.append(\"--- Tail Truncation Budget Curve (CodeLlama-13B) ---\")\nlines.append(\"  tail-256 (codellama13b_full_trace_tail256_seed42): accuracy=0.779  CI:[0.757, 0.803]  pass_f1: 0.843  fail_f1: 0.626\")\nlines.append(\"  tail-384 (codellama13b_full_trace_tail384_seed42): accuracy=0.827  CI:[0.807, 0.847]  pass_f1: 0.887  fail_f1: 0.630\")\nlines.append(\"    NOTE: label_only_loss used; conclusion=negative (lower than expected)\")\nlines.append(\"  tail-512 (codellama13b_full_trace_tail512_seed42): accuracy=0.9824 CI:[0.9748, 0.9899]\")\nlines.append(\"    pass_f1: 0.9878  fail_f1: 0.9680  lift: 0.2672  (all 3 seeds identical)\")\nlines.append(\"  tail-1024 (v3, label_only_loss): accuracy_epoch1=0.9824 accuracy_epoch3=0.9756  best_epoch=1\")\nlines.append(\"    pass_f1_epoch1: 0.988  fail_f1_epoch1: 0.968\")\nlines.append(\"  head-2048 (codellama13b_full_trace_head2048_seed42): accuracy=0.7992  CI:[0.7765, 0.8227]\")\nlines.append(\"    pass_f1: 0.8602  fail_f1: 0.6438  lift: 0.084\")\nlines.append(\"\")\nlines.append(\"--- Tail Truncation Budget Curve (Qwen-1.5B) ---\")\nlines.append(\"  tail-256 (qwen15b_full_trace_tail256_seed42):  accuracy=0.7260  CI:[0.700, 0.753]  lift_over_majority: 0.011 (near-0)\")\nlines.append(\"  tail-384 (qwen15b_full_trace_tail384_seed42):  accuracy=0.7361  CI:[0.7101, 0.7622]  lift: 0.021\")\nlines.append(\"  tail-512 (qwen15b_full_trace_tail512_seed42):  accuracy=0.9560  CI:[0.945, 0.968]\")\nlines.append(\"  tail-1024 (qwen15b_full_trace_tail1024_seed42): accuracy=0.966   CI:[0.955, 0.976]   pass_f1: 0.98  fail_f1: 0.94\")\nlines.append(\"  tail-2048 (qwen15b_full_trace_tail2048_seed42): accuracy=0.979   CI:[0.9706, 0.9874]  pass_f1: 0.986  fail_f1: 0.962\")\nlines.append(\"  head-2048 (qwen15b_full_trace_head2048_seed42): accuracy=0.7529  CI:[0.7286, 0.7782]  pass_f1: 0.835  fail_f1: 0.508\")\nlines.append(\"\")\n\nlines.append(\"\")\nlines.append(\"=\" * 100)\nlines.append(\"SECTION 5: REGEX AND MAJORITY BASELINES\")\nlines.append(\"=\" * 100)\nlines.append(\"\")\n\nlines.append(\"--- Regex Baseline (marker condition) ---\")\nlines.append(\"  exp_id: regex_baseline_analysis  n=1190\")\nlines.append(\"  B1 (ERROR presence):   0.9345\")\nlines.append(\"  B2 (Traceback):        0.7151\")\nlines.append(\"  B3 (any keyword):      0.9345\")\nlines.append(\"  B4 (exception type):   0.9361\")\nlines.append(\"  B5 (format marker):    0.9933  ← best regex, McNemar p=0.041 vs SFT\")\nlines.append(\"  B6 (error count ≥2):   0.9202\")\nlines.append(\"  SFT exception_only:    0.9983\")\nlines.append(\"  Best regex gap vs SFT: -0.0622 (B5 at 99.33%, SFT at 99.83%)\")\nlines.append(\"\")\nlines.append(\"--- Regex Baseline (nomarker condition) ---\")\nlines.append(\"  exp_id: regex_nomarker_baseline  n=1190\")\nlines.append(\"  B5_marker_acc:   0.9933  (original with marker)\")\nlines.append(\"  B5_nomarker_acc: 0.2849  (drops 70.84pp without marker)\")\nlines.append(\"  B5_delta_pp:     -70.84\")\nlines.append(\"  B1_marker_acc:   0.9345\")\nlines.append(\"  B1_nomarker_acc: 0.7151\")\nlines.append(\"  B4_marker_acc:   0.9361\")\nlines.append(\"  B4_nomarker_acc: 0.9361  (unchanged — exception type is format-independent)\")\nlines.append(\"  B5b_nomarker_acc: 0.9345  (alternative regex without marker dependency)\")\nlines.append(\"\")\nlines.append(\"--- Majority Baseline (from experiment metrics) ---\")\nlines.append(\"  majority_baseline across experiments: 0.7151 (standard HumanEval/MBPP split)\")\nlines.append(\"  DebugBench majority_baseline: 0.5141  (50/50 pass/fail)\")\nlines.append(\"  Cross-HE2MBPP majority_baseline: 0.6902\")\nlines.append(\"\")\n\nlines.append(\"\")\nlines.append(\"=\" * 100)\nlines.append(\"SECTION 6: CALIBRATION (ECE / Brier Score)\")\nlines.append(\"=\" * 100)\nlines.append(\"\")\n\nlines.append(\"--- Qwen-7B calibration across conditions (exp_id: calibration_analysis_seed42, n=1190) ---\")\nlines.append(\"  no_trace:\")\nlines.append(\"    ECE: 0.171476  MCE: 0.475643  Brier: 0.197152  accuracy: 0.751261\")\nlines.append(\"  full_trace:\")\nlines.append(\"    ECE: 0.095817  MCE: 0.249061  Brier: 0.143924  accuracy: 0.817647\")\nlines.append(\"  label_only:\")\nlines.append(\"    ECE: 0.110686  MCE: 0.417124  Brier: 0.120144  accuracy: 0.862185\")\nlines.append(\"  loop_only:\")\nlines.append(\"    ECE: 0.083085  MCE: 0.183406  Brier: 0.118335  accuracy: 0.856303\")\nlines.append(\"  ae_only:\")\nlines.append(\"    ECE: 0.000415  MCE: 0.000415  Brier: 0.000847  accuracy: 0.99916\")\nlines.append(\"  exception_only:\")\nlines.append(\"    ECE: 0.002717  MCE: 0.835484  Brier: 0.001311  accuracy: 0.998319\")\nlines.append(\"  vota:\")\nlines.append(\"    ECE: 0.005410  MCE: 0.622459  Brier: 0.005234  accuracy: 0.994118\")\nlines.append(\"\")\nlines.append(\"--- Cross-model calibration (exp_id: cross_model_calibration_eval, exception_only, n=1190) ---\")\nlines.append(\"  Qwen-7B:\")\nlines.append(\"    ECE: 0.0027  MCE: 0.8355  Brier: 0.0013  accuracy: 0.9983\")\nlines.append(\"  Qwen-1.5B:\")\nlines.append(\"    ECE: 0.0020  MCE: 0.7549  Brier: 0.0013  accuracy: 0.9983\")\nlines.append(\"  CodeLlama-13B:\")\nlines.append(\"    ECE: 0.0020  MCE: 0.0411  Brier: 0.0013  accuracy: 0.9983\")\nlines.append(\"  DeepSeek-6.7B:\")\nlines.append(\"    ECE: 0.0064  MCE: 0.7756  Brier: 0.0061  accuracy: 0.9933\")\nlines.append(\"  ALL: ECE < 0.007, Brier < 0.007 — universally well-calibrated across architectures\")\nlines.append(\"\")\n\nlines.append(\"\")\nlines.append(\"=\" * 100)\nlines.append(\"SECTION 7: CROSS-DATASET GENERALIZATION\")\nlines.append(\"=\" * 100)\nlines.append(\"\")\n\nlines.append(\"--- HE→MBPP (train HumanEval, test MBPP) ---\")\nlines.append(\"  exception_only (exp_id: cross_he2mbpp_exception_only_seed42):\")\nlines.append(\"    accuracy: 0.9941  majority_baseline: 0.6902  lift: 0.3040\")\nlines.append(\"    pass_f1: 0.9957  fail_f1: 0.9906\")\nlines.append(\"    pass_precision: 0.9980  pass_recall: 0.9936\")\nlines.append(\"    fail_precision: 0.9858  fail_recall: 0.9955\")\nlines.append(\"  no_trace (exp_id: cross_he2mbpp_no_trace_seed42):\")\nlines.append(\"    accuracy: 0.7056  majority_baseline: 0.6902  lift: 0.0155\")\nlines.append(\"    pass_f1: 0.8074  fail_f1: 0.3756\")\nlines.append(\"    pass_precision: 0.7360  pass_recall: 0.8941\")\nlines.append(\"    fail_precision: 0.5478  fail_recall: 0.2857\")\nlines.append(\"\")\nlines.append(\"--- MBPP→HE (train MBPP, test HumanEval) ---\")\nlines.append(\"  exception_only (exp_id: cross_mbpp2he_exception_only_seed42): status=DONE, no metrics in spec\")\nlines.append(\"  no_trace (exp_id: cross_mbpp2he_no_trace_seed42): status=DONE, no metrics in spec\")\nlines.append(\"\")\nlines.append(\"--- Cross-dataset nomarker ablation (HE→MBPP, nomarker) ---\")\nlines.append(\"  exp_id: nomarker_cross_he2mbpp_exception_only\")\nlines.append(\"  accuracy: 0.9546  (vs marker 0.9941 → delta = -0.0395)\")\nlines.append(\"  pass_f1: 0.9662  fail_f1: 0.9309\")\nlines.append(\"  pass_precision: 0.9943  pass_recall: 0.9396\")\nlines.append(\"  fail_precision: 0.8801  fail_recall: 0.9879\")\nlines.append(\"  eval_loss: 1.09  train_loss: 0.247\")\nlines.append(\"  NOTE: even without markers, cross-dataset accuracy ~95.5% (strong generalization)\")\nlines.append(\"\")\n\nlines.append(\"\")\nlines.append(\"=\" * 100)\nlines.append(\"SECTION 8: OUT-OF-DISTRIBUTION (DebugBench)\")\nlines.append(\"=\" * 100)\nlines.append(\"\")\n\nlines.append(\"  DebugBench exception_only (exp_id: debugbench_exception_only_seed42, n=426):\")\nlines.append(\"    accuracy: 1.0000  CI_wilson:[0.9914, 1.0]  majority_baseline: 0.5141  lift: 0.4859\")\nlines.append(\"    pass_f1: 1.0  fail_f1: 1.0  (zero errors)\")\nlines.append(\"\")\nlines.append(\"  DebugBench VOTA (exp_id: debugbench_vota_seed42, n=426):\")\nlines.append(\"    accuracy: 0.9977  errors: 1  CI:[0.993, 1.0]  majority_baseline: 0.5141  lift: 0.4836\")\nlines.append(\"    pass_f1: 1.0  fail_f1: 1.0\")\nlines.append(\"\")\nlines.append(\"  DebugBench no_trace (exp_id: debugbench_no_trace_seed42):\")\nlines.append(\"    accuracy: 0.9671  majority_baseline: 0.5141  lift: 0.4531\")\nlines.append(\"    pass_f1: 0.967  fail_f1: 0.967\")\nlines.append(\"    CI: [0.948, 0.984]\")\nlines.append(\"  NOTE: no_trace lift is higher on DebugBench because 50/50 class balance\")\nlines.append(\"\")\n\nlines.append(\"\")\nlines.append(\"=\" * 100)\nlines.append(\"SECTION 9: FRONTIER LLM COMPARISON (GPT-4o, GPT-4.1, zero-shot Qwen-7B)\")\nlines.append(\"=\" * 100)\nlines.append(\"\")\n\nlines.append(\"  GPT-4o 0-shot exception_only (exp_id: fewshot_gpt4o_exception_only_0shot):\")\nlines.append(\"    accuracy: 0.8798  fail_f1: 0.8228\")\nlines.append(\"  GPT-4o 3-shot exception_only (exp_id: fewshot_gpt4o_exception_only_3shot):\")\nlines.append(\"    accuracy: 0.8681  fail_f1: 0.7995  (3-shot worse than 0-shot)\")\nlines.append(\"  GPT-4o 0-shot no_trace (exp_id: fewshot_gpt4o_no_trace_0shot):\")\nlines.append(\"    accuracy: 0.8445  fail_f1: 0.7543\")\nlines.append(\"\")\nlines.append(\"  GPT-4.1 0-shot exception_only (exp_id: fewshot_gpt41_exception_only_0shot):\")\nlines.append(\"    accuracy: 0.8218  fail_f1: 0.7452\")\nlines.append(\"  GPT-4.1 3-shot exception_only (exp_id: fewshot_gpt41_exception_only_3shot):\")\nlines.append(\"    accuracy: 0.8193  fail_f1: 0.7413\")\nlines.append(\"  GPT-4.1 0-shot no_trace (exp_id: fewshot_gpt41_no_trace_0shot):\")\nlines.append(\"    accuracy: 0.7731  fail_f1: 0.6608\")\nlines.append(\"\")\nlines.append(\"  Qwen-7B 0-shot exception_only (exp_id: zeroshot_qwen7b_exception_only):\")\nlines.append(\"    accuracy: 0.8908  CI:[0.8731, 0.9076]  pass_f1: 0.9276  fail_f1: 0.7774  n: 1190\")\nlines.append(\"  Qwen-7B 3-shot exception_only (exp_id: fewshot_qwen7b_exception_only):\")\nlines.append(\"    accuracy: 0.9084  CI:[0.8908, 0.9244]  pass_f1: 0.9368  fail_f1: 0.8336  n: 1190\")\nlines.append(\"  → SFT Qwen-7B exception_only: 0.9983  (gap vs 0-shot: +10.75pp)\")\nlines.append(\"\")\nlines.append(\"  DeepSeek-6.7B 0-shot (exp_id: zeroshot_deepseek7b_exception_only):\")\nlines.append(\"    accuracy: 0.9059  CI:[0.8899, 0.9218]  pass_f1: 0.9313  fail_f1: 0.8507  n: 1190\")\nlines.append(\"  Qwen-1.5B 0-shot (exp_id: zeroshot_qwen15b_exception_only):\")\nlines.append(\"    accuracy: 0.9345  CI:[0.9202, 0.9479]  pass_f1: 0.9690  fail_f1: 0.8730  n: 1190  unknown: 24\")\nlines.append(\"  CodeLlama-13B 0-shot (exp_id: zeroshot_codellama13b_exception_only):\")\nlines.append(\"    accuracy: 0.5101  CI:[0.4824, 0.5395]  pass_f1: 0.5187  fail_f1: 0.5146  n: 1190  unknown: 30\")\nlines.append(\"    NOTE: near-random, heavy bias toward fail\")\nlines.append(\"\")\n\nlines.append(\"\")\nlines.append(\"=\" * 100)\nlines.append(\"SECTION 10: LEARNING DYNAMICS (step-level, Qwen-7B)\")\nlines.append(\"=\" * 100)\nlines.append(\"\")\n\nlines.append(\"  exception_only dynamics (exp_id: qwen7b_exception_only_dynamics_seed42):\")\nlines.append(\"    step50:  0.9933  step100: 0.9933  step150: 0.9933\")\nlines.append(\"    step200: 0.9983  step250: 0.9983  step300: 0.9983\")\nlines.append(\"    step350: 0.9983  step400: 0.9983  step444: 0.9983\")\nlines.append(\"    saturation_step: 200  final_loss: 0.0329  pass_f1: 0.9988  fail_f1: 0.9971\")\nlines.append(\"\")\nlines.append(\"  full_trace (label_only_loss) dynamics (exp_id: qwen7b_full_trace_dynamics_seed42):\")\nlines.append(\"    step50:  0.8739  step100: 0.821  step150: 0.857\")\nlines.append(\"    step200: 0.866   step250: 0.874  step300: 0.849\")\nlines.append(\"    step350: 0.888   step400: 0.857  step444: 0.882\")\nlines.append(\"    best_step: 350  best_acc: 0.8882  final_loss: 0.0085\")\nlines.append(\"    NOTE: non-monotonic, no saturation (vs exception_only which saturates at step 200)\")\nlines.append(\"\")\n\nlines.append(\"\")\nlines.append(\"=\" * 100)\nlines.append(\"SECTION 11: MISC / COVERAGE NOTES\")\nlines.append(\"=\" * 100)\nlines.append(\"\")\n\nlines.append(\"  attention_gradient_analysis: DONE, no numeric metrics stored\")\nlines.append(\"\")\nlines.append(\"  Qwen-1.5B (earlier alias qwen1.5b_*): all killed — use qwen15b_* experiments\")\nlines.append(\"  CodeLlama (earlier alias codellama_*): all killed — use codellama13b_* experiments\")\nlines.append(\"\")\nlines.append(\"  cross_mbpp2he_exception_only_seed42: DONE, metrics NOT stored in registry\")\nlines.append(\"  cross_mbpp2he_no_trace_seed42: DONE, metrics NOT stored in registry\")\nlines.append(\"\")\nlines.append(\"  Seed-42 canonical for Qwen-7B exception_only NOT separately recorded;\")\nlines.append(\"    accuracy confirmed 0.9983 via seed_comparison fields in seed123 and seed456 records\")\nlines.append(\"\")\nlines.append(\"  codellama_gradient_masking_seed42: accuracy=1.0000 dilution_pct=-0.11 (better than baseline)\")\nlines.append(\"\")\nlines.append(\"  deepseek_gradient_masking summary:\")\nlines.append(\"    seed42: accuracy=0.9933 (success) | seed123: accuracy=0.9395 (negative — below 98.5% threshold)\")\nlines.append(\"\")\n\nlines.append(\"=\" * 100)\nlines.append(\"END OF REGISTRY AUDIT EXTRACT\")\nlines.append(\"=\" * 100)\n\noutput = \"\\n\".join(lines)\nwith open(output_path, 'w') as f:\n    f.write(output)\n\nprint(f\"Written {len(output)} chars / {len(lines)} lines to {output_path}\")\nPYEOF\n",
  "description": "Compile comprehensive audit extract and write to artifacts file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_final-maintext-tables_20260523T191655",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 << 'PYEOF'\nimport json\n\nfilepath = \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study/d5f32b76-3066-49a9-b711-4657d91efad8/tool-results/mcp-agent-ml-research-read_registry-1779563834793.txt\"\n\nwith open(filepath, 'r') as f:\n    outer = json.load(f)\n\ninner = json.loads(outer['result'])\nexperiments = inner['data']['experiments']\n\noutput_path = \"/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/_audit_registry_extract.txt\"\n\nlines = []\nlines.append(\"=\" * 100)\nlines.append(\"REGISTRY AUDIT EXTRACT — trace-verdict-study\")\nlines.append(\"Generated from: mcp-agent-ml-research-read_registry-1779563834793.txt\")\nlines.append(f\"Total experiments in registry: {len(experiments)}\")\nlines.append(\"=\" * 100)\nlines.append(\"\")\n\n# ============================================================================================\n# SECTION 1: TABLE 1 — MAIN CONDITION RESULTS (Qwen-7B canonical, all seeds)\n# ============================================================================================\nlines.append(\"=\" * 100)\nlines.append(\"SECTION 1: TABLE 1 CANDIDATES — Main SFT Conditions (Qwen2.5-Coder-7B-Instruct, n=1190)\")\nlines.append(\"=\" * 100)\nlines.append(\"\")\n\n# --- exception_only (Qwen-7B) ---\nlines.append(\"--- exception_only (Qwen-7B) ---\")\nlines.append(\"  Seed 42 accuracy: 0.9983 (from seed_comparison in exception_only_seed123)\")\nlines.append(\"  Seed 123 accuracy: 0.9983  | exp_id: exception_only_seed123\")\nlines.append(\"    accuracy_ci: [0.9958, 1.0]\")\nlines.append(\"    pass_precision: 1.0000  pass_recall: 0.9976  pass_f1: 0.9988\")\nlines.append(\"    fail_precision: 0.9941  fail_recall: 1.0000  fail_f1: 0.9971\")\nlines.append(\"    majority_baseline: 0.7151  lift: 0.2832  n: 1190\")\nlines.append(\"  Seed 456 accuracy: 0.9983  | exp_id: exception_only_seed456\")\nlines.append(\"    accuracy_ci: [0.9958, 1.0]  eval_loss: 0.4629  train_loss: 0.1087\")\nlines.append(\"  MEAN across 3 seeds: 0.9983 ± 0.0000 (all identical, max_diff=0)\")\nlines.append(\"  NOTE: each seed has exactly 2/1190 errors\")\nlines.append(\"\")\n\n# --- full_trace (Qwen-7B) ---\nlines.append(\"--- full_trace (Qwen-7B) ---\")\nlines.append(\"  Seed 123 accuracy: 0.7958  | exp_id: full_trace_seed123\")\nlines.append(\"    accuracy_ci_lower: 0.7714  accuracy_ci_upper: 0.8202\")\nlines.append(\"    pass_precision: 0.8753  pass_recall: 0.8331  pass_f1: 0.8537\")\nlines.append(\"    fail_precision: 0.6263  fail_recall: 0.7021  fail_f1: 0.6620\")\nlines.append(\"    majority_baseline: 0.7151  lift: 0.0807  n: 1190\")\nlines.append(\"  Seed 42 (v5) accuracy: 0.8176  | exp_id: full_trace_seed42_v5\")\nlines.append(\"    accuracy_ci_lower: 0.797  accuracy_ci_upper: 0.839\")\nlines.append(\"    pass_precision: 0.8774  pass_recall: 0.8660  pass_f1: 0.8717\")\nlines.append(\"    fail_precision: 0.6743  fail_recall: 0.6962  fail_f1: 0.6851\")\nlines.append(\"    lift: 0.1025  lift_vs_notrace: 0.0664  (CI: [0.0437, 0.0899])\")\nlines.append(\"    epoch_level: epoch1=0.8303 epoch2=0.7630 epoch3=0.8176 (non-monotonic)\")\nlines.append(\"  Seed 456 accuracy: 0.8050  | exp_id: full_trace_seed456\")\nlines.append(\"    accuracy_ci_lower: 0.7824  accuracy_ci_upper: 0.8269\")\nlines.append(\"    pass_f1: 0.8637  fail_f1: 0.6578\")\nlines.append(\"    lift: 0.0899\")\nlines.append(\"  Seed 123 (qwen7b_full_trace_seed123) accuracy: 0.8020  | exp_id: qwen7b_full_trace_seed123\")\nlines.append(\"    ci_lower: 0.778  ci_upper: 0.825  lift_pp: 8.7\")\nlines.append(\"  Seed 456 (v2) accuracy: 0.8235  | exp_id: qwen7b_full_trace_seed456_v2\")\nlines.append(\"    ci_lower: 0.8017  ci_upper: 0.8454  lift_pp: 10.84\")\nlines.append(\"  3-SEED MEAN (seed42=0.8176, seed123=0.8020, seed456=0.8235): ~0.814\")\nlines.append(\"\")\n\n# --- no_trace (Qwen-7B) ---\nlines.append(\"--- no_trace (Qwen-7B) ---\")\nlines.append(\"  Seed 42 (v4/v5) accuracy: 0.7513  | exp_id: no_trace_seed42_v5\")\nlines.append(\"    accuracy_ci_lower: 0.7277  accuracy_ci_upper: 0.7748\")\nlines.append(\"    pass_precision: 0.8776  pass_recall: 0.7579  pass_f1: 0.8134\")\nlines.append(\"    fail_precision: 0.5473  fail_recall: 0.7345  fail_f1: 0.6272\")\nlines.append(\"    majority_baseline: 0.7151  lift: 0.0361  (CI: [0.0042, 0.0706])\")\nlines.append(\"    epoch_level: epoch1=0.7429 epoch2=0.7630 epoch3=0.7513\")\nlines.append(\"  Seed 123 accuracy: 0.7908  | exp_id: no_trace_seed123\")\nlines.append(\"    pass_f1: 0.8523  fail_f1: 0.6581  n: 1190\")\nlines.append(\"  Seed 456 accuracy: 0.7504  | exp_id: no_trace_seed456\")\nlines.append(\"    accuracy_ci: [0.7235, 0.7748]  pass_f1: 0.8119  fail_f1: 0.6292\")\nlines.append(\"  3-SEED MEAN (seed42=0.7513, seed123=0.7908, seed456=0.7504): ~0.764\")\nlines.append(\"\")\n\n# --- VOTA (Qwen-7B) ---\nlines.append(\"--- VOTA (Qwen-7B) ---\")\nlines.append(\"  Seed 42 (v4) accuracy: 0.9563  | exp_id: vota_seed42_v4  [canonical v4]\")\nlines.append(\"    lift: 0.2412  lift_vs_notrace: 0.2050  (CI: [0.177, 0.234])\")\nlines.append(\"    pass_precision: 0.9440  pass_recall: 0.9980  pass_f1: 0.9700\")\nlines.append(\"    fail_precision: 0.9930  fail_recall: 0.8530  fail_f1: 0.9170\")\nlines.append(\"  Seed 42 (v5) accuracy: 0.9941  | exp_id: vota_seed42_v5  [note: diff script]\")\nlines.append(\"    pass_precision: 1.0000  pass_recall: 0.9918  pass_f1: 0.9959\")\nlines.append(\"    fail_precision: 0.9798  fail_recall: 1.0000  fail_f1: 0.9898  n: 1190\")\nlines.append(\"  Seed 123 accuracy: 0.9866  | exp_id: qwen7b_vota_seed123\")\nlines.append(\"    accuracy_ci_lower: 0.9790  accuracy_ci_upper: 0.9925  lift: 0.2714\")\nlines.append(\"    pass_f1: 0.9905  fail_f1: 0.9769\")\nlines.append(\"  Seed 456 accuracy: 0.9908  | exp_id: qwen7b_vota_seed456\")\nlines.append(\"    accuracy_ci_lower: 0.9849  accuracy_ci_upper: 0.9958  lift: 0.2756\")\nlines.append(\"    pass_f1: 0.9935  fail_f1: 0.9840\")\nlines.append(\"  Seed 456 v2 accuracy: 0.9908  | exp_id: vota_seed456_v2\")\nlines.append(\"    ci_95: [0.985, 0.996]  pass_f1: 0.9930  fail_f1: 0.9840\")\nlines.append(\"  3-SEED MEAN (seed42=0.9941, seed123=0.9866, seed456=0.9908): ~0.991\")\nlines.append(\"    [using v5 for seed42; note v4 gives 0.9563 — version discrepancy]\")\nlines.append(\"\")\n\n# --- ae_only (Qwen-7B) ---\nlines.append(\"--- ae_only (Qwen-7B) ---\")\nlines.append(\"  Seed 42 accuracy: 0.9992  | exp_id: vota_ae_only_seed42\")\nlines.append(\"    accuracy_ci: [0.9975, 1.0000]\")\nlines.append(\"    bootstrap vs no_trace: diff=0.2479 CI=[0.2235, 0.2731] p=0\")\nlines.append(\"    bootstrap vs exception_only: diff=0.0008 CI=[-0.0017, 0.0034] p=0.8002 (n.s.)\")\nlines.append(\"    bootstrap vs vota: diff=0.0050 CI=[0.0017, 0.0092] p=0.0046\")\nlines.append(\"  Seed 123 accuracy: 0.9908  | exp_id: ae_only_seed123\")\nlines.append(\"    pass_recall: 0.987  fail_recall: 1.0  n: 1190  lift: 0.2757\")\nlines.append(\"  Seed 456 accuracy: 0.9992  | exp_id: ae_only_seed456\")\nlines.append(\"    lift: 0.2841  n: 1190\")\nlines.append(\"    seed_comparison: seed42=0.9992 seed123=0.9908 seed456=0.9992 → mean=0.9964 ± 0.0049\")\nlines.append(\"  3-SEED MEAN: 0.9964 ± 0.0049\")\nlines.append(\"\")\n\n# --- loop_only (Qwen-7B) ---\nlines.append(\"--- loop_only (Qwen-7B) ---\")\nlines.append(\"  Seed 42 accuracy: 0.8563  | exp_id: vota_loop_only_seed42\")\nlines.append(\"    accuracy_ci: [0.8353, 0.8756]  lift: 0.1412\")\nlines.append(\"    pass_precision: 0.9239  pass_recall: 0.8707  pass_f1: 0.8966\")\nlines.append(\"    fail_precision: 0.7165  fail_recall: 0.8201  fail_f1: 0.7648\")\nlines.append(\"    bootstrap vs vota: diff=-0.1378 CI=[-0.1571, -0.1185] (sig)\")\nlines.append(\"  Seed 123 accuracy: 0.8588  | exp_id: loop_only_seed123\")\nlines.append(\"    accuracy_ci: [0.8403, 0.8773]  lift: 0.1437\")\nlines.append(\"    pass_f1: 0.8999  fail_f1: 0.7607\")\nlines.append(\"  Seed 456 accuracy: 0.8664  | exp_id: loop_only_seed456\")\nlines.append(\"    accuracy_ci: [0.8470, 0.8840]\")\nlines.append(\"    pass_f1: 0.9053  fail_f1: 0.7732\")\nlines.append(\"    seed_comparison: seed42=0.8563 seed123=0.8588 seed456=0.8664 → mean=0.8605 ± 0.0053\")\nlines.append(\"  3-SEED MEAN: 0.8605 ± 0.0053\")\nlines.append(\"\")\n\n# --- label_only / full_trace_label_only (Qwen-7B) ---\nlines.append(\"--- label_only / full_trace_label_only_loss (Qwen-7B) ---\")\nlines.append(\"  Seed 42 (full_trace, label_only_loss) accuracy: 0.8622  | exp_id: full_trace_label_only_seed42\")\nlines.append(\"    accuracy_ci_lower: 0.8437  accuracy_ci_upper: 0.8807  lift: 0.1471\")\nlines.append(\"    pass_f1: 0.9063  fail_f1: 0.7397  n: 1190\")\nlines.append(\"    lift_vs_notrace: 0.1109  CI: [0.0849, 0.1370]\")\nlines.append(\"    lift_vs_standard_fulltrace: 0.0445  CI: [0.0235, 0.0655]  p=0\")\nlines.append(\"  Seed 123 accuracy: 0.8689  | exp_id: qwen7b_full_trace_label_only_seed123\")\nlines.append(\"    accuracy_ci: [0.8496, 0.8874]  pass_f1: 0.9121  fail_f1: 0.7426  lift: 0.1538\")\nlines.append(\"  Seed 456 accuracy: 0.8470  | exp_id: qwen7b_full_trace_label_only_seed456\")\nlines.append(\"    accuracy_ci: [0.827, 0.866]  pass_f1: 0.9000  fail_f1: 0.7100  lift: 0.1319\")\nlines.append(\"  NOTE: standalone label_only seeds (no trace at all):\")\nlines.append(\"    label_only_seed123 accuracy: 0.8706  pass_f1: 0.915  fail_f1: 0.729\")\nlines.append(\"    label_only_seed456 accuracy: 0.8590  pass_f1: 0.905  fail_f1: 0.727\")\nlines.append(\"\")\n\nlines.append(\"\")\nlines.append(\"=\" * 100)\nlines.append(\"SECTION 2: CROSS-MODEL TABLE — All 4 Models × Main Conditions\")\nlines.append(\"=\" * 100)\nlines.append(\"\")\n\n# --- DeepSeek-Coder-6.7B ---\nlines.append(\"--- DeepSeek-Coder-6.7B ---\")\nlines.append(\"\")\nlines.append(\"  exception_only:\")\nlines.append(\"    Seed 42  accuracy: 0.9933  | exp_id: deepseek_exception_only_seed42\")\nlines.append(\"      pass_f1: 0.9953  fail_f1: 0.9883  n: 1190  lift: 0.2782\")\nlines.append(\"    Seed 123 accuracy: 0.9950  | exp_id: deepseek_exception_only_seed123_v2\")\nlines.append(\"    Seed 456 accuracy: 0.9933  | exp_id: deepseek_exception_only_seed456\")\nlines.append(\"      accuracy_ci: [0.9882, 0.9975]\")\nlines.append(\"      seed_comparison: seed42=0.9933 seed456=0.9933 seed123=0.9109 (outlier)\")\nlines.append(\"      NOTE: seed123 v1 was OOM-crash; seed123_v2 = 0.9950 (canonical)\")\nlines.append(\"    3-SEED MEAN (using v2 for seed123): ~0.994\")\nlines.append(\"\")\nlines.append(\"  full_trace:\")\nlines.append(\"    Seed 42 (v3) accuracy: 0.7916  | exp_id: deepseek_full_trace_seed42_v3\")\nlines.append(\"      accuracy_ci: [0.768, 0.813]  lift: 0.0765\")\nlines.append(\"      pass_f1: 0.854  fail_f1: 0.637  n: 1190\")\nlines.append(\"    (v1, v2 = killed/negative)\")\nlines.append(\"\")\nlines.append(\"  no_trace:\")\nlines.append(\"    Seed 42 accuracy: 0.7336  | exp_id: deepseek_no_trace_seed42\")\nlines.append(\"      accuracy_ci: [0.708, 0.757]  lift: 0.0185\")\nlines.append(\"      pass_f1: 0.8130  fail_f1: 0.5390  n: 1190\")\nlines.append(\"\")\nlines.append(\"  VOTA:\")\nlines.append(\"    Seed 42 accuracy: 0.8445  | exp_id: deepseek_vota_seed42  [early canonical]\")\nlines.append(\"      accuracy_ci: [0.826, 0.864]  lift: 0.1294\")\nlines.append(\"      pass_f1: 0.9020  fail_f1: 0.6250\")\nlines.append(\"    Seed 123 accuracy: 0.9916  | exp_id: deepseek_vota_seed123\")\nlines.append(\"      accuracy_ci_lower: 0.9857  accuracy_ci_upper: 0.9966\")\nlines.append(\"    Seed 456 accuracy: 0.9933  | exp_id: deepseek_vota_seed456\")\nlines.append(\"    NOTE: large seed variance — seed42 may be from different pipeline version\")\nlines.append(\"\")\nlines.append(\"  ae_only:\")\nlines.append(\"    Seed 42 accuracy: 0.9874  | exp_id: deepseek_ae_only_seed42\")\nlines.append(\"      accuracy_ci: [0.9807, 0.9933]  pass_f1: 0.9910  fail_f1: 0.9770\")\nlines.append(\"    Seed 123 accuracy: 0.9832  | exp_id: deepseek_ae_only_seed123\")\nlines.append(\"\")\nlines.append(\"  loop_only:\")\nlines.append(\"    Seed 42 accuracy: 0.8126  | exp_id: deepseek_loop_only_seed42\")\nlines.append(\"      accuracy_ci: [0.7908, 0.8345]\")\nlines.append(\"    Seed 123 accuracy: 0.8126  | exp_id: deepseek_loop_only_seed123\")\nlines.append(\"      accuracy_ci: [0.792, 0.834]\")\nlines.append(\"    Seed 456 accuracy: 0.784   | exp_id: deepseek_loop_only_seed456\")\nlines.append(\"      fail_f1: 0.63  majority_baseline: 0.715\")\nlines.append(\"\")\nlines.append(\"  label_only (full_trace_label_only_loss):\")\nlines.append(\"    Seed 42 accuracy: 0.285   | exp_id: deepseek_label_only_seed42  [COLLAPSED]\")\nlines.append(\"      accuracy_ci: [0.261, 0.308]  lift: -0.430\")\nlines.append(\"      pass_f1: 0.0  fail_f1: 0.44\")\nlines.append(\"\")\n\n# --- CodeLlama-13B ---\nlines.append(\"--- CodeLlama-13B ---\")\nlines.append(\"\")\nlines.append(\"  exception_only:\")\nlines.append(\"    Seed 42  accuracy: 0.9983  | exp_id: codellama13b_exception_only_seed42\")\nlines.append(\"      accuracy_ci: [0.9958, 1.000]  pass_f1: 0.9988  fail_f1: 0.9971\")\nlines.append(\"    Seed 123 accuracy: 1.0000  | exp_id: codellama13b_exception_only_seed123\")\nlines.append(\"      pass_f1: 1.0  fail_f1: 1.0  n: 1190\")\nlines.append(\"    Seed 456 accuracy: 0.9983  | exp_id: codellama13b_exception_only_seed456\")\nlines.append(\"      pass_f1: 0.9988  fail_f1: 0.9971  n: 1190\")\nlines.append(\"    3-SEED MEAN: 0.9989\")\nlines.append(\"\")\nlines.append(\"  full_trace (canonical tail512, label_only_loss):\")\nlines.append(\"    Seed 42  accuracy: 0.9824  | exp_id: codellama13b_full_trace_tail512_seed42\")\nlines.append(\"      accuracy_ci: [0.9748, 0.9899]  lift: 0.2672  pass_f1: 0.9878  fail_f1: 0.9680\")\nlines.append(\"    Seed 123 accuracy: 0.9824  | exp_id: codellama13b_full_trace_tail512_seed123\")\nlines.append(\"      accuracy_ci: [0.9748, 0.9899]\")\nlines.append(\"    Seed 456 accuracy: 0.9824  | exp_id: codellama13b_full_trace_tail512_seed456\")\nlines.append(\"      NOTE: all 3 seeds identical at 0.9824\")\nlines.append(\"    NOTE: full-seq loss at tail2048 collapsed (0.296); label_only_loss v3 at tail1024 = 0.9824 epoch1\")\nlines.append(\"\")\nlines.append(\"  no_trace:\")\nlines.append(\"    Seed 42 accuracy: 0.7650  | exp_id: codellama13b_no_trace_seed42\")\nlines.append(\"      accuracy_ci: [0.738, 0.787]  lift: 0.050\")\nlines.append(\"      pass_f1: 0.840  fail_f1: 0.590  n: 1190\")\nlines.append(\"\")\nlines.append(\"  VOTA:\")\nlines.append(\"    Seed 42  accuracy: 0.9857  | exp_id: codellama13b_vota_seed42\")\nlines.append(\"      accuracy_ci: [0.9790, 0.9916]  pass_f1: 0.9900  fail_f1: 0.9748\")\nlines.append(\"    Seed 123 accuracy: 0.9891  | exp_id: codellama13b_vota_seed123\")\nlines.append(\"      accuracy_ci: [0.9832, 0.9941]  pass_f1: 0.9924  fail_f1: 0.9809  n: 1190  lift: 0.2739\")\nlines.append(\"\")\nlines.append(\"  ae_only:\")\nlines.append(\"    Seed 42  accuracy: 0.9908  | exp_id: codellama13b_ae_only_seed42\")\nlines.append(\"      accuracy_ci: [0.9849, 0.9958]  pass_f1: 0.9935  fail_f1: 0.9840\")\nlines.append(\"    Seed 123 accuracy: 0.9908  | exp_id: codellama13b_ae_only_seed123\")\nlines.append(\"      accuracy_ci: [0.9849, 0.9958]  pass_f1: 0.9930  fail_f1: 0.9840\")\nlines.append(\"\")\nlines.append(\"  loop_only:\")\nlines.append(\"    Seed 42  accuracy: 0.7706  | exp_id: codellama13b_loop_only_seed42\")\nlines.append(\"      accuracy_ci: [0.7487, 0.7941]  lift: 0.0555  pass_f1: 0.820  fail_f1: 0.670\")\nlines.append(\"    Seed 123 accuracy: 0.7605  | exp_id: codellama13b_loop_only_seed123\")\nlines.append(\"      accuracy_ci: [0.7387, 0.7857]  pass_f1: 0.8078  fail_f1: 0.6823  lift: 0.0454\")\nlines.append(\"    Seed 456 accuracy: 0.7908  | exp_id: codellama13b_loop_only_seed456\")\nlines.append(\"      pass_f1: 0.843  fail_f1: 0.688  n: 1190  lift: 0.0757\")\nlines.append(\"\")\nlines.append(\"  label_only (full_trace_label_only_loss):\")\nlines.append(\"    Seed 42 (v2) accuracy: 0.2849  | exp_id: codellama13b_label_only_seed42_v2  [COLLAPSED]\")\nlines.append(\"      accuracy_ci: [0.2613, 0.3084]  pass_f1: 0.0  fail_f1: 0.4434\")\nlines.append(\"    Seed 123 (v2) accuracy: 'collapsed' | exp_id: codellama13b_label_only_seed123_v2\")\nlines.append(\"\")\n\n# --- Qwen-1.5B ---\nlines.append(\"--- Qwen2.5-Coder-1.5B ---\")\nlines.append(\"\")\nlines.append(\"  exception_only:\")\nlines.append(\"    Seed 42  accuracy: 0.9983  | exp_id: qwen15b_exception_only_seed42\")\nlines.append(\"      accuracy_ci: [0.9958, 1.000]  lift: 0.283  pass_f1: 0.9988  fail_f1: 0.9971\")\nlines.append(\"    Seed 123 accuracy: 0.9983  | exp_id: qwen15b_exception_only_seed123_v2\")\nlines.append(\"      accuracy_ci: [0.9958, 1.000]\")\nlines.append(\"    Seed 456 accuracy: 0.9983  | exp_id: qwen15b_exception_only_seed456\")\nlines.append(\"      seed_comparison: all 3 seeds identical — fully seed-robust\")\nlines.append(\"    3-SEED MEAN: 0.9983 ± 0.0000\")\nlines.append(\"\")\nlines.append(\"  full_trace:\")\nlines.append(\"    Seed 42 (full_trace, no trunc) accuracy: 0.7706  | exp_id: qwen15b_full_trace_seed42\")\nlines.append(\"    Seed 42 (tail512) accuracy: 0.956   | exp_id: qwen15b_full_trace_tail512_seed42\")\nlines.append(\"      accuracy_ci: [0.945, 0.968]  pass_f1: 0.970  fail_f1: 0.920\")\nlines.append(\"    Seed 123 (tail512) accuracy: 0.9765  | exp_id: qwen15b_full_trace_tail512_seed123\")\nlines.append(\"      accuracy_ci: [0.9681, 0.9849]  lift: 0.2613\")\nlines.append(\"    Seed 456 (tail512) accuracy: 0.9672  | exp_id: qwen15b_full_trace_tail512_seed456\")\nlines.append(\"      accuracy_ci: [0.9563, 0.9773]  lift: 0.2521\")\nlines.append(\"\")\nlines.append(\"  no_trace:\")\nlines.append(\"    Seed 42  accuracy: 0.6731  | exp_id: qwen15b_no_trace_seed42\")\nlines.append(\"      pass_f1: 0.7527  fail_f1: 0.518  n: 1190\")\nlines.append(\"    Seed 123 accuracy: 0.7588  | exp_id: qwen15b_no_trace_seed123\")\nlines.append(\"      accuracy_ci: [0.7328, 0.7824]  lift: 0.0437\")\nlines.append(\"      pass_f1: 0.8323  fail_f1: 0.571\")\nlines.append(\"    Seed 456 accuracy: 0.7387  | exp_id: qwen15b_no_trace_seed456\")\nlines.append(\"      pass_f1: 0.8195  fail_f1: 0.5266\")\nlines.append(\"\")\nlines.append(\"  VOTA:\")\nlines.append(\"    Seed 42  accuracy: 0.9958  | exp_id: qwen15b_vota_seed42\")\nlines.append(\"      pass_f1: 0.9971  fail_f1: 0.9926  n: 1190\")\nlines.append(\"    Seed 123 accuracy: 0.9950  | exp_id: qwen15b_vota_seed123\")\nlines.append(\"      ci_95: [0.9908, 0.9983]  pass_f1: 0.9965  fail_f1: 0.9912\")\nlines.append(\"\")\nlines.append(\"  ae_only:\")\nlines.append(\"    Seed 42  accuracy: 0.9908  | exp_id: qwen15b_ae_only_seed42\")\nlines.append(\"      accuracy_ci: [0.9849, 0.9958]  lift: 0.2756  pass_f1: 0.9935  fail_f1: 0.9840\")\nlines.append(\"    Seed 123 accuracy: 0.9857  | exp_id: qwen15b_ae_only_seed123\")\nlines.append(\"      majority_baseline: 0.715  fail_f1: 0.975\")\nlines.append(\"\")\nlines.append(\"  loop_only:\")\nlines.append(\"    Seed 42  accuracy: 0.7832  | exp_id: qwen15b_loop_only_seed42\")\nlines.append(\"      pass_f1: 0.8526  fail_f1: 0.5905\")\nlines.append(\"    Seed 123 accuracy: 0.8109  | exp_id: qwen15b_loop_only_seed123\")\nlines.append(\"      pass_f1: 0.8737  fail_f1: 0.6244\")\nlines.append(\"    Seed 456 accuracy: 0.7920  | exp_id: qwen15b_loop_only_seed456\")\nlines.append(\"      ci_95: [0.768, 0.813]  majority_baseline: 0.715\")\nlines.append(\"\")\nlines.append(\"  label_only (full_trace_label_only_loss):\")\nlines.append(\"    Seed 42 (v2) accuracy: 0.7890  | exp_id: qwen15b_label_only_seed42_v2\")\nlines.append(\"      accuracy_ci: [0.766, 0.812]  pass_f1: 0.860  fail_f1: 0.570\")\nlines.append(\"    Seed 123 (v2) accuracy: 0.8134  | exp_id: qwen15b_label_only_seed123_v2\")\nlines.append(\"      accuracy_ci: [0.7924, 0.8345]  pass_f1: 0.878  fail_f1: 0.602\")\nlines.append(\"    Seed 456 (v2) accuracy: 0.8252  | exp_id: qwen15b_label_only_seed456_v2\")\nlines.append(\"      pass_f1: 0.885  fail_f1: 0.639\")\nlines.append(\"\")\n\nlines.append(\"\")\nlines.append(\"=\" * 100)\nlines.append(\"SECTION 3: TABLE 2 — ABLATION CONDITIONS (Qwen-7B, seed42 canonical)\")\nlines.append(\"=\" * 100)\nlines.append(\"\")\n\nlines.append(\"--- Ablation: VOTA component decomposition ---\")\nlines.append(\"  ae_only (Qwen-7B seed42) accuracy: 0.9992  CI:[0.9975, 1.0]  | exp_id: vota_ae_only_seed42\")\nlines.append(\"  exception_only (Qwen-7B) accuracy: 0.9983  CI:[0.9958, 1.0]  | exp_id: vota_exception_only_seed42_v2\")\nlines.append(\"  loop_only (Qwen-7B seed42) accuracy: 0.8563  CI:[0.8353, 0.8756]  | exp_id: vota_loop_only_seed42\")\nlines.append(\"  VOTA-no-ae (Qwen-7B seed42) accuracy: 0.9940  CI:[0.989, 0.998]  | exp_id: vota_no_ae_seed42\")\nlines.append(\"    lift_vs_notrace: 0.2430  CI:[0.218, 0.268]\")\nlines.append(\"\")\nlines.append(\"--- Ablation: Exception sub-component ---\")\nlines.append(\"  exc_message_only_seed42: accuracy=0.9950 CI:[0.991, 0.998] | exp_id: exc_message_only_seed42\")\nlines.append(\"    pass_f1: 0.9960  fail_f1: 0.9910  n: 1190\")\nlines.append(\"  exc_stacktrace_only_seed42: accuracy=0.9980 CI:[0.996, 1.0] | exp_id: exc_stacktrace_only_seed42\")\nlines.append(\"    pass_f1: 0.9990  fail_f1: 0.9970  n: 1190\")\nlines.append(\"  exc_type_only_seed42: no metrics (None conclusion)\")\nlines.append(\"\")\nlines.append(\"--- Ablation: full_trace with label_only_loss ---\")\nlines.append(\"  full_trace_label_only_seed42: accuracy=0.8622 CI:[0.8437, 0.8807] | exp_id: full_trace_label_only_seed42\")\nlines.append(\"    lift_vs_notrace: 0.1109 CI:[0.0849, 0.1370]\")\nlines.append(\"    lift_vs_standard_fulltrace: +0.0445 CI:[0.0235, 0.0655] p=0\")\nlines.append(\"    pass_f1: 0.9063  fail_f1: 0.7397\")\nlines.append(\"\")\nlines.append(\"--- Ablation: nomarker (Qwen-7B) ---\")\nlines.append(\"  Seed 42  accuracy: 0.9655  CI:[0.955, 0.976] | exp_id: exception_only_nomarker_seed42\")\nlines.append(\"  Seed 123 accuracy: 0.9832  CI:[0.9756, 0.9899] | exp_id: exception_only_nomarker_seed123\")\nlines.append(\"    pass_f1: 0.9882  fail_f1: 0.9705  lift_over_majority: 0.2681\")\nlines.append(\"  Seed 456 accuracy: 0.9807  CI:[0.9712, 0.9871] | exp_id: exception_only_nomarker_seed456\")\nlines.append(\"    errors: 23  pass_f1: 0.9865  fail_f1: 0.9658  lift_over_majority: 0.2660\")\nlines.append(\"  NOTE: vs exception_only (0.9983), marker contributes ~1.5-3.3pp\")\nlines.append(\"\")\nlines.append(\"--- Ablation: nomarker (Qwen-1.5B) ---\")\nlines.append(\"  qwen15b_nomarker_seed42: accuracy=0.9780 CI:[0.970, 0.986]  | exp_id: qwen15b_nomarker_seed42\")\nlines.append(\"    majority_baseline: 0.715  lift: 0.263\")\nlines.append(\"    pass_precision: 0.970  pass_recall: 1.0  pass_f1: 0.980\")\nlines.append(\"    fail_precision: 1.0    fail_recall: 0.92  fail_f1: 0.960\")\nlines.append(\"\")\nlines.append(\"--- Ablation: exception_only padded to 2048 tokens ---\")\nlines.append(\"  exception_only_padded2048_seed42: accuracy=0.9983  | exp_id: exception_only_padded2048_seed42\")\nlines.append(\"    (identical to unpadded — padding does not degrade accuracy)\")\nlines.append(\"\")\n\nlines.append(\"\")\nlines.append(\"=\" * 100)\nlines.append(\"SECTION 4: TABLE 3 — DENSITY DECOMPOSITION (gradient masking, tail truncation)\")\nlines.append(\"=\" * 100)\nlines.append(\"\")\n\nlines.append(\"--- Gradient Masking (99.8% masked, exception_only) ---\")\nlines.append(\"  Qwen-7B Seed 42 accuracy: 0.9933 CI:[0.9882, 0.9975] | exp_id: gradient_masking_qwen7b_seed42\")\nlines.append(\"    NOTE: metrics empty (None conclusion) — see seed123/456 for canonical\")\nlines.append(\"  Qwen-7B Seed 123 accuracy: 0.9933 CI:[0.9882, 0.9975] | exp_id: gradient_masking_qwen7b_seed123\")\nlines.append(\"    pass_f1: 0.9953  fail_f1: 0.9883  lift: 0.2782  train_loss: 1.6031  eval_loss: 0.0381\")\nlines.append(\"  Qwen-7B Seed 456 accuracy: 0.9933 CI:[0.9882, 0.9975] | exp_id: gradient_masking_qwen7b_seed456\")\nlines.append(\"    (identical to seed123)\")\nlines.append(\"  3-SEED MEAN: 0.9933 ± 0.0000  dilution_pct: N/A (vs baseline 0.9983 → dilution ~0.5%)\")\nlines.append(\"\")\nlines.append(\"  DeepSeek-6.7B Seed 42 accuracy: 0.9933 CI:[0.9882, 0.9975] | exp_id: deepseek_gradient_masking_seed42\")\nlines.append(\"    dilution_pct: N/A  baseline_accuracy: 99.39%  lift: 0.278  eval_loss: 0.0529\")\nlines.append(\"    majority_baseline: 0.715\")\nlines.append(\"  DeepSeek-6.7B Seed 123 accuracy: 0.9395 | exp_id: deepseek_gradient_masking_seed123\")\nlines.append(\"    pass_precision: 0.924  pass_recall: 0.998  pass_f1: 0.959\")\nlines.append(\"    fail_precision: 0.993  fail_recall: 0.794  fail_f1: 0.882\")\nlines.append(\"    conclusion: negative (fell below 98.5% threshold)\")\nlines.append(\"\")\nlines.append(\"  CodeLlama-13B Seed 42 accuracy: 1.0000 | exp_id: codellama_gradient_masking_seed42\")\nlines.append(\"    accuracy_ci_lower: 1.0  accuracy_ci_upper: 1.0\")\nlines.append(\"    eval_loss: 0.0625  dilution_pct: -0.11  pass_f1: 1.0  fail_f1: 1.0  n_test: 1190\")\nlines.append(\"    baseline_accuracy: 99.89%\")\nlines.append(\"\")\n\nlines.append(\"--- Tail Truncation Budget Curve (Qwen-7B) ---\")\nlines.append(\"  tail-256 (full_trace_tail_256_seed42):  accuracy=0.7748  CI:[0.7496, 0.7975]  pass_f1: 0.8333  fail_f1: 0.6528\")\nlines.append(\"  tail-384 (qwen7b_full_trace_tail384_seed42): accuracy=0.798  CI:[0.776, 0.821]  pass_f1: 0.85  fail_f1: 0.68\")\nlines.append(\"  tail-512 (full_trace_tail_512_seed42):  accuracy=0.9360  CI:[0.922, 0.950]   pass_f1: 0.950  fail_f1: 0.890\")\nlines.append(\"  tail-512 Seed 123 (qwen7b_full_trace_tail512_seed123): accuracy=0.9597 CI:[0.9487, 0.9706]\")\nlines.append(\"  tail-512 Seed 456 (qwen7b_full_trace_tail512_seed456): accuracy=0.9765 CI:[0.9681, 0.9849]\")\nlines.append(\"  tail-1024 (full_trace_tail_1024_seed42): accuracy=0.9647  CI:[0.9546, 0.9748]  pass_f1: 0.9753  fail_f1: 0.9381\")\nlines.append(\"  tail-2048 (full_trace_tail_seed42):     accuracy=0.9730  CI:[0.964, 0.982]    pass_f1: 0.980  fail_f1: 0.950\")\nlines.append(\"  head-2048 (qwen7b_full_trace_head2048_seed42): accuracy=0.8160 (epoch1 best)\")\nlines.append(\"    pass_f1_epoch1: 0.87  fail_f1_epoch1: 0.686\")\nlines.append(\"\")\nlines.append(\"--- Tail Truncation Budget Curve (DeepSeek-6.7B) ---\")\nlines.append(\"  tail-256 (deepseek_full_trace_tail256_seed42):  accuracy=0.7639  CI:[0.7403, 0.7874]  pass_f1: 0.8424  fail_f1: 0.5293\")\nlines.append(\"  tail-384 (deepseek_full_trace_tail384_seed42):  accuracy=0.8070  CI:[0.786, 0.829]    pass_f1: 0.87  fail_f1: 0.60\")\nlines.append(\"  tail-512 (deepseek_full_trace_tail512_seed42):  accuracy=0.9390  CI:[0.926, 0.953]    pass_f1: 0.960  fail_f1: 0.900\")\nlines.append(\"  tail-512 Seed 123 (v2): accuracy=0.9504  CI:[0.9387, 0.9630]\")\nlines.append(\"  tail-512 Seed 456: accuracy=0.9605  CI:[0.9496, 0.9714]\")\nlines.append(\"  tail-1024 (deepseek_full_trace_tail1024_seed42): accuracy=0.9647 CI:[0.9538, 0.9748]  pass_f1: 0.976  fail_f1: 0.936\")\nlines.append(\"  tail-2048 (deepseek_full_trace_tail2048_seed42): accuracy=0.9496 CI:[0.937, 0.962]    pass_f1: 0.965  fail_f1: 0.913\")\nlines.append(\"  head-2048 (deepseek_full_trace_head2048_seed42): accuracy=0.7870 CI:[0.765, 0.810]    pass_f1: 0.850  fail_f1: 0.620\")\nlines.append(\"\")\nlines.append(\"--- Tail Truncation Budget Curve (CodeLlama-13B) ---\")\nlines.append(\"  tail-256 (codellama13b_full_trace_tail256_seed42): accuracy=0.779  CI:[0.757, 0.803]  pass_f1: 0.843  fail_f1: 0.626\")\nlines.append(\"  tail-384 (codellama13b_full_trace_tail384_seed42): accuracy=0.827  CI:[0.807, 0.847]  pass_f1: 0.887  fail_f1: 0.630\")\nlines.append(\"    NOTE: label_only_loss used; conclusion=negative (lower than expected)\")\nlines.append(\"  tail-512 (codellama13b_full_trace_tail512_seed42): accuracy=0.9824 CI:[0.9748, 0.9899]\")\nlines.append(\"    pass_f1: 0.9878  fail_f1: 0.9680  lift: 0.2672  (all 3 seeds identical)\")\nlines.append(\"  tail-1024 (v3, label_only_loss): accuracy_epoch1=0.9824 accuracy_epoch3=0.9756  best_epoch=1\")\nlines.append(\"    pass_f1_epoch1: 0.988  fail_f1_epoch1: 0.968\")\nlines.append(\"  head-2048 (codellama13b_full_trace_head2048_seed42): accuracy=0.7992  CI:[0.7765, 0.8227]\")\nlines.append(\"    pass_f1: 0.8602  fail_f1: 0.6438  lift: 0.084\")\nlines.append(\"\")\nlines.append(\"--- Tail Truncation Budget Curve (Qwen-1.5B) ---\")\nlines.append(\"  tail-256 (qwen15b_full_trace_tail256_seed42):  accuracy=0.7260  CI:[0.700, 0.753]  lift_over_majority: 0.011 (near-0)\")\nlines.append(\"  tail-384 (qwen15b_full_trace_tail384_seed42):  accuracy=0.7361  CI:[0.7101, 0.7622]  lift: 0.021\")\nlines.append(\"  tail-512 (qwen15b_full_trace_tail512_seed42):  accuracy=0.9560  CI:[0.945, 0.968]\")\nlines.append(\"  tail-1024 (qwen15b_full_trace_tail1024_seed42): accuracy=0.966   CI:[0.955, 0.976]   pass_f1: 0.98  fail_f1: 0.94\")\nlines.append(\"  tail-2048 (qwen15b_full_trace_tail2048_seed42): accuracy=0.979   CI:[0.9706, 0.9874]  pass_f1: 0.986  fail_f1: 0.962\")\nlines.append(\"  head-2048 (qwen15b_full_trace_head2048_seed42): accuracy=0.7529  CI:[0.7286, 0.7782]  pass_f1: 0.835  fail_f1: 0.508\")\nlines.append(\"\")\n\nlines.append(\"\")\nlines.append(\"=\" * 100)\nlines.append(\"SECTION 5: REGEX AND MAJORITY BASELINES\")\nlines.append(\"=\" * 100)\nlines.append(\"\")\n\nlines.append(\"--- Regex Baseline (marker condition) ---\")\nlines.append(\"  exp_id: regex_baseline_analysis  n=1190\")\nlines.append(\"  B1 (ERROR presence):   0.9345\")\nlines.append(\"  B2 (Traceback):        0.7151\")\nlines.append(\"  B3 (any keyword):      0.9345\")\nlines.append(\"  B4 (exception type):   0.9361\")\nlines.append(\"  B5 (format marker):    0.9933  ← best regex, McNemar p=0.041 vs SFT\")\nlines.append(\"  B6 (error count ≥2):   0.9202\")\nlines.append(\"  SFT exception_only:    0.9983\")\nlines.append(\"  Best regex gap vs SFT: -0.0622 (B5 at 99.33%, SFT at 99.83%)\")\nlines.append(\"\")\nlines.append(\"--- Regex Baseline (nomarker condition) ---\")\nlines.append(\"  exp_id: regex_nomarker_baseline  n=1190\")\nlines.append(\"  B5_marker_acc:   0.9933  (original with marker)\")\nlines.append(\"  B5_nomarker_acc: 0.2849  (drops 70.84pp without marker)\")\nlines.append(\"  B5_delta_pp:     -70.84\")\nlines.append(\"  B1_marker_acc:   0.9345\")\nlines.append(\"  B1_nomarker_acc: 0.7151\")\nlines.append(\"  B4_marker_acc:   0.9361\")\nlines.append(\"  B4_nomarker_acc: 0.9361  (unchanged — exception type is format-independent)\")\nlines.append(\"  B5b_nomarker_acc: 0.9345  (alternative regex without marker dependency)\")\nlines.append(\"\")\nlines.append(\"--- Majority Baseline (from experiment metrics) ---\")\nlines.append(\"  majority_baseline across experiments: 0.7151 (standard HumanEval/MBPP split)\")\nlines.append(\"  DebugBench majority_baseline: 0.5141  (50/50 pass/fail)\")\nlines.append(\"  Cross-HE2MBPP majority_baseline: 0.6902\")\nlines.append(\"\")\n\nlines.append(\"\")\nlines.append(\"=\" * 100)\nlines.append(\"SECTION 6: CALIBRATION (ECE / Brier Score)\")\nlines.append(\"=\" * 100)\nlines.append(\"\")\n\nlines.append(\"--- Qwen-7B calibration across conditions (exp_id: calibration_analysis_seed42, n=1190) ---\")\nlines.append(\"  no_trace:\")\nlines.append(\"    ECE: 0.171476  MCE: 0.475643  Brier: 0.197152  accuracy: 0.751261\")\nlines.append(\"  full_trace:\")\nlines.append(\"    ECE: 0.095817  MCE: 0.249061  Brier: 0.143924  accuracy: 0.817647\")\nlines.append(\"  label_only:\")\nlines.append(\"    ECE: 0.110686  MCE: 0.417124  Brier: 0.120144  accuracy: 0.862185\")\nlines.append(\"  loop_only:\")\nlines.append(\"    ECE: 0.083085  MCE: 0.183406  Brier: 0.118335  accuracy: 0.856303\")\nlines.append(\"  ae_only:\")\nlines.append(\"    ECE: 0.000415  MCE: 0.000415  Brier: 0.000847  accuracy: 0.99916\")\nlines.append(\"  exception_only:\")\nlines.append(\"    ECE: 0.002717  MCE: 0.835484  Brier: 0.001311  accuracy: 0.998319\")\nlines.append(\"  vota:\")\nlines.append(\"    ECE: 0.005410  MCE: 0.622459  Brier: 0.005234  accuracy: 0.994118\")\nlines.append(\"\")\nlines.append(\"--- Cross-model calibration (exp_id: cross_model_calibration_eval, exception_only, n=1190) ---\")\nlines.append(\"  Qwen-7B:\")\nlines.append(\"    ECE: 0.0027  MCE: 0.8355  Brier: 0.0013  accuracy: 0.9983\")\nlines.append(\"  Qwen-1.5B:\")\nlines.append(\"    ECE: 0.0020  MCE: 0.7549  Brier: 0.0013  accuracy: 0.9983\")\nlines.append(\"  CodeLlama-13B:\")\nlines.append(\"    ECE: 0.0020  MCE: 0.0411  Brier: 0.0013  accuracy: 0.9983\")\nlines.append(\"  DeepSeek-6.7B:\")\nlines.append(\"    ECE: 0.0064  MCE: 0.7756  Brier: 0.0061  accuracy: 0.9933\")\nlines.append(\"  ALL: ECE < 0.007, Brier < 0.007 — universally well-calibrated across architectures\")\nlines.append(\"\")\n\nlines.append(\"\")\nlines.append(\"=\" * 100)\nlines.append(\"SECTION 7: CROSS-DATASET GENERALIZATION\")\nlines.append(\"=\" * 100)\nlines.append(\"\")\n\nlines.append(\"--- HE→MBPP (train HumanEval, test MBPP) ---\")\nlines.append(\"  exception_only (exp_id: cross_he2mbpp_exception_only_seed42):\")\nlines.append(\"    accuracy: 0.9941  majority_baseline: 0.6902  lift: 0.3040\")\nlines.append(\"    pass_f1: 0.9957  fail_f1: 0.9906\")\nlines.append(\"    pass_precision: 0.9980  pass_recall: 0.9936\")\nlines.append(\"    fail_precision: 0.9858  fail_recall: 0.9955\")\nlines.append(\"  no_trace (exp_id: cross_he2mbpp_no_trace_seed42):\")\nlines.append(\"    accuracy: 0.7056  majority_baseline: 0.6902  lift: 0.0155\")\nlines.append(\"    pass_f1: 0.8074  fail_f1: 0.3756\")\nlines.append(\"    pass_precision: 0.7360  pass_recall: 0.8941\")\nlines.append(\"    fail_precision: 0.5478  fail_recall: 0.2857\")\nlines.append(\"\")\nlines.append(\"--- MBPP→HE (train MBPP, test HumanEval) ---\")\nlines.append(\"  exception_only (exp_id: cross_mbpp2he_exception_only_seed42): status=DONE, no metrics in spec\")\nlines.append(\"  no_trace (exp_id: cross_mbpp2he_no_trace_seed42): status=DONE, no metrics in spec\")\nlines.append(\"\")\nlines.append(\"--- Cross-dataset nomarker ablation (HE→MBPP, nomarker) ---\")\nlines.append(\"  exp_id: nomarker_cross_he2mbpp_exception_only\")\nlines.append(\"  accuracy: 0.9546  (vs marker 0.9941 → delta = -0.0395)\")\nlines.append(\"  pass_f1: 0.9662  fail_f1: 0.9309\")\nlines.append(\"  pass_precision: 0.9943  pass_recall: 0.9396\")\nlines.append(\"  fail_precision: 0.8801  fail_recall: 0.9879\")\nlines.append(\"  eval_loss: 1.09  train_loss: 0.247\")\nlines.append(\"  NOTE: even without markers, cross-dataset accuracy ~95.5% (strong generalization)\")\nlines.append(\"\")\n\nlines.append(\"\")\nlines.append(\"=\" * 100)\nlines.append(\"SECTION 8: OUT-OF-DISTRIBUTION (DebugBench)\")\nlines.append(\"=\" * 100)\nlines.append(\"\")\n\nlines.append(\"  DebugBench exception_only (exp_id: debugbench_exception_only_seed42, n=426):\")\nlines.append(\"    accuracy: 1.0000  CI_wilson:[0.9914, 1.0]  majority_baseline: 0.5141  lift: 0.4859\")\nlines.append(\"    pass_f1: 1.0  fail_f1: 1.0  (zero errors)\")\nlines.append(\"\")\nlines.append(\"  DebugBench VOTA (exp_id: debugbench_vota_seed42, n=426):\")\nlines.append(\"    accuracy: 0.9977  errors: 1  CI:[0.993, 1.0]  majority_baseline: 0.5141  lift: 0.4836\")\nlines.append(\"    pass_f1: 1.0  fail_f1: 1.0\")\nlines.append(\"\")\nlines.append(\"  DebugBench no_trace (exp_id: debugbench_no_trace_seed42):\")\nlines.append(\"    accuracy: 0.9671  majority_baseline: 0.5141  lift: 0.4531\")\nlines.append(\"    pass_f1: 0.967  fail_f1: 0.967\")\nlines.append(\"    CI: [0.948, 0.984]\")\nlines.append(\"  NOTE: no_trace lift is higher on DebugBench because 50/50 class balance\")\nlines.append(\"\")\n\nlines.append(\"\")\nlines.append(\"=\" * 100)\nlines.append(\"SECTION 9: FRONTIER LLM COMPARISON (GPT-4o, GPT-4.1, zero-shot Qwen-7B)\")\nlines.append(\"=\" * 100)\nlines.append(\"\")\n\nlines.append(\"  GPT-4o 0-shot exception_only (exp_id: fewshot_gpt4o_exception_only_0shot):\")\nlines.append(\"    accuracy: 0.8798  fail_f1: 0.8228\")\nlines.append(\"  GPT-4o 3-shot exception_only (exp_id: fewshot_gpt4o_exception_only_3shot):\")\nlines.append(\"    accuracy: 0.8681  fail_f1: 0.7995  (3-shot worse than 0-shot)\")\nlines.append(\"  GPT-4o 0-shot no_trace (exp_id: fewshot_gpt4o_no_trace_0shot):\")\nlines.append(\"    accuracy: 0.8445  fail_f1: 0.7543\")\nlines.append(\"\")\nlines.append(\"  GPT-4.1 0-shot exception_only (exp_id: fewshot_gpt41_exception_only_0shot):\")\nlines.append(\"    accuracy: 0.8218  fail_f1: 0.7452\")\nlines.append(\"  GPT-4.1 3-shot exception_only (exp_id: fewshot_gpt41_exception_only_3shot):\")\nlines.append(\"    accuracy: 0.8193  fail_f1: 0.7413\")\nlines.append(\"  GPT-4.1 0-shot no_trace (exp_id: fewshot_gpt41_no_trace_0shot):\")\nlines.append(\"    accuracy: 0.7731  fail_f1: 0.6608\")\nlines.append(\"\")\nlines.append(\"  Qwen-7B 0-shot exception_only (exp_id: zeroshot_qwen7b_exception_only):\")\nlines.append(\"    accuracy: 0.8908  CI:[0.8731, 0.9076]  pass_f1: 0.9276  fail_f1: 0.7774  n: 1190\")\nlines.append(\"  Qwen-7B 3-shot exception_only (exp_id: fewshot_qwen7b_exception_only):\")\nlines.append(\"    accuracy: 0.9084  CI:[0.8908, 0.9244]  pass_f1: 0.9368  fail_f1: 0.8336  n: 1190\")\nlines.append(\"  → SFT Qwen-7B exception_only: 0.9983  (gap vs 0-shot: +10.75pp)\")\nlines.append(\"\")\nlines.append(\"  DeepSeek-6.7B 0-shot (exp_id: zeroshot_deepseek7b_exception_only):\")\nlines.append(\"    accuracy: 0.9059  CI:[0.8899, 0.9218]  pass_f1: 0.9313  fail_f1: 0.8507  n: 1190\")\nlines.append(\"  Qwen-1.5B 0-shot (exp_id: zeroshot_qwen15b_exception_only):\")\nlines.append(\"    accuracy: 0.9345  CI:[0.9202, 0.9479]  pass_f1: 0.9690  fail_f1: 0.8730  n: 1190  unknown: 24\")\nlines.append(\"  CodeLlama-13B 0-shot (exp_id: zeroshot_codellama13b_exception_only):\")\nlines.append(\"    accuracy: 0.5101  CI:[0.4824, 0.5395]  pass_f1: 0.5187  fail_f1: 0.5146  n: 1190  unknown: 30\")\nlines.append(\"    NOTE: near-random, heavy bias toward fail\")\nlines.append(\"\")\n\nlines.append(\"\")\nlines.append(\"=\" * 100)\nlines.append(\"SECTION 10: LEARNING DYNAMICS (step-level, Qwen-7B)\")\nlines.append(\"=\" * 100)\nlines.append(\"\")\n\nlines.append(\"  exception_only dynamics (exp_id: qwen7b_exception_only_dynamics_seed42):\")\nlines.append(\"    step50:  0.9933  step100: 0.9933  step150: 0.9933\")\nlines.append(\"    step200: 0.9983  step250: 0.9983  step300: 0.9983\")\nlines.append(\"    step350: 0.9983  step400: 0.9983  step444: 0.9983\")\nlines.append(\"    saturation_step: 200  final_loss: 0.0329  pass_f1: 0.9988  fail_f1: 0.9971\")\nlines.append(\"\")\nlines.append(\"  full_trace (label_only_loss) dynamics (exp_id: qwen7b_full_trace_dynamics_seed42):\")\nlines.append(\"    step50:  0.8739  step100: 0.821  step150: 0.857\")\nlines.append(\"    step200: 0.866   step250: 0.874  step300: 0.849\")\nlines.append(\"    step350: 0.888   step400: 0.857  step444: 0.882\")\nlines.append(\"    best_step: 350  best_acc: 0.8882  final_loss: 0.0085\")\nlines.append(\"    NOTE: non-monotonic, no saturation (vs exception_only which saturates at step 200)\")\nlines.append(\"\")\n\nlines.append(\"\")\nlines.append(\"=\" * 100)\nlines.append(\"SECTION 11: MISC / COVERAGE NOTES\")\nlines.append(\"=\" * 100)\nlines.append(\"\")\n\nlines.append(\"  attention_gradient_analysis: DONE, no numeric metrics stored\")\nlines.append(\"\")\nlines.append(\"  Qwen-1.5B (earlier alias qwen1.5b_*): all killed — use qwen15b_* experiments\")\nlines.append(\"  CodeLlama (earlier alias codellama_*): all killed — use codellama13b_* experiments\")\nlines.append(\"\")\nlines.append(\"  cross_mbpp2he_exception_only_seed42: DONE, metrics NOT stored in registry\")\nlines.append(\"  cross_mbpp2he_no_trace_seed42: DONE, metrics NOT stored in registry\")\nlines.append(\"\")\nlines.append(\"  Seed-42 canonical for Qwen-7B exception_only NOT separately recorded;\")\nlines.append(\"    accuracy confirmed 0.9983 via seed_comparison fields in seed123 and seed456 records\")\nlines.append(\"\")\nlines.append(\"  codellama_gradient_masking_seed42: accuracy=1.0000 dilution_pct=-0.11 (better than baseline)\")\nlines.append(\"\")\nlines.append(\"  deepseek_gradient_masking summary:\")\nlines.append(\"    seed42: accuracy=0.9933 (success) | seed123: accuracy=0.9395 (negative — below 98.5% threshold)\")\nlines.append(\"\")\n\nlines.append(\"=\" * 100)\nlines.append(\"END OF REGISTRY AUDIT EXTRACT\")\nlines.append(\"=\" * 100)\n\noutput = \"\\n\".join(lines)\nwith open(output_path, 'w') as f:\n    f.write(output)\n\nprint(f\"Written {len(output)} chars / {len(lines)} lines to {output_path}\")\nPYEOF\n",
    "description": "Compile comprehensive audit extract and write to artifacts file"
  }
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-23T19:33:00.196347+00:00_

Written 30821 chars / 578 lines to /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/_audit_registry_extract.txt

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_final-maintext-tables_20260523T191655",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-23T19:33:00.196502+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "wc -l /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/_audit_registry_extract.txt",
  "description": "Verify file line count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_final-maintext-tables_20260523T191655",
  "tool": "Bash",
  "tool_args": {
    "command": "wc -l /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/_audit_registry_extract.txt",
    "description": "Verify file line count"
  }
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-23T19:33:00.196626+00:00_

577 /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/_audit_registry_extract.txt

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_final-maintext-tables_20260523T191655",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-23T19:33:00.196788+00:00_

The audit extract has been written to `/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/_audit_registry_extract.txt` (577 lines, 30K chars).

**What was extracted from 188 registry experiments:**

**Section 1 — Table 1 (Qwen-7B main conditions):**
- exception_only: 0.9983 ± 0.0000 across all 3 seeds (identical)
- full_trace: ~0.814 mean (seed42=0.8176, seed123=0.8020, seed456=0.8235)
- no_trace: ~0.764 mean (seed42=0.7513, seed123=0.7908, seed456=0.7504)
- VOTA: ~0.991 (seed42_v5=0.9941, seed123=0.9866, seed456=0.9908)
- ae_only: 0.9964 ± 0.0049; loop_only: 0.8605 ± 0.0053

**Section 2 — Cross-model (all 4 architectures × conditions), including all CI bounds**

**Section 3 — Table 2 ablations:** VOTA component decomposition, exception sub-components (message=0.9950, stacktrace=0.9980), nomarker (~0.965–0.983), label_only_loss

**Section 4 — Density/tail truncation curves** for all 4 models (256→384→512→1024→2048 tokens, head vs tail); gradient masking results

**Section 5 — Regex baselines:** B1–B6 exact numbers; B5 nomarker collapse (0.9933→0.2849, -70.84pp)

**Section 6 — ECE/Brier:** All 7 conditions for Qwen-7B; cross-model calibration (all ECE < 0.007)

**Sections 7–11:** Cross-dataset (HE→MBPP, MBPP→HE), DebugBench OOD, GPT-4o/4.1 frontier comparison, learning dynamics, and coverage gaps (cross_mbpp2he has no stored metrics).
agentId: ad4eda51cd882ef4e (use SendMessage with to: 'ad4eda51cd882ef4e' to continue this agent)
&lt;usage>total_tokens: 77651
tool_uses: 14
duration_ms: 349229&lt;/usage>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_final-maintext-tables_20260523T191655",
  "tool": "Agent",
  "elapsed_ms": 5
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-23T19:33:00.196968+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/_audit_registry_extract.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_final-maintext-tables_20260523T191655",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/_audit_registry_extract.txt"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-23T19:33:00.197303+00:00_

1	====================================================================================================
2	REGISTRY AUDIT EXTRACT — trace-verdict-study
3	Generated from: mcp-agent-ml-research-read_registry-1779563834793.txt
4	Total experiments in registry: 188
5	====================================================================================================
6	
7	====================================================================================================
8	SECTION 1: TABLE 1 CANDIDATES — Main SFT Conditions (Qwen2.5-Coder-7B-Instruct, n=1190)
9	====================================================================================================
10	
11	--- exception_only (Qwen-7B) ---
12	  Seed 42 accuracy: 0.9983 (from seed_comparison in exception_only_seed123)
13	  Seed 123 accuracy: 0.9983  | exp_id: exception_only_seed123
14	    accuracy_ci: [0.9958, 1.0]
15	    pass_precision: 1.0000  pass_recall: 0.9976  pass_f1: 0.9988
16	    fail_precision: 0.9941  fail_recall: 1.0000  fail_f1: 0.9971
17	    majority_baseline: 0.7151  lift: 0.2832  n: 1190
18	  Seed 456 accuracy: 0.9983  | exp_id: exception_only_seed456
19	    accuracy_ci: [0.9958, 1.0]  eval_loss: 0.4629  train_loss: 0.1087
20	  MEAN across 3 seeds: 0.9983 ± 0.0000 (all identical, max_diff=0)
21	  NOTE: each seed has exactly 2/1190 errors
22	
23	--- full_trace (Qwen-7B) ---
24	  Seed 123 accuracy: 0.7958  | exp_id: full_trace_seed123
25	    accuracy_ci_lower: 0.7714  accuracy_ci_upper: 0.8202
26	    pass_precision: 0.8753  pass_recall: 0.8331  pass_f1: 0.8537
27	    fail_precision: 0.6263  fail_recall: 0.7021  fail_f1: 0.6620
28	    majority_baseline: 0.7151  lift: 0.0807  n: 1190
29	  Seed 42 (v5) accuracy: 0.8176  | exp_id: full_trace_seed42_v5
30	    accuracy_ci_lower: 0.797  accuracy_ci_upper: 0.839
31	    pass_precision: 0.8774  pass_recall: 0.8660  pass_f1: 0.8717
32	    fail_precision: 0.6743  fail_recall: 0.6962  fail_f1: 0.6851
33	    lift: 0.1025  lift_vs_notrace: 0.0664  (CI: [0.0437, 0.08
…[truncated 31025 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_final-maintext-tables_20260523T191655",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 55 · 2026-05-23T19:33:00.197954+00:00_

所有数据已就绪。开始逐项核对。

---

## 数据审计报告

### 一、Abstract 6 个核心数字

```
[Abstract] "77--82%" → Table 1 full_trace 4 models means: 77.06/79.16/79.9/81.44
  → range = 77.06--81.44 → ⚠️ 上界 81.44 ≈ 81，非 82；82.35 仅为 Qwen-7B 单 seed 最大值

[Abstract] "≥99.33%" → DS seed42=99.33, seed456=99.33 (全模型全 seed 最低)
  → registry: DS seeds 99.33/99.50/99.33 → ✅

[Abstract] "28.49%" → regex_nomarker_baseline: B5_nomarker_acc=0.2849 → ✅

[Abstract] "97.65%" → nomarker 3-seed: 96.55/98.32/98.07, mean=97.647 → ✅

[Abstract] "≤4%" → 0.61pp / 18.07pp = 3.37% → ✅ (前提是 grad mask mean=99.22)
  → ⚠️ 但 registry 3 seeds 均为 99.33 (见 Table 3 详细核对)

[Abstract] "12pp" → SFT 99.83 − GPT-4o 87.98 = 11.85pp ≈ 12pp → ✅
  → GPT-4o 来源: fewshot_gpt4o_exception_only_0shot: 0.8798 → ✅
```

### 二、Table 1 (cross_model) 逐格核对

**exception_only 行：**
```
[T1] Qwen-7B  99.83±0.00 → seeds 99.83/99.83/99.83 → ✅
[T1] Qwen-1.5B 99.83±0.00 → seeds 99.83/99.83/99.83 → ✅
[T1] CL-13B   99.89±0.10 → seeds 99.83/100.00/99.83, mean=99.89, std=0.098≈0.10 → ✅
[T1] DS-6.7B  99.39±0.10 → seeds 99.33/99.50/99.33, mean=99.39, std=0.098≈0.10 → ✅
```

**ae_only 行：**
```
[T1] Qwen-7B  99.64±0.49 → seeds 99.92/99.08/99.92, mean=99.64, std=0.49 → ✅
[T1] Qwen-1.5B 98.83±0.36 → seeds 99.08/98.57 (2-seed), mean=98.83, std=0.36 → ✅
[T1] CL-13B   99.08±0.00 → seeds 99.08/99.08, identical → ✅
[T1] DS-6.7B  98.53±0.30 → seeds 98.74/98.32 (2-seed), mean=98.53, std=0.30 → ✅
```

**VOTA 行：**
```
[T1] Qwen-7B  99.05±0.38 → seeds(v5) 99.41/98.66/99.08, mean=99.05, std=0.38 → ✅
[T1] Qwen-1.5B 99.54±0.06 → seeds 99.58/99.50 (2-seed), mean=99.54, std=0.06 → ✅
[T1] CL-13B   98.74±0.24 → seeds 98.57/98.91 (2-seed), mean=98.74, std=0.24 → ✅
[T1] DS-6.7B  99.25‡ (2-seed) → seeds(excl 42) 99.16/99.33, mean=99.25 → ✅
```

**loop_only 行：**
```
[T1] Qwen-7B  86.05±0.52 → seeds 85.63/85.88/86.64, mean=86.05, std=0.526≈0.52 → ✅
[T1] Qwen-1.5B 79.54±1.42 → seeds 78.32/81.09/79.20, mean=79.54, std=1.42 → ✅
[T1] CL-13B   77.40±1.54 → seeds 77.06/76.05/79.08, mean=77.40, std=1.54 → ✅
[T1] DS-6.7B  80.31±1.65 → seeds 81.26/81.26/78.40, mean=80.31, std=1.65 → ✅
```

**full_trace 行：**
```
[T1] Qwen-7B  81.44±1.11 → seeds 81.76/80.20/82.35, mean=81.44, std=1.11 → ✅
[T1] Qwen-1.5B 77.06† → registry qwen15b_full_trace_seed42=0.7706 → ✅
[T1] CL-13B   79.9§ → registry codellama13b_head2048_seed42=0.7992≈79.9 → ✅
[T1] DS-6.7B  79.16† → registry deepseek_full_trace_seed42_v3=0.7916 → ✅
```

**no_trace 行：**
```
[T1] Qwen-7B  75.13† → registry no_trace_seed42_v5=0.7513 → ✅
[T1] Qwen-1.5B 72.35±4.48 → seeds 67.31/75.88/73.87, mean=72.35, std=4.48 → ✅
[T1] CL-13B   76.47† → registry=0.7650, 但 910/1190=0.76471 → ⚠️ registry 四舍五入，论文值正确
[T1] DS-6.7B  73.36† → registry deepseek_no_trace_seed42=0.7336 → ✅
```

**Baselines：**
```
[T1] Regex B5 99.33 → registry B5=0.9933 → ✅
[T1] Majority 71.51 → registry=0.7151 → ✅
```

### 三、Table 2 (ablation) 核对

```
[T2] ae_only      99.64†  CI[99.26,99.87] Tier 1 → mean=99.64 ✅
[T2] exception_only 99.83 CI[99.58,100.00] Tier 1 → 99.83 ✅
[T2] VOTA         99.05§  CI[98.49,99.50]        → mean=99.05 ✅
[T2] VOTA_no_ae   99.41   CI[98.90,99.80]        → registry=0.9940→99.40, 论文99.41 → ⚠️ 微小四舍五入
[T2] loop_only    86.05‡  CI[83.97,87.96] Tier 2 → mean=86.05 ✅
[T2] full_trace   81.44±1.11                      → mean=81.44 ✅
[T2] no_trace     75.13   CI[72.77,77.48]        → 75.13 ✅
[T2] Regex (best) 93.61                           → B4=0.9361 ✅
[T2] 3-shot       90.84                           → fewshot_qwen7b=0.9084 ✅
[T2] Zero-shot    51.0--93.5                      → CL=51.01, Q1.5B=93.45 ✅
```

### 四、Table 3 (density decomposition) 核对

```
[T3] exception_only  99.83±0.00           → ✅
[T3] +grad mask      99.22±0.20  Δ−0.61pp → ❌ registry 3 seeds 均为 99.33±0.00
     论文 seeds "98.99/99.33/99.33" → mean=99.22, std=0.20（内部一致）
     但 registry gradient_masking_qwen7b_seed{42,123,456} 均记录 accuracy=0.9933
     seed42 注明 "metrics empty (None conclusion)"，可能原始值为 98.99 但被覆盖
     → ≤4% 结论不受影响 (0.61/18.07=3.4% 或 0.50/18.07=2.8%)，但具体数值需确认

[T3] full_trace      81.76‡    Δ−18.07pp → seed42_v5=0.8176 ✅
     脚注 "3-seed mean 81.44%±1.11"    → ✅

[T3] label-only      85.94±1.12 Δ+4.50pp → seeds 86.22/86.89/84.70, mean=85.94, std=1.12 ✅
     Δ vs full_trace: 85.94−81.44=4.50pp → ✅
```

### 五、正文引用数字交叉核对

**Introduction：**
```
[Intro] "77--82%" complete traces → range 77.06--81.44 → ⚠️ 同 Abstract
[Intro] "≥99%" exception_only → min across means = 99.39 → ✅
[Intro] "18--23pp gap" → exc−full_trace: 18.39/22.77/19.99/20.23 → range 18--23 → ✅
[Intro] "71pp" regex drop → 99.33−28.49=70.84≈71 → ✅
[Intro] ">97%" SFT nomarker → 97.65% → ✅
[Intro] "99.4--100%" cross-dataset → HE→MBPP=99.41, MBPP→HE=100.0 → ⚠️ MBPP→HE 无 registry 数据
[Intro] "≤4%" gradient dilution → ✅
[Intro] "≥99.33%" → ✅
[Intro] "23--27pp" exception lift → lifts: 24.70/27.48/23.42/26.03 → range 23--27 ✅
```

**Experiments：**
```
[Exp §3.1] "spanning only 0.50pp" exc_only cross-model → 99.89−99.39=0.50 → ✅
[Exp §3.1] "loop_only spans 8.57pp" → 86.05−77.40=8.65pp → ⚠️ 应为 8.65 非 8.57
[Exp §3.1] "σ=4.48pp" no_trace → Qwen-1.5B no_trace std=4.48 → ✅
[Exp §3.2] "ae_only on DeepSeek, 98.53%±0.30" → ✅
[Exp §3.2] "loop_only on Qwen-7B, 86.05%" → ✅
[Exp §3.2] "12.48pp" → 98.53−86.05=12.48 → ✅
[Exp §3.2] "Qwen +10.92pp(7B) +7.19pp(1.5B); DS +6.95pp; CL +0.93pp" →
            86.05−75.13=10.92 ✅; 79.54−72.35=7.19 ✅; 80.31−73.36=6.95 ✅; 77.40−76.47=0.93 ✅
[Exp §3.2] B4 "93.61%" → ✅
[Exp §3.2] "trailing by 6.22pp" → 99.83−93.61=6.22 → ✅
[Exp §3.2] "+3.62--23.86pp" → ⚠️ VOTA gap 用 seed42(99.41)=23.86 而非 3-seed mean(99.05)=23.50
            no_trace +3.62 ✅; full_trace +4.37 ✅; exc +6.22 ✅
[Exp §3.2] "Zero-shot spans 51.0--93.5% (42.44pp range)" → 93.45−51.01=42.44 → ✅
[Exp §3.2] "3-shot ICL (90.84%) improves only 1.76pp" → 90.84−89.08=1.76 → ✅
[Exp §3.2] "SFT compresses to 0.50pp (99.39--99.89%)" → ✅
[Exp §3.2] "6--49pp gap" → 6.38--48.88 → 6--49 → ✅
[Exp §3.2] "GPT-4o (84.45%)" no_trace → registry=0.8445 → ✅
[Exp §3.2] "GPT-4.1 (77.31%)" no_trace → registry=0.7731 → ✅
[Exp §3.2] "SFT 99.83% vs GPT-4o 87.98%" → ✅
[Exp §3.3] "97.65% ± 0.96 (seeds 96.55/98.32/98.07)" → ✅
[Exp §3.3] "Qwen-1.5B: 97.82%, drop of 2.01pp" → registry=97.80 → ⚠️ 97.82 vs 97.80
[Exp §3.3] "~2pp accounts for ~9% of 24.70pp" → 2.18/24.70=8.8%≈9% → ✅
[Exp §3.3] "B5 99.33% collapses to 28.49%" → ✅
[Exp §3.3] "SFT nomarker 97.65% exceeds B4 by 4.04pp" → 97.65−93.61=4.04 → ✅
[Exp §3.3] "HE→MBPP 99.41% (N=4,270)" → registry=0.9941 → ✅
[Exp §3.3] "MBPP→HE 100.0% (N=1,640)" → ⚠️ registry 无存储指标，不可验证
[Exp §3.3] "no_trace: 70.56% vs 69.02% majority" → registry=0.7056/0.6902 → ✅
[Exp §3.3] "67.99% vs 61.65%" MBPP→HE no_trace → ⚠️ 不可验证
[Exp §3.3] "cross-dataset drops to 95.5% (−3.9pp)" → 95.46≈95.5, 99.41−95.46=3.95≈3.9 → ✅
[Exp §3.4] "18.07pp gap (99.83% vs 81.76%)" → ✅
[Exp §3.4] "99.22% (mean −0.61pp)" → ❌ 同 Table 3 issue
[Exp §3.4] "≤4% of 18.07pp" → ✅ (无论用 0.61 还是 0.50)
[Exp §3.4] "label-only +4.50pp" → ✅
[Exp §3.4] "DS 99.33%, CL 100% under masking" → registry ✅
[Exp §3.5] "1024-token (77.23%) vs 512-token (80.42%, p=.002)" → ✅
[Exp §3.5] "no-limit 81.76%" → ✅
[Exp §3.5] "tail-2048 exceeds head-2048 by 15.5--22.6pp" → 15.5/22.6/16.3 → ✅
[Exp §3.5] "+13.2--22.0pp" at 384→512 → 13.7/13.2/15.5/22.0 → ✅
[Exp §3.5] "[93.61%, 98.24%]" tail-512 all seeds → ✅
[Exp §3.5] "2--5pp residual gap" → max gap=4.33pp(DS) → ⚠️ 上界应为 ~4 而非 5
[Exp §3.5] "ECE=0.0027 vs 0.171, 63×" → 0.171476/0.002717=63.1 → ✅
[Exp §3.5] "ECE < 0.007" all models → max=0.0064(DS) → ✅
```

**Discussion：**
```
[Disc] "3--6pp full_trace lift" → lifts: 6.31/4.71/3.43/5.80 → range 3.4--6.3 ≈ 3--6 → ✅
[Disc] "23--27pp exception lift" → lifts: 24.70/27.48/23.42/26.03 → ✅
[Disc] "97.65% under marker removal" → ✅
[Disc] "28.49%" regex collapse → ✅
[Disc] "63× better calibration" → ✅
```

**Conclusion：**
```
[Conc] "≥99.33%" → ✅
[Conc] "77--82%" → ⚠️ 同 Abstract
[Conc] "18--23pp" → ✅
[Conc] "≤4% dilution" → ✅
[Conc] "99.4--100%" cross-dataset → ⚠️ MBPP→HE 不可验证
[Conc] "93--98%" tail fallback → tail-512 range 93.6--98.2 → ✅
```

### 六、Appendix 数据核对

```
[App full_qwen] exception_only S42/123/456=99.83 all → ✅
[App full_qwen] ae_only S42=99.92 S123=99.08 S456=99.92, mean=99.64±0.49 → ✅
[App full_qwen] VOTA S42=99.41 S123=98.66 S456=99.08, mean=99.05±0.38 → ✅
[App full_qwen] label_only S42=86.22 S123=86.89 S456=84.70, mean=85.94±1.12 → ✅
[App full_qwen] loop_only S42=85.63 S123=85.88 S456=86.64, mean=86.05±0.52 → ✅
[App full_qwen] full_trace S42=81.76 S123=80.20 S456=82.35, mean=81.44±1.11 → ✅
[App full_deepseek] exception_only 99.33/99.50/99.33 → ✅
[App full_deepseek] VOTA 84.45/99.16/99.33 → ✅

[App per_class] "Full Trace (LO)" acc=85.94 → ❌ 表标注 seed 42，但 85.94 是 3-seed mean；
               seed42 实际值=86.22 (registry: full_trace_label_only_seed42=0.8622)
               F1 值来自 seed42 (pass_f1=0.9063, fail_f1=0.7397 ✓)，仅 accuracy 错误

[App calibration] ECE/Brier (Qwen-7B conditions) → 与 registry 一致 ✅
[App calibration_cross] 4 models ECE → 与 registry cross_model_calibration_eval 一致 ✅
[App calibration_model_level] → ❌ 与 calibration_cross 表数值冲突：
     Qwen-1.5B: 0.0014 vs 0.0020
     Qwen-7B:   0.0017 vs 0.0027
     DS-6.7B:   0.0048 vs 0.0064
     两表均标注 "seed 42, N=1190"，但 ECE 值不同，疑为不同 bin 策略或计算版本
```

### 七、精度统一性

```
主表 (T1/T2/T3): 一般 2 位小数 (99.83, 98.53 等)
CL full_trace: 79.9 (1 位) → ⚠️ 其他 cell 均 2 位
Appendix tail tables: 1 位小数 (78.9, 93.6 等) → 与主表不同但可接受
ECE/Brier: 小数位数不一（0.0004 vs 0.005）→ 可接受
```

---

## 汇总

| 类别 | 数量 |
|------|------|
| 核对总数 | ~85 项 |
| ✅ 一致 | 72 |
| ⚠️ 轻微/可讨论 | 10 |
| ❌ 需修复 | 3 |

### ❌ 需修复（3 项）

1. **Table 3 gradient masking 99.22±0.20**：Registry 3 seeds 均记录 99.33，mean 应为 99.33±0.00。论文 seeds "98.99/99.33/99.33" 内部自洽，但与 registry 不符。seed42 registry 注明 "metrics empty"，可能原始值 98.99 被后续覆写。需确认 seed42 实际值。≤4% 结论不受影响。

2. **Appendix per_class 表 "Full Trace (LO)" accuracy**：表标注 seed 42，但 accuracy=85.94 是 3-seed mean（seed42 实际为 86.22）。应改为 86.22。

3. **Appendix 两个 calibration 表 ECE 数值冲突**：tab:calibration\_cross 和 tab:calibration\_model\_level 对同一模型同一条件报告不同 ECE（如 Qwen-7B: 0.0027 vs 0.0017），两表均标注 seed 42 / N=1190。需统一或标注计算方法差异。

### ⚠️ 需关注（10 项）

1. **"77--82%"**：Table 1 mean 范围 77.06--81.44，严格说应为 77--81%。82% 仅为单 seed 最大值。
2. **"loop_only spans 8.57pp"**：实际 86.05−77.40=8.65pp。
3. **"+3.62--23.86pp"**（SFT vs regex）：VOTA gap 23.86 用 seed42(99.41) 非 3-seed mean(99.05)=23.50。
4. **"2--5pp" tail residual gap**：最大实际 gap 仅 4.33pp(DS)，非 5pp。
5. **Qwen-1.5B nomarker "97.82%"**：Registry=97.80%（0.02pp 差）。
6. **MBPP→HE 100.0% / 67.99%**：Registry 无存储指标，不可从 registry 验证。
7. **CL no_trace 76.47 vs registry 76.50**：Registry 四舍五入，论文值 910/1190=76.47 正确。
8. **cross-dataset nomarker "95.5%"**：实际 95.46%。
9. **VOTA_no_ae 99.41 vs registry 99.40**：1183/1190=99.41%，registry 四舍五入。
10. **CL full_trace "79.9"**（1 位小数）：其他 cell 均 2 位。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_audit_final-maintext-tables_20260523T191655"
}
```

</details>

---
