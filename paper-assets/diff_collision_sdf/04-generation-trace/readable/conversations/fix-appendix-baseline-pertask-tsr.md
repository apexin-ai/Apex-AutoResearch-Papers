# fix appendix baseline pertask tsr

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 0
- **Tool calls:** 5
- **Original source:** `logs/chats/worker_fix_appendix_baseline_pertask_tsr_20260528T011343.jsonl`
- **Structured JSON:** [`d1b62394ced6f3f6f85c.json`](../../sessions/d1/d1b62394ced6f3f6f85c.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

11 recorded events

### Tool call

_source line 1 · 2026-05-28T01:14:19.453937+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/appendix.tex",
  "offset": "60",
  "limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_appendix_baseline_pertask_tsr_20260528T011343",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/appendix.tex",
    "offset": "60",
    "limit": "30"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-28T01:14:19.454279+00:00_

60	
61	\section{Per-Task TSR Breakdown}\label{sec:appendix_tsr_pertask}
62	
63	Table~\ref{tab:per_task_tsr} decomposes TSR by task for the avoidance source attribution experiments (Section~\ref{sec:avoidance_source}). All tasks retain meaningful success rates after fine-tuning, with Chocolate Pudding most resilient and Orange Juice most affected.
64	
65	\begin{table}[h]
66	\centering
67	\caption{Per-task TSR (\%) at 30K training steps. Baseline reports the original 3-seed evaluation (aggregate TSR\,=\,71.5\% under the unified seed-7 protocol; per-task reeval data not available). LoRA-only reports 3-seed means (re-evaluated with unified seed-7 protocol); SDF conditions report 3-seed means.}
68	\label{tab:per_task_tsr}
69	\vspace{2pt}
70	\small
71	\begin{tabular}{lcccc}
72	\toprule
73	Task & Pi0.5 Base & LoRA-only & SDF $\lambda{=}0.005$ & SDF $\lambda{=}0.01$ \\
74	 & (3 seeds) & (3 seeds) & (3 seeds) & (3 seeds) \\
75	\midrule
76	Orange Juice      & 70.7 & 30.0 & 33.3 & 24.7 \\
77	Choco.\ Pudding   & 86.0 & 70.7 & 78.0 & 76.7 \\
78	Milk              & 66.0 & 44.7 & 35.3 & 48.7 \\
79	BBQ Sauce         & 76.0 & 60.7 & 69.3 & 65.3 \\
80	\midrule
81	Mean              & 74.7 & 51.5 & 54.0 & 53.8 \\
82	\bottomrule
83	\end{tabular}
84	\end{table}
85	
86	\section{Per-Task CAR Breakdown}\label{sec:appendix_pertask_car}
87	
88	Table~\ref{tab:per_task_car} decomposes CAR by task for all fine-tuned conditions, supporting the claim that per-task ordering is preserved across SDF loss weights (\S\ref{sec:avoidance_source}). Chocolate Pudding is consistently highest and BBQ Sauce consistently lowest across all conditions, including $\lambda = 0.1$. The intermediate tasks (Orange Juice and Milk) exchange rank between seeds but remain bounded by the extremes. This invariance indicates that avoidance patterns reflect the spatial statistics of collision-free demonstrations rather than geometric supervision.
89	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_appendix_baseline_pertask_tsr_20260528T011343",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-28T01:14:19.454522+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/appendix.tex",
  "old_string": "Baseline reports the original 3-seed evaluation (aggregate TSR\\,=\\,71.5\\% under the unified seed-7 protocol; per-task reeval data not available). LoRA-only reports 3-seed means (re-evaluated with unified seed-7 protocol); SDF conditions report 3-seed means.",
  "new_string": "Baseline reports the unified seed-7 re-evaluation (aggregate TSR\\,=\\,71.5\\%). LoRA-only reports 3-seed means (re-evaluated with unified seed-7 protocol); SDF conditions report 3-seed means."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_appendix_baseline_pertask_tsr_20260528T011343",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/appendix.tex",
    "old_string": "Baseline reports the original 3-seed evaluation (aggregate TSR\\,=\\,71.5\\% under the unified seed-7 protocol; per-task reeval data not available). LoRA-only reports 3-seed means (re-evaluated with unified seed-7 protocol); SDF conditions report 3-seed means.",
    "new_string": "Baseline reports the unified seed-7 re-evaluation (aggregate TSR\\,=\\,71.5\\%). LoRA-only reports 3-seed means (re-evaluated with unified seed-7 protocol); SDF conditions report 3-seed means."
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-28T01:14:19.454803+00:00_

The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/appendix.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_appendix_baseline_pertask_tsr_20260528T011343",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-28T01:14:19.454952+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/appendix.tex",
  "old_string": " & (3 seeds) & (3 seeds) & (3 seeds) & (3 seeds) \\\\",
  "new_string": " & (seed\\,=\\,7) & (3 seeds) & (3 seeds) & (3 seeds) \\\\"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_appendix_baseline_pertask_tsr_20260528T011343",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/appendix.tex",
    "old_string": " & (3 seeds) & (3 seeds) & (3 seeds) & (3 seeds) \\\\",
    "new_string": " & (seed\\,=\\,7) & (3 seeds) & (3 seeds) & (3 seeds) \\\\"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-28T01:14:19.455159+00:00_

The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/appendix.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_appendix_baseline_pertask_tsr_20260528T011343",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-28T01:14:19.455296+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/appendix.tex",
  "old_string": "Orange Juice      & 70.7 & 30.0 & 33.3 & 24.7 \\\\\nChoco.\\ Pudding   & 86.0 & 70.7 & 78.0 & 76.7 \\\\\nMilk              & 66.0 & 44.7 & 35.3 & 48.7 \\\\\nBBQ Sauce         & 76.0 & 60.7 & 69.3 & 65.3 \\\\\n\\midrule\nMean              & 74.7 & 51.5 & 54.0 & 53.8 \\\\",
  "new_string": "Orange Juice      & 74.0 & 30.0 & 33.3 & 24.7 \\\\\nChoco.\\ Pudding   & 80.0 & 70.7 & 78.0 & 76.7 \\\\\nMilk              & 66.0 & 44.7 & 35.3 & 48.7 \\\\\nBBQ Sauce         & 66.0 & 60.7 & 69.3 & 65.3 \\\\\n\\midrule\nMean              & 71.5 & 51.5 & 54.0 & 53.8 \\\\"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_appendix_baseline_pertask_tsr_20260528T011343",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/appendix.tex",
    "old_string": "Orange Juice      & 70.7 & 30.0 & 33.3 & 24.7 \\\\\nChoco.\\ Pudding   & 86.0 & 70.7 & 78.0 & 76.7 \\\\\nMilk              & 66.0 & 44.7 & 35.3 & 48.7 \\\\\nBBQ Sauce         & 76.0 & 60.7 & 69.3 & 65.3 \\\\\n\\midrule\nMean              & 74.7 & 51.5 & 54.0 & 53.8 \\\\",
    "new_string": "Orange Juice      & 74.0 & 30.0 & 33.3 & 24.7 \\\\\nChoco.\\ Pudding   & 80.0 & 70.7 & 78.0 & 76.7 \\\\\nMilk              & 66.0 & 44.7 & 35.3 & 48.7 \\\\\nBBQ Sauce         & 66.0 & 60.7 & 69.3 & 65.3 \\\\\n\\midrule\nMean              & 71.5 & 51.5 & 54.0 & 53.8 \\\\"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-28T01:14:19.455513+00:00_

The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/appendix.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_appendix_baseline_pertask_tsr_20260528T011343",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-28T01:14:19.455683+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/appendix.tex",
  "offset": "60",
  "limit": "25"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_appendix_baseline_pertask_tsr_20260528T011343",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/appendix.tex",
    "offset": "60",
    "limit": "25"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-28T01:14:19.455826+00:00_

60	
61	\section{Per-Task TSR Breakdown}\label{sec:appendix_tsr_pertask}
62	
63	Table~\ref{tab:per_task_tsr} decomposes TSR by task for the avoidance source attribution experiments (Section~\ref{sec:avoidance_source}). All tasks retain meaningful success rates after fine-tuning, with Chocolate Pudding most resilient and Orange Juice most affected.
64	
65	\begin{table}[h]
66	\centering
67	\caption{Per-task TSR (\%) at 30K training steps. Baseline reports the unified seed-7 re-evaluation (aggregate TSR\,=\,71.5\%). LoRA-only reports 3-seed means (re-evaluated with unified seed-7 protocol); SDF conditions report 3-seed means.}
68	\label{tab:per_task_tsr}
69	\vspace{2pt}
70	\small
71	\begin{tabular}{lcccc}
72	\toprule
73	Task & Pi0.5 Base & LoRA-only & SDF $\lambda{=}0.005$ & SDF $\lambda{=}0.01$ \\
74	 & (seed\,=\,7) & (3 seeds) & (3 seeds) & (3 seeds) \\
75	\midrule
76	Orange Juice      & 74.0 & 30.0 & 33.3 & 24.7 \\
77	Choco.\ Pudding   & 80.0 & 70.7 & 78.0 & 76.7 \\
78	Milk              & 66.0 & 44.7 & 35.3 & 48.7 \\
79	BBQ Sauce         & 66.0 & 60.7 & 69.3 & 65.3 \\
80	\midrule
81	Mean              & 71.5 & 51.5 & 54.0 & 53.8 \\
82	\bottomrule
83	\end{tabular}
84	\end{table}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_appendix_baseline_pertask_tsr_20260528T011343",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-28T01:14:19.455998+00:00_

全部修改完成，验证通过：

1. Baseline per-task TSR：74.0 / 80.0 / 66.0 / 66.0 ✓
2. Mean = 71.5 ✓
3. Caption 已移除 "per-task reeval data not available"，改为 "unified seed-7 re-evaluation" ✓
4. Baseline 列头从 "(3 seeds)" 改为 "(seed=7)" ✓
5. LoRA 列不变：30.0 / 70.7 / 44.7 / 60.7 / 51.5 ✓
6. SDF 两列未改动 ✓

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_fix_appendix_baseline_pertask_tsr_20260528T011343"
}
```

</details>

---
