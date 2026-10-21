# fix reviewer w1 w2 issues

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 155
- **Recorded user turns:** 0
- **Tool calls:** 77
- **Original source:** `logs/chats/worker_fix_reviewer_w1_w2_issues_20260525T204337.jsonl`
- **Structured JSON:** [`e31bdff7cee4f6be8781.json`](../../sessions/e3/e31bdff7cee4f6be8781.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

155 recorded events

### Tool call

_source line 1 · 2026-05-25T20:53:38.984452+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Find crossmodel and perseed tables",
  "prompt": "Find the exact file paths for:\n1. The crossmodel detail table (tab_crossmodel_detail or similar) - likely in /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/_project/paper/ or paper/sections/\n2. The perseed table for TG (tab_perseed or similar)\n3. The cost table (tab_cost or similar)\n4. Any tex files in paper/sections/ that mention \"SS\" gap ratio like \"1.2\" or \"7.8\" or \"7.9\"\n\nSearch in /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/\n\nReport back the exact file paths and the relevant line numbers/content."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Agent",
  "tool_args": {
    "subagent_type": "Explore",
    "description": "Find crossmodel and perseed tables",
    "prompt": "Find the exact file paths for:\n1. The crossmodel detail table (tab_crossmodel_detail or similar) - likely in /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/_project/paper/ or paper/sections/\n2. The perseed table for TG (tab_perseed or similar)\n3. The cost table (tab_cost or similar)\n4. Any tex files in paper/sections/ that mention \"SS\" gap ratio like \"1.2\" or \"7.8\" or \"7.9\"\n\nSearch in /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/\n\nReport back the exact file paths and the relevant line numbers/content."
  }
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-25T20:53:38.984834+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/**/*crossmodel*"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Glob",
  "tool_args": {
    "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/**/*crossmodel*"
  }
}
```

</details>

---

### Tool result

_source line 3 · 2026-05-25T20:53:38.985016+00:00_

logs/workers/worker_viz_gate_profile_crossmodel_20260522T152840.log
logs/chats/worker_viz_gate_profile_crossmodel_20260522T152840.lock
logs/chats/worker_viz_gate_profile_crossmodel_20260522T152840.jsonl
logs/workers/worker_viz_gate_profile_crossmodel_20260522T152840_result.json
artifacts/_project/chart/fig_gate_profile_crossmodel_info.txt
artifacts/fig_gate_profile_crossmodel.pdf
artifacts/fig_gate_profile_crossmodel.png
logs/workers/worker_code_appendix_seeds_perturn_crossmodel_20260524T150612.log
logs/chats/worker_code_appendix_seeds_perturn_crossmodel_20260524T150612.lock
logs/chats/worker_code_appendix_seeds_perturn_crossmodel_20260524T150612.jsonl
logs/workers/worker_code_appendix_seeds_perturn_crossmodel_20260524T150612_result.json
artifacts/appendix_expansion/tab_crossmodel_detail.tex
figures/paper/gen_fig_gate_profile_crossmodel.py
figures/paper/fig_gate_profile_crossmodel.pdf
figures/paper/fig_gate_profile_crossmodel.png
figures/paper/gen_fig_crossmodel.py
figures/paper/fig_crossmodel.pdf
figures/paper/fig_crossmodel.png

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-25T20:53:38.985169+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/**/*perseed*"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Glob",
  "tool_args": {
    "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/**/*perseed*"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-25T20:53:38.985300+00:00_

artifacts/appendix_expansion/tab_perseed_ss.tex
artifacts/appendix_expansion/tab_perseed_tg.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-25T20:53:38.985463+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/**/*cost*"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Glob",
  "tool_args": {
    "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/**/*cost*"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-25T20:53:38.985602+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-25T20:53:38.985729+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/_project/paper/**/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Glob",
  "tool_args": {
    "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/_project/paper/**/*.tex"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-25T20:53:38.985845+00:00_

artifacts/_project/paper/analysis.tex
artifacts/_project/paper/table_steering_full.tex
artifacts/_project/paper/tab_dataset_stats.tex
artifacts/_project/paper/tab_gar_robustness.tex
artifacts/_project/paper/tab_mmlu_detail.tex
artifacts/_project/paper/tab_qwen15b_results.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-25T20:53:38.986019+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/_project/paper/sections/**/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Glob",
  "tool_args": {
    "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/_project/paper/sections/**/*.tex"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-25T20:53:38.986154+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-25T20:53:38.986278+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/**/*tab*"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Glob",
  "tool_args": {
    "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/**/*tab*"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-25T20:53:38.986440+00:00_

artifacts/_project/paper/table_steering_full.tex
logs/workers/worker_viz_beta_steering_table_20260522T154749.log
logs/workers/worker_viz_beta_steering_table_20260522T154749_result.json
artifacts/table_steering_full.tex
logs/workers/worker_paper_loss_iteration_table_20260522T160702.log
logs/workers/worker_paper_loss_iteration_table_20260522T160702_result.json
artifacts/_project/paper/tab_dataset_stats.tex
artifacts/_project/paper/tab_gar_robustness.tex
artifacts/_project/paper/tab_mmlu_detail.tex
artifacts/_project/paper/tab_qwen15b_results.tex
artifacts/_project/data/tab_statistical_tests.tex
artifacts/appendix_expansion/tab_gar_robustness.tex
artifacts/appendix_expansion/tab_statistical_tests.tex
artifacts/appendix_expansion/tab_perseed_ss.tex
artifacts/appendix_expansion/tab_perseed_tg.tex
artifacts/appendix_expansion/tab_perturn_qwen.tex
artifacts/appendix_expansion/tab_mmlu_detail.tex
artifacts/appendix_expansion/tab_qwen15b_results.tex
artifacts/appendix_expansion/tab_crossmodel_detail.tex
.venv/lib/python3.14/site-packages/pip/_internal/operations/build/metadata_editable.py
.venv/lib/python3.14/site-packages/pip/_internal/operations/build/wheel_editable.py
.venv/lib/python3.14/site-packages/pip/_internal/operations/install/editable_legacy.py
.venv/lib/python3.14/site-packages/pip/_vendor/distlib/database.py
.venv/lib/python3.14/site-packages/pip/_vendor/rich/table.py
.venv/lib/python3.14/site-packages/pip/_internal/operations/build/__pycache__/metadata_editable.cpython-314.pyc
.venv/lib/python3.14/site-packages/pip/_internal/operations/build/__pycache__/wheel_editable.cpython-314.pyc
.venv/lib/python3.14/site-packages/pip/_internal/operations/install/__pycache__/editable_legacy.cpython-314.pyc
.venv/lib/python3.14/site-packages/pip/_vendor/distlib/__pycache__/database.cpython-314.pyc
.venv/lib/python3.14/site-packages/pip/_vendor/rich/__pycache__/table.cpython-314.pyc
.venv/lib/python3.14/site-packages/pygments/lexers/tablegen.py
.venv/lib/python3.14/site-pack
…[truncated 4948 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-25T20:53:38.986606+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "SS|gap|ratio|1\\.2|7\\.[89]",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/_project/paper",
  "type": "tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Grep",
  "tool_args": {
    "pattern": "SS|gap|ratio|1\\.2|7\\.[89]",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/_project/paper",
    "type": "tex"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-25T20:53:38.986725+00:00_

Found 4 files
artifacts/_project/paper/tab_mmlu_detail.tex
artifacts/_project/paper/tab_gar_robustness.tex
artifacts/_project/paper/table_steering_full.tex
artifacts/_project/paper/analysis.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-25T20:53:38.986845+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_crossmodel_detail.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_crossmodel_detail.tex"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-25T20:53:38.986975+00:00_

1	% Cross-model detailed comparison: Qwen2.5-7B-Instruct vs Llama-3.1-8B-Instruct
2	% Conditions shared by both models: Base, ThreadGate, LoRA-only
3	% Qwen TF: N=200 held-out; Qwen AR: d048_final_ar N=50 gen beta=0
4	% Llama TF: N=50 held-out T=4; Llama AR: eval_llama_ar_n20 N=20 T=4
5	% Llama SS: p1_llama_ss_eval (epoch_1 checkpoint, N=50)
6	\begin{table*}[t]
7	\centering
8	\caption{Cross-model comparison of goal-adherence metrics on Qwen2.5-7B-Instruct and Llama-3.1-8B-Instruct.
9	Gap ratio = TF GAR / AR GAR; lower is better (less exposure bias).
10	Qwen AR uses $N{=}50$ gen-mode evaluation; Llama AR uses $N{=}20$, $T{=}4$ (SS: $N{=}50$).
11	Llama AR GAR and gaps are mean-based; median-based TG gap is 27$\times$ (\S\ref{subsec:cross-model}).}
12	\label{tab:crossmodel-detail}
13	\small
14	\begin{tabular}{@{}ll ccccc@{}}
15	\toprule
16	\textbf{Model} & \textbf{Condition} & \textbf{TF GAR}$\uparrow$ & \textbf{AR GAR}$\uparrow$ & \textbf{TF PPL}$\downarrow$ & \textbf{AR PPL}$\downarrow$ & \textbf{Gap}$\downarrow$ \\
17	\midrule
18	\multirow{4}{*}{Qwen-7B}
19	  & Base      & 0.013 & 0.019 & 4.34 & 1.447 & 0.7$\times$ \\
20	  & TG        & 0.504 & 0.064 & 2.78 & 1.432 & 7.9$\times$ \\
21	  & LoRA-only & 0.498 & 0.037 & 2.78 & 1.431 & 13.5$\times$ \\
22	  & \textbf{SS} & 0.498 & \textbf{0.401} & 2.78 & 1.441 & \textbf{1.2$\times$} \\
23	\midrule
24	\multirow{4}{*}{Llama-8B}
25	  & Base      & 0.017 & 0.009 & 3.45 & 1.293 & 1.9$\times$ \\
26	  & TG        & 0.484 & 0.043 & 2.57 & 1.437 & 11.2$\times$ \\
27	  & LoRA-only & 0.481 & 0.028 & 2.60 & 1.419 & 17.2$\times$ \\
28	  & \textbf{SS} & 0.477 & \textbf{0.166} & 2.82 & 1.370 & \textbf{2.9$\times$} \\
29	\bottomrule
30	\end{tabular}
31	\end{table*}
32	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-25T20:53:38.987111+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_perseed_tg.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_perseed_tg.tex"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-25T20:53:38.987237+00:00_

1	% Per-seed detailed results for ThreadGate (TG) — seeds 42, 123
2	% TF eval: N=200 held-out conversations
3	% AR eval: N=5, T=10 model-generated conversations (original eval protocol)
4	\begin{table}[h]
5	\centering
6	\caption{Per-seed results for ThreadGate (TG) on Qwen2.5-7B-Instruct.
7	TF evaluation uses 200 held-out conversations.
8	AR evaluation uses 5 model-generated conversations with 10 turns each.}
9	\label{tab:perseed-tg}
10	\resizebox{\columnwidth}{!}{
11	\begin{tabular}{@{}l cc c@{}}
12	\toprule
13	\textbf{Metric} & \textbf{Seed 42} & \textbf{Seed 123} & \textbf{Mean $\pm$ Std} \\
14	\midrule
15	\multicolumn{4}{@{}l}{\textit{Teacher-Forced (TF)}} \\
16	\quad GAR-ours $\uparrow$   & 0.504 & 0.505 & 0.504 $\pm$ 0.001 \\
17	\quad GAR-Dongre $\uparrow$ & 0.015 & 0.012 & 0.014 $\pm$ 0.002 \\
18	\quad PPL $\downarrow$       & 2.784 & 2.780 & 2.782 $\pm$ 0.003 \\
19	\midrule
20	\multicolumn{4}{@{}l}{\textit{Autoregressive (AR), $\beta = 0$}} \\
21	\quad GAR-ours $\uparrow$   & 0.016 & 0.017 & 0.016 $\pm$ 0.001 \\
22	\quad GAR-Dongre $\uparrow$ & 0.019 & 0.018 & 0.019 $\pm$ 0.001 \\
23	\quad PPL $\downarrow$       & 1.360 & 1.386 & 1.373 $\pm$ 0.018 \\
24	\midrule
25	\multicolumn{4}{@{}l}{\textit{Derived}} \\
26	\quad Gap ratio (TF/AR GAR-ours) $\downarrow$ & 32.1 & 30.6 & 31.4 $\pm$ 1.1 \\
27	\bottomrule
28	\end{tabular}}
29	\end{table}
30	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-25T20:53:38.987378+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_perseed_ss.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_perseed_ss.tex"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-25T20:53:38.987576+00:00_

1	% Per-seed detailed results for Scheduled Sampling (SS) — seeds 42, 123, 456
2	% TF eval: N=200, T=3 (teacher-forced on held-out eval_200 set)
3	% AR eval: N=50 gen-mode, beta=0/3/5 (from d048_final_ar)
4	\begin{table}[h]
5	\centering
6	\caption{Per-seed results for Scheduled Sampling (SS) on Qwen2.5-7B-Instruct.
7	TF evaluation uses 200 held-out conversations; AR evaluation uses 50 model-generated conversations in free-form generation mode ($N_{\text{valid}} \approx 39$).}
8	\label{tab:perseed-ss}
9	\resizebox{\columnwidth}{!}{
10	\begin{tabular}{@{}l ccc c@{}}
11	\toprule
12	\textbf{Metric} & \textbf{Seed 42} & \textbf{Seed 123} & \textbf{Seed 456} & \textbf{Mean $\pm$ Std} \\
13	\midrule
14	\multicolumn{5}{@{}l}{\textit{Teacher-Forced (TF)}} \\
15	\quad GAR-ours $\uparrow$   & 0.502 & 0.554 & 0.496 & 0.517 $\pm$ 0.032 \\
16	\quad GAR-Dongre $\uparrow$ & 0.389 & 0.411 & 0.386 & 0.395 $\pm$ 0.014 \\
17	\quad PPL $\downarrow$       & 2.780 & 2.612 & 2.611 & 2.668 $\pm$ 0.097 \\
18	\midrule
19	\multicolumn{5}{@{}l}{\textit{Autoregressive (AR), $\beta = 0$}} \\
20	\quad GAR-ours $\uparrow$   & 0.347 & 0.423 & 0.433 & 0.401 $\pm$ 0.047 \\
21	\quad PPL $\downarrow$       & 1.442 & 1.441 & 1.439 & 1.441 $\pm$ 0.002 \\
22	\midrule
23	\multicolumn{5}{@{}l}{\textit{Autoregressive (AR), $\beta = 3$}} \\
24	\quad GAR-ours $\uparrow$   & 0.593 & 0.590 & 0.605 & 0.596 $\pm$ 0.008 \\
25	\quad PPL $\downarrow$       & 1.564 & 1.607 & 1.587 & 1.586 $\pm$ 0.022 \\
26	\midrule
27	\multicolumn{5}{@{}l}{\textit{Autoregressive (AR), $\beta = 5$}} \\
28	\quad GAR-ours $\uparrow$   & 0.717 & 0.717 & 0.716 & 0.717 $\pm$ 0.001 \\
29	\quad PPL $\downarrow$       & 1.779 & 1.785 & 1.804 & 1.789 $\pm$ 0.013 \\
30	\bottomrule
31	\end{tabular}}
32	\end{table}
33	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-25T20:53:38.987729+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "(1\\.2|7\\.[89])",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/_project/paper",
  "type": "tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Grep",
  "tool_args": {
    "pattern": "(1\\.2|7\\.[89])",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/_project/paper",
    "type": "tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-25T20:53:38.987847+00:00_

artifacts/_project/paper/analysis.tex:20:2 & $-$0.042 & 67.9 & 14.7$\times$ \\
artifacts/_project/paper/tab_gar_robustness.tex:13:  & TG        & 0.3938 & 0.3254 & 1.21$\times$ \\
artifacts/_project/paper/tab_mmlu_detail.tex:14:Other          & 68.25 & 67.59 & 68.12 & 67.95 & 67.06 & 66.80 \\

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-25T20:53:38.987974+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating -type f -name \"*cost*\" | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating -type f -name \"*cost*\" | head -20"
  }
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-25T20:53:38.988097+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/_project/paper/tab_gar_robustness.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/_project/paper/tab_gar_robustness.tex"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-25T20:53:38.988208+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-25T20:53:38.988324+00:00_

1	% GAR definition robustness: 4 token selection strategies x 3 conditions
2	\begin{table}[t]
3	\centering
4	\small
5	\caption{GAR robustness across token selection strategies. We evaluate four ways to select the token position for gradient attribution: \textbf{Last} (final token of each turn), \textbf{All} (mean over all tokens), \textbf{First} (first token), and \textbf{Goal-only} (goal token as in \citet{dongre2024multi}). Turn-1 and Mid-turn GAR are measured under autoregressive generation on 50 held-out conversations. Gap Ratio = Turn-1 / Mid-turn; lower indicates better gradient preservation across turns.}
6	\label{tab:gar_robustness}
7	\begin{tabular}{@{}ll ccc@{}}
8	\toprule
9	\textbf{Token Selection} & \textbf{Condition} & \textbf{Turn-1 GAR} & \textbf{Mid-turn GAR} & \textbf{Gap Ratio} $\downarrow$ \\
10	\midrule
11	\multirow{3}{*}{Last (ours)}
12	  & Base      & 0.0858 & 0.0152 & 5.64$\times$ \\
13	  & TG        & 0.3938 & 0.3254 & 1.21$\times$ \\
14	  & SS        & 0.5274 & 0.4582 & 1.15$\times$ \\
15	\midrule
16	\multirow{3}{*}{All tokens}
17	  & Base      & 0.1152 & 0.0152 & 7.57$\times$ \\
18	  & TG        & 0.1275 & 0.0253 & 5.04$\times$ \\
19	  & SS        & 0.5043 & 0.3658 & 1.38$\times$ \\
20	\midrule
21	\multirow{3}{*}{First token}
22	  & Base      & 0.2987 & 0.0224 & 13.32$\times$ \\
23	  & TG        & 0.3225 & 0.0392 & 8.24$\times$ \\
24	  & SS        & 0.7549 & 0.4118 & 1.83$\times$ \\
25	\midrule
26	\multirow{3}{*}{Goal-only}
27	  & Base      & 0.0110 & 0.0049 & 2.23$\times$ \\
28	  & TG        & 0.3313 & 0.3103 & 1.07$\times$ \\
29	  & SS        & 0.4528 & 0.4435 & 1.02$\times$ \\
30	\bottomrule
31	\end{tabular}
32	\end{table}
33	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-25T20:53:38.988484+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/_project/paper/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/_project/paper/analysis.tex"
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-25T20:53:38.988638+00:00_

1	\section{Analysis}\label{sec:analysis}
2	
3	The four-way ablation in \S\ref{sec:experiments} established that gating produces no measurable benefit over LoRA-only fine-tuning. This section investigates why. We first characterize the gradient dynamics between the two training objectives (\S\ref{subsec:gradient-conflict}), then show that the learned gates exhibit behavior opposite to the design intent (\S\ref{subsec:gate-conditioning}). A targeted causal experiment rules out gradient direction conflict as the explanation (\S\ref{subsec:pcgrad}), and a distribution shift analysis identifies the actual failure mode (\S\ref{subsec:dist-shift}).
4	
5	\subsection{Gradient Conflict Observation}\label{subsec:gradient-conflict}
6	
7	To understand how the two loss terms interact during training, we measure the cosine similarity between $\nabla_\theta \mathcal{L}_\text{NTP}$ and $\nabla_\theta \mathcal{L}_\text{GAR}$ at each transformer layer across three training epochs. Table~\ref{tab:grad-conflict} summarizes the results.
8	
9	\begin{table}[t]
10	\centering
11	\small
12	\caption{Gradient interaction between $\mathcal{L}_\text{NTP}$ and $\mathcal{L}_\text{GAR}$ across training epochs. \textit{cos\_sim}: mean cosine similarity across layers. \textit{neg\%}: percentage of layers with negative cosine similarity. \textit{mag\_ratio}: ratio of NTP to GAR gradient magnitudes.}
13	\label{tab:grad-conflict}
14	\begin{tabular}{lccc}
15	\toprule
16	\textbf{Epoch} & \textbf{cos\_sim} & \textbf{neg\%} & \textbf{mag\_ratio} \\
17	\midrule
18	0 & $-$0.089 & 78.6 & 7.5$\times$ \\
19	1 & $-$0.054 & 71.4 & 13.7$\times$ \\
20	2 & $-$0.042 & 67.9 & 14.7$\times$ \\
21	\bottomrule
22	\end{tabular}
23	\end{table}
24	
25	Two patterns are apparent. First, the NTP and GAR gradients point in opposing directions across 68--79\% of layers throughout training. The mean cosine similarity is negative at every epoch, though it attenuates slightly from $-$0.089 to $-$0.042 as training progresses. Second, t
…[truncated 7811 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-25T20:53:38.988791+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "cost|Cost|COST|computation|Computation",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/_project/paper",
  "type": "tex",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Grep",
  "tool_args": {
    "pattern": "cost|Cost|COST|computation|Computation",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/_project/paper",
    "type": "tex",
    "output_mode": "files_with_matches"
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-25T20:53:38.988908+00:00_

Found 1 file
artifacts/_project/paper/analysis.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-25T20:53:38.989030+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts -name \"*.tex\" | xargs grep -l \"cost\\|Cost\" | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts -name \"*.tex\" | xargs grep -l \"cost\\|Cost\" | head -20"
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-25T20:53:38.989146+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/median/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/worst/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/best/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260524T081135/median/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260524T081135/worst/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260524T081135/best/paper.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-25T20:53:38.989273+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/_project/paper/sections/ 2>/dev/null || echo \"Directory does not exist\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/_project/paper/sections/ 2>/dev/null || echo \"Directory does not exist\""
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-25T20:53:38.989385+00:00_

Directory does not exist

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-25T20:53:38.989527+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/**/*tab*cost*"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Glob",
  "tool_args": {
    "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/**/*tab*cost*"
  }
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-25T20:53:38.989637+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-25T20:53:38.989755+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts -name \"tab_*.tex\" -type f 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts -name \"tab_*.tex\" -type f 2>/dev/null"
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-25T20:53:38.989904+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/_project/paper/tab_mmlu_detail.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/_project/paper/tab_qwen15b_results.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/_project/paper/tab_dataset_stats.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/_project/paper/tab_gar_robustness.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/_project/data/tab_statistical_tests.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_mmlu_detail.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_crossmodel_detail.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_statistical_tests.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_qwen15b_results.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_perturn_qwen.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_dataset_stats.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_perseed_ss.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_gar_robustness.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_perseed_tg.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_perturn_llama.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-25T20:53:38.990063+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"tab_cost\\|cost\\|Cost\\|computational\\|Computational\" /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/_project/paper/*.tex 2>/dev/null | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"tab_cost\\|cost\\|Cost\\|computational\\|Computational\" /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/_project/paper/*.tex 2>/dev/null | head -20"
  }
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-25T20:53:38.990193+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/_project/paper/ | grep -i \"tab\\|cost\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/_project/paper/ | grep -i \"tab\\|cost\""
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-25T20:53:38.990305+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-25T20:53:38.990436+00:00_

-rw-r--r-- 1 ubuntu ubuntu     932 May 24 15:13 tab_dataset_stats.tex
-rw-r--r-- 1 ubuntu ubuntu    1593 May 24 15:13 tab_gar_robustness.tex
-rw-r--r-- 1 ubuntu ubuntu     962 May 24 15:13 tab_mmlu_detail.tex
-rw-r--r-- 1 ubuntu ubuntu    1450 May 24 15:13 tab_qwen15b_results.tex
-rw-r--r-- 1 ubuntu ubuntu    1398 May 22 15:49 table_steering_full.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-25T20:53:38.990584+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"1\\.2\\|7\\.[89]\\|gap\\|Gap\" /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/_project/paper/*.tex 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"1\\.2\\|7\\.[89]\\|gap\\|Gap\" /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/_project/paper/*.tex 2>/dev/null"
  }
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-25T20:53:38.990711+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/_project/paper/analysis.tex:2 & $-$0.042 & 67.9 & 14.7$\times$ \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/_project/paper/analysis.tex:Recall from \S\ref{sec:experiments} that teacher-forced GAR-ours reaches 0.49 for all fine-tuned variants, while autoregressive GAR-ours drops to 0.016, a 30$\times$ gap. We decompose this gap by comparing same-distribution and cross-distribution evaluation. Under same-distribution evaluation (teacher-forced UltraChat text), GAR-ours is approximately 0.49, confirming that the model has learned the intended attention pattern on the training distribution. Under cross-distribution evaluation (model-generated text), GAR-ours drops to 0.016. The training itself is sound; the failure is one of generalization.
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/_project/paper/analysis.tex:GAR-Dongre provides a revealing control. Across both evaluation conditions, GAR-Dongre remains uniformly low (0.01--0.02) with no distribution gap. The distribution shift selectively destroys the concentrated attention pattern captured by GAR-ours (last-token, summary-position attention) while leaving the diffuse attention pattern captured by GAR-Dongre (averaged across all positions) unaffected. This selectivity implies that the distribution shift disrupts a specific learned routing behavior rather than attention computation in general.
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/_project/paper/tab_gar_robustness.tex:\caption{GAR robustness across token selection strategies. We evaluate four ways to select the token position for gradient attribution: \textbf{Last} (final token of each turn), \textbf{All} (mean over all tokens), \textbf{First} (first token), and \textbf{Goal-only} (goal token as in \citet{dongre2024multi}). Turn-1 and Mid-tu
…[truncated 1057 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-25T20:53:38.990902+00:00_

Perfect! Now let me compile a comprehensive summary with all the exact file paths and relevant content:

## Summary of Findings

I've found all the requested files in the turn_residual_gating project. Here are the exact file paths and relevant content:

### 1. Crossmodel Detail Table (tab_crossmodel_detail)
**File path:** `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_crossmodel_detail.tex`

**Relevant lines:** Lines 1-32 (full table)
- Contains cross-model comparison of goal-adherence metrics on Qwen2.5-7B-Instruct and Llama-3.1-8B-Instruct
- **Key SS gap ratios mentioned:**
  - Line 22: Qwen SS condition shows **1.2$\times$** gap (the lowest gap ratio)
  - Line 20: Qwen TG shows **7.9$\times$** gap
  - Lines 25-28: Llama results including gap ratios

### 2. Per-seed Table for TG (ThreadGate)
**File path:** `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_perseed_tg.tex`

**Relevant lines:** Lines 1-30 (full table)
- Per-seed detailed results for ThreadGate (TG) with seeds 42 and 123
- TF evaluation uses 200 held-out conversations
- AR evaluation uses 5 model-generated conversations with 10 turns each
- Line 26: Shows gap ratio (TF/AR GAR-ours) values: 32.1 and 30.6 with mean 31.4 ± 1.1

### 3. Per-seed Table for SS (Scheduled Sampling)
**File path:** `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_perseed_ss.tex`

**Relevant lines:** Lines 1-32 (full table)
- Per-seed detailed results for Scheduled Sampling (SS) with seeds 42, 123, 456
- TF evaluation: N=200, T=3 on held-out eval_200 set
- AR evaluation: N=50 gen-mode

### 4. Cost Table
**Result:** No dedicated cost/computational cost table (tab_cost) was found in the project. The search found no files matching "*cost*" patterns in the artifacts directory.

### 5. TEX Files with SS Gap Ratio Values
**File path 1:** `/home/
…[truncated 845 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Agent",
  "elapsed_ms": 6
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-25T20:53:38.991050+00:00_

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
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
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

_source line 48 · 2026-05-25T20:53:38.991175+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-25T20:53:38.991303+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_crossmodel_detail.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_crossmodel_detail.tex"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-25T20:53:38.991470+00:00_

1	% Cross-model detailed comparison: Qwen2.5-7B-Instruct vs Llama-3.1-8B-Instruct
2	% Conditions shared by both models: Base, ThreadGate, LoRA-only
3	% Qwen TF: N=200 held-out; Qwen AR: d048_final_ar N=50 gen beta=0
4	% Llama TF: N=50 held-out T=4; Llama AR: eval_llama_ar_n20 N=20 T=4
5	% Llama SS: p1_llama_ss_eval (epoch_1 checkpoint, N=50)
6	\begin{table*}[t]
7	\centering
8	\caption{Cross-model comparison of goal-adherence metrics on Qwen2.5-7B-Instruct and Llama-3.1-8B-Instruct.
9	Gap ratio = TF GAR / AR GAR; lower is better (less exposure bias).
10	Qwen AR uses $N{=}50$ gen-mode evaluation; Llama AR uses $N{=}20$, $T{=}4$ (SS: $N{=}50$).
11	Llama AR GAR and gaps are mean-based; median-based TG gap is 27$\times$ (\S\ref{subsec:cross-model}).}
12	\label{tab:crossmodel-detail}
13	\small
14	\begin{tabular}{@{}ll ccccc@{}}
15	\toprule
16	\textbf{Model} & \textbf{Condition} & \textbf{TF GAR}$\uparrow$ & \textbf{AR GAR}$\uparrow$ & \textbf{TF PPL}$\downarrow$ & \textbf{AR PPL}$\downarrow$ & \textbf{Gap}$\downarrow$ \\
17	\midrule
18	\multirow{4}{*}{Qwen-7B}
19	  & Base      & 0.013 & 0.019 & 4.34 & 1.447 & 0.7$\times$ \\
20	  & TG        & 0.504 & 0.064 & 2.78 & 1.432 & 7.9$\times$ \\
21	  & LoRA-only & 0.498 & 0.037 & 2.78 & 1.431 & 13.5$\times$ \\
22	  & \textbf{SS} & 0.498 & \textbf{0.401} & 2.78 & 1.441 & \textbf{1.2$\times$} \\
23	\midrule
24	\multirow{4}{*}{Llama-8B}
25	  & Base      & 0.017 & 0.009 & 3.45 & 1.293 & 1.9$\times$ \\
26	  & TG        & 0.484 & 0.043 & 2.57 & 1.437 & 11.2$\times$ \\
27	  & LoRA-only & 0.481 & 0.028 & 2.60 & 1.419 & 17.2$\times$ \\
28	  & \textbf{SS} & 0.477 & \textbf{0.166} & 2.82 & 1.370 & \textbf{2.9$\times$} \\
29	\bottomrule
30	\end{tabular}
31	\end{table*}
32	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-25T20:53:38.991615+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_perseed_tg.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_perseed_tg.tex"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-25T20:53:38.991752+00:00_

1	% Per-seed detailed results for ThreadGate (TG) — seeds 42, 123
2	% TF eval: N=200 held-out conversations
3	% AR eval: N=5, T=10 model-generated conversations (original eval protocol)
4	\begin{table}[h]
5	\centering
6	\caption{Per-seed results for ThreadGate (TG) on Qwen2.5-7B-Instruct.
7	TF evaluation uses 200 held-out conversations.
8	AR evaluation uses 5 model-generated conversations with 10 turns each.}
9	\label{tab:perseed-tg}
10	\resizebox{\columnwidth}{!}{
11	\begin{tabular}{@{}l cc c@{}}
12	\toprule
13	\textbf{Metric} & \textbf{Seed 42} & \textbf{Seed 123} & \textbf{Mean $\pm$ Std} \\
14	\midrule
15	\multicolumn{4}{@{}l}{\textit{Teacher-Forced (TF)}} \\
16	\quad GAR-ours $\uparrow$   & 0.504 & 0.505 & 0.504 $\pm$ 0.001 \\
17	\quad GAR-Dongre $\uparrow$ & 0.015 & 0.012 & 0.014 $\pm$ 0.002 \\
18	\quad PPL $\downarrow$       & 2.784 & 2.780 & 2.782 $\pm$ 0.003 \\
19	\midrule
20	\multicolumn{4}{@{}l}{\textit{Autoregressive (AR), $\beta = 0$}} \\
21	\quad GAR-ours $\uparrow$   & 0.016 & 0.017 & 0.016 $\pm$ 0.001 \\
22	\quad GAR-Dongre $\uparrow$ & 0.019 & 0.018 & 0.019 $\pm$ 0.001 \\
23	\quad PPL $\downarrow$       & 1.360 & 1.386 & 1.373 $\pm$ 0.018 \\
24	\midrule
25	\multicolumn{4}{@{}l}{\textit{Derived}} \\
26	\quad Gap ratio (TF/AR GAR-ours) $\downarrow$ & 32.1 & 30.6 & 31.4 $\pm$ 1.1 \\
27	\bottomrule
28	\end{tabular}}
29	\end{table}
30	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-25T20:53:38.991890+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_perseed_ss.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_perseed_ss.tex"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-25T20:53:38.992029+00:00_

1	% Per-seed detailed results for Scheduled Sampling (SS) — seeds 42, 123, 456
2	% TF eval: N=200, T=3 (teacher-forced on held-out eval_200 set)
3	% AR eval: N=50 gen-mode, beta=0/3/5 (from d048_final_ar)
4	\begin{table}[h]
5	\centering
6	\caption{Per-seed results for Scheduled Sampling (SS) on Qwen2.5-7B-Instruct.
7	TF evaluation uses 200 held-out conversations; AR evaluation uses 50 model-generated conversations in free-form generation mode ($N_{\text{valid}} \approx 39$).}
8	\label{tab:perseed-ss}
9	\resizebox{\columnwidth}{!}{
10	\begin{tabular}{@{}l ccc c@{}}
11	\toprule
12	\textbf{Metric} & \textbf{Seed 42} & \textbf{Seed 123} & \textbf{Seed 456} & \textbf{Mean $\pm$ Std} \\
13	\midrule
14	\multicolumn{5}{@{}l}{\textit{Teacher-Forced (TF)}} \\
15	\quad GAR-ours $\uparrow$   & 0.502 & 0.554 & 0.496 & 0.517 $\pm$ 0.032 \\
16	\quad GAR-Dongre $\uparrow$ & 0.389 & 0.411 & 0.386 & 0.395 $\pm$ 0.014 \\
17	\quad PPL $\downarrow$       & 2.780 & 2.612 & 2.611 & 2.668 $\pm$ 0.097 \\
18	\midrule
19	\multicolumn{5}{@{}l}{\textit{Autoregressive (AR), $\beta = 0$}} \\
20	\quad GAR-ours $\uparrow$   & 0.347 & 0.423 & 0.433 & 0.401 $\pm$ 0.047 \\
21	\quad PPL $\downarrow$       & 1.442 & 1.441 & 1.439 & 1.441 $\pm$ 0.002 \\
22	\midrule
23	\multicolumn{5}{@{}l}{\textit{Autoregressive (AR), $\beta = 3$}} \\
24	\quad GAR-ours $\uparrow$   & 0.593 & 0.590 & 0.605 & 0.596 $\pm$ 0.008 \\
25	\quad PPL $\downarrow$       & 1.564 & 1.607 & 1.587 & 1.586 $\pm$ 0.022 \\
26	\midrule
27	\multicolumn{5}{@{}l}{\textit{Autoregressive (AR), $\beta = 5$}} \\
28	\quad GAR-ours $\uparrow$   & 0.717 & 0.717 & 0.716 & 0.717 $\pm$ 0.001 \\
29	\quad PPL $\downarrow$       & 1.779 & 1.785 & 1.804 & 1.789 $\pm$ 0.013 \\
30	\bottomrule
31	\end{tabular}}
32	\end{table}
33	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-25T20:53:38.992168+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "turn_residual_gating",
  "filters": "{'exp_id': 'tg'}",
  "fields": "['*']",
  "limit": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "turn_residual_gating",
    "filters": "{'exp_id': 'tg'}",
    "fields": "['*']",
    "limit": "20"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-25T20:53:38.992294+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.204}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-25T20:53:38.992430+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "1\\.2[×x\\\\times]|7\\.[89][×x\\\\times]|SS.*gap|gap.*SS|1\\.3[×x\\\\times]",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections",
  "output_mode": "content",
  "-n": "True",
  "context": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Grep",
  "tool_args": {
    "pattern": "1\\.2[×x\\\\times]|7\\.[89][×x\\\\times]|SS.*gap|gap.*SS|1\\.3[×x\\\\times]",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections",
    "output_mode": "content",
    "-n": "True",
    "context": "2"
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-25T20:53:38.992599+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex-39-[Omitted long context line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex-40-
paper/sections/analysis.tex:41:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex-42-
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex-36-\end{figure}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex-37-
paper/sections/experiments.tex:38:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex-39-
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex-40-
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex-226-\midrule
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex-227-Mean cos sim & $-$0.042 & +0.005 \\
paper/sections/appendix.tex:228:Neg-layer \% & 67.9\% & 53.1\% \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex-229-NTP/GAR mag ratio & 14.7$\times$ & 25.7$\times$ \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex-230-\bottomrule
--
paper/sections/appendix.tex-489-Figure~\ref{fig:eb-scaling} quantifies two scaling dimensions of the exposure bias phenomenon: cross-variant gap ratios (panel~a) and length-dependent gap compounding (panel~b).
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex-490-
paper/sections/appendix.tex:491:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_ge
…[truncated 3841 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-25T20:53:38.992770+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex",
  "offset": "35",
  "limit": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex",
    "offset": "35",
    "limit": "10"
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-25T20:53:38.992903+00:00_

35	  \label{fig:ss-gap}
36	\end{figure}
37	
38	Scheduled sampling (SS; \citealp{bengio2015scheduled}), which mixes model-generated tokens into training prefixes with linearly increasing probability (Appendix~\ref{sec:appendix-ss}), directly targets the training-inference mismatch. Across three seeds, AR GAR-ours rises to $0.401\pm0.047$, compressing the gap from 7.9$\times$ to ${\sim}$1.2$\times$ (TF GAR $0.498\pm0.004$) with no PPL cost ($1.441\pm0.002$; Figure~\ref{fig:ss-gap}; per-seed details in Appendix~\ref{sec:appendix-perseed}). Steering on SS models nearly eliminates seed variance ($\beta$\,=\,5: $0.717\pm0.001$, std 0.047$\to$0.001; Figure~\ref{fig:ss-multiseed}). SS generalizes across GAR definitions (mid-turn GAR above 0.36 for all token-position variants; Appendix~\ref{sec:appendix-gar-robust}; extended robustness in Appendix~\ref{sec:appendix-gar-ext}) and across architectures: on Llama-3.1-8B, SS compresses the gap from ${\sim}$27$\times$ to 2.9$\times$, weaker than Qwen likely due to fewer training epochs (2 vs.\ 3; \S\ref{subsec:cross-model}). The benefit diminishes in longer dialogues (Appendix~\ref{sec:appendix-n5}), consistent with exposure bias compounding over turns.
39	
40	
41	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-25T20:53:38.993035+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex",
  "offset": "38",
  "limit": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex",
    "offset": "38",
    "limit": "10"
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-25T20:53:38.993164+00:00_

38	
39	We replicate on Llama-3.1-8B-Instruct \citep{grattafiori2024llama3} (Base, ThreadGate, LoRA-only; $N$\,=\,20, 4 turns). TF GAR-ours is 0.484 (TG) / 0.481 (LoRA-only); gating contributes zero benefit. The AR distribution is heavy-tailed (coefficient of variation, CoV\,$>$\,100\%); we report medians: 0.018 (TG and LoRA-only), 0.009 (Base), yielding gaps of 27$\times$ and 26$\times$ (Figure~\ref{fig:crossmodel}a in Appendix~\ref{sec:appendix-llama}; per-turn values in Appendix~\ref{sec:appendix-perturn-detail}). Gate profiles differ qualitatively (Figure~\ref{fig:crossmodel}b): Qwen attenuates early layers (L1\,=\,0.793) while Llama dips at late layers (L25\,=\,0.719), an architecture-dependent pattern, but convergence toward identity is universal (Appendix~\ref{sec:appendix-viz}). The gap is substantial on both architectures, consistent with exposure bias as architecture-independent.
40	
41	Scheduled sampling confirms cross-model generalization: Llama SS compresses the gap from ${\sim}$27$\times$ to 2.9$\times$ (TF GAR 0.477, AR GAR 0.166), weaker than Qwen's ${\sim}$1.2$\times$ likely due to fewer training epochs (2 vs.\ 3). The phase transition is architecture-dependent: $\beta$\,=\,3 triggers recovery on Qwen SS (0.593) but not Llama SS (0.173); Llama requires $\beta$\,=\,5 (GAR 0.791, exceeding Qwen SS 0.717; Appendix~\ref{sec:appendix-llama-ss}). Cross-scale validation on Qwen-2.5-1.5B confirms the same pattern (79.8\% GAR decay, $\beta$-steering recovery to 0.715; Appendix~\ref{sec:appendix-1.5b}).
42	
43	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-25T20:53:38.993288+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex",
  "offset": "488",
  "limit": "25"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex",
    "offset": "488",
    "limit": "25"
  }
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-25T20:53:38.993443+00:00_

488	
489	Figure~\ref{fig:eb-scaling} quantifies two scaling dimensions of the exposure bias phenomenon: cross-variant gap ratios (panel~a) and length-dependent gap compounding (panel~b).
490	
491	\paragraph{Cross-variant gaps.} On Qwen, ThreadGate achieves the smallest gap among standard variants (7.9$\times$) while PCGrad shows the largest (16.7$\times$, consistent with its counterproductive effect on AR GAR). Scheduled sampling reduces the gap to ${\sim}$1.2$\times$, the only variant approaching parity. The ordering of gap ratios (SS $\ll$ TG $<$ LoRA $<$ UG $<$ PCGrad) differs from the ordering of TF GAR (all $\approx$ 0.50), confirming that training-time optimization success does not predict inference-time robustness. On Llama, both ThreadGate and LoRA-only show $\sim$27$\times$ gaps (by median), larger than any Qwen variant. The consistently larger Llama gaps may reflect its deeper architecture (32 vs.\ 28 layers), which provides more layers for distributional drift to compound through.
492	
493	\paragraph{Length-dependent compounding.} Panel~(b) shows that the gap compounds with conversation length: at 3.6 mean turns ($N$\,=\,50), ThreadGate's gap is 8$\times$; at 10 turns ($N$\,=\,5), it widens to 31$\times$. The relationship is approximately linear in the number of turns on a log scale, suggesting that the per-turn drift contribution is roughly multiplicative. Extrapolating this trend suggests that at 20 turns the gap would exceed 100$\times$, making any training-time attention signal essentially undetectable. This length dependence is consistent with cumulative distributional drift---each model-generated turn introduces additional divergence from the teacher-forced training distribution, and by turn~10 the accumulated drift overwhelms any gating signal.
494	
495	\paragraph{Implications for deployment.} These scaling results have practical implications: (1)~for applications requiring sustained attention over many turns (e.g., long-form tutoring, multi-step r
…[truncated 2461 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-25T20:53:38.993596+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex",
  "offset": "505",
  "limit": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex",
    "offset": "505",
    "limit": "10"
  }
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-25T20:53:38.993726+00:00_

505	
506	To characterize how goal attention evolves across conversation turns under autoregressive generation, we compute per-turn AR GAR for all six Qwen-2.5-7B training configurations (Base, LoRA-only, Uniform Gate, PCGrad, Scheduled Sampling, ThreadGate) on the held-out evaluation set. Figure~\ref{fig:kl_ar_gar_curves} plots per-turn AR GAR trajectories across turns 1--5, and Figure~\ref{fig:kl_ar_gar_bar} compares mid-turn AR GAR levels across configurations.
507	
508	All six configurations exhibit monotonic GAR decay as turn index increases, consistent with cumulative exposure bias eroding attention to goal tokens. The decay rate varies substantially: Scheduled Sampling retains by far the highest mid-turn GAR (0.423), followed distantly by ThreadGate (0.064), LoRA-only (0.037), Uniform Gate (0.033), PCGrad (0.030), and Base (0.019). Base decays most rapidly, losing the majority of its initial GAR within the first few turns. The large SS--TG gap mirrors Table~\ref{tab:five-way} and confirms that distributional robustification---not gating architecture alone---is the primary driver of AR GAR retention.\footnote{SS configuration uses seed 123 data; all other configurations use seed 42. Cross-seed trends are consistent (\S\ref{subsec:ss}).}
509	
510	\begin{figure}[t]
511	\centering
512	\includegraphics[width=\columnwidth]{fig_kl_ar_gar_curves.pdf}
513	\caption{Per-turn AR GAR trajectories for six Qwen-2.5-7B configurations (turns 1--5). All models show monotonic decay; Scheduled Sampling retains far higher GAR throughout (0.53$\to$0.39), while the remaining five variants cluster below 0.13 and decay rapidly.}
514	\label{fig:kl_ar_gar_curves}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-25T20:53:38.993855+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex",
  "offset": "628",
  "limit": "15"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex",
    "offset": "628",
    "limit": "15"
  }
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-25T20:53:38.993991+00:00_

628	
629	\section{Per-Seed Detailed Results}\label{sec:appendix-perseed}
630	
631	Tables~\ref{tab:perseed-ss} and~\ref{tab:perseed-tg} report full per-seed breakdowns for the two multi-seed configurations, providing evidence that our main findings are robust to random initialization.
632	
633	\paragraph{Scheduled sampling (3 seeds).} TF GAR-ours averages $0.517\pm0.032$ across seeds under the held-out protocol (Table~\ref{tab:perseed-ss}); under IID evaluation, TF is more stable ($0.499\pm0.003$), with the held-out variance driven by seed~123's higher value on the larger $N$\,=\,200 sample. AR GAR shows meaningful variance (std\,=\,0.047): seed 42 produces the lowest AR GAR (0.347, gap 1.4$\times$), seed 123 is intermediate (0.423, gap 1.3$\times$), and seed 456 is highest (0.433, gap 1.2$\times$). This variance is expected: AR evaluation involves free-form generation where small differences in learned attention patterns can compound across turns. The variance is asymmetric---all seeds remain well above the non-SS baseline (0.064)---so the qualitative conclusion (SS provides order-of-magnitude improvement) holds across seeds. At $\beta$\,=\,5, the cross-seed variance nearly vanishes ($0.717\pm0.001$), confirming that strong steering converges to a seed-independent attention equilibrium that overwhelms initialization differences.
634	
635	\paragraph{ThreadGate (2 seeds).} Two seeds produce nearly identical TF metrics ($0.504\pm0.001$) and similar AR GAR (0.064 vs.\ 0.055), with gap ratios of 7.9$\times$ and 9.1$\times$ respectively. The 15\% relative difference in AR GAR is small compared to the order-of-magnitude TF-AR gap, confirming that the exposure bias phenomenon is not seed-dependent.
636	
637	\paragraph{Training dynamics.} Seed variance in training time is non-trivial for scheduled sampling: seed 123 requires 10.8 hours (80\% overhead) vs.\ 6.5 hours for seeds 42 and 456 (8\% overhead). This variance is driven by the stochastic Bernoulli sampling of model-gen
…[truncated 461 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-25T20:53:38.994137+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex",
  "offset": "810",
  "limit": "15"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex",
    "offset": "810",
    "limit": "15"
  }
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-25T20:53:38.994274+00:00_

810	Table~\ref{tab:llama-vs-qwen-ss} compares scheduled sampling across both architectures. Both models show large gap compression relative to their ThreadGate baselines, but the residual gap on Llama (2.9$\times$) is larger than Qwen's (1.2$\times$). We attribute this to training duration: Llama received only 2 epochs of scheduled sampling exposure versus Qwen's 3 epochs. Llama reduces its median-based gap by 9.3$\times$ (from 27$\times$ to 2.9$\times$) while Qwen reduces by 6.6$\times$ (from 7.9$\times$ to 1.2$\times$), suggesting that a third epoch would likely narrow the residual gap further. Notably, $\beta$-steering is more effective on Llama (0.791 vs.\ 0.717 at $\beta$\,=\,5), partially compensating for the weaker training-time compression.
811	
812	\paragraph{Architectural differences.}
813	Several architectural differences between Qwen-2.5-7B and Llama-3.1-8B may contribute to the cross-model gap variation. Llama uses Grouped Query Attention (GQA) with 8 KV heads (vs.\ Qwen's full 28-head multi-head attention, MHA), which reduces the number of independently steerable attention heads by 3.5$\times$. Llama also uses Rotary Position Embedding (RoPE) with a longer default context (128K tokens vs.\ Qwen's 32K), which may affect how positional information interacts with goal-token attention at different conversation depths. Despite these differences, the qualitative pattern is identical: TF convergence, AR collapse, and SS-mediated recovery, confirming that exposure bias on auxiliary attention losses is architecture-general rather than an artifact of a specific attention implementation.
814	
815	\paragraph{Training dynamics.}
816	The Llama SS training loss trajectory closely mirrors Qwen's during the first two epochs: NTP loss converges within epoch~1 (final NTP loss 0.62 for Llama vs.\ 0.58 for Qwen), while GAR loss continues to decrease throughout epoch~2. The scheduled sampling ratio reaches ${\sim}$0.20 at the end of epoch~2 (vs.\ 0.30 at end of epoch~3 for 
…[truncated 529 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 71 · 2026-05-25T20:53:38.994432+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "5\\.72|6\\.11|LoRA.*h|UG.*h|tab.cost|cost.*table|training.*time|train.*hour",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex",
  "output_mode": "content",
  "-n": "True",
  "context": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Grep",
  "tool_args": {
    "pattern": "5\\.72|6\\.11|LoRA.*h|UG.*h|tab.cost|cost.*table|training.*time|train.*hour",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex",
    "output_mode": "content",
    "-n": "True",
    "context": "3"
  }
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-25T20:53:38.994704+00:00_

1-\section{Training Configuration}\label{sec:appendix-hyper}
2-
3:[Omitted long matching line]
4-
5-\begin{table}[t]
6-\centering\small
--
11-\textbf{Parameter} & \textbf{Value} \\
12-\midrule
13-Base model & Qwen-2.5-7B-Instruct \\
14:LoRA rank / $\alpha$ & 16 / 32 \\
15-LoRA targets & \texttt{q\_proj}, \texttt{v\_proj} \\
16-Optimizer & AdamW ($\beta_1$\!=\!0.9, $\beta_2$\!=\!0.999) \\
17-Learning rate & $2 \times 10^{-4}$ \\
--
106-
107-The main results (Table~\ref{tab:five-way}) report AR GAR from $N$\,=\,50 held-out conversations with a mean of 3.6 user turns. Table~\ref{tab:n5-ar} presents complementary results on $N$\,=\,5 conversations with 10 turns each, testing whether the observed patterns generalize beyond the training distribution's conversation length.
108-
109:[Omitted long matching line]
110-
111:[Omitted long matching line]
112-
113-\paragraph{Caveats.} The $N$\,=\,5 sample size limits statistical power, and the 10-turn conversations may differ systematically from the 3--5 turn training distribution in ways beyond length (e.g., topic complexity, user engagement patterns). We present these results as directional evidence rather than definitive conclusions.
114-
--
134-
135-All statistical tests reported in the main text use non-parametric methods due to the non-normal, heavy-tailed distribution of per-conversation GAR values. Table~\ref{tab:stat-tests} consolidates the full results.
136-
137:[Omitted long matching line]
138-
139-\paragraph{Bootstrap confidence intervals.} The 95\% CIs in Table~\ref{tab:five-way} are computed via 10,000 bootstrap resamples of per-conversation mid-turn GAR averages (turns 2--$T$), using the percentile method.
140-
--
168-
169-\section{Llama-3.1-8B Complete Results}\label{sec:appendix-llama}
170-
171:Table~\ref{tab:llama-full} presents the complete Llama-3.1-8B-Instruct results, complementing the summary in \S\ref{subsec:cross-model}. Three configurations were trained (Base, ThreadGate, LoRA-only) using the same trainin
…[truncated 12351 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 73 · 2026-05-25T20:53:38.994906+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex",
  "offset": "386",
  "limit": "25"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex",
    "offset": "386",
    "limit": "25"
  }
}
```

</details>

---

### Tool result

_source line 74 · 2026-05-25T20:53:38.995065+00:00_

386	
387	\begin{table}[t]
388	\centering\small
389	\caption{Computational cost across training configurations. All experiments use a single NVIDIA RTX PRO 6000 (96\,GB VRAM). VRAM reports peak allocated memory (excluding optimizer states).}
390	\label{tab:cost}
391	\resizebox{\columnwidth}{!}{%
392	\begin{tabular}{lcccc}
393	\toprule
394	\textbf{Config} & \textbf{Params} & \textbf{Time (h)} & \textbf{VRAM} & \textbf{Overhead} \\
395	\midrule
396	\multicolumn{5}{l}{\emph{Qwen-2.5-7B-Instruct}} \\
397	LoRA-only & 4.2M & 5.7 & 42\,GB & baseline \\
398	ThreadGate & 4.3M & 6.0 & 43\,GB & $+$57K \\
399	\;+\,PCGrad & 4.3M & 8.0 & 43\,GB & $+$33\% \\
400	Uniform Gate & 4.3M & 6.0 & 43\,GB & $+$57K \\
401	SS (s42) & 4.3M & 6.5 & 43\,GB & $+$8\% \\
402	SS (s123) & 4.3M & 10.8 & 43\,GB & $+$80\% \\
403	SS (s456) & 4.3M & 6.5 & 43\,GB & $+$8\% \\
404	\midrule
405	\multicolumn{5}{l}{\emph{Llama-3.1-8B-Instruct}} \\
406	LoRA-only & 4.2M & 7.0 & 45\,GB & baseline \\
407	ThreadGate & 4.3M & 7.3 & 46\,GB & $+$65K \\
408	\bottomrule
409	\end{tabular}}
410	\end{table}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 75 · 2026-05-25T20:53:38.995205+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "1\\.2.{0,3}\\\\times|gap.*1\\.2|1\\.2.*gap",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Grep",
  "tool_args": {
    "pattern": "1\\.2.{0,3}\\\\times|gap.*1\\.2|1\\.2.*gap",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 76 · 2026-05-25T20:53:38.995348+00:00_

paper/sections/analysis.tex:28:We test specificity with Turn-level Residual Coherence (TRC), the cosine similarity between adjacent-turn hidden states. TF/AR TRC is 0.334/0.332 for ThreadGate (gap $+$0.002) and 0.349/0.411 for LoRA-only (gap $-$0.062, reversed); exposure bias thus disrupts a specific routing behavior while leaving representations intact. Cross-model evaluation confirms: GAR-Dongre shows negligible shift on both Llama (1.002$\times$) and Qwen (1.28$\times$) vs.\ the order-of-magnitude GAR-ours collapse.
paper/sections/analysis.tex:41:[Omitted long matching line]
paper/sections/experiments.tex:34:  \caption{Scheduled sampling compresses the TF-AR gap from 7.9$\times$ to ${\sim}$1.2$\times$, the only variant approaching parity across five training conditions.}
paper/sections/experiments.tex:38:[Omitted long matching line]
paper/sections/conclusion.tex:3:[Omitted long matching line]
paper/sections/appendix.tex:207:[Omitted long matching line]
paper/sections/appendix.tex:211:\paragraph{GAR-Dongre cross-model comparison.} GAR-Dongre shows negligible distribution shift on Llama (AR/TF ratio 1.002$\times$), compared to 1.28$\times$ on Qwen. This confirms the mechanism specificity finding: exposure bias selectively disrupts the concentrated last-token attention pattern (GAR-ours) while leaving the diffuse all-token attention (GAR-Dongre) unaffected across both architectures.
paper/sections/appendix.tex:491:[Omitted long matching line]
paper/sections/appendix.tex:495:[Omitted long matching line]
paper/sections/appendix.tex:500:\caption{Exposure bias scaling analysis. (a)~TF/AR gap ratio across training variants; scheduled sampling (SS, ${\sim}$1.2$\times$) is the only variant near parity. Llama gaps ($\sim$27$\times$) exceed all Qwen variants. (b)~Gap compounds with conversation length: ThreadGate's gap widens from 8$\times$ (3.6 turns) to 31$\times$ (10 turns).}
paper/sections/appendix.tex:633:[Omitted long matching line]
paper/sections/appendix.tex:689:[Omi
…[truncated 988 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 77 · 2026-05-25T20:53:38.995596+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "1\\.2.{0,3}\\\\times|gap.*1\\.2|1\\.2.*gap",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/abstract.tex",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Grep",
  "tool_args": {
    "pattern": "1\\.2.{0,3}\\\\times|gap.*1\\.2|1\\.2.*gap",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/abstract.tex",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 78 · 2026-05-25T20:53:38.995738+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 79 · 2026-05-25T20:53:38.995860+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "1\\.2.{0,3}\\\\times|gap.*1\\.2|1\\.2.*gap",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/conclusion.tex",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Grep",
  "tool_args": {
    "pattern": "1\\.2.{0,3}\\\\times|gap.*1\\.2|1\\.2.*gap",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/conclusion.tex",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 80 · 2026-05-25T20:53:38.995978+00:00_

3:[Omitted long matching line]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 81 · 2026-05-25T20:53:38.996090+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/conclusion.tex",
  "offset": "1",
  "limit": "15"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/conclusion.tex",
    "offset": "1",
    "limit": "15"
  }
}
```

</details>

---

### Tool result

_source line 82 · 2026-05-25T20:53:38.996221+00:00_

1	\section{Conclusion}\label{sec:conclusion}
2	
3	\looseness=-1 Auxiliary attention losses converge under teacher forcing (GAR\,=\,0.50) but collapse by an order of magnitude under autoregressive generation on two architectures. A five-way diagnostic comparison identifies exposure bias as a primary contributing factor; $\beta$-steering recovers GAR above the TF baseline, consistent with attention misallocation as a proximal cause (KV cache drift remains untested). Scheduled sampling compresses the gap to ${\sim}$1.2$\times$ (Qwen) and ${\sim}$2.9$\times$ (Llama), generalizing across architectures and seeds; to our knowledge, the first such transfer to auxiliary attention objectives in multi-turn transformers.
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 83 · 2026-05-25T20:53:38.996345+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/introduction.tex",
  "offset": "10",
  "limit": "15"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/introduction.tex",
    "offset": "10",
    "limit": "15"
  }
}
```

</details>

---

### Tool result

_source line 84 · 2026-05-25T20:53:38.996516+00:00_

10	  \centering
11	  \includegraphics[width=\textwidth]{fig1_headline.pdf}
12	  \caption{Exposure bias collapses auxiliary attention losses. \textbf{(a)}~Goal attention decays 85--90\% across turns under AR generation on both Qwen-2.5-7B and Llama-3.1-8B. \textbf{(b)}~Under TF evaluation all variants reach GAR$\approx$0.50, but AR generation collapses GAR by 8--17$\times$ (log scale). \textbf{(c)}~Scheduled sampling compresses the TF--AR gap from 7.9$\times$ to 1.2$\times$ (Qwen) and ${\sim}$27$\times$ to 2.9$\times$ (Llama).}
13	  \label{fig:headline}
14	\end{figure*}
15	
16	Our contributions are:
17	\begin{enumerate}\raggedright
18	    \item \textbf{Exposure bias characterization.} To our knowledge, the first empirical demonstration that exposure bias collapses auxiliary attention objectives in multi-turn transformers, with an order-of-magnitude TF--AR gap reproduced across two architectures (Qwen-2.5-7B, Llama-3.1-8B) and model scales (1.5B--8B).
19	    \item \textbf{Causal exclusion testbed.} A five-way diagnostic design, informed by seven loss-formulation iterations, that isolates the failure mechanism via causal exclusion, including a PCGrad \emph{modus tollens} argument ruling out gradient direction conflict ($p$\,=\,0.002, effect reverses).
20	    \item \textbf{Attention misallocation diagnosis.} Inference-time $\beta$-steering recovers goal attention with modest perplexity cost, evidence that the collapse is an attention routing failure, not a representational one.
21	    \item \textbf{Scheduled sampling as remedy.} The first application of scheduled sampling to auxiliary attention objectives in multi-turn transformers, compressing the TF--AR gap to ${\sim}$1.2$\times$ on Qwen and ${\sim}$2.9$\times$ on Llama with no perplexity degradation, robust across three seeds.
22	\end{enumerate}
23	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 85 · 2026-05-25T20:53:38.996659+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex",
  "offset": "32",
  "limit": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex",
    "offset": "32",
    "limit": "10"
  }
}
```

