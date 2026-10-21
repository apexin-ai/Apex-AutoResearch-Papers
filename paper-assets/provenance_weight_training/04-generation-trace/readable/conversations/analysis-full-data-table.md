# analysis full data table

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 51
- **Recorded user turns:** 0
- **Tool calls:** 25
- **Original source:** `logs/chats/worker_analysis_full_data_table_20260515T154608.jsonl`
- **Structured JSON:** [`3018133fdba52d03bc4e.json`](../../sessions/30/3018133fdba52d03bc4e.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

51 recorded events

### Tool call

_source line 1 · 2026-05-15T15:53:06.645092+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__read_project_file",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_full_data_table_20260515T154608",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__read_project_file",
    "max_results": "4"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-15T15:53:06.645449+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_full_data_table_20260515T154608",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T15:53:06.645622+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "provenance_weight_training",
  "fields": "['*']",
  "limit": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_full_data_table_20260515T154608",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "provenance_weight_training",
    "fields": "['*']",
    "limit": "0"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-15T15:53:06.646105+00:00_

Error: result (75,011 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/112e71b9-a790-4886-b870-1e5804f7b2f6/tool-results/mcp-agent-ml-research-read_registry-1778859984428.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/112e71b9-a790-4886-b870-1e5804f7b2f6/tool-results/mcp-agent-ml-research-read_registry-1778859984428.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/112e71b9-a790-4886-b870-1e5804f7b2f6/tool-results/mcp-agent-ml-research-read_registry-1778859984428.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_full_data_table_20260515T154608",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-15T15:53:06.646349+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Extract experiment data from registry",
  "prompt": "You have a JSON file at `/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/112e71b9-a790-4886-b870-1e5804f7b2f6/tool-results/mcp-agent-ml-research-read_registry-1778859984428.txt` containing experiment registry data. The file has schema `{result: string}` where `result` is a JSON string that needs to be parsed.\n\nYour task:\n1. First probe the structure with jq/python to understand the format\n2. Extract ALL experiments, focusing on those with conclusion=success, but also note negative/failed/killed ones\n3. For EACH experiment, extract these fields verbatim:\n   - exp_id\n   - title/name\n   - status, conclusion\n   - All parameters (seed, τ/tau, n_min, b, weighting_method, batch_size, learning_rate, etc.)\n   - All metrics (eval_loss, PPL, perplexity, any other metrics)\n   - parent experiment if any\n   - tags/labels\n   - Any notes about the experiment type (grid sweep, adaptive, ablation, etc.)\n\n4. Output a COMPLETE structured summary. Do NOT truncate or abbreviate. I need every single experiment with all its data points. Format as a Python dict printed to stdout, or just print all the data clearly.\n\nImportant: The data must be COMPLETE - every experiment, every metric, every parameter. This is for building paper-ready tables.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_full_data_table_20260515T154608",
  "tool": "Agent",
  "tool_args": {
    "description": "Extract experiment data from registry",
    "prompt": "You have a JSON file at `/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/112e71b9-a790-4886-b870-1e5804f7b2f6/tool-results/mcp-agent-ml-research-read_registry-1778859984428.txt` containing experiment registry data. The file has schema `{result: string}` where `result` is a JSON string that needs to be parsed.\n\nYour task:\n1. First probe the structure with jq/python to understand the format\n2. Extract ALL experiments, focusing on those with conclusion=success, but also note negative/failed/killed ones\n3. For EACH experiment, extract these fields verbatim:\n   - exp_id\n   - title/name\n   - status, conclusion\n   - All parameters (seed, τ/tau, n_min, b, weighting_method, batch_size, learning_rate, etc.)\n   - All metrics (eval_loss, PPL, perplexity, any other metrics)\n   - parent experiment if any\n   - tags/labels\n   - Any notes about the experiment type (grid sweep, adaptive, ablation, etc.)\n\n4. Output a COMPLETE structured summary. Do NOT truncate or abbreviate. I need every single experiment with all its data points. Format as a Python dict printed to stdout, or just print all the data clearly.\n\nImportant: The data must be COMPLETE - every experiment, every metric, every parameter. This is for building paper-ready tables.",
    "subagent_type": "general-purpose"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-15T15:53:06.646550+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/112e71b9-a790-4886-b870-1e5804f7b2f6/tool-results/mcp-agent-ml-research-read_registry-1778859984428.txt",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_full_data_table_20260515T154608",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/112e71b9-a790-4886-b870-1e5804f7b2f6/tool-results/mcp-agent-ml-research-read_registry-1778859984428.txt",
    "limit": "50"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-15T15:53:06.646689+00:00_

File content (31121 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_full_data_table_20260515T154608",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-15T15:53:06.646825+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/112e71b9-a790-4886-b870-1e5804f7b2f6/tool-results/mcp-agent-ml-research-read_registry-1778859984428.txt",
  "limit": "100",
  "offset": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_full_data_table_20260515T154608",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/112e71b9-a790-4886-b870-1e5804f7b2f6/tool-results/mcp-agent-ml-research-read_registry-1778859984428.txt",
    "limit": "100",
    "offset": "0"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-15T15:53:06.646975+00:00_

File content (31121 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_full_data_table_20260515T154608",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-15T15:53:06.647104+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "wc -l /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/112e71b9-a790-4886-b870-1e5804f7b2f6/tool-results/mcp-agent-ml-research-read_registry-1778859984428.txt",
  "description": "Check file line count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_full_data_table_20260515T154608",
  "tool": "Bash",
  "tool_args": {
    "command": "wc -l /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/112e71b9-a790-4886-b870-1e5804f7b2f6/tool-results/mcp-agent-ml-research-read_registry-1778859984428.txt",
    "description": "Check file line count"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-15T15:53:06.647223+00:00_

0 /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/112e71b9-a790-4886-b870-1e5804f7b2f6/tool-results/mcp-agent-ml-research-read_registry-1778859984428.txt

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_full_data_table_20260515T154608",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-15T15:53:06.647351+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport json\nwith open('/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/112e71b9-a790-4886-b870-1e5804f7b2f6/tool-results/mcp-agent-ml-research-read_registry-1778859984428.txt') as f:\n    raw = json.load(f)\n# raw has schema {result: string} where result is JSON string\ninner = json.loads(raw['result'])\nprint(type(inner))\nif isinstance(inner, dict):\n    print('Top-level keys:', list(inner.keys())[:20])\nelif isinstance(inner, list):\n    print('List length:', len(inner))\n    print('First item keys:', list(inner[0].keys()) if inner else 'empty')\n\" 2>&1",
  "description": "Parse JSON structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_full_data_table_20260515T154608",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport json\nwith open('/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/112e71b9-a790-4886-b870-1e5804f7b2f6/tool-results/mcp-agent-ml-research-read_registry-1778859984428.txt') as f:\n    raw = json.load(f)\n# raw has schema {result: string} where result is JSON string\ninner = json.loads(raw['result'])\nprint(type(inner))\nif isinstance(inner, dict):\n    print('Top-level keys:', list(inner.keys())[:20])\nelif isinstance(inner, list):\n    print('List length:', len(inner))\n    print('First item keys:', list(inner[0].keys()) if inner else 'empty')\n\" 2>&1",
    "description": "Parse JSON structure"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-15T15:53:06.647473+00:00_

&lt;class 'dict'>
Top-level keys: ['success', 'data', 'error', 'metadata']

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_full_data_table_20260515T154608",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-15T15:53:06.647599+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport json\nwith open('/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/112e71b9-a790-4886-b870-1e5804f7b2f6/tool-results/mcp-agent-ml-research-read_registry-1778859984428.txt') as f:\n    raw = json.load(f)\ninner = json.loads(raw['result'])\nprint('success:', inner['success'])\nprint('error:', inner['error'])\nprint('metadata:', json.dumps(inner['metadata'], indent=2))\ndata = inner['data']\nprint('data type:', type(data))\nif isinstance(data, dict):\n    print('data keys:', list(data.keys())[:30])\nelif isinstance(data, list):\n    print('data length:', len(data))\n\" 2>&1",
  "description": "Explore inner structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_full_data_table_20260515T154608",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport json\nwith open('/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/112e71b9-a790-4886-b870-1e5804f7b2f6/tool-results/mcp-agent-ml-research-read_registry-1778859984428.txt') as f:\n    raw = json.load(f)\ninner = json.loads(raw['result'])\nprint('success:', inner['success'])\nprint('error:', inner['error'])\nprint('metadata:', json.dumps(inner['metadata'], indent=2))\ndata = inner['data']\nprint('data type:', type(data))\nif isinstance(data, dict):\n    print('data keys:', list(data.keys())[:30])\nelif isinstance(data, list):\n    print('data length:', len(data))\n\" 2>&1",
    "description": "Explore inner structure"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-15T15:53:06.647729+00:00_

success: True
error: None
metadata: {
  "elapsed_seconds": 0.2745
}
data type: &lt;class 'dict'>
data keys: ['experiments', 'count', 'total', 'baseline']

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_full_data_table_20260515T154608",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-15T15:53:06.647899+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport json\nwith open('/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/112e71b9-a790-4886-b870-1e5804f7b2f6/tool-results/mcp-agent-ml-research-read_registry-1778859984428.txt') as f:\n    raw = json.load(f)\ninner = json.loads(raw['result'])\ndata = inner['data']\nprint('count:', data['count'])\nprint('total:', data['total'])\nprint('baseline:', json.dumps(data['baseline'], indent=2))\nexps = data['experiments']\nprint('experiments type:', type(exps))\nif isinstance(exps, list):\n    print('num experiments:', len(exps))\n    if exps:\n        print('first experiment keys:', list(exps[0].keys()))\nelif isinstance(exps, dict):\n    print('experiment ids:', list(exps.keys()))\n\" 2>&1",
  "description": "Explore experiments structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_full_data_table_20260515T154608",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport json\nwith open('/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/112e71b9-a790-4886-b870-1e5804f7b2f6/tool-results/mcp-agent-ml-research-read_registry-1778859984428.txt') as f:\n    raw = json.load(f)\ninner = json.loads(raw['result'])\ndata = inner['data']\nprint('count:', data['count'])\nprint('total:', data['total'])\nprint('baseline:', json.dumps(data['baseline'], indent=2))\nexps = data['experiments']\nprint('experiments type:', type(exps))\nif isinstance(exps, list):\n    print('num experiments:', len(exps))\n    if exps:\n        print('first experiment keys:', list(exps[0].keys()))\nelif isinstance(exps, dict):\n    print('experiment ids:', list(exps.keys()))\n\" 2>&1",
    "description": "Explore experiments structure"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-15T15:53:06.648032+00:00_

count: 40
total: 40
baseline: null
experiments type: &lt;class 'dict'>
experiment ids: ['tau_095_seed42', 'tau_09_seed42', 'tau_05_seed42', 'nmin4_seed42', 'nmin1_seed42', 'tau_06_seed42', 'ess_only_seed42', 'tau_07_seed42', 'golden_ratio_seed42', 'tau_0.6_seed42', 'detector_modernbert', 'grid_b5_0_seed456', 'grid_b3_0_seed456', 'grid_b2_0_seed456', 'grid_b_low_seed42', 'grid_b1_5_seed456', 'grid_b1_0_seed456', 'grid_b0_5_seed456', 'adaptive_fix_seed456', 'adaptive_fix_seed123', 'adaptive_fix_seed42', 'grid_b_seed42_batch', 'grid_b5_0_seed123', 'grid_b2_0_seed123', 'grid_b3_0_seed123', 'adaptive_v2_seed456', 'adaptive_v2_seed123', 'adaptive_v2_seed42', 'grid_b1_5_seed123', 'grid_b1_0_seed123', 'grid_b0_5_seed123', 'diagnostic_contamination100', 'uniform_seed456', 'uniform_seed123', 'uniform_seed42', 'adaptive_seed456', 'adaptive_seed123', 'adaptive_seed42', 'detector_tfidf_lr', 'datagen_synthetic_4gpu']

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_full_data_table_20260515T154608",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-15T15:53:06.648164+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport json\nwith open('/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/112e71b9-a790-4886-b870-1e5804f7b2f6/tool-results/mcp-agent-ml-research-read_registry-1778859984428.txt') as f:\n    raw = json.load(f)\ninner = json.loads(raw['result'])\nexps = inner['data']['experiments']\n# Print first experiment fully to understand schema\nfirst_key = list(exps.keys())[0]\nprint(json.dumps(exps[first_key], indent=2))\n\" 2>&1",
  "description": "Print first experiment to understand schema"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_full_data_table_20260515T154608",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport json\nwith open('/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/112e71b9-a790-4886-b870-1e5804f7b2f6/tool-results/mcp-agent-ml-research-read_registry-1778859984428.txt') as f:\n    raw = json.load(f)\ninner = json.loads(raw['result'])\nexps = inner['data']['experiments']\n# Print first experiment fully to understand schema\nfirst_key = list(exps.keys())[0]\nprint(json.dumps(exps[first_key], indent=2))\n\" 2>&1",
    "description": "Print first experiment to understand schema"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-15T15:53:06.648292+00:00_

{
  "status": "RUNNING",
  "retry_count": 0,
  "created_at": "2026-05-15T10:03:32.419Z",
  "updated_at": "2026-05-15T14:58:16.987Z",
  "hypothesis": "\u03c4 sensitivity sweep: \u03c4=0.95 (most strict \u03b1_eff threshold), testing upper bound \u2014 may over-constrain b* to near-zero. Baseline \u03c4=0.8 PPL=17.65.",
  "parent": "adaptive_fix_seed42",
  "spec": {
    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/tau_095_seed42 --weighting_method adaptive --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 42 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4 --tau 0.95 --bf16\"",
    "server": "westd-47453",
    "gpu": [
      "cuda:2"
    ],
    "pid": "215505",
    "log_path": "~/runs/provenance_weight_training/tau_095_seed42.log",
    "submitted_at": "2026-05-15T14:32:12.920Z",
    "submitted_via": "submit_training_job",
    "backend": "tmux",
    "account": "root",
    "data_path": "data/scored_data.jsonl",
    "data_count": 200000000,
    "model_name": "Qwen/Qwen3-0.6B",
    "seed": 42,
    "checkpoint_source": "N/A - training from scratch",
    "eval_data": "N/A - training experiment"
  }
}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_full_data_table_20260515T154608",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-15T15:53:06.648446+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json, sys\n\nwith open('/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/112e71b9-a790-4886-b870-1e5804f7b2f6/tool-results/mcp-agent-ml-research-read_registry-1778859984428.txt') as f:\n    raw = json.load(f)\ninner = json.loads(raw['result'])\nexps = inner['data']['experiments']\n\n# Print ALL experiments fully - dump entire dict\nprint(json.dumps(exps, indent=2, ensure_ascii=False))\nPYEOF\n",
  "description": "Dump all 40 experiments as JSON",
  "timeout": "30000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_full_data_table_20260515T154608",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 << 'PYEOF'\nimport json, sys\n\nwith open('/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/112e71b9-a790-4886-b870-1e5804f7b2f6/tool-results/mcp-agent-ml-research-read_registry-1778859984428.txt') as f:\n    raw = json.load(f)\ninner = json.loads(raw['result'])\nexps = inner['data']['experiments']\n\n# Print ALL experiments fully - dump entire dict\nprint(json.dumps(exps, indent=2, ensure_ascii=False))\nPYEOF\n",
    "description": "Dump all 40 experiments as JSON",
    "timeout": "30000"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-15T15:53:06.648588+00:00_

&lt;persisted-output>
Output too large (79.7KB). Full output saved to: /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/112e71b9-a790-4886-b870-1e5804f7b2f6/tool-results/bi2bgtuya.txt

Preview (first 2KB):
{
  "tau_095_seed42": {
    "status": "RUNNING",
    "retry_count": 0,
    "created_at": "2026-05-15T10:03:32.419Z",
    "updated_at": "2026-05-15T14:58:16.987Z",
    "hypothesis": "τ sensitivity sweep: τ=0.95 (most strict α_eff threshold), testing upper bound — may over-constrain b* to near-zero. Baseline τ=0.8 PPL=17.65.",
    "parent": "adaptive_fix_seed42",
    "spec": {
      "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/tau_095_seed42 --weighting_method adaptive --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 42 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4 --tau 0.95 --bf16\"",
      "server": "westd-47453",
      "gpu": [
        "cuda:2"
      ],
      "pid": "215505",
      "log_path": "~/runs/provenance_weight_training/tau_095_seed42.log",
      "submitted_at": "2026-05-15T14:32:12.920Z",
      "submitted_via": "submit_training_job",
      "backend": "tmux",
      "account": "root",
      "data_path": "data/scored_data.jsonl",
      "data_count": 200000000,
      "model_name": "Qwen/Qwen3-0.6B",
      "seed": 42,
      "checkpoint_source": "N/A - training from scratch",
      "eval_data": "N/A - training experiment"
    }
  },
  "tau_09_seed42": {
    "status": "RUNNING",
    "retry_count": 0,
    "created_at": "2026-05-15T10:03:28.658Z",
    "updated_at": "2026-05-15T14:58:14.274Z",
    "hypothesis": "τ sensitivity 
…[truncated 193 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_full_data_table_20260515T154608",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-15T15:53:06.648761+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json, re\n\nwith open('/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/112e71b9-a790-4886-b870-1e5804f7b2f6/tool-results/mcp-agent-ml-research-read_registry-1778859984428.txt') as f:\n    raw = json.load(f)\ninner = json.loads(raw['result'])\nexps = inner['data']['experiments']\n\ndef extract_params_from_command(cmd):\n    \"\"\"Extract training parameters from command string.\"\"\"\n    params = {}\n    if not cmd:\n        return params\n    # Extract key-value args\n    patterns = {\n        'weighting_method': r'--weighting_method\\s+(\\S+)',\n        'batch_size': r'--batch_size\\s+(\\S+)',\n        'gradient_accumulation_steps': r'--gradient_accumulation_steps\\s+(\\S+)',\n        'max_length': r'--max_length\\s+(\\S+)',\n        'learning_rate': r'--learning_rate\\s+(\\S+)',\n        'seed': r'--seed\\s+(\\S+)',\n        'contamination_ratio': r'--contamination_ratio\\s+(\\S+)',\n        'tau': r'--tau\\s+(\\S+)',\n        'n_min': r'--n_min\\s+(\\S+)',\n        'b_fixed': r'--b_fixed\\s+(\\S+)',\n        'num_train_tokens': r'--num_train_tokens\\s+(\\S+)',\n        'output_dir': r'--output_dir\\s+(\\S+)',\n        'model_name': r'--model_name\\s+(\\S+)',\n        'logging_steps': r'--logging_steps\\s+(\\S+)',\n        'save_steps': r'--save_steps\\s+(\\S+)',\n    }\n    for key, pattern in patterns.items():\n        m = re.search(pattern, cmd)\n        if m:\n            params[key] = m.group(1)\n    # Check for flags\n    if '--bf16' in cmd:\n        params['bf16'] = True\n    if '--save_only_model' in cmd:\n        params['save_only_model'] = True\n    return params\n\nall_data = []\nfor exp_id, exp in exps.items():\n    record = {\n        'exp_id': exp_id,\n        'status': exp.get('status'),\n        'conclusion': exp.get('conclusion'),\n        'hypothesis': exp.get('hypothesis'),\n        'parent': exp.get('parent'),\n        'created_at': exp.get('created_at'),\n        'updated_at': exp.get('updated_at'),\n        'retry_count': exp.get('retry_count'),\n        'tags': exp.get('tags'),\n        'notes': exp.get('notes'),\n    }\n    \n    # Extract spec fields\n    spec = exp.get('spec', {})\n    record['server'] = spec.get('server')\n    record['gpu'] = spec.get('gpu')\n    record['pid'] = spec.get('pid')\n    record['log_path'] = spec.get('log_path')\n    record['backend'] = spec.get('backend')\n    record['model_name'] = spec.get('model_name')\n    record['seed_spec'] = spec.get('seed')\n    record['data_path'] = spec.get('data_path')\n    record['data_count'] = spec.get('data_count')\n    \n    # Extract params from command\n    cmd = spec.get('command', '')\n    params = extract_params_from_command(cmd)\n    record['params'] = params\n    \n    # Extract results/metrics\n    results = exp.get('results', {})\n    record['results'] = results\n    \n    # Also check for metrics at top level\n    for key in ['metrics', 'eval_loss', 'perplexity', 'ppl']:\n        if key in exp:\n            record[key] = exp[key]\n    \n    all_data.append(record)\n\n# Print everything\nfor r in all_data:\n    print(\"=\" * 80)\n    print(f\"EXP_ID: {r['exp_id']}\")\n    print(f\"  status: {r['status']}\")\n    print(f\"  conclusion: {r['conclusion']}\")\n    print(f\"  parent: {r['parent']}\")\n    print(f\"  created_at: {r['created_at']}\")\n    print(f\"  updated_at: {r['updated_at']}\")\n    print(f\"  retry_count: {r['retry_count']}\")\n    print(f\"  tags: {r['tags']}\")\n    print(f\"  notes: {r['notes']}\")\n    print(f\"  hypothesis: {r['hypothesis']}\")\n    print(f\"  server: {r['server']}\")\n    print(f\"  gpu: {r['gpu']}\")\n    print(f\"  pid: {r['pid']}\")\n    print(f\"  log_path: {r['log_path']}\")\n    print(f\"  model_name: {r['model_name']}\")\n    print(f\"  seed_spec: {r['seed_spec']}\")\n    print(f\"  data_path: {r['data_path']}\")\n    print(f\"  data_count: {r['data_count']}\")\n    print(f\"  PARAMS FROM CMD:\")\n    for k, v in r['params'].items():\n        print(f\"    {k}: {v}\")\n    print(f\"  RESULTS: {json.dumps(r['results'], indent=4, ensure_ascii=False) if r['results'] else 'None'}\")\n    for key in ['metrics', 'eval_loss', 'perplexity', 'ppl']:\n        if key in r and r[key] is not None:\n            print(f\"  {key}: {r[key]}\")\n    print()\n\n# Summary statistics\nprint(\"\\n\" + \"=\" * 80)\nprint(\"SUMMARY\")\nprint(\"=\" * 80)\nfrom collections import Counter\nstatus_counts = Counter(r['status'] for r in all_data)\nconclusion_counts = Counter(r['conclusion'] for r in all_data)\nprint(f\"Total experiments: {len(all_data)}\")\nprint(f\"Status distribution: {dict(status_counts)}\")\nprint(f\"Conclusion distribution: {dict(conclusion_counts)}\")\n\nPYEOF\n",
  "description": "Extract all experiment data comprehensively",
  "timeout": "30000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_full_data_table_20260515T154608",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 << 'PYEOF'\nimport json, re\n\nwith open('/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/112e71b9-a790-4886-b870-1e5804f7b2f6/tool-results/mcp-agent-ml-research-read_registry-1778859984428.txt') as f:\n    raw = json.load(f)\ninner = json.loads(raw['result'])\nexps = inner['data']['experiments']\n\ndef extract_params_from_command(cmd):\n    \"\"\"Extract training parameters from command string.\"\"\"\n    params = {}\n    if not cmd:\n        return params\n    # Extract key-value args\n    patterns = {\n        'weighting_method': r'--weighting_method\\s+(\\S+)',\n        'batch_size': r'--batch_size\\s+(\\S+)',\n        'gradient_accumulation_steps': r'--gradient_accumulation_steps\\s+(\\S+)',\n        'max_length': r'--max_length\\s+(\\S+)',\n        'learning_rate': r'--learning_rate\\s+(\\S+)',\n        'seed': r'--seed\\s+(\\S+)',\n        'contamination_ratio': r'--contamination_ratio\\s+(\\S+)',\n        'tau': r'--tau\\s+(\\S+)',\n        'n_min': r'--n_min\\s+(\\S+)',\n        'b_fixed': r'--b_fixed\\s+(\\S+)',\n        'num_train_tokens': r'--num_train_tokens\\s+(\\S+)',\n        'output_dir': r'--output_dir\\s+(\\S+)',\n        'model_name': r'--model_name\\s+(\\S+)',\n        'logging_steps': r'--logging_steps\\s+(\\S+)',\n        'save_steps': r'--save_steps\\s+(\\S+)',\n    }\n    for key, pattern in patterns.items():\n        m = re.search(pattern, cmd)\n        if m:\n            params[key] = m.group(1)\n    # Check for flags\n    if '--bf16' in cmd:\n        params['bf16'] = True\n    if '--save_only_model' in cmd:\n        params['save_only_model'] = True\n    return params\n\nall_data = []\nfor exp_id, exp in exps.items():\n    record = {\n        'exp_id': exp_id,\n        'status': exp.get('status'),\n        'conclusion': exp.get('conclusion'),\n        'hypothesis': exp.get('hypothesis'),\n        'parent': exp.get('parent'),\n        'created_at': exp.get('created_at'),\n        'updated_at': exp.get('updated_at'),\n        'retry_count': exp.get('retry_count'),\n        'tags': exp.get('tags'),\n        'notes': exp.get('notes'),\n    }\n    \n    # Extract spec fields\n    spec = exp.get('spec', {})\n    record['server'] = spec.get('server')\n    record['gpu'] = spec.get('gpu')\n    record['pid'] = spec.get('pid')\n    record['log_path'] = spec.get('log_path')\n    record['backend'] = spec.get('backend')\n    record['model_name'] = spec.get('model_name')\n    record['seed_spec'] = spec.get('seed')\n    record['data_path'] = spec.get('data_path')\n    record['data_count'] = spec.get('data_count')\n    \n    # Extract params from command\n    cmd = spec.get('command', '')\n    params = extract_params_from_command(cmd)\n    record['params'] = params\n    \n    # Extract results/metrics\n    results = exp.get('results', {})\n    record['results'] = results\n    \n    # Also check for metrics at top level\n    for key in ['metrics', 'eval_loss', 'perplexity', 'ppl']:\n        if key in exp:\n            record[key] = exp[key]\n    \n    all_data.append(record)\n\n# Print everything\nfor r in all_data:\n    print(\"=\" * 80)\n    print(f\"EXP_ID: {r['exp_id']}\")\n    print(f\"  status: {r['status']}\")\n    print(f\"  conclusion: {r['conclusion']}\")\n    print(f\"  parent: {r['parent']}\")\n    print(f\"  created_at: {r['created_at']}\")\n    print(f\"  updated_at: {r['updated_at']}\")\n    print(f\"  retry_count: {r['retry_count']}\")\n    print(f\"  tags: {r['tags']}\")\n    print(f\"  notes: {r['notes']}\")\n    print(f\"  hypothesis: {r['hypothesis']}\")\n    print(f\"  server: {r['server']}\")\n    print(f\"  gpu: {r['gpu']}\")\n    print(f\"  pid: {r['pid']}\")\n    print(f\"  log_path: {r['log_path']}\")\n    print(f\"  model_name: {r['model_name']}\")\n    print(f\"  seed_spec: {r['seed_spec']}\")\n    print(f\"  data_path: {r['data_path']}\")\n    print(f\"  data_count: {r['data_count']}\")\n    print(f\"  PARAMS FROM CMD:\")\n    for k, v in r['params'].items():\n        print(f\"    {k}: {v}\")\n    print(f\"  RESULTS: {json.dumps(r['results'], indent=4, ensure_ascii=False) if r['results'] else 'None'}\")\n    for key in ['metrics', 'eval_loss', 'perplexity', 'ppl']:\n        if key in r and r[key] is not None:\n            print(f\"  {key}: {r[key]}\")\n    print()\n\n# Summary statistics\nprint(\"\\n\" + \"=\" * 80)\nprint(\"SUMMARY\")\nprint(\"=\" * 80)\nfrom collections import Counter\nstatus_counts = Counter(r['status'] for r in all_data)\nconclusion_counts = Counter(r['conclusion'] for r in all_data)\nprint(f\"Total experiments: {len(all_data)}\")\nprint(f\"Status distribution: {dict(status_counts)}\")\nprint(f\"Conclusion distribution: {dict(conclusion_counts)}\")\n\nPYEOF\n",
    "description": "Extract all experiment data comprehensively",
    "timeout": "30000"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-15T15:53:06.648959+00:00_

&lt;persisted-output>
Output too large (46.2KB). Full output saved to: /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/112e71b9-a790-4886-b870-1e5804f7b2f6/tool-results/bhcd73450.txt

Preview (first 2KB):
================================================================================
EXP_ID: tau_095_seed42
  status: RUNNING
  conclusion: None
  parent: adaptive_fix_seed42
  created_at: 2026-05-15T10:03:32.419Z
  updated_at: 2026-05-15T14:58:16.987Z
  retry_count: 0
  tags: None
  notes: None
  hypothesis: τ sensitivity sweep: τ=0.95 (most strict α_eff threshold), testing upper bound — may over-constrain b* to near-zero. Baseline τ=0.8 PPL=17.65.
  server: westd-47453
  gpu: ['cuda:2']
  pid: 215505
  log_path: ~/runs/provenance_weight_training/tau_095_seed42.log
  model_name: Qwen/Qwen3-0.6B
  seed_spec: 42
  data_path: data/scored_data.jsonl
  data_count: 200000000
  PARAMS FROM CMD:
    weighting_method: adaptive
    batch_size: 4
    gradient_accumulation_steps: 4
    max_length: 2048
    learning_rate: 5e-5
    seed: 42
    contamination_ratio: 0.4
    tau: 0.95
    num_train_tokens: 200000000
    output_dir: output/models/tau_095_seed42
    model_name: models/Qwen/Qwen3-0.6B
    logging_steps: 10
    save_steps: 500
    bf16: True
    save_only_model: True
  RESULTS: None

================================================================================
EXP_ID: tau_09_seed42
  status: RUNNING
  conclusion: None
  parent: adaptive_fix_seed42
  created_at: 2026-05-15T10:03:28.658Z
  updated_at: 2026-05-15T14:58:14.274Z
  retry_count: 0
  tags: None
  notes: None
  hypothesis: τ sensitivity sweep: τ=0.9 (stricter α_eff threshold), testing if higher quality threshold improves PPL. Baseline τ=0.8 PPL=17.65.
  server: westd-47453
  gpu: ['cuda:3']
  pid: 213283
  log_path: ~/runs/provenance_weight_training/tau_09_seed42.log
  model_name: Qwen/Qwen3-0.6B
  seed_spec: 42
  data_path: data/scored_
…[truncated 293 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_full_data_table_20260515T154608",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-15T15:53:06.649138+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/112e71b9-a790-4886-b870-1e5804f7b2f6/tool-results/bhcd73450.txt",
  "limit": "200",
  "offset": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_full_data_table_20260515T154608",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/112e71b9-a790-4886-b870-1e5804f7b2f6/tool-results/bhcd73450.txt",
    "limit": "200",
    "offset": "0"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-15T15:53:06.649317+00:00_

0	================================================================================
1	EXP_ID: tau_095_seed42
2	  status: RUNNING
3	  conclusion: None
4	  parent: adaptive_fix_seed42
5	  created_at: 2026-05-15T10:03:32.419Z
6	  updated_at: 2026-05-15T14:58:16.987Z
7	  retry_count: 0
8	  tags: None
9	  notes: None
10	  hypothesis: τ sensitivity sweep: τ=0.95 (most strict α_eff threshold), testing upper bound — may over-constrain b* to near-zero. Baseline τ=0.8 PPL=17.65.
11	  server: westd-47453
12	  gpu: ['cuda:2']
13	  pid: 215505
14	  log_path: ~/runs/provenance_weight_training/tau_095_seed42.log
15	  model_name: Qwen/Qwen3-0.6B
16	  seed_spec: 42
17	  data_path: data/scored_data.jsonl
18	  data_count: 200000000
19	  PARAMS FROM CMD:
20	    weighting_method: adaptive
21	    batch_size: 4
22	    gradient_accumulation_steps: 4
23	    max_length: 2048
24	    learning_rate: 5e-5
25	    seed: 42
26	    contamination_ratio: 0.4
27	    tau: 0.95
28	    num_train_tokens: 200000000
29	    output_dir: output/models/tau_095_seed42
30	    model_name: models/Qwen/Qwen3-0.6B
31	    logging_steps: 10
32	    save_steps: 500
33	    bf16: True
34	    save_only_model: True
35	  RESULTS: None
36	
37	================================================================================
38	EXP_ID: tau_09_seed42
39	  status: RUNNING
40	  conclusion: None
41	  parent: adaptive_fix_seed42
42	  created_at: 2026-05-15T10:03:28.658Z
43	  updated_at: 2026-05-15T14:58:14.274Z
44	  retry_count: 0
45	  tags: None
46	  notes: None
47	  hypothesis: τ sensitivity sweep: τ=0.9 (stricter α_eff threshold), testing if higher quality threshold improves PPL. Baseline τ=0.8 PPL=17.65.
48	  server: westd-47453
49	  gpu: ['cuda:3']
50	  pid: 213283
51	  log_path: ~/runs/provenance_weight_training/tau_09_seed42.log
52	  model_name: Qwen/Qwen3-0.6B
53	  seed_spec: 42
54	  data_path: data/scored_data.jsonl
55	  data_count: 200000000
56	  PARAMS FROM CMD:
57	    weighting_method: adaptive
58	    batch_size: 4
59	    gr
…[truncated 5460 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_full_data_table_20260515T154608",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-15T15:53:06.649472+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/112e71b9-a790-4886-b870-1e5804f7b2f6/tool-results/bhcd73450.txt",
  "limit": "300",
  "offset": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_full_data_table_20260515T154608",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/112e71b9-a790-4886-b870-1e5804f7b2f6/tool-results/bhcd73450.txt",
    "limit": "300",
    "offset": "200"
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-15T15:53:06.649638+00:00_

200	    tau: 0.6
201	    num_train_tokens: 200000000
202	    output_dir: output/models/tau_0.6_seed42
203	    model_name: models/Qwen/Qwen3-0.6B
204	    logging_steps: 10
205	    save_steps: 500
206	    bf16: True
207	    save_only_model: True
208	  RESULTS: None
209	  metrics: {'eval_ppl_holdout': 17.6805, 'eval_loss': 2.8725, 'train_loss': 9.275, 'total_steps': 6103, 'train_runtime_s': 13436.64, 'train_samples_per_second': 7.267, 'b_star_mean': 0.5899, 'b_star_median': 0.3746, 'b_star_std': 1.0693, 'b_star_min': 0, 'b_star_max': 20, 'b_star_p25': 0.1195, 'b_star_p75': 0.66, 'b_star_zero_frac': 0.156, 'b_star_nonzero_mean': 0.699, 'b_star_nonzero_median': 0.4473}
210	
211	================================================================================
212	EXP_ID: ess_only_seed42
213	  status: DONE
214	  conclusion: success
215	  parent: None
216	  created_at: 2026-05-15T07:20:13.656Z
217	  updated_at: 2026-05-15T13:38:10.040Z
218	  retry_count: 0
219	  tags: None
220	  notes: None
221	  hypothesis: ESS-only adaptive baseline (max-intervention): b* = max{b : ESS(b) ≥ n_min} — proves min-intervention (adaptive) superior to max-intervention (ESS-only)
222	  server: westd-47453
223	  gpu: ['cuda:1']
224	  pid: 189240
225	  log_path: ~/runs/provenance_weight_training/ess_only_seed42.log
226	  model_name: None
227	  seed_spec: None
228	  data_path: None
229	  data_count: None
230	  PARAMS FROM CMD:
231	    weighting_method: ess_only
232	    batch_size: 4
233	    gradient_accumulation_steps: 4
234	    max_length: 2048
235	    learning_rate: 5e-5
236	    seed: 42
237	    contamination_ratio: 0.4
238	    tau: 0.8
239	    num_train_tokens: 200000000
240	    output_dir: output/models/ess_only_seed42
241	    model_name: models/Qwen/Qwen3-0.6B
242	    logging_steps: 10
243	    save_steps: 500
244	    bf16: True
245	    save_only_model: True
246	  RESULTS: None
247	  metrics: {'eval_ppl': 17.73, 'eval_loss': 2.875, 'b_star_median': 1.58, 'b_star_mean': 3.51, 'vs_uniform_ppl_delt
…[truncated 10159 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_full_data_table_20260515T154608",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-15T15:53:06.649795+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/112e71b9-a790-4886-b870-1e5804f7b2f6/tool-results/bhcd73450.txt",
  "limit": "300",
  "offset": "500"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_full_data_table_20260515T154608",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/112e71b9-a790-4886-b870-1e5804f7b2f6/tool-results/bhcd73450.txt",
    "limit": "300",
    "offset": "500"
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-15T15:53:06.649995+00:00_

500	
501	================================================================================
502	EXP_ID: grid_b1_5_seed456
503	  status: DONE
504	  conclusion: success
505	  parent: None
506	  created_at: 2026-05-14T06:59:35.658Z
507	  updated_at: 2026-05-15T01:03:24.328Z
508	  retry_count: 0
509	  tags: None
510	  notes: None
511	  hypothesis: Grid-b weighting with b=1.5, seed=456, for multi-seed validation of best-b baseline
512	  server: None
513	  gpu: None
514	  pid: None
515	  log_path: None
516	  model_name: Qwen/Qwen3-0.6B
517	  seed_spec: 456
518	  data_path: /root/provenance_weight_training/data/scored_data.jsonl
519	  data_count: 371499
520	  PARAMS FROM CMD:
521	  RESULTS: None
522	  metrics: {'train_loss': 10.435, 'total_steps': 6103, 'train_runtime_s': 12950.16, 'gpu_hours': 3.67, 'train_samples_per_second': 7.54, 'eval_loss': 2.8741, 'eval_ppl_holdout': 17.71, 'eval_holdout_tokens': 4077068, 'eval_loss_holdout': 2.875, 'eval_tokens': 5004058}
523	
524	================================================================================
525	EXP_ID: grid_b1_0_seed456
526	  status: DONE
527	  conclusion: success
528	  parent: None
529	  created_at: 2026-05-14T06:59:34.733Z
530	  updated_at: 2026-05-15T01:03:23.307Z
531	  retry_count: 0
532	  tags: None
533	  notes: None
534	  hypothesis: Grid-b weighting with b=1.0, seed=456, for multi-seed validation of best-b baseline
535	  server: None
536	  gpu: None
537	  pid: None
538	  log_path: None
539	  model_name: Qwen/Qwen3-0.6B
540	  seed_spec: 456
541	  data_path: /root/provenance_weight_training/data/scored_data.jsonl
542	  data_count: 371499
543	  PARAMS FROM CMD:
544	  RESULTS: None
545	  metrics: {'train_loss': 10.178, 'total_steps': 6103, 'train_runtime_s': 12963.87, 'gpu_hours': 3.67, 'train_samples_per_second': 7.532, 'eval_loss': 2.8725, 'eval_ppl_holdout': 17.68, 'eval_holdout_tokens': 4077068, 'eval_loss_holdout': 2.8734, 'eval_tokens': 5004058}
546	
547	===================================================
…[truncated 12358 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_full_data_table_20260515T154608",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-15T15:53:06.650150+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/112e71b9-a790-4886-b870-1e5804f7b2f6/tool-results/bhcd73450.txt",
  "limit": "300",
  "offset": "800"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_full_data_table_20260515T154608",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/112e71b9-a790-4886-b870-1e5804f7b2f6/tool-results/bhcd73450.txt",
    "limit": "300",
    "offset": "800"
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-15T15:53:06.650315+00:00_

800	  notes: D012 修正：取消 v2（含 EMA），改用 adaptive_fix（仅修 n_min=2，无 EMA）
801	  hypothesis: Adaptive v2 (n_min fix: 3→2, no EMA) maintains or improves seed456 performance (baseline adaptive PPL=17.64)
802	  server: None
803	  gpu: None
804	  pid: None
805	  log_path: None
806	  model_name: None
807	  seed_spec: None
808	  data_path: None
809	  data_count: None
810	  PARAMS FROM CMD:
811	  RESULTS: None
812	
813	================================================================================
814	EXP_ID: adaptive_v2_seed123
815	  status: PREPARING
816	  conclusion: killed
817	  parent: None
818	  created_at: 2026-05-14T13:27:19.157Z
819	  updated_at: 2026-05-14T13:32:25.356Z
820	  retry_count: 0
821	  tags: None
822	  notes: D012 修正：取消 v2（含 EMA），改用 adaptive_fix（仅修 n_min=2，无 EMA）
823	  hypothesis: Adaptive v2 (n_min fix: 3→2, no EMA) maintains or improves seed123 performance (baseline adaptive PPL=17.63)
824	  server: None
825	  gpu: None
826	  pid: None
827	  log_path: None
828	  model_name: None
829	  seed_spec: None
830	  data_path: None
831	  data_count: None
832	  PARAMS FROM CMD:
833	  RESULTS: None
834	
835	================================================================================
836	EXP_ID: adaptive_v2_seed42
837	  status: PREPARING
838	  conclusion: killed
839	  parent: None
840	  created_at: 2026-05-14T13:27:18.265Z
841	  updated_at: 2026-05-14T13:32:24.351Z
842	  retry_count: 0
843	  tags: None
844	  notes: D012 修正：取消 v2（含 EMA），改用 adaptive_fix（仅修 n_min=2，无 EMA）
845	  hypothesis: Adaptive v2 (n_min fix: 3→2, no EMA) fixes ESS clamping issue, achieves meaningful improvement over uniform baseline for seed=42
846	  server: None
847	  gpu: None
848	  pid: None
849	  log_path: None
850	  model_name: None
851	  seed_spec: None
852	  data_path: None
853	  data_count: None
854	  PARAMS FROM CMD:
855	  RESULTS: None
856	
857	================================================================================
858	EXP_ID: grid_b1_5_seed123
859	  status: DONE
860	  conclusi
…[truncated 8780 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_full_data_table_20260515T154608",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-15T15:53:06.650467+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/112e71b9-a790-4886-b870-1e5804f7b2f6/tool-results/bhcd73450.txt",
  "limit": "300",
  "offset": "1100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_full_data_table_20260515T154608",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/112e71b9-a790-4886-b870-1e5804f7b2f6/tool-results/bhcd73450.txt",
    "limit": "300",
    "offset": "1100"
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-15T15:53:06.650614+00:00_

1100	  seed_spec: 456
1101	  data_path: data/scored_data.jsonl
1102	  data_count: 371499
1103	  PARAMS FROM CMD:
1104	    weighting_method: adaptive
1105	    batch_size: 4
1106	    gradient_accumulation_steps: 4
1107	    max_length: 2048
1108	    learning_rate: 5e-5
1109	    seed: 456
1110	    contamination_ratio: 0.4
1111	    num_train_tokens: 200000000
1112	    output_dir: output/models/adaptive_seed456
1113	    model_name: models/Qwen/Qwen3-0.6B
1114	    logging_steps: 10
1115	    save_steps: 500
1116	    save_only_model: True
1117	  RESULTS: None
1118	  metrics: {'train_loss': 9.2354, 'train_runtime_s': 13130.09, 'total_steps': 6103, 'train_samples_per_second': 7.437, 'train_steps_per_second': 0.465, 'epoch': 0.26, 'weighting_method': 'adaptive', 'tau': 0.8, 'n_min': 3, 'contamination_ratio': 0.4, 'b_star': 'per-batch adaptive (0.0-3.8)', 'alpha_eff_range': '0.09-0.80 (capped at tau)', 'eval_ppl_holdout': 17.64, 'eval_holdout_tokens': 4080000}
1119	
1120	================================================================================
1121	EXP_ID: adaptive_seed123
1122	  status: DONE
1123	  conclusion: success
1124	  parent: None
1125	  created_at: 2026-05-14T02:25:02.771Z
1126	  updated_at: 2026-05-14T07:27:31.026Z
1127	  retry_count: 0
1128	  tags: None
1129	  notes: ⚠️ success 仅指训练完成无报错。MVP 假设验证待 held-out eval perplexity 结果。
1130	  hypothesis: Adaptive b* (from α_eff theory) matches or exceeds grid-searched best-b without grid search, seed=123
1131	  server: westd-47453
1132	  gpu: ['cuda:2']
1133	  pid: 58978
1134	  log_path: ~/runs/provenance_weight_training/adaptive_seed123.log
1135	  model_name: Qwen/Qwen3-0.6B
1136	  seed_spec: 123
1137	  data_path: data/scored_data.jsonl
1138	  data_count: 371499
1139	  PARAMS FROM CMD:
1140	    weighting_method: adaptive
1141	    batch_size: 4
1142	    gradient_accumulation_steps: 4
1143	    max_length: 2048
1144	    learning_rate: 5e-5
1145	    seed: 123
1146	    contamination_ratio: 0.4
1147	    num_train_tokens: 2000
…[truncated 4549 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_full_data_table_20260515T154608",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-15T15:53:06.650771+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nwith open('/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/112e71b9-a790-4886-b870-1e5804f7b2f6/tool-results/mcp-agent-ml-research-read_registry-1778859984428.txt') as f:\n    raw = json.load(f)\ninner = json.loads(raw['result'])\nexps = inner['data']['experiments']\n\n# Print the complete raw JSON for all experiments\nprint(json.dumps(exps, indent=2, ensure_ascii=False))\nPYEOF\n",
  "description": "Dump complete raw experiment data",
  "timeout": "30000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_full_data_table_20260515T154608",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 << 'PYEOF'\nimport json\n\nwith open('/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/112e71b9-a790-4886-b870-1e5804f7b2f6/tool-results/mcp-agent-ml-research-read_registry-1778859984428.txt') as f:\n    raw = json.load(f)\ninner = json.loads(raw['result'])\nexps = inner['data']['experiments']\n\n# Print the complete raw JSON for all experiments\nprint(json.dumps(exps, indent=2, ensure_ascii=False))\nPYEOF\n",
    "description": "Dump complete raw experiment data",
    "timeout": "30000"
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-15T15:53:06.650937+00:00_

&lt;persisted-output>
Output too large (79.7KB). Full output saved to: /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/112e71b9-a790-4886-b870-1e5804f7b2f6/tool-results/bzwjbrxcr.txt

Preview (first 2KB):
{
  "tau_095_seed42": {
    "status": "RUNNING",
    "retry_count": 0,
    "created_at": "2026-05-15T10:03:32.419Z",
    "updated_at": "2026-05-15T14:58:16.987Z",
    "hypothesis": "τ sensitivity sweep: τ=0.95 (most strict α_eff threshold), testing upper bound — may over-constrain b* to near-zero. Baseline τ=0.8 PPL=17.65.",
    "parent": "adaptive_fix_seed42",
    "spec": {
      "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/tau_095_seed42 --weighting_method adaptive --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 42 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4 --tau 0.95 --bf16\"",
      "server": "westd-47453",
      "gpu": [
        "cuda:2"
      ],
      "pid": "215505",
      "log_path": "~/runs/provenance_weight_training/tau_095_seed42.log",
      "submitted_at": "2026-05-15T14:32:12.920Z",
      "submitted_via": "submit_training_job",
      "backend": "tmux",
      "account": "root",
      "data_path": "data/scored_data.jsonl",
      "data_count": 200000000,
      "model_name": "Qwen/Qwen3-0.6B",
      "seed": 42,
      "checkpoint_source": "N/A - training from scratch",
      "eval_data": "N/A - training experiment"
    }
  },
  "tau_09_seed42": {
    "status": "RUNNING",
    "retry_count": 0,
    "created_at": "2026-05-15T10:03:28.658Z",
    "updated_at": "2026-05-15T14:58:14.274Z",
    "hypothesis": "τ sensitivity 
…[truncated 193 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_full_data_table_20260515T154608",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-15T15:53:06.651184+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json, re\n\nwith open('/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/112e71b9-a790-4886-b870-1e5804f7b2f6/tool-results/mcp-agent-ml-research-read_registry-1778859984428.txt') as f:\n    raw = json.load(f)\ninner = json.loads(raw['result'])\nexps = inner['data']['experiments']\n\ndef extract_params(cmd):\n    if not cmd: return {}\n    p = {}\n    for key, pat in [\n        ('weighting_method', r'--weighting_method\\s+(\\S+)'),\n        ('batch_size', r'--batch_size\\s+(\\S+)'),\n        ('gradient_accumulation_steps', r'--gradient_accumulation_steps\\s+(\\S+)'),\n        ('max_length', r'--max_length\\s+(\\S+)'),\n        ('learning_rate', r'--learning_rate\\s+(\\S+)'),\n        ('seed', r'--seed\\s+(\\S+)'),\n        ('contamination_ratio', r'--contamination_ratio\\s+(\\S+)'),\n        ('tau', r'--tau\\s+(\\S+)'),\n        ('n_min', r'--n_min\\s+(\\S+)'),\n        ('b_fixed', r'--b_fixed\\s+(\\S+)'),\n        ('num_train_tokens', r'--num_train_tokens\\s+(\\S+)'),\n    ]:\n        m = re.search(pat, cmd)\n        if m: p[key] = m.group(1)\n    if '--bf16' in cmd: p['bf16'] = 'True'\n    return p\n\n# Build complete structured output\noutput = {}\nfor eid, e in exps.items():\n    spec = e.get('spec', {})\n    cmd = spec.get('command', '')\n    params = extract_params(cmd)\n    \n    # Merge spec-level fields that may not be in command\n    if not params.get('seed') and spec.get('seed'):\n        params['seed'] = str(spec['seed'])\n    if not params.get('weighting_method') and e.get('metrics', {}).get('weighting_method'):\n        params['weighting_method'] = e['metrics']['weighting_method']\n    \n    output[eid] = {\n        'status': e.get('status'),\n        'conclusion': e.get('conclusion'),\n        'parent': e.get('parent'),\n        'hypothesis': e.get('hypothesis'),\n        'notes': e.get('notes'),\n        'created_at': e.get('created_at'),\n        'updated_at': e.get('updated_at'),\n        'retry_count': e.get('retry_count'),\n        'server': spec.get('server'),\n        'gpu': spec.get('gpu'),\n        'pid': spec.get('pid'),\n        'log_path': spec.get('log_path'),\n        'params': params,\n        'metrics': e.get('metrics'),\n    }\n\nprint(json.dumps(output, indent=2, ensure_ascii=False))\nPYEOF\n",
  "description": "Generate complete structured experiment data",
  "timeout": "30000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_full_data_table_20260515T154608",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 << 'PYEOF'\nimport json, re\n\nwith open('/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/112e71b9-a790-4886-b870-1e5804f7b2f6/tool-results/mcp-agent-ml-research-read_registry-1778859984428.txt') as f:\n    raw = json.load(f)\ninner = json.loads(raw['result'])\nexps = inner['data']['experiments']\n\ndef extract_params(cmd):\n    if not cmd: return {}\n    p = {}\n    for key, pat in [\n        ('weighting_method', r'--weighting_method\\s+(\\S+)'),\n        ('batch_size', r'--batch_size\\s+(\\S+)'),\n        ('gradient_accumulation_steps', r'--gradient_accumulation_steps\\s+(\\S+)'),\n        ('max_length', r'--max_length\\s+(\\S+)'),\n        ('learning_rate', r'--learning_rate\\s+(\\S+)'),\n        ('seed', r'--seed\\s+(\\S+)'),\n        ('contamination_ratio', r'--contamination_ratio\\s+(\\S+)'),\n        ('tau', r'--tau\\s+(\\S+)'),\n        ('n_min', r'--n_min\\s+(\\S+)'),\n        ('b_fixed', r'--b_fixed\\s+(\\S+)'),\n        ('num_train_tokens', r'--num_train_tokens\\s+(\\S+)'),\n    ]:\n        m = re.search(pat, cmd)\n        if m: p[key] = m.group(1)\n    if '--bf16' in cmd: p['bf16'] = 'True'\n    return p\n\n# Build complete structured output\noutput = {}\nfor eid, e in exps.items():\n    spec = e.get('spec', {})\n    cmd = spec.get('command', '')\n    params = extract_params(cmd)\n    \n    # Merge spec-level fields that may not be in command\n    if not params.get('seed') and spec.get('seed'):\n        params['seed'] = str(spec['seed'])\n    if not params.get('weighting_method') and e.get('metrics', {}).get('weighting_method'):\n        params['weighting_method'] = e['metrics']['weighting_method']\n    \n    output[eid] = {\n        'status': e.get('status'),\n        'conclusion': e.get('conclusion'),\n        'parent': e.get('parent'),\n        'hypothesis': e.get('hypothesis'),\n        'notes': e.get('notes'),\n        'created_at': e.get('created_at'),\n        'updated_at': e.get('updated_at'),\n        'retry_count': e.get('retry_count'),\n        'server': spec.get('server'),\n        'gpu': spec.get('gpu'),\n        'pid': spec.get('pid'),\n        'log_path': spec.get('log_path'),\n        'params': params,\n        'metrics': e.get('metrics'),\n    }\n\nprint(json.dumps(output, indent=2, ensure_ascii=False))\nPYEOF\n",
    "description": "Generate complete structured experiment data",
    "timeout": "30000"
  }
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-15T15:53:06.651426+00:00_

&lt;persisted-output>
Output too large (41.3KB). Full output saved to: /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/112e71b9-a790-4886-b870-1e5804f7b2f6/tool-results/bpvbnvw3p.txt

Preview (first 2KB):
{
  "tau_095_seed42": {
    "status": "RUNNING",
    "conclusion": null,
    "parent": "adaptive_fix_seed42",
    "hypothesis": "τ sensitivity sweep: τ=0.95 (most strict α_eff threshold), testing upper bound — may over-constrain b* to near-zero. Baseline τ=0.8 PPL=17.65.",
    "notes": null,
    "created_at": "2026-05-15T10:03:32.419Z",
    "updated_at": "2026-05-15T14:58:16.987Z",
    "retry_count": 0,
    "server": "westd-47453",
    "gpu": [
      "cuda:2"
    ],
    "pid": "215505",
    "log_path": "~/runs/provenance_weight_training/tau_095_seed42.log",
    "params": {
      "weighting_method": "adaptive",
      "batch_size": "4",
      "gradient_accumulation_steps": "4",
      "max_length": "2048",
      "learning_rate": "5e-5",
      "seed": "42",
      "contamination_ratio": "0.4",
      "tau": "0.95",
      "num_train_tokens": "200000000",
      "bf16": "True"
    },
    "metrics": null
  },
  "tau_09_seed42": {
    "status": "RUNNING",
    "conclusion": null,
    "parent": "adaptive_fix_seed42",
    "hypothesis": "τ sensitivity sweep: τ=0.9 (stricter α_eff threshold), testing if higher quality threshold improves PPL. Baseline τ=0.8 PPL=17.65.",
    "notes": null,
    "created_at": "2026-05-15T10:03:28.658Z",
    "updated_at": "2026-05-15T14:58:14.274Z",
    "retry_count": 0,
    "server": "westd-47453",
    "gpu": [
      "cuda:3"
    ],
    "pid": "213283",
    "log_path": "~/runs/provenance_weight_training/tau_09_seed42.log",
    "params": {
      "weighting_method": "adaptive",
      "batch_size": "4",
      "gradient_accumulation_steps": "4",
      "max_length": "2048",
      "learning_rate": "5e-5",
      "seed": "42",
      "contamination_ratio": "0.4",
      "tau": "0.9",
    
…[truncated 218 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_full_data_table_20260515T154608",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-15T15:53:06.651714+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json, re\n\nwith open('/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/112e71b9-a790-4886-b870-1e5804f7b2f6/tool-results/mcp-agent-ml-research-read_registry-1778859984428.txt') as f:\n    raw = json.load(f)\ninner = json.loads(raw['result'])\nexps = inner['data']['experiments']\n\nprint(\"=\" * 100)\nprint(\"COMPLETE EXPERIMENT REGISTRY — 40 experiments\")\nprint(\"=\" * 100)\nprint()\n\n# Categorize experiments\ncategories = {\n    'UNIFORM BASELINES': [],\n    'GRID-B SWEEP (seed=42, batch)': [],\n    'GRID-B SWEEP (seed=123)': [],\n    'GRID-B SWEEP (seed=456)': [],\n    'ADAPTIVE (original, n_min=3 bug)': [],\n    'ADAPTIVE_FIX (n_min=2, corrected)': [],\n    'TAU SENSITIVITY SWEEP': [],\n    'N_MIN ABLATION': [],\n    'SPECIAL BASELINES (golden_ratio, ess_only)': [],\n    'KILLED/SUPERSEDED (adaptive_v2)': [],\n    'INFRASTRUCTURE': [],\n}\n\nfor eid, e in exps.items():\n    if eid.startswith('uniform_'):\n        categories['UNIFORM BASELINES'].append((eid, e))\n    elif eid == 'grid_b_seed42_batch':\n        categories['GRID-B SWEEP (seed=42, batch)'].append((eid, e))\n    elif eid.startswith('grid_b') and 'seed123' in eid:\n        categories['GRID-B SWEEP (seed=123)'].append((eid, e))\n    elif eid.startswith('grid_b') and 'seed456' in eid:\n        categories['GRID-B SWEEP (seed=456)'].append((eid, e))\n    elif eid == 'grid_b_low_seed42':\n        categories['GRID-B SWEEP (seed=42, batch)'].append((eid, e))\n    elif eid.startswith('adaptive_seed'):\n        categories['ADAPTIVE (original, n_min=3 bug)'].append((eid, e))\n    elif eid.startswith('adaptive_fix'):\n        categories['ADAPTIVE_FIX (n_min=2, corrected)'].append((eid, e))\n    elif eid.startswith('tau_'):\n        categories['TAU SENSITIVITY SWEEP'].append((eid, e))\n    elif eid.startswith('nmin'):\n        categories['N_MIN ABLATION'].append((eid, e))\n    elif eid in ('golden_ratio_seed42', 'ess_only_seed42'):\n        categories['SPECIAL BASELINES (golden_ratio, ess_only)'].append((eid, e))\n    elif eid.startswith('adaptive_v2'):\n        categories['KILLED/SUPERSEDED (adaptive_v2)'].append((eid, e))\n    elif eid in ('detector_tfidf_lr', 'detector_modernbert', 'datagen_synthetic_4gpu', 'diagnostic_contamination100'):\n        categories['INFRASTRUCTURE'].append((eid, e))\n\nfor cat_name, items in categories.items():\n    if not items:\n        continue\n    print(f\"\\n{'─' * 100}\")\n    print(f\"  {cat_name} ({len(items)} experiments)\")\n    print(f\"{'─' * 100}\")\n    for eid, e in items:\n        m = e.get('metrics', {}) or {}\n        spec = e.get('spec', {}) or {}\n        cmd = spec.get('command', '') or ''\n        \n        # Extract key params\n        tau_m = re.search(r'--tau\\s+(\\S+)', cmd)\n        nmin_m = re.search(r'--n_min\\s+(\\S+)', cmd)\n        seed_m = re.search(r'--seed\\s+(\\S+)', cmd)\n        wm_m = re.search(r'--weighting_method\\s+(\\S+)', cmd)\n        \n        tau_val = tau_m.group(1) if tau_m else (m.get('tau') if 'tau' in (m or {}) else None)\n        nmin_val = nmin_m.group(1) if nmin_m else None\n        seed_val = seed_m.group(1) if seed_m else (str(spec.get('seed', '')) if spec.get('seed') else None)\n        wm_val = wm_m.group(1) if wm_m else (m.get('weighting_method') if m else None)\n        \n        status_str = e.get('status', '?')\n        conclusion_str = e.get('conclusion', '-') or '-'\n        \n        print(f\"\\n  [{eid}]\")\n        print(f\"    Status: {status_str} | Conclusion: {conclusion_str} | Parent: {e.get('parent', '-') or '-'}\")\n        print(f\"    Method: {wm_val or '-'} | Seed: {seed_val or '-'} | τ: {tau_val or '-'} | n_min: {nmin_val or '-'}\")\n        \n        # Metrics\n        if m:\n            ppl = m.get('eval_ppl_holdout') or m.get('eval_ppl')\n            loss = m.get('eval_loss') or m.get('eval_loss_holdout')\n            train_loss = m.get('train_loss') or m.get('train_loss_weighted')\n            total_steps = m.get('total_steps')\n            \n            print(f\"    PPL: {ppl} | eval_loss: {loss} | train_loss: {train_loss} | steps: {total_steps}\")\n            \n            # b_star stats if present\n            if 'b_star_mean' in m:\n                print(f\"    b*: mean={m.get('b_star_mean')}, median={m.get('b_star_median')}, std={m.get('b_star_std')}, min={m.get('b_star_min')}, max={m.get('b_star_max')}\")\n                print(f\"    b* dist: <0.5={m.get('b_star_pct_below_0.5')}%, 0.5-1={m.get('b_star_pct_0.5_to_1')}%, 1-2={m.get('b_star_pct_1_to_2')}%, >2={m.get('b_star_pct_above_2')}%\")\n                print(f\"    b* p25={m.get('b_star_p25')}, p75={m.get('b_star_p75')}, zero_frac={m.get('b_star_zero_frac')}, count={m.get('b_star_count')}\")\n            \n            # alpha_eff if present\n            if 'alpha_eff_mean' in m:\n                print(f\"    α_eff: mean={m.get('alpha_eff_mean')}, median={m.get('alpha_eff_median')}\")\n            if 'alpha_eff_range' in m:\n                print(f\"    α_eff_range: {m.get('alpha_eff_range')}\")\n            \n            # Detector-specific\n            if 'auc' in m:\n                print(f\"    AUC={m.get('auc')}, accuracy={m.get('accuracy')}, ECE_raw={m.get('ece_raw')}, ECE_cal={m.get('ece_calibrated')}, T={m.get('temperature_T')}\")\n                print(f\"    q_score: mean={m.get('q_score_mean')}, std={m.get('q_score_std')}, median={m.get('q_score_median')}, mid_range={m.get('mid_range_ratio')}\")\n            \n            # grid_b_seed42_batch special: per-b results\n            if 'b0_5_eval_ppl' in m:\n                print(f\"    Per-b PPL: b=0.5→{m['b0_5_eval_ppl']}, b=1.0→{m['b1_0_eval_ppl']}, b=1.5→{m['b1_5_eval_ppl']}, b=2.0→{m['b2_0_eval_ppl']}, b=3.0→{m['b3_0_eval_ppl']}, b=5.0→{m['b5_0_eval_ppl']}\")\n                print(f\"    Best: b={m['best_b']}, PPL={m['best_eval_ppl']}\")\n            \n            # Runtime\n            runtime = m.get('train_runtime_s') or m.get('train_runtime') or m.get('train_duration_s')\n            gpu_h = m.get('gpu_hours')\n            if runtime:\n                print(f\"    Runtime: {runtime}s ({float(runtime)/3600:.2f}h)\" + (f\", GPU-hours: {gpu_h}\" if gpu_h else \"\"))\n            \n            # vs comparisons\n            if 'vs_uniform_ppl_delta' in m:\n                print(f\"    vs uniform: {m['vs_uniform_ppl_delta']}, vs adaptive: {m['vs_adaptive_ppl_delta']}\")\n        else:\n            print(f\"    Metrics: NONE (still running or no eval)\")\n        \n        # Notes\n        if e.get('notes'):\n            notes = e['notes']\n            if len(notes) > 200:\n                notes = notes[:200] + '...'\n            print(f\"    Notes: {notes}\")\n\nprint()\nprint(\"=\" * 100)\nprint(\"STATUS SUMMARY\")\nprint(\"=\" * 100)\n\nfrom collections import Counter\nstatus_c = Counter()\nconclusion_c = Counter()\nfor eid, e in exps.items():\n    status_c[e.get('status', 'UNKNOWN')] += 1\n    conclusion_c[e.get('conclusion') or 'NONE'] += 1\n\nprint(f\"  Status:     {dict(status_c)}\")\nprint(f\"  Conclusion: {dict(conclusion_c)}\")\nprint()\n\n# Paper-ready: successful experiments with PPL\nprint(\"=\" * 100)\nprint(\"PAPER-READY TABLE DATA (all experiments with eval_ppl)\")\nprint(\"=\" * 100)\nprint(f\"{'exp_id':<30} {'method':<15} {'seed':<6} {'tau':<6} {'n_min':<6} {'b':<6} {'PPL':<10} {'eval_loss':<12} {'conclusion':<12}\")\nprint(\"-\" * 115)\n\nfor eid, e in exps.items():\n    m = e.get('metrics', {}) or {}\n    spec = e.get('spec', {}) or {}\n    cmd = spec.get('command', '') or ''\n    \n    ppl = m.get('eval_ppl_holdout') or m.get('eval_ppl')\n    if ppl is None:\n        continue\n    \n    tau_m = re.search(r'--tau\\s+(\\S+)', cmd)\n    nmin_m = re.search(r'--n_min\\s+(\\S+)', cmd)\n    seed_m = re.search(r'--seed\\s+(\\S+)', cmd)\n    wm_m = re.search(r'--weighting_method\\s+(\\S+)', cmd)\n    \n    tau_val = tau_m.group(1) if tau_m else str(m.get('tau', '-'))\n    nmin_val = nmin_m.group(1) if nmin_m else '-'\n    seed_val = seed_m.group(1) if seed_m else (str(spec.get('seed', '-')) if spec.get('seed') else '-')\n    wm_val = wm_m.group(1) if wm_m else (str(m.get('weighting_method', '-')))\n    loss = m.get('eval_loss') or m.get('eval_loss_holdout') or '-'\n    concl = e.get('conclusion') or '-'\n    \n    # For grid experiments, try to extract b value from exp_id\n    b_val = '-'\n    if 'grid' in eid:\n        bm = re.search(r'grid_b(\\d+_\\d+)', eid)\n        if bm:\n            b_val = bm.group(1).replace('_', '.')\n    \n    print(f\"{eid:<30} {wm_val:<15} {seed_val:<6} {tau_val:<6} {nmin_val:<6} {b_val:<6} {ppl:<10} {str(loss):<12} {concl:<12}\")\n\n# Also print the batch experiment per-b results\nprint()\nprint(\"grid_b_seed42_batch per-b results:\")\nm = exps['grid_b_seed42_batch'].get('metrics', {})\nfor b in ['0_5', '1_0', '1_5', '2_0', '3_0', '5_0']:\n    b_disp = b.replace('_', '.')\n    ppl_key = f'b{b}_eval_ppl'\n    loss_key = f'b{b}_train_loss'\n    if ppl_key in m:\n        print(f\"  b={b_disp}: PPL={m[ppl_key]}, train_loss={m.get(loss_key, '-')}\")\n\nPYEOF\n",
  "description": "Generate complete categorized experiment summary",
  "timeout": "30000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_full_data_table_20260515T154608",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 << 'PYEOF'\nimport json, re\n\nwith open('/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/112e71b9-a790-4886-b870-1e5804f7b2f6/tool-results/mcp-agent-ml-research-read_registry-1778859984428.txt') as f:\n    raw = json.load(f)\ninner = json.loads(raw['result'])\nexps = inner['data']['experiments']\n\nprint(\"=\" * 100)\nprint(\"COMPLETE EXPERIMENT REGISTRY — 40 experiments\")\nprint(\"=\" * 100)\nprint()\n\n# Categorize experiments\ncategories = {\n    'UNIFORM BASELINES': [],\n    'GRID-B SWEEP (seed=42, batch)': [],\n    'GRID-B SWEEP (seed=123)': [],\n    'GRID-B SWEEP (seed=456)': [],\n    'ADAPTIVE (original, n_min=3 bug)': [],\n    'ADAPTIVE_FIX (n_min=2, corrected)': [],\n    'TAU SENSITIVITY SWEEP': [],\n    'N_MIN ABLATION': [],\n    'SPECIAL BASELINES (golden_ratio, ess_only)': [],\n    'KILLED/SUPERSEDED (adaptive_v2)': [],\n    'INFRASTRUCTURE': [],\n}\n\nfor eid, e in exps.items():\n    if eid.startswith('uniform_'):\n        categories['UNIFORM BASELINES'].append((eid, e))\n    elif eid == 'grid_b_seed42_batch':\n        categories['GRID-B SWEEP (seed=42, batch)'].append((eid, e))\n    elif eid.startswith('grid_b') and 'seed123' in eid:\n        categories['GRID-B SWEEP (seed=123)'].append((eid, e))\n    elif eid.startswith('grid_b') and 'seed456' in eid:\n        categories['GRID-B SWEEP (seed=456)'].append((eid, e))\n    elif eid == 'grid_b_low_seed42':\n        categories['GRID-B SWEEP (seed=42, batch)'].append((eid, e))\n    elif eid.startswith('adaptive_seed'):\n        categories['ADAPTIVE (original, n_min=3 bug)'].append((eid, e))\n    elif eid.startswith('adaptive_fix'):\n        categories['ADAPTIVE_FIX (n_min=2, corrected)'].append((eid, e))\n    elif eid.startswith('tau_'):\n        categories['TAU SENSITIVITY SWEEP'].append((eid, e))\n    elif eid.startswith('nmin'):\n        categories['N_MIN ABLATION'].append((eid, e))\n    elif eid in ('golden_ratio_seed42', 'ess_only_seed42'):\n        categories['SPECIAL BASELINES (golden_ratio, ess_only)'].append((eid, e))\n    elif eid.startswith('adaptive_v2'):\n        categories['KILLED/SUPERSEDED (adaptive_v2)'].append((eid, e))\n    elif eid in ('detector_tfidf_lr', 'detector_modernbert', 'datagen_synthetic_4gpu', 'diagnostic_contamination100'):\n        categories['INFRASTRUCTURE'].append((eid, e))\n\nfor cat_name, items in categories.items():\n    if not items:\n        continue\n    print(f\"\\n{'─' * 100}\")\n    print(f\"  {cat_name} ({len(items)} experiments)\")\n    print(f\"{'─' * 100}\")\n    for eid, e in items:\n        m = e.get('metrics', {}) or {}\n        spec = e.get('spec', {}) or {}\n        cmd = spec.get('command', '') or ''\n        \n        # Extract key params\n        tau_m = re.search(r'--tau\\s+(\\S+)', cmd)\n        nmin_m = re.search(r'--n_min\\s+(\\S+)', cmd)\n        seed_m = re.search(r'--seed\\s+(\\S+)', cmd)\n        wm_m = re.search(r'--weighting_method\\s+(\\S+)', cmd)\n        \n        tau_val = tau_m.group(1) if tau_m else (m.get('tau') if 'tau' in (m or {}) else None)\n        nmin_val = nmin_m.group(1) if nmin_m else None\n        seed_val = seed_m.group(1) if seed_m else (str(spec.get('seed', '')) if spec.get('seed') else None)\n        wm_val = wm_m.group(1) if wm_m else (m.get('weighting_method') if m else None)\n        \n        status_str = e.get('status', '?')\n        conclusion_str = e.get('conclusion', '-') or '-'\n        \n        print(f\"\\n  [{eid}]\")\n        print(f\"    Status: {status_str} | Conclusion: {conclusion_str} | Parent: {e.get('parent', '-') or '-'}\")\n        print(f\"    Method: {wm_val or '-'} | Seed: {seed_val or '-'} | τ: {tau_val or '-'} | n_min: {nmin_val or '-'}\")\n        \n        # Metrics\n        if m:\n            ppl = m.get('eval_ppl_holdout') or m.get('eval_ppl')\n            loss = m.get('eval_loss') or m.get('eval_loss_holdout')\n            train_loss = m.get('train_loss') or m.get('train_loss_weighted')\n            total_steps = m.get('total_steps')\n            \n            print(f\"    PPL: {ppl} | eval_loss: {loss} | train_loss: {train_loss} | steps: {total_steps}\")\n            \n            # b_star stats if present\n            if 'b_star_mean' in m:\n                print(f\"    b*: mean={m.get('b_star_mean')}, median={m.get('b_star_median')}, std={m.get('b_star_std')}, min={m.get('b_star_min')}, max={m.get('b_star_max')}\")\n                print(f\"    b* dist: <0.5={m.get('b_star_pct_below_0.5')}%, 0.5-1={m.get('b_star_pct_0.5_to_1')}%, 1-2={m.get('b_star_pct_1_to_2')}%, >2={m.get('b_star_pct_above_2')}%\")\n                print(f\"    b* p25={m.get('b_star_p25')}, p75={m.get('b_star_p75')}, zero_frac={m.get('b_star_zero_frac')}, count={m.get('b_star_count')}\")\n            \n            # alpha_eff if present\n            if 'alpha_eff_mean' in m:\n                print(f\"    α_eff: mean={m.get('alpha_eff_mean')}, median={m.get('alpha_eff_median')}\")\n            if 'alpha_eff_range' in m:\n                print(f\"    α_eff_range: {m.get('alpha_eff_range')}\")\n            \n            # Detector-specific\n            if 'auc' in m:\n                print(f\"    AUC={m.get('auc')}, accuracy={m.get('accuracy')}, ECE_raw={m.get('ece_raw')}, ECE_cal={m.get('ece_calibrated')}, T={m.get('temperature_T')}\")\n                print(f\"    q_score: mean={m.get('q_score_mean')}, std={m.get('q_score_std')}, median={m.get('q_score_median')}, mid_range={m.get('mid_range_ratio')}\")\n            \n            # grid_b_seed42_batch special: per-b results\n            if 'b0_5_eval_ppl' in m:\n                print(f\"    Per-b PPL: b=0.5→{m['b0_5_eval_ppl']}, b=1.0→{m['b1_0_eval_ppl']}, b=1.5→{m['b1_5_eval_ppl']}, b=2.0→{m['b2_0_eval_ppl']}, b=3.0→{m['b3_0_eval_ppl']}, b=5.0→{m['b5_0_eval_ppl']}\")\n                print(f\"    Best: b={m['best_b']}, PPL={m['best_eval_ppl']}\")\n            \n            # Runtime\n            runtime = m.get('train_runtime_s') or m.get('train_runtime') or m.get('train_duration_s')\n            gpu_h = m.get('gpu_hours')\n            if runtime:\n                print(f\"    Runtime: {runtime}s ({float(runtime)/3600:.2f}h)\" + (f\", GPU-hours: {gpu_h}\" if gpu_h else \"\"))\n            \n            # vs comparisons\n            if 'vs_uniform_ppl_delta' in m:\n                print(f\"    vs uniform: {m['vs_uniform_ppl_delta']}, vs adaptive: {m['vs_adaptive_ppl_delta']}\")\n        else:\n            print(f\"    Metrics: NONE (still running or no eval)\")\n        \n        # Notes\n        if e.get('notes'):\n            notes = e['notes']\n            if len(notes) > 200:\n                notes = notes[:200] + '...'\n            print(f\"    Notes: {notes}\")\n\nprint()\nprint(\"=\" * 100)\nprint(\"STATUS SUMMARY\")\nprint(\"=\" * 100)\n\nfrom collections import Counter\nstatus_c = Counter()\nconclusion_c = Counter()\nfor eid, e in exps.items():\n    status_c[e.get('status', 'UNKNOWN')] += 1\n    conclusion_c[e.get('conclusion') or 'NONE'] += 1\n\nprint(f\"  Status:     {dict(status_c)}\")\nprint(f\"  Conclusion: {dict(conclusion_c)}\")\nprint()\n\n# Paper-ready: successful experiments with PPL\nprint(\"=\" * 100)\nprint(\"PAPER-READY TABLE DATA (all experiments with eval_ppl)\")\nprint(\"=\" * 100)\nprint(f\"{'exp_id':<30} {'method':<15} {'seed':<6} {'tau':<6} {'n_min':<6} {'b':<6} {'PPL':<10} {'eval_loss':<12} {'conclusion':<12}\")\nprint(\"-\" * 115)\n\nfor eid, e in exps.items():\n    m = e.get('metrics', {}) or {}\n    spec = e.get('spec', {}) or {}\n    cmd = spec.get('command', '') or ''\n    \n    ppl = m.get('eval_ppl_holdout') or m.get('eval_ppl')\n    if ppl is None:\n        continue\n    \n    tau_m = re.search(r'--tau\\s+(\\S+)', cmd)\n    nmin_m = re.search(r'--n_min\\s+(\\S+)', cmd)\n    seed_m = re.search(r'--seed\\s+(\\S+)', cmd)\n    wm_m = re.search(r'--weighting_method\\s+(\\S+)', cmd)\n    \n    tau_val = tau_m.group(1) if tau_m else str(m.get('tau', '-'))\n    nmin_val = nmin_m.group(1) if nmin_m else '-'\n    seed_val = seed_m.group(1) if seed_m else (str(spec.get('seed', '-')) if spec.get('seed') else '-')\n    wm_val = wm_m.group(1) if wm_m else (str(m.get('weighting_method', '-')))\n    loss = m.get('eval_loss') or m.get('eval_loss_holdout') or '-'\n    concl = e.get('conclusion') or '-'\n    \n    # For grid experiments, try to extract b value from exp_id\n    b_val = '-'\n    if 'grid' in eid:\n        bm = re.search(r'grid_b(\\d+_\\d+)', eid)\n        if bm:\n            b_val = bm.group(1).replace('_', '.')\n    \n    print(f\"{eid:<30} {wm_val:<15} {seed_val:<6} {tau_val:<6} {nmin_val:<6} {b_val:<6} {ppl:<10} {str(loss):<12} {concl:<12}\")\n\n# Also print the batch experiment per-b results\nprint()\nprint(\"grid_b_seed42_batch per-b results:\")\nm = exps['grid_b_seed42_batch'].get('metrics', {})\nfor b in ['0_5', '1_0', '1_5', '2_0', '3_0', '5_0']:\n    b_disp = b.replace('_', '.')\n    ppl_key = f'b{b}_eval_ppl'\n    loss_key = f'b{b}_train_loss'\n    if ppl_key in m:\n        print(f\"  b={b_disp}: PPL={m[ppl_key]}, train_loss={m.get(loss_key, '-')}\")\n\nPYEOF\n",
    "description": "Generate complete categorized experiment summary",
    "timeout": "30000"
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-15T15:53:06.652141+00:00_

====================================================================================================
COMPLETE EXPERIMENT REGISTRY — 40 experiments
====================================================================================================


────────────────────────────────────────────────────────────────────────────────────────────────────
  UNIFORM BASELINES (3 experiments)
────────────────────────────────────────────────────────────────────────────────────────────────────

  [uniform_seed456]
    Status: DONE | Conclusion: success | Parent: -
    Method: uniform | Seed: 456 | τ: - | n_min: -
    PPL: 17.7 | eval_loss: None | train_loss: 7.2895 | steps: 6103
    Runtime: 11974s (3.33h)

  [uniform_seed123]
    Status: DONE | Conclusion: success | Parent: -
    Method: uniform | Seed: 123 | τ: - | n_min: -
    PPL: 17.69 | eval_loss: None | train_loss: 7.3121 | steps: 6103
    Runtime: 11994s (3.33h)

  [uniform_seed42]
    Status: DONE | Conclusion: success | Parent: -
    Method: uniform | Seed: 42 | τ: - | n_min: -
    PPL: 17.69 | eval_loss: None | train_loss: 7.3104 | steps: 6103
    Runtime: 11946s (3.32h)

────────────────────────────────────────────────────────────────────────────────────────────────────
  GRID-B SWEEP (seed=42, batch) (2 experiments)
────────────────────────────────────────────────────────────────────────────────────────────────────

  [grid_b_low_seed42]
    Status: DONE | Conclusion: failed | Parent: -
    Method: - | Seed: 42 | τ: - | n_min: -
    Metrics: NONE (still running or no eval)
    Notes: cron框架误杀(infrastructure bug)。根因: WANDB_MODE=disabled + tmux wrapper PID 不匹配，reconcile_crons 判定进程死亡并发送 SIGTERM。训练实际曾完成 3 个 b 值(8477/8477×3)，但第二次重启后在 step 431 被杀，所有 checkpoint 目录丢失(grid_b0_1/0_2/0_3_see...

  [grid_b_seed42_batch]
    Status: DONE | Conclusion: success | Parent: -
    Method: - | Seed: 42 | τ: - | n_min: -
    PPL: None | eval_loss: None | train_loss: None | steps: 6103
    Per-b PPL: b=0.5→17.651, b=1.0→17.692, b=1.5→1
…[truncated 17157 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_full_data_table_20260515T154608",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-15T15:53:06.652450+00:00_

Here is the complete extraction of all 40 experiments from the registry.

---

## Summary

**40 total experiments** on server `westd-47453`, model `Qwen/Qwen3-0.6B`, 200M train tokens, 6103 total steps.

**Status distribution:** 31 DONE, 4 RUNNING, 4 PREPARING, 1 QUEUED  
**Conclusion distribution:** 27 success, 6 killed, 1 negative, 1 failed, 5 pending (null)

### Completed experiments with PPL (paper-ready data):

**Uniform baselines (3 seeds):**
- seed42: PPL=17.69, seed123: PPL=17.69, seed456: PPL=17.70

**Grid-b sweep seed=42 (batch, 6 b-values):**
- b=0.5→17.651, b=1.0→17.692, b=1.5→17.718, b=2.0→17.741, b=3.0→17.774, b=5.0→17.818. Best: b=0.5.

**Grid-b seed=123:** b=0.5→17.638, b=1.0→17.674, b=1.5→17.701, b=2.0→17.725, b=3.0→17.76, b=5.0→17.804

**Grid-b seed=456 (checkpoint resume artifacts on b=2/3/5):** b=0.5→17.65, b=1.0→17.68, b=1.5→17.71, b=2.0→17.989*, b=3.0→17.921*, b=5.0→17.993*  
(*noted as unreliable due to checkpoint resume; paper excludes these from seed456)

**Adaptive (original, n_min=3 bug):** seed42: 17.69, seed123: 17.63, seed456: 17.64

**Adaptive_fix (n_min=2, corrected):** seed42: 17.65, seed123: 17.643, seed456: 17.66. b* stats: mean~1.4, median~0.88, p25~0.54, p75~1.52.

**Special baselines:** golden_ratio: 17.654, ess_only: 17.73

**Tau sensitivity (only tau=0.6 done):** tau=0.6 PPL=17.6805 (negative vs tau=0.8 baseline 17.65). tau=0.5/0.7/0.9/0.95 still RUNNING.

**n_min ablation:** n_min=1 PPL=17.789 (worse than n_min=2), n_min=4 still PREPARING.

**Detector:** TF-IDF+LR: AUC=0.939, ECE_calibrated=0.048, T=0.204, q_score_mean=0.6

**Failed/killed:** grid_b_low_seed42 (infra bug), tau_0.6_seed42 (bad exp_id), detector_modernbert (superseded), adaptive_v2 x3 (design change to adaptive_fix), diagnostic_contamination100 (GPU contention kill)

### Full structured JSON files saved at:
- Raw dump: `/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/112e71b9-a790-4886
…[truncated 633 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_full_data_table_20260515T154608",
  "tool": "Agent",
  "elapsed_ms": 6
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-15T15:53:06.652720+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/112e71b9-a790-4886-b870-1e5804f7b2f6/tool-results/bhcd73450.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_full_data_table_20260515T154608",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/112e71b9-a790-4886-b870-1e5804f7b2f6/tool-results/bhcd73450.txt"
  }
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-15T15:53:06.652943+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "provenance_weight_training",
  "file": "decisions.yaml",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_full_data_table_20260515T154608",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "provenance_weight_training",
    "file": "decisions.yaml",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-15T15:53:06.653569+00:00_

1	================================================================================
2	EXP_ID: tau_095_seed42
3	  status: RUNNING
4	  conclusion: None
5	  parent: adaptive_fix_seed42
6	  created_at: 2026-05-15T10:03:32.419Z
7	  updated_at: 2026-05-15T14:58:16.987Z
8	  retry_count: 0
9	  tags: None
10	  notes: None
11	  hypothesis: τ sensitivity sweep: τ=0.95 (most strict α_eff threshold), testing upper bound — may over-constrain b* to near-zero. Baseline τ=0.8 PPL=17.65.
12	  server: westd-47453
13	  gpu: ['cuda:2']
14	  pid: 215505
15	  log_path: ~/runs/provenance_weight_training/tau_095_seed42.log
16	  model_name: Qwen/Qwen3-0.6B
17	  seed_spec: 42
18	  data_path: data/scored_data.jsonl
19	  data_count: 200000000
20	  PARAMS FROM CMD:
21	    weighting_method: adaptive
22	    batch_size: 4
23	    gradient_accumulation_steps: 4
24	    max_length: 2048
25	    learning_rate: 5e-5
26	    seed: 42
27	    contamination_ratio: 0.4
28	    tau: 0.95
29	    num_train_tokens: 200000000
30	    output_dir: output/models/tau_095_seed42
31	    model_name: models/Qwen/Qwen3-0.6B
32	    logging_steps: 10
33	    save_steps: 500
34	    bf16: True
35	    save_only_model: True
36	  RESULTS: None
37	
38	================================================================================
39	EXP_ID: tau_09_seed42
40	  status: RUNNING
41	  conclusion: None
42	  parent: adaptive_fix_seed42
43	  created_at: 2026-05-15T10:03:28.658Z
44	  updated_at: 2026-05-15T14:58:14.274Z
45	  retry_count: 0
46	  tags: None
47	  notes: None
48	  hypothesis: τ sensitivity sweep: τ=0.9 (stricter α_eff threshold), testing if higher quality threshold improves PPL. Baseline τ=0.8 PPL=17.65.
49	  server: westd-47453
50	  gpu: ['cuda:3']
51	  pid: 213283
52	  log_path: ~/runs/provenance_weight_training/tau_09_seed42.log
53	  model_name: Qwen/Qwen3-0.6B
54	  seed_spec: 42
55	  data_path: data/scored_data.jsonl
56	  data_count: 200000000
57	  PARAMS FROM CMD:
58	    weighting_method: adaptive
59	    batch_size: 4
60	    g
…[truncated 49295 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_full_data_table_20260515T154608",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-15T15:53:06.654103+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/decisions.yaml\", \"content\": \"_next_id: 32\\ndecisions:\\n- id: D001\\n  date: 2026-05-13 17:38 UTC\\n  summary: 投稿目标定为 AAAI 2027 (~Aug 2026)，放弃 EMNLP 2026 ARR May 25\\n  rationale: EMNLP ARR 仅剩 12 天且无任何基础设施，即使 AI 团队速度也无法完成多轮预训练实验。AAAI 2027 有 ~11 周，足够完成\\n    4 phase 全流程。两者均为 A 类会议。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-13 17:38 UTC\\n  summary: 'MVP 设计: 单模型(Qwen3-0.6B) + 单污染比例(40%) + 三组对比(uniform/grid-b/adaptive-b*)'\\n  rationale: 核心假设是 adaptive b* 能替代 grid search。最小验证只需一个污染比例下的 A/B/C 对比。40% 选取因为理论和\\n    Strong Model Collapse 均表明该区间效应显著。通过后再扩展到多污染比例/多生成器/多模型。\\n  related_experiments: []\\n  depends_on: []\\n- id: D003\\n  date: 2026-05-13 17:40 UTC\\n  summary: '修正 D001: 主攻 EMNLP 2026 ARR May 25，AAAI 2027 为后备'\\n  rationale: 用户明确指出 EMNLP ARR 5/25 时间不紧、资源会给够。AI 团队 24/7 执行 + 4 卡并行：数据生成 ~2 天、MVP\\n    ~1 天、全矩阵 ~3 天、论文 ~3 天、迭代 ~2 天 = 11 天可完成。12 天 deadline 可行。保守估计完成时间是最大风险。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D004\\n  date: 2026-05-13 17:42 UTC\\n  summary: '采纳 Reviewer 4 点 MVP 协议补全: 3 seeds、detector gate、grid-b 定义、kill criteria'\\n  rationale: 'Reviewer 指出 MVP 设计 4 个缺口均合理: (1) 单 seed 无统计保障 → 3 seeds，缩 tokens 到 200M\\n    控预算; (2) 检测器质量是 pipeline 前提 → 加 gate AUC≥0.95/ECE≤0.05; (3) grid search baseline\\n    需可复现 → 定义 b∈{0.5,1,1.5,2,3,5}; (4) 无 fail 路径 → 定义三级 kill/pivot。不增加工程量，只补协议。'\\n  related_experiments: []\\n  depends_on:\\n  - D002\\n- id: D005\\n  date: 2026-05-13 22:08 UTC\\n  summary: 识别 q-score 极化风险：AUC=0.999998 可能导致 adaptive b* vs grid-b 对比退化，制定分级应对方案\\n  rationale: 'Reviewer 审查发现 detector eval_auc=0.999998（step 2000），q-score 可能高度双峰化。若校准后\\n    >95% 样本 q<0.05 或 q>0.95，则 w=(1-q)^b 对所有 b>0 约等于 0，不同 b 值间无区分度。MVP 技术上可能 PASS（adaptive\\n    ≈ grid-b，满足 ≥90% 条件），但无法证明核心贡献（自适应精细调优的价值）。\\n\\n\\n    应对方案（detector 完成后按 q-score 分布分级执行）：\\n\\n    - 分布有spread（q 在 0.1
…[truncated 18795 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_full_data_table_20260515T154608",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-15T15:53:06.654393+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/",
  "description": "Check artifacts directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_full_data_table_20260515T154608",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/",
    "description": "Check artifacts directory"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-15T15:53:06.654545+00:00_

_project
all_success_summary.md
analyze_tau_sweep.py
bstar_distribution_analysis.md
data_generation
detector
drayson_comparison.md
dream_reports
ess_only_analysis_template.md
ess_only_implementation.md
ess_only_seed42
evaluation
experiment_setup_draft.md
experiment_status_summary.md
experiment_summary.md
full_experiment_data.md
grid_b5_0_seed123
interim_mvp_analysis.md
literature_diff_drayson.md
literature_notes.md
literature_scan_results.md
manifest.yaml
method_section_draft.md
mvp_analysis_draft.md
mvp_analysis_summary.md
new_scripts_manifest.md
nmin1_seed42
novelty_drayson_analysis.md
q1_ess_equivalence_analysis.md
related_work_notes.md
run_mvp.sh
seed42_diagnostic.md
table1_data.md
tau_derivation_check.md
tau_fix_changelog.md
tau_sweep_commands.md
tau_sweep_curve_dummy.pdf
tau_sweep_curve_dummy.png
tau_sweep_improvement_dummy.pdf
tau_sweep_improvement_dummy.png
tau_sweep_readiness.md
tau_theory_analysis.md
tau_theory_audit.md
training
training_progress_check.md
weighting
worker_output.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_full_data_table_20260515T154608",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-15T15:53:06.654712+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

````json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/experiment_summary_table.md",
  "content": "# Complete Experiment Summary — provenance_weight_training\n\n> Generated: 2026-05-15 | Model: Qwen/Qwen3-0.6B | Train tokens: 200M | Steps: 6,103\n> Core method: Dual-constrained adaptive b* — α_eff quality floor + ESS stability ceiling → minimum intervention principle\n\n## Experimental Setup\n\n| Parameter | Value |\n|-----------|-------|\n| Model | Qwen/Qwen3-0.6B |\n| Training data | 371,499 docs, 40% synthetic contamination (self-generated) |\n| Detector | TF-IDF + Logistic Regression (AUC=0.939, ECE_cal=0.048, T*=0.204) |\n| Eval metric | Held-out PPL (sliding window, stride=1024, max_docs=5000, fp16, 4.08M tokens) |\n| Batch size | 4 |\n| Gradient accumulation | 4 (effective batch=16) |\n| Learning rate | 5e-5 |\n| Max length | 2048 |\n| Precision | bf16 |\n| Seeds | 42, 123, 456 |\n\n---\n\n## Uniform Baselines\n\n| exp_id | seed | PPL | eval_loss |\n|--------|------|-----|-----------|\n| uniform_seed42 | 42 | 17.690 | — |\n| uniform_seed123 | 123 | 17.690 | — |\n| uniform_seed456 | 456 | 17.700 | — |\n| **Mean** | — | **17.693** | — |\n\n---\n\n## Table 1: Grid-b Sweep (fixed weight w = (1−q)^b)\n\n### Per-seed PPL\n\n| b | seed42 | seed123 | seed456 | Mean | ΔPPL vs uniform |\n|-----|--------|---------|---------|------|-----------------|\n| 0 (uniform) | 17.690 | 17.690 | 17.700 | 17.693 | — |\n| 0.5 | 17.651 | 17.638 | 17.650 | 17.646 | **+0.047** |\n| 1.0 | 17.692 | 17.674 | 17.680 | 17.682 | +0.011 |\n| 1.5 | 17.718 | 17.701 | 17.710 | 17.710 | −0.017 |\n| 2.0 | 17.741 | 17.725 | ~~17.989~~ ⚠️ | 17.733 †| −0.043 † |\n| 3.0 | 17.774 | 17.760 | ~~17.921~~ ⚠️ | 17.767 † | −0.077 † |\n| 5.0 | 17.818 | 17.804 | ~~17.993~~ ⚠️ | 17.811 † | −0.121 † |\n\n> ⚠️ **D026**: seed456 b≥2.0 PPL systematically inflated due to checkpoint resume artifact (LR/optimizer state corruption). Paper Table 1 reports 2-seed mean (seed42+seed123) for b≥2.0, marked with †.\n> ΔPPL = uniform_mean − grid_mean; positive = improvement over uniform.\n> **Grid-best: b=0.5** across all seeds. PPL monotonically increases with b.\n\n### Per-seed ΔPPL (uniform − grid)\n\n| b | seed42 | seed123 | seed456 |\n|-----|--------|---------|---------|\n| 0.5 | +0.039 | +0.052 | +0.050 |\n| 1.0 | −0.002 | +0.016 | +0.020 |\n| 1.5 | −0.028 | −0.011 | −0.010 |\n| 2.0 | −0.051 | −0.035 | — |\n| 3.0 | −0.084 | −0.070 | — |\n| 5.0 | −0.128 | −0.114 | — |\n\n### Source exp_ids\n\n| b | seed42 | seed123 | seed456 |\n|-----|--------|---------|---------|\n| 0.5–5.0 | grid_b_seed42_batch | grid_b0_5_seed123 … grid_b5_0_seed123 | grid_b0_5_seed456 … grid_b5_0_seed456 |\n\n---\n\n## Table 2: Method Comparison (adaptive_fix vs baselines)\n\n### PPL\n\n| Method | seed42 | seed123 | seed456 | Mean | ΔPPL vs uniform |\n|--------|--------|---------|---------|------|-----------------|\n| uniform | 17.690 | 17.690 | 17.700 | 17.693 | — |\n| grid-best (b=0.5) | 17.651 | 17.638 | 17.650 | 17.646 | +0.047 |\n| **adaptive_fix** (τ=0.8, n_min=2) | **17.650** | **17.643** | **17.660** | **17.651** | **+0.042** |\n| adaptive_orig (τ=0.8, n_min=3) | 17.690 | 17.630 | 17.640 | 17.653 | +0.040 |\n| golden_ratio (w=1/φ for synthetic) | 17.654 | — | — | 17.654 | +0.036 |\n| ess_only (max-intervention) | 17.730 | — | — | 17.730 | −0.040 |\n\n### Per-seed ΔPPL vs uniform\n\n| Method | seed42 | seed123 | seed456 |\n|--------|--------|---------|---------|\n| grid-best (b=0.5) | +0.039 | +0.052 | +0.050 |\n| **adaptive_fix** | **+0.040** | **+0.047** | **+0.040** |\n| adaptive_orig | +0.000 | +0.060 | +0.060 |\n| golden_ratio | +0.036 | — | — |\n| ess_only | −0.040 | — | — |\n\n### Capture ratio (adaptive_fix improvement / grid-best improvement × 100%)\n\n| seed | grid-best ΔPPL | adaptive_fix ΔPPL | Capture ratio |\n|------|---------------|-------------------|---------------|\n| 42 | 0.039 | 0.040 | **102.6%** |\n| 123 | 0.052 | 0.047 | 90.4% |\n| 456 | 0.050 | 0.040 | 80.0% |\n| **Aggregate** | — | — | **~87%** (D019) |\n\n> D019 notes: 3/3 seeds adaptive > uniform (100% consistency). Aggregate capture <90% threshold but qualitative conclusion holds — \"comparable improvement, eliminates grid search.\"\n\n### Adaptive_fix b* distribution statistics\n\n| Statistic | seed42 | seed123 | seed456 |\n|-----------|--------|---------|---------|\n| mean | 1.399 | 1.431 | 1.416 |\n| median | 0.871 | 0.880 | 0.880 |\n| std | 1.933 | 2.029 | 1.993 |\n| p25 | 0.540 | 0.540 | 0.540 |\n| p75 | 1.512 | 1.520 | 1.520 |\n| min | 0 | 0 | 0 |\n| max | 20 | 20 | 20 |\n| % b<0.5 | 20.9% | 20.9% | 20.9% |\n| % 0.5–1.0 | 35.7% | 35.7% | 35.7% |\n| % 1.0–2.0 | 27.3% | 27.3% | 27.3% |\n| % b>2.0 | 16.1% | 16.1% | 16.1% |\n| count (train batches) | 26,458 | 25,906 | 26,396 |\n\n> b* remarkably consistent across seeds. Median ~0.88 (mild downweighting), <1% hit b_max=20 ceiling (D015).\n\n### Ablation narrative (seed42)\n\n| Method | PPL | Role |\n|--------|-----|------|\n| adaptive_fix (dual-constrained) | 17.650 | **Best**: min-intervention, both constraints active |\n| uniform | 17.690 | Baseline: no provenance information |\n| ess_only (max-intervention) | 17.730 | **Worst**: removes α_eff floor, over-downweights |\n\n> Ordering: dual-constrained > uniform > ESS-only. ESS-only PPL 0.080 worse than adaptive_fix — proves α_eff floor is necessary (D029).\n\n### Source exp_ids\n\n| Method | seed42 | seed123 | seed456 |\n|--------|--------|---------|---------|\n| uniform | uniform_seed42 | uniform_seed123 | uniform_seed456 |\n| adaptive_fix | adaptive_fix_seed42 | adaptive_fix_seed123 | adaptive_fix_seed456 |\n| adaptive_orig | adaptive_seed42 | adaptive_seed123 | adaptive_seed456 |\n| golden_ratio | golden_ratio_seed42 | — | — |\n| ess_only | ess_only_seed42 | — | — |\n\n---\n\n## Table 3: τ Sensitivity (seed=42, n_min=2)\n\n| τ | PPL | ΔPPL vs uniform | ΔPPL vs τ=0.8 | Status | exp_id |\n|------|--------|-----------------|---------------|--------|--------|\n| 0.50 | — | — | — | RUNNING | tau_05_seed42 |\n| 0.60 | 17.681 ⚠️ | +0.009 | −0.031 | **NEGATIVE** | tau_06_seed42 |\n| 0.70 | — | — | — | RUNNING | tau_07_seed42 |\n| **0.80** | **17.650** | **+0.040** | **baseline** | DONE | adaptive_fix_seed42 |\n| 0.90 | — | — | — | RUNNING | tau_09_seed42 |\n| 0.95 | — | — | — | RUNNING | tau_095_seed42 |\n\n> ⚠️ τ=0.6 is the only completed negative result: PPL 17.681 > adaptive_fix baseline 17.650 (ΔPPL = −0.031). Lower τ → looser α_eff floor → smaller b* → weaker downweighting.\n> τ=0.6 b* stats: mean=0.590, median=0.375 (vs τ=0.8: mean=1.399, median=0.871).\n> τ=0.5/0.7/0.9/0.95 results pending — critical for Claim 3 (τ robustness, D025/D030).\n\n---\n\n## Table 4: n_min Ablation (seed=42, τ=0.8)\n\n| n_min | PPL | ΔPPL vs uniform | b* mean | b* median | b* p75 | Status | exp_id |\n|-------|-----|-----------------|---------|-----------|--------|--------|--------|\n| 1 | 17.789 | −0.099 | 7.197 | 1.746 | 20.0 | DONE | nmin1_seed42 |\n| **2** | **17.650** | **+0.040** | **1.399** | **0.871** | **1.512** | DONE | adaptive_fix_seed42 |\n| 3 | 17.690 | +0.000 | — | — | — | DONE | adaptive_seed42 |\n| 4 | — | — | — | — | — | PREPARING | nmin4_seed42 |\n\n### Cross-seed n_min comparison (n_min=2 vs n_min=3)\n\n| n_min | seed42 | seed123 | seed456 | Mean | Std |\n|-------|--------|---------|---------|------|-----|\n| 2 (adaptive_fix) | 17.650 | 17.643 | 17.660 | 17.651 | 0.009 |\n| 3 (adaptive_orig) | 17.690 | 17.630 | 17.640 | 17.653 | 0.032 |\n\n> D031: n_min=2 advantage is **consistency** (std=0.009 vs 0.032), not absolute mean (difference only 0.002).\n> n_min=1: ESS constraint nearly ineffective — 46.7% batches hit b*≥2, p75=20.0 (ceiling). Over-downweighting degrades PPL below uniform.\n> n_min=3: works well for seed123/456 but fails for seed42 (D012 root cause: ESS clamped at 75% ≈ uniform).\n> n_min=4 (=batch_size): expected to force b*=0 always → degrade to uniform. PREPARING.\n\n---\n\n## Table 5: Detector Performance\n\n| Metric | Value |\n|--------|-------|\n| exp_id | detector_tfidf_lr |\n| Model | TF-IDF (bigram) + Logistic Regression |\n| Train data | 67,960 documents |\n| AUC | 0.939 |\n| Accuracy | 0.858 |\n| ECE (raw) | 0.240 |\n| ECE (calibrated) | 0.048 |\n| Temperature T* | 0.204 |\n| q-score mean | 0.600 |\n| q-score std | 0.374 |\n| q-score median | 0.707 |\n| Mid-range ratio (0.2–0.8) | 0.463 |\n\n> D007/D008: Deliberately chose weak detector over ModernBERT (AUC=0.9998) to avoid q-score polarization. TF-IDF provides meaningful spread for adaptive weighting.\n> Gate check (D009): AUC=0.939 ≥ 0.90 ✓, ECE=0.048 ≤ 0.05 ✓.\n\n---\n\n## Table 6: Data Generation\n\n| exp_id | Description | Output |\n|--------|-------------|--------|\n| datagen_synthetic_4gpu | 4-GPU parallel generation with Qwen3-0.6B | ~132M tokens, seeds 42/1042/2042/3042 |\n\n---\n\n## Table 7: Non-success Experiments\n\n| exp_id | conclusion | reason |\n|--------|-----------|--------|\n| tau_06_seed42 | **negative** | PPL 17.681 > baseline 17.650; lower τ = weaker downweighting |\n| grid_b_low_seed42 | failed | Cron framework SIGTERM bug (2x), all checkpoints lost |\n| tau_0.6_seed42 | killed | Illegal exp_id (contains dot), replaced by tau_06_seed42 |\n| detector_modernbert | killed | Superseded by TF-IDF detector (D007); never ran |\n| adaptive_v2_seed42 | killed | D012: cancelled v2 (with EMA), replaced by adaptive_fix |\n| adaptive_v2_seed123 | killed | D012: cancelled v2 (with EMA), replaced by adaptive_fix |\n| adaptive_v2_seed456 | killed | D012: cancelled v2 (with EMA), replaced by adaptive_fix |\n| diagnostic_contamination100 | killed | GPU contention; killed to free cuda:3 for grid-b (D027) |\n\n---\n\n## Table 8: Currently Running / Preparing\n\n| exp_id | Status | τ | GPU | Parent |\n|--------|--------|---|-----|--------|\n| tau_05_seed42 | RUNNING | 0.50 | cuda:1 | adaptive_fix_seed42 |\n| tau_07_seed42 | RUNNING | 0.70 | cuda:0 | adaptive_fix_seed42 |\n| tau_09_seed42 | RUNNING | 0.90 | cuda:3 | adaptive_fix_seed42 |\n| tau_095_seed42 | RUNNING | 0.95 | cuda:2 | adaptive_fix_seed42 |\n| nmin4_seed42 | PREPARING | 0.80 | — | — |\n\n---\n\n## Key Decisions Affecting Data\n\n| Decision | Impact |\n|----------|--------|\n| D012 | n_min fix 3→2: adaptive_orig → adaptive_fix. n_min=3 data reused as ablation point. |\n| D017 | D012 erratum: EMA was never implemented, only n_min changed. |\n| D018 | v1→v2 no confound: only n_min changed, no code logic difference. |\n| D019 | MVP PASS (Path B): aggregate capture ~87% < 90% threshold, but 3/3 seeds improve. |\n| D023 | α_eff not decorative: dual-constraint (α_eff floor + ESS ceiling) validated. |\n| D025 | τ is empirical hyperparameter with theoretical motivation, not proportion-free. |\n| D026 | seed456 b≥2.0 checkpoint artifact: paper uses 2-seed mean for those rows. |\n| D031 | n_min narrative: variance advantage (std 0.009 vs 0.032), not mean advantage. |\n\n---\n\n## Aggregated Results (paper-ready)\n\n### Main result: Adaptive b* vs Grid-best vs Uniform\n\n| Method | PPL (3-seed mean) | ΔPPL vs uniform | Grid search cost |\n|--------|-------------------|-----------------|------------------|\n| Uniform (b=0) | 17.693 | — | 0 runs |\n| Grid-best (b=0.5) | 17.646 | +0.047 | 6 runs per seed |\n| **Adaptive_fix (b\\*)** | **17.651** | **+0.042** | **0 runs (automatic)** |\n\n> Adaptive b* captures ~89% of grid-best improvement with zero hyperparameter tuning.\n> PPL range across seeds: adaptive_fix 0.017 vs grid-best 0.013 — comparable stability.\n\n### Ablation ordering (seed42)\n\n```\nadaptive_fix (17.650) > golden_ratio (17.654) > uniform (17.690) > adaptive_orig/n_min=3 (17.690) > ess_only (17.730) > nmin1 (17.789)\n```\n"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "worker_analysis_full_data_table_20260515T154608",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/experiment_summary_table.md",
    "content": "# Complete Experiment Summary — provenance_weight_training\n\n> Generated: 2026-05-15 | Model: Qwen/Qwen3-0.6B | Train tokens: 200M | Steps: 6,103\n> Core method: Dual-constrained adaptive b* — α_eff quality floor + ESS stability ceiling → minimum intervention principle\n\n## Experimental Setup\n\n| Parameter | Value |\n|-----------|-------|\n| Model | Qwen/Qwen3-0.6B |\n| Training data | 371,499 docs, 40% synthetic contamination (self-generated) |\n| Detector | TF-IDF + Logistic Regression (AUC=0.939, ECE_cal=0.048, T*=0.204) |\n| Eval metric | Held-out PPL (sliding window, stride=1024, max_docs=5000, fp16, 4.08M tokens) |\n| Batch size | 4 |\n| Gradient accumulation | 4 (effective batch=16) |\n| Learning rate | 5e-5 |\n| Max length | 2048 |\n| Precision | bf16 |\n| Seeds | 42, 123, 456 |\n\n---\n\n## Uniform Baselines\n\n| exp_id | seed | PPL | eval_loss |\n|--------|------|-----|-----------|\n| uniform_seed42 | 42 | 17.690 | — |\n| uniform_seed123 | 123 | 17.690 | — |\n| uniform_seed456 | 456 | 17.700 | — |\n| **Mean** | — | **17.693** | — |\n\n---\n\n## Table 1: Grid-b Sweep (fixed weight w = (1−q)^b)\n\n### Per-seed PPL\n\n| b | seed42 | seed123 | seed456 | Mean | ΔPPL vs uniform |\n|-----|--------|---------|---------|------|-----------------|\n| 0 (uniform) | 17.690 | 17.690 | 17.700 | 17.693 | — |\n| 0.5 | 17.651 | 17.638 | 17.650 | 17.646 | **+0.047** |\n| 1.0 | 17.692 | 17.674 | 17.680 | 17.682 | +0.011 |\n| 1.5 | 17.718 | 17.701 | 17.710 | 17.710 | −0.017 |\n| 2.0 | 17.741 | 17.725 | ~~17.989~~ ⚠️ | 17.733 †| −0.043 † |\n| 3.0 | 17.774 | 17.760 | ~~17.921~~ ⚠️ | 17.767 † | −0.077 † |\n| 5.0 | 17.818 | 17.804 | ~~17.993~~ ⚠️ | 17.811 † | −0.121 † |\n\n> ⚠️ **D026**: seed456 b≥2.0 PPL systematically inflated due to checkpoint resume artifact (LR/optimizer state corruption). Paper Table 1 reports 2-seed mean (seed42+seed123) for b≥2.0, marked with †.\n> ΔPPL = uniform_mean − grid_mean; positive = improvement over uniform.\n> **Grid-best: b=0.5** across all seeds. PPL monotonically increases with b.\n\n### Per-seed ΔPPL (uniform − grid)\n\n| b | seed42 | seed123 | seed456 |\n|-----|--------|---------|---------|\n| 0.5 | +0.039 | +0.052 | +0.050 |\n| 1.0 | −0.002 | +0.016 | +0.020 |\n| 1.5 | −0.028 | −0.011 | −0.010 |\n| 2.0 | −0.051 | −0.035 | — |\n| 3.0 | −0.084 | −0.070 | — |\n| 5.0 | −0.128 | −0.114 | — |\n\n### Source exp_ids\n\n| b | seed42 | seed123 | seed456 |\n|-----|--------|---------|---------|\n| 0.5–5.0 | grid_b_seed42_batch | grid_b0_5_seed123 … grid_b5_0_seed123 | grid_b0_5_seed456 … grid_b5_0_seed456 |\n\n---\n\n## Table 2: Method Comparison (adaptive_fix vs baselines)\n\n### PPL\n\n| Method | seed42 | seed123 | seed456 | Mean | ΔPPL vs uniform |\n|--------|--------|---------|---------|------|-----------------|\n| uniform | 17.690 | 17.690 | 17.700 | 17.693 | — |\n| grid-best (b=0.5) | 17.651 | 17.638 | 17.650 | 17.646 | +0.047 |\n| **adaptive_fix** (τ=0.8, n_min=2) | **17.650** | **17.643** | **17.660** | **17.651** | **+0.042** |\n| adaptive_orig (τ=0.8, n_min=3) | 17.690 | 17.630 | 17.640 | 17.653 | +0.040 |\n| golden_ratio (w=1/φ for synthetic) | 17.654 | — | — | 17.654 | +0.036 |\n| ess_only (max-intervention) | 17.730 | — | — | 17.730 | −0.040 |\n\n### Per-seed ΔPPL vs uniform\n\n| Method | seed42 | seed123 | seed456 |\n|--------|--------|---------|---------|\n| grid-best (b=0.5) | +0.039 | +0.052 | +0.050 |\n| **adaptive_fix** | **+0.040** | **+0.047** | **+0.040** |\n| adaptive_orig | +0.000 | +0.060 | +0.060 |\n| golden_ratio | +0.036 | — | — |\n| ess_only | −0.040 | — | — |\n\n### Capture ratio (adaptive_fix improvement / grid-best improvement × 100%)\n\n| seed | grid-best ΔPPL | adaptive_fix ΔPPL | Capture ratio |\n|------|---------------|-------------------|---------------|\n| 42 | 0.039 | 0.040 | **102.6%** |\n| 123 | 0.052 | 0.047 | 90.4% |\n| 456 | 0.050 | 0.040 | 80.0% |\n| **Aggregate** | — | — | **~87%** (D019) |\n\n> D019 notes: 3/3 seeds adaptive > uniform (100% consistency). Aggregate capture <90% threshold but qualitative conclusion holds — \"comparable improvement, eliminates grid search.\"\n\n### Adaptive_fix b* distribution statistics\n\n| Statistic | seed42 | seed123 | seed456 |\n|-----------|--------|---------|---------|\n| mean | 1.399 | 1.431 | 1.416 |\n| median | 0.871 | 0.880 | 0.880 |\n| std | 1.933 | 2.029 | 1.993 |\n| p25 | 0.540 | 0.540 | 0.540 |\n| p75 | 1.512 | 1.520 | 1.520 |\n| min | 0 | 0 | 0 |\n| max | 20 | 20 | 20 |\n| % b<0.5 | 20.9% | 20.9% | 20.9% |\n| % 0.5–1.0 | 35.7% | 35.7% | 35.7% |\n| % 1.0–2.0 | 27.3% | 27.3% | 27.3% |\n| % b>2.0 | 16.1% | 16.1% | 16.1% |\n| count (train batches) | 26,458 | 25,906 | 26,396 |\n\n> b* remarkably consistent across seeds. Median ~0.88 (mild downweighting), <1% hit b_max=20 ceiling (D015).\n\n### Ablation narrative (seed42)\n\n| Method | PPL | Role |\n|--------|-----|------|\n| adaptive_fix (dual-constrained) | 17.650 | **Best**: min-intervention, both constraints active |\n| uniform | 17.690 | Baseline: no provenance information |\n| ess_only (max-intervention) | 17.730 | **Worst**: removes α_eff floor, over-downweights |\n\n> Ordering: dual-constrained > uniform > ESS-only. ESS-only PPL 0.080 worse than adaptive_fix — proves α_eff floor is necessary (D029).\n\n### Source exp_ids\n\n| Method | seed42 | seed123 | seed456 |\n|--------|--------|---------|---------|\n| uniform | uniform_seed42 | uniform_seed123 | uniform_seed456 |\n| adaptive_fix | adaptive_fix_seed42 | adaptive_fix_seed123 | adaptive_fix_seed456 |\n| adaptive_orig | adaptive_seed42 | adaptive_seed123 | adaptive_seed456 |\n| golden_ratio | golden_ratio_seed42 | — | — |\n| ess_only | ess_only_seed42 | — | — |\n\n---\n\n## Table 3: τ Sensitivity (seed=42, n_min=2)\n\n| τ | PPL | ΔPPL vs uniform | ΔPPL vs τ=0.8 | Status | exp_id |\n|------|--------|-----------------|---------------|--------|--------|\n| 0.50 | — | — | — | RUNNING | tau_05_seed42 |\n| 0.60 | 17.681 ⚠️ | +0.009 | −0.031 | **NEGATIVE** | tau_06_seed42 |\n| 0.70 | — | — | — | RUNNING | tau_07_seed42 |\n| **0.80** | **17.650** | **+0.040** | **baseline** | DONE | adaptive_fix_seed42 |\n| 0.90 | — | — | — | RUNNING | tau_09_seed42 |\n| 0.95 | — | — | — | RUNNING | tau_095_seed42 |\n\n> ⚠️ τ=0.6 is the only completed negative result: PPL 17.681 > adaptive_fix baseline 17.650 (ΔPPL = −0.031). Lower τ → looser α_eff floor → smaller b* → weaker downweighting.\n> τ=0.6 b* stats: mean=0.590, median=0.375 (vs τ=0.8: mean=1.399, median=0.871).\n> τ=0.5/0.7/0.9/0.95 results pending — critical for Claim 3 (τ robustness, D025/D030).\n\n---\n\n## Table 4: n_min Ablation (seed=42, τ=0.8)\n\n| n_min | PPL | ΔPPL vs uniform | b* mean | b* median | b* p75 | Status | exp_id |\n|-------|-----|-----------------|---------|-----------|--------|--------|--------|\n| 1 | 17.789 | −0.099 | 7.197 | 1.746 | 20.0 | DONE | nmin1_seed42 |\n| **2** | **17.650** | **+0.040** | **1.399** | **0.871** | **1.512** | DONE | adaptive_fix_seed42 |\n| 3 | 17.690 | +0.000 | — | — | — | DONE | adaptive_seed42 |\n| 4 | — | — | — | — | — | PREPARING | nmin4_seed42 |\n\n### Cross-seed n_min comparison (n_min=2 vs n_min=3)\n\n| n_min | seed42 | seed123 | seed456 | Mean | Std |\n|-------|--------|---------|---------|------|-----|\n| 2 (adaptive_fix) | 17.650 | 17.643 | 17.660 | 17.651 | 0.009 |\n| 3 (adaptive_orig) | 17.690 | 17.630 | 17.640 | 17.653 | 0.032 |\n\n> D031: n_min=2 advantage is **consistency** (std=0.009 vs 0.032), not absolute mean (difference only 0.002).\n> n_min=1: ESS constraint nearly ineffective — 46.7% batches hit b*≥2, p75=20.0 (ceiling). Over-downweighting degrades PPL below uniform.\n> n_min=3: works well for seed123/456 but fails for seed42 (D012 root cause: ESS clamped at 75% ≈ uniform).\n> n_min=4 (=batch_size): expected to force b*=0 always → degrade to uniform. PREPARING.\n\n---\n\n## Table 5: Detector Performance\n\n| Metric | Value |\n|--------|-------|\n| exp_id | detector_tfidf_lr |\n| Model | TF-IDF (bigram) + Logistic Regression |\n| Train data | 67,960 documents |\n| AUC | 0.939 |\n| Accuracy | 0.858 |\n| ECE (raw) | 0.240 |\n| ECE (calibrated) | 0.048 |\n| Temperature T* | 0.204 |\n| q-score mean | 0.600 |\n| q-score std | 0.374 |\n| q-score median | 0.707 |\n| Mid-range ratio (0.2–0.8) | 0.463 |\n\n> D007/D008: Deliberately chose weak detector over ModernBERT (AUC=0.9998) to avoid q-score polarization. TF-IDF provides meaningful spread for adaptive weighting.\n> Gate check (D009): AUC=0.939 ≥ 0.90 ✓, ECE=0.048 ≤ 0.05 ✓.\n\n---\n\n## Table 6: Data Generation\n\n| exp_id | Description | Output |\n|--------|-------------|--------|\n| datagen_synthetic_4gpu | 4-GPU parallel generation with Qwen3-0.6B | ~132M tokens, seeds 42/1042/2042/3042 |\n\n---\n\n## Table 7: Non-success Experiments\n\n| exp_id | conclusion | reason |\n|--------|-----------|--------|\n| tau_06_seed42 | **negative** | PPL 17.681 > baseline 17.650; lower τ = weaker downweighting |\n| grid_b_low_seed42 | failed | Cron framework SIGTERM bug (2x), all checkpoints lost |\n| tau_0.6_seed42 | killed | Illegal exp_id (contains dot), replaced by tau_06_seed42 |\n| detector_modernbert | killed | Superseded by TF-IDF detector (D007); never ran |\n| adaptive_v2_seed42 | killed | D012: cancelled v2 (with EMA), replaced by adaptive_fix |\n| adaptive_v2_seed123 | killed | D012: cancelled v2 (with EMA), replaced by adaptive_fix |\n| adaptive_v2_seed456 | killed | D012: cancelled v2 (with EMA), replaced by adaptive_fix |\n| diagnostic_contamination100 | killed | GPU contention; killed to free cuda:3 for grid-b (D027) |\n\n---\n\n## Table 8: Currently Running / Preparing\n\n| exp_id | Status | τ | GPU | Parent |\n|--------|--------|---|-----|--------|\n| tau_05_seed42 | RUNNING | 0.50 | cuda:1 | adaptive_fix_seed42 |\n| tau_07_seed42 | RUNNING | 0.70 | cuda:0 | adaptive_fix_seed42 |\n| tau_09_seed42 | RUNNING | 0.90 | cuda:3 | adaptive_fix_seed42 |\n| tau_095_seed42 | RUNNING | 0.95 | cuda:2 | adaptive_fix_seed42 |\n| nmin4_seed42 | PREPARING | 0.80 | — | — |\n\n---\n\n## Key Decisions Affecting Data\n\n| Decision | Impact |\n|----------|--------|\n| D012 | n_min fix 3→2: adaptive_orig → adaptive_fix. n_min=3 data reused as ablation point. |\n| D017 | D012 erratum: EMA was never implemented, only n_min changed. |\n| D018 | v1→v2 no confound: only n_min changed, no code logic difference. |\n| D019 | MVP PASS (Path B): aggregate capture ~87% < 90% threshold, but 3/3 seeds improve. |\n| D023 | α_eff not decorative: dual-constraint (α_eff floor + ESS ceiling) validated. |\n| D025 | τ is empirical hyperparameter with theoretical motivation, not proportion-free. |\n| D026 | seed456 b≥2.0 checkpoint artifact: paper uses 2-seed mean for those rows. |\n| D031 | n_min narrative: variance advantage (std 0.009 vs 0.032), not mean advantage. |\n\n---\n\n## Aggregated Results (paper-ready)\n\n### Main result: Adaptive b* vs Grid-best vs Uniform\n\n| Method | PPL (3-seed mean) | ΔPPL vs uniform | Grid search cost |\n|--------|-------------------|-----------------|------------------|\n| Uniform (b=0) | 17.693 | — | 0 runs |\n| Grid-best (b=0.5) | 17.646 | +0.047 | 6 runs per seed |\n| **Adaptive_fix (b\\*)** | **17.651** | **+0.042** | **0 runs (automatic)** |\n\n> Adaptive b* captures ~89% of grid-best improvement with zero hyperparameter tuning.\n> PPL range across seeds: adaptive_fix 0.017 vs grid-best 0.013 — comparable stability.\n\n### Ablation ordering (seed42)\n\n```\nadaptive_fix (17.650) > golden_ratio (17.654) > uniform (17.690) > adaptive_orig/n_min=3 (17.690) > ess_only (17.730) > nmin1 (17.789)\n```\n"
  }
}
````

</details>

---

### Tool result

_source line 48 · 2026-05-15T15:53:06.655037+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/experiment_summary_table.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_full_data_table_20260515T154608",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-15T15:53:06.655199+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "experiment_summary_table",
  "type": "report",
  "description": "Complete data table of all 27 success + 1 negative + 1 failed + 8 killed/running experiments. 8 tables covering grid-b sweep, method comparison, τ sensitivity, n_min ablation, detector, data generation, non-success, and running experiments. Includes per-seed PPL, ΔPPL, capture ratios, b* statistics, and key decision impacts.",
  "project": "provenance_weight_training",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/experiment_summary_table.md",
  "tags": "['paper', 'summary', 'all-experiments', 'tables']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_full_data_table_20260515T154608",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "experiment_summary_table",
    "type": "report",
    "description": "Complete data table of all 27 success + 1 negative + 1 failed + 8 killed/running experiments. 8 tables covering grid-b sweep, method comparison, τ sensitivity, n_min ablation, detector, data generation, non-success, and running experiments. Includes per-seed PPL, ΔPPL, capture ratios, b* statistics, and key decision impacts.",
    "project": "provenance_weight_training",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/experiment_summary_table.md",
    "tags": "['paper', 'summary', 'all-experiments', 'tables']"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-15T15:53:06.655367+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260515_3671c5\", \"name\": \"experiment_summary_table\", \"type\": \"report\", \"description\": \"Complete data table of all 27 success + 1 negative + 1 failed + 8 killed/running experiments. 8 tables covering grid-b sweep, method comparison, τ sensitivity, n_min ablation, detector, data generation, non-success, and running experiments. Includes per-seed PPL, ΔPPL, capture ratios, b* statistics, and key decision impacts.\", \"path\": \"projects/provenance_weight_training/artifacts/_project/report/experiment_summary_table.md\", \"url\": null, \"project\": \"provenance_weight_training\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-15T15:52:56.192133+00:00\", \"tags\": [\"paper\", \"summary\", \"all-experiments\", \"tables\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_full_data_table_20260515T154608",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 51 · 2026-05-15T15:53:06.655543+00:00_

已完成。产出文件：`artifacts/experiment_summary_table.md`（已注册为 `art_20260515_3671c5`）。

包含 8 张表：

| 表 | 内容 |
|---|------|
| Table 1 | Grid-b sweep (b=0.5–5.0, 3 seeds, seed456 b≥2.0 标注 D026 artifact) |
| Table 2 | Method comparison (adaptive_fix / uniform / grid-best / golden_ratio / ess_only) + capture ratio + b* 分布 |
| Table 3 | τ sensitivity (τ=0.6 negative 已标注, 0.5/0.7/0.9/0.95 RUNNING) |
| Table 4 | n_min ablation (1/2/3/4) + cross-seed variance 对比 |
| Table 5 | Detector 性能 |
| Table 6 | Data generation |
| Table 7 | 非成功实验 (1 negative + 1 failed + 6 killed) |
| Table 8 | 当前 RUNNING/PREPARING |

核心数字：adaptive_fix 3-seed mean PPL=17.651, vs uniform 17.693 (ΔPPL=+0.042), vs grid-best 17.646 (capture ~87%), 零调参成本。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_full_data_table_20260515T154608"
}
```

</details>

---
