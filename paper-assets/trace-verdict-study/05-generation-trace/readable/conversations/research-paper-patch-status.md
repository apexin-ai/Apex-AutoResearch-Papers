# research paper patch status

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 25
- **Recorded user turns:** 0
- **Tool calls:** 12
- **Original source:** `logs/chats/worker_research_paper_patch_status_20260518T014706.jsonl`
- **Structured JSON:** [`bd9316f8e67859ed301b.json`](../../sessions/bd/bd9316f8e67859ed301b.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

25 recorded events

### Tool call

_source line 1 · 2026-05-18T01:48:58.235586+00:00_

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
  "session": "worker_research_paper_patch_status_20260518T014706",
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

_source line 2 · 2026-05-18T01:48:58.236027+00:00_

artifacts/dream_reports/dream_20260515T013018/best/paper.tex
artifacts/dream_reports/dream_20260515T013018/median/paper.tex
artifacts/dream_reports/dream_20260515T013018/worst/paper.tex
artifacts/dream_reports/dream_20260515T084908/best/paper.tex
artifacts/dream_reports/dream_20260515T084908/median/paper.tex
artifacts/dream_reports/dream_20260515T084908/worst/paper.tex
artifacts/_project/paper/related_work.tex
artifacts/per_class_breakdown.tex
artifacts/_project/paper/section3_experimental_setup_d4f1e8.tex
artifacts/_project/paper/section3_experimental_setup.tex
artifacts/_project/paper/ethics_statement.tex
artifacts/_project/paper/ethics_statement_77cf5f.tex
artifacts/_project/paper/arr_checklist.tex
artifacts/_project/paper/main_results_tables.tex
artifacts/_project/paper/main_results_tables_d8c8b6.tex
artifacts/paper_tables/main_results_tables.tex
artifacts/_project/paper/experiments.tex
artifacts/dream_reports/dream_20260516T105259/best/paper.tex
artifacts/dream_reports/dream_20260516T105259/median/paper.tex
artifacts/dream_reports/dream_20260516T105259/worst/paper.tex
artifacts/dream_reports/dream_20260516T155731/best/paper.tex
artifacts/dream_reports/dream_20260516T155731/median/paper.tex
artifacts/dream_reports/dream_20260516T155731/worst/paper.tex
docs/paper/arr_checklist.tex
docs/paper/method.tex
docs/paper/conclusion.tex
docs/paper/main.tex
docs/paper/related_work.tex
docs/paper/introduction.tex
docs/paper/appendix.tex
docs/paper/experiments.tex
docs/paper/discussion.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper_patch_status_20260518T014706",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-18T01:48:58.236245+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper_patch_status_20260518T014706",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-18T01:48:58.236451+00:00_

task_context/history/director/loop_1.md
task_context/history/agent/loop_1.md
docs/IDEA_BRIEF.md
artifacts/dream_reports/dream_20260515T013018/best/paper_framing.md
artifacts/dream_reports/dream_20260515T013018/median/paper_framing.md
task_context/history/agent/loop_2.md
task_context/history/reviewer/loop_1.md
artifacts/dream_reports/dream_20260515T013018/worst/paper_framing.md
artifacts/dream_reports/dream_20260515T013018/best/review_report.md
artifacts/dream_reports/dream_20260515T013018/median/review_report.md
artifacts/dream_reports/dream_20260515T013018/worst/review_report.md
.claude/sessions/agent_9c2cd44d/CLAUDE.md
.claude/sessions/agent_9c2cd44d/AGENTS.md
.claude/sessions/agent_6bb99313/CLAUDE.md
.claude/sessions/agent_6bb99313/AGENTS.md
task_context/history/director/loop_2.md
task_context/history/agent/loop_3.md
.claude/sessions/agent_42a1e69e/CLAUDE.md
.claude/sessions/agent_42a1e69e/AGENTS.md
task_context/history/agent/loop_2_1778837550.md
artifacts/report_training_progress.md
artifacts/plan_001_literature_linkage.md
artifacts/dream_reports/dream_20260515T084908/best/paper_framing.md
artifacts/dream_reports/dream_20260515T084908/median/paper_framing.md
artifacts/dream_reports/dream_20260515T084908/worst/paper_framing.md
artifacts/dream_reports/dream_20260515T084908/best/review_report.md
task_context/history/agent/loop_4.md
artifacts/dream_reports/dream_20260515T084908/median/review_report.md
artifacts/dream_reports/dream_20260515T084908/worst/review_report.md
artifacts/_project/intermediate/results_table_draft.md
artifacts/results_table_draft.md
task_context/history/reviewer/loop_2.md
task_context/history/director/loop_3.md
task_context/history/agent/loop_4_1778846671.md
task_context/history/agent/loop_4_1778849725.md
artifacts/_project/intermediate/literature_survey_20260515.md
task_context/history/director/loop_4.md
task_context/history/agent/loop_5.md
artifacts/deepseek_vota_fail_recall_analysis.md
task_context/history/agent/loop_5_1778856729.md
artifac
…[truncated 2906 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper_patch_status_20260518T014706",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-18T01:48:58.236647+00:00_

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
  "session": "worker_research_paper_patch_status_20260518T014706",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-18T01:48:58.236905+00:00_

1	\section{Experiments}
2	
3	We evaluate across two research questions:
4	(1)~Do Tier~1 exception signals generalize across models?
5	(2)~What is the relative contribution of each trace component?
6	All experiments use $N{=}1{,}190$ test samples; accuracy is reported with Wilson 95\% CIs.
7	Pairwise comparisons use paired bootstrap resampling ($B{=}10{,}000$, seed=42); all differences are significant at $p{<}0.0001$ unless noted.
8	
9	\subsection{Cross-Model Comparison}
10	\label{sec:cross_model}
11	
12	Table~\ref{tab:cross_model} compares four models spanning an 8.7$\times$ parameter range (1.5B--13B) and three architecture families (Qwen, DeepSeek, CodeLlama) under key conditions.
13	
14	\begin{table}[t]
15	\centering
16	\caption{Cross-model verdict accuracy (\%, $N{=}1{,}190$). Bold: best accuracy per model. Multi-seed entries show mean$\pm$std (3 seeds). $^\dag$2/3 seeds; one seed excluded due to LoRA initialization failure (91.09\%, fail recall = 70.5\%; see Appendix~\ref{sec:training_dynamics}). \texttt{ae\_only} and \texttt{loop\_only} ablations tested on Qwen-7B (3 seeds) to isolate component contributions; cross-model validation focused on the primary conditions. Full CIs in Appendix~\ref{sec:full_results}.}
17	\label{tab:cross_model}
18	\small
19	\resizebox{\columnwidth}{!}{%
20	\begin{tabular}{lcccc}
21	\toprule
22	\textbf{Condition} & \textbf{Qwen-7B} & \textbf{Qwen-1.5B} & \textbf{CL-13B} & \textbf{DS-6.7B} \\
23	\midrule
24	exception\_only & \textbf{99.83}{\scriptsize$\pm$0.00} & \textbf{99.83} & \textbf{99.89}{\scriptsize$\pm$0.10} & \textbf{99.33}$^\dag$ \\
25	ae\_only & 99.64{\scriptsize$\pm$0.49} & --- & --- & --- \\
26	VOTA & 99.41 & 99.58 & 98.57 & 84.45 \\
27	no\_trace & 75.13 & 67.31 & 76.50 & 73.36 \\
28	\midrule
29	Majority baseline & \multicolumn{4}{c}{71.51} \\
30	\bottomrule
31	\end{tabular}%
32	}
33	\end{table}
34	
35	\paragraph{Exception dominance across families.}
36	Under \texttt{exception\_only}, the Qwen and CodeLlama families achiev
…[truncated 12512 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper_patch_status_20260518T014706",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-18T01:48:58.237067+00:00_

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
  "session": "worker_research_paper_patch_status_20260518T014706",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-18T01:48:58.237277+00:00_

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
12	\title{Exception Events Are All You Need: \\Component Ablation for Trace-Based Verdict Prediction}
13	\author{Anonymous ACL submission}
14	
15	\begin{document}
16	\maketitle
17	
18	\begin{abstract}
19	Execution traces are increasingly used to enhance code language models, but which trace components matter for downstream tasks remains poorly understood.
20	We present the first systematic component ablation of trace representations for verdict prediction (classifying whether a test passes or fails) across four models spanning three architecture families and 1.5B to 13B parameters.
21	Exception events alone achieve ${\geq}$99.33\% accuracy across all four models (${\geq}$99.83\% on three of four; one seed reaches 100\%), while a code-only baseline shows 9.19pp scale sensitivity (67.3--76.5\%).
22	Adding more trace information actively hurts: a multi-component representation underperforms exception-only, and the full-trace gap approximately decomposes into information overload (${\sim}$74\%) and gradient dilution (${\sim}$26\%).
23	Tail-truncation experiments reveal that diagnostic signal concentrates near the trace terminus (in a localized window, not the absolute end), recovering 86\% of the gap to exception-only.
24	A format-marker ablation confirms ${\sim}$91\% of the exception signal is semantic (learned by SFT to distinguish caught from uncaught exceptions) rather than format-driven.
25	These results reveal a two-tier diagnostic hierarchy: Tier~1 signals (exception events, assertion points) individually achieve ${\geq}$99\%, while Tier~2 (loop compression) reaches 85.6\%.
26	Cross-dataset evaluation on DebugBench ($N{=}426$) confir
…[truncated 3929 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper_patch_status_20260518T014706",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-18T01:48:58.237479+00:00_

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
  "session": "worker_research_paper_patch_status_20260518T014706",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/appendix.tex"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-18T01:48:58.237906+00:00_

1	\section{Per-Class Performance Breakdown}
2	\label{sec:per_class}
3	
4	Table~\ref{tab:per_class} reports per-class precision, recall, and F1 for all experimental conditions.
5	
6	\begin{table*}[t]
7	\centering
8	\caption{Per-class precision, recall, and F1 for all experimental conditions (seed 42). DeepSeek VOTA achieves 100\% fail precision but only 45.4\% fail recall, indicating systematic bias toward predicting \texttt{pass}. DeepSeek \texttt{exception\_only} seed 42 achieves 100\% fail recall, but seed 123 drops to 70.5\% (see Table~\ref{tab:full_deepseek}).}
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
22	VOTA\_no\_ae       & Qwen-2.5-7B & 99.41 & 99.88 & 99.29 & 99.59 & 98.26 & 99.71 & 98.98 \\
23	\midrule
24	No Trace          & DeepSeek-6.7B & 73.36 & 81.71 & 80.85 & 81.28 & 53.16 & 54.57 & 53.86 \\
25	Full Trace        & DeepSeek-6.7B & 79.16 & 85.70 & 85.10 & 85.40 & 63.20 & 64.30 & 63.70 \\
26	VOTA              & DeepSeek-6.7B & 84.45 & 82.14 & 100.00 & 90.20 & 100.00 & 45.40 & 62.50 \\
27	Exception Only    & DeepSeek-6.7B & 99.33 & 100.00 & 99.06 & 99.53 & 97.69 & 100.00 & 98.83 \\
28	\bottomrule
…[truncated 44301 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper_patch_status_20260518T014706",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-18T01:48:58.238126+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "CodeLlama.*tail|codellama.*tail|CL-13B.*tail",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper_patch_status_20260518T014706",
  "tool": "Grep",
  "tool_args": {
    "pattern": "CodeLlama.*tail|codellama.*tail|CL-13B.*tail",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-18T01:48:58.238321+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper_patch_status_20260518T014706",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-18T01:48:58.238452+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/paper_patch_audit/ 2>/dev/null || echo \"DIR_NOT_EXISTS\"",
  "description": "Check if output directory exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper_patch_status_20260518T014706",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/paper_patch_audit/ 2>/dev/null || echo \"DIR_NOT_EXISTS\"",
    "description": "Check if output directory exists"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-18T01:48:58.238572+00:00_

DIR_NOT_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper_patch_status_20260518T014706",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-18T01:48:58.238688+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/paper_patch_audit",
  "description": "Create output directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper_patch_status_20260518T014706",
  "tool": "Bash",
  "tool_args": {
    "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/paper_patch_audit",
    "description": "Create output directory"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-18T01:48:58.238804+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper_patch_status_20260518T014706",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-18T01:48:58.238945+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/paper_patch_audit/paper_patch_status.md",
  "content": "# Paper Patch Status: Budget Curve + Head-Tail Data\n\n**审计时间**: 2026-05-18  \n**论文路径**: `/root/trace-verdict-study/docs/paper/` (服务器) / `docs/paper/` (本地)\n\n---\n\n## 一、Budget Curve（tail-256/512/1024/2048）\n\n### 已写入 ✅\n\n| 数据点 | 位置 | 状态 |\n|--------|------|------|\n| Qwen-7B: 78.9/93.6/96.5/97.3 | appendix.tex Table 6 (`tab:tail_cross_model`) | ✅ 完整 |\n| DeepSeek-6.7B: 76.4/93.9/96.5/95.0↓ | appendix.tex Table 6 | ✅ 完整 |\n| Qwen-1.5B: 72.6/95.6/96.6/97.9 | appendix.tex Table 6 | ✅ 完整 |\n| Phase transition 256→512: +14.7~+23pp | experiments.tex L152 + appendix.tex L419-421 | ✅ |\n| tail-512 convergence (93.6-95.6% band) | appendix.tex L422-423 | ✅ |\n| tail-1024 convergence (96.5-96.6%) | appendix.tex L422-423 | ✅ |\n| Non-monotonicity: DeepSeek only, -1.5pp at 1024→2048 | experiments.tex L147, appendix.tex L428-429 | ✅ 正确描述为 architecture-specific |\n| Scale behavior inversion (signal-poor vs signal-rich) | appendix.tex L425-426 | ✅ |\n| Budget curve figure (`budget_curve`) | appendix.tex Fig 5 (`fig:trace_length`) | ✅ (仅 Qwen-7B) |\n\n### 缺失 ❌\n\n| 数据点 | 状态 | 说明 |\n|--------|------|------|\n| **CodeLlama-13B tail-512 = 97.5%** | ❌ 未写入 | 数据已有，表格和正文均无 |\n| **CodeLlama-13B tail-256** | ⏳ 实验运行中 | 等待结果 |\n| **CodeLlama-13B tail-1024** | ⏳ 实验运行中 | 等待结果 |\n| **CodeLlama-13B tail-2048** | ❓ 未确认 | 未见相关数据 |\n| 4-model budget curve figure 更新 | ❌ | 当前 figure 仅含 Qwen-7B 单模型 |\n\n### 正文描述需更新的地方\n\n- `experiments.tex` L152: \"all three models jump\" → 需改为 4 模型（待 CL-13B 数据齐全）\n- `appendix.tex` L382-383: \"three models spanning two architecture families\" → 需扩展为 four models, three families\n- `appendix.tex` Table 6 caption: 需加入 CodeLlama-13B 行\n- `appendix.tex` L419: \"all three models\" → \"all four models\"（待数据齐全）\n\n---\n\n## 二、Head-Tail Gap（跨模型对比）\n\n### 已写入 ✅\n\n| 数据点 | 位置 | 状态 |\n|--------|------|------|\n| Qwen-7B: head-2048=81.8%, tail-2048=97.3%, gap=+15.5pp | appendix.tex Table 7 (`tab:head_vs_tail`) | ✅ |\n| DeepSeek-6.7B: head-2048=78.7%, tail-2048=95.0%, gap=+16.3pp | appendix.tex Table 7 | ✅ |\n| Qwen-1.5B: head-2048=75.3%, tail-2048=97.9%, gap=+22.6pp | appendix.tex Table 7 | ✅ |\n| 15.5-22.6pp gap range | experiments.tex L150 | ✅ |\n| 小模型 gap 更大 (Qwen-1.5B +22.6pp vs Qwen-7B +15.5pp) | experiments.tex L150-151 + appendix.tex L431-432 | ✅ |\n\n### 缺失 ❌\n\n| 数据点 | 状态 | 说明 |\n|--------|------|------|\n| **CodeLlama-13B head-2048 vs tail-2048** | ❌ | 无 head-2048 实验数据 |\n\n---\n\n## 三、Non-Monotonicity Correction\n\n### 已写入 ✅\n\n正文和附录均已正确表述：仅 DeepSeek 在 tail-1024→2048 下降 1.5pp，非 universal pattern。\n\n- experiments.tex L147: \"only DeepSeek showing a mild architecture-specific reversal\"\n- appendix.tex L357: \"only DeepSeek-6.7B shows a mild −1.5pp decrease\"\n- appendix.tex L428-429: 明确说 \"while the other two models increase monotonically\"\n\n**状态**: ✅ 无需修改\n\n---\n\n## 四、总结\n\n### 已完成的 patch\n1. ✅ 3-model budget curve 表格和分析（Qwen-7B, DeepSeek, Qwen-1.5B）\n2. ✅ Phase transition / convergence / scale inversion 叙事\n3. ✅ 3-model head-tail gap 表格和分析\n4. ✅ Non-monotonicity 正确描述\n5. ✅ Budget curve figure (单模型版)\n\n### 待完成的 patch（按优先级）\n1. **P1**: CodeLlama-13B tail-512=97.5% 写入 Table 6（数据已有，立即可做）\n2. **P2**: 等待 CL-13B tail-256 和 tail-1024 实验完成后补全表格\n3. **P3**: 更新正文 \"three models\" → \"four models\"（待 P2 完成）\n4. **P4**: 更新 budget curve figure 为 4-model 版本\n5. **P5**: CodeLlama-13B head-tail gap 数据（需要 head-2048 实验）\n\n### 需要更新的章节列表\n| 文件 | 章节/位置 | 更新内容 |\n|------|-----------|----------|\n| `experiments.tex` | §4.5 Additional Analyses, L149-156 | 加入 CL-13B 数据，更新 \"three models\" |\n| `appendix.tex` | §Trace Length Full, Table 6 | 加 CL-13B 行 |\n| `appendix.tex` | §Trace Length Full, Table 7 | 加 CL-13B 行（待 head-2048 数据）|\n| `appendix.tex` | L382-383, L419 | \"three models\" → \"four models\" |\n| `appendix.tex` | budget_curve figure | 更新为多模型版本 |\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper_patch_status_20260518T014706",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/paper_patch_audit/paper_patch_status.md",
    "content": "# Paper Patch Status: Budget Curve + Head-Tail Data\n\n**审计时间**: 2026-05-18  \n**论文路径**: `/root/trace-verdict-study/docs/paper/` (服务器) / `docs/paper/` (本地)\n\n---\n\n## 一、Budget Curve（tail-256/512/1024/2048）\n\n### 已写入 ✅\n\n| 数据点 | 位置 | 状态 |\n|--------|------|------|\n| Qwen-7B: 78.9/93.6/96.5/97.3 | appendix.tex Table 6 (`tab:tail_cross_model`) | ✅ 完整 |\n| DeepSeek-6.7B: 76.4/93.9/96.5/95.0↓ | appendix.tex Table 6 | ✅ 完整 |\n| Qwen-1.5B: 72.6/95.6/96.6/97.9 | appendix.tex Table 6 | ✅ 完整 |\n| Phase transition 256→512: +14.7~+23pp | experiments.tex L152 + appendix.tex L419-421 | ✅ |\n| tail-512 convergence (93.6-95.6% band) | appendix.tex L422-423 | ✅ |\n| tail-1024 convergence (96.5-96.6%) | appendix.tex L422-423 | ✅ |\n| Non-monotonicity: DeepSeek only, -1.5pp at 1024→2048 | experiments.tex L147, appendix.tex L428-429 | ✅ 正确描述为 architecture-specific |\n| Scale behavior inversion (signal-poor vs signal-rich) | appendix.tex L425-426 | ✅ |\n| Budget curve figure (`budget_curve`) | appendix.tex Fig 5 (`fig:trace_length`) | ✅ (仅 Qwen-7B) |\n\n### 缺失 ❌\n\n| 数据点 | 状态 | 说明 |\n|--------|------|------|\n| **CodeLlama-13B tail-512 = 97.5%** | ❌ 未写入 | 数据已有，表格和正文均无 |\n| **CodeLlama-13B tail-256** | ⏳ 实验运行中 | 等待结果 |\n| **CodeLlama-13B tail-1024** | ⏳ 实验运行中 | 等待结果 |\n| **CodeLlama-13B tail-2048** | ❓ 未确认 | 未见相关数据 |\n| 4-model budget curve figure 更新 | ❌ | 当前 figure 仅含 Qwen-7B 单模型 |\n\n### 正文描述需更新的地方\n\n- `experiments.tex` L152: \"all three models jump\" → 需改为 4 模型（待 CL-13B 数据齐全）\n- `appendix.tex` L382-383: \"three models spanning two architecture families\" → 需扩展为 four models, three families\n- `appendix.tex` Table 6 caption: 需加入 CodeLlama-13B 行\n- `appendix.tex` L419: \"all three models\" → \"all four models\"（待数据齐全）\n\n---\n\n## 二、Head-Tail Gap（跨模型对比）\n\n### 已写入 ✅\n\n| 数据点 | 位置 | 状态 |\n|--------|------|------|\n| Qwen-7B: head-2048=81.8%, tail-2048=97.3%, gap=+15.5pp | appendix.tex Table 7 (`tab:head_vs_tail`) | ✅ |\n| DeepSeek-6.7B: head-2048=78.7%, tail-2048=95.0%, gap=+16.3pp | appendix.tex Table 7 | ✅ |\n| Qwen-1.5B: head-2048=75.3%, tail-2048=97.9%, gap=+22.6pp | appendix.tex Table 7 | ✅ |\n| 15.5-22.6pp gap range | experiments.tex L150 | ✅ |\n| 小模型 gap 更大 (Qwen-1.5B +22.6pp vs Qwen-7B +15.5pp) | experiments.tex L150-151 + appendix.tex L431-432 | ✅ |\n\n### 缺失 ❌\n\n| 数据点 | 状态 | 说明 |\n|--------|------|------|\n| **CodeLlama-13B head-2048 vs tail-2048** | ❌ | 无 head-2048 实验数据 |\n\n---\n\n## 三、Non-Monotonicity Correction\n\n### 已写入 ✅\n\n正文和附录均已正确表述：仅 DeepSeek 在 tail-1024→2048 下降 1.5pp，非 universal pattern。\n\n- experiments.tex L147: \"only DeepSeek showing a mild architecture-specific reversal\"\n- appendix.tex L357: \"only DeepSeek-6.7B shows a mild −1.5pp decrease\"\n- appendix.tex L428-429: 明确说 \"while the other two models increase monotonically\"\n\n**状态**: ✅ 无需修改\n\n---\n\n## 四、总结\n\n### 已完成的 patch\n1. ✅ 3-model budget curve 表格和分析（Qwen-7B, DeepSeek, Qwen-1.5B）\n2. ✅ Phase transition / convergence / scale inversion 叙事\n3. ✅ 3-model head-tail gap 表格和分析\n4. ✅ Non-monotonicity 正确描述\n5. ✅ Budget curve figure (单模型版)\n\n### 待完成的 patch（按优先级）\n1. **P1**: CodeLlama-13B tail-512=97.5% 写入 Table 6（数据已有，立即可做）\n2. **P2**: 等待 CL-13B tail-256 和 tail-1024 实验完成后补全表格\n3. **P3**: 更新正文 \"three models\" → \"four models\"（待 P2 完成）\n4. **P4**: 更新 budget curve figure 为 4-model 版本\n5. **P5**: CodeLlama-13B head-tail gap 数据（需要 head-2048 实验）\n\n### 需要更新的章节列表\n| 文件 | 章节/位置 | 更新内容 |\n|------|-----------|----------|\n| `experiments.tex` | §4.5 Additional Analyses, L149-156 | 加入 CL-13B 数据，更新 \"three models\" |\n| `appendix.tex` | §Trace Length Full, Table 6 | 加 CL-13B 行 |\n| `appendix.tex` | §Trace Length Full, Table 7 | 加 CL-13B 行（待 head-2048 数据）|\n| `appendix.tex` | L382-383, L419 | \"three models\" → \"four models\" |\n| `appendix.tex` | budget_curve figure | 更新为多模型版本 |\n"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-18T01:48:58.239138+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/paper_patch_audit/paper_patch_status.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper_patch_status_20260518T014706",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-18T01:48:58.239301+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__save_project_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper_patch_status_20260518T014706",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__save_project_file",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-18T01:48:58.239429+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper_patch_status_20260518T014706",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-18T01:48:58.239559+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "register_artifact",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper_patch_status_20260518T014706",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "register_artifact",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-18T01:48:58.239673+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper_patch_status_20260518T014706",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-18T01:48:58.239785+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "artifact",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper_patch_status_20260518T014706",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "artifact",
    "max_results": "5"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-18T01:48:58.239894+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper_patch_status_20260518T014706",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-18T01:48:58.240053+00:00_

没有 `register_artifact` 工具可用。报告已写入本地路径。

---

## 审计结果摘要

**已写入论文的数据（完整）：**
- 3 模型 budget curve 完整数据（Qwen-7B / DeepSeek / Qwen-1.5B × tail-256/512/1024/2048）
- Phase transition、convergence、scale inversion 叙事
- 3 模型 head-tail gap 表格（15.5–22.6pp）
- Non-monotonicity 已正确修正为 "仅 DeepSeek, -1.5pp"

**缺失：**
1. **P1（立即可做）**: CodeLlama-13B tail-512=97.5% 未写入 Table 6
2. **P2（等实验）**: CL-13B tail-256 和 tail-1024 还在跑
3. **P3**: 正文多处 "three models" 需改为 "four models"（待 P2）
4. **P4**: Budget curve figure 需更新为 4-model 版本
5. **P5**: CL-13B head-2048 数据缺失，无法填 head-tail gap 表

报告已写到 `artifacts/paper_patch_audit/paper_patch_status.md`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_paper_patch_status_20260518T014706"
}
```

</details>

---