</details>

---

### Tool result

_source line 86 · 2026-05-25T20:53:38.996790+00:00_

32	  \centering
33	  \includegraphics[width=\columnwidth]{fig_ss_gap_compression.pdf}
34	  \caption{Scheduled sampling compresses the TF-AR gap from 7.9$\times$ to ${\sim}$1.2$\times$, the only variant approaching parity across five training conditions.}
35	  \label{fig:ss-gap}
36	\end{figure}
37	
38	Scheduled sampling (SS; \citealp{bengio2015scheduled}), which mixes model-generated tokens into training prefixes with linearly increasing probability (Appendix~\ref{sec:appendix-ss}), directly targets the training-inference mismatch. Across three seeds, AR GAR-ours rises to $0.401\pm0.047$, compressing the gap from 7.9$\times$ to ${\sim}$1.2$\times$ (TF GAR $0.498\pm0.004$) with no PPL cost ($1.441\pm0.002$; Figure~\ref{fig:ss-gap}; per-seed details in Appendix~\ref{sec:appendix-perseed}). Steering on SS models nearly eliminates seed variance ($\beta$\,=\,5: $0.717\pm0.001$, std 0.047$\to$0.001; Figure~\ref{fig:ss-multiseed}). SS generalizes across GAR definitions (mid-turn GAR above 0.36 for all token-position variants; Appendix~\ref{sec:appendix-gar-robust}; extended robustness in Appendix~\ref{sec:appendix-gar-ext}) and across architectures: on Llama-3.1-8B, SS compresses the gap from ${\sim}$27$\times$ to 2.9$\times$, weaker than Qwen likely due to fewer training epochs (2 vs.\ 3; \S\ref{subsec:cross-model}). The benefit diminishes in longer dialogues (Appendix~\ref{sec:appendix-n5}), consistent with exposure bias compounding over turns.
39	
40	
41	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 87 · 2026-05-25T20:53:38.996924+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex",
  "offset": "205",
  "limit": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex",
    "offset": "205",
    "limit": "10"
  }
}
```

</details>

---

### Tool result

_source line 88 · 2026-05-25T20:53:38.997054+00:00_

205	\end{figure}
206	
207	\paragraph{Cross-model summary.} Table~\ref{tab:crossmodel-detail} consolidates the cross-model comparison, showing TF GAR, AR GAR, PPL, and gap ratios side by side for both architectures. The consistent pattern---TF GAR $\approx$ 0.5, AR GAR $\ll$ 0.1, gap $\geq$ 7.9$\times$---across two architectures with different layer counts, attention head configurations, and pre-training corpora provides strong evidence that exposure bias is architecture-independent. Notably, Llama's larger gaps (27$\times$ by median for TG; mean-based range 11.2--17.2$\times$) compared to Qwen's (7.9--13.5$\times$) may reflect its deeper architecture (32 vs.\ 28 layers), which allows more layers for distributional drift to compound through.
208	
209	\input{../artifacts/appendix_expansion/tab_crossmodel_detail.tex}
210	
211	\paragraph{GAR-Dongre cross-model comparison.} GAR-Dongre shows negligible distribution shift on Llama (AR/TF ratio 1.002$\times$), compared to 1.28$\times$ on Qwen. This confirms the mechanism specificity finding: exposure bias selectively disrupts the concentrated last-token attention pattern (GAR-ours) while leaving the diffuse all-token attention (GAR-Dongre) unaffected across both architectures.
212	
213	\paragraph{Training details.} Llama variants used the same pipeline as Qwen: 8K UltraChat conversations, LoRA rank 16 targeting $q$/$v$ projections, 3 epochs. Training loss converged to 0.929 (LoRA-only) and 0.934 (ThreadGate); the slight difference is attributable to the additional GAR loss component. Wall-clock time was 7.0h (LoRA-only) and 7.3h (ThreadGate), approximately 17\% longer than Qwen due to Llama's larger layer count (32 vs.\ 28 layers).
214	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 89 · 2026-05-25T20:53:38.997182+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex",
  "offset": "686",
  "limit": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex",
    "offset": "686",
    "limit": "10"
  }
}
```

