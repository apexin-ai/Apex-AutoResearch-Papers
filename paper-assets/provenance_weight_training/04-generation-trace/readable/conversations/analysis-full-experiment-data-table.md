# analysis full experiment data table

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 67
- **Recorded user turns:** 0
- **Tool calls:** 33
- **Original source:** `logs/chats/worker_analysis_full_experiment_data_table_20260515T110438.jsonl`
- **Structured JSON:** [`3c5300294492d478ace6.json`](../../sessions/3c/3c5300294492d478ace6.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

67 recorded events

### Tool call

_source line 1 · 2026-05-15T11:11:52.755751+00:00_

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
  "session": "worker_analysis_full_experiment_data_table_20260515T110438",
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

_source line 2 · 2026-05-15T11:11:52.756100+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_full_experiment_data_table_20260515T110438",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T11:11:52.756280+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "provenance_weight_training",
  "limit": "0",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_full_experiment_data_table_20260515T110438",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "provenance_weight_training",
    "limit": "0",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-15T11:11:52.756656+00:00_

Error: result (65,401 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/9b1b3290-57d1-413f-bf56-b2da5c5109ee/tool-results/mcp-agent-ml-research-read_registry-1778843095164.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/9b1b3290-57d1-413f-bf56-b2da5c5109ee/tool-results/mcp-agent-ml-research-read_registry-1778843095164.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/9b1b3290-57d1-413f-bf56-b2da5c5109ee/tool-results/mcp-agent-ml-research-read_registry-1778843095164.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_full_experiment_data_table_20260515T110438",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-15T11:11:52.756823+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "provenance_weight_training",
  "file": "artifacts/experiment_summary.md",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_full_experiment_data_table_20260515T110438",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "provenance_weight_training",
    "file": "artifacts/experiment_summary.md",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-15T11:11:52.757002+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'artifacts/experiment_summary.md'\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_full_experiment_data_table_20260515T110438",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-15T11:11:52.757206+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/experiment_summary.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_full_experiment_data_table_20260515T110438",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/experiment_summary.md"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-15T11:11:52.757369+00:00_

1	# Experiment Summary: Provenance Weight Training
2	
3	All data sourced from project registry (`provenance_weight_training`). Generated 2026-05-15.
4	
5	**Setup**: Qwen3-0.6B, 200M tokens, 371K samples (40% synthetic contamination), eval on held-out human data (4.08M tokens).
6	
7	---
8	
9	## Table 1: Grid-b Sweep — Full Record (eval_ppl_holdout)
10	
11	| b | seed42 | seed123 | seed456 | Mean | Std | Seeds |
12	|-----|--------|---------|---------|-------|-------|-------|
13	| 0.5 | 17.651 | 17.638 | 17.650 | 17.646 | 0.007 | 3 |
14	| 1.0 | 17.692 | 17.674 | 17.680 | 17.682 | 0.009 | 3 |
15	| 1.5 | 17.718 | 17.701 | 17.710 | 17.710 | 0.009 | 3 |
16	| 2.0 | 17.741 | 17.725 | 17.989† | 17.733 | 0.011 | 2* |
17	| 3.0 | 17.774 | 17.760 | 17.921† | 17.767 | 0.010 | 2* |
18	| 5.0 | 17.818 | 17.804 | 17.993† | 17.811 | 0.010 | 2* |
19	
20	†checkpoint resume artifact: seed456 b={2.0, 3.0, 5.0} training was interrupted and resumed from checkpoint, causing systematic PPL inflation of +0.15 to +0.25. These values are excluded from Mean/Std computation.
21	
22	\*Mean/Std computed from seed42 + seed123 only.
23	
24	- Best b = 0.5 across all seeds (monotonically increasing PPL with b)
25	
26	---
27	
28	## Table 1a: Grid-b Sweep — Paper View (eval_ppl_holdout)
29	
30	| b | Mean | Std | Seeds |
31	|-----|-------|-------|-------|
32	| 0.5 | 17.646 | 0.007 | 3 |
33	| 1.0 | 17.682 | 0.009 | 3 |
34	| 1.5 | 17.710 | 0.009 | 3 |
35	| 2.0 | 17.733 | 0.011 | 2 |
36	| 3.0 | 17.767 | 0.010 | 2 |
37	| 5.0 | 17.811 | 0.010 | 2 |
38	
39	For paper Table 1: b=0.5/1.0/1.5 report 3-seed mean+/-std; b=2.0/3.0/5.0 report 2-seed mean+/-std (seed42+seed123).
40	
41	---
42	
43	## Table 2: Method Comparison (eval_ppl_holdout)
44	
45	| Method | seed42 | seed123 | seed456 | Mean | Std |
46	|------------------|--------|---------|---------|-------|-------|
47	| Uniform | 17.690 | 17.690 | 17.700 | 17.693 | 0.006 |
48	| Grid-best (b=0.5)| 17.651 | 17.638 | 17.650 | 17.646 | 0.007 |
49	| Adaptive_fix | 17.650 
…[truncated 2788 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_full_experiment_data_table_20260515T110438",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-15T11:11:52.757534+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Extract registry experiment data",
  "prompt": "I need you to extract structured experiment data from a JSON registry file for the provenance_weight_training project.\n\nThe file is at: /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/9b1b3290-57d1-413f-bf56-b2da5c5109ee/tool-results/mcp-agent-ml-research-read_registry-1778843095164.txt\n\nIt's JSON with schema: {result: string} where `result` is a JSON-encoded string containing experiment records.\n\nSteps:\n1. First probe the structure with `jq 'type, length, keys' file`\n2. Then use python or jq to extract ALL experiment records\n\nFor each experiment, I need:\n- exp_id\n- status (DONE, FAILED, KILLED, INVALIDATED, etc.)\n- type/category (grid_b_sweep, uniform_baseline, adaptive, etc.)\n- seed\n- b value (if grid sweep) or tau value (if adaptive)\n- eval_ppl (the final evaluation perplexity metric)\n- Any conclusion or notes\n\nPlease return the data as a comprehensive, structured text summary organized by experiment type. Include ALL experiments, not just successful ones. Quote all numeric values exactly as they appear in the registry.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_full_experiment_data_table_20260515T110438",
  "tool": "Agent",
  "tool_args": {
    "description": "Extract registry experiment data",
    "prompt": "I need you to extract structured experiment data from a JSON registry file for the provenance_weight_training project.\n\nThe file is at: /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/9b1b3290-57d1-413f-bf56-b2da5c5109ee/tool-results/mcp-agent-ml-research-read_registry-1778843095164.txt\n\nIt's JSON with schema: {result: string} where `result` is a JSON-encoded string containing experiment records.\n\nSteps:\n1. First probe the structure with `jq 'type, length, keys' file`\n2. Then use python or jq to extract ALL experiment records\n\nFor each experiment, I need:\n- exp_id\n- status (DONE, FAILED, KILLED, INVALIDATED, etc.)\n- type/category (grid_b_sweep, uniform_baseline, adaptive, etc.)\n- seed\n- b value (if grid sweep) or tau value (if adaptive)\n- eval_ppl (the final evaluation perplexity metric)\n- Any conclusion or notes\n\nPlease return the data as a comprehensive, structured text summary organized by experiment type. Include ALL experiments, not just successful ones. Quote all numeric values exactly as they appear in the registry.",
    "subagent_type": "general-purpose"
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-15T11:11:52.757701+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/9b1b3290-57d1-413f-bf56-b2da5c5109ee/tool-results/mcp-agent-ml-research-read_registry-1778843095164.txt",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_full_experiment_data_table_20260515T110438",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/9b1b3290-57d1-413f-bf56-b2da5c5109ee/tool-results/mcp-agent-ml-research-read_registry-1778843095164.txt",
    "limit": "50"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-15T11:11:52.757829+00:00_

File content (27067 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_full_experiment_data_table_20260515T110438",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-15T11:11:52.757978+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/9b1b3290-57d1-413f-bf56-b2da5c5109ee/tool-results/mcp-agent-ml-research-read_registry-1778843095164.txt",
  "limit": "100",
  "offset": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_full_experiment_data_table_20260515T110438",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/9b1b3290-57d1-413f-bf56-b2da5c5109ee/tool-results/mcp-agent-ml-research-read_registry-1778843095164.txt",
    "limit": "100",
    "offset": "0"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-15T11:11:52.758096+00:00_

File content (27067 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_full_experiment_data_table_20260515T110438",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-15T11:11:52.758216+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "wc -l /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/9b1b3290-57d1-413f-bf56-b2da5c5109ee/tool-results/mcp-agent-ml-research-read_registry-1778843095164.txt",
  "description": "Count lines in the registry file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_full_experiment_data_table_20260515T110438",
  "tool": "Bash",
  "tool_args": {
    "command": "wc -l /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/9b1b3290-57d1-413f-bf56-b2da5c5109ee/tool-results/mcp-agent-ml-research-read_registry-1778843095164.txt",
    "description": "Count lines in the registry file"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-15T11:11:52.758327+00:00_

0 /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/9b1b3290-57d1-413f-bf56-b2da5c5109ee/tool-results/mcp-agent-ml-research-read_registry-1778843095164.txt

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_full_experiment_data_table_20260515T110438",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-15T11:11:52.758448+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/9b1b3290-57d1-413f-bf56-b2da5c5109ee/tool-results/mcp-agent-ml-research-read_registry-1778843095164.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nprint('Top-level type:', type(data).__name__)\nprint('Top-level keys:', list(data.keys()) if isinstance(data, dict) else 'N/A')\n# The result field is a JSON-encoded string\nresult = data.get('result', '')\nif isinstance(result, str):\n    inner = json.loads(result)\n    print('Inner type:', type(inner).__name__)\n    if isinstance(inner, dict):\n        print('Inner keys:', list(inner.keys()))\n    elif isinstance(inner, list):\n        print('Inner length:', len(inner))\n        if len(inner) > 0:\n            print('First item type:', type(inner[0]).__name__)\n            if isinstance(inner[0], dict):\n                print('First item keys:', list(inner[0].keys()))\n\"\n",
  "description": "Probe JSON structure of registry file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_full_experiment_data_table_20260515T110438",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/9b1b3290-57d1-413f-bf56-b2da5c5109ee/tool-results/mcp-agent-ml-research-read_registry-1778843095164.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nprint('Top-level type:', type(data).__name__)\nprint('Top-level keys:', list(data.keys()) if isinstance(data, dict) else 'N/A')\n# The result field is a JSON-encoded string\nresult = data.get('result', '')\nif isinstance(result, str):\n    inner = json.loads(result)\n    print('Inner type:', type(inner).__name__)\n    if isinstance(inner, dict):\n        print('Inner keys:', list(inner.keys()))\n    elif isinstance(inner, list):\n        print('Inner length:', len(inner))\n        if len(inner) > 0:\n            print('First item type:', type(inner[0]).__name__)\n            if isinstance(inner[0], dict):\n                print('First item keys:', list(inner[0].keys()))\n\"\n",
    "description": "Probe JSON structure of registry file"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-15T11:11:52.758564+00:00_

Top-level type: dict
Top-level keys: ['result']
Inner type: dict
Inner keys: ['success', 'data', 'error', 'metadata']

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_full_experiment_data_table_20260515T110438",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-15T11:11:52.758681+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/9b1b3290-57d1-413f-bf56-b2da5c5109ee/tool-results/mcp-agent-ml-research-read_registry-1778843095164.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\ninner = json.loads(data['result'])\nprint('success:', inner['success'])\nprint('error:', inner['error'])\nprint('metadata:', json.dumps(inner['metadata'], indent=2))\nprint()\nd = inner['data']\nprint('data type:', type(d).__name__)\nif isinstance(d, dict):\n    print('data keys:', list(d.keys())[:20])\n    print('total keys:', len(d.keys()))\nelif isinstance(d, list):\n    print('data length:', len(d))\n\"\n",
  "description": "Explore inner structure of registry data"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_full_experiment_data_table_20260515T110438",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/9b1b3290-57d1-413f-bf56-b2da5c5109ee/tool-results/mcp-agent-ml-research-read_registry-1778843095164.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\ninner = json.loads(data['result'])\nprint('success:', inner['success'])\nprint('error:', inner['error'])\nprint('metadata:', json.dumps(inner['metadata'], indent=2))\nprint()\nd = inner['data']\nprint('data type:', type(d).__name__)\nif isinstance(d, dict):\n    print('data keys:', list(d.keys())[:20])\n    print('total keys:', len(d.keys()))\nelif isinstance(d, list):\n    print('data length:', len(d))\n\"\n",
    "description": "Explore inner structure of registry data"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-15T11:11:52.758806+00:00_

success: True
error: None
metadata: {
  "elapsed_seconds": 0.1044
}

data type: dict
data keys: ['experiments', 'count', 'total', 'baseline']
total keys: 4

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_full_experiment_data_table_20260515T110438",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-15T11:11:52.758948+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/9b1b3290-57d1-413f-bf56-b2da5c5109ee/tool-results/mcp-agent-ml-research-read_registry-1778843095164.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\ninner = json.loads(data['result'])\nd = inner['data']\nprint('count:', d['count'])\nprint('total:', d['total'])\nprint('baseline:', json.dumps(d['baseline'], indent=2))\nprint()\nexps = d['experiments']\nprint('experiments type:', type(exps).__name__)\nif isinstance(exps, list):\n    print('experiments length:', len(exps))\n    if len(exps) > 0:\n        print('First experiment keys:', list(exps[0].keys()))\n        print()\n        print('First experiment:')\n        print(json.dumps(exps[0], indent=2))\nelif isinstance(exps, dict):\n    print('experiments keys:', list(exps.keys())[:10])\n    print('total experiments:', len(exps))\n\"\n",
  "description": "Explore experiments structure and baseline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_full_experiment_data_table_20260515T110438",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/9b1b3290-57d1-413f-bf56-b2da5c5109ee/tool-results/mcp-agent-ml-research-read_registry-1778843095164.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\ninner = json.loads(data['result'])\nd = inner['data']\nprint('count:', d['count'])\nprint('total:', d['total'])\nprint('baseline:', json.dumps(d['baseline'], indent=2))\nprint()\nexps = d['experiments']\nprint('experiments type:', type(exps).__name__)\nif isinstance(exps, list):\n    print('experiments length:', len(exps))\n    if len(exps) > 0:\n        print('First experiment keys:', list(exps[0].keys()))\n        print()\n        print('First experiment:')\n        print(json.dumps(exps[0], indent=2))\nelif isinstance(exps, dict):\n    print('experiments keys:', list(exps.keys())[:10])\n    print('total experiments:', len(exps))\n\"\n",
    "description": "Explore experiments structure and baseline"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-15T11:11:52.759069+00:00_

count: 39
total: 39
baseline: null

experiments type: dict
experiments keys: ['grid_b5_0_seed456', 'grid_b3_0_seed456', 'grid_b2_0_seed456', 'tau_095_seed42', 'tau_09_seed42', 'tau_07_seed42', 'tau_05_seed42', 'tau_0.6_seed42', 'tau_06_seed42', 'nmin1_seed42']
total experiments: 39

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_full_experiment_data_table_20260515T110438",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-15T11:11:52.759188+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/9b1b3290-57d1-413f-bf56-b2da5c5109ee/tool-results/mcp-agent-ml-research-read_registry-1778843095164.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\ninner = json.loads(data['result'])\nexps = inner['data']['experiments']\n\n# Print all experiment keys\nprint('All experiment IDs:')\nfor k in exps.keys():\n    print(f'  {k}')\nprint(f'\\nTotal: {len(exps)}')\n\" \n",
  "description": "List all experiment IDs"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_full_experiment_data_table_20260515T110438",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/9b1b3290-57d1-413f-bf56-b2da5c5109ee/tool-results/mcp-agent-ml-research-read_registry-1778843095164.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\ninner = json.loads(data['result'])\nexps = inner['data']['experiments']\n\n# Print all experiment keys\nprint('All experiment IDs:')\nfor k in exps.keys():\n    print(f'  {k}')\nprint(f'\\nTotal: {len(exps)}')\n\" \n",
    "description": "List all experiment IDs"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-15T11:11:52.759304+00:00_

All experiment IDs:
  grid_b5_0_seed456
  grid_b3_0_seed456
  grid_b2_0_seed456
  tau_095_seed42
  tau_09_seed42
  tau_07_seed42
  tau_05_seed42
  tau_0.6_seed42
  tau_06_seed42
  nmin1_seed42
  golden_ratio_seed42
  grid_b_low_seed42
  ess_only_seed42
  grid_b1_5_seed456
  grid_b1_0_seed456
  grid_b0_5_seed456
  adaptive_fix_seed456
  adaptive_fix_seed123
  adaptive_fix_seed42
  grid_b_seed42_batch
  grid_b5_0_seed123
  grid_b2_0_seed123
  grid_b3_0_seed123
  adaptive_v2_seed456
  adaptive_v2_seed123
  adaptive_v2_seed42
  grid_b1_5_seed123
  grid_b1_0_seed123
  grid_b0_5_seed123
  diagnostic_contamination100
  uniform_seed456
  uniform_seed123
  uniform_seed42
  adaptive_seed456
  adaptive_seed123
  adaptive_seed42
  detector_tfidf_lr
  detector_modernbert
  datagen_synthetic_4gpu

Total: 39

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_full_experiment_data_table_20260515T110438",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-15T11:11:52.759434+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/9b1b3290-57d1-413f-bf56-b2da5c5109ee/tool-results/mcp-agent-ml-research-read_registry-1778843095164.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\ninner = json.loads(data['result'])\nexps = inner['data']['experiments']\n\n# Print full details for each experiment\nfor k, v in exps.items():\n    print(f'=== {k} ===')\n    print(json.dumps(v, indent=2))\n    print()\n\" 2>&1 | head -600\n",
  "description": "Extract full details of all experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_full_experiment_data_table_20260515T110438",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/9b1b3290-57d1-413f-bf56-b2da5c5109ee/tool-results/mcp-agent-ml-research-read_registry-1778843095164.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\ninner = json.loads(data['result'])\nexps = inner['data']['experiments']\n\n# Print full details for each experiment\nfor k, v in exps.items():\n    print(f'=== {k} ===')\n    print(json.dumps(v, indent=2))\n    print()\n\" 2>&1 | head -600\n",
    "description": "Extract full details of all experiments"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-15T11:11:52.759564+00:00_

&lt;persisted-output>
Output too large (30.4KB). Full output saved to: /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/9b1b3290-57d1-413f-bf56-b2da5c5109ee/tool-results/bni9z62kv.txt

Preview (first 2KB):
=== grid_b5_0_seed456 ===
{
  "status": "DONE",
  "retry_count": 1,
  "created_at": "2026-05-14T06:59:39.050Z",
  "updated_at": "2026-05-15T10:05:51.443Z",
  "hypothesis": "Grid-b weighting with b=5.0, seed=456, for multi-seed validation of best-b baseline",
  "server": "westd-47453",
  "gpu": "cuda:2",
  "account": "root",
  "reproduce": {
    "server": "westd-47453",
    "gpu": "cuda:2",
    "started_at": "2026-05-15T00:52:41.923Z",
    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/grid_b5_0_seed456 --weighting_method grid --grid_b_value 5.0 --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 456 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4 --eval_data_path data/human/eval_holdout.jsonl --eval_steps 500\"",
    "finished_at": "2026-05-15T09:31:34.604Z",
    "training_hours": 8.65
  },
  "failure_reason": "",
  "notes": "\u26a0\ufe0f checkpoint resume artifact: PPL=17.993, \u6bd4 seed42(17.818)/seed123(17.804) \u9ad8 +0.18\u3002\u8bad\u7ec3\u4e2d\u65ad\u540e\u4ece checkpoint-3000 \u6062\u590d\uff0c\u5bfc\u81f4\u7cfb\u7edf\u6027 PPL \u504f\u9ad8\u3002\u8bba\u6587 Table 1 \u4e2d b=5.0 \u884c\u4ec5\u62a5 2 seeds (seed42+seed123)\u3002",
  "completed_at": "2026-05-15T07:46:15.281Z",
  "extra": {
    "hook_events": [
      {
        "event": "on_failed",
        "action": "agent",
        "ts": "2026-05-15T07:46:16.570901+00:00"
     
…[truncated 214 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_full_experiment_data_table_20260515T110438",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-15T11:11:52.759706+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/9b1b3290-57d1-413f-bf56-b2da5c5109ee/tool-results/bni9z62kv.txt",
  "limit": "300",
  "offset": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_full_experiment_data_table_20260515T110438",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/9b1b3290-57d1-413f-bf56-b2da5c5109ee/tool-results/bni9z62kv.txt",
    "limit": "300",
    "offset": "0"
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-15T11:11:52.759910+00:00_

0	=== grid_b5_0_seed456 ===
1	{
2	  "status": "DONE",
3	  "retry_count": 1,
4	  "created_at": "2026-05-14T06:59:39.050Z",
5	  "updated_at": "2026-05-15T10:05:51.443Z",
6	  "hypothesis": "Grid-b weighting with b=5.0, seed=456, for multi-seed validation of best-b baseline",
7	  "server": "westd-47453",
8	  "gpu": "cuda:2",
9	  "account": "root",
10	  "reproduce": {
11	    "server": "westd-47453",
12	    "gpu": "cuda:2",
13	    "started_at": "2026-05-15T00:52:41.923Z",
14	    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/grid_b5_0_seed456 --weighting_method grid --grid_b_value 5.0 --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 456 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4 --eval_data_path data/human/eval_holdout.jsonl --eval_steps 500\"",
15	    "finished_at": "2026-05-15T09:31:34.604Z",
16	    "training_hours": 8.65
17	  },
18	  "failure_reason": "",
19	  "notes": "\u26a0\ufe0f checkpoint resume artifact: PPL=17.993, \u6bd4 seed42(17.818)/seed123(17.804) \u9ad8 +0.18\u3002\u8bad\u7ec3\u4e2d\u65ad\u540e\u4ece checkpoint-3000 \u6062\u590d\uff0c\u5bfc\u81f4\u7cfb\u7edf\u6027 PPL \u504f\u9ad8\u3002\u8bba\u6587 Table 1 \u4e2d b=5.0 \u884c\u4ec5\u62a5 2 seeds (seed42+seed123)\u3002",
20	  "completed_at": "2026-05-15T07:46:15.281Z",
21	  "extra": {
22	    "hook_events": [
23	      {
24	        "event": "on_failed",
25	        "action": "agent",
26	        "ts": "2026-05-15T07:46:16.570901+00:00"
27	      },
28	      {
29	        "event": "on_complete",
30	        "action": "agent",
31	        "ts": "2026-05-15T09:31:35.946616+00:00"
32	      }
33	    ],
34	    "previous_failure": {
35	      "conclusion": 
…[truncated 14766 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_full_experiment_data_table_20260515T110438",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-15T11:11:52.760073+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/9b1b3290-57d1-413f-bf56-b2da5c5109ee/tool-results/bni9z62kv.txt",
  "limit": "300",
  "offset": "300"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_full_experiment_data_table_20260515T110438",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/9b1b3290-57d1-413f-bf56-b2da5c5109ee/tool-results/bni9z62kv.txt",
    "limit": "300",
    "offset": "300"
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-15T11:11:52.760266+00:00_

300	    "gpu": "cuda:2",
301	    "started_at": "2026-05-15T09:34:56.077Z",
302	    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/nmin1_seed42 --weighting_method adaptive --n_min 1 --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 42 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4 --tau 0.8 --bf16\""
303	  },
304	  "spec": {
305	    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/nmin1_seed42 --weighting_method adaptive --n_min 1 --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 42 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4 --tau 0.8 --bf16\"",
306	    "server": "westd-47453",
307	    "gpu": [
308	      "cuda:2"
309	    ],
310	    "pid": "194005",
311	    "log_path": "~/runs/provenance_weight_training/nmin1_seed42.log",
312	    "submitted_at": "2026-05-15T09:36:06.479Z",
313	    "submitted_via": "submit_training_job",
314	    "backend": "tmux",
315	    "account": "root"
316	  },
317	  "pid": "194005",
318	  "log_path": "~/runs/provenance_weight_training/nmin1_seed42.log"
319	}
320	
321	=== golden_ratio_seed42 ===
322	{
323	  "status": "RUNNING",
324	  "retry_count": 0,
325	  "created_at": "2026-05-15T07:20:12.943Z",
326	  "updated_at": "2026-05-15T09:36:04.772Z",
327	  "hypothesis": "Golden Ratio oracle baseline: w=1/\u03c6\u22480.618 for syn
…[truncated 14608 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_full_experiment_data_table_20260515T110438",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-15T11:11:52.760421+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/9b1b3290-57d1-413f-bf56-b2da5c5109ee/tool-results/bni9z62kv.txt",
  "limit": "300",
  "offset": "600"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_full_experiment_data_table_20260515T110438",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/9b1b3290-57d1-413f-bf56-b2da5c5109ee/tool-results/bni9z62kv.txt",
    "limit": "300",
    "offset": "600"
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-15T11:11:52.760542+00:00_

600	    "train_runtime_s": 12953.96,
601	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_full_experiment_data_table_20260515T110438",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-15T11:11:52.760688+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/9b1b3290-57d1-413f-bf56-b2da5c5109ee/tool-results/mcp-agent-ml-research-read_registry-1778843095164.txt | python3 << 'PYEOF'\nimport json, sys\n\ndata = json.load(sys.stdin)\ninner = json.loads(data['result'])\nexps = inner['data']['experiments']\n\n# Extract structured data for all experiments\nrecords = []\nfor exp_id, v in exps.items():\n    rec = {\n        'exp_id': exp_id,\n        'status': v.get('status', 'UNKNOWN'),\n        'conclusion': v.get('conclusion', ''),\n        'hypothesis': v.get('hypothesis', ''),\n        'notes': v.get('notes', ''),\n        'failure_reason': v.get('failure_reason', ''),\n    }\n    \n    # Extract seed\n    spec = v.get('spec', {})\n    rec['seed'] = spec.get('seed', '')\n    \n    # Extract metrics\n    metrics = v.get('metrics', {})\n    rec['eval_ppl'] = metrics.get('eval_ppl_holdout', metrics.get('eval_ppl', ''))\n    rec['eval_loss'] = metrics.get('eval_loss', '')\n    rec['train_loss'] = metrics.get('train_loss', '')\n    rec['total_steps'] = metrics.get('total_steps', '')\n    rec['gpu_hours'] = metrics.get('gpu_hours', '')\n    rec['eval_method'] = metrics.get('eval_method', '')\n    \n    # Extract b value or tau value from command\n    command = ''\n    if 'reproduce' in v and isinstance(v['reproduce'], dict):\n        command = v['reproduce'].get('command', '')\n    if not command and 'spec' in v and isinstance(v['spec'], dict):\n        command = v['spec'].get('command', '')\n    \n    rec['weighting_method'] = ''\n    rec['grid_b_value'] = ''\n    rec['tau'] = ''\n    rec['n_min'] = ''\n    \n    if command:\n        import re\n        m = re.search(r'--weighting_method\\s+(\\S+)', command)\n        if m: rec['weighting_method'] = m.group(1)\n        m = re.search(r'--grid_b_value\\s+(\\S+)', command)\n        if m: rec['grid_b_value'] = m.group(1)\n        m = re.search(r'--tau\\s+(\\S+)', command)\n        if m: rec['tau'] = m.group(1)\n        m = re.search(r'--n_min\\s+(\\S+)', command)\n        if m: rec['n_min'] = m.group(1)\n    \n    # Parent\n    rec['parent'] = v.get('parent', '')\n    \n    # Server/GPU\n    rec['server'] = v.get('server', '')\n    rec['gpu'] = v.get('gpu', '')\n    \n    # Retry count\n    rec['retry_count'] = v.get('retry_count', 0)\n    \n    # Checkpoint path\n    rec['checkpoint_path'] = v.get('checkpoint_path', '')\n    \n    # Training hours\n    reproduce = v.get('reproduce', {})\n    if isinstance(reproduce, dict):\n        rec['training_hours'] = reproduce.get('training_hours', '')\n    else:\n        rec['training_hours'] = ''\n    \n    records.append(rec)\n\n# Now categorize and print\ncategories = {}\nfor r in records:\n    # Determine category\n    eid = r['exp_id']\n    wm = r['weighting_method']\n    \n    if eid.startswith('grid_b') and wm == 'grid':\n        cat = 'grid_b_sweep'\n    elif eid.startswith('tau_'):\n        cat = 'tau_sensitivity_sweep'\n    elif eid.startswith('uniform_'):\n        cat = 'uniform_baseline'\n    elif eid.startswith('adaptive_v2_'):\n        cat = 'adaptive_v2'\n    elif eid.startswith('adaptive_fix_'):\n        cat = 'adaptive_fix'\n    elif eid.startswith('adaptive_seed'):\n        cat = 'adaptive_original'\n    elif eid.startswith('detector_'):\n        cat = 'detector'\n    elif eid.startswith('datagen_'):\n        cat = 'datagen'\n    elif eid.startswith('diagnostic_'):\n        cat = 'diagnostic'\n    elif eid.startswith('nmin'):\n        cat = 'n_min_sensitivity'\n    elif eid.startswith('golden_ratio'):\n        cat = 'golden_ratio_oracle'\n    elif eid.startswith('ess_only'):\n        cat = 'ess_only_baseline'\n    else:\n        cat = 'other'\n    \n    if cat not in categories:\n        categories[cat] = []\n    categories[cat].append(r)\n\n# Print structured output\nfor cat in ['grid_b_sweep', 'uniform_baseline', 'adaptive_original', 'adaptive_v2', 'adaptive_fix', \n            'tau_sensitivity_sweep', 'n_min_sensitivity', 'golden_ratio_oracle', 'ess_only_baseline',\n            'diagnostic', 'detector', 'datagen', 'other']:\n    if cat not in categories:\n        continue\n    recs = categories[cat]\n    print(f\"\\n{'='*80}\")\n    print(f\"  CATEGORY: {cat}  ({len(recs)} experiments)\")\n    print(f\"{'='*80}\")\n    \n    for r in recs:\n        print(f\"\\n  --- {r['exp_id']} ---\")\n        print(f\"  Status:           {r['status']}\")\n        print(f\"  Conclusion:       {r['conclusion']}\")\n        print(f\"  Seed:             {r['seed']}\")\n        print(f\"  Weighting method: {r['weighting_method']}\")\n        if r['grid_b_value']:\n            print(f\"  Grid b value:     {r['grid_b_value']}\")\n        if r['tau']:\n            print(f\"  Tau:              {r['tau']}\")\n        if r['n_min']:\n            print(f\"  n_min:            {r['n_min']}\")\n        if r['eval_ppl']:\n            print(f\"  Eval PPL:         {r['eval_ppl']}\")\n        if r['eval_loss']:\n            print(f\"  Eval loss:        {r['eval_loss']}\")\n        if r['train_loss']:\n            print(f\"  Train loss:       {r['train_loss']}\")\n        if r['total_steps']:\n            print(f\"  Total steps:      {r['total_steps']}\")\n        if r['gpu_hours']:\n            print(f\"  GPU hours:        {r['gpu_hours']}\")\n        if r['training_hours']:\n            print(f\"  Training hours:   {r['training_hours']}\")\n        if r['retry_count']:\n            print(f\"  Retry count:      {r['retry_count']}\")\n        if r['checkpoint_path']:\n            print(f\"  Checkpoint:       {r['checkpoint_path']}\")\n        if r['parent']:\n            print(f\"  Parent:           {r['parent']}\")\n        if r['hypothesis']:\n            print(f\"  Hypothesis:       {r['hypothesis']}\")\n        if r['notes']:\n            print(f\"  Notes:            {r['notes']}\")\n        if r['failure_reason']:\n            print(f\"  Failure reason:   {r['failure_reason']}\")\n        if r['eval_method']:\n            print(f\"  Eval method:      {r['eval_method']}\")\n\nprint(f\"\\n{'='*80}\")\nprint(f\"  SUMMARY STATISTICS\")\nprint(f\"{'='*80}\")\ndone_count = sum(1 for r in records if r['status'] == 'DONE')\nrunning_count = sum(1 for r in records if r['status'] == 'RUNNING')\npreparing_count = sum(1 for r in records if r['status'] == 'PREPARING')\nqueued_count = sum(1 for r in records if r['status'] == 'QUEUED')\nfailed_count = sum(1 for r in records if r['conclusion'] == 'failed')\nkilled_count = sum(1 for r in records if r['conclusion'] == 'killed')\ninvalidated_count = sum(1 for r in records if r['conclusion'] == 'invalidated')\nsuccess_count = sum(1 for r in records if r['conclusion'] == 'success')\n\nprint(f\"  Total experiments: {len(records)}\")\nprint(f\"  Status breakdown:\")\nprint(f\"    DONE:       {done_count}\")\nprint(f\"    RUNNING:    {running_count}\")\nprint(f\"    PREPARING:  {preparing_count}\")\nprint(f\"    QUEUED:     {queued_count}\")\nprint(f\"  Conclusion breakdown:\")\nprint(f\"    success:     {success_count}\")\nprint(f\"    failed:      {failed_count}\")\nprint(f\"    killed:      {killed_count}\")\nprint(f\"    invalidated: {invalidated_count}\")\n\n# PPL leaderboard\nppl_records = [(r['exp_id'], r['eval_ppl'], r['weighting_method'], r['grid_b_value'], r['seed']) \n               for r in records if r['eval_ppl'] and isinstance(r['eval_ppl'], (int, float))]\nppl_records.sort(key=lambda x: x[1])\nprint(f\"\\n  PPL Leaderboard (lower is better):\")\nfor eid, ppl, wm, bv, seed in ppl_records:\n    bstr = f\" b={bv}\" if bv else \"\"\n    print(f\"    {ppl:>8.3f}  {eid:<30s}  method={wm}{bstr}  seed={seed}\")\n\nPYEOF\n",
  "description": "Extract all experiment records structured by category",
  "timeout": "30000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_full_experiment_data_table_20260515T110438",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/9b1b3290-57d1-413f-bf56-b2da5c5109ee/tool-results/mcp-agent-ml-research-read_registry-1778843095164.txt | python3 << 'PYEOF'\nimport json, sys\n\ndata = json.load(sys.stdin)\ninner = json.loads(data['result'])\nexps = inner['data']['experiments']\n\n# Extract structured data for all experiments\nrecords = []\nfor exp_id, v in exps.items():\n    rec = {\n        'exp_id': exp_id,\n        'status': v.get('status', 'UNKNOWN'),\n        'conclusion': v.get('conclusion', ''),\n        'hypothesis': v.get('hypothesis', ''),\n        'notes': v.get('notes', ''),\n        'failure_reason': v.get('failure_reason', ''),\n    }\n    \n    # Extract seed\n    spec = v.get('spec', {})\n    rec['seed'] = spec.get('seed', '')\n    \n    # Extract metrics\n    metrics = v.get('metrics', {})\n    rec['eval_ppl'] = metrics.get('eval_ppl_holdout', metrics.get('eval_ppl', ''))\n    rec['eval_loss'] = metrics.get('eval_loss', '')\n    rec['train_loss'] = metrics.get('train_loss', '')\n    rec['total_steps'] = metrics.get('total_steps', '')\n    rec['gpu_hours'] = metrics.get('gpu_hours', '')\n    rec['eval_method'] = metrics.get('eval_method', '')\n    \n    # Extract b value or tau value from command\n    command = ''\n    if 'reproduce' in v and isinstance(v['reproduce'], dict):\n        command = v['reproduce'].get('command', '')\n    if not command and 'spec' in v and isinstance(v['spec'], dict):\n        command = v['spec'].get('command', '')\n    \n    rec['weighting_method'] = ''\n    rec['grid_b_value'] = ''\n    rec['tau'] = ''\n    rec['n_min'] = ''\n    \n    if command:\n        import re\n        m = re.search(r'--weighting_method\\s+(\\S+)', command)\n        if m: rec['weighting_method'] = m.group(1)\n        m = re.search(r'--grid_b_value\\s+(\\S+)', command)\n        if m: rec['grid_b_value'] = m.group(1)\n        m = re.search(r'--tau\\s+(\\S+)', command)\n        if m: rec['tau'] = m.group(1)\n        m = re.search(r'--n_min\\s+(\\S+)', command)\n        if m: rec['n_min'] = m.group(1)\n    \n    # Parent\n    rec['parent'] = v.get('parent', '')\n    \n    # Server/GPU\n    rec['server'] = v.get('server', '')\n    rec['gpu'] = v.get('gpu', '')\n    \n    # Retry count\n    rec['retry_count'] = v.get('retry_count', 0)\n    \n    # Checkpoint path\n    rec['checkpoint_path'] = v.get('checkpoint_path', '')\n    \n    # Training hours\n    reproduce = v.get('reproduce', {})\n    if isinstance(reproduce, dict):\n        rec['training_hours'] = reproduce.get('training_hours', '')\n    else:\n        rec['training_hours'] = ''\n    \n    records.append(rec)\n\n# Now categorize and print\ncategories = {}\nfor r in records:\n    # Determine category\n    eid = r['exp_id']\n    wm = r['weighting_method']\n    \n    if eid.startswith('grid_b') and wm == 'grid':\n        cat = 'grid_b_sweep'\n    elif eid.startswith('tau_'):\n        cat = 'tau_sensitivity_sweep'\n    elif eid.startswith('uniform_'):\n        cat = 'uniform_baseline'\n    elif eid.startswith('adaptive_v2_'):\n        cat = 'adaptive_v2'\n    elif eid.startswith('adaptive_fix_'):\n        cat = 'adaptive_fix'\n    elif eid.startswith('adaptive_seed'):\n        cat = 'adaptive_original'\n    elif eid.startswith('detector_'):\n        cat = 'detector'\n    elif eid.startswith('datagen_'):\n        cat = 'datagen'\n    elif eid.startswith('diagnostic_'):\n        cat = 'diagnostic'\n    elif eid.startswith('nmin'):\n        cat = 'n_min_sensitivity'\n    elif eid.startswith('golden_ratio'):\n        cat = 'golden_ratio_oracle'\n    elif eid.startswith('ess_only'):\n        cat = 'ess_only_baseline'\n    else:\n        cat = 'other'\n    \n    if cat not in categories:\n        categories[cat] = []\n    categories[cat].append(r)\n\n# Print structured output\nfor cat in ['grid_b_sweep', 'uniform_baseline', 'adaptive_original', 'adaptive_v2', 'adaptive_fix', \n            'tau_sensitivity_sweep', 'n_min_sensitivity', 'golden_ratio_oracle', 'ess_only_baseline',\n            'diagnostic', 'detector', 'datagen', 'other']:\n    if cat not in categories:\n        continue\n    recs = categories[cat]\n    print(f\"\\n{'='*80}\")\n    print(f\"  CATEGORY: {cat}  ({len(recs)} experiments)\")\n    print(f\"{'='*80}\")\n    \n    for r in recs:\n        print(f\"\\n  --- {r['exp_id']} ---\")\n        print(f\"  Status:           {r['status']}\")\n        print(f\"  Conclusion:       {r['conclusion']}\")\n        print(f\"  Seed:             {r['seed']}\")\n        print(f\"  Weighting method: {r['weighting_method']}\")\n        if r['grid_b_value']:\n            print(f\"  Grid b value:     {r['grid_b_value']}\")\n        if r['tau']:\n            print(f\"  Tau:              {r['tau']}\")\n        if r['n_min']:\n            print(f\"  n_min:            {r['n_min']}\")\n        if r['eval_ppl']:\n            print(f\"  Eval PPL:         {r['eval_ppl']}\")\n        if r['eval_loss']:\n            print(f\"  Eval loss:        {r['eval_loss']}\")\n        if r['train_loss']:\n            print(f\"  Train loss:       {r['train_loss']}\")\n        if r['total_steps']:\n            print(f\"  Total steps:      {r['total_steps']}\")\n        if r['gpu_hours']:\n            print(f\"  GPU hours:        {r['gpu_hours']}\")\n        if r['training_hours']:\n            print(f\"  Training hours:   {r['training_hours']}\")\n        if r['retry_count']:\n            print(f\"  Retry count:      {r['retry_count']}\")\n        if r['checkpoint_path']:\n            print(f\"  Checkpoint:       {r['checkpoint_path']}\")\n        if r['parent']:\n            print(f\"  Parent:           {r['parent']}\")\n        if r['hypothesis']:\n            print(f\"  Hypothesis:       {r['hypothesis']}\")\n        if r['notes']:\n            print(f\"  Notes:            {r['notes']}\")\n        if r['failure_reason']:\n            print(f\"  Failure reason:   {r['failure_reason']}\")\n        if r['eval_method']:\n            print(f\"  Eval method:      {r['eval_method']}\")\n\nprint(f\"\\n{'='*80}\")\nprint(f\"  SUMMARY STATISTICS\")\nprint(f\"{'='*80}\")\ndone_count = sum(1 for r in records if r['status'] == 'DONE')\nrunning_count = sum(1 for r in records if r['status'] == 'RUNNING')\npreparing_count = sum(1 for r in records if r['status'] == 'PREPARING')\nqueued_count = sum(1 for r in records if r['status'] == 'QUEUED')\nfailed_count = sum(1 for r in records if r['conclusion'] == 'failed')\nkilled_count = sum(1 for r in records if r['conclusion'] == 'killed')\ninvalidated_count = sum(1 for r in records if r['conclusion'] == 'invalidated')\nsuccess_count = sum(1 for r in records if r['conclusion'] == 'success')\n\nprint(f\"  Total experiments: {len(records)}\")\nprint(f\"  Status breakdown:\")\nprint(f\"    DONE:       {done_count}\")\nprint(f\"    RUNNING:    {running_count}\")\nprint(f\"    PREPARING:  {preparing_count}\")\nprint(f\"    QUEUED:     {queued_count}\")\nprint(f\"  Conclusion breakdown:\")\nprint(f\"    success:     {success_count}\")\nprint(f\"    failed:      {failed_count}\")\nprint(f\"    killed:      {killed_count}\")\nprint(f\"    invalidated: {invalidated_count}\")\n\n# PPL leaderboard\nppl_records = [(r['exp_id'], r['eval_ppl'], r['weighting_method'], r['grid_b_value'], r['seed']) \n               for r in records if r['eval_ppl'] and isinstance(r['eval_ppl'], (int, float))]\nppl_records.sort(key=lambda x: x[1])\nprint(f\"\\n  PPL Leaderboard (lower is better):\")\nfor eid, ppl, wm, bv, seed in ppl_records:\n    bstr = f\" b={bv}\" if bv else \"\"\n    print(f\"    {ppl:>8.3f}  {eid:<30s}  method={wm}{bstr}  seed={seed}\")\n\nPYEOF\n",
    "description": "Extract all experiment records structured by category",
    "timeout": "30000"
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-15T11:11:52.760890+00:00_

Exit code 1
Traceback (most recent call last):
  File "&lt;stdin>", line 3, in &lt;module>
  File "/usr/lib/python3.14/json/__init__.py", line 298, in load
    return loads(fp.read(),
        cls=cls, object_hook=object_hook,
        parse_float=parse_float, parse_int=parse_int,
        parse_constant=parse_constant, object_pairs_hook=object_pairs_hook, **kw)
  File "/usr/lib/python3.14/json/__init__.py", line 352, in loads
    return _default_decoder.decode(s)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^
  File "/usr/lib/python3.14/json/decoder.py", line 345, in decode
    obj, end = self.raw_decode(s, idx=_w(s, 0).end())
               ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.14/json/decoder.py", line 363, in raw_decode
    raise JSONDecodeError("Expecting value", s, err.value) from None
json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_full_experiment_data_table_20260515T110438",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-15T11:11:52.761031+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "head -c 200 /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/9b1b3290-57d1-413f-bf56-b2da5c5109ee/tool-results/mcp-agent-ml-research-read_registry-1778843095164.txt | xxd | head -20",
  "description": "Check raw bytes at start of file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_full_experiment_data_table_20260515T110438",
  "tool": "Bash",
  "tool_args": {
    "command": "head -c 200 /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/9b1b3290-57d1-413f-bf56-b2da5c5109ee/tool-results/mcp-agent-ml-research-read_registry-1778843095164.txt | xxd | head -20",
    "description": "Check raw bytes at start of file"
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-15T11:11:52.761166+00:00_

00000000: 7b22 7265 7375 6c74 223a 227b 5c22 7375  {"result":"{\"su
00000010: 6363 6573 735c 223a 2074 7275 652c 205c  ccess\": true, \
00000020: 2264 6174 615c 223a 207b 5c22 6578 7065  "data\": {\"expe
00000030: 7269 6d65 6e74 735c 223a 207b 5c22 6772  riments\": {\"gr
00000040: 6964 5f62 355f 305f 7365 6564 3435 365c  id_b5_0_seed456\
00000050: 223a 207b 5c22 7374 6174 7573 5c22 3a20  ": {\"status\": 
00000060: 5c22 444f 4e45 5c22 2c20 5c22 7265 7472  \"DONE\", \"retr
00000070: 795f 636f 756e 745c 223a 2031 2c20 5c22  y_count\": 1, \"
00000080: 6372 6561 7465 645f 6174 5c22 3a20 5c22  created_at\": \"
00000090: 3230 3236 2d30 352d 3134 5430 363a 3539  2026-05-14T06:59
000000a0: 3a33 392e 3035 305a 5c22 2c20 5c22 7570  :39.050Z\", \"up
000000b0: 6461 7465 645f 6174 5c22 3a20 5c22 3230  dated_at\": \"20
000000c0: 3236 2d30 352d 3135                      26-05-15

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_full_experiment_data_table_20260515T110438",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-15T11:11:52.761324+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json, re\n\nfilepath = \"/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/9b1b3290-57d1-413f-bf56-b2da5c5109ee/tool-results/mcp-agent-ml-research-read_registry-1778843095164.txt\"\n\nwith open(filepath, 'r') as f:\n    raw = f.read()\n\ndata = json.loads(raw)\ninner = json.loads(data['result'])\nexps = inner['data']['experiments']\n\n# Extract structured data for all experiments\nrecords = []\nfor exp_id, v in exps.items():\n    rec = {\n        'exp_id': exp_id,\n        'status': v.get('status', 'UNKNOWN'),\n        'conclusion': v.get('conclusion', ''),\n        'hypothesis': v.get('hypothesis', ''),\n        'notes': v.get('notes', ''),\n        'failure_reason': v.get('failure_reason', ''),\n    }\n    \n    # Extract seed\n    spec = v.get('spec', {})\n    if isinstance(spec, dict):\n        rec['seed'] = spec.get('seed', '')\n    else:\n        rec['seed'] = ''\n    \n    # Extract metrics\n    metrics = v.get('metrics', {})\n    if isinstance(metrics, dict):\n        rec['eval_ppl'] = metrics.get('eval_ppl_holdout', metrics.get('eval_ppl', ''))\n        rec['eval_loss'] = metrics.get('eval_loss', '')\n        rec['train_loss'] = metrics.get('train_loss', '')\n        rec['total_steps'] = metrics.get('total_steps', '')\n        rec['gpu_hours'] = metrics.get('gpu_hours', '')\n        rec['eval_method'] = metrics.get('eval_method', '')\n    else:\n        rec['eval_ppl'] = rec['eval_loss'] = rec['train_loss'] = ''\n        rec['total_steps'] = rec['gpu_hours'] = rec['eval_method'] = ''\n    \n    # Extract b value or tau value from command\n    command = ''\n    if 'reproduce' in v and isinstance(v['reproduce'], dict):\n        command = v['reproduce'].get('command', '')\n    if not command and 'spec' in v and isinstance(v['spec'], dict):\n        command = v['spec'].get('command', '')\n    \n    rec['weighting_method'] = ''\n    rec['grid_b_value'] = ''\n    rec['tau'] = ''\n    rec['n_min'] = ''\n    \n    if command:\n        m = re.search(r'--weighting_method\\s+(\\S+)', command)\n        if m: rec['weighting_method'] = m.group(1)\n        m = re.search(r'--grid_b_value\\s+(\\S+)', command)\n        if m: rec['grid_b_value'] = m.group(1)\n        m = re.search(r'--tau\\s+(\\S+)', command)\n        if m: rec['tau'] = m.group(1)\n        m = re.search(r'--n_min\\s+(\\S+)', command)\n        if m: rec['n_min'] = m.group(1)\n    \n    rec['parent'] = v.get('parent', '')\n    rec['server'] = v.get('server', '')\n    rec['gpu'] = v.get('gpu', '')\n    rec['retry_count'] = v.get('retry_count', 0)\n    rec['checkpoint_path'] = v.get('checkpoint_path', '')\n    \n    reproduce = v.get('reproduce', {})\n    if isinstance(reproduce, dict):\n        rec['training_hours'] = reproduce.get('training_hours', '')\n    else:\n        rec['training_hours'] = ''\n    \n    records.append(rec)\n\n# Categorize\ncategories = {}\nfor r in records:\n    eid = r['exp_id']\n    wm = r['weighting_method']\n    \n    if eid.startswith('grid_b') and (wm == 'grid' or 'grid' in eid):\n        cat = 'grid_b_sweep'\n    elif eid.startswith('tau_'):\n        cat = 'tau_sensitivity_sweep'\n    elif eid.startswith('uniform_'):\n        cat = 'uniform_baseline'\n    elif eid.startswith('adaptive_v2_'):\n        cat = 'adaptive_v2'\n    elif eid.startswith('adaptive_fix_'):\n        cat = 'adaptive_fix'\n    elif eid.startswith('adaptive_seed'):\n        cat = 'adaptive_original'\n    elif eid.startswith('detector_'):\n        cat = 'detector'\n    elif eid.startswith('datagen_'):\n        cat = 'datagen'\n    elif eid.startswith('diagnostic_'):\n        cat = 'diagnostic'\n    elif eid.startswith('nmin'):\n        cat = 'n_min_sensitivity'\n    elif eid.startswith('golden_ratio'):\n        cat = 'golden_ratio_oracle'\n    elif eid.startswith('ess_only'):\n        cat = 'ess_only_baseline'\n    else:\n        cat = 'other'\n    \n    if cat not in categories:\n        categories[cat] = []\n    categories[cat].append(r)\n\n# Print structured output\nfor cat in ['grid_b_sweep', 'uniform_baseline', 'adaptive_original', 'adaptive_v2', 'adaptive_fix', \n            'tau_sensitivity_sweep', 'n_min_sensitivity', 'golden_ratio_oracle', 'ess_only_baseline',\n            'diagnostic', 'detector', 'datagen', 'other']:\n    if cat not in categories:\n        continue\n    recs = categories[cat]\n    print(f\"\\n{'='*80}\")\n    print(f\"  CATEGORY: {cat}  ({len(recs)} experiments)\")\n    print(f\"{'='*80}\")\n    \n    for r in recs:\n        print(f\"\\n  --- {r['exp_id']} ---\")\n        print(f\"  Status:           {r['status']}\")\n        if r['conclusion']:\n            print(f\"  Conclusion:       {r['conclusion']}\")\n        if r['seed']:\n            print(f\"  Seed:             {r['seed']}\")\n        if r['weighting_method']:\n            print(f\"  Weighting method: {r['weighting_method']}\")\n        if r['grid_b_value']:\n            print(f\"  Grid b value:     {r['grid_b_value']}\")\n        if r['tau']:\n            print(f\"  Tau:              {r['tau']}\")\n        if r['n_min']:\n            print(f\"  n_min:            {r['n_min']}\")\n        if r['eval_ppl'] != '':\n            print(f\"  Eval PPL:         {r['eval_ppl']}\")\n        if r['eval_loss'] != '':\n            print(f\"  Eval loss:        {r['eval_loss']}\")\n        if r['train_loss'] != '':\n            print(f\"  Train loss:       {r['train_loss']}\")\n        if r['total_steps'] != '':\n            print(f\"  Total steps:      {r['total_steps']}\")\n        if r['gpu_hours'] != '':\n            print(f\"  GPU hours:        {r['gpu_hours']}\")\n        if r['training_hours'] != '':\n            print(f\"  Training hours:   {r['training_hours']}\")\n        if r['retry_count']:\n            print(f\"  Retry count:      {r['retry_count']}\")\n        if r['checkpoint_path']:\n            print(f\"  Checkpoint:       {r['checkpoint_path']}\")\n        if r['parent']:\n            print(f\"  Parent:           {r['parent']}\")\n        if r['hypothesis']:\n            print(f\"  Hypothesis:       {r['hypothesis']}\")\n        if r['notes']:\n            print(f\"  Notes:            {r['notes']}\")\n        if r['failure_reason']:\n            print(f\"  Failure reason:   {r['failure_reason']}\")\n        if r['eval_method']:\n            print(f\"  Eval method:      {r['eval_method']}\")\n\nprint(f\"\\n{'='*80}\")\nprint(f\"  SUMMARY STATISTICS\")\nprint(f\"{'='*80}\")\nstatus_counts = {}\nconclusion_counts = {}\nfor r in records:\n    s = r['status']\n    status_counts[s] = status_counts.get(s, 0) + 1\n    c = r['conclusion'] or '(none)'\n    conclusion_counts[c] = conclusion_counts.get(c, 0) + 1\n\nprint(f\"  Total experiments: {len(records)}\")\nprint(f\"  Status breakdown:\")\nfor s, c in sorted(status_counts.items()):\n    print(f\"    {s:<15s} {c}\")\nprint(f\"  Conclusion breakdown:\")\nfor s, c in sorted(conclusion_counts.items()):\n    print(f\"    {s:<15s} {c}\")\n\n# PPL leaderboard\nppl_records = [(r['exp_id'], r['eval_ppl'], r['weighting_method'], r['grid_b_value'], r['tau'], r['seed']) \n               for r in records if r['eval_ppl'] != '' and isinstance(r['eval_ppl'], (int, float))]\nppl_records.sort(key=lambda x: x[1])\nprint(f\"\\n  PPL Leaderboard (lower is better):\")\nfor eid, ppl, wm, bv, tau, seed in ppl_records:\n    extras = []\n    if bv: extras.append(f\"b={bv}\")\n    if tau: extras.append(f\"tau={tau}\")\n    estr = \", \".join(extras)\n    if estr: estr = f\"  ({estr})\"\n    print(f\"    {ppl:>8.3f}  {eid:<30s}  method={wm}{estr}  seed={seed}\")\n\nPYEOF\n",
  "description": "Extract all experiment records with Python (reading file directly)",
  "timeout": "30000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_full_experiment_data_table_20260515T110438",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 << 'PYEOF'\nimport json, re\n\nfilepath = \"/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/9b1b3290-57d1-413f-bf56-b2da5c5109ee/tool-results/mcp-agent-ml-research-read_registry-1778843095164.txt\"\n\nwith open(filepath, 'r') as f:\n    raw = f.read()\n\ndata = json.loads(raw)\ninner = json.loads(data['result'])\nexps = inner['data']['experiments']\n\n# Extract structured data for all experiments\nrecords = []\nfor exp_id, v in exps.items():\n    rec = {\n        'exp_id': exp_id,\n        'status': v.get('status', 'UNKNOWN'),\n        'conclusion': v.get('conclusion', ''),\n        'hypothesis': v.get('hypothesis', ''),\n        'notes': v.get('notes', ''),\n        'failure_reason': v.get('failure_reason', ''),\n    }\n    \n    # Extract seed\n    spec = v.get('spec', {})\n    if isinstance(spec, dict):\n        rec['seed'] = spec.get('seed', '')\n    else:\n        rec['seed'] = ''\n    \n    # Extract metrics\n    metrics = v.get('metrics', {})\n    if isinstance(metrics, dict):\n        rec['eval_ppl'] = metrics.get('eval_ppl_holdout', metrics.get('eval_ppl', ''))\n        rec['eval_loss'] = metrics.get('eval_loss', '')\n        rec['train_loss'] = metrics.get('train_loss', '')\n        rec['total_steps'] = metrics.get('total_steps', '')\n        rec['gpu_hours'] = metrics.get('gpu_hours', '')\n        rec['eval_method'] = metrics.get('eval_method', '')\n    else:\n        rec['eval_ppl'] = rec['eval_loss'] = rec['train_loss'] = ''\n        rec['total_steps'] = rec['gpu_hours'] = rec['eval_method'] = ''\n    \n    # Extract b value or tau value from command\n    command = ''\n    if 'reproduce' in v and isinstance(v['reproduce'], dict):\n        command = v['reproduce'].get('command', '')\n    if not command and 'spec' in v and isinstance(v['spec'], dict):\n        command = v['spec'].get('command', '')\n    \n    rec['weighting_method'] = ''\n    rec['grid_b_value'] = ''\n    rec['tau'] = ''\n    rec['n_min'] = ''\n    \n    if command:\n        m = re.search(r'--weighting_method\\s+(\\S+)', command)\n        if m: rec['weighting_method'] = m.group(1)\n        m = re.search(r'--grid_b_value\\s+(\\S+)', command)\n        if m: rec['grid_b_value'] = m.group(1)\n        m = re.search(r'--tau\\s+(\\S+)', command)\n        if m: rec['tau'] = m.group(1)\n        m = re.search(r'--n_min\\s+(\\S+)', command)\n        if m: rec['n_min'] = m.group(1)\n    \n    rec['parent'] = v.get('parent', '')\n    rec['server'] = v.get('server', '')\n    rec['gpu'] = v.get('gpu', '')\n    rec['retry_count'] = v.get('retry_count', 0)\n    rec['checkpoint_path'] = v.get('checkpoint_path', '')\n    \n    reproduce = v.get('reproduce', {})\n    if isinstance(reproduce, dict):\n        rec['training_hours'] = reproduce.get('training_hours', '')\n    else:\n        rec['training_hours'] = ''\n    \n    records.append(rec)\n\n# Categorize\ncategories = {}\nfor r in records:\n    eid = r['exp_id']\n    wm = r['weighting_method']\n    \n    if eid.startswith('grid_b') and (wm == 'grid' or 'grid' in eid):\n        cat = 'grid_b_sweep'\n    elif eid.startswith('tau_'):\n        cat = 'tau_sensitivity_sweep'\n    elif eid.startswith('uniform_'):\n        cat = 'uniform_baseline'\n    elif eid.startswith('adaptive_v2_'):\n        cat = 'adaptive_v2'\n    elif eid.startswith('adaptive_fix_'):\n        cat = 'adaptive_fix'\n    elif eid.startswith('adaptive_seed'):\n        cat = 'adaptive_original'\n    elif eid.startswith('detector_'):\n        cat = 'detector'\n    elif eid.startswith('datagen_'):\n        cat = 'datagen'\n    elif eid.startswith('diagnostic_'):\n        cat = 'diagnostic'\n    elif eid.startswith('nmin'):\n        cat = 'n_min_sensitivity'\n    elif eid.startswith('golden_ratio'):\n        cat = 'golden_ratio_oracle'\n    elif eid.startswith('ess_only'):\n        cat = 'ess_only_baseline'\n    else:\n        cat = 'other'\n    \n    if cat not in categories:\n        categories[cat] = []\n    categories[cat].append(r)\n\n# Print structured output\nfor cat in ['grid_b_sweep', 'uniform_baseline', 'adaptive_original', 'adaptive_v2', 'adaptive_fix', \n            'tau_sensitivity_sweep', 'n_min_sensitivity', 'golden_ratio_oracle', 'ess_only_baseline',\n            'diagnostic', 'detector', 'datagen', 'other']:\n    if cat not in categories:\n        continue\n    recs = categories[cat]\n    print(f\"\\n{'='*80}\")\n    print(f\"  CATEGORY: {cat}  ({len(recs)} experiments)\")\n    print(f\"{'='*80}\")\n    \n    for r in recs:\n        print(f\"\\n  --- {r['exp_id']} ---\")\n        print(f\"  Status:           {r['status']}\")\n        if r['conclusion']:\n            print(f\"  Conclusion:       {r['conclusion']}\")\n        if r['seed']:\n            print(f\"  Seed:             {r['seed']}\")\n        if r['weighting_method']:\n            print(f\"  Weighting method: {r['weighting_method']}\")\n        if r['grid_b_value']:\n            print(f\"  Grid b value:     {r['grid_b_value']}\")\n        if r['tau']:\n            print(f\"  Tau:              {r['tau']}\")\n        if r['n_min']:\n            print(f\"  n_min:            {r['n_min']}\")\n        if r['eval_ppl'] != '':\n            print(f\"  Eval PPL:         {r['eval_ppl']}\")\n        if r['eval_loss'] != '':\n            print(f\"  Eval loss:        {r['eval_loss']}\")\n        if r['train_loss'] != '':\n            print(f\"  Train loss:       {r['train_loss']}\")\n        if r['total_steps'] != '':\n            print(f\"  Total steps:      {r['total_steps']}\")\n        if r['gpu_hours'] != '':\n            print(f\"  GPU hours:        {r['gpu_hours']}\")\n        if r['training_hours'] != '':\n            print(f\"  Training hours:   {r['training_hours']}\")\n        if r['retry_count']:\n            print(f\"  Retry count:      {r['retry_count']}\")\n        if r['checkpoint_path']:\n            print(f\"  Checkpoint:       {r['checkpoint_path']}\")\n        if r['parent']:\n            print(f\"  Parent:           {r['parent']}\")\n        if r['hypothesis']:\n            print(f\"  Hypothesis:       {r['hypothesis']}\")\n        if r['notes']:\n            print(f\"  Notes:            {r['notes']}\")\n        if r['failure_reason']:\n            print(f\"  Failure reason:   {r['failure_reason']}\")\n        if r['eval_method']:\n            print(f\"  Eval method:      {r['eval_method']}\")\n\nprint(f\"\\n{'='*80}\")\nprint(f\"  SUMMARY STATISTICS\")\nprint(f\"{'='*80}\")\nstatus_counts = {}\nconclusion_counts = {}\nfor r in records:\n    s = r['status']\n    status_counts[s] = status_counts.get(s, 0) + 1\n    c = r['conclusion'] or '(none)'\n    conclusion_counts[c] = conclusion_counts.get(c, 0) + 1\n\nprint(f\"  Total experiments: {len(records)}\")\nprint(f\"  Status breakdown:\")\nfor s, c in sorted(status_counts.items()):\n    print(f\"    {s:<15s} {c}\")\nprint(f\"  Conclusion breakdown:\")\nfor s, c in sorted(conclusion_counts.items()):\n    print(f\"    {s:<15s} {c}\")\n\n# PPL leaderboard\nppl_records = [(r['exp_id'], r['eval_ppl'], r['weighting_method'], r['grid_b_value'], r['tau'], r['seed']) \n               for r in records if r['eval_ppl'] != '' and isinstance(r['eval_ppl'], (int, float))]\nppl_records.sort(key=lambda x: x[1])\nprint(f\"\\n  PPL Leaderboard (lower is better):\")\nfor eid, ppl, wm, bv, tau, seed in ppl_records:\n    extras = []\n    if bv: extras.append(f\"b={bv}\")\n    if tau: extras.append(f\"tau={tau}\")\n    estr = \", \".join(extras)\n    if estr: estr = f\"  ({estr})\"\n    print(f\"    {ppl:>8.3f}  {eid:<30s}  method={wm}{estr}  seed={seed}\")\n\nPYEOF\n",
    "description": "Extract all experiment records with Python (reading file directly)",
    "timeout": "30000"
  }
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-15T11:11:52.761559+00:00_

================================================================================
  CATEGORY: grid_b_sweep  (14 experiments)
================================================================================

  --- grid_b5_0_seed456 ---
  Status:           DONE
  Conclusion:       success
  Seed:             456
  Weighting method: grid
  Grid b value:     5.0
  Eval PPL:         17.993
  Eval loss:        2.89
  Train loss:       5.488
  Total steps:      6103
  GPU hours:        1.83
  Training hours:   8.65
  Retry count:      1
  Checkpoint:       output/models/grid_b5_0_seed456/final
  Hypothesis:       Grid-b weighting with b=5.0, seed=456, for multi-seed validation of best-b baseline
  Notes:            ⚠️ checkpoint resume artifact: PPL=17.993, 比 seed42(17.818)/seed123(17.804) 高 +0.18。训练中断后从 checkpoint-3000 恢复，导致系统性 PPL 偏高。论文 Table 1 中 b=5.0 行仅报 2 seeds (seed42+seed123)。
  Eval method:      eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)

  --- grid_b3_0_seed456 ---
  Status:           DONE
  Conclusion:       success
  Seed:             456
  Weighting method: grid
  Grid b value:     3.0
  Eval PPL:         17.921
  Eval loss:        2.886
  Train loss:       5.435
  Total steps:      6103
  GPU hours:        1.83
  Training hours:   8.65
  Retry count:      1
  Checkpoint:       output/models/grid_b3_0_seed456/final
  Hypothesis:       Grid-b weighting with b=3.0, seed=456, for multi-seed validation of best-b baseline
  Notes:            ⚠️ checkpoint resume artifact: PPL=17.921, 比 seed42(17.774)/seed123(17.76) 高 +0.16。训练中断后从 checkpoint-3000 恢复，导致系统性 PPL 偏高。论文 Table 1 中 b=3.0 行仅报 2 seeds (seed42+seed123)。
  Eval method:      eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)

  --- grid_b2_0_seed456 ---
  Status:           DONE
  Conclusion:       success
  Weighting method: grid
  Grid b value:     2.0
  Eval PPL:         17.989
  Eval loss:        2.8898
  Train loss:       10.625
  Total steps:      6103
  GPU hour
…[truncated 18404 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_full_experiment_data_table_20260515T110438",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-15T11:11:52.761724+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nfilepath = \"/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/9b1b3290-57d1-413f-bf56-b2da5c5109ee/tool-results/mcp-agent-ml-research-read_registry-1778843095164.txt\"\n\nwith open(filepath, 'r') as f:\n    raw = f.read()\n\ndata = json.loads(raw)\ninner = json.loads(data['result'])\nexps = inner['data']['experiments']\n\n# Print detailed metrics for grid_b_seed42_batch\nbatch = exps['grid_b_seed42_batch']\nprint(\"=== grid_b_seed42_batch (full record) ===\")\nprint(json.dumps(batch, indent=2))\n\n# Also print full records for detector/datagen\nfor k in ['detector_tfidf_lr', 'detector_modernbert', 'datagen_synthetic_4gpu']:\n    print(f\"\\n=== {k} (full record) ===\")\n    print(json.dumps(exps[k], indent=2))\nPYEOF\n",
  "description": "Get full details for batch and utility experiments",
  "timeout": "15000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_full_experiment_data_table_20260515T110438",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 << 'PYEOF'\nimport json\n\nfilepath = \"/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/9b1b3290-57d1-413f-bf56-b2da5c5109ee/tool-results/mcp-agent-ml-research-read_registry-1778843095164.txt\"\n\nwith open(filepath, 'r') as f:\n    raw = f.read()\n\ndata = json.loads(raw)\ninner = json.loads(data['result'])\nexps = inner['data']['experiments']\n\n# Print detailed metrics for grid_b_seed42_batch\nbatch = exps['grid_b_seed42_batch']\nprint(\"=== grid_b_seed42_batch (full record) ===\")\nprint(json.dumps(batch, indent=2))\n\n# Also print full records for detector/datagen\nfor k in ['detector_tfidf_lr', 'detector_modernbert', 'datagen_synthetic_4gpu']:\n    print(f\"\\n=== {k} (full record) ===\")\n    print(json.dumps(exps[k], indent=2))\nPYEOF\n",
    "description": "Get full details for batch and utility experiments",
    "timeout": "15000"
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-15T11:11:52.761895+00:00_

=== grid_b_seed42_batch (full record) ===
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-13T23:50:09.001Z",
  "updated_at": "2026-05-14T22:21:47.253Z",
  "spec": {
    "command": "bash run_grid_b_seed42.sh (6 b values serial: 0.5, 1.0, 1.5, 2.0, 3.0, 5.0)",
    "server": "westd-47453",
    "gpu": [
      "cuda:0"
    ],
    "pid": "50134",
    "log_path": "~/runs/provenance_weight_training/grid_b_seed42_batch.log",
    "submitted_at": "2026-05-13T23:50:08.990Z",
    "submitted_via": "submit_training_job",
    "backend": "tmux",
    "account": "root",
    "data_path": "/root/provenance_weight_training/data/scored_data.jsonl",
    "data_count": 371499,
    "model_name": "Qwen/Qwen3-0.6B",
    "seed": 42,
    "wall_clock_seconds": 81098.3,
    "gpu_hours": 22.53
  },
  "hypothesis": "Grid-b weighting with 6 b values (0.5, 1.0, 1.5, 2.0, 3.0, 5.0) for seed=42, establishes best-b baseline for comparison with adaptive b*",
  "metrics": {
    "b_values": [
      0.5,
      1,
      1.5,
      2,
      3,
      5
    ],
    "b0_5_train_loss": 9.598,
    "b0_5_completed": true,
    "b1_0_completed": true,
    "b1_5_completed": true,
    "b2_0_current_step": 5149,
    "b2_0_total_steps": 6103,
    "completed_b_values": [
      0.5,
      1,
      1.5,
      2,
      3
    ],
    "current_b": 5,
    "total_steps": 6103,
    "current_step": 3422,
    "b5_0_progress_pct": 56,
    "eta_minutes": 95,
    "b2_0_completed": true,
    "b2_0_train_loss": 10.621,
    "b2_0_train_runtime_s": 13034,
    "b3_0_completed": true,
    "b3_0_train_loss": 10.754,
    "b3_0_train_runtime_s": 13036,
    "all_completed": true,
    "b1_0_train_loss": 10.223,
    "b1_5_train_loss": 10.485,
    "b5_0_train_loss": 10.858,
    "b0_5_runtime_s": 13036,
    "b1_0_runtime_s": 12968,
    "b1_5_runtime_s": 14789,
    "b2_0_runtime_s": 13034,
    "b3_0_runtime_s": 13036,
    "b5_0_runtime_s": 13115,
    "note": "eval_ppl missing - no --eval_data_path in batch script, post-hoc eval pendin
…[truncated 3205 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_full_experiment_data_table_20260515T110438",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-15T11:11:52.762116+00:00_

Here is the complete structured summary of all 39 experiments in the provenance_weight_training registry.

---

## CATEGORY: grid_b_sweep (14 experiments)

These experiments test fixed exponential downweighting `w = (1-q)^b` with various `b` values across 3 seeds (42, 123, 456). Model: Qwen3-0.6B, 200M train tokens, contamination_ratio=0.4.

### Seed 42 (batch run)

| exp_id | b | status | eval_ppl | train_loss | notes |
|--------|---|--------|----------|------------|-------|
| grid_b_seed42_batch | 0.5 | DONE/success | 17.651 | 9.598 | best_b=0.5 |
| grid_b_seed42_batch | 1.0 | DONE/success | 17.692 | 10.223 | |
| grid_b_seed42_batch | 1.5 | DONE/success | 17.718 | 10.485 | |
| grid_b_seed42_batch | 2.0 | DONE/success | 17.741 | 10.621 | |
| grid_b_seed42_batch | 3.0 | DONE/success | 17.774 | 10.754 | |
| grid_b_seed42_batch | 5.0 | DONE/success | 17.818 | 10.858 | |

Eval holdout tokens: 4077068. Total steps per b: 6103. Total GPU hours for batch: 22.53.

### Seed 123

| exp_id | b | status | eval_ppl | eval_loss | train_loss |
|--------|---|--------|----------|-----------|------------|
| grid_b0_5_seed123 | 0.5 | DONE/success | 17.638 | 2.87 | 9.601 |
| grid_b1_0_seed123 | 1.0 | DONE/success | 17.674 | 2.8721 | 10.218 |
| grid_b1_5_seed123 | 1.5 | DONE/success | 17.701 | 2.8736 | 10.4776 |
| grid_b2_0_seed123 | 2.0 | DONE/success | 17.725 | 2.875 | 10.61 |
| grid_b3_0_seed123 | 3.0 | DONE/success | 17.76 | 2.877 | 10.7422 |
| grid_b5_0_seed123 | 5.0 | DONE/success | 17.8039 | 2.8794 | 10.8468 |

### Seed 456 (checkpoint resume artifacts -- PPL systematically higher)

| exp_id | b | status | eval_ppl | eval_loss | train_loss | notes |
|--------|---|--------|----------|-----------|------------|-------|
| grid_b0_5_seed456 | 0.5 | DONE/success | 17.65 | 2.8705 | 9.5622 | retry_count=1 (OOM then re-submitted) |
| grid_b1_0_seed456 | 1.0 | DONE/success | 17.68 | 2.8725 | 10.178 | |
| grid_b1_5_seed456 | 1.5 | DONE/success | 17.71 | 2.8741 | 10.435 | |
| grid_b2_0_seed
…[truncated 7017 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_full_experiment_data_table_20260515T110438",
  "tool": "Agent",
  "elapsed_ms": 4
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-15T11:11:52.762367+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/9b1b3290-57d1-413f-bf56-b2da5c5109ee/tool-results && python3 -c \"\nimport json\nwith open('mcp-agent-ml-research-read_registry-1778843095164.txt') as f:\n    data = json.load(f)\nresult = json.loads(data['result'])\nfor exp in result:\n    if 'adaptive_fix' in exp.get('exp_id', ''):\n        print(f\\\"\\\\n=== {exp['exp_id']} ===\\\")\n        metrics = exp.get('metrics', {})\n        for k, v in sorted(metrics.items()):\n            if 'b_star' in k or 'bstar' in k or 'above' in k or 'below' in k or 'pct' in k:\n                print(f'  {k}: {v}')\n        # Also check config\n        config = exp.get('config', {})\n        for k, v in sorted(config.items()):\n            if 'tau' in k or 'n_min' in k:\n                print(f'  config.{k}: {v}')\n\"\n",
  "description": "Extract adaptive_fix b* distribution stats from registry"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_full_experiment_data_table_20260515T110438",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/9b1b3290-57d1-413f-bf56-b2da5c5109ee/tool-results && python3 -c \"\nimport json\nwith open('mcp-agent-ml-research-read_registry-1778843095164.txt') as f:\n    data = json.load(f)\nresult = json.loads(data['result'])\nfor exp in result:\n    if 'adaptive_fix' in exp.get('exp_id', ''):\n        print(f\\\"\\\\n=== {exp['exp_id']} ===\\\")\n        metrics = exp.get('metrics', {})\n        for k, v in sorted(metrics.items()):\n            if 'b_star' in k or 'bstar' in k or 'above' in k or 'below' in k or 'pct' in k:\n                print(f'  {k}: {v}')\n        # Also check config\n        config = exp.get('config', {})\n        for k, v in sorted(config.items()):\n            if 'tau' in k or 'n_min' in k:\n                print(f'  config.{k}: {v}')\n\"\n",
    "description": "Extract adaptive_fix b* distribution stats from registry"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-15T11:11:52.762537+00:00_

Exit code 1
Traceback (most recent call last):
  File "&lt;string>", line 7, in &lt;module>
    if 'adaptive_fix' in exp.get('exp_id', ''):
                         ^^^^^^^
AttributeError: 'str' object has no attribute 'get'

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_full_experiment_data_table_20260515T110438",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-15T11:11:52.762669+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/9b1b3290-57d1-413f-bf56-b2da5c5109ee/tool-results && python3 -c \"\nimport json\nwith open('mcp-agent-ml-research-read_registry-1778843095164.txt') as f:\n    data = json.load(f)\nresult_str = data['result']\n# Check what type result is\nresult = json.loads(result_str) if isinstance(result_str, str) else result_str\nprint(type(result))\nif isinstance(result, list):\n    print(f'List of {len(result)} items')\n    print(type(result[0]))\n    print(json.dumps(result[0], indent=2)[:500])\nelif isinstance(result, dict):\n    print(list(result.keys())[:10])\n\"\n",
  "description": "Probe registry JSON structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_full_experiment_data_table_20260515T110438",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/9b1b3290-57d1-413f-bf56-b2da5c5109ee/tool-results && python3 -c \"\nimport json\nwith open('mcp-agent-ml-research-read_registry-1778843095164.txt') as f:\n    data = json.load(f)\nresult_str = data['result']\n# Check what type result is\nresult = json.loads(result_str) if isinstance(result_str, str) else result_str\nprint(type(result))\nif isinstance(result, list):\n    print(f'List of {len(result)} items')\n    print(type(result[0]))\n    print(json.dumps(result[0], indent=2)[:500])\nelif isinstance(result, dict):\n    print(list(result.keys())[:10])\n\"\n",
    "description": "Probe registry JSON structure"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-15T11:11:52.762796+00:00_

&lt;class 'dict'>
['success', 'data', 'error', 'metadata']
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_full_experiment_data_table_20260515T110438",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-15T11:11:52.762962+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport json\nf = '/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/9b1b3290-57d1-413f-bf56-b2da5c5109ee/tool-results/mcp-agent-ml-research-read_registry-1778843095164.txt'\nwith open(f) as fh:\n    data = json.load(fh)\nresult = json.loads(data['result'])\nexperiments = result['data']\nprint(f'Total experiments: {len(experiments)}')\nfor exp in experiments:\n    if 'adaptive_fix' in exp.get('exp_id', ''):\n        print(f\\\"\\\\n=== {exp['exp_id']} ===\\\")\n        metrics = exp.get('metrics', {})\n        for k, v in sorted(metrics.items()):\n            print(f'  {k}: {v}')\n\"\n",
  "description": "Extract adaptive_fix metrics from registry"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_full_experiment_data_table_20260515T110438",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport json\nf = '/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/9b1b3290-57d1-413f-bf56-b2da5c5109ee/tool-results/mcp-agent-ml-research-read_registry-1778843095164.txt'\nwith open(f) as fh:\n    data = json.load(fh)\nresult = json.loads(data['result'])\nexperiments = result['data']\nprint(f'Total experiments: {len(experiments)}')\nfor exp in experiments:\n    if 'adaptive_fix' in exp.get('exp_id', ''):\n        print(f\\\"\\\\n=== {exp['exp_id']} ===\\\")\n        metrics = exp.get('metrics', {})\n        for k, v in sorted(metrics.items()):\n            print(f'  {k}: {v}')\n\"\n",
    "description": "Extract adaptive_fix metrics from registry"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-15T11:11:52.763144+00:00_

Exit code 1
Traceback (most recent call last):
  File "&lt;string>", line 10, in &lt;module>
    if 'adaptive_fix' in exp.get('exp_id', ''):
                         ^^^^^^^
AttributeError: 'str' object has no attribute 'get'
Total experiments: 4

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_full_experiment_data_table_20260515T110438",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-15T11:11:52.763269+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport json\nf = '/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/9b1b3290-57d1-413f-bf56-b2da5c5109ee/tool-results/mcp-agent-ml-research-read_registry-1778843095164.txt'\nwith open(f) as fh:\n    data = json.load(fh)\nresult = json.loads(data['result'])\nprint(type(result['data']))\nif isinstance(result['data'], dict):\n    print(list(result['data'].keys())[:5])\nelif isinstance(result['data'], list):\n    print(len(result['data']))\n    print(type(result['data'][0]))\n    if isinstance(result['data'][0], str):\n        print(result['data'][:3])\n\"\n",
  "description": "Check registry data structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_full_experiment_data_table_20260515T110438",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport json\nf = '/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/9b1b3290-57d1-413f-bf56-b2da5c5109ee/tool-results/mcp-agent-ml-research-read_registry-1778843095164.txt'\nwith open(f) as fh:\n    data = json.load(fh)\nresult = json.loads(data['result'])\nprint(type(result['data']))\nif isinstance(result['data'], dict):\n    print(list(result['data'].keys())[:5])\nelif isinstance(result['data'], list):\n    print(len(result['data']))\n    print(type(result['data'][0]))\n    if isinstance(result['data'][0], str):\n        print(result['data'][:3])\n\"\n",
    "description": "Check registry data structure"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-15T11:11:52.763396+00:00_

&lt;class 'dict'>
['experiments', 'count', 'total', 'baseline']

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_full_experiment_data_table_20260515T110438",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-15T11:11:52.763513+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport json\nf = '/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/9b1b3290-57d1-413f-bf56-b2da5c5109ee/tool-results/mcp-agent-ml-research-read_registry-1778843095164.txt'\nwith open(f) as fh:\n    data = json.load(fh)\nresult = json.loads(data['result'])\nexperiments = result['data']['experiments']\nprint(f'Total experiments: {len(experiments)}')\nfor exp in experiments:\n    if 'adaptive_fix' in exp.get('exp_id', ''):\n        print(f\\\"\\\\n=== {exp['exp_id']} ===\\\")\n        metrics = exp.get('metrics', {})\n        for k, v in sorted(metrics.items()):\n            print(f'  {k}: {v}')\n\"\n",
  "description": "Extract adaptive_fix metrics"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_full_experiment_data_table_20260515T110438",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport json\nf = '/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/9b1b3290-57d1-413f-bf56-b2da5c5109ee/tool-results/mcp-agent-ml-research-read_registry-1778843095164.txt'\nwith open(f) as fh:\n    data = json.load(fh)\nresult = json.loads(data['result'])\nexperiments = result['data']['experiments']\nprint(f'Total experiments: {len(experiments)}')\nfor exp in experiments:\n    if 'adaptive_fix' in exp.get('exp_id', ''):\n        print(f\\\"\\\\n=== {exp['exp_id']} ===\\\")\n        metrics = exp.get('metrics', {})\n        for k, v in sorted(metrics.items()):\n            print(f'  {k}: {v}')\n\"\n",
    "description": "Extract adaptive_fix metrics"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-15T11:11:52.763632+00:00_

Exit code 1
Traceback (most recent call last):
  File "&lt;string>", line 10, in &lt;module>
    if 'adaptive_fix' in exp.get('exp_id', ''):
                         ^^^^^^^
AttributeError: 'str' object has no attribute 'get'
Total experiments: 39

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_full_experiment_data_table_20260515T110438",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-15T11:11:52.763747+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport json\nf = '/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/9b1b3290-57d1-413f-bf56-b2da5c5109ee/tool-results/mcp-agent-ml-research-read_registry-1778843095164.txt'\nwith open(f) as fh:\n    data = json.load(fh)\nresult = json.loads(data['result'])\nexperiments = result['data']['experiments']\n# Check type of first experiment\nprint(type(experiments[0]))\nif isinstance(experiments[0], str):\n    # It's a list of strings (JSON-encoded)\n    exp = json.loads(experiments[0])\n    print(json.dumps(exp, indent=2)[:300])\nelif isinstance(experiments[0], dict):\n    print(json.dumps(experiments[0], indent=2)[:300])\nelse:\n    print(experiments[0][:300])\n\"\n",
  "description": "Check experiment entry format"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_full_experiment_data_table_20260515T110438",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport json\nf = '/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/9b1b3290-57d1-413f-bf56-b2da5c5109ee/tool-results/mcp-agent-ml-research-read_registry-1778843095164.txt'\nwith open(f) as fh:\n    data = json.load(fh)\nresult = json.loads(data['result'])\nexperiments = result['data']['experiments']\n# Check type of first experiment\nprint(type(experiments[0]))\nif isinstance(experiments[0], str):\n    # It's a list of strings (JSON-encoded)\n    exp = json.loads(experiments[0])\n    print(json.dumps(exp, indent=2)[:300])\nelif isinstance(experiments[0], dict):\n    print(json.dumps(experiments[0], indent=2)[:300])\nelse:\n    print(experiments[0][:300])\n\"\n",
    "description": "Check experiment entry format"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-15T11:11:52.763892+00:00_

Exit code 1
Traceback (most recent call last):
  File "&lt;string>", line 9, in &lt;module>
    print(type(experiments[0]))
               ~~~~~~~~~~~^^^
KeyError: 0

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_full_experiment_data_table_20260515T110438",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-15T11:11:52.764027+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport json\nf = '/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/9b1b3290-57d1-413f-bf56-b2da5c5109ee/tool-results/mcp-agent-ml-research-read_registry-1778843095164.txt'\nwith open(f) as fh:\n    data = json.load(fh)\nresult = json.loads(data['result'])\nexperiments = result['data']['experiments']\n# It's a dict!\nprint(type(experiments))\nkeys = list(experiments.keys())\nprint(f'Keys: {keys[:5]}')\n# Get adaptive_fix entries\nfor k in keys:\n    if 'adaptive_fix' in k:\n        exp = experiments[k]\n        print(f'\\\\n=== {k} ===')\n        print(type(exp))\n        if isinstance(exp, dict):\n            metrics = exp.get('metrics', {})\n            for mk, mv in sorted(metrics.items()):\n                print(f'  {mk}: {mv}')\n        elif isinstance(exp, str):\n            e = json.loads(exp)\n            metrics = e.get('metrics', {})\n            for mk, mv in sorted(metrics.items()):\n                print(f'  {mk}: {mv}')\n\"\n",
  "description": "Extract adaptive_fix metrics from dict-keyed registry"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_full_experiment_data_table_20260515T110438",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport json\nf = '/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/9b1b3290-57d1-413f-bf56-b2da5c5109ee/tool-results/mcp-agent-ml-research-read_registry-1778843095164.txt'\nwith open(f) as fh:\n    data = json.load(fh)\nresult = json.loads(data['result'])\nexperiments = result['data']['experiments']\n# It's a dict!\nprint(type(experiments))\nkeys = list(experiments.keys())\nprint(f'Keys: {keys[:5]}')\n# Get adaptive_fix entries\nfor k in keys:\n    if 'adaptive_fix' in k:\n        exp = experiments[k]\n        print(f'\\\\n=== {k} ===')\n        print(type(exp))\n        if isinstance(exp, dict):\n            metrics = exp.get('metrics', {})\n            for mk, mv in sorted(metrics.items()):\n                print(f'  {mk}: {mv}')\n        elif isinstance(exp, str):\n            e = json.loads(exp)\n            metrics = e.get('metrics', {})\n            for mk, mv in sorted(metrics.items()):\n                print(f'  {mk}: {mv}')\n\"\n",
    "description": "Extract adaptive_fix metrics from dict-keyed registry"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-15T11:11:52.764171+00:00_

&lt;class 'dict'>
Keys: ['grid_b5_0_seed456', 'grid_b3_0_seed456', 'grid_b2_0_seed456', 'tau_095_seed42', 'tau_09_seed42']

=== adaptive_fix_seed456 ===
&lt;class 'dict'>
  b_star_count: 26396
  b_star_max: 20
  b_star_mean: 1.416
  b_star_median: 0.88
  b_star_min: 0
  b_star_note: Training-only records (eval checkpoint records with b*=0 excluded)
  b_star_p25: 0.54
  b_star_p75: 1.52
  b_star_pct_0.5_to_1: 35.7
  b_star_pct_1_to_2: 27.3
  b_star_pct_above_2: 16.1
  b_star_pct_below_0.5: 20.9
  b_star_std: 1.993
  eval_loss_holdout: 2.8711
  eval_ppl_holdout: 17.66
  eval_tokens: 4077068
  total_steps: 6103
  train_loss: 8.3124
  train_runtime: 11436.05
  train_samples_per_second: 8.539
  train_steps_per_second: 0.534

=== adaptive_fix_seed123 ===
&lt;class 'dict'>
  b_star_count: 25906
  b_star_max: 20
  b_star_mean: 1.431
  b_star_median: 0.88
  b_star_min: 0
  b_star_note: Training-only records (eval checkpoint records with b*=0 excluded)
  b_star_p25: 0.54
  b_star_p75: 1.52
  b_star_pct_0.5_to_1: 35.7
  b_star_pct_1_to_2: 27.3
  b_star_pct_2_to_5: 6.3
  b_star_pct_above_2: 16.1
  b_star_pct_above_5: 1.9
  b_star_pct_below_0.5: 20.9
  b_star_std: 2.029
  epoch: 0.26
  eval_loss: 2.8704
  eval_ppl_holdout: 17.643
  eval_tokens: 4077068
  total_steps: 6103
  train_loss_weighted: 7.517
  train_runtime_s: 10347

=== adaptive_fix_seed42 ===
&lt;class 'dict'>
  b_star_count: 26458
  b_star_max: 20
  b_star_mean: 1.399
  b_star_median: 0.871
  b_star_min: 0
  b_star_note: Training-only records (eval checkpoint records with b*=0 excluded)
  b_star_p25: 0.54
  b_star_p75: 1.512
  b_star_pct_0.5_to_1: 35.7
  b_star_pct_1_to_2: 27.3
  b_star_pct_above_2: 16.1
  b_star_pct_below_0.5: 20.9
  b_star_std: 1.933
  eval_loss_holdout: 2.8709
  eval_ppl_holdout: 17.65
  eval_tokens: 4077068
  total_steps: 6103
  train_loss: 7.5167
  train_runtime: 10304.37
  train_samples_per_second: 9.476
  train_steps_per_second: 0.592

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_full_experiment_data_table_20260515T110438",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-15T11:11:52.764329+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport json\nf = '/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/9b1b3290-57d1-413f-bf56-b2da5c5109ee/tool-results/mcp-agent-ml-research-read_registry-1778843095164.txt'\nwith open(f) as fh:\n    data = json.load(fh)\nresult = json.loads(data['result'])\nexperiments = result['data']['experiments']\n\nfor k in sorted(experiments.keys()):\n    exp = experiments[k]\n    status = exp.get('status', '?')\n    conclusion = exp.get('conclusion', '')\n    metrics = exp.get('metrics', {})\n    config = exp.get('config', {})\n    ppl = metrics.get('eval_ppl_holdout', metrics.get('eval_ppl', ''))\n    seed = config.get('seed', exp.get('seed', ''))\n    b_val = config.get('b', config.get('b_value', ''))\n    tau = config.get('tau', config.get('tau_threshold', ''))\n    exp_type = exp.get('type', exp.get('category', ''))\n    hypothesis = exp.get('hypothesis', '')[:80] if exp.get('hypothesis') else ''\n    print(f'{k} | status={status} | conclusion={conclusion} | ppl={ppl} | seed={seed} | b={b_val} | tau={tau} | type={exp_type} | hyp={hypothesis}')\n\"\n",
  "description": "Extract all experiments with key fields"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_full_experiment_data_table_20260515T110438",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport json\nf = '/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/9b1b3290-57d1-413f-bf56-b2da5c5109ee/tool-results/mcp-agent-ml-research-read_registry-1778843095164.txt'\nwith open(f) as fh:\n    data = json.load(fh)\nresult = json.loads(data['result'])\nexperiments = result['data']['experiments']\n\nfor k in sorted(experiments.keys()):\n    exp = experiments[k]\n    status = exp.get('status', '?')\n    conclusion = exp.get('conclusion', '')\n    metrics = exp.get('metrics', {})\n    config = exp.get('config', {})\n    ppl = metrics.get('eval_ppl_holdout', metrics.get('eval_ppl', ''))\n    seed = config.get('seed', exp.get('seed', ''))\n    b_val = config.get('b', config.get('b_value', ''))\n    tau = config.get('tau', config.get('tau_threshold', ''))\n    exp_type = exp.get('type', exp.get('category', ''))\n    hypothesis = exp.get('hypothesis', '')[:80] if exp.get('hypothesis') else ''\n    print(f'{k} | status={status} | conclusion={conclusion} | ppl={ppl} | seed={seed} | b={b_val} | tau={tau} | type={exp_type} | hyp={hypothesis}')\n\"\n",
    "description": "Extract all experiments with key fields"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-15T11:11:52.764490+00:00_

adaptive_fix_seed123 | status=DONE | conclusion=success | ppl=17.643 | seed= | b= | tau= | type= | hyp=D012 n_min fix (3→2, batch_size//2): adaptive b* with corrected ESS constraint m
adaptive_fix_seed42 | status=DONE | conclusion=success | ppl=17.65 | seed= | b= | tau= | type= | hyp=D012 n_min fix (3→2, batch_size//2): adaptive b* with corrected ESS constraint a
adaptive_fix_seed456 | status=DONE | conclusion=success | ppl=17.66 | seed= | b= | tau= | type= | hyp=D012 n_min fix (3→2, batch_size//2): adaptive b* with corrected ESS constraint m
adaptive_seed123 | status=DONE | conclusion=success | ppl=17.63 | seed= | b= | tau= | type= | hyp=Adaptive b* (from α_eff theory) matches or exceeds grid-searched best-b without 
adaptive_seed42 | status=DONE | conclusion=success | ppl=17.69 | seed= | b= | tau= | type= | hyp=Adaptive b* (from α_eff theory) matches or exceeds grid-searched best-b without 
adaptive_seed456 | status=DONE | conclusion=success | ppl=17.64 | seed= | b= | tau= | type= | hyp=Adaptive b* (from α_eff theory) matches or exceeds grid-searched best-b without 
adaptive_v2_seed123 | status=PREPARING | conclusion=killed | ppl= | seed= | b= | tau= | type= | hyp=Adaptive v2 (n_min fix: 3→2, no EMA) maintains or improves seed123 performance (
adaptive_v2_seed42 | status=PREPARING | conclusion=killed | ppl= | seed= | b= | tau= | type= | hyp=Adaptive v2 (n_min fix: 3→2, no EMA) fixes ESS clamping issue, achieves meaningf
adaptive_v2_seed456 | status=PREPARING | conclusion=killed | ppl= | seed= | b= | tau= | type= | hyp=Adaptive v2 (n_min fix: 3→2, no EMA) maintains or improves seed456 performance (
datagen_synthetic_4gpu | status=DONE | conclusion=success | ppl= | seed= | b= | tau= | type= | hyp=
detector_modernbert | status=QUEUED | conclusion=success | ppl= | seed= | b= | tau= | type= | hyp=ModernBERT-base can distinguish Qwen3-0.6B synthetic text from FineWeb human tex
detector_tfidf_lr | status=DONE | conclusion=success | ppl= | seed= | b= | tau= | type= | hyp=
…[truncated 4361 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_full_experiment_data_table_20260515T110438",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-15T11:11:52.764648+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport json\nf = '/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/9b1b3290-57d1-413f-bf56-b2da5c5109ee/tool-results/mcp-agent-ml-research-read_registry-1778843095164.txt'\nwith open(f) as fh:\n    data = json.load(fh)\nresult = json.loads(data['result'])\nexperiments = result['data']['experiments']\n\n# Get grid_b_seed42_batch full metrics\nexp = experiments['grid_b_seed42_batch']\nmetrics = exp.get('metrics', {})\nfor k, v in sorted(metrics.items()):\n    print(f'{k}: {v}')\n\"\n",
  "description": "Get grid_b_seed42_batch metrics"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_full_experiment_data_table_20260515T110438",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport json\nf = '/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/9b1b3290-57d1-413f-bf56-b2da5c5109ee/tool-results/mcp-agent-ml-research-read_registry-1778843095164.txt'\nwith open(f) as fh:\n    data = json.load(fh)\nresult = json.loads(data['result'])\nexperiments = result['data']['experiments']\n\n# Get grid_b_seed42_batch full metrics\nexp = experiments['grid_b_seed42_batch']\nmetrics = exp.get('metrics', {})\nfor k, v in sorted(metrics.items()):\n    print(f'{k}: {v}')\n\"\n",
    "description": "Get grid_b_seed42_batch metrics"
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-15T11:11:52.764779+00:00_

all_completed: True
b0_5_completed: True
b0_5_eval_ppl: 17.651
b0_5_runtime_s: 13036
b0_5_train_loss: 9.598
b1_0_completed: True
b1_0_eval_ppl: 17.692
b1_0_runtime_s: 12968
b1_0_train_loss: 10.223
b1_5_completed: True
b1_5_eval_ppl: 17.718
b1_5_runtime_s: 14789
b1_5_train_loss: 10.485
b2_0_completed: True
b2_0_current_step: 5149
b2_0_eval_ppl: 17.741
b2_0_runtime_s: 13034
b2_0_total_steps: 6103
b2_0_train_loss: 10.621
b2_0_train_runtime_s: 13034
b3_0_completed: True
b3_0_eval_ppl: 17.774
b3_0_runtime_s: 13036
b3_0_train_loss: 10.754
b3_0_train_runtime_s: 13036
b5_0_eval_ppl: 17.818
b5_0_progress_pct: 56
b5_0_runtime_s: 13115
b5_0_train_loss: 10.858
b_values: [0.5, 1, 1.5, 2, 3, 5]
best_b: 0.5
best_eval_ppl: 17.651
completed_b_values: [0.5, 1, 1.5, 2, 3]
current_b: 5
current_step: 3422
eta_minutes: 95
eval_holdout_tokens: 4077068
note: eval_ppl missing - no --eval_data_path in batch script, post-hoc eval pending
total_steps: 6103

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_full_experiment_data_table_20260515T110438",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-15T11:11:52.764954+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport json\nf = '/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/9b1b3290-57d1-413f-bf56-b2da5c5109ee/tool-results/mcp-agent-ml-research-read_registry-1778843095164.txt'\nwith open(f) as fh:\n    data = json.load(fh)\nresult = json.loads(data['result'])\nexperiments = result['data']['experiments']\n\n# Uniform experiments\nfor k in ['uniform_seed42', 'uniform_seed123', 'uniform_seed456']:\n    exp = experiments[k]\n    metrics = exp.get('metrics', {})\n    print(f'\\\\n=== {k} ===')\n    for mk, mv in sorted(metrics.items()):\n        print(f'  {mk}: {mv}')\n\n# Also check seed123 grid b values for exact decimal places\nfor k in ['grid_b0_5_seed123', 'grid_b1_0_seed123', 'grid_b1_5_seed123', 'grid_b2_0_seed123', 'grid_b3_0_seed123', 'grid_b5_0_seed123']:\n    exp = experiments[k]\n    metrics = exp.get('metrics', {})\n    ppl = metrics.get('eval_ppl_holdout', metrics.get('eval_ppl', ''))\n    loss = metrics.get('eval_loss_holdout', metrics.get('eval_loss', ''))\n    tloss = metrics.get('train_loss', metrics.get('train_loss_weighted', ''))\n    print(f'{k}: ppl={ppl}, eval_loss={loss}, train_loss={tloss}')\n\"\n",
  "description": "Verify uniform and seed123 grid metrics"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_full_experiment_data_table_20260515T110438",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport json\nf = '/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/9b1b3290-57d1-413f-bf56-b2da5c5109ee/tool-results/mcp-agent-ml-research-read_registry-1778843095164.txt'\nwith open(f) as fh:\n    data = json.load(fh)\nresult = json.loads(data['result'])\nexperiments = result['data']['experiments']\n\n# Uniform experiments\nfor k in ['uniform_seed42', 'uniform_seed123', 'uniform_seed456']:\n    exp = experiments[k]\n    metrics = exp.get('metrics', {})\n    print(f'\\\\n=== {k} ===')\n    for mk, mv in sorted(metrics.items()):\n        print(f'  {mk}: {mv}')\n\n# Also check seed123 grid b values for exact decimal places\nfor k in ['grid_b0_5_seed123', 'grid_b1_0_seed123', 'grid_b1_5_seed123', 'grid_b2_0_seed123', 'grid_b3_0_seed123', 'grid_b5_0_seed123']:\n    exp = experiments[k]\n    metrics = exp.get('metrics', {})\n    ppl = metrics.get('eval_ppl_holdout', metrics.get('eval_ppl', ''))\n    loss = metrics.get('eval_loss_holdout', metrics.get('eval_loss', ''))\n    tloss = metrics.get('train_loss', metrics.get('train_loss_weighted', ''))\n    print(f'{k}: ppl={ppl}, eval_loss={loss}, train_loss={tloss}')\n\"\n",
    "description": "Verify uniform and seed123 grid metrics"
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-15T11:11:52.765100+00:00_

=== uniform_seed42 ===
  eval_holdout_tokens: 4080000
  eval_ppl_holdout: 17.69
  total_steps: 6103
  train_duration_s: 11946
  train_loss: 7.3104

=== uniform_seed123 ===
  eval_holdout_tokens: 4080000
  eval_ppl_holdout: 17.69
  total_steps: 6103
  train_duration_s: 11994
  train_loss: 7.3121

=== uniform_seed456 ===
  eval_holdout_tokens: 4080000
  eval_ppl_holdout: 17.7
  total_steps: 6103
  train_duration_s: 11974
  train_loss: 7.2895
grid_b0_5_seed123: ppl=17.638, eval_loss=2.87, train_loss=9.601
grid_b1_0_seed123: ppl=17.674, eval_loss=2.8721, train_loss=10.218
grid_b1_5_seed123: ppl=17.701, eval_loss=2.8736, train_loss=10.4776
grid_b2_0_seed123: ppl=17.725, eval_loss=2.875, train_loss=10.61
grid_b3_0_seed123: ppl=17.76, eval_loss=2.877, train_loss=10.7422
grid_b5_0_seed123: ppl=17.8039, eval_loss=2.8794, train_loss=10.8468

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_full_experiment_data_table_20260515T110438",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-15T11:11:52.765240+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport json\nf = '/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/9b1b3290-57d1-413f-bf56-b2da5c5109ee/tool-results/mcp-agent-ml-research-read_registry-1778843095164.txt'\nwith open(f) as fh:\n    data = json.load(fh)\nresult = json.loads(data['result'])\nexperiments = result['data']['experiments']\n\n# Seed456 grid\nfor k in ['grid_b0_5_seed456', 'grid_b1_0_seed456', 'grid_b1_5_seed456', 'grid_b2_0_seed456', 'grid_b3_0_seed456', 'grid_b5_0_seed456']:\n    exp = experiments[k]\n    metrics = exp.get('metrics', {})\n    ppl = metrics.get('eval_ppl_holdout', metrics.get('eval_ppl', ''))\n    loss = metrics.get('eval_loss_holdout', metrics.get('eval_loss', ''))\n    tloss = metrics.get('train_loss', '')\n    print(f'{k}: ppl={ppl}, eval_loss={loss}, train_loss={tloss}')\n\n# adaptive_original\nprint()\nfor k in ['adaptive_seed42', 'adaptive_seed123', 'adaptive_seed456']:\n    exp = experiments[k]\n    metrics = exp.get('metrics', {})\n    for mk, mv in sorted(metrics.items()):\n        print(f'{k}.{mk}: {mv}')\n    print()\n\"\n",
  "description": "Get seed456 grid and adaptive_original metrics"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_full_experiment_data_table_20260515T110438",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport json\nf = '/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/9b1b3290-57d1-413f-bf56-b2da5c5109ee/tool-results/mcp-agent-ml-research-read_registry-1778843095164.txt'\nwith open(f) as fh:\n    data = json.load(fh)\nresult = json.loads(data['result'])\nexperiments = result['data']['experiments']\n\n# Seed456 grid\nfor k in ['grid_b0_5_seed456', 'grid_b1_0_seed456', 'grid_b1_5_seed456', 'grid_b2_0_seed456', 'grid_b3_0_seed456', 'grid_b5_0_seed456']:\n    exp = experiments[k]\n    metrics = exp.get('metrics', {})\n    ppl = metrics.get('eval_ppl_holdout', metrics.get('eval_ppl', ''))\n    loss = metrics.get('eval_loss_holdout', metrics.get('eval_loss', ''))\n    tloss = metrics.get('train_loss', '')\n    print(f'{k}: ppl={ppl}, eval_loss={loss}, train_loss={tloss}')\n\n# adaptive_original\nprint()\nfor k in ['adaptive_seed42', 'adaptive_seed123', 'adaptive_seed456']:\n    exp = experiments[k]\n    metrics = exp.get('metrics', {})\n    for mk, mv in sorted(metrics.items()):\n        print(f'{k}.{mk}: {mv}')\n    print()\n\"\n",
    "description": "Get seed456 grid and adaptive_original metrics"
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-15T11:11:52.765387+00:00_

grid_b0_5_seed456: ppl=17.65, eval_loss=2.8705, train_loss=9.5622
grid_b1_0_seed456: ppl=17.68, eval_loss=2.8734, train_loss=10.178
grid_b1_5_seed456: ppl=17.71, eval_loss=2.875, train_loss=10.435
grid_b2_0_seed456: ppl=17.989, eval_loss=2.8898, train_loss=10.625
grid_b3_0_seed456: ppl=17.921, eval_loss=2.886, train_loss=5.435
grid_b5_0_seed456: ppl=17.993, eval_loss=2.89, train_loss=5.488

adaptive_seed42.alpha_eff_range: 0.03-0.80 (capped at tau)
adaptive_seed42.b_star: per-batch adaptive (0.0-3.8)
adaptive_seed42.contamination_ratio: 0.4
adaptive_seed42.epoch: 0.26
adaptive_seed42.eval_holdout_tokens: 4080000
adaptive_seed42.eval_ppl_holdout: 17.69
adaptive_seed42.n_min: 3
adaptive_seed42.tau: 0.8
adaptive_seed42.total_steps: 6103
adaptive_seed42.train_loss: 9.2665
adaptive_seed42.train_runtime_s: 13115.09
adaptive_seed42.train_samples_per_second: 7.445
adaptive_seed42.train_steps_per_second: 0.465
adaptive_seed42.weighting_method: adaptive

adaptive_seed123.alpha_eff_range: 0.04-0.80 (capped at tau)
adaptive_seed123.b_star: per-batch adaptive (0.0-3.8)
adaptive_seed123.contamination_ratio: 0.4
adaptive_seed123.epoch: 0.26
adaptive_seed123.eval_holdout_tokens: 4080000
adaptive_seed123.eval_ppl_holdout: 17.63
adaptive_seed123.n_min: 3
adaptive_seed123.tau: 0.8
adaptive_seed123.total_steps: 6103
adaptive_seed123.train_loss: 9.2665
adaptive_seed123.train_runtime_s: 13197.18
adaptive_seed123.train_samples_per_second: 7.399
adaptive_seed123.train_steps_per_second: 0.462
adaptive_seed123.weighting_method: adaptive

adaptive_seed456.alpha_eff_range: 0.09-0.80 (capped at tau)
adaptive_seed456.b_star: per-batch adaptive (0.0-3.8)
adaptive_seed456.contamination_ratio: 0.4
adaptive_seed456.epoch: 0.26
adaptive_seed456.eval_holdout_tokens: 4080000
adaptive_seed456.eval_ppl_holdout: 17.64
adaptive_seed456.n_min: 3
adaptive_seed456.tau: 0.8
adaptive_seed456.total_steps: 6103
adaptive_seed456.train_loss: 9.2354
adaptive_seed456.train_runtime_s: 13130.09
adaptive_seed456.train_s
…[truncated 115 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_full_experiment_data_table_20260515T110438",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-15T11:11:52.765612+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/full_experiment_data.md",
  "content": "# Full Experiment Data — Provenance Weight Training\n\nAll values sourced from project registry (`provenance_weight_training`). Generated 2026-05-15.\n\n**Setup**: Qwen3-0.6B, 200M train tokens (371K samples, 40% synthetic contamination), eval on held-out human data (4.08M tokens), 6103 training steps per run.\n\n---\n\n## Table A: Grid-b Sweep (eval_ppl_holdout)\n\n| b | seed42 | seed123 | seed456 | Mean ± Std | Valid Seeds |\n|-----|--------|---------|---------|------------|-------------|\n| 0.5 | 17.651 | 17.638 | 17.650 | 17.646 ± 0.007 | 3 |\n| 1.0 | 17.692 | 17.674 | 17.680 | 17.682 ± 0.009 | 3 |\n| 1.5 | 17.718 | 17.701 | 17.710 | 17.710 ± 0.009 | 3 |\n| 2.0 | 17.741 | 17.725 | 17.989† | 17.733 ± 0.011 | 2\\* |\n| 3.0 | 17.774 | 17.760 | 17.921† | 17.767 ± 0.010 | 2\\* |\n| 5.0 | 17.818 | 17.804 | 17.993† | 17.811 ± 0.010 | 2\\* |\n\n†INVALIDATED: seed456 b∈{2.0, 3.0, 5.0} training was interrupted and resumed from checkpoint (D026), causing systematic PPL inflation of +0.15 to +0.25. These values are excluded from Mean/Std.\n\n\\*Mean/Std computed from seed42 + seed123 only.\n\n**Observations**:\n- PPL increases monotonically with b (best b = 0.5)\n- Effect is consistent across all seeds\n- Std is small (0.007–0.011), confirming reproducibility\n\n---\n\n## Table B: Method Comparison (eval_ppl_holdout)\n\n| Method | seed42 | seed123 | seed456 | Mean | Std |\n|-------------------|--------|---------|---------|-------|-------|\n| Uniform (w=1) | 17.690 | 17.690 | 17.700 | 17.693 | 0.006 |\n| Grid-best (b=0.5) | 17.651 | 17.638 | 17.650 | 17.646 | 0.007 |\n| Adaptive_fix (τ=0.8) | 17.650 | 17.643 | 17.660 | 17.651 | 0.009 |\n\n### Improvement Analysis\n\n| Metric | seed42 | seed123 | seed456 | Mean |\n|-----------------------------|---------|---------|---------|---------|\n| Δ(adaptive vs uniform) | 0.040 | 0.047 | 0.040 | 0.042 |\n| Δ(grid-best vs uniform) | 0.039 | 0.052 | 0.050 | 0.047 |\n| Per-seed ratio (Δ_a/Δ_g %) | 102.6% | 90.4% | 80.0% | 91.0% |\n\n### Ratio-of-Means (论文口径)\n\n$$\\text{ratio-of-means} = \\frac{\\bar{PPL}_{\\text{adaptive}} - \\bar{PPL}_{\\text{uniform}}}{\\bar{PPL}_{\\text{grid}} - \\bar{PPL}_{\\text{uniform}}} = \\frac{17.651 - 17.693}{17.646 - 17.693} = \\frac{-0.042}{-0.047} = 89.4\\%$$\n\nAdaptive_fix recovers **89.4%** of grid-best improvement without grid search (ratio-of-means). Mean-of-ratios = 91.0% — reported for reference but not used as paper headline.\n\n---\n\n## Table C: b\\* Distribution Statistics (from adaptive_fix, τ=0.8)\n\n| Statistic | seed42 | seed123 | seed456 | Mean | CV |\n|---------------|--------|---------|---------|-------|------|\n| b\\* Mean | 1.399 | 1.431 | 1.416 | 1.415 | 1.1% |\n| b\\* Median | 0.871 | 0.880 | 0.880 | 0.877 | 0.6% |\n| b\\* Std | 1.933 | 2.029 | 1.993 | 1.985 | 2.4% |\n| b\\* P25 | 0.540 | 0.540 | 0.540 | 0.540 | 0.0% |\n| b\\* P75 | 1.512 | 1.520 | 1.520 | 1.517 | 0.3% |\n| % below 0.5 | 20.9% | 20.9% | 20.9% | 20.9% | 0.0% |\n| % above 2.0 | 16.1% | 16.1% | 16.1% | 16.1% | 0.0% |\n\n**Observations**:\n- b\\* distribution is highly stable across seeds (CV < 2.5% for all statistics)\n- Median b\\* ≈ 0.88, reflecting moderate downweighting for most batches\n- Right-skewed: mean (1.415) > median (0.877), driven by ~16% of batches with b\\* > 2.0\n- ~21% of batches receive strong downweighting (b\\* < 0.5)\n\n---\n\n## Table D: Complete Experiment Index\n\n### D.1 — DONE experiments (26 total)\n\n| exp_id | type | seed | b / τ | eval_ppl | status | conclusion |\n|-------------------------------|---------------|------|------------|----------|--------|-------------------------------------|\n| grid_b_seed42_batch | grid_b_sweep | 42 | b=0.5–5.0 | 17.651\\* | DONE | success (\\*best_b=0.5) |\n| grid_b0_5_seed123 | grid_b_sweep | 123 | b=0.5 | 17.638 | DONE | success |\n| grid_b1_0_seed123 | grid_b_sweep | 123 | b=1.0 | 17.674 | DONE | success |\n| grid_b1_5_seed123 | grid_b_sweep | 123 | b=1.5 | 17.701 | DONE | success |\n| grid_b2_0_seed123 | grid_b_sweep | 123 | b=2.0 | 17.725 | DONE | success |\n| grid_b3_0_seed123 | grid_b_sweep | 123 | b=3.0 | 17.760 | DONE | success |\n| grid_b5_0_seed123 | grid_b_sweep | 123 | b=5.0 | 17.804 | DONE | success |\n| grid_b0_5_seed456 | grid_b_sweep | 456 | b=0.5 | 17.650 | DONE | success |\n| grid_b1_0_seed456 | grid_b_sweep | 456 | b=1.0 | 17.680 | DONE | success |\n| grid_b1_5_seed456 | grid_b_sweep | 456 | b=1.5 | 17.710 | DONE | success |\n| grid_b2_0_seed456 | grid_b_sweep | 456 | b=2.0 | 17.989 | DONE | INVALIDATED (D026 checkpoint resume) |\n| grid_b3_0_seed456 | grid_b_sweep | 456 | b=3.0 | 17.921 | DONE | INVALIDATED (D026 checkpoint resume) |\n| grid_b5_0_seed456 | grid_b_sweep | 456 | b=5.0 | 17.993 | DONE | INVALIDATED (D026 checkpoint resume) |\n| grid_b_low_seed42 | grid_b_low | 42 | b=0.1/0.2/0.3 | — | DONE | failed (infra: cron killed process) |\n| uniform_seed42 | uniform | 42 | — | 17.690 | DONE | success |\n| uniform_seed123 | uniform | 123 | — | 17.690 | DONE | success |\n| uniform_seed456 | uniform | 456 | — | 17.700 | DONE | success |\n| adaptive_seed42 | adaptive | 42 | τ=0.8 | 17.690 | DONE | success (n_min=3 bug, superseded) |\n| adaptive_seed123 | adaptive | 123 | τ=0.8 | 17.630 | DONE | success (n_min=3 bug, superseded) |\n| adaptive_seed456 | adaptive | 456 | τ=0.8 | 17.640 | DONE | success (n_min=3 bug, superseded) |\n| adaptive_fix_seed42 | adaptive_fix | 42 | τ=0.8 | 17.650 | DONE | success |\n| adaptive_fix_seed123 | adaptive_fix | 123 | τ=0.8 | 17.643 | DONE | success |\n| adaptive_fix_seed456 | adaptive_fix | 456 | τ=0.8 | 17.660 | DONE | success |\n| datagen_synthetic_4gpu | datagen | — | — | — | DONE | success (340992 docs, 132M tokens) |\n| detector_tfidf_lr | detector | — | — | — | DONE | success (AUC=0.939, ECE_cal=0.048) |\n| diagnostic_contamination100 | diagnostic | — | — | — | DONE | killed (freed GPU for grid-b seed123) |\n\n### D.2 — RUNNING experiments (4 total)\n\n| exp_id | type | seed | params | status |\n|---------------------|-------------------|------|--------------|---------|\n| ess_only_seed42 | ess_only_baseline | 42 | n_min=2 | RUNNING |\n| golden_ratio_seed42 | golden_ratio | 42 | w=1/φ oracle | RUNNING |\n| nmin1_seed42 | n_min_sensitivity | 42 | n_min=1, τ=0.8 | RUNNING |\n| tau_06_seed42 | tau_sweep | 42 | τ=0.6 | RUNNING |\n\n### D.3 — PREPARING / QUEUED experiments (9 total)\n\n| exp_id | type | seed | params | status | conclusion |\n|-----------------------|-----------|------|--------|-----------|------------|\n| adaptive_v2_seed42 | adaptive_v2 | 42 | — | PREPARING | killed |\n| adaptive_v2_seed123 | adaptive_v2 | 123 | — | PREPARING | killed |\n| adaptive_v2_seed456 | adaptive_v2 | 456 | — | PREPARING | killed |\n| tau_0.6_seed42 | tau_sweep | 42 | τ=0.6 | QUEUED | killed (replaced by tau_06_seed42) |\n| detector_modernbert | detector | — | — | QUEUED | success (superseded by TF-IDF) |\n| tau_05_seed42 | tau_sweep | 42 | τ=0.5 | PREPARING | — |\n| tau_07_seed42 | tau_sweep | 42 | τ=0.7 | PREPARING | — |\n| tau_09_seed42 | tau_sweep | 42 | τ=0.9 | PREPARING | — |\n| tau_095_seed42 | tau_sweep | 42 | τ=0.95 | PREPARING | — |\n\n---\n\n## Summary\n\n| Category | Total | Success | Invalidated | Failed | Killed | Running/Pending |\n|------------------|-------|---------|-------------|--------|--------|-----------------|\n| grid_b_sweep | 20 | 15 | 3 | 1 | 0 | 0+1\\*\\* |\n| uniform | 3 | 3 | 0 | 0 | 0 | 0 |\n| adaptive (orig) | 3 | 3 | 0 | 0 | 0 | 0 |\n| adaptive_v2 | 3 | 0 | 0 | 0 | 3 | 0 |\n| adaptive_fix | 3 | 3 | 0 | 0 | 0 | 0 |\n| tau_sweep | 6 | 0 | 0 | 0 | 1 | 1+4 |\n| n_min_sensitivity | 1 | 0 | 0 | 0 | 0 | 1 |\n| ess_only | 1 | 0 | 0 | 0 | 0 | 1 |\n| golden_ratio | 1 | 0 | 0 | 0 | 0 | 1 |\n| datagen | 1 | 1 | 0 | 0 | 0 | 0 |\n| detector | 2 | 2 | 0 | 0 | 0 | 0 |\n| diagnostic | 1 | 0 | 0 | 0 | 1 | 0 |\n| **Total** | **39** | **24\\*** | **3** | **1** | **5** | **4+5** |\n\n\\*\\*grid_b_low_seed42 = failed (infra bug, not re-run).\n\\*24 DONE with conclusion=success (includes 3 invalidated experiments which completed but have unreliable metrics).\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_full_experiment_data_table_20260515T110438",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/full_experiment_data.md",
    "content": "# Full Experiment Data — Provenance Weight Training\n\nAll values sourced from project registry (`provenance_weight_training`). Generated 2026-05-15.\n\n**Setup**: Qwen3-0.6B, 200M train tokens (371K samples, 40% synthetic contamination), eval on held-out human data (4.08M tokens), 6103 training steps per run.\n\n---\n\n## Table A: Grid-b Sweep (eval_ppl_holdout)\n\n| b | seed42 | seed123 | seed456 | Mean ± Std | Valid Seeds |\n|-----|--------|---------|---------|------------|-------------|\n| 0.5 | 17.651 | 17.638 | 17.650 | 17.646 ± 0.007 | 3 |\n| 1.0 | 17.692 | 17.674 | 17.680 | 17.682 ± 0.009 | 3 |\n| 1.5 | 17.718 | 17.701 | 17.710 | 17.710 ± 0.009 | 3 |\n| 2.0 | 17.741 | 17.725 | 17.989† | 17.733 ± 0.011 | 2\\* |\n| 3.0 | 17.774 | 17.760 | 17.921† | 17.767 ± 0.010 | 2\\* |\n| 5.0 | 17.818 | 17.804 | 17.993† | 17.811 ± 0.010 | 2\\* |\n\n†INVALIDATED: seed456 b∈{2.0, 3.0, 5.0} training was interrupted and resumed from checkpoint (D026), causing systematic PPL inflation of +0.15 to +0.25. These values are excluded from Mean/Std.\n\n\\*Mean/Std computed from seed42 + seed123 only.\n\n**Observations**:\n- PPL increases monotonically with b (best b = 0.5)\n- Effect is consistent across all seeds\n- Std is small (0.007–0.011), confirming reproducibility\n\n---\n\n## Table B: Method Comparison (eval_ppl_holdout)\n\n| Method | seed42 | seed123 | seed456 | Mean | Std |\n|-------------------|--------|---------|---------|-------|-------|\n| Uniform (w=1) | 17.690 | 17.690 | 17.700 | 17.693 | 0.006 |\n| Grid-best (b=0.5) | 17.651 | 17.638 | 17.650 | 17.646 | 0.007 |\n| Adaptive_fix (τ=0.8) | 17.650 | 17.643 | 17.660 | 17.651 | 0.009 |\n\n### Improvement Analysis\n\n| Metric | seed42 | seed123 | seed456 | Mean |\n|-----------------------------|---------|---------|---------|---------|\n| Δ(adaptive vs uniform) | 0.040 | 0.047 | 0.040 | 0.042 |\n| Δ(grid-best vs uniform) | 0.039 | 0.052 | 0.050 | 0.047 |\n| Per-seed ratio (Δ_a/Δ_g %) | 102.6% | 90.4% | 80.0% | 91.0% |\n\n### Ratio-of-Means (论文口径)\n\n$$\\text{ratio-of-means} = \\frac{\\bar{PPL}_{\\text{adaptive}} - \\bar{PPL}_{\\text{uniform}}}{\\bar{PPL}_{\\text{grid}} - \\bar{PPL}_{\\text{uniform}}} = \\frac{17.651 - 17.693}{17.646 - 17.693} = \\frac{-0.042}{-0.047} = 89.4\\%$$\n\nAdaptive_fix recovers **89.4%** of grid-best improvement without grid search (ratio-of-means). Mean-of-ratios = 91.0% — reported for reference but not used as paper headline.\n\n---\n\n## Table C: b\\* Distribution Statistics (from adaptive_fix, τ=0.8)\n\n| Statistic | seed42 | seed123 | seed456 | Mean | CV |\n|---------------|--------|---------|---------|-------|------|\n| b\\* Mean | 1.399 | 1.431 | 1.416 | 1.415 | 1.1% |\n| b\\* Median | 0.871 | 0.880 | 0.880 | 0.877 | 0.6% |\n| b\\* Std | 1.933 | 2.029 | 1.993 | 1.985 | 2.4% |\n| b\\* P25 | 0.540 | 0.540 | 0.540 | 0.540 | 0.0% |\n| b\\* P75 | 1.512 | 1.520 | 1.520 | 1.517 | 0.3% |\n| % below 0.5 | 20.9% | 20.9% | 20.9% | 20.9% | 0.0% |\n| % above 2.0 | 16.1% | 16.1% | 16.1% | 16.1% | 0.0% |\n\n**Observations**:\n- b\\* distribution is highly stable across seeds (CV < 2.5% for all statistics)\n- Median b\\* ≈ 0.88, reflecting moderate downweighting for most batches\n- Right-skewed: mean (1.415) > median (0.877), driven by ~16% of batches with b\\* > 2.0\n- ~21% of batches receive strong downweighting (b\\* < 0.5)\n\n---\n\n## Table D: Complete Experiment Index\n\n### D.1 — DONE experiments (26 total)\n\n| exp_id | type | seed | b / τ | eval_ppl | status | conclusion |\n|-------------------------------|---------------|------|------------|----------|--------|-------------------------------------|\n| grid_b_seed42_batch | grid_b_sweep | 42 | b=0.5–5.0 | 17.651\\* | DONE | success (\\*best_b=0.5) |\n| grid_b0_5_seed123 | grid_b_sweep | 123 | b=0.5 | 17.638 | DONE | success |\n| grid_b1_0_seed123 | grid_b_sweep | 123 | b=1.0 | 17.674 | DONE | success |\n| grid_b1_5_seed123 | grid_b_sweep | 123 | b=1.5 | 17.701 | DONE | success |\n| grid_b2_0_seed123 | grid_b_sweep | 123 | b=2.0 | 17.725 | DONE | success |\n| grid_b3_0_seed123 | grid_b_sweep | 123 | b=3.0 | 17.760 | DONE | success |\n| grid_b5_0_seed123 | grid_b_sweep | 123 | b=5.0 | 17.804 | DONE | success |\n| grid_b0_5_seed456 | grid_b_sweep | 456 | b=0.5 | 17.650 | DONE | success |\n| grid_b1_0_seed456 | grid_b_sweep | 456 | b=1.0 | 17.680 | DONE | success |\n| grid_b1_5_seed456 | grid_b_sweep | 456 | b=1.5 | 17.710 | DONE | success |\n| grid_b2_0_seed456 | grid_b_sweep | 456 | b=2.0 | 17.989 | DONE | INVALIDATED (D026 checkpoint resume) |\n| grid_b3_0_seed456 | grid_b_sweep | 456 | b=3.0 | 17.921 | DONE | INVALIDATED (D026 checkpoint resume) |\n| grid_b5_0_seed456 | grid_b_sweep | 456 | b=5.0 | 17.993 | DONE | INVALIDATED (D026 checkpoint resume) |\n| grid_b_low_seed42 | grid_b_low | 42 | b=0.1/0.2/0.3 | — | DONE | failed (infra: cron killed process) |\n| uniform_seed42 | uniform | 42 | — | 17.690 | DONE | success |\n| uniform_seed123 | uniform | 123 | — | 17.690 | DONE | success |\n| uniform_seed456 | uniform | 456 | — | 17.700 | DONE | success |\n| adaptive_seed42 | adaptive | 42 | τ=0.8 | 17.690 | DONE | success (n_min=3 bug, superseded) |\n| adaptive_seed123 | adaptive | 123 | τ=0.8 | 17.630 | DONE | success (n_min=3 bug, superseded) |\n| adaptive_seed456 | adaptive | 456 | τ=0.8 | 17.640 | DONE | success (n_min=3 bug, superseded) |\n| adaptive_fix_seed42 | adaptive_fix | 42 | τ=0.8 | 17.650 | DONE | success |\n| adaptive_fix_seed123 | adaptive_fix | 123 | τ=0.8 | 17.643 | DONE | success |\n| adaptive_fix_seed456 | adaptive_fix | 456 | τ=0.8 | 17.660 | DONE | success |\n| datagen_synthetic_4gpu | datagen | — | — | — | DONE | success (340992 docs, 132M tokens) |\n| detector_tfidf_lr | detector | — | — | — | DONE | success (AUC=0.939, ECE_cal=0.048) |\n| diagnostic_contamination100 | diagnostic | — | — | — | DONE | killed (freed GPU for grid-b seed123) |\n\n### D.2 — RUNNING experiments (4 total)\n\n| exp_id | type | seed | params | status |\n|---------------------|-------------------|------|--------------|---------|\n| ess_only_seed42 | ess_only_baseline | 42 | n_min=2 | RUNNING |\n| golden_ratio_seed42 | golden_ratio | 42 | w=1/φ oracle | RUNNING |\n| nmin1_seed42 | n_min_sensitivity | 42 | n_min=1, τ=0.8 | RUNNING |\n| tau_06_seed42 | tau_sweep | 42 | τ=0.6 | RUNNING |\n\n### D.3 — PREPARING / QUEUED experiments (9 total)\n\n| exp_id | type | seed | params | status | conclusion |\n|-----------------------|-----------|------|--------|-----------|------------|\n| adaptive_v2_seed42 | adaptive_v2 | 42 | — | PREPARING | killed |\n| adaptive_v2_seed123 | adaptive_v2 | 123 | — | PREPARING | killed |\n| adaptive_v2_seed456 | adaptive_v2 | 456 | — | PREPARING | killed |\n| tau_0.6_seed42 | tau_sweep | 42 | τ=0.6 | QUEUED | killed (replaced by tau_06_seed42) |\n| detector_modernbert | detector | — | — | QUEUED | success (superseded by TF-IDF) |\n| tau_05_seed42 | tau_sweep | 42 | τ=0.5 | PREPARING | — |\n| tau_07_seed42 | tau_sweep | 42 | τ=0.7 | PREPARING | — |\n| tau_09_seed42 | tau_sweep | 42 | τ=0.9 | PREPARING | — |\n| tau_095_seed42 | tau_sweep | 42 | τ=0.95 | PREPARING | — |\n\n---\n\n## Summary\n\n| Category | Total | Success | Invalidated | Failed | Killed | Running/Pending |\n|------------------|-------|---------|-------------|--------|--------|-----------------|\n| grid_b_sweep | 20 | 15 | 3 | 1 | 0 | 0+1\\*\\* |\n| uniform | 3 | 3 | 0 | 0 | 0 | 0 |\n| adaptive (orig) | 3 | 3 | 0 | 0 | 0 | 0 |\n| adaptive_v2 | 3 | 0 | 0 | 0 | 3 | 0 |\n| adaptive_fix | 3 | 3 | 0 | 0 | 0 | 0 |\n| tau_sweep | 6 | 0 | 0 | 0 | 1 | 1+4 |\n| n_min_sensitivity | 1 | 0 | 0 | 0 | 0 | 1 |\n| ess_only | 1 | 0 | 0 | 0 | 0 | 1 |\n| golden_ratio | 1 | 0 | 0 | 0 | 0 | 1 |\n| datagen | 1 | 1 | 0 | 0 | 0 | 0 |\n| detector | 2 | 2 | 0 | 0 | 0 | 0 |\n| diagnostic | 1 | 0 | 0 | 0 | 1 | 0 |\n| **Total** | **39** | **24\\*** | **3** | **1** | **5** | **4+5** |\n\n\\*\\*grid_b_low_seed42 = failed (infra bug, not re-run).\n\\*24 DONE with conclusion=success (includes 3 invalidated experiments which completed but have unreliable metrics).\n"
  }
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-15T11:11:52.765865+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/full_experiment_data.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_full_experiment_data_table_20260515T110438",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-15T11:11:52.766003+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "full_experiment_data",
  "type": "data",
  "description": "Complete paper-ready experiment data tables: Grid-b sweep (Table A), Method comparison with ratio-of-means (Table B), b* distribution (Table C), and full experiment index (Table D). All 39 experiments indexed.",
  "project": "provenance_weight_training",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/full_experiment_data.md",
  "tags": "['paper', 'data', 'experiment-summary', 'tables']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_full_experiment_data_table_20260515T110438",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "full_experiment_data",
    "type": "data",
    "description": "Complete paper-ready experiment data tables: Grid-b sweep (Table A), Method comparison with ratio-of-means (Table B), b* distribution (Table C), and full experiment index (Table D). All 39 experiments indexed.",
    "project": "provenance_weight_training",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/full_experiment_data.md",
    "tags": "['paper', 'data', 'experiment-summary', 'tables']"
  }
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-15T11:11:52.766155+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260515_1c92c5\", \"name\": \"full_experiment_data\", \"type\": \"data\", \"description\": \"Complete paper-ready experiment data tables: Grid-b sweep (Table A), Method comparison with ratio-of-means (Table B), b* distribution (Table C), and full experiment index (Table D). All 39 experiments indexed.\", \"path\": \"projects/provenance_weight_training/artifacts/_project/data/full_experiment_data.md\", \"url\": null, \"project\": \"provenance_weight_training\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-15T11:11:45.944437+00:00\", \"tags\": [\"paper\", \"data\", \"experiment-summary\", \"tables\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_full_experiment_data_table_20260515T110438",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 67 · 2026-05-15T11:11:52.766320+00:00_

文件已创建并注册：`artifacts/full_experiment_data.md`

内容包含：
- **Table A**: Grid-b sweep 6×3 完整记录，seed456 b≥2.0 标注 INVALIDATED，有效 mean±std 已计算
- **Table B**: Method comparison + ratio-of-means = **89.4%**（区别于 mean-of-ratios 91.0%）
- **Table C**: b* 分布统计含 % below 0.5 (20.9%) 和 % above 2.0 (16.1%)，CV 全部 <2.5%
- **Table D**: 全部 39 个实验索引，按 DONE/RUNNING/PREPARING 分组，含 status、conclusion、PPL

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_full_experiment_data_table_20260515T110438"
}
```

</details>

---
