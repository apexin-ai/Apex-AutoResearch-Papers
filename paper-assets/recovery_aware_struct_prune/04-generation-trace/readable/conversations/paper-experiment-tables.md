# paper experiment tables

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 9
- **Recorded user turns:** 0
- **Tool calls:** 4
- **Original source:** `logs/chats/worker_paper_experiment-tables_20260515T043938.jsonl`
- **Structured JSON:** [`09999af0c8a0f9498e69.json`](../../sessions/09/09999af0c8a0f9498e69.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

9 recorded events

### Tool call

_source line 1 · 2026-05-15T04:40:11.610808+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/tables",
  "description": "Create tables directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_experiment-tables_20260515T043938",
  "tool": "Bash",
  "tool_args": {
    "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/tables",
    "description": "Create tables directory"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-15T04:40:11.611125+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_experiment-tables_20260515T043938",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T04:40:11.611316+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/tables/table1_postprune.tex",
  "content": "\\begin{table}[t]\n\\centering\n\\caption{Post-prune accuracy on GSM8K (N=100). Baseline: Qwen2.5-7B. Standard and RASP remove identical parameter counts at matched sparsity; the difference is purely in head selection strategy.}\n\\label{tab:postprune}\n\\sisetup{round-mode=places, round-precision=0, table-format=2.0}\n\\begin{tabular}{l S[table-format=2.0] S[table-format=2.0] S[table-format=6.0]}\n\\toprule\n{Method} & {Sparsity (\\%)} & {GSM8K Acc (\\%)} & {Params Removed} \\\\\n\\midrule\nBaseline (no prune) & 0  & 94 & 0 \\\\\nStandard            & 20 & 1  & 395232 \\\\\nRASP ($\\alpha{=}1.0$) & 20 & 29 & 395232 \\\\\nGRASPrune           & 20 & \\textcolor{gray}{TBD} & \\textcolor{gray}{TBD} \\\\\n\\midrule\nStandard            & 25 & \\textcolor{gray}{TBD} & \\textcolor{gray}{TBD} \\\\\nRASP                & 25 & \\textcolor{gray}{TBD} & \\textcolor{gray}{TBD} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_experiment-tables_20260515T043938",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/tables/table1_postprune.tex",
    "content": "\\begin{table}[t]\n\\centering\n\\caption{Post-prune accuracy on GSM8K (N=100). Baseline: Qwen2.5-7B. Standard and RASP remove identical parameter counts at matched sparsity; the difference is purely in head selection strategy.}\n\\label{tab:postprune}\n\\sisetup{round-mode=places, round-precision=0, table-format=2.0}\n\\begin{tabular}{l S[table-format=2.0] S[table-format=2.0] S[table-format=6.0]}\n\\toprule\n{Method} & {Sparsity (\\%)} & {GSM8K Acc (\\%)} & {Params Removed} \\\\\n\\midrule\nBaseline (no prune) & 0  & 94 & 0 \\\\\nStandard            & 20 & 1  & 395232 \\\\\nRASP ($\\alpha{=}1.0$) & 20 & 29 & 395232 \\\\\nGRASPrune           & 20 & \\textcolor{gray}{TBD} & \\textcolor{gray}{TBD} \\\\\n\\midrule\nStandard            & 25 & \\textcolor{gray}{TBD} & \\textcolor{gray}{TBD} \\\\\nRASP                & 25 & \\textcolor{gray}{TBD} & \\textcolor{gray}{TBD} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-15T04:40:11.611472+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/tables/table1_postprune.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_experiment-tables_20260515T043938",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-15T04:40:11.611601+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/tables/table2_recovery.tex",
  "content": "\\begin{table}[t]\n\\centering\n\\caption{Recovery pipeline comparison on GSM8K (N=100, greedy decoding). Each column shows accuracy after the corresponding stage. Recovery $\\Delta$ = final accuracy $-$ post-prune accuracy.}\n\\label{tab:recovery}\n\\begin{tabular}{l S[table-format=2.0] S[table-format=2.0] S[table-format=2.0] S[table-format=3.0]}\n\\toprule\n{Pruning Method} & {Post-Prune (\\%)} & {+SFT (\\%)} & {+GRPO (\\%)} & {Recovery $\\Delta$} \\\\\n\\midrule\nStandard 20\\%  & 1  & 64 & \\textcolor{gray}{TBD} & \\textcolor{gray}{TBD} \\\\\nRASP 20\\%      & 29 & 57 & \\textcolor{gray}{TBD} & \\textcolor{gray}{TBD} \\\\\nGRASPrune 20\\% & \\textcolor{gray}{TBD} & \\textcolor{gray}{TBD} & \\textcolor{gray}{TBD} & \\textcolor{gray}{TBD} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_experiment-tables_20260515T043938",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/tables/table2_recovery.tex",
    "content": "\\begin{table}[t]\n\\centering\n\\caption{Recovery pipeline comparison on GSM8K (N=100, greedy decoding). Each column shows accuracy after the corresponding stage. Recovery $\\Delta$ = final accuracy $-$ post-prune accuracy.}\n\\label{tab:recovery}\n\\begin{tabular}{l S[table-format=2.0] S[table-format=2.0] S[table-format=2.0] S[table-format=3.0]}\n\\toprule\n{Pruning Method} & {Post-Prune (\\%)} & {+SFT (\\%)} & {+GRPO (\\%)} & {Recovery $\\Delta$} \\\\\n\\midrule\nStandard 20\\%  & 1  & 64 & \\textcolor{gray}{TBD} & \\textcolor{gray}{TBD} \\\\\nRASP 20\\%      & 29 & 57 & \\textcolor{gray}{TBD} & \\textcolor{gray}{TBD} \\\\\nGRASPrune 20\\% & \\textcolor{gray}{TBD} & \\textcolor{gray}{TBD} & \\textcolor{gray}{TBD} & \\textcolor{gray}{TBD} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-15T04:40:11.611732+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/tables/table2_recovery.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_experiment-tables_20260515T043938",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-15T04:40:11.611852+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/tables/table3_alpha.tex",
  "content": "\\begin{table}[t]\n\\centering\n\\caption{Ablation over the CKA balancing coefficient $\\alpha$ at 20\\% sparsity. $\\alpha{=}0$ reduces to standard importance-only pruning; higher $\\alpha$ increases the weight of CKA-based representational similarity in head selection.}\n\\label{tab:alpha}\n\\begin{tabular}{S[table-format=1.2] S[table-format=2.0] l l}\n\\toprule\n{$\\alpha$} & {Post-Prune Acc (\\%)} & {CKA Weight} & {Interpretation} \\\\\n\\midrule\n0.00 & \\textcolor{gray}{TBD} & None         & $=$ Standard pruning \\\\\n0.25 & \\textcolor{gray}{TBD} & Low          & Slight CKA awareness \\\\\n0.50 & \\textcolor{gray}{TBD} & Medium       & Balanced \\\\\n1.00 & 29                     & Full         & Default RASP \\\\\n2.00 & \\textcolor{gray}{TBD} & High         & Strong CKA emphasis \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_experiment-tables_20260515T043938",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/tables/table3_alpha.tex",
    "content": "\\begin{table}[t]\n\\centering\n\\caption{Ablation over the CKA balancing coefficient $\\alpha$ at 20\\% sparsity. $\\alpha{=}0$ reduces to standard importance-only pruning; higher $\\alpha$ increases the weight of CKA-based representational similarity in head selection.}\n\\label{tab:alpha}\n\\begin{tabular}{S[table-format=1.2] S[table-format=2.0] l l}\n\\toprule\n{$\\alpha$} & {Post-Prune Acc (\\%)} & {CKA Weight} & {Interpretation} \\\\\n\\midrule\n0.00 & \\textcolor{gray}{TBD} & None         & $=$ Standard pruning \\\\\n0.25 & \\textcolor{gray}{TBD} & Low          & Slight CKA awareness \\\\\n0.50 & \\textcolor{gray}{TBD} & Medium       & Balanced \\\\\n1.00 & 29                     & Full         & Default RASP \\\\\n2.00 & \\textcolor{gray}{TBD} & High         & Strong CKA emphasis \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-15T04:40:11.611989+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/tables/table3_alpha.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_experiment-tables_20260515T043938",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 9 · 2026-05-15T04:40:11.612141+00:00_

三个表格已创建：

- `artifacts/tables/table1_postprune.tex` — Post-prune 对比，已填入 Baseline/Standard/RASP 20% 数据
- `artifacts/tables/table2_recovery.tex` — Recovery pipeline 对比，已填入 Post-Prune 和 +SFT 数据
- `artifacts/tables/table3_alpha.tex` — α 消融，已填入 α=1.0 数据

所有表格使用 booktabs + siunitx S 列类型，TBD 以 `\textcolor{gray}{TBD}` 标记。主论文引用方式：`\input{tables/table1_postprune}`。需要在 preamble 中加载 `booktabs`、`siunitx`、`xcolor`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_experiment-tables_20260515T043938"
}
```

</details>

---