</details>

---

### Tool result

_source line 90 · 2026-05-25T20:53:38.997313+00:00_

686	
687	Table~\ref{tab:gar_robustness} and Figure~\ref{fig:gar-robust-grouped} extend the GAR robustness analysis from \S\ref{sec:appendix-gar-robust} with turn-1 GAR and gap ratio metrics across all four token-position variants. We evaluate four ways to select the query token position for gradient attribution: (1)~\textit{Last} (our default): the final token of each assistant turn, which captures the model's ``summary'' attention pattern at the prediction boundary; (2)~\textit{All}: the mean over all assistant tokens, providing a position-averaged view; (3)~\textit{First}: the first assistant token, which reflects initial attention allocation; (4)~\textit{Goal-only}: attention to goal tokens as defined by \citet{dongre2026attention}, which restricts the target set to system-prompt tokens.
688	
689	\paragraph{Position-specific vs.\ broad improvement.} The key finding is a clear dichotomy between ThreadGate and Scheduled Sampling. ThreadGate improvements are restricted to last-token and goal-only positions (the two definitions sharing the query position targeted by the GAR loss): gap ratios drop to 1.21$\times$ and 1.07$\times$ respectively. All-token (5.04$\times$) and first-token (8.24$\times$) GAR remain near base levels, confirming that the learned routing is position-specific. Scheduled Sampling raises all four definitions above 0.36 with gap ratios $\leq$1.83$\times$, demonstrating that distributional robustification builds broad goal attention across token positions rather than overfitting to the position targeted by the loss.
690	
691	\paragraph{Turn-1 vs.\ mid-turn dynamics.} Turn-1 GAR is consistently higher than mid-turn GAR across all definitions and conditions, reflecting the first turn's proximity to the ground-truth prefix in training. The gap ratio quantifies how much of this initial attention survives into later turns. First-token GAR shows the largest gap ratios (Base: 13.3$\times$, TG: 8.2$\times$), indicating that the first-token position is most
…[truncated 290 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 91 · 2026-05-25T20:53:38.997475+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex",
  "offset": "825",
  "limit": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex",
    "offset": "825",
    "limit": "10"
  }
}
```

</details>

---

### Tool result

_source line 92 · 2026-05-25T20:53:38.997603+00:00_

825	\midrule
826	SS epochs & 3 & 2 \\
827	TF GAR & 0.498 & 0.477 \\
828	AR GAR ($\beta$\,=\,0) & 0.401 & 0.166 \\
829	TF/AR gap & 1.2$\times$ & 2.9$\times$ \\
830	Baseline TG gap & 7.9$\times$ & 27$\times$ (median) \\
831	Gap compression & 6.6$\times$ & 9.3$\times$ \\
832	AR GAR ($\beta$\,=\,5) & 0.717 & 0.791 \\
833	TF PPL & 2.78 & 2.82 \\
834	AR PPL & 1.441 & 1.370 \\

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 93 · 2026-05-25T20:53:38.997750+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "turn_residual_gating",
  "limit": "0",
  "fields": "['exp_id', 'status', 'conclusion']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "turn_residual_gating",
    "limit": "0",
    "fields": "['exp_id', 'status', 'conclusion']"
  }
}
```

