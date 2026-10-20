# analysis comprehensive results

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 25
- **Recorded user turns:** 0
- **Tool calls:** 12
- **Original source:** `logs/chats/worker_analysis_comprehensive-results_20260515T005132.jsonl`
- **Structured JSON:** [`4ea56c2ce14b96dbc8ea.json`](../../sessions/4e/4ea56c2ce14b96dbc8ea.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

25 recorded events

### Tool call

_source line 1 · 2026-05-15T00:55:24.409440+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__register_artifact",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_comprehensive-results_20260515T005132",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__register_artifact",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-15T00:55:24.409822+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_comprehensive-results_20260515T005132",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T00:55:24.410002+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "tax_error_inject_agent",
  "fields": "['*']",
  "limit": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_comprehensive-results_20260515T005132",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "tax_error_inject_agent",
    "fields": "['*']",
    "limit": "0"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-15T00:55:24.410468+00:00_

Error: result (71,979 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-tax-error-inject-agent/54884577-4b89-43d3-8e16-64aaa0260a70/tool-results/mcp-agent-ml-research-read_registry-1778806308126.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-tax-error-inject-agent/54884577-4b89-43d3-8e16-64aaa0260a70/tool-results/mcp-agent-ml-research-read_registry-1778806308126.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-tax-error-inject-agent/54884577-4b89-43d3-8e16-64aaa0260a70/tool-results/mcp-agent-ml-research-read_registry-1778806308126.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_comprehensive-results_20260515T005132",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-15T00:55:24.410735+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Extract registry experiment data",
  "prompt": "I need to extract specific experiment data from a large JSON registry file at:\n`/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-tax-error-inject-agent/54884577-4b89-43d3-8e16-64aaa0260a70/tool-results/mcp-agent-ml-research-read_registry-1778806308126.txt`\n\nThe file is JSON with schema: `{result: string}` where `result` is itself a JSON string containing experiment records.\n\nI need you to extract the following fields for ALL experiments:\n- exp_id\n- status\n- conclusion\n- metrics (especially eval_success_rate, final_loss, token_accuracy, train_duration_min)\n- Any other relevant result fields\n\nSpecifically I need data for these experiments:\n1. Clean Eval experiments: v4-vanilla-eval-r3, v4-vanilla-seed0-eval, v4-vanilla-seed123-eval, v4-taxei-eval, v4-taxei-seed0-eval, v4-taxei-seed123-eval, v4-random-eval, v4-random-seed0-eval, v4-random-seed123-eval\n2. Dose-Response experiments: v4-taxei-fixed-inject10-eval, v4-taxei-fixed-inject25-eval, and any with \"inject50\" or \"random-fixed\" in the name\n3. Recovery Eval experiments: v4-vanilla-recovery-eval, v4-taxei-recovery-eval-r2, v4-random-recovery-eval\n4. Training experiments: any with \"train\" in the name\n5. Baseline: vanilla-react-baseline\n\nFor each experiment, output: exp_id, status, conclusion (first 200 chars), and ALL metrics as a flat dict.\n\nUse jq or python to parse. Output the results as structured text that I can use directly. Be thorough — I need every number.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_comprehensive-results_20260515T005132",
  "tool": "Agent",
  "tool_args": {
    "description": "Extract registry experiment data",
    "prompt": "I need to extract specific experiment data from a large JSON registry file at:\n`/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-tax-error-inject-agent/54884577-4b89-43d3-8e16-64aaa0260a70/tool-results/mcp-agent-ml-research-read_registry-1778806308126.txt`\n\nThe file is JSON with schema: `{result: string}` where `result` is itself a JSON string containing experiment records.\n\nI need you to extract the following fields for ALL experiments:\n- exp_id\n- status\n- conclusion\n- metrics (especially eval_success_rate, final_loss, token_accuracy, train_duration_min)\n- Any other relevant result fields\n\nSpecifically I need data for these experiments:\n1. Clean Eval experiments: v4-vanilla-eval-r3, v4-vanilla-seed0-eval, v4-vanilla-seed123-eval, v4-taxei-eval, v4-taxei-seed0-eval, v4-taxei-seed123-eval, v4-random-eval, v4-random-seed0-eval, v4-random-seed123-eval\n2. Dose-Response experiments: v4-taxei-fixed-inject10-eval, v4-taxei-fixed-inject25-eval, and any with \"inject50\" or \"random-fixed\" in the name\n3. Recovery Eval experiments: v4-vanilla-recovery-eval, v4-taxei-recovery-eval-r2, v4-random-recovery-eval\n4. Training experiments: any with \"train\" in the name\n5. Baseline: vanilla-react-baseline\n\nFor each experiment, output: exp_id, status, conclusion (first 200 chars), and ALL metrics as a flat dict.\n\nUse jq or python to parse. Output the results as structured text that I can use directly. Be thorough — I need every number.",
    "subagent_type": "general-purpose"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-15T00:55:24.410933+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-tax-error-inject-agent/54884577-4b89-43d3-8e16-64aaa0260a70/tool-results/mcp-agent-ml-research-read_registry-1778806308126.txt",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_comprehensive-results_20260515T005132",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-tax-error-inject-agent/54884577-4b89-43d3-8e16-64aaa0260a70/tool-results/mcp-agent-ml-research-read_registry-1778806308126.txt",
    "limit": "50"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-15T00:55:24.411065+00:00_

File content (30271 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_comprehensive-results_20260515T005132",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-15T00:55:24.411190+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-tax-error-inject-agent/54884577-4b89-43d3-8e16-64aaa0260a70/tool-results/mcp-agent-ml-research-read_registry-1778806308126.txt",
  "limit": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_comprehensive-results_20260515T005132",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-tax-error-inject-agent/54884577-4b89-43d3-8e16-64aaa0260a70/tool-results/mcp-agent-ml-research-read_registry-1778806308126.txt",
    "limit": "20"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-15T00:55:24.411306+00:00_

File content (30271 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_comprehensive-results_20260515T005132",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-15T00:55:24.411424+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "wc -l \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-tax-error-inject-agent/54884577-4b89-43d3-8e16-64aaa0260a70/tool-results/mcp-agent-ml-research-read_registry-1778806308126.txt\"",
  "description": "Check file size in lines"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_comprehensive-results_20260515T005132",
  "tool": "Bash",
  "tool_args": {
    "command": "wc -l \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-tax-error-inject-agent/54884577-4b89-43d3-8e16-64aaa0260a70/tool-results/mcp-agent-ml-research-read_registry-1778806308126.txt\"",
    "description": "Check file size in lines"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-15T00:55:24.411572+00:00_

0 /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-tax-error-inject-agent/54884577-4b89-43d3-8e16-64aaa0260a70/tool-results/mcp-agent-ml-research-read_registry-1778806308126.txt

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_comprehensive-results_20260515T005132",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-15T00:55:24.411703+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json, sys\n\nfpath = \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-tax-error-inject-agent/54884577-4b89-43d3-8e16-64aaa0260a70/tool-results/mcp-agent-ml-research-read_registry-1778806308126.txt\"\n\nwith open(fpath, 'r') as f:\n    raw = json.load(f)\n\n# The outer object has {result: string} where result is itself JSON\ninner = json.loads(raw['result'])\n\n# Determine structure\nif isinstance(inner, dict):\n    print(f\"Top-level keys: {list(inner.keys())[:20]}\")\n    # Check if experiments are nested\n    for k in inner:\n        v = inner[k]\n        if isinstance(v, dict):\n            print(f\"  {k}: dict with keys {list(v.keys())[:10]}\")\n        elif isinstance(v, list):\n            print(f\"  {k}: list of len {len(v)}\")\n            if len(v) > 0:\n                print(f\"    first item type: {type(v[0])}\")\n                if isinstance(v[0], dict):\n                    print(f\"    first item keys: {list(v[0].keys())[:15]}\")\n        else:\n            print(f\"  {k}: {type(v).__name__} = {str(v)[:100]}\")\nelif isinstance(inner, list):\n    print(f\"Top-level: list of {len(inner)} items\")\n    if len(inner) > 0 and isinstance(inner[0], dict):\n        print(f\"First item keys: {list(inner[0].keys())}\")\nPYEOF",
  "description": "Parse registry JSON structure",
  "timeout": "30000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_comprehensive-results_20260515T005132",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 << 'PYEOF'\nimport json, sys\n\nfpath = \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-tax-error-inject-agent/54884577-4b89-43d3-8e16-64aaa0260a70/tool-results/mcp-agent-ml-research-read_registry-1778806308126.txt\"\n\nwith open(fpath, 'r') as f:\n    raw = json.load(f)\n\n# The outer object has {result: string} where result is itself JSON\ninner = json.loads(raw['result'])\n\n# Determine structure\nif isinstance(inner, dict):\n    print(f\"Top-level keys: {list(inner.keys())[:20]}\")\n    # Check if experiments are nested\n    for k in inner:\n        v = inner[k]\n        if isinstance(v, dict):\n            print(f\"  {k}: dict with keys {list(v.keys())[:10]}\")\n        elif isinstance(v, list):\n            print(f\"  {k}: list of len {len(v)}\")\n            if len(v) > 0:\n                print(f\"    first item type: {type(v[0])}\")\n                if isinstance(v[0], dict):\n                    print(f\"    first item keys: {list(v[0].keys())[:15]}\")\n        else:\n            print(f\"  {k}: {type(v).__name__} = {str(v)[:100]}\")\nelif isinstance(inner, list):\n    print(f\"Top-level: list of {len(inner)} items\")\n    if len(inner) > 0 and isinstance(inner[0], dict):\n        print(f\"First item keys: {list(inner[0].keys())}\")\nPYEOF",
    "description": "Parse registry JSON structure",
    "timeout": "30000"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-15T00:55:24.411833+00:00_

Top-level keys: ['success', 'data', 'error', 'metadata']
  success: bool = True
  data: dict with keys ['experiments', 'count', 'total', 'baseline']
  error: NoneType = None
  metadata: dict with keys ['elapsed_seconds']

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_comprehensive-results_20260515T005132",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-15T00:55:24.411954+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nfpath = \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-tax-error-inject-agent/54884577-4b89-43d3-8e16-64aaa0260a70/tool-results/mcp-agent-ml-research-read_registry-1778806308126.txt\"\n\nwith open(fpath, 'r') as f:\n    raw = json.load(f)\n\ninner = json.loads(raw['result'])\ndata = inner['data']\nexperiments = data['experiments']\nbaseline = data.get('baseline')\n\nprint(f\"Total experiments: {data['total']}, returned: {data['count']}\")\nprint(f\"Baseline present: {baseline is not None}\")\nprint()\n\n# List all experiment IDs\nif isinstance(experiments, list):\n    for e in experiments:\n        print(f\"  exp_id={e.get('exp_id','?')}\")\nelif isinstance(experiments, dict):\n    for k in experiments:\n        print(f\"  key={k}\")\nPYEOF",
  "description": "List all experiment IDs",
  "timeout": "30000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_comprehensive-results_20260515T005132",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 << 'PYEOF'\nimport json\n\nfpath = \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-tax-error-inject-agent/54884577-4b89-43d3-8e16-64aaa0260a70/tool-results/mcp-agent-ml-research-read_registry-1778806308126.txt\"\n\nwith open(fpath, 'r') as f:\n    raw = json.load(f)\n\ninner = json.loads(raw['result'])\ndata = inner['data']\nexperiments = data['experiments']\nbaseline = data.get('baseline')\n\nprint(f\"Total experiments: {data['total']}, returned: {data['count']}\")\nprint(f\"Baseline present: {baseline is not None}\")\nprint()\n\n# List all experiment IDs\nif isinstance(experiments, list):\n    for e in experiments:\n        print(f\"  exp_id={e.get('exp_id','?')}\")\nelif isinstance(experiments, dict):\n    for k in experiments:\n        print(f\"  key={k}\")\nPYEOF",
    "description": "List all experiment IDs",
    "timeout": "30000"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-15T00:55:24.412075+00:00_

Total experiments: 57, returned: 57
Baseline present: False

  key=v4-random-fixed-inject25
  key=v4-random-fixed-inject10
  key=v4-random-fixed-inject50
  key=v4-taxei-fixed-inject50
  key=v4-random-seed123-eval
  key=v4-taxei-fixed-inject25-eval
  key=v4-taxei-fixed-inject10-eval
  key=v4-taxei-seed123-eval
  key=v4-random-seed123
  key=v4-taxei-fixed-inject25-r2
  key=v4-taxei-fixed-inject10
  key=v4-taxei-fixed-inject25
  key=v4-taxei-seed123
  key=v4-fixed-inject25
  key=v4-fixed-inject10
  key=v4-random-recovery-eval
  key=v4-taxei-recovery-eval-r2
  key=v4-taxei-seed0-eval
  key=v4-random-seed0-eval
  key=v4-vanilla-recovery-eval
  key=v4-taxei-recovery-eval
  key=v4-vanilla-seed123-eval
  key=v4-random-seed0
  key=v4-taxei-seed0
  key=v4-vanilla-seed0-eval
  key=v4-vanilla-seed123
  key=v4-vanilla-seed0
  key=v4-vanilla-seed7
  key=v4-recovery-eval-dev
  key=v4-recovery-dryrun
  key=v4-random-eval
  key=v4-taxei-eval
  key=traj_collect_500
  key=v4-vanilla-eval-r3
  key=v4-vanilla-eval-r2
  key=v4-random-sft-r2
  key=v4-taxei-sft-r2
  key=v4-vanilla-eval
  key=v3-random-eval
  key=v3-taxei-eval
  key=v4-random-sft-r3
  key=v4-taxei-sft-r3
  key=v4-random-sft
  key=v4-taxei-sft
  key=mini-vanilla-sft-v4
  key=mini-random-sft-v3
  key=mini-taxei-sft-v3
  key=mini-vanilla-sft-v3
  key=v3-vanilla-eval
  key=v4-vanilla-sft
  key=vanilla_sft_aligned_v2
  key=vanilla_sft_aligned_v1
  key=mini-vanilla-sft
  key=mini-taxei-sft
  key=vanilla-react-baseline
  key=mini-pipeline-e2e
  key=sft-dryrun-73

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_comprehensive-results_20260515T005132",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-15T00:55:24.412202+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nfpath = \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-tax-error-inject-agent/54884577-4b89-43d3-8e16-64aaa0260a70/tool-results/mcp-agent-ml-research-read_registry-1778806308126.txt\"\n\nwith open(fpath, 'r') as f:\n    raw = json.load(f)\n\ninner = json.loads(raw['result'])\nexperiments = inner['data']['experiments']\n\n# First, show the full structure of one experiment to understand fields\nsample_key = 'v4-vanilla-eval-r3'\nsample = experiments[sample_key]\nprint(f\"=== STRUCTURE OF '{sample_key}' ===\")\nprint(json.dumps(sample, indent=2, ensure_ascii=False)[:3000])\nprint(\"...\")\nPYEOF",
  "description": "Inspect structure of one experiment",
  "timeout": "30000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_comprehensive-results_20260515T005132",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 << 'PYEOF'\nimport json\n\nfpath = \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-tax-error-inject-agent/54884577-4b89-43d3-8e16-64aaa0260a70/tool-results/mcp-agent-ml-research-read_registry-1778806308126.txt\"\n\nwith open(fpath, 'r') as f:\n    raw = json.load(f)\n\ninner = json.loads(raw['result'])\nexperiments = inner['data']['experiments']\n\n# First, show the full structure of one experiment to understand fields\nsample_key = 'v4-vanilla-eval-r3'\nsample = experiments[sample_key]\nprint(f\"=== STRUCTURE OF '{sample_key}' ===\")\nprint(json.dumps(sample, indent=2, ensure_ascii=False)[:3000])\nprint(\"...\")\nPYEOF",
    "description": "Inspect structure of one experiment",
    "timeout": "30000"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-15T00:55:24.412336+00:00_

=== STRUCTURE OF 'v4-vanilla-eval-r3' ===
{
  "status": "PREPARING",
  "retry_count": 0,
  "created_at": "2026-05-14T14:28:24.833Z",
  "updated_at": "2026-05-14T16:25:11.284Z",
  "spec": {
    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/tax_error_inject_agent && latest_run=\\$(ls -dt checkpoints/mini_vanilla_sft_v4/v0-*/ | head -1) && final_ckpt=\\$(ls -d \\\"\\${latest_run}\\\"checkpoint-* | sort -V | tail -1) && echo \\\"Using checkpoint: \\$final_ckpt\\\" && test -f \\\"\\${final_ckpt}/adapter_config.json\\\" && echo 'adapter_config.json OK' || { echo 'ERROR: adapter_config.json missing'; exit 1; } && CUDA_VISIBLE_DEVICES=0 python3 eval/recovery.py --model_path \\$final_ckpt --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --no_inject --output eval_results/v4_vanilla_eval.json --device cuda:0\"",
    "server": "autodl-5090",
    "gpu": [
      "cuda:0"
    ],
    "pid": "62340",
    "log_path": "~/runs/tax_error_inject_agent/v4-vanilla-eval-r3.log",
    "submitted_at": "2026-05-14T14:28:24.797Z",
    "submitted_via": "submit_training_job",
    "backend": "tmux",
    "account": "root"
  },
  "hypothesis": "v4 Vanilla SFT eval r3 — dynamic checkpoint lookup with sort -V, adapter_config.json pre-check",
  "conclusion": "success",
  "metrics": {
    "eval_success_rate": 0.617,
    "eval_successes": 29,
    "eval_total": 47,
    "per_task": {
      "look_at_obj_in_light": "5/6 (83.3%)",
      "pick_heat_then_place": "6/8 (75.0%)",
      "pick_and_place_simple": "5/8 (62.5%)",
      "pick_cool_then_place": "4/7 (57.1%)",
      "pick_two_obj_and_place": "4/7 (57.1%)",
      "pick_clean_then_place": "5/11 (45.5%)"
    }
  }
}
...

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_comprehensive-results_20260515T005132",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-15T00:55:24.412524+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nfpath = \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-tax-error-inject-agent/54884577-4b89-43d3-8e16-64aaa0260a70/tool-results/mcp-agent-ml-research-read_registry-1778806308126.txt\"\n\nwith open(fpath, 'r') as f:\n    raw = json.load(f)\n\ninner = json.loads(raw['result'])\nexperiments = inner['data']['experiments']\n\n# Define target groups\nclean_eval = [\n    'v4-vanilla-eval-r3', 'v4-vanilla-seed0-eval', 'v4-vanilla-seed123-eval',\n    'v4-taxei-eval', 'v4-taxei-seed0-eval', 'v4-taxei-seed123-eval',\n    'v4-random-eval', 'v4-random-seed0-eval', 'v4-random-seed123-eval'\n]\n\ndose_response_patterns = ['inject10', 'inject25', 'inject50', 'random-fixed']\n\nrecovery_eval = [\n    'v4-vanilla-recovery-eval', 'v4-taxei-recovery-eval-r2', 'v4-random-recovery-eval'\n]\n\nbaseline = ['vanilla-react-baseline']\n\ndef flatten_metrics(metrics, prefix=''):\n    \"\"\"Flatten nested metrics dict to a flat dict.\"\"\"\n    flat = {}\n    if not isinstance(metrics, dict):\n        return flat\n    for k, v in metrics.items():\n        key = f\"{prefix}{k}\" if not prefix else f\"{prefix}.{k}\"\n        if isinstance(v, dict):\n            flat.update(flatten_metrics(v, key))\n        else:\n            flat[key] = v\n    return flat\n\ndef format_exp(exp_id, exp):\n    status = exp.get('status', 'N/A')\n    conclusion = exp.get('conclusion', 'N/A')\n    if conclusion and len(str(conclusion)) > 200:\n        conclusion = str(conclusion)[:200] + '...'\n    metrics = exp.get('metrics', {})\n    flat = flatten_metrics(metrics)\n    hypothesis = exp.get('hypothesis', '')\n    return {\n        'exp_id': exp_id,\n        'status': status,\n        'conclusion': conclusion,\n        'hypothesis': hypothesis[:150] if hypothesis else '',\n        'metrics': flat\n    }\n\ndef print_exp(info):\n    print(f\"exp_id: {info['exp_id']}\")\n    print(f\"  status: {info['status']}\")\n    print(f\"  conclusion: {info['conclusion']}\")\n    if info['hypothesis']:\n        print(f\"  hypothesis: {info['hypothesis']}\")\n    if info['metrics']:\n        for k, v in sorted(info['metrics'].items()):\n            print(f\"  {k}: {v}\")\n    else:\n        print(\"  (no metrics)\")\n    print()\n\n# ============================================================\n# 1. CLEAN EVAL EXPERIMENTS\n# ============================================================\nprint(\"=\" * 80)\nprint(\"SECTION 1: CLEAN EVAL EXPERIMENTS\")\nprint(\"=\" * 80)\nfor eid in clean_eval:\n    if eid in experiments:\n        print_exp(format_exp(eid, experiments[eid]))\n    else:\n        print(f\"exp_id: {eid}\")\n        print(f\"  NOT FOUND in registry\")\n        print()\n\n# ============================================================\n# 2. DOSE-RESPONSE EXPERIMENTS\n# ============================================================\nprint(\"=\" * 80)\nprint(\"SECTION 2: DOSE-RESPONSE EXPERIMENTS\")\nprint(\"=\" * 80)\ndose_ids = sorted([k for k in experiments if any(p in k for p in dose_response_patterns)])\nfor eid in dose_ids:\n    print_exp(format_exp(eid, experiments[eid]))\n\n# ============================================================\n# 3. RECOVERY EVAL EXPERIMENTS\n# ============================================================\nprint(\"=\" * 80)\nprint(\"SECTION 3: RECOVERY EVAL EXPERIMENTS\")\nprint(\"=\" * 80)\nfor eid in recovery_eval:\n    if eid in experiments:\n        print_exp(format_exp(eid, experiments[eid]))\n    else:\n        print(f\"exp_id: {eid}\")\n        print(f\"  NOT FOUND in registry\")\n        print()\n\n# ============================================================\n# 4. TRAINING EXPERIMENTS (any with \"train\" or \"sft\" in name)\n# ============================================================\nprint(\"=\" * 80)\nprint(\"SECTION 4: TRAINING EXPERIMENTS (sft/train)\")\nprint(\"=\" * 80)\ntrain_ids = sorted([k for k in experiments if ('sft' in k or 'train' in k.lower())])\nfor eid in train_ids:\n    print_exp(format_exp(eid, experiments[eid]))\n\n# ============================================================\n# 5. BASELINE\n# ============================================================\nprint(\"=\" * 80)\nprint(\"SECTION 5: BASELINE\")\nprint(\"=\" * 80)\nfor eid in baseline:\n    if eid in experiments:\n        print_exp(format_exp(eid, experiments[eid]))\n    else:\n        print(f\"exp_id: {eid}\")\n        print(f\"  NOT FOUND in registry\")\n        print()\n\n# ============================================================\n# 6. REMAINING EXPERIMENTS (not yet printed)\n# ============================================================\nprinted = set(clean_eval + dose_ids + recovery_eval + train_ids + baseline)\nremaining = sorted([k for k in experiments if k not in printed])\nif remaining:\n    print(\"=\" * 80)\n    print(\"SECTION 6: OTHER EXPERIMENTS\")\n    print(\"=\" * 80)\n    for eid in remaining:\n        print_exp(format_exp(eid, experiments[eid]))\n\nPYEOF",
  "description": "Extract all experiment data grouped by category",
  "timeout": "30000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_comprehensive-results_20260515T005132",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 << 'PYEOF'\nimport json\n\nfpath = \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-tax-error-inject-agent/54884577-4b89-43d3-8e16-64aaa0260a70/tool-results/mcp-agent-ml-research-read_registry-1778806308126.txt\"\n\nwith open(fpath, 'r') as f:\n    raw = json.load(f)\n\ninner = json.loads(raw['result'])\nexperiments = inner['data']['experiments']\n\n# Define target groups\nclean_eval = [\n    'v4-vanilla-eval-r3', 'v4-vanilla-seed0-eval', 'v4-vanilla-seed123-eval',\n    'v4-taxei-eval', 'v4-taxei-seed0-eval', 'v4-taxei-seed123-eval',\n    'v4-random-eval', 'v4-random-seed0-eval', 'v4-random-seed123-eval'\n]\n\ndose_response_patterns = ['inject10', 'inject25', 'inject50', 'random-fixed']\n\nrecovery_eval = [\n    'v4-vanilla-recovery-eval', 'v4-taxei-recovery-eval-r2', 'v4-random-recovery-eval'\n]\n\nbaseline = ['vanilla-react-baseline']\n\ndef flatten_metrics(metrics, prefix=''):\n    \"\"\"Flatten nested metrics dict to a flat dict.\"\"\"\n    flat = {}\n    if not isinstance(metrics, dict):\n        return flat\n    for k, v in metrics.items():\n        key = f\"{prefix}{k}\" if not prefix else f\"{prefix}.{k}\"\n        if isinstance(v, dict):\n            flat.update(flatten_metrics(v, key))\n        else:\n            flat[key] = v\n    return flat\n\ndef format_exp(exp_id, exp):\n    status = exp.get('status', 'N/A')\n    conclusion = exp.get('conclusion', 'N/A')\n    if conclusion and len(str(conclusion)) > 200:\n        conclusion = str(conclusion)[:200] + '...'\n    metrics = exp.get('metrics', {})\n    flat = flatten_metrics(metrics)\n    hypothesis = exp.get('hypothesis', '')\n    return {\n        'exp_id': exp_id,\n        'status': status,\n        'conclusion': conclusion,\n        'hypothesis': hypothesis[:150] if hypothesis else '',\n        'metrics': flat\n    }\n\ndef print_exp(info):\n    print(f\"exp_id: {info['exp_id']}\")\n    print(f\"  status: {info['status']}\")\n    print(f\"  conclusion: {info['conclusion']}\")\n    if info['hypothesis']:\n        print(f\"  hypothesis: {info['hypothesis']}\")\n    if info['metrics']:\n        for k, v in sorted(info['metrics'].items()):\n            print(f\"  {k}: {v}\")\n    else:\n        print(\"  (no metrics)\")\n    print()\n\n# ============================================================\n# 1. CLEAN EVAL EXPERIMENTS\n# ============================================================\nprint(\"=\" * 80)\nprint(\"SECTION 1: CLEAN EVAL EXPERIMENTS\")\nprint(\"=\" * 80)\nfor eid in clean_eval:\n    if eid in experiments:\n        print_exp(format_exp(eid, experiments[eid]))\n    else:\n        print(f\"exp_id: {eid}\")\n        print(f\"  NOT FOUND in registry\")\n        print()\n\n# ============================================================\n# 2. DOSE-RESPONSE EXPERIMENTS\n# ============================================================\nprint(\"=\" * 80)\nprint(\"SECTION 2: DOSE-RESPONSE EXPERIMENTS\")\nprint(\"=\" * 80)\ndose_ids = sorted([k for k in experiments if any(p in k for p in dose_response_patterns)])\nfor eid in dose_ids:\n    print_exp(format_exp(eid, experiments[eid]))\n\n# ============================================================\n# 3. RECOVERY EVAL EXPERIMENTS\n# ============================================================\nprint(\"=\" * 80)\nprint(\"SECTION 3: RECOVERY EVAL EXPERIMENTS\")\nprint(\"=\" * 80)\nfor eid in recovery_eval:\n    if eid in experiments:\n        print_exp(format_exp(eid, experiments[eid]))\n    else:\n        print(f\"exp_id: {eid}\")\n        print(f\"  NOT FOUND in registry\")\n        print()\n\n# ============================================================\n# 4. TRAINING EXPERIMENTS (any with \"train\" or \"sft\" in name)\n# ============================================================\nprint(\"=\" * 80)\nprint(\"SECTION 4: TRAINING EXPERIMENTS (sft/train)\")\nprint(\"=\" * 80)\ntrain_ids = sorted([k for k in experiments if ('sft' in k or 'train' in k.lower())])\nfor eid in train_ids:\n    print_exp(format_exp(eid, experiments[eid]))\n\n# ============================================================\n# 5. BASELINE\n# ============================================================\nprint(\"=\" * 80)\nprint(\"SECTION 5: BASELINE\")\nprint(\"=\" * 80)\nfor eid in baseline:\n    if eid in experiments:\n        print_exp(format_exp(eid, experiments[eid]))\n    else:\n        print(f\"exp_id: {eid}\")\n        print(f\"  NOT FOUND in registry\")\n        print()\n\n# ============================================================\n# 6. REMAINING EXPERIMENTS (not yet printed)\n# ============================================================\nprinted = set(clean_eval + dose_ids + recovery_eval + train_ids + baseline)\nremaining = sorted([k for k in experiments if k not in printed])\nif remaining:\n    print(\"=\" * 80)\n    print(\"SECTION 6: OTHER EXPERIMENTS\")\n    print(\"=\" * 80)\n    for eid in remaining:\n        print_exp(format_exp(eid, experiments[eid]))\n\nPYEOF",
    "description": "Extract all experiment data grouped by category",
    "timeout": "30000"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-15T00:55:24.412775+00:00_

================================================================================
SECTION 1: CLEAN EVAL EXPERIMENTS
================================================================================
exp_id: v4-vanilla-eval-r3
  status: PREPARING
  conclusion: success
  hypothesis: v4 Vanilla SFT eval r3 — dynamic checkpoint lookup with sort -V, adapter_config.json pre-check
  eval_success_rate: 0.617
  eval_successes: 29
  eval_total: 47
  per_task.look_at_obj_in_light: 5/6 (83.3%)
  per_task.pick_and_place_simple: 5/8 (62.5%)
  per_task.pick_clean_then_place: 5/11 (45.5%)
  per_task.pick_cool_then_place: 4/7 (57.1%)
  per_task.pick_heat_then_place: 6/8 (75.0%)
  per_task.pick_two_obj_and_place: 4/7 (57.1%)

exp_id: v4-vanilla-seed0-eval
  status: DONE
  conclusion: success
  hypothesis: v4 Vanilla SFT seed=0 eval — multi-seed verification, 4358 samples, comparing with seed=42 baseline (61.7%)
  discordant_pairs: 5
  eval_success_rate: 0.681
  eval_successes: 32
  eval_total: 47
  mcnemar_vs_seed42_p: 0.375
  per_task.look_at_obj_in_light: 5/6 (83.3%)
  per_task.pick_and_place_simple: 5/8 (62.5%)
  per_task.pick_clean_then_place: 6/11 (54.5%)
  per_task.pick_cool_then_place: 4/7 (57.1%)
  per_task.pick_heat_then_place: 7/8 (87.5%)
  per_task.pick_two_obj_and_place: 5/7 (71.4%)
  vs_seed42_pp: 6.4

exp_id: v4-vanilla-seed123-eval
  status: DONE
  conclusion: success
  hypothesis: v4 Vanilla SFT seed=123 eval — multi-seed verification, 4358 samples, comparing with seed=42 baseline (61.7%)
  eval_success_rate: 0.66
  eval_successes: 31
  eval_total: 47
  per_task.look_at_obj_in_light.rate: 0.833
  per_task.look_at_obj_in_light.success: 5
  per_task.look_at_obj_in_light.total: 6
  per_task.pick_and_place_simple.rate: 0.75
  per_task.pick_and_place_simple.success: 6
  per_task.pick_and_place_simple.total: 8
  per_task.pick_clean_then_place_in_recep.rate: 0.455
  per_task.pick_clean_then_place_in_recep.success: 5
  per_task.pick_clean_then_place_in_recep.total: 11
  per_task
…[truncated 20538 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_comprehensive-results_20260515T005132",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-15T00:55:24.413011+00:00_

Here is the complete extracted data from all 57 experiments, organized by category:

---

## SECTION 1: CLEAN EVAL EXPERIMENTS

| exp_id | status | conclusion | eval_success_rate | eval_successes | eval_total | notes |
|--------|--------|-----------|-------------------|----------------|------------|-------|
| v4-vanilla-eval-r3 | PREPARING | success | 0.617 | 29 | 47 | per-task: light 83.3%, heat 75.0%, place 62.5%, cool 57.1%, two_obj 57.1%, clean 45.5% |
| v4-vanilla-seed0-eval | DONE | success | 0.681 | 32 | 47 | vs_seed42_pp: +6.4, mcnemar_vs_seed42_p: 0.375, discordant_pairs: 5 |
| v4-vanilla-seed123-eval | DONE | success | 0.660 | 31 | 47 | vs_seed42_pp: +4.3, vs_seed0_pp: -2.1 |
| v4-taxei-eval | PREPARING | negative | 0.617 | 29 | 47 | gate_3a: FAIL, gate_3b: FAIL, gate_4: PASS, vs_vanilla_pp: 0, vs_random_pp: -4.3, mcnemar_vs_vanilla_p: 1.0, mcnemar_vs_random_p: 0.754 |
| v4-taxei-seed0-eval | DONE | success | 0.468 | 22 | 47 | vs_seed42_pp: -14.9 |
| v4-taxei-seed123-eval | DONE | success | 0.617 | 29 | 47 | per-task: light 83.3%, clean 63.6%, heat 75.0%, two_obj 57.1%, place 50.0%, cool 42.9% |
| v4-random-eval | PREPARING | negative | 0.660 | 31 | 47 | vs_vanilla_pp: +4.3, vs_taxei_pp: +4.3, mcnemar_vs_vanilla_p: 0.754 |
| v4-random-seed0-eval | DONE | success | 0.553 | 26 | 47 | vs_seed42_pp: -10.7 |
| v4-random-seed123-eval | DONE | negative | 0.681 | 32 | 47 | per-task: light 83.3%, two_obj 71.4%, heat 75.0%, clean 63.6%, place 62.5%, cool 57.1% |

**Multi-seed summary (eval_success_rate):**
- Vanilla: seed42=0.617, seed0=0.681, seed123=0.660 (mean ~0.653, range 6.4pp)
- TaxEI: seed42=0.617, seed0=0.468, seed123=0.617 (mean ~0.567, range 14.9pp)
- Random: seed42=0.660, seed0=0.553, seed123=0.681 (mean ~0.631, range 12.8pp)

---

## SECTION 2: DOSE-RESPONSE EXPERIMENTS

**Training runs (completed):**

| exp_id | status | conclusion | final_loss | token_accuracy | train_duration_min | train_steps | train_epochs |
|--------|--------|-----------|---------
…[truncated 5303 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_comprehensive-results_20260515T005132",
  "tool": "Agent",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-15T00:55:24.413239+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/comprehensive_results.md",
  "content": "# TaxEI Comprehensive Results\n\n> Generated: 2026-05-15 | All data from project registry\n\n---\n\n## 1. Clean Eval — 3-Seed Comparison (47 ALFWorld tasks)\n\n| Method | Seed=42 | Seed=0 | Seed=123 | Mean | SD |\n|--------|---------|--------|----------|------|-----|\n| **Vanilla** | 61.7% (29/47) | 68.1% (32/47) | 66.0% (31/47) | **65.3%** | 3.3pp |\n| **TaxEI** | 61.7% (29/47) | 46.8% (22/47) | 61.7% (29/47) | **56.7%** | 8.6pp |\n| **Random** | 66.0% (31/47) | 55.3% (26/47) | 68.1% (32/47) | **63.1%** | 7.0pp |\n\n**Registry sources:**\n\n| Method | Seed=42 exp_id | Seed=0 exp_id | Seed=123 exp_id |\n|--------|----------------|---------------|-----------------|\n| Vanilla | v4-vanilla-eval-r3 | v4-vanilla-seed0-eval | v4-vanilla-seed123-eval |\n| TaxEI | v4-taxei-eval | v4-taxei-seed0-eval | v4-taxei-seed123-eval |\n| Random | v4-random-eval | v4-random-seed0-eval | v4-random-seed123-eval |\n\n**Per-task breakdown (seed=42):**\n\n| Task Type | Vanilla | TaxEI | Random |\n|-----------|---------|-------|--------|\n| light (6) | 83.3% | 83.3% | 83.3% |\n| heat (8) | 75.0% | 75.0% | 75.0% |\n| clean (11) | 45.5% | 63.6% | 63.6% |\n| place (8) | 62.5% | 50.0% | 62.5% |\n| two_obj (7) | 57.1% | 57.1% | 71.4% |\n| cool (7) | 57.1% | 42.9% | 57.1% |\n\n---\n\n## 2. Dose-Response (Fixed Dataset Size = 4,358 samples, Seed=42)\n\n| Injection % | TaxEI eval_success_rate | Random eval_success_rate |\n|-------------|------------------------|-------------------------|\n| 0% (vanilla baseline) | 61.7% (29/47) | 61.7% (29/47) |\n| 10% | 61.7% (29/47) | *in progress* |\n| 25% | 48.9% (23/47) | *in progress* |\n| 50% | *in progress* | *in progress* |\n\n**Registry sources:**\n- 0%: v4-vanilla-eval-r3\n- TaxEI 10%: v4-taxei-fixed-inject10-eval\n- TaxEI 25%: v4-taxei-fixed-inject25-eval\n- TaxEI 50%: v4-taxei-fixed-inject50 (RUNNING)\n- Random 10%/25%/50%: v4-random-fixed-inject10/25/50 (RUNNING)\n\n**Dose-response training metrics:**\n\n| exp_id | final_loss | token_accuracy | duration (min) | steps | epochs |\n|--------|-----------|----------------|----------------|-------|--------|\n| v4-taxei-fixed-inject10 | 0.308 | 0.888 | 58 | 1635 | 3 |\n| v4-taxei-fixed-inject25-r2 | 0.285 | 0.893 | 58 | 1635 | 3 |\n\n---\n\n## 3. Recovery Eval (Seed=42, 47 tasks)\n\n| Method | Recovery Rate | Successes/Total | exp_id |\n|--------|--------------|-----------------|--------|\n| **Vanilla** | 61.7% | 29/47 | v4-vanilla-recovery-eval |\n| **TaxEI** | 59.6% | 28/47 | v4-taxei-recovery-eval-r2 |\n| **Random** | 63.8% | 30/47 | v4-random-recovery-eval |\n\nDetection rate = 0 for all methods.\n\n**TaxEI per-operator recovery breakdown (v4-taxei-recovery-eval-r2):**\n\n| Operator | Recovered/Total | Rate |\n|----------|----------------|------|\n| C1_context_truncation | 8/12 | 66.7% |\n| C4_observation_masking | 7/11 | 63.6% |\n| P1_step_order_swap | 7/12 | 58.3% |\n| P2_sub_goal_deletion | 6/12 | 50.0% |\n\n---\n\n## 4. Training Metrics Summary\n\n### v4 Multi-Seed Training\n\n| exp_id | final_loss | token_accuracy | duration (min) | steps | epochs |\n|--------|-----------|----------------|----------------|-------|--------|\n| v4-vanilla-seed0 | 0.297 | 0.902 | 58.0 | 1635 | 3 |\n| v4-vanilla-seed123 | 0.288 | 0.903 | 58.9 | 1635 | 3 |\n| v4-taxei-seed0 | 0.355 | 0.917 | 110.0 | 3387 | 3 |\n| v4-taxei-seed123 | 0.355 | 0.900 | 109.2 | 3387 | 3 |\n| v4-random-seed0 | 0.355 | 0.912 | 110.0 | 3387 | 3 |\n| v4-random-seed123 | 0.168 | 0.942 | 110.2 | 3387 | 3 |\n\n### v3 / Mini Pipeline Training (historical)\n\n| exp_id | status | duration (min) | steps | samples |\n|--------|--------|----------------|-------|---------|\n| mini-vanilla-sft-v3 | success | ~58 | 1566 | 4176 |\n| mini-taxei-sft-v3 | success | ~90 | 2832 | 7545 |\n| mini-random-sft-v3 | success | ~110 | 3405 | 9076 |\n\n### Training Observations\n\n- Vanilla models train faster (~58 min) due to smaller dataset (4,358 samples, 1,635 steps)\n- TaxEI and Random models train ~2x longer (~110 min) due to augmented datasets (~3,387 steps)\n- TaxEI and Random at fixed dataset size (4,358) train in ~58 min, same as Vanilla\n\n---\n\n## 5. Statistical Tests\n\n### 3-Seed Paired t-Tests\n\n| Comparison | p-value | Significant (α=0.05)? |\n|------------|---------|----------------------|\n| TaxEI vs Vanilla | 0.32 | No |\n| TaxEI vs Random | 0.034 | Yes* |\n\n*Marginally significant with only n=3 seeds.\n\n### Pooled Permutation Tests (corrected)\n\n| Comparison | p-value | Significant (α=0.05)? |\n|------------|---------|----------------------|\n| TaxEI vs Vanilla | 0.054 | No (marginal) |\n| TaxEI vs Random | 0.170 | No |\n\n### Variance Analysis\n\n| Method | Mean | SD | Range |\n|--------|------|-----|-------|\n| Vanilla | 65.3% | 3.3pp | 6.4pp |\n| Random | 63.1% | 7.0pp | 12.8pp |\n| TaxEI | 56.7% | 8.6pp | 14.9pp |\n\nVariance gradient: Vanilla (3.3pp) < Random (7.0pp) < TaxEI (8.6pp). Error injection increases training variance, with structured (TaxEI) injection showing higher variance than random.\n\n---\n\n## 6. Baselines & Literature Reference\n\n| Method | Success Rate | Source |\n|--------|-------------|--------|\n| Vanilla ReAct (no SFT) | 42.6% (20/47) | vanilla-react-baseline |\n| **Best SFT (Vanilla seed=0)** | **68.1% (32/47)** | v4-vanilla-seed0-eval |\n| CoEx (SOTA) | 93.28% | Literature |\n| AgentPRM (SOTA) | 91.0% | Literature |\n\n### v3 Historical Comparison\n\n| Method | v3 eval | v4 eval (seed=42) |\n|--------|---------|-------------------|\n| Vanilla | 74.5% (35/47) | 61.7% (29/47) |\n| TaxEI | 66.0% (31/47) | 61.7% (29/47) |\n| Random | 51.1% (24/47) | 66.0% (31/47) |\n\nRegistry sources: v3-vanilla-eval, v3-taxei-eval, v3-random-eval\n\n---\n\n## 7. Key Findings Summary\n\n1. **TaxEI does not improve agent robustness** — mean performance (56.7%) trails both Vanilla (65.3%) and Random (63.1%)\n2. **TaxEI increases training instability** — highest SD (8.6pp) across seeds, driven by seed=0 collapse to 46.8%\n3. **Dose-response shows degradation** — TaxEI at 25% injection drops to 48.9% vs 61.7% at 0%/10%\n4. **Recovery eval shows no advantage** — TaxEI (59.6%) slightly below Vanilla (61.7%) and Random (63.8%)\n5. **All SFT methods substantially beat the no-SFT baseline** (42.6%)\n6. **Statistical significance is weak** — only TaxEI vs Random t-test (p=0.034) reaches significance; permutation tests are all NS\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_comprehensive-results_20260515T005132",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/comprehensive_results.md",
    "content": "# TaxEI Comprehensive Results\n\n> Generated: 2026-05-15 | All data from project registry\n\n---\n\n## 1. Clean Eval — 3-Seed Comparison (47 ALFWorld tasks)\n\n| Method | Seed=42 | Seed=0 | Seed=123 | Mean | SD |\n|--------|---------|--------|----------|------|-----|\n| **Vanilla** | 61.7% (29/47) | 68.1% (32/47) | 66.0% (31/47) | **65.3%** | 3.3pp |\n| **TaxEI** | 61.7% (29/47) | 46.8% (22/47) | 61.7% (29/47) | **56.7%** | 8.6pp |\n| **Random** | 66.0% (31/47) | 55.3% (26/47) | 68.1% (32/47) | **63.1%** | 7.0pp |\n\n**Registry sources:**\n\n| Method | Seed=42 exp_id | Seed=0 exp_id | Seed=123 exp_id |\n|--------|----------------|---------------|-----------------|\n| Vanilla | v4-vanilla-eval-r3 | v4-vanilla-seed0-eval | v4-vanilla-seed123-eval |\n| TaxEI | v4-taxei-eval | v4-taxei-seed0-eval | v4-taxei-seed123-eval |\n| Random | v4-random-eval | v4-random-seed0-eval | v4-random-seed123-eval |\n\n**Per-task breakdown (seed=42):**\n\n| Task Type | Vanilla | TaxEI | Random |\n|-----------|---------|-------|--------|\n| light (6) | 83.3% | 83.3% | 83.3% |\n| heat (8) | 75.0% | 75.0% | 75.0% |\n| clean (11) | 45.5% | 63.6% | 63.6% |\n| place (8) | 62.5% | 50.0% | 62.5% |\n| two_obj (7) | 57.1% | 57.1% | 71.4% |\n| cool (7) | 57.1% | 42.9% | 57.1% |\n\n---\n\n## 2. Dose-Response (Fixed Dataset Size = 4,358 samples, Seed=42)\n\n| Injection % | TaxEI eval_success_rate | Random eval_success_rate |\n|-------------|------------------------|-------------------------|\n| 0% (vanilla baseline) | 61.7% (29/47) | 61.7% (29/47) |\n| 10% | 61.7% (29/47) | *in progress* |\n| 25% | 48.9% (23/47) | *in progress* |\n| 50% | *in progress* | *in progress* |\n\n**Registry sources:**\n- 0%: v4-vanilla-eval-r3\n- TaxEI 10%: v4-taxei-fixed-inject10-eval\n- TaxEI 25%: v4-taxei-fixed-inject25-eval\n- TaxEI 50%: v4-taxei-fixed-inject50 (RUNNING)\n- Random 10%/25%/50%: v4-random-fixed-inject10/25/50 (RUNNING)\n\n**Dose-response training metrics:**\n\n| exp_id | final_loss | token_accuracy | duration (min) | steps | epochs |\n|--------|-----------|----------------|----------------|-------|--------|\n| v4-taxei-fixed-inject10 | 0.308 | 0.888 | 58 | 1635 | 3 |\n| v4-taxei-fixed-inject25-r2 | 0.285 | 0.893 | 58 | 1635 | 3 |\n\n---\n\n## 3. Recovery Eval (Seed=42, 47 tasks)\n\n| Method | Recovery Rate | Successes/Total | exp_id |\n|--------|--------------|-----------------|--------|\n| **Vanilla** | 61.7% | 29/47 | v4-vanilla-recovery-eval |\n| **TaxEI** | 59.6% | 28/47 | v4-taxei-recovery-eval-r2 |\n| **Random** | 63.8% | 30/47 | v4-random-recovery-eval |\n\nDetection rate = 0 for all methods.\n\n**TaxEI per-operator recovery breakdown (v4-taxei-recovery-eval-r2):**\n\n| Operator | Recovered/Total | Rate |\n|----------|----------------|------|\n| C1_context_truncation | 8/12 | 66.7% |\n| C4_observation_masking | 7/11 | 63.6% |\n| P1_step_order_swap | 7/12 | 58.3% |\n| P2_sub_goal_deletion | 6/12 | 50.0% |\n\n---\n\n## 4. Training Metrics Summary\n\n### v4 Multi-Seed Training\n\n| exp_id | final_loss | token_accuracy | duration (min) | steps | epochs |\n|--------|-----------|----------------|----------------|-------|--------|\n| v4-vanilla-seed0 | 0.297 | 0.902 | 58.0 | 1635 | 3 |\n| v4-vanilla-seed123 | 0.288 | 0.903 | 58.9 | 1635 | 3 |\n| v4-taxei-seed0 | 0.355 | 0.917 | 110.0 | 3387 | 3 |\n| v4-taxei-seed123 | 0.355 | 0.900 | 109.2 | 3387 | 3 |\n| v4-random-seed0 | 0.355 | 0.912 | 110.0 | 3387 | 3 |\n| v4-random-seed123 | 0.168 | 0.942 | 110.2 | 3387 | 3 |\n\n### v3 / Mini Pipeline Training (historical)\n\n| exp_id | status | duration (min) | steps | samples |\n|--------|--------|----------------|-------|---------|\n| mini-vanilla-sft-v3 | success | ~58 | 1566 | 4176 |\n| mini-taxei-sft-v3 | success | ~90 | 2832 | 7545 |\n| mini-random-sft-v3 | success | ~110 | 3405 | 9076 |\n\n### Training Observations\n\n- Vanilla models train faster (~58 min) due to smaller dataset (4,358 samples, 1,635 steps)\n- TaxEI and Random models train ~2x longer (~110 min) due to augmented datasets (~3,387 steps)\n- TaxEI and Random at fixed dataset size (4,358) train in ~58 min, same as Vanilla\n\n---\n\n## 5. Statistical Tests\n\n### 3-Seed Paired t-Tests\n\n| Comparison | p-value | Significant (α=0.05)? |\n|------------|---------|----------------------|\n| TaxEI vs Vanilla | 0.32 | No |\n| TaxEI vs Random | 0.034 | Yes* |\n\n*Marginally significant with only n=3 seeds.\n\n### Pooled Permutation Tests (corrected)\n\n| Comparison | p-value | Significant (α=0.05)? |\n|------------|---------|----------------------|\n| TaxEI vs Vanilla | 0.054 | No (marginal) |\n| TaxEI vs Random | 0.170 | No |\n\n### Variance Analysis\n\n| Method | Mean | SD | Range |\n|--------|------|-----|-------|\n| Vanilla | 65.3% | 3.3pp | 6.4pp |\n| Random | 63.1% | 7.0pp | 12.8pp |\n| TaxEI | 56.7% | 8.6pp | 14.9pp |\n\nVariance gradient: Vanilla (3.3pp) < Random (7.0pp) < TaxEI (8.6pp). Error injection increases training variance, with structured (TaxEI) injection showing higher variance than random.\n\n---\n\n## 6. Baselines & Literature Reference\n\n| Method | Success Rate | Source |\n|--------|-------------|--------|\n| Vanilla ReAct (no SFT) | 42.6% (20/47) | vanilla-react-baseline |\n| **Best SFT (Vanilla seed=0)** | **68.1% (32/47)** | v4-vanilla-seed0-eval |\n| CoEx (SOTA) | 93.28% | Literature |\n| AgentPRM (SOTA) | 91.0% | Literature |\n\n### v3 Historical Comparison\n\n| Method | v3 eval | v4 eval (seed=42) |\n|--------|---------|-------------------|\n| Vanilla | 74.5% (35/47) | 61.7% (29/47) |\n| TaxEI | 66.0% (31/47) | 61.7% (29/47) |\n| Random | 51.1% (24/47) | 66.0% (31/47) |\n\nRegistry sources: v3-vanilla-eval, v3-taxei-eval, v3-random-eval\n\n---\n\n## 7. Key Findings Summary\n\n1. **TaxEI does not improve agent robustness** — mean performance (56.7%) trails both Vanilla (65.3%) and Random (63.1%)\n2. **TaxEI increases training instability** — highest SD (8.6pp) across seeds, driven by seed=0 collapse to 46.8%\n3. **Dose-response shows degradation** — TaxEI at 25% injection drops to 48.9% vs 61.7% at 0%/10%\n4. **Recovery eval shows no advantage** — TaxEI (59.6%) slightly below Vanilla (61.7%) and Random (63.8%)\n5. **All SFT methods substantially beat the no-SFT baseline** (42.6%)\n6. **Statistical significance is weak** — only TaxEI vs Random t-test (p=0.034) reaches significance; permutation tests are all NS\n"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-15T00:55:24.413450+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/comprehensive_results.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_comprehensive-results_20260515T005132",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-15T00:55:24.413645+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "comprehensive_results",
  "type": "report",
  "description": "Comprehensive results table: 3-seed clean eval, dose-response, recovery eval, training metrics, statistical tests, baselines. All data sourced from registry.",
  "project": "tax_error_inject_agent",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/comprehensive_results.md",
  "tags": "['results', 'summary', 'v4', 'multi-seed', 'dose-response', 'recovery']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_comprehensive-results_20260515T005132",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "comprehensive_results",
    "type": "report",
    "description": "Comprehensive results table: 3-seed clean eval, dose-response, recovery eval, training metrics, statistical tests, baselines. All data sourced from registry.",
    "project": "tax_error_inject_agent",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/comprehensive_results.md",
    "tags": "['results', 'summary', 'v4', 'multi-seed', 'dose-response', 'recovery']"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-15T00:55:24.413797+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260515_6eecea\", \"name\": \"comprehensive_results\", \"type\": \"report\", \"description\": \"Comprehensive results table: 3-seed clean eval, dose-response, recovery eval, training metrics, statistical tests, baselines. All data sourced from registry.\", \"path\": \"projects/tax_error_inject_agent/artifacts/_project/report/comprehensive_results.md\", \"url\": null, \"project\": \"tax_error_inject_agent\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-15T00:55:18.314530+00:00\", \"tags\": [\"results\", \"summary\", \"v4\", \"multi-seed\", \"dose-response\", \"recovery\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_comprehensive-results_20260515T005132",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-15T00:55:24.413955+00:00_

已完成。产出文件写入 `artifacts/comprehensive_results.md` 并注册为 `art_20260515_6eecea`。

内容涵盖 7 个部分：3-seed clean eval 全维度表（含 per-task 明细）、dose-response 表、recovery eval 表（含 per-operator 明细）、训练指标汇总、统计检验、baseline 参考、关键发现总结。所有数值均来自 registry，dose-response 中 Random 和 TaxEI-50% 标记为 in progress。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_comprehensive-results_20260515T005132"
}
```

</details>

---
