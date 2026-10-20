# paper compile results tables

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 21
- **Recorded user turns:** 0
- **Tool calls:** 10
- **Original source:** `logs/chats/worker_paper_compile_results_tables_20260516T001056.jsonl`
- **Structured JSON:** [`3e9b4ed10a93dc0a3772.json`](../../sessions/3e/3e9b4ed10a93dc0a3772.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

21 recorded events

### Tool call

_source line 1 · 2026-05-16T00:15:58.516570+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__register_artifact",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_compile_results_tables_20260516T001056",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__register_artifact",
    "max_results": "4"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-16T00:15:58.516923+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_compile_results_tables_20260516T001056",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-16T00:15:58.517107+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "trace-verdict-study",
  "fields": "['*']",
  "limit": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_compile_results_tables_20260516T001056",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "trace-verdict-study",
    "fields": "['*']",
    "limit": "0"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-16T00:15:58.517277+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "trace-verdict-study",
  "file": "paper_framing.md",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_compile_results_tables_20260516T001056",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "trace-verdict-study",
    "file": "paper_framing.md",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-16T00:15:58.517750+00:00_

Error: result (71,579 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study/e9f265c4-8adc-40a5-9fbd-4166ad09cdc9/tool-results/mcp-agent-ml-research-read_registry-1778890274580.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study/e9f265c4-8adc-40a5-9fbd-4166ad09cdc9/tool-results/mcp-agent-ml-research-read_registry-1778890274580.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_compile_results_tables_20260516T001056",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-16T00:15:58.518399+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/paper_framing.md\", \"content\": \"# Paper Framing — trace-verdict-study\\n\\n> v3.0 — [UPDATED 2026-05-15] D030 CLOSED: DeepSeek VOTA 84.45% confirmed correct (confirmatory re-eval). **Critical narrative fix**: to_chat_text() preserves labels → VOTA 训练时 verdict label 未被截断 → 论文中 \\\"label truncation/corruption\\\" 措辞对 VOTA 不成立。正确叙事: trace INPUT content 被截断 (91.7% samples), 84.45% 反映 trace information loss。新增 D11: VOTA cross-model gap confounded by training-time truncation。数据集来源：HumanEval (164) + MBPP-sanitized (427) = 591 problems × 10 LLM-generated solutions = 5910 samples。\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (ARR submission)\\n- Fallback: EMNLP 2026 Findings\\n- Deadline: ARR May 25, 2026\\n\\n## Core Insight\\n\\nVerdict prediction (pass/fail) is fundamentally a **fault detection** task. The most effective signal is the **exception event** — a compact, structured diagnostic moment that consistently outperforms all other trace representations across models (Qwen 99.83% ± 0.00 across 3 seeds; DeepSeek 91-99% depending on seed, but always > VOTA 84.45% and no_trace 73.36%). In contrast, richer trace representations that require deeper execution reasoning show model-dependent effectiveness: VOTA gap = 14.96pp, no_trace gap = 1.77pp. Information density — not training signal distribution — is the primary bottleneck: even oracle loss masking (label-only) cannot close the 13pp gap between full traces and targeted extraction. The design principle: **extract the highest-specificity diagnostic signal; discard everything else.** Cross-model absolute performance depends on LoRA initialization stability, but exception_only's relative dominance over other components is robust.\\n\\nVOTA's primary contribution is **fault indicator isolation** — automatically extracting exception events from noisy full traces — rather than generic trace
…[truncated 28918 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_compile_results_tables_20260516T001056",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-16T00:15:58.518648+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study/e9f265c4-8adc-40a5-9fbd-4166ad09cdc9/tool-results/mcp-agent-ml-research-read_registry-1778890274580.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nexps = json.loads(data['result'])\n# Extract key fields for all DONE experiments\nfor e in exps:\n    if e.get('status') == 'DONE':\n        exp_id = e.get('exp_id', '')\n        metrics = e.get('metrics', {})\n        conclusion = e.get('conclusion', '')\n        print(f'=== {exp_id} ===')\n        print(f'  metrics: {json.dumps(metrics, indent=2)}')\n        print(f'  conclusion: {conclusion[:200]}')\n        print()\n\" 2>&1 | head -500",
  "description": "Extract DONE experiments with metrics from registry"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_compile_results_tables_20260516T001056",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study/e9f265c4-8adc-40a5-9fbd-4166ad09cdc9/tool-results/mcp-agent-ml-research-read_registry-1778890274580.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nexps = json.loads(data['result'])\n# Extract key fields for all DONE experiments\nfor e in exps:\n    if e.get('status') == 'DONE':\n        exp_id = e.get('exp_id', '')\n        metrics = e.get('metrics', {})\n        conclusion = e.get('conclusion', '')\n        print(f'=== {exp_id} ===')\n        print(f'  metrics: {json.dumps(metrics, indent=2)}')\n        print(f'  conclusion: {conclusion[:200]}')\n        print()\n\" 2>&1 | head -500",
    "description": "Extract DONE experiments with metrics from registry"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-16T00:15:58.518794+00:00_

Traceback (most recent call last):
  File "&lt;string>", line 7, in &lt;module>
    if e.get('status') == 'DONE':
       ^^^^^
AttributeError: 'str' object has no attribute 'get'

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_compile_results_tables_20260516T001056",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-16T00:15:58.518919+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study/e9f265c4-8adc-40a5-9fbd-4166ad09cdc9/tool-results/mcp-agent-ml-research-read_registry-1778890274580.txt",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_compile_results_tables_20260516T001056",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study/e9f265c4-8adc-40a5-9fbd-4166ad09cdc9/tool-results/mcp-agent-ml-research-read_registry-1778890274580.txt",
    "limit": "100"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-16T00:15:58.519039+00:00_

File content (29395 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_compile_results_tables_20260516T001056",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-16T00:15:58.519152+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "head -c 500 /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study/e9f265c4-8adc-40a5-9fbd-4166ad09cdc9/tool-results/mcp-agent-ml-research-read_registry-1778890274580.txt",
  "description": "Inspect file structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_compile_results_tables_20260516T001056",
  "tool": "Bash",
  "tool_args": {
    "command": "head -c 500 /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study/e9f265c4-8adc-40a5-9fbd-4166ad09cdc9/tool-results/mcp-agent-ml-research-read_registry-1778890274580.txt",
    "description": "Inspect file structure"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-16T00:15:58.519299+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"full_trace_256tok_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T22:27:14.119Z\", \"updated_at\": \"2026-05-16T00:03:55.505Z\", \"spec\": {\"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/full_trace_{train,test}.jsonl\", \"data_count\": 4720, \"model_name\": \"Qwen/Qwen2.5-Coder-7B-Instruct\", \"seed\": 42, \"max_trace_tokens\": 256}, \"server\": \"westd-11235\", \"gpu\": \"cuda:1\", \"acco

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_compile_results_tables_20260516T001056",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-16T00:15:58.519435+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport json\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study/e9f265c4-8adc-40a5-9fbd-4166ad09cdc9/tool-results/mcp-agent-ml-research-read_registry-1778890274580.txt') as f:\n    raw = json.load(f)\ndata = json.loads(raw['result'])\nexps = data['data']['experiments']\nfor eid, e in exps.items():\n    if e.get('status') == 'DONE':\n        m = e.get('metrics', {})\n        print(f'=== {eid} ===')\n        for k,v in m.items():\n            print(f'  {k}: {v}')\n        print()\n\" 2>&1 | head -600",
  "description": "Parse registry experiments and extract metrics"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_compile_results_tables_20260516T001056",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport json\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study/e9f265c4-8adc-40a5-9fbd-4166ad09cdc9/tool-results/mcp-agent-ml-research-read_registry-1778890274580.txt') as f:\n    raw = json.load(f)\ndata = json.loads(raw['result'])\nexps = data['data']['experiments']\nfor eid, e in exps.items():\n    if e.get('status') == 'DONE':\n        m = e.get('metrics', {})\n        print(f'=== {eid} ===')\n        for k,v in m.items():\n            print(f'  {k}: {v}')\n        print()\n\" 2>&1 | head -600",
    "description": "Parse registry experiments and extract metrics"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-16T00:15:58.519659+00:00_

=== full_trace_256tok_seed42 ===
  accuracy: 0.7882
  majority_baseline: 0.7151
  lift: 0.0731
  n: 1190
  pass_precision: 0.903
  pass_recall: 0.788
  pass_f1: 0.842
  fail_precision: 0.597
  fail_recall: 0.788
  fail_f1: 0.679
  accuracy_ci: [0.764, 0.81]
  train_loss: 0.1094
  train_runtime_sec: 3047
  epochs: 3

=== deepseek_full_trace_seed42_v3 ===
  eval_loss: 0.1108
  eval_mean_token_accuracy: 0.9801
  train_loss: 0.0547
  train_runtime_seconds: 8891
  epochs: 3
  accuracy: 0.7916
  majority_baseline: 0.7151
  lift: 0.0765
  n: 1190
  pass_precision: 0.857
  pass_recall: 0.851
  pass_f1: 0.854
  fail_precision: 0.632
  fail_recall: 0.643
  fail_f1: 0.637
  accuracy_ci: [0.768, 0.813]
  pass_f1_ci: [0.836, 0.87]
  fail_f1_ci: [0.592, 0.678]

=== debugbench_exception_bug_fix ===

=== deepseek_vota_seed42 ===
  accuracy: 0.8445
  majority_baseline: 0.7151
  lift: 0.1294
  accuracy_ci: [0.826, 0.864]
  pass_precision: 0.821
  pass_recall: 1
  pass_f1: 0.902
  fail_precision: 1
  fail_recall: 0.454
  fail_f1: 0.625
  eval_loss_epoch1: 0.0679
  eval_loss_epoch2: 0.095
  eval_loss_epoch3: 0.1121
  final_train_loss: 0.0522
  epoch1_checkpoint_eval: {'accuracy': 0.7815, 'accuracy_ci': [0.76, 0.803], 'fail_recall': 0.233, 'fail_precision': 1, 'pass_recall': 1, 'pass_precision': 0.766, 'fail_f1': 0.378, 'pass_f1': 0.867, 'conclusion': 'epoch3_final_is_better'}
  reeval_with_fixed_script: {'accuracy': 0.16, 'accuracy_ci': [0.139, 0.18], 'fail_f1': 0.61, 'fail_precision': 0.9, 'fail_recall': 0.47, 'pass_f1': 0.07, 'pass_precision': 1, 'pass_recall': 0.04, 'note': 'CATASTROPHIC: re-eval with corrected evaluate.py shows 16% (vs original 84.45%). Model predicts fail for almost everything. Previous 84.45% may have been from buggy eval. NEEDS INVESTIGATION.'}
  group_analysis: {'train_truncated': {'n': 1091, 'accuracy': 0.8304, 'ci_95': [0.8075, 0.8524], 'correct': 906, 'incorrect': 185, 'pass_accuracy': 1, 'pass_n': 822, 'fail_accuracy': 0.3123, 'fail_n': 269}, 'train_intact'
…[truncated 10927 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_compile_results_tables_20260516T001056",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-16T00:15:58.519928+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/paper_tables",
  "description": "Create output directory for paper tables"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_compile_results_tables_20260516T001056",
  "tool": "Bash",
  "tool_args": {
    "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/paper_tables",
    "description": "Create output directory for paper tables"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-16T00:15:58.520063+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_compile_results_tables_20260516T001056",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-16T00:15:58.520241+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/paper_tables/main_results_tables.tex",
  "content": "% =============================================================================\n% Paper Tables for trace-verdict-study\n% EMNLP 2026 Main — ARR May 25\n% Generated from experiment registry (2026-05-16)\n% =============================================================================\n\n% Required packages (add to preamble):\n% \\usepackage{booktabs}\n% \\usepackage{multirow}\n\n\n% =============================================================================\n% TABLE 1: Qwen-2.5-Coder-7B Main Results\n% =============================================================================\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\begin{tabular}{@{}llcccc@{}}\n\\toprule\n& \\textbf{Condition} & \\textbf{Acc.\\,(\\%)} & \\textbf{Pass\\,$F_1$} & \\textbf{Fail\\,$F_1$} & \\textbf{95\\% CI} \\\\\n\\midrule\n\\multirow{2}{*}{\\textit{Baselines}}\n& Majority (pass)           & 71.51 & ---   & ---   & --- \\\\\n& No trace                  & 75.13 & 81.3  & 62.7  & [72.8, 77.5] \\\\\n\\midrule\n\\multirow{2}{*}{\\textit{Full trace}}\n& Standard                  & 81.76 & 87.2  & 68.5  & [79.7, 83.9] \\\\\n& Label-only loss            & 86.22 & 90.6  & 74.0  & [84.4, 88.1] \\\\\n\\midrule\n\\multirow{3}{*}{\\textit{Components}}\n& Loop only (Tier\\,2)       & 85.63 & 89.7  & 76.5  & [83.5, 87.6] \\\\\n& Exception only (Tier\\,1)  & \\textbf{99.83} & \\textbf{99.9}  & \\textbf{99.7}  & [99.6, 100] \\\\\n& A/E only (Tier\\,1)        & 99.92 & 99.9$^\\dagger$  & 99.9$^\\dagger$ & [99.8, 100] \\\\\n\\midrule\n\\multirow{2}{*}{\\textit{VOTA}}\n& VOTA ($-$A/E)             & 99.41 & 99.6  & 98.9  & [98.9, 99.8] \\\\\n& VOTA (full)               & 99.41 & 99.4  & 98.6  & [98.8, 99.8] \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{\nVerdict prediction results on Qwen-2.5-Coder-7B-Instruct (seed\\,=\\,42, $n$\\,=\\,1190).\n\\textit{Label-only loss}: full trace input with gradient computed only on verdict tokens (oracle loss masking).\n\\textit{A/E}: actual/expected assertion-point component.\nTier\\,1 components (exception, A/E) individually achieve near-perfect accuracy;\nTier\\,2 (loop) carries substantial signal but is subsumed by Tier\\,1.\nVOTA combining both tiers introduces noise: exception only (99.83\\%) $>$ VOTA full (99.41\\%), $p$\\,=\\,0.01 (paired bootstrap, $B$\\,=\\,10{,}000).\n$^\\dagger$F$_1$ computed from confusion matrix (1 error / 1190 samples).\nAll CIs: percentile bootstrap, $B$\\,=\\,10{,}000.\n}\n\\label{tab:main-results}\n\\end{table*}\n\n\n% =============================================================================\n% TABLE 2: Cross-Model Comparison (DeepSeek-Coder-6.7B)\n% =============================================================================\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n\\textbf{Condition} & \\textbf{Acc.\\,(\\%)} & \\textbf{Pass\\,$F_1$} & \\textbf{Fail\\,$F_1$} & \\textbf{95\\% CI} \\\\\n\\midrule\nNo trace           & 73.36 & 81.3  & 53.9  & [70.8, 75.7] \\\\\nFull trace (v3)    & 79.16 & 85.4  & 63.7  & [76.8, 81.3] \\\\\nVOTA               & 84.45 & 90.2  & 62.5  & [82.6, 86.4] \\\\\nException only     & \\textbf{99.33} & \\textbf{99.5} & \\textbf{98.8} & [98.8, 99.8] \\\\\n\\midrule\n\\multicolumn{5}{@{}l}{\\textit{Cross-model gap (Qwen $-$ DeepSeek):}} \\\\\n\\quad No trace     & \\multicolumn{4}{l}{$+$1.77\\,pp} \\\\\n\\quad VOTA         & \\multicolumn{4}{l}{$+$14.96\\,pp} \\\\\n\\quad Exception    & \\multicolumn{4}{l}{$+$0.50\\,pp} \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{\nDeepSeek-Coder-6.7B-Instruct results (seed\\,=\\,42, epoch\\,3, $n$\\,=\\,1190).\nException only is the best component on both models.\nThe cross-model gap scales with signal complexity:\nminimal for exception (0.50\\,pp), moderate for no trace (1.77\\,pp),\nlarge for VOTA (14.96\\,pp).\nVOTA gap partly attributable to training-time trace content truncation\n(91.7\\% of samples truncated to ${\\sim}$2048 tokens; labels preserved).\nFull trace v3 uses label-preserving truncation (v1 collapsed due to label truncation).\nAll CIs: percentile bootstrap, $B$\\,=\\,10{,}000 (unpaired).\n}\n\\label{tab:cross-model}\n\\end{table}\n\n\n% =============================================================================\n% TABLE 3: Seed Robustness\n% =============================================================================\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{@{}llccc@{}}\n\\toprule\n\\textbf{Model} & \\textbf{Seed} & \\textbf{Acc.\\,(\\%)} & \\textbf{Fail\\,$R$} & \\textbf{95\\% CI} \\\\\n\\midrule\n\\multicolumn{5}{@{}l}{\\textit{Exception only}} \\\\\n\\midrule\n\\multirow{3}{*}{Qwen-7B}\n& 42  & 99.83 & 1.000 & [99.6, 100] \\\\\n& 123 & 99.83 & 1.000 & [99.6, 100] \\\\\n& 456 & 99.83 & 1.000 & [99.6, 100] \\\\\n\\cmidrule{2-5}\n& \\textit{$\\sigma$} & \\textit{0.00} & & \\\\\n\\midrule\n\\multirow{3}{*}{DeepSeek-6.7B}\n& 42  & 99.33 & 1.000 & --- \\\\\n& 456 & 99.33 & 1.000 & [98.8, 99.8] \\\\\n& 123 & 91.09$^*$ & 0.705 & [89.4, 92.6] \\\\\n\\cmidrule{2-5}\n& \\textit{$\\sigma$} & \\textit{$\\approx$4.8} & & \\\\\n\\midrule\n\\multicolumn{5}{@{}l}{\\textit{VOTA}} \\\\\n\\midrule\n\\multirow{2}{*}{Qwen-7B}\n& 42  & 99.41 & 1.000 & [98.8, 99.8] \\\\\n& 456 & 99.08 & 1.000 & [98.5, 99.6] \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{\nSeed robustness across models and conditions.\nQwen exception only is perfectly robust: 3 seeds yield identical accuracy (99.83\\%),\nidentical error samples (id\\,=\\,901, 905; both \\texttt{GeneratorExit} false alarms),\nconfirming 99.83\\% as the representation's theoretical ceiling.\nDeepSeek shows seed-dependent performance: 2/3 seeds match at 99.33\\%,\nseed\\,123 is a LoRA initialization outlier (fail recall\\,=\\,0.705) but\nstill exceeds VOTA (84.45\\%) and no trace (73.36\\%).\n$^*$LoRA initialization outlier.\nFail\\,$R$: fail recall.\n}\n\\label{tab:seed-robustness}\n\\end{table}\n\n\n% =============================================================================\n% TABLE 4: Calibration Analysis (Qwen-2.5-Coder-7B, seed = 42)\n% =============================================================================\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n\\textbf{Condition} & \\textbf{Acc.\\,(\\%)} & \\textbf{ECE\\,$\\downarrow$} & \\textbf{MCE\\,$\\downarrow$} & \\textbf{Brier\\,$\\downarrow$} \\\\\n\\midrule\nNo trace            & 75.13 & .1715 & .4756 & .1972 \\\\\nFull trace          & 81.76 & .0958 & .2491 & .1439 \\\\\nLabel-only loss     & 86.22 & .1107 & .4171 & .1201 \\\\\nLoop only           & 85.63 & .0831 & .1834 & .1183 \\\\\n\\midrule\nVOTA                & 99.41 & .0054 & .6225 & .0052 \\\\\nException only      & 99.83 & .0027 & .8355$^\\ddagger$ & .0013 \\\\\nA/E only            & \\textbf{99.92} & \\textbf{.0004} & \\textbf{.0004} & \\textbf{.0008} \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{\nCalibration metrics on Qwen-2.5-Coder-7B (seed\\,=\\,42, $n$\\,=\\,1190).\nECE: expected calibration error (10 bins).\nMCE: maximum calibration error.\nBrier: Brier score.\nTier\\,1 components achieve near-perfect calibration\n(ECE $\\leq$ 0.003, Brier $\\leq$ 0.005),\nwhile no-trace ECE is ${\\sim}$63$\\times$ higher than exception only\nand Brier is ${\\sim}$152$\\times$ higher.\n$^\\ddagger$Exception only MCE is inflated by a single low-population bin\ncontaining the 2 irreducible \\texttt{GeneratorExit} errors\n(high-confidence incorrect predictions); ECE and Brier\nare more representative of overall calibration quality.\n}\n\\label{tab:calibration}\n\\end{table}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_compile_results_tables_20260516T001056",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/paper_tables/main_results_tables.tex",
    "content": "% =============================================================================\n% Paper Tables for trace-verdict-study\n% EMNLP 2026 Main — ARR May 25\n% Generated from experiment registry (2026-05-16)\n% =============================================================================\n\n% Required packages (add to preamble):\n% \\usepackage{booktabs}\n% \\usepackage{multirow}\n\n\n% =============================================================================\n% TABLE 1: Qwen-2.5-Coder-7B Main Results\n% =============================================================================\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\begin{tabular}{@{}llcccc@{}}\n\\toprule\n& \\textbf{Condition} & \\textbf{Acc.\\,(\\%)} & \\textbf{Pass\\,$F_1$} & \\textbf{Fail\\,$F_1$} & \\textbf{95\\% CI} \\\\\n\\midrule\n\\multirow{2}{*}{\\textit{Baselines}}\n& Majority (pass)           & 71.51 & ---   & ---   & --- \\\\\n& No trace                  & 75.13 & 81.3  & 62.7  & [72.8, 77.5] \\\\\n\\midrule\n\\multirow{2}{*}{\\textit{Full trace}}\n& Standard                  & 81.76 & 87.2  & 68.5  & [79.7, 83.9] \\\\\n& Label-only loss            & 86.22 & 90.6  & 74.0  & [84.4, 88.1] \\\\\n\\midrule\n\\multirow{3}{*}{\\textit{Components}}\n& Loop only (Tier\\,2)       & 85.63 & 89.7  & 76.5  & [83.5, 87.6] \\\\\n& Exception only (Tier\\,1)  & \\textbf{99.83} & \\textbf{99.9}  & \\textbf{99.7}  & [99.6, 100] \\\\\n& A/E only (Tier\\,1)        & 99.92 & 99.9$^\\dagger$  & 99.9$^\\dagger$ & [99.8, 100] \\\\\n\\midrule\n\\multirow{2}{*}{\\textit{VOTA}}\n& VOTA ($-$A/E)             & 99.41 & 99.6  & 98.9  & [98.9, 99.8] \\\\\n& VOTA (full)               & 99.41 & 99.4  & 98.6  & [98.8, 99.8] \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{\nVerdict prediction results on Qwen-2.5-Coder-7B-Instruct (seed\\,=\\,42, $n$\\,=\\,1190).\n\\textit{Label-only loss}: full trace input with gradient computed only on verdict tokens (oracle loss masking).\n\\textit{A/E}: actual/expected assertion-point component.\nTier\\,1 components (exception, A/E) individually achieve near-perfect accuracy;\nTier\\,2 (loop) carries substantial signal but is subsumed by Tier\\,1.\nVOTA combining both tiers introduces noise: exception only (99.83\\%) $>$ VOTA full (99.41\\%), $p$\\,=\\,0.01 (paired bootstrap, $B$\\,=\\,10{,}000).\n$^\\dagger$F$_1$ computed from confusion matrix (1 error / 1190 samples).\nAll CIs: percentile bootstrap, $B$\\,=\\,10{,}000.\n}\n\\label{tab:main-results}\n\\end{table*}\n\n\n% =============================================================================\n% TABLE 2: Cross-Model Comparison (DeepSeek-Coder-6.7B)\n% =============================================================================\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n\\textbf{Condition} & \\textbf{Acc.\\,(\\%)} & \\textbf{Pass\\,$F_1$} & \\textbf{Fail\\,$F_1$} & \\textbf{95\\% CI} \\\\\n\\midrule\nNo trace           & 73.36 & 81.3  & 53.9  & [70.8, 75.7] \\\\\nFull trace (v3)    & 79.16 & 85.4  & 63.7  & [76.8, 81.3] \\\\\nVOTA               & 84.45 & 90.2  & 62.5  & [82.6, 86.4] \\\\\nException only     & \\textbf{99.33} & \\textbf{99.5} & \\textbf{98.8} & [98.8, 99.8] \\\\\n\\midrule\n\\multicolumn{5}{@{}l}{\\textit{Cross-model gap (Qwen $-$ DeepSeek):}} \\\\\n\\quad No trace     & \\multicolumn{4}{l}{$+$1.77\\,pp} \\\\\n\\quad VOTA         & \\multicolumn{4}{l}{$+$14.96\\,pp} \\\\\n\\quad Exception    & \\multicolumn{4}{l}{$+$0.50\\,pp} \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{\nDeepSeek-Coder-6.7B-Instruct results (seed\\,=\\,42, epoch\\,3, $n$\\,=\\,1190).\nException only is the best component on both models.\nThe cross-model gap scales with signal complexity:\nminimal for exception (0.50\\,pp), moderate for no trace (1.77\\,pp),\nlarge for VOTA (14.96\\,pp).\nVOTA gap partly attributable to training-time trace content truncation\n(91.7\\% of samples truncated to ${\\sim}$2048 tokens; labels preserved).\nFull trace v3 uses label-preserving truncation (v1 collapsed due to label truncation).\nAll CIs: percentile bootstrap, $B$\\,=\\,10{,}000 (unpaired).\n}\n\\label{tab:cross-model}\n\\end{table}\n\n\n% =============================================================================\n% TABLE 3: Seed Robustness\n% =============================================================================\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{@{}llccc@{}}\n\\toprule\n\\textbf{Model} & \\textbf{Seed} & \\textbf{Acc.\\,(\\%)} & \\textbf{Fail\\,$R$} & \\textbf{95\\% CI} \\\\\n\\midrule\n\\multicolumn{5}{@{}l}{\\textit{Exception only}} \\\\\n\\midrule\n\\multirow{3}{*}{Qwen-7B}\n& 42  & 99.83 & 1.000 & [99.6, 100] \\\\\n& 123 & 99.83 & 1.000 & [99.6, 100] \\\\\n& 456 & 99.83 & 1.000 & [99.6, 100] \\\\\n\\cmidrule{2-5}\n& \\textit{$\\sigma$} & \\textit{0.00} & & \\\\\n\\midrule\n\\multirow{3}{*}{DeepSeek-6.7B}\n& 42  & 99.33 & 1.000 & --- \\\\\n& 456 & 99.33 & 1.000 & [98.8, 99.8] \\\\\n& 123 & 91.09$^*$ & 0.705 & [89.4, 92.6] \\\\\n\\cmidrule{2-5}\n& \\textit{$\\sigma$} & \\textit{$\\approx$4.8} & & \\\\\n\\midrule\n\\multicolumn{5}{@{}l}{\\textit{VOTA}} \\\\\n\\midrule\n\\multirow{2}{*}{Qwen-7B}\n& 42  & 99.41 & 1.000 & [98.8, 99.8] \\\\\n& 456 & 99.08 & 1.000 & [98.5, 99.6] \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{\nSeed robustness across models and conditions.\nQwen exception only is perfectly robust: 3 seeds yield identical accuracy (99.83\\%),\nidentical error samples (id\\,=\\,901, 905; both \\texttt{GeneratorExit} false alarms),\nconfirming 99.83\\% as the representation's theoretical ceiling.\nDeepSeek shows seed-dependent performance: 2/3 seeds match at 99.33\\%,\nseed\\,123 is a LoRA initialization outlier (fail recall\\,=\\,0.705) but\nstill exceeds VOTA (84.45\\%) and no trace (73.36\\%).\n$^*$LoRA initialization outlier.\nFail\\,$R$: fail recall.\n}\n\\label{tab:seed-robustness}\n\\end{table}\n\n\n% =============================================================================\n% TABLE 4: Calibration Analysis (Qwen-2.5-Coder-7B, seed = 42)\n% =============================================================================\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n\\textbf{Condition} & \\textbf{Acc.\\,(\\%)} & \\textbf{ECE\\,$\\downarrow$} & \\textbf{MCE\\,$\\downarrow$} & \\textbf{Brier\\,$\\downarrow$} \\\\\n\\midrule\nNo trace            & 75.13 & .1715 & .4756 & .1972 \\\\\nFull trace          & 81.76 & .0958 & .2491 & .1439 \\\\\nLabel-only loss     & 86.22 & .1107 & .4171 & .1201 \\\\\nLoop only           & 85.63 & .0831 & .1834 & .1183 \\\\\n\\midrule\nVOTA                & 99.41 & .0054 & .6225 & .0052 \\\\\nException only      & 99.83 & .0027 & .8355$^\\ddagger$ & .0013 \\\\\nA/E only            & \\textbf{99.92} & \\textbf{.0004} & \\textbf{.0004} & \\textbf{.0008} \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{\nCalibration metrics on Qwen-2.5-Coder-7B (seed\\,=\\,42, $n$\\,=\\,1190).\nECE: expected calibration error (10 bins).\nMCE: maximum calibration error.\nBrier: Brier score.\nTier\\,1 components achieve near-perfect calibration\n(ECE $\\leq$ 0.003, Brier $\\leq$ 0.005),\nwhile no-trace ECE is ${\\sim}$63$\\times$ higher than exception only\nand Brier is ${\\sim}$152$\\times$ higher.\n$^\\ddagger$Exception only MCE is inflated by a single low-population bin\ncontaining the 2 irreducible \\texttt{GeneratorExit} errors\n(high-confidence incorrect predictions); ECE and Brier\nare more representative of overall calibration quality.\n}\n\\label{tab:calibration}\n\\end{table}\n"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-16T00:15:58.520497+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/paper_tables/main_results_tables.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_compile_results_tables_20260516T001056",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-16T00:15:58.520644+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "paper_main_results_tables",
  "type": "paper",
  "description": "4 LaTeX tables for EMNLP 2026 paper: Table 1 (Qwen main results with 9 conditions), Table 2 (DeepSeek cross-model comparison), Table 3 (seed robustness), Table 4 (calibration ECE/MCE/Brier). All numbers verified against experiment registry.",
  "project": "trace-verdict-study",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/paper_tables/main_results_tables.tex",
  "tags": "['paper', 'tables', 'results', 'emnlp2026']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_compile_results_tables_20260516T001056",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "paper_main_results_tables",
    "type": "paper",
    "description": "4 LaTeX tables for EMNLP 2026 paper: Table 1 (Qwen main results with 9 conditions), Table 2 (DeepSeek cross-model comparison), Table 3 (seed robustness), Table 4 (calibration ECE/MCE/Brier). All numbers verified against experiment registry.",
    "project": "trace-verdict-study",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/paper_tables/main_results_tables.tex",
    "tags": "['paper', 'tables', 'results', 'emnlp2026']"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-16T00:15:58.520831+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260516_9050b2\", \"name\": \"paper_main_results_tables\", \"type\": \"paper\", \"description\": \"4 LaTeX tables for EMNLP 2026 paper: Table 1 (Qwen main results with 9 conditions), Table 2 (DeepSeek cross-model comparison), Table 3 (seed robustness), Table 4 (calibration ECE/MCE/Brier). All numbers verified against experiment registry.\", \"path\": \"projects/trace-verdict-study/artifacts/_project/paper/main_results_tables.tex\", \"url\": null, \"project\": \"trace-verdict-study\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-16T00:15:44.379100+00:00\", \"tags\": [\"paper\", \"tables\", \"results\", \"emnlp2026\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_compile_results_tables_20260516T001056",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-16T00:15:58.521140+00:00_

4 张表格已生成并注册，保存在 `artifacts/paper_tables/main_results_tables.tex`。

**数据校验摘要**：

| 表格 | 内容 | 数据源 |
|------|------|--------|
| Table 1 | Qwen 9 条件主结果 | 全部来自 registry（v5 系列 + 组件实验） |
| Table 2 | DeepSeek 4 条件 + 跨模型 gap | deepseek_* registry 条目 |
| Table 3 | 种子鲁棒性（Qwen 3 seed + DeepSeek 3 seed + VOTA 2 seed） | exception_only_seed{42,123,456} + deepseek 对应条目 |
| Table 4 | 校准指标 ECE/MCE/Brier | calibration_analysis_seed42 registry 条目 |

**注意事项**：
- ae_only 的 F1 值（标注 †）是从混淆矩阵推导的（registry 无显式 F1），1 个错误 / 1190 样本
- exception_only MCE=0.8355 已加脚注说明是低样本 bin 导致的膨胀（2 个 GeneratorExit 不可约误差）
- Table 2 脚注标注 DeepSeek 用 unpaired bootstrap，且 VOTA gap 部分归因于训练时 trace content 截断（非 label 截断，符合 v3.0 framing）
- DeepSeek full_trace 使用 v3（label-preserving truncation fix），脚注已标注

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_compile_results_tables_20260516T001056"
}
```

</details>

---