</details>

---

### Tool result

_source line 94 · 2026-05-25T20:53:38.997958+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"phase1a_multiseed_qwen\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"p1_ss_lora_only\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"phase2_switching\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"phase2_tf_ar_switching\": {\"status\": \"QUEUED\"}, \"phase1a_multiseed_8runs\": {\"status\": \"PREPARING\"}, \"phase1b_llama_complement\": {\"status\": \"PREPARING\"}, \"p1_llama_ss_eval\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"p1_llama_ss_training\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"mmlu_eval_all\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"p2_llama_gradient_conflict\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"p1_tf_ar_kl_divergence\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"qwen15b_phase1_diag\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"d048_eval_ss_s456\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"d048_ss_s456\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"p0_ss_steering_eval\": {\"status\": \"PREPARING\", \"conclusion\": \"killed\"}, \"d048_eval_ss_s123\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"d048_ss_s123\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"d048_split_softmax_eval\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"d048_final_ar_eval\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"d048_queue_runner\": {\"status\": \"PREPARING\", \"conclusion\": \"failed\"}, \"d048_eval_ss_s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"d048_ss_s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"d048_ss_s42_resume\": {\"status\": \"PREPARING\"}, \"eval_llama_ar_n20\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_llama_lora_only_s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"llama_lora_only_s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"phase2_tg_s42_v6\": {
…[truncated 2747 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 95 · 2026-05-25T20:53:38.998132+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "turn_residual_gating",
  "filters": "{'exp_id': 'd048_final_ar_eval'}",
  "fields": "['*']",
  "limit": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "turn_residual_gating",
    "filters": "{'exp_id': 'd048_final_ar_eval'}",
    "fields": "['*']",
    "limit": "1"
  }
}
```

</details>

---

### Tool call

_source line 96 · 2026-05-25T20:53:38.998264+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "turn_residual_gating",
  "filters": "{'exp_id': 'eval_v7_tg_s123'}",
  "fields": "['*']",
  "limit": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "turn_residual_gating",
    "filters": "{'exp_id': 'eval_v7_tg_s123'}",
    "fields": "['*']",
    "limit": "1"
  }
}
```

