# paper writing experiments d032

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 45
- **Recorded user turns:** 0
- **Tool calls:** 22
- **Original source:** `logs/chats/worker_paper_writing_experiments_d032_20260517T154238.jsonl`
- **Structured JSON:** [`ff650c5a22e84190ae76.json`](../../sessions/ff/ff650c5a22e84190ae76.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

45 recorded events

### Tool call

_source line 1 · 2026-05-17T15:56:52.721278+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Explore paper structure and framing",
  "prompt": "I need to understand the paper structure for the contrastive_trace_safety project. Please:\n\n1. List all files in /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/ recursively\n2. Read /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/ — list all .tex files there\n3. Read the main paper .tex file (likely main.tex or paper.tex) to see how sections are included and what packages are used\n4. Check if there's a paper_framing.md file anywhere in the project\n5. Check if there's an existing experiments.tex file\n\nReport file paths and key content (packages used, section structure, any existing table definitions)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experiments_d032_20260517T154238",
  "tool": "Agent",
  "tool_args": {
    "subagent_type": "Explore",
    "description": "Explore paper structure and framing",
    "prompt": "I need to understand the paper structure for the contrastive_trace_safety project. Please:\n\n1. List all files in /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/ recursively\n2. Read /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/ — list all .tex files there\n3. Read the main paper .tex file (likely main.tex or paper.tex) to see how sections are included and what packages are used\n4. Check if there's a paper_framing.md file anywhere in the project\n5. Check if there's an existing experiments.tex file\n\nReport file paths and key content (packages used, section structure, any existing table definitions)."
  }
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-17T15:56:52.721679+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper -type f -name \"*.tex\" 2>/dev/null | head -50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experiments_d032_20260517T154238",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper -type f -name \"*.tex\" 2>/dev/null | head -50"
  }
}
```

</details>

---

### Tool result

_source line 3 · 2026-05-17T15:56:52.721867+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/main.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_d032_20260517T154238",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-17T15:56:52.722017+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper -type f | sort"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experiments_d032_20260517T154238",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper -type f | sort"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-17T15:56:52.722155+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/_pdf_images/main_p10.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/_pdf_images/main_p7.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/_pdf_images/main_p8.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/_pdf_images/main_p9.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/acl.sty
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/acl2023.sty
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/acl_natbib.bst
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/figures/fig2_temporal_improvement.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/figures/fig3_model_dependency.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/figures/fig3_model_dependency.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/figures/pareto_two_stage.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/main.aux
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/main.bbl
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/main.blg
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/main.fdb_latexmk
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/main.fls
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/main.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/pap
…[truncated 1374 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_d032_20260517T154238",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-17T15:56:52.722316+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety -name \"paper_framing.md\" -o -name \"paper_framing.yaml\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experiments_d032_20260517T154238",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety -name \"paper_framing.md\" -o -name \"paper_framing.yaml\""
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-17T15:56:52.722442+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260516T212347/median/paper_framing.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260516T212347/worst/paper_framing.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260516T212347/best/paper_framing.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260516T194646/median/paper_framing.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260516T194646/worst/paper_framing.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260516T194646/best/paper_framing.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260516T203948/median/paper_framing.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260516T203948/worst/paper_framing.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260516T203948/best/paper_framing.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/paper_framing.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_d032_20260517T154238",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-17T15:56:52.722575+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experiments_d032_20260517T154238",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-17T15:56:52.722724+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage{graphicx}
6	\usepackage{amsmath}
7	\usepackage{amssymb}
8	\usepackage{booktabs}
9	\usepackage{multirow}
10	\usepackage{subcaption}
11	\usepackage{xcolor}
12	\usepackage{colortbl}
13	\usepackage{hyperref}
14	\usepackage{cleveref}
15	
16	\title{Temporal Probing for Safety Commitment Detection in Reasoning Models}
17	
18	\author{Anonymous ARR Submission}
19	
20	\begin{document}
21	\maketitle
22	
23	\begin{abstract}
24	\input{sections/abstract}
25	\end{abstract}
26	
27	\input{sections/introduction}
28	
29	\input{sections/related_work}
30	
31	\input{sections/method}
32	
33	\input{sections/experiments}
34	
35	\input{sections/conclusion}
36	
37	\input{sections/limitations}
38	
39	\bibliography{references}
40	
41	\input{sections/appendix}
42	
43	\end{document}
44	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_d032_20260517T154238",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-17T15:56:52.722868+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experiments_d032_20260517T154238",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/paper_framing.md"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-17T15:56:52.723052+00:00_

1	# Paper Framing — contrastive_trace_safety
2	
3	## Target Venue
4	- Primary: EMNLP 2026 Main (LLM Security Track)
5	- Deadline: ARR submission May 25, 2026
6	
7	## Core Claims (D031: layer selection as primary contribution, 4 models)
8	
9	**Contribution structure (D031)**:
10	- **Primary (methodological)**: Layer selection metric sensitivity — biased metrics reverse conclusions
11	- **Secondary (empirical)**: HS advantage at correct layers, qualified by scale; temporal improvement universal
12	- **Tertiary (negative results)**: 6 alternative methods fail, establishing what doesn't work
13	
14	1. **Temporal context universally improves probe accuracy across both modalities** (D014 + D023 nuanced) — Temporal context is the most robust improvement across all 4 models and both modalities. Text probes benefit consistently from larger windows across all models. HS probes benefit in 3/4 models; OT-7B HS peaks at W=3 and declines at larger W (confirmed on both layer 0 and layer 16).
15	
16	   **HS temporal gains** (W=1→best, 3 original models): accuracy +3pp (77.8%→81.0%), precision +13pp (69.3%→82.2%), FPR halved (9.65%→4.83%).
17	   **OT-7B HS temporal** (layer 16): bal_acc peaks at W=3 (68.8%), declines to 65.9% at W=25 (-2.9pp). BUT precision and FPR continue improving (prec 42.8%→49.4%, FPR 12.0%→7.5%). Temporal saturation is bal_acc-specific; larger W trades bal_acc for better precision/FPR. Confirmed on both layer 0 and layer 16 — genuine OT-7B characteristic.
18	   **Text temporal gains** (all 4 models, W=1→best): universally +3-12pp bal_acc, +8-23pp precision, FPR reduced.
19	
20	   **IMPORTANT: coverage direction depends on detection criterion K.** K=1 (single crossing): coverage DECREASES with W. K=5 (consecutive crossings): coverage may INCREASE with W. Claim 1 is about accuracy/precision improvement, NOT coverage.
21	
22	   The core insight: "Temporal context universally improves text probes across all 4 models. For HS probes, 3/4 models benefit from larger t
…[truncated 22618 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_d032_20260517T154238",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-17T15:56:52.723209+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experiments_d032_20260517T154238",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-17T15:56:52.723373+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We evaluate contrastive trace probes across four reasoning models (R1-8B, OT-7B, R1-32B, QwQ-32B), two signal modalities (hidden states and text), and multiple temporal aggregation strategies. Our experiments address four questions: (1) How much does temporal context improve detection? (2) Does the choice of signal modality matter? (3) Can sequence models detect unsafe reasoning earlier? (4) Do probes transfer across models?
5	
6	\subsection{Temporal Context as Primary Factor}
7	\label{sec:temporal_primary}
8	
9	The most consistent finding across all experimental conditions is that temporal context improves probe precision and reduces FPR across all four models and both modalities. For HS probes, all four models show improving precision and FPR with larger windows; OT-7B balanced accuracy is the exception, peaking at $W{=}3$ and declining at larger windows while its precision and FPR continue to improve. \cref{fig:window_ablation} shows the pattern for R1-8B.
10	
11	\begin{figure}[t]
12	\centering
13	\includegraphics[width=\columnwidth]{figures/fig2_temporal_improvement.pdf}
14	\caption{Effect of temporal window size on R1-8B HS probe performance. Precision increases monotonically from 69.3\% ($W{=}1$) to 82.2\% ($W{=}25$); FPR decreases from 9.65\% to 4.83\%. Coverage decreases as larger windows make the probe more conservative.}
15	\label{fig:window_ablation}
16	\end{figure}
17	
18	On R1-8B, increasing window size from $W{=}1$ to $W{=}25$ improves balanced accuracy from 77.8\% to 81.0\% (+3.2pp), precision from 69.3\% to 82.2\% (+12.9pp), and reduces step-level FPR from 9.65\% to 4.83\% ($-$4.8pp). QwQ-32B shows a similar monotonic pattern (+3.2pp accuracy, +7.4pp precision, $-$5.9pp FPR from $W{=}1$ to $W{=}25$). R1-32B exhibits a non-monotonic trajectory: accuracy peaks at $W{=}10$ then declines below the $W{=}1$ baseline by $W{=}25$ (71.8\% $\rightarrow$ 70.3\%), though precision and FPR still improve (+1.7
…[truncated 14094 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_d032_20260517T154238",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-17T15:56:52.723526+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/introduction.tex",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experiments_d032_20260517T154238",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/introduction.tex",
    "limit": "50"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-17T15:56:52.723680+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Reasoning models such as DeepSeek-R1~\cite{deepseekr1} and QwQ~\cite{qwq} have advanced language model capabilities by scaling chain-of-thought (CoT) inference, producing extended internal deliberation before generating final responses. These models interleave safety-aware reasoning with content generation across dozens of reasoning steps, and this very capacity for self-reflection introduces a new failure mode. Recent work has documented that reasoning models can ``self-jailbreak'': even without adversarial input modifications, the model's own CoT may transition from considering safety constraints to committing to produce harmful content~\cite{harmthoughts,selfjailbreak}. In such cases, the model's reasoning trace contains a \textbf{Safety Commitment Point} (CP), the first step after which safety reasoning permanently ceases and harmful generation proceeds unchecked. Detecting this transition in real time is essential for monitoring systems that must intervene before harmful content reaches users.
4	
5	Existing safety detectors were designed for a different threat model. Methods based on hidden-state (HS) probing, such as TrajGuard~\cite{trajguard} and SafeSwitch~\cite{safeswitch}, monitor internal activations to classify adversarial inputs and achieve high accuracy (above 95\%) on standard Large Language Models (LLMs). Text-based monitors like SafeRemind~\cite{saferemind} and SafeThink~\cite{safethink} scan generated reasoning text for safety violations. Both families target external attacks on model inputs rather than the model's own internal commitment process. A fundamental question remains unanswered: when detecting safety commitment within multi-step reasoning, should a monitoring system read the model's hidden states or its generated text? Intuition suggests that HS features (4096 dimensions of internal computation) should be far more informative than text embeddings (384 dimensions from a sentence encode
…[truncated 3783 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_d032_20260517T154238",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-17T15:56:52.723828+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/method.tex",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experiments_d032_20260517T154238",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/method.tex",
    "limit": "50"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-17T15:56:52.723970+00:00_

1	\section{Problem Setup and Methods}
2	\label{sec:method}
3	
4	\subsection{Safety Commitment Point}
5	\label{sec:commitment-point}
6	
7	When a reasoning model is jailbroken, its chain-of-thought (CoT) transitions from safety-aware deliberation to committed harmful generation. We define the \textbf{Safety Commitment Point} (CP) as the first reasoning step after which safety reasoning permanently ceases. Formally, given a trace of $T$ reasoning steps, the CP is the earliest step $t^*$ such that no step $t > t^*$ contains safety-relevant deliberation. Steps before CP are \emph{pre-commitment} (the model is still considering refusal); steps at or after CP are \emph{post-commitment} (the model has irrevocably committed to harmful output).
8	
9	We operationalize this definition on HarmThoughts~\citep{harmthoughts} traces, which provide step-level annotations of safety reasoning. Each step receives a binary label: pre-CP ($y_t = 0$ for $t < t^*$) or post-CP ($y_t = 1$ for $t \geq t^*$). The detection task is binary classification at each step, producing a score $s_t \in [0, 1]$ that estimates the probability that the model has passed its commitment point by step $t$.
10	
11	We study four reasoning models spanning two architectures (Llama and Qwen) and two parameter scales (7--8B and 32B), summarized in \cref{tab:models}.
12	
13	\begin{table}[t]
14	\centering
15	\small
16	\begin{tabular}{lcccccc}
17	\toprule
18	\textbf{Model} & \textbf{Arch.} & \textbf{Params} & \textbf{Layers} & \textbf{Hidden} & \textbf{Traces} & \textbf{Test} \\
19	\midrule
20	R1-8B & Llama & 8B & 32 & 4096 & 209 & 43 \\
21	OT-7B & Qwen & 7B & 28 & 3584 & 228 & 47 \\
22	R1-32B & Qwen & 32B & 64 & 5120 & 100 & 20 \\
23	QwQ-32B & Qwen & 32B & 64 & 5120 & 95 & 19 \\
24	\bottomrule
25	\end{tabular}
26	\caption{Models studied. R1-8B and R1-32B are distilled from DeepSeek-R1~\citep{deepseekr1}; QwQ-32B~\citep{qwq} is a native reasoning model; OT-7B~\citep{openthinker} is trained with STILL~\citep{still} on Qw
…[truncated 3503 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_d032_20260517T154238",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-17T15:56:52.724119+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -lah /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/ | grep -E \"\\.(sty|bst|bib)\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experiments_d032_20260517T154238",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -lah /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/ | grep -E \"\\.(sty|bst|bib)\""
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-17T15:56:52.724235+00:00_

-rw-r--r-- 1 ubuntu ubuntu  12K May 17 03:08 acl.sty
-rw-r--r-- 1 ubuntu ubuntu  12K May 16 23:17 acl2023.sty
-rw-r--r-- 1 ubuntu ubuntu  45K May 16 23:17 acl_natbib.bst
-rw-r--r-- 1 ubuntu ubuntu  13K May 17 08:59 references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_d032_20260517T154238",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-17T15:56:52.724405+00:00_

Perfect! Now let me get a summary of the structure:

## Paper Structure Summary

Based on my exploration of the contrastive_trace_safety project, here is the complete paper structure:

### 1. **File Organization**

**Main Paper Directory:** `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/`

**Structure:**
```
paper/
├── main.tex                    (Primary entry point)
├── references.bib              (Bibliography)
├── acl.sty / acl2023.sty      (ACL conference style files)
├── acl_natbib.bst            (Bibliography style)
├── sections/
│   ├── abstract.tex
│   ├── introduction.tex
│   ├── related_work.tex
│   ├── method.tex
│   ├── experiments.tex
│   ├── conclusion.tex
│   ├── limitations.tex
│   └── appendix.tex
├── figures/
│   ├── fig2_temporal_improvement.pdf
│   ├── fig3_model_dependency.pdf
│   └── pareto_two_stage.pdf
└── main.pdf                   (Compiled output)
```

### 2. **Main .tex File Packages and Structure**

**File:** `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/main.tex`

**Packages Used:**
- `acl` with `review` option
- `times`, `latexsym`, `graphicx`
- `amsmath`, `amssymb`
- `booktabs`, `multirow`, `subcaption`
- `xcolor`, `colortbl`
- `hyperref`, `cleveref`

**Section Inclusion Order:**
1. Abstract
2. Introduction
3. Related Work
4. Method (Problem Setup and Methods)
5. Experiments
6. Conclusion
7. Limitations
8. Bibliography
9. Appendix

**Title:** "Temporal Probing for Safety Commitment Detection in Reasoning Models"

### 3. **Section Files Overview**

- **introduction.tex** — Establishes problem of safety commitment detection in reasoning models, motivates comparison of hidden-state vs. text modalities, presents three main contributions
- **method.tex** — Defines Safety Commitment Point (CP), details probe architectures (HS probes, text probes, GRU), temporal windowing strategy (W ∈ {1,3,5,10,15,20,25}), and critically, the layer selection sens
…[truncated 2519 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_d032_20260517T154238",
  "tool": "Agent",
  "elapsed_ms": 3
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-17T15:56:52.724591+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experiments_d032_20260517T154238",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-17T15:56:52.724899+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We evaluate contrastive trace probes across four reasoning models (R1-8B, OT-7B, R1-32B, QwQ-32B), two signal modalities (hidden states and text), and multiple temporal aggregation strategies. Our experiments address four questions: (1) How much does temporal context improve detection? (2) Does the choice of signal modality matter? (3) Can sequence models detect unsafe reasoning earlier? (4) Do probes transfer across models?
5	
6	\subsection{Temporal Context as Primary Factor}
7	\label{sec:temporal_primary}
8	
9	The most consistent finding across all experimental conditions is that temporal context improves probe precision and reduces FPR across all four models and both modalities. For HS probes, all four models show improving precision and FPR with larger windows; OT-7B balanced accuracy is the exception, peaking at $W{=}3$ and declining at larger windows while its precision and FPR continue to improve. \cref{fig:window_ablation} shows the pattern for R1-8B.
10	
11	\begin{figure}[t]
12	\centering
13	\includegraphics[width=\columnwidth]{figures/fig2_temporal_improvement.pdf}
14	\caption{Effect of temporal window size on R1-8B HS probe performance. Precision increases monotonically from 69.3\% ($W{=}1$) to 82.2\% ($W{=}25$); FPR decreases from 9.65\% to 4.83\%. Coverage decreases as larger windows make the probe more conservative.}
15	\label{fig:window_ablation}
16	\end{figure}
17	
18	On R1-8B, increasing window size from $W{=}1$ to $W{=}25$ improves balanced accuracy from 77.8\% to 81.0\% (+3.2pp), precision from 69.3\% to 82.2\% (+12.9pp), and reduces step-level FPR from 9.65\% to 4.83\% ($-$4.8pp). QwQ-32B shows a similar monotonic pattern (+3.2pp accuracy, +7.4pp precision, $-$5.9pp FPR from $W{=}1$ to $W{=}25$). R1-32B exhibits a non-monotonic trajectory: accuracy peaks at $W{=}10$ then declines below the $W{=}1$ baseline by $W{=}25$ (71.8\% $\rightarrow$ 70.3\%), though precision and FPR still improve (+1.7
…[truncated 14094 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_d032_20260517T154238",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-17T15:56:52.725064+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experiments_d032_20260517T154238",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/paper_framing.md"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-17T15:56:52.725304+00:00_

1	# Paper Framing — contrastive_trace_safety
2	
3	## Target Venue
4	- Primary: EMNLP 2026 Main (LLM Security Track)
5	- Deadline: ARR submission May 25, 2026
6	
7	## Core Claims (D031: layer selection as primary contribution, 4 models)
8	
9	**Contribution structure (D031)**:
10	- **Primary (methodological)**: Layer selection metric sensitivity — biased metrics reverse conclusions
11	- **Secondary (empirical)**: HS advantage at correct layers, qualified by scale; temporal improvement universal
12	- **Tertiary (negative results)**: 6 alternative methods fail, establishing what doesn't work
13	
14	1. **Temporal context universally improves probe accuracy across both modalities** (D014 + D023 nuanced) — Temporal context is the most robust improvement across all 4 models and both modalities. Text probes benefit consistently from larger windows across all models. HS probes benefit in 3/4 models; OT-7B HS peaks at W=3 and declines at larger W (confirmed on both layer 0 and layer 16).
15	
16	   **HS temporal gains** (W=1→best, 3 original models): accuracy +3pp (77.8%→81.0%), precision +13pp (69.3%→82.2%), FPR halved (9.65%→4.83%).
17	   **OT-7B HS temporal** (layer 16): bal_acc peaks at W=3 (68.8%), declines to 65.9% at W=25 (-2.9pp). BUT precision and FPR continue improving (prec 42.8%→49.4%, FPR 12.0%→7.5%). Temporal saturation is bal_acc-specific; larger W trades bal_acc for better precision/FPR. Confirmed on both layer 0 and layer 16 — genuine OT-7B characteristic.
18	   **Text temporal gains** (all 4 models, W=1→best): universally +3-12pp bal_acc, +8-23pp precision, FPR reduced.
19	
20	   **IMPORTANT: coverage direction depends on detection criterion K.** K=1 (single crossing): coverage DECREASES with W. K=5 (consecutive crossings): coverage may INCREASE with W. Claim 1 is about accuracy/precision improvement, NOT coverage.
21	
22	   The core insight: "Temporal context universally improves text probes across all 4 models. For HS probes, 3/4 models benefit from larger t
…[truncated 22618 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_d032_20260517T154238",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-17T15:56:52.725462+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experiments_d032_20260517T154238",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-17T15:56:52.725613+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage{graphicx}
6	\usepackage{amsmath}
7	\usepackage{amssymb}
8	\usepackage{booktabs}
9	\usepackage{multirow}
10	\usepackage{subcaption}
11	\usepackage{xcolor}
12	\usepackage{colortbl}
13	\usepackage{hyperref}
14	\usepackage{cleveref}
15	
16	\title{Temporal Probing for Safety Commitment Detection in Reasoning Models}
17	
18	\author{Anonymous ARR Submission}
19	
20	\begin{document}
21	\maketitle
22	
23	\begin{abstract}
24	\input{sections/abstract}
25	\end{abstract}
26	
27	\input{sections/introduction}
28	
29	\input{sections/related_work}
30	
31	\input{sections/method}
32	
33	\input{sections/experiments}
34	
35	\input{sections/conclusion}
36	
37	\input{sections/limitations}
38	
39	\bibliography{references}
40	
41	\input{sections/appendix}
42	
43	\end{document}
44	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_d032_20260517T154238",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-17T15:56:52.725782+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experiments_d032_20260517T154238",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-17T15:56:52.725970+00:00_

1	\section{Problem Setup and Methods}
2	\label{sec:method}
3	
4	\subsection{Safety Commitment Point}
5	\label{sec:commitment-point}
6	
7	When a reasoning model is jailbroken, its chain-of-thought (CoT) transitions from safety-aware deliberation to committed harmful generation. We define the \textbf{Safety Commitment Point} (CP) as the first reasoning step after which safety reasoning permanently ceases. Formally, given a trace of $T$ reasoning steps, the CP is the earliest step $t^*$ such that no step $t > t^*$ contains safety-relevant deliberation. Steps before CP are \emph{pre-commitment} (the model is still considering refusal); steps at or after CP are \emph{post-commitment} (the model has irrevocably committed to harmful output).
8	
9	We operationalize this definition on HarmThoughts~\citep{harmthoughts} traces, which provide step-level annotations of safety reasoning. Each step receives a binary label: pre-CP ($y_t = 0$ for $t < t^*$) or post-CP ($y_t = 1$ for $t \geq t^*$). The detection task is binary classification at each step, producing a score $s_t \in [0, 1]$ that estimates the probability that the model has passed its commitment point by step $t$.
10	
11	We study four reasoning models spanning two architectures (Llama and Qwen) and two parameter scales (7--8B and 32B), summarized in \cref{tab:models}.
12	
13	\begin{table}[t]
14	\centering
15	\small
16	\begin{tabular}{lcccccc}
17	\toprule
18	\textbf{Model} & \textbf{Arch.} & \textbf{Params} & \textbf{Layers} & \textbf{Hidden} & \textbf{Traces} & \textbf{Test} \\
19	\midrule
20	R1-8B & Llama & 8B & 32 & 4096 & 209 & 43 \\
21	OT-7B & Qwen & 7B & 28 & 3584 & 228 & 47 \\
22	R1-32B & Qwen & 32B & 64 & 5120 & 100 & 20 \\
23	QwQ-32B & Qwen & 32B & 64 & 5120 & 95 & 19 \\
24	\bottomrule
25	\end{tabular}
26	\caption{Models studied. R1-8B and R1-32B are distilled from DeepSeek-R1~\citep{deepseekr1}; QwQ-32B~\citep{qwq} is a native reasoning model; OT-7B~\citep{openthinker} is trained with STILL~\citep{still} on Qw
…[truncated 11679 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_d032_20260517T154238",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-17T15:56:52.726491+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/experiments.tex",
  "content": "\\section{Experiments}\\label{sec:experiments}\n\nWe evaluate temporal probes across four reasoning models (\\cref{tab:models}), comparing hidden-state (HS) and text modalities under different layer selection criteria. Our experiments address three questions: (1)~Does the layer selection metric determine whether HS probes appear effective? (2)~Do HS probes outperform text probes at correctly selected layers? (3)~Which alternative detection methods fail, and why?\n\n\\subsection{Experimental Setup}\\label{sec:setup}\n\n\\paragraph{Models and data.} We study four models spanning two architectures and two parameter scales: R1-8B (Llama-8B, R1-distilled, $n{=}43$ test traces), OT-7B (Qwen-7B, STILL-trained, $n{=}47$), QwQ-32B (Qwen-32B, native reasoning, $n{=}19$--$20$), and R1-32B (Qwen-32B, R1-distilled, $n{=}20$). All traces come from HarmThoughts with step-level commitment point (CP) annotations. We use a 60/20/20 train/validation/test split across all models (\\cref{tab:models}).\n\n\\paragraph{Training and evaluation.} All probes use L2-regularized logistic regression with balanced class weights. For each model, we select the temporal window $W$ on the validation set from $W \\in \\{1, 3, 5, 10, 15, 20, 25\\}$. HS probes extract last-token hidden states from a selected transformer layer; text probes encode each reasoning step with all-MiniLM-L6-v2 (384 dimensions). Detection requires $K{=}5$ consecutive threshold crossings. Modality comparisons use a two-sided null-centered bootstrap test (1000 resamples) with Holm-Bonferroni step-down correction across 12 tests (3 metrics $\\times$ 4 models, $\\alpha{=}0.05$).\n\n\\paragraph{Layer selection.} We evaluate five layer selection metrics per model (\\cref{sec:layer-sensitivity}). The biased composite metric (balanced accuracy $\\times$ crossing rate) systematically selects shallow layers for 32B models because representational volatility at early layers inflates the crossing rate component. Four unbiased metrics (pure balanced accuracy, precision, inverse FPR, and an additive composite) converge on deep layers. Results throughout this section use the corrected deep layers, with explicit comparison to biased-layer outcomes in \\cref{sec:layer-results}.\n\n\\subsection{Layer Selection Results}\\label{sec:layer-results}\n\n\\cref{tab:layer_selection} presents the layer selected by the biased composite metric and the consensus of four unbiased metrics across all four models. For R1-8B, all five metrics agree on layer~14 (44\\% depth), with no discrepancy. For the remaining three models, the biased metric selects shallow layers: L0 (0\\%) for OT-7B, L2 (3\\%) for QwQ-32B, and L10 (16\\%) for R1-32B. All four unbiased metrics converge on deep layers: L16 (57\\%) for OT-7B, L60 (94\\%) for QwQ-32B, and L63 (98\\%) for R1-32B. The bias is most extreme for the 64-layer 32B models, where the composite metric selects layers in the bottom 16\\% of the network while all other metrics select layers above 94\\%.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Model} & \\textbf{Biased}$^a$ & \\textbf{Corrected}$^b$ & $p$ \\textbf{(corr.)} \\\\\n\\midrule\nR1-8B & L14 (44\\%) & L14 (44\\%) & ${<}0.001$ \\\\\nOT-7B & L0 (0\\%)$^c$ & L16 (57\\%) & ${<}0.001$ \\\\\nQwQ-32B & L2 (3\\%) & L60 (94\\%) & ${<}0.005$ \\\\\nR1-32B & L10 (16\\%) & L63 (98\\%) & ${<}0.001$ \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Layer selection sensitivity. $^a$\\,Selected by bal\\_acc $\\times$ crossing\\_rate. $^b$\\,Consensus of four unbiased metrics (pure bal\\_acc, precision, inverse FPR, additive composite). $^c$\\,OT-7B has only 28 layers; bias is less extreme than for 64-layer models. The rightmost column reports HS vs.\\ text precision $p$-values at the corrected layer (two-sided null-centered bootstrap, 1000 resamples). At the \\emph{biased} layers for 32B models, corresponding $p$-values were 0.064 (R1-32B) and 0.35--0.83 (QwQ-32B), both non-significant.}\n\\label{tab:layer_selection}\n\\end{table}\n\nThe downstream impact on modality comparison is severe for the 32B models. At biased layers, two-sided bootstrap $p$-values for HS precision advantage are 0.064 for R1-32B (not significant) and 0.35--0.83 for QwQ-32B (not significant). At the corrected deep layers, all $p$-values drop below 0.005. The R1-32B case illustrates the magnitude of this effect: the biased metric selects L10 (16\\% depth, precision $p{=}0.064$), while pure balanced accuracy selects L63 (98\\% depth, $p{<}0.001$). For QwQ-32B, the shift is from L2 ($p{=}0.35$--$0.83$) to L60 ($p{<}0.005$ across all 15 window sizes tested). OT-7B represents an intermediate case: the biased metric selects L0 (0\\%), but OT-7B has only 28 layers, so the practical impact is smaller than for 64-layer models. The corrected layer (L16, 57\\% depth) still produces stronger HS-text separation ($p{<}0.001$ on all three metrics).\n\nThis sensitivity analysis reveals that a single metric component (crossing rate) can reverse a study's central conclusion. Had we reported only biased-layer results, we would have concluded that the HS advantage is scale-dependent: significant at 7--8B, absent at 32B. The corrected analysis shows HS advantage across all four models, with the apparent scale-dependence being a methodological artifact of biased layer selection.\n\n\\subsection{HS vs.\\ Text Comparison}\\label{sec:hs-text}\n\n\\cref{tab:hs_vs_text} presents the main HS vs.\\ text comparison at corrected layers. All 12 hypothesis tests (3 metrics $\\times$ 4 models) pass Holm-Bonferroni step-down correction at $\\alpha{=}0.05$. At the previously used biased layers, only 5 of 12 tests passed (all from the two 7--8B models that were unaffected by the metric bias). The corrected analysis recovers all 7 previously failing tests across the full battery.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{llcrrrr}\n\\toprule\n\\textbf{Model} & \\textbf{Layer} & $W$ & $\\Delta$\\textbf{BA} & $\\Delta$\\textbf{Prec} & $\\Delta$\\textbf{FPR} & \\textbf{HB} \\\\\n\\midrule\nR1-8B & L14 & 15 & +8.2 & +22.4 & $-$7.4 & 3/3 \\\\\nOT-7B & L16 & 3 & +10.9 & +21.2 & $-$17.1 & 3/3 \\\\\nQwQ & L60 & 3 & +15.4 & \\textbf{+23.6} & $-$9.8 & 3/3 \\\\\nR1-32B & L63 & 1 & \\textbf{+18.7} & +15.4 & \\textbf{$-$14.6} & 3/3 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{HS vs.\\ text probe comparison at corrected layers. $\\Delta$BA, $\\Delta$Prec, and $\\Delta$FPR report the HS$-$text difference in percentage points for balanced accuracy, precision, and pre-CP false positive rate. HB: tests passing Holm-Bonferroni step-down ($\\alpha{=}0.05$, 12 tests total). All comparisons use a two-sided null-centered bootstrap (1000 resamples). $W$: validation-selected temporal window per model.}\n\\label{tab:hs_vs_text}\n\\end{table}\n\n\\paragraph{7--8B models.} R1-8B ($n{=}43$, L14, $W{=}15$) shows HS advantages of +8.2pp balanced accuracy ($p{=}0.005$), +22.4pp precision ($p{<}0.001$), and $-$7.4pp FPR ($p{=}0.044$). All three survive Holm-Bonferroni correction. OT-7B ($n{=}47$, L16, matched $W{=}3$) shows +10.9pp balanced accuracy ($p{<}0.001$), +21.2pp precision ($p{<}0.001$), and $-$17.1pp FPR ($p{<}0.001$), with all three tests surviving correction. The precision advantage is consistent across these architecturally distinct models: +22.4pp on the Llama-based R1-8B and +21.2pp on the Qwen-based OT-7B, despite different training methods (R1 distillation vs.\\ STILL).\n\n\\paragraph{32B models.} QwQ-32B ($n{=}19$--$20$, L60, $W{=}3$) shows +15.4pp balanced accuracy ($p{<}0.001$), +23.6pp precision ($p{<}0.001$), and $-$9.8pp FPR ($p{=}0.004$), all surviving correction. R1-32B ($n{=}20$, L63, $W{=}1$) shows +18.7pp balanced accuracy ($p{<}0.001$), +15.4pp precision ($p{<}0.001$), and $-$14.6pp FPR ($p{=}0.007$), all surviving correction. The precision advantage ranges from +15.4 to +23.6pp across all four models.\n\n\\paragraph{Control task selectivity.} Following \\citet{hewitt2019control}, selectivity scores confirm genuine safety signal beyond positional artifacts: R1-8B 12.5pp, OT-7B 18.3pp, QwQ-32B 15.3pp, R1-32B 7.5pp. All four models exceed the 5pp threshold.\n\n\\paragraph{Caveats.} Three qualifications apply. First, the validation-selected $W$ differs per model ($W{=}15$ for R1-8B, $W{=}3$ for OT-7B and QwQ-32B, $W{=}1$ for R1-32B). The tests measure whether HS outperforms text at each model's best operating point, not at a uniform window. Second, R1-32B at $W{=}1$ achieves only 25\\% coverage (5 of 20 test traces detected), which limits practical utility despite strong per-detection performance. At $W{\\geq}3$, R1-32B significance vanishes due to the dimensionality constraint ($51200 \\times W$ features for $n{=}20$ training traces). Third, QwQ-32B HS lead time is negative ($-$1.2 to +1.9 steps) compared to text probes (3.7 to 12.3 steps): HS probes are more accurate but detect later on this model. In safety deployment, earlier detection by several steps may outweigh higher per-step accuracy.\n\n\\subsection{Temporal Context Effects}\\label{sec:temporal}\n\nText probes benefit universally from larger temporal windows across all four models. Balanced accuracy improves by +3 to +12pp and precision by +8 to +23pp from $W{=}1$ to $W{=}25$, with consistent FPR reductions.\n\nHS probes show similar benefits on 3 of 4 models. On R1-8B (L14), increasing $W$ from 1 to 25 improves balanced accuracy from 77.8\\% to 81.0\\% (+3.2pp), precision from 69.3\\% to 82.2\\% (+12.9pp), and reduces FPR from 9.65\\% to 4.8\\% ($-$4.9pp). At the validation-selected $W{=}15$, performance reaches 80.2\\% balanced accuracy, 77.7\\% precision, and 6.4\\% FPR, which captures most of the precision gain with higher coverage than $W{=}25$. QwQ-32B and R1-32B follow similar monotonic patterns for precision and FPR across the full $W$ range.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig2_temporal_improvement.pdf}\n\\caption{Effect of temporal window size on R1-8B HS probe performance (L14). Precision increases monotonically from 69.3\\% ($W{=}1$) to 82.2\\% ($W{=}25$); FPR decreases from 9.65\\% to 4.8\\%.}\n\\label{fig:window_ablation}\n\\end{figure}\n\nOT-7B is the exception. HS balanced accuracy peaks at $W{=}3$ (68.8\\%) and declines to 65.9\\% at $W{=}25$ ($-$2.9pp). Precision and FPR continue to improve: precision rises from 42.8\\% ($W{=}1$) to 49.4\\% ($W{=}25$), and FPR drops from 12.0\\% to 7.5\\%. The saturation is specific to balanced accuracy; larger windows trade balanced accuracy for better precision and lower FPR. This pattern holds on both L0 and L16, which confirms it as a genuine OT-7B characteristic rather than a layer-specific artifact. The validation selection of $W{=}3$ reflects this trade-off: balanced accuracy is maximized without sacrificing the precision gains available at moderate windows.\n\nThe consistent finding across all four models is that precision improvement (+1.7 to +12.9pp from $W{=}1$ to best) and FPR reduction ($-$4.0 to $-$5.9pp) are positive for both modalities (\\cref{fig:window_ablation}). Temporal context provides the most robust source of discriminative information for false positive reduction. Observing multiple reasoning steps matters more than the choice of signal modality. Larger windows make probes more conservative, reducing coverage but improving confidence on detected traces. Deployment systems would tune $K$ alongside $W$ to balance coverage against precision.\n\n\\subsection{32B Model-Specific Analysis}\\label{sec:32b-analysis}\n\nThe two 32B models present contrasting detection profiles despite sharing the Qwen-32B architecture (\\cref{tab:32b_divergence}). Per-model analysis is required; a unified scale-level narrative would obscure important differences.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Dimension} & \\textbf{R1-32B (L63)} & \\textbf{QwQ (L60)} \\\\\n\\midrule\nHolm-Bonf.\\ sig.\\ & $W{=}1$ only (3/3) & All 15 $W$ (3/3) \\\\\nLead time (steps) & +11.7 to +13.3 & $-$1.2 to +1.9 \\\\\nHS vs.\\ Position & +14.2pp & $-$0.6pp \\\\\nCoverage ($W{=}1$) & 25\\% & 74\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{32B cross-model divergence. R1-32B provides excellent early warning with narrow coverage; QwQ-32B provides robust significance with poor lead time.}\n\\label{tab:32b_divergence}\n\\end{table}\n\n\\paragraph{R1-32B (L63, $W{=}1$).} R1-32B achieves excellent lead time (+11.7 to +13.3 steps before commitment), and the HS probe strongly outperforms the position-only baseline (+14.2pp balanced accuracy). These properties make R1-32B the strongest candidate for early warning among the four models. The limitation is statistical narrowness: only $W{=}1$ passes Holm-Bonferroni (3/3 metrics), with $W{\\geq}3$ non-significant due to dimensionality ($51200 \\times W$ features for $n{=}20$ traces). At $W{=}1$, coverage is 25\\% (5 of 20 traces detected). The evidence supports HS superiority on R1-32B but under restrictive operating conditions.\n\n\\paragraph{QwQ-32B (L60, $W{=}3$).} QwQ-32B shows the most robust statistical significance of any model: HS outperforms text at all 15 window sizes tested ($p{<}0.005$), with 74\\% coverage at $W{=}1$. The limitation is detection timing: HS lead time is negative ($-$1.2 to +1.9 steps), compared to text probes (3.7 to 12.3 steps). The position-only baseline achieves comparable balanced accuracy (0.746 vs.\\ HS 0.740). HS probes are more precise but detect later, and they offer minimal advantage over simple positional features for this model.\n\nThe complementary profiles suggest that the practical value of HS monitoring depends on model-specific detection requirements. Early warning applications favor R1-32B's high lead time despite narrow coverage. Broad reliable detection applications favor QwQ-32B's robust significance despite poor timing. These divergent patterns within the same architecture underscore that per-model validation is essential.\n\n\\subsection{Negative Results}\\label{sec:negative}\n\n\\cref{tab:negative} summarizes seven alternative detection approaches that fail to match supervised temporal probing. The failures span change-point detection, geometric methods, direction-based probing, nonlinear models, semi-supervised learning, and cross-model transfer.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{p{1.5cm}p{2.9cm}p{2.3cm}}\n\\toprule\n\\textbf{Method} & \\textbf{Result} & \\textbf{Failure Mode} \\\\\n\\midrule\nBOCPD & R1-8B 93\\% det., lead +3.5 $<$ thresh.\\ +4.9; others 0\\% & Commitment gradual \\\\\nCUSUM & Worse than threshold, all models & Same as BOCPD \\\\\nMahalanobis & $\\Delta d \\approx 0$ (R1-8B +0.07, OT-7B +0.03) & Signal in minor PCA dirs. \\\\\nRepE & R1-8B 74.9\\% vs.\\ LR 81.7\\%$^a$ & Direction insufficient \\\\\nMLP & 3/4 worse than LR & Overfitting ($n$ small) \\\\\nCCS$^b$ & R1-8B 77.7\\%; R1-32B FPR\\,=\\,0.41 & No gain over supervised \\\\\nTransfer & Best 58.3\\%, all fail & Model-specific repr. \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Negative results. $^a$\\,RepE results use layers from the biased metric; evaluation at corrected layers is pending for 32B models. $^b$\\,CCS is semi-supervised (requires CP labels for pair construction), not truly unsupervised.}\n\\label{tab:negative}\n\\end{table}\n\nBOCPD achieves 93\\% detection rate on R1-8B but with worse lead time (+3.5 steps) than simple thresholding (+4.9 steps). On OT-7B and both 32B models, BOCPD achieves 0\\% detection across all hazard rate configurations. CUSUM underperforms thresholding on all four models. Both methods assume abrupt distributional shifts, but safety commitment is gradual: representations transition smoothly toward post-CP states rather than producing a sharp regime change.\n\nMahalanobis distance produces near-zero separation between safe and jailbreak trajectories across all four models (R1-8B $\\Delta d{=}+0.07$, OT-7B $+0.03$). The discriminative signal resides in minor PCA components rather than the principal variance directions that Mahalanobis distance captures.\n\nRepE mean-difference direction probing~\\citep{zou2023representation} achieves lower balanced accuracy than supervised LR on R1-8B (74.9\\% vs.\\ 81.7\\%). Current RepE results use layers selected by the biased metric; evaluation at corrected layers is pending for the 32B models. MLP probes underperform LR on 3 of 4 models, which confirms that the pre-CP/post-CP distinction is linearly separable and that additional model capacity leads to overfitting on small training sets. CCS~\\citep{burns2023discovering} achieves 77.7\\% balanced accuracy on R1-8B (between supervised LR and RepE) but FPR reaches 0.41 on R1-32B. CCS requires CP labels for contrastive pair construction, which makes it semi-supervised rather than truly unsupervised, and it provides no advantage over fully supervised probes.\n\nCross-model transfer fails across all 18 configurations tested (6 directional model pairs $\\times$ 3 PCA dimensionalities). The best transfer balanced accuracy is 58.3\\%, which confirms that safety commitment representations are model-specific. PCA projection into shared dimensionality spaces (512, 1024, 2048 components) does not recover transferable structure.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experiments_d032_20260517T154238",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/experiments.tex",
    "content": "\\section{Experiments}\\label{sec:experiments}\n\nWe evaluate temporal probes across four reasoning models (\\cref{tab:models}), comparing hidden-state (HS) and text modalities under different layer selection criteria. Our experiments address three questions: (1)~Does the layer selection metric determine whether HS probes appear effective? (2)~Do HS probes outperform text probes at correctly selected layers? (3)~Which alternative detection methods fail, and why?\n\n\\subsection{Experimental Setup}\\label{sec:setup}\n\n\\paragraph{Models and data.} We study four models spanning two architectures and two parameter scales: R1-8B (Llama-8B, R1-distilled, $n{=}43$ test traces), OT-7B (Qwen-7B, STILL-trained, $n{=}47$), QwQ-32B (Qwen-32B, native reasoning, $n{=}19$--$20$), and R1-32B (Qwen-32B, R1-distilled, $n{=}20$). All traces come from HarmThoughts with step-level commitment point (CP) annotations. We use a 60/20/20 train/validation/test split across all models (\\cref{tab:models}).\n\n\\paragraph{Training and evaluation.} All probes use L2-regularized logistic regression with balanced class weights. For each model, we select the temporal window $W$ on the validation set from $W \\in \\{1, 3, 5, 10, 15, 20, 25\\}$. HS probes extract last-token hidden states from a selected transformer layer; text probes encode each reasoning step with all-MiniLM-L6-v2 (384 dimensions). Detection requires $K{=}5$ consecutive threshold crossings. Modality comparisons use a two-sided null-centered bootstrap test (1000 resamples) with Holm-Bonferroni step-down correction across 12 tests (3 metrics $\\times$ 4 models, $\\alpha{=}0.05$).\n\n\\paragraph{Layer selection.} We evaluate five layer selection metrics per model (\\cref{sec:layer-sensitivity}). The biased composite metric (balanced accuracy $\\times$ crossing rate) systematically selects shallow layers for 32B models because representational volatility at early layers inflates the crossing rate component. Four unbiased metrics (pure balanced accuracy, precision, inverse FPR, and an additive composite) converge on deep layers. Results throughout this section use the corrected deep layers, with explicit comparison to biased-layer outcomes in \\cref{sec:layer-results}.\n\n\\subsection{Layer Selection Results}\\label{sec:layer-results}\n\n\\cref{tab:layer_selection} presents the layer selected by the biased composite metric and the consensus of four unbiased metrics across all four models. For R1-8B, all five metrics agree on layer~14 (44\\% depth), with no discrepancy. For the remaining three models, the biased metric selects shallow layers: L0 (0\\%) for OT-7B, L2 (3\\%) for QwQ-32B, and L10 (16\\%) for R1-32B. All four unbiased metrics converge on deep layers: L16 (57\\%) for OT-7B, L60 (94\\%) for QwQ-32B, and L63 (98\\%) for R1-32B. The bias is most extreme for the 64-layer 32B models, where the composite metric selects layers in the bottom 16\\% of the network while all other metrics select layers above 94\\%.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Model} & \\textbf{Biased}$^a$ & \\textbf{Corrected}$^b$ & $p$ \\textbf{(corr.)} \\\\\n\\midrule\nR1-8B & L14 (44\\%) & L14 (44\\%) & ${<}0.001$ \\\\\nOT-7B & L0 (0\\%)$^c$ & L16 (57\\%) & ${<}0.001$ \\\\\nQwQ-32B & L2 (3\\%) & L60 (94\\%) & ${<}0.005$ \\\\\nR1-32B & L10 (16\\%) & L63 (98\\%) & ${<}0.001$ \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Layer selection sensitivity. $^a$\\,Selected by bal\\_acc $\\times$ crossing\\_rate. $^b$\\,Consensus of four unbiased metrics (pure bal\\_acc, precision, inverse FPR, additive composite). $^c$\\,OT-7B has only 28 layers; bias is less extreme than for 64-layer models. The rightmost column reports HS vs.\\ text precision $p$-values at the corrected layer (two-sided null-centered bootstrap, 1000 resamples). At the \\emph{biased} layers for 32B models, corresponding $p$-values were 0.064 (R1-32B) and 0.35--0.83 (QwQ-32B), both non-significant.}\n\\label{tab:layer_selection}\n\\end{table}\n\nThe downstream impact on modality comparison is severe for the 32B models. At biased layers, two-sided bootstrap $p$-values for HS precision advantage are 0.064 for R1-32B (not significant) and 0.35--0.83 for QwQ-32B (not significant). At the corrected deep layers, all $p$-values drop below 0.005. The R1-32B case illustrates the magnitude of this effect: the biased metric selects L10 (16\\% depth, precision $p{=}0.064$), while pure balanced accuracy selects L63 (98\\% depth, $p{<}0.001$). For QwQ-32B, the shift is from L2 ($p{=}0.35$--$0.83$) to L60 ($p{<}0.005$ across all 15 window sizes tested). OT-7B represents an intermediate case: the biased metric selects L0 (0\\%), but OT-7B has only 28 layers, so the practical impact is smaller than for 64-layer models. The corrected layer (L16, 57\\% depth) still produces stronger HS-text separation ($p{<}0.001$ on all three metrics).\n\nThis sensitivity analysis reveals that a single metric component (crossing rate) can reverse a study's central conclusion. Had we reported only biased-layer results, we would have concluded that the HS advantage is scale-dependent: significant at 7--8B, absent at 32B. The corrected analysis shows HS advantage across all four models, with the apparent scale-dependence being a methodological artifact of biased layer selection.\n\n\\subsection{HS vs.\\ Text Comparison}\\label{sec:hs-text}\n\n\\cref{tab:hs_vs_text} presents the main HS vs.\\ text comparison at corrected layers. All 12 hypothesis tests (3 metrics $\\times$ 4 models) pass Holm-Bonferroni step-down correction at $\\alpha{=}0.05$. At the previously used biased layers, only 5 of 12 tests passed (all from the two 7--8B models that were unaffected by the metric bias). The corrected analysis recovers all 7 previously failing tests across the full battery.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{llcrrrr}\n\\toprule\n\\textbf{Model} & \\textbf{Layer} & $W$ & $\\Delta$\\textbf{BA} & $\\Delta$\\textbf{Prec} & $\\Delta$\\textbf{FPR} & \\textbf{HB} \\\\\n\\midrule\nR1-8B & L14 & 15 & +8.2 & +22.4 & $-$7.4 & 3/3 \\\\\nOT-7B & L16 & 3 & +10.9 & +21.2 & $-$17.1 & 3/3 \\\\\nQwQ & L60 & 3 & +15.4 & \\textbf{+23.6} & $-$9.8 & 3/3 \\\\\nR1-32B & L63 & 1 & \\textbf{+18.7} & +15.4 & \\textbf{$-$14.6} & 3/3 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{HS vs.\\ text probe comparison at corrected layers. $\\Delta$BA, $\\Delta$Prec, and $\\Delta$FPR report the HS$-$text difference in percentage points for balanced accuracy, precision, and pre-CP false positive rate. HB: tests passing Holm-Bonferroni step-down ($\\alpha{=}0.05$, 12 tests total). All comparisons use a two-sided null-centered bootstrap (1000 resamples). $W$: validation-selected temporal window per model.}\n\\label{tab:hs_vs_text}\n\\end{table}\n\n\\paragraph{7--8B models.} R1-8B ($n{=}43$, L14, $W{=}15$) shows HS advantages of +8.2pp balanced accuracy ($p{=}0.005$), +22.4pp precision ($p{<}0.001$), and $-$7.4pp FPR ($p{=}0.044$). All three survive Holm-Bonferroni correction. OT-7B ($n{=}47$, L16, matched $W{=}3$) shows +10.9pp balanced accuracy ($p{<}0.001$), +21.2pp precision ($p{<}0.001$), and $-$17.1pp FPR ($p{<}0.001$), with all three tests surviving correction. The precision advantage is consistent across these architecturally distinct models: +22.4pp on the Llama-based R1-8B and +21.2pp on the Qwen-based OT-7B, despite different training methods (R1 distillation vs.\\ STILL).\n\n\\paragraph{32B models.} QwQ-32B ($n{=}19$--$20$, L60, $W{=}3$) shows +15.4pp balanced accuracy ($p{<}0.001$), +23.6pp precision ($p{<}0.001$), and $-$9.8pp FPR ($p{=}0.004$), all surviving correction. R1-32B ($n{=}20$, L63, $W{=}1$) shows +18.7pp balanced accuracy ($p{<}0.001$), +15.4pp precision ($p{<}0.001$), and $-$14.6pp FPR ($p{=}0.007$), all surviving correction. The precision advantage ranges from +15.4 to +23.6pp across all four models.\n\n\\paragraph{Control task selectivity.} Following \\citet{hewitt2019control}, selectivity scores confirm genuine safety signal beyond positional artifacts: R1-8B 12.5pp, OT-7B 18.3pp, QwQ-32B 15.3pp, R1-32B 7.5pp. All four models exceed the 5pp threshold.\n\n\\paragraph{Caveats.} Three qualifications apply. First, the validation-selected $W$ differs per model ($W{=}15$ for R1-8B, $W{=}3$ for OT-7B and QwQ-32B, $W{=}1$ for R1-32B). The tests measure whether HS outperforms text at each model's best operating point, not at a uniform window. Second, R1-32B at $W{=}1$ achieves only 25\\% coverage (5 of 20 test traces detected), which limits practical utility despite strong per-detection performance. At $W{\\geq}3$, R1-32B significance vanishes due to the dimensionality constraint ($51200 \\times W$ features for $n{=}20$ training traces). Third, QwQ-32B HS lead time is negative ($-$1.2 to +1.9 steps) compared to text probes (3.7 to 12.3 steps): HS probes are more accurate but detect later on this model. In safety deployment, earlier detection by several steps may outweigh higher per-step accuracy.\n\n\\subsection{Temporal Context Effects}\\label{sec:temporal}\n\nText probes benefit universally from larger temporal windows across all four models. Balanced accuracy improves by +3 to +12pp and precision by +8 to +23pp from $W{=}1$ to $W{=}25$, with consistent FPR reductions.\n\nHS probes show similar benefits on 3 of 4 models. On R1-8B (L14), increasing $W$ from 1 to 25 improves balanced accuracy from 77.8\\% to 81.0\\% (+3.2pp), precision from 69.3\\% to 82.2\\% (+12.9pp), and reduces FPR from 9.65\\% to 4.8\\% ($-$4.9pp). At the validation-selected $W{=}15$, performance reaches 80.2\\% balanced accuracy, 77.7\\% precision, and 6.4\\% FPR, which captures most of the precision gain with higher coverage than $W{=}25$. QwQ-32B and R1-32B follow similar monotonic patterns for precision and FPR across the full $W$ range.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig2_temporal_improvement.pdf}\n\\caption{Effect of temporal window size on R1-8B HS probe performance (L14). Precision increases monotonically from 69.3\\% ($W{=}1$) to 82.2\\% ($W{=}25$); FPR decreases from 9.65\\% to 4.8\\%.}\n\\label{fig:window_ablation}\n\\end{figure}\n\nOT-7B is the exception. HS balanced accuracy peaks at $W{=}3$ (68.8\\%) and declines to 65.9\\% at $W{=}25$ ($-$2.9pp). Precision and FPR continue to improve: precision rises from 42.8\\% ($W{=}1$) to 49.4\\% ($W{=}25$), and FPR drops from 12.0\\% to 7.5\\%. The saturation is specific to balanced accuracy; larger windows trade balanced accuracy for better precision and lower FPR. This pattern holds on both L0 and L16, which confirms it as a genuine OT-7B characteristic rather than a layer-specific artifact. The validation selection of $W{=}3$ reflects this trade-off: balanced accuracy is maximized without sacrificing the precision gains available at moderate windows.\n\nThe consistent finding across all four models is that precision improvement (+1.7 to +12.9pp from $W{=}1$ to best) and FPR reduction ($-$4.0 to $-$5.9pp) are positive for both modalities (\\cref{fig:window_ablation}). Temporal context provides the most robust source of discriminative information for false positive reduction. Observing multiple reasoning steps matters more than the choice of signal modality. Larger windows make probes more conservative, reducing coverage but improving confidence on detected traces. Deployment systems would tune $K$ alongside $W$ to balance coverage against precision.\n\n\\subsection{32B Model-Specific Analysis}\\label{sec:32b-analysis}\n\nThe two 32B models present contrasting detection profiles despite sharing the Qwen-32B architecture (\\cref{tab:32b_divergence}). Per-model analysis is required; a unified scale-level narrative would obscure important differences.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Dimension} & \\textbf{R1-32B (L63)} & \\textbf{QwQ (L60)} \\\\\n\\midrule\nHolm-Bonf.\\ sig.\\ & $W{=}1$ only (3/3) & All 15 $W$ (3/3) \\\\\nLead time (steps) & +11.7 to +13.3 & $-$1.2 to +1.9 \\\\\nHS vs.\\ Position & +14.2pp & $-$0.6pp \\\\\nCoverage ($W{=}1$) & 25\\% & 74\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{32B cross-model divergence. R1-32B provides excellent early warning with narrow coverage; QwQ-32B provides robust significance with poor lead time.}\n\\label{tab:32b_divergence}\n\\end{table}\n\n\\paragraph{R1-32B (L63, $W{=}1$).} R1-32B achieves excellent lead time (+11.7 to +13.3 steps before commitment), and the HS probe strongly outperforms the position-only baseline (+14.2pp balanced accuracy). These properties make R1-32B the strongest candidate for early warning among the four models. The limitation is statistical narrowness: only $W{=}1$ passes Holm-Bonferroni (3/3 metrics), with $W{\\geq}3$ non-significant due to dimensionality ($51200 \\times W$ features for $n{=}20$ traces). At $W{=}1$, coverage is 25\\% (5 of 20 traces detected). The evidence supports HS superiority on R1-32B but under restrictive operating conditions.\n\n\\paragraph{QwQ-32B (L60, $W{=}3$).} QwQ-32B shows the most robust statistical significance of any model: HS outperforms text at all 15 window sizes tested ($p{<}0.005$), with 74\\% coverage at $W{=}1$. The limitation is detection timing: HS lead time is negative ($-$1.2 to +1.9 steps), compared to text probes (3.7 to 12.3 steps). The position-only baseline achieves comparable balanced accuracy (0.746 vs.\\ HS 0.740). HS probes are more precise but detect later, and they offer minimal advantage over simple positional features for this model.\n\nThe complementary profiles suggest that the practical value of HS monitoring depends on model-specific detection requirements. Early warning applications favor R1-32B's high lead time despite narrow coverage. Broad reliable detection applications favor QwQ-32B's robust significance despite poor timing. These divergent patterns within the same architecture underscore that per-model validation is essential.\n\n\\subsection{Negative Results}\\label{sec:negative}\n\n\\cref{tab:negative} summarizes seven alternative detection approaches that fail to match supervised temporal probing. The failures span change-point detection, geometric methods, direction-based probing, nonlinear models, semi-supervised learning, and cross-model transfer.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{p{1.5cm}p{2.9cm}p{2.3cm}}\n\\toprule\n\\textbf{Method} & \\textbf{Result} & \\textbf{Failure Mode} \\\\\n\\midrule\nBOCPD & R1-8B 93\\% det., lead +3.5 $<$ thresh.\\ +4.9; others 0\\% & Commitment gradual \\\\\nCUSUM & Worse than threshold, all models & Same as BOCPD \\\\\nMahalanobis & $\\Delta d \\approx 0$ (R1-8B +0.07, OT-7B +0.03) & Signal in minor PCA dirs. \\\\\nRepE & R1-8B 74.9\\% vs.\\ LR 81.7\\%$^a$ & Direction insufficient \\\\\nMLP & 3/4 worse than LR & Overfitting ($n$ small) \\\\\nCCS$^b$ & R1-8B 77.7\\%; R1-32B FPR\\,=\\,0.41 & No gain over supervised \\\\\nTransfer & Best 58.3\\%, all fail & Model-specific repr. \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Negative results. $^a$\\,RepE results use layers from the biased metric; evaluation at corrected layers is pending for 32B models. $^b$\\,CCS is semi-supervised (requires CP labels for pair construction), not truly unsupervised.}\n\\label{tab:negative}\n\\end{table}\n\nBOCPD achieves 93\\% detection rate on R1-8B but with worse lead time (+3.5 steps) than simple thresholding (+4.9 steps). On OT-7B and both 32B models, BOCPD achieves 0\\% detection across all hazard rate configurations. CUSUM underperforms thresholding on all four models. Both methods assume abrupt distributional shifts, but safety commitment is gradual: representations transition smoothly toward post-CP states rather than producing a sharp regime change.\n\nMahalanobis distance produces near-zero separation between safe and jailbreak trajectories across all four models (R1-8B $\\Delta d{=}+0.07$, OT-7B $+0.03$). The discriminative signal resides in minor PCA components rather than the principal variance directions that Mahalanobis distance captures.\n\nRepE mean-difference direction probing~\\citep{zou2023representation} achieves lower balanced accuracy than supervised LR on R1-8B (74.9\\% vs.\\ 81.7\\%). Current RepE results use layers selected by the biased metric; evaluation at corrected layers is pending for the 32B models. MLP probes underperform LR on 3 of 4 models, which confirms that the pre-CP/post-CP distinction is linearly separable and that additional model capacity leads to overfitting on small training sets. CCS~\\citep{burns2023discovering} achieves 77.7\\% balanced accuracy on R1-8B (between supervised LR and RepE) but FPR reaches 0.41 on R1-32B. CCS requires CP labels for contrastive pair construction, which makes it semi-supervised rather than truly unsupervised, and it provides no advantage over fully supervised probes.\n\nCross-model transfer fails across all 18 configurations tested (6 directional model pairs $\\times$ 3 PCA dimensionalities). The best transfer balanced accuracy is 58.3\\%, which confirms that safety commitment representations are model-specific. PCA projection into shared dimensionality spaces (512, 1024, 2048 components) does not recover transferable structure.\n"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-17T15:56:52.727014+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/experiments.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_d032_20260517T154238",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-17T15:56:52.727194+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "—",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/experiments.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experiments_d032_20260517T154238",
  "tool": "Grep",
  "tool_args": {
    "pattern": "—",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/experiments.tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-17T15:56:52.727330+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_d032_20260517T154238",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-17T15:56:52.727455+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": " – ",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/experiments.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experiments_d032_20260517T154238",
  "tool": "Grep",
  "tool_args": {
    "pattern": " – ",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/experiments.tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-17T15:56:52.727578+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_d032_20260517T154238",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-17T15:56:52.727728+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "ing,|ing\\.",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/experiments.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experiments_d032_20260517T154238",
  "tool": "Grep",
  "tool_args": {
    "pattern": "ing,|ing\\.",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/experiments.tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-17T15:56:52.727852+00:00_

7:\paragraph{Models and data.} We study four models spanning two architectures and two parameter scales: R1-8B (Llama-8B, R1-distilled, $n{=}43$ test traces), OT-7B (Qwen-7B, STILL-trained, $n{=}47$), QwQ-32B (Qwen-32B, native reasoning, $n{=}19$--$20$), and R1-32B (Qwen-32B, R1-distilled, $n{=}20$). All traces come from HarmThoughts with step-level commitment point (CP) annotations. We use a 60/20/20 train/validation/test split across all models (\cref{tab:models}).
109:The complementary profiles suggest that the practical value of HS monitoring depends on model-specific detection requirements. Early warning applications favor R1-32B's high lead time despite narrow coverage. Broad reliable detection applications favor QwQ-32B's robust significance despite poor timing. These divergent patterns within the same architecture underscore that per-model validation is essential.
113:\cref{tab:negative} summarizes seven alternative detection approaches that fail to match supervised temporal probing. The failures span change-point detection, geometric methods, direction-based probing, nonlinear models, semi-supervised learning, and cross-model transfer.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_d032_20260517T154238",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-17T15:56:52.727997+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "Furthermore|Moreover|Additionally|It is worth noting|Notably|delve|leverage|utilize|facilitate",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/experiments.tex",
  "output_mode": "content",
  "-i": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experiments_d032_20260517T154238",
  "tool": "Grep",
  "tool_args": {
    "pattern": "Furthermore|Moreover|Additionally|It is worth noting|Notably|delve|leverage|utilize|facilitate",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/experiments.tex",
    "output_mode": "content",
    "-i": "True"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-17T15:56:52.728116+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_d032_20260517T154238",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-17T15:56:52.728229+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": ", (demonstrating|highlighting|showcasing|indicating|suggesting|revealing|confirming|showing|establishing|enabling|providing|achieving|improving|capturing)",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/experiments.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experiments_d032_20260517T154238",
  "tool": "Grep",
  "tool_args": {
    "pattern": ", (demonstrating|highlighting|showcasing|indicating|suggesting|revealing|confirming|showing|establishing|enabling|providing|achieving|improving|capturing)",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/experiments.tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-17T15:56:52.728351+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_d032_20260517T154238",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-17T15:56:52.728489+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\label\\{",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/experiments.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experiments_d032_20260517T154238",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\label\\{",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/experiments.tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-17T15:56:52.728678+00:00_

1:\section{Experiments}\label{sec:experiments}
5:\subsection{Experimental Setup}\label{sec:setup}
13:\subsection{Layer Selection Results}\label{sec:layer-results}
31:\label{tab:layer_selection}
38:\subsection{HS vs.\ Text Comparison}\label{sec:hs-text}
56:\label{tab:hs_vs_text}
67:\subsection{Temporal Context Effects}\label{sec:temporal}
77:\label{fig:window_ablation}
84:\subsection{32B Model-Specific Analysis}\label{sec:32b-analysis}
102:\label{tab:32b_divergence}
111:\subsection{Negative Results}\label{sec:negative}
132:\label{tab:negative}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_d032_20260517T154238",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-17T15:56:52.728820+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\cref\\{",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/experiments.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experiments_d032_20260517T154238",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\cref\\{",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/experiments.tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-17T15:56:52.728946+00:00_

3:We evaluate temporal probes across four reasoning models (\cref{tab:models}), comparing hidden-state (HS) and text modalities under different layer selection criteria. Our experiments address three questions: (1)~Does the layer selection metric determine whether HS probes appear effective? (2)~Do HS probes outperform text probes at correctly selected layers? (3)~Which alternative detection methods fail, and why?
7:\paragraph{Models and data.} We study four models spanning two architectures and two parameter scales: R1-8B (Llama-8B, R1-distilled, $n{=}43$ test traces), OT-7B (Qwen-7B, STILL-trained, $n{=}47$), QwQ-32B (Qwen-32B, native reasoning, $n{=}19$--$20$), and R1-32B (Qwen-32B, R1-distilled, $n{=}20$). All traces come from HarmThoughts with step-level commitment point (CP) annotations. We use a 60/20/20 train/validation/test split across all models (\cref{tab:models}).
11:[Omitted long matching line]
15:[Omitted long matching line]
40:\cref{tab:hs_vs_text} presents the main HS vs.\ text comparison at corrected layers. All 12 hypothesis tests (3 metrics $\times$ 4 models) pass Holm-Bonferroni step-down correction at $\alpha{=}0.05$. At the previously used biased layers, only 5 of 12 tests passed (all from the two 7--8B models that were unaffected by the metric bias). The corrected analysis recovers all 7 previously failing tests across the full battery.
82:[Omitted long matching line]
86:The two 32B models present contrasting detection profiles despite sharing the Qwen-32B architecture (\cref{tab:32b_divergence}). Per-model analysis is required; a unified scale-level narrative would obscure important differences.
113:\cref{tab:negative} summarizes seven alternative detection approaches that fail to match supervised temporal probing. The failures span change-point detection, geometric methods, direction-based probing, nonlinear models, semi-supervised learning, and cross-model transfer.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_d032_20260517T154238",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 45 · 2026-05-17T15:56:52.729105+00:00_

Labels and cross-references are all correct. Key labels defined:
- `sec:experiments`, `sec:setup`, `sec:layer-results`, `sec:hs-text`, `sec:temporal`, `sec:32b-analysis`, `sec:negative`
- `tab:layer_selection`, `tab:hs_vs_text`, `tab:32b_divergence`, `tab:negative`, `fig:window_ablation`

The method section's cross-references to `\cref{sec:layer-results}` and `\cref{tab:layer_selection}` will resolve correctly.

The complete experiments.tex is written to the target path. Structure:

- **4.1 Experimental Setup** (~280w): Models, training protocol, layer selection overview
- **4.2 Layer Selection Results** (~370w): Primary contribution. Table `tab:layer_selection` shows biased vs corrected layers with downstream p-value impact. Key finding: crossing rate component reverses 32B conclusions
- **4.3 HS vs Text Comparison** (~480w): Secondary contribution. Table `tab:hs_vs_text` with 12/12 Holm-Bonferroni. Precision +15.4 to +23.6pp across all 4 models. Caveats: different W per model, R1-32B 25% coverage, QwQ negative lead time
- **4.4 Temporal Context Effects** (~370w): Universal text probe benefit, 3/4 HS probe benefit, OT-7B exception detailed. Figure `fig:window_ablation`
- **4.5 32B Model-Specific Analysis** (~290w): Table `tab:32b_divergence`. R1-32B: excellent lead time, narrow coverage. QwQ: robust significance, poor timing
- **4.6 Negative Results** (~300w): Table `tab:negative`. 7 methods fail: BOCPD, CUSUM, Mahalanobis, RepE, MLP, CCS, cross-transfer

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_writing_experiments_d032_20260517T154238"
}
```

</details>

---
