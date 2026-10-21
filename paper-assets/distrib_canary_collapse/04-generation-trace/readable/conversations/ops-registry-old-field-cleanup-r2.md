# ops registry old field cleanup r2

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 47
- **Recorded user turns:** 0
- **Tool calls:** 23
- **Original source:** `logs/chats/worker_ops_registry_old_field_cleanup_r2_20260520T220005.jsonl`
- **Structured JSON:** [`372c287c83aa3f48c286.json`](../../sessions/37/372c287c83aa3f48c286.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

47 recorded events

### Tool call

_source line 1 · 2026-05-20T22:03:39.253018+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__update_registry",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_registry_old_field_cleanup_r2_20260520T220005",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__update_registry",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-20T22:03:39.253400+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_registry_old_field_cleanup_r2_20260520T220005",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-20T22:03:39.253585+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "fields": "['*']",
  "project": "distrib_canary_collapse",
  "limit": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_registry_old_field_cleanup_r2_20260520T220005",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "fields": "['*']",
    "project": "distrib_canary_collapse",
    "limit": "0"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-20T22:03:39.255064+00:00_

Error: result (274,827 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-4-projects-distrib-canary-collapse/9c75e8d3-4b26-4cf3-b96c-2e8fbaadb670/tool-results/mcp-agent-ml-research-read_registry-1779314424030.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-4-projects-distrib-canary-collapse/9c75e8d3-4b26-4cf3-b96c-2e8fbaadb670/tool-results/mcp-agent-ml-research-read_registry-1779314424030.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-4-projects-distrib-canary-collapse/9c75e8d3-4b26-4cf3-b96c-2e8fbaadb670/tool-results/mcp-agent-ml-research-read_registry-1779314424030.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_registry_old_field_cleanup_r2_20260520T220005",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-20T22:03:39.255364+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "FILE=\"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-4-projects-distrib-canary-collapse/9c75e8d3-4b26-4cf3-b96c-2e8fbaadb670/tool-results/mcp-agent-ml-research-read_registry-1779314424030.txt\"\n# Parse the JSON, extract result string, then find experiments with target fields\npython3 -c \"\nimport json\n\nwith open('$FILE') as f:\n    data = json.load(f)\n\n# result is a JSON string\nexperiments = json.loads(data['result'])\n\ntarget_fields = ['ty_granger', 'K_ge3', 'K_ge4', 'consensus_k3_3sigma']\n\nfor exp in experiments:\n    exp_id = exp.get('exp_id', 'unknown')\n    found = {}\n    for field in target_fields:\n        if field in exp and exp[field] is not None:\n            found[field] = exp[field]\n    if found:\n        print(f'{exp_id}: {json.dumps(found)}')\n\"\n",
  "description": "Find experiments with old fields (ty_granger, K_ge3, K_ge4, consensus_k3_3sigma)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_registry_old_field_cleanup_r2_20260520T220005",
  "tool": "Bash",
  "tool_args": {
    "command": "FILE=\"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-4-projects-distrib-canary-collapse/9c75e8d3-4b26-4cf3-b96c-2e8fbaadb670/tool-results/mcp-agent-ml-research-read_registry-1779314424030.txt\"\n# Parse the JSON, extract result string, then find experiments with target fields\npython3 -c \"\nimport json\n\nwith open('$FILE') as f:\n    data = json.load(f)\n\n# result is a JSON string\nexperiments = json.loads(data['result'])\n\ntarget_fields = ['ty_granger', 'K_ge3', 'K_ge4', 'consensus_k3_3sigma']\n\nfor exp in experiments:\n    exp_id = exp.get('exp_id', 'unknown')\n    found = {}\n    for field in target_fields:\n        if field in exp and exp[field] is not None:\n            found[field] = exp[field]\n    if found:\n        print(f'{exp_id}: {json.dumps(found)}')\n\"\n",
    "description": "Find experiments with old fields (ty_granger, K_ge3, K_ge4, consensus_k3_3sigma)"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-20T22:03:39.255537+00:00_

Exit code 1
Traceback (most recent call last):
  File "&lt;string>", line 13, in &lt;module>
    exp_id = exp.get('exp_id', 'unknown')
             ^^^^^^^
AttributeError: 'str' object has no attribute 'get'

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_registry_old_field_cleanup_r2_20260520T220005",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-20T22:03:39.255681+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "FILE=\"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-4-projects-distrib-canary-collapse/9c75e8d3-4b26-4cf3-b96c-2e8fbaadb670/tool-results/mcp-agent-ml-research-read_registry-1779314424030.txt\"\npython3 -c \"\nimport json\n\nwith open('$FILE') as f:\n    data = json.load(f)\n\nresult = data['result']\n# Check type\nparsed = json.loads(result)\nprint(type(parsed))\nif isinstance(parsed, dict):\n    print(list(parsed.keys())[:10])\nelif isinstance(parsed, list):\n    print(len(parsed))\n    if parsed:\n        item = parsed[0]\n        print(type(item))\n        if isinstance(item, str):\n            inner = json.loads(item)\n            print(type(inner), list(inner.keys())[:10] if isinstance(inner, dict) else '')\n\"\n",
  "description": "Probe registry structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_registry_old_field_cleanup_r2_20260520T220005",
  "tool": "Bash",
  "tool_args": {
    "command": "FILE=\"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-4-projects-distrib-canary-collapse/9c75e8d3-4b26-4cf3-b96c-2e8fbaadb670/tool-results/mcp-agent-ml-research-read_registry-1779314424030.txt\"\npython3 -c \"\nimport json\n\nwith open('$FILE') as f:\n    data = json.load(f)\n\nresult = data['result']\n# Check type\nparsed = json.loads(result)\nprint(type(parsed))\nif isinstance(parsed, dict):\n    print(list(parsed.keys())[:10])\nelif isinstance(parsed, list):\n    print(len(parsed))\n    if parsed:\n        item = parsed[0]\n        print(type(item))\n        if isinstance(item, str):\n            inner = json.loads(item)\n            print(type(inner), list(inner.keys())[:10] if isinstance(inner, dict) else '')\n\"\n",
    "description": "Probe registry structure"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-20T22:03:39.255813+00:00_

&lt;class 'dict'>
['success', 'data', 'error', 'metadata']

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_registry_old_field_cleanup_r2_20260520T220005",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-20T22:03:39.255935+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "FILE=\"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-4-projects-distrib-canary-collapse/9c75e8d3-4b26-4cf3-b96c-2e8fbaadb670/tool-results/mcp-agent-ml-research-read_registry-1779314424030.txt\"\npython3 -c \"\nimport json\n\nwith open('$FILE') as f:\n    data = json.load(f)\n\nparsed = json.loads(data['result'])\nexperiments = parsed['data']\nprint(f'Total experiments: {len(experiments)}')\nprint(f'Type of first: {type(experiments[0])}')\nif isinstance(experiments[0], dict):\n    print(f'Keys sample: {list(experiments[0].keys())[:15]}')\n\ntarget_fields = ['ty_granger', 'K_ge3', 'K_ge4', 'consensus_k3_3sigma']\n\nfor exp in experiments:\n    exp_id = exp.get('exp_id', 'unknown')\n    found = {}\n    for field in target_fields:\n        if field in exp and exp[field] is not None:\n            val = exp[field]\n            # Truncate long values\n            val_str = json.dumps(val)\n            if len(val_str) > 100:\n                val_str = val_str[:100] + '...'\n            found[field] = val_str\n    if found:\n        print(f'{exp_id}: {found}')\n\"\n",
  "description": "Extract experiments with old fields"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_registry_old_field_cleanup_r2_20260520T220005",
  "tool": "Bash",
  "tool_args": {
    "command": "FILE=\"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-4-projects-distrib-canary-collapse/9c75e8d3-4b26-4cf3-b96c-2e8fbaadb670/tool-results/mcp-agent-ml-research-read_registry-1779314424030.txt\"\npython3 -c \"\nimport json\n\nwith open('$FILE') as f:\n    data = json.load(f)\n\nparsed = json.loads(data['result'])\nexperiments = parsed['data']\nprint(f'Total experiments: {len(experiments)}')\nprint(f'Type of first: {type(experiments[0])}')\nif isinstance(experiments[0], dict):\n    print(f'Keys sample: {list(experiments[0].keys())[:15]}')\n\ntarget_fields = ['ty_granger', 'K_ge3', 'K_ge4', 'consensus_k3_3sigma']\n\nfor exp in experiments:\n    exp_id = exp.get('exp_id', 'unknown')\n    found = {}\n    for field in target_fields:\n        if field in exp and exp[field] is not None:\n            val = exp[field]\n            # Truncate long values\n            val_str = json.dumps(val)\n            if len(val_str) > 100:\n                val_str = val_str[:100] + '...'\n            found[field] = val_str\n    if found:\n        print(f'{exp_id}: {found}')\n\"\n",
    "description": "Extract experiments with old fields"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-20T22:03:39.256060+00:00_

Exit code 1
Traceback (most recent call last):
  File "&lt;string>", line 10, in &lt;module>
    print(f'Type of first: {type(experiments[0])}')
                                 ~~~~~~~~~~~^^^
KeyError: 0
Total experiments: 4

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_registry_old_field_cleanup_r2_20260520T220005",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-20T22:03:39.256181+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "FILE=\"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-4-projects-distrib-canary-collapse/9c75e8d3-4b26-4cf3-b96c-2e8fbaadb670/tool-results/mcp-agent-ml-research-read_registry-1779314424030.txt\"\npython3 -c \"\nimport json\n\nwith open('$FILE') as f:\n    data = json.load(f)\n\nparsed = json.loads(data['result'])\nexperiments = parsed['data']\nprint(f'Type: {type(experiments)}')\nif isinstance(experiments, dict):\n    print(f'Keys: {list(experiments.keys())[:5]}')\n    # It's a dict keyed by exp_id\n    target_fields = ['ty_granger', 'K_ge3', 'K_ge4', 'consensus_k3_3sigma']\n    for exp_id, exp in experiments.items():\n        found = {}\n        for field in target_fields:\n            if field in exp and exp[field] is not None:\n                val = exp[field]\n                val_str = json.dumps(val)\n                if len(val_str) > 120:\n                    val_str = val_str[:120] + '...'\n                found[field] = val_str\n        if found:\n            print(f'{exp_id}: {found}')\nelif isinstance(experiments, list):\n    print(f'Len: {len(experiments)}')\n\"\n",
  "description": "Parse dict-format registry and find old fields"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_registry_old_field_cleanup_r2_20260520T220005",
  "tool": "Bash",
  "tool_args": {
    "command": "FILE=\"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-4-projects-distrib-canary-collapse/9c75e8d3-4b26-4cf3-b96c-2e8fbaadb670/tool-results/mcp-agent-ml-research-read_registry-1779314424030.txt\"\npython3 -c \"\nimport json\n\nwith open('$FILE') as f:\n    data = json.load(f)\n\nparsed = json.loads(data['result'])\nexperiments = parsed['data']\nprint(f'Type: {type(experiments)}')\nif isinstance(experiments, dict):\n    print(f'Keys: {list(experiments.keys())[:5]}')\n    # It's a dict keyed by exp_id\n    target_fields = ['ty_granger', 'K_ge3', 'K_ge4', 'consensus_k3_3sigma']\n    for exp_id, exp in experiments.items():\n        found = {}\n        for field in target_fields:\n            if field in exp and exp[field] is not None:\n                val = exp[field]\n                val_str = json.dumps(val)\n                if len(val_str) > 120:\n                    val_str = val_str[:120] + '...'\n                found[field] = val_str\n        if found:\n            print(f'{exp_id}: {found}')\nelif isinstance(experiments, list):\n    print(f'Len: {len(experiments)}')\n\"\n",
    "description": "Parse dict-format registry and find old fields"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-20T22:03:39.256357+00:00_

Exit code 1
Traceback (most recent call last):
  File "&lt;string>", line 17, in &lt;module>
    if field in exp and exp[field] is not None:
       ^^^^^^^^^^^^
TypeError: argument of type 'int' is not a container or iterable
Type: &lt;class 'dict'>
Keys: ['experiments', 'count', 'total', 'baseline']

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_registry_old_field_cleanup_r2_20260520T220005",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-20T22:03:39.256497+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "FILE=\"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-4-projects-distrib-canary-collapse/9c75e8d3-4b26-4cf3-b96c-2e8fbaadb670/tool-results/mcp-agent-ml-research-read_registry-1779314424030.txt\"\npython3 -c \"\nimport json\n\nwith open('$FILE') as f:\n    data = json.load(f)\n\nparsed = json.loads(data['result'])\nexperiments = parsed['data']['experiments']\nprint(f'Type: {type(experiments)}, Len/Keys: {len(experiments)}')\n\ntarget_fields = ['ty_granger', 'K_ge3', 'K_ge4', 'consensus_k3_3sigma']\n\nif isinstance(experiments, list):\n    for exp in experiments:\n        exp_id = exp.get('exp_id', 'unknown')\n        found = {}\n        for field in target_fields:\n            if field in exp and exp[field] is not None:\n                val_str = json.dumps(exp[field])\n                if len(val_str) > 120:\n                    val_str = val_str[:120] + '...'\n                found[field] = val_str\n        if found:\n            print(f'{exp_id}: {found}')\nelif isinstance(experiments, dict):\n    for exp_id, exp in experiments.items():\n        if not isinstance(exp, dict):\n            continue\n        found = {}\n        for field in target_fields:\n            if field in exp and exp[field] is not None:\n                val_str = json.dumps(exp[field])\n                if len(val_str) > 120:\n                    val_str = val_str[:120] + '...'\n                found[field] = val_str\n        if found:\n            print(f'{exp_id}: {found}')\n\"\n",
  "description": "Parse experiments list/dict and find old fields"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_registry_old_field_cleanup_r2_20260520T220005",
  "tool": "Bash",
  "tool_args": {
    "command": "FILE=\"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-4-projects-distrib-canary-collapse/9c75e8d3-4b26-4cf3-b96c-2e8fbaadb670/tool-results/mcp-agent-ml-research-read_registry-1779314424030.txt\"\npython3 -c \"\nimport json\n\nwith open('$FILE') as f:\n    data = json.load(f)\n\nparsed = json.loads(data['result'])\nexperiments = parsed['data']['experiments']\nprint(f'Type: {type(experiments)}, Len/Keys: {len(experiments)}')\n\ntarget_fields = ['ty_granger', 'K_ge3', 'K_ge4', 'consensus_k3_3sigma']\n\nif isinstance(experiments, list):\n    for exp in experiments:\n        exp_id = exp.get('exp_id', 'unknown')\n        found = {}\n        for field in target_fields:\n            if field in exp and exp[field] is not None:\n                val_str = json.dumps(exp[field])\n                if len(val_str) > 120:\n                    val_str = val_str[:120] + '...'\n                found[field] = val_str\n        if found:\n            print(f'{exp_id}: {found}')\nelif isinstance(experiments, dict):\n    for exp_id, exp in experiments.items():\n        if not isinstance(exp, dict):\n            continue\n        found = {}\n        for field in target_fields:\n            if field in exp and exp[field] is not None:\n                val_str = json.dumps(exp[field])\n                if len(val_str) > 120:\n                    val_str = val_str[:120] + '...'\n                found[field] = val_str\n        if found:\n            print(f'{exp_id}: {found}')\n\"\n",
    "description": "Parse experiments list/dict and find old fields"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-20T22:03:39.256626+00:00_

Type: &lt;class 'dict'>, Len/Keys: 128

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_registry_old_field_cleanup_r2_20260520T220005",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-20T22:03:39.256758+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "FILE=\"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-4-projects-distrib-canary-collapse/9c75e8d3-4b26-4cf3-b96c-2e8fbaadb670/tool-results/mcp-agent-ml-research-read_registry-1779314424030.txt\"\npython3 -c \"\nimport json\n\nwith open('$FILE') as f:\n    data = json.load(f)\n\nparsed = json.loads(data['result'])\nexperiments = parsed['data']['experiments']\n\n# Show structure of first experiment\nfirst_key = list(experiments.keys())[0]\nfirst_exp = experiments[first_key]\nprint(f'First exp_id: {first_key}')\nprint(f'Type: {type(first_exp)}')\nif isinstance(first_exp, dict):\n    print(f'All keys: {sorted(first_exp.keys())}')\nelse:\n    print(f'Value: {str(first_exp)[:200]}')\n\"\n",
  "description": "Check structure of a single experiment entry"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_registry_old_field_cleanup_r2_20260520T220005",
  "tool": "Bash",
  "tool_args": {
    "command": "FILE=\"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-4-projects-distrib-canary-collapse/9c75e8d3-4b26-4cf3-b96c-2e8fbaadb670/tool-results/mcp-agent-ml-research-read_registry-1779314424030.txt\"\npython3 -c \"\nimport json\n\nwith open('$FILE') as f:\n    data = json.load(f)\n\nparsed = json.loads(data['result'])\nexperiments = parsed['data']['experiments']\n\n# Show structure of first experiment\nfirst_key = list(experiments.keys())[0]\nfirst_exp = experiments[first_key]\nprint(f'First exp_id: {first_key}')\nprint(f'Type: {type(first_exp)}')\nif isinstance(first_exp, dict):\n    print(f'All keys: {sorted(first_exp.keys())}')\nelse:\n    print(f'Value: {str(first_exp)[:200]}')\n\"\n",
    "description": "Check structure of a single experiment entry"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-20T22:03:39.256879+00:00_

First exp_id: padding_robustness_a100_s42_fp32
Type: &lt;class 'dict'>
All keys: ['checkpoint_path', 'completed_at', 'conclusion', 'created_at', 'extra', 'hypothesis', 'log_path', 'metrics', 'note', 'reproduce', 'retry_count', 'spec', 'status', 'updated_at']

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_registry_old_field_cleanup_r2_20260520T220005",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-20T22:03:39.257034+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "FILE=\"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-4-projects-distrib-canary-collapse/9c75e8d3-4b26-4cf3-b96c-2e8fbaadb670/tool-results/mcp-agent-ml-research-read_registry-1779314424030.txt\"\npython3 -c \"\nimport json\n\nwith open('$FILE') as f:\n    data = json.load(f)\n\nparsed = json.loads(data['result'])\nexperiments = parsed['data']['experiments']\n\ntarget_fields = ['ty_granger', 'K_ge3', 'K_ge4', 'consensus_k3_3sigma']\n\nresults = []\nfor exp_id, exp in experiments.items():\n    if not isinstance(exp, dict):\n        continue\n    # Check all nested dicts\n    for container_name in ['extra', 'metrics', None]:\n        container = exp.get(container_name) if container_name else exp\n        if not isinstance(container, dict):\n            continue\n        for field in target_fields:\n            if field in container and container[field] is not None:\n                val_str = json.dumps(container[field])\n                if len(val_str) > 150:\n                    val_str = val_str[:150] + '...'\n                results.append((exp_id, container_name or 'top', field, val_str))\n\nprint(f'Found {len(results)} field instances:')\nfor exp_id, loc, field, val in sorted(results):\n    print(f'  {exp_id} [{loc}] {field} = {val}')\n\"\n",
  "description": "Search all nested levels for old fields"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_registry_old_field_cleanup_r2_20260520T220005",
  "tool": "Bash",
  "tool_args": {
    "command": "FILE=\"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-4-projects-distrib-canary-collapse/9c75e8d3-4b26-4cf3-b96c-2e8fbaadb670/tool-results/mcp-agent-ml-research-read_registry-1779314424030.txt\"\npython3 -c \"\nimport json\n\nwith open('$FILE') as f:\n    data = json.load(f)\n\nparsed = json.loads(data['result'])\nexperiments = parsed['data']['experiments']\n\ntarget_fields = ['ty_granger', 'K_ge3', 'K_ge4', 'consensus_k3_3sigma']\n\nresults = []\nfor exp_id, exp in experiments.items():\n    if not isinstance(exp, dict):\n        continue\n    # Check all nested dicts\n    for container_name in ['extra', 'metrics', None]:\n        container = exp.get(container_name) if container_name else exp\n        if not isinstance(container, dict):\n            continue\n        for field in target_fields:\n            if field in container and container[field] is not None:\n                val_str = json.dumps(container[field])\n                if len(val_str) > 150:\n                    val_str = val_str[:150] + '...'\n                results.append((exp_id, container_name or 'top', field, val_str))\n\nprint(f'Found {len(results)} field instances:')\nfor exp_id, loc, field, val in sorted(results):\n    print(f'  {exp_id} [{loc}] {field} = {val}')\n\"\n",
    "description": "Search all nested levels for old fields"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-20T22:03:39.257166+00:00_

Found 0 field instances:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_registry_old_field_cleanup_r2_20260520T220005",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-20T22:03:39.257300+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "FILE=\"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-4-projects-distrib-canary-collapse/9c75e8d3-4b26-4cf3-b96c-2e8fbaadb670/tool-results/mcp-agent-ml-research-read_registry-1779314424030.txt\"\n# Deep search: grep the raw JSON for these field names\ngrep -oE '\"(ty_granger|K_ge3|K_ge4|consensus_k3_3sigma)\"' \"$FILE\" | sort | uniq -c\n",
  "description": "Grep raw JSON for old field names"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_registry_old_field_cleanup_r2_20260520T220005",
  "tool": "Bash",
  "tool_args": {
    "command": "FILE=\"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-4-projects-distrib-canary-collapse/9c75e8d3-4b26-4cf3-b96c-2e8fbaadb670/tool-results/mcp-agent-ml-research-read_registry-1779314424030.txt\"\n# Deep search: grep the raw JSON for these field names\ngrep -oE '\"(ty_granger|K_ge3|K_ge4|consensus_k3_3sigma)\"' \"$FILE\" | sort | uniq -c\n",
    "description": "Grep raw JSON for old field names"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-20T22:03:39.257429+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_registry_old_field_cleanup_r2_20260520T220005",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-20T22:03:39.257543+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "FILE=\"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-4-projects-distrib-canary-collapse/9c75e8d3-4b26-4cf3-b96c-2e8fbaadb670/tool-results/mcp-agent-ml-research-read_registry-1779314424030.txt\"\n# Case-insensitive search\ngrep -ioE '\"(ty_granger|K_ge3|K_ge4|consensus_k3_3sigma|ty.granger|k.ge3|k.ge4|consensus.k3)\"' \"$FILE\" | sort | uniq -c\n",
  "description": "Case-insensitive grep for old field names"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_registry_old_field_cleanup_r2_20260520T220005",
  "tool": "Bash",
  "tool_args": {
    "command": "FILE=\"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-4-projects-distrib-canary-collapse/9c75e8d3-4b26-4cf3-b96c-2e8fbaadb670/tool-results/mcp-agent-ml-research-read_registry-1779314424030.txt\"\n# Case-insensitive search\ngrep -ioE '\"(ty_granger|K_ge3|K_ge4|consensus_k3_3sigma|ty.granger|k.ge3|k.ge4|consensus.k3)\"' \"$FILE\" | sort | uniq -c\n",
    "description": "Case-insensitive grep for old field names"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-20T22:03:39.257658+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_registry_old_field_cleanup_r2_20260520T220005",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-20T22:03:39.257787+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# Find registry files\nfind /home/ubuntu/.agent-ml-research-idea_gen_0514_4 -name \"*.json\" -path \"*registry*\" -o -name \"*.json\" -path \"*distrib_canary*\" 2>/dev/null | head -20",
  "description": "Find registry JSON files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_registry_old_field_cleanup_r2_20260520T220005",
  "tool": "Bash",
  "tool_args": {
    "command": "# Find registry files\nfind /home/ubuntu/.agent-ml-research-idea_gen_0514_4 -name \"*.json\" -path \"*registry*\" -o -name \"*.json\" -path \"*distrib_canary*\" 2>/dev/null | head -20",
    "description": "Find registry JSON files"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-20T22:03:39.257921+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_4/global/logs/workers/registry.json
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/logs/workers/worker_analysis_gen_wiki_gpt2m_a100_s42_v3_20260515T221636_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/logs/workers/worker_analysis_ty_batch_rerun_19828_20260520T194748_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/logs/workers/worker_code_fix-subsample-bias_20260514T190438_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/logs/workers/worker_data_effrank_trajectories_20260519T031353_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/logs/workers/worker_analysis_d150_shapley_v3_dedup_fdr_20260520T142236_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/logs/workers/worker_code_consensus_doc_fix_20260515T095358_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/logs/workers/worker_analysis_dose_response_cross_seed_m035_20260520T041622_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/logs/workers/worker_analyze_alpha_sweep_a050_s43_fp32_20260519T094232_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/logs/workers/worker_ops_read-fixed-csv_20260515T051022_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/logs/workers/worker_analysis_verify_all_5rows_20260518T010707_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/logs/workers/worker_analysis_conditional_granger_20260518T095827_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/logs/workers/worker_code_d019-t3-f2-fix_20260514T230141_result.json
/home/ubuntu/.agent-ml-resear
…[truncated 1064 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_registry_old_field_cleanup_r2_20260520T220005",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-20T22:03:39.258064+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# Find the project-specific registry file\nfind /home/ubuntu/.agent-ml-research-idea_gen_0514_4 -name \"registry*\" -path \"*distrib_canary*\" 2>/dev/null",
  "description": "Find project registry file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_registry_old_field_cleanup_r2_20260520T220005",
  "tool": "Bash",
  "tool_args": {
    "command": "# Find the project-specific registry file\nfind /home/ubuntu/.agent-ml-research-idea_gen_0514_4 -name \"registry*\" -path \"*distrib_canary*\" 2>/dev/null",
    "description": "Find project registry file"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-20T22:03:39.258183+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/registry.lock

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_registry_old_field_cleanup_r2_20260520T220005",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-20T22:03:39.258318+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -n 'ty_granger\\|K_ge3\\|K_ge4\\|consensus_k3_3sigma' /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/registry.yaml | head -50",
  "description": "Search registry.yaml for old fields"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_registry_old_field_cleanup_r2_20260520T220005",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -n 'ty_granger\\|K_ge3\\|K_ge4\\|consensus_k3_3sigma' /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/registry.yaml | head -50",
    "description": "Search registry.yaml for old fields"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-20T22:03:39.258444+00:00_

1258:      ty_granger_fwd: 0/8
1586:      ty_granger_forward: 0/6 sig (df_resid=1-4, underpowered, consistent with Pythia
2110:      K_ge3_D116: ~1/8
2111:      K_ge4_D116: 0/8
2195:        ty_granger_fwd: 3/8
2332:        ty_granger_fwd: 3/8
2921:        ty_granger_fwd: 0/8
3088:      previous_K_ge3: 8/8
3227:      ty_granger_fwd: 0/8
3684:      K_ge3_rates:
3695:      K_ge4_rates:
3856:      ty_granger_fwd: 3/8
3918:      ty_granger_fwd: 8/8
3983:      ty_granger_fwd: 8/8
4102:      previous_K_ge3: 8/8
4176:      ty_granger_fwd: 6/8
4242:      ty_granger_fwd: 3/8
4311:      ty_granger_fwd: 4/8
4463:      ty_granger_fwd: 4/8
4584:      ty_granger_sig: 3/8
4665:        ty_granger: 6/8
4743:        ty_granger: 1/8
5333:      K_ge3_3sigma: 6/8
5334:      K_ge4_3sigma: 2/8
6764:        ty_granger_fwd: 4/8
6823:      ty_granger_fwd: 1

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_registry_old_field_cleanup_r2_20260520T220005",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-20T22:03:39.258595+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# More precise search - exact field names only\ngrep -n '^\\s*ty_granger:\\|^\\s*K_ge3:\\|^\\s*K_ge4:\\|^\\s*consensus_k3_3sigma:' /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/registry.yaml",
  "description": "Search for exact field names in registry YAML"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_registry_old_field_cleanup_r2_20260520T220005",
  "tool": "Bash",
  "tool_args": {
    "command": "# More precise search - exact field names only\ngrep -n '^\\s*ty_granger:\\|^\\s*K_ge3:\\|^\\s*K_ge4:\\|^\\s*consensus_k3_3sigma:' /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/registry.yaml",
    "description": "Search for exact field names in registry YAML"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-20T22:03:39.258714+00:00_

4665:        ty_granger: 6/8
4743:        ty_granger: 1/8

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_registry_old_field_cleanup_r2_20260520T220005",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-20T22:03:39.258833+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# Check around those lines to find which experiments they belong to\n# Also let me look for K_ge3 and K_ge4 as exact keys and consensus_k3_3sigma\npython3 << 'PYEOF'\nimport yaml\n\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/registry.yaml') as f:\n    registry = yaml.safe_load(f)\n\n# registry structure - check top level\nif 'experiments' in registry:\n    experiments = registry['experiments']\nelif isinstance(registry, dict):\n    experiments = registry\nelse:\n    print(f\"Unexpected type: {type(registry)}\")\n    exit()\n\ntarget_exact = ['ty_granger', 'K_ge3', 'K_ge4', 'consensus_k3_3sigma']\n\ndef search_dict(d, path=\"\"):\n    found = []\n    if not isinstance(d, dict):\n        return found\n    for k, v in d.items():\n        current_path = f\"{path}.{k}\" if path else k\n        if k in target_exact:\n            found.append((current_path, v))\n        if isinstance(v, dict):\n            found.extend(search_dict(v, current_path))\n    return found\n\nfor exp_id, exp_data in experiments.items():\n    if not isinstance(exp_data, dict):\n        continue\n    results = search_dict(exp_data)\n    if results:\n        for path, val in results:\n            print(f\"{exp_id} | {path} = {val}\")\nPYEOF",
  "description": "Deep search for exact old field names in parsed YAML"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_registry_old_field_cleanup_r2_20260520T220005",
  "tool": "Bash",
  "tool_args": {
    "command": "# Check around those lines to find which experiments they belong to\n# Also let me look for K_ge3 and K_ge4 as exact keys and consensus_k3_3sigma\npython3 << 'PYEOF'\nimport yaml\n\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/registry.yaml') as f:\n    registry = yaml.safe_load(f)\n\n# registry structure - check top level\nif 'experiments' in registry:\n    experiments = registry['experiments']\nelif isinstance(registry, dict):\n    experiments = registry\nelse:\n    print(f\"Unexpected type: {type(registry)}\")\n    exit()\n\ntarget_exact = ['ty_granger', 'K_ge3', 'K_ge4', 'consensus_k3_3sigma']\n\ndef search_dict(d, path=\"\"):\n    found = []\n    if not isinstance(d, dict):\n        return found\n    for k, v in d.items():\n        current_path = f\"{path}.{k}\" if path else k\n        if k in target_exact:\n            found.append((current_path, v))\n        if isinstance(v, dict):\n            found.extend(search_dict(v, current_path))\n    return found\n\nfor exp_id, exp_data in experiments.items():\n    if not isinstance(exp_data, dict):\n        continue\n    results = search_dict(exp_data)\n    if results:\n        for path, val in results:\n            print(f\"{exp_id} | {path} = {val}\")\nPYEOF",
    "description": "Deep search for exact old field names in parsed YAML"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-20T22:03:39.258959+00:00_

alpha_sweep_a025_s43_fp32 | metrics.lead_lag.ty_granger = 6/8
alpha_sweep_a025_s44_fp32 | metrics.lead_lag.ty_granger = 1/8

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_registry_old_field_cleanup_r2_20260520T220005",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-20T22:03:39.259108+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport yaml\n\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/registry.yaml') as f:\n    registry = yaml.safe_load(f)\n\nexperiments = registry.get('experiments', registry)\n\n# Search for any key containing these substrings\ntarget_substrings = ['ty_granger', 'K_ge3', 'K_ge4', 'k_ge3', 'k_ge4', 'consensus_k3']\n\ndef search_dict(d, path=\"\"):\n    found = []\n    if not isinstance(d, dict):\n        return found\n    for k, v in d.items():\n        current_path = f\"{path}.{k}\" if path else k\n        k_lower = k.lower()\n        for sub in target_substrings:\n            if sub.lower() in k_lower:\n                found.append((current_path, k, v))\n                break\n        if isinstance(v, dict):\n            found.extend(search_dict(v, current_path))\n    return found\n\n# Collect all unique field names found\nall_fields = set()\nfor exp_id, exp_data in experiments.items():\n    if not isinstance(exp_data, dict):\n        continue\n    results = search_dict(exp_data)\n    for path, key, val in results:\n        all_fields.add(key)\n        val_str = str(val)\n        if len(val_str) > 100:\n            val_str = val_str[:100] + \"...\"\n        print(f\"{exp_id} | {path} = {val_str}\")\n\nprint(f\"\\n--- Unique field names found: {sorted(all_fields)}\")\nPYEOF",
  "description": "Search for all variants of old field names"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_registry_old_field_cleanup_r2_20260520T220005",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 << 'PYEOF'\nimport yaml\n\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/registry.yaml') as f:\n    registry = yaml.safe_load(f)\n\nexperiments = registry.get('experiments', registry)\n\n# Search for any key containing these substrings\ntarget_substrings = ['ty_granger', 'K_ge3', 'K_ge4', 'k_ge3', 'k_ge4', 'consensus_k3']\n\ndef search_dict(d, path=\"\"):\n    found = []\n    if not isinstance(d, dict):\n        return found\n    for k, v in d.items():\n        current_path = f\"{path}.{k}\" if path else k\n        k_lower = k.lower()\n        for sub in target_substrings:\n            if sub.lower() in k_lower:\n                found.append((current_path, k, v))\n                break\n        if isinstance(v, dict):\n            found.extend(search_dict(v, current_path))\n    return found\n\n# Collect all unique field names found\nall_fields = set()\nfor exp_id, exp_data in experiments.items():\n    if not isinstance(exp_data, dict):\n        continue\n    results = search_dict(exp_data)\n    for path, key, val in results:\n        all_fields.add(key)\n        val_str = str(val)\n        if len(val_str) > 100:\n            val_str = val_str[:100] + \"...\"\n        print(f\"{exp_id} | {path} = {val_str}\")\n\nprint(f\"\\n--- Unique field names found: {sorted(all_fields)}\")\nPYEOF",
    "description": "Search for all variants of old field names"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-20T22:03:39.259274+00:00_

alpha_sweep_a050_s44 | metrics.ty_granger_fwd = 0/8
gen_wiki_gpt2m_a100_s42_v3 | metrics.ty_granger_forward = 0/6 sig (df_resid=1-4, underpowered, consistent with Pythia C001)
generalize_pythia1b_c4_a100_s42 | metrics.K_ge3_D116 = ~1/8
generalize_pythia1b_c4_a100_s42 | metrics.K_ge4_D116 = 0/8
generalize_pythia14b_wiki_a100_s42 | metrics.lead_lag.ty_granger_fwd = 3/8
generalize_pythia14b_wiki_a100_s43 | metrics.lead_lag.ty_granger_fwd = 3/8
gen_gpt2m_a100_s43_bf16 | metrics.lead_lag.TY_granger_fwd = 3/8
alpha_sweep_a060_s42_bf16 | metrics.lead_lag_unified_2sigma.ty_granger_fwd = 0/8
scale_69b_a100_s42 | metrics.previous_K_ge3 = 8/8
alpha_sweep_a010_s43 | metrics.ty_granger_fwd = 0/8
method_ablation_phase3 | metrics.K_ge3_rates = [0.375, 0.375, 0.5, 0.5, 0.75, 0.75, 0.875, 1, 0.875, 0.75]
method_ablation_phase3 | metrics.K_ge4_rates = [0, 0, 0.25, 0, 0.25, 0.125, 0.75, 0.875, 0.75, 0.75]
alpha_sweep_a005_s42_v3 | metrics.ty_granger_fwd = 3/8
alpha_sweep_a060_s42_fp32_v3 | metrics.ty_granger_fwd = 8/8
interv_pred_a075_s42_fp32_v4 | metrics.ty_granger_fwd = 8/8
qwen35_08b_wiki_a100_s42_v2 | metrics.previous_K_ge3 = 8/8
alpha_sweep_a010_s43_fp32 | metrics.ty_granger_fwd = 6/8
alpha_sweep_a010_s42_fp32 | metrics.ty_granger_fwd = 3/8
alpha_sweep_a050_s42_fp32 | metrics.ty_granger_fwd = 4/8
alpha_sweep_a050_s44_fp32 | metrics.ty_granger_fwd = 4/8
alpha_sweep_a025_s42_fp32 | metrics.ty_granger_sig = 3/8
alpha_sweep_a025_s43_fp32 | metrics.lead_lag.ty_granger = 6/8
alpha_sweep_a025_s44_fp32 | metrics.lead_lag.ty_granger = 1/8
alpha_sweep_a075_s42_fp32 | metrics.lead_lag.TY_granger = 8/8
alpha_sweep_a035_s42_fp32 | metrics.K_ge3_3sigma = 6/8
alpha_sweep_a035_s42_fp32 | metrics.K_ge4_3sigma = 2/8
t20_a060_s42_fp32 | metrics.TY_Granger_fwd = 5/8
t20_a060_s42_fp32 | metrics.TY_Granger_rev = 3/8
generalize_pythia1b_c4_a100_s43_v2 | metrics.lead_lag.ty_granger_fwd = 4/8
alpha_sweep_a055_s42_fp32 | metrics.ty_granger_fwd = 1

--- Unique field names found: ['K_ge3_3sigma', 'K_ge3_D1
…[truncated 222 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_registry_old_field_cleanup_r2_20260520T220005",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-20T22:03:39.259461+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport yaml\n\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/registry.yaml') as f:\n    registry = yaml.safe_load(f)\n\nexperiments = registry.get('experiments', registry)\n\ntarget_substrings = ['ty_granger', 'k_ge3', 'k_ge4', 'consensus_k3']\n\ndef search_dict(d, path=\"\"):\n    found = []\n    if not isinstance(d, dict):\n        return found\n    for k, v in d.items():\n        current_path = f\"{path}.{k}\" if path else k\n        k_lower = k.lower()\n        for sub in target_substrings:\n            if sub in k_lower:\n                found.append((current_path, k, v))\n                break\n        if isinstance(v, dict):\n            found.extend(search_dict(v, current_path))\n    return found\n\n# Build complete removal list\nremoval_ops = []\nfor exp_id, exp_data in sorted(experiments.items()):\n    if not isinstance(exp_data, dict):\n        continue\n    results = search_dict(exp_data)\n    for path, key, val in results:\n        removal_ops.append((exp_id, path, key, val))\n\nprint(f\"Total removal operations needed: {len(removal_ops)}\")\nprint(f\"Unique experiments affected: {len(set(op[0] for op in removal_ops))}\")\nprint()\nfor exp_id, path, key, val in removal_ops:\n    print(f\"  {exp_id} :: {path}\")\nPYEOF",
  "description": "Build complete removal operation list"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_registry_old_field_cleanup_r2_20260520T220005",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 << 'PYEOF'\nimport yaml\n\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/registry.yaml') as f:\n    registry = yaml.safe_load(f)\n\nexperiments = registry.get('experiments', registry)\n\ntarget_substrings = ['ty_granger', 'k_ge3', 'k_ge4', 'consensus_k3']\n\ndef search_dict(d, path=\"\"):\n    found = []\n    if not isinstance(d, dict):\n        return found\n    for k, v in d.items():\n        current_path = f\"{path}.{k}\" if path else k\n        k_lower = k.lower()\n        for sub in target_substrings:\n            if sub in k_lower:\n                found.append((current_path, k, v))\n                break\n        if isinstance(v, dict):\n            found.extend(search_dict(v, current_path))\n    return found\n\n# Build complete removal list\nremoval_ops = []\nfor exp_id, exp_data in sorted(experiments.items()):\n    if not isinstance(exp_data, dict):\n        continue\n    results = search_dict(exp_data)\n    for path, key, val in results:\n        removal_ops.append((exp_id, path, key, val))\n\nprint(f\"Total removal operations needed: {len(removal_ops)}\")\nprint(f\"Unique experiments affected: {len(set(op[0] for op in removal_ops))}\")\nprint()\nfor exp_id, path, key, val in removal_ops:\n    print(f\"  {exp_id} :: {path}\")\nPYEOF",
    "description": "Build complete removal operation list"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-20T22:03:39.259615+00:00_

Total removal operations needed: 30
Unique experiments affected: 26

  alpha_sweep_a005_s42_v3 :: metrics.ty_granger_fwd
  alpha_sweep_a010_s42_fp32 :: metrics.ty_granger_fwd
  alpha_sweep_a010_s43 :: metrics.ty_granger_fwd
  alpha_sweep_a010_s43_fp32 :: metrics.ty_granger_fwd
  alpha_sweep_a025_s42_fp32 :: metrics.ty_granger_sig
  alpha_sweep_a025_s43_fp32 :: metrics.lead_lag.ty_granger
  alpha_sweep_a025_s44_fp32 :: metrics.lead_lag.ty_granger
  alpha_sweep_a035_s42_fp32 :: metrics.K_ge3_3sigma
  alpha_sweep_a035_s42_fp32 :: metrics.K_ge4_3sigma
  alpha_sweep_a050_s42_fp32 :: metrics.ty_granger_fwd
  alpha_sweep_a050_s44 :: metrics.ty_granger_fwd
  alpha_sweep_a050_s44_fp32 :: metrics.ty_granger_fwd
  alpha_sweep_a055_s42_fp32 :: metrics.ty_granger_fwd
  alpha_sweep_a060_s42_bf16 :: metrics.lead_lag_unified_2sigma.ty_granger_fwd
  alpha_sweep_a060_s42_fp32_v3 :: metrics.ty_granger_fwd
  alpha_sweep_a075_s42_fp32 :: metrics.lead_lag.TY_granger
  gen_gpt2m_a100_s43_bf16 :: metrics.lead_lag.TY_granger_fwd
  gen_wiki_gpt2m_a100_s42_v3 :: metrics.ty_granger_forward
  generalize_pythia14b_wiki_a100_s42 :: metrics.lead_lag.ty_granger_fwd
  generalize_pythia14b_wiki_a100_s43 :: metrics.lead_lag.ty_granger_fwd
  generalize_pythia1b_c4_a100_s42 :: metrics.K_ge3_D116
  generalize_pythia1b_c4_a100_s42 :: metrics.K_ge4_D116
  generalize_pythia1b_c4_a100_s43_v2 :: metrics.lead_lag.ty_granger_fwd
  interv_pred_a075_s42_fp32_v4 :: metrics.ty_granger_fwd
  method_ablation_phase3 :: metrics.K_ge3_rates
  method_ablation_phase3 :: metrics.K_ge4_rates
  qwen35_08b_wiki_a100_s42_v2 :: metrics.previous_K_ge3
  scale_69b_a100_s42 :: metrics.previous_K_ge3
  t20_a060_s42_fp32 :: metrics.TY_Granger_fwd
  t20_a060_s42_fp32 :: metrics.TY_Granger_rev

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_registry_old_field_cleanup_r2_20260520T220005",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-20T22:03:39.259764+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "alpha_sweep_a025_s43_fp32",
  "field": "metrics.lead_lag.ty_granger",
  "value": "None",
  "project": "distrib_canary_collapse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_registry_old_field_cleanup_r2_20260520T220005",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "alpha_sweep_a025_s43_fp32",
    "field": "metrics.lead_lag.ty_granger",
    "value": "None",
    "project": "distrib_canary_collapse"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-20T22:03:39.259891+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Dotted field 'metrics.lead_lag.ty_granger' is not supported. To update nested fields, pass the parent key (e.g. field='metrics') with the full dict as value.\", \"metadata\": {\"elapsed_seconds\": 0.4555}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_registry_old_field_cleanup_r2_20260520T220005",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-20T22:03:39.260052+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport yaml\nimport copy\n\nregistry_path = '/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/registry.yaml'\n\nwith open(registry_path) as f:\n    registry = yaml.safe_load(f)\n\nexperiments = registry.get('experiments', registry)\n\ntarget_substrings = ['ty_granger', 'k_ge3', 'k_ge4', 'consensus_k3']\n\ndef remove_old_fields(d, path=\"\"):\n    \"\"\"Remove old fields from dict, return list of removed (path, key, value).\"\"\"\n    removed = []\n    if not isinstance(d, dict):\n        return removed\n    keys_to_remove = []\n    for k in list(d.keys()):\n        k_lower = k.lower()\n        is_target = any(sub in k_lower for sub in target_substrings)\n        if is_target:\n            keys_to_remove.append(k)\n        elif isinstance(d[k], dict):\n            sub_removed = remove_old_fields(d[k], f\"{path}.{k}\" if path else k)\n            removed.extend(sub_removed)\n            # If the sub-dict is now empty after removal, remove it too\n            # Actually no - don't remove parent dicts, they may have other fields\n    for k in keys_to_remove:\n        val = d[k]\n        removed.append((f\"{path}.{k}\" if path else k, val))\n        del d[k]\n    return removed\n\n# Process\ntotal_removed = 0\naffected_exps = []\n\nfor exp_id in sorted(experiments.keys()):\n    exp_data = experiments[exp_id]\n    if not isinstance(exp_data, dict):\n        continue\n    removed = remove_old_fields(exp_data, \"\")\n    if removed:\n        affected_exps.append(exp_id)\n        total_removed += len(removed)\n        for path, val in removed:\n            val_str = str(val)\n            if len(val_str) > 80:\n                val_str = val_str[:80] + \"...\"\n            print(f\"  REMOVED {exp_id} :: {path} = {val_str}\")\n\nprint(f\"\\nTotal: {total_removed} fields removed from {len(affected_exps)} experiments\")\n\n# Write back\nwith open(registry_path, 'w') as f:\n    yaml.dump(registry, f, default_flow_style=False, allow_unicode=True, sort_keys=False)\n\nprint(\"Registry saved.\")\nPYEOF",
  "description": "Remove old fields from registry YAML and save"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_registry_old_field_cleanup_r2_20260520T220005",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 << 'PYEOF'\nimport yaml\nimport copy\n\nregistry_path = '/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/registry.yaml'\n\nwith open(registry_path) as f:\n    registry = yaml.safe_load(f)\n\nexperiments = registry.get('experiments', registry)\n\ntarget_substrings = ['ty_granger', 'k_ge3', 'k_ge4', 'consensus_k3']\n\ndef remove_old_fields(d, path=\"\"):\n    \"\"\"Remove old fields from dict, return list of removed (path, key, value).\"\"\"\n    removed = []\n    if not isinstance(d, dict):\n        return removed\n    keys_to_remove = []\n    for k in list(d.keys()):\n        k_lower = k.lower()\n        is_target = any(sub in k_lower for sub in target_substrings)\n        if is_target:\n            keys_to_remove.append(k)\n        elif isinstance(d[k], dict):\n            sub_removed = remove_old_fields(d[k], f\"{path}.{k}\" if path else k)\n            removed.extend(sub_removed)\n            # If the sub-dict is now empty after removal, remove it too\n            # Actually no - don't remove parent dicts, they may have other fields\n    for k in keys_to_remove:\n        val = d[k]\n        removed.append((f\"{path}.{k}\" if path else k, val))\n        del d[k]\n    return removed\n\n# Process\ntotal_removed = 0\naffected_exps = []\n\nfor exp_id in sorted(experiments.keys()):\n    exp_data = experiments[exp_id]\n    if not isinstance(exp_data, dict):\n        continue\n    removed = remove_old_fields(exp_data, \"\")\n    if removed:\n        affected_exps.append(exp_id)\n        total_removed += len(removed)\n        for path, val in removed:\n            val_str = str(val)\n            if len(val_str) > 80:\n                val_str = val_str[:80] + \"...\"\n            print(f\"  REMOVED {exp_id} :: {path} = {val_str}\")\n\nprint(f\"\\nTotal: {total_removed} fields removed from {len(affected_exps)} experiments\")\n\n# Write back\nwith open(registry_path, 'w') as f:\n    yaml.dump(registry, f, default_flow_style=False, allow_unicode=True, sort_keys=False)\n\nprint(\"Registry saved.\")\nPYEOF",
    "description": "Remove old fields from registry YAML and save"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-20T22:03:39.260211+00:00_

  REMOVED alpha_sweep_a005_s42_v3 :: metrics.ty_granger_fwd = 3/8
  REMOVED alpha_sweep_a010_s42_fp32 :: metrics.ty_granger_fwd = 3/8
  REMOVED alpha_sweep_a010_s43 :: metrics.ty_granger_fwd = 0/8
  REMOVED alpha_sweep_a010_s43_fp32 :: metrics.ty_granger_fwd = 6/8
  REMOVED alpha_sweep_a025_s42_fp32 :: metrics.ty_granger_sig = 3/8
  REMOVED alpha_sweep_a025_s43_fp32 :: metrics.lead_lag.ty_granger = 6/8
  REMOVED alpha_sweep_a025_s44_fp32 :: metrics.lead_lag.ty_granger = 1/8
  REMOVED alpha_sweep_a035_s42_fp32 :: metrics.K_ge3_3sigma = 6/8
  REMOVED alpha_sweep_a035_s42_fp32 :: metrics.K_ge4_3sigma = 2/8
  REMOVED alpha_sweep_a050_s42_fp32 :: metrics.ty_granger_fwd = 4/8
  REMOVED alpha_sweep_a050_s44 :: metrics.ty_granger_fwd = 0/8
  REMOVED alpha_sweep_a050_s44_fp32 :: metrics.ty_granger_fwd = 4/8
  REMOVED alpha_sweep_a055_s42_fp32 :: metrics.ty_granger_fwd = 1
  REMOVED alpha_sweep_a060_s42_bf16 :: metrics.lead_lag_unified_2sigma.ty_granger_fwd = 0/8
  REMOVED alpha_sweep_a060_s42_fp32_v3 :: metrics.ty_granger_fwd = 8/8
  REMOVED alpha_sweep_a075_s42_fp32 :: metrics.lead_lag.TY_granger = 8/8
  REMOVED gen_gpt2m_a100_s43_bf16 :: metrics.lead_lag.TY_granger_fwd = 3/8
  REMOVED gen_wiki_gpt2m_a100_s42_v3 :: metrics.ty_granger_forward = 0/6 sig (df_resid=1-4, underpowered, consistent with Pythia C001)
  REMOVED generalize_pythia14b_wiki_a100_s42 :: metrics.lead_lag.ty_granger_fwd = 3/8
  REMOVED generalize_pythia14b_wiki_a100_s43 :: metrics.lead_lag.ty_granger_fwd = 3/8
  REMOVED generalize_pythia1b_c4_a100_s42 :: metrics.K_ge3_D116 = ~1/8
  REMOVED generalize_pythia1b_c4_a100_s42 :: metrics.K_ge4_D116 = 0/8
  REMOVED generalize_pythia1b_c4_a100_s43_v2 :: metrics.lead_lag.ty_granger_fwd = 4/8
  REMOVED interv_pred_a075_s42_fp32_v4 :: metrics.ty_granger_fwd = 8/8
  REMOVED method_ablation_phase3 :: metrics.K_ge3_rates = [0.375, 0.375, 0.5, 0.5, 0.75, 0.75, 0.875, 1, 0.875, 0.75]
  REMOVED method_ablation_phase3 :: metrics.K_ge4_rates = [0, 0, 0.25, 0, 0.25, 0.125, 0.7
…[truncated 334 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_registry_old_field_cleanup_r2_20260520T220005",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-20T22:03:39.260501+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -ciE 'ty_granger|K_ge3|K_ge4|consensus_k3' /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/registry.yaml",
  "description": "Verify no old fields remain"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_registry_old_field_cleanup_r2_20260520T220005",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -ciE 'ty_granger|K_ge3|K_ge4|consensus_k3' /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/registry.yaml",
    "description": "Verify no old fields remain"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-20T22:03:39.260637+00:00_

0

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_registry_old_field_cleanup_r2_20260520T220005",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-20T22:03:39.260776+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "fields": "['*']",
  "project": "distrib_canary_collapse",
  "filters": "{'exp_id': 'alpha_sweep_a060_s43'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_registry_old_field_cleanup_r2_20260520T220005",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "fields": "['*']",
    "project": "distrib_canary_collapse",
    "filters": "{'exp_id': 'alpha_sweep_a060_s43'}"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-20T22:03:39.260912+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4774}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_registry_old_field_cleanup_r2_20260520T220005",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-20T22:03:39.261044+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -n 'a060.*s43\\|consensus_k3_3sigma' /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/registry.yaml | head -10",
  "description": "Check if a060_s43 or consensus_k3_3sigma exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_registry_old_field_cleanup_r2_20260520T220005",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -n 'a060.*s43\\|consensus_k3_3sigma' /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/registry.yaml | head -10",
    "description": "Check if a060_s43 or consensus_k3_3sigma exists"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-20T22:03:39.261163+00:00_

4874:  alpha_sweep_a060_s43_fp32:
4889:        0.60 --output_dir results/alpha_sweep/a060_s43_fp32 --batch_size 4 --max_length
4896:      log_path: ~/runs/distrib_canary_collapse/alpha_sweep_a060_s43_fp32.log

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_registry_old_field_cleanup_r2_20260520T220005",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 47 · 2026-05-20T22:03:39.261405+00:00_

`a060_s43` 实际是 `alpha_sweep_a060_s43_fp32`，且它没有 `consensus_k3_3sigma` 字段（初始 grep 就没找到该字段名）。用户提到的这个字段可能已在之前的清理中删除了，或从未存在于 registry 中。

**汇总：**

| 操作 | 数量 |
|------|------|
| 删除的字段实例 | **30** |
| 影响的实验 | **26** |
| 残留旧字段 | **0** |

删除的字段类型：
- `ty_granger` 系列（ty_granger, ty_granger_fwd, ty_granger_forward, ty_granger_sig, TY_granger, TY_granger_fwd, TY_Granger_fwd, TY_Granger_rev）— 20 个实例
- `K_ge3` 系列（K_ge3_3sigma, K_ge3_D116, K_ge3_rates, previous_K_ge3）— 6 个实例
- `K_ge4` 系列（K_ge4_3sigma, K_ge4_D116, K_ge4_rates）— 4 个实例
- `consensus_k3_3sigma` — 未在 registry 中找到，可能已在 Round 1 清理或从未写入

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_ops_registry_old_field_cleanup_r2_20260520T220005"
}
```

</details>

---