</details>

---

### Tool result

_source line 97 · 2026-05-25T20:53:38.998389+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1612}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 98 · 2026-05-25T20:53:38.998529+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1607}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 99 · 2026-05-25T20:53:38.998659+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "turn_residual_gating",
  "filters": "{'status': 'DONE'}",
  "fields": "['exp_id', 'metrics', 'conclusion']",
  "limit": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "turn_residual_gating",
    "filters": "{'status': 'DONE'}",
    "fields": "['exp_id', 'metrics', 'conclusion']",
    "limit": "5"
  }
}
```

</details>

---

### Tool result

_source line 100 · 2026-05-25T20:53:38.998796+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"phase1a_multiseed_qwen\": {\"conclusion\": \"killed\"}, \"p1_ss_lora_only\": {\"conclusion\": \"killed\"}, \"phase2_switching\": {\"conclusion\": \"killed\"}, \"p1_llama_ss_eval\": {\"conclusion\": \"success\", \"metrics\": {\"ss_tf_gar\": 0.477, \"ss_tf_ppl\": 2.82, \"ss_ar_b0_gar\": 0.1662, \"ss_ar_b0_ppl\": 1.37, \"ss_ar_b5_gar\": 0.7905, \"ss_ar_b5_ppl\": 1.81, \"base_ar_gar\": 0.0179, \"base_ar_ppl\": 1.22, \"tf_ar_gap\": 2.87}}, \"p1_llama_ss_training\": {\"conclusion\": \"success\"}}, \"count\": 5, \"total\": 53, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1662}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 101 · 2026-05-25T20:53:38.998941+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "d048_final_ar|eval_v7_tg_s123|tg.*s123.*ar|tg.*n50",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/dream_registry.yaml",
  "output_mode": "content",
  "-n": "True",
  "context": "5",
  "head_limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Grep",
  "tool_args": {
    "pattern": "d048_final_ar|eval_v7_tg_s123|tg.*s123.*ar|tg.*n50",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/dream_registry.yaml",
    "output_mode": "content",
    "-n": "True",
    "context": "5",
    "head_limit": "80"
  }
}
```

