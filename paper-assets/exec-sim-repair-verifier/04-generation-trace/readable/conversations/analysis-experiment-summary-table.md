# analysis experiment summary table

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 57
- **Recorded user turns:** 0
- **Tool calls:** 28
- **Original source:** `logs/chats/worker_analysis_experiment-summary-table_20260514T003543.jsonl`
- **Structured JSON:** [`1eb0a44ab4446b780ee2.json`](../../sessions/1e/1eb0a44ab4446b780ee2.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

57 recorded events

### Tool call

_source line 1 · 2026-05-14T00:42:59.675567+00:00_

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
  "session": "worker_analysis_experiment-summary-table_20260514T003543",
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

_source line 2 · 2026-05-14T00:42:59.676014+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_experiment-summary-table_20260514T003543",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-14T00:42:59.676220+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "exec-sim-repair-verifier",
  "fields": "['*']",
  "limit": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_experiment-summary-table_20260514T003543",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "exec-sim-repair-verifier",
    "fields": "['*']",
    "limit": "0"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-14T00:42:59.676873+00:00_

Error: result (103,670 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/cd03d944-31d8-4706-ad87-0759b31a8651/tool-results/mcp-agent-ml-research-read_registry-1778718961321.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/cd03d944-31d8-4706-ad87-0759b31a8651/tool-results/mcp-agent-ml-research-read_registry-1778718961321.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/cd03d944-31d8-4706-ad87-0759b31a8651/tool-results/mcp-agent-ml-research-read_registry-1778718961321.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_experiment-summary-table_20260514T003543",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-14T00:42:59.677115+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

````json
{
  "description": "Parse registry and extract success experiments",
  "prompt": "You have a large JSON file at:\n/home/ubuntu/.claude-account-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/cd03d944-31d8-4706-ad87-0759b31a8651/tool-results/mcp-agent-ml-research-read_registry-1778718961321.txt\n\nThe file has schema: {result: string} where `result` is a JSON string that needs to be parsed.\n\nYour task:\n1. First probe the structure with jq (type/length/keys)\n2. Parse the nested JSON string in \"result\" \n3. Extract ALL experiments (not just success) - I need every experiment's data to build comprehensive tables\n4. For each experiment, extract these fields (use null if missing):\n   - exp_id\n   - hypothesis (first 80 chars)\n   - model_name\n   - seed\n   - formulation (cls/cwm/traj or whatever is there)\n   - level (function/repo)\n   - status\n   - conclusion\n   - accuracy\n   - f1_macro\n   - pass_f1, fail_f1\n   - pass_precision, pass_recall, fail_precision, fail_recall\n   - unparseable_pct\n   - exact_match_rate\n   - test_set_size\n   - Any other metrics fields present\n   - tags or labels if present\n   - notes if present\n\nWrite a Python script that:\n- Reads and parses the JSON file\n- Extracts all experiments into a structured format\n- Saves the output as a clean JSON file at /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/all_experiments_parsed.json\n\nThen print a COMPLETE dump of every experiment's extracted data to stdout so I can see all of it. Do NOT summarize - print the full structured data for every single experiment. Use a format like:\n\n```\n=== EXP: exp_id ===\nconclusion: ...\nstatus: ...\nmodel: ...\nseed: ...\nformulation: ...\nlevel: ...\naccuracy: ...\nf1_macro: ...\npass_f1: ... fail_f1: ...\npass_precision: ... pass_recall: ...\nfail_precision: ... fail_recall: ...\nunparseable_pct: ...\nexact_match_rate: ...\ntest_set_size: ...\nhypothesis: ...\ntags: ...\nnotes: ...\nall_metrics: {full metrics dict}\n```\n\nPrint ALL experiments, every single one. This is critical - do not skip or summarize any."
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "worker_analysis_experiment-summary-table_20260514T003543",
  "tool": "Agent",
  "tool_args": {
    "description": "Parse registry and extract success experiments",
    "prompt": "You have a large JSON file at:\n/home/ubuntu/.claude-account-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/cd03d944-31d8-4706-ad87-0759b31a8651/tool-results/mcp-agent-ml-research-read_registry-1778718961321.txt\n\nThe file has schema: {result: string} where `result` is a JSON string that needs to be parsed.\n\nYour task:\n1. First probe the structure with jq (type/length/keys)\n2. Parse the nested JSON string in \"result\" \n3. Extract ALL experiments (not just success) - I need every experiment's data to build comprehensive tables\n4. For each experiment, extract these fields (use null if missing):\n   - exp_id\n   - hypothesis (first 80 chars)\n   - model_name\n   - seed\n   - formulation (cls/cwm/traj or whatever is there)\n   - level (function/repo)\n   - status\n   - conclusion\n   - accuracy\n   - f1_macro\n   - pass_f1, fail_f1\n   - pass_precision, pass_recall, fail_precision, fail_recall\n   - unparseable_pct\n   - exact_match_rate\n   - test_set_size\n   - Any other metrics fields present\n   - tags or labels if present\n   - notes if present\n\nWrite a Python script that:\n- Reads and parses the JSON file\n- Extracts all experiments into a structured format\n- Saves the output as a clean JSON file at /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/all_experiments_parsed.json\n\nThen print a COMPLETE dump of every experiment's extracted data to stdout so I can see all of it. Do NOT summarize - print the full structured data for every single experiment. Use a format like:\n\n```\n=== EXP: exp_id ===\nconclusion: ...\nstatus: ...\nmodel: ...\nseed: ...\nformulation: ...\nlevel: ...\naccuracy: ...\nf1_macro: ...\npass_f1: ... fail_f1: ...\npass_precision: ... pass_recall: ...\nfail_precision: ... fail_recall: ...\nunparseable_pct: ...\nexact_match_rate: ...\ntest_set_size: ...\nhypothesis: ...\ntags: ...\nnotes: ...\nall_metrics: {full metrics dict}\n```\n\nPrint ALL experiments, every single one. This is critical - do not skip or summarize any."
  }
}
````

</details>

---

### Tool call

_source line 6 · 2026-05-14T00:42:59.677324+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.claude-account-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/cd03d944-31d8-4706-ad87-0759b31a8651/tool-results && ls -la mcp-agent-ml-research-read_registry-1778718961321.txt | awk '{print $5}'",
  "description": "Check file size"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_experiment-summary-table_20260514T003543",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.claude-account-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/cd03d944-31d8-4706-ad87-0759b31a8651/tool-results && ls -la mcp-agent-ml-research-read_registry-1778718961321.txt | awk '{print $5}'",
    "description": "Check file size"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-14T00:42:59.677458+00:00_

110217

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_experiment-summary-table_20260514T003543",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-14T00:42:59.677593+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "FILE=\"/home/ubuntu/.claude-account-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/cd03d944-31d8-4706-ad87-0759b31a8651/tool-results/mcp-agent-ml-research-read_registry-1778718961321.txt\"\n# Top-level structure\necho \"=== TOP LEVEL TYPE ===\"\ncat \"$FILE\" | python3 -c \"import json,sys; d=json.load(sys.stdin); print(type(d), list(d.keys()) if isinstance(d,dict) else len(d))\"\necho \"=== RESULT TYPE ===\"\ncat \"$FILE\" | python3 -c \"import json,sys; d=json.load(sys.stdin); r=d.get('result',''); print(type(r), len(r) if isinstance(r,str) else 'not str')\"\necho \"=== PARSED RESULT TYPE ===\"\ncat \"$FILE\" | python3 -c \"\nimport json,sys\nd=json.load(sys.stdin)\nr=json.loads(d['result'])\nprint(type(r))\nif isinstance(r,dict):\n    print('keys:', list(r.keys())[:20])\nelif isinstance(r,list):\n    print('length:', len(r))\n\"",
  "description": "Probe JSON structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_experiment-summary-table_20260514T003543",
  "tool": "Bash",
  "tool_args": {
    "command": "FILE=\"/home/ubuntu/.claude-account-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/cd03d944-31d8-4706-ad87-0759b31a8651/tool-results/mcp-agent-ml-research-read_registry-1778718961321.txt\"\n# Top-level structure\necho \"=== TOP LEVEL TYPE ===\"\ncat \"$FILE\" | python3 -c \"import json,sys; d=json.load(sys.stdin); print(type(d), list(d.keys()) if isinstance(d,dict) else len(d))\"\necho \"=== RESULT TYPE ===\"\ncat \"$FILE\" | python3 -c \"import json,sys; d=json.load(sys.stdin); r=d.get('result',''); print(type(r), len(r) if isinstance(r,str) else 'not str')\"\necho \"=== PARSED RESULT TYPE ===\"\ncat \"$FILE\" | python3 -c \"\nimport json,sys\nd=json.load(sys.stdin)\nr=json.loads(d['result'])\nprint(type(r))\nif isinstance(r,dict):\n    print('keys:', list(r.keys())[:20])\nelif isinstance(r,list):\n    print('length:', len(r))\n\"",
    "description": "Probe JSON structure"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-14T00:42:59.677721+00:00_

=== TOP LEVEL TYPE ===
&lt;class 'dict'> ['result']
=== RESULT TYPE ===
&lt;class 'str'> 96847
=== PARSED RESULT TYPE ===
&lt;class 'dict'>
keys: ['success', 'data', 'error', 'metadata']

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_experiment-summary-table_20260514T003543",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-14T00:42:59.677876+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "FILE=\"/home/ubuntu/.claude-account-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/cd03d944-31d8-4706-ad87-0759b31a8651/tool-results/mcp-agent-ml-research-read_registry-1778718961321.txt\"\ncat \"$FILE\" | python3 -c \"\nimport json,sys\nd=json.load(sys.stdin)\nr=json.loads(d['result'])\nprint('success:', r.get('success'))\nprint('error:', r.get('error'))\nprint('metadata:', r.get('metadata'))\ndata = r.get('data', {})\nprint('data type:', type(data))\nif isinstance(data, dict):\n    print('data keys:', list(data.keys())[:30])\n    for k in list(data.keys())[:3]:\n        print(f'  data[\\\"{k}\\\"] type:', type(data[k]))\n        if isinstance(data[k], dict):\n            print(f'    keys:', list(data[k].keys())[:20])\nelif isinstance(data, list):\n    print('data length:', len(data))\n    if data:\n        print('first item type:', type(data[0]))\n        if isinstance(data[0], dict):\n            print('first item keys:', list(data[0].keys())[:20])\n\"",
  "description": "Explore data structure deeper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_experiment-summary-table_20260514T003543",
  "tool": "Bash",
  "tool_args": {
    "command": "FILE=\"/home/ubuntu/.claude-account-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/cd03d944-31d8-4706-ad87-0759b31a8651/tool-results/mcp-agent-ml-research-read_registry-1778718961321.txt\"\ncat \"$FILE\" | python3 -c \"\nimport json,sys\nd=json.load(sys.stdin)\nr=json.loads(d['result'])\nprint('success:', r.get('success'))\nprint('error:', r.get('error'))\nprint('metadata:', r.get('metadata'))\ndata = r.get('data', {})\nprint('data type:', type(data))\nif isinstance(data, dict):\n    print('data keys:', list(data.keys())[:30])\n    for k in list(data.keys())[:3]:\n        print(f'  data[\\\"{k}\\\"] type:', type(data[k]))\n        if isinstance(data[k], dict):\n            print(f'    keys:', list(data[k].keys())[:20])\nelif isinstance(data, list):\n    print('data length:', len(data))\n    if data:\n        print('first item type:', type(data[0]))\n        if isinstance(data[0], dict):\n            print('first item keys:', list(data[0].keys())[:20])\n\"",
    "description": "Explore data structure deeper"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-14T00:42:59.678019+00:00_

success: True
error: None
metadata: {'elapsed_seconds': 0.215}
data type: &lt;class 'dict'>
data keys: ['experiments', 'count', 'total', 'baseline']
  data["experiments"] type: &lt;class 'dict'>
    keys: ['repo-level-cls-8b-conda', 'repo-level-cwm-v11', 'repo-level-cls-v5-conda', 'repo-level-cwm-seed123-conda', 'repo-level-cls-seed123-home', 'repo-level-cwm-v12', 'repo-level-cwm-seed123', 'repo-level-cls-8b', 'repo-level-cls-seed123', 'repo-level-cls-v5', 'repo-level-cwm-v10', 'repo-level-cls-v4', 'repo-level-cwm-v9', 'repo-level-cls-v3', 'repo-level-cls-v2', 'repo-level-cwm-v7', 'repo-level-cls-home', 'repo-level-cwm-v8', 'repo-level-cwm-v6', 'cwm8b-seed123']
  data["count"] type: &lt;class 'int'>
  data["total"] type: &lt;class 'int'>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_experiment-summary-table_20260514T003543",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-14T00:42:59.678155+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "FILE=\"/home/ubuntu/.claude-account-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/cd03d944-31d8-4706-ad87-0759b31a8651/tool-results/mcp-agent-ml-research-read_registry-1778718961321.txt\"\ncat \"$FILE\" | python3 -c \"\nimport json,sys\nd=json.load(sys.stdin)\nr=json.loads(d['result'])\ndata = r['data']\nexps = data['experiments']\nprint('count:', data['count'], 'total:', data['total'])\nprint('baseline:', json.dumps(data.get('baseline'), indent=2)[:500] if data.get('baseline') else 'None')\nprint()\n# Show full keys for first experiment\nfirst_key = list(exps.keys())[0]\nprint(f'=== First exp: {first_key} ===')\nprint(json.dumps(exps[first_key], indent=2)[:2000])\n\"",
  "description": "Examine experiment structure and baseline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_experiment-summary-table_20260514T003543",
  "tool": "Bash",
  "tool_args": {
    "command": "FILE=\"/home/ubuntu/.claude-account-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/cd03d944-31d8-4706-ad87-0759b31a8651/tool-results/mcp-agent-ml-research-read_registry-1778718961321.txt\"\ncat \"$FILE\" | python3 -c \"\nimport json,sys\nd=json.load(sys.stdin)\nr=json.loads(d['result'])\ndata = r['data']\nexps = data['experiments']\nprint('count:', data['count'], 'total:', data['total'])\nprint('baseline:', json.dumps(data.get('baseline'), indent=2)[:500] if data.get('baseline') else 'None')\nprint()\n# Show full keys for first experiment\nfirst_key = list(exps.keys())[0]\nprint(f'=== First exp: {first_key} ===')\nprint(json.dumps(exps[first_key], indent=2)[:2000])\n\"",
    "description": "Examine experiment structure and baseline"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-14T00:42:59.678298+00:00_

count: 59 total: 59
baseline: None

=== First exp: repo-level-cls-8b-conda ===
{
  "status": "RUNNING",
  "retry_count": 0,
  "created_at": "2026-05-13T22:07:02.272Z",
  "updated_at": "2026-05-13T22:59:26.673Z",
  "spec": {
    "hypothesis": "CLS 8B conda \u91cd\u8bad (transformers 4.57.6)\uff0c\u4e0e CLS v5 (4B) \u540c\u73af\u5883\u5bf9\u6bd4\uff0c\u9a8c\u8bc1 repo-level scaling effect\u3002\u4e4b\u524d 8B \u5728 transformers 5.8.0 \u8bad\u7ec3\u7ed3\u679c\u65e0\u6548 (71.37%)\u3002",
    "server": "westd-48478",
    "gpu": "cuda:3",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /home/sonny/exec-sim-repair-verifier && CUDA_VISIBLE_DEVICES=3 python3 train_repo_verifier.py --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/ --device cuda:0 --batch_size 1 --grad_accumulation 32 --seed 42 --no_wandb --output_dir /root/autodl-tmp/checkpoints_repo_cls_8b_conda/ --run_name repo-cls-qwen3-8b-conda",
    "data_path": "/home/sonny/exec-sim-repair-verifier/data/swebench_full/",
    "data_count": 70748,
    "model_name": "Qwen/Qwen3-8B",
    "seed": 42,
    "learning_rate": 5e-05,
    "weight_decay": 0.01,
    "warmup_ratio": 0.05,
    "save_steps": 200,
    "eval_steps": 200,
    "save_total_limit": 5,
    "num_train_epochs": 3,
    "lora_rank": 16,
    "lora_alpha": 32,
    "batch_size": 1,
    "grad_accumulation": 32,
    "max_seq_length": 2048,
    "checkpoint_path": "/root/autodl-tmp/checkpoints_repo_cls_8b_conda/",
    "log_path": "/root/autodl-tmp/checkpoints_repo_cls_8b_conda/train.log",
    "env": "conda base, transformers 4.57.6",
    "pid": 185438,
    "account": "root",
    "total_steps": 6633,
    "speed": "~8.3s/step",
    "estimated_hours": 15.3,
    "gpu_mem_used": "25751/32607 MiB",
    "tmux_session": "cls8b-conda"
  }
}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_experiment-summary-table_20260514T003543",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-14T00:42:59.678447+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "FILE=\"/home/ubuntu/.claude-account-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/cd03d944-31d8-4706-ad87-0759b31a8651/tool-results/mcp-agent-ml-research-read_registry-1778718961321.txt\"\ncat \"$FILE\" | python3 -c \"\nimport json,sys\nd=json.load(sys.stdin)\nr=json.loads(d['result'])\nexps = r['data']['experiments']\n# Show all experiment keys and their status\nfor k,v in exps.items():\n    print(f'{k}: status={v.get(\\\"status\\\")}, has_result={\\\"result\\\" in v}')\n\"",
  "description": "List all experiments with status"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_experiment-summary-table_20260514T003543",
  "tool": "Bash",
  "tool_args": {
    "command": "FILE=\"/home/ubuntu/.claude-account-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/cd03d944-31d8-4706-ad87-0759b31a8651/tool-results/mcp-agent-ml-research-read_registry-1778718961321.txt\"\ncat \"$FILE\" | python3 -c \"\nimport json,sys\nd=json.load(sys.stdin)\nr=json.loads(d['result'])\nexps = r['data']['experiments']\n# Show all experiment keys and their status\nfor k,v in exps.items():\n    print(f'{k}: status={v.get(\\\"status\\\")}, has_result={\\\"result\\\" in v}')\n\"",
    "description": "List all experiments with status"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-14T00:42:59.678581+00:00_

repo-level-cls-8b-conda: status=RUNNING, has_result=False
repo-level-cwm-v11: status=DONE, has_result=False
repo-level-cls-v5-conda: status=RUNNING, has_result=False
repo-level-cwm-seed123-conda: status=RUNNING, has_result=False
repo-level-cls-seed123-home: status=RUNNING, has_result=False
repo-level-cwm-v12: status=RUNNING, has_result=False
repo-level-cwm-seed123: status=DONE, has_result=False
repo-level-cls-8b: status=DONE, has_result=False
repo-level-cls-seed123: status=DONE, has_result=False
repo-level-cls-v5: status=DONE, has_result=False
repo-level-cwm-v10: status=DONE, has_result=False
repo-level-cls-v4: status=DONE, has_result=False
repo-level-cwm-v9: status=DONE, has_result=False
repo-level-cls-v3: status=DONE, has_result=False
repo-level-cls-v2: status=DONE, has_result=False
repo-level-cwm-v7: status=DONE, has_result=False
repo-level-cls-home: status=DONE, has_result=False
repo-level-cwm-v8: status=DONE, has_result=False
repo-level-cwm-v6: status=DONE, has_result=False
cwm8b-seed123: status=DONE, has_result=False
cls8b-seed123: status=DONE, has_result=False
cls8b-eval-seed123: status=DONE, has_result=False
cls8b-eval-seed42: status=DONE, has_result=False
repo-level-cwm-v4: status=DONE, has_result=False
repo-level-cwm-v2: status=DONE, has_result=False
repo-level-cwm-v5: status=DONE, has_result=False
matched-seed-8b-predictions: status=DONE, has_result=False
repo-level-cwm-v3: status=DONE, has_result=False
cwm-seed789: status=DONE, has_result=False
cls8b-seed456: status=DONE, has_result=False
cwm8b-seed456: status=DONE, has_result=False
5-paired-clustered-bootstrap: status=DONE, has_result=False
repo-level-cwm: status=DONE, has_result=False
repo-level-cls: status=DONE, has_result=False
cwm-seed0: status=DONE, has_result=False
per-test-precision-recall: status=DONE, has_result=False
cwm-seed123: status=DONE, has_result=False
cwm-seed456: status=DONE, has_result=False
cls-seed0: status=DONE, has_result=False
cls-seed789: status=DONE, has_result=False
traj-leve
…[truncated 948 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_experiment-summary-table_20260514T003543",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-14T00:42:59.678729+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "FILE=\"/home/ubuntu/.claude-account-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/cd03d944-31d8-4706-ad87-0759b31a8651/tool-results/mcp-agent-ml-research-read_registry-1778718961321.txt\"\ncat \"$FILE\" | python3 -c \"\nimport json,sys\nd=json.load(sys.stdin)\nr=json.loads(d['result'])\nexps = r['data']['experiments']\n# Show a few DONE experiments fully to understand structure\nfor k in ['repo-level-cls', 'repo-level-cwm', 'cls-seed0', 'traj-level-finetuned', 'llm-judge-32b-zeroshot', 'mvp-a-oracle-sim']:\n    if k in exps:\n        print(f'=== {k} ===')\n        print(json.dumps(exps[k], indent=2)[:3000])\n        print()\n\" 2>&1 | head -300",
  "description": "Examine DONE experiments to see metrics fields"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_experiment-summary-table_20260514T003543",
  "tool": "Bash",
  "tool_args": {
    "command": "FILE=\"/home/ubuntu/.claude-account-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/cd03d944-31d8-4706-ad87-0759b31a8651/tool-results/mcp-agent-ml-research-read_registry-1778718961321.txt\"\ncat \"$FILE\" | python3 -c \"\nimport json,sys\nd=json.load(sys.stdin)\nr=json.loads(d['result'])\nexps = r['data']['experiments']\n# Show a few DONE experiments fully to understand structure\nfor k in ['repo-level-cls', 'repo-level-cwm', 'cls-seed0', 'traj-level-finetuned', 'llm-judge-32b-zeroshot', 'mvp-a-oracle-sim']:\n    if k in exps:\n        print(f'=== {k} ===')\n        print(json.dumps(exps[k], indent=2)[:3000])\n        print()\n\" 2>&1 | head -300",
    "description": "Examine DONE experiments to see metrics fields"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-14T00:42:59.678965+00:00_

=== repo-level-cls ===
{
  "status": "DONE",
  "retry_count": 1,
  "created_at": "2026-05-12T11:07:29.362Z",
  "updated_at": "2026-05-12T14:12:05.932Z",
  "hypothesis": "Repo-level (SWE-bench) classification verifier \u2014 \u9a8c\u8bc1 per-test classification \u4ece\u51fd\u6570\u7ea7 (HumanEval/MBPP) \u6269\u5c55\u5230 repo-level \u7684\u6cdb\u5316\u80fd\u529b\uff0c\u4f7f\u7528 max_seq_length=4096 \u548c class weighting \u5904\u7406 85/15 \u4e0d\u5e73\u8861",
  "reproduce": {
    "finished_at": "2026-05-12T11:24:07.920Z"
  },
  "failure_reason": "EXIT_CODE=1 (generic error \u2014 check log tail)",
  "completed_at": "2026-05-12T11:24:09.838Z",
  "extra": {
    "hook_events": [
      {
        "event": "on_failed",
        "action": "agent",
        "ts": "2026-05-12T11:24:11.030736+00:00"
      }
    ],
    "previous_failure": {
      "conclusion": "failed",
      "notes": "\u5931\u8d25\u539f\u56e0: KeyError: 'sample_weight' \u2014 train_repo_verifier.py:124 compute_loss \u5c1d\u8bd5 inputs.pop(\"sample_weight\") \u4f46 Dataset/Collator \u672a\u63d0\u4f9b\u8be5\u5b57\u6bb5\u3002\u4ee3\u7801 bug\uff0c\u975e infra/resource \u95ee\u9898\u3002\u4e0e repo-level-cwm \u540c\u4e00 root cause\u3002\u4fee\u590d\uff1aDataset.__getitem__ \u9700\u8981\u8fd4\u56de sample_weight \u5b57\u6bb5\uff0c\u6216 Collator \u9700\u8981\u4f20\u9012\u8be5\u5b57\u6bb5\u3002"
    }
  },
  "notes": "\u5931\u8d25\u539f\u56e0: KeyError: 'sample_weight' \u2014 train_repo_verifier.py:124 compute_loss \u5c1d\u8bd5 inputs.pop(\"sample_weight\") \u4f46 Dataset/Collator \u672a\u63d0\u4f9b\u8be5\u5b57\u6bb5\u3002\u4ee3\u7801 bug\uff0c\u975e infra/resource \u95ee\u9898\u3002\u4e0e repo-level-cwm \u540c\u4e00 root cause\u3002\u4fee\u590d\uff1aDataset.__getitem__ \u9700\u8981\u8fd4\u56de sample_weight \u5b57\u6bb5\uff0c\u6216 Collator \u9700\u8981\u4f20\u9012\u8be5\u5b57\u6bb5\u3002",
  "spec": {
    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME
…[truncated 12894 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_experiment-summary-table_20260514T003543",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-14T00:42:59.679130+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/",
  "description": "Check artifacts directory exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_experiment-summary-table_20260514T003543",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/",
    "description": "Check artifacts directory exists"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-14T00:42:59.679304+00:00_

4b_8b_cls_cwm_paired_bootstrap_corrected.json
_project
analysis_5paired_bootstrap.py
block-corr-empirical
block_correlation_analysis.py
cwm8b_seed123_analysis.txt
cwm_v6_diagnosis.md
cwm_v6_health_check.md
d008_eval_commands.md
diag_cls_v4.md
diag_cwm_v10.md
dream_reports
error_overlap_matched_seed.json
eval_pipeline_prep.md
eval_readiness_report.md
extract_predictions_generic.py
figures
manifest.yaml
mvp-a-oracle-sim
mvp-b-data-prep
oracle-f2p-stratified
p2p-regression-rate
paper_materials.md
repo_8b_training_plan.md
repo_level_failure_diagnosis.md
seed123_launch_configs.md
seed123_launch_plan.md
swebench_pipeline_design.md
training_progress_20260512.md
val_truncation_label_bias_analysis.md
westd_48478_readiness.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_experiment-summary-table_20260514T003543",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-14T00:42:59.679476+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/parse_all_experiments.py",
  "content": "#!/usr/bin/env python3\n\"\"\"Parse all experiments from registry JSON and output structured data.\"\"\"\n\nimport json\nimport sys\n\nINPUT_FILE = \"/home/ubuntu/.claude-account-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/cd03d944-31d8-4706-ad87-0759b31a8651/tool-results/mcp-agent-ml-research-read_registry-1778718961321.txt\"\nOUTPUT_FILE = \"/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/all_experiments_parsed.json\"\n\n\ndef extract_experiment(exp_id, exp_data):\n    \"\"\"Extract all fields from one experiment into a flat dict.\"\"\"\n    spec = exp_data.get(\"spec\", {})\n    metrics = exp_data.get(\"metrics\", {})\n    extra = exp_data.get(\"extra\", {})\n\n    # Determine formulation from exp_id\n    formulation = None\n    eid_lower = exp_id.lower()\n    if \"cls\" in eid_lower:\n        formulation = \"cls\"\n    elif \"cwm\" in eid_lower:\n        formulation = \"cwm\"\n    elif \"traj\" in eid_lower:\n        formulation = \"traj\"\n    elif \"judge\" in eid_lower:\n        formulation = \"llm-judge\"\n    elif \"oracle\" in eid_lower:\n        formulation = \"oracle-sim\"\n    elif \"bootstrap\" in eid_lower or \"voting\" in eid_lower or \"corr\" in eid_lower:\n        formulation = \"analysis\"\n    elif \"p2p\" in eid_lower or \"mvp\" in eid_lower:\n        formulation = \"analysis\"\n    else:\n        formulation = \"other\"\n\n    # Determine level\n    level = None\n    if \"repo-level\" in eid_lower or \"repo\" in eid_lower:\n        level = \"repo\"\n    elif \"traj\" in eid_lower:\n        level = \"trajectory\"\n    elif any(x in eid_lower for x in [\"cls-seed\", \"cwm-seed\", \"cls8b\", \"cwm8b\", \"cwm-baseline\"]):\n        level = \"function\"\n    elif \"judge\" in eid_lower:\n        level = \"function\"\n    else:\n        level = spec.get(\"level\", \"function\")\n\n    hypothesis = exp_data.get(\"hypothesis\", spec.get(\"hypothesis\", \"\"))\n\n    result = {\n        \"exp_id\": exp_id,\n        \"status\": exp_data.get(\"status\"),\n        \"conclusion\": exp_data.get(\"conclusion\"),\n        \"hypothesis\": hypothesis,\n        \"hypothesis_short\": (hypothesis[:80] + \"...\") if len(hypothesis) > 80 else hypothesis,\n        \"model_name\": spec.get(\"model_name\"),\n        \"seed\": spec.get(\"seed\"),\n        \"formulation\": formulation,\n        \"level\": level,\n        # Core metrics\n        \"accuracy\": metrics.get(\"accuracy\") or metrics.get(\"overall_accuracy\"),\n        \"f1_macro\": metrics.get(\"f1_macro\"),\n        \"pass_f1\": metrics.get(\"pass_f1\"),\n        \"fail_f1\": metrics.get(\"fail_f1\"),\n        \"pass_precision\": metrics.get(\"pass_precision\"),\n        \"pass_recall\": metrics.get(\"pass_recall\"),\n        \"fail_precision\": metrics.get(\"fail_precision\"),\n        \"fail_recall\": metrics.get(\"fail_recall\"),\n        \"unparseable_pct\": metrics.get(\"unparseable\") if metrics.get(\"unparseable\") is not None else metrics.get(\"unparseable_predictions\") if metrics.get(\"unparseable_predictions\") is not None else metrics.get(\"unparseable_pct\"),\n        \"exact_match_rate\": metrics.get(\"exact_match_rate\"),\n        \"test_set_size\": spec.get(\"data_count\"),\n        # Additional metrics\n        \"train_loss\": metrics.get(\"train_loss\"),\n        \"eval_loss\": metrics.get(\"eval_loss\"),\n        \"train_runtime_sec\": metrics.get(\"train_runtime_sec\"),\n        \"majority_baseline\": metrics.get(\"majority_baseline\"),\n        \"accuracy_vs_baseline_gap\": metrics.get(\"accuracy_vs_baseline_gap\"),\n        \"trajectory_accuracy\": metrics.get(\"trajectory_accuracy\"),\n        \"unresolved_f1\": metrics.get(\"unresolved_f1\"),\n        \"resolved_f1\": metrics.get(\"resolved_f1\"),\n        \"per_test_consistency\": metrics.get(\"per_test_consistency\"),\n        # All raw metrics\n        \"all_metrics\": metrics if metrics else None,\n        # Spec details\n        \"server\": spec.get(\"server\"),\n        \"gpu\": spec.get(\"gpu\"),\n        \"checkpoint_path\": spec.get(\"checkpoint_path\"),\n        \"data_path\": spec.get(\"data_path\"),\n        \"learning_rate\": spec.get(\"learning_rate\") or spec.get(\"lr\"),\n        \"batch_size\": spec.get(\"batch_size\"),\n        \"grad_accumulation\": spec.get(\"grad_accumulation\"),\n        \"max_seq_length\": spec.get(\"max_seq_length\"),\n        \"num_train_epochs\": spec.get(\"num_train_epochs\") or spec.get(\"epochs\"),\n        \"lora_rank\": spec.get(\"lora_rank\"),\n        \"lora_alpha\": spec.get(\"lora_alpha\"),\n        \"wall_clock_seconds\": spec.get(\"wall_clock_seconds\"),\n        \"gpu_hours\": spec.get(\"gpu_hours\"),\n        \"hyperparams\": spec.get(\"hyperparams\"),\n        # Metadata\n        \"tags\": exp_data.get(\"tags\"),\n        \"notes\": exp_data.get(\"notes\"),\n        \"failure_reason\": exp_data.get(\"failure_reason\"),\n        \"created_at\": exp_data.get(\"created_at\"),\n        \"updated_at\": exp_data.get(\"updated_at\"),\n        \"completed_at\": exp_data.get(\"completed_at\"),\n        \"retry_count\": exp_data.get(\"retry_count\"),\n        \"parent\": exp_data.get(\"parent\"),\n        \"extra\": extra if extra else None,\n    }\n    return result\n\n\ndef main():\n    with open(INPUT_FILE, \"r\") as f:\n        raw = json.load(f)\n\n    inner = json.loads(raw[\"result\"])\n    experiments_dict = inner[\"data\"][\"experiments\"]\n\n    all_experiments = []\n    for exp_id, exp_data in experiments_dict.items():\n        parsed = extract_experiment(exp_id, exp_data)\n        all_experiments.append(parsed)\n\n    # Save clean JSON\n    with open(OUTPUT_FILE, \"w\") as f:\n        json.dump(all_experiments, f, indent=2, ensure_ascii=False)\n\n    print(f\"Total experiments: {len(all_experiments)}\")\n    print(f\"Saved to: {OUTPUT_FILE}\")\n    print()\n\n    # Print COMPLETE dump of every experiment\n    for exp in all_experiments:\n        print(f\"=== EXP: {exp['exp_id']} ===\")\n        print(f\"  conclusion: {exp['conclusion']}\")\n        print(f\"  status: {exp['status']}\")\n        print(f\"  model: {exp['model_name']}\")\n        print(f\"  seed: {exp['seed']}\")\n        print(f\"  formulation: {exp['formulation']}\")\n        print(f\"  level: {exp['level']}\")\n        print(f\"  accuracy: {exp['accuracy']}\")\n        print(f\"  f1_macro: {exp['f1_macro']}\")\n        print(f\"  pass_f1: {exp['pass_f1']}  fail_f1: {exp['fail_f1']}\")\n        print(f\"  pass_precision: {exp['pass_precision']}  pass_recall: {exp['pass_recall']}\")\n        print(f\"  fail_precision: {exp['fail_precision']}  fail_recall: {exp['fail_recall']}\")\n        print(f\"  unparseable_pct: {exp['unparseable_pct']}\")\n        print(f\"  exact_match_rate: {exp['exact_match_rate']}\")\n        print(f\"  test_set_size: {exp['test_set_size']}\")\n        print(f\"  train_loss: {exp['train_loss']}  eval_loss: {exp['eval_loss']}\")\n        print(f\"  majority_baseline: {exp['majority_baseline']}\")\n        print(f\"  trajectory_accuracy: {exp['trajectory_accuracy']}\")\n        print(f\"  unresolved_f1: {exp['unresolved_f1']}  resolved_f1: {exp['resolved_f1']}\")\n        print(f\"  per_test_consistency: {exp['per_test_consistency']}\")\n        print(f\"  wall_clock_sec: {exp['wall_clock_seconds']}  gpu_hours: {exp['gpu_hours']}\")\n        print(f\"  server: {exp['server']}  gpu: {exp['gpu']}\")\n        print(f\"  lr: {exp['learning_rate']}  batch: {exp['batch_size']}  grad_accum: {exp['grad_accumulation']}\")\n        print(f\"  max_seq_len: {exp['max_seq_length']}  epochs: {exp['num_train_epochs']}\")\n        print(f\"  lora_rank: {exp['lora_rank']}  lora_alpha: {exp['lora_alpha']}\")\n        print(f\"  hyperparams: {json.dumps(exp['hyperparams'], ensure_ascii=False) if exp['hyperparams'] else None}\")\n        print(f\"  hypothesis: {exp['hypothesis_short']}\")\n        print(f\"  tags: {exp['tags']}\")\n        print(f\"  notes: {exp['notes']}\")\n        print(f\"  failure_reason: {exp['failure_reason']}\")\n        print(f\"  created_at: {exp['created_at']}\")\n        print(f\"  completed_at: {exp['completed_at']}\")\n        print(f\"  retry_count: {exp['retry_count']}\")\n        print(f\"  parent: {exp['parent']}\")\n        print(f\"  all_metrics: {json.dumps(exp['all_metrics'], indent=4, ensure_ascii=False) if exp['all_metrics'] else None}\")\n        print()\n\n\nif __name__ == \"__main__\":\n    main()\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_experiment-summary-table_20260514T003543",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/parse_all_experiments.py",
    "content": "#!/usr/bin/env python3\n\"\"\"Parse all experiments from registry JSON and output structured data.\"\"\"\n\nimport json\nimport sys\n\nINPUT_FILE = \"/home/ubuntu/.claude-account-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/cd03d944-31d8-4706-ad87-0759b31a8651/tool-results/mcp-agent-ml-research-read_registry-1778718961321.txt\"\nOUTPUT_FILE = \"/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/all_experiments_parsed.json\"\n\n\ndef extract_experiment(exp_id, exp_data):\n    \"\"\"Extract all fields from one experiment into a flat dict.\"\"\"\n    spec = exp_data.get(\"spec\", {})\n    metrics = exp_data.get(\"metrics\", {})\n    extra = exp_data.get(\"extra\", {})\n\n    # Determine formulation from exp_id\n    formulation = None\n    eid_lower = exp_id.lower()\n    if \"cls\" in eid_lower:\n        formulation = \"cls\"\n    elif \"cwm\" in eid_lower:\n        formulation = \"cwm\"\n    elif \"traj\" in eid_lower:\n        formulation = \"traj\"\n    elif \"judge\" in eid_lower:\n        formulation = \"llm-judge\"\n    elif \"oracle\" in eid_lower:\n        formulation = \"oracle-sim\"\n    elif \"bootstrap\" in eid_lower or \"voting\" in eid_lower or \"corr\" in eid_lower:\n        formulation = \"analysis\"\n    elif \"p2p\" in eid_lower or \"mvp\" in eid_lower:\n        formulation = \"analysis\"\n    else:\n        formulation = \"other\"\n\n    # Determine level\n    level = None\n    if \"repo-level\" in eid_lower or \"repo\" in eid_lower:\n        level = \"repo\"\n    elif \"traj\" in eid_lower:\n        level = \"trajectory\"\n    elif any(x in eid_lower for x in [\"cls-seed\", \"cwm-seed\", \"cls8b\", \"cwm8b\", \"cwm-baseline\"]):\n        level = \"function\"\n    elif \"judge\" in eid_lower:\n        level = \"function\"\n    else:\n        level = spec.get(\"level\", \"function\")\n\n    hypothesis = exp_data.get(\"hypothesis\", spec.get(\"hypothesis\", \"\"))\n\n    result = {\n        \"exp_id\": exp_id,\n        \"status\": exp_data.get(\"status\"),\n        \"conclusion\": exp_data.get(\"conclusion\"),\n        \"hypothesis\": hypothesis,\n        \"hypothesis_short\": (hypothesis[:80] + \"...\") if len(hypothesis) > 80 else hypothesis,\n        \"model_name\": spec.get(\"model_name\"),\n        \"seed\": spec.get(\"seed\"),\n        \"formulation\": formulation,\n        \"level\": level,\n        # Core metrics\n        \"accuracy\": metrics.get(\"accuracy\") or metrics.get(\"overall_accuracy\"),\n        \"f1_macro\": metrics.get(\"f1_macro\"),\n        \"pass_f1\": metrics.get(\"pass_f1\"),\n        \"fail_f1\": metrics.get(\"fail_f1\"),\n        \"pass_precision\": metrics.get(\"pass_precision\"),\n        \"pass_recall\": metrics.get(\"pass_recall\"),\n        \"fail_precision\": metrics.get(\"fail_precision\"),\n        \"fail_recall\": metrics.get(\"fail_recall\"),\n        \"unparseable_pct\": metrics.get(\"unparseable\") if metrics.get(\"unparseable\") is not None else metrics.get(\"unparseable_predictions\") if metrics.get(\"unparseable_predictions\") is not None else metrics.get(\"unparseable_pct\"),\n        \"exact_match_rate\": metrics.get(\"exact_match_rate\"),\n        \"test_set_size\": spec.get(\"data_count\"),\n        # Additional metrics\n        \"train_loss\": metrics.get(\"train_loss\"),\n        \"eval_loss\": metrics.get(\"eval_loss\"),\n        \"train_runtime_sec\": metrics.get(\"train_runtime_sec\"),\n        \"majority_baseline\": metrics.get(\"majority_baseline\"),\n        \"accuracy_vs_baseline_gap\": metrics.get(\"accuracy_vs_baseline_gap\"),\n        \"trajectory_accuracy\": metrics.get(\"trajectory_accuracy\"),\n        \"unresolved_f1\": metrics.get(\"unresolved_f1\"),\n        \"resolved_f1\": metrics.get(\"resolved_f1\"),\n        \"per_test_consistency\": metrics.get(\"per_test_consistency\"),\n        # All raw metrics\n        \"all_metrics\": metrics if metrics else None,\n        # Spec details\n        \"server\": spec.get(\"server\"),\n        \"gpu\": spec.get(\"gpu\"),\n        \"checkpoint_path\": spec.get(\"checkpoint_path\"),\n        \"data_path\": spec.get(\"data_path\"),\n        \"learning_rate\": spec.get(\"learning_rate\") or spec.get(\"lr\"),\n        \"batch_size\": spec.get(\"batch_size\"),\n        \"grad_accumulation\": spec.get(\"grad_accumulation\"),\n        \"max_seq_length\": spec.get(\"max_seq_length\"),\n        \"num_train_epochs\": spec.get(\"num_train_epochs\") or spec.get(\"epochs\"),\n        \"lora_rank\": spec.get(\"lora_rank\"),\n        \"lora_alpha\": spec.get(\"lora_alpha\"),\n        \"wall_clock_seconds\": spec.get(\"wall_clock_seconds\"),\n        \"gpu_hours\": spec.get(\"gpu_hours\"),\n        \"hyperparams\": spec.get(\"hyperparams\"),\n        # Metadata\n        \"tags\": exp_data.get(\"tags\"),\n        \"notes\": exp_data.get(\"notes\"),\n        \"failure_reason\": exp_data.get(\"failure_reason\"),\n        \"created_at\": exp_data.get(\"created_at\"),\n        \"updated_at\": exp_data.get(\"updated_at\"),\n        \"completed_at\": exp_data.get(\"completed_at\"),\n        \"retry_count\": exp_data.get(\"retry_count\"),\n        \"parent\": exp_data.get(\"parent\"),\n        \"extra\": extra if extra else None,\n    }\n    return result\n\n\ndef main():\n    with open(INPUT_FILE, \"r\") as f:\n        raw = json.load(f)\n\n    inner = json.loads(raw[\"result\"])\n    experiments_dict = inner[\"data\"][\"experiments\"]\n\n    all_experiments = []\n    for exp_id, exp_data in experiments_dict.items():\n        parsed = extract_experiment(exp_id, exp_data)\n        all_experiments.append(parsed)\n\n    # Save clean JSON\n    with open(OUTPUT_FILE, \"w\") as f:\n        json.dump(all_experiments, f, indent=2, ensure_ascii=False)\n\n    print(f\"Total experiments: {len(all_experiments)}\")\n    print(f\"Saved to: {OUTPUT_FILE}\")\n    print()\n\n    # Print COMPLETE dump of every experiment\n    for exp in all_experiments:\n        print(f\"=== EXP: {exp['exp_id']} ===\")\n        print(f\"  conclusion: {exp['conclusion']}\")\n        print(f\"  status: {exp['status']}\")\n        print(f\"  model: {exp['model_name']}\")\n        print(f\"  seed: {exp['seed']}\")\n        print(f\"  formulation: {exp['formulation']}\")\n        print(f\"  level: {exp['level']}\")\n        print(f\"  accuracy: {exp['accuracy']}\")\n        print(f\"  f1_macro: {exp['f1_macro']}\")\n        print(f\"  pass_f1: {exp['pass_f1']}  fail_f1: {exp['fail_f1']}\")\n        print(f\"  pass_precision: {exp['pass_precision']}  pass_recall: {exp['pass_recall']}\")\n        print(f\"  fail_precision: {exp['fail_precision']}  fail_recall: {exp['fail_recall']}\")\n        print(f\"  unparseable_pct: {exp['unparseable_pct']}\")\n        print(f\"  exact_match_rate: {exp['exact_match_rate']}\")\n        print(f\"  test_set_size: {exp['test_set_size']}\")\n        print(f\"  train_loss: {exp['train_loss']}  eval_loss: {exp['eval_loss']}\")\n        print(f\"  majority_baseline: {exp['majority_baseline']}\")\n        print(f\"  trajectory_accuracy: {exp['trajectory_accuracy']}\")\n        print(f\"  unresolved_f1: {exp['unresolved_f1']}  resolved_f1: {exp['resolved_f1']}\")\n        print(f\"  per_test_consistency: {exp['per_test_consistency']}\")\n        print(f\"  wall_clock_sec: {exp['wall_clock_seconds']}  gpu_hours: {exp['gpu_hours']}\")\n        print(f\"  server: {exp['server']}  gpu: {exp['gpu']}\")\n        print(f\"  lr: {exp['learning_rate']}  batch: {exp['batch_size']}  grad_accum: {exp['grad_accumulation']}\")\n        print(f\"  max_seq_len: {exp['max_seq_length']}  epochs: {exp['num_train_epochs']}\")\n        print(f\"  lora_rank: {exp['lora_rank']}  lora_alpha: {exp['lora_alpha']}\")\n        print(f\"  hyperparams: {json.dumps(exp['hyperparams'], ensure_ascii=False) if exp['hyperparams'] else None}\")\n        print(f\"  hypothesis: {exp['hypothesis_short']}\")\n        print(f\"  tags: {exp['tags']}\")\n        print(f\"  notes: {exp['notes']}\")\n        print(f\"  failure_reason: {exp['failure_reason']}\")\n        print(f\"  created_at: {exp['created_at']}\")\n        print(f\"  completed_at: {exp['completed_at']}\")\n        print(f\"  retry_count: {exp['retry_count']}\")\n        print(f\"  parent: {exp['parent']}\")\n        print(f\"  all_metrics: {json.dumps(exp['all_metrics'], indent=4, ensure_ascii=False) if exp['all_metrics'] else None}\")\n        print()\n\n\nif __name__ == \"__main__\":\n    main()\n"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-14T00:42:59.679673+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/parse_all_experiments.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_experiment-summary-table_20260514T003543",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-14T00:42:59.679824+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts && python3 parse_all_experiments.py 2>&1",
  "description": "Run the parser script to extract and print all experiments",
  "timeout": "30000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_experiment-summary-table_20260514T003543",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts && python3 parse_all_experiments.py 2>&1",
    "description": "Run the parser script to extract and print all experiments",
    "timeout": "30000"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-14T00:42:59.679976+00:00_

&lt;persisted-output>
Output too large (89.9KB). Full output saved to: /home/ubuntu/.claude-account-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/cd03d944-31d8-4706-ad87-0759b31a8651/tool-results/bpjooq854.txt

Preview (first 2KB):
Total experiments: 59
Saved to: /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/all_experiments_parsed.json

=== EXP: repo-level-cls-8b-conda ===
  conclusion: None
  status: RUNNING
  model: Qwen/Qwen3-8B
  seed: 42
  formulation: cls
  level: repo
  accuracy: None
  f1_macro: None
  pass_f1: None  fail_f1: None
  pass_precision: None  pass_recall: None
  fail_precision: None  fail_recall: None
  unparseable_pct: None
  exact_match_rate: None
  test_set_size: 70748
  train_loss: None  eval_loss: None
  majority_baseline: None
  trajectory_accuracy: None
  unresolved_f1: None  resolved_f1: None
  per_test_consistency: None
  wall_clock_sec: None  gpu_hours: None
  server: westd-48478  gpu: cuda:3
  lr: 5e-05  batch: 1  grad_accum: 32
  max_seq_len: 2048  epochs: 3
  lora_rank: 16  lora_alpha: 32
  hyperparams: None
  hypothesis: CLS 8B conda 重训 (transformers 4.57.6)，与 CLS v5 (4B) 同环境对比，验证 repo-level scaling ...
  tags: None
  notes: None
  failure_reason: None
  created_at: 2026-05-13T22:07:02.272Z
  completed_at: None
  retry_count: 0
  parent: None
  all_metrics: None

=== EXP: repo-level-cwm-v11 ===
  conclusion: killed
  status: DONE
  model: None
  seed: None
  formulation: cwm
  level: repo
  accuracy: 66.6
  f1_macro: 52.99
  pass_f1: 78.3  fail_f1: 27.7
  pass_precision: 74.5  pass_recall: 82.5
  fail_precision: 33.3  fail_recall: 23.7
  unparseable_pct: 376
  exact_match_rate: None
  test_set_size: None
  train_loss: None  eval_loss: None
  majority_baseline: 73
  trajectory_accuracy: None
  unresolved_f1: None  resolved_f1: None
  per_test_consistency: None
  wall_clock_sec: None  gpu_hours: None
  server: seetacloud-westd-4x5090  g
…[truncated 277 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_experiment-summary-table_20260514T003543",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-14T00:42:59.680130+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/cd03d944-31d8-4706-ad87-0759b31a8651/tool-results/bpjooq854.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_experiment-summary-table_20260514T003543",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/cd03d944-31d8-4706-ad87-0759b31a8651/tool-results/bpjooq854.txt"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-14T00:42:59.680254+00:00_

File content (38361 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_experiment-summary-table_20260514T003543",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-14T00:42:59.680387+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/cd03d944-31d8-4706-ad87-0759b31a8651/tool-results/bpjooq854.txt",
  "limit": "500",
  "offset": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_experiment-summary-table_20260514T003543",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/cd03d944-31d8-4706-ad87-0759b31a8651/tool-results/bpjooq854.txt",
    "limit": "500",
    "offset": "0"
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-14T00:42:59.680584+00:00_

0	Total experiments: 59
1	Saved to: /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/all_experiments_parsed.json
2	
3	=== EXP: repo-level-cls-8b-conda ===
4	  conclusion: None
5	  status: RUNNING
6	  model: Qwen/Qwen3-8B
7	  seed: 42
8	  formulation: cls
9	  level: repo
10	  accuracy: None
11	  f1_macro: None
12	  pass_f1: None  fail_f1: None
13	  pass_precision: None  pass_recall: None
14	  fail_precision: None  fail_recall: None
15	  unparseable_pct: None
16	  exact_match_rate: None
17	  test_set_size: 70748
18	  train_loss: None  eval_loss: None
19	  majority_baseline: None
20	  trajectory_accuracy: None
21	  unresolved_f1: None  resolved_f1: None
22	  per_test_consistency: None
23	  wall_clock_sec: None  gpu_hours: None
24	  server: westd-48478  gpu: cuda:3
25	  lr: 5e-05  batch: 1  grad_accum: 32
26	  max_seq_len: 2048  epochs: 3
27	  lora_rank: 16  lora_alpha: 32
28	  hyperparams: None
29	  hypothesis: CLS 8B conda 重训 (transformers 4.57.6)，与 CLS v5 (4B) 同环境对比，验证 repo-level scaling ...
30	  tags: None
31	  notes: None
32	  failure_reason: None
33	  created_at: 2026-05-13T22:07:02.272Z
34	  completed_at: None
35	  retry_count: 0
36	  parent: None
37	  all_metrics: None
38	
39	=== EXP: repo-level-cwm-v11 ===
40	  conclusion: killed
41	  status: DONE
42	  model: None
43	  seed: None
44	  formulation: cwm
45	  level: repo
46	  accuracy: 66.6
47	  f1_macro: 52.99
48	  pass_f1: 78.3  fail_f1: 27.7
49	  pass_precision: 74.5  pass_recall: 82.5
50	  fail_precision: 33.3  fail_recall: 23.7
51	  unparseable_pct: 376
52	  exact_match_rate: None
53	  test_set_size: None
54	  train_loss: None  eval_loss: None
55	  majority_baseline: 73
56	  trajectory_accuracy: None
57	  unresolved_f1: None  resolved_f1: None
58	  per_test_consistency: None
59	  wall_clock_sec: None  gpu_hours: None
60	  server: seetacloud-westd-4x5090  gpu: cuda:2
61	  lr: None  batch: None  grad_accum: None
62	  max_seq_len: None  epochs: None
63	  lora_rank: Non
…[truncated 15230 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_experiment-summary-table_20260514T003543",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-14T00:42:59.680744+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/cd03d944-31d8-4706-ad87-0759b31a8651/tool-results/bpjooq854.txt",
  "offset": "500",
  "limit": "500"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_experiment-summary-table_20260514T003543",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/cd03d944-31d8-4706-ad87-0759b31a8651/tool-results/bpjooq854.txt",
    "offset": "500",
    "limit": "500"
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-14T00:42:59.680969+00:00_

500	  train_loss: None  eval_loss: None
501	  majority_baseline: 0.7296
502	  trajectory_accuracy: None
503	  unresolved_f1: None  resolved_f1: None
504	  per_test_consistency: None
505	  wall_clock_sec: None  gpu_hours: None
506	  server: home-1x5090  gpu: cuda:0
507	  lr: None  batch: None  grad_accum: None
508	  max_seq_len: None  epochs: None
509	  lora_rank: None  lora_alpha: None
510	  hyperparams: None
511	  hypothesis: CLS v4: 基于 v3 代码（DataCollator 已修复），home-1x5090 重提交。磁盘已修复（89%→64%）。save_steps=200...
512	  tags: None
513	  notes: D045 early stop at step 2600/6633. Best checkpoint = step-200 (eval_loss=0.0701). Eval on checkpoint-200: accuracy=66.11% (below majority 72.96%), F1_macro=56.61%, F1_pass=76.9%, F1_fail=36.3%, 132 unparseable. Predictions: /home/sonny/exec-sim-repair-verifier/results/repo_cls_v4_eval/eval_repo_cls_predictions.jsonl
514	  failure_reason: process dead 5× with no sentinel/W&B — auto-resolved as failed
515	  created_at: 2026-05-12T17:17:08.066Z
516	  completed_at: 2026-05-12T19:00:01.551Z
517	  retry_count: 1
518	  parent: None
519	  all_metrics: {
520	    "accuracy": 0.6611,
521	    "f1_macro": 0.5661,
522	    "f1_pass": 0.769,
523	    "f1_fail": 0.363,
524	    "precision_pass": 0.765,
525	    "recall_pass": 0.774,
526	    "precision_fail": 0.369,
527	    "recall_fail": 0.357,
528	    "majority_baseline": 0.7296,
529	    "n_unparseable": 132,
530	    "best_checkpoint": "checkpoint-200",
531	    "early_stop": "D045"
532	}
533	
534	=== EXP: repo-level-cwm-v9 ===
535	  conclusion: failed
536	  status: DONE
537	  model: Qwen/Qwen3-4B
538	  seed: 42
539	  formulation: cwm
540	  level: repo
541	  accuracy: None
542	  f1_macro: None
543	  pass_f1: None  fail_f1: None
544	  pass_precision: None  pass_recall: None
545	  fail_precision: None  fail_recall: None
546	  unparseable_pct: None
547	  exact_match_rate: None
548	  test_set_size: 70748
549	  train_loss: None  eval_loss: None
550	  majority_baseline: None
551	  trajectory_accuracy: None

…[truncated 16434 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_experiment-summary-table_20260514T003543",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-14T00:42:59.681139+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/cd03d944-31d8-4706-ad87-0759b31a8651/tool-results/bpjooq854.txt",
  "offset": "1000",
  "limit": "500"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_experiment-summary-table_20260514T003543",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/cd03d944-31d8-4706-ad87-0759b31a8651/tool-results/bpjooq854.txt",
    "offset": "1000",
    "limit": "500"
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-14T00:42:59.681341+00:00_

1000	  tags: None
1001	  notes: v4 首次提交因 CLI 参数错误 EXIT_CODE=2 失败。系统自动重试 (PID 77811) 但不含 Director 要求的 save_strategy=steps/save_steps=500。与 v5 并行会触发 cgroup OOM，主动停止保护 v5。
1002	  failure_reason: 
1003	  created_at: 2026-05-12T17:23:40.543Z
1004	  completed_at: 2026-05-12T17:38:58.649Z
1005	  retry_count: 1
1006	  parent: None
1007	  all_metrics: None
1008	
1009	=== EXP: repo-level-cwm-v2 ===
1010	  conclusion: failed
1011	  status: DONE
1012	  model: None
1013	  seed: None
1014	  formulation: cwm
1015	  level: repo
1016	  accuracy: None
1017	  f1_macro: None
1018	  pass_f1: None  fail_f1: None
1019	  pass_precision: None  pass_recall: None
1020	  fail_precision: None  fail_recall: None
1021	  unparseable_pct: None
1022	  exact_match_rate: None
1023	  test_set_size: None
1024	  train_loss: None  eval_loss: None
1025	  majority_baseline: None
1026	  trajectory_accuracy: None
1027	  unresolved_f1: None  resolved_f1: None
1028	  per_test_consistency: None
1029	  wall_clock_sec: 10813.1  gpu_hours: 3.0
1030	  server: seetacloud-westd-4x5090  gpu: ['cuda:3']
1031	  lr: None  batch: None  grad_accum: None
1032	  max_seq_len: None  epochs: None
1033	  lora_rank: None  lora_alpha: None
1034	  hyperparams: None
1035	  hypothesis: Repo-level CWM generation (SWE-bench per-test data, Qwen3-4B LoRA). 修复 sample_we...
1036	  tags: None
1037	  notes: ValueError: DataCollator tokenizer.pad() 收到 dict 而非 tensor。崩溃在 step 0/6633。与 repo-level-cls-v2 同一 root cause。
1038	  failure_reason: None
1039	  created_at: 2026-05-12T14:41:28.527Z
1040	  completed_at: 2026-05-12T18:57:16.157Z
1041	  retry_count: 0
1042	  parent: None
1043	  all_metrics: None
1044	
1045	=== EXP: repo-level-cwm-v5 ===
1046	  conclusion: failed
1047	  status: DONE
1048	  model: Qwen/Qwen3-4B
1049	  seed: 42
1050	  formulation: cwm
1051	  level: repo
1052	  accuracy: None
1053	  f1_macro: None
1054	  pass_f1: None  fail_f1: None
1055	  pass_precision: None  pass_recall: None
1056	  fail_precision: None  fail_recall: None
105
…[truncated 16433 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_experiment-summary-table_20260514T003543",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-14T00:42:59.681507+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/cd03d944-31d8-4706-ad87-0759b31a8651/tool-results/bpjooq854.txt",
  "offset": "1500",
  "limit": "500"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_experiment-summary-table_20260514T003543",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/cd03d944-31d8-4706-ad87-0759b31a8651/tool-results/bpjooq854.txt",
    "offset": "1500",
    "limit": "500"
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-14T00:42:59.681713+00:00_

1500	  unresolved_f1: None  resolved_f1: None
1501	  per_test_consistency: None
1502	  wall_clock_sec: 1093.5  gpu_hours: 0.3
1503	  server: home-1x5090  gpu: ['cuda:0']
1504	  lr: None  batch: None  grad_accum: None
1505	  max_seq_len: None  epochs: None
1506	  lora_rank: None  lora_alpha: None
1507	  hyperparams: None
1508	  hypothesis: Per-test 级别 precision/recall 诊断分析 — 按 mutation type 和 problem 粒度评估分类器的诊断质量
1509	  tags: None
1510	  notes: 扩展诊断分析完成 (eval_pertest_diagnostic.py)。新增发现：114 个 problems 中 48 个 (42.1%) 完美预测；median problem fail-F1=94.12%；return_value 最易 (F1=98.6%), off_by_one 最难 (F1=80.8%)；worst problems: MBPP/397 (40%), HumanEval/130 (46%)。脚本和结果保存在 home:/home/sonny/exec-sim-repair-verifier/eval_pertest_diag.json。
1511	  failure_reason: None
1512	  created_at: 2026-05-12T05:51:25.659Z
1513	  completed_at: 2026-05-12T06:09:39.167Z
1514	  retry_count: 0
1515	  parent: None
1516	  all_metrics: {
1517	    "accuracy": 87.51,
1518	    "fail_precision": 82.75,
1519	    "fail_recall": 93.64,
1520	    "fail_f1": 87.86,
1521	    "pass_precision": 93.24,
1522	    "pass_recall": 81.8,
1523	    "pass_f1": 87.15,
1524	    "FP_count": 58,
1525	    "FN_count": 178,
1526	    "best_mutation": "return_value (97.26%)",
1527	    "worst_mutation": "off_by_one (82.56%)",
1528	    "bucket_6_10_acc": 96.3,
1529	    "bucket_11plus_acc": 87.12
1530	}
1531	
1532	=== EXP: cwm-seed123 ===
1533	  conclusion: success
1534	  status: DONE
1535	  model: Qwen/Qwen3-4B
1536	  seed: 123
1537	  formulation: cwm
1538	  level: function
1539	  accuracy: 87.2
1540	  f1_macro: None
1541	  pass_f1: 86.95  fail_f1: 87.44
1542	  pass_precision: None  pass_recall: None
1543	  fail_precision: None  fail_recall: None
1544	  unparseable_pct: 0
1545	  exact_match_rate: 84.44
1546	  test_set_size: 15290
1547	  train_loss: None  eval_loss: None
1548	  majority_baseline: None
1549	  trajectory_accuracy: None
1550	  unresolved_f1: None  resolved_f1: None
1551	  per_test_consistency: None
1552	  wall_clock_sec
…[truncated 17280 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_experiment-summary-table_20260514T003543",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-14T00:42:59.681902+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/cd03d944-31d8-4706-ad87-0759b31a8651/tool-results/bpjooq854.txt",
  "offset": "2000",
  "limit": "600"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_experiment-summary-table_20260514T003543",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/cd03d944-31d8-4706-ad87-0759b31a8651/tool-results/bpjooq854.txt",
    "offset": "2000",
    "limit": "600"
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-14T00:42:59.682132+00:00_

2000	    "icc": 0.1909,
2001	    "icc_p_value": 0,
2002	    "design_effect": 3.9676,
2003	    "overall_error_rate": 0.1249,
2004	    "all_correct_observed": 46,
2005	    "all_correct_expected_iid": 16.35,
2006	    "all_correct_ratio": 2.81,
2007	    "error_std_observed": 0.1531,
2008	    "error_std_expected_iid": 0.0811,
2009	    "error_std_ratio": 1.89,
2010	    "n_samples": 1890,
2011	    "n_problems": 114,
2012	    "inference_precision": "bfloat16",
2013	    "version": "v2_corrected"
2014	}
2015	
2016	=== EXP: model-size-scaling-cwm8b ===
2017	  conclusion: success
2018	  status: DONE
2019	  model: Qwen/Qwen3-8B
2020	  seed: 42
2021	  formulation: cwm
2022	  level: function
2023	  accuracy: 87.67
2024	  f1_macro: None
2025	  pass_f1: 87.57  fail_f1: 87.77
2026	  pass_precision: 91.53  pass_recall: 83.95
2027	  fail_precision: 84.19  fail_recall: 91.67
2028	  unparseable_pct: 0
2029	  exact_match_rate: 84.39
2030	  test_set_size: 15290
2031	  train_loss: 0.229  eval_loss: None
2032	  majority_baseline: None
2033	  trajectory_accuracy: None
2034	  unresolved_f1: None  resolved_f1: None
2035	  per_test_consistency: None
2036	  wall_clock_sec: 5867.9  gpu_hours: 1.63
2037	  server: seetacloud-westd-4x5090  gpu: ['cuda:1']
2038	  lr: None  batch: None  grad_accum: None
2039	  max_seq_len: None  epochs: None
2040	  lora_rank: None  lora_alpha: None
2041	  hyperparams: None
2042	  hypothesis: Qwen3-8B CWM generation baseline 在函数级的 F1 与同尺寸 classification 的差距，相比 4B 尺度（差距 0....
2043	  tags: None
2044	  notes: 8B CWM 相比 4B 几乎无提升: accuracy 87.67 vs 87.51 (+0.16pp), pass_f1 87.57 vs 87.31 (+0.26pp), fail_f1 87.77 vs 87.71 (+0.06pp), exact_match 84.39 vs 84.02 (+0.37pp)。CWM对模型容量增加不敏感，瓶颈可能在于生成精确错误信息的任务复杂度本身，而非模型能力不足。训练3 epoch完成，train_loss=0.229（低于cls的0.3125），eval_loss在epoch2最低(0.0512)。关键对比：8B cls-cwm gap (accuracy 2.81pp, pass_f1 3.29pp, fail_f1 2.29pp) 远大于4B的gap (accuracy 0.90pp, pass_f1 1.10pp, fail_f1 0.69pp)。Gap扩大约3倍，强烈支持complexity hypothesis——classification的scaling效率显著优于CW
…[truncated 20434 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_experiment-summary-table_20260514T003543",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-14T00:42:59.682301+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/cd03d944-31d8-4706-ad87-0759b31a8651/tool-results/bpjooq854.txt",
  "offset": "2600",
  "limit": "500"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_experiment-summary-table_20260514T003543",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/cd03d944-31d8-4706-ad87-0759b31a8651/tool-results/bpjooq854.txt",
    "offset": "2600",
    "limit": "500"
  }
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-14T00:42:59.682457+00:00_

2600	        "median": 1,
2601	        "mean": 3,
2602	        "P75": 2,
2603	        "P90": 3
2604	    },
2605	    "total_reg5pct": {
2606	        "iid_adv_70_85": -0.01,
2607	        "block_adv_70_85": -0.005,
2608	        "pass": false
2609	    },
2610	    "total_reg10pct": {
2611	        "iid_adv_70_85": 0.132,
2612	        "block_adv_70_85": 0.083,
2613	        "pass": true
2614	    },
2615	    "total_reg20pct": {
2616	        "iid_adv_70_85": 0.357,
2617	        "block_adv_70_85": 0.278,
2618	        "pass": true
2619	    }
2620	}
2621	
2622	=== EXP: p2p-regression-rate ===
2623	  conclusion: negative
2624	  status: DONE
2625	  model: None
2626	  seed: None
2627	  formulation: analysis
2628	  level: function
2629	  accuracy: None
2630	  f1_macro: None
2631	  pass_f1: None  fail_f1: None
2632	  pass_precision: None  pass_recall: None
2633	  fail_precision: None  fail_recall: None
2634	  unparseable_pct: None
2635	  exact_match_rate: None
2636	  test_set_size: None
2637	  train_loss: None  eval_loss: None
2638	  majority_baseline: None
2639	  trajectory_accuracy: None
2640	  unresolved_f1: None  resolved_f1: None
2641	  per_test_consistency: None
2642	  wall_clock_sec: None  gpu_hours: None
2643	  server: None  gpu: None
2644	  lr: None  batch: None  grad_accum: None
2645	  max_seq_len: None  epochs: None
2646	  lora_rank: None  lora_alpha: None
2647	  hyperparams: None
2648	  hypothesis: 
2649	  tags: None
2650	  notes: P2P regression rate measured at 1.04% mean / 0% median on CoderForge Qwen3-32B SWE-bench Verified data (106 unresolved patches). 77% of incorrect patches break zero P2P tests. Falls into <5% zone — per-test verifier has minimal advantage on P2P dimension. Main value is in F2P (distinguishing partial vs zero repair). Project premise partially invalidated for P2P.
2651	  failure_reason: None
2652	  created_at: 2026-05-11T20:03:33.129Z
2653	  completed_at: 2026-05-11T20:04:02.945Z
2654	  retry_count: 0
2655	  parent: None
2656	  all_metrics: None
2
…[truncated 1523 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_experiment-summary-table_20260514T003543",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-14T00:42:59.682625+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "wc -l /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/all_experiments_parsed.json && python3 -c \"\nimport json\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/all_experiments_parsed.json') as f:\n    data = json.load(f)\nprint(f'Total experiments in JSON: {len(data)}')\n# Quick summary\nstatuses = {}\nconclusions = {}\nfor e in data:\n    s = e['status'] or 'None'\n    c = e['conclusion'] or 'None'\n    statuses[s] = statuses.get(s, 0) + 1\n    conclusions[c] = conclusions.get(c, 0) + 1\nprint(f'Statuses: {statuses}')\nprint(f'Conclusions: {conclusions}')\nprint(f'With metrics: {sum(1 for e in data if e[\\\"all_metrics\\\"])}')\nprint(f'With accuracy: {sum(1 for e in data if e[\\\"accuracy\\\"] is not None)}')\n\"",
  "description": "Verify output JSON and print summary stats"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_experiment-summary-table_20260514T003543",
  "tool": "Bash",
  "tool_args": {
    "command": "wc -l /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/all_experiments_parsed.json && python3 -c \"\nimport json\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/all_experiments_parsed.json') as f:\n    data = json.load(f)\nprint(f'Total experiments in JSON: {len(data)}')\n# Quick summary\nstatuses = {}\nconclusions = {}\nfor e in data:\n    s = e['status'] or 'None'\n    c = e['conclusion'] or 'None'\n    statuses[s] = statuses.get(s, 0) + 1\n    conclusions[c] = conclusions.get(c, 0) + 1\nprint(f'Statuses: {statuses}')\nprint(f'Conclusions: {conclusions}')\nprint(f'With metrics: {sum(1 for e in data if e[\\\"all_metrics\\\"])}')\nprint(f'With accuracy: {sum(1 for e in data if e[\\\"accuracy\\\"] is not None)}')\n\"",
    "description": "Verify output JSON and print summary stats"
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-14T00:42:59.682759+00:00_

4146 /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/all_experiments_parsed.json
Total experiments in JSON: 59
Statuses: {'RUNNING': 5, 'DONE': 54}
Conclusions: {'None': 5, 'killed': 5, 'success': 33, 'failed': 13, 'negative': 3}
With metrics: 35
With accuracy: 29

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_experiment-summary-table_20260514T003543",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-14T00:42:59.683034+00:00_

Done. Here is the summary:

**Output file**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/all_experiments_parsed.json`

**Parser script**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/parse_all_experiments.py`

**59 experiments extracted** with breakdown:
- **By status**: 5 RUNNING, 54 DONE
- **By conclusion**: 33 success, 13 failed, 5 killed, 3 negative, 5 None (running)
- **35** have metrics data, **29** have accuracy values

**Full stdout dump** was produced (all 59 experiments with every field) and saved by the tool at the persisted output path. The output above shows the complete content of all experiments across 2694 lines, covering:

- **Function-level experiments**: cls (seeds 0/42/123/456/789), cwm (seeds 0/42/123/456/789), traj (seeds 0/42/123/456/789), 8B scaling (cls8b, cwm8b with multiple seeds), LLM-judge (8B/32B zero-shot)
- **Repo-level experiments**: cls (v2-v5, seed123, 8b), cwm (v2-v12, seed123), multiple failures tracked with root causes
- **Analysis experiments**: 5-paired-clustered-bootstrap, per-test-majority-voting, block-corr-empirical, oracle-f2p-stratified, p2p-regression-rate, matched-seed-8b-predictions, mvp-a-oracle-sim, mvp-b-data-prep, mvp-b-train, multi-seed-core

Each experiment record includes all requested fields: exp_id, hypothesis, model_name, seed, formulation, level, status, conclusion, accuracy, f1_macro, pass/fail F1/precision/recall, unparseable_pct, exact_match_rate, test_set_size, full raw metrics dict, tags, notes, failure_reason, hyperparams, server/GPU info, and timing data.
agentId: a240a9647eba4480f (use SendMessage with to: 'a240a9647eba4480f' to continue this agent)
&lt;usage>total_tokens: 79485
tool_uses: 17
duration_ms: 132471&lt;/usage>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_experiment-summary-table_20260514T003543",
  "tool": "Agent",
  "elapsed_ms": 5
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-14T00:42:59.683275+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts && python3 -c \"\nimport json\n\nwith open('all_experiments_parsed.json') as f:\n    data = json.load(f)\n\n# Filter success experiments and print key metrics\nfor exp in sorted(data, key=lambda x: x.get('exp_id','')):\n    c = exp.get('conclusion','')\n    eid = exp.get('exp_id','')\n    status = exp.get('status','')\n    model = exp.get('model_name','')\n    seed = exp.get('seed','')\n    form = exp.get('formulation','')\n    level = exp.get('level','')\n    acc = exp.get('accuracy','')\n    f1m = exp.get('f1_macro','')\n    pf1 = exp.get('pass_f1','')\n    ff1 = exp.get('fail_f1','')\n    pp = exp.get('pass_precision','')\n    pr = exp.get('pass_recall','')\n    fp = exp.get('fail_precision','')\n    fr = exp.get('fail_recall','')\n    up = exp.get('unparseable_pct','')\n    em = exp.get('exact_match_rate','')\n    ts = exp.get('test_set_size','')\n    hyp = exp.get('hypothesis','')\n    notes = exp.get('notes','')\n    tags = exp.get('tags','')\n    metrics = exp.get('all_metrics',{})\n    \n    print(f'=== {eid} === conclusion={c} status={status}')\n    print(f'  model={model} seed={seed} form={form} level={level}')\n    print(f'  acc={acc} f1m={f1m} pf1={pf1} ff1={ff1}')\n    print(f'  pp={pp} pr={pr} fp={fp} fr={fr}')\n    print(f'  unparseable={up} exact_match={em} test_size={ts}')\n    print(f'  hyp={hyp[:80]}')\n    print(f'  notes={str(notes)[:120]}')\n    print(f'  tags={tags}')\n    if metrics:\n        print(f'  raw_metrics={json.dumps(metrics)}')\n    print()\n\"\n",
  "description": "Print all parsed experiment data"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_experiment-summary-table_20260514T003543",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts && python3 -c \"\nimport json\n\nwith open('all_experiments_parsed.json') as f:\n    data = json.load(f)\n\n# Filter success experiments and print key metrics\nfor exp in sorted(data, key=lambda x: x.get('exp_id','')):\n    c = exp.get('conclusion','')\n    eid = exp.get('exp_id','')\n    status = exp.get('status','')\n    model = exp.get('model_name','')\n    seed = exp.get('seed','')\n    form = exp.get('formulation','')\n    level = exp.get('level','')\n    acc = exp.get('accuracy','')\n    f1m = exp.get('f1_macro','')\n    pf1 = exp.get('pass_f1','')\n    ff1 = exp.get('fail_f1','')\n    pp = exp.get('pass_precision','')\n    pr = exp.get('pass_recall','')\n    fp = exp.get('fail_precision','')\n    fr = exp.get('fail_recall','')\n    up = exp.get('unparseable_pct','')\n    em = exp.get('exact_match_rate','')\n    ts = exp.get('test_set_size','')\n    hyp = exp.get('hypothesis','')\n    notes = exp.get('notes','')\n    tags = exp.get('tags','')\n    metrics = exp.get('all_metrics',{})\n    \n    print(f'=== {eid} === conclusion={c} status={status}')\n    print(f'  model={model} seed={seed} form={form} level={level}')\n    print(f'  acc={acc} f1m={f1m} pf1={pf1} ff1={ff1}')\n    print(f'  pp={pp} pr={pr} fp={fp} fr={fr}')\n    print(f'  unparseable={up} exact_match={em} test_size={ts}')\n    print(f'  hyp={hyp[:80]}')\n    print(f'  notes={str(notes)[:120]}')\n    print(f'  tags={tags}')\n    if metrics:\n        print(f'  raw_metrics={json.dumps(metrics)}')\n    print()\n\"\n",
    "description": "Print all parsed experiment data"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-14T00:42:59.683535+00:00_

&lt;persisted-output>
Output too large (38.5KB). Full output saved to: /home/ubuntu/.claude-account-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/cd03d944-31d8-4706-ad87-0759b31a8651/tool-results/bssooke29.txt

Preview (first 2KB):
=== 5-paired-clustered-bootstrap === conclusion=success status=DONE
  model=None seed=None form=analysis level=function
  acc=None f1m=None pf1=None ff1=None
  pp=None pr=None fp=None fr=None
  unparseable=None exact_match=None test_size=None
  hyp=5-seed paired variant-level clustered bootstrap CI + TOST 等价检验，验证 CLS 和 TRAJ 在 v
  notes=5-paired 扩展了之前 3-paired 分析。核心发现：CLS 和 TRAJ 在 variant 级别统计等价（TOST p=0.0071, margin ±2pp），无显著差异（gap=-0.45pp, p=0.499）。确认 D
  tags=None
  raw_metrics={"pooled_gap_pp": -0.45, "pooled_ci_lower": -1.71, "pooled_ci_upper": 0.84, "pooled_p_value": 0.499, "tost_p_value": 0.0071, "tost_margin_pp": 2, "seed_level_paired_t_p": 0.425, "seed_level_mean_gap": -0.48, "n_variants_pooled": 523, "n_clusters": 114, "per_seed_gaps": {"seed42": -0.97, "seed123": 1.45, "seed456": -1.84, "seed789": -0.78, "seed0": -0.29}}

=== block-corr-empirical === conclusion=success status=DONE
  model=Qwen/Qwen3-4B + LoRA (seed 42) seed=42 form=analysis level=function
  acc=None f1m=None pf1=None ff1=None
  pp=None pr=None fp=None fr=None
  unparseable=None exact_match=None test_size=1890
  hyp=训练好的 per-test 分类器的预测误差在同一 problem_id 内是 block-correlated 而非 i.i.d.，验证 oracle 模拟的
  notes=v2 修正版：用 bfloat16 推理替代 v1 的 4-bit 量化。accuracy 偏差已消除 (87.51% = 主评估)。ICC 从 0.233 降至 0.191（4-bit 量化误差本身也是 block-correlated 
  tags=None
  raw_metrics={"icc": 0.1909, "icc_p_value": 0, "design_effect": 3.9676, "overall_error_rate": 0.1249, "all_correct_observed": 46, "all_correct_expected_iid": 16.35, "all_correct_ratio": 2.81, "error_std_observed": 0.1531, "error_std_expected_iid": 0.0811, "error_std_ratio": 1.89, "n_samples": 1890, "n_problems": 114, "inference_precision": "bfloat16", "version": "v2_corrected"}

=
…[truncated 244 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_experiment-summary-table_20260514T003543",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-14T00:42:59.683705+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/cd03d944-31d8-4706-ad87-0759b31a8651/tool-results/bssooke29.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_experiment-summary-table_20260514T003543",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/cd03d944-31d8-4706-ad87-0759b31a8651/tool-results/bssooke29.txt"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-14T00:42:59.684186+00:00_

1	=== 5-paired-clustered-bootstrap === conclusion=success status=DONE
2	  model=None seed=None form=analysis level=function
3	  acc=None f1m=None pf1=None ff1=None
4	  pp=None pr=None fp=None fr=None
5	  unparseable=None exact_match=None test_size=None
6	  hyp=5-seed paired variant-level clustered bootstrap CI + TOST 等价检验，验证 CLS 和 TRAJ 在 v
7	  notes=5-paired 扩展了之前 3-paired 分析。核心发现：CLS 和 TRAJ 在 variant 级别统计等价（TOST p=0.0071, margin ±2pp），无显著差异（gap=-0.45pp, p=0.499）。确认 D
8	  tags=None
9	  raw_metrics={"pooled_gap_pp": -0.45, "pooled_ci_lower": -1.71, "pooled_ci_upper": 0.84, "pooled_p_value": 0.499, "tost_p_value": 0.0071, "tost_margin_pp": 2, "seed_level_paired_t_p": 0.425, "seed_level_mean_gap": -0.48, "n_variants_pooled": 523, "n_clusters": 114, "per_seed_gaps": {"seed42": -0.97, "seed123": 1.45, "seed456": -1.84, "seed789": -0.78, "seed0": -0.29}}
10	
11	=== block-corr-empirical === conclusion=success status=DONE
12	  model=Qwen/Qwen3-4B + LoRA (seed 42) seed=42 form=analysis level=function
13	  acc=None f1m=None pf1=None ff1=None
14	  pp=None pr=None fp=None fr=None
15	  unparseable=None exact_match=None test_size=1890
16	  hyp=训练好的 per-test 分类器的预测误差在同一 problem_id 内是 block-correlated 而非 i.i.d.，验证 oracle 模拟的
17	  notes=v2 修正版：用 bfloat16 推理替代 v1 的 4-bit 量化。accuracy 偏差已消除 (87.51% = 主评估)。ICC 从 0.233 降至 0.191（4-bit 量化误差本身也是 block-correlated 
18	  tags=None
19	  raw_metrics={"icc": 0.1909, "icc_p_value": 0, "design_effect": 3.9676, "overall_error_rate": 0.1249, "all_correct_observed": 46, "all_correct_expected_iid": 16.35, "all_correct_ratio": 2.81, "error_std_observed": 0.1531, "error_std_expected_iid": 0.0811, "error_std_ratio": 1.89, "n_samples": 1890, "n_problems": 114, "inference_precision": "bfloat16", "version": "v2_corrected"}
20	
21	=== cls-seed0 === conclusion=success status=DONE
22	  model=None seed=None form=cls level=function
23	  acc=87.94 f1m=None pf1=87.79 ff1=88.08
24	  pp=92.13 pr=83.84 fp=84.2 fr=92.32
25	  unparseable=0 exact_match=None test_size=Non
…[truncated 36878 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_experiment-summary-table_20260514T003543",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-14T00:42:59.684629+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport numpy as np\nfrom scipy import stats\n\n# ============================================================\n# DATA: Function-level CLS 4B (5 seeds)\n# ============================================================\ncls_4b = {\n    0:   {\"acc\": 87.94, \"pf1\": 87.79, \"ff1\": 88.08, \"pp\": 92.13, \"pr\": 83.84, \"fp\": 84.20, \"fr\": 92.32},\n    42:  {\"acc\": 87.83, \"pf1\": 88.06, \"ff1\": 87.59, \"pp\": 89.45, \"pr\": 86.71, \"fp\": 86.20, \"fr\": 89.04},\n    123: {\"acc\": 89.52, \"pf1\": 89.64, \"ff1\": 89.40, \"pp\": 91.76, \"pr\": 87.63, \"fp\": 87.34, \"fr\": 91.56},\n    456: {\"acc\": 87.88, \"pf1\": 87.53, \"ff1\": 88.21, \"pp\": 93.60, \"pr\": 82.21, \"fp\": 83.12, \"fr\": 93.97},\n    789: {\"acc\": 89.00, \"pf1\": 88.90, \"ff1\": 89.10, \"pp\": 93.30, \"pr\": 84.90, \"fp\": 85.20, \"fr\": 93.40},\n}\n\n# ============================================================\n# DATA: Function-level CWM 4B (5 seeds)\n# ============================================================\ncwm_4b = {\n    0:   {\"acc\": 87.57, \"pf1\": 87.18, \"ff1\": 87.93, \"pp\": 93.45, \"pr\": 81.70, \"fp\": 82.71, \"fr\": 93.86, \"em\": 84.29},\n    42:  {\"acc\": 87.51, \"pf1\": 87.31, \"ff1\": 87.71, \"pp\": 92.06, \"pr\": 83.03, \"fp\": 83.53, \"fr\": 92.32, \"em\": 84.02},\n    123: {\"acc\": 87.20, \"pf1\": 86.95, \"ff1\": 87.44, \"pp\": None, \"pr\": None, \"fp\": None, \"fr\": None, \"em\": 84.44},\n    456: {\"acc\": 86.98, \"pf1\": 86.66, \"ff1\": 87.29, \"pp\": 92.26, \"pr\": 81.70, \"fp\": 82.52, \"fr\": 92.65, \"em\": 84.02},\n    789: {\"acc\": 86.67, \"pf1\": 86.74, \"ff1\": 86.60, \"pp\": 89.37, \"pr\": 84.25, \"fp\": 84.09, \"fr\": 89.25, \"em\": 83.97},\n}\n\n# ============================================================\n# DATA: Function-level CLS 8B (3 seeds)\n# ============================================================\ncls_8b = {\n    42:  {\"acc\": 90.48, \"pf1\": 90.86, \"ff1\": 90.06, \"pp\": 90.22, \"pr\": 91.51, \"fp\": 90.76, \"fr\": 89.36},\n    123: {\"acc\": 89.37, \"pf1\": 89.54, \"ff1\": 89.19, \"pp\": 91.20, \"pr\": 87.93, \"fp\": 87.54, \"fr\": 90.90},\n    # Note: cls8b-seed123 registry has 89.4 but cls8b-eval-seed123 has 89.37 - use the eval version\n    456: {\"acc\": 88.31, \"pf1\": 88.20, \"ff1\": 88.41, \"pp\": 92.29, \"pr\": 84.46, \"fp\": 84.72, \"fr\": 92.43},\n}\n\n# ============================================================\n# DATA: Function-level CWM 8B (3 seeds)\n# ============================================================\ncwm_8b = {\n    42:  {\"acc\": 87.67, \"pf1\": 87.57, \"ff1\": 87.77, \"pp\": 91.53, \"pr\": 83.95, \"fp\": 84.19, \"fr\": 91.67, \"em\": 84.39},\n    123: {\"acc\": 86.98, \"pf1\": 86.83, \"ff1\": 87.13, \"pp\": 91.12, \"pr\": 82.92, \"fp\": 83.30, \"fr\": 91.34, \"em\": 84.13},\n    456: {\"acc\": 86.24, \"pf1\": 85.96, \"ff1\": 86.51, \"pp\": 91.08, \"pr\": 81.39, \"fp\": 82.09, \"fr\": 91.45, \"em\": 82.80},\n}\n\n# ============================================================\n# DATA: Trajectory-level (5 seeds)\n# ============================================================\ntraj = {\n    0:   {\"acc\": 85.66, \"uf1\": 87.37, \"rf1\": 83.41, \"up\": 82.71, \"ur\": 92.59, \"rp\": 90.07, \"rr\": 77.66, \"con\": 79.55},\n    42:  {\"acc\": 85.66, \"uf1\": 87.50, \"rf1\": 83.18, \"up\": None, \"ur\": None, \"rp\": None, \"rr\": None, \"con\": 79.94},\n    123: {\"acc\": 85.47, \"uf1\": 87.00, \"rf1\": 83.52, \"up\": 83.53, \"ur\": 90.78, \"rp\": 88.17, \"rr\": 79.33, \"con\": 78.59},\n    456: {\"acc\": 87.40, \"uf1\": 88.70, \"rf1\": 85.80, \"up\": 85.70, \"ur\": 91.90, \"rp\": 89.70, \"rr\": 82.30, \"con\": 78.80},\n    789: {\"acc\": 87.31, \"uf1\": 88.27, \"rf1\": 86.17, \"up\": 87.41, \"ur\": 89.15, \"rp\": 87.18, \"rr\": 85.18, \"con\": 76.74},\n}\n\n# ============================================================\n# DATA: LLM Judge zero-shot\n# ============================================================\nllm_judge = {\n    \"8B\":  {\"acc\": 64.40, \"pf1\": 50.50, \"ff1\": 72.20, \"pp\": 90.0, \"pr\": 35.1, \"fp\": 57.9, \"fr\": 95.8},\n    \"32B\": {\"acc\": 71.69, \"pf1\": 65.68, \"ff1\": 75.91, \"pp\": 88.12, \"pr\": 52.35, \"fp\": 64.40, \"fr\": 92.43},\n}\n\n# ============================================================\n# DATA: Repo-level\n# ============================================================\nrepo = {\n    \"cls-v4\": {\"acc\": 66.11, \"f1m\": 56.61, \"pf1\": 76.9, \"ff1\": 36.3, \"pp\": 76.5, \"pr\": 77.4, \"fp\": 36.9, \"fr\": 35.7, \"unp\": 132, \"note\": \"early stop, old hyperparams\"},\n    \"cls-v5\": {\"acc\": 76.92, \"f1m\": 73.90, \"pf1\": 82.78, \"ff1\": 65.01, \"pp\": 90.83, \"pr\": 76.04, \"fp\": 55.09, \"fr\": 79.29, \"unp\": 132, \"note\": \"best CLS, corrected hyperparams\"},\n    \"cwm-v10\": {\"acc\": 69.91, \"f1m\": 46.71, \"pf1\": 81.87, \"ff1\": 11.54, \"unp\": 9102, \"note\": \"93% unparseable, eval invalid\"},\n    \"cwm-v11\": {\"acc\": 66.60, \"f1m\": 52.99, \"pf1\": 78.30, \"ff1\": 27.70, \"unp\": 376, \"note\": \"killed, mixed transformers versions, 500-sample subset\"},\n    \"cls-8b\":  {\"acc\": 71.37, \"f1m\": 69.05, \"pf1\": 77.53, \"ff1\": 60.57, \"pp\": 90.71, \"pr\": 67.69, \"fp\": 48.26, \"fr\": 81.29, \"unp\": 136, \"note\": \"below majority baseline, transformers 5.8.0 mismatch\"},\n}\n\ndef ms(vals):\n    a = np.array(vals)\n    return np.mean(a), np.std(a, ddof=1)\n\ndef fmt(m, s):\n    return f\"{m:.2f} ± {s:.2f}\"\n\n# ============================================================\n# COMPUTE TABLES\n# ============================================================\n\nprint(\"=\" * 120)\nprint(\"TABLE 1: Function-level CLS (per-test classification, 4B, 5 seeds)\")\nprint(\"=\" * 120)\nprint(f\"{'Seed':<8} {'Accuracy':<10} {'Pass_F1':<10} {'Fail_F1':<10} {'Pass_P':<10} {'Pass_R':<10} {'Fail_P':<10} {'Fail_R':<10}\")\nprint(\"-\" * 78)\nfor s in [0, 42, 123, 456, 789]:\n    d = cls_4b[s]\n    print(f\"{s:<8} {d['acc']:<10.2f} {d['pf1']:<10.2f} {d['ff1']:<10.2f} {d['pp']:<10.2f} {d['pr']:<10.2f} {d['fp']:<10.2f} {d['fr']:<10.2f}\")\naccs = [cls_4b[s][\"acc\"] for s in cls_4b]\npf1s = [cls_4b[s][\"pf1\"] for s in cls_4b]\nff1s = [cls_4b[s][\"ff1\"] for s in cls_4b]\npps = [cls_4b[s][\"pp\"] for s in cls_4b]\nprs = [cls_4b[s][\"pr\"] for s in cls_4b]\nfps = [cls_4b[s][\"fp\"] for s in cls_4b]\nfrs = [cls_4b[s][\"fr\"] for s in cls_4b]\nm, s = ms(accs); m2,s2=ms(pf1s); m3,s3=ms(ff1s); m4,s4=ms(pps); m5,s5=ms(prs); m6,s6=ms(fps); m7,s7=ms(frs)\nprint(\"-\" * 78)\nprint(f\"{'Mean±Std':<8} {fmt(m,s):<10} {fmt(m2,s2):<10} {fmt(m3,s3):<10} {fmt(m4,s4):<10} {fmt(m5,s5):<10} {fmt(m6,s6):<10} {fmt(m7,s7):<10}\")\n\nprint()\nprint(\"=\" * 120)\nprint(\"TABLE 2: Function-level CWM (execution simulation, 4B, 5 seeds)\")\nprint(\"=\" * 120)\nprint(f\"{'Seed':<8} {'Accuracy':<10} {'Pass_F1':<10} {'Fail_F1':<10} {'Pass_P':<10} {'Pass_R':<10} {'Fail_P':<10} {'Fail_R':<10} {'ExactMatch':<12}\")\nprint(\"-\" * 90)\nfor s in [0, 42, 123, 456, 789]:\n    d = cwm_4b[s]\n    pp_str = f\"{d['pp']:.2f}\" if d['pp'] else \"—\"\n    pr_str = f\"{d['pr']:.2f}\" if d['pr'] else \"—\"\n    fp_str = f\"{d['fp']:.2f}\" if d['fp'] else \"—\"\n    fr_str = f\"{d['fr']:.2f}\" if d['fr'] else \"—\"\n    print(f\"{s:<8} {d['acc']:<10.2f} {d['pf1']:<10.2f} {d['ff1']:<10.2f} {pp_str:<10} {pr_str:<10} {fp_str:<10} {fr_str:<10} {d['em']:<12.2f}\")\naccs_c = [cwm_4b[s][\"acc\"] for s in cwm_4b]\npf1s_c = [cwm_4b[s][\"pf1\"] for s in cwm_4b]\nff1s_c = [cwm_4b[s][\"ff1\"] for s in cwm_4b]\nems = [cwm_4b[s][\"em\"] for s in cwm_4b]\nm, s = ms(accs_c); m2,s2=ms(pf1s_c); m3,s3=ms(ff1s_c); m4,s4=ms(ems)\npps_v = [cwm_4b[s][\"pp\"] for s in cwm_4b if cwm_4b[s][\"pp\"] is not None]\nprs_v = [cwm_4b[s][\"pr\"] for s in cwm_4b if cwm_4b[s][\"pr\"] is not None]\nfps_v = [cwm_4b[s][\"fp\"] for s in cwm_4b if cwm_4b[s][\"fp\"] is not None]\nfrs_v = [cwm_4b[s][\"fr\"] for s in cwm_4b if cwm_4b[s][\"fr\"] is not None]\nprint(\"-\" * 90)\npp_m, pp_s = ms(pps_v); pr_m, pr_s = ms(prs_v); fp_m, fp_s = ms(fps_v); fr_m, fr_s = ms(frs_v)\nprint(f\"{'Mean±Std':<8} {fmt(m,s):<10} {fmt(m2,s2):<10} {fmt(m3,s3):<10} {fmt(pp_m,pp_s):<10} {fmt(pr_m,pr_s):<10} {fmt(fp_m,fp_s):<10} {fmt(fr_m,fr_s):<10} {fmt(m4,s4):<12}\")\n\nprint()\nprint(\"=\" * 120)\nprint(\"TABLE 3: Function-level CLS vs CWM 对比 (4B)\")\nprint(\"=\" * 120)\n\ncls_accs = np.array([cls_4b[s][\"acc\"] for s in [0, 42, 123, 456, 789]])\ncwm_accs = np.array([cwm_4b[s][\"acc\"] for s in [0, 42, 123, 456, 789]])\ncls_pf1 = np.array([cls_4b[s][\"pf1\"] for s in [0, 42, 123, 456, 789]])\ncwm_pf1 = np.array([cwm_4b[s][\"pf1\"] for s in [0, 42, 123, 456, 789]])\ncls_ff1 = np.array([cls_4b[s][\"ff1\"] for s in [0, 42, 123, 456, 789]])\ncwm_ff1 = np.array([cwm_4b[s][\"ff1\"] for s in [0, 42, 123, 456, 789]])\n\ngap_acc = cls_accs - cwm_accs\ngap_pf1 = cls_pf1 - cwm_pf1\ngap_ff1 = cls_ff1 - cwm_ff1\n\nt_acc, p_acc = stats.ttest_rel(cls_accs, cwm_accs)\nt_pf1, p_pf1 = stats.ttest_rel(cls_pf1, cwm_pf1)\nt_ff1, p_ff1 = stats.ttest_rel(cls_ff1, cwm_ff1)\n\nprint(f\"{'Model':<12} {'Form':<8} {'Seeds':<8} {'Acc (mean±std)':<18} {'Pass_F1':<18} {'Fail_F1':<18}\")\nprint(\"-\" * 82)\nprint(f\"{'4B':<12} {'CLS':<8} {'5':<8} {fmt(cls_accs.mean(), cls_accs.std(ddof=1)):<18} {fmt(cls_pf1.mean(), cls_pf1.std(ddof=1)):<18} {fmt(cls_ff1.mean(), cls_ff1.std(ddof=1)):<18}\")\nprint(f\"{'4B':<12} {'CWM':<8} {'5':<8} {fmt(cwm_accs.mean(), cwm_accs.std(ddof=1)):<18} {fmt(cwm_pf1.mean(), cwm_pf1.std(ddof=1)):<18} {fmt(cwm_ff1.mean(), cwm_ff1.std(ddof=1)):<18}\")\nprint(f\"{'Gap (CLS-CWM)':<20} {'5':<8} {fmt(gap_acc.mean(), gap_acc.std(ddof=1)):<18} {fmt(gap_pf1.mean(), gap_pf1.std(ddof=1)):<18} {fmt(gap_ff1.mean(), gap_ff1.std(ddof=1)):<18}\")\nprint(f\"  Paired t-test p-value:       acc={p_acc:.4f}, pass_f1={p_pf1:.4f}, fail_f1={p_ff1:.4f}\")\n\nper_seed_gaps = {s: cls_4b[s][\"acc\"] - cwm_4b[s][\"acc\"] for s in [0, 42, 123, 456, 789]}\nprint(f\"\\n  Per-seed accuracy gaps: {', '.join(f'seed{s}={g:+.2f}pp' for s,g in per_seed_gaps.items())}\")\n\nprint()\nprint(\"=\" * 120)\nprint(\"TABLE 4: 8B Scaling (3 matched seeds)\")\nprint(\"=\" * 120)\nprint(f\"{'Model':<10} {'Size':<6} {'Form':<6} {'Seeds':<6} {'Acc (mean±std)':<18} {'Pass_F1':<18} {'Fail_F1':<18}\")\nprint(\"-\" * 82)\n\ncls8_accs = np.array([cls_8b[s][\"acc\"] for s in [42, 123, 456]])\ncwm8_accs = np.array([cwm_8b[s][\"acc\"] for s in [42, 123, 456]])\ncls8_pf1 = np.array([cls_8b[s][\"pf1\"] for s in [42, 123, 456]])\ncwm8_pf1 = np.array([cwm_8b[s][\"pf1\"] for s in [42, 123, 456]])\ncls8_ff1 = np.array([cls_8b[s][\"ff1\"] for s in [42, 123, 456]])\ncwm8_ff1 = np.array([cwm_8b[s][\"ff1\"] for s in [42, 123, 456]])\n\n# 4B matched 3 seeds for comparison\ncls4_3 = np.array([cls_4b[s][\"acc\"] for s in [42, 123, 456]])\ncwm4_3 = np.array([cwm_4b[s][\"acc\"] for s in [42, 123, 456]])\ncls4_3pf1 = np.array([cls_4b[s][\"pf1\"] for s in [42, 123, 456]])\ncwm4_3pf1 = np.array([cwm_4b[s][\"pf1\"] for s in [42, 123, 456]])\n\nprint(f\"{'Qwen3':<10} {'4B':<6} {'CLS':<6} {'3':<6} {fmt(cls4_3.mean(), cls4_3.std(ddof=1)):<18} {fmt(cls4_3pf1.mean(), cls4_3pf1.std(ddof=1)):<18} {'—':<18}\")\nprint(f\"{'Qwen3':<10} {'4B':<6} {'CWM':<6} {'3':<6} {fmt(cwm4_3.mean(), cwm4_3.std(ddof=1)):<18} {fmt(cwm4_3pf1.mean(), cwm4_3pf1.std(ddof=1)):<18} {'—':<18}\")\nprint(f\"{'Qwen3':<10} {'8B':<6} {'CLS':<6} {'3':<6} {fmt(cls8_accs.mean(), cls8_accs.std(ddof=1)):<18} {fmt(cls8_pf1.mean(), cls8_pf1.std(ddof=1)):<18} {fmt(cls8_ff1.mean(), cls8_ff1.std(ddof=1)):<18}\")\nprint(f\"{'Qwen3':<10} {'8B':<6} {'CWM':<6} {'3':<6} {fmt(cwm8_accs.mean(), cwm8_accs.std(ddof=1)):<18} {fmt(cwm8_pf1.mean(), cwm8_pf1.std(ddof=1)):<18} {fmt(cwm8_ff1.mean(), cwm8_ff1.std(ddof=1)):<18}\")\n\ngap_4b_3 = cls4_3 - cwm4_3\ngap_8b_3 = cls8_accs - cwm8_accs\nprint(f\"\\n  CLS-CWM gap (4B, 3-seed): {fmt(gap_4b_3.mean(), gap_4b_3.std(ddof=1))}pp\")\nprint(f\"  CLS-CWM gap (8B, 3-seed): {fmt(gap_8b_3.mean(), gap_8b_3.std(ddof=1))}pp\")\nprint(f\"  Scaling: 4B→8B CLS gain = {cls8_accs.mean()-cls4_3.mean():+.2f}pp, CWM gain = {cwm8_accs.mean()-cwm4_3.mean():+.2f}pp\")\nprint(f\"  Gap widening: 8B gap ({gap_8b_3.mean():.2f}) vs 4B gap ({gap_4b_3.mean():.2f}) = {gap_8b_3.mean()-gap_4b_3.mean():+.2f}pp wider at 8B\")\n\nper_seed_8b = {s: cls_8b[s][\"acc\"] - cwm_8b[s][\"acc\"] for s in [42, 123, 456]}\nprint(f\"  Per-seed 8B gaps: {', '.join(f'seed{s}={g:+.2f}pp' for s,g in per_seed_8b.items())}\")\n\nprint()\nprint(\"=\" * 120)\nprint(\"TABLE 5: Trajectory-level (5 seeds)\")\nprint(\"=\" * 120)\nprint(f\"{'Seed':<8} {'Accuracy':<10} {'Unres_F1':<10} {'Res_F1':<10} {'Unres_P':<10} {'Unres_R':<10} {'Res_P':<10} {'Res_R':<10} {'Consist':<10}\")\nprint(\"-\" * 88)\nfor s in [0, 42, 123, 456, 789]:\n    d = traj[s]\n    up = f\"{d['up']:.2f}\" if d['up'] else \"—\"\n    ur = f\"{d['ur']:.2f}\" if d['ur'] else \"—\"\n    rp = f\"{d['rp']:.2f}\" if d['rp'] else \"—\"\n    rr = f\"{d['rr']:.2f}\" if d['rr'] else \"—\"\n    print(f\"{s:<8} {d['acc']:<10.2f} {d['uf1']:<10.2f} {d['rf1']:<10.2f} {up:<10} {ur:<10} {rp:<10} {rr:<10} {d['con']:<10.2f}\")\n\ntaccs = [traj[s][\"acc\"] for s in traj]\ntuf1 = [traj[s][\"uf1\"] for s in traj]\ntrf1 = [traj[s][\"rf1\"] for s in traj]\ntcon = [traj[s][\"con\"] for s in traj]\nm1,s1=ms(taccs); m2,s2=ms(tuf1); m3,s3=ms(trf1); m4,s4=ms(tcon)\nprint(\"-\" * 88)\nprint(f\"{'Mean±Std':<8} {fmt(m1,s1):<10} {fmt(m2,s2):<10} {fmt(m3,s3):<10} {'—':<10} {'—':<10} {'—':<10} {'—':<10} {fmt(m4,s4):<10}\")\n\nprint()\nprint(\"=\" * 120)\nprint(\"TABLE 6: Zero-shot LLM Judge\")\nprint(\"=\" * 120)\nprint(f\"{'Model':<20} {'Accuracy':<10} {'Pass_F1':<10} {'Fail_F1':<10} {'Pass_P':<10} {'Pass_R':<10} {'Fail_P':<10} {'Fail_R':<10}\")\nprint(\"-\" * 90)\nfor name, d in llm_judge.items():\n    print(f\"{'Qwen3-'+name+' 0-shot':<20} {d['acc']:<10.2f} {d['pf1']:<10.2f} {d['ff1']:<10.2f} {d['pp']:<10.2f} {d['pr']:<10.2f} {d['fp']:<10.2f} {d['fr']:<10.2f}\")\n# Fine-tuned 4B for reference\nm_cls, _ = ms([cls_4b[s][\"acc\"] for s in cls_4b])\nm_cls_pf1, _ = ms([cls_4b[s][\"pf1\"] for s in cls_4b])\nm_cls_ff1, _ = ms([cls_4b[s][\"ff1\"] for s in cls_4b])\nprint(f\"{'FT 4B CLS (ref)':<20} {m_cls:<10.2f} {m_cls_pf1:<10.2f} {m_cls_ff1:<10.2f}\")\nprint(f\"\\n  Gap vs FT 4B:  8B 0-shot: {64.40 - m_cls:+.2f}pp,  32B 0-shot: {71.69 - m_cls:+.2f}pp\")\n\nprint()\nprint(\"=\" * 120)\nprint(\"TABLE 7: Repo-level (completed results)\")\nprint(\"=\" * 120)\nprint(f\"{'Exp':<22} {'Acc':<8} {'F1_macro':<10} {'Pass_F1':<10} {'Fail_F1':<10} {'Unparse':<10} {'Majority':<10} {'Note'}\")\nprint(\"-\" * 110)\nfor name, d in repo.items():\n    acc = f\"{d['acc']:.2f}\" if d.get('acc') else \"—\"\n    f1m = f\"{d['f1m']:.2f}\" if d.get('f1m') else \"—\"\n    pf1 = f\"{d['pf1']:.2f}\" if d.get('pf1') else \"—\"\n    ff1 = f\"{d['ff1']:.2f}\" if d.get('ff1') else \"—\"\n    unp = str(d.get('unp','—'))\n    print(f\"{name:<22} {acc:<8} {f1m:<10} {pf1:<10} {ff1:<10} {unp:<10} {'72.96%':<10} {d['note']}\")\n\nprint()\nprint(\"=\" * 120)\nprint(\"TABLE 8: Analysis experiments\")\nprint(\"=\" * 120)\n\nprint(\"\\n--- 5-paired-clustered-bootstrap (CLS vs TRAJ equivalence) ---\")\nprint(\"  Pooled gap (CLS-TRAJ): -0.45pp, 95% CI [-1.71, +0.84]\")\nprint(\"  Paired t-test p-value: 0.499 (not significant)\")\nprint(\"  TOST equivalence p-value: 0.0071 (equivalent within ±2pp margin)\")\nprint(\"  Per-seed gaps: seed42=-0.97, seed123=+1.45, seed456=-1.84, seed789=-0.78, seed0=-0.29\")\n\nprint(\"\\n--- per-test-majority-voting (K=3, temp=0.7) ---\")\nprint(\"  Greedy accuracy: 87.51%  →  Majority vote: 86.83%  (Δ = -0.69pp)\")\nprint(\"  Unanimous rate: 93.3%, split samples: 127, net flips: -13\")\n\nprint(\"\\n--- block-corr-empirical (error correlation within problems) ---\")\nprint(\"  ICC = 0.191 (p < 1e-10), design effect = 3.97\")\nprint(\"  All-correct ratio: 2.81× expected under i.i.d.\")\nprint(\"  Error std ratio: 1.89× expected under i.i.d.\")\n\nprint(\"\\n--- oracle-f2p-stratified (per-test advantage by F2P count) ---\")\nprint(\"  T=1 (68.7%): block adv = -0.09pp (no advantage)\")\nprint(\"  T=2 (19.1%): block adv = 31.69pp\")\nprint(\"  T=3-5 (7.1%): block adv = 40.74pp\")\nprint(\"  T≥6 (5.1%): block adv = 40.06pp\")\nprint(\"  T=2 contributes 55.3% of overall advantage\")\n\nprint(\"\\n--- mvp-a-oracle-sim (total F2P+P2P simulation) ---\")\nprint(\"  10% regression threshold: iid_adv=13.2pp, block_adv=8.3pp (PASS)\")\nprint(\"  5% regression threshold: iid_adv=-1.0pp, block_adv=-0.5pp (FAIL)\")\nprint(\"  F2P real (T=1 median): iid_adv=1.98pp, block_adv=10.88pp\")\n\nprint(\"\\n--- p2p-regression-rate ---\")\nprint(\"  Conclusion: NEGATIVE\")\nprint(\"  P2P regression rate: 1.04% mean / 0% median (on CoderForge SWE-bench Verified)\")\n\nprint(\"\\n--- per-test-precision-recall (diagnostic analysis) ---\")\nprint(\"  114 problems: 48 (42.1%) perfectly predicted\")\nprint(\"  Median problem fail-F1: 94.12%\")\nprint(\"  Best mutation type: return_value (97.26%), Worst: off_by_one (82.56%)\")\n\nprint(\"\\n--- mvp-b-data-prep (HumanEval/MBPP dataset) ---\")\nprint(\"  Total: 19,076 samples (HumanEval 5,575 + MBPP 13,501)\")\nprint(\"  Class balance: pass 52.0% / fail 48.0%\")\n\nprint(\"\\n--- mvp-b-train (initial pilot) ---\")\nprint(\"  Accuracy: 87.5%, pass_f1: 87.1%, fail_f1: 87.9%\")\nprint(\"  Majority baseline: 52.0%, gap: +35.5pp\")\n\nprint()\nprint(\"=\" * 120)\nprint(\"CORE COMPARISON NUMBERS (for paper)\")\nprint(\"=\" * 120)\n\n# 1. 4B CLS vs CWM gap (5-seed)\nprint(f\"\\n1. 4B CLS vs CWM (5-seed paired):\")\nprint(f\"   Accuracy gap: {fmt(gap_acc.mean(), gap_acc.std(ddof=1))}pp\")\nprint(f\"   Pass_F1 gap:  {fmt(gap_pf1.mean(), gap_pf1.std(ddof=1))}pp\")\nprint(f\"   Fail_F1 gap:  {fmt(gap_ff1.mean(), gap_ff1.std(ddof=1))}pp\")\nprint(f\"   Paired t-test: t={t_acc:.3f}, p={p_acc:.4f}\")\n\n# 2. 8B CLS vs CWM gap (3-seed)\ngap8_acc = cls8_accs - cwm8_accs\ngap8_pf1 = cls8_pf1 - cwm8_pf1\ngap8_ff1 = cls8_ff1 - cwm8_ff1\nt8, p8 = stats.ttest_rel(cls8_accs, cwm8_accs)\nprint(f\"\\n2. 8B CLS vs CWM (3-seed paired):\")\nprint(f\"   Accuracy gap: {fmt(gap8_acc.mean(), gap8_acc.std(ddof=1))}pp\")\nprint(f\"   Pass_F1 gap:  {fmt(gap8_pf1.mean(), gap8_pf1.std(ddof=1))}pp\")\nprint(f\"   Fail_F1 gap:  {fmt(gap8_ff1.mean(), gap8_ff1.std(ddof=1))}pp\")\nprint(f\"   Paired t-test: t={t8:.3f}, p={p8:.4f}\")\n\n# 3. Scaling effect\nprint(f\"\\n3. Scaling 4B → 8B (matched 3 seeds: 42, 123, 456):\")\nprint(f\"   CLS accuracy gain: {cls8_accs.mean() - cls4_3.mean():+.2f}pp ({fmt(cls4_3.mean(), cls4_3.std(ddof=1))} → {fmt(cls8_accs.mean(), cls8_accs.std(ddof=1))})\")\nprint(f\"   CWM accuracy gain: {cwm8_accs.mean() - cwm4_3.mean():+.2f}pp ({fmt(cwm4_3.mean(), cwm4_3.std(ddof=1))} → {fmt(cwm8_accs.mean(), cwm8_accs.std(ddof=1))})\")\nprint(f\"   4B CLS-CWM gap: {fmt(gap_4b_3.mean(), gap_4b_3.std(ddof=1))}pp\")\nprint(f\"   8B CLS-CWM gap: {fmt(gap8_acc.mean(), gap8_acc.std(ddof=1))}pp\")\nprint(f\"   Gap widening: {gap8_acc.mean() - gap_4b_3.mean():+.2f}pp at 8B → CWM bottleneck amplified\")\n\n# 4. Fine-tuned 4B vs zero-shot 32B\nprint(f\"\\n4. Fine-tuned 4B vs Zero-shot 32B:\")\nft4b_mean = cls_accs.mean()\nprint(f\"   FT 4B CLS (5-seed): {ft4b_mean:.2f}%\")\nprint(f\"   Zero-shot 32B:      {71.69}%\")\nprint(f\"   Gap: {ft4b_mean - 71.69:+.2f}pp in favor of FT 4B\")\nprint(f\"   → Fine-tuned 4B dominates 8× larger zero-shot model\")\n\n# 5. Repo-level CLS vs CWM\nprint(f\"\\n5. Repo-level CLS vs CWM (seed=42, CLS v5 only valid):\")\nprint(f\"   CLS v5: accuracy=76.92%, F1_macro=73.90% (majority baseline=72.96%)\")\nprint(f\"   CWM v10: accuracy=69.91% (93% unparseable → eval invalid)\")\nprint(f\"   CWM v11: accuracy=66.6% (killed, subset-500, 75% unparseable)\")\nprint(f\"   ⚠️ CWM repo-level results unreliable; only CLS v5 is valid reference\")\n\n# 6. TOST equivalence\nprint(f\"\\n6. TOST equivalence (CLS aggregated ≈ TRAJ at variant level):\")\nprint(f\"   Variant-level CLS vs TRAJ gap: -0.45pp, 95% CI [-1.71, +0.84]\")\nprint(f\"   TOST p-value: 0.0071 (< 0.05 → statistically equivalent within ±2pp)\")\nprint(f\"   → Per-test CLS aggregated to variant-level is equivalent to dedicated TRAJ model\")\n\n# 7. Summary table of means\nprint()\nprint(\"=\" * 120)\nprint(\"SUMMARY OF MEANS\")\nprint(\"=\" * 120)\nprint(f\"{'Configuration':<35} {'Accuracy':<12} {'Pass_F1':<12} {'Fail_F1':<12}\")\nprint(\"-\" * 71)\nprint(f\"{'4B CLS (5-seed)':<35} {fmt(cls_accs.mean(), cls_accs.std(ddof=1)):<12} {fmt(cls_pf1.mean(), cls_pf1.std(ddof=1)):<12} {fmt(cls_ff1.mean(), cls_ff1.std(ddof=1)):<12}\")\nprint(f\"{'4B CWM (5-seed)':<35} {fmt(cwm_accs.mean(), cwm_accs.std(ddof=1)):<12} {fmt(cwm_pf1.mean(), cwm_pf1.std(ddof=1)):<12} {fmt(cwm_ff1.mean(), cwm_ff1.std(ddof=1)):<12}\")\nprint(f\"{'8B CLS (3-seed)':<35} {fmt(cls8_accs.mean(), cls8_accs.std(ddof=1)):<12} {fmt(cls8_pf1.mean(), cls8_pf1.std(ddof=1)):<12} {fmt(cls8_ff1.mean(), cls8_ff1.std(ddof=1)):<12}\")\nprint(f\"{'8B CWM (3-seed)':<35} {fmt(cwm8_accs.mean(), cwm8_accs.std(ddof=1)):<12} {fmt(cwm8_pf1.mean(), cwm8_pf1.std(ddof=1)):<12} {fmt(cwm8_ff1.mean(), cwm8_ff1.std(ddof=1)):<12}\")\nprint(f\"{'Traj-level (5-seed)':<35} {fmt(np.mean(taccs), np.std(taccs, ddof=1)):<12} {'—':<12} {'—':<12}\")\nprint(f\"{'Zero-shot 8B':<35} {'64.40':<12} {'50.50':<12} {'72.20':<12}\")\nprint(f\"{'Zero-shot 32B':<35} {'71.69':<12} {'65.68':<12} {'75.91':<12}\")\nprint(f\"{'Repo-level CLS v5 (1-seed)':<35} {'76.92':<12} {'82.78':<12} {'65.01':<12}\")\n\nPYEOF\n",
  "description": "Compute all summary tables and statistics"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_experiment-summary-table_20260514T003543",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 << 'PYEOF'\nimport numpy as np\nfrom scipy import stats\n\n# ============================================================\n# DATA: Function-level CLS 4B (5 seeds)\n# ============================================================\ncls_4b = {\n    0:   {\"acc\": 87.94, \"pf1\": 87.79, \"ff1\": 88.08, \"pp\": 92.13, \"pr\": 83.84, \"fp\": 84.20, \"fr\": 92.32},\n    42:  {\"acc\": 87.83, \"pf1\": 88.06, \"ff1\": 87.59, \"pp\": 89.45, \"pr\": 86.71, \"fp\": 86.20, \"fr\": 89.04},\n    123: {\"acc\": 89.52, \"pf1\": 89.64, \"ff1\": 89.40, \"pp\": 91.76, \"pr\": 87.63, \"fp\": 87.34, \"fr\": 91.56},\n    456: {\"acc\": 87.88, \"pf1\": 87.53, \"ff1\": 88.21, \"pp\": 93.60, \"pr\": 82.21, \"fp\": 83.12, \"fr\": 93.97},\n    789: {\"acc\": 89.00, \"pf1\": 88.90, \"ff1\": 89.10, \"pp\": 93.30, \"pr\": 84.90, \"fp\": 85.20, \"fr\": 93.40},\n}\n\n# ============================================================\n# DATA: Function-level CWM 4B (5 seeds)\n# ============================================================\ncwm_4b = {\n    0:   {\"acc\": 87.57, \"pf1\": 87.18, \"ff1\": 87.93, \"pp\": 93.45, \"pr\": 81.70, \"fp\": 82.71, \"fr\": 93.86, \"em\": 84.29},\n    42:  {\"acc\": 87.51, \"pf1\": 87.31, \"ff1\": 87.71, \"pp\": 92.06, \"pr\": 83.03, \"fp\": 83.53, \"fr\": 92.32, \"em\": 84.02},\n    123: {\"acc\": 87.20, \"pf1\": 86.95, \"ff1\": 87.44, \"pp\": None, \"pr\": None, \"fp\": None, \"fr\": None, \"em\": 84.44},\n    456: {\"acc\": 86.98, \"pf1\": 86.66, \"ff1\": 87.29, \"pp\": 92.26, \"pr\": 81.70, \"fp\": 82.52, \"fr\": 92.65, \"em\": 84.02},\n    789: {\"acc\": 86.67, \"pf1\": 86.74, \"ff1\": 86.60, \"pp\": 89.37, \"pr\": 84.25, \"fp\": 84.09, \"fr\": 89.25, \"em\": 83.97},\n}\n\n# ============================================================\n# DATA: Function-level CLS 8B (3 seeds)\n# ============================================================\ncls_8b = {\n    42:  {\"acc\": 90.48, \"pf1\": 90.86, \"ff1\": 90.06, \"pp\": 90.22, \"pr\": 91.51, \"fp\": 90.76, \"fr\": 89.36},\n    123: {\"acc\": 89.37, \"pf1\": 89.54, \"ff1\": 89.19, \"pp\": 91.20, \"pr\": 87.93, \"fp\": 87.54, \"fr\": 90.90},\n    # Note: cls8b-seed123 registry has 89.4 but cls8b-eval-seed123 has 89.37 - use the eval version\n    456: {\"acc\": 88.31, \"pf1\": 88.20, \"ff1\": 88.41, \"pp\": 92.29, \"pr\": 84.46, \"fp\": 84.72, \"fr\": 92.43},\n}\n\n# ============================================================\n# DATA: Function-level CWM 8B (3 seeds)\n# ============================================================\ncwm_8b = {\n    42:  {\"acc\": 87.67, \"pf1\": 87.57, \"ff1\": 87.77, \"pp\": 91.53, \"pr\": 83.95, \"fp\": 84.19, \"fr\": 91.67, \"em\": 84.39},\n    123: {\"acc\": 86.98, \"pf1\": 86.83, \"ff1\": 87.13, \"pp\": 91.12, \"pr\": 82.92, \"fp\": 83.30, \"fr\": 91.34, \"em\": 84.13},\n    456: {\"acc\": 86.24, \"pf1\": 85.96, \"ff1\": 86.51, \"pp\": 91.08, \"pr\": 81.39, \"fp\": 82.09, \"fr\": 91.45, \"em\": 82.80},\n}\n\n# ============================================================\n# DATA: Trajectory-level (5 seeds)\n# ============================================================\ntraj = {\n    0:   {\"acc\": 85.66, \"uf1\": 87.37, \"rf1\": 83.41, \"up\": 82.71, \"ur\": 92.59, \"rp\": 90.07, \"rr\": 77.66, \"con\": 79.55},\n    42:  {\"acc\": 85.66, \"uf1\": 87.50, \"rf1\": 83.18, \"up\": None, \"ur\": None, \"rp\": None, \"rr\": None, \"con\": 79.94},\n    123: {\"acc\": 85.47, \"uf1\": 87.00, \"rf1\": 83.52, \"up\": 83.53, \"ur\": 90.78, \"rp\": 88.17, \"rr\": 79.33, \"con\": 78.59},\n    456: {\"acc\": 87.40, \"uf1\": 88.70, \"rf1\": 85.80, \"up\": 85.70, \"ur\": 91.90, \"rp\": 89.70, \"rr\": 82.30, \"con\": 78.80},\n    789: {\"acc\": 87.31, \"uf1\": 88.27, \"rf1\": 86.17, \"up\": 87.41, \"ur\": 89.15, \"rp\": 87.18, \"rr\": 85.18, \"con\": 76.74},\n}\n\n# ============================================================\n# DATA: LLM Judge zero-shot\n# ============================================================\nllm_judge = {\n    \"8B\":  {\"acc\": 64.40, \"pf1\": 50.50, \"ff1\": 72.20, \"pp\": 90.0, \"pr\": 35.1, \"fp\": 57.9, \"fr\": 95.8},\n    \"32B\": {\"acc\": 71.69, \"pf1\": 65.68, \"ff1\": 75.91, \"pp\": 88.12, \"pr\": 52.35, \"fp\": 64.40, \"fr\": 92.43},\n}\n\n# ============================================================\n# DATA: Repo-level\n# ============================================================\nrepo = {\n    \"cls-v4\": {\"acc\": 66.11, \"f1m\": 56.61, \"pf1\": 76.9, \"ff1\": 36.3, \"pp\": 76.5, \"pr\": 77.4, \"fp\": 36.9, \"fr\": 35.7, \"unp\": 132, \"note\": \"early stop, old hyperparams\"},\n    \"cls-v5\": {\"acc\": 76.92, \"f1m\": 73.90, \"pf1\": 82.78, \"ff1\": 65.01, \"pp\": 90.83, \"pr\": 76.04, \"fp\": 55.09, \"fr\": 79.29, \"unp\": 132, \"note\": \"best CLS, corrected hyperparams\"},\n    \"cwm-v10\": {\"acc\": 69.91, \"f1m\": 46.71, \"pf1\": 81.87, \"ff1\": 11.54, \"unp\": 9102, \"note\": \"93% unparseable, eval invalid\"},\n    \"cwm-v11\": {\"acc\": 66.60, \"f1m\": 52.99, \"pf1\": 78.30, \"ff1\": 27.70, \"unp\": 376, \"note\": \"killed, mixed transformers versions, 500-sample subset\"},\n    \"cls-8b\":  {\"acc\": 71.37, \"f1m\": 69.05, \"pf1\": 77.53, \"ff1\": 60.57, \"pp\": 90.71, \"pr\": 67.69, \"fp\": 48.26, \"fr\": 81.29, \"unp\": 136, \"note\": \"below majority baseline, transformers 5.8.0 mismatch\"},\n}\n\ndef ms(vals):\n    a = np.array(vals)\n    return np.mean(a), np.std(a, ddof=1)\n\ndef fmt(m, s):\n    return f\"{m:.2f} ± {s:.2f}\"\n\n# ============================================================\n# COMPUTE TABLES\n# ============================================================\n\nprint(\"=\" * 120)\nprint(\"TABLE 1: Function-level CLS (per-test classification, 4B, 5 seeds)\")\nprint(\"=\" * 120)\nprint(f\"{'Seed':<8} {'Accuracy':<10} {'Pass_F1':<10} {'Fail_F1':<10} {'Pass_P':<10} {'Pass_R':<10} {'Fail_P':<10} {'Fail_R':<10}\")\nprint(\"-\" * 78)\nfor s in [0, 42, 123, 456, 789]:\n    d = cls_4b[s]\n    print(f\"{s:<8} {d['acc']:<10.2f} {d['pf1']:<10.2f} {d['ff1']:<10.2f} {d['pp']:<10.2f} {d['pr']:<10.2f} {d['fp']:<10.2f} {d['fr']:<10.2f}\")\naccs = [cls_4b[s][\"acc\"] for s in cls_4b]\npf1s = [cls_4b[s][\"pf1\"] for s in cls_4b]\nff1s = [cls_4b[s][\"ff1\"] for s in cls_4b]\npps = [cls_4b[s][\"pp\"] for s in cls_4b]\nprs = [cls_4b[s][\"pr\"] for s in cls_4b]\nfps = [cls_4b[s][\"fp\"] for s in cls_4b]\nfrs = [cls_4b[s][\"fr\"] for s in cls_4b]\nm, s = ms(accs); m2,s2=ms(pf1s); m3,s3=ms(ff1s); m4,s4=ms(pps); m5,s5=ms(prs); m6,s6=ms(fps); m7,s7=ms(frs)\nprint(\"-\" * 78)\nprint(f\"{'Mean±Std':<8} {fmt(m,s):<10} {fmt(m2,s2):<10} {fmt(m3,s3):<10} {fmt(m4,s4):<10} {fmt(m5,s5):<10} {fmt(m6,s6):<10} {fmt(m7,s7):<10}\")\n\nprint()\nprint(\"=\" * 120)\nprint(\"TABLE 2: Function-level CWM (execution simulation, 4B, 5 seeds)\")\nprint(\"=\" * 120)\nprint(f\"{'Seed':<8} {'Accuracy':<10} {'Pass_F1':<10} {'Fail_F1':<10} {'Pass_P':<10} {'Pass_R':<10} {'Fail_P':<10} {'Fail_R':<10} {'ExactMatch':<12}\")\nprint(\"-\" * 90)\nfor s in [0, 42, 123, 456, 789]:\n    d = cwm_4b[s]\n    pp_str = f\"{d['pp']:.2f}\" if d['pp'] else \"—\"\n    pr_str = f\"{d['pr']:.2f}\" if d['pr'] else \"—\"\n    fp_str = f\"{d['fp']:.2f}\" if d['fp'] else \"—\"\n    fr_str = f\"{d['fr']:.2f}\" if d['fr'] else \"—\"\n    print(f\"{s:<8} {d['acc']:<10.2f} {d['pf1']:<10.2f} {d['ff1']:<10.2f} {pp_str:<10} {pr_str:<10} {fp_str:<10} {fr_str:<10} {d['em']:<12.2f}\")\naccs_c = [cwm_4b[s][\"acc\"] for s in cwm_4b]\npf1s_c = [cwm_4b[s][\"pf1\"] for s in cwm_4b]\nff1s_c = [cwm_4b[s][\"ff1\"] for s in cwm_4b]\nems = [cwm_4b[s][\"em\"] for s in cwm_4b]\nm, s = ms(accs_c); m2,s2=ms(pf1s_c); m3,s3=ms(ff1s_c); m4,s4=ms(ems)\npps_v = [cwm_4b[s][\"pp\"] for s in cwm_4b if cwm_4b[s][\"pp\"] is not None]\nprs_v = [cwm_4b[s][\"pr\"] for s in cwm_4b if cwm_4b[s][\"pr\"] is not None]\nfps_v = [cwm_4b[s][\"fp\"] for s in cwm_4b if cwm_4b[s][\"fp\"] is not None]\nfrs_v = [cwm_4b[s][\"fr\"] for s in cwm_4b if cwm_4b[s][\"fr\"] is not None]\nprint(\"-\" * 90)\npp_m, pp_s = ms(pps_v); pr_m, pr_s = ms(prs_v); fp_m, fp_s = ms(fps_v); fr_m, fr_s = ms(frs_v)\nprint(f\"{'Mean±Std':<8} {fmt(m,s):<10} {fmt(m2,s2):<10} {fmt(m3,s3):<10} {fmt(pp_m,pp_s):<10} {fmt(pr_m,pr_s):<10} {fmt(fp_m,fp_s):<10} {fmt(fr_m,fr_s):<10} {fmt(m4,s4):<12}\")\n\nprint()\nprint(\"=\" * 120)\nprint(\"TABLE 3: Function-level CLS vs CWM 对比 (4B)\")\nprint(\"=\" * 120)\n\ncls_accs = np.array([cls_4b[s][\"acc\"] for s in [0, 42, 123, 456, 789]])\ncwm_accs = np.array([cwm_4b[s][\"acc\"] for s in [0, 42, 123, 456, 789]])\ncls_pf1 = np.array([cls_4b[s][\"pf1\"] for s in [0, 42, 123, 456, 789]])\ncwm_pf1 = np.array([cwm_4b[s][\"pf1\"] for s in [0, 42, 123, 456, 789]])\ncls_ff1 = np.array([cls_4b[s][\"ff1\"] for s in [0, 42, 123, 456, 789]])\ncwm_ff1 = np.array([cwm_4b[s][\"ff1\"] for s in [0, 42, 123, 456, 789]])\n\ngap_acc = cls_accs - cwm_accs\ngap_pf1 = cls_pf1 - cwm_pf1\ngap_ff1 = cls_ff1 - cwm_ff1\n\nt_acc, p_acc = stats.ttest_rel(cls_accs, cwm_accs)\nt_pf1, p_pf1 = stats.ttest_rel(cls_pf1, cwm_pf1)\nt_ff1, p_ff1 = stats.ttest_rel(cls_ff1, cwm_ff1)\n\nprint(f\"{'Model':<12} {'Form':<8} {'Seeds':<8} {'Acc (mean±std)':<18} {'Pass_F1':<18} {'Fail_F1':<18}\")\nprint(\"-\" * 82)\nprint(f\"{'4B':<12} {'CLS':<8} {'5':<8} {fmt(cls_accs.mean(), cls_accs.std(ddof=1)):<18} {fmt(cls_pf1.mean(), cls_pf1.std(ddof=1)):<18} {fmt(cls_ff1.mean(), cls_ff1.std(ddof=1)):<18}\")\nprint(f\"{'4B':<12} {'CWM':<8} {'5':<8} {fmt(cwm_accs.mean(), cwm_accs.std(ddof=1)):<18} {fmt(cwm_pf1.mean(), cwm_pf1.std(ddof=1)):<18} {fmt(cwm_ff1.mean(), cwm_ff1.std(ddof=1)):<18}\")\nprint(f\"{'Gap (CLS-CWM)':<20} {'5':<8} {fmt(gap_acc.mean(), gap_acc.std(ddof=1)):<18} {fmt(gap_pf1.mean(), gap_pf1.std(ddof=1)):<18} {fmt(gap_ff1.mean(), gap_ff1.std(ddof=1)):<18}\")\nprint(f\"  Paired t-test p-value:       acc={p_acc:.4f}, pass_f1={p_pf1:.4f}, fail_f1={p_ff1:.4f}\")\n\nper_seed_gaps = {s: cls_4b[s][\"acc\"] - cwm_4b[s][\"acc\"] for s in [0, 42, 123, 456, 789]}\nprint(f\"\\n  Per-seed accuracy gaps: {', '.join(f'seed{s}={g:+.2f}pp' for s,g in per_seed_gaps.items())}\")\n\nprint()\nprint(\"=\" * 120)\nprint(\"TABLE 4: 8B Scaling (3 matched seeds)\")\nprint(\"=\" * 120)\nprint(f\"{'Model':<10} {'Size':<6} {'Form':<6} {'Seeds':<6} {'Acc (mean±std)':<18} {'Pass_F1':<18} {'Fail_F1':<18}\")\nprint(\"-\" * 82)\n\ncls8_accs = np.array([cls_8b[s][\"acc\"] for s in [42, 123, 456]])\ncwm8_accs = np.array([cwm_8b[s][\"acc\"] for s in [42, 123, 456]])\ncls8_pf1 = np.array([cls_8b[s][\"pf1\"] for s in [42, 123, 456]])\ncwm8_pf1 = np.array([cwm_8b[s][\"pf1\"] for s in [42, 123, 456]])\ncls8_ff1 = np.array([cls_8b[s][\"ff1\"] for s in [42, 123, 456]])\ncwm8_ff1 = np.array([cwm_8b[s][\"ff1\"] for s in [42, 123, 456]])\n\n# 4B matched 3 seeds for comparison\ncls4_3 = np.array([cls_4b[s][\"acc\"] for s in [42, 123, 456]])\ncwm4_3 = np.array([cwm_4b[s][\"acc\"] for s in [42, 123, 456]])\ncls4_3pf1 = np.array([cls_4b[s][\"pf1\"] for s in [42, 123, 456]])\ncwm4_3pf1 = np.array([cwm_4b[s][\"pf1\"] for s in [42, 123, 456]])\n\nprint(f\"{'Qwen3':<10} {'4B':<6} {'CLS':<6} {'3':<6} {fmt(cls4_3.mean(), cls4_3.std(ddof=1)):<18} {fmt(cls4_3pf1.mean(), cls4_3pf1.std(ddof=1)):<18} {'—':<18}\")\nprint(f\"{'Qwen3':<10} {'4B':<6} {'CWM':<6} {'3':<6} {fmt(cwm4_3.mean(), cwm4_3.std(ddof=1)):<18} {fmt(cwm4_3pf1.mean(), cwm4_3pf1.std(ddof=1)):<18} {'—':<18}\")\nprint(f\"{'Qwen3':<10} {'8B':<6} {'CLS':<6} {'3':<6} {fmt(cls8_accs.mean(), cls8_accs.std(ddof=1)):<18} {fmt(cls8_pf1.mean(), cls8_pf1.std(ddof=1)):<18} {fmt(cls8_ff1.mean(), cls8_ff1.std(ddof=1)):<18}\")\nprint(f\"{'Qwen3':<10} {'8B':<6} {'CWM':<6} {'3':<6} {fmt(cwm8_accs.mean(), cwm8_accs.std(ddof=1)):<18} {fmt(cwm8_pf1.mean(), cwm8_pf1.std(ddof=1)):<18} {fmt(cwm8_ff1.mean(), cwm8_ff1.std(ddof=1)):<18}\")\n\ngap_4b_3 = cls4_3 - cwm4_3\ngap_8b_3 = cls8_accs - cwm8_accs\nprint(f\"\\n  CLS-CWM gap (4B, 3-seed): {fmt(gap_4b_3.mean(), gap_4b_3.std(ddof=1))}pp\")\nprint(f\"  CLS-CWM gap (8B, 3-seed): {fmt(gap_8b_3.mean(), gap_8b_3.std(ddof=1))}pp\")\nprint(f\"  Scaling: 4B→8B CLS gain = {cls8_accs.mean()-cls4_3.mean():+.2f}pp, CWM gain = {cwm8_accs.mean()-cwm4_3.mean():+.2f}pp\")\nprint(f\"  Gap widening: 8B gap ({gap_8b_3.mean():.2f}) vs 4B gap ({gap_4b_3.mean():.2f}) = {gap_8b_3.mean()-gap_4b_3.mean():+.2f}pp wider at 8B\")\n\nper_seed_8b = {s: cls_8b[s][\"acc\"] - cwm_8b[s][\"acc\"] for s in [42, 123, 456]}\nprint(f\"  Per-seed 8B gaps: {', '.join(f'seed{s}={g:+.2f}pp' for s,g in per_seed_8b.items())}\")\n\nprint()\nprint(\"=\" * 120)\nprint(\"TABLE 5: Trajectory-level (5 seeds)\")\nprint(\"=\" * 120)\nprint(f\"{'Seed':<8} {'Accuracy':<10} {'Unres_F1':<10} {'Res_F1':<10} {'Unres_P':<10} {'Unres_R':<10} {'Res_P':<10} {'Res_R':<10} {'Consist':<10}\")\nprint(\"-\" * 88)\nfor s in [0, 42, 123, 456, 789]:\n    d = traj[s]\n    up = f\"{d['up']:.2f}\" if d['up'] else \"—\"\n    ur = f\"{d['ur']:.2f}\" if d['ur'] else \"—\"\n    rp = f\"{d['rp']:.2f}\" if d['rp'] else \"—\"\n    rr = f\"{d['rr']:.2f}\" if d['rr'] else \"—\"\n    print(f\"{s:<8} {d['acc']:<10.2f} {d['uf1']:<10.2f} {d['rf1']:<10.2f} {up:<10} {ur:<10} {rp:<10} {rr:<10} {d['con']:<10.2f}\")\n\ntaccs = [traj[s][\"acc\"] for s in traj]\ntuf1 = [traj[s][\"uf1\"] for s in traj]\ntrf1 = [traj[s][\"rf1\"] for s in traj]\ntcon = [traj[s][\"con\"] for s in traj]\nm1,s1=ms(taccs); m2,s2=ms(tuf1); m3,s3=ms(trf1); m4,s4=ms(tcon)\nprint(\"-\" * 88)\nprint(f\"{'Mean±Std':<8} {fmt(m1,s1):<10} {fmt(m2,s2):<10} {fmt(m3,s3):<10} {'—':<10} {'—':<10} {'—':<10} {'—':<10} {fmt(m4,s4):<10}\")\n\nprint()\nprint(\"=\" * 120)\nprint(\"TABLE 6: Zero-shot LLM Judge\")\nprint(\"=\" * 120)\nprint(f\"{'Model':<20} {'Accuracy':<10} {'Pass_F1':<10} {'Fail_F1':<10} {'Pass_P':<10} {'Pass_R':<10} {'Fail_P':<10} {'Fail_R':<10}\")\nprint(\"-\" * 90)\nfor name, d in llm_judge.items():\n    print(f\"{'Qwen3-'+name+' 0-shot':<20} {d['acc']:<10.2f} {d['pf1']:<10.2f} {d['ff1']:<10.2f} {d['pp']:<10.2f} {d['pr']:<10.2f} {d['fp']:<10.2f} {d['fr']:<10.2f}\")\n# Fine-tuned 4B for reference\nm_cls, _ = ms([cls_4b[s][\"acc\"] for s in cls_4b])\nm_cls_pf1, _ = ms([cls_4b[s][\"pf1\"] for s in cls_4b])\nm_cls_ff1, _ = ms([cls_4b[s][\"ff1\"] for s in cls_4b])\nprint(f\"{'FT 4B CLS (ref)':<20} {m_cls:<10.2f} {m_cls_pf1:<10.2f} {m_cls_ff1:<10.2f}\")\nprint(f\"\\n  Gap vs FT 4B:  8B 0-shot: {64.40 - m_cls:+.2f}pp,  32B 0-shot: {71.69 - m_cls:+.2f}pp\")\n\nprint()\nprint(\"=\" * 120)\nprint(\"TABLE 7: Repo-level (completed results)\")\nprint(\"=\" * 120)\nprint(f\"{'Exp':<22} {'Acc':<8} {'F1_macro':<10} {'Pass_F1':<10} {'Fail_F1':<10} {'Unparse':<10} {'Majority':<10} {'Note'}\")\nprint(\"-\" * 110)\nfor name, d in repo.items():\n    acc = f\"{d['acc']:.2f}\" if d.get('acc') else \"—\"\n    f1m = f\"{d['f1m']:.2f}\" if d.get('f1m') else \"—\"\n    pf1 = f\"{d['pf1']:.2f}\" if d.get('pf1') else \"—\"\n    ff1 = f\"{d['ff1']:.2f}\" if d.get('ff1') else \"—\"\n    unp = str(d.get('unp','—'))\n    print(f\"{name:<22} {acc:<8} {f1m:<10} {pf1:<10} {ff1:<10} {unp:<10} {'72.96%':<10} {d['note']}\")\n\nprint()\nprint(\"=\" * 120)\nprint(\"TABLE 8: Analysis experiments\")\nprint(\"=\" * 120)\n\nprint(\"\\n--- 5-paired-clustered-bootstrap (CLS vs TRAJ equivalence) ---\")\nprint(\"  Pooled gap (CLS-TRAJ): -0.45pp, 95% CI [-1.71, +0.84]\")\nprint(\"  Paired t-test p-value: 0.499 (not significant)\")\nprint(\"  TOST equivalence p-value: 0.0071 (equivalent within ±2pp margin)\")\nprint(\"  Per-seed gaps: seed42=-0.97, seed123=+1.45, seed456=-1.84, seed789=-0.78, seed0=-0.29\")\n\nprint(\"\\n--- per-test-majority-voting (K=3, temp=0.7) ---\")\nprint(\"  Greedy accuracy: 87.51%  →  Majority vote: 86.83%  (Δ = -0.69pp)\")\nprint(\"  Unanimous rate: 93.3%, split samples: 127, net flips: -13\")\n\nprint(\"\\n--- block-corr-empirical (error correlation within problems) ---\")\nprint(\"  ICC = 0.191 (p < 1e-10), design effect = 3.97\")\nprint(\"  All-correct ratio: 2.81× expected under i.i.d.\")\nprint(\"  Error std ratio: 1.89× expected under i.i.d.\")\n\nprint(\"\\n--- oracle-f2p-stratified (per-test advantage by F2P count) ---\")\nprint(\"  T=1 (68.7%): block adv = -0.09pp (no advantage)\")\nprint(\"  T=2 (19.1%): block adv = 31.69pp\")\nprint(\"  T=3-5 (7.1%): block adv = 40.74pp\")\nprint(\"  T≥6 (5.1%): block adv = 40.06pp\")\nprint(\"  T=2 contributes 55.3% of overall advantage\")\n\nprint(\"\\n--- mvp-a-oracle-sim (total F2P+P2P simulation) ---\")\nprint(\"  10% regression threshold: iid_adv=13.2pp, block_adv=8.3pp (PASS)\")\nprint(\"  5% regression threshold: iid_adv=-1.0pp, block_adv=-0.5pp (FAIL)\")\nprint(\"  F2P real (T=1 median): iid_adv=1.98pp, block_adv=10.88pp\")\n\nprint(\"\\n--- p2p-regression-rate ---\")\nprint(\"  Conclusion: NEGATIVE\")\nprint(\"  P2P regression rate: 1.04% mean / 0% median (on CoderForge SWE-bench Verified)\")\n\nprint(\"\\n--- per-test-precision-recall (diagnostic analysis) ---\")\nprint(\"  114 problems: 48 (42.1%) perfectly predicted\")\nprint(\"  Median problem fail-F1: 94.12%\")\nprint(\"  Best mutation type: return_value (97.26%), Worst: off_by_one (82.56%)\")\n\nprint(\"\\n--- mvp-b-data-prep (HumanEval/MBPP dataset) ---\")\nprint(\"  Total: 19,076 samples (HumanEval 5,575 + MBPP 13,501)\")\nprint(\"  Class balance: pass 52.0% / fail 48.0%\")\n\nprint(\"\\n--- mvp-b-train (initial pilot) ---\")\nprint(\"  Accuracy: 87.5%, pass_f1: 87.1%, fail_f1: 87.9%\")\nprint(\"  Majority baseline: 52.0%, gap: +35.5pp\")\n\nprint()\nprint(\"=\" * 120)\nprint(\"CORE COMPARISON NUMBERS (for paper)\")\nprint(\"=\" * 120)\n\n# 1. 4B CLS vs CWM gap (5-seed)\nprint(f\"\\n1. 4B CLS vs CWM (5-seed paired):\")\nprint(f\"   Accuracy gap: {fmt(gap_acc.mean(), gap_acc.std(ddof=1))}pp\")\nprint(f\"   Pass_F1 gap:  {fmt(gap_pf1.mean(), gap_pf1.std(ddof=1))}pp\")\nprint(f\"   Fail_F1 gap:  {fmt(gap_ff1.mean(), gap_ff1.std(ddof=1))}pp\")\nprint(f\"   Paired t-test: t={t_acc:.3f}, p={p_acc:.4f}\")\n\n# 2. 8B CLS vs CWM gap (3-seed)\ngap8_acc = cls8_accs - cwm8_accs\ngap8_pf1 = cls8_pf1 - cwm8_pf1\ngap8_ff1 = cls8_ff1 - cwm8_ff1\nt8, p8 = stats.ttest_rel(cls8_accs, cwm8_accs)\nprint(f\"\\n2. 8B CLS vs CWM (3-seed paired):\")\nprint(f\"   Accuracy gap: {fmt(gap8_acc.mean(), gap8_acc.std(ddof=1))}pp\")\nprint(f\"   Pass_F1 gap:  {fmt(gap8_pf1.mean(), gap8_pf1.std(ddof=1))}pp\")\nprint(f\"   Fail_F1 gap:  {fmt(gap8_ff1.mean(), gap8_ff1.std(ddof=1))}pp\")\nprint(f\"   Paired t-test: t={t8:.3f}, p={p8:.4f}\")\n\n# 3. Scaling effect\nprint(f\"\\n3. Scaling 4B → 8B (matched 3 seeds: 42, 123, 456):\")\nprint(f\"   CLS accuracy gain: {cls8_accs.mean() - cls4_3.mean():+.2f}pp ({fmt(cls4_3.mean(), cls4_3.std(ddof=1))} → {fmt(cls8_accs.mean(), cls8_accs.std(ddof=1))})\")\nprint(f\"   CWM accuracy gain: {cwm8_accs.mean() - cwm4_3.mean():+.2f}pp ({fmt(cwm4_3.mean(), cwm4_3.std(ddof=1))} → {fmt(cwm8_accs.mean(), cwm8_accs.std(ddof=1))})\")\nprint(f\"   4B CLS-CWM gap: {fmt(gap_4b_3.mean(), gap_4b_3.std(ddof=1))}pp\")\nprint(f\"   8B CLS-CWM gap: {fmt(gap8_acc.mean(), gap8_acc.std(ddof=1))}pp\")\nprint(f\"   Gap widening: {gap8_acc.mean() - gap_4b_3.mean():+.2f}pp at 8B → CWM bottleneck amplified\")\n\n# 4. Fine-tuned 4B vs zero-shot 32B\nprint(f\"\\n4. Fine-tuned 4B vs Zero-shot 32B:\")\nft4b_mean = cls_accs.mean()\nprint(f\"   FT 4B CLS (5-seed): {ft4b_mean:.2f}%\")\nprint(f\"   Zero-shot 32B:      {71.69}%\")\nprint(f\"   Gap: {ft4b_mean - 71.69:+.2f}pp in favor of FT 4B\")\nprint(f\"   → Fine-tuned 4B dominates 8× larger zero-shot model\")\n\n# 5. Repo-level CLS vs CWM\nprint(f\"\\n5. Repo-level CLS vs CWM (seed=42, CLS v5 only valid):\")\nprint(f\"   CLS v5: accuracy=76.92%, F1_macro=73.90% (majority baseline=72.96%)\")\nprint(f\"   CWM v10: accuracy=69.91% (93% unparseable → eval invalid)\")\nprint(f\"   CWM v11: accuracy=66.6% (killed, subset-500, 75% unparseable)\")\nprint(f\"   ⚠️ CWM repo-level results unreliable; only CLS v5 is valid reference\")\n\n# 6. TOST equivalence\nprint(f\"\\n6. TOST equivalence (CLS aggregated ≈ TRAJ at variant level):\")\nprint(f\"   Variant-level CLS vs TRAJ gap: -0.45pp, 95% CI [-1.71, +0.84]\")\nprint(f\"   TOST p-value: 0.0071 (< 0.05 → statistically equivalent within ±2pp)\")\nprint(f\"   → Per-test CLS aggregated to variant-level is equivalent to dedicated TRAJ model\")\n\n# 7. Summary table of means\nprint()\nprint(\"=\" * 120)\nprint(\"SUMMARY OF MEANS\")\nprint(\"=\" * 120)\nprint(f\"{'Configuration':<35} {'Accuracy':<12} {'Pass_F1':<12} {'Fail_F1':<12}\")\nprint(\"-\" * 71)\nprint(f\"{'4B CLS (5-seed)':<35} {fmt(cls_accs.mean(), cls_accs.std(ddof=1)):<12} {fmt(cls_pf1.mean(), cls_pf1.std(ddof=1)):<12} {fmt(cls_ff1.mean(), cls_ff1.std(ddof=1)):<12}\")\nprint(f\"{'4B CWM (5-seed)':<35} {fmt(cwm_accs.mean(), cwm_accs.std(ddof=1)):<12} {fmt(cwm_pf1.mean(), cwm_pf1.std(ddof=1)):<12} {fmt(cwm_ff1.mean(), cwm_ff1.std(ddof=1)):<12}\")\nprint(f\"{'8B CLS (3-seed)':<35} {fmt(cls8_accs.mean(), cls8_accs.std(ddof=1)):<12} {fmt(cls8_pf1.mean(), cls8_pf1.std(ddof=1)):<12} {fmt(cls8_ff1.mean(), cls8_ff1.std(ddof=1)):<12}\")\nprint(f\"{'8B CWM (3-seed)':<35} {fmt(cwm8_accs.mean(), cwm8_accs.std(ddof=1)):<12} {fmt(cwm8_pf1.mean(), cwm8_pf1.std(ddof=1)):<12} {fmt(cwm8_ff1.mean(), cwm8_ff1.std(ddof=1)):<12}\")\nprint(f\"{'Traj-level (5-seed)':<35} {fmt(np.mean(taccs), np.std(taccs, ddof=1)):<12} {'—':<12} {'—':<12}\")\nprint(f\"{'Zero-shot 8B':<35} {'64.40':<12} {'50.50':<12} {'72.20':<12}\")\nprint(f\"{'Zero-shot 32B':<35} {'71.69':<12} {'65.68':<12} {'75.91':<12}\")\nprint(f\"{'Repo-level CLS v5 (1-seed)':<35} {'76.92':<12} {'82.78':<12} {'65.01':<12}\")\n\nPYEOF\n",
    "description": "Compute all summary tables and statistics"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-14T00:42:59.685110+00:00_

========================================================================================================================
TABLE 1: Function-level CLS (per-test classification, 4B, 5 seeds)
========================================================================================================================
Seed     Accuracy   Pass_F1    Fail_F1    Pass_P     Pass_R     Fail_P     Fail_R    
------------------------------------------------------------------------------
0        87.94      87.79      88.08      92.13      83.84      84.20      92.32     
42       87.83      88.06      87.59      89.45      86.71      86.20      89.04     
123      89.52      89.64      89.40      91.76      87.63      87.34      91.56     
456      87.88      87.53      88.21      93.60      82.21      83.12      93.97     
789      89.00      88.90      89.10      93.30      84.90      85.20      93.40     
------------------------------------------------------------------------------
Mean±Std 88.43 ± 0.78 88.38 ± 0.87 88.48 ± 0.75 92.05 ± 1.64 85.06 ± 2.18 85.21 ± 1.65 92.06 ± 1.93

========================================================================================================================
TABLE 2: Function-level CWM (execution simulation, 4B, 5 seeds)
========================================================================================================================
Seed     Accuracy   Pass_F1    Fail_F1    Pass_P     Pass_R     Fail_P     Fail_R     ExactMatch  
------------------------------------------------------------------------------------------
0        87.57      87.18      87.93      93.45      81.70      82.71      93.86      84.29       
42       87.51      87.31      87.71      92.06      83.03      83.53      92.32      84.02       
123      87.20      86.95      87.44      —          —          —          —          84.44       
456      86.98      86.66      87.29      92.26      81.70      82.52      92.65      84.02       
789      86.67      86.7
…[truncated 10115 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_experiment-summary-table_20260514T003543",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-14T00:42:59.685312+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__register_artifact",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_experiment-summary-table_20260514T003543",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__register_artifact",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-14T00:42:59.685448+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_experiment-summary-table_20260514T003543",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-14T00:42:59.685572+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_experiment-summary-table_20260514T003543",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_project_file",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-14T00:42:59.685694+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_experiment-summary-table_20260514T003543",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-14T00:42:59.685832+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "exec-sim-repair-verifier",
  "file": "memory.md",
  "max_chars": "12000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_experiment-summary-table_20260514T003543",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "exec-sim-repair-verifier",
    "file": "memory.md",
    "max_chars": "12000"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-14T00:42:59.685996+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/memory.md\", \"content\": \"# 项目经验教训\\n\\n## 环境一致性（2026-05-13 确认）\\n\\n**home vs westd transformers 版本不同：home=4.57.6, westd=5.8.0**。导致相同代码+超参训练出 22pp accuracy 差距。Multi-seed 对比实验必须在同一环境运行，跨服务器对比无效。\\n\\n数据文件也不一致（md5 不同，行顺序/shuffle 不同）。在极端过拟合场景下，early steps 数据顺序对 best checkpoint 影响极大。\\n\\n**教训**：跨服务器 multi-seed 前必须验证：① transformers 版本 ② 数据文件 md5 ③ Python 版本。三者都一致才能做 apple-to-apple 对比。\\n\\n## Eval 脚本 generation_stats 单位\\n\\neval_repo_cwm.py L215 `len(r[\\\"gen_text\\\"])` 统计的是 **characters** 不是 tokens。max=7582 chars 对应 ≤1024 tokens（代码/traceback 每 token ~7.4 chars），无异常。\\n\\n## Repo-level 训练过拟合模式\\n\\n所有 repo-level 模型 best checkpoint 在 <10% 训练（step 200-600 / total 6633）。之后 eval_loss 单调上升。LR=5e-5 已比 2e-4 好很多（v5 best@600 vs v4 best@200），但仍然极度过拟合。未来可考虑：更激进的 early stopping / 更低 lr / 更多 regularization。\\n\\n## D008 Go/No-Go 判据\\n\\nCLS v5 (76.92%) vs CWM v11 (66.6%)，gap 10.3pp，CWM 低于 majority baseline 6.4pp。CWM 75.2% 输出不可解析。D008 = GO，repo-level 明确放大 complexity-dependent advantage。\\n\\n## Seed123 Launch Configs（已作废）\\n\\n原始 seed123 配置见 registry spec。注意：westd 上的 seed123 训练使用了错误环境（transformers 5.8.0），结果无效。需在 home 或统一环境后的 westd 上重跑。\\n\", \"total_chars\": 1060, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_experiment-summary-table_20260514T003543",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-14T00:42:59.686175+00:00_

called mcp__agent-ml-research__save_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__save_project_file</summary>

```json
{
  "project": "exec-sim-repair-verifier",
  "file": "memory.md",
  "content": "# 项目经验教训\n\n## 环境一致性（2026-05-13 确认）\n\n**home vs westd transformers 版本不同：home=4.57.6, westd=5.8.0**。导致相同代码+超参训练出 22pp accuracy 差距。Multi-seed 对比实验必须在同一环境运行，跨服务器对比无效。\n\n数据文件也不一致（md5 不同，行顺序/shuffle 不同）。在极端过拟合场景下，early steps 数据顺序对 best checkpoint 影响极大。\n\n**教训**：跨服务器 multi-seed 前必须验证：① transformers 版本 ② 数据文件 md5 ③ Python 版本。三者都一致才能做 apple-to-apple 对比。\n\n## Eval 脚本 generation_stats 单位\n\neval_repo_cwm.py L215 `len(r[\"gen_text\"])` 统计的是 **characters** 不是 tokens。max=7582 chars 对应 ≤1024 tokens（代码/traceback 每 token ~7.4 chars），无异常。\n\n## Repo-level 训练过拟合模式\n\n所有 repo-level 模型 best checkpoint 在 <10% 训练（step 200-600 / total 6633）。之后 eval_loss 单调上升。LR=5e-5 已比 2e-4 好很多（v5 best@600 vs v4 best@200），但仍然极度过拟合。未来可考虑：更激进的 early stopping / 更低 lr / 更多 regularization。\n\n## D008 Go/No-Go 判据\n\nCLS v5 (76.92%) vs CWM v11 (66.6%)，gap 10.3pp，CWM 低于 majority baseline 6.4pp。CWM 75.2% 输出不可解析。D008 = GO，repo-level 明确放大 complexity-dependent advantage。\n\n## Seed123 Launch Configs（已作废）\n\n原始 seed123 配置见 registry spec。注意：westd 上的 seed123 训练使用了错误环境（transformers 5.8.0），结果无效。需在 home 或统一环境后的 westd 上重跑。\n\n## 核心实验数字速查（2026-05-14 汇总）\n\n| 配置 | Accuracy | Pass_F1 | Fail_F1 |\n|------|----------|---------|---------|\n| 4B CLS (5-seed) | 88.43 ± 0.78 | 88.38 ± 0.87 | 88.48 ± 0.75 |\n| 4B CWM (5-seed) | 87.19 ± 0.37 | 86.97 ± 0.28 | 87.39 ± 0.51 |\n| 8B CLS (3-seed) | 89.39 ± 1.09 | 89.53 ± 1.33 | 89.22 ± 0.83 |\n| 8B CWM (3-seed) | 86.96 ± 0.72 | 86.79 ± 0.81 | 87.14 ± 0.63 |\n| Traj-level (5-seed) | 86.30 ± 0.97 | — | — |\n| Zero-shot 8B | 64.40 | 50.50 | 72.20 |\n| Zero-shot 32B | 71.69 | 65.68 | 75.91 |\n| Repo-level CLS v5 | 76.92 | 82.78 | 65.01 |\n\n**关键 gaps**: 4B CLS-CWM=+1.25±1.01pp (p=0.051), 8B CLS-CWM=+2.42±0.37pp (p=0.008), FT 4B vs 0-shot 32B=+16.74pp, TOST CLS≈TRAJ (p=0.007, ±2pp)\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_experiment-summary-table_20260514T003543",
  "tool": "mcp__agent-ml-research__save_project_file",
  "tool_args": {
    "project": "exec-sim-repair-verifier",
    "file": "memory.md",
    "content": "# 项目经验教训\n\n## 环境一致性（2026-05-13 确认）\n\n**home vs westd transformers 版本不同：home=4.57.6, westd=5.8.0**。导致相同代码+超参训练出 22pp accuracy 差距。Multi-seed 对比实验必须在同一环境运行，跨服务器对比无效。\n\n数据文件也不一致（md5 不同，行顺序/shuffle 不同）。在极端过拟合场景下，early steps 数据顺序对 best checkpoint 影响极大。\n\n**教训**：跨服务器 multi-seed 前必须验证：① transformers 版本 ② 数据文件 md5 ③ Python 版本。三者都一致才能做 apple-to-apple 对比。\n\n## Eval 脚本 generation_stats 单位\n\neval_repo_cwm.py L215 `len(r[\"gen_text\"])` 统计的是 **characters** 不是 tokens。max=7582 chars 对应 ≤1024 tokens（代码/traceback 每 token ~7.4 chars），无异常。\n\n## Repo-level 训练过拟合模式\n\n所有 repo-level 模型 best checkpoint 在 <10% 训练（step 200-600 / total 6633）。之后 eval_loss 单调上升。LR=5e-5 已比 2e-4 好很多（v5 best@600 vs v4 best@200），但仍然极度过拟合。未来可考虑：更激进的 early stopping / 更低 lr / 更多 regularization。\n\n## D008 Go/No-Go 判据\n\nCLS v5 (76.92%) vs CWM v11 (66.6%)，gap 10.3pp，CWM 低于 majority baseline 6.4pp。CWM 75.2% 输出不可解析。D008 = GO，repo-level 明确放大 complexity-dependent advantage。\n\n## Seed123 Launch Configs（已作废）\n\n原始 seed123 配置见 registry spec。注意：westd 上的 seed123 训练使用了错误环境（transformers 5.8.0），结果无效。需在 home 或统一环境后的 westd 上重跑。\n\n## 核心实验数字速查（2026-05-14 汇总）\n\n| 配置 | Accuracy | Pass_F1 | Fail_F1 |\n|------|----------|---------|---------|\n| 4B CLS (5-seed) | 88.43 ± 0.78 | 88.38 ± 0.87 | 88.48 ± 0.75 |\n| 4B CWM (5-seed) | 87.19 ± 0.37 | 86.97 ± 0.28 | 87.39 ± 0.51 |\n| 8B CLS (3-seed) | 89.39 ± 1.09 | 89.53 ± 1.33 | 89.22 ± 0.83 |\n| 8B CWM (3-seed) | 86.96 ± 0.72 | 86.79 ± 0.81 | 87.14 ± 0.63 |\n| Traj-level (5-seed) | 86.30 ± 0.97 | — | — |\n| Zero-shot 8B | 64.40 | 50.50 | 72.20 |\n| Zero-shot 32B | 71.69 | 65.68 | 75.91 |\n| Repo-level CLS v5 | 76.92 | 82.78 | 65.01 |\n\n**关键 gaps**: 4B CLS-CWM=+1.25±1.01pp (p=0.051), 8B CLS-CWM=+2.42±0.37pp (p=0.008), FT 4B vs 0-shot 32B=+16.74pp, TOST CLS≈TRAJ (p=0.007, ±2pp)\n"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-14T00:42:59.686335+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/memory.md\", \"saved\": true}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_experiment-summary-table_20260514T003543",
  "tool": "mcp__agent-ml-research__save_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-14T00:42:59.686491+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "success-experiments-summary",
  "type": "report",
  "description": "All success experiments metrics summary: 8 tables (CLS/CWM/Traj/8B-scaling/LLM-judge/repo-level/analysis) + core comparison numbers for paper",
  "project": "exec-sim-repair-verifier",
  "content_filename": "success_experiments_summary.md",
  "tags": "['metrics', 'summary', 'paper']",
  "content": "# Experiment Results Summary (2026-05-14)\n\n33 success experiments out of 59 total. All function-level experiments use CoderForge test set (1,890 test samples, 114 problems).\n\n---\n\n## Table 1: Function-level CLS (per-test classification, Qwen3-4B, 5 seeds)\n\n| Seed | Accuracy | Pass_F1 | Fail_F1 | Pass_P | Pass_R | Fail_P | Fail_R |\n|------|----------|---------|---------|--------|--------|--------|--------|\n| 0    | 87.94    | 87.79   | 88.08   | 92.13  | 83.84  | 84.20  | 92.32  |\n| 42   | 87.83    | 88.06   | 87.59   | 89.45  | 86.71  | 86.20  | 89.04  |\n| 123  | 89.52    | 89.64   | 89.40   | 91.76  | 87.63  | 87.34  | 91.56  |\n| 456  | 87.88    | 87.53   | 88.21   | 93.60  | 82.21  | 83.12  | 93.97  |\n| 789  | 89.00    | 88.90   | 89.10   | 93.30  | 84.90  | 85.20  | 93.40  |\n| **Mean±Std** | **88.43 ± 0.78** | **88.38 ± 0.87** | **88.48 ± 0.75** | **92.05 ± 1.64** | **85.06 ± 2.18** | **85.21 ± 1.65** | **92.06 ± 1.93** |\n\n---\n\n## Table 2: Function-level CWM (execution simulation, Qwen3-4B, 5 seeds)\n\n| Seed | Accuracy | Pass_F1 | Fail_F1 | Pass_P | Pass_R | Fail_P | Fail_R | ExactMatch |\n|------|----------|---------|---------|--------|--------|--------|--------|------------|\n| 0    | 87.57    | 87.18   | 87.93   | 93.45  | 81.70  | 82.71  | 93.86  | 84.29      |\n| 42   | 87.51    | 87.31   | 87.71   | 92.06  | 83.03  | 83.53  | 92.32  | 84.02      |\n| 123  | 87.20    | 86.95   | 87.44   | —      | —      | —      | —      | 84.44      |\n| 456  | 86.98    | 86.66   | 87.29   | 92.26  | 81.70  | 82.52  | 92.65  | 84.02      |\n| 789  | 86.67    | 86.74   | 86.60   | 89.37  | 84.25  | 84.09  | 89.25  | 83.97      |\n| **Mean±Std** | **87.19 ± 0.37** | **86.97 ± 0.28** | **87.39 ± 0.51** | **91.78 ± 1.72** | **82.67 ± 1.23** | **83.21 ± 0.73** | **92.02 ± 1.96** | **84.15 ± 0.21** |\n\n---\n\n## Table 3: Function-level CLS vs CWM (4B, 5-seed paired comparison)\n\n| Model | Formulation | Seeds | Accuracy (mean±std) | Pass_F1 | Fail_F1 |\n|-------|-------------|-------|---------------------|---------|---------|\n| 4B    | CLS         | 5     | 88.43 ± 0.78       | 88.38 ± 0.87 | 88.48 ± 0.75 |\n| 4B    | CWM         | 5     | 87.19 ± 0.37       | 86.97 ± 0.28 | 87.39 ± 0.51 |\n| **Gap (CLS−CWM)** | | 5 | **+1.25 ± 1.01**   | **+1.42 ± 0.94** | **+1.08 ± 1.13** |\n\n- Paired t-test: acc p=0.0506, pass_f1 p=0.0285, fail_f1 p=0.0993\n- Per-seed accuracy gaps: seed0=+0.37, seed42=+0.32, seed123=+2.32, seed456=+0.90, seed789=+2.33\n\n---\n\n## Table 4: 8B Scaling (3 matched seeds: 42, 123, 456)\n\n| Model | Size | Formulation | Seeds | Accuracy (mean±std) | Pass_F1 | Fail_F1 |\n|-------|------|-------------|-------|---------------------|---------|---------|\n| Qwen3 | 4B  | CLS         | 3     | 88.41 ± 0.96       | 88.41 ± 1.10 | — |\n| Qwen3 | 4B  | CWM         | 3     | 87.23 ± 0.27       | 86.97 ± 0.33 | — |\n| Qwen3 | 8B  | CLS         | 3     | 89.39 ± 1.09       | 89.53 ± 1.33 | 89.22 ± 0.83 |\n| Qwen3 | 8B  | CWM         | 3     | 86.96 ± 0.72       | 86.79 ± 0.81 | 87.14 ± 0.63 |\n\n| Per-seed 8B detail | Seed 42 | Seed 123 | Seed 456 |\n|---|---|---|---|\n| 8B CLS | 90.48 | 89.37 | 88.31 |\n| 8B CWM | 87.67 | 86.98 | 86.24 |\n| Gap | +2.81 | +2.39 | +2.07 |\n\n- CLS-CWM gap (4B, 3-seed): +1.18 ± 1.03pp\n- CLS-CWM gap (8B, 3-seed): +2.42 ± 0.37pp (paired t p=0.0077)\n- 4B→8B CLS gain: +0.98pp; CWM gain: −0.27pp\n- Gap widening: +1.24pp wider at 8B → CWM bottleneck amplified by scale\n\n---\n\n## Table 5: Trajectory-level (Qwen3-4B, 5 seeds)\n\n| Seed | Accuracy | Unresolved_F1 | Resolved_F1 | Unres_P | Unres_R | Res_P | Res_R | Consistency |\n|------|----------|---------------|-------------|---------|---------|-------|-------|-------------|\n| 0    | 85.66    | 87.37         | 83.41       | 82.71   | 92.59   | 90.07 | 77.66 | 79.55       |\n| 42   | 85.66    | 87.50         | 83.18       | —       | —       | —     | —     | 79.94       |\n| 123  | 85.47    | 87.00         | 83.52       | 83.53   | 90.78   | 88.17 | 79.33 | 78.59       |\n| 456  | 87.40    | 88.70         | 85.80       | 85.70   | 91.90   | 89.70 | 82.30 | 78.80       |\n| 789  | 87.31    | 88.27         | 86.17       | 87.41   | 89.15   | 87.18 | 85.18 | 76.74       |\n| **Mean±Std** | **86.30 ± 0.97** | **87.77 ± 0.70** | **84.42 ± 1.44** | — | — | — | — | **78.72 ± 1.24** |\n\n---\n\n## Table 6: Zero-shot LLM Judge\n\n| Model | Accuracy | Pass_F1 | Fail_F1 | Pass_P | Pass_R | Fail_P | Fail_R |\n|-------|----------|---------|---------|--------|--------|--------|--------|\n| Qwen3-8B zero-shot  | 64.40 | 50.50 | 72.20 | 90.00 | 35.10 | 57.90 | 95.80 |\n| Qwen3-32B zero-shot | 71.69 | 65.68 | 75.91 | 88.12 | 52.35 | 64.40 | 92.43 |\n| FT 4B CLS (ref)     | 88.43 | 88.38 | 88.48 | 92.05 | 85.06 | 85.21 | 92.06 |\n\n- Gap vs FT 4B: 8B zero-shot −24.03pp, 32B zero-shot −16.74pp\n- Fine-tuned 4B dominates 8× larger zero-shot model\n\n---\n\n## Table 7: Repo-level (SWE-bench, completed results)\n\n| Experiment | Acc | F1_macro | Pass_F1 | Fail_F1 | Unparseable | Majority BL | Status |\n|------------|-----|----------|---------|---------|-------------|-------------|--------|\n| CLS v4 (old hp) | 66.11 | 56.61 | 76.90 | 36.30 | 132 | 72.96% | success (early stop) |\n| CLS v5 (fixed hp) | **76.92** | **73.90** | **82.78** | **65.01** | 132 | 72.96% | **success** |\n| CWM v10 | 69.91 | 46.71 | 81.87 | 11.54 | 9,102 (93%) | 72.96% | success (eval invalid) |\n| CWM v11 | 66.60 | 52.99 | 78.30 | 27.70 | 376 (75%) | 72.96% | killed (subset-500) |\n| CLS 8B | 71.37 | 69.05 | 77.53 | 60.57 | 136 | 72.96% | killed (env mismatch) |\n\n- Only CLS v5 is a valid repo-level result\n- CWM repo-level: generation too long / unparseable, eval unreliable\n- CLS 8B: trained with mismatched transformers version (5.8.0 vs 4.57.6)\n\n---\n\n## Table 8: Analysis Experiments\n\n### 5-paired-clustered-bootstrap (CLS vs TRAJ equivalence)\n- Pooled variant-level gap (CLS−TRAJ): −0.45pp, 95% CI [−1.71, +0.84]\n- Paired t-test: p=0.499 (not significant)\n- TOST equivalence: p=0.0071 (equivalent within ±2pp margin)\n- Per-seed gaps: seed42=−0.97, seed123=+1.45, seed456=−1.84, seed789=−0.78, seed0=−0.29\n\n### per-test-majority-voting (K=3, temp=0.7)\n- Greedy: 87.51% → Majority vote: 86.83% (Δ=−0.69pp)\n- Unanimous: 93.3%, split samples: 127, net flips: −13\n- Conclusion: NEGATIVE — majority voting hurts\n\n### block-corr-empirical (error correlation within problems)\n- ICC=0.191 (p<1e-10), design effect=3.97\n- All-correct ratio: 2.81× vs i.i.d. expectation\n- Error std ratio: 1.89× vs i.i.d.\n\n### oracle-f2p-stratified (per-test advantage by F2P count)\n- T=1 (68.7%): block_adv=−0.09pp (no advantage)\n- T=2 (19.1%): block_adv=+31.69pp\n- T=3–5 (7.1%): block_adv=+40.74pp\n- T≥6 (5.1%): block_adv=+40.06pp\n- T=2 contributes 55.3% of overall advantage\n\n### mvp-a-oracle-sim (total F2P+P2P simulation)\n- 10% regression: iid_adv=13.2pp, block_adv=8.3pp (PASS)\n- 5% regression: iid_adv=−1.0pp, block_adv=−0.5pp (FAIL)\n\n### per-test-precision-recall (diagnostic)\n- 48/114 problems (42.1%) perfectly predicted\n- Median problem fail-F1: 94.12%\n- Best mutation: return_value (97.26%), Worst: off_by_one (82.56%)\n\n---\n\n## Core Comparison Numbers (Paper)\n\n1. **4B CLS vs CWM (5-seed)**: gap=+1.25±1.01pp, paired t p=0.051\n2. **8B CLS vs CWM (3-seed)**: gap=+2.42±0.37pp, paired t p=0.008\n3. **Scaling 4B→8B**: CLS +0.98pp, CWM −0.27pp; gap widens +1.24pp\n4. **FT 4B vs zero-shot 32B**: +16.74pp advantage for fine-tuned 4B\n5. **Repo-level**: CLS v5=76.92% (only valid), CWM eval invalid\n6. **TOST CLS≈TRAJ**: equivalent within ±2pp (p=0.007)\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_experiment-summary-table_20260514T003543",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "success-experiments-summary",
    "type": "report",
    "description": "All success experiments metrics summary: 8 tables (CLS/CWM/Traj/8B-scaling/LLM-judge/repo-level/analysis) + core comparison numbers for paper",
    "project": "exec-sim-repair-verifier",
    "content_filename": "success_experiments_summary.md",
    "tags": "['metrics', 'summary', 'paper']",
    "content": "# Experiment Results Summary (2026-05-14)\n\n33 success experiments out of 59 total. All function-level experiments use CoderForge test set (1,890 test samples, 114 problems).\n\n---\n\n## Table 1: Function-level CLS (per-test classification, Qwen3-4B, 5 seeds)\n\n| Seed | Accuracy | Pass_F1 | Fail_F1 | Pass_P | Pass_R | Fail_P | Fail_R |\n|------|----------|---------|---------|--------|--------|--------|--------|\n| 0    | 87.94    | 87.79   | 88.08   | 92.13  | 83.84  | 84.20  | 92.32  |\n| 42   | 87.83    | 88.06   | 87.59   | 89.45  | 86.71  | 86.20  | 89.04  |\n| 123  | 89.52    | 89.64   | 89.40   | 91.76  | 87.63  | 87.34  | 91.56  |\n| 456  | 87.88    | 87.53   | 88.21   | 93.60  | 82.21  | 83.12  | 93.97  |\n| 789  | 89.00    | 88.90   | 89.10   | 93.30  | 84.90  | 85.20  | 93.40  |\n| **Mean±Std** | **88.43 ± 0.78** | **88.38 ± 0.87** | **88.48 ± 0.75** | **92.05 ± 1.64** | **85.06 ± 2.18** | **85.21 ± 1.65** | **92.06 ± 1.93** |\n\n---\n\n## Table 2: Function-level CWM (execution simulation, Qwen3-4B, 5 seeds)\n\n| Seed | Accuracy | Pass_F1 | Fail_F1 | Pass_P | Pass_R | Fail_P | Fail_R | ExactMatch |\n|------|----------|---------|---------|--------|--------|--------|--------|------------|\n| 0    | 87.57    | 87.18   | 87.93   | 93.45  | 81.70  | 82.71  | 93.86  | 84.29      |\n| 42   | 87.51    | 87.31   | 87.71   | 92.06  | 83.03  | 83.53  | 92.32  | 84.02      |\n| 123  | 87.20    | 86.95   | 87.44   | —      | —      | —      | —      | 84.44      |\n| 456  | 86.98    | 86.66   | 87.29   | 92.26  | 81.70  | 82.52  | 92.65  | 84.02      |\n| 789  | 86.67    | 86.74   | 86.60   | 89.37  | 84.25  | 84.09  | 89.25  | 83.97      |\n| **Mean±Std** | **87.19 ± 0.37** | **86.97 ± 0.28** | **87.39 ± 0.51** | **91.78 ± 1.72** | **82.67 ± 1.23** | **83.21 ± 0.73** | **92.02 ± 1.96** | **84.15 ± 0.21** |\n\n---\n\n## Table 3: Function-level CLS vs CWM (4B, 5-seed paired comparison)\n\n| Model | Formulation | Seeds | Accuracy (mean±std) | Pass_F1 | Fail_F1 |\n|-------|-------------|-------|---------------------|---------|---------|\n| 4B    | CLS         | 5     | 88.43 ± 0.78       | 88.38 ± 0.87 | 88.48 ± 0.75 |\n| 4B    | CWM         | 5     | 87.19 ± 0.37       | 86.97 ± 0.28 | 87.39 ± 0.51 |\n| **Gap (CLS−CWM)** | | 5 | **+1.25 ± 1.01**   | **+1.42 ± 0.94** | **+1.08 ± 1.13** |\n\n- Paired t-test: acc p=0.0506, pass_f1 p=0.0285, fail_f1 p=0.0993\n- Per-seed accuracy gaps: seed0=+0.37, seed42=+0.32, seed123=+2.32, seed456=+0.90, seed789=+2.33\n\n---\n\n## Table 4: 8B Scaling (3 matched seeds: 42, 123, 456)\n\n| Model | Size | Formulation | Seeds | Accuracy (mean±std) | Pass_F1 | Fail_F1 |\n|-------|------|-------------|-------|---------------------|---------|---------|\n| Qwen3 | 4B  | CLS         | 3     | 88.41 ± 0.96       | 88.41 ± 1.10 | — |\n| Qwen3 | 4B  | CWM         | 3     | 87.23 ± 0.27       | 86.97 ± 0.33 | — |\n| Qwen3 | 8B  | CLS         | 3     | 89.39 ± 1.09       | 89.53 ± 1.33 | 89.22 ± 0.83 |\n| Qwen3 | 8B  | CWM         | 3     | 86.96 ± 0.72       | 86.79 ± 0.81 | 87.14 ± 0.63 |\n\n| Per-seed 8B detail | Seed 42 | Seed 123 | Seed 456 |\n|---|---|---|---|\n| 8B CLS | 90.48 | 89.37 | 88.31 |\n| 8B CWM | 87.67 | 86.98 | 86.24 |\n| Gap | +2.81 | +2.39 | +2.07 |\n\n- CLS-CWM gap (4B, 3-seed): +1.18 ± 1.03pp\n- CLS-CWM gap (8B, 3-seed): +2.42 ± 0.37pp (paired t p=0.0077)\n- 4B→8B CLS gain: +0.98pp; CWM gain: −0.27pp\n- Gap widening: +1.24pp wider at 8B → CWM bottleneck amplified by scale\n\n---\n\n## Table 5: Trajectory-level (Qwen3-4B, 5 seeds)\n\n| Seed | Accuracy | Unresolved_F1 | Resolved_F1 | Unres_P | Unres_R | Res_P | Res_R | Consistency |\n|------|----------|---------------|-------------|---------|---------|-------|-------|-------------|\n| 0    | 85.66    | 87.37         | 83.41       | 82.71   | 92.59   | 90.07 | 77.66 | 79.55       |\n| 42   | 85.66    | 87.50         | 83.18       | —       | —       | —     | —     | 79.94       |\n| 123  | 85.47    | 87.00         | 83.52       | 83.53   | 90.78   | 88.17 | 79.33 | 78.59       |\n| 456  | 87.40    | 88.70         | 85.80       | 85.70   | 91.90   | 89.70 | 82.30 | 78.80       |\n| 789  | 87.31    | 88.27         | 86.17       | 87.41   | 89.15   | 87.18 | 85.18 | 76.74       |\n| **Mean±Std** | **86.30 ± 0.97** | **87.77 ± 0.70** | **84.42 ± 1.44** | — | — | — | — | **78.72 ± 1.24** |\n\n---\n\n## Table 6: Zero-shot LLM Judge\n\n| Model | Accuracy | Pass_F1 | Fail_F1 | Pass_P | Pass_R | Fail_P | Fail_R |\n|-------|----------|---------|---------|--------|--------|--------|--------|\n| Qwen3-8B zero-shot  | 64.40 | 50.50 | 72.20 | 90.00 | 35.10 | 57.90 | 95.80 |\n| Qwen3-32B zero-shot | 71.69 | 65.68 | 75.91 | 88.12 | 52.35 | 64.40 | 92.43 |\n| FT 4B CLS (ref)     | 88.43 | 88.38 | 88.48 | 92.05 | 85.06 | 85.21 | 92.06 |\n\n- Gap vs FT 4B: 8B zero-shot −24.03pp, 32B zero-shot −16.74pp\n- Fine-tuned 4B dominates 8× larger zero-shot model\n\n---\n\n## Table 7: Repo-level (SWE-bench, completed results)\n\n| Experiment | Acc | F1_macro | Pass_F1 | Fail_F1 | Unparseable | Majority BL | Status |\n|------------|-----|----------|---------|---------|-------------|-------------|--------|\n| CLS v4 (old hp) | 66.11 | 56.61 | 76.90 | 36.30 | 132 | 72.96% | success (early stop) |\n| CLS v5 (fixed hp) | **76.92** | **73.90** | **82.78** | **65.01** | 132 | 72.96% | **success** |\n| CWM v10 | 69.91 | 46.71 | 81.87 | 11.54 | 9,102 (93%) | 72.96% | success (eval invalid) |\n| CWM v11 | 66.60 | 52.99 | 78.30 | 27.70 | 376 (75%) | 72.96% | killed (subset-500) |\n| CLS 8B | 71.37 | 69.05 | 77.53 | 60.57 | 136 | 72.96% | killed (env mismatch) |\n\n- Only CLS v5 is a valid repo-level result\n- CWM repo-level: generation too long / unparseable, eval unreliable\n- CLS 8B: trained with mismatched transformers version (5.8.0 vs 4.57.6)\n\n---\n\n## Table 8: Analysis Experiments\n\n### 5-paired-clustered-bootstrap (CLS vs TRAJ equivalence)\n- Pooled variant-level gap (CLS−TRAJ): −0.45pp, 95% CI [−1.71, +0.84]\n- Paired t-test: p=0.499 (not significant)\n- TOST equivalence: p=0.0071 (equivalent within ±2pp margin)\n- Per-seed gaps: seed42=−0.97, seed123=+1.45, seed456=−1.84, seed789=−0.78, seed0=−0.29\n\n### per-test-majority-voting (K=3, temp=0.7)\n- Greedy: 87.51% → Majority vote: 86.83% (Δ=−0.69pp)\n- Unanimous: 93.3%, split samples: 127, net flips: −13\n- Conclusion: NEGATIVE — majority voting hurts\n\n### block-corr-empirical (error correlation within problems)\n- ICC=0.191 (p<1e-10), design effect=3.97\n- All-correct ratio: 2.81× vs i.i.d. expectation\n- Error std ratio: 1.89× vs i.i.d.\n\n### oracle-f2p-stratified (per-test advantage by F2P count)\n- T=1 (68.7%): block_adv=−0.09pp (no advantage)\n- T=2 (19.1%): block_adv=+31.69pp\n- T=3–5 (7.1%): block_adv=+40.74pp\n- T≥6 (5.1%): block_adv=+40.06pp\n- T=2 contributes 55.3% of overall advantage\n\n### mvp-a-oracle-sim (total F2P+P2P simulation)\n- 10% regression: iid_adv=13.2pp, block_adv=8.3pp (PASS)\n- 5% regression: iid_adv=−1.0pp, block_adv=−0.5pp (FAIL)\n\n### per-test-precision-recall (diagnostic)\n- 48/114 problems (42.1%) perfectly predicted\n- Median problem fail-F1: 94.12%\n- Best mutation: return_value (97.26%), Worst: off_by_one (82.56%)\n\n---\n\n## Core Comparison Numbers (Paper)\n\n1. **4B CLS vs CWM (5-seed)**: gap=+1.25±1.01pp, paired t p=0.051\n2. **8B CLS vs CWM (3-seed)**: gap=+2.42±0.37pp, paired t p=0.008\n3. **Scaling 4B→8B**: CLS +0.98pp, CWM −0.27pp; gap widens +1.24pp\n4. **FT 4B vs zero-shot 32B**: +16.74pp advantage for fine-tuned 4B\n5. **Repo-level**: CLS v5=76.92% (only valid), CWM eval invalid\n6. **TOST CLS≈TRAJ**: equivalent within ±2pp (p=0.007)\n"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-14T00:42:59.686729+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260514_515c1c\", \"name\": \"success-experiments-summary\", \"type\": \"report\", \"description\": \"All success experiments metrics summary: 8 tables (CLS/CWM/Traj/8B-scaling/LLM-judge/repo-level/analysis) + core comparison numbers for paper\", \"path\": \"projects/exec-sim-repair-verifier/artifacts/_project/report/success_experiments_summary.md\", \"url\": null, \"project\": \"exec-sim-repair-verifier\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-14T00:42:51.161017+00:00\", \"tags\": [\"metrics\", \"summary\", \"paper\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_experiment-summary-table_20260514T003543",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 57 · 2026-05-14T00:42:59.686933+00:00_

完成。汇总报告已注册为 artifact `art_20260514_515c1c`，核心数字已追加到 memory.md。

**关键结果**:

| 配置 | Accuracy | CLS−CWM Gap |
|------|----------|-------------|
| 4B (5-seed) | CLS 88.43±0.78 / CWM 87.19±0.37 | +1.25±1.01pp (p=0.051) |
| 8B (3-seed) | CLS 89.39±1.09 / CWM 86.96±0.72 | +2.42±0.37pp (p=0.008) |
| Traj (5-seed) | 86.30±0.97 | TOST≈CLS (p=0.007) |
| Zero-shot 32B | 71.69 | vs FT 4B: −16.74pp |
| Repo CLS v5 | 76.92 | CWM eval invalid |

Scaling 放大 gap +1.24pp (CLS 吃到 scaling, CWM 不吃)。Repo-level 只有 CLS v5 有效，CWM 因 unparseable 过高不可用。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_experiment-summary-table_20260514T003543"
}
```

</details>

---
