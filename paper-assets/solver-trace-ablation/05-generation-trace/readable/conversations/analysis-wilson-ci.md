# analysis wilson ci

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 57
- **Recorded user turns:** 0
- **Tool calls:** 28
- **Original source:** `logs/chats/worker_analysis_wilson-ci_20260515T075227.jsonl`
- **Structured JSON:** [`647f46b15eeb0a32efe2.json`](../../sessions/64/647f46b15eeb0a32efe2.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

57 recorded events

### Tool call

_source line 1 · 2026-05-15T07:59:05.932615+00:00_

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
  "session": "worker_analysis_wilson-ci_20260515T075227",
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

_source line 2 · 2026-05-15T07:59:05.933005+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_wilson-ci_20260515T075227",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T07:59:05.933186+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "solver-trace-ablation",
  "limit": "0",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_wilson-ci_20260515T075227",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "solver-trace-ablation",
    "limit": "0",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-15T07:59:05.933893+00:00_

Error: result (146,227 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/d80fed44-dadc-4e6f-9333-1a32a5430a13/tool-results/mcp-agent-ml-research-read_registry-1778831563449.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/d80fed44-dadc-4e6f-9333-1a32a5430a13/tool-results/mcp-agent-ml-research-read_registry-1778831563449.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/d80fed44-dadc-4e6f-9333-1a32a5430a13/tool-results/mcp-agent-ml-research-read_registry-1778831563449.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_wilson-ci_20260515T075227",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-15T07:59:05.934135+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Extract registry classification data",
  "prompt": "I need to extract experiment classification data from a registry JSON file. The file is at:\n/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/d80fed44-dadc-4e6f-9333-1a32a5430a13/tool-results/mcp-agent-ml-research-read_registry-1778831563449.txt\n\nThe file has schema: {result: string} where result is a JSON string that needs to be parsed.\n\nI need you to extract the following for every experiment that has classification data:\n- experiment name/ID\n- condition (exec-only, ISR β=0.1, Random β=0.1, ISR β=0.3, Random β=0.3, SFT, etc.)\n- seed (s42, s43, s44)\n- n_proved (could be called eval_n_proved or n_proved)\n- h7_count, h1_count, genuine_count (genuine might be called non_hacking_count)\n- Any rates if available (h7_rate, h1_rate, genuine_rate, non_hacking_rate)\n\nThe key experiments I need:\n- exec-only: s42, s43, s44\n- ISR β=0.1: s42, s43, s44\n- ISR β=0.3: s42, s43, s44\n- Random β=0.1: s42, s43, s44\n- Random β=0.3: s42, s43, s44\n- SFT: s42\n\nUse Python to parse the JSON and extract this data. Write the extracted data as a clean JSON file to:\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/registry_extract.json\n\nThe output JSON should be a list of dicts, each with keys: experiment_id, condition, seed, n_proved, h7_count, h1_count, genuine_count, h7_rate, h1_rate, genuine_rate\n\nFor any missing fields, use null. Include ALL experiments that have any classification data, not just the ones I listed above. Also print out the extracted data so I can see it.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_wilson-ci_20260515T075227",
  "tool": "Agent",
  "tool_args": {
    "description": "Extract registry classification data",
    "prompt": "I need to extract experiment classification data from a registry JSON file. The file is at:\n/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/d80fed44-dadc-4e6f-9333-1a32a5430a13/tool-results/mcp-agent-ml-research-read_registry-1778831563449.txt\n\nThe file has schema: {result: string} where result is a JSON string that needs to be parsed.\n\nI need you to extract the following for every experiment that has classification data:\n- experiment name/ID\n- condition (exec-only, ISR β=0.1, Random β=0.1, ISR β=0.3, Random β=0.3, SFT, etc.)\n- seed (s42, s43, s44)\n- n_proved (could be called eval_n_proved or n_proved)\n- h7_count, h1_count, genuine_count (genuine might be called non_hacking_count)\n- Any rates if available (h7_rate, h1_rate, genuine_rate, non_hacking_rate)\n\nThe key experiments I need:\n- exec-only: s42, s43, s44\n- ISR β=0.1: s42, s43, s44\n- ISR β=0.3: s42, s43, s44\n- Random β=0.1: s42, s43, s44\n- Random β=0.3: s42, s43, s44\n- SFT: s42\n\nUse Python to parse the JSON and extract this data. Write the extracted data as a clean JSON file to:\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/registry_extract.json\n\nThe output JSON should be a list of dicts, each with keys: experiment_id, condition, seed, n_proved, h7_count, h1_count, genuine_count, h7_rate, h1_rate, genuine_rate\n\nFor any missing fields, use null. Include ALL experiments that have any classification data, not just the ones I listed above. Also print out the extracted data so I can see it.",
    "subagent_type": "general-purpose"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-15T07:59:05.934339+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/d80fed44-dadc-4e6f-9333-1a32a5430a13/tool-results/mcp-agent-ml-research-read_registry-1778831563449.txt",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_wilson-ci_20260515T075227",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/d80fed44-dadc-4e6f-9333-1a32a5430a13/tool-results/mcp-agent-ml-research-read_registry-1778831563449.txt",
    "limit": "100"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-15T07:59:05.934475+00:00_

File content (63034 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_wilson-ci_20260515T075227",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-15T07:59:05.934605+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/d80fed44-dadc-4e6f-9333-1a32a5430a13/tool-results/mcp-agent-ml-research-read_registry-1778831563449.txt",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_wilson-ci_20260515T075227",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/d80fed44-dadc-4e6f-9333-1a32a5430a13/tool-results/mcp-agent-ml-research-read_registry-1778831563449.txt",
    "limit": "50"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-15T07:59:05.934779+00:00_

File content (63034 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_wilson-ci_20260515T075227",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-15T07:59:05.934967+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "wc -l /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/d80fed44-dadc-4e6f-9333-1a32a5430a13/tool-results/mcp-agent-ml-research-read_registry-1778831563449.txt",
  "description": "Check file line count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_wilson-ci_20260515T075227",
  "tool": "Bash",
  "tool_args": {
    "command": "wc -l /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/d80fed44-dadc-4e6f-9333-1a32a5430a13/tool-results/mcp-agent-ml-research-read_registry-1778831563449.txt",
    "description": "Check file line count"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-15T07:59:05.935090+00:00_

0 /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/d80fed44-dadc-4e6f-9333-1a32a5430a13/tool-results/mcp-agent-ml-research-read_registry-1778831563449.txt

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_wilson-ci_20260515T075227",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-15T07:59:05.935216+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nfpath = \"/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/d80fed44-dadc-4e6f-9333-1a32a5430a13/tool-results/mcp-agent-ml-research-read_registry-1778831563449.txt\"\n\nwith open(fpath, 'r') as f:\n    raw = f.read()\n\n# Parse the outer JSON\nouter = json.loads(raw)\n# The result field is a JSON string\nregistry = json.loads(outer['result'])\n\n# Show top-level keys\nif isinstance(registry, dict):\n    print(\"Type: dict\")\n    print(\"Top-level keys:\", list(registry.keys())[:20])\n    print(\"Total keys:\", len(registry.keys()))\nelif isinstance(registry, list):\n    print(\"Type: list\")\n    print(\"Length:\", len(registry))\n    if len(registry) > 0:\n        print(\"First item keys:\", list(registry[0].keys()) if isinstance(registry[0], dict) else type(registry[0]))\nPYEOF\n",
  "description": "Parse outer JSON structure of registry file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_wilson-ci_20260515T075227",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 << 'PYEOF'\nimport json\n\nfpath = \"/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/d80fed44-dadc-4e6f-9333-1a32a5430a13/tool-results/mcp-agent-ml-research-read_registry-1778831563449.txt\"\n\nwith open(fpath, 'r') as f:\n    raw = f.read()\n\n# Parse the outer JSON\nouter = json.loads(raw)\n# The result field is a JSON string\nregistry = json.loads(outer['result'])\n\n# Show top-level keys\nif isinstance(registry, dict):\n    print(\"Type: dict\")\n    print(\"Top-level keys:\", list(registry.keys())[:20])\n    print(\"Total keys:\", len(registry.keys()))\nelif isinstance(registry, list):\n    print(\"Type: list\")\n    print(\"Length:\", len(registry))\n    if len(registry) > 0:\n        print(\"First item keys:\", list(registry[0].keys()) if isinstance(registry[0], dict) else type(registry[0]))\nPYEOF\n",
    "description": "Parse outer JSON structure of registry file"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-15T07:59:05.935346+00:00_

Type: dict
Top-level keys: ['success', 'data', 'error', 'metadata']
Total keys: 4

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_wilson-ci_20260515T075227",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-15T07:59:05.935481+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nfpath = \"/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/d80fed44-dadc-4e6f-9333-1a32a5430a13/tool-results/mcp-agent-ml-research-read_registry-1778831563449.txt\"\n\nwith open(fpath, 'r') as f:\n    raw = f.read()\n\nouter = json.loads(raw)\nregistry = json.loads(outer['result'])\n\ndata = registry['data']\nprint(\"data type:\", type(data))\nif isinstance(data, dict):\n    print(\"data keys:\", list(data.keys())[:30])\n    print(\"total entries:\", len(data))\nelif isinstance(data, list):\n    print(\"data length:\", len(data))\n    if len(data) > 0:\n        print(\"first item type:\", type(data[0]))\n        if isinstance(data[0], dict):\n            print(\"first item keys:\", list(data[0].keys()))\nPYEOF\n",
  "description": "Explore registry data structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_wilson-ci_20260515T075227",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 << 'PYEOF'\nimport json\n\nfpath = \"/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/d80fed44-dadc-4e6f-9333-1a32a5430a13/tool-results/mcp-agent-ml-research-read_registry-1778831563449.txt\"\n\nwith open(fpath, 'r') as f:\n    raw = f.read()\n\nouter = json.loads(raw)\nregistry = json.loads(outer['result'])\n\ndata = registry['data']\nprint(\"data type:\", type(data))\nif isinstance(data, dict):\n    print(\"data keys:\", list(data.keys())[:30])\n    print(\"total entries:\", len(data))\nelif isinstance(data, list):\n    print(\"data length:\", len(data))\n    if len(data) > 0:\n        print(\"first item type:\", type(data[0]))\n        if isinstance(data[0], dict):\n            print(\"first item keys:\", list(data[0].keys()))\nPYEOF\n",
    "description": "Explore registry data structure"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-15T07:59:05.935600+00:00_

data type: &lt;class 'dict'>
data keys: ['experiments', 'count', 'total', 'baseline']
total entries: 4

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_wilson-ci_20260515T075227",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-15T07:59:05.935746+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nfpath = \"/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/d80fed44-dadc-4e6f-9333-1a32a5430a13/tool-results/mcp-agent-ml-research-read_registry-1778831563449.txt\"\n\nwith open(fpath, 'r') as f:\n    raw = f.read()\n\nouter = json.loads(raw)\nregistry = json.loads(outer['result'])\n\nexperiments = registry['data']['experiments']\nprint(\"experiments type:\", type(experiments))\nif isinstance(experiments, list):\n    print(\"Number of experiments:\", len(experiments))\n    for i, exp in enumerate(experiments):\n        if isinstance(exp, dict):\n            print(f\"\\n--- Experiment {i} ---\")\n            print(\"Keys:\", list(exp.keys()))\n            # Print id/name/condition fields\n            for k in ['id', 'name', 'experiment_id', 'condition', 'seed', 'status']:\n                if k in exp:\n                    print(f\"  {k}: {exp[k]}\")\nelif isinstance(experiments, dict):\n    print(\"Number of experiments:\", len(experiments))\n    for k in list(experiments.keys())[:5]:\n        print(f\"\\n--- {k} ---\")\n        v = experiments[k]\n        if isinstance(v, dict):\n            print(\"Keys:\", list(v.keys()))\nPYEOF\n",
  "description": "Explore experiments structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_wilson-ci_20260515T075227",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 << 'PYEOF'\nimport json\n\nfpath = \"/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/d80fed44-dadc-4e6f-9333-1a32a5430a13/tool-results/mcp-agent-ml-research-read_registry-1778831563449.txt\"\n\nwith open(fpath, 'r') as f:\n    raw = f.read()\n\nouter = json.loads(raw)\nregistry = json.loads(outer['result'])\n\nexperiments = registry['data']['experiments']\nprint(\"experiments type:\", type(experiments))\nif isinstance(experiments, list):\n    print(\"Number of experiments:\", len(experiments))\n    for i, exp in enumerate(experiments):\n        if isinstance(exp, dict):\n            print(f\"\\n--- Experiment {i} ---\")\n            print(\"Keys:\", list(exp.keys()))\n            # Print id/name/condition fields\n            for k in ['id', 'name', 'experiment_id', 'condition', 'seed', 'status']:\n                if k in exp:\n                    print(f\"  {k}: {exp[k]}\")\nelif isinstance(experiments, dict):\n    print(\"Number of experiments:\", len(experiments))\n    for k in list(experiments.keys())[:5]:\n        print(f\"\\n--- {k} ---\")\n        v = experiments[k]\n        if isinstance(v, dict):\n            print(\"Keys:\", list(v.keys()))\nPYEOF\n",
    "description": "Explore experiments structure"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-15T07:59:05.935882+00:00_

experiments type: &lt;class 'dict'>
Number of experiments: 70

--- plan009-sft-baseline-s43 ---
Keys: ['status', 'retry_count', 'created_at', 'updated_at', 'spec', 'server', 'gpu', 'account', 'pid', 'log_path', 'reproduce', 'extra', 'checkpoint_path', 'metrics', 'conclusion', 'completed_at']

--- plan004-o1-ablation-s42 ---
Keys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'server', 'gpu', 'account', 'reproduce', 'spec', 'metrics', 'conclusion', 'notes', 'checkpoint_path', 'log_path', 'completed_at']

--- plan009-sft-baseline-s44 ---
Keys: ['status', 'retry_count', 'created_at', 'updated_at', 'spec']

--- plan002-additive-b01-s42-1000 ---
Keys: ['status', 'retry_count', 'created_at', 'updated_at', 'spec', 'server', 'gpu', 'account', 'pid', 'log_path', 'reproduce']

--- plan018-additive-random-b01-s42-1000 ---
Keys: ['status', 'retry_count', 'created_at', 'updated_at', 'spec']

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_wilson-ci_20260515T075227",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-15T07:59:05.936011+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nfpath = \"/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/d80fed44-dadc-4e6f-9333-1a32a5430a13/tool-results/mcp-agent-ml-research-read_registry-1778831563449.txt\"\n\nwith open(fpath, 'r') as f:\n    raw = f.read()\n\nouter = json.loads(raw)\nregistry = json.loads(outer['result'])\nexperiments = registry['data']['experiments']\n\n# Look at all experiment keys\nprint(\"All experiment IDs:\")\nfor k in sorted(experiments.keys()):\n    exp = experiments[k]\n    status = exp.get('status', '?')\n    has_metrics = 'metrics' in exp and exp['metrics']\n    has_conclusion = 'conclusion' in exp and exp['conclusion']\n    print(f\"  {k:50s} status={status:12s} metrics={'Y' if has_metrics else 'N'} conclusion={'Y' if has_conclusion else 'N'}\")\nPYEOF\n",
  "description": "List all experiment IDs with status"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_wilson-ci_20260515T075227",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 << 'PYEOF'\nimport json\n\nfpath = \"/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/d80fed44-dadc-4e6f-9333-1a32a5430a13/tool-results/mcp-agent-ml-research-read_registry-1778831563449.txt\"\n\nwith open(fpath, 'r') as f:\n    raw = f.read()\n\nouter = json.loads(raw)\nregistry = json.loads(outer['result'])\nexperiments = registry['data']['experiments']\n\n# Look at all experiment keys\nprint(\"All experiment IDs:\")\nfor k in sorted(experiments.keys()):\n    exp = experiments[k]\n    status = exp.get('status', '?')\n    has_metrics = 'metrics' in exp and exp['metrics']\n    has_conclusion = 'conclusion' in exp and exp['conclusion']\n    print(f\"  {k:50s} status={status:12s} metrics={'Y' if has_metrics else 'N'} conclusion={'Y' if has_conclusion else 'N'}\")\nPYEOF\n",
    "description": "List all experiment IDs with status"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-15T07:59:05.936157+00:00_

All experiment IDs:
  exp1-isr-b03-s43                                   status=DONE         metrics=Y conclusion=Y
  exp1-isr-b03-s43-r2                                status=DONE         metrics=N conclusion=Y
  exp1-isr-b03-s43-r3                                status=DONE         metrics=Y conclusion=Y
  exp1-isr-b03-s43-r4                                status=DONE         metrics=N conclusion=Y
  exp1-isr-b03-s44                                   status=DONE         metrics=N conclusion=Y
  exp1-isr-b03-s44-r2                                status=DONE         metrics=Y conclusion=Y
  exp1-random-b03-s43                                status=DONE         metrics=Y conclusion=Y
  exp1-random-b03-s43-r2                             status=DONE         metrics=N conclusion=Y
  exp1-random-b03-s43-r3                             status=DONE         metrics=N conclusion=Y
  exp1-random-b03-s43-r4                             status=DONE         metrics=Y conclusion=Y
  exp1-random-b03-s44                                status=DONE         metrics=N conclusion=Y
  exp1-random-b03-s44-r2                             status=DONE         metrics=Y conclusion=Y
  exp2-exec-s43-greedy                               status=DONE         metrics=N conclusion=Y
  exp4-100step-h1h7                                  status=DONE         metrics=N conclusion=Y
  plan001-exec-only-s42                              status=DONE         metrics=N conclusion=Y
  plan001-exec-only-s42-r2                           status=DONE         metrics=Y conclusion=Y
  plan001-exec-only-s42-r3                           status=DONE         metrics=N conclusion=Y
  plan001-exec-only-s43                              status=DONE         metrics=N conclusion=Y
  plan001-exec-only-s43-r2                           status=DONE         metrics=N conclusion=Y
  plan001-exec-only-s43-r3                           status=DONE         metrics=N conclusion=Y
  plan001-exec-only-s43-r4                           status=
…[truncated 4739 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_wilson-ci_20260515T075227",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-15T07:59:05.936310+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nfpath = \"/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/d80fed44-dadc-4e6f-9333-1a32a5430a13/tool-results/mcp-agent-ml-research-read_registry-1778831563449.txt\"\n\nwith open(fpath, 'r') as f:\n    raw = f.read()\n\nouter = json.loads(raw)\nregistry = json.loads(outer['result'])\nexperiments = registry['data']['experiments']\n\n# Look for classification-related fields in metrics and conclusion\nclassification_keys = ['h7_count', 'h1_count', 'genuine_count', 'non_hacking_count', \n                       'h7_rate', 'h1_rate', 'genuine_rate', 'non_hacking_rate',\n                       'n_proved', 'eval_n_proved', 'classification', 'hacking']\n\nfor exp_id in sorted(experiments.keys()):\n    exp = experiments[exp_id]\n    \n    # Check metrics\n    metrics = exp.get('metrics', {})\n    conclusion = exp.get('conclusion', {})\n    extra = exp.get('extra', {})\n    \n    # Search recursively for classification keys\n    def find_keys(obj, prefix=\"\"):\n        found = {}\n        if isinstance(obj, dict):\n            for k, v in obj.items():\n                full_key = f\"{prefix}.{k}\" if prefix else k\n                if any(ck in k.lower() for ck in ['h7', 'h1', 'genuine', 'hacking', 'proved', 'classify', 'classification']):\n                    found[full_key] = v\n                if isinstance(v, (dict, list)):\n                    found.update(find_keys(v, full_key))\n        elif isinstance(obj, list):\n            for i, item in enumerate(obj):\n                found.update(find_keys(item, f\"{prefix}[{i}]\"))\n        return found\n    \n    all_found = {}\n    for section_name, section_data in [('metrics', metrics), ('conclusion', conclusion), ('extra', extra)]:\n        if section_data:\n            results = find_keys(section_data, section_name)\n            all_found.update(results)\n    \n    if all_found:\n        print(f\"\\n=== {exp_id} ===\")\n        for k, v in all_found.items():\n            # Truncate long values\n            sv = str(v)\n            if len(sv) > 200:\n                sv = sv[:200] + \"...\"\n            print(f\"  {k}: {sv}\")\nPYEOF\n",
  "description": "Search for classification-related fields across all experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_wilson-ci_20260515T075227",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 << 'PYEOF'\nimport json\n\nfpath = \"/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/d80fed44-dadc-4e6f-9333-1a32a5430a13/tool-results/mcp-agent-ml-research-read_registry-1778831563449.txt\"\n\nwith open(fpath, 'r') as f:\n    raw = f.read()\n\nouter = json.loads(raw)\nregistry = json.loads(outer['result'])\nexperiments = registry['data']['experiments']\n\n# Look for classification-related fields in metrics and conclusion\nclassification_keys = ['h7_count', 'h1_count', 'genuine_count', 'non_hacking_count', \n                       'h7_rate', 'h1_rate', 'genuine_rate', 'non_hacking_rate',\n                       'n_proved', 'eval_n_proved', 'classification', 'hacking']\n\nfor exp_id in sorted(experiments.keys()):\n    exp = experiments[exp_id]\n    \n    # Check metrics\n    metrics = exp.get('metrics', {})\n    conclusion = exp.get('conclusion', {})\n    extra = exp.get('extra', {})\n    \n    # Search recursively for classification keys\n    def find_keys(obj, prefix=\"\"):\n        found = {}\n        if isinstance(obj, dict):\n            for k, v in obj.items():\n                full_key = f\"{prefix}.{k}\" if prefix else k\n                if any(ck in k.lower() for ck in ['h7', 'h1', 'genuine', 'hacking', 'proved', 'classify', 'classification']):\n                    found[full_key] = v\n                if isinstance(v, (dict, list)):\n                    found.update(find_keys(v, full_key))\n        elif isinstance(obj, list):\n            for i, item in enumerate(obj):\n                found.update(find_keys(item, f\"{prefix}[{i}]\"))\n        return found\n    \n    all_found = {}\n    for section_name, section_data in [('metrics', metrics), ('conclusion', conclusion), ('extra', extra)]:\n        if section_data:\n            results = find_keys(section_data, section_name)\n            all_found.update(results)\n    \n    if all_found:\n        print(f\"\\n=== {exp_id} ===\")\n        for k, v in all_found.items():\n            # Truncate long values\n            sv = str(v)\n            if len(sv) > 200:\n                sv = sv[:200] + \"...\"\n            print(f\"  {k}: {sv}\")\nPYEOF\n",
    "description": "Search for classification-related fields across all experiments"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-15T07:59:05.936480+00:00_

=== exp1-isr-b03-s43 ===
  metrics.proved_only_mean_isr: 0.283
  metrics.hacking_rate_strict_h7: 0.022
  metrics.hacking_rate_functional: 0.3297
  metrics.genuine_rate: 0.6703
  metrics.genuine_count: 61
  metrics.n_proved: 91
  metrics.h1_conclusion_in_premise: 0.747

=== exp1-isr-b03-s43-r3 ===
  metrics.eval_proved_only_mean_isr: 0.2948
  metrics.eval_n_proved: 86
  metrics.eval_h7_strict_rate: 0.047
  metrics.eval_h7_strict_count: 4
  metrics.eval_h1_strict_rate: 0.686
  metrics.eval_h1_strict_count: 59
  metrics.eval_genuine_rate: 0.267
  metrics.eval_genuine_count: 23
  metrics.eval_by_answer_type.false.proved: 23
  metrics.eval_by_answer_type.unknown.proved: 35
  metrics.eval_by_answer_type.true.proved: 28

=== exp1-isr-b03-s44-r2 ===
  metrics.proved_only_isr: 0.7421
  metrics.n_proved: 95
  metrics.h7_rate: 1
  metrics.h7_count: 95
  metrics.h1_rate: 0
  metrics.h1_count: 0
  metrics.genuine_rate: 0
  metrics.genuine_count: 0

=== exp1-random-b03-s43 ===
  metrics.proved_only_mean_isr: 0.2209
  metrics.hacking_rate_strict_h7: 0
  metrics.hacking_rate_functional: 0.1013
  metrics.genuine_rate: 0.8987
  metrics.genuine_count: 71
  metrics.n_proved: 79
  metrics.h1_conclusion_in_premise: 0.759

=== exp1-random-b03-s43-r4 ===
  metrics.eval_proved_only_mean_isr: 0.1803
  metrics.eval_n_proved: 92
  metrics.eval_h7_strict_rate: 0.076
  metrics.eval_h7_strict_count: 7
  metrics.eval_h1_strict_rate: 0.978
  metrics.eval_h1_strict_count: 90
  metrics.eval_genuine_rate: 0.022
  metrics.eval_genuine_count: 2
  metrics.eval_by_answer_type.false.proved: 23
  metrics.eval_by_answer_type.unknown.proved: 37
  metrics.eval_by_answer_type.true.proved: 32

=== exp1-random-b03-s44-r2 ===
  metrics.eval_proved_only_mean_isr: 0
  metrics.eval_n_proved: 23
  metrics.eval_h7_strict_rate: 0
  metrics.eval_h7_strict_count: 0
  metrics.eval_h1_strict_rate: 1
  metrics.eval_h1_strict_count: 23
  metrics.eval_genuine_rate: 0
  metrics.eval_genuine_count: 0

=== plan001-exec-only-s42-r
…[truncated 6844 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_wilson-ci_20260515T075227",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-15T07:59:05.936632+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nfpath = \"/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/d80fed44-dadc-4e6f-9333-1a32a5430a13/tool-results/mcp-agent-ml-research-read_registry-1778831563449.txt\"\n\nwith open(fpath, 'r') as f:\n    raw = f.read()\n\nouter = json.loads(raw)\nregistry = json.loads(outer['result'])\nexperiments = registry['data']['experiments']\n\n# For experiments with classification data, check spec for condition/seed info\nclassification_exps = [\n    'plan001-exec-only-s42-r2', 'plan001-exec-only-s43-r4', 'plan001-exec-only-s44',\n    'plan002-additive-b01-s42', 'plan002-additive-b01-s43', 'plan002-additive-b01-s44',\n    'plan002-additive-b03-s42',\n    'exp1-isr-b03-s43', 'exp1-isr-b03-s43-r3', 'exp1-isr-b03-s44-r2',\n    'exp1-random-b03-s43', 'exp1-random-b03-s43-r4', 'exp1-random-b03-s44-r2',\n    'plan009-sft-baseline-s42-r4', 'plan009-sft-baseline-s43',\n    'plan013-random-reward-s42-r4',\n    'plan018-additive-random-b01-s42', 'plan018-additive-random-b01-s43-r2', 'plan018-additive-random-b01-s44',\n]\n\nfor exp_id in classification_exps:\n    exp = experiments.get(exp_id, {})\n    spec = exp.get('spec', {})\n    print(f\"\\n=== {exp_id} ===\")\n    if isinstance(spec, dict):\n        for k in ['condition', 'seed', 'beta', 'reward_type', 'method', 'training_type', 'n_proved', 'eval_n_proved']:\n            if k in spec:\n                print(f\"  spec.{k}: {spec[k]}\")\n        # Also look at spec keys\n        print(f\"  spec keys: {list(spec.keys())}\")\n    elif isinstance(spec, str):\n        print(f\"  spec: {spec[:200]}\")\n    \n    # Check conclusion for n_proved\n    conclusion = exp.get('conclusion', {})\n    if conclusion:\n        if isinstance(conclusion, dict):\n            for k in ['n_proved', 'eval_n_proved']:\n                if k in conclusion:\n                    print(f\"  conclusion.{k}: {conclusion[k]}\")\n        elif isinstance(conclusion, str):\n            if 'proved' in conclusion.lower():\n                print(f\"  conclusion (excerpt): {conclusion[:200]}\")\nPYEOF\n",
  "description": "Check spec fields for condition/seed info"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_wilson-ci_20260515T075227",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 << 'PYEOF'\nimport json\n\nfpath = \"/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/d80fed44-dadc-4e6f-9333-1a32a5430a13/tool-results/mcp-agent-ml-research-read_registry-1778831563449.txt\"\n\nwith open(fpath, 'r') as f:\n    raw = f.read()\n\nouter = json.loads(raw)\nregistry = json.loads(outer['result'])\nexperiments = registry['data']['experiments']\n\n# For experiments with classification data, check spec for condition/seed info\nclassification_exps = [\n    'plan001-exec-only-s42-r2', 'plan001-exec-only-s43-r4', 'plan001-exec-only-s44',\n    'plan002-additive-b01-s42', 'plan002-additive-b01-s43', 'plan002-additive-b01-s44',\n    'plan002-additive-b03-s42',\n    'exp1-isr-b03-s43', 'exp1-isr-b03-s43-r3', 'exp1-isr-b03-s44-r2',\n    'exp1-random-b03-s43', 'exp1-random-b03-s43-r4', 'exp1-random-b03-s44-r2',\n    'plan009-sft-baseline-s42-r4', 'plan009-sft-baseline-s43',\n    'plan013-random-reward-s42-r4',\n    'plan018-additive-random-b01-s42', 'plan018-additive-random-b01-s43-r2', 'plan018-additive-random-b01-s44',\n]\n\nfor exp_id in classification_exps:\n    exp = experiments.get(exp_id, {})\n    spec = exp.get('spec', {})\n    print(f\"\\n=== {exp_id} ===\")\n    if isinstance(spec, dict):\n        for k in ['condition', 'seed', 'beta', 'reward_type', 'method', 'training_type', 'n_proved', 'eval_n_proved']:\n            if k in spec:\n                print(f\"  spec.{k}: {spec[k]}\")\n        # Also look at spec keys\n        print(f\"  spec keys: {list(spec.keys())}\")\n    elif isinstance(spec, str):\n        print(f\"  spec: {spec[:200]}\")\n    \n    # Check conclusion for n_proved\n    conclusion = exp.get('conclusion', {})\n    if conclusion:\n        if isinstance(conclusion, dict):\n            for k in ['n_proved', 'eval_n_proved']:\n                if k in conclusion:\n                    print(f\"  conclusion.{k}: {conclusion[k]}\")\n        elif isinstance(conclusion, str):\n            if 'proved' in conclusion.lower():\n                print(f\"  conclusion (excerpt): {conclusion[:200]}\")\nPYEOF\n",
    "description": "Check spec fields for condition/seed info"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-15T07:59:05.936907+00:00_

=== plan001-exec-only-s42-r2 ===
  spec.seed: 42
  spec keys: ['command', 'server', 'data_path', 'data_count', 'model_name', 'seed', 'hypothesis', 'pid', 'gpu', 'log_path', 'submitted_at', 'submitted_via', 'backend', 'account', 'wall_clock_seconds', 'gpu_hours']

=== plan001-exec-only-s43-r4 ===
  spec.seed: 43
  spec keys: ['command', 'server', 'gpu', 'pid', 'log_path', 'submitted_at', 'submitted_via', 'backend', 'account', 'data_path', 'data_count', 'model_name', 'seed', 'hypothesis', 'plan_id', 'wall_clock_seconds', 'gpu_hours']

=== plan001-exec-only-s44 ===
  spec keys: ['command', 'server', 'gpu', 'pid', 'log_path', 'submitted_at', 'submitted_via', 'backend', 'account', 'wall_clock_seconds', 'gpu_hours']

=== plan002-additive-b01-s42 ===
  spec.seed: 42
  spec keys: ['command', 'server', 'gpu', 'pid', 'log_path', 'submitted_at', 'submitted_via', 'backend', 'account', 'data_path', 'data_count', 'model_name', 'seed', 'plan_id', 'reward_formula', 'num_steps', 'wall_clock_seconds', 'gpu_hours', 'checkpoint_path']

=== plan002-additive-b01-s43 ===
  spec keys: ['command', 'server', 'gpu', 'pid', 'log_path', 'submitted_at', 'submitted_via', 'backend', 'account', 'wall_clock_seconds', 'gpu_hours']

=== plan002-additive-b01-s44 ===
  spec.seed: 44
  spec keys: ['command', 'server', 'gpu', 'pid', 'log_path', 'submitted_at', 'submitted_via', 'backend', 'account', 'data_path', 'data_count', 'model_name', 'seed', 'wall_clock_seconds', 'gpu_hours']

=== plan002-additive-b03-s42 ===
  spec.seed: 42
  spec.beta: 0.3
  spec keys: ['data_path', 'data_count', 'model_name', 'seed', 'hypothesis', 'plan_id', 'reward_formula', 'beta', 'command', 'server', 'gpu', 'pid']

=== exp1-isr-b03-s43 ===
  spec.seed: 43
  spec.beta: 0.3
  spec keys: ['data_path', 'data_count', 'model_name', 'seed', 'hypothesis', 'plan_id', 'reward_formula', 'num_steps', 'beta', 'command', 'server', 'gpu', 'pid', 'checkpoint_path']

=== exp1-isr-b03-s43-r3 ===
  spec.seed: 43
  spec keys: ['command', 'server'
…[truncated 2729 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_wilson-ci_20260515T075227",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-15T07:59:05.937149+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nfpath = \"/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/d80fed44-dadc-4e6f-9333-1a32a5430a13/tool-results/mcp-agent-ml-research-read_registry-1778831563449.txt\"\n\nwith open(fpath, 'r') as f:\n    raw = f.read()\n\nouter = json.loads(raw)\nregistry = json.loads(outer['result'])\nexperiments = registry['data']['experiments']\n\n# Check conclusion for experiments that have classification in metrics but missing n_proved\ncheck_exps = ['plan002-additive-b01-s43', 'plan002-additive-b01-s44', 'plan018-additive-random-b01-s44',\n              'plan013-random-reward-s42-r4', 'plan004-o1-ablation-s42', 'plan009-sft-baseline-s43',\n              'plan018-additive-random-b01-s42', 'plan018-additive-random-b01-s43-r2']\n\nfor exp_id in check_exps:\n    exp = experiments.get(exp_id, {})\n    conclusion = exp.get('conclusion', {})\n    metrics = exp.get('metrics', {})\n    print(f\"\\n=== {exp_id} ===\")\n    print(f\"  metrics: {json.dumps(metrics, indent=2)[:500]}\")\n    if isinstance(conclusion, str):\n        print(f\"  conclusion: {conclusion[:300]}\")\n    elif isinstance(conclusion, dict):\n        print(f\"  conclusion: {json.dumps(conclusion, indent=2)[:300]}\")\nPYEOF\n",
  "description": "Check conclusion and metrics for experiments missing n_proved"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_wilson-ci_20260515T075227",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 << 'PYEOF'\nimport json\n\nfpath = \"/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/d80fed44-dadc-4e6f-9333-1a32a5430a13/tool-results/mcp-agent-ml-research-read_registry-1778831563449.txt\"\n\nwith open(fpath, 'r') as f:\n    raw = f.read()\n\nouter = json.loads(raw)\nregistry = json.loads(outer['result'])\nexperiments = registry['data']['experiments']\n\n# Check conclusion for experiments that have classification in metrics but missing n_proved\ncheck_exps = ['plan002-additive-b01-s43', 'plan002-additive-b01-s44', 'plan018-additive-random-b01-s44',\n              'plan013-random-reward-s42-r4', 'plan004-o1-ablation-s42', 'plan009-sft-baseline-s43',\n              'plan018-additive-random-b01-s42', 'plan018-additive-random-b01-s43-r2']\n\nfor exp_id in check_exps:\n    exp = experiments.get(exp_id, {})\n    conclusion = exp.get('conclusion', {})\n    metrics = exp.get('metrics', {})\n    print(f\"\\n=== {exp_id} ===\")\n    print(f\"  metrics: {json.dumps(metrics, indent=2)[:500]}\")\n    if isinstance(conclusion, str):\n        print(f\"  conclusion: {conclusion[:300]}\")\n    elif isinstance(conclusion, dict):\n        print(f\"  conclusion: {json.dumps(conclusion, indent=2)[:300]}\")\nPYEOF\n",
    "description": "Check conclusion and metrics for experiments missing n_proved"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-15T07:59:05.937332+00:00_

=== plan002-additive-b01-s43 ===
  metrics: {
  "eval_prove_rate": 0.61,
  "eval_mean_isr": 0.5063,
  "eval_isr_std": 0.4518,
  "eval_median_isr": 0.5,
  "eval_proved_only_isr": 0.8301,
  "component_count_mean": 4.03,
  "component_count_2_ratio": 0,
  "tautological_collapse": false,
  "isr_0_ratio": 0.39,
  "isr_1_ratio": 0.656,
  "proved_single_premise_ratio": 1,
  "h7_rate_calibrated": 0.967,
  "h7_definition": "single_premise AND premise==conclusion (normalized)",
  "hacking_mode": "conclusion_duplication_isr_inflation",
  "conclusion_
  conclusion: negative

=== plan002-additive-b01-s44 ===
  metrics: {
  "eval_prove_rate": 0.89,
  "eval_mean_isr": 0.803,
  "eval_isr_std": 0.3418,
  "eval_median_isr": 1,
  "component_count_mean": 4.33,
  "component_count_2_ratio": 0.022,
  "tautological_collapse": false,
  "isr_0_ratio": 0.12,
  "isr_1_ratio": 0.73,
  "proved_single_premise_ratio": 1,
  "h7_rate_calibrated": 0.865,
  "h7_definition": "single_premise AND premise==conclusion (normalized)",
  "hacking_mode": "conclusion_duplication_isr_inflation",
  "conclusion_embedding": true,
  "component_dis
  conclusion: negative

=== plan018-additive-random-b01-s44 ===
  metrics: {
  "prove_rate": 0.89,
  "mean_isr": 0.0619,
  "isr_std": 0.1756,
  "median_isr": 0,
  "proved_only_mean_isr": 0.0695,
  "n_proved": 89,
  "n_problems": 100,
  "max_isr": 1,
  "min_isr": 0,
  "isr_pr_ratio": 0.0695,
  "isr_zero_count": 72,
  "isr_one_count": 2,
  "by_answer_type": {
    "false": {
      "count": 25,
      "proved": 21,
      "prove_rate": 0.84,
      "mean_isr": 0.0533
    },
    "unknown": {
      "count": 41,
      "proved": 40,
      "prove_rate": 0.976,
      "mean_isr": 0.
  conclusion: success

=== plan013-random-reward-s42-r4 ===
  metrics: {
  "eval_prove_rate": 1,
  "eval_mean_isr": 0.535,
  "eval_isr_std": 0.1282,
  "eval_proved_only_isr": 0.535,
  "eval_median_isr": 0.5,
  "eval_n_proved": 100,
  "eval_n_problems": 100,
  "eval_method": "eval_sta.py full STA",
  "eval_dat
…[truncated 1837 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_wilson-ci_20260515T075227",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-15T07:59:05.937498+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nfpath = \"/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/d80fed44-dadc-4e6f-9333-1a32a5430a13/tool-results/mcp-agent-ml-research-read_registry-1778831563449.txt\"\n\nwith open(fpath, 'r') as f:\n    raw = f.read()\n\nouter = json.loads(raw)\nregistry = json.loads(outer['result'])\nexperiments = registry['data']['experiments']\n\n# Get full metrics for experiments I need to derive n_proved from\ncheck = ['plan002-additive-b01-s43', 'plan002-additive-b01-s44', 'plan004-o1-ablation-s42',\n         'plan009-sft-baseline-s42-r4', 'plan009-sft-baseline-s43',\n         'plan018-additive-random-b01-s43-r2', 'plan001-exec-only-s44']\n\nfor exp_id in check:\n    exp = experiments.get(exp_id, {})\n    m = exp.get('metrics', {})\n    # Try to find n_proved or compute it\n    n_proved = m.get('n_proved') or m.get('eval_n_proved')\n    if not n_proved:\n        # Try prove_rate * n_problems\n        pr = m.get('eval_prove_rate') or m.get('prove_rate')\n        n = m.get('eval_n_problems') or m.get('n_problems', 100)\n        if pr:\n            n_proved = int(pr * n) if pr <= 1 else int(pr)\n    \n    h7 = m.get('h7_count') or m.get('eval_h7_strict_count') or m.get('eval_greedy_h7_count')\n    h1 = m.get('h1_count') or m.get('eval_h1_strict_count') or m.get('eval_greedy_h1_count')\n    genuine = m.get('genuine_count') or m.get('eval_genuine_count')\n    \n    print(f\"{exp_id}: n_proved={n_proved}, h7={h7}, h1={h1}, genuine={genuine}\")\n    \n    # Also check for h7_rate_calibrated as proxy\n    h7rc = m.get('h7_rate_calibrated')\n    if h7rc:\n        print(f\"  h7_rate_calibrated={h7rc}\")\nPYEOF\n",
  "description": "Derive n_proved for experiments missing it"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_wilson-ci_20260515T075227",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 << 'PYEOF'\nimport json\n\nfpath = \"/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/d80fed44-dadc-4e6f-9333-1a32a5430a13/tool-results/mcp-agent-ml-research-read_registry-1778831563449.txt\"\n\nwith open(fpath, 'r') as f:\n    raw = f.read()\n\nouter = json.loads(raw)\nregistry = json.loads(outer['result'])\nexperiments = registry['data']['experiments']\n\n# Get full metrics for experiments I need to derive n_proved from\ncheck = ['plan002-additive-b01-s43', 'plan002-additive-b01-s44', 'plan004-o1-ablation-s42',\n         'plan009-sft-baseline-s42-r4', 'plan009-sft-baseline-s43',\n         'plan018-additive-random-b01-s43-r2', 'plan001-exec-only-s44']\n\nfor exp_id in check:\n    exp = experiments.get(exp_id, {})\n    m = exp.get('metrics', {})\n    # Try to find n_proved or compute it\n    n_proved = m.get('n_proved') or m.get('eval_n_proved')\n    if not n_proved:\n        # Try prove_rate * n_problems\n        pr = m.get('eval_prove_rate') or m.get('prove_rate')\n        n = m.get('eval_n_problems') or m.get('n_problems', 100)\n        if pr:\n            n_proved = int(pr * n) if pr <= 1 else int(pr)\n    \n    h7 = m.get('h7_count') or m.get('eval_h7_strict_count') or m.get('eval_greedy_h7_count')\n    h1 = m.get('h1_count') or m.get('eval_h1_strict_count') or m.get('eval_greedy_h1_count')\n    genuine = m.get('genuine_count') or m.get('eval_genuine_count')\n    \n    print(f\"{exp_id}: n_proved={n_proved}, h7={h7}, h1={h1}, genuine={genuine}\")\n    \n    # Also check for h7_rate_calibrated as proxy\n    h7rc = m.get('h7_rate_calibrated')\n    if h7rc:\n        print(f\"  h7_rate_calibrated={h7rc}\")\nPYEOF\n",
    "description": "Derive n_proved for experiments missing it"
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-15T07:59:05.937634+00:00_

plan002-additive-b01-s43: n_proved=61, h7=None, h1=None, genuine=None
  h7_rate_calibrated=0.967
plan002-additive-b01-s44: n_proved=89, h7=None, h1=None, genuine=None
  h7_rate_calibrated=0.865
plan004-o1-ablation-s42: n_proved=63, h7=None, h1=63, genuine=None
plan009-sft-baseline-s42-r4: n_proved=14, h7=None, h1=1, genuine=13
plan009-sft-baseline-s43: n_proved=15, h7=None, h1=1, genuine=14
plan018-additive-random-b01-s43-r2: n_proved=88, h7=None, h1=82, genuine=6
plan001-exec-only-s44: n_proved=98, h7=97, h1=None, genuine=None

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_wilson-ci_20260515T075227",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-15T07:59:05.937878+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\nimport os\n\nfpath = \"/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/d80fed44-dadc-4e6f-9333-1a32a5430a13/tool-results/mcp-agent-ml-research-read_registry-1778831563449.txt\"\n\nwith open(fpath, 'r') as f:\n    raw = f.read()\n\nouter = json.loads(raw)\nregistry = json.loads(outer['result'])\nexperiments = registry['data']['experiments']\n\ndef infer_condition(exp_id):\n    \"\"\"Infer the experimental condition from the experiment ID.\"\"\"\n    eid = exp_id.lower()\n    if 'sft' in eid:\n        return 'SFT'\n    if 'o1-ablation' in eid:\n        return 'o1-ablation'\n    if 'prolog-exec' in eid:\n        return 'Prolog exec-only'\n    if 'prolog-sta' in eid:\n        return 'Prolog STA'\n    if 'sta-phase0' in eid:\n        return 'STA phase0 baseline'\n    if 'sta-phase1-exec-only' in eid:\n        return 'STA exec-only'\n    if 'sta-phase1-exec-sta' in eid:\n        return 'STA exec+STA'\n    if 'sta-gt-isr' in eid:\n        return 'STA GT ISR baseline'\n    if 'downstream-nli' in eid:\n        return 'downstream NLI'\n    if 'linear' in eid:\n        return 'linear'\n    if 'extended-1000' in eid:\n        return 'extended-1000'\n    if 'hacking-taxonomy' in eid:\n        return 'hacking-taxonomy'\n    if 'random-reward' in eid:\n        return 'Random reward (no STA)'\n    \n    # Determine ISR vs Random vs exec-only\n    if 'exec-only' in eid or 'exec-s' in eid:\n        return 'exec-only'\n    \n    # additive-random = Random β\n    if 'additive-random' in eid or 'random-b0' in eid:\n        # Determine beta\n        if 'b01' in eid:\n            return 'Random β=0.1'\n        elif 'b03' in eid:\n            return 'Random β=0.3'\n        else:\n            return 'Random β=0.3'  # default for exp1-random\n    \n    # additive (non-random) = ISR β\n    if 'additive-b0' in eid or 'isr-b0' in eid:\n        if 'b01' in eid:\n            return 'ISR β=0.1'\n        elif 'b03' in eid:\n            return 'ISR β=0.3'\n        else:\n            return 'ISR β=0.1'\n    \n    # eval-exec-only\n    if 'eval-exec-only' in eid:\n        return 'exec-only (eval)'\n    \n    return 'unknown'\n\ndef infer_seed(exp_id, spec):\n    \"\"\"Infer seed from experiment ID or spec.\"\"\"\n    # Check spec first\n    seed = spec.get('seed') if isinstance(spec, dict) else None\n    if seed:\n        return f\"s{seed}\"\n    \n    # Parse from ID\n    eid = exp_id.lower()\n    if '-s42' in eid:\n        return 's42'\n    elif '-s43' in eid:\n        return 's43'\n    elif '-s44' in eid:\n        return 's44'\n    return None\n\ndef extract_classification(exp_id, exp):\n    \"\"\"Extract classification data from an experiment.\"\"\"\n    m = exp.get('metrics', {})\n    if not m or not isinstance(m, dict):\n        return None\n    \n    # Get n_proved\n    n_proved = m.get('n_proved') or m.get('eval_n_proved') or m.get('eval_greedy_n_proved')\n    if not n_proved:\n        pr = m.get('eval_prove_rate') or m.get('prove_rate')\n        n = m.get('eval_n_problems') or m.get('n_problems', 100)\n        if pr is not None and n:\n            n_proved = int(round(pr * n)) if pr <= 1 else int(pr)\n    \n    # Get h7\n    h7_count = m.get('h7_count') or m.get('eval_h7_strict_count') or m.get('eval_greedy_h7_count')\n    h7_rate = m.get('h7_rate') or m.get('eval_h7_strict_rate') or m.get('eval_greedy_h7_rate') or m.get('hacking_rate_strict_h7') or m.get('h7_rate_calibrated')\n    \n    # Check nested h7_classification\n    h7c = m.get('h7_classification', {})\n    if isinstance(h7c, dict):\n        if h7_count is None:\n            h7_count = h7c.get('h7_strict')\n        if h7_rate is None:\n            h7_rate = h7c.get('h7_rate')\n    \n    # Get h1\n    h1_count = m.get('h1_count') or m.get('eval_h1_strict_count') or m.get('eval_greedy_h1_count')\n    h1_rate = m.get('h1_rate') or m.get('eval_h1_strict_rate') or m.get('eval_greedy_h1_rate') or m.get('hacking_rate_functional')\n    if isinstance(h7c, dict):\n        if h1_count is None:\n            h1_count = h7c.get('h1_strict')\n        if h1_rate is None:\n            h1_rate = h7c.get('h1_rate')\n    \n    # Get genuine\n    genuine_count = m.get('genuine_count') or m.get('eval_genuine_count') or m.get('non_hacking_count')\n    genuine_rate = m.get('genuine_rate') or m.get('eval_genuine_rate') or m.get('non_hacking_rate') or m.get('eval_greedy_genuine_rate')\n    if isinstance(h7c, dict):\n        if genuine_count is None:\n            genuine_count = h7c.get('genuine_count')\n        if genuine_rate is None:\n            genuine_rate = h7c.get('genuine_rate')\n    \n    # Only return if we have at least some classification data\n    has_any = any(v is not None for v in [h7_count, h7_rate, h1_count, h1_rate, genuine_count, genuine_rate])\n    if not has_any:\n        return None\n    \n    spec = exp.get('spec', {})\n    condition = infer_condition(exp_id)\n    seed = infer_seed(exp_id, spec)\n    \n    return {\n        'experiment_id': exp_id,\n        'condition': condition,\n        'seed': seed,\n        'n_proved': n_proved,\n        'h7_count': h7_count,\n        'h1_count': h1_count,\n        'genuine_count': genuine_count,\n        'h7_rate': h7_rate,\n        'h1_rate': h1_rate,\n        'genuine_rate': genuine_rate,\n    }\n\n# Extract all\nresults = []\nfor exp_id in sorted(experiments.keys()):\n    exp = experiments[exp_id]\n    row = extract_classification(exp_id, exp)\n    if row:\n        results.append(row)\n\n# Print results\nprint(f\"Extracted {len(results)} experiments with classification data:\\n\")\nprint(f\"{'experiment_id':45s} {'condition':20s} {'seed':5s} {'n_proved':>8s} {'h7_count':>8s} {'h1_count':>8s} {'genuine':>8s} {'h7_rate':>8s} {'h1_rate':>8s} {'gen_rate':>8s}\")\nprint(\"-\" * 160)\nfor r in results:\n    def fmt(v):\n        if v is None:\n            return \"null\"\n        if isinstance(v, float):\n            return f\"{v:.3f}\"\n        return str(v)\n    \n    print(f\"{r['experiment_id']:45s} {r['condition']:20s} {str(r['seed'] or ''):5s} \"\n          f\"{fmt(r['n_proved']):>8s} {fmt(r['h7_count']):>8s} {fmt(r['h1_count']):>8s} \"\n          f\"{fmt(r['genuine_count']):>8s} {fmt(r['h7_rate']):>8s} {fmt(r['h1_rate']):>8s} \"\n          f\"{fmt(r['genuine_rate']):>8s}\")\n\n# Write output\noutpath = \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/registry_extract.json\"\nos.makedirs(os.path.dirname(outpath), exist_ok=True)\nwith open(outpath, 'w') as f:\n    json.dump(results, f, indent=2)\n\nprint(f\"\\nWritten to {outpath}\")\nPYEOF\n",
  "description": "Extract classification data from all experiments and write output JSON"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_wilson-ci_20260515T075227",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 << 'PYEOF'\nimport json\nimport os\n\nfpath = \"/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/d80fed44-dadc-4e6f-9333-1a32a5430a13/tool-results/mcp-agent-ml-research-read_registry-1778831563449.txt\"\n\nwith open(fpath, 'r') as f:\n    raw = f.read()\n\nouter = json.loads(raw)\nregistry = json.loads(outer['result'])\nexperiments = registry['data']['experiments']\n\ndef infer_condition(exp_id):\n    \"\"\"Infer the experimental condition from the experiment ID.\"\"\"\n    eid = exp_id.lower()\n    if 'sft' in eid:\n        return 'SFT'\n    if 'o1-ablation' in eid:\n        return 'o1-ablation'\n    if 'prolog-exec' in eid:\n        return 'Prolog exec-only'\n    if 'prolog-sta' in eid:\n        return 'Prolog STA'\n    if 'sta-phase0' in eid:\n        return 'STA phase0 baseline'\n    if 'sta-phase1-exec-only' in eid:\n        return 'STA exec-only'\n    if 'sta-phase1-exec-sta' in eid:\n        return 'STA exec+STA'\n    if 'sta-gt-isr' in eid:\n        return 'STA GT ISR baseline'\n    if 'downstream-nli' in eid:\n        return 'downstream NLI'\n    if 'linear' in eid:\n        return 'linear'\n    if 'extended-1000' in eid:\n        return 'extended-1000'\n    if 'hacking-taxonomy' in eid:\n        return 'hacking-taxonomy'\n    if 'random-reward' in eid:\n        return 'Random reward (no STA)'\n    \n    # Determine ISR vs Random vs exec-only\n    if 'exec-only' in eid or 'exec-s' in eid:\n        return 'exec-only'\n    \n    # additive-random = Random β\n    if 'additive-random' in eid or 'random-b0' in eid:\n        # Determine beta\n        if 'b01' in eid:\n            return 'Random β=0.1'\n        elif 'b03' in eid:\n            return 'Random β=0.3'\n        else:\n            return 'Random β=0.3'  # default for exp1-random\n    \n    # additive (non-random) = ISR β\n    if 'additive-b0' in eid or 'isr-b0' in eid:\n        if 'b01' in eid:\n            return 'ISR β=0.1'\n        elif 'b03' in eid:\n            return 'ISR β=0.3'\n        else:\n            return 'ISR β=0.1'\n    \n    # eval-exec-only\n    if 'eval-exec-only' in eid:\n        return 'exec-only (eval)'\n    \n    return 'unknown'\n\ndef infer_seed(exp_id, spec):\n    \"\"\"Infer seed from experiment ID or spec.\"\"\"\n    # Check spec first\n    seed = spec.get('seed') if isinstance(spec, dict) else None\n    if seed:\n        return f\"s{seed}\"\n    \n    # Parse from ID\n    eid = exp_id.lower()\n    if '-s42' in eid:\n        return 's42'\n    elif '-s43' in eid:\n        return 's43'\n    elif '-s44' in eid:\n        return 's44'\n    return None\n\ndef extract_classification(exp_id, exp):\n    \"\"\"Extract classification data from an experiment.\"\"\"\n    m = exp.get('metrics', {})\n    if not m or not isinstance(m, dict):\n        return None\n    \n    # Get n_proved\n    n_proved = m.get('n_proved') or m.get('eval_n_proved') or m.get('eval_greedy_n_proved')\n    if not n_proved:\n        pr = m.get('eval_prove_rate') or m.get('prove_rate')\n        n = m.get('eval_n_problems') or m.get('n_problems', 100)\n        if pr is not None and n:\n            n_proved = int(round(pr * n)) if pr <= 1 else int(pr)\n    \n    # Get h7\n    h7_count = m.get('h7_count') or m.get('eval_h7_strict_count') or m.get('eval_greedy_h7_count')\n    h7_rate = m.get('h7_rate') or m.get('eval_h7_strict_rate') or m.get('eval_greedy_h7_rate') or m.get('hacking_rate_strict_h7') or m.get('h7_rate_calibrated')\n    \n    # Check nested h7_classification\n    h7c = m.get('h7_classification', {})\n    if isinstance(h7c, dict):\n        if h7_count is None:\n            h7_count = h7c.get('h7_strict')\n        if h7_rate is None:\n            h7_rate = h7c.get('h7_rate')\n    \n    # Get h1\n    h1_count = m.get('h1_count') or m.get('eval_h1_strict_count') or m.get('eval_greedy_h1_count')\n    h1_rate = m.get('h1_rate') or m.get('eval_h1_strict_rate') or m.get('eval_greedy_h1_rate') or m.get('hacking_rate_functional')\n    if isinstance(h7c, dict):\n        if h1_count is None:\n            h1_count = h7c.get('h1_strict')\n        if h1_rate is None:\n            h1_rate = h7c.get('h1_rate')\n    \n    # Get genuine\n    genuine_count = m.get('genuine_count') or m.get('eval_genuine_count') or m.get('non_hacking_count')\n    genuine_rate = m.get('genuine_rate') or m.get('eval_genuine_rate') or m.get('non_hacking_rate') or m.get('eval_greedy_genuine_rate')\n    if isinstance(h7c, dict):\n        if genuine_count is None:\n            genuine_count = h7c.get('genuine_count')\n        if genuine_rate is None:\n            genuine_rate = h7c.get('genuine_rate')\n    \n    # Only return if we have at least some classification data\n    has_any = any(v is not None for v in [h7_count, h7_rate, h1_count, h1_rate, genuine_count, genuine_rate])\n    if not has_any:\n        return None\n    \n    spec = exp.get('spec', {})\n    condition = infer_condition(exp_id)\n    seed = infer_seed(exp_id, spec)\n    \n    return {\n        'experiment_id': exp_id,\n        'condition': condition,\n        'seed': seed,\n        'n_proved': n_proved,\n        'h7_count': h7_count,\n        'h1_count': h1_count,\n        'genuine_count': genuine_count,\n        'h7_rate': h7_rate,\n        'h1_rate': h1_rate,\n        'genuine_rate': genuine_rate,\n    }\n\n# Extract all\nresults = []\nfor exp_id in sorted(experiments.keys()):\n    exp = experiments[exp_id]\n    row = extract_classification(exp_id, exp)\n    if row:\n        results.append(row)\n\n# Print results\nprint(f\"Extracted {len(results)} experiments with classification data:\\n\")\nprint(f\"{'experiment_id':45s} {'condition':20s} {'seed':5s} {'n_proved':>8s} {'h7_count':>8s} {'h1_count':>8s} {'genuine':>8s} {'h7_rate':>8s} {'h1_rate':>8s} {'gen_rate':>8s}\")\nprint(\"-\" * 160)\nfor r in results:\n    def fmt(v):\n        if v is None:\n            return \"null\"\n        if isinstance(v, float):\n            return f\"{v:.3f}\"\n        return str(v)\n    \n    print(f\"{r['experiment_id']:45s} {r['condition']:20s} {str(r['seed'] or ''):5s} \"\n          f\"{fmt(r['n_proved']):>8s} {fmt(r['h7_count']):>8s} {fmt(r['h1_count']):>8s} \"\n          f\"{fmt(r['genuine_count']):>8s} {fmt(r['h7_rate']):>8s} {fmt(r['h1_rate']):>8s} \"\n          f\"{fmt(r['genuine_rate']):>8s}\")\n\n# Write output\noutpath = \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/registry_extract.json\"\nos.makedirs(os.path.dirname(outpath), exist_ok=True)\nwith open(outpath, 'w') as f:\n    json.dump(results, f, indent=2)\n\nprint(f\"\\nWritten to {outpath}\")\nPYEOF\n",
    "description": "Extract classification data from all experiments and write output JSON"
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-15T07:59:05.938121+00:00_

Extracted 20 experiments with classification data:

experiment_id                                 condition            seed  n_proved h7_count h1_count  genuine  h7_rate  h1_rate gen_rate
----------------------------------------------------------------------------------------------------------------------------------------------------------------
exp1-isr-b03-s43                              ISR β=0.3            s43         91     null     null       61    0.022    0.330    0.670
exp1-isr-b03-s43-r3                           ISR β=0.3            s43         86        4       59       23    0.047    0.686    0.267
exp1-isr-b03-s44-r2                           ISR β=0.3            s44         95       95     null     null        1     null     null
exp1-random-b03-s43                           Random β=0.3         s43         79     null     null       71     null    0.101    0.899
exp1-random-b03-s43-r4                        Random β=0.3         s43         92        7       90        2    0.076    0.978    0.022
exp1-random-b03-s44-r2                        Random β=0.3         s44         23     null       23     null     null        1     null
plan001-exec-only-s42-r2                      exec-only            s42         93     null       81       12     null    0.871    0.129
plan001-exec-only-s43-r4                      exec-only            s43         13        0       13     null     null        1        0
plan001-exec-only-s44                         exec-only            s44         98       97     null     null        1     null     null
plan002-additive-b01-s42                      ISR β=0.1            s42         81       13       42       25    0.160    0.519    0.309
plan002-additive-b01-s43                      ISR β=0.1            s43         61     null     null     null    0.967     null     null
plan002-additive-b01-s44                      ISR β=0.1            s44         89     null     null     null    0.865     null     null
plan002-additive-b0
…[truncated 1191 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_wilson-ci_20260515T075227",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-15T07:59:05.938285+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nfpath = \"/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/d80fed44-dadc-4e6f-9333-1a32a5430a13/tool-results/mcp-agent-ml-research-read_registry-1778831563449.txt\"\n\nwith open(fpath, 'r') as f:\n    raw = f.read()\n\nouter = json.loads(raw)\nregistry = json.loads(outer['result'])\nexperiments = registry['data']['experiments']\n\n# Check some additional experiments\nextras = ['plan018-additive-random-b01-s42', 'plan018-additive-random-b01-s44',\n          'plan006-prolog-exec-s42', 'plan006-prolog-sta-s42', 'plan006-prolog-sta-s44',\n          'exp1-isr-b03-s44-r2', 'exp1-random-b03-s44-r2',\n          'plan001-exec-only-s44', 'plan013-random-reward-s42-r4',\n          'exp1-random-b03-s43', 'exp1-isr-b03-s43']\n\nfor exp_id in extras:\n    exp = experiments.get(exp_id, {})\n    m = exp.get('metrics', {})\n    print(f\"\\n=== {exp_id} ===\")\n    print(json.dumps(m, indent=2)[:600])\nPYEOF\n",
  "description": "Check full metrics for additional experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_wilson-ci_20260515T075227",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 << 'PYEOF'\nimport json\n\nfpath = \"/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/d80fed44-dadc-4e6f-9333-1a32a5430a13/tool-results/mcp-agent-ml-research-read_registry-1778831563449.txt\"\n\nwith open(fpath, 'r') as f:\n    raw = f.read()\n\nouter = json.loads(raw)\nregistry = json.loads(outer['result'])\nexperiments = registry['data']['experiments']\n\n# Check some additional experiments\nextras = ['plan018-additive-random-b01-s42', 'plan018-additive-random-b01-s44',\n          'plan006-prolog-exec-s42', 'plan006-prolog-sta-s42', 'plan006-prolog-sta-s44',\n          'exp1-isr-b03-s44-r2', 'exp1-random-b03-s44-r2',\n          'plan001-exec-only-s44', 'plan013-random-reward-s42-r4',\n          'exp1-random-b03-s43', 'exp1-isr-b03-s43']\n\nfor exp_id in extras:\n    exp = experiments.get(exp_id, {})\n    m = exp.get('metrics', {})\n    print(f\"\\n=== {exp_id} ===\")\n    print(json.dumps(m, indent=2)[:600])\nPYEOF\n",
    "description": "Check full metrics for additional experiments"
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-15T07:59:05.938455+00:00_

=== plan018-additive-random-b01-s42 ===
{
  "eval_prove_rate": 0.79,
  "eval_mean_isr": 0.1038,
  "eval_isr_std": 0.1369,
  "eval_median_isr": 0.0357,
  "eval_proved_only_isr": 0.1314,
  "eval_n_proved": 79,
  "eval_n_problems": 100,
  "eval_component_count_mean": 8.46,
  "eval_component_count_median": 8,
  "eval_component_count_2_ratio": 0,
  "eval_isr_1_ratio": 0,
  "eval_isr_0_ratio": 0.367,
  "eval_isr_gt0_ratio": 0.633,
  "eval_by_type_false_pr": 0.8,
  "eval_by_type_false_isr": 0.1318,
  "eval_by_type_unknown_pr": 0.7317,
  "eval_by_type_unknown_isr": 0.0944,
  "eval_by_type_true_pr": 0.8529,
  "eval_by_type_true_isr": 0.0945,

=== plan018-additive-random-b01-s44 ===
{
  "prove_rate": 0.89,
  "mean_isr": 0.0619,
  "isr_std": 0.1756,
  "median_isr": 0,
  "proved_only_mean_isr": 0.0695,
  "n_proved": 89,
  "n_problems": 100,
  "max_isr": 1,
  "min_isr": 0,
  "isr_pr_ratio": 0.0695,
  "isr_zero_count": 72,
  "isr_one_count": 2,
  "by_answer_type": {
    "false": {
      "count": 25,
      "proved": 21,
      "prove_rate": 0.84,
      "mean_isr": 0.0533
    },
    "unknown": {
      "count": 41,
      "proved": 40,
      "prove_rate": 0.976,
      "mean_isr": 0.0892
    },
    "true": {
      "count": 34,
      "proved": 28,
      "prove_rate": 0.824,
      "m

=== plan006-prolog-exec-s42 ===
{
  "eval_prove_rate": 0.83,
  "eval_mean_isr": 0.031,
  "eval_proved_only_isr": 0.037,
  "eval_median_isr": 0,
  "eval_max_isr": 0.2,
  "eval_isr_std": 0.0534,
  "h7_rate": 0,
  "h1_rate": 0,
  "isr_1_rate": 0,
  "single_premise_rate": 0,
  "by_answer_type": {
    "true": {
      "proved": 37,
      "count": 40,
      "pr": 0.925,
      "isr": 0.037
    },
    "false": {
      "proved": 21,
      "count": 29,
      "pr": 0.724,
      "isr": 0.038
    },
    "unknown": {
      "proved": 25,
      "count": 31,
      "pr": 0.806,
      "isr": 0.016
    }
  }
}

=== plan006-prolog-sta-s42 ===
{
  "cumulative_prove_rate": 0.848,
  "cumulative_mean_isr": 0.787,
  "final_prove_rate
…[truncated 3816 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_wilson-ci_20260515T075227",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-15T07:59:05.938641+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\nimport os\n\nfpath = \"/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/d80fed44-dadc-4e6f-9333-1a32a5430a13/tool-results/mcp-agent-ml-research-read_registry-1778831563449.txt\"\n\nwith open(fpath, 'r') as f:\n    raw = f.read()\n\nouter = json.loads(raw)\nregistry = json.loads(outer['result'])\nexperiments = registry['data']['experiments']\n\ndef infer_condition(exp_id):\n    eid = exp_id.lower()\n    if 'sft' in eid:\n        return 'SFT'\n    if 'o1-ablation' in eid:\n        return 'o1-ablation'\n    if 'prolog-exec' in eid:\n        return 'Prolog exec-only'\n    if 'prolog-sta' in eid:\n        return 'Prolog STA'\n    if 'sta-phase0' in eid:\n        return 'STA phase0 baseline'\n    if 'sta-phase1-exec-only' in eid:\n        return 'STA exec-only'\n    if 'sta-phase1-exec-sta' in eid:\n        return 'STA exec+STA'\n    if 'sta-gt-isr' in eid:\n        return 'STA GT ISR baseline'\n    if 'downstream-nli' in eid:\n        return 'downstream NLI'\n    if 'linear' in eid:\n        return 'linear'\n    if 'extended-1000' in eid:\n        return 'extended-1000'\n    if 'hacking-taxonomy' in eid:\n        return 'hacking-taxonomy'\n    if 'random-reward' in eid:\n        return 'Random reward (no STA)'\n    if 'exec-only' in eid or (eid.startswith('plan001') and 'exec' in eid) or eid.startswith('plan003-eval-exec'):\n        return 'exec-only'\n    # Random β variants\n    if 'additive-random' in eid or eid.startswith('plan017') or eid.startswith('plan018'):\n        if 'b01' in eid:\n            return 'Random β=0.1'\n        return 'Random β=0.3'\n    if 'random-b0' in eid or eid.startswith('exp1-random'):\n        if 'b01' in eid:\n            return 'Random β=0.1'\n        return 'Random β=0.3'\n    # ISR β variants\n    if 'additive-b0' in eid or eid.startswith('plan002'):\n        if 'b01' in eid:\n            return 'ISR β=0.1'\n        if 'b03' in eid:\n            return 'ISR β=0.3'\n        return 'ISR β=0.1'\n    if 'isr-b0' in eid or eid.startswith('exp1-isr'):\n        if 'b01' in eid:\n            return 'ISR β=0.1'\n        return 'ISR β=0.3'\n    return 'unknown'\n\ndef infer_seed(exp_id, spec):\n    seed = spec.get('seed') if isinstance(spec, dict) else None\n    if seed:\n        return f\"s{seed}\"\n    eid = exp_id.lower()\n    if '-s42' in eid:\n        return 's42'\n    elif '-s43' in eid:\n        return 's43'\n    elif '-s44' in eid:\n        return 's44'\n    return None\n\ndef normalize_rate(val):\n    \"\"\"Normalize rates that might be in percentage form (>1) to [0,1] fraction.\"\"\"\n    if val is None:\n        return None\n    if isinstance(val, (int, float)) and val > 1:\n        return round(val / 100, 4)\n    return val\n\ndef extract_classification(exp_id, exp):\n    m = exp.get('metrics', {})\n    if not m or not isinstance(m, dict):\n        return None\n    \n    # Get n_proved from multiple sources\n    n_proved = m.get('n_proved') or m.get('eval_n_proved') or m.get('eval_greedy_n_proved') or m.get('eval_proved_count') or m.get('proved_count')\n    if not n_proved:\n        pr = m.get('eval_prove_rate') or m.get('prove_rate')\n        n = m.get('eval_n_problems') or m.get('n_problems', 100)\n        if pr is not None and n:\n            n_proved = int(round(pr * n)) if pr <= 1 else int(pr)\n    \n    # h7\n    h7_count = None\n    for k in ['h7_count', 'eval_h7_strict_count', 'eval_greedy_h7_count', 'eval_h7_count']:\n        if k in m and m[k] is not None:\n            h7_count = m[k]\n            break\n    \n    h7_rate = None\n    for k in ['h7_rate', 'eval_h7_strict_rate', 'eval_greedy_h7_rate', 'hacking_rate_strict_h7',\n              'h7_rate_calibrated', 'eval_h7_rate', 'h7_functional_rate']:\n        if k in m and m[k] is not None:\n            h7_rate = m[k]\n            break\n    \n    # h1\n    h1_count = None\n    for k in ['h1_count', 'eval_h1_strict_count', 'eval_greedy_h1_count']:\n        if k in m and m[k] is not None:\n            h1_count = m[k]\n            break\n    \n    h1_rate = None\n    for k in ['h1_rate', 'eval_h1_strict_rate', 'eval_greedy_h1_rate', 'hacking_rate_functional']:\n        if k in m and m[k] is not None:\n            h1_rate = m[k]\n            break\n    \n    # genuine\n    genuine_count = None\n    for k in ['genuine_count', 'eval_genuine_count', 'non_hacking_count']:\n        if k in m and m[k] is not None:\n            genuine_count = m[k]\n            break\n    \n    genuine_rate = None\n    for k in ['genuine_rate', 'eval_genuine_rate', 'non_hacking_rate', 'eval_greedy_genuine_rate']:\n        if k in m and m[k] is not None:\n            genuine_rate = m[k]\n            break\n    \n    # Check nested h7_classification\n    h7c = m.get('h7_classification', {})\n    if isinstance(h7c, dict):\n        if h7_count is None and 'h7_strict' in h7c:\n            h7_count = h7c['h7_strict']\n        if h7_rate is None and 'h7_rate' in h7c:\n            h7_rate = h7c['h7_rate']\n        if h1_count is None and 'h1_strict' in h7c:\n            h1_count = h7c['h1_strict']\n        if h1_rate is None and 'h1_rate' in h7c:\n            h1_rate = h7c['h1_rate']\n        if genuine_count is None and 'genuine_count' in h7c:\n            genuine_count = h7c['genuine_count']\n        if genuine_rate is None and 'genuine_rate' in h7c:\n            genuine_rate = h7c['genuine_rate']\n    \n    # Normalize rates > 1 (percentage form)\n    h7_rate = normalize_rate(h7_rate)\n    h1_rate = normalize_rate(h1_rate)\n    genuine_rate = normalize_rate(genuine_rate)\n    \n    # Fill in missing counts from rates if n_proved available\n    if n_proved:\n        if h7_count is None and h7_rate is not None:\n            h7_count = int(round(h7_rate * n_proved))\n        if h1_count is None and h1_rate is not None:\n            h1_count = int(round(h1_rate * n_proved))\n        if genuine_count is None and genuine_rate is not None:\n            genuine_count = int(round(genuine_rate * n_proved))\n    \n    # Fill in missing rates from counts if n_proved available\n    if n_proved and n_proved > 0:\n        if h7_rate is None and h7_count is not None:\n            h7_rate = round(h7_count / n_proved, 4)\n        if h1_rate is None and h1_count is not None:\n            h1_rate = round(h1_count / n_proved, 4)\n        if genuine_rate is None and genuine_count is not None:\n            genuine_rate = round(genuine_count / n_proved, 4)\n    \n    # Only return if we have at least some classification data\n    has_any = any(v is not None for v in [h7_count, h7_rate, h1_count, h1_rate, genuine_count, genuine_rate])\n    if not has_any:\n        return None\n    \n    spec = exp.get('spec', {})\n    condition = infer_condition(exp_id)\n    seed = infer_seed(exp_id, spec)\n    \n    return {\n        'experiment_id': exp_id,\n        'condition': condition,\n        'seed': seed,\n        'n_proved': n_proved,\n        'h7_count': h7_count,\n        'h1_count': h1_count,\n        'genuine_count': genuine_count,\n        'h7_rate': h7_rate,\n        'h1_rate': h1_rate,\n        'genuine_rate': genuine_rate,\n    }\n\n# Extract all\nresults = []\nfor exp_id in sorted(experiments.keys()):\n    exp = experiments[exp_id]\n    row = extract_classification(exp_id, exp)\n    if row:\n        results.append(row)\n\n# Print formatted table\nprint(f\"Extracted {len(results)} experiments with classification data:\\n\")\nprint(f\"{'experiment_id':45s} {'condition':25s} {'seed':5s} {'n_prov':>6s} {'h7_cnt':>6s} {'h1_cnt':>6s} {'gen_cnt':>7s} {'h7_rate':>7s} {'h1_rate':>7s} {'gen_rt':>7s}\")\nprint(\"-\" * 145)\nfor r in results:\n    def fmt(v):\n        if v is None:\n            return \"-\"\n        if isinstance(v, float):\n            return f\"{v:.3f}\"\n        return str(v)\n    \n    print(f\"{r['experiment_id']:45s} {r['condition']:25s} {str(r['seed'] or '-'):5s} \"\n          f\"{fmt(r['n_proved']):>6s} {fmt(r['h7_count']):>6s} {fmt(r['h1_count']):>6s} \"\n          f\"{fmt(r['genuine_count']):>7s} {fmt(r['h7_rate']):>7s} {fmt(r['h1_rate']):>7s} \"\n          f\"{fmt(r['genuine_rate']):>7s}\")\n\n# Group by condition for summary\nprint(\"\\n\\n=== Summary by condition ===\")\nconditions = {}\nfor r in results:\n    c = r['condition']\n    if c not in conditions:\n        conditions[c] = []\n    conditions[c].append(r)\n\nfor c in sorted(conditions.keys()):\n    exps = conditions[c]\n    seeds = [e['seed'] for e in exps]\n    print(f\"\\n{c}: {len(exps)} experiments, seeds: {seeds}\")\n    for e in exps:\n        print(f\"  {e['experiment_id']:40s} seed={e['seed']}  n_proved={e['n_proved']}  h7={e['h7_count']}  h1={e['h1_count']}  genuine={e['genuine_count']}\")\n\n# Write output\noutpath = \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/registry_extract.json\"\nos.makedirs(os.path.dirname(outpath), exist_ok=True)\nwith open(outpath, 'w') as f:\n    json.dump(results, f, indent=2)\n\nprint(f\"\\n\\nWritten {len(results)} records to {outpath}\")\nPYEOF\n",
  "description": "Build final extraction with normalized rates and derived counts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_wilson-ci_20260515T075227",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 << 'PYEOF'\nimport json\nimport os\n\nfpath = \"/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/d80fed44-dadc-4e6f-9333-1a32a5430a13/tool-results/mcp-agent-ml-research-read_registry-1778831563449.txt\"\n\nwith open(fpath, 'r') as f:\n    raw = f.read()\n\nouter = json.loads(raw)\nregistry = json.loads(outer['result'])\nexperiments = registry['data']['experiments']\n\ndef infer_condition(exp_id):\n    eid = exp_id.lower()\n    if 'sft' in eid:\n        return 'SFT'\n    if 'o1-ablation' in eid:\n        return 'o1-ablation'\n    if 'prolog-exec' in eid:\n        return 'Prolog exec-only'\n    if 'prolog-sta' in eid:\n        return 'Prolog STA'\n    if 'sta-phase0' in eid:\n        return 'STA phase0 baseline'\n    if 'sta-phase1-exec-only' in eid:\n        return 'STA exec-only'\n    if 'sta-phase1-exec-sta' in eid:\n        return 'STA exec+STA'\n    if 'sta-gt-isr' in eid:\n        return 'STA GT ISR baseline'\n    if 'downstream-nli' in eid:\n        return 'downstream NLI'\n    if 'linear' in eid:\n        return 'linear'\n    if 'extended-1000' in eid:\n        return 'extended-1000'\n    if 'hacking-taxonomy' in eid:\n        return 'hacking-taxonomy'\n    if 'random-reward' in eid:\n        return 'Random reward (no STA)'\n    if 'exec-only' in eid or (eid.startswith('plan001') and 'exec' in eid) or eid.startswith('plan003-eval-exec'):\n        return 'exec-only'\n    # Random β variants\n    if 'additive-random' in eid or eid.startswith('plan017') or eid.startswith('plan018'):\n        if 'b01' in eid:\n            return 'Random β=0.1'\n        return 'Random β=0.3'\n    if 'random-b0' in eid or eid.startswith('exp1-random'):\n        if 'b01' in eid:\n            return 'Random β=0.1'\n        return 'Random β=0.3'\n    # ISR β variants\n    if 'additive-b0' in eid or eid.startswith('plan002'):\n        if 'b01' in eid:\n            return 'ISR β=0.1'\n        if 'b03' in eid:\n            return 'ISR β=0.3'\n        return 'ISR β=0.1'\n    if 'isr-b0' in eid or eid.startswith('exp1-isr'):\n        if 'b01' in eid:\n            return 'ISR β=0.1'\n        return 'ISR β=0.3'\n    return 'unknown'\n\ndef infer_seed(exp_id, spec):\n    seed = spec.get('seed') if isinstance(spec, dict) else None\n    if seed:\n        return f\"s{seed}\"\n    eid = exp_id.lower()\n    if '-s42' in eid:\n        return 's42'\n    elif '-s43' in eid:\n        return 's43'\n    elif '-s44' in eid:\n        return 's44'\n    return None\n\ndef normalize_rate(val):\n    \"\"\"Normalize rates that might be in percentage form (>1) to [0,1] fraction.\"\"\"\n    if val is None:\n        return None\n    if isinstance(val, (int, float)) and val > 1:\n        return round(val / 100, 4)\n    return val\n\ndef extract_classification(exp_id, exp):\n    m = exp.get('metrics', {})\n    if not m or not isinstance(m, dict):\n        return None\n    \n    # Get n_proved from multiple sources\n    n_proved = m.get('n_proved') or m.get('eval_n_proved') or m.get('eval_greedy_n_proved') or m.get('eval_proved_count') or m.get('proved_count')\n    if not n_proved:\n        pr = m.get('eval_prove_rate') or m.get('prove_rate')\n        n = m.get('eval_n_problems') or m.get('n_problems', 100)\n        if pr is not None and n:\n            n_proved = int(round(pr * n)) if pr <= 1 else int(pr)\n    \n    # h7\n    h7_count = None\n    for k in ['h7_count', 'eval_h7_strict_count', 'eval_greedy_h7_count', 'eval_h7_count']:\n        if k in m and m[k] is not None:\n            h7_count = m[k]\n            break\n    \n    h7_rate = None\n    for k in ['h7_rate', 'eval_h7_strict_rate', 'eval_greedy_h7_rate', 'hacking_rate_strict_h7',\n              'h7_rate_calibrated', 'eval_h7_rate', 'h7_functional_rate']:\n        if k in m and m[k] is not None:\n            h7_rate = m[k]\n            break\n    \n    # h1\n    h1_count = None\n    for k in ['h1_count', 'eval_h1_strict_count', 'eval_greedy_h1_count']:\n        if k in m and m[k] is not None:\n            h1_count = m[k]\n            break\n    \n    h1_rate = None\n    for k in ['h1_rate', 'eval_h1_strict_rate', 'eval_greedy_h1_rate', 'hacking_rate_functional']:\n        if k in m and m[k] is not None:\n            h1_rate = m[k]\n            break\n    \n    # genuine\n    genuine_count = None\n    for k in ['genuine_count', 'eval_genuine_count', 'non_hacking_count']:\n        if k in m and m[k] is not None:\n            genuine_count = m[k]\n            break\n    \n    genuine_rate = None\n    for k in ['genuine_rate', 'eval_genuine_rate', 'non_hacking_rate', 'eval_greedy_genuine_rate']:\n        if k in m and m[k] is not None:\n            genuine_rate = m[k]\n            break\n    \n    # Check nested h7_classification\n    h7c = m.get('h7_classification', {})\n    if isinstance(h7c, dict):\n        if h7_count is None and 'h7_strict' in h7c:\n            h7_count = h7c['h7_strict']\n        if h7_rate is None and 'h7_rate' in h7c:\n            h7_rate = h7c['h7_rate']\n        if h1_count is None and 'h1_strict' in h7c:\n            h1_count = h7c['h1_strict']\n        if h1_rate is None and 'h1_rate' in h7c:\n            h1_rate = h7c['h1_rate']\n        if genuine_count is None and 'genuine_count' in h7c:\n            genuine_count = h7c['genuine_count']\n        if genuine_rate is None and 'genuine_rate' in h7c:\n            genuine_rate = h7c['genuine_rate']\n    \n    # Normalize rates > 1 (percentage form)\n    h7_rate = normalize_rate(h7_rate)\n    h1_rate = normalize_rate(h1_rate)\n    genuine_rate = normalize_rate(genuine_rate)\n    \n    # Fill in missing counts from rates if n_proved available\n    if n_proved:\n        if h7_count is None and h7_rate is not None:\n            h7_count = int(round(h7_rate * n_proved))\n        if h1_count is None and h1_rate is not None:\n            h1_count = int(round(h1_rate * n_proved))\n        if genuine_count is None and genuine_rate is not None:\n            genuine_count = int(round(genuine_rate * n_proved))\n    \n    # Fill in missing rates from counts if n_proved available\n    if n_proved and n_proved > 0:\n        if h7_rate is None and h7_count is not None:\n            h7_rate = round(h7_count / n_proved, 4)\n        if h1_rate is None and h1_count is not None:\n            h1_rate = round(h1_count / n_proved, 4)\n        if genuine_rate is None and genuine_count is not None:\n            genuine_rate = round(genuine_count / n_proved, 4)\n    \n    # Only return if we have at least some classification data\n    has_any = any(v is not None for v in [h7_count, h7_rate, h1_count, h1_rate, genuine_count, genuine_rate])\n    if not has_any:\n        return None\n    \n    spec = exp.get('spec', {})\n    condition = infer_condition(exp_id)\n    seed = infer_seed(exp_id, spec)\n    \n    return {\n        'experiment_id': exp_id,\n        'condition': condition,\n        'seed': seed,\n        'n_proved': n_proved,\n        'h7_count': h7_count,\n        'h1_count': h1_count,\n        'genuine_count': genuine_count,\n        'h7_rate': h7_rate,\n        'h1_rate': h1_rate,\n        'genuine_rate': genuine_rate,\n    }\n\n# Extract all\nresults = []\nfor exp_id in sorted(experiments.keys()):\n    exp = experiments[exp_id]\n    row = extract_classification(exp_id, exp)\n    if row:\n        results.append(row)\n\n# Print formatted table\nprint(f\"Extracted {len(results)} experiments with classification data:\\n\")\nprint(f\"{'experiment_id':45s} {'condition':25s} {'seed':5s} {'n_prov':>6s} {'h7_cnt':>6s} {'h1_cnt':>6s} {'gen_cnt':>7s} {'h7_rate':>7s} {'h1_rate':>7s} {'gen_rt':>7s}\")\nprint(\"-\" * 145)\nfor r in results:\n    def fmt(v):\n        if v is None:\n            return \"-\"\n        if isinstance(v, float):\n            return f\"{v:.3f}\"\n        return str(v)\n    \n    print(f\"{r['experiment_id']:45s} {r['condition']:25s} {str(r['seed'] or '-'):5s} \"\n          f\"{fmt(r['n_proved']):>6s} {fmt(r['h7_count']):>6s} {fmt(r['h1_count']):>6s} \"\n          f\"{fmt(r['genuine_count']):>7s} {fmt(r['h7_rate']):>7s} {fmt(r['h1_rate']):>7s} \"\n          f\"{fmt(r['genuine_rate']):>7s}\")\n\n# Group by condition for summary\nprint(\"\\n\\n=== Summary by condition ===\")\nconditions = {}\nfor r in results:\n    c = r['condition']\n    if c not in conditions:\n        conditions[c] = []\n    conditions[c].append(r)\n\nfor c in sorted(conditions.keys()):\n    exps = conditions[c]\n    seeds = [e['seed'] for e in exps]\n    print(f\"\\n{c}: {len(exps)} experiments, seeds: {seeds}\")\n    for e in exps:\n        print(f\"  {e['experiment_id']:40s} seed={e['seed']}  n_proved={e['n_proved']}  h7={e['h7_count']}  h1={e['h1_count']}  genuine={e['genuine_count']}\")\n\n# Write output\noutpath = \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/registry_extract.json\"\nos.makedirs(os.path.dirname(outpath), exist_ok=True)\nwith open(outpath, 'w') as f:\n    json.dump(results, f, indent=2)\n\nprint(f\"\\n\\nWritten {len(results)} records to {outpath}\")\nPYEOF\n",
    "description": "Build final extraction with normalized rates and derived counts"
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-15T07:59:05.939071+00:00_

Extracted 23 experiments with classification data:

experiment_id                                 condition                 seed  n_prov h7_cnt h1_cnt gen_cnt h7_rate h1_rate  gen_rt
-------------------------------------------------------------------------------------------------------------------------------------------------
exp1-isr-b03-s43                              ISR β=0.3                 s43       91      2     30      61   0.022   0.330   0.670
exp1-isr-b03-s43-r3                           ISR β=0.3                 s43       86      4     59      23   0.047   0.686   0.267
exp1-isr-b03-s44-r2                           ISR β=0.3                 s44       95     95      0       0       1       0       0
exp1-random-b03-s43                           Random β=0.3              s43       79      0      8      71       0   0.101   0.899
exp1-random-b03-s43-r4                        Random β=0.3              s43       92      7     90       2   0.076   0.978   0.022
exp1-random-b03-s44-r2                        Random β=0.3              s44       23      0     23       0       0       1       0
plan001-exec-only-s42-r2                      exec-only                 s42       93      0     81      12       0   0.871   0.129
plan001-exec-only-s43-r4                      exec-only                 s43       13      0     13       0       0       1       0
plan001-exec-only-s44                         exec-only                 s44       98     97      0       0       1       0       0
plan002-additive-b01-s42                      ISR β=0.1                 s42       81     13     42      25   0.160   0.519   0.309
plan002-additive-b01-s43                      ISR β=0.1                 s43       61     59      -       -   0.967       -       -
plan002-additive-b01-s44                      ISR β=0.1                 s44       89     77      -       -   0.865       -       -
plan002-additive-b03-s42                      ISR β=0.3                 s42       18      0     14 
…[truncated 4116 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_wilson-ci_20260515T075227",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-15T07:59:05.939251+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"import json; data = json.load(open('/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/registry_extract.json')); print(f'Records: {len(data)}'); print(json.dumps(data[0], indent=2))\"",
  "description": "Verify output JSON file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_wilson-ci_20260515T075227",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"import json; data = json.load(open('/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/registry_extract.json')); print(f'Records: {len(data)}'); print(json.dumps(data[0], indent=2))\"",
    "description": "Verify output JSON file"
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-15T07:59:05.939380+00:00_

Records: 23
{
  "experiment_id": "exp1-isr-b03-s43",
  "condition": "ISR \u03b2=0.3",
  "seed": "s43",
  "n_proved": 91,
  "h7_count": 2,
  "h1_count": 30,
  "genuine_count": 61,
  "h7_rate": 0.022,
  "h1_rate": 0.3297,
  "genuine_rate": 0.6703
}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_wilson-ci_20260515T075227",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-15T07:59:05.939549+00:00_

The extraction is complete. Here is what was done and the key findings:

**Output file**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/registry_extract.json` -- 23 records.

**Data processing notes**:
- Rates stored as >1 (percentage form, e.g. `h1_rate: 93.2`) were normalized to [0,1] fractions
- Missing counts were derived from rates * n_proved where possible, and vice versa
- n_proved was sourced from `n_proved`, `eval_n_proved`, `eval_proved_count`, or computed as `prove_rate * n_problems`
- Multiple naming conventions were unified (e.g. `eval_h7_strict_count` -> `h7_count`, `hacking_rate_strict_h7` -> `h7_rate`, `eval_genuine_count` -> `genuine_count`)

**Coverage for the requested conditions**:

| Condition | Seeds found | Experiments |
|-----------|------------|-------------|
| exec-only | s42, s43, s44 | 3 (plan001 series) |
| ISR β=0.1 | s42, s43, s44 | 3 (plan002 series) |
| ISR β=0.3 | s42, s43, s44 | 4 (exp1 + plan002 series; s43 has 2 runs) |
| Random β=0.1 | s43 only | 1 (plan018 series; s42 and s44 lack classification) |
| Random β=0.3 | s42, s43, s44 | 4 (exp1 + plan017 series; s43 has 2 runs) |
| SFT | s42, s43 | 2 (plan009 series) |

**Gaps**: Random β=0.1 is missing s42 and s44 classification data (plan018-additive-random-b01-s42 has n_proved=79 but no h7/h1/genuine breakdown; plan018-additive-random-b01-s44 has n_proved=89 but also no breakdown). ISR β=0.1 s43 and s44 have h7_rate_calibrated but no h1/genuine breakdown. Some experiments have duplicate runs (retries r2, r3, r4) with different classification results -- the latest retry is typically the canonical one.
agentId: a135cccaf5aa264c2 (use SendMessage with to: 'a135cccaf5aa264c2' to continue this agent)
&lt;usage>total_tokens: 44367
tool_uses: 15
duration_ms: 227155&lt;/usage>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_wilson-ci_20260515T075227",
  "tool": "Agent",
  "elapsed_ms": 5
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-15T07:59:05.939747+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/registry_extract.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_wilson-ci_20260515T075227",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/registry_extract.json"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-15T07:59:05.939967+00:00_

1	[
2	  {
3	    "experiment_id": "exp1-isr-b03-s43",
4	    "condition": "ISR \u03b2=0.3",
5	    "seed": "s43",
6	    "n_proved": 91,
7	    "h7_count": 2,
8	    "h1_count": 30,
9	    "genuine_count": 61,
10	    "h7_rate": 0.022,
11	    "h1_rate": 0.3297,
12	    "genuine_rate": 0.6703
13	  },
14	  {
15	    "experiment_id": "exp1-isr-b03-s43-r3",
16	    "condition": "ISR \u03b2=0.3",
17	    "seed": "s43",
18	    "n_proved": 86,
19	    "h7_count": 4,
20	    "h1_count": 59,
21	    "genuine_count": 23,
22	    "h7_rate": 0.047,
23	    "h1_rate": 0.686,
24	    "genuine_rate": 0.267
25	  },
26	  {
27	    "experiment_id": "exp1-isr-b03-s44-r2",
28	    "condition": "ISR \u03b2=0.3",
29	    "seed": "s44",
30	    "n_proved": 95,
31	    "h7_count": 95,
32	    "h1_count": 0,
33	    "genuine_count": 0,
34	    "h7_rate": 1,
35	    "h1_rate": 0,
36	    "genuine_rate": 0
37	  },
38	  {
39	    "experiment_id": "exp1-random-b03-s43",
40	    "condition": "Random \u03b2=0.3",
41	    "seed": "s43",
42	    "n_proved": 79,
43	    "h7_count": 0,
44	    "h1_count": 8,
45	    "genuine_count": 71,
46	    "h7_rate": 0,
47	    "h1_rate": 0.1013,
48	    "genuine_rate": 0.8987
49	  },
50	  {
51	    "experiment_id": "exp1-random-b03-s43-r4",
52	    "condition": "Random \u03b2=0.3",
53	    "seed": "s43",
54	    "n_proved": 92,
55	    "h7_count": 7,
56	    "h1_count": 90,
57	    "genuine_count": 2,
58	    "h7_rate": 0.076,
59	    "h1_rate": 0.978,
60	    "genuine_rate": 0.022
61	  },
62	  {
63	    "experiment_id": "exp1-random-b03-s44-r2",
64	    "condition": "Random \u03b2=0.3",
65	    "seed": "s44",
66	    "n_proved": 23,
67	    "h7_count": 0,
68	    "h1_count": 23,
69	    "genuine_count": 0,
70	    "h7_rate": 0,
71	    "h1_rate": 1,
72	    "genuine_rate": 0
73	  },
74	  {
75	    "experiment_id": "plan001-exec-only-s42-r2",
76	    "condition": "exec-only",
77	    "seed": "s42",
78	    "n_proved": 93,
79	    "h7_count": 0,
80	    "h1_count": 81,
81	    "genuine_count": 12,
82	    "h7_rate": 0,
83	    
…[truncated 4944 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_wilson-ci_20260515T075227",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-15T07:59:05.940219+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/wilson_ci.py",
  "content": "#!/usr/bin/env python3\n\"\"\"Wilson score CI + Fisher exact test for solver-trace-ablation classification data.\"\"\"\n\nimport json\nimport csv\nimport math\nfrom scipy import stats\nfrom collections import defaultdict\n\ndef wilson_ci(k, n, alpha=0.05):\n    \"\"\"Wilson score interval for binomial proportion.\"\"\"\n    if n == 0 or k is None:\n        return (None, None, None)\n    p_hat = k / n\n    z = stats.norm.ppf(1 - alpha / 2)\n    denom = 1 + z**2 / n\n    center = (p_hat + z**2 / (2 * n)) / denom\n    margin = z * math.sqrt(p_hat * (1 - p_hat) / n + z**2 / (4 * n**2)) / denom\n    return (p_hat, max(0, center - margin), min(1, center + margin))\n\n\ndef pick_canonical(experiments):\n    \"\"\"For each (condition, seed), pick the latest retry.\"\"\"\n    by_key = defaultdict(list)\n    for exp in experiments:\n        key = (exp[\"condition\"], exp[\"seed\"])\n        by_key[key].append(exp)\n\n    canonical = []\n    for key, exps in by_key.items():\n        def retry_order(e):\n            eid = e[\"experiment_id\"]\n            if \"-r\" in eid:\n                try:\n                    return int(eid.split(\"-r\")[-1])\n                except ValueError:\n                    return 0\n            return 0\n        exps.sort(key=retry_order)\n        canonical.append(exps[-1])\n    return canonical\n\n\ndef main():\n    with open(\"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/registry_extract.json\") as f:\n        all_experiments = json.load(f)\n\n    canonical = pick_canonical(all_experiments)\n    canonical.sort(key=lambda e: (e[\"condition\"], e[\"seed\"]))\n\n    # --- Per-experiment Wilson CIs ---\n    csv_rows = []\n    per_exp_results = []\n\n    for exp in canonical:\n        n = exp[\"n_proved\"]\n        if n is None or n == 0:\n            continue\n\n        row = {\n            \"experiment_id\": exp[\"experiment_id\"],\n            \"condition\": exp[\"condition\"],\n            \"seed\": exp[\"seed\"],\n            \"n_proved\": n,\n        }\n\n        for cat in [\"h7\", \"h1\", \"genuine\"]:\n            k = exp.get(f\"{cat}_count\")\n            rate, ci_lo, ci_hi = wilson_ci(k, n)\n            row[f\"{cat}_count\"] = k\n            row[f\"{cat}_rate\"] = rate\n            row[f\"{cat}_ci_lo\"] = ci_lo\n            row[f\"{cat}_ci_hi\"] = ci_hi\n\n        csv_rows.append(row)\n        per_exp_results.append(row)\n\n    # --- Pooled analysis for multi-seed conditions ---\n    CONDITIONS_TO_POOL = [\n        \"exec-only\", \"ISR β=0.1\", \"Random β=0.1\",\n        \"ISR β=0.3\", \"Random β=0.3\", \"SFT\",\n    ]\n\n    pooled_results = {}\n    for cond in CONDITIONS_TO_POOL:\n        cond_exps = [e for e in per_exp_results if e[\"condition\"] == cond]\n        if not cond_exps:\n            continue\n\n        pool = {\"condition\": cond, \"n_seeds\": len(cond_exps), \"seeds\": [e[\"seed\"] for e in cond_exps]}\n        total_n = sum(e[\"n_proved\"] for e in cond_exps)\n        pool[\"n_proved_total\"] = total_n\n\n        for cat in [\"h7\", \"h1\", \"genuine\"]:\n            counts = [e[f\"{cat}_count\"] for e in cond_exps if e[f\"{cat}_count\"] is not None]\n            if not counts:\n                pool[f\"{cat}_pooled_count\"] = None\n                pool[f\"{cat}_pooled_rate\"] = None\n                pool[f\"{cat}_pooled_ci_lo\"] = None\n                pool[f\"{cat}_pooled_ci_hi\"] = None\n                continue\n            n_with_data = sum(e[\"n_proved\"] for e in cond_exps if e[f\"{cat}_count\"] is not None)\n            total_k = sum(counts)\n            rate, ci_lo, ci_hi = wilson_ci(total_k, n_with_data)\n            pool[f\"{cat}_pooled_count\"] = total_k\n            pool[f\"{cat}_pooled_n\"] = n_with_data\n            pool[f\"{cat}_pooled_rate\"] = rate\n            pool[f\"{cat}_pooled_ci_lo\"] = ci_lo\n            pool[f\"{cat}_pooled_ci_hi\"] = ci_hi\n\n        pooled_results[cond] = pool\n\n    # --- Fisher exact tests ---\n    fisher_tests = []\n\n    comparisons = [\n        (\"ISR β=0.1\", \"Random β=0.1\", \"genuine\"),\n        (\"ISR β=0.1\", \"Random β=0.1\", \"h7\"),\n        (\"ISR β=0.3\", \"Random β=0.3\", \"genuine\"),\n        (\"ISR β=0.3\", \"Random β=0.3\", \"h7\"),\n        (\"ISR β=0.1\", \"Random β=0.1\", \"h1\"),\n        (\"ISR β=0.3\", \"Random β=0.3\", \"h1\"),\n        (\"ISR β=0.1\", \"exec-only\", \"genuine\"),\n        (\"ISR β=0.3\", \"exec-only\", \"genuine\"),\n        (\"Random β=0.1\", \"exec-only\", \"genuine\"),\n        (\"Random β=0.3\", \"exec-only\", \"genuine\"),\n    ]\n\n    for cond_a, cond_b, cat in comparisons:\n        pa = pooled_results.get(cond_a)\n        pb = pooled_results.get(cond_b)\n        if not pa or not pb:\n            continue\n        ka = pa.get(f\"{cat}_pooled_count\")\n        na = pa.get(f\"{cat}_pooled_n\")\n        kb = pb.get(f\"{cat}_pooled_count\")\n        nb = pb.get(f\"{cat}_pooled_n\")\n        if ka is None or kb is None or na is None or nb is None:\n            continue\n\n        table = [[ka, na - ka], [kb, nb - kb]]\n        odds_ratio, p_value = stats.fisher_exact(table)\n        fisher_tests.append({\n            \"comparison\": f\"{cond_a} vs {cond_b}\",\n            \"category\": cat,\n            \"a_count\": ka, \"a_n\": na, \"a_rate\": ka / na if na > 0 else None,\n            \"b_count\": kb, \"b_n\": nb, \"b_rate\": kb / nb if nb > 0 else None,\n            \"odds_ratio\": odds_ratio,\n            \"p_value\": p_value,\n            \"significant_005\": p_value < 0.05,\n            \"significant_001\": p_value < 0.01,\n        })\n\n    # --- Write CSV ---\n    csv_path = \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/wilson_ci_results.csv\"\n    fieldnames = [\n        \"condition\", \"seed\", \"experiment_id\", \"n_proved\",\n        \"h7_count\", \"h7_rate\", \"h7_ci_lo\", \"h7_ci_hi\",\n        \"h1_count\", \"h1_rate\", \"h1_ci_lo\", \"h1_ci_hi\",\n        \"genuine_count\", \"genuine_rate\", \"genuine_ci_lo\", \"genuine_ci_hi\",\n    ]\n    with open(csv_path, \"w\", newline=\"\") as f:\n        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction=\"ignore\")\n        writer.writeheader()\n        for row in csv_rows:\n            writer.writerow(row)\n\n    # --- Write JSON ---\n    json_path = \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/wilson_ci_results.json\"\n    output = {\n        \"per_experiment\": per_exp_results,\n        \"pooled\": pooled_results,\n        \"fisher_tests\": fisher_tests,\n    }\n    with open(json_path, \"w\") as f:\n        json.dump(output, f, indent=2, ensure_ascii=False)\n\n    # --- Print summary ---\n    print(\"=\" * 80)\n    print(\"WILSON SCORE 95% CI — PER EXPERIMENT\")\n    print(\"=\" * 80)\n    for r in per_exp_results:\n        print(f\"\\n{r['experiment_id']} ({r['condition']}, {r['seed']}, n={r['n_proved']})\")\n        for cat in [\"h7\", \"h1\", \"genuine\"]:\n            k = r[f\"{cat}_count\"]\n            rate = r[f\"{cat}_rate\"]\n            lo = r[f\"{cat}_ci_lo\"]\n            hi = r[f\"{cat}_ci_hi\"]\n            if rate is not None:\n                print(f\"  {cat:>7}: {k:3d}/{r['n_proved']:3d} = {rate:.3f}  [{lo:.3f}, {hi:.3f}]\")\n            else:\n                print(f\"  {cat:>7}: N/A\")\n\n    print(\"\\n\" + \"=\" * 80)\n    print(\"POOLED WILSON SCORE 95% CI\")\n    print(\"=\" * 80)\n    for cond in CONDITIONS_TO_POOL:\n        p = pooled_results.get(cond)\n        if not p:\n            continue\n        print(f\"\\n{cond} (seeds={p['seeds']}, total_n={p['n_proved_total']})\")\n        for cat in [\"h7\", \"h1\", \"genuine\"]:\n            k = p.get(f\"{cat}_pooled_count\")\n            n = p.get(f\"{cat}_pooled_n\")\n            rate = p.get(f\"{cat}_pooled_rate\")\n            lo = p.get(f\"{cat}_pooled_ci_lo\")\n            hi = p.get(f\"{cat}_pooled_ci_hi\")\n            if rate is not None:\n                print(f\"  {cat:>7}: {k:3d}/{n:3d} = {rate:.3f}  [{lo:.3f}, {hi:.3f}]\")\n            else:\n                print(f\"  {cat:>7}: N/A (missing data for some seeds)\")\n\n    print(\"\\n\" + \"=\" * 80)\n    print(\"FISHER EXACT TESTS\")\n    print(\"=\" * 80)\n    for t in fisher_tests:\n        sig = \"***\" if t[\"significant_001\"] else (\"*\" if t[\"significant_005\"] else \"ns\")\n        print(f\"\\n{t['comparison']} — {t['category']}\")\n        print(f\"  A: {t['a_count']}/{t['a_n']} = {t['a_rate']:.3f}\")\n        print(f\"  B: {t['b_count']}/{t['b_n']} = {t['b_rate']:.3f}\")\n        print(f\"  OR = {t['odds_ratio']:.3f}, p = {t['p_value']:.4f} {sig}\")\n\n\nif __name__ == \"__main__\":\n    main()\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_wilson-ci_20260515T075227",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/wilson_ci.py",
    "content": "#!/usr/bin/env python3\n\"\"\"Wilson score CI + Fisher exact test for solver-trace-ablation classification data.\"\"\"\n\nimport json\nimport csv\nimport math\nfrom scipy import stats\nfrom collections import defaultdict\n\ndef wilson_ci(k, n, alpha=0.05):\n    \"\"\"Wilson score interval for binomial proportion.\"\"\"\n    if n == 0 or k is None:\n        return (None, None, None)\n    p_hat = k / n\n    z = stats.norm.ppf(1 - alpha / 2)\n    denom = 1 + z**2 / n\n    center = (p_hat + z**2 / (2 * n)) / denom\n    margin = z * math.sqrt(p_hat * (1 - p_hat) / n + z**2 / (4 * n**2)) / denom\n    return (p_hat, max(0, center - margin), min(1, center + margin))\n\n\ndef pick_canonical(experiments):\n    \"\"\"For each (condition, seed), pick the latest retry.\"\"\"\n    by_key = defaultdict(list)\n    for exp in experiments:\n        key = (exp[\"condition\"], exp[\"seed\"])\n        by_key[key].append(exp)\n\n    canonical = []\n    for key, exps in by_key.items():\n        def retry_order(e):\n            eid = e[\"experiment_id\"]\n            if \"-r\" in eid:\n                try:\n                    return int(eid.split(\"-r\")[-1])\n                except ValueError:\n                    return 0\n            return 0\n        exps.sort(key=retry_order)\n        canonical.append(exps[-1])\n    return canonical\n\n\ndef main():\n    with open(\"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/registry_extract.json\") as f:\n        all_experiments = json.load(f)\n\n    canonical = pick_canonical(all_experiments)\n    canonical.sort(key=lambda e: (e[\"condition\"], e[\"seed\"]))\n\n    # --- Per-experiment Wilson CIs ---\n    csv_rows = []\n    per_exp_results = []\n\n    for exp in canonical:\n        n = exp[\"n_proved\"]\n        if n is None or n == 0:\n            continue\n\n        row = {\n            \"experiment_id\": exp[\"experiment_id\"],\n            \"condition\": exp[\"condition\"],\n            \"seed\": exp[\"seed\"],\n            \"n_proved\": n,\n        }\n\n        for cat in [\"h7\", \"h1\", \"genuine\"]:\n            k = exp.get(f\"{cat}_count\")\n            rate, ci_lo, ci_hi = wilson_ci(k, n)\n            row[f\"{cat}_count\"] = k\n            row[f\"{cat}_rate\"] = rate\n            row[f\"{cat}_ci_lo\"] = ci_lo\n            row[f\"{cat}_ci_hi\"] = ci_hi\n\n        csv_rows.append(row)\n        per_exp_results.append(row)\n\n    # --- Pooled analysis for multi-seed conditions ---\n    CONDITIONS_TO_POOL = [\n        \"exec-only\", \"ISR β=0.1\", \"Random β=0.1\",\n        \"ISR β=0.3\", \"Random β=0.3\", \"SFT\",\n    ]\n\n    pooled_results = {}\n    for cond in CONDITIONS_TO_POOL:\n        cond_exps = [e for e in per_exp_results if e[\"condition\"] == cond]\n        if not cond_exps:\n            continue\n\n        pool = {\"condition\": cond, \"n_seeds\": len(cond_exps), \"seeds\": [e[\"seed\"] for e in cond_exps]}\n        total_n = sum(e[\"n_proved\"] for e in cond_exps)\n        pool[\"n_proved_total\"] = total_n\n\n        for cat in [\"h7\", \"h1\", \"genuine\"]:\n            counts = [e[f\"{cat}_count\"] for e in cond_exps if e[f\"{cat}_count\"] is not None]\n            if not counts:\n                pool[f\"{cat}_pooled_count\"] = None\n                pool[f\"{cat}_pooled_rate\"] = None\n                pool[f\"{cat}_pooled_ci_lo\"] = None\n                pool[f\"{cat}_pooled_ci_hi\"] = None\n                continue\n            n_with_data = sum(e[\"n_proved\"] for e in cond_exps if e[f\"{cat}_count\"] is not None)\n            total_k = sum(counts)\n            rate, ci_lo, ci_hi = wilson_ci(total_k, n_with_data)\n            pool[f\"{cat}_pooled_count\"] = total_k\n            pool[f\"{cat}_pooled_n\"] = n_with_data\n            pool[f\"{cat}_pooled_rate\"] = rate\n            pool[f\"{cat}_pooled_ci_lo\"] = ci_lo\n            pool[f\"{cat}_pooled_ci_hi\"] = ci_hi\n\n        pooled_results[cond] = pool\n\n    # --- Fisher exact tests ---\n    fisher_tests = []\n\n    comparisons = [\n        (\"ISR β=0.1\", \"Random β=0.1\", \"genuine\"),\n        (\"ISR β=0.1\", \"Random β=0.1\", \"h7\"),\n        (\"ISR β=0.3\", \"Random β=0.3\", \"genuine\"),\n        (\"ISR β=0.3\", \"Random β=0.3\", \"h7\"),\n        (\"ISR β=0.1\", \"Random β=0.1\", \"h1\"),\n        (\"ISR β=0.3\", \"Random β=0.3\", \"h1\"),\n        (\"ISR β=0.1\", \"exec-only\", \"genuine\"),\n        (\"ISR β=0.3\", \"exec-only\", \"genuine\"),\n        (\"Random β=0.1\", \"exec-only\", \"genuine\"),\n        (\"Random β=0.3\", \"exec-only\", \"genuine\"),\n    ]\n\n    for cond_a, cond_b, cat in comparisons:\n        pa = pooled_results.get(cond_a)\n        pb = pooled_results.get(cond_b)\n        if not pa or not pb:\n            continue\n        ka = pa.get(f\"{cat}_pooled_count\")\n        na = pa.get(f\"{cat}_pooled_n\")\n        kb = pb.get(f\"{cat}_pooled_count\")\n        nb = pb.get(f\"{cat}_pooled_n\")\n        if ka is None or kb is None or na is None or nb is None:\n            continue\n\n        table = [[ka, na - ka], [kb, nb - kb]]\n        odds_ratio, p_value = stats.fisher_exact(table)\n        fisher_tests.append({\n            \"comparison\": f\"{cond_a} vs {cond_b}\",\n            \"category\": cat,\n            \"a_count\": ka, \"a_n\": na, \"a_rate\": ka / na if na > 0 else None,\n            \"b_count\": kb, \"b_n\": nb, \"b_rate\": kb / nb if nb > 0 else None,\n            \"odds_ratio\": odds_ratio,\n            \"p_value\": p_value,\n            \"significant_005\": p_value < 0.05,\n            \"significant_001\": p_value < 0.01,\n        })\n\n    # --- Write CSV ---\n    csv_path = \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/wilson_ci_results.csv\"\n    fieldnames = [\n        \"condition\", \"seed\", \"experiment_id\", \"n_proved\",\n        \"h7_count\", \"h7_rate\", \"h7_ci_lo\", \"h7_ci_hi\",\n        \"h1_count\", \"h1_rate\", \"h1_ci_lo\", \"h1_ci_hi\",\n        \"genuine_count\", \"genuine_rate\", \"genuine_ci_lo\", \"genuine_ci_hi\",\n    ]\n    with open(csv_path, \"w\", newline=\"\") as f:\n        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction=\"ignore\")\n        writer.writeheader()\n        for row in csv_rows:\n            writer.writerow(row)\n\n    # --- Write JSON ---\n    json_path = \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/wilson_ci_results.json\"\n    output = {\n        \"per_experiment\": per_exp_results,\n        \"pooled\": pooled_results,\n        \"fisher_tests\": fisher_tests,\n    }\n    with open(json_path, \"w\") as f:\n        json.dump(output, f, indent=2, ensure_ascii=False)\n\n    # --- Print summary ---\n    print(\"=\" * 80)\n    print(\"WILSON SCORE 95% CI — PER EXPERIMENT\")\n    print(\"=\" * 80)\n    for r in per_exp_results:\n        print(f\"\\n{r['experiment_id']} ({r['condition']}, {r['seed']}, n={r['n_proved']})\")\n        for cat in [\"h7\", \"h1\", \"genuine\"]:\n            k = r[f\"{cat}_count\"]\n            rate = r[f\"{cat}_rate\"]\n            lo = r[f\"{cat}_ci_lo\"]\n            hi = r[f\"{cat}_ci_hi\"]\n            if rate is not None:\n                print(f\"  {cat:>7}: {k:3d}/{r['n_proved']:3d} = {rate:.3f}  [{lo:.3f}, {hi:.3f}]\")\n            else:\n                print(f\"  {cat:>7}: N/A\")\n\n    print(\"\\n\" + \"=\" * 80)\n    print(\"POOLED WILSON SCORE 95% CI\")\n    print(\"=\" * 80)\n    for cond in CONDITIONS_TO_POOL:\n        p = pooled_results.get(cond)\n        if not p:\n            continue\n        print(f\"\\n{cond} (seeds={p['seeds']}, total_n={p['n_proved_total']})\")\n        for cat in [\"h7\", \"h1\", \"genuine\"]:\n            k = p.get(f\"{cat}_pooled_count\")\n            n = p.get(f\"{cat}_pooled_n\")\n            rate = p.get(f\"{cat}_pooled_rate\")\n            lo = p.get(f\"{cat}_pooled_ci_lo\")\n            hi = p.get(f\"{cat}_pooled_ci_hi\")\n            if rate is not None:\n                print(f\"  {cat:>7}: {k:3d}/{n:3d} = {rate:.3f}  [{lo:.3f}, {hi:.3f}]\")\n            else:\n                print(f\"  {cat:>7}: N/A (missing data for some seeds)\")\n\n    print(\"\\n\" + \"=\" * 80)\n    print(\"FISHER EXACT TESTS\")\n    print(\"=\" * 80)\n    for t in fisher_tests:\n        sig = \"***\" if t[\"significant_001\"] else (\"*\" if t[\"significant_005\"] else \"ns\")\n        print(f\"\\n{t['comparison']} — {t['category']}\")\n        print(f\"  A: {t['a_count']}/{t['a_n']} = {t['a_rate']:.3f}\")\n        print(f\"  B: {t['b_count']}/{t['b_n']} = {t['b_rate']:.3f}\")\n        print(f\"  OR = {t['odds_ratio']:.3f}, p = {t['p_value']:.4f} {sig}\")\n\n\nif __name__ == \"__main__\":\n    main()\n"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-15T07:59:05.940490+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/wilson_ci.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_wilson-ci_20260515T075227",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-15T07:59:05.940625+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python artifacts/wilson_ci.py",
  "description": "Run Wilson CI analysis script"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_wilson-ci_20260515T075227",
  "tool": "Bash",
  "tool_args": {
    "command": "python artifacts/wilson_ci.py",
    "description": "Run Wilson CI analysis script"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-15T07:59:05.940766+00:00_

Exit code 127
/bin/bash: line 1: python: command not found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_wilson-ci_20260515T075227",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-15T07:59:05.940885+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 artifacts/wilson_ci.py",
  "description": "Run Wilson CI analysis script"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_wilson-ci_20260515T075227",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 artifacts/wilson_ci.py",
    "description": "Run Wilson CI analysis script"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-15T07:59:05.941009+00:00_

Exit code 1
Traceback (most recent call last):
  File "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/wilson_ci.py", line 225, in &lt;module>
    main()
    ~~~~^^
  File "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/wilson_ci.py", line 176, in main
    json.dump(output, f, indent=2, ensure_ascii=False)
    ~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.14/json/__init__.py", line 181, in dump
    for chunk in iterable:
                 ^^^^^^^^
  File "/usr/lib/python3.14/json/encoder.py", line 444, in _iterencode
    yield from _iterencode_dict(o, _current_indent_level)
  File "/usr/lib/python3.14/json/encoder.py", line 413, in _iterencode_dict
    yield from chunks
  File "/usr/lib/python3.14/json/encoder.py", line 326, in _iterencode_list
    yield from chunks
  File "/usr/lib/python3.14/json/encoder.py", line 413, in _iterencode_dict
    yield from chunks
  File "/usr/lib/python3.14/json/encoder.py", line 451, in _iterencode
    newobj = _default(o)
  File "/usr/lib/python3.14/json/encoder.py", line 182, in default
    raise TypeError(f'Object of type {o.__class__.__name__} '
                    f'is not JSON serializable')
TypeError: Object of type bool is not JSON serializable
when serializing dict item 'significant_005'
when serializing list item 0
when serializing dict item 'fisher_tests'

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_wilson-ci_20260515T075227",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-15T07:59:05.941137+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/wilson_ci.py",
  "old_string": "            \"significant_005\": p_value < 0.05,\n            \"significant_001\": p_value < 0.01,",
  "new_string": "            \"significant_005\": bool(p_value < 0.05),\n            \"significant_001\": bool(p_value < 0.01),"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_wilson-ci_20260515T075227",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/wilson_ci.py",
    "old_string": "            \"significant_005\": p_value < 0.05,\n            \"significant_001\": p_value < 0.01,",
    "new_string": "            \"significant_005\": bool(p_value < 0.05),\n            \"significant_001\": bool(p_value < 0.01),"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-15T07:59:05.941321+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/wilson_ci.py has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_wilson-ci_20260515T075227",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-15T07:59:05.941445+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 artifacts/wilson_ci.py",
  "description": "Run Wilson CI analysis script"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_wilson-ci_20260515T075227",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 artifacts/wilson_ci.py",
    "description": "Run Wilson CI analysis script"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-15T07:59:05.941602+00:00_

================================================================================
WILSON SCORE 95% CI — PER EXPERIMENT
================================================================================

plan002-additive-b01-s42 (ISR β=0.1, s42, n=81)
       h7:  13/ 81 = 0.160  [0.096, 0.255]
       h1:  42/ 81 = 0.519  [0.411, 0.624]
  genuine:  25/ 81 = 0.309  [0.219, 0.416]

plan002-additive-b01-s43 (ISR β=0.1, s43, n=61)
       h7:  59/ 61 = 0.967  [0.888, 0.991]
       h1: N/A
  genuine: N/A

plan002-additive-b01-s44 (ISR β=0.1, s44, n=89)
       h7:  77/ 89 = 0.865  [0.779, 0.921]
       h1: N/A
  genuine: N/A

plan002-additive-b03-s42 (ISR β=0.3, s42, n=18)
       h7:   0/ 18 = 0.000  [0.000, 0.176]
       h1:  14/ 18 = 0.778  [0.548, 0.910]
  genuine:   4/ 18 = 0.222  [0.090, 0.452]

exp1-isr-b03-s43-r3 (ISR β=0.3, s43, n=86)
       h7:   4/ 86 = 0.047  [0.018, 0.114]
       h1:  59/ 86 = 0.686  [0.582, 0.774]
  genuine:  23/ 86 = 0.267  [0.185, 0.369]

exp1-isr-b03-s44-r2 (ISR β=0.3, s44, n=95)
       h7:  95/ 95 = 1.000  [0.961, 1.000]
       h1:   0/ 95 = 0.000  [0.000, 0.039]
  genuine:   0/ 95 = 0.000  [0.000, 0.039]

plan006-prolog-sta-s42 (Prolog STA, s42, n=50)
       h7:  50/ 50 = 1.000  [0.929, 1.000]
       h1: N/A
  genuine: N/A

plan006-prolog-exec-s42 (Prolog exec-only, s42, n=83)
       h7:   0/ 83 = 0.000  [0.000, 0.044]
       h1:   0/ 83 = 0.000  [0.000, 0.044]
  genuine: N/A

plan018-additive-random-b01-s43-r2 (Random β=0.1, s43, n=88)
       h7:   0/ 88 = 0.000  [0.000, 0.042]
       h1:  82/ 88 = 0.932  [0.859, 0.968]
  genuine:   6/ 88 = 0.068  [0.032, 0.141]

plan017-additive-random-s42 (Random β=0.3, s42, n=48)
       h7:   0/ 48 = 0.000  [0.000, 0.074]
       h1:  48/ 48 = 1.000  [0.926, 1.000]
  genuine:   0/ 48 = 0.000  [0.000, 0.074]

exp1-random-b03-s43-r4 (Random β=0.3, s43, n=92)
       h7:   7/ 92 = 0.076  [0.037, 0.149]
       h1:  90/ 92 = 0.978  [0.924, 0.994]
  genuine:   2/ 92 = 0.022  [0.006, 0.076]

exp1-random-b03-s44-r2 
…[truncated 3859 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_wilson-ci_20260515T075227",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-15T07:59:05.941800+00:00_

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
  "session": "worker_analysis_wilson-ci_20260515T075227",
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

_source line 50 · 2026-05-15T07:59:05.941926+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_wilson-ci_20260515T075227",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-15T07:59:05.942062+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "wilson_ci_results_csv",
  "type": "data",
  "description": "Wilson score 95% CI for all experiment classifications (H7, H1, genuine) — per-experiment CSV",
  "project": "solver-trace-ablation",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/wilson_ci_results.csv",
  "tags": "['statistics', 'wilson-ci', 'classification']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_wilson-ci_20260515T075227",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "wilson_ci_results_csv",
    "type": "data",
    "description": "Wilson score 95% CI for all experiment classifications (H7, H1, genuine) — per-experiment CSV",
    "project": "solver-trace-ablation",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/wilson_ci_results.csv",
    "tags": "['statistics', 'wilson-ci', 'classification']"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-15T07:59:05.942226+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260515_f66df1\", \"name\": \"wilson_ci_results_csv\", \"type\": \"data\", \"description\": \"Wilson score 95% CI for all experiment classifications (H7, H1, genuine) — per-experiment CSV\", \"path\": \"projects/solver-trace-ablation/artifacts/_project/data/wilson_ci_results.csv\", \"url\": null, \"project\": \"solver-trace-ablation\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-15T07:58:37.622128+00:00\", \"tags\": [\"statistics\", \"wilson-ci\", \"classification\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_wilson-ci_20260515T075227",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-15T07:59:05.942363+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "wilson_ci_results_json",
  "type": "data",
  "description": "Wilson score 95% CI + pooled CI + Fisher exact tests — full JSON with per-experiment, pooled, and comparison results",
  "project": "solver-trace-ablation",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/wilson_ci_results.json",
  "tags": "['statistics', 'wilson-ci', 'fisher-test', 'classification']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_wilson-ci_20260515T075227",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "wilson_ci_results_json",
    "type": "data",
    "description": "Wilson score 95% CI + pooled CI + Fisher exact tests — full JSON with per-experiment, pooled, and comparison results",
    "project": "solver-trace-ablation",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/wilson_ci_results.json",
    "tags": "['statistics', 'wilson-ci', 'fisher-test', 'classification']"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-15T07:59:05.942511+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260515_0f412d\", \"name\": \"wilson_ci_results_json\", \"type\": \"data\", \"description\": \"Wilson score 95% CI + pooled CI + Fisher exact tests — full JSON with per-experiment, pooled, and comparison results\", \"path\": \"projects/solver-trace-ablation/artifacts/_project/data/wilson_ci_results.json\", \"url\": null, \"project\": \"solver-trace-ablation\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-15T07:58:40.498039+00:00\", \"tags\": [\"statistics\", \"wilson-ci\", \"fisher-test\", \"classification\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_wilson-ci_20260515T075227",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-15T07:59:05.942642+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "wilson_ci_script",
  "type": "intermediate",
  "description": "Python script computing Wilson score CI and Fisher exact tests from registry classification data",
  "project": "solver-trace-ablation",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/wilson_ci.py",
  "tags": "['statistics', 'script']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_wilson-ci_20260515T075227",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "wilson_ci_script",
    "type": "intermediate",
    "description": "Python script computing Wilson score CI and Fisher exact tests from registry classification data",
    "project": "solver-trace-ablation",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/wilson_ci.py",
    "tags": "['statistics', 'script']"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-15T07:59:05.942820+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260515_9dd3c4\", \"name\": \"wilson_ci_script\", \"type\": \"intermediate\", \"description\": \"Python script computing Wilson score CI and Fisher exact tests from registry classification data\", \"path\": \"projects/solver-trace-ablation/artifacts/_project/intermediate/wilson_ci.py\", \"url\": null, \"project\": \"solver-trace-ablation\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-15T07:58:41.987194+00:00\", \"tags\": [\"statistics\", \"script\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_wilson-ci_20260515T075227",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 57 · 2026-05-15T07:59:05.943036+00:00_

## 结果汇总

### Pooled Wilson 95% CI

| Condition | H7 rate [CI] | H1 rate [CI] | Genuine rate [CI] |
|---|---|---|---|
| **exec-only** (3 seeds, n=204) | 0.475 [0.408, 0.544] | 0.461 [0.394, 0.529] | 0.059 [0.034, 0.100] |
| **ISR β=0.1** (3 seeds, n=231) | 0.645 [0.581, 0.704] | 0.519 [0.411, 0.624]† | 0.309 [0.219, 0.416]† |
| **ISR β=0.3** (3 seeds, n=199) | 0.497 [0.429, 0.566] | 0.367 [0.303, 0.436] | 0.136 [0.095, 0.190] |
| **Random β=0.1** (1 seed, n=88) | 0.000 [0.000, 0.042] | 0.932 [0.859, 0.968] | 0.068 [0.032, 0.141] |
| **Random β=0.3** (3 seeds, n=163) | 0.043 [0.021, 0.086] | 0.988 [0.956, 0.997] | 0.012 [0.003, 0.044] |
| **SFT** (2 seeds, n=29) | 0.000 [0.000, 0.117] | 0.069 [0.019, 0.220] | 0.931 [0.780, 0.981] |

†ISR β=0.1 的 H1/genuine 仅有 s42 数据（s43/s44 缺 H1/genuine 分解），pooled 实际 n=81。

### Fisher Exact Tests (关键对比)

| 对比 | 类别 | OR | p-value | |
|---|---|---|---|---|
| ISR β=0.1 vs Random β=0.1 | genuine | 6.10 | 0.0001 | *** |
| ISR β=0.1 vs Random β=0.1 | H7 | ∞ | <0.0001 | *** |
| ISR β=0.3 vs Random β=0.3 | genuine | 12.64 | <0.0001 | *** |
| ISR β=0.3 vs Random β=0.3 | H7 | 22.06 | <0.0001 | *** |
| ISR β=0.1 vs exec-only | genuine | 7.14 | <0.0001 | *** |
| ISR β=0.3 vs exec-only | genuine | 2.51 | 0.011 | * |
| Random β=0.1 vs exec-only | genuine | 1.17 | 0.793 | ns |
| Random β=0.3 vs exec-only | genuine | 0.20 | 0.026 | * |

### 关键发现

1. **ISR 训练显著提升 genuine rate**：ISR β=0.1 genuine=30.9% vs Random β=0.1 genuine=6.8%（OR=6.1, p=0.0001）；ISR β=0.3 genuine=13.6% vs Random β=0.3 genuine=1.2%（OR=12.6, p<0.0001）。

2. **ISR 训练也带来更高 H7 rate**：ISR β=0.1 H7=64.5% vs Random β=0.1 H7=0%；ISR β=0.3 H7=49.7% vs Random β=0.3 H7=4.3%。这与 C006 约束一致——ISR+exec 的高 H7 可能是 Goodhart 效应（metric gaming）。

3. **Random 和 exec-only 的 genuine rate 无显著差异**（Random β=0.1 vs exec-only: p=0.793, ns），说明 random trace ablation 不比纯执行训练产生更多 genuine reasoning。

4. **SFT 有最高 genuine rate（93.1%）**，但样本极小（n=29），CI 很宽 [0.780, 0.981]。

5. **数据局限**：ISR β=0.1 的 H1/genuine pooled 仅基于 s42 一个 seed（s43/s44 缺分解数据）；Random β=0.1 仅有 s43 一个 seed。

产出文件已注册：`wilson_ci_results.csv`、`wilson_ci_results.json`、`wilson_ci.py`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_wilson-ci_20260515T075227"
}
```

</details>

---