</details>

---

### Tool result

_source line 102 · 2026-05-25T20:53:38.999062+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 103 · 2026-05-25T20:53:38.999174+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/dream_registry*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/dream_registry*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating"
  }
}
```

</details>

---

### Tool result

_source line 104 · 2026-05-25T20:53:38.999289+00:00_

dream_registry.lock
dream_registry.yaml.bak
dream_registry.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 105 · 2026-05-25T20:53:38.999485+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "d048_final_ar|eval_v7_tg_s123",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/dream_registry.yaml",
  "output_mode": "content",
  "-n": "True",
  "context": "20",
  "head_limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Grep",
  "tool_args": {
    "pattern": "d048_final_ar|eval_v7_tg_s123",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/dream_registry.yaml",
    "output_mode": "content",
    "-n": "True",
    "context": "20",
    "head_limit": "100"
  }
}
```

</details>

---

### Tool result

_source line 106 · 2026-05-25T20:53:38.999622+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 107 · 2026-05-25T20:53:38.999738+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "head -50 /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/dream_registry.yaml",
  "description": "Check registry file structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Bash",
  "tool_args": {
    "command": "head -50 /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/dream_registry.yaml",
    "description": "Check registry file structure"
  }
}
```

</details>

---

### Tool result

_source line 108 · 2026-05-25T20:53:38.999881+00:00_

dreams:
  dream_20260519T143220:
    card_message_id: om_x100b6ff3099c98b0b2f684134f7af4e
    chat_id: oc_640e53b6afbbd5e34eb7273cd5a707a0
    context_hash: b2394bf844a8292b084341ce00a4696d3109f9097c3655ddedb907f36b4b7856
    dream_id: dream_20260519T143220
    error: 'killed by director: outdated focus (pre-framing-fix), slot needed for
      re-dream'
    focus: 'Route B negative result paper: core novelty is teacher-forcing distribution
      shift destroying auxiliary attention loss generalization (30x GAR gap), NOT
      just "gating failed". Key risks: single-model weakness (W1, mitigated by Llama-3
      plan), "didn''t try hard enough" (W2), GAR as sole proxy metric (W3). Gradient
      conflict data now available (cos_sim -0.089→-0.042, mag_ratio 7.5→14.7x). Eval
      data overlaps training set — held-out eval planned but not yet done.'
    pid: null
    project: turn_residual_gating
    review_mode: full
    review_visible: true
    stages_completed:
    - imagine
    started_at: '2026-05-19T14:32:20+00:00'
    status: failed
    updated_at: '2026-05-19T14:45:10+00:00'
    venue: ''
    what_if: []
    writing_visible: true
  dream_20260519T145320:
    card_message_id: om_x100b6ff3d8f81d04b295df32981809c
    chat_id: oc_640e53b6afbbd5e34eb7273cd5a707a0
    context_hash: 630be4b057d5da6bd00addfe5079a518cb2a5802ad67652f889409fc0bb7aca6
    dream_id: dream_20260519T145320
    error: null
    focus: 'Route B negative result paper post-framing-fix. Core novelty: first quantitative
      measurement of exposure bias impact on auxiliary attention losses (30x GAR gap
      training vs inference). Claims narrowed to lightweight residual gating + GAR
      auxiliary loss scope (not all attention steering). Held-out eval DONE: three-way
      convergence confirmed (TG≈UG≈LoRA-only, GAR diff &lt;0.6pp, PPL identical).
      Bootstrap CI: all 95% CIs include 0, statistically confirms zero benefit. Gradient
      conflict quantified (cos_sim negative, mag_ratio 7.5→14.
…[truncated 396 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 109 · 2026-05-25T20:53:39.000210+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_crossmodel_detail.tex",
  "old_string": "  & \\textbf{SS} & 0.498 & \\textbf{0.401} & 2.78 & 1.441 & \\textbf{1.2$\\times$} \\\\",
  "new_string": "  & \\textbf{SS} & 0.502 & \\textbf{0.347} & 2.78 & 1.441 & \\textbf{1.4$\\times$} \\\\"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_crossmodel_detail.tex",
    "old_string": "  & \\textbf{SS} & 0.498 & \\textbf{0.401} & 2.78 & 1.441 & \\textbf{1.2$\\times$} \\\\",
    "new_string": "  & \\textbf{SS} & 0.502 & \\textbf{0.347} & 2.78 & 1.441 & \\textbf{1.4$\\times$} \\\\"
  }
}
```

</details>

---

### Tool result

_source line 110 · 2026-05-25T20:53:39.000375+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_crossmodel_detail.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 111 · 2026-05-25T20:53:39.000532+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_crossmodel_detail.tex",
  "old_string": "\\caption{Cross-model comparison of goal-adherence metrics on Qwen2.5-7B-Instruct and Llama-3.1-8B-Instruct.\nGap ratio = TF GAR / AR GAR; lower is better (less exposure bias).\nQwen AR uses $N{=}50$ gen-mode evaluation; Llama AR uses $N{=}20$, $T{=}4$ (SS: $N{=}50$).\nLlama AR GAR and gaps are mean-based; median-based TG gap is 27$\\times$ (\\S\\ref{subsec:cross-model}).}",
  "new_string": "\\caption{Cross-model comparison of goal-adherence metrics on Qwen2.5-7B-Instruct and Llama-3.1-8B-Instruct.\nGap ratio = TF GAR / AR GAR; lower is better (less exposure bias).\nAll Qwen rows use seed 42; SS per-seed mean analysis in Table~\\ref{tab:perseed-ss}.\nQwen AR uses $N{=}50$ gen-mode evaluation; Llama AR uses $N{=}20$, $T{=}4$ (SS: $N{=}50$).\nLlama AR GAR and gaps are mean-based; median-based TG gap is 27$\\times$ (\\S\\ref{subsec:cross-model}).}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_crossmodel_detail.tex",
    "old_string": "\\caption{Cross-model comparison of goal-adherence metrics on Qwen2.5-7B-Instruct and Llama-3.1-8B-Instruct.\nGap ratio = TF GAR / AR GAR; lower is better (less exposure bias).\nQwen AR uses $N{=}50$ gen-mode evaluation; Llama AR uses $N{=}20$, $T{=}4$ (SS: $N{=}50$).\nLlama AR GAR and gaps are mean-based; median-based TG gap is 27$\\times$ (\\S\\ref{subsec:cross-model}).}",
    "new_string": "\\caption{Cross-model comparison of goal-adherence metrics on Qwen2.5-7B-Instruct and Llama-3.1-8B-Instruct.\nGap ratio = TF GAR / AR GAR; lower is better (less exposure bias).\nAll Qwen rows use seed 42; SS per-seed mean analysis in Table~\\ref{tab:perseed-ss}.\nQwen AR uses $N{=}50$ gen-mode evaluation; Llama AR uses $N{=}20$, $T{=}4$ (SS: $N{=}50$).\nLlama AR GAR and gaps are mean-based; median-based TG gap is 27$\\times$ (\\S\\ref{subsec:cross-model}).}"
  }
}
```

</details>

---

### Tool result

_source line 112 · 2026-05-25T20:53:39.000680+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_crossmodel_detail.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 113 · 2026-05-25T20:53:39.000804+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_perseed_tg.tex",
  "old_string": "\\caption{Per-seed results for ThreadGate (TG) on Qwen2.5-7B-Instruct.\nTF evaluation uses 200 held-out conversations.\nAR evaluation uses 5 model-generated conversations with 10 turns each.}",
  "new_string": "\\caption{Per-seed results for ThreadGate (TG) on Qwen2.5-7B-Instruct.\nTF evaluation uses 200 held-out conversations.\nAR evaluation uses extended-generation protocol ($N{=}5$, $T{=}10$ turns); under the gen-mode protocol ($N{=}50$) used in Table~\\ref{tab:five-way}, AR GAR is 0.064 (s42) and 0.055 (s123) with gap ratios 7.9$\\times$ and 9.1$\\times$ respectively.}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_perseed_tg.tex",
    "old_string": "\\caption{Per-seed results for ThreadGate (TG) on Qwen2.5-7B-Instruct.\nTF evaluation uses 200 held-out conversations.\nAR evaluation uses 5 model-generated conversations with 10 turns each.}",
    "new_string": "\\caption{Per-seed results for ThreadGate (TG) on Qwen2.5-7B-Instruct.\nTF evaluation uses 200 held-out conversations.\nAR evaluation uses extended-generation protocol ($N{=}5$, $T{=}10$ turns); under the gen-mode protocol ($N{=}50$) used in Table~\\ref{tab:five-way}, AR GAR is 0.064 (s42) and 0.055 (s123) with gap ratios 7.9$\\times$ and 9.1$\\times$ respectively.}"
  }
}
```

</details>

---

### Tool result

_source line 114 · 2026-05-25T20:53:39.000956+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_perseed_tg.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 115 · 2026-05-25T20:53:39.001082+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex",
  "old_string": "Uniform Gate & 4.3M & 6.0 & 43\\,GB & $+$57K \\\\",
  "new_string": "Uniform Gate & 4.3M & 6.1 & 43\\,GB & $+$57K \\\\"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex",
    "old_string": "Uniform Gate & 4.3M & 6.0 & 43\\,GB & $+$57K \\\\",
    "new_string": "Uniform Gate & 4.3M & 6.1 & 43\\,GB & $+$57K \\\\"
  }
}
```

</details>

---

### Tool result

_source line 116 · 2026-05-25T20:53:39.001489+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 117 · 2026-05-25T20:53:39.001665+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex",
  "old_string": "\\caption{Scheduled sampling compresses the TF-AR gap from 7.9$\\times$ to ${\\sim}$1.2$\\times$, the only variant approaching parity across five training conditions.}",
  "new_string": "\\caption{Scheduled sampling compresses the TF-AR gap from 7.9$\\times$ to ${\\sim}$1.3$\\times$ (3-seed mean), the only variant approaching parity across five training conditions.}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex",
    "old_string": "\\caption{Scheduled sampling compresses the TF-AR gap from 7.9$\\times$ to ${\\sim}$1.2$\\times$, the only variant approaching parity across five training conditions.}",
    "new_string": "\\caption{Scheduled sampling compresses the TF-AR gap from 7.9$\\times$ to ${\\sim}$1.3$\\times$ (3-seed mean), the only variant approaching parity across five training conditions.}"
  }
}
```

</details>

---

### Tool result

_source line 118 · 2026-05-25T20:53:39.001824+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 119 · 2026-05-25T20:53:39.001950+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex",
  "old_string": "Across three seeds, AR GAR-ours rises to $0.401\\pm0.047$, compressing the gap from 7.9$\\times$ to ${\\sim}$1.2$\\times$ (TF GAR $0.498\\pm0.004$) with no PPL cost ($1.441\\pm0.002$; Figure~\\ref{fig:ss-gap}; per-seed details in Appendix~\\ref{sec:appendix-perseed}).",
  "new_string": "Across three seeds, AR GAR-ours rises to $0.401\\pm0.047$, compressing the gap from 7.9$\\times$ to ${\\sim}$1.3$\\times$ (TF GAR $0.517\\pm0.032$; 3-seed mean) with no PPL cost ($1.441\\pm0.002$; Figure~\\ref{fig:ss-gap}; per-seed details in Appendix~\\ref{sec:appendix-perseed})."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex",
    "old_string": "Across three seeds, AR GAR-ours rises to $0.401\\pm0.047$, compressing the gap from 7.9$\\times$ to ${\\sim}$1.2$\\times$ (TF GAR $0.498\\pm0.004$) with no PPL cost ($1.441\\pm0.002$; Figure~\\ref{fig:ss-gap}; per-seed details in Appendix~\\ref{sec:appendix-perseed}).",
    "new_string": "Across three seeds, AR GAR-ours rises to $0.401\\pm0.047$, compressing the gap from 7.9$\\times$ to ${\\sim}$1.3$\\times$ (TF GAR $0.517\\pm0.032$; 3-seed mean) with no PPL cost ($1.441\\pm0.002$; Figure~\\ref{fig:ss-gap}; per-seed details in Appendix~\\ref{sec:appendix-perseed})."
  }
}
```

</details>

---

### Tool result

_source line 120 · 2026-05-25T20:53:39.002106+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 121 · 2026-05-25T20:53:39.002231+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/introduction.tex",
  "old_string": "\\caption{Exposure bias collapses auxiliary attention losses. \\textbf{(a)}~Goal attention decays 85--90\\% across turns under AR generation on both Qwen-2.5-7B and Llama-3.1-8B. \\textbf{(b)}~Under TF evaluation all variants reach GAR$\\approx$0.50, but AR generation collapses GAR by 8--17$\\times$ (log scale). \\textbf{(c)}~Scheduled sampling compresses the TF--AR gap from 7.9$\\times$ to 1.2$\\times$ (Qwen) and ${\\sim}$27$\\times$ to 2.9$\\times$ (Llama).}",
  "new_string": "\\caption{Exposure bias collapses auxiliary attention losses. \\textbf{(a)}~Goal attention decays 85--90\\% across turns under AR generation on both Qwen-2.5-7B and Llama-3.1-8B. \\textbf{(b)}~Under TF evaluation all variants reach GAR$\\approx$0.50, but AR generation collapses GAR by 8--17$\\times$ (log scale). \\textbf{(c)}~Scheduled sampling compresses the TF--AR gap from 7.9$\\times$ to 1.3$\\times$ (Qwen, 3-seed mean) and ${\\sim}$27$\\times$ to 2.9$\\times$ (Llama).}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/introduction.tex",
    "old_string": "\\caption{Exposure bias collapses auxiliary attention losses. \\textbf{(a)}~Goal attention decays 85--90\\% across turns under AR generation on both Qwen-2.5-7B and Llama-3.1-8B. \\textbf{(b)}~Under TF evaluation all variants reach GAR$\\approx$0.50, but AR generation collapses GAR by 8--17$\\times$ (log scale). \\textbf{(c)}~Scheduled sampling compresses the TF--AR gap from 7.9$\\times$ to 1.2$\\times$ (Qwen) and ${\\sim}$27$\\times$ to 2.9$\\times$ (Llama).}",
    "new_string": "\\caption{Exposure bias collapses auxiliary attention losses. \\textbf{(a)}~Goal attention decays 85--90\\% across turns under AR generation on both Qwen-2.5-7B and Llama-3.1-8B. \\textbf{(b)}~Under TF evaluation all variants reach GAR$\\approx$0.50, but AR generation collapses GAR by 8--17$\\times$ (log scale). \\textbf{(c)}~Scheduled sampling compresses the TF--AR gap from 7.9$\\times$ to 1.3$\\times$ (Qwen, 3-seed mean) and ${\\sim}$27$\\times$ to 2.9$\\times$ (Llama).}"
  }
}
```

