# analysis vla baseline aggregation

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 49
- **Recorded user turns:** 0
- **Tool calls:** 24
- **Original source:** `logs/chats/worker_analysis_vla-baseline-aggregation_20260519T182814.jsonl`
- **Structured JSON:** [`540bec930ea9b966f80b.json`](../../sessions/54/540bec930ea9b966f80b.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

49 recorded events

### Tool call

_source line 1 · 2026-05-19T18:34:06.642949+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__register_artifact",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_vla-baseline-aggregation_20260519T182814",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__register_artifact",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-19T18:34:06.643463+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_vla-baseline-aggregation_20260519T182814",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-19T18:34:06.643756+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "limit": "0",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_vla-baseline-aggregation_20260519T182814",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "limit": "0",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-19T18:34:06.647195+00:00_

Error: result (521,114 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/dcc029ef-2962-4d39-bee8-d40a10c23560/tool-results/mcp-agent-ml-research-read_registry-1779215323676.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/dcc029ef-2962-4d39-bee8-d40a10c23560/tool-results/mcp-agent-ml-research-read_registry-1779215323676.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_vla-baseline-aggregation_20260519T182814",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 3
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-19T18:34:06.647612+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/dcc029ef-2962-4d39-bee8-d40a10c23560/tool-results/mcp-agent-ml-research-read_registry-1779215323676.txt | python3 -c \"\nimport json, sys\ndata = json.loads(sys.stdin.read())\nresult = json.loads(data['result'])\n# Filter vla-only with conclusion=success\nvla_only = [e for e in result if 'vla-only' in e.get('exp_id','') and e.get('conclusion') == 'success']\nprint(f'Found {len(vla_only)} vla-only success experiments')\nfor e in vla_only:\n    print(f\\\"  {e['exp_id']}\\\")\nprint()\n# Filter obs_only experiments\nobs_only = [e for e in result if 'obs_only' in e.get('exp_id','') and e.get('conclusion') == 'success']\nprint(f'Found {len(obs_only)} obs_only success experiments')\nfor e in obs_only:\n    print(f\\\"  {e['exp_id']}\\\")\n\"\n",
  "description": "Filter registry for vla-only and obs_only experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_vla-baseline-aggregation_20260519T182814",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/dcc029ef-2962-4d39-bee8-d40a10c23560/tool-results/mcp-agent-ml-research-read_registry-1779215323676.txt | python3 -c \"\nimport json, sys\ndata = json.loads(sys.stdin.read())\nresult = json.loads(data['result'])\n# Filter vla-only with conclusion=success\nvla_only = [e for e in result if 'vla-only' in e.get('exp_id','') and e.get('conclusion') == 'success']\nprint(f'Found {len(vla_only)} vla-only success experiments')\nfor e in vla_only:\n    print(f\\\"  {e['exp_id']}\\\")\nprint()\n# Filter obs_only experiments\nobs_only = [e for e in result if 'obs_only' in e.get('exp_id','') and e.get('conclusion') == 'success']\nprint(f'Found {len(obs_only)} obs_only success experiments')\nfor e in obs_only:\n    print(f\\\"  {e['exp_id']}\\\")\n\"\n",
    "description": "Filter registry for vla-only and obs_only experiments"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-19T18:34:06.647847+00:00_

Exit code 1
Traceback (most recent call last):
  File "&lt;string>", line 6, in &lt;module>
    vla_only = [e for e in result if 'vla-only' in e.get('exp_id','') and e.get('conclusion') == 'success']
                                                   ^^^^^
AttributeError: 'str' object has no attribute 'get'

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_vla-baseline-aggregation_20260519T182814",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-19T18:34:06.648128+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "head -c 2000 /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/dcc029ef-2962-4d39-bee8-d40a10c23560/tool-results/mcp-agent-ml-research-read_registry-1779215323676.txt | python3 -c \"\nimport json, sys\ndata = json.loads(sys.stdin.read())\nr = data['result']\nprint(type(r))\nprint(r[:500])\n\"\n",
  "description": "Inspect registry data structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_vla-baseline-aggregation_20260519T182814",
  "tool": "Bash",
  "tool_args": {
    "command": "head -c 2000 /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/dcc029ef-2962-4d39-bee8-d40a10c23560/tool-results/mcp-agent-ml-research-read_registry-1779215323676.txt | python3 -c \"\nimport json, sys\ndata = json.loads(sys.stdin.read())\nr = data['result']\nprint(type(r))\nprint(r[:500])\n\"\n",
    "description": "Inspect registry data structure"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-19T18:34:06.648410+00:00_

Exit code 1
Traceback (most recent call last):
  File "&lt;string>", line 3, in &lt;module>
    data = json.loads(sys.stdin.read())
  File "/usr/lib/python3.14/json/__init__.py", line 352, in loads
    return _default_decoder.decode(s)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^
  File "/usr/lib/python3.14/json/decoder.py", line 345, in decode
    obj, end = self.raw_decode(s, idx=_w(s, 0).end())
               ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.14/json/decoder.py", line 361, in raw_decode
    obj, end = self.scan_once(s, idx)
               ~~~~~~~~~~~~~~^^^^^^^^
json.decoder.JSONDecodeError: Unterminated string starting at: line 1 column 11 (char 10)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_vla-baseline-aggregation_20260519T182814",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-19T18:34:06.648630+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/dcc029ef-2962-4d39-bee8-d40a10c23560/tool-results/mcp-agent-ml-research-read_registry-1779215323676.txt",
  "limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_vla-baseline-aggregation_20260519T182814",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/dcc029ef-2962-4d39-bee8-d40a10c23560/tool-results/mcp-agent-ml-research-read_registry-1779215323676.txt",
    "limit": "30"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-19T18:34:06.648848+00:00_

File content (219974 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_vla-baseline-aggregation_20260519T182814",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-19T18:34:06.649050+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport json\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/dcc029ef-2962-4d39-bee8-d40a10c23560/tool-results/mcp-agent-ml-research-read_registry-1779215323676.txt') as f:\n    data = json.load(f)\nresult_str = data['result']\n# It's a big string, parse it\nresult = json.loads(result_str)\nprint(type(result), len(result) if isinstance(result, list) else '')\nif isinstance(result, list) and len(result) > 0:\n    print(type(result[0]))\n    if isinstance(result[0], str):\n        # Maybe it's YAML or something else\n        print(result[0][:300])\n    elif isinstance(result[0], dict):\n        print(list(result[0].keys()))\n\" 2>&1 | head -20\n",
  "description": "Parse registry JSON structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_vla-baseline-aggregation_20260519T182814",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport json\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/dcc029ef-2962-4d39-bee8-d40a10c23560/tool-results/mcp-agent-ml-research-read_registry-1779215323676.txt') as f:\n    data = json.load(f)\nresult_str = data['result']\n# It's a big string, parse it\nresult = json.loads(result_str)\nprint(type(result), len(result) if isinstance(result, list) else '')\nif isinstance(result, list) and len(result) > 0:\n    print(type(result[0]))\n    if isinstance(result[0], str):\n        # Maybe it's YAML or something else\n        print(result[0][:300])\n    elif isinstance(result[0], dict):\n        print(list(result[0].keys()))\n\" 2>&1 | head -20\n",
    "description": "Parse registry JSON structure"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-19T18:34:06.649251+00:00_

&lt;class 'dict'>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_vla-baseline-aggregation_20260519T182814",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-19T18:34:06.649466+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport json\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/dcc029ef-2962-4d39-bee8-d40a10c23560/tool-results/mcp-agent-ml-research-read_registry-1779215323676.txt') as f:\n    data = json.load(f)\nresult = json.loads(data['result'])\nprint(type(result))\nprint(list(result.keys())[:20])\n\" 2>&1\n",
  "description": "Check registry dict keys"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_vla-baseline-aggregation_20260519T182814",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport json\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/dcc029ef-2962-4d39-bee8-d40a10c23560/tool-results/mcp-agent-ml-research-read_registry-1779215323676.txt') as f:\n    data = json.load(f)\nresult = json.loads(data['result'])\nprint(type(result))\nprint(list(result.keys())[:20])\n\" 2>&1\n",
    "description": "Check registry dict keys"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-19T18:34:06.649665+00:00_

&lt;class 'dict'>
['success', 'data', 'error', 'metadata']

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_vla-baseline-aggregation_20260519T182814",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-19T18:34:06.649872+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport json\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/dcc029ef-2962-4d39-bee8-d40a10c23560/tool-results/mcp-agent-ml-research-read_registry-1779215323676.txt') as f:\n    data = json.load(f)\nresult = json.loads(data['result'])\nexperiments = result['data']\nprint(f'Total experiments: {len(experiments)}')\nprint(f'Type: {type(experiments[0])}')\n# Filter vla-only success\nvla_only = [e for e in experiments if 'vla-only' in e.get('exp_id','') and e.get('conclusion') == 'success']\nprint(f'VLA-only success: {len(vla_only)}')\nfor e in vla_only:\n    print(f\\\"  {e['exp_id']}\\\")\nprint()\n# Filter obs_only success  \nobs_only = [e for e in experiments if 'obs_only' in e.get('exp_id','') and e.get('conclusion') == 'success']\nprint(f'obs_only success: {len(obs_only)}')\nfor e in obs_only:\n    print(f\\\"  {e['exp_id']}\\\")\n\" 2>&1\n",
  "description": "Filter vla-only and obs_only experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_vla-baseline-aggregation_20260519T182814",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport json\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/dcc029ef-2962-4d39-bee8-d40a10c23560/tool-results/mcp-agent-ml-research-read_registry-1779215323676.txt') as f:\n    data = json.load(f)\nresult = json.loads(data['result'])\nexperiments = result['data']\nprint(f'Total experiments: {len(experiments)}')\nprint(f'Type: {type(experiments[0])}')\n# Filter vla-only success\nvla_only = [e for e in experiments if 'vla-only' in e.get('exp_id','') and e.get('conclusion') == 'success']\nprint(f'VLA-only success: {len(vla_only)}')\nfor e in vla_only:\n    print(f\\\"  {e['exp_id']}\\\")\nprint()\n# Filter obs_only success  \nobs_only = [e for e in experiments if 'obs_only' in e.get('exp_id','') and e.get('conclusion') == 'success']\nprint(f'obs_only success: {len(obs_only)}')\nfor e in obs_only:\n    print(f\\\"  {e['exp_id']}\\\")\n\" 2>&1\n",
    "description": "Filter vla-only and obs_only experiments"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-19T18:34:06.650091+00:00_

Exit code 1
Traceback (most recent call last):
  File "&lt;string>", line 8, in &lt;module>
    print(f'Type: {type(experiments[0])}')
                        ~~~~~~~~~~~^^^
KeyError: 0
Total experiments: 4

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_vla-baseline-aggregation_20260519T182814",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-19T18:34:06.650304+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport json\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/dcc029ef-2962-4d39-bee8-d40a10c23560/tool-results/mcp-agent-ml-research-read_registry-1779215323676.txt') as f:\n    data = json.load(f)\nresult = json.loads(data['result'])\nexperiments = result['data']\nprint(type(experiments))\nif isinstance(experiments, dict):\n    print(list(experiments.keys())[:5])\n    # it's a dict keyed by exp_id\n    for k in experiments:\n        print(f'  Key: {k}, type: {type(experiments[k])}')\n\" 2>&1\n",
  "description": "Understand experiments data structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_vla-baseline-aggregation_20260519T182814",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport json\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/dcc029ef-2962-4d39-bee8-d40a10c23560/tool-results/mcp-agent-ml-research-read_registry-1779215323676.txt') as f:\n    data = json.load(f)\nresult = json.loads(data['result'])\nexperiments = result['data']\nprint(type(experiments))\nif isinstance(experiments, dict):\n    print(list(experiments.keys())[:5])\n    # it's a dict keyed by exp_id\n    for k in experiments:\n        print(f'  Key: {k}, type: {type(experiments[k])}')\n\" 2>&1\n",
    "description": "Understand experiments data structure"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-19T18:34:06.650523+00:00_

&lt;class 'dict'>
['experiments', 'count', 'total', 'baseline']
  Key: experiments, type: &lt;class 'dict'>
  Key: count, type: &lt;class 'int'>
  Key: total, type: &lt;class 'int'>
  Key: baseline, type: &lt;class 'NoneType'>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_vla-baseline-aggregation_20260519T182814",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-19T18:34:06.650734+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport json\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/dcc029ef-2962-4d39-bee8-d40a10c23560/tool-results/mcp-agent-ml-research-read_registry-1779215323676.txt') as f:\n    data = json.load(f)\nresult = json.loads(data['result'])\nexperiments = result['data']['experiments']\nprint(f'Total: {len(experiments)}')\n# Filter\nvla_only = {k:v for k,v in experiments.items() if 'vla-only' in k and v.get('conclusion') == 'success'}\nprint(f'VLA-only success: {len(vla_only)}')\nfor k in sorted(vla_only.keys()):\n    print(f'  {k}')\nprint()\nobs_only = {k:v for k,v in experiments.items() if 'obs_only' in k and v.get('conclusion') == 'success'}\nprint(f'obs_only success: {len(obs_only)}')\nfor k in sorted(obs_only.keys()):\n    print(f'  {k}')\n\" 2>&1\n",
  "description": "Filter experiments from nested structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_vla-baseline-aggregation_20260519T182814",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport json\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/dcc029ef-2962-4d39-bee8-d40a10c23560/tool-results/mcp-agent-ml-research-read_registry-1779215323676.txt') as f:\n    data = json.load(f)\nresult = json.loads(data['result'])\nexperiments = result['data']['experiments']\nprint(f'Total: {len(experiments)}')\n# Filter\nvla_only = {k:v for k,v in experiments.items() if 'vla-only' in k and v.get('conclusion') == 'success'}\nprint(f'VLA-only success: {len(vla_only)}')\nfor k in sorted(vla_only.keys()):\n    print(f'  {k}')\nprint()\nobs_only = {k:v for k,v in experiments.items() if 'obs_only' in k and v.get('conclusion') == 'success'}\nprint(f'obs_only success: {len(obs_only)}')\nfor k in sorted(obs_only.keys()):\n    print(f'  {k}')\n\" 2>&1\n",
    "description": "Filter experiments from nested structure"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-19T18:34:06.650957+00:00_

Total: 338
VLA-only success: 17
  eval-lto-splitA-vla-only-r2
  eval-lto-splitA-vla-only-r3
  eval-lto-splitA-vla-only-v2
  eval-openvla-object-vla-only-seed42-v2
  eval-vla-only-goal-seed42
  eval-vla-only-goal-seed43
  eval-vla-only-goal-seed44-r2
  eval-vla-only-object
  eval-vla-only-object-seed43
  eval-vla-only-object-seed44-r2
  eval-vla-only-object-seed45
  eval-vla-only-object-seed45-r2
  eval-vla-only-object-seed46
  eval-vla-only-spatial-seed42
  eval-vla-only-spatial-seed43
  eval-vla-only-spatial-seed44
  eval-vla-only-spatial-seed45

obs_only success: 2
  eval_obs_only_norm01_seed48
  eval_obs_only_norm03_seed48

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_vla-baseline-aggregation_20260519T182814",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-19T18:34:06.651165+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport json\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/dcc029ef-2962-4d39-bee8-d40a10c23560/tool-results/mcp-agent-ml-research-read_registry-1779215323676.txt') as f:\n    data = json.load(f)\nresult = json.loads(data['result'])\nexperiments = result['data']['experiments']\n\n# Also check for obs_only without conclusion filter\nobs_all = {k:v for k,v in experiments.items() if 'obs_only' in k}\nprint(f'obs_only ALL (any conclusion): {len(obs_all)}')\nfor k in sorted(obs_all.keys()):\n    print(f'  {k} -> conclusion={obs_all[k].get(\\\"conclusion\\\")}, status={obs_all[k].get(\\\"status\\\")}')\n\n# Also check for crm experiments\ncrm = {k:v for k,v in experiments.items() if 'crm' in k.lower() and v.get('conclusion') == 'success'}\nprint(f'\\nCRM success: {len(crm)}')\nfor k in sorted(crm.keys()):\n    print(f'  {k}')\n\" 2>&1\n",
  "description": "Check obs_only and CRM experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_vla-baseline-aggregation_20260519T182814",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport json\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/dcc029ef-2962-4d39-bee8-d40a10c23560/tool-results/mcp-agent-ml-research-read_registry-1779215323676.txt') as f:\n    data = json.load(f)\nresult = json.loads(data['result'])\nexperiments = result['data']['experiments']\n\n# Also check for obs_only without conclusion filter\nobs_all = {k:v for k,v in experiments.items() if 'obs_only' in k}\nprint(f'obs_only ALL (any conclusion): {len(obs_all)}')\nfor k in sorted(obs_all.keys()):\n    print(f'  {k} -> conclusion={obs_all[k].get(\\\"conclusion\\\")}, status={obs_all[k].get(\\\"status\\\")}')\n\n# Also check for crm experiments\ncrm = {k:v for k,v in experiments.items() if 'crm' in k.lower() and v.get('conclusion') == 'success'}\nprint(f'\\nCRM success: {len(crm)}')\nfor k in sorted(crm.keys()):\n    print(f'  {k}')\n\" 2>&1\n",
    "description": "Check obs_only and CRM experiments"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-19T18:34:06.651404+00:00_

obs_only ALL (any conclusion): 4
  eval_obs_only_norm01_seed48 -> conclusion=success, status=DONE
  eval_obs_only_norm03_seed48 -> conclusion=success, status=DONE
  mag_obs_only_norm01_seed46 -> conclusion=killed, status=DONE
  mag_obs_only_norm01_seed47 -> conclusion=killed, status=DONE

CRM success: 12
  crm-lto-splitA-train
  crm-lto-splitA-train-fixed
  crm-train-v2-obs-only
  crm-train-v2-perdof
  crm-train-v2-scalar-unc
  crm-train-v3-norm
  crm-train-v3-norm-obs-only
  crm-train-v3-norm-scalar-unc
  plan_701-crm-k1-train
  train-crm-k1-accg-object-seed42-fallback
  train-crm-k1-accg-object-seed42-full
  train-crm-k1-accg-object-seed42-v2

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_vla-baseline-aggregation_20260519T182814",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-19T18:34:06.651639+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport json\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/dcc029ef-2962-4d39-bee8-d40a10c23560/tool-results/mcp-agent-ml-research-read_registry-1779215323676.txt') as f:\n    data = json.load(f)\nresult = json.loads(data['result'])\nexperiments = result['data']['experiments']\n\n# Check for CRM eval obs_only experiments\ncrm_eval = {k:v for k,v in experiments.items() if ('eval' in k.lower() or 'crm' in k.lower()) and 'obs' in k.lower()}\nprint(f'CRM/eval obs_only: {len(crm_eval)}')\nfor k in sorted(crm_eval.keys()):\n    print(f'  {k} -> conclusion={crm_eval[k].get(\\\"conclusion\\\")}, status={crm_eval[k].get(\\\"status\\\")}')\n\n# More broadly, search for K=10 or K=5 obs_only norm02\nfor pattern in ['k10', 'k5', 'K10', 'K5', 'norm02', 'obs-only']:\n    matches = {k:v for k,v in experiments.items() if pattern in k}\n    if matches:\n        print(f'\\nPattern \\\"{pattern}\\\": {len(matches)}')\n        for k in sorted(matches.keys()):\n            print(f'  {k} -> conclusion={matches[k].get(\\\"conclusion\\\")}')\n\" 2>&1\n",
  "description": "Search for CRM obs_only eval experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_vla-baseline-aggregation_20260519T182814",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport json\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/dcc029ef-2962-4d39-bee8-d40a10c23560/tool-results/mcp-agent-ml-research-read_registry-1779215323676.txt') as f:\n    data = json.load(f)\nresult = json.loads(data['result'])\nexperiments = result['data']['experiments']\n\n# Check for CRM eval obs_only experiments\ncrm_eval = {k:v for k,v in experiments.items() if ('eval' in k.lower() or 'crm' in k.lower()) and 'obs' in k.lower()}\nprint(f'CRM/eval obs_only: {len(crm_eval)}')\nfor k in sorted(crm_eval.keys()):\n    print(f'  {k} -> conclusion={crm_eval[k].get(\\\"conclusion\\\")}, status={crm_eval[k].get(\\\"status\\\")}')\n\n# More broadly, search for K=10 or K=5 obs_only norm02\nfor pattern in ['k10', 'k5', 'K10', 'K5', 'norm02', 'obs-only']:\n    matches = {k:v for k,v in experiments.items() if pattern in k}\n    if matches:\n        print(f'\\nPattern \\\"{pattern}\\\": {len(matches)}')\n        for k in sorted(matches.keys()):\n            print(f'  {k} -> conclusion={matches[k].get(\\\"conclusion\\\")}')\n\" 2>&1\n",
    "description": "Search for CRM obs_only eval experiments"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-19T18:34:06.652020+00:00_

CRM/eval obs_only: 112
  crm-train-a3-obs-only -> conclusion=killed, status=DONE
  crm-train-v2-obs-only -> conclusion=success, status=DONE
  crm-train-v3-norm-obs-only -> conclusion=success, status=DONE
  crm-train-v3-obs-only -> conclusion=killed, status=DONE
  eval-acr-object-obs-only-default -> conclusion=success, status=DONE
  eval-acr-object-obs-only-norm02 -> conclusion=success, status=DONE
  eval-acr-object-v4-obs-only -> conclusion=success, status=DONE
  eval-acr-object-v4-obs-only-b2 -> conclusion=killed, status=DONE
  eval-acr-spatial-v4-obs-only -> conclusion=failed, status=DONE
  eval-acr-spatial-v4-obs-only-r2 -> conclusion=killed, status=DONE
  eval-acr-spatial-v4-obs-only-r3 -> conclusion=success, status=DONE
  eval-mag-obsonly-norm-0.3-r3 -> conclusion=killed, status=DONE
  eval-mag-obsonly-norm-0p3-r3 -> conclusion=killed, status=DONE
  eval-mag-obsonly-norm003 -> conclusion=killed, status=DONE
  eval-mag-obsonly-norm003-b2 -> conclusion=success, status=DONE
  eval-mag-obsonly-norm003-object -> conclusion=success, status=DONE
  eval-mag-obsonly-norm005 -> conclusion=success, status=DONE
  eval-mag-obsonly-norm005-object -> conclusion=success, status=DONE
  eval-mag-obsonly-norm02 -> conclusion=negative, status=DONE
  eval-mag-obsonly-norm02-object -> conclusion=killed, status=DONE
  eval-mag-obsonly-norm03 -> conclusion=killed, status=DONE
  eval-mag-obsonly-norm03-b2 -> conclusion=failed, status=DONE
  eval-mag-obsonly-norm03-b3 -> conclusion=killed, status=DONE
  eval-mag-obsonly-norm03-b4 -> conclusion=killed, status=DONE
  eval-mag-obsonly-norm03-object -> conclusion=success, status=DONE
  eval-mag-obsonly-norm03-r2 -> conclusion=success, status=DONE
  eval-obs-only-object-default-seed44 -> conclusion=success, status=DONE
  eval-obs-only-object-default-seed45 -> conclusion=success, status=DONE
  eval-obs-only-object-default-seed45-r2 -> conclusion=success, status=DONE
  eval-obs-only-object-default-seed46 -> conclusion=success, status=DONE
  ev
…[truncated 16529 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_vla-baseline-aggregation_20260519T182814",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-19T18:34:06.652306+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/dcc029ef-2962-4d39-bee8-d40a10c23560/tool-results/mcp-agent-ml-research-read_registry-1779215323676.txt') as f:\n    data = json.load(f)\nresult = json.loads(data['result'])\nexperiments = result['data']['experiments']\n\n# VLA-only success experiments\nvla_ids = [k for k in experiments if 'vla-only' in k and experiments[k].get('conclusion') == 'success']\nprint(\"=== VLA-ONLY EXPERIMENTS ===\")\nfor eid in sorted(vla_ids):\n    e = experiments[eid]\n    metrics = e.get('metrics', {})\n    print(f\"\\n--- {eid} ---\")\n    print(json.dumps(metrics, indent=2))\nPYEOF\n",
  "description": "Extract VLA-only experiment metrics"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_vla-baseline-aggregation_20260519T182814",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 << 'PYEOF'\nimport json\n\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/dcc029ef-2962-4d39-bee8-d40a10c23560/tool-results/mcp-agent-ml-research-read_registry-1779215323676.txt') as f:\n    data = json.load(f)\nresult = json.loads(data['result'])\nexperiments = result['data']['experiments']\n\n# VLA-only success experiments\nvla_ids = [k for k in experiments if 'vla-only' in k and experiments[k].get('conclusion') == 'success']\nprint(\"=== VLA-ONLY EXPERIMENTS ===\")\nfor eid in sorted(vla_ids):\n    e = experiments[eid]\n    metrics = e.get('metrics', {})\n    print(f\"\\n--- {eid} ---\")\n    print(json.dumps(metrics, indent=2))\nPYEOF\n",
    "description": "Extract VLA-only experiment metrics"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-19T18:34:06.652621+00:00_

=== VLA-ONLY EXPERIMENTS ===

--- eval-lto-splitA-vla-only-r2 ---
{
  "success_rate": 0.14,
  "n_tasks": 5,
  "n_rollouts": 10,
  "total_rollouts": 50,
  "successes": 7
}

--- eval-lto-splitA-vla-only-r3 ---
{
  "success_rate": 0.14,
  "n_tasks": 5,
  "n_rollouts": 10,
  "total_rollouts": 50,
  "successes": 7
}

--- eval-lto-splitA-vla-only-v2 ---
{
  "success_rate": 0.14,
  "n_tasks": 5,
  "n_rollouts": 10,
  "total_rollouts": 50,
  "successes": 7
}

--- eval-openvla-object-vla-only-seed42-v2 ---
{
  "overall_sr": 0.69,
  "n_tasks": 10,
  "n_trials_per_task": 10,
  "total_rollouts": 100
}

--- eval-vla-only-goal-seed42 ---
{
  "overall_success_rate": 0.71,
  "per_task": {
    "open_the_middle_drawer_of_the_cabinet": 0.9,
    "put_the_bowl_on_the_stove": 0.9,
    "put_the_wine_bottle_on_top_of_the_cabinet": 0.6,
    "open_the_top_drawer_and_put_the_bowl_inside": 0.4,
    "put_the_bowl_on_top_of_the_cabinet": 0.7,
    "push_the_plate_to_the_front_of_the_stove": 0.9,
    "put_the_cream_cheese_in_the_bowl": 0.2,
    "turn_on_the_stove": 0.9,
    "put_the_bowl_on_the_plate": 0.9,
    "put_the_wine_bottle_on_the_rack": 0.7
  }
}

--- eval-vla-only-goal-seed43 ---
{
  "overall_success_rate": 0.69,
  "per_task": {
    "open_the_middle_drawer_of_the_cabinet": 0.9,
    "put_the_bowl_on_the_stove": 0.9,
    "put_the_wine_bottle_on_top_of_the_cabinet": 0.4,
    "open_the_top_drawer_and_put_the_bowl_inside": 0.5,
    "put_the_bowl_on_top_of_the_cabinet": 0.5,
    "push_the_plate_to_the_front_of_the_stove": 0.8,
    "put_the_cream_cheese_in_the_bowl": 0.4,
    "turn_on_the_stove": 0.9,
    "put_the_bowl_on_the_plate": 1,
    "put_the_wine_bottle_on_the_rack": 0.6
  }
}

--- eval-vla-only-goal-seed44-r2 ---
{
  "success_rate": 0.73,
  "per_task": {
    "open_the_middle_drawer_of_the_cabinet": 0.8,
    "put_the_bowl_on_the_stove": 0.9,
    "put_the_wine_bottle_on_top_of_the_cabinet": 0.4,
    "open_the_top_drawer_and_put_the_bowl_inside": 0.6,
    "put_the_bowl_on_top_of_the_cabin
…[truncated 4648 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_vla-baseline-aggregation_20260519T182814",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-19T18:34:06.652890+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/dcc029ef-2962-4d39-bee8-d40a10c23560/tool-results/mcp-agent-ml-research-read_registry-1779215323676.txt') as f:\n    data = json.load(f)\nresult = json.loads(data['result'])\nexperiments = result['data']['experiments']\n\n# CRM obs_only experiments for Object K=10 norm02 (no k5 in name, has norm02)\ntarget_ids = [\n    # Object K=10 obs_only norm02 (default K is 10)\n    'eval-obs-only-object-norm02-seed43-r2',\n    'eval-obs-only-object-norm02-seed44-r2',\n    'eval-obs-only-object-norm02-seed45',\n    'eval-obs-only-object-norm02-seed46',\n    'eval-obs-only-object-norm02-seed47',\n    'eval-obs-only-object-norm02-seed48-r2',\n    # Spatial K=10 obs_only norm02\n    'eval-obs-only-spatial-norm02-seed44',\n    'eval-obs-only-spatial-norm02-seed45',\n    'eval-obs-only-spatial-norm02-seed47',\n    # Object K=5 obs_only norm02\n    'eval-obs-only-object-norm02-k5-seed42',\n    'eval-obs-only-object-norm02-k5-seed43',\n    'eval-obs-only-object-norm02-k5-seed44',\n    'eval-obs-only-object-norm02-k5-seed45',\n    'eval-obs-only-object-norm02-k5-seed46',\n    'eval-obs-only-object-norm02-k5-seed47',\n    'eval-obs-only-object-norm02-k5-seed48',\n    # Spatial K=5 obs_only norm02\n    'eval-obs-only-spatial-norm02-k5-seed42',\n    'eval-obs-only-spatial-norm02-k5-seed43',\n    'eval-obs-only-spatial-norm02-k5-seed44-r2',\n    'eval-obs-only-spatial-norm02-k5-seed45-r2',\n]\n\nprint(\"=== CRM OBS_ONLY EXPERIMENTS ===\")\nfor eid in target_ids:\n    if eid in experiments:\n        e = experiments[eid]\n        metrics = e.get('metrics', {})\n        print(f\"\\n--- {eid} (conclusion={e.get('conclusion')}) ---\")\n        print(json.dumps(metrics, indent=2))\n    else:\n        print(f\"\\n--- {eid} --- NOT FOUND\")\nPYEOF\n",
  "description": "Extract CRM obs_only experiment metrics"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_vla-baseline-aggregation_20260519T182814",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 << 'PYEOF'\nimport json\n\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/dcc029ef-2962-4d39-bee8-d40a10c23560/tool-results/mcp-agent-ml-research-read_registry-1779215323676.txt') as f:\n    data = json.load(f)\nresult = json.loads(data['result'])\nexperiments = result['data']['experiments']\n\n# CRM obs_only experiments for Object K=10 norm02 (no k5 in name, has norm02)\ntarget_ids = [\n    # Object K=10 obs_only norm02 (default K is 10)\n    'eval-obs-only-object-norm02-seed43-r2',\n    'eval-obs-only-object-norm02-seed44-r2',\n    'eval-obs-only-object-norm02-seed45',\n    'eval-obs-only-object-norm02-seed46',\n    'eval-obs-only-object-norm02-seed47',\n    'eval-obs-only-object-norm02-seed48-r2',\n    # Spatial K=10 obs_only norm02\n    'eval-obs-only-spatial-norm02-seed44',\n    'eval-obs-only-spatial-norm02-seed45',\n    'eval-obs-only-spatial-norm02-seed47',\n    # Object K=5 obs_only norm02\n    'eval-obs-only-object-norm02-k5-seed42',\n    'eval-obs-only-object-norm02-k5-seed43',\n    'eval-obs-only-object-norm02-k5-seed44',\n    'eval-obs-only-object-norm02-k5-seed45',\n    'eval-obs-only-object-norm02-k5-seed46',\n    'eval-obs-only-object-norm02-k5-seed47',\n    'eval-obs-only-object-norm02-k5-seed48',\n    # Spatial K=5 obs_only norm02\n    'eval-obs-only-spatial-norm02-k5-seed42',\n    'eval-obs-only-spatial-norm02-k5-seed43',\n    'eval-obs-only-spatial-norm02-k5-seed44-r2',\n    'eval-obs-only-spatial-norm02-k5-seed45-r2',\n]\n\nprint(\"=== CRM OBS_ONLY EXPERIMENTS ===\")\nfor eid in target_ids:\n    if eid in experiments:\n        e = experiments[eid]\n        metrics = e.get('metrics', {})\n        print(f\"\\n--- {eid} (conclusion={e.get('conclusion')}) ---\")\n        print(json.dumps(metrics, indent=2))\n    else:\n        print(f\"\\n--- {eid} --- NOT FOUND\")\nPYEOF\n",
    "description": "Extract CRM obs_only experiment metrics"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-19T18:34:06.653251+00:00_

=== CRM OBS_ONLY EXPERIMENTS ===

--- eval-obs-only-object-norm02-seed43-r2 (conclusion=success) ---
{
  "overall_sr": 0.16,
  "successes": 16,
  "total": 100,
  "per_task": {
    "alphabet_soup": 0,
    "cream_cheese": 0.1,
    "salad_dressing": 0.2,
    "bbq_sauce": 0.4,
    "ketchup": 0,
    "tomato_sauce": 0.1,
    "butter": 0.1,
    "milk": 0.1,
    "chocolate_pudding": 0.4,
    "orange_juice": 0.2
  },
  "vs_seed42": "-6pp (22% \u2192 16%)",
  "vs_argmin_seed43": "-1pp (17% \u2192 16%)",
  "pooled_2seed_obs_only_02": "19% (38/200)",
  "pooled_2seed_argmin": "14.5% (29/200)"
}

--- eval-obs-only-object-norm02-seed44-r2 (conclusion=success) ---
{
  "overall_sr": 0.16,
  "per_task_sr": {
    "alphabet_soup": 0,
    "cream_cheese": 0.1,
    "salad_dressing": 0.2,
    "bbq_sauce": 0.2,
    "ketchup": 0.1,
    "tomato_sauce": 0.1,
    "butter": 0.2,
    "milk": 0.1,
    "chocolate_pudding": 0.3,
    "orange_juice": 0.3
  }
}

--- eval-obs-only-object-norm02-seed45 (conclusion=success) ---
{
  "overall_sr": 0.16,
  "successes": 16,
  "total_rollouts": 100,
  "tasks_completed": "10/10"
}

--- eval-obs-only-object-norm02-seed46 (conclusion=success) ---
{
  "success_rate": 0.15,
  "total_episodes": 100,
  "successes": 15,
  "per_task": {
    "alphabet_soup": 0,
    "cream_cheese": 0,
    "salad_dressing": 2,
    "bbq_sauce": 3,
    "ketchup": 0,
    "tomato_sauce": 1,
    "butter": 1,
    "milk": 1,
    "chocolate_pudding": 4,
    "orange_juice": 3
  }
}

--- eval-obs-only-object-norm02-seed47 (conclusion=success) ---
{
  "success_rate": 0.2,
  "successes": 20,
  "total": 100,
  "benchmark": "object",
  "mode": "obs_only",
  "norm": 0.2,
  "seed": 47
}

--- eval-obs-only-object-norm02-seed48-r2 (conclusion=success) ---
{
  "success_rate": 0.18,
  "n_tasks": 10,
  "n_rollouts": 10,
  "total_rollouts": 100
}

--- eval-obs-only-spatial-norm02-seed44 (conclusion=success) ---
{
  "success_rate": 0.36,
  "successes": 36,
  "total": 100
}

--- eval-obs-only-spatial-norm02-seed
…[truncated 3451 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_vla-baseline-aggregation_20260519T182814",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-19T18:34:06.653553+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/dcc029ef-2962-4d39-bee8-d40a10c23560/tool-results/mcp-agent-ml-research-read_registry-1779215323676.txt') as f:\n    data = json.load(f)\nresult = json.loads(data['result'])\nexperiments = result['data']['experiments']\n\n# Check eval-openvla-object-vla-only-seed42-v2\ne = experiments.get('eval-openvla-object-vla-only-seed42-v2', {})\nprint(\"eval-openvla-object-vla-only-seed42-v2:\")\nprint(json.dumps(e.get('metrics', {}), indent=2))\nprint(f\"  notes: {e.get('notes','')[:200]}\")\nprint()\n\n# eval-vla-only-object (presumably seed42)\ne = experiments.get('eval-vla-only-object', {})\nprint(\"eval-vla-only-object:\")\nprint(f\"  notes: {e.get('notes','')[:200]}\")\nprint()\n\n# eval-vla-only-object-seed45 - has 200 rollouts, seems like a different run\ne = experiments.get('eval-vla-only-object-seed45', {})\nprint(\"eval-vla-only-object-seed45:\")\nprint(json.dumps(e.get('metrics', {}), indent=2))\nprint(f\"  notes: {e.get('notes','')[:200]}\")\nprint()\n\n# eval-vla-only-object-seed45-r2\ne = experiments.get('eval-vla-only-object-seed45-r2', {})\nprint(\"eval-vla-only-object-seed45-r2:\")\nprint(json.dumps(e.get('metrics', {}), indent=2))\n\n# LTO experiments\nfor eid in ['eval-lto-splitA-vla-only-r2', 'eval-lto-splitA-vla-only-r3', 'eval-lto-splitA-vla-only-v2']:\n    e = experiments[eid]\n    print(f\"\\n{eid}:\")\n    print(f\"  notes: {e.get('notes','')[:300]}\")\nPYEOF\n",
  "description": "Check specific experiment details"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_vla-baseline-aggregation_20260519T182814",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 << 'PYEOF'\nimport json\n\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/dcc029ef-2962-4d39-bee8-d40a10c23560/tool-results/mcp-agent-ml-research-read_registry-1779215323676.txt') as f:\n    data = json.load(f)\nresult = json.loads(data['result'])\nexperiments = result['data']['experiments']\n\n# Check eval-openvla-object-vla-only-seed42-v2\ne = experiments.get('eval-openvla-object-vla-only-seed42-v2', {})\nprint(\"eval-openvla-object-vla-only-seed42-v2:\")\nprint(json.dumps(e.get('metrics', {}), indent=2))\nprint(f\"  notes: {e.get('notes','')[:200]}\")\nprint()\n\n# eval-vla-only-object (presumably seed42)\ne = experiments.get('eval-vla-only-object', {})\nprint(\"eval-vla-only-object:\")\nprint(f\"  notes: {e.get('notes','')[:200]}\")\nprint()\n\n# eval-vla-only-object-seed45 - has 200 rollouts, seems like a different run\ne = experiments.get('eval-vla-only-object-seed45', {})\nprint(\"eval-vla-only-object-seed45:\")\nprint(json.dumps(e.get('metrics', {}), indent=2))\nprint(f\"  notes: {e.get('notes','')[:200]}\")\nprint()\n\n# eval-vla-only-object-seed45-r2\ne = experiments.get('eval-vla-only-object-seed45-r2', {})\nprint(\"eval-vla-only-object-seed45-r2:\")\nprint(json.dumps(e.get('metrics', {}), indent=2))\n\n# LTO experiments\nfor eid in ['eval-lto-splitA-vla-only-r2', 'eval-lto-splitA-vla-only-r3', 'eval-lto-splitA-vla-only-v2']:\n    e = experiments[eid]\n    print(f\"\\n{eid}:\")\n    print(f\"  notes: {e.get('notes','')[:300]}\")\nPYEOF\n",
    "description": "Check specific experiment details"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-19T18:34:06.653786+00:00_

eval-openvla-object-vla-only-seed42-v2:
{
  "overall_sr": 0.69,
  "n_tasks": 10,
  "n_trials_per_task": 10,
  "total_rollouts": 100
}
  notes: 

eval-vla-only-object:
  notes: 

eval-vla-only-object-seed45:
{
  "overall_sr": 0.09,
  "successes": 18,
  "total": 200,
  "tasks_done": 10
}
  notes: 

eval-vla-only-object-seed45-r2:
{
  "overall_success_rate": 0.11,
  "n_tasks": 10,
  "n_rollouts_per_task": 10,
  "total_rollouts": 100,
  "per_task": {
    "alphabet_soup": 0,
    "cream_cheese": 0.3,
    "salad_dressing": 0.2,
    "bbq_sauce": 0.2,
    "ketchup": 0,
    "tomato_sauce": 0.1,
    "butter": 0,
    "milk": 0,
    "chocolate_pudding": 0.1,
    "orange_juice": 0.2
  }
}

eval-lto-splitA-vla-only-r2:
  notes: 

eval-lto-splitA-vla-only-r3:
  notes: 

eval-lto-splitA-vla-only-v2:
  notes:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_vla-baseline-aggregation_20260519T182814",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-19T18:34:06.654032+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/dcc029ef-2962-4d39-bee8-d40a10c23560/tool-results/mcp-agent-ml-research-read_registry-1779215323676.txt') as f:\n    data = json.load(f)\nresult = json.loads(data['result'])\nexperiments = result['data']['experiments']\n\n# Check full detail of eval-openvla-object-vla-only-seed42-v2\ne = experiments.get('eval-openvla-object-vla-only-seed42-v2', {})\nprint(\"eval-openvla-object-vla-only-seed42-v2 FULL:\")\n# print all keys except metrics\nfor k, v in e.items():\n    if k != 'metrics':\n        val_str = str(v)[:300]\n        print(f\"  {k}: {val_str}\")\nprint()\n\n# Check description/config for eval-vla-only-object (is it the same model?)\ne = experiments.get('eval-vla-only-object', {})\nprint(\"eval-vla-only-object FULL:\")\nfor k, v in e.items():\n    if k != 'metrics':\n        val_str = str(v)[:300]\n        print(f\"  {k}: {val_str}\")\n\n# Check LTO experiments - are these different seeds or same?\nprint(\"\\n\\nLTO EXPERIMENTS FULL:\")\nfor eid in ['eval-lto-splitA-vla-only-r2', 'eval-lto-splitA-vla-only-r3', 'eval-lto-splitA-vla-only-v2']:\n    e = experiments[eid]\n    print(f\"\\n{eid}:\")\n    for k, v in e.items():\n        if k not in ['metrics']:\n            val_str = str(v)[:300]\n            print(f\"  {k}: {val_str}\")\nPYEOF\n",
  "description": "Check experiment configs for model identity"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_vla-baseline-aggregation_20260519T182814",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 << 'PYEOF'\nimport json\n\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/dcc029ef-2962-4d39-bee8-d40a10c23560/tool-results/mcp-agent-ml-research-read_registry-1779215323676.txt') as f:\n    data = json.load(f)\nresult = json.loads(data['result'])\nexperiments = result['data']['experiments']\n\n# Check full detail of eval-openvla-object-vla-only-seed42-v2\ne = experiments.get('eval-openvla-object-vla-only-seed42-v2', {})\nprint(\"eval-openvla-object-vla-only-seed42-v2 FULL:\")\n# print all keys except metrics\nfor k, v in e.items():\n    if k != 'metrics':\n        val_str = str(v)[:300]\n        print(f\"  {k}: {val_str}\")\nprint()\n\n# Check description/config for eval-vla-only-object (is it the same model?)\ne = experiments.get('eval-vla-only-object', {})\nprint(\"eval-vla-only-object FULL:\")\nfor k, v in e.items():\n    if k != 'metrics':\n        val_str = str(v)[:300]\n        print(f\"  {k}: {val_str}\")\n\n# Check LTO experiments - are these different seeds or same?\nprint(\"\\n\\nLTO EXPERIMENTS FULL:\")\nfor eid in ['eval-lto-splitA-vla-only-r2', 'eval-lto-splitA-vla-only-r3', 'eval-lto-splitA-vla-only-v2']:\n    e = experiments[eid]\n    print(f\"\\n{eid}:\")\n    for k, v in e.items():\n        if k not in ['metrics']:\n            val_str = str(v)[:300]\n            print(f\"  {k}: {val_str}\")\nPYEOF\n",
    "description": "Check experiment configs for model identity"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-19T18:34:06.654378+00:00_

eval-openvla-object-vla-only-seed42-v2 FULL:
  status: DONE
  retry_count: 0
  created_at: 2026-05-17T20:06:55.243Z
  updated_at: 2026-05-17T22:39:25.302Z
  hypothesis: OpenVLA 7B finetuned VLA-only baseline on LIBERO-Object using official eval code (transformers 4.40.1, isolated conda env). v1 failed due to transformers 5.8 DynamicCache bug. Dry-run on libero_spatial confirmed 80% SR. This run uses openvla-libero-object finetuned model with 10 trials/task.
  spec: {'command': 'bash -c "source /root/autodl-tmp/conda_envs/openvla/bin/activate && cd /root/autodl-tmp/openvla && MUJOCO_GL=egl python experiments/robot/libero/run_libero_eval.py --model_family openvla --pretrained_checkpoint /root/autodl-tmp/models/openvla-libero-object --task_suite_name libero_objec
  conclusion: success
  completed_at: 2026-05-17T22:39:25.302Z

eval-vla-only-object FULL:
  status: DONE
  retry_count: 0
  created_at: 2026-05-15T02:54:57.323Z
  updated_at: 2026-05-15T04:47:47.959Z
  spec: {'command': 'python -u src/evaluate.py --benchmark object --mode vla_only --baseline_mode single --n_rollouts 10 --K 1 --output_file logs/eval_object_vla_only.json', 'server': 'bjb1-32546', 'data_path': 'LIBERO object benchmark', 'data_count': '10 tasks x 10 rollouts', 'model_name': 'SmolVLA (VLA-on
  conclusion: success
  hypothesis: VLA-only baseline (K=1, no mean, no CRM) on LIBERO object benchmark. Single sample from flow-matching VLA.
  gpu: bjb1-32546:cuda:4
  pid: 17222
  log_path: /root/acr-vla-conformal-refinement/logs/eval_object_vla_only.log
  checkpoint_path: /root/acr-vla-conformal-refinement/logs/eval_object_vla_only.json
  completed_at: 2026-05-15T04:42:20.025Z


LTO EXPERIMENTS FULL:

eval-lto-splitA-vla-only-r2:
  status: DONE
  retry_count: 0
  created_at: 2026-05-19T04:55:29.003Z
  updated_at: 2026-05-19T12:47:58.882Z
  spec: {'command': 'bash -c "source /root/miniconda3/bin/activate base && cd /root/acr-vla-conformal-refinement/src && CUDA_VISIBLE_DEVICES=2 timeout 57600 python -u eval
…[truncated 1810 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_vla-baseline-aggregation_20260519T182814",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-19T18:34:06.654679+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/dcc029ef-2962-4d39-bee8-d40a10c23560/tool-results/mcp-agent-ml-research-read_registry-1779215323676.txt') as f:\n    data = json.load(f)\nresult = json.loads(data['result'])\nexperiments = result['data']['experiments']\n\n# Search for \"long\" benchmark experiments\nlong_exps = {k:v for k,v in experiments.items() if 'long' in k.lower() and 'vla' in k.lower()}\nprint(f\"Long VLA experiments: {len(long_exps)}\")\nfor k in sorted(long_exps.keys()):\n    print(f\"  {k} -> conclusion={long_exps[k].get('conclusion')}\")\n\n# Also search for libero-10 or libero_10\nl10 = {k:v for k,v in experiments.items() if '10' in k.lower() and 'vla' in k.lower()}\nprint(f\"\\nLibero-10 VLA: {len(l10)}\")\nfor k in sorted(l10.keys()):\n    print(f\"  {k} -> conclusion={l10[k].get('conclusion')}\")\n\n# Also check for \"long\" benchmark in any experiment\nlong_any = {k:v for k,v in experiments.items() if 'long' in k.lower()}\nprint(f\"\\nAny 'long': {len(long_any)}\")\nfor k in sorted(long_any.keys()):\n    print(f\"  {k} -> conclusion={long_any[k].get('conclusion')}\")\nPYEOF\n",
  "description": "Search for LIBERO-Long experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_vla-baseline-aggregation_20260519T182814",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 << 'PYEOF'\nimport json\n\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/dcc029ef-2962-4d39-bee8-d40a10c23560/tool-results/mcp-agent-ml-research-read_registry-1779215323676.txt') as f:\n    data = json.load(f)\nresult = json.loads(data['result'])\nexperiments = result['data']['experiments']\n\n# Search for \"long\" benchmark experiments\nlong_exps = {k:v for k,v in experiments.items() if 'long' in k.lower() and 'vla' in k.lower()}\nprint(f\"Long VLA experiments: {len(long_exps)}\")\nfor k in sorted(long_exps.keys()):\n    print(f\"  {k} -> conclusion={long_exps[k].get('conclusion')}\")\n\n# Also search for libero-10 or libero_10\nl10 = {k:v for k,v in experiments.items() if '10' in k.lower() and 'vla' in k.lower()}\nprint(f\"\\nLibero-10 VLA: {len(l10)}\")\nfor k in sorted(l10.keys()):\n    print(f\"  {k} -> conclusion={l10[k].get('conclusion')}\")\n\n# Also check for \"long\" benchmark in any experiment\nlong_any = {k:v for k,v in experiments.items() if 'long' in k.lower()}\nprint(f\"\\nAny 'long': {len(long_any)}\")\nfor k in sorted(long_any.keys()):\n    print(f\"  {k} -> conclusion={long_any[k].get('conclusion')}\")\nPYEOF\n",
    "description": "Search for LIBERO-Long experiments"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-19T18:34:06.654907+00:00_

Long VLA experiments: 5
  eval-vla-only-long-seed42 -> conclusion=None
  eval-vla-only-long-seed43 -> conclusion=None
  eval-vla-only-long-seed44 -> conclusion=None
  eval-vla-only-long-seed45 -> conclusion=None
  eval-vla-only-long-seed46 -> conclusion=None

Libero-10 VLA: 1
  eval-vla-mean-spatial-t10 -> conclusion=success

Any 'long': 5
  eval-vla-only-long-seed42 -> conclusion=None
  eval-vla-only-long-seed43 -> conclusion=None
  eval-vla-only-long-seed44 -> conclusion=None
  eval-vla-only-long-seed45 -> conclusion=None
  eval-vla-only-long-seed46 -> conclusion=None

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_vla-baseline-aggregation_20260519T182814",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-19T18:34:06.655114+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/dcc029ef-2962-4d39-bee8-d40a10c23560/tool-results/mcp-agent-ml-research-read_registry-1779215323676.txt') as f:\n    data = json.load(f)\nresult = json.loads(data['result'])\nexperiments = result['data']['experiments']\n\n# Check long experiments - they are RUNNING\nfor eid in ['eval-vla-only-long-seed42', 'eval-vla-only-long-seed43', 'eval-vla-only-long-seed44', 'eval-vla-only-long-seed45', 'eval-vla-only-long-seed46']:\n    e = experiments[eid]\n    print(f\"{eid}:\")\n    print(f\"  status: {e.get('status')}, conclusion: {e.get('conclusion')}\")\n    print(f\"  metrics: {e.get('metrics', {})}\")\n    print()\nPYEOF\n",
  "description": "Check LIBERO-Long experiment status"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_vla-baseline-aggregation_20260519T182814",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 << 'PYEOF'\nimport json\n\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/dcc029ef-2962-4d39-bee8-d40a10c23560/tool-results/mcp-agent-ml-research-read_registry-1779215323676.txt') as f:\n    data = json.load(f)\nresult = json.loads(data['result'])\nexperiments = result['data']['experiments']\n\n# Check long experiments - they are RUNNING\nfor eid in ['eval-vla-only-long-seed42', 'eval-vla-only-long-seed43', 'eval-vla-only-long-seed44', 'eval-vla-only-long-seed45', 'eval-vla-only-long-seed46']:\n    e = experiments[eid]\n    print(f\"{eid}:\")\n    print(f\"  status: {e.get('status')}, conclusion: {e.get('conclusion')}\")\n    print(f\"  metrics: {e.get('metrics', {})}\")\n    print()\nPYEOF\n",
    "description": "Check LIBERO-Long experiment status"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-19T18:34:06.655352+00:00_

eval-vla-only-long-seed42:
  status: RUNNING, conclusion: None
  metrics: {}

eval-vla-only-long-seed43:
  status: RUNNING, conclusion: None
  metrics: {}

eval-vla-only-long-seed44:
  status: RUNNING, conclusion: None
  metrics: {}

eval-vla-only-long-seed45:
  status: RUNNING, conclusion: None
  metrics: {}

eval-vla-only-long-seed46:
  status: RUNNING, conclusion: None
  metrics: {}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_vla-baseline-aggregation_20260519T182814",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-19T18:34:06.655597+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/dcc029ef-2962-4d39-bee8-d40a10c23560/tool-results/mcp-agent-ml-research-read_registry-1779215323676.txt') as f:\n    data = json.load(f)\nresult = json.loads(data['result'])\nexperiments = result['data']['experiments']\n\n# Check if there's a spatial norm02 seed42 (K=10 default)\nspatial_norm02 = {k:v for k,v in experiments.items() if 'spatial' in k and 'norm02' in k and 'k5' not in k and 'k20' not in k}\nprint(\"Spatial norm02 K=10:\")\nfor k in sorted(spatial_norm02.keys()):\n    e = spatial_norm02[k]\n    sr = e.get('metrics', {}).get('success_rate', e.get('metrics', {}).get('overall_success_rate', 'N/A'))\n    print(f\"  {k}: conclusion={e.get('conclusion')}, SR={sr}\")\n\n# Also check eval-acr experiments for spatial obs_only\nacr_spatial = {k:v for k,v in experiments.items() if 'acr' in k and 'spatial' in k}\nprint(\"\\nACR Spatial:\")\nfor k in sorted(acr_spatial.keys()):\n    e = acr_spatial[k]\n    print(f\"  {k}: conclusion={e.get('conclusion')}, metrics={json.dumps(e.get('metrics',{}))[:200]}\")\n\n# Check the seed42 of obs_only object norm02 (K=10)\n# The original one might be eval-acr-object-obs-only-norm02\ne = experiments.get('eval-acr-object-obs-only-norm02', {})\nprint(f\"\\neval-acr-object-obs-only-norm02: conclusion={e.get('conclusion')}\")\nprint(f\"  metrics: {json.dumps(e.get('metrics', {}), indent=2)}\")\n\n# Also check eval-acr-object-obs-only-default as a potential seed42\ne = experiments.get('eval-acr-object-obs-only-default', {})\nprint(f\"\\neval-acr-object-obs-only-default: conclusion={e.get('conclusion')}\")\nprint(f\"  metrics: {json.dumps(e.get('metrics', {}), indent=2)}\")\nPYEOF\n",
  "description": "Check spatial K=10 norm02 and ACR experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_vla-baseline-aggregation_20260519T182814",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 << 'PYEOF'\nimport json\n\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/dcc029ef-2962-4d39-bee8-d40a10c23560/tool-results/mcp-agent-ml-research-read_registry-1779215323676.txt') as f:\n    data = json.load(f)\nresult = json.loads(data['result'])\nexperiments = result['data']['experiments']\n\n# Check if there's a spatial norm02 seed42 (K=10 default)\nspatial_norm02 = {k:v for k,v in experiments.items() if 'spatial' in k and 'norm02' in k and 'k5' not in k and 'k20' not in k}\nprint(\"Spatial norm02 K=10:\")\nfor k in sorted(spatial_norm02.keys()):\n    e = spatial_norm02[k]\n    sr = e.get('metrics', {}).get('success_rate', e.get('metrics', {}).get('overall_success_rate', 'N/A'))\n    print(f\"  {k}: conclusion={e.get('conclusion')}, SR={sr}\")\n\n# Also check eval-acr experiments for spatial obs_only\nacr_spatial = {k:v for k,v in experiments.items() if 'acr' in k and 'spatial' in k}\nprint(\"\\nACR Spatial:\")\nfor k in sorted(acr_spatial.keys()):\n    e = acr_spatial[k]\n    print(f\"  {k}: conclusion={e.get('conclusion')}, metrics={json.dumps(e.get('metrics',{}))[:200]}\")\n\n# Check the seed42 of obs_only object norm02 (K=10)\n# The original one might be eval-acr-object-obs-only-norm02\ne = experiments.get('eval-acr-object-obs-only-norm02', {})\nprint(f\"\\neval-acr-object-obs-only-norm02: conclusion={e.get('conclusion')}\")\nprint(f\"  metrics: {json.dumps(e.get('metrics', {}), indent=2)}\")\n\n# Also check eval-acr-object-obs-only-default as a potential seed42\ne = experiments.get('eval-acr-object-obs-only-default', {})\nprint(f\"\\neval-acr-object-obs-only-default: conclusion={e.get('conclusion')}\")\nprint(f\"  metrics: {json.dumps(e.get('metrics', {}), indent=2)}\")\nPYEOF\n",
    "description": "Check spatial K=10 norm02 and ACR experiments"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-19T18:34:06.655891+00:00_

Spatial norm02 K=10:
  eval-obs-only-spatial-norm02-seed43: conclusion=failed, SR=N/A
  eval-obs-only-spatial-norm02-seed43-r2: conclusion=None, SR=N/A
  eval-obs-only-spatial-norm02-seed44: conclusion=success, SR=0.36
  eval-obs-only-spatial-norm02-seed45: conclusion=success, SR=0.34
  eval-obs-only-spatial-norm02-seed46: conclusion=failed, SR=N/A
  eval-obs-only-spatial-norm02-seed46-r2: conclusion=None, SR=N/A
  eval-obs-only-spatial-norm02-seed47: conclusion=success, SR=0.32

ACR Spatial:
  eval-acr-spatial-v1: conclusion=killed, metrics={}
  eval-acr-spatial-v2: conclusion=killed, metrics={}
  eval-acr-spatial-v3: conclusion=success, metrics={"tasks_done": "4/10", "overall_success_rate": 0.025, "total_successes": 1, "total_rollouts": 40, "per_task_partial": {"pick_up_black_bowl_between_plate_and_ramekin": 0.1, "pick_up_black_bowl_next_to_
  eval-acr-spatial-v4-default: conclusion=failed, metrics={"tasks_done": "0/10", "status_alert": "NO PROCESS FOUND - registry says RUNNING but no matching PID or tmux session on bjb1-18228. GPU 0 occupied by stale eval-acr-spatial-v3 tmux + crm-train-obs-onl
  eval-acr-spatial-v4-default-r2: conclusion=killed, metrics={}
  eval-acr-spatial-v4-default-r3: conclusion=killed, metrics={}
  eval-acr-spatial-v4-obs-only: conclusion=failed, metrics={}
  eval-acr-spatial-v4-obs-only-r2: conclusion=killed, metrics={"tasks_done": "6/10", "partial_results": {"between_plate_and_ramekin": "90.0% (9/10)", "next_to_ramekin": "100.0% (10/10)", "from_table_center": "0.0% (0/10)", "on_cookie_box": "40.0% (4/10)", "in_to
  eval-acr-spatial-v4-obs-only-r3: conclusion=success, metrics={"overall_sr": "35.0% (35/100)", "total_success": 35, "total_rollouts": 100, "mode": "crm_obs_only", "benchmark": "spatial", "max_correction_norm": 0.1, "seed": 42, "K": 10, "per_task": {"T0": "90%", 
  eval-acr-spatial-v4-scalar: conclusion=killed, metrics={"tasks_done": "3/10", "partial_results": {"between_plate_and_ramekin": "60.0% (6/10)", "next_to_ramekin": "100
…[truncated 1740 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_vla-baseline-aggregation_20260519T182814",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-19T18:34:06.656168+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/dcc029ef-2962-4d39-bee8-d40a10c23560/tool-results/mcp-agent-ml-research-read_registry-1779215323676.txt') as f:\n    data = json.load(f)\nresult = json.loads(data['result'])\nexperiments = result['data']['experiments']\n\n# Check seed info for the acr experiments\nfor eid in ['eval-acr-object-obs-only-norm02', 'eval-acr-spatial-v4-obs-only-r3']:\n    e = experiments[eid]\n    spec = e.get('spec', {})\n    hyp = e.get('hypothesis', '')\n    cmd = spec.get('command', '')[:500] if isinstance(spec, dict) else ''\n    print(f\"{eid}:\")\n    print(f\"  hypothesis: {hyp[:300]}\")\n    print(f\"  command: {cmd}\")\n    print(f\"  metrics seed: {e.get('metrics',{}).get('seed','N/A')}\")\n    print()\n\n# Also check object norm02 seed42 existence\nobj_norm02_seed42 = {k:v for k,v in experiments.items() \n                     if 'object' in k and 'norm02' in k and 'seed42' in k and 'obs' in k}\nprint(\"Object norm02 seed42 obs-only:\")\nfor k in sorted(obj_norm02_seed42.keys()):\n    print(f\"  {k}: conclusion={obj_norm02_seed42[k].get('conclusion')}\")\nPYEOF\n",
  "description": "Check seed info for ACR experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_vla-baseline-aggregation_20260519T182814",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 << 'PYEOF'\nimport json\n\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/dcc029ef-2962-4d39-bee8-d40a10c23560/tool-results/mcp-agent-ml-research-read_registry-1779215323676.txt') as f:\n    data = json.load(f)\nresult = json.loads(data['result'])\nexperiments = result['data']['experiments']\n\n# Check seed info for the acr experiments\nfor eid in ['eval-acr-object-obs-only-norm02', 'eval-acr-spatial-v4-obs-only-r3']:\n    e = experiments[eid]\n    spec = e.get('spec', {})\n    hyp = e.get('hypothesis', '')\n    cmd = spec.get('command', '')[:500] if isinstance(spec, dict) else ''\n    print(f\"{eid}:\")\n    print(f\"  hypothesis: {hyp[:300]}\")\n    print(f\"  command: {cmd}\")\n    print(f\"  metrics seed: {e.get('metrics',{}).get('seed','N/A')}\")\n    print()\n\n# Also check object norm02 seed42 existence\nobj_norm02_seed42 = {k:v for k,v in experiments.items() \n                     if 'object' in k and 'norm02' in k and 'seed42' in k and 'obs' in k}\nprint(\"Object norm02 seed42 obs-only:\")\nfor k in sorted(obj_norm02_seed42.keys()):\n    print(f\"  {k}: conclusion={obj_norm02_seed42[k].get('conclusion')}\")\nPYEOF\n",
    "description": "Check seed info for ACR experiments"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-19T18:34:06.656412+00:00_

eval-acr-object-obs-only-norm02:
  hypothesis: ACR with obs-only CRM and max_correction_norm=0.2 on LIBERO-Object achieves meaningful improvement over VLA-only baseline by applying visually-guided corrections without requiring action history
  command: python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_obs_only_norm02.json
  metrics seed: N/A

eval-acr-spatial-v4-obs-only-r3:
  hypothesis: Restart from T6. obs_only CRM v3-norm with max_correction_norm=0.1 on spatial. If obs_only >= perdof, conformal features need restructuring.
  command: python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1 --start_task 6
  metrics seed: 42

Object norm02 seed42 obs-only:
  eval-obs-only-object-norm02-k20-seed42: conclusion=killed
  eval-obs-only-object-norm02-k5-seed42: conclusion=success

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_vla-baseline-aggregation_20260519T182814",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-19T18:34:06.656727+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport numpy as np\n\n# ============================================================\n# VLA-ONLY BASELINES\n# ============================================================\n\n# --- LIBERO-Object ---\nobject_seeds = {\n    42: {'sr': 0.12, 'exp': 'eval-vla-only-object',\n         'per_task': {'alphabet_soup':0,'cream_cheese':0.1,'salad_dressing':0.2,'bbq_sauce':0.2,'ketchup':0,'tomato_sauce':0.1,'butter':0,'milk':0.1,'chocolate_pudding':0.2,'orange_juice':0.3}},\n    43: {'sr': 0.12, 'exp': 'eval-vla-only-object-seed43',\n         'per_task': {'alphabet_soup':0,'cream_cheese':0.1,'salad_dressing':0.1,'bbq_sauce':0.3,'ketchup':0,'tomato_sauce':0,'butter':0,'milk':0.1,'chocolate_pudding':0.4,'orange_juice':0.2}},\n    44: {'sr': 0.10, 'exp': 'eval-vla-only-object-seed44-r2',\n         'per_task': {'alphabet_soup':0,'cream_cheese':0.1,'salad_dressing':0.2,'bbq_sauce':0.2,'ketchup':0,'tomato_sauce':0,'butter':0,'milk':0.1,'chocolate_pudding':0.2,'orange_juice':0.2}},\n    45: {'sr': 0.11, 'exp': 'eval-vla-only-object-seed45-r2',\n         'per_task': {'alphabet_soup':0,'cream_cheese':0.3,'salad_dressing':0.2,'bbq_sauce':0.2,'ketchup':0,'tomato_sauce':0.1,'butter':0,'milk':0,'chocolate_pudding':0.1,'orange_juice':0.2}},\n    46: {'sr': 0.13, 'exp': 'eval-vla-only-object-seed46',\n         'per_task': None},\n}\n\n# --- LIBERO-Spatial ---\nspatial_seeds = {\n    42: {'sr': 0.30, 'exp': 'eval-vla-only-spatial-seed42',\n         'per_task': {'between_plate_and_ramekin':0.6,'next_to_ramekin':1.0,'from_table_center':0,'on_cookie_box':0.2,'in_top_drawer':0,'on_ramekin':0,'next_to_cookie_box':0.9,'on_stove':0,'next_to_plate':0.3,'on_wooden_cabinet':0}},\n    43: {'sr': 0.29, 'exp': 'eval-vla-only-spatial-seed43',\n         'per_task': {'between_plate_and_ramekin':0.7,'next_to_ramekin':0.8,'from_table_center':0.1,'on_cookie_box':0.3,'in_top_drawer':0,'on_ramekin':0,'next_to_cookie_box':0.9,'on_stove':0,'next_to_plate':0.1,'on_wooden_cabinet':0}},\n    44: {'sr': 0.31, 'exp': 'eval-vla-only-spatial-seed44',\n         'per_task': {'between_plate_and_ramekin':0.6,'next_to_ramekin':1.0,'from_table_center':0,'on_cookie_box':0.3,'in_top_drawer':0,'on_ramekin':0,'next_to_cookie_box':0.9,'on_stove':0,'next_to_plate':0.3,'on_wooden_cabinet':0}},\n    45: {'sr': 0.27, 'exp': 'eval-vla-only-spatial-seed45',\n         'per_task': {'between_plate_and_ramekin':0.7,'next_to_ramekin':0.9,'from_table_center':0,'on_cookie_box':0.2,'in_top_drawer':0,'on_ramekin':0,'next_to_cookie_box':0.9,'on_stove':0,'next_to_plate':0,'on_wooden_cabinet':0}},\n}\n\n# --- LIBERO-Goal ---\ngoal_seeds = {\n    42: {'sr': 0.71, 'exp': 'eval-vla-only-goal-seed42',\n         'per_task': {'open_middle_drawer':0.9,'bowl_on_stove':0.9,'wine_on_cabinet':0.6,'drawer_bowl_inside':0.4,'bowl_on_cabinet':0.7,'plate_front_stove':0.9,'cream_cheese_in_bowl':0.2,'turn_on_stove':0.9,'bowl_on_plate':0.9,'wine_on_rack':0.7}},\n    43: {'sr': 0.69, 'exp': 'eval-vla-only-goal-seed43',\n         'per_task': {'open_middle_drawer':0.9,'bowl_on_stove':0.9,'wine_on_cabinet':0.4,'drawer_bowl_inside':0.5,'bowl_on_cabinet':0.5,'plate_front_stove':0.8,'cream_cheese_in_bowl':0.4,'turn_on_stove':0.9,'bowl_on_plate':1.0,'wine_on_rack':0.6}},\n    44: {'sr': 0.73, 'exp': 'eval-vla-only-goal-seed44-r2',\n         'per_task': {'open_middle_drawer':0.8,'bowl_on_stove':0.9,'wine_on_cabinet':0.4,'drawer_bowl_inside':0.6,'bowl_on_cabinet':0.7,'plate_front_stove':0.9,'cream_cheese_in_bowl':0.3,'turn_on_stove':0.9,'bowl_on_plate':1.0,'wine_on_rack':0.8}},\n}\n\n# --- LIBERO-Long ---\n# All 5 seeds (42-46) are RUNNING, no results yet\n\n# --- LTO Split-A ---\nlto_seeds = {\n    'r2': {'sr': 0.14, 'exp': 'eval-lto-splitA-vla-only-r2'},\n    'r3': {'sr': 0.14, 'exp': 'eval-lto-splitA-vla-only-r3'},\n    'v2': {'sr': 0.14, 'exp': 'eval-lto-splitA-vla-only-v2'},\n}\n\n# ============================================================\n# CRM OBS_ONLY\n# ============================================================\n\n# Object K=10 norm02\ncrm_obj_k10 = {\n    42: 0.22, 43: 0.16, 44: 0.16, 45: 0.16, 46: 0.15, 47: 0.20, 48: 0.18,\n}\n\n# Spatial K=10 norm02\ncrm_spa_k10 = {44: 0.36, 45: 0.34, 47: 0.32}\n\n# Object K=5 norm02\ncrm_obj_k5 = {42: 0.14, 43: 0.19, 44: 0.17, 45: 0.15, 46: 0.16, 47: 0.13, 48: 0.18}\n\n# Spatial K=5 norm02\ncrm_spa_k5 = {42: 0.35, 43: 0.32, 44: 0.37, 45: 0.34}\n\ndef mean_std(vals):\n    m = np.mean(vals)\n    s = np.std(vals, ddof=1) if len(vals) > 1 else 0\n    return m, s\n\n# Compute stats\nobj_srs = [v['sr'] for v in object_seeds.values()]\nspa_srs = [v['sr'] for v in spatial_seeds.values()]\ngoal_srs = [v['sr'] for v in goal_seeds.values()]\n\nobj_m, obj_s = mean_std(obj_srs)\nspa_m, spa_s = mean_std(spa_srs)\ngoal_m, goal_s = mean_std(goal_srs)\n\ncrm_obj_k10_m, crm_obj_k10_s = mean_std(list(crm_obj_k10.values()))\ncrm_spa_k10_m, crm_spa_k10_s = mean_std(list(crm_spa_k10.values()))\ncrm_obj_k5_m, crm_obj_k5_s = mean_std(list(crm_obj_k5.values()))\ncrm_spa_k5_m, crm_spa_k5_s = mean_std(list(crm_spa_k5.values()))\n\nprint(f\"Object: {obj_m:.3f} ± {obj_s:.3f} (n={len(obj_srs)})\")\nprint(f\"Spatial: {spa_m:.3f} ± {spa_s:.3f} (n={len(spa_srs)})\")\nprint(f\"Goal: {goal_m:.3f} ± {goal_s:.3f} (n={len(goal_srs)})\")\nprint()\nprint(f\"CRM obj K10 norm02: {crm_obj_k10_m:.3f} ± {crm_obj_k10_s:.3f} (n={len(crm_obj_k10)})\")\nprint(f\"CRM spa K10 norm02: {crm_spa_k10_m:.3f} ± {crm_spa_k10_s:.3f} (n={len(crm_spa_k10)})\")\nprint(f\"CRM obj K5 norm02: {crm_obj_k5_m:.3f} ± {crm_obj_k5_s:.3f} (n={len(crm_obj_k5)})\")\nprint(f\"CRM spa K5 norm02: {crm_spa_k5_m:.3f} ± {crm_spa_k5_s:.3f} (n={len(crm_spa_k5)})\")\nPYEOF\n",
  "description": "Compute summary statistics"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_vla-baseline-aggregation_20260519T182814",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 << 'PYEOF'\nimport numpy as np\n\n# ============================================================\n# VLA-ONLY BASELINES\n# ============================================================\n\n# --- LIBERO-Object ---\nobject_seeds = {\n    42: {'sr': 0.12, 'exp': 'eval-vla-only-object',\n         'per_task': {'alphabet_soup':0,'cream_cheese':0.1,'salad_dressing':0.2,'bbq_sauce':0.2,'ketchup':0,'tomato_sauce':0.1,'butter':0,'milk':0.1,'chocolate_pudding':0.2,'orange_juice':0.3}},\n    43: {'sr': 0.12, 'exp': 'eval-vla-only-object-seed43',\n         'per_task': {'alphabet_soup':0,'cream_cheese':0.1,'salad_dressing':0.1,'bbq_sauce':0.3,'ketchup':0,'tomato_sauce':0,'butter':0,'milk':0.1,'chocolate_pudding':0.4,'orange_juice':0.2}},\n    44: {'sr': 0.10, 'exp': 'eval-vla-only-object-seed44-r2',\n         'per_task': {'alphabet_soup':0,'cream_cheese':0.1,'salad_dressing':0.2,'bbq_sauce':0.2,'ketchup':0,'tomato_sauce':0,'butter':0,'milk':0.1,'chocolate_pudding':0.2,'orange_juice':0.2}},\n    45: {'sr': 0.11, 'exp': 'eval-vla-only-object-seed45-r2',\n         'per_task': {'alphabet_soup':0,'cream_cheese':0.3,'salad_dressing':0.2,'bbq_sauce':0.2,'ketchup':0,'tomato_sauce':0.1,'butter':0,'milk':0,'chocolate_pudding':0.1,'orange_juice':0.2}},\n    46: {'sr': 0.13, 'exp': 'eval-vla-only-object-seed46',\n         'per_task': None},\n}\n\n# --- LIBERO-Spatial ---\nspatial_seeds = {\n    42: {'sr': 0.30, 'exp': 'eval-vla-only-spatial-seed42',\n         'per_task': {'between_plate_and_ramekin':0.6,'next_to_ramekin':1.0,'from_table_center':0,'on_cookie_box':0.2,'in_top_drawer':0,'on_ramekin':0,'next_to_cookie_box':0.9,'on_stove':0,'next_to_plate':0.3,'on_wooden_cabinet':0}},\n    43: {'sr': 0.29, 'exp': 'eval-vla-only-spatial-seed43',\n         'per_task': {'between_plate_and_ramekin':0.7,'next_to_ramekin':0.8,'from_table_center':0.1,'on_cookie_box':0.3,'in_top_drawer':0,'on_ramekin':0,'next_to_cookie_box':0.9,'on_stove':0,'next_to_plate':0.1,'on_wooden_cabinet':0}},\n    44: {'sr': 0.31, 'exp': 'eval-vla-only-spatial-seed44',\n         'per_task': {'between_plate_and_ramekin':0.6,'next_to_ramekin':1.0,'from_table_center':0,'on_cookie_box':0.3,'in_top_drawer':0,'on_ramekin':0,'next_to_cookie_box':0.9,'on_stove':0,'next_to_plate':0.3,'on_wooden_cabinet':0}},\n    45: {'sr': 0.27, 'exp': 'eval-vla-only-spatial-seed45',\n         'per_task': {'between_plate_and_ramekin':0.7,'next_to_ramekin':0.9,'from_table_center':0,'on_cookie_box':0.2,'in_top_drawer':0,'on_ramekin':0,'next_to_cookie_box':0.9,'on_stove':0,'next_to_plate':0,'on_wooden_cabinet':0}},\n}\n\n# --- LIBERO-Goal ---\ngoal_seeds = {\n    42: {'sr': 0.71, 'exp': 'eval-vla-only-goal-seed42',\n         'per_task': {'open_middle_drawer':0.9,'bowl_on_stove':0.9,'wine_on_cabinet':0.6,'drawer_bowl_inside':0.4,'bowl_on_cabinet':0.7,'plate_front_stove':0.9,'cream_cheese_in_bowl':0.2,'turn_on_stove':0.9,'bowl_on_plate':0.9,'wine_on_rack':0.7}},\n    43: {'sr': 0.69, 'exp': 'eval-vla-only-goal-seed43',\n         'per_task': {'open_middle_drawer':0.9,'bowl_on_stove':0.9,'wine_on_cabinet':0.4,'drawer_bowl_inside':0.5,'bowl_on_cabinet':0.5,'plate_front_stove':0.8,'cream_cheese_in_bowl':0.4,'turn_on_stove':0.9,'bowl_on_plate':1.0,'wine_on_rack':0.6}},\n    44: {'sr': 0.73, 'exp': 'eval-vla-only-goal-seed44-r2',\n         'per_task': {'open_middle_drawer':0.8,'bowl_on_stove':0.9,'wine_on_cabinet':0.4,'drawer_bowl_inside':0.6,'bowl_on_cabinet':0.7,'plate_front_stove':0.9,'cream_cheese_in_bowl':0.3,'turn_on_stove':0.9,'bowl_on_plate':1.0,'wine_on_rack':0.8}},\n}\n\n# --- LIBERO-Long ---\n# All 5 seeds (42-46) are RUNNING, no results yet\n\n# --- LTO Split-A ---\nlto_seeds = {\n    'r2': {'sr': 0.14, 'exp': 'eval-lto-splitA-vla-only-r2'},\n    'r3': {'sr': 0.14, 'exp': 'eval-lto-splitA-vla-only-r3'},\n    'v2': {'sr': 0.14, 'exp': 'eval-lto-splitA-vla-only-v2'},\n}\n\n# ============================================================\n# CRM OBS_ONLY\n# ============================================================\n\n# Object K=10 norm02\ncrm_obj_k10 = {\n    42: 0.22, 43: 0.16, 44: 0.16, 45: 0.16, 46: 0.15, 47: 0.20, 48: 0.18,\n}\n\n# Spatial K=10 norm02\ncrm_spa_k10 = {44: 0.36, 45: 0.34, 47: 0.32}\n\n# Object K=5 norm02\ncrm_obj_k5 = {42: 0.14, 43: 0.19, 44: 0.17, 45: 0.15, 46: 0.16, 47: 0.13, 48: 0.18}\n\n# Spatial K=5 norm02\ncrm_spa_k5 = {42: 0.35, 43: 0.32, 44: 0.37, 45: 0.34}\n\ndef mean_std(vals):\n    m = np.mean(vals)\n    s = np.std(vals, ddof=1) if len(vals) > 1 else 0\n    return m, s\n\n# Compute stats\nobj_srs = [v['sr'] for v in object_seeds.values()]\nspa_srs = [v['sr'] for v in spatial_seeds.values()]\ngoal_srs = [v['sr'] for v in goal_seeds.values()]\n\nobj_m, obj_s = mean_std(obj_srs)\nspa_m, spa_s = mean_std(spa_srs)\ngoal_m, goal_s = mean_std(goal_srs)\n\ncrm_obj_k10_m, crm_obj_k10_s = mean_std(list(crm_obj_k10.values()))\ncrm_spa_k10_m, crm_spa_k10_s = mean_std(list(crm_spa_k10.values()))\ncrm_obj_k5_m, crm_obj_k5_s = mean_std(list(crm_obj_k5.values()))\ncrm_spa_k5_m, crm_spa_k5_s = mean_std(list(crm_spa_k5.values()))\n\nprint(f\"Object: {obj_m:.3f} ± {obj_s:.3f} (n={len(obj_srs)})\")\nprint(f\"Spatial: {spa_m:.3f} ± {spa_s:.3f} (n={len(spa_srs)})\")\nprint(f\"Goal: {goal_m:.3f} ± {goal_s:.3f} (n={len(goal_srs)})\")\nprint()\nprint(f\"CRM obj K10 norm02: {crm_obj_k10_m:.3f} ± {crm_obj_k10_s:.3f} (n={len(crm_obj_k10)})\")\nprint(f\"CRM spa K10 norm02: {crm_spa_k10_m:.3f} ± {crm_spa_k10_s:.3f} (n={len(crm_spa_k10)})\")\nprint(f\"CRM obj K5 norm02: {crm_obj_k5_m:.3f} ± {crm_obj_k5_s:.3f} (n={len(crm_obj_k5)})\")\nprint(f\"CRM spa K5 norm02: {crm_spa_k5_m:.3f} ± {crm_spa_k5_s:.3f} (n={len(crm_spa_k5)})\")\nPYEOF\n",
    "description": "Compute summary statistics"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-19T18:34:06.656998+00:00_

Object: 0.116 ± 0.011 (n=5)
Spatial: 0.292 ± 0.017 (n=4)
Goal: 0.710 ± 0.020 (n=3)

CRM obj K10 norm02: 0.176 ± 0.026 (n=7)
CRM spa K10 norm02: 0.340 ± 0.020 (n=3)
CRM obj K5 norm02: 0.160 ± 0.022 (n=7)
CRM spa K5 norm02: 0.345 ± 0.021 (n=4)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_vla-baseline-aggregation_20260519T182814",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-19T18:34:06.657210+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/",
  "description": "List artifacts directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_vla-baseline-aggregation_20260519T182814",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/",
    "description": "List artifacts directory"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-19T18:34:06.657475+00:00_

__pycache__
_project
ablation_eval_commands.md
adaptive_k_design.md
analysis
analysis_magnitude_sweep.py
analysis_object_benchmark.py
analysis_spatial_final.py
argmin_seed44_r2_results.json
batched_inference_feasibility_report.md
benchmark_survey.md
citation_attribution_audit.md
citation_audit_report.md
competitive_analysis_20260515.md
competitor_analysis.md
conclusion_draft.md
contribution_list.md
corl_paper_outline.md
correction_degradation_literature.md
crm-train-v2-k5
crm_bug_audit.md
crm_k1_model.py
diag-eval-v6-batch-failure.md
diag_bjb1_18228.md
diag_bjb2_28827.md
diagnose-norm02-seed44-r2.md
diagnose-random-selection-seed46-r2.md
diagnose_default_seed46.md
diagnose_spatial_k5_seed44_r2.md
diagnosis-eval-obs-only-object-norm003-seed43.md
diagnosis_random_k5_seed44_r2.md
dream_reports
eval-acr-object-v4-obs-only
eval-acr-object-v4-scalar
eval-argmin-object-seed44-r2
eval-mag-perdof-norm03
eval-obs-only-object-default-seed45
eval-obs-only-object-norm01-seed45-r2
eval-obs-only-object-norm02-seed44-r2
eval-obs-only-object-norm02-seed46
eval-obs-only-object-norm03-seed44
eval-openvla-object-vla-only-seed42
eval-openvla-object-vla-only-seed42-v2
eval-random-selection-object-k5-seed44-r2
eval-reconvla-spatial-v1-diag.md
eval-vla-mean-object-seed44
experiment_progress_20260515.md
experiments_draft.md
fallback_narrative_draft.md
fig_magnitude_curve.py
figures
fisher_analysis.py
fix_plan_code_sketch.md
gpu_health_snapshot_20260515.md
introduction_draft.md
k_value_curve_data.json
latency_breakdown.json
lerobot-pipeline-alignment.md
libero-smolvla-env-report.md
literature_gap_report.md
magnitude_curve.pdf
magnitude_curve.png
magnitude_curve_data.json
magnitude_curve_data.md
magnitude_curve_draft.pdf
magnitude_curve_draft.png
magnitude_multiseed_data.md
magnitude_sweep_summary.md
manifest.yaml
method_draft.md
method_section_draft.tex
mvp-point-reaching
n_rollouts_audit_report.md
narrative_b_abstract_draft.md
narrative_b_abstract_final.md
narrative_b_draft.md
next_batch_pl
…[truncated 830 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_vla-baseline-aggregation_20260519T182814",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-19T18:34:06.657758+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/vla_baseline_summary.md",
  "content": "# VLA-Only Baseline & CRM obs_only Summary\n\nGenerated: 2026-05-19\n\n## 1. VLA-Only Baselines (SmolVLA, K=1, no CRM)\n\n### LIBERO-Object\n\n| Seed | Overall SR | exp_id |\n|------|-----------|--------|\n| 42 | 0.12 | eval-vla-only-object |\n| 43 | 0.12 | eval-vla-only-object-seed43 |\n| 44 | 0.10 | eval-vla-only-object-seed44-r2 |\n| 45 | 0.11 | eval-vla-only-object-seed45-r2 |\n| 46 | 0.13 | eval-vla-only-object-seed46 |\n| **Mean ± Std** | **0.116 ± 0.011** | **n=5** |\n\nPer-task breakdown (seeds with data):\n\n| Task | s42 | s43 | s44 | s45 |\n|------|-----|-----|-----|-----|\n| alphabet_soup | 0.0 | 0.0 | 0.0 | 0.0 |\n| cream_cheese | 0.1 | 0.1 | 0.1 | 0.3 |\n| salad_dressing | 0.2 | 0.1 | 0.2 | 0.2 |\n| bbq_sauce | 0.2 | 0.3 | 0.2 | 0.2 |\n| ketchup | 0.0 | 0.0 | 0.0 | 0.0 |\n| tomato_sauce | 0.1 | 0.0 | 0.0 | 0.1 |\n| butter | 0.0 | 0.0 | 0.0 | 0.0 |\n| milk | 0.1 | 0.1 | 0.1 | 0.0 |\n| chocolate_pudding | 0.2 | 0.4 | 0.2 | 0.1 |\n| orange_juice | 0.3 | 0.2 | 0.2 | 0.2 |\n\n### LIBERO-Spatial\n\n| Seed | Overall SR | exp_id |\n|------|-----------|--------|\n| 42 | 0.30 | eval-vla-only-spatial-seed42 |\n| 43 | 0.29 | eval-vla-only-spatial-seed43 |\n| 44 | 0.31 | eval-vla-only-spatial-seed44 |\n| 45 | 0.27 | eval-vla-only-spatial-seed45 |\n| **Mean ± Std** | **0.292 ± 0.017** | **n=4** |\n\nPer-task breakdown:\n\n| Task | s42 | s43 | s44 | s45 |\n|------|-----|-----|-----|-----|\n| between_plate_and_ramekin | 0.6 | 0.7 | 0.6 | 0.7 |\n| next_to_ramekin | 1.0 | 0.8 | 1.0 | 0.9 |\n| from_table_center | 0.0 | 0.1 | 0.0 | 0.0 |\n| on_cookie_box | 0.2 | 0.3 | 0.3 | 0.2 |\n| in_top_drawer | 0.0 | 0.0 | 0.0 | 0.0 |\n| on_ramekin | 0.0 | 0.0 | 0.0 | 0.0 |\n| next_to_cookie_box | 0.9 | 0.9 | 0.9 | 0.9 |\n| on_stove | 0.0 | 0.0 | 0.0 | 0.0 |\n| next_to_plate | 0.3 | 0.1 | 0.3 | 0.0 |\n| on_wooden_cabinet | 0.0 | 0.0 | 0.0 | 0.0 |\n\n### LIBERO-Goal\n\n| Seed | Overall SR | exp_id |\n|------|-----------|--------|\n| 42 | 0.71 | eval-vla-only-goal-seed42 |\n| 43 | 0.69 | eval-vla-only-goal-seed43 |\n| 44 | 0.73 | eval-vla-only-goal-seed44-r2 |\n| **Mean ± Std** | **0.710 ± 0.020** | **n=3** |\n\nPer-task breakdown:\n\n| Task | s42 | s43 | s44 |\n|------|-----|-----|-----|\n| open_middle_drawer | 0.9 | 0.9 | 0.8 |\n| bowl_on_stove | 0.9 | 0.9 | 0.9 |\n| wine_on_cabinet | 0.6 | 0.4 | 0.4 |\n| drawer_bowl_inside | 0.4 | 0.5 | 0.6 |\n| bowl_on_cabinet | 0.7 | 0.5 | 0.7 |\n| plate_front_stove | 0.9 | 0.8 | 0.9 |\n| cream_cheese_in_bowl | 0.2 | 0.4 | 0.3 |\n| turn_on_stove | 0.9 | 0.9 | 0.9 |\n| bowl_on_plate | 0.9 | 1.0 | 1.0 |\n| wine_on_rack | 0.7 | 0.6 | 0.8 |\n\n### LIBERO-Long\n\nAll 5 seeds (42-46) currently **RUNNING** — no results yet.\n\n### LTO Split-A (5 held-out tasks, not LIBERO-Long)\n\n| Run | SR | exp_id |\n|-----|-----|--------|\n| r2 | 0.14 | eval-lto-splitA-vla-only-r2 |\n| r3 | 0.14 | eval-lto-splitA-vla-only-r3 |\n| v2 | 0.14 | eval-lto-splitA-vla-only-v2 |\n\nTasks: ketchup, milk, orange_juice, salad_dressing, tomato_sauce (5 tasks × 10 rollouts = 50 total, 7 successes)\n\n### OpenVLA 7B Baseline (different model)\n\n| Seed | Suite | SR | exp_id |\n|------|-------|-----|--------|\n| 42 | Object | 0.69 | eval-openvla-object-vla-only-seed42-v2 |\n\n---\n\n## 2. CRM obs_only Comparisons (norm=0.2)\n\n### Object K=10\n\n| Seed | SR | exp_id |\n|------|-----|--------|\n| 42 | 0.22 | eval-acr-object-obs-only-norm02 |\n| 43 | 0.16 | eval-obs-only-object-norm02-seed43-r2 |\n| 44 | 0.16 | eval-obs-only-object-norm02-seed44-r2 |\n| 45 | 0.16 | eval-obs-only-object-norm02-seed45 |\n| 46 | 0.15 | eval-obs-only-object-norm02-seed46 |\n| 47 | 0.20 | eval-obs-only-object-norm02-seed47 |\n| 48 | 0.18 | eval-obs-only-object-norm02-seed48-r2 |\n| **Mean ± Std** | **0.176 ± 0.026** | **n=7** |\n\n### Spatial K=10\n\n| Seed | SR | exp_id |\n|------|-----|--------|\n| 44 | 0.36 | eval-obs-only-spatial-norm02-seed44 |\n| 45 | 0.34 | eval-obs-only-spatial-norm02-seed45 |\n| 47 | 0.32 | eval-obs-only-spatial-norm02-seed47 |\n| **Mean ± Std** | **0.340 ± 0.020** | **n=3** |\n\n### Object K=5\n\n| Seed | SR | exp_id |\n|------|-----|--------|\n| 42 | 0.14 | eval-obs-only-object-norm02-k5-seed42 |\n| 43 | 0.19 | eval-obs-only-object-norm02-k5-seed43 |\n| 44 | 0.17 | eval-obs-only-object-norm02-k5-seed44 |\n| 45 | 0.15 | eval-obs-only-object-norm02-k5-seed45 |\n| 46 | 0.16 | eval-obs-only-object-norm02-k5-seed46 |\n| 47 | 0.13 | eval-obs-only-object-norm02-k5-seed47 |\n| 48 | 0.18 | eval-obs-only-object-norm02-k5-seed48 |\n| **Mean ± Std** | **0.160 ± 0.022** | **n=7** |\n\n### Spatial K=5\n\n| Seed | SR | exp_id |\n|------|-----|--------|\n| 42 | 0.35 | eval-obs-only-spatial-norm02-k5-seed42 |\n| 43 | 0.32 | eval-obs-only-spatial-norm02-k5-seed43 |\n| 44 | 0.37 | eval-obs-only-spatial-norm02-k5-seed44-r2 |\n| 45 | 0.34 | eval-obs-only-spatial-norm02-k5-seed45-r2 |\n| **Mean ± Std** | **0.345 ± 0.021** | **n=4** |\n\n---\n\n## 3. Comparison Summary\n\n| Suite | VLA-only | CRM obs_only K=10 | CRM obs_only K=5 | Δ(K=10) | Δ(K=5) |\n|-------|----------|-------------------|-------------------|---------|--------|\n| Object | 0.116 ± 0.011 (n=5) | 0.176 ± 0.026 (n=7) | 0.160 ± 0.022 (n=7) | +6.0pp | +4.4pp |\n| Spatial | 0.292 ± 0.017 (n=4) | 0.340 ± 0.020 (n=3) | 0.345 ± 0.021 (n=4) | +4.8pp | +5.3pp |\n| Goal | 0.710 ± 0.020 (n=3) | — | — | — | — |\n| Long | RUNNING | — | — | — | — |\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_vla-baseline-aggregation_20260519T182814",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/vla_baseline_summary.md",
    "content": "# VLA-Only Baseline & CRM obs_only Summary\n\nGenerated: 2026-05-19\n\n## 1. VLA-Only Baselines (SmolVLA, K=1, no CRM)\n\n### LIBERO-Object\n\n| Seed | Overall SR | exp_id |\n|------|-----------|--------|\n| 42 | 0.12 | eval-vla-only-object |\n| 43 | 0.12 | eval-vla-only-object-seed43 |\n| 44 | 0.10 | eval-vla-only-object-seed44-r2 |\n| 45 | 0.11 | eval-vla-only-object-seed45-r2 |\n| 46 | 0.13 | eval-vla-only-object-seed46 |\n| **Mean ± Std** | **0.116 ± 0.011** | **n=5** |\n\nPer-task breakdown (seeds with data):\n\n| Task | s42 | s43 | s44 | s45 |\n|------|-----|-----|-----|-----|\n| alphabet_soup | 0.0 | 0.0 | 0.0 | 0.0 |\n| cream_cheese | 0.1 | 0.1 | 0.1 | 0.3 |\n| salad_dressing | 0.2 | 0.1 | 0.2 | 0.2 |\n| bbq_sauce | 0.2 | 0.3 | 0.2 | 0.2 |\n| ketchup | 0.0 | 0.0 | 0.0 | 0.0 |\n| tomato_sauce | 0.1 | 0.0 | 0.0 | 0.1 |\n| butter | 0.0 | 0.0 | 0.0 | 0.0 |\n| milk | 0.1 | 0.1 | 0.1 | 0.0 |\n| chocolate_pudding | 0.2 | 0.4 | 0.2 | 0.1 |\n| orange_juice | 0.3 | 0.2 | 0.2 | 0.2 |\n\n### LIBERO-Spatial\n\n| Seed | Overall SR | exp_id |\n|------|-----------|--------|\n| 42 | 0.30 | eval-vla-only-spatial-seed42 |\n| 43 | 0.29 | eval-vla-only-spatial-seed43 |\n| 44 | 0.31 | eval-vla-only-spatial-seed44 |\n| 45 | 0.27 | eval-vla-only-spatial-seed45 |\n| **Mean ± Std** | **0.292 ± 0.017** | **n=4** |\n\nPer-task breakdown:\n\n| Task | s42 | s43 | s44 | s45 |\n|------|-----|-----|-----|-----|\n| between_plate_and_ramekin | 0.6 | 0.7 | 0.6 | 0.7 |\n| next_to_ramekin | 1.0 | 0.8 | 1.0 | 0.9 |\n| from_table_center | 0.0 | 0.1 | 0.0 | 0.0 |\n| on_cookie_box | 0.2 | 0.3 | 0.3 | 0.2 |\n| in_top_drawer | 0.0 | 0.0 | 0.0 | 0.0 |\n| on_ramekin | 0.0 | 0.0 | 0.0 | 0.0 |\n| next_to_cookie_box | 0.9 | 0.9 | 0.9 | 0.9 |\n| on_stove | 0.0 | 0.0 | 0.0 | 0.0 |\n| next_to_plate | 0.3 | 0.1 | 0.3 | 0.0 |\n| on_wooden_cabinet | 0.0 | 0.0 | 0.0 | 0.0 |\n\n### LIBERO-Goal\n\n| Seed | Overall SR | exp_id |\n|------|-----------|--------|\n| 42 | 0.71 | eval-vla-only-goal-seed42 |\n| 43 | 0.69 | eval-vla-only-goal-seed43 |\n| 44 | 0.73 | eval-vla-only-goal-seed44-r2 |\n| **Mean ± Std** | **0.710 ± 0.020** | **n=3** |\n\nPer-task breakdown:\n\n| Task | s42 | s43 | s44 |\n|------|-----|-----|-----|\n| open_middle_drawer | 0.9 | 0.9 | 0.8 |\n| bowl_on_stove | 0.9 | 0.9 | 0.9 |\n| wine_on_cabinet | 0.6 | 0.4 | 0.4 |\n| drawer_bowl_inside | 0.4 | 0.5 | 0.6 |\n| bowl_on_cabinet | 0.7 | 0.5 | 0.7 |\n| plate_front_stove | 0.9 | 0.8 | 0.9 |\n| cream_cheese_in_bowl | 0.2 | 0.4 | 0.3 |\n| turn_on_stove | 0.9 | 0.9 | 0.9 |\n| bowl_on_plate | 0.9 | 1.0 | 1.0 |\n| wine_on_rack | 0.7 | 0.6 | 0.8 |\n\n### LIBERO-Long\n\nAll 5 seeds (42-46) currently **RUNNING** — no results yet.\n\n### LTO Split-A (5 held-out tasks, not LIBERO-Long)\n\n| Run | SR | exp_id |\n|-----|-----|--------|\n| r2 | 0.14 | eval-lto-splitA-vla-only-r2 |\n| r3 | 0.14 | eval-lto-splitA-vla-only-r3 |\n| v2 | 0.14 | eval-lto-splitA-vla-only-v2 |\n\nTasks: ketchup, milk, orange_juice, salad_dressing, tomato_sauce (5 tasks × 10 rollouts = 50 total, 7 successes)\n\n### OpenVLA 7B Baseline (different model)\n\n| Seed | Suite | SR | exp_id |\n|------|-------|-----|--------|\n| 42 | Object | 0.69 | eval-openvla-object-vla-only-seed42-v2 |\n\n---\n\n## 2. CRM obs_only Comparisons (norm=0.2)\n\n### Object K=10\n\n| Seed | SR | exp_id |\n|------|-----|--------|\n| 42 | 0.22 | eval-acr-object-obs-only-norm02 |\n| 43 | 0.16 | eval-obs-only-object-norm02-seed43-r2 |\n| 44 | 0.16 | eval-obs-only-object-norm02-seed44-r2 |\n| 45 | 0.16 | eval-obs-only-object-norm02-seed45 |\n| 46 | 0.15 | eval-obs-only-object-norm02-seed46 |\n| 47 | 0.20 | eval-obs-only-object-norm02-seed47 |\n| 48 | 0.18 | eval-obs-only-object-norm02-seed48-r2 |\n| **Mean ± Std** | **0.176 ± 0.026** | **n=7** |\n\n### Spatial K=10\n\n| Seed | SR | exp_id |\n|------|-----|--------|\n| 44 | 0.36 | eval-obs-only-spatial-norm02-seed44 |\n| 45 | 0.34 | eval-obs-only-spatial-norm02-seed45 |\n| 47 | 0.32 | eval-obs-only-spatial-norm02-seed47 |\n| **Mean ± Std** | **0.340 ± 0.020** | **n=3** |\n\n### Object K=5\n\n| Seed | SR | exp_id |\n|------|-----|--------|\n| 42 | 0.14 | eval-obs-only-object-norm02-k5-seed42 |\n| 43 | 0.19 | eval-obs-only-object-norm02-k5-seed43 |\n| 44 | 0.17 | eval-obs-only-object-norm02-k5-seed44 |\n| 45 | 0.15 | eval-obs-only-object-norm02-k5-seed45 |\n| 46 | 0.16 | eval-obs-only-object-norm02-k5-seed46 |\n| 47 | 0.13 | eval-obs-only-object-norm02-k5-seed47 |\n| 48 | 0.18 | eval-obs-only-object-norm02-k5-seed48 |\n| **Mean ± Std** | **0.160 ± 0.022** | **n=7** |\n\n### Spatial K=5\n\n| Seed | SR | exp_id |\n|------|-----|--------|\n| 42 | 0.35 | eval-obs-only-spatial-norm02-k5-seed42 |\n| 43 | 0.32 | eval-obs-only-spatial-norm02-k5-seed43 |\n| 44 | 0.37 | eval-obs-only-spatial-norm02-k5-seed44-r2 |\n| 45 | 0.34 | eval-obs-only-spatial-norm02-k5-seed45-r2 |\n| **Mean ± Std** | **0.345 ± 0.021** | **n=4** |\n\n---\n\n## 3. Comparison Summary\n\n| Suite | VLA-only | CRM obs_only K=10 | CRM obs_only K=5 | Δ(K=10) | Δ(K=5) |\n|-------|----------|-------------------|-------------------|---------|--------|\n| Object | 0.116 ± 0.011 (n=5) | 0.176 ± 0.026 (n=7) | 0.160 ± 0.022 (n=7) | +6.0pp | +4.4pp |\n| Spatial | 0.292 ± 0.017 (n=4) | 0.340 ± 0.020 (n=3) | 0.345 ± 0.021 (n=4) | +4.8pp | +5.3pp |\n| Goal | 0.710 ± 0.020 (n=3) | — | — | — | — |\n| Long | RUNNING | — | — | — | — |\n"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-19T18:34:06.658092+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/vla_baseline_summary.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_vla-baseline-aggregation_20260519T182814",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-19T18:34:06.658316+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "vla_baseline_summary",
  "type": "report",
  "description": "VLA-only baseline and CRM obs_only summary across LIBERO suites (Object/Spatial/Goal/Long), with per-seed SR, mean±std, per-task breakdown, and K=10/K=5 comparisons",
  "project": "acr-vla-conformal-refinement",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/vla_baseline_summary.md",
  "tags": "['baseline', 'vla-only', 'obs_only', 'summary', 'libero']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_vla-baseline-aggregation_20260519T182814",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "vla_baseline_summary",
    "type": "report",
    "description": "VLA-only baseline and CRM obs_only summary across LIBERO suites (Object/Spatial/Goal/Long), with per-seed SR, mean±std, per-task breakdown, and K=10/K=5 comparisons",
    "project": "acr-vla-conformal-refinement",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/vla_baseline_summary.md",
    "tags": "['baseline', 'vla-only', 'obs_only', 'summary', 'libero']"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-19T18:34:06.658562+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260519_311a6c\", \"name\": \"vla_baseline_summary\", \"type\": \"report\", \"description\": \"VLA-only baseline and CRM obs_only summary across LIBERO suites (Object/Spatial/Goal/Long), with per-seed SR, mean±std, per-task breakdown, and K=10/K=5 comparisons\", \"path\": \"projects/acr-vla-conformal-refinement/artifacts/_project/report/vla_baseline_summary.md\", \"url\": null, \"project\": \"acr-vla-conformal-refinement\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-19T18:33:59.987311+00:00\", \"tags\": [\"baseline\", \"vla-only\", \"obs_only\", \"summary\", \"libero\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_vla-baseline-aggregation_20260519T182814",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 49 · 2026-05-19T18:34:06.658844+00:00_

已完成。汇总结果：

| Suite | VLA-only (SmolVLA) | CRM obs_only K=10 | CRM obs_only K=5 |
|-------|-------------------|-------------------|-------------------|
| **Object** | 11.6% ± 1.1% (n=5) | 17.6% ± 2.6% (n=7) | 16.0% ± 2.2% (n=7) |
| **Spatial** | 29.2% ± 1.7% (n=4) | 34.0% ± 2.0% (n=3) | 34.5% ± 2.1% (n=4) |
| **Goal** | 71.0% ± 2.0% (n=3) | — | — |
| **Long** | RUNNING (5 seeds) | — | — |

文件已保存至 `artifacts/vla_baseline_summary.md` 并注册（`art_20260519_311a6c`）。含 per-task breakdown 和 per-seed 明细。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_vla-baseline-aggregation_20260519T182814"
}
```

</details>

---
