# analysis acc qw s020 n100 b2 fix

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 15
- **Recorded user turns:** 0
- **Tool calls:** 7
- **Original source:** `logs/chats/worker_analysis_acc_qw_s020_n100_b2_fix_20260515T224237.jsonl`
- **Structured JSON:** [`f62ae3175ffead47741f.json`](../../sessions/f6/f62ae3175ffead47741f.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

15 recorded events

### Tool call

_source line 1 · 2026-05-15T22:43:29.561951+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__update_registry",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_acc_qw_s020_n100_b2_fix_20260515T224237",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__update_registry",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-15T22:43:29.562502+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_acc_qw_s020_n100_b2_fix_20260515T224237",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T22:43:29.574866+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "tail -50 ~/runs/phase-gated-compound-sparse/acc_qw_s020_n100_b2_fix.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_acc_qw_s020_n100_b2_fix_20260515T224237",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "tail -50 ~/runs/phase-gated-compound-sparse/acc_qw_s020_n100_b2_fix.log",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-15T22:43:29.575148+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "find /root/autodl-tmp/pacs -name \"accuracy_eval_qw_s020*b2_fix*\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_acc_qw_s020_n100_b2_fix_20260515T224237",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "find /root/autodl-tmp/pacs -name \"accuracy_eval_qw_s020*b2_fix*\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-15T22:43:29.575520+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"  Importance collected (0.0s)\\n  [importance_s020] heads_pruned=140, kv_evicted=18/91\\n  [importance_s020] ✗ pred=3 ref=1 (5.9s) running=20/42\\n\\n[Problem 43/50] prompt_len=88\\n  Importance collected (0.0s)\\n  [importance_s020] heads_pruned=140, kv_evicted=17/88\\n  [importance_s020] ✗ pred=\\\\frac{224}{78125} ref=\\\\frac{448}{15625} (11.3s) running=20/43\\n\\n[Problem 44/50] prompt_len=91\\n  Importance collected (0.0s)\\n  [importance_s020] heads_pruned=140, kv_evicted=18/91\\n  [importance_s020] ✓ pred=33 ref=33 (78.2s) running=21/44\\n\\n[Problem 45/50] prompt_len=396\\n  Importance collected (0.0s)\\n  [importance_s020] heads_pruned=140, kv_evicted=79/396\\n  [importance_s020] ✗ pred=78^\\\\circ ref=80 (11.3s) running=21/45\\n\\n[Problem 46/50] prompt_len=127\\n  Importance collected (0.0s)\\n  [importance_s020] heads_pruned=140, kv_evicted=25/127\\n  [importance_s020] ✓ pred=-4 ref=-4 (12.7s) running=22/46\\n\\n[Problem 47/50] prompt_len=156\\n  Importance collected (0.0s)\\n  [importance_s020] heads_pruned=140, kv_evicted=31/156\\n  [importance_s020] ✗ pred=3 ref=1 \\\\pm \\\\sqrt{19} (12.5s) running=22/47\\n\\n[Problem 48/50] prompt_len=93\\n  Importance collected (0.0s)\\n  [importance_s020] heads_pruned=140, kv_evicted=18/93\\n  [importance_s020] ✗ pred=\\\\text{southwest} ref=\\\\text{east} (6.2s) running=22/48\\n\\n[Problem 49/50] prompt_len=66\\n  Importance collected (0.0s)\\n  [importance_s020] heads_pruned=140, kv_evicted=13/66\\n  [importance_s020] ✓ pred=2k + 2 ref=2k+2 (4.1s) running=23/49\\n\\n[Problem 50/50] prompt_len=144\\n  Importance collected (0.0s)\\n  [importance_s020] heads_pruned=140, kv_evicted=28/144\\n  [importance_s020] ✗ pred=\\\\begin{pmatrix} -\\\\frac{1}{3} \\\\\\\\ \\\\frac{2}{3} \\\\\\\\ \\\\frac{5}{3} \\\\end{pmatrix} ref=\\\\begin{pmatrix} -1/3 \\\\\\\\ 2/3 \\\\\\\\ 5/3 \\\\end{pmatrix} (19.6s) running=23/50\\n\\n=================================================
…[truncated 340 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_acc_qw_s020_n100_b2_fix_20260515T224237",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-15T22:43:29.582602+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/pacs/analysis_output/accuracy_eval_qw_s020_b2_fix.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_acc_qw_s020_n100_b2_fix_20260515T224237",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 7
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-15T22:43:29.618980+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "cat /root/autodl-tmp/pacs/analysis_output/accuracy_eval_qw_s020_b2_fix.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_acc_qw_s020_n100_b2_fix_20260515T224237",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "cat /root/autodl-tmp/pacs/analysis_output/accuracy_eval_qw_s020_b2_fix.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-15T22:43:29.619952+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"config\\\": {\\n    \\\"model\\\": \\\"checkpoints/Qwen2.5-7B-Instruct\\\",\\n    \\\"num_problems\\\": 50,\\n    \\\"max_new_tokens\\\": 8192,\\n    \\\"device\\\": \\\"cuda:0\\\",\\n    \\\"conditions\\\": [\\n      \\\"importance_s020\\\"\\n    ],\\n    \\\"seed\\\": 42\\n  },\\n  \\\"conditions\\\": {\\n    \\\"importance_s020\\\": {\\n      \\\"accuracy\\\": 0.46,\\n      \\\"correct\\\": 23,\\n      \\\"n_problems\\\": 50,\\n      \\\"details\\\": [\\n        {\\n          \\\"id\\\": \\\"test/number_theory/1055.json\\\",\\n          \\\"pred_answer\\\": \\\"88\\\",\\n          \\\"ref_answer\\\": \\\"203\\\",\\n          \\\"match\\\": false,\\n          \\\"gen_length\\\": 723,\\n          \\\"time_seconds\\\": 14.7\\n        },\\n        {\\n          \\\"id\\\": \\\"test/intermediate_algebra/1217.json\\\",\\n          \\\"pred_answer\\\": \\\"x^5 - x^4 +x^3 -x^2 + x - 1\\\",\\n          \\\"ref_answer\\\": \\\"x^5 - x^4 + x^3 - x^2 + x - 1\\\",\\n          \\\"match\\\": true,\\n          \\\"gen_length\\\": 844,\\n          \\\"time_seconds\\\": 17.1\\n        },\\n        {\\n          \\\"id\\\": \\\"test/prealgebra/951.json\\\",\\n          \\\"pred_answer\\\": \\\"9.165\\\",\\n          \\\"ref_answer\\\": \\\"12\\\",\\n          \\\"match\\\": false,\\n          \\\"gen_length\\\": 338,\\n          \\\"time_seconds\\\": 6.7\\n        },\\n        {\\n          \\\"id\\\": \\\"test/precalculus/1105.json\\\",\\n          \\\"pred_answer\\\": \\\"-\\\\\\\\frac{\\\\\\\\pi}{6}\\\",\\n          \\\"ref_answer\\\": \\\"-\\\\\\\\frac{\\\\\\\\pi}{6}\\\",\\n          \\\"match\\\": true,\\n          \\\"gen_length\\\": 270,\\n          \\\"time_seconds\\\": 5.3\\n        },\\n        {\\n          \\\"id\\\": \\\"test/prealgebra/572.json\\\",\\n          \\\"pred_answer\\\": \\\"0.15\\\",\\n          \\\"ref_answer\\\": \\\"0.15\\\",\\n          \\\"match\\\": true,\\n          \\\"gen_length\\\
…[truncated 8892 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_acc_qw_s020_n100_b2_fix_20260515T224237",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-15T22:43:29.644764+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "acc_qw_s020_n100_b2_fix",
  "field": "conclusion",
  "value": "success",
  "project": "phase-gated-compound-sparse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_acc_qw_s020_n100_b2_fix_20260515T224237",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "acc_qw_s020_n100_b2_fix",
    "field": "conclusion",
    "value": "success",
    "project": "phase-gated-compound-sparse"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-15T22:43:29.645226+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"acc_qw_s020_n100_b2_fix\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T22:22:55.755Z\", \"updated_at\": \"2026-05-15T22:43:14.397Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/pacs && python run_accuracy_eval.py --model checkpoints/Qwen2.5-7B-Instruct --conditions importance_s020 --num-problems 50 --start-index 50 --max-new-tokens 8192 --gpu cuda:0 --seed 42 --output-name accuracy_eval_qw_s020_b2_fix.json\\\"\", \"server\": \"westd-22162\", \"gpu\": [\"cuda:1\"], \"pid\": \"283051\", \"log_path\": \"~/runs/phase-gated-compound-sparse/acc_qw_s020_n100_b2_fix.log\", \"submitted_at\": \"2026-05-15T22:25:18.472Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"hypothesis\": \"重跑 QW s020 batch2 (problems 51-100) with max_new_tokens=8192，修复原 batch2 使用 2048 的不一致问题。\", \"parent\": \"acc_qw_s020_n100\", \"server\": \"westd-22162\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-22162\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-15T22:25:15.841Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/pacs && python run_accuracy_eval.py --model checkpoints/Qwen2.5-7B-Instruct --conditions importance_s020 --num-problems 50 --start-index 50 --max-new-tokens 8192 --gpu cuda:0 --seed 42 --output-name accuracy_eval_qw_s020_b2_fix.json\\\"\", \"code_commit\": \"1b4f61aa366a9fe320f8563c8f7acb5af58d78b7\", \"finished_at\": \"2026-05-15T22:40:53.877Z\", \"training_hours\": 0.26}, \"pid\": \"283051\", \"log_path\": \"~/runs/phase-gated-compound-sparse/acc_qw_s020_n100_b2_fix.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T22:40:57.414634+00:00\"}]}, \"conclusion\": \"success\"}}, \"erro
…[truncated 57 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_acc_qw_s020_n100_b2_fix_20260515T224237",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-15T22:43:29.645542+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "acc_qw_s020_n100_b2_fix",
  "field": "metrics",
  "value": "{'batch2_correct': 23, 'batch2_total': 50, 'batch2_acc': 0.46, 'batch1_correct_v2': 13, 'batch1_total': 50, 'batch1_acc_v2': 0.26, 'combined_correct': 36, 'combined_total': 100, 'combined_acc': 0.36, 'null_count': 2, 'truncated_count': 1, 'total_time_seconds': 884.3, 'max_new_tokens': 8192, 'original_batch2_correct': 22, 'original_batch2_acc': 0.44, 'delta_vs_original': '+1 correct (+0.02 acc)'}",
  "project": "phase-gated-compound-sparse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_acc_qw_s020_n100_b2_fix_20260515T224237",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "acc_qw_s020_n100_b2_fix",
    "field": "metrics",
    "value": "{'batch2_correct': 23, 'batch2_total': 50, 'batch2_acc': 0.46, 'batch1_correct_v2': 13, 'batch1_total': 50, 'batch1_acc_v2': 0.26, 'combined_correct': 36, 'combined_total': 100, 'combined_acc': 0.36, 'null_count': 2, 'truncated_count': 1, 'total_time_seconds': 884.3, 'max_new_tokens': 8192, 'original_batch2_correct': 22, 'original_batch2_acc': 0.44, 'delta_vs_original': '+1 correct (+0.02 acc)'}",
    "project": "phase-gated-compound-sparse"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-15T22:43:29.645865+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"acc_qw_s020_n100_b2_fix\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T22:22:55.755Z\", \"updated_at\": \"2026-05-15T22:43:20.497Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/pacs && python run_accuracy_eval.py --model checkpoints/Qwen2.5-7B-Instruct --conditions importance_s020 --num-problems 50 --start-index 50 --max-new-tokens 8192 --gpu cuda:0 --seed 42 --output-name accuracy_eval_qw_s020_b2_fix.json\\\"\", \"server\": \"westd-22162\", \"gpu\": [\"cuda:1\"], \"pid\": \"283051\", \"log_path\": \"~/runs/phase-gated-compound-sparse/acc_qw_s020_n100_b2_fix.log\", \"submitted_at\": \"2026-05-15T22:25:18.472Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"hypothesis\": \"重跑 QW s020 batch2 (problems 51-100) with max_new_tokens=8192，修复原 batch2 使用 2048 的不一致问题。\", \"parent\": \"acc_qw_s020_n100\", \"server\": \"westd-22162\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-22162\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-15T22:25:15.841Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/pacs && python run_accuracy_eval.py --model checkpoints/Qwen2.5-7B-Instruct --conditions importance_s020 --num-problems 50 --start-index 50 --max-new-tokens 8192 --gpu cuda:0 --seed 42 --output-name accuracy_eval_qw_s020_b2_fix.json\\\"\", \"code_commit\": \"1b4f61aa366a9fe320f8563c8f7acb5af58d78b7\", \"finished_at\": \"2026-05-15T22:40:53.877Z\", \"training_hours\": 0.26}, \"pid\": \"283051\", \"log_path\": \"~/runs/phase-gated-compound-sparse/acc_qw_s020_n100_b2_fix.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T22:40:57.414634+00:00\"}]}, \"conclusion\": \"success\", \"metric
…[truncated 504 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_acc_qw_s020_n100_b2_fix_20260515T224237",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-15T22:43:29.646111+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "acc_qw_s020_n100_b2_fix",
  "field": "checkpoint_path",
  "value": "N/A (eval only)",
  "project": "phase-gated-compound-sparse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_acc_qw_s020_n100_b2_fix_20260515T224237",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "acc_qw_s020_n100_b2_fix",
    "field": "checkpoint_path",
    "value": "N/A (eval only)",
    "project": "phase-gated-compound-sparse"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-15T22:43:29.646386+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"acc_qw_s020_n100_b2_fix\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T22:22:55.755Z\", \"updated_at\": \"2026-05-15T22:43:21.368Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/pacs && python run_accuracy_eval.py --model checkpoints/Qwen2.5-7B-Instruct --conditions importance_s020 --num-problems 50 --start-index 50 --max-new-tokens 8192 --gpu cuda:0 --seed 42 --output-name accuracy_eval_qw_s020_b2_fix.json\\\"\", \"server\": \"westd-22162\", \"gpu\": [\"cuda:1\"], \"pid\": \"283051\", \"log_path\": \"~/runs/phase-gated-compound-sparse/acc_qw_s020_n100_b2_fix.log\", \"submitted_at\": \"2026-05-15T22:25:18.472Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"hypothesis\": \"重跑 QW s020 batch2 (problems 51-100) with max_new_tokens=8192，修复原 batch2 使用 2048 的不一致问题。\", \"parent\": \"acc_qw_s020_n100\", \"server\": \"westd-22162\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-22162\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-15T22:25:15.841Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/pacs && python run_accuracy_eval.py --model checkpoints/Qwen2.5-7B-Instruct --conditions importance_s020 --num-problems 50 --start-index 50 --max-new-tokens 8192 --gpu cuda:0 --seed 42 --output-name accuracy_eval_qw_s020_b2_fix.json\\\"\", \"code_commit\": \"1b4f61aa366a9fe320f8563c8f7acb5af58d78b7\", \"finished_at\": \"2026-05-15T22:40:53.877Z\", \"training_hours\": 0.26}, \"pid\": \"283051\", \"log_path\": \"~/runs/phase-gated-compound-sparse/acc_qw_s020_n100_b2_fix.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T22:40:57.414634+00:00\"}]}, \"conclusion\": \"success\", \"metric
…[truncated 546 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_acc_qw_s020_n100_b2_fix_20260515T224237",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-15T22:43:29.684364+00:00_

Registry 已更新。总结：

**acc_qw_s020_n100_b2_fix 结果**

| 指标 | 值 |
|------|-----|
| batch2 fix | 23/50 = 0.46 |
| 原 batch2 (2048 tokens) | 22/50 = 0.44 |
| **差异** | **+1 correct (+0.02)** |
| batch1 v2 rescored | 13/50 = 0.26 |
| **combined** | **36/100 = 0.36** |
| null predictions | 2 |
| truncated (hit 8192) | 1 |
| 用时 | 884s |

**更新后 QW dose curve**：

| sparsity | accuracy |
|----------|----------|
| dense | 0.40 |
| s015 | 0.36 |
| **s020** | **0.36** (原 0.35) |
| s025 | 0.33 |
| s030 | 0.19 |

max_new_tokens 修复影响极小（仅 +1 题），s020 从 0.35 微调至 0.36，与 s015 持平。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_acc_qw_s020_n100_b2_fix_20260515T224237"
}
```

</details>

---