</details>

---

### Tool result

_source line 122 · 2026-05-25T20:53:39.002396+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/introduction.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 123 · 2026-05-25T20:53:39.002585+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/introduction.tex",
  "old_string": "\\item \\textbf{Scheduled sampling as remedy.} The first application of scheduled sampling to auxiliary attention objectives in multi-turn transformers, compressing the TF--AR gap to ${\\sim}$1.2$\\times$ on Qwen and ${\\sim}$2.9$\\times$ on Llama with no perplexity degradation, robust across three seeds.",
  "new_string": "\\item \\textbf{Scheduled sampling as remedy.} The first application of scheduled sampling to auxiliary attention objectives in multi-turn transformers, compressing the TF--AR gap to ${\\sim}$1.3$\\times$ on Qwen (3-seed mean) and ${\\sim}$2.9$\\times$ on Llama with no perplexity degradation, robust across three seeds."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/introduction.tex",
    "old_string": "\\item \\textbf{Scheduled sampling as remedy.} The first application of scheduled sampling to auxiliary attention objectives in multi-turn transformers, compressing the TF--AR gap to ${\\sim}$1.2$\\times$ on Qwen and ${\\sim}$2.9$\\times$ on Llama with no perplexity degradation, robust across three seeds.",
    "new_string": "\\item \\textbf{Scheduled sampling as remedy.} The first application of scheduled sampling to auxiliary attention objectives in multi-turn transformers, compressing the TF--AR gap to ${\\sim}$1.3$\\times$ on Qwen (3-seed mean) and ${\\sim}$2.9$\\times$ on Llama with no perplexity degradation, robust across three seeds."
  }
}
```

</details>

---

### Tool result

_source line 124 · 2026-05-25T20:53:39.002741+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/introduction.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 125 · 2026-05-25T20:53:39.002863+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/conclusion.tex",
  "old_string": "Scheduled sampling compresses the gap to ${\\sim}$1.2$\\times$ (Qwen) and ${\\sim}$2.9$\\times$ (Llama), generalizing across architectures and seeds",
  "new_string": "Scheduled sampling compresses the gap to ${\\sim}$1.3$\\times$ (Qwen, 3-seed mean) and ${\\sim}$2.9$\\times$ (Llama), generalizing across architectures and seeds"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/conclusion.tex",
    "old_string": "Scheduled sampling compresses the gap to ${\\sim}$1.2$\\times$ (Qwen) and ${\\sim}$2.9$\\times$ (Llama), generalizing across architectures and seeds",
    "new_string": "Scheduled sampling compresses the gap to ${\\sim}$1.3$\\times$ (Qwen, 3-seed mean) and ${\\sim}$2.9$\\times$ (Llama), generalizing across architectures and seeds"
  }
}
```

</details>

---

### Tool result

_source line 126 · 2026-05-25T20:53:39.002997+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/conclusion.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 127 · 2026-05-25T20:53:39.003114+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex",
  "old_string": "weaker than Qwen's ${\\sim}$1.2$\\times$ likely due to fewer training epochs",
  "new_string": "weaker than Qwen's ${\\sim}$1.3$\\times$ (3-seed mean) likely due to fewer training epochs"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex",
    "old_string": "weaker than Qwen's ${\\sim}$1.2$\\times$ likely due to fewer training epochs",
    "new_string": "weaker than Qwen's ${\\sim}$1.3$\\times$ (3-seed mean) likely due to fewer training epochs"
  }
}
```

</details>

---

### Tool result

_source line 128 · 2026-05-25T20:53:39.003276+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 129 · 2026-05-25T20:53:39.003451+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex",
  "old_string": "Scheduled sampling reduces the gap to ${\\sim}$1.2$\\times$, the only variant approaching parity.",
  "new_string": "Scheduled sampling reduces the gap to ${\\sim}$1.3$\\times$ (3-seed mean), the only variant approaching parity."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex",
    "old_string": "Scheduled sampling reduces the gap to ${\\sim}$1.2$\\times$, the only variant approaching parity.",
    "new_string": "Scheduled sampling reduces the gap to ${\\sim}$1.3$\\times$ (3-seed mean), the only variant approaching parity."
  }
}
```

</details>

---

### Tool result

_source line 130 · 2026-05-25T20:53:39.003906+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 131 · 2026-05-25T20:53:39.004060+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex",
  "old_string": "the near-parity of scheduled sampling (${\\sim}$1.2$\\times$ gap) suggests that bridging",
  "new_string": "the near-parity of scheduled sampling (${\\sim}$1.3$\\times$ gap) suggests that bridging"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex",
    "old_string": "the near-parity of scheduled sampling (${\\sim}$1.2$\\times$ gap) suggests that bridging",
    "new_string": "the near-parity of scheduled sampling (${\\sim}$1.3$\\times$ gap) suggests that bridging"
  }
}
```

</details>

---

### Tool result

_source line 132 · 2026-05-25T20:53:39.004442+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 133 · 2026-05-25T20:53:39.004598+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex",
  "old_string": "\\caption{Exposure bias scaling analysis. (a)~TF/AR gap ratio across training variants; scheduled sampling (SS, ${\\sim}$1.2$\\times$) is the only variant near parity. Llama gaps ($\\sim$27$\\times$) exceed all Qwen variants. (b)~Gap compounds with conversation length: ThreadGate's gap widens from 8$\\times$ (3.6 turns) to 31$\\times$ (10 turns).}",
  "new_string": "\\caption{Exposure bias scaling analysis. (a)~TF/AR gap ratio across training variants; scheduled sampling (SS, ${\\sim}$1.3$\\times$, 3-seed mean) is the only variant near parity. Llama gaps ($\\sim$27$\\times$) exceed all Qwen variants. (b)~Gap compounds with conversation length: ThreadGate's gap widens from 8$\\times$ (3.6 turns) to 31$\\times$ (10 turns).}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex",
    "old_string": "\\caption{Exposure bias scaling analysis. (a)~TF/AR gap ratio across training variants; scheduled sampling (SS, ${\\sim}$1.2$\\times$) is the only variant near parity. Llama gaps ($\\sim$27$\\times$) exceed all Qwen variants. (b)~Gap compounds with conversation length: ThreadGate's gap widens from 8$\\times$ (3.6 turns) to 31$\\times$ (10 turns).}",
    "new_string": "\\caption{Exposure bias scaling analysis. (a)~TF/AR gap ratio across training variants; scheduled sampling (SS, ${\\sim}$1.3$\\times$, 3-seed mean) is the only variant near parity. Llama gaps ($\\sim$27$\\times$) exceed all Qwen variants. (b)~Gap compounds with conversation length: ThreadGate's gap widens from 8$\\times$ (3.6 turns) to 31$\\times$ (10 turns).}"
  }
}
```

</details>

---

### Tool result

_source line 134 · 2026-05-25T20:53:39.004981+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 135 · 2026-05-25T20:53:39.005213+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex",
  "offset": "808",
  "limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex",
    "offset": "808",
    "limit": "30"
  }
}
```

</details>

---

### Tool result

_source line 136 · 2026-05-25T20:53:39.005376+00:00_

808	
809	\paragraph{Cross-model comparison.}
810	Table~\ref{tab:llama-vs-qwen-ss} compares scheduled sampling across both architectures. Both models show large gap compression relative to their ThreadGate baselines, but the residual gap on Llama (2.9$\times$) is larger than Qwen's (1.2$\times$). We attribute this to training duration: Llama received only 2 epochs of scheduled sampling exposure versus Qwen's 3 epochs. Llama reduces its median-based gap by 9.3$\times$ (from 27$\times$ to 2.9$\times$) while Qwen reduces by 6.6$\times$ (from 7.9$\times$ to 1.2$\times$), suggesting that a third epoch would likely narrow the residual gap further. Notably, $\beta$-steering is more effective on Llama (0.791 vs.\ 0.717 at $\beta$\,=\,5), partially compensating for the weaker training-time compression.
811	
812	\paragraph{Architectural differences.}
813	Several architectural differences between Qwen-2.5-7B and Llama-3.1-8B may contribute to the cross-model gap variation. Llama uses Grouped Query Attention (GQA) with 8 KV heads (vs.\ Qwen's full 28-head multi-head attention, MHA), which reduces the number of independently steerable attention heads by 3.5$\times$. Llama also uses Rotary Position Embedding (RoPE) with a longer default context (128K tokens vs.\ Qwen's 32K), which may affect how positional information interacts with goal-token attention at different conversation depths. Despite these differences, the qualitative pattern is identical: TF convergence, AR collapse, and SS-mediated recovery, confirming that exposure bias on auxiliary attention losses is architecture-general rather than an artifact of a specific attention implementation.
814	
815	\paragraph{Training dynamics.}
816	The Llama SS training loss trajectory closely mirrors Qwen's during the first two epochs: NTP loss converges within epoch~1 (final NTP loss 0.62 for Llama vs.\ 0.58 for Qwen), while GAR loss continues to decrease throughout epoch~2. The scheduled sampling ratio reaches ${\sim}$0.20 at the end
…[truncated 997 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 137 · 2026-05-25T20:53:39.005598+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex",
  "old_string": "TF GAR & 0.498 & 0.477 \\\\\nAR GAR ($\\beta$\\,=\\,0) & 0.401 & 0.166 \\\\\nTF/AR gap & 1.2$\\times$ & 2.9$\\times$ \\\\\nBaseline TG gap & 7.9$\\times$ & 27$\\times$ (median) \\\\\nGap compression & 6.6$\\times$ & 9.3$\\times$ \\\\",
  "new_string": "TF GAR & 0.517 & 0.477 \\\\\nAR GAR ($\\beta$\\,=\\,0) & 0.401 & 0.166 \\\\\nTF/AR gap & 1.3$\\times$ & 2.9$\\times$ \\\\\nBaseline TG gap & 7.9$\\times$ & 27$\\times$ (median) \\\\\nGap compression & 6.1$\\times$ & 9.3$\\times$ \\\\"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex",
    "old_string": "TF GAR & 0.498 & 0.477 \\\\\nAR GAR ($\\beta$\\,=\\,0) & 0.401 & 0.166 \\\\\nTF/AR gap & 1.2$\\times$ & 2.9$\\times$ \\\\\nBaseline TG gap & 7.9$\\times$ & 27$\\times$ (median) \\\\\nGap compression & 6.6$\\times$ & 9.3$\\times$ \\\\",
    "new_string": "TF GAR & 0.517 & 0.477 \\\\\nAR GAR ($\\beta$\\,=\\,0) & 0.401 & 0.166 \\\\\nTF/AR gap & 1.3$\\times$ & 2.9$\\times$ \\\\\nBaseline TG gap & 7.9$\\times$ & 27$\\times$ (median) \\\\\nGap compression & 6.1$\\times$ & 9.3$\\times$ \\\\"
  }
}
```

</details>

---

### Tool result

_source line 138 · 2026-05-25T20:53:39.005973+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 139 · 2026-05-25T20:53:39.006129+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex",
  "old_string": "the residual gap on Llama (2.9$\\times$) is larger than Qwen's (1.2$\\times$). We attribute this to training duration: Llama received only 2 epochs of scheduled sampling exposure versus Qwen's 3 epochs. Llama reduces its median-based gap by 9.3$\\times$ (from 27$\\times$ to 2.9$\\times$) while Qwen reduces by 6.6$\\times$ (from 7.9$\\times$ to 1.2$\\times$), suggesting that a third epoch would likely narrow the residual gap further.",
  "new_string": "the residual gap on Llama (2.9$\\times$) is larger than Qwen's (${\\sim}$1.3$\\times$, 3-seed mean). We attribute this to training duration: Llama received only 2 epochs of scheduled sampling exposure versus Qwen's 3 epochs. Llama reduces its median-based gap by 9.3$\\times$ (from 27$\\times$ to 2.9$\\times$) while Qwen reduces by 6.1$\\times$ (from 7.9$\\times$ to ${\\sim}$1.3$\\times$), suggesting that a third epoch would likely narrow the residual gap further."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex",
    "old_string": "the residual gap on Llama (2.9$\\times$) is larger than Qwen's (1.2$\\times$). We attribute this to training duration: Llama received only 2 epochs of scheduled sampling exposure versus Qwen's 3 epochs. Llama reduces its median-based gap by 9.3$\\times$ (from 27$\\times$ to 2.9$\\times$) while Qwen reduces by 6.6$\\times$ (from 7.9$\\times$ to 1.2$\\times$), suggesting that a third epoch would likely narrow the residual gap further.",
    "new_string": "the residual gap on Llama (2.9$\\times$) is larger than Qwen's (${\\sim}$1.3$\\times$, 3-seed mean). We attribute this to training duration: Llama received only 2 epochs of scheduled sampling exposure versus Qwen's 3 epochs. Llama reduces its median-based gap by 9.3$\\times$ (from 27$\\times$ to 2.9$\\times$) while Qwen reduces by 6.1$\\times$ (from 7.9$\\times$ to ${\\sim}$1.3$\\times$), suggesting that a third epoch would likely narrow the residual gap further."
  }
}
```

</details>

---

### Tool result

_source line 140 · 2026-05-25T20:53:39.006524+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 141 · 2026-05-25T20:53:39.006756+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "1\\.2.{0,5}\\\\times",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Grep",
  "tool_args": {
    "pattern": "1\\.2.{0,5}\\\\times",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 142 · 2026-05-25T20:53:39.006909+00:00_

paper/sections/analysis.tex:28:We test specificity with Turn-level Residual Coherence (TRC), the cosine similarity between adjacent-turn hidden states. TF/AR TRC is 0.334/0.332 for ThreadGate (gap $+$0.002) and 0.349/0.411 for LoRA-only (gap $-$0.062, reversed); exposure bias thus disrupts a specific routing behavior while leaving representations intact. Cross-model evaluation confirms: GAR-Dongre shows negligible shift on both Llama (1.002$\times$) and Qwen (1.28$\times$) vs.\ the order-of-magnitude GAR-ours collapse.
paper/sections/appendix.tex:211:\paragraph{GAR-Dongre cross-model comparison.} GAR-Dongre shows negligible distribution shift on Llama (AR/TF ratio 1.002$\times$), compared to 1.28$\times$ on Qwen. This confirms the mechanism specificity finding: exposure bias selectively disrupts the concentrated last-token attention pattern (GAR-ours) while leaving the diffuse all-token attention (GAR-Dongre) unaffected across both architectures.
paper/sections/appendix.tex:633:[Omitted long matching line]
paper/sections/appendix.tex:689:[Omitted long matching line]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 143 · 2026-05-25T20:53:39.007081+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_crossmodel_detail.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_crossmodel_detail.tex"
  }
}
```

