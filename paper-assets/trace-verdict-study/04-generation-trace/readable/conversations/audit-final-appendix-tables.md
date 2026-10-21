# audit final appendix tables

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 49
- **Recorded user turns:** 0
- **Tool calls:** 24
- **Original source:** `logs/chats/worker_audit_final-appendix-tables_20260523T191706.jsonl`
- **Structured JSON:** [`660edbe9e0c9ea88bb0a.json`](../../sessions/66/660edbe9e0c9ea88bb0a.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

49 recorded events

### Tool call

_source line 1 · 2026-05-23T19:27:44.675061+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_final-appendix-tables_20260523T191706",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/paper/appendix.tex"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-23T19:27:44.675460+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_final-appendix-tables_20260523T191706",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-23T19:27:44.675636+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_final-appendix-tables_20260523T191706",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/paper/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-23T19:27:44.675771+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_final-appendix-tables_20260523T191706",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-23T19:27:44.675891+00:00_

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
  "session": "worker_audit_final-appendix-tables_20260523T191706",
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

_source line 6 · 2026-05-23T19:27:44.676013+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_final-appendix-tables_20260523T191706",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-23T19:27:44.676152+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_final-appendix-tables_20260523T191706",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/appendix.tex"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-23T19:27:44.676309+00:00_

artifacts/_project/paper/appendix.tex
docs/paper/appendix.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_final-appendix-tables_20260523T191706",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-23T19:27:44.676439+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_final-appendix-tables_20260523T191706",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-23T19:27:44.676553+00:00_

artifacts/_project/paper/experiments.tex
docs/paper/experiments.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_final-appendix-tables_20260523T191706",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-23T19:27:44.676665+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "limit": "0",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_final-appendix-tables_20260523T191706",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "limit": "0",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-23T19:27:44.677184+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"no_trace_seed123\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-22T23:16:15.921Z\", \"updated_at\": \"2026-05-22T23:42:31.000Z\", \"hypothesis\": \"Replication of no_trace baseline with seed=123 to establish multi-seed statistics. Without execution traces, SFT should produce accuracy around 75% (matching seed42's result), confirming the no_trace baseline is stable across seeds.\", \"spec\": {\"command\": \"bash -c \\\"... python train/train_sft.py --condition no_trace --gpu 0 --gradient_checkpointing --seed 123\\\"\", \"server\": \"westd-11235\", \"data_path\": \"/root/trace-verdict-study/data/humaneval_trainset.jsonl\", \"data_count\": 1190, \"model_name\": \"Qwen/Qwen2.5-7B-Instruct\", \"seed\": 123, \"checkpoint_source\": \"trained_from_scratch\", \"eval_data\": \"humaneval_testset_1190\"}}, \"no_trace_seed456\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-22T23:16:16.072Z\", \"updated_at\": \"2026-05-22T23:16:26.102Z\", \"hypothesis\": \"Replication of no_trace baseline with seed=456 to establish multi-seed statistics. Without execution traces, SFT should produce accuracy around 75% (matching seed42's result), confirming the no_trace baseline is stable across seeds.\"}, \"attention_gradient_analysis\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T19:26:08.040Z\", \"updated_at\": \"2026-05-22T19:26:34.240Z\", \"hypothesis\": \"In full_trace models, execution trace tokens dominate input but receive disproportionately low attention and gradient signal at verdict position, demonstrating gradient dilution where non-diagnostic tokens dilute learning signal away from diagnostic content.\", \"spec\": {\"command\": \"attention gradient analysis script\", \"server\": \"westd-11235\", \"data_path\": \"/root/trace-verdict-study/data/\", \"data_count\": 1190, \"model_name\": \"Qwen/Qwen2.5-7B-Instruct\", \"seed\": 42, \"checkpoint
…[truncated 25684 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_final-appendix-tables_20260523T191706",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-23T19:27:44.677440+00:00_

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
  "session": "worker_audit_final-appendix-tables_20260523T191706",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/appendix.tex"
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-23T19:27:44.677575+00:00_

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
  "session": "worker_audit_final-appendix-tables_20260523T191706",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-23T19:27:44.677828+00:00_

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
  "session": "worker_audit_final-appendix-tables_20260523T191706",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-23T19:27:44.678333+00:00_

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
  "session": "worker_audit_final-appendix-tables_20260523T191706",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-23T19:27:44.678568+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/eval_results*.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_final-appendix-tables_20260523T191706",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/eval_results*.json"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-23T19:27:44.678698+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_final-appendix-tables_20260523T191706",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-23T19:27:44.678816+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/results*.csv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_final-appendix-tables_20260523T191706",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/results*.csv"
  }
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-23T19:27:44.678932+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/artifacts/**/*.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_final-appendix-tables_20260523T191706",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/artifacts/**/*.json"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-23T19:27:44.679042+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_final-appendix-tables_20260523T191706",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-23T19:27:44.679169+00:00_

artifacts/dream_reports/dream_20260515T013018/best/experiment_data.json
artifacts/dream_reports/dream_20260515T013018/median/experiment_data.json
artifacts/dream_reports/dream_20260515T013018/worst/experiment_data.json
artifacts/dream_reports/dream_20260515T084908/best/experiment_data.json
artifacts/dream_reports/dream_20260515T084908/median/experiment_data.json
artifacts/dream_reports/dream_20260515T084908/worst/experiment_data.json
artifacts/_project/data/trace_ablation_bootstrap.json
artifacts/trace_ablation_bootstrap.json
artifacts/_project/data/regex_baseline_results.json
artifacts/regex_baseline_analysis/data/regex_baseline_results.json
artifacts/_project/data/debugbench_results_04bcfc.json
artifacts/_project/data/debugbench_results.json
artifacts/_project/data/c1_edge_samples.json
artifacts/_project/report/cluster_robust_ci.json
artifacts/analysis/cluster_robust_ci.json
artifacts/cluster_robust_ci.json
artifacts/dream_reports/dream_20260516T105259/best/experiment_data.json
artifacts/dream_reports/dream_20260516T105259/median/experiment_data.json
artifacts/dream_reports/dream_20260516T105259/worst/experiment_data.json
artifacts/dream_reports/dream_20260516T155731/best/experiment_data.json
artifacts/dream_reports/dream_20260516T155731/median/experiment_data.json
artifacts/dream_reports/dream_20260516T155731/worst/experiment_data.json
artifacts/_project/data/table1_final.json
artifacts/table1_final.json
artifacts/dream_reports/dream_20260518T113804/best/experiment_data.json
artifacts/dream_reports/dream_20260518T113804/median/experiment_data.json
artifacts/dream_reports/dream_20260518T113804/worst/experiment_data.json
artifacts/dream_reports/dream_20260518T125926/best/experiment_data.json
artifacts/dream_reports/dream_20260518T125926/median/experiment_data.json
artifacts/dream_reports/dream_20260518T125926/worst/experiment_data.json
artifacts/deepseek_label_only_seed42/data/deepseek_label_only_seed42_results.json
artifacts/deepseek_label_only_seed42_results.json
…[truncated 550 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_final-appendix-tables_20260523T191706",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-23T19:27:44.679392+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/_project/data/table1_final.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_final-appendix-tables_20260523T191706",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/_project/data/table1_final.json"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-23T19:27:44.679643+00:00_

1	[
2	  {
3	    "model": "Qwen-2.5-Coder-7B",
4	    "condition": "no_trace",
5	    "accuracy": 0.7513,
6	    "ci_lower": 0.7277,
7	    "ci_upper": 0.7748,
8	    "n": 1190,
9	    "lift": 0.0362,
10	    "exp_id": "no_trace_seed42_v5",
11	    "seeds": 1
12	  },
13	  {
14	    "model": "Qwen-2.5-Coder-7B",
15	    "condition": "full_trace",
16	    "accuracy": 0.8176,
17	    "ci_lower": 0.7970,
18	    "ci_upper": 0.8390,
19	    "n": 1190,
20	    "lift": 0.1025,
21	    "exp_id": "full_trace_seed42_v5",
22	    "seeds": 1
23	  },
24	  {
25	    "model": "Qwen-2.5-Coder-7B",
26	    "condition": "label_only",
27	    "accuracy": 0.8648,
28	    "ci_lower": 0.8454,
29	    "ci_upper": 0.8842,
30	    "n": 1190,
31	    "lift": 0.1497,
32	    "exp_id": "label_only_seed123",
33	    "seeds": 2,
34	    "seed_values": [0.8706, 0.8590],
35	    "std": 0.0082
36	  },
37	  {
38	    "model": "Qwen-2.5-Coder-7B",
39	    "condition": "loop_only",
40	    "accuracy": 0.8605,
41	    "ci_lower": 0.8350,
42	    "ci_upper": 0.8840,
43	    "n": 1190,
44	    "lift": 0.1454,
45	    "exp_id": "loop_only_seed123",
46	    "seeds": 3,
47	    "seed_values": [0.8588, 0.8664, 0.8563],
48	    "std": 0.0043
49	  },
50	  {
51	    "model": "Qwen-2.5-Coder-7B",
52	    "condition": "VOTA",
53	    "accuracy": 0.9941,
54	    "ci_lower": 0.9882,
55	    "ci_upper": 0.9983,
56	    "n": 1190,
57	    "lift": 0.2790,
58	    "exp_id": "vota_seed42_v5",
59	    "seeds": 1
60	  },
61	  {
62	    "model": "Qwen-2.5-Coder-7B",
63	    "condition": "exception_only",
64	    "accuracy": 0.9983,
65	    "ci_lower": 0.9958,
66	    "ci_upper": 1.0000,
67	    "n": 1190,
68	    "lift": 0.2832,
69	    "exp_id": "exception_only_seed123",
70	    "seeds": 3,
71	    "seed_values": [0.9983, 0.9983, 0.9983],
72	    "std": 0.0000
73	  },
74	  {
75	    "model": "Qwen-2.5-Coder-7B",
76	    "condition": "ae_only",
77	    "accuracy": 0.9964,
78	    "ci_lower": 0.9930,
79	    "ci_upper": 0.9998,
80	    "n": 1190,
81	    "lift": 0.2813,
82	    "exp_id": "v
…[truncated 4327 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_final-appendix-tables_20260523T191706",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-23T19:27:44.679801+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/_project/data/regex_baseline_results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_final-appendix-tables_20260523T191706",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/_project/data/regex_baseline_results.json"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-23T19:27:44.679987+00:00_

1	{
2	  "experiment_id": "regex_baseline_analysis",
3	  "dataset": "HumanEval+MBPP_exception_only_test",
4	  "n": 1190,
5	  "majority_baseline": 0.7151,
6	  "sft_exception_only": 0.9983,
7	  "baselines": {
8	    "B1_ERROR_presence": {
9	      "accuracy": 0.9345,
10	      "description": "Checks if 'ERROR' keyword appears in exception text"
11	    },
12	    "B2_Traceback": {
13	      "accuracy": 0.7151,
14	      "description": "Checks if 'Traceback' appears in exception text"
15	    },
16	    "B3_any_keyword": {
17	      "accuracy": 0.9345,
18	      "description": "Any error keyword match (union of patterns)"
19	    },
20	    "B4_exception_type": {
21	      "accuracy": 0.9361,
22	      "description": "Named exception type detection (e.g. ValueError, TypeError)"
23	    },
24	    "B5_format_marker": {
25	      "accuracy": 0.9933,
26	      "description": "Format-based verdict marker detection (structural pattern)"
27	    },
28	    "B6_error_count_ge2": {
29	      "accuracy": 0.9202,
30	      "description": "Two or more error occurrences in trace"
31	    }
32	  },
33	  "best_semantic_regex": {
34	    "name": "B4_exception_type",
35	    "accuracy": 0.9361,
36	    "gap_vs_sft_pp": -6.22
37	  },
38	  "best_overall_regex": {
39	    "name": "B5_format_marker",
40	    "accuracy": 0.9933,
41	    "gap_vs_sft_pp": -0.50,
42	    "mcnemar_p_vs_sft": 0.041
43	  },
44	  "conclusion": "Best regex 93.61% (semantic) / 99.33% (format). SFT 99.83% significantly better than strongest regex (McNemar p=0.041). SFT learns patterns beyond simple regex matching.",
45	  "source": "registry:regex_baseline_analysis"
46	}
47	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_final-appendix-tables_20260523T191706",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-23T19:27:44.680246+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/_project/data/debugbench_results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_final-appendix-tables_20260523T191706",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/_project/data/debugbench_results.json"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-23T19:27:44.680432+00:00_

1	{
2	  "dataset": "DebugBench",
3	  "task_type": "bug_detection",
4	  "model": "Qwen-2.5-Coder-7B",
5	  "n_test": 426,
6	  "majority_baseline": 0.5141,
7	  "conditions": {
8	    "exception_only": {
9	      "accuracy": 1.0000,
10	      "accuracy_ci_wilson": [0.9914, 1.0000],
11	      "pass_precision": 1.0, "pass_recall": 1.0, "pass_f1": 1.0,
12	      "fail_precision": 1.0, "fail_recall": 1.0, "fail_f1": 1.0,
13	      "lift_vs_majority": 0.4859,
14	      "train_loss": 0.2435,
15	      "eval_loss": 0.4157,
16	      "exp_id": "debugbench_exception_only_seed42"
17	    },
18	    "vota": {
19	      "accuracy": 0.9977,
20	      "accuracy_ci": [0.993, 1.0],
21	      "pass_precision": 1.0, "pass_recall": 1.0, "pass_f1": 1.0,
22	      "fail_precision": 1.0, "fail_recall": 1.0, "fail_f1": 1.0,
23	      "lift_vs_majority": 0.4836,
24	      "errors": 1,
25	      "train_loss": 0.098,
26	      "eval_loss": 0.1179,
27	      "exp_id": "debugbench_vota_seed42"
28	    },
29	    "no_trace": {
30	      "accuracy": 0.9671,
31	      "accuracy_ci": [0.948, 0.984],
32	      "pass_precision": 1.0, "pass_recall": 0.936, "pass_f1": 0.967,
33	      "fail_precision": 0.937, "fail_recall": 1.0, "fail_f1": 0.967,
34	      "lift_vs_majority": 0.4531,
35	      "train_loss": 0.249,
36	      "eval_loss": 0.532,
37	      "exp_id": "debugbench_no_trace_seed42"
38	    }
39	  },
40	  "key_finding": "Exception_only achieves perfect accuracy (100%) on DebugBench, confirming cross-task generalization. Even no_trace baseline is 96.71% (DebugBench bugs almost always throw exceptions).",
41	  "source": "registry:debugbench_*_seed42"
42	}
43	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_final-appendix-tables_20260523T191706",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-23T19:27:44.680583+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/_project/data/cross_model_calibration_results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_final-appendix-tables_20260523T191706",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/_project/data/cross_model_calibration_results.json"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-23T19:27:44.680707+00:00_

1	qwen_7b: ECE=0.0027 MCE=0.8355 Brier=0.0013 Acc=0.9983\nqwen_1.5b: ECE=0.0020 MCE=0.7549 Brier=0.0013 Acc=0.9983\ncodellama_13b: ECE=0.0020 MCE=0.0411 Brier=0.0013 Acc=0.9983\ndeepseek_6.7b: ECE=0.0064 MCE=0.7756 Brier=0.0061 Acc=0.9933

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_final-appendix-tables_20260523T191706",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-23T19:27:44.680824+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/_project/data/trace_ablation_bootstrap.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_final-appendix-tables_20260523T191706",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/_project/data/trace_ablation_bootstrap.json"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-23T19:27:44.681003+00:00_

1	{
2	  "paired_tests": [
3	    {
4	      "pair": "256tok vs 512tok",
5	      "n_samples": 1190,
6	      "acc_a": 0.788235294117647,
7	      "acc_b": 0.8042016806722689,
8	      "diff": -0.015966386554621903,
9	      "ci_lower": -0.03529411764705892,
10	      "ci_upper": 0.003361344537815114,
11	      "p_value": 0.11698830116988301,
12	      "sig": "ns"
13	    },
14	    {
15	      "pair": "512tok vs 1024tok",
16	      "n_samples": 1190,
17	      "acc_a": 0.8042016806722689,
18	      "acc_b": 0.7722689075630252,
19	      "diff": 0.031932773109243695,
20	      "ci_lower": 0.01092436974789912,
21	      "ci_upper": 0.05294117647058827,
22	      "p_value": 0.0021997800219978004,
23	      "sig": "**"
24	    },
25	    {
26	      "pair": "1024tok vs no_limit",
27	      "n_samples": 1190,
28	      "acc_a": 0.7722689075630252,
29	      "acc_b": 0.8176470588235294,
30	      "diff": -0.04537815126050415,
31	      "ci_lower": -0.06554621848739495,
32	      "ci_upper": -0.025210084033613467,
33	      "p_value": 0.00019998000199980003,
34	      "sig": "***"
35	    },
36	    {
37	      "pair": "256tok vs no_limit",
38	      "n_samples": 1190,
39	      "acc_a": 0.788235294117647,
40	      "acc_b": 0.8176470588235294,
41	      "diff": -0.02941176470588236,
42	      "ci_lower": -0.05044117647058825,
43	      "ci_upper": -0.008403361344537896,
44	      "p_value": 0.0057994200579942,
45	      "sig": "**"
46	    },
47	    {
48	      "pair": "256tok vs no_trace",
49	      "n_samples": 1190,
50	      "acc_a": 0.788235294117647,
51	      "acc_b": 0.7512605042016807,
52	      "diff": 0.036974789915966366,
53	      "ci_lower": 0.014285714285714235,
54	      "ci_upper": 0.060504201680672276,
55	      "p_value": 0.0023997600239976003,
56	      "sig": "**"
57	    },
58	    {
59	      "pair": "512tok vs no_trace",
60	      "n_samples": 1190,
61	      "acc_a": 0.8042016806722689,
62	      "acc_b": 0.7512605042016807,
63	      "diff": 0.05294117647058827,
64	      "ci_lower": 0.030252100840336138,

…[truncated 3316 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_final-appendix-tables_20260523T191706",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-23T19:27:44.681181+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/artifacts/**/*calibration*"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_final-appendix-tables_20260523T191706",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/artifacts/**/*calibration*"
  }
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-23T19:27:44.681350+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/artifacts/**/*nomarker*"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_final-appendix-tables_20260523T191706",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/artifacts/**/*nomarker*"
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-23T19:27:44.681478+00:00_

artifacts/plot_calibration.py
artifacts/calibration_analysis_seed42/chart/calibration_reliability_diagram_info.txt
artifacts/calibration_analysis_seed42/data/calibration_metrics_summary.txt
artifacts/calibration_analysis_seed42/data/calibration_v2.py
artifacts/_project/chart/fig2_calibration.pdf
artifacts/_project/chart/fig2_calibration_info.md
artifacts/_project/chart/calibration_reliability_ref.md
artifacts/_project/report/cross_model_calibration.md
artifacts/cross_model_calibration.md
artifacts/_project/data/cross_model_calibration_results.json
artifacts/_project/report/calibration_report.md
artifacts/calibration_report.md
artifacts/_project/report/calibration_analysis.md
artifacts/calibration_analysis.md
artifacts/_project/paper/figures/calibration_reliability.pdf
artifacts/_project/paper/figures/calibration_reliability.png
artifacts/_project/report/calibration_cross_model_analysis.md
artifacts/calibration_cross_model_analysis.md
artifacts/cross_model_calibration/data/cross_model_calibration_results.txt
artifacts/_project/report/cross_model_calibration_plan019.md
artifacts/_project/chart/cross_model_calibration_plan019_diagram_ref.txt
artifacts/_project/data/cross_model_calibration_plan019_data.txt
artifacts/_project/report/cross_model_calibration_plan019_a3fb00.md
artifacts/cross_model_calibration_plan019.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_final-appendix-tables_20260523T191706",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-23T19:27:44.681600+00:00_

artifacts/nomarker_command.txt

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_final-appendix-tables_20260523T191706",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-23T19:27:44.681710+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/artifacts/**/*cross*"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_final-appendix-tables_20260523T191706",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/artifacts/**/*cross*"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-23T19:27:44.681828+00:00_

artifacts/cross_model_analysis/cross_model_comparison.md
artifacts/_project/report/cross_model_comparison.md
artifacts/_project/chart/fig3_cross_model_gap.pdf
artifacts/exception_only_seed_cross_analysis.md
artifacts/_project/chart/fig3_cross_model_gap_info.md
artifacts/_project/report/debugbench_cross_task_analysis.md
artifacts/debugbench_cross_task_analysis.md
artifacts/_project/report/cross_model_exception_only_overlap.md
artifacts/cross_model_exception_only_overlap.md
artifacts/_project/paper/cross_family_analysis_draft.md
artifacts/cross_family_analysis_draft.md
artifacts/_project/report/cross_model_comparison_table.md
artifacts/cross_model_comparison_table.md
artifacts/_project/report/cross_model_calibration.md
artifacts/cross_model_calibration.md
artifacts/_project/data/cross_model_calibration_results.json
artifacts/_project/report/calibration_cross_model_analysis.md
artifacts/calibration_cross_model_analysis.md
artifacts/cross_model_calibration/data/cross_model_calibration_results.txt
artifacts/_project/report/cross_model_calibration_plan019.md
artifacts/_project/chart/cross_model_calibration_plan019_diagram_ref.txt
artifacts/_project/data/cross_model_calibration_plan019_data.txt
artifacts/_project/report/cross_model_calibration_plan019_a3fb00.md
artifacts/cross_model_calibration_plan019.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_final-appendix-tables_20260523T191706",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-23T19:27:44.681955+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/artifacts/**/*per_class*"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_final-appendix-tables_20260523T191706",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/artifacts/**/*per_class*"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-23T19:27:44.682067+00:00_

artifacts/per_class_breakdown.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_final-appendix-tables_20260523T191706",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-23T19:27:44.682175+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/calibration_analysis_seed42/data/calibration_metrics_summary.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_final-appendix-tables_20260523T191706",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/calibration_analysis_seed42/data/calibration_metrics_summary.txt"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-23T19:27:44.682313+00:00_

1	Server path: /root/autodl-tmp/trace-verdict-study-checkpoints/calibration/calibration_metrics.json
2	
3	Summary:
4	No Trace:       Acc=0.7513  ECE=0.1715  MCE=0.4754  Brier=0.1972
5	Full Trace:     Acc=0.8176  ECE=0.0946  MCE=0.2490  Brier=0.1438
6	Exception Only: Acc=0.9983  ECE=0.0024  MCE=0.8359  Brier=0.0013
7	VOTA:           Acc=0.9941  ECE=0.0054  MCE=0.6211  Brier=0.0052
8	
9	Note: High MCE for Exception Only and VOTA is due to sparse low-confidence bins (1-2 samples).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_final-appendix-tables_20260523T191706",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-23T19:27:44.682431+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/_project/report/cross_model_calibration.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_final-appendix-tables_20260523T191706",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/_project/report/cross_model_calibration.md"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-23T19:27:44.682577+00:00_

1	# Cross-Model Calibration Analysis: Exception-Only Condition
2	
3	**Date**: 2026-05-18
4	**Test set**: 1190 samples (851 pass, 339 fail)
5	**Method**: Greedy generation + logit-based confidence (softmax over pass/fail token logits)
6	**Bins**: 10 equal-width bins from 0.5 to 1.0
7	
8	## Summary Table
9	
10	| Model | Accuracy | ECE | MCE | Brier Score |
11	|---|---|---|---|---|
12	| Qwen-7B | 0.9983 | 0.002717 | 0.8355 | 0.001311 |
13	| Qwen-1.5B | 0.9983 | 0.001976 | 0.7549 | 0.001255 |
14	| DeepSeek-6.7B | 0.9933 | 0.006411 | 0.7756 | 0.006126 |
15	| CodeLlama-13B | 0.9983 | 0.002039 | 0.0411 | 0.001310 |
16	
17	## Per-Class Calibration
18	
19	| Model | Class | ECE | MCE | Brier | n |
20	|---|---|---|---|---|---|
21	| Qwen-7B | pass | 0.0037 | 0.8355 | 0.0018 | 851 |
22	| Qwen-7B | fail | 0.0003 | 0.0003 | 0.0000 | 339 |
23	| Qwen-1.5B | pass | 0.0027 | 0.7549 | 0.0018 | 851 |
24	| Qwen-1.5B | fail | 0.0003 | 0.0003 | 0.0000 | 339 |
25	| DeepSeek-6.7B | pass | 0.0069 | 0.9149 | 0.0081 | 851 |
26	| DeepSeek-6.7B | fail | 0.0079 | 0.4073 | 0.0012 | 339 |
27	| CodeLlama-13B | pass | 0.0016 | 0.0411 | 0.0018 | 851 |
28	| CodeLlama-13B | fail | 0.0033 | 0.0033 | 0.0000 | 339 |
29	
30	## Reliability Diagram Data (non-empty bins only)
31	
32	### Qwen-7B
33	| Bin | Confidence | Accuracy | Count |
34	|---|---|---|---|
35	| [0.80, 0.85) | 0.835 | 0.000 | 1 |
36	| [0.90, 0.95) | 0.942 | 0.857 | 7 |
37	| [0.95, 1.00] | 0.998 | 1.000 | 1182 |
38	
39	### Qwen-1.5B
40	| Bin | Confidence | Accuracy | Count |
41	|---|---|---|---|
42	| [0.75, 0.80) | 0.755 | 0.000 | 1 |
43	| [0.90, 0.95) | 0.907 | 0.857 | 7 |
44	| [0.95, 1.00] | 0.999 | 1.000 | 1182 |
45	
46	### DeepSeek-6.7B
47	| Bin | Confidence | Accuracy | Count |
48	|---|---|---|---|
49	| [0.55, 0.60) | 0.593 | 1.000 | 1 |
50	| [0.75, 0.80) | 0.798 | 1.000 | 2 |
51	| [0.80, 0.85) | 0.835 | 1.000 | 1 |
52	| [0.85, 0.90) | 0.883 | 1.000 | 8 |
53	| [0.90, 0.95) | 0.918 | 0.143 | 7 |
54	| [0.95, 1.00] | 0.998 | 0.998 | 1171 |
55	
…[truncated 2102 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_final-appendix-tables_20260523T191706",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-23T19:27:44.682721+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/_project/data/cross_model_calibration_plan019_data.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_final-appendix-tables_20260523T191706",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/_project/data/cross_model_calibration_plan019_data.txt"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-23T19:27:44.682842+00:00_

1	Qwen2.5-7B: acc=0.9983 ece=0.002717 mce=0.835484 brier=0.001311 conf=0.998006
2	DeepSeek-6.7B: acc=0.9933 ece=0.004890 mce=0.469227 brier=0.005887 conf=0.997062
3	CodeLlama-13B: acc=0.9983 ece=0.001971 mce=0.041056 brier=0.001310 conf=0.996348
4	Qwen2.5-1.5B: acc=0.9983 ece=0.001976 mce=0.754915 brier=0.001255 conf=0.998203
5	
6	Full JSON with reliability bins at remote: /root/trace-verdict-study/artifacts/cross_model_calibration_plan019.json

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_final-appendix-tables_20260523T191706",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-23T19:27:44.683205+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/cross_model_calibration/data/cross_model_calibration_results.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_final-appendix-tables_20260523T191706",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/cross_model_calibration/data/cross_model_calibration_results.txt"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-23T19:27:44.683407+00:00_

1	Cross-model Calibration Results (exception_only, n=1190)
2	
3	Model            Accuracy   ECE      MCE      Brier
4	Qwen2.5-7B      0.9983     0.0027   0.8355   0.0013
5	Qwen2.5-1.5B    0.9983     0.0020   0.7549   0.0013
6	CodeLlama-13B   0.9983     0.0020   0.0411   0.0013
7	DeepSeek-6.7B   0.9933     0.0064   0.7756   0.0061
8	
9	Findings:
10	- ECE < 0.007 for all 4 models: calibration quality is universally strong
11	- 3/4 models achieve identical accuracy (99.83%), DeepSeek slightly lower (99.33%)
12	- Brier scores tightly clustered: 0.0013 for 3 models, 0.0061 for DeepSeek
13	- CodeLlama-13B has notably low MCE (0.041), indicating no high-confidence errors
14	- DeepSeek-6.7B weakest but still excellent calibration
15	
16	Source: /root/autodl-tmp/trace-verdict-study-checkpoints/cross_model_calibration/

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_final-appendix-tables_20260523T191706",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 49 · 2026-05-23T19:27:44.683631+00:00_

Audit complete. Here is the full report.

---

## Appendix Tables 5–23 数据审计报告

**核对范围**: 19 个数据表, ~250+ 个数值单元格
**数据源**: registry (36 experiments), table1_final.json, regex_baseline_results.json, debugbench_results.json, cross_model_calibration_results.json/txt, trace_ablation_bootstrap.json, calibration_metrics_summary.txt

---

### ❌ 必须修复 (4 issues)

**Issue 1: tab:per_class — 3 行 Acc 列用了 3-seed mean, P/R/F1 用 seed42**

Caption 标注 "seed 42"，但 VOTA/loop_only/Full Trace (LO) 的 Acc 列是 3-seed mean：

| Row | Acc(论文) | 来源 | Acc(seed42) | P/R/F1验算→Acc |
|-----|----------|------|-------------|---------------|
| VOTA, Qwen-7B | 99.05 | 3-seed mean | 99.41 | Pass R=99.18 → 7 errors → **99.41** |
| loop_only, Qwen-7B | 86.05 | 3-seed mean | 85.63 | Pass R=87.07 + Fail R=82.01 → 171 errors → **85.63** |
| Full Trace (LO), Qwen-7B | 85.94 | 3-seed mean | 86.22 | Pass R=93.18 + Fail R=68.73 → 164 errors → **86.22** |

修复方案：将这 3 行的 Acc 改为 seed42 值 (99.41/85.63/86.22)。

---

**Issue 2: VOTA regex Δ 三处不一致**

| 位置 | 值 | 来源 |
|------|---|------|
| tab:regex_cross_format (appendix table) | Δ=+23.50 | 99.05(3-seed) − 75.55 |
| appendix text (§B.10 inline) | +23.86 | 99.41(seed42) − 75.55 |
| experiments.tex line 105 | "+3.62–23.86pp" | same seed42 calc |

表和正文自相矛盾。修复方案：统一为 +23.50 (与表一致，用 3-seed mean) 或全改为 +6.22 (exception_only) 作为 max Δ 并重述。

---

**Issue 3: 两个 calibration 表 ECE 值不同**

tab:calibration_cross (§B.8) 和 tab:calibration_model_level (§C.1) 报告了同一组实验的不同 ECE：

| Model | tab:calibration_cross ECE | tab:calibration_model_level ECE | 差异 |
|-------|--------------------------|-------------------------------|------|
| Qwen-1.5B | 0.0020 | 0.0014 | −0.0006 |
| Qwen-7B | 0.0027 | 0.0017 | −0.0010 |
| DeepSeek-6.7B | 0.0064 | 0.0048 | −0.0016 |
| CodeLlama-13B | 0.0020 | 0.0020 | 0.0000 |

数据溯源：tab:calibration_cross 来自 cross_model_calibration_results.txt (bins 0.5–1.0)；tab:calibration_model_level 来自 plan019 run (不同 bin 配置)。

修复方案：统一 bin 配置，保留一个表删除另一个，或在 caption 明确标注 bin 差异。

---

**Issue 4: Qwen-7B tail-256 两表数值不一致**

| 表 | 值 |
|----|---|
| tab:trace_length (§B.7) | 77.48 |
| tab:tail_cross_model (§B.7) | 78.9 |

同一实验 (Qwen-7B, seed=42, N=1190) 不应有两个不同数值。78.9 可能误用了 head-256 (78.82→78.8)。

修复方案：核实原始 eval 结果，统一为正确值。

---

### ⚠️ 需确认 (4 items)

| # | 位置 | 问题 | 详情 |
|---|------|------|------|
| 5 | tab:calibration, full_trace ECE | 0.096 vs raw 0.0946 | 0.0946 at 3dp = 0.095, not 0.096 |
| 6 | tab:tail512_seeds, Qwen-7B σ | 2.05 vs computed 2.03 | 微小差异，可能由于显示精度 |
| 7 | tab:tail_cross_model, CL exc_only | 99.89 (3-seed mean) | 其他列均为 seed42，此处混用 |
| 8 | tab:density, grad mask 3-seed | mean=99.22±0.20 | seed123 registry 状态 PREPARING，未见结果 |

---

### ✅ 已验证一致 (全部表)

| Table | 内容 | 核对数 | 结果 |
|-------|------|--------|------|
| tab:full_qwen | Qwen-7B 全条件全 seed | 24 cells | ✅ mean/std 全部正确 |
| tab:full_deepseek | DS-6.7B 全条件全 seed | 16 cells | ✅ |
| tab:exc_subcomponent | 3 子成分 ablation | 12 cells | ✅ registry 完全匹配 |
| tab:trace_length | Head-truncation 4 条件 | 8 cells + CIs | ✅ bootstrap JSON 完全匹配 |
| tab:trace_length_pairwise | 12 对 pairwise bootstrap | 48 cells | ✅ JSON 精确匹配 |
| tab:tail512_seeds | 4 模型 ×3 seed at tail-512 | 20 cells | ✅ (σ 微偏 ⚠️) |
| tab:head_vs_tail | 4 模型 head vs tail | 9 cells | ✅ gaps 精确 |
| tab:calibration | Qwen-7B 5 条件 calibration | 10 cells | ✅ (full_trace ECE ⚠️) |
| tab:calibration_cross | 4 模型 cross-model cal | 12 cells | ✅ 与 raw data 匹配 |
| tab:exception_type | 10 类异常分类准确率 | 20 cells | ✅ 样本总和=1190 |
| tab:dedup | 去重统计 | 9 cells | ✅ 比例精确 |
| tab:regex | 6 regex baselines | 8 cells | ✅ JSON 完全匹配 |
| tab:regex_cross_format | 4 格式 SFT vs regex | 12 cells | ✅ Δ 算术正确 |
| tab:zeroshot_cross_model | 4 模型 zero-shot vs SFT | 16 cells | ✅ 范围/Δ 正确 |
| tab:debugbench | DebugBench 3 条件 | 8 cells | ✅ JSON 完全匹配 |
| tab:hyperparams | 超参数 | config | ✅ (非数据) |
| tab:train_time | 训练时间 | config | ✅ (非数据) |

---

### 主文↔Appendix 引用一致性

| 主文引用 | 值 | Appendix 值 | 状态 |
|----------|---|-------------|------|
| ECE 63× gap (experiments.tex:198) | 0.171/0.0027=63.3 | tab:calibration | ✅ |
| All ECE<0.007 (experiments.tex:199) | ref tab:calibration_model_level | 0.0014–0.0048 | ✅ |
| "+3.62–23.86pp" (experiments.tex:105) | — | tab:regex_cross_format max Δ=23.50 | ❌ |
| nomarker 97.65±0.96 (experiments.tex:120) | — | 无 appendix 表 | ✅ (自洽) |
| Cross-dataset 99.41% N=4270 (experiments.tex:127) | — | 无 appendix 表 | ✅ |
| Tier boundary 12.48pp (experiments.tex:100) | 98.53−86.05 | tab:cross_model | ✅ |

---

### 汇总

| 类别 | 数量 |
|------|------|
| 核对总数 | ~250 cells |
| ✅ 一致 | ~240 |
| ❌ 必须修复 | **4** (per_class 3行 Acc, VOTA Δ 矛盾, 2个 calibration 表, tail-256 矛盾) |
| ⚠️ 需确认 | **4** (rounding/labeling/registry gap) |

4 个 ❌ 都是同类问题：**seed42 vs 3-seed mean 混用**或**不同运行结果未统一**。建议在 DDL 前统一数据源并 one-pass 替换。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_audit_final-appendix-tables_20260523T191706"
}
```

</details>

---