</details>

---

### Tool result

_source line 144 · 2026-05-25T20:53:39.007224+00:00_

1	% Cross-model detailed comparison: Qwen2.5-7B-Instruct vs Llama-3.1-8B-Instruct
2	% Conditions shared by both models: Base, ThreadGate, LoRA-only
3	% Qwen TF: N=200 held-out; Qwen AR: d048_final_ar N=50 gen beta=0
4	% Llama TF: N=50 held-out T=4; Llama AR: eval_llama_ar_n20 N=20 T=4
5	% Llama SS: p1_llama_ss_eval (epoch_1 checkpoint, N=50)
6	\begin{table*}[t]
7	\centering
8	\caption{Cross-model comparison of goal-adherence metrics on Qwen2.5-7B-Instruct and Llama-3.1-8B-Instruct.
9	Gap ratio = TF GAR / AR GAR; lower is better (less exposure bias).
10	All Qwen rows use seed 42; SS per-seed mean analysis in Table~\ref{tab:perseed-ss}.
11	Qwen AR uses $N{=}50$ gen-mode evaluation; Llama AR uses $N{=}20$, $T{=}4$ (SS: $N{=}50$).
12	Llama AR GAR and gaps are mean-based; median-based TG gap is 27$\times$ (\S\ref{subsec:cross-model}).}
13	\label{tab:crossmodel-detail}
14	\small
15	\begin{tabular}{@{}ll ccccc@{}}
16	\toprule
17	\textbf{Model} & \textbf{Condition} & \textbf{TF GAR}$\uparrow$ & \textbf{AR GAR}$\uparrow$ & \textbf{TF PPL}$\downarrow$ & \textbf{AR PPL}$\downarrow$ & \textbf{Gap}$\downarrow$ \\
18	\midrule
19	\multirow{4}{*}{Qwen-7B}
20	  & Base      & 0.013 & 0.019 & 4.34 & 1.447 & 0.7$\times$ \\
21	  & TG        & 0.504 & 0.064 & 2.78 & 1.432 & 7.9$\times$ \\
22	  & LoRA-only & 0.498 & 0.037 & 2.78 & 1.431 & 13.5$\times$ \\
23	  & \textbf{SS} & 0.502 & \textbf{0.347} & 2.78 & 1.441 & \textbf{1.4$\times$} \\
24	\midrule
25	\multirow{4}{*}{Llama-8B}
26	  & Base      & 0.017 & 0.009 & 3.45 & 1.293 & 1.9$\times$ \\
27	  & TG        & 0.484 & 0.043 & 2.57 & 1.437 & 11.2$\times$ \\
28	  & LoRA-only & 0.481 & 0.028 & 2.60 & 1.419 & 17.2$\times$ \\
29	  & \textbf{SS} & 0.477 & \textbf{0.166} & 2.82 & 1.370 & \textbf{2.9$\times$} \\
30	\bottomrule
31	\end{tabular}
32	\end{table*}
33	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 145 · 2026-05-25T20:53:39.007400+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_perseed_tg.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_perseed_tg.tex"
  }
}
```

</details>

---

### Tool result

_source line 146 · 2026-05-25T20:53:39.007599+00:00_

1	% Per-seed detailed results for ThreadGate (TG) — seeds 42, 123
2	% TF eval: N=200 held-out conversations
3	% AR eval: N=5, T=10 model-generated conversations (original eval protocol)
4	\begin{table}[h]
5	\centering
6	\caption{Per-seed results for ThreadGate (TG) on Qwen2.5-7B-Instruct.
7	TF evaluation uses 200 held-out conversations.
8	AR evaluation uses extended-generation protocol ($N{=}5$, $T{=}10$ turns); under the gen-mode protocol ($N{=}50$) used in Table~\ref{tab:five-way}, AR GAR is 0.064 (s42) and 0.055 (s123) with gap ratios 7.9$\times$ and 9.1$\times$ respectively.}
9	\label{tab:perseed-tg}
10	\resizebox{\columnwidth}{!}{
11	\begin{tabular}{@{}l cc c@{}}
12	\toprule
13	\textbf{Metric} & \textbf{Seed 42} & \textbf{Seed 123} & \textbf{Mean $\pm$ Std} \\
14	\midrule
15	\multicolumn{4}{@{}l}{\textit{Teacher-Forced (TF)}} \\
16	\quad GAR-ours $\uparrow$   & 0.504 & 0.505 & 0.504 $\pm$ 0.001 \\
17	\quad GAR-Dongre $\uparrow$ & 0.015 & 0.012 & 0.014 $\pm$ 0.002 \\
18	\quad PPL $\downarrow$       & 2.784 & 2.780 & 2.782 $\pm$ 0.003 \\
19	\midrule
20	\multicolumn{4}{@{}l}{\textit{Autoregressive (AR), $\beta = 0$}} \\
21	\quad GAR-ours $\uparrow$   & 0.016 & 0.017 & 0.016 $\pm$ 0.001 \\
22	\quad GAR-Dongre $\uparrow$ & 0.019 & 0.018 & 0.019 $\pm$ 0.001 \\
23	\quad PPL $\downarrow$       & 1.360 & 1.386 & 1.373 $\pm$ 0.018 \\
24	\midrule
25	\multicolumn{4}{@{}l}{\textit{Derived}} \\
26	\quad Gap ratio (TF/AR GAR-ours) $\downarrow$ & 32.1 & 30.6 & 31.4 $\pm$ 1.1 \\
27	\bottomrule
28	\end{tabular}}
29	\end{table}
30	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 147 · 2026-05-25T20:53:39.007776+00:00_

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
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
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

_source line 148 · 2026-05-25T20:53:39.007902+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 149 · 2026-05-25T20:53:39.008045+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/fix_w1_w2_report.md",
  "content": "# Fix Report: W1 + W2 + INFO-1 + INFO-2\n\n## W1: tab_crossmodel_detail SS row (WARNING)\n\n**Problem:** TF GAR from IID s42 (0.498), AR GAR from 3-seed mean (0.401), mixed data sources.\n\n**Fix:**\n- SS row updated to consistent s42 data: TF=0.502, AR=0.347, Gap=1.4x\n- Caption: added \"All Qwen rows use seed 42; SS per-seed mean analysis in Table perseed-ss\"\n- File: `artifacts/appendix_expansion/tab_crossmodel_detail.tex`\n\n**Cascade updates (narrative references to SS gap):**\nAll main-text references changed from ~1.2x to ~1.3x (3-seed mean = 0.517/0.401 = 1.29):\n- `introduction.tex`: fig1 caption + contribution bullet\n- `experiments.tex`: fig caption + SS paragraph (TF GAR updated to 0.517+-0.032)\n- `analysis.tex`: cross-model paragraph\n- `conclusion.tex`: summary sentence\n- `appendix.tex`: EB scaling section (lines 491, 495, 500), llama-vs-qwen-ss table (TF 0.498->0.517, gap 1.2->1.3, compression 6.6->6.1), surrounding text (line 810)\n\n## W2: tab_perseed_tg AR protocol mismatch (WARNING)\n\n**Problem:** Table uses N=5, T=10 protocol (AR GAR 0.016/0.017), main results use N=50 gen-mode (0.064).\n\n**Fix:** No N=50 per-seed data for all metrics (PPL, GAR-Dongre). Added protocol clarification to caption:\n\"AR evaluation uses extended-generation protocol (N=5, T=10 turns); under the gen-mode protocol (N=50) used in Table five-way, AR GAR is 0.064 (s42) and 0.055 (s123) with gap ratios 7.9x and 9.1x respectively.\"\n\nFile: `artifacts/appendix_expansion/tab_perseed_tg.tex`\n\n## INFO-1: SS s42 TF GAR cross-table inconsistency\n\n**Problem:** perseed table s42 TF=0.502, crossmodel table had 0.498.\n**Fix:** Resolved by W1 fix (crossmodel SS TF now 0.502).\n\n## INFO-2: Cost table training time precision\n\n**Problem:** Uniform Gate actual 6.11h rounded to 6.0h (same as ThreadGate).\n**Fix:** Uniform Gate time changed from 6.0 to 6.1 in `appendix.tex` cost table.\n\n## Unchanged (verified correct)\n- `tab_perseed_ss.tex`: no changes needed\n- Per-seed gap values in appendix paragraph (s42=1.4x, s123=1.3x, s456=1.2x): already correct\n- Llama SS values: unchanged (single evaluation, internally consistent)\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/fix_w1_w2_report.md",
    "content": "# Fix Report: W1 + W2 + INFO-1 + INFO-2\n\n## W1: tab_crossmodel_detail SS row (WARNING)\n\n**Problem:** TF GAR from IID s42 (0.498), AR GAR from 3-seed mean (0.401), mixed data sources.\n\n**Fix:**\n- SS row updated to consistent s42 data: TF=0.502, AR=0.347, Gap=1.4x\n- Caption: added \"All Qwen rows use seed 42; SS per-seed mean analysis in Table perseed-ss\"\n- File: `artifacts/appendix_expansion/tab_crossmodel_detail.tex`\n\n**Cascade updates (narrative references to SS gap):**\nAll main-text references changed from ~1.2x to ~1.3x (3-seed mean = 0.517/0.401 = 1.29):\n- `introduction.tex`: fig1 caption + contribution bullet\n- `experiments.tex`: fig caption + SS paragraph (TF GAR updated to 0.517+-0.032)\n- `analysis.tex`: cross-model paragraph\n- `conclusion.tex`: summary sentence\n- `appendix.tex`: EB scaling section (lines 491, 495, 500), llama-vs-qwen-ss table (TF 0.498->0.517, gap 1.2->1.3, compression 6.6->6.1), surrounding text (line 810)\n\n## W2: tab_perseed_tg AR protocol mismatch (WARNING)\n\n**Problem:** Table uses N=5, T=10 protocol (AR GAR 0.016/0.017), main results use N=50 gen-mode (0.064).\n\n**Fix:** No N=50 per-seed data for all metrics (PPL, GAR-Dongre). Added protocol clarification to caption:\n\"AR evaluation uses extended-generation protocol (N=5, T=10 turns); under the gen-mode protocol (N=50) used in Table five-way, AR GAR is 0.064 (s42) and 0.055 (s123) with gap ratios 7.9x and 9.1x respectively.\"\n\nFile: `artifacts/appendix_expansion/tab_perseed_tg.tex`\n\n## INFO-1: SS s42 TF GAR cross-table inconsistency\n\n**Problem:** perseed table s42 TF=0.502, crossmodel table had 0.498.\n**Fix:** Resolved by W1 fix (crossmodel SS TF now 0.502).\n\n## INFO-2: Cost table training time precision\n\n**Problem:** Uniform Gate actual 6.11h rounded to 6.0h (same as ThreadGate).\n**Fix:** Uniform Gate time changed from 6.0 to 6.1 in `appendix.tex` cost table.\n\n## Unchanged (verified correct)\n- `tab_perseed_ss.tex`: no changes needed\n- Per-seed gap values in appendix paragraph (s42=1.4x, s123=1.3x, s456=1.2x): already correct\n- Llama SS values: unchanged (single evaluation, internally consistent)\n"
  }
}
```

</details>

---

### Tool result

_source line 150 · 2026-05-25T20:53:39.008243+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/fix_w1_w2_report.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 151 · 2026-05-25T20:53:39.008371+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__register_artifact",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__register_artifact",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 152 · 2026-05-25T20:53:39.008526+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 153 · 2026-05-25T20:53:39.008650+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "fix_w1_w2_report",
  "type": "report",
  "description": "Fix report for 2 WARNING + 2 INFO data consistency issues found by reviewer",
  "project": "turn_residual_gating",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/fix_w1_w2_report.md",
  "tags": "['paper', 'review-fix', 'data-consistency']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "fix_w1_w2_report",
    "type": "report",
    "description": "Fix report for 2 WARNING + 2 INFO data consistency issues found by reviewer",
    "project": "turn_residual_gating",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/fix_w1_w2_report.md",
    "tags": "['paper', 'review-fix', 'data-consistency']"
  }
}
```

</details>

---

### Tool result

_source line 154 · 2026-05-25T20:53:39.008791+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260525_9fee72\", \"name\": \"fix_w1_w2_report\", \"type\": \"report\", \"description\": \"Fix report for 2 WARNING + 2 INFO data consistency issues found by reviewer\", \"path\": \"projects/turn_residual_gating/artifacts/_project/report/fix_w1_w2_report.md\", \"url\": null, \"project\": \"turn_residual_gating\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-25T20:53:28.029703+00:00\", \"tags\": [\"paper\", \"review-fix\", \"data-consistency\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 155 · 2026-05-25T20:53:39.008953+00:00_

全部修正完成。总结：

**W1** — crossmodel 表 SS 行统一用 s42：TF 0.502, AR 0.347, Gap 1.4×；caption 标注 seed 42。

**W2** — perseed TG 表 caption 增加 N=50 协议下的 AR GAR (0.064/0.055) 和 gap (7.9×/9.1×) 说明，解释与主表的协议差异。

**INFO-1** — 已由 W1 修正覆盖（crossmodel TF 0.498→0.502）。

**INFO-2** — cost 表 Uniform Gate 时间 6.0→6.1h。

**连锁更新** — 正文/附录中 SS gap 从 ~1.2× 改为 ~1.3×（3-seed mean），涉及 introduction/experiments/analysis/conclusion/appendix 共 11 处；experiments.tex 的 TF GAR 同步更新为 0.517±0.032；llama-vs-qwen-ss 对比表的 Qwen TF/gap/compression 一并修正。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_fix_reviewer_w1_w2_issues_20260525T204337"
}
```

</details>

---
