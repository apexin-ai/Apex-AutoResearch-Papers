# audit canonical data protocol

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 98
- **Recorded user turns:** 0
- **Tool calls:** 48
- **Original source:** `logs/chats/worker_audit_canonical-data-protocol_20260524T224440.jsonl`
- **Structured JSON:** [`ec8e009968512b7a32dd.json`](../../sessions/ec/ec8e009968512b7a32dd.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

98 recorded events

### Assistant

_source line 1 · 2026-05-24T22:44:49.953145+00:00_

Not logged in · Please run /login

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_audit_canonical-data-protocol_20260524T224440"
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-24T22:54:53.165577+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,TodoWrite",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_canonical-data-protocol_20260524T224440",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,TodoWrite",
    "max_results": "10"
  }
}
```

</details>

---

### Tool result

_source line 3 · 2026-05-24T22:54:53.165886+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_canonical-data-protocol_20260524T224440",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-24T22:54:53.166052+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Read registry for all spatial experiments', 'activeForm': 'Reading registry for spatial experiments', 'status': 'in_progress'}, {'content': 'SSH each server to verify result files', 'activeForm': 'SSH each server to verify result files', 'status': 'pending'}, {'content': 'Build audit matrix and canonical pairs', 'activeForm': 'Building audit matrix and canonical pairs', 'status': 'pending'}, {'content': 'Compute final p-values from canonical pairs', 'activeForm': 'Computing final p-values from canonical pairs', 'status': 'pending'}, {'content': 'Report audit matrix + yaml + p-values + gaps', 'activeForm': 'Reporting audit matrix + yaml + p-values + gaps', 'status': 'pending'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_canonical-data-protocol_20260524T224440",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Read registry for all spatial experiments', 'activeForm': 'Reading registry for spatial experiments', 'status': 'in_progress'}, {'content': 'SSH each server to verify result files', 'activeForm': 'SSH each server to verify result files', 'status': 'pending'}, {'content': 'Build audit matrix and canonical pairs', 'activeForm': 'Building audit matrix and canonical pairs', 'status': 'pending'}, {'content': 'Compute final p-values from canonical pairs', 'activeForm': 'Computing final p-values from canonical pairs', 'status': 'pending'}, {'content': 'Report audit matrix + yaml + p-values + gaps', 'activeForm': 'Reporting audit matrix + yaml + p-values + gaps', 'status': 'pending'}]"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-24T22:54:53.166206+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_canonical-data-protocol_20260524T224440",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-24T22:54:53.166390+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "fields": "['*']",
  "limit": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_canonical-data-protocol_20260524T224440",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "fields": "['*']",
    "limit": "0"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-24T22:54:53.166978+00:00_

Error: result (118,819 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/b8bff12d-79aa-4770-9cbd-73119cfe4314/tool-results/mcp-agent-ml-research-read_registry-1779662712168.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/b8bff12d-79aa-4770-9cbd-73119cfe4314/tool-results/mcp-agent-ml-research-read_registry-1779662712168.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_canonical-data-protocol_20260524T224440",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-24T22:54:53.167153+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "wc -l /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/b8bff12d-79aa-4770-9cbd-73119cfe4314/tool-results/mcp-agent-ml-research-read_registry-1779662712168.txt",
  "description": "Count lines in registry file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_canonical-data-protocol_20260524T224440",
  "tool": "Bash",
  "tool_args": {
    "command": "wc -l /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/b8bff12d-79aa-4770-9cbd-73119cfe4314/tool-results/mcp-agent-ml-research-read_registry-1779662712168.txt",
    "description": "Count lines in registry file"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-24T22:54:53.167340+00:00_

0 /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/b8bff12d-79aa-4770-9cbd-73119cfe4314/tool-results/mcp-agent-ml-research-read_registry-1779662712168.txt

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_canonical-data-protocol_20260524T224440",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-24T22:54:53.167490+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/b8bff12d-79aa-4770-9cbd-73119cfe4314/tool-results/ && python3 -c \"\nimport json\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/b8bff12d-79aa-4770-9cbd-73119cfe4314/tool-results/mcp-agent-ml-research-read_registry-1779662712168.txt') as f:\n    data = json.load(f)\nprint(type(data), list(data.keys()) if hasattr(data,'keys') else len(data))\nprint('Total chars in result:', len(data['result']))\n\"",
  "description": "Inspect registry file structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_canonical-data-protocol_20260524T224440",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/b8bff12d-79aa-4770-9cbd-73119cfe4314/tool-results/ && python3 -c \"\nimport json\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/b8bff12d-79aa-4770-9cbd-73119cfe4314/tool-results/mcp-agent-ml-research-read_registry-1779662712168.txt') as f:\n    data = json.load(f)\nprint(type(data), list(data.keys()) if hasattr(data,'keys') else len(data))\nprint('Total chars in result:', len(data['result']))\n\"",
    "description": "Inspect registry file structure"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-24T22:54:53.167629+00:00_

total 128
drwxr-xr-x 2 ubuntu ubuntu   4096 May 24 22:45 .
drwxr-xr-x 3 ubuntu ubuntu   4096 May 24 22:45 ..
-rw-r--r-- 1 ubuntu ubuntu 119298 May 24 22:45 mcp-agent-ml-research-read_registry-1779662712168.txt
&lt;class 'dict'> ['result']
Total chars in result: 110382

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_canonical-data-protocol_20260524T224440",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-24T22:54:53.167753+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 << 'EOF'\nimport json, re\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/b8bff12d-79aa-4770-9cbd-73119cfe4314/tool-results/mcp-agent-ml-research-read_registry-1779662712168.txt') as f:\n    data = json.load(f)\nresult_str = data['result']\nprint(\"First 500 chars:\", result_str[:500])\nprint(\"---\")\nprint(\"Last 500 chars:\", result_str[-500:])\nEOF",
  "description": "Inspect registry result format"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_canonical-data-protocol_20260524T224440",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 << 'EOF'\nimport json, re\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/b8bff12d-79aa-4770-9cbd-73119cfe4314/tool-results/mcp-agent-ml-research-read_registry-1779662712168.txt') as f:\n    data = json.load(f)\nresult_str = data['result']\nprint(\"First 500 chars:\", result_str[:500])\nprint(\"---\")\nprint(\"Last 500 chars:\", result_str[-500:])\nEOF",
    "description": "Inspect registry result format"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-24T22:54:53.167890+00:00_

First 500 chars: {"success": true, "data": {"experiments": {"eval-a1-baseline-object-s42": {"status": "DONE", "retry_count": 0, "created_at": "2026-05-24T13:36:46.351Z", "updated_at": "2026-05-24T20:11:08.467Z", "hypothesis": "A1 VLA baseline (8.8B params, official LIBERO scores: Object 99.8%) evaluated under our framework for cross-architecture comparison.", "spec": {"command": "CUDA_VISIBLE_DEVICES=0 python -u src/eval_a1_baseline.py --benchmark object --n_rollouts 20 --seed 42 --gpu 0 --tokenizer_path /root/a
---
Last 500 chars: 0, "salad_dressing": 0.3, "bbq_sauce": 0.3, "ketchup": 0, "tomato_sauce": 0.1, "butter": 0.2, "milk": 0.2, "chocolate_pudding": 0.5, "orange_juice": 0.3}}, "checkpoint_path": "/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt", "log_path": "/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm03.log", "conclusion": "success", "completed_at": "2026-05-16T07:41:53.597Z"}}, "count": 138, "total": 138, "baseline": null}, "error": null, "metadata": {"elapsed_seconds": 0.2397}}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_canonical-data-protocol_20260524T224440",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-24T22:54:53.168022+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 << 'EOF'\nimport json, re\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/b8bff12d-79aa-4770-9cbd-73119cfe4314/tool-results/mcp-agent-ml-research-read_registry-1779662712168.txt') as f:\n    data = json.load(f)\nparsed = json.loads(data['result'])\nexps = parsed['data']['experiments']\nprint(\"Total experiments:\", len(exps))\n\n# Filter spatial experiments\nspatial_exps = {k: v for k, v in exps.items() if 'spatial' in k.lower() or (v.get('spec', {}).get('command', '').find('--benchmark spatial') != -1)}\nprint(f\"Spatial-related experiments: {len(spatial_exps)}\")\nprint()\n# List spatial keys\nfor k in sorted(spatial_exps.keys()):\n    v = spatial_exps[k]\n    status = v.get('status', '?')\n    print(f\"  {k}  [{status}]\")\nEOF",
  "description": "List all spatial experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_canonical-data-protocol_20260524T224440",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 << 'EOF'\nimport json, re\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/b8bff12d-79aa-4770-9cbd-73119cfe4314/tool-results/mcp-agent-ml-research-read_registry-1779662712168.txt') as f:\n    data = json.load(f)\nparsed = json.loads(data['result'])\nexps = parsed['data']['experiments']\nprint(\"Total experiments:\", len(exps))\n\n# Filter spatial experiments\nspatial_exps = {k: v for k, v in exps.items() if 'spatial' in k.lower() or (v.get('spec', {}).get('command', '').find('--benchmark spatial') != -1)}\nprint(f\"Spatial-related experiments: {len(spatial_exps)}\")\nprint()\n# List spatial keys\nfor k in sorted(spatial_exps.keys()):\n    v = spatial_exps[k]\n    status = v.get('status', '?')\n    print(f\"  {k}  [{status}]\")\nEOF",
    "description": "List all spatial experiments"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-24T22:54:53.168168+00:00_

Total experiments: 138
Spatial-related experiments: 42

  eval-adaptive-k-spatial-p25-seed44  [DONE]
  eval-adaptive-k-spatial-p50-seed42  [DONE]
  eval-adaptive-k-spatial-p75-seed44  [DONE]
  eval-adaptive-k-spatial-p90-seed42  [DONE]
  eval-adaptive-k-spatial-p90-seed43  [DONE]
  eval-crm-spatial-k10-seed49  [DONE]
  eval-crm-spatial-k10-seed50  [DONE]
  eval-crm-spatial-seed47  [DONE]
  eval-crm-spatial-seed48  [DONE]
  eval-obs-only-spatial-norm02-seed44  [DONE]
  eval-obs-only-spatial-norm02-seed46-r2  [DONE]
  eval-obs-only-spatial-norm02-seed47  [DONE]
  eval-pi05-crm-spatial-seed42  [PREPARING]
  eval-pi05-crm-spatial-seed43  [PREPARING]
  eval-pi05-crm-spatial-seed44  [PREPARING]
  eval-pi05-vla-only-spatial-seed42-r4  [PREPARING]
  eval-pi05-vla-only-spatial-seed43-r4  [PREPARING]
  eval-pi05-vla-only-spatial-seed44-r4  [PREPARING]
  eval-random-selection-spatial-seed42  [DONE]
  eval-random-selection-spatial-seed43  [DONE]
  eval-random-selection-spatial-seed44  [DONE]
  eval-smolvla-lerobot-spatial-seed43-v3  [RUNNING]
  eval-supp-adapt-tau015-spatial-s42-r2  [DONE]
  eval-supp-adapt-tau025-spatial-s42-r2  [DONE]
  eval-supp-adapt-tau025-spatial-s46  [PREPARING]
  eval-supp-adapt-tau025-spatial-s47  [PREPARING]
  eval-supp-adapt-tau035-spatial-s42-r2  [DONE]
  eval-supp-crm-norm02-spatial-s42-r2  [DONE]
  eval-supp-spatial-adapt-tau025-s45-r3  [RUNNING]
  eval-supp-spatial-adapt-tau025-s47  [PREPARING]
  eval-supp-spatial-k2mean-s46  [RUNNING]
  eval-supp-spatial-k2mean-s47  [PREPARING]
  eval-supp-spatial-reconvla-s45  [DONE]
  eval-supp-spatial-reconvla-s46  [RUNNING]
  eval-supp-spatial-vla-only-s47  [PREPARING]
  eval-vla-only-spatial-seed45  [DONE]
  eval-vla-only-spatial-seed50  [DONE]
  eval-vla-only-spatial-seed51  [DONE]
  eval-vla-only-spatial-seed52  [DONE]
  eval-vla-only-spatial-seed53  [DONE]
  eval-vla-only-spatial-seed54  [DONE]
  precompute-pi05-spatial-2048-r2  [DONE]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_canonical-data-protocol_20260524T224440",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-24T22:54:53.168360+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 << 'EOF'\nimport json, re\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/b8bff12d-79aa-4770-9cbd-73119cfe4314/tool-results/mcp-agent-ml-research-read_registry-1779662712168.txt') as f:\n    data = json.load(f)\nparsed = json.loads(data['result'])\nexps = parsed['data']['experiments']\n\n# Filter spatial experiments via command field too\nspatial = {}\nfor k, v in exps.items():\n    cmd = v.get('spec', {}).get('command', '') or ''\n    if 'spatial' in k.lower() or '--benchmark spatial' in cmd or '/spatial' in cmd:\n        spatial[k] = v\n\nprint(f\"Total spatial-like: {len(spatial)}\")\n\n# For each, dump key fields\nfor k in sorted(spatial.keys()):\n    v = spatial[k]\n    status = v.get('status', '?')\n    if status != 'DONE':\n        continue\n    cmd = v.get('spec', {}).get('command', '')\n    server = v.get('spec', {}).get('server') or v.get('server') or v.get('spec',{}).get('host') or v.get('metadata',{}).get('server') or ''\n    # try to find seed\n    sm = re.search(r'--seed\\s+(\\d+)', cmd) or re.search(r'seed[\\-_](\\d+)', k)\n    seed = sm.group(1) if sm else '?'\n    # K\n    km = re.search(r'--k\\s+(\\d+)', cmd, re.IGNORECASE) or re.search(r'--K\\s+(\\d+)', cmd) or re.search(r'k(\\d+)[-_]', k)\n    K = km.group(1) if km else None\n    # mode hints\n    mode_hints = []\n    for tag in ['vla_only', 'vla-only', 'adaptive', 'crm', 'random-selection', 'random_selection', 'obs-only', 'reconvla', 'k2mean']:\n        if tag in k.lower() or tag in cmd.lower():\n            mode_hints.append(tag)\n    # results\n    metrics = v.get('metrics') or {}\n    sr = metrics.get('success_rate') or metrics.get('SR') or metrics.get('avg_success') or None\n    conc = v.get('conclusion', '')\n    created = v.get('created_at', '')\n    print(f\"{k}\\n  status={status} seed={seed} K={K} hints={mode_hints} SR={sr}\\n  server={server!r}\\n  created={created}\\n  cmd_snippet={cmd[:200]}\\n\")\nEOF",
  "description": "Extract spatial DONE experiments details"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_canonical-data-protocol_20260524T224440",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 << 'EOF'\nimport json, re\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/b8bff12d-79aa-4770-9cbd-73119cfe4314/tool-results/mcp-agent-ml-research-read_registry-1779662712168.txt') as f:\n    data = json.load(f)\nparsed = json.loads(data['result'])\nexps = parsed['data']['experiments']\n\n# Filter spatial experiments via command field too\nspatial = {}\nfor k, v in exps.items():\n    cmd = v.get('spec', {}).get('command', '') or ''\n    if 'spatial' in k.lower() or '--benchmark spatial' in cmd or '/spatial' in cmd:\n        spatial[k] = v\n\nprint(f\"Total spatial-like: {len(spatial)}\")\n\n# For each, dump key fields\nfor k in sorted(spatial.keys()):\n    v = spatial[k]\n    status = v.get('status', '?')\n    if status != 'DONE':\n        continue\n    cmd = v.get('spec', {}).get('command', '')\n    server = v.get('spec', {}).get('server') or v.get('server') or v.get('spec',{}).get('host') or v.get('metadata',{}).get('server') or ''\n    # try to find seed\n    sm = re.search(r'--seed\\s+(\\d+)', cmd) or re.search(r'seed[\\-_](\\d+)', k)\n    seed = sm.group(1) if sm else '?'\n    # K\n    km = re.search(r'--k\\s+(\\d+)', cmd, re.IGNORECASE) or re.search(r'--K\\s+(\\d+)', cmd) or re.search(r'k(\\d+)[-_]', k)\n    K = km.group(1) if km else None\n    # mode hints\n    mode_hints = []\n    for tag in ['vla_only', 'vla-only', 'adaptive', 'crm', 'random-selection', 'random_selection', 'obs-only', 'reconvla', 'k2mean']:\n        if tag in k.lower() or tag in cmd.lower():\n            mode_hints.append(tag)\n    # results\n    metrics = v.get('metrics') or {}\n    sr = metrics.get('success_rate') or metrics.get('SR') or metrics.get('avg_success') or None\n    conc = v.get('conclusion', '')\n    created = v.get('created_at', '')\n    print(f\"{k}\\n  status={status} seed={seed} K={K} hints={mode_hints} SR={sr}\\n  server={server!r}\\n  created={created}\\n  cmd_snippet={cmd[:200]}\\n\")\nEOF",
    "description": "Extract spatial DONE experiments details"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-24T22:54:53.168546+00:00_

Total spatial-like: 42
eval-adaptive-k-spatial-p25-seed44
  status=DONE seed=44 K=None hints=['adaptive'] SR=None
  server='bjb2-28827'
  created=2026-05-20T10:52:04.790Z
  cmd_snippet=python -u src/evaluate.py --mode adaptive_k --benchmark LIBERO-Spatial --seed 44 --n_rollouts 10 --adaptive_k_threshold 0.054959 --output_file logs/eval-adaptive-k-spatial-p25-seed44.json

eval-adaptive-k-spatial-p50-seed42
  status=DONE seed=42 K=None hints=['adaptive'] SR=None
  server='bjb2-40593'
  created=2026-05-20T11:24:12.894Z
  cmd_snippet=python -u src/evaluate.py --mode adaptive_k --benchmark LIBERO-Spatial --seed 42 --n_rollouts 10 --adaptive_k_threshold 0.074855

eval-adaptive-k-spatial-p75-seed44
  status=DONE seed=44 K=None hints=['adaptive'] SR=None
  server='bjb2-28827'
  created=2026-05-20T10:52:04.320Z
  cmd_snippet=python -u src/evaluate.py --mode adaptive_k --benchmark LIBERO-Spatial --seed 44 --n_rollouts 10 --adaptive_k_threshold 0.098735 --output_file logs/eval-adaptive-k-spatial-p75-seed44.json

eval-adaptive-k-spatial-p90-seed42
  status=DONE seed=42 K=None hints=['adaptive'] SR=None
  server='bjb2-28827'
  created=2026-05-20T10:52:05.759Z
  cmd_snippet=python -u src/evaluate.py --mode adaptive_k --benchmark LIBERO-Spatial --seed 42 --n_rollouts 10 --adaptive_k_threshold 0.125870 --output_file logs/eval-adaptive-k-spatial-p90-seed42.json

eval-adaptive-k-spatial-p90-seed43
  status=DONE seed=43 K=None hints=['adaptive'] SR=0.32
  server='bjb1-18228'
  created=2026-05-20T10:52:06.660Z
  cmd_snippet=python -u src/evaluate.py --mode adaptive_k --benchmark LIBERO-Spatial --seed 43 --n_rollouts 10 --adaptive_k_threshold 0.125870 --output_file logs/eval-adaptive-k-spatial-p90-seed43.json

eval-crm-spatial-k10-seed49
  status=DONE seed=? K=10 hints=['crm'] SR=None
  server='bjb2-28827'
  created=2026-05-21T04:23:28.274Z
  cmd_snippet=harvest

eval-crm-spatial-k10-seed50
  status=DONE seed=? K=10 hints=['crm'] SR=None
  server='bjb1-32546'
  created=2026-05-21T04:23:
…[truncated 5417 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_canonical-data-protocol_20260524T224440",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-24T22:54:53.168710+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 << 'EOF'\nimport json\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/b8bff12d-79aa-4770-9cbd-73119cfe4314/tool-results/mcp-agent-ml-research-read_registry-1779662712168.txt') as f:\n    data = json.load(f)\nparsed = json.loads(data['result'])\nexps = parsed['data']['experiments']\n\n# Print full record for harvest-style spatial experiments\nharvest_keys = [\n    'eval-crm-spatial-k10-seed49',\n    'eval-crm-spatial-k10-seed50',\n    'eval-crm-spatial-seed47',\n    'eval-crm-spatial-seed48',\n    'eval-vla-only-spatial-seed50',\n    'eval-vla-only-spatial-seed51',\n    'eval-vla-only-spatial-seed52',\n    'eval-vla-only-spatial-seed53',\n    'eval-vla-only-spatial-seed54',\n]\nfor k in harvest_keys:\n    if k in exps:\n        v = exps[k]\n        print(f\"==== {k} ====\")\n        print(json.dumps(v, indent=2, default=str)[:1500])\n        print()\nEOF",
  "description": "Inspect harvest-style spatial records"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_canonical-data-protocol_20260524T224440",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 << 'EOF'\nimport json\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/b8bff12d-79aa-4770-9cbd-73119cfe4314/tool-results/mcp-agent-ml-research-read_registry-1779662712168.txt') as f:\n    data = json.load(f)\nparsed = json.loads(data['result'])\nexps = parsed['data']['experiments']\n\n# Print full record for harvest-style spatial experiments\nharvest_keys = [\n    'eval-crm-spatial-k10-seed49',\n    'eval-crm-spatial-k10-seed50',\n    'eval-crm-spatial-seed47',\n    'eval-crm-spatial-seed48',\n    'eval-vla-only-spatial-seed50',\n    'eval-vla-only-spatial-seed51',\n    'eval-vla-only-spatial-seed52',\n    'eval-vla-only-spatial-seed53',\n    'eval-vla-only-spatial-seed54',\n]\nfor k in harvest_keys:\n    if k in exps:\n        v = exps[k]\n        print(f\"==== {k} ====\")\n        print(json.dumps(v, indent=2, default=str)[:1500])\n        print()\nEOF",
    "description": "Inspect harvest-style spatial records"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-24T22:54:53.168924+00:00_

==== eval-crm-spatial-k10-seed49 ====
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-21T04:23:28.274Z",
  "updated_at": "2026-05-21T04:27:48.274Z",
  "spec": {
    "command": "harvest",
    "server": "bjb2-28827",
    "data_path": "logs/eval_spatial_obs_only_norm02_seed49.json",
    "data_count": 100,
    "model_name": "openvla",
    "seed": 49,
    "checkpoint_source": "harvested",
    "eval_data": "spatial",
    "checkpoint_path": "/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed49.json",
    "log_path": "/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed49.json"
  },
  "hypothesis": "CRM with k=10 candidates and observation-only refinement (norm=0.2) on spatial task \u2014 tests refinement quality with larger candidate pool.",
  "conclusion": "success",
  "metrics": {
    "overall_success_rate": 0.32
  },
  "completed_at": "2026-05-21T04:27:48.274Z"
}

==== eval-crm-spatial-k10-seed50 ====
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-21T04:23:09.772Z",
  "updated_at": "2026-05-21T04:27:29.713Z",
  "spec": {
    "command": "harvest",
    "server": "bjb1-32546",
    "data_path": "logs/eval_spatial_obs_only_norm02_seed50.json",
    "data_count": 100,
    "model_name": "openvla",
    "seed": 50,
    "checkpoint_source": "harvested",
    "eval_data": "spatial",
    "checkpoint_path": "/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed50.json",
    "log_path": "/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed50.json"
  },
  "hypothesis": "CRM with k=10 candidates and observation-only refinement (norm=0.2) on spatial task \u2014 tests refinement quality with larger candidate pool.",
  "conclusion": "success",
  "metrics": {
    "overall_success_rate": 0.35
  },
  "completed_at": "2026-05-21T04:27:29.713Z"
}

==== eval-crm-spatial-seed47 ====
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-21T04:23:26.099Z",
  "updat
…[truncated 6339 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_canonical-data-protocol_20260524T224440",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-24T22:54:53.169100+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 << 'EOF'\nimport json\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/b8bff12d-79aa-4770-9cbd-73119cfe4314/tool-results/mcp-agent-ml-research-read_registry-1779662712168.txt') as f:\n    data = json.load(f)\nparsed = json.loads(data['result'])\nexps = parsed['data']['experiments']\n\n# Full record for supp adaptive entries to find file paths\nkeys_to_inspect = [\n    'eval-supp-adapt-tau015-spatial-s42-r2',\n    'eval-supp-adapt-tau025-spatial-s42-r2',\n    'eval-supp-adapt-tau035-spatial-s42-r2',\n    'eval-supp-crm-norm02-spatial-s42-r2',\n    'eval-supp-spatial-reconvla-s45',\n    'eval-vla-only-spatial-seed45',\n    'eval-adaptive-k-spatial-p50-seed42',\n    'eval-adaptive-k-spatial-p90-seed42',\n    'eval-adaptive-k-spatial-p90-seed43',\n    'eval-adaptive-k-spatial-p25-seed44',\n    'eval-adaptive-k-spatial-p75-seed44',\n    'eval-obs-only-spatial-norm02-seed44',\n    'eval-obs-only-spatial-norm02-seed47',\n    'eval-obs-only-spatial-norm02-seed46-r2',\n]\nfor k in keys_to_inspect:\n    if k in exps:\n        v = exps[k]\n        cmd = v.get('spec', {}).get('command', '')\n        server = v.get('spec', {}).get('server','')\n        metrics = v.get('metrics', {})\n        print(f\"{k}\")\n        print(f\"  server={server}\")\n        print(f\"  metrics={metrics}\")\n        print(f\"  cmd={cmd[:400]}\")\n        print()\nEOF",
  "description": "Inspect adaptive and supp full commands"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_canonical-data-protocol_20260524T224440",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 << 'EOF'\nimport json\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/b8bff12d-79aa-4770-9cbd-73119cfe4314/tool-results/mcp-agent-ml-research-read_registry-1779662712168.txt') as f:\n    data = json.load(f)\nparsed = json.loads(data['result'])\nexps = parsed['data']['experiments']\n\n# Full record for supp adaptive entries to find file paths\nkeys_to_inspect = [\n    'eval-supp-adapt-tau015-spatial-s42-r2',\n    'eval-supp-adapt-tau025-spatial-s42-r2',\n    'eval-supp-adapt-tau035-spatial-s42-r2',\n    'eval-supp-crm-norm02-spatial-s42-r2',\n    'eval-supp-spatial-reconvla-s45',\n    'eval-vla-only-spatial-seed45',\n    'eval-adaptive-k-spatial-p50-seed42',\n    'eval-adaptive-k-spatial-p90-seed42',\n    'eval-adaptive-k-spatial-p90-seed43',\n    'eval-adaptive-k-spatial-p25-seed44',\n    'eval-adaptive-k-spatial-p75-seed44',\n    'eval-obs-only-spatial-norm02-seed44',\n    'eval-obs-only-spatial-norm02-seed47',\n    'eval-obs-only-spatial-norm02-seed46-r2',\n]\nfor k in keys_to_inspect:\n    if k in exps:\n        v = exps[k]\n        cmd = v.get('spec', {}).get('command', '')\n        server = v.get('spec', {}).get('server','')\n        metrics = v.get('metrics', {})\n        print(f\"{k}\")\n        print(f\"  server={server}\")\n        print(f\"  metrics={metrics}\")\n        print(f\"  cmd={cmd[:400]}\")\n        print()\nEOF",
    "description": "Inspect adaptive and supp full commands"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-24T22:54:53.169285+00:00_

eval-supp-adapt-tau015-spatial-s42-r2
  server=bjb1-32546
  metrics={'success_rate': 0.805, 'trigger_rate': 0.407, 'mean_unc': 0.1852, 'per_task_sr': {'between_plate_ramekin': 1, 'next_to_ramekin': 0.9, 'table_center': 0.95, 'cookie_box': 0.95, 'top_drawer': 0.75, 'on_ramekin': 0, 'next_to_cookie_box': 0.95, 'stove': 0.9, 'next_to_plate': 0.8, 'wooden_cabinet': 0.85}}
  cmd=python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark spatial --seed 42 --n_rollouts 20 --conformal_threshold 0.15 --max_correction_norm 0.2

eval-supp-adapt-tau025-spatial-s42-r2
  server=bjb1-32546
  metrics={'success_rate': 0.82, 'trigger_rate': 0.194, 'mean_unc': 0.1847, 'per_task_sr': {'between_plate_ramekin': 0.95, 'next_to_ramekin': 0.95, 'table_center': 1, 'cookie_box': 1, 'top_drawer': 0.75, 'on_ramekin': 0, 'next_to_cookie_box': 0.9, 'stove': 0.9, 'next_to_plate': 0.9, 'wooden_cabinet': 0.85}}
  cmd=python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark spatial --seed 42 --n_rollouts 20 --conformal_threshold 0.25 --max_correction_norm 0.2

eval-supp-adapt-tau035-spatial-s42-r2
  server=bjb1-32546
  metrics={'success_rate': 0.8, 'trigger_rate': 0.122, 'mean_unc': 0.1873, 'per_task_sr': {'between_plate_ramekin': 0.95, 'next_to_ramekin': 1, 'table_center': 0.9, 'cookie_box': 0.95, 'top_drawer': 0.7, 'on_ramekin': 0, 'next_to_cookie_box': 0.95, 'stove': 0.85, 'next_to_plate': 0.85, 'wooden_cabinet': 0.85}}
  cmd=python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark spatial --seed 42 --n_rollouts 20 --conformal_threshold 0.35 --max_correction_norm 0.2

eval-supp-crm-norm02-spatial-s42-r2
  server=bjb1-32546
  metrics={'success_rate': 0.79, 'per_task_sr': {'between_plate_ramekin': 1, 'next_to_ramekin': 0.9, 'table_ce
…[truncated 4153 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_canonical-data-protocol_20260524T224440",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-24T22:54:53.169471+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ 2>&1 | head -30",
  "description": "List project root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_canonical-data-protocol_20260524T224440",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ 2>&1 | head -30",
    "description": "List project root"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-24T22:54:53.169606+00:00_

total 3940
drwxr-xr-x 12 ubuntu ubuntu    4096 May 24 22:43 .
drwxrwxr-x  6 ubuntu ubuntu    4096 May 24 19:27 ..
drwxr-xr-x  3 ubuntu ubuntu    4096 May 13 01:01 .claude
-rw-------  1 ubuntu ubuntu       0 May 19 12:44 .registry_33t8xd4z.tmp
-rw-------  1 ubuntu ubuntu 1106966 May 24 03:57 .registry_3rh2tyz0.tmp
-rw-------  1 ubuntu ubuntu  614962 May 24 18:18 .registry_hp5nas9m.tmp
-rw-r--r--  1 ubuntu ubuntu   13092 May 24 22:47 AGENTS.md
-rw-r--r--  1 ubuntu ubuntu       0 May 13 01:03 ROADMAP.lock
-rw-------  1 ubuntu ubuntu    4497 May 24 22:43 ROADMAP.md
-rw-r--r--  1 ubuntu ubuntu      90 May 21 17:00 _last_visual_review.json
drwxr-xr-x 36 ubuntu ubuntu   12288 May 24 22:37 artifacts
drwxr-xr-x  2 ubuntu ubuntu  499712 May 24 22:43 checkpoints
-rw-r--r--  1 ubuntu ubuntu       0 May 13 01:03 decisions.lock
-rw-------  1 ubuntu ubuntu  134105 May 24 22:43 decisions.yaml
drwxr-xr-x  4 ubuntu ubuntu    4096 May 24 09:10 docs
-rwxr-xr-x  1 ubuntu ubuntu       0 May 13 01:50 dream_registry.lock
-rw-------  1 ubuntu ubuntu    1890 May 13 03:26 dream_registry.yaml
-rw-r--r--  1 ubuntu ubuntu    1895 May 13 03:26 dream_registry.yaml.bak
-rw-r--r--  1 ubuntu ubuntu       0 May 13 04:05 experiment_plan.lock
-rw-------  1 ubuntu ubuntu    7945 May 21 04:34 experiment_plan.yaml
drwxr-xr-x  3 ubuntu ubuntu    4096 May 24 07:23 figures
-rw-r--r--  1 ubuntu ubuntu   41299 May 18 09:27 literature_map.yaml
drwxr-xr-x  4 ubuntu ubuntu    4096 May 13 01:23 logs
-rw-r--r--  1 ubuntu ubuntu    3869 May 23 21:30 memory.md
-rw-r--r--  1 ubuntu ubuntu       0 May 17 03:06 mistakes.lock
-rw-------  1 ubuntu ubuntu   87656 May 24 22:42 mistakes.yaml
-rw-r--r--  1 ubuntu ubuntu   15290 May 22 06:17 openvla_oft_wrapper.py
drwxr-xr-x  3 ubuntu ubuntu    4096 May 21 11:28 paper
-rw-r--r--  1 ubuntu ubuntu   36276 May 24 21:53 paper_framing.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_canonical-data-protocol_20260524T224440",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-24T22:54:53.169747+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/ | head -50 && echo \"---\" && ls /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/ | grep -i -E \"spatial|canonical|p_value|pvalue|paired\"",
  "description": "List artifacts and search spatial/canonical"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_canonical-data-protocol_20260524T224440",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/ | head -50 && echo \"---\" && ls /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/ | grep -i -E \"spatial|canonical|p_value|pvalue|paired\"",
    "description": "List artifacts and search spatial/canonical"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-24T22:54:53.169884+00:00_

3dir_spatial_s42_results.md
__pycache__
_project
ablation_eval_commands.md
adaptive_k_design.md
adaptive_k_eval_prep.md
analysis
analysis-train-crm-unified-4suite-r6.md
analysis_magnitude_sweep.py
analysis_object_benchmark.py
analysis_rank_deficient
analysis_rank_deficient.py
analysis_spatial_final.py
argmin_seed44_r2_results.json
batched_inference_feasibility_report.md
benchmark_data_audit.md
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
crm_eval_partial_results.md
crm_eval_results_harvest.md
crm_k1_model.py
d139_status_scan.md
deploy_3dir_spatial_seed42.md
deploy_adaptive_k_eval.sh
deploy_pi05_crm_eval.sh
deploy_smolvla_crm_eval.sh
diag-eval-supp-goal-reconvla-s45.md
diag-eval-v6-batch-failure.md
diag_bjb1_18228.md
diag_bjb2_28827.md
diag_cqa1_32758_failures_20260524.md
diag_plan_a_spatial_seed42_43.md
diagnose-eval-adaptive-k-spatial-p50-seed44.md
diagnose-norm02-seed44-r2.md
diagnose-random-selection-seed46-r2.md
diagnose_bjb1_18228_failure.md
diagnose_bjb1_32546_batch_failure.md
diagnose_bjb2_failures_20260523.md
diagnose_crm_long_seed45.md
diagnose_crm_spatial_timeout.md
diagnose_default_seed46.md
---
3dir_spatial_s42_results.md
analysis_spatial_final.py
deploy_3dir_spatial_seed42.md
diag_plan_a_spatial_seed42_43.md
diagnose-eval-adaptive-k-spatial-p50-seed44.md
diagnose_crm_spatial_timeout.md
diagnose_spatial_k5_seed44_r2.md
eval-reconvla-spatial-v1-diag.md
eval-supp-k2mean-spatial-s42
spatial_analysis_prep.md
spatial_cache_diagnosis.md
spatial_comparison_template.md
spatial_per_task_breakdown.md
spatial_training_diagnosis.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_canonical-data-protocol_20260524T224440",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-24T22:54:53.170013+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/ | grep -i -E \"audit|cross|server|reviewer|protocol\"",
  "description": "List artifacts related to audit/reviewer"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_canonical-data-protocol_20260524T224440",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/ | grep -i -E \"audit|cross|server|reviewer|protocol\"",
    "description": "List artifacts related to audit/reviewer"
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-24T22:54:53.170132+00:00_

benchmark_data_audit.md
citation_attribution_audit.md
citation_audit_report.md
crm_bug_audit.md
n_rollouts_audit_report.md
paper_audit_20260521.md
pi05_cross_vla_outline.md
pi05_server.py
pi05_server_client_feasibility.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_canonical-data-protocol_20260524T224440",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-24T22:54:53.170255+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/memory.md",
  "description": "Read project memory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_canonical-data-protocol_20260524T224440",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/memory.md",
    "description": "Read project memory"
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-24T22:54:53.170424+00:00_

# Server Scan Report — 2026-05-24 05:30 UTC

## bjb2-28827 (6× RTX 4090)

| exp_id | GPU | 预期PID | 实际PID | 状态 | 备注 |
|--------|-----|---------|---------|------|------|
| eval-supp-goal-vla-only-s45 | cuda:0 | — | 926766 | ALIVE | 19% util, 3685 MiB |
| eval-supp-goal-crm-norm005-s45 | cuda:1 | — | 927030 | ALIVE | 22% util, 4235 MiB |
| eval-supp-goal-reconvla-s45 | cuda:2 | — | 927237 | ALIVE | 28% util, 3747 MiB |
| eval-supp-long-k2mean-s45 | cuda:4 | 924226 | 924226 | ALIVE | 18% util, 5591 MiB |
| eval-supp-long-k2mean-s44 | cuda:5 | 850410 | 850410 | ALIVE | 22% util, 2307 MiB |
| *eval-supp-long-reconvla-s44* | cuda:3 | — | 849677 | ALIVE | **未在预期列表** 0% GPU util但占1755 MiB |

空闲 GPU: **无**

Tmux sessions: eval-goal-crm-s45, eval-goal-reconvla-s45, eval-goal-vla-s45, eval-long-k2mean-s45, eval-supp-long-k2mean-s44, eval-supp-long-reconvla-s44

---

## bjb1-32546 (6× RTX 4090)

| exp_id | GPU | 预期PID | 实际PID | 状态 | 备注 |
|--------|-----|---------|---------|------|------|
| eval-supp-crm-norm005-obj-s46 | cuda:0 | — | 102927 | ALIVE | 33% util, 3389 MiB |
| eval-supp-long-vla-only-s45 | cuda:1 | — | 103128 | ALIVE | 21% util, 4911 MiB |
| eval-supp-long-adapt-tau025-s45 | cuda:2 | — | 103397 | ALIVE | 23% util, 4917 MiB |
| eval-supp-long-crm-norm005-s45 | cuda:3 | — | 103675 | ALIVE | 24% util, 5011 MiB |
| eval-supp-long-reconvla-s45 | cuda:4 | — | 103942 | ALIVE | 31% util, 4973 MiB |
| eval-supp-goal-adapt-tau025-s45 | cuda:5 | — | 104216 | ALIVE | 22% util, 2786 MiB |

空闲 GPU: **无**

Tmux sessions: eval-crm-obj-s46, eval-goal-adapt-s45, eval-long-adapt-s45, eval-long-crm-s45, eval-long-reconvla-s45, eval-long-vla-s45

---

## cqa1-32758 (6× RTX 4090 D)

| exp_id | GPU | 预期PID | 实际PID | 状态 | 备注 |
|--------|-----|---------|---------|------|------|
| eval-supp-reconvla-obj-s46 | cuda:2 | — | 380176 | ALIVE | 32% util, 2183 MiB |
| eval-supp-k2mean-obj-s46 | cuda:3 | — | — | COMPLETED | 76.5% (153/200), saved eval_object_vla_only_seed46.json |
| eval-supp-k2mean
…[truncated 1586 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_canonical-data-protocol_20260524T224440",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-24T22:54:53.170568+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/analysis_spatial_final.py 2>/dev/null | head -200",
  "description": "Read analysis_spatial_final.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_canonical-data-protocol_20260524T224440",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/analysis_spatial_final.py 2>/dev/null | head -200",
    "description": "Read analysis_spatial_final.py"
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-24T22:54:53.170746+00:00_

#!/usr/bin/env python3
"""Spatial benchmark final analysis: merge partial + restart results, generate comparison table."""

import json
import os
import re
import sys

import yaml
import matplotlib
matplotlib.use("Agg")

# ── paths ──────────────────────────────────────────────────────────────
REGISTRY = os.path.join(os.path.dirname(__file__), "..", "registry.yaml")
OUT_DIR = os.path.join(os.path.dirname(__file__), "figures")
os.makedirs(OUT_DIR, exist_ok=True)

# ── canonical spatial tasks (order from eval-spatial-v7-full) ──────────
SPATIAL_TASKS = [
    "between_plate_and_ramekin",
    "next_to_ramekin",
    "from_table_center",
    "on_cookie_box",
    "in_top_drawer",
    "on_ramekin",
    "next_to_cookie_box",
    "on_stove",
    "next_to_plate",
    "on_wooden_cabinet",
]

TASK_SHORT_TO_FULL = {t: f"pick_up_black_bowl_{t}" for t in SPATIAL_TASKS}

TASK_DISPLAY = {
    "between_plate_and_ramekin": "Betw. Plate\n& Ramekin",
    "next_to_ramekin": "Next to\nRamekin",
    "from_table_center": "Table\nCenter",
    "on_cookie_box": "On Cookie\nBox",
    "in_top_drawer": "In Top\nDrawer",
    "on_ramekin": "On\nRamekin",
    "next_to_cookie_box": "Next to\nCookie Box",
    "on_stove": "On\nStove",
    "next_to_plate": "Next to\nPlate",
    "on_wooden_cabinet": "On Wooden\nCabinet",
}

# ── experiments to merge per method ────────────────────────────────────
# Each method maps to a list of experiment IDs to merge (base + restarts).
# Later experiments overwrite earlier ones for the same task.
SPATIAL_METHODS = {
    "VLA-only (K=1)": {
        "exp_ids": ["eval-spatial-v7-full"],
        "color": "#AAAAAA",
    },
    "VLA-mean (K=10)": {
        "exp_ids": ["eval-vla-mean-spatial", "eval-vla-mean-spatial-t10"],
        "color": "#888888",
    },
    "ReconVLA argmin (K=10)": {
        "exp_ids": ["eval-reconvla-spatial-v3"],
        "color": "#555555",
    },
    "Argmin-only (K=10)": {
        "exp_ids": ["eval-argmin-only-spatial", "eval-argmin-only-spatial-r2"],

…[truncated 4237 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_canonical-data-protocol_20260524T224440",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-24T22:54:53.170915+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/ | grep -i -E \"p_value|pvalue|paired|stat|signif|t_test|ttest\"",
  "description": "Search artifacts for p-value/stat files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_canonical-data-protocol_20260524T224440",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/ | grep -i -E \"p_value|pvalue|paired|stat|signif|t_test|ttest\"",
    "description": "Search artifacts for p-value/stat files"
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-24T22:54:53.171042+00:00_

d139_status_scan.md
experiment_status_20260523_session25.md
experiment_status_check.md
gpu_status_bjb1_32546.md
pi05_fix3_status_check.md
precompute_pipeline_status_latest.md
precompute_status_check.md
report_running_status.md
smolvla_baseline_status_20260522.md
statistical_analysis.py
statistical_analysis_output.txt
statistical_analysis_output_v2.txt
statistical_analysis_output_v3.txt
statistical_analysis_output_v4.txt
tau_k_sweep_status.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_canonical-data-protocol_20260524T224440",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-24T22:54:53.171161+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/statistical_analysis_output_v4.txt 2>/dev/null | head -120",
  "description": "Read latest statistical analysis output"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_canonical-data-protocol_20260524T224440",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/statistical_analysis_output_v4.txt 2>/dev/null | head -120",
    "description": "Read latest statistical analysis output"
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-24T22:54:53.171345+00:00_

================================================================================
STATISTICAL ANALYSIS: ACR-VLA Conformal Refinement Experiments
All success rates are fractions (0.0 to 1.0)
Object benchmark primary CRM config: norm02 (ε=0.2), K=10
================================================================================

1. LIBERO-SPATIAL
--------------------------------------------------------------------------------
  CRM obs_only (n=8): n=8, mean=0.3438, std=0.0141, min=0.3200, max=0.3600
    values: [0.35, 0.34, 0.36, 0.34, 0.33, 0.32, 0.35, 0.36]
  VLA-only (n=9): n=9, mean=0.2956, std=0.0113, min=0.2700, max=0.3100
    values: [0.3, 0.29, 0.31, 0.27, 0.3, 0.3, 0.3, 0.29, 0.3]

  CRM vs VLA-only:
    Difference: +0.0482 (+4.82 pp)
    Welch's t-test: t=7.7198, p=0.000003 ***
    Mann-Whitney U: U=72.0, p=0.000526 ***
    Cohen's d: 3.8024 (large)


2. LIBERO-LONG
--------------------------------------------------------------------------------
  CRM obs_only (n=7): n=7, mean=0.1700, std=0.0200, min=0.1400, max=0.2000
    values: [0.17, 0.15, 0.2, 0.18, 0.18, 0.17, 0.14]
  VLA-only (n=10): n=10, mean=0.1470, std=0.0231, min=0.1100, max=0.1800
    values: [0.11, 0.13, 0.12, 0.17, 0.18, 0.14, 0.14, 0.16, 0.15, 0.17]

  CRM vs VLA-only:
    Difference: +0.0230 (+2.30 pp)
    Welch's t-test: t=2.1871, p=0.045951 *
    Mann-Whitney U: U=54.5, p=0.060630 n.s.
    Cohen's d: 1.0491 (large)


3. LIBERO-GOAL
--------------------------------------------------------------------------------
  CRM obs_only (n=6): n=6, mean=0.6817, std=0.0343, min=0.6400, max=0.7200
    values: [0.67, 0.72, 0.64, 0.65, 0.72, 0.69]
  VLA-only (n=6): n=6, mean=0.6867, std=0.0388, min=0.6300, max=0.7300
    values: [0.71, 0.69, 0.73, 0.63, 0.71, 0.65]

  CRM vs VLA-only:
    Difference: -0.0050 (-0.50 pp)
    Welch's t-test: t=-0.2364, p=0.817940 n.s.
    Mann-Whitney U: U=17.0, p=0.935736 n.s.
    Cohen's d: -0.1365 (negligible)


4. LIBERO-OBJECT
------------------------------------------
…[truncated 2679 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_canonical-data-protocol_20260524T224440",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-24T22:54:53.171532+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/statistical_analysis_output_v4.txt 2>/dev/null | wc -l && echo \"---\" && cat /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/statistical_analysis.py 2>/dev/null | head -100",
  "description": "Check statistical_analysis.py and v4 length"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_canonical-data-protocol_20260524T224440",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/statistical_analysis_output_v4.txt 2>/dev/null | wc -l && echo \"---\" && cat /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/statistical_analysis.py 2>/dev/null | head -100",
    "description": "Check statistical_analysis.py and v4 length"
  }
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-24T22:54:53.171694+00:00_

201
---
#!/usr/bin/env python3
"""
Statistical analysis of ACR-VLA Conformal Refinement experiments.
Compares CRM (obs_only) vs VLA-only baselines across LIBERO benchmarks.
Also includes Argmin and Adaptive-K baselines.

Primary CRM config for Object: norm02 (ε=0.2), K=10.
"""

import numpy as np
from scipy import stats

def print_separator(char='=', width=80):
    print(char * width)

def print_group_stats(name, values):
    arr = np.array(values)
    print(f"  {name}: n={len(arr)}, mean={arr.mean():.4f}, std={arr.std(ddof=1):.4f}, "
          f"min={arr.min():.4f}, max={arr.max():.4f}")
    print(f"    values: {[round(v, 4) for v in values]}")

def run_tests(name_a, vals_a, name_b, vals_b):
    a = np.array(vals_a)
    b = np.array(vals_b)

    t_stat, t_pval = stats.ttest_ind(a, b, equal_var=False)
    u_stat, u_pval = stats.mannwhitneyu(a, b, alternative='two-sided')

    pooled_std = np.sqrt(((len(a)-1)*a.std(ddof=1)**2 + (len(b)-1)*b.std(ddof=1)**2) /
                         (len(a) + len(b) - 2))
    cohens_d = (a.mean() - b.mean()) / pooled_std if pooled_std > 0 else float('inf')

    diff = a.mean() - b.mean()
    diff_pct = diff * 100

    print(f"\n  {name_a} vs {name_b}:")
    print(f"    Difference: {diff:+.4f} ({diff_pct:+.2f} pp)")
    print(f"    Welch's t-test: t={t_stat:.4f}, p={t_pval:.6f} {'***' if t_pval < 0.001 else '**' if t_pval < 0.01 else '*' if t_pval < 0.05 else 'n.s.'}")
    print(f"    Mann-Whitney U: U={u_stat:.1f}, p={u_pval:.6f} {'***' if u_pval < 0.001 else '**' if u_pval < 0.01 else '*' if u_pval < 0.05 else 'n.s.'}")
    print(f"    Cohen's d: {cohens_d:.4f} ({'large' if abs(cohens_d) > 0.8 else 'medium' if abs(cohens_d) > 0.5 else 'small' if abs(cohens_d) > 0.2 else 'negligible'})")

    return t_pval, u_pval

# ============================================================================
# DATA (from registry, conclusion=success, 2026-05-20)
# Each seed appears once; r2/r3 supersedes earlier runs.
# =============================
…[truncated 2489 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_canonical-data-protocol_20260524T224440",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-24T22:54:53.171846+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/statistical_analysis_output_v4.txt 2>/dev/null | tail -120",
  "description": "Tail of statistical analysis output"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_canonical-data-protocol_20260524T224440",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/statistical_analysis_output_v4.txt 2>/dev/null | tail -120",
    "description": "Tail of statistical analysis output"
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-24T22:54:53.172011+00:00_

    Cohen's d: 2.8903 (large)


5. ARGMIN BASELINES (Object)
--------------------------------------------------------------------------------
  Argmin K=10 (n=5): n=5, mean=0.1240, std=0.0288, min=0.1000, max=0.1700
    values: [0.17, 0.13, 0.12, 0.1, 0.1]
  Argmin K=5 (n=4): n=4, mean=0.1300, std=0.0163, min=0.1100, max=0.1500
    values: [0.15, 0.13, 0.11, 0.13]
  VLA-only (n=8): n=8, mean=0.1088, std=0.0136, min=0.0900, max=0.1300
    values: [0.12, 0.12, 0.1, 0.11, 0.13, 0.1, 0.1, 0.09]
  CRM norm02 K=10 (n=6): n=6, mean=0.1683, std=0.0183, min=0.1500, max=0.2000
    values: [0.16, 0.16, 0.16, 0.15, 0.2, 0.18]

  Argmin K=10 vs VLA-only:

  Argmin K=10 vs VLA-only:
    Difference: +0.0152 (+1.52 pp)
    Welch's t-test: t=1.1093, p=0.316589 n.s.
    Mann-Whitney U: U=26.5, p=0.362759 n.s.
    Cohen's d: 0.7451 (medium)

  Argmin K=10 vs CRM norm02 K=10:

  Argmin K=10 vs CRM norm02:
    Difference: -0.0443 (-4.43 pp)
    Welch's t-test: t=-2.9747, p=0.022297 *
    Mann-Whitney U: U=4.0, p=0.052478 n.s.
    Cohen's d: -1.8803 (large)


6. ADAPTIVE-K BASELINES (Object)
--------------------------------------------------------------------------------
  Adaptive-K p25 (n=3): n=3, mean=0.1433, std=0.0115, min=0.1300, max=0.1500
    values: [0.15, 0.13, 0.15]
  Adaptive-K p50 (n=3): n=3, mean=0.1533, std=0.0115, min=0.1400, max=0.1600
    values: [0.16, 0.16, 0.14]
  Adaptive-K p75 (n=3): n=3, mean=0.1367, std=0.0208, min=0.1200, max=0.1600
    values: [0.12, 0.13, 0.16]
  Adaptive-K p90 (n=3): n=3, mean=0.1333, std=0.0115, min=0.1200, max=0.1400
    values: [0.12, 0.14, 0.14]
  Adaptive-K all (n=12): n=12, mean=0.1417, std=0.0147, min=0.1200, max=0.1600
    values: [0.15, 0.13, 0.15, 0.16, 0.16, 0.14, 0.12, 0.13, 0.16, 0.12, 0.14, 0.14]
  VLA-only (n=8): n=8, mean=0.1088, std=0.0136, min=0.0900, max=0.1300
    values: [0.12, 0.12, 0.1, 0.11, 0.13, 0.1, 0.1, 0.09]
  CRM norm02 K=10 (n=6): n=6, mean=0.1683, std=0.0183, min=0.1500, max=0.2000
    values: [0.16, 0.16, 0.16
…[truncated 3989 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_canonical-data-protocol_20260524T224440",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-24T22:54:53.172173+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -t /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/ | grep -i -E \"stat|p_value|paired|canonical|spatial|reviewer|reanalys\" | head -30",
  "description": "Recent stat/spatial artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_canonical-data-protocol_20260524T224440",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -t /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/ | grep -i -E \"stat|p_value|paired|canonical|spatial|reviewer|reanalys\" | head -30",
    "description": "Recent stat/spatial artifacts"
  }
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-24T22:54:53.172358+00:00_

spatial_per_task_breakdown.md
tau_k_sweep_status.md
d139_status_scan.md
eval-supp-k2mean-spatial-s42
experiment_status_20260523_session25.md
3dir_spatial_s42_results.md
gpu_status_bjb1_32546.md
experiment_status_check.md
deploy_3dir_spatial_seed42.md
smolvla_baseline_status_20260522.md
diagnose_crm_spatial_timeout.md
spatial_cache_diagnosis.md
spatial_training_diagnosis.md
precompute_pipeline_status_latest.md
precompute_status_check.md
pi05_fix3_status_check.md
diag_plan_a_spatial_seed42_43.md
statistical_analysis.py
statistical_analysis_output_v4.txt
statistical_analysis_output_v3.txt
diagnose-eval-adaptive-k-spatial-p50-seed44.md
statistical_analysis_output_v2.txt
statistical_analysis_output.txt
diagnose_spatial_k5_seed44_r2.md
analysis_spatial_final.py
spatial_analysis_prep.md
report_running_status.md
spatial_comparison_template.md
eval-reconvla-spatial-v1-diag.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_canonical-data-protocol_20260524T224440",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-24T22:54:53.172506+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/spatial_per_task_breakdown.md 2>/dev/null | head -100",
  "description": "Read spatial per task breakdown"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_canonical-data-protocol_20260524T224440",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/spatial_per_task_breakdown.md 2>/dev/null | head -100",
    "description": "Read spatial per task breakdown"
  }
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-24T22:54:53.172657+00:00_

# Spatial Per-Task SR Breakdown (P0: Reviewer Response)

Generated: 2026-05-24
Eval regime: LIBERO-Spatial, n_rollouts=20 per task, 10 tasks, 8 seeds (42-49)
Methods: VLA-only (baseline_mode=single) vs Adaptive Conformal CRM (τ=0.25, norm=0.2)

## Data Sources (canonical files used)

| Seed | VLA-only source | Adaptive source |
|------|-----------------|-----------------|
| 42 | cqa1-32758 | bjb1-32546 |
| 43 | cqa1-32758 | bjb1-32546 |
| 44 | bjb2-40593 | bjb1-32546 |
| 45 | cqa1-32758 | cqa1-32758 |
| 46 | cqa1-32758 | cqa1-32758 |
| 47 | cqa1-32758 | cqa1-32758 |
| 48 | cqa1-32758 | bjb2-28827 |
| 49 | cqa1-32758 | bjb2-28827 |

All files: `logs/eval_spatial_vla_only_seedXX.json`,
`logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seedXX.json`.

## Per-Task SR (mean over 8 seeds × 20 rollouts = 160 trials per cell)

| Task | VLA-only SR | Adaptive SR | Δ | 备注 |
|------|-------------|-------------|-----|------|
| between_plate_and_ramekin | 92.5% | 96.3% | **+3.75pp** | |
| next_to_ramekin | 94.4% | 96.3% | +1.88pp | |
| from_table_center | 95.6% | 98.8% | **+3.12pp** | |
| on_cookie_box | 95.6% | 98.8% | **+3.12pp** | |
| in_top_drawer | 71.9% | 69.4% | **-2.50pp** | Adaptive 反降；唯一负 Δ task |
| on_ramekin | 0.0% | 0.0% | 0.00pp | **always-0%** (任务自身极难) |
| next_to_cookie_box | 96.9% | 97.5% | +0.62pp | 接近天花板 |
| on_stove | 81.3% | 82.5% | +1.25pp | |
| next_to_plate | 78.8% | 81.3% | +2.50pp | |
| on_wooden_cabinet | 83.8% | 85.0% | +1.25pp | |
| **10-task overall** | **79.06%** | **80.56%** | **+1.50pp** | |

## Per-Seed Overall SR and Trigger Rate (all 10 tasks)

| Seed | VLA-only | Adaptive | Δ | trigger_rate |
|------|----------|----------|-----|--------------|
| 42 | 78.50% | 79.50% | +1.00pp | 19.65% |
| 43 | 79.00% | 80.00% | +1.00pp | 19.45% |
| 44 | 78.50% | 80.50% | +2.00pp | 19.98% |
| 45 | 77.00% | 80.00% | +3.00pp | 19.96% |
| 46 | 80.50% | 80.00% | -0.50pp | 19.92% |
| 47 | 81.00% | 81.50% | +0.50pp | 20.46% |
| 48 | 79.50% | 81.00% | +1.50pp 
…[truncated 2079 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_canonical-data-protocol_20260524T224440",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-24T22:54:53.172828+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "find /root/acr-vla-conformal-refinement/logs -maxdepth 2 -name \"eval_spatial*\" -type f -printf \"%f\\t%s\\t%TY-%Tm-%Td %TH:%TM\\n\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_canonical-data-protocol_20260524T224440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "find /root/acr-vla-conformal-refinement/logs -maxdepth 2 -name \"eval_spatial*\" -type f -printf \"%f\\t%s\\t%TY-%Tm-%Td %TH:%TM\\n\""
  }
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-24T22:54:53.172991+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"eval_spatial_norm02_seed45.log\\t13445\\t2026-05-19 20:41\\neval_spatial_obs_only_norm02_k5_seed43.json\\t1697\\t2026-05-19 18:18\\neval_spatial_obs_only_norm02_seed45.json\\t1697\\t2026-05-19 20:41\\neval_spatial_vla_only_seed42.json\\t1692\\t2026-05-19 22:32\\neval_spatial_vla_only_seed45.json\\t1692\\t2026-05-19 23:16\\neval_spatial_obs_only_norm02_seed47.json\\t1696\\t2026-05-20 00:58\\neval_spatial_obs_only_norm02_seed43_r2.json\\t1698\\t2026-05-20 03:44\\neval_spatial_vla_only_seed46.json\\t1691\\t2026-05-20 04:23\\neval_spatial_vla_only_seed47.json\\t1691\\t2026-05-20 11:13\\neval_spatial_vla_only_seed48.log\\t4643\\t2026-05-20 06:06\\neval_spatial_vla_only_seed48.json\\t1692\\t2026-05-20 06:06\\neval_spatial_vla_only_seed49.json\\t1692\\t2026-05-20 06:50\\neval_spatial_obs_only_norm02_seed48.json\\t1697\\t2026-05-20 10:53\\neval_spatial_obs_only_norm02_seed50.json\\t1697\\t2026-05-20 12:17\\neval_spatial_vla_only_seed51.json\\t1693\\t2026-05-20 12:47\\neval_spatial_vla_only_seed54.json\\t1692\\t2026-05-20 15:13\\neval_spatial_vla_only_pi05_seed42.json\\t1704\\t2026-05-25 02:46\\neval_spatial_vla_only_pi05_seed45.json\\t1703\\t2026-05-21 20:15\\neval_spatial_vla_only_pi05_seed43.json\\t1704\\t2026-05-25 02:50\\neval_spatial_crm_obs_only_norm0.05_seed42.json\\t1708\\t2026-05-23 11:10\\neval_spatial_crm_obs_only_norm0.1_seed42.json\\t1711\\t2026-05-23 11:14\\neval_spatial_reconvla_seed42.json\\t1706\\t2026-05-23 16:28\\neval_spatial_adaptive_conformal_crm_tau0.074855_seed42.json\\t1907\\t2026-05-23 11:18\\neval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed42.json\\t1904\\t2026-05-25 01:09\\neval_spatial_crm_obs_only_norm0.2_seed42.json\\t1711\\t2026-05-23 14:06\\neval_spatial_adaptive_conformal_crm_norm0.2_tau0.15_seed42.json\\t1907\\t2026-05-23 14:09\\neval_spatial_adaptive_conformal_crm_norm0.2_tau0.35_seed42.json\\t1905\\t2026-05-23 14:14\\neval_spatial_crm_obs_only_norm0.05_seed43.json\\t1711\\t2
…[truncated 714 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_canonical-data-protocol_20260524T224440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-24T22:54:53.173137+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "find /root/acr-vla-conformal-refinement/logs -maxdepth 2 -name \"eval_spatial*\" -type f -printf \"%f\\t%s\\t%TY-%Tm-%Td %TH:%TM\\n\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_canonical-data-protocol_20260524T224440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "find /root/acr-vla-conformal-refinement/logs -maxdepth 2 -name \"eval_spatial*\" -type f -printf \"%f\\t%s\\t%TY-%Tm-%Td %TH:%TM\\n\""
  }
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-24T22:54:53.173310+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"eval_spatial_perdof_norm003.log\\t1313\\t2026-05-15 11:11\\neval_spatial_perdof_norm005.log\\t1315\\t2026-05-15 11:12\\neval_spatial_perdof_norm02.log\\t1311\\t2026-05-15 11:14\\neval_spatial_perdof_norm03.log\\t1313\\t2026-05-15 11:17\\neval_spatial_obsonly_norm005.log\\t1329\\t2026-05-15 11:19\\neval_spatial_obsonly_norm02.log\\t1329\\t2026-05-15 11:21\\neval_spatial_norm02_seed44.log\\t13528\\t2026-05-19 22:03\\neval_spatial_obs_only_norm02_k5_seed42.json\\t1697\\t2026-05-19 18:55\\neval_spatial_obs_only_norm02_k5_seed44.log\\t4965\\t2026-05-19 23:45\\neval_spatial_obs_only_norm02_k5_seed45.log\\t4958\\t2026-05-19 23:49\\neval_spatial_obs_only_norm02_seed44.json\\t1698\\t2026-05-19 22:03\\neval_spatial_vla_only_seed44.json\\t1705\\t2026-05-23 09:30\\neval_spatial_obs_only_norm02_k5_seed44.json\\t1698\\t2026-05-19 23:45\\neval_spatial_obs_only_norm02_k5_seed45.json\\t1697\\t2026-05-19 23:49\\neval_spatial_obs_only_norm02_seed46_r2.json\\t1697\\t2026-05-20 02:50\\neval_spatial_obs_only_norm02_seed49.json\\t1696\\t2026-05-20 12:37\\neval_spatial_obs_only_seed45.log\\t4937\\t2026-05-21 16:48\\neval_spatial_obs_only_seed45.json\\t1696\\t2026-05-21 16:48\\neval_spatial_vla_only_seed43.json\\t1707\\t2026-05-23 09:31\\neval_spatial_vla_only_seed42.json\\t1705\\t2026-05-23 17:32\\neval_spatial_vla_only_seed45.json\\t1704\\t2026-05-24 17:05\\neval_spatial_crm_obs_only_norm0.05_seed45.json\\t1707\\t2026-05-24 17:06\\neval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed45.json\\t1903\\t2026-05-24 17:09\\neval_spatial_vla_only_seed46.json\\t1707\\t2026-05-24 17:10\\neval_spatial_crm_obs_only_norm0.05_seed46.json\\t1709\\t2026-05-24 17:30\\neval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed49.json\\t1903\\t2026-05-25 01:58\\neval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed48.json\\t1905\\t2026-05-25 02:00\\neval_spatial_crm_obs_only_norm0.05_seed49.json\\t1709\\t2026-05-25 06:33\\neval_spatial_crm_obs_on
…[truncated 156 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_canonical-data-protocol_20260524T224440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-24T22:54:53.173467+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-40593",
  "command": "find /root/acr-vla-conformal-refinement/logs -maxdepth 2 -name \"eval_spatial*\" -type f -printf \"%f\\t%s\\t%TY-%Tm-%Td %TH:%TM\\n\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_canonical-data-protocol_20260524T224440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-40593",
    "command": "find /root/acr-vla-conformal-refinement/logs -maxdepth 2 -name \"eval_spatial*\" -type f -printf \"%f\\t%s\\t%TY-%Tm-%Td %TH:%TM\\n\""
  }
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-24T22:54:53.173604+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"eval_spatial_obs_only_norm02_seed43.log\\t4246\\t2026-05-20 00:31\\neval_spatial_obs_only_norm02_seed44.log\\t4787\\t2026-05-20 04:28\\neval_spatial_obs_only_norm02_seed44.json\\t1696\\t2026-05-20 04:28\\neval_spatial_obs_only_norm02_seed45.log\\t1283\\t2026-05-20 04:29\\neval_spatial_vla_only_seed44.json\\t1705\\t2026-05-23 23:14\\neval_spatial_k2mean_seed45.json\\t1702\\t2026-05-24 10:14\\neval_spatial_crm_obs_only_norm0.05_seed47.json\\t1709\\t2026-05-24 18:15\\neval_spatial_reconvla_seed47.json\\t1703\\t2026-05-24 23:02\\neval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed42.json\\t1904\\t2026-05-25 05:04\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.09}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_canonical-data-protocol_20260524T224440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-24T22:54:53.173728+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-18228",
  "command": "find /root/acr-vla-conformal-refinement/logs -maxdepth 2 -name \"eval_spatial*\" -type f -printf \"%f\\t%s\\t%TY-%Tm-%Td %TH:%TM\\n\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_canonical-data-protocol_20260524T224440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-18228",
    "command": "find /root/acr-vla-conformal-refinement/logs -maxdepth 2 -name \"eval_spatial*\" -type f -printf \"%f\\t%s\\t%TY-%Tm-%Td %TH:%TM\\n\""
  }
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-24T22:54:53.173848+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-32758",
  "command": "find /root/acr-vla-conformal-refinement/logs -maxdepth 2 -name \"eval_spatial*\" -type f -printf \"%f\\t%s\\t%TY-%Tm-%Td %TH:%TM\\n\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_canonical-data-protocol_20260524T224440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-32758",
    "command": "find /root/acr-vla-conformal-refinement/logs -maxdepth 2 -name \"eval_spatial*\" -type f -printf \"%f\\t%s\\t%TY-%Tm-%Td %TH:%TM\\n\""
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-24T22:54:53.173978+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"eval_spatial_vla_only_seed43.json\\t1692\\t2026-05-19 22:38\\neval_spatial_obs_only_norm02_seed47.json\\t1696\\t2026-05-20 11:00\\neval_spatial_vla_only_seed50.json\\t1691\\t2026-05-20 11:21\\neval_spatial_obs_only_norm02_seed51.json\\t1698\\t2026-05-20 12:41\\neval_spatial_vla_only_seed52.json\\t1693\\t2026-05-20 15:18\\neval_spatial_vla_only_seed53.json\\t1693\\t2026-05-20 15:21\\neval_spatial_vla_only_pi05_seed44.json\\t1704\\t2026-05-22 20:17\\neval_spatial_vla_only_pi05_seed42.json\\t1704\\t2026-05-22 20:17\\neval_spatial_vla_only_pi05_seed43.json\\t1704\\t2026-05-22 20:18\\neval_spatial_vla_only_seed42.json\\t1704\\t2026-05-25 02:20\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.84}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_canonical-data-protocol_20260524T224440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-24T22:54:53.174119+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"eval_spatial_obs_only_norm02_seed43.log\\t4246\\t2026-05-23 15:26\\neval_spatial_obs_only_norm02_seed44.log\\t4787\\t2026-05-23 15:26\\neval_spatial_obs_only_norm02_seed44.json\\t1696\\t2026-05-23 15:26\\neval_spatial_obs_only_norm02_seed45.log\\t1283\\t2026-05-23 15:26\\neval_spatial_reconvla_seed43.json\\t1705\\t2026-05-23 19:18\\neval_spatial_reconvla_seed44.json\\t1705\\t2026-05-23 19:21\\neval_spatial_vla_only_seed44.json\\t1703\\t2026-05-23 22:22\\neval_spatial_vla_only_seed43.json\\t1707\\t2026-05-23 22:34\\neval_spatial_reconvla_seed45.json\\t1705\\t2026-05-24 08:14\\neval_spatial_crm_obs_only_norm0.05_seed45.json\\t1707\\t2026-05-24 08:24\\neval_spatial_vla_only_seed45.json\\t1705\\t2026-05-24 08:27\\neval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed45.json\\t1904\\t2026-05-24 09:14\\neval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed46.json\\t1903\\t2026-05-24 10:38\\neval_spatial_crm_obs_only_norm0.05_seed46.json\\t1709\\t2026-05-24 10:59\\neval_spatial_reconvla_seed46.json\\t1704\\t2026-05-24 11:01\\neval_spatial_vla_only_seed46.json\\t1705\\t2026-05-24 11:09\\neval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed47.json\\t1903\\t2026-05-24 18:05\\neval_spatial_vla_only_seed47.json\\t1703\\t2026-05-24 21:22\\neval_spatial_reconvla_seed47.json\\t1705\\t2026-05-24 18:07\\neval_spatial_adaptive_conformal_crm_tau0.25_seed47.json\\t1905\\t2026-05-24 21:26\\neval_spatial_vla_only_seed48.json\\t1707\\t2026-05-25 02:31\\neval_spatial_vla_only_seed49.json\\t1707\\t2026-05-25 02:40\\neval_spatial_vla_only_seed42.json\\t1707\\t2026-05-25 06:27\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.77}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_canonical-data-protocol_20260524T224440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 54 · 2026-05-24T22:54:53.174307+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-32758",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed45.json /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed46.json /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed47.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed45.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed46.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed47.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed48.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed49.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed42.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed43.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed44.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_canonical-data-protocol_20260524T224440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-32758",
    "command": "cat /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed45.json /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed46.json /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed47.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed45.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed46.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed47.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed48.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed49.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed42.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed43.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed44.json"
  }
}
```

</details>

---

### Tool result

_source line 55 · 2026-05-24T22:54:53.174650+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"adaptive_conformal_crm\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"spatial\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.8,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.75,\\n      \\\"successes\\\": 15,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.8,\\n      \\\"successes\\\": 16,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.8,\\n      \\\"successes\\\": 16,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pic
…[truncated 8148 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_canonical-data-protocol_20260524T224440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 56 · 2026-05-24T22:54:53.174815+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed45.json /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed48.json /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed49.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed45.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed46.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed42.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed43.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed44.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_canonical-data-protocol_20260524T224440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "cat /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed45.json /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed48.json /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed49.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed45.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed46.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed42.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed43.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed44.json"
  }
}
```

</details>

---

### Tool result

_source line 57 · 2026-05-24T22:54:53.175141+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"adaptive_conformal_crm\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"spatial\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.8,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.75,\\n      \\\"successes\\\": 15,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.75,\\n      \\\"successes\\\": 15,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.8,\\n      \\\"successes\\\": 16,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pic
…[truncated 8147 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_canonical-data-protocol_20260524T224440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 58 · 2026-05-24T22:54:53.175326+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed42.json /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed43.json /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed44.json /root/acr-vla-conformal-refinement/logs/eval_spatial_k2mean_seed46.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_canonical-data-protocol_20260524T224440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "cat /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed42.json /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed43.json /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed44.json /root/acr-vla-conformal-refinement/logs/eval_spatial_k2mean_seed46.json"
  }
}
```

</details>

---

### Tool result

_source line 59 · 2026-05-24T22:54:53.175596+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"adaptive_conformal_crm\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"spatial\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.795,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.65,\\n      \\\"successes\\\": 13,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.8,\\n      \\\"successes\\\": 16,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.8,\\n      \\\"successes\\\": 16,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pi
…[truncated 7365 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_canonical-data-protocol_20260524T224440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 60 · 2026-05-24T22:54:53.175756+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-40593",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed42.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed44.json /root/acr-vla-conformal-refinement/logs/eval_spatial_k2mean_seed45.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_canonical-data-protocol_20260524T224440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-40593",
    "command": "cat /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed42.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed44.json /root/acr-vla-conformal-refinement/logs/eval_spatial_k2mean_seed45.json"
  }
}
```

</details>

---

### Tool result

_source line 61 · 2026-05-24T22:54:53.175982+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"adaptive_conformal_crm\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"spatial\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.79,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 18,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.65,\\n      \\\"successes\\\": 13,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.8,\\n      \\\"successes\\\": 16,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.85,\\n      \\\"successes\\\": 17,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pi
…[truncated 4751 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_canonical-data-protocol_20260524T224440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 62 · 2026-05-24T22:54:53.176177+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Read registry for all spatial experiments', 'activeForm': 'Reading registry for spatial experiments', 'status': 'completed'}, {'content': 'SSH each server to extract structured metadata from JSON files', 'activeForm': 'SSH each server to extract structured metadata', 'status': 'in_progress'}, {'content': 'Build audit matrix and canonical pairs', 'activeForm': 'Building audit matrix and canonical pairs', 'status': 'pending'}, {'content': 'Compute final p-values from canonical pairs', 'activeForm': 'Computing final p-values from canonical pairs', 'status': 'pending'}, {'content': 'Report audit matrix + yaml + p-values + gaps', 'activeForm': 'Reporting audit matrix + yaml + p-values + gaps', 'status': 'pending'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_canonical-data-protocol_20260524T224440",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Read registry for all spatial experiments', 'activeForm': 'Reading registry for spatial experiments', 'status': 'completed'}, {'content': 'SSH each server to extract structured metadata from JSON files', 'activeForm': 'SSH each server to extract structured metadata', 'status': 'in_progress'}, {'content': 'Build audit matrix and canonical pairs', 'activeForm': 'Building audit matrix and canonical pairs', 'status': 'pending'}, {'content': 'Compute final p-values from canonical pairs', 'activeForm': 'Computing final p-values from canonical pairs', 'status': 'pending'}, {'content': 'Report audit matrix + yaml + p-values + gaps', 'activeForm': 'Reporting audit matrix + yaml + p-values + gaps', 'status': 'pending'}]"
  }
}
```

</details>

---

### Tool result

_source line 63 · 2026-05-24T22:54:53.176432+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_canonical-data-protocol_20260524T224440",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 64 · 2026-05-24T22:54:53.176577+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "python3 -c \"import json,glob,os; [print(os.path.basename(f), '|', json.load(open(f)).get('mode'), '|', json.load(open(f)).get('baseline_mode'), '|', 'K=', json.load(open(f)).get('K'), '|', 'n_rollouts=', json.load(open(f)).get('n_rollouts'), '|', 'SR=', json.load(open(f)).get('overall_success_rate'), '|', 'tau=', (json.load(open(f)).get('adaptive_stats') or {}).get('tau')) for f in sorted(glob.glob('/root/acr-vla-conformal-refinement/logs/eval_spatial*.json'))]\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_canonical-data-protocol_20260524T224440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "python3 -c \"import json,glob,os; [print(os.path.basename(f), '|', json.load(open(f)).get('mode'), '|', json.load(open(f)).get('baseline_mode'), '|', 'K=', json.load(open(f)).get('K'), '|', 'n_rollouts=', json.load(open(f)).get('n_rollouts'), '|', 'SR=', json.load(open(f)).get('overall_success_rate'), '|', 'tau=', (json.load(open(f)).get('adaptive_stats') or {}).get('tau')) for f in sorted(glob.glob('/root/acr-vla-conformal-refinement/logs/eval_spatial*.json'))]\""
  }
}
```

</details>

---

### Tool result

_source line 65 · 2026-05-24T22:54:53.176710+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_canonical-data-protocol_20260524T224440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 66 · 2026-05-24T22:54:53.176835+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "python3 -c \"import json,glob,os; [print(os.path.basename(f), '|', json.load(open(f)).get('mode'), '|', json.load(open(f)).get('baseline_mode'), '|', 'K=', json.load(open(f)).get('K'), '|', 'n_rollouts=', json.load(open(f)).get('n_rollouts'), '|', 'SR=', json.load(open(f)).get('overall_success_rate'), '|', 'tau=', (json.load(open(f)).get('adaptive_stats') or {}).get('tau')) for f in sorted(glob.glob('/root/acr-vla-conformal-refinement/logs/eval_spatial*.json'))]\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_canonical-data-protocol_20260524T224440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "python3 -c \"import json,glob,os; [print(os.path.basename(f), '|', json.load(open(f)).get('mode'), '|', json.load(open(f)).get('baseline_mode'), '|', 'K=', json.load(open(f)).get('K'), '|', 'n_rollouts=', json.load(open(f)).get('n_rollouts'), '|', 'SR=', json.load(open(f)).get('overall_success_rate'), '|', 'tau=', (json.load(open(f)).get('adaptive_stats') or {}).get('tau')) for f in sorted(glob.glob('/root/acr-vla-conformal-refinement/logs/eval_spatial*.json'))]\""
  }
}
```

</details>

---

### Tool result

_source line 67 · 2026-05-24T22:54:53.176965+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_canonical-data-protocol_20260524T224440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 68 · 2026-05-24T22:54:53.177116+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-40593",
  "command": "python3 -c \"import json,glob,os; [print(os.path.basename(f), '|', json.load(open(f)).get('mode'), '|', json.load(open(f)).get('baseline_mode'), '|', 'K=', json.load(open(f)).get('K'), '|', 'n_rollouts=', json.load(open(f)).get('n_rollouts'), '|', 'SR=', json.load(open(f)).get('overall_success_rate'), '|', 'tau=', (json.load(open(f)).get('adaptive_stats') or {}).get('tau')) for f in sorted(glob.glob('/root/acr-vla-conformal-refinement/logs/eval_spatial*.json'))]\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_canonical-data-protocol_20260524T224440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-40593",
    "command": "python3 -c \"import json,glob,os; [print(os.path.basename(f), '|', json.load(open(f)).get('mode'), '|', json.load(open(f)).get('baseline_mode'), '|', 'K=', json.load(open(f)).get('K'), '|', 'n_rollouts=', json.load(open(f)).get('n_rollouts'), '|', 'SR=', json.load(open(f)).get('overall_success_rate'), '|', 'tau=', (json.load(open(f)).get('adaptive_stats') or {}).get('tau')) for f in sorted(glob.glob('/root/acr-vla-conformal-refinement/logs/eval_spatial*.json'))]\""
  }
}
```

</details>

---

### Tool result

_source line 69 · 2026-05-24T22:54:53.177322+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_canonical-data-protocol_20260524T224440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 70 · 2026-05-24T22:54:53.177467+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-18228",
  "command": "python3 -c \"import json,glob,os; [print(os.path.basename(f), '|', json.load(open(f)).get('mode'), '|', json.load(open(f)).get('baseline_mode'), '|', 'K=', json.load(open(f)).get('K'), '|', 'n_rollouts=', json.load(open(f)).get('n_rollouts'), '|', 'SR=', json.load(open(f)).get('overall_success_rate'), '|', 'tau=', (json.load(open(f)).get('adaptive_stats') or {}).get('tau')) for f in sorted(glob.glob('/root/acr-vla-conformal-refinement/logs/eval_spatial*.json'))]\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_canonical-data-protocol_20260524T224440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-18228",
    "command": "python3 -c \"import json,glob,os; [print(os.path.basename(f), '|', json.load(open(f)).get('mode'), '|', json.load(open(f)).get('baseline_mode'), '|', 'K=', json.load(open(f)).get('K'), '|', 'n_rollouts=', json.load(open(f)).get('n_rollouts'), '|', 'SR=', json.load(open(f)).get('overall_success_rate'), '|', 'tau=', (json.load(open(f)).get('adaptive_stats') or {}).get('tau')) for f in sorted(glob.glob('/root/acr-vla-conformal-refinement/logs/eval_spatial*.json'))]\""
  }
}
```

</details>

---

### Tool result

_source line 71 · 2026-05-24T22:54:53.177594+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_canonical-data-protocol_20260524T224440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 72 · 2026-05-24T22:54:53.177721+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-32758",
  "command": "python3 -c \"import json,glob,os; [print(os.path.basename(f), '|', json.load(open(f)).get('mode'), '|', json.load(open(f)).get('baseline_mode'), '|', 'K=', json.load(open(f)).get('K'), '|', 'n_rollouts=', json.load(open(f)).get('n_rollouts'), '|', 'SR=', json.load(open(f)).get('overall_success_rate'), '|', 'tau=', (json.load(open(f)).get('adaptive_stats') or {}).get('tau')) for f in sorted(glob.glob('/root/acr-vla-conformal-refinement/logs/eval_spatial*.json'))]\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_canonical-data-protocol_20260524T224440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-32758",
    "command": "python3 -c \"import json,glob,os; [print(os.path.basename(f), '|', json.load(open(f)).get('mode'), '|', json.load(open(f)).get('baseline_mode'), '|', 'K=', json.load(open(f)).get('K'), '|', 'n_rollouts=', json.load(open(f)).get('n_rollouts'), '|', 'SR=', json.load(open(f)).get('overall_success_rate'), '|', 'tau=', (json.load(open(f)).get('adaptive_stats') or {}).get('tau')) for f in sorted(glob.glob('/root/acr-vla-conformal-refinement/logs/eval_spatial*.json'))]\""
  }
}
```

</details>

---

### Tool result

_source line 73 · 2026-05-24T22:54:53.177886+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_canonical-data-protocol_20260524T224440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 74 · 2026-05-24T22:54:53.178026+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "grep -H -E \"\\\"(mode|baseline_mode|K|n_rollouts|overall_success_rate|tau|trigger_rate)\\\"\" /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed42.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed45.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed46.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed47.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed48.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed49.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed51.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed54.json /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed42.json /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed43.json /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed44.json /root/acr-vla-conformal-refinement/logs/eval_spatial_k2mean_seed46.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_canonical-data-protocol_20260524T224440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "grep -H -E \"\\\"(mode|baseline_mode|K|n_rollouts|overall_success_rate|tau|trigger_rate)\\\"\" /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed42.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed45.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed46.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed47.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed48.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed49.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed51.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed54.json /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed42.json /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed43.json /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed44.json /root/acr-vla-conformal-refinement/logs/eval_spatial_k2mean_seed46.json"
  }
}
```

</details>

---

### Tool result

_source line 75 · 2026-05-24T22:54:53.178159+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_canonical-data-protocol_20260524T224440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 76 · 2026-05-24T22:54:53.178309+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "grep -H -E \"\\\"(mode|baseline_mode|K|n_rollouts|overall_success_rate|tau|trigger_rate)\\\"\" /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed42.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed43.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed44.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed45.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed46.json /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed45.json /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed48.json /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed49.json /root/acr-vla-conformal-refinement/logs/eval_spatial_k2mean_seed45.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_canonical-data-protocol_20260524T224440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "grep -H -E \"\\\"(mode|baseline_mode|K|n_rollouts|overall_success_rate|tau|trigger_rate)\\\"\" /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed42.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed43.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed44.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed45.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed46.json /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed45.json /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed48.json /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed49.json /root/acr-vla-conformal-refinement/logs/eval_spatial_k2mean_seed45.json"
  }
}
```

</details>

---

### Tool result

_source line 77 · 2026-05-24T22:54:53.178478+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_canonical-data-protocol_20260524T224440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 78 · 2026-05-24T22:54:53.178601+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-40593",
  "command": "grep -H -E \"\\\"(mode|baseline_mode|K|n_rollouts|overall_success_rate|tau|trigger_rate)\\\"\" /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed44.json /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed42.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_canonical-data-protocol_20260524T224440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-40593",
    "command": "grep -H -E \"\\\"(mode|baseline_mode|K|n_rollouts|overall_success_rate|tau|trigger_rate)\\\"\" /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed44.json /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed42.json"
  }
}
```

</details>

---

### Tool result

_source line 79 · 2026-05-24T22:54:53.178720+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_canonical-data-protocol_20260524T224440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 80 · 2026-05-24T22:54:53.178837+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-18228",
  "command": "grep -H -E \"\\\"(mode|baseline_mode|K|n_rollouts|overall_success_rate|tau|trigger_rate)\\\"\" /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed42.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed43.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed50.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed52.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed53.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_canonical-data-protocol_20260524T224440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-18228",
    "command": "grep -H -E \"\\\"(mode|baseline_mode|K|n_rollouts|overall_success_rate|tau|trigger_rate)\\\"\" /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed42.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed43.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed50.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed52.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed53.json"
  }
}
```

</details>

---

### Tool result

_source line 81 · 2026-05-24T22:54:53.178962+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_canonical-data-protocol_20260524T224440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 82 · 2026-05-24T22:54:53.179081+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-32758",
  "command": "grep -H -E \"\\\"(mode|baseline_mode|K|n_rollouts|overall_success_rate|tau|trigger_rate)\\\"\" /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed42.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed43.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed44.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed45.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed46.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed47.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed48.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed49.json /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed45.json /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed46.json /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed47.json /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_tau0.25_seed47.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_canonical-data-protocol_20260524T224440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-32758",
    "command": "grep -H -E \"\\\"(mode|baseline_mode|K|n_rollouts|overall_success_rate|tau|trigger_rate)\\\"\" /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed42.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed43.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed44.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed45.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed46.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed47.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed48.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed49.json /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed45.json /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed46.json /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed47.json /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_tau0.25_seed47.json"
  }
}
```

</details>

---

### Tool result

_source line 83 · 2026-05-24T22:54:53.179201+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_canonical-data-protocol_20260524T224440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 84 · 2026-05-24T22:54:53.179353+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "grep -H -e \"\\\"mode\\\"\" -e \"\\\"baseline_mode\\\"\" -e \"\\\"K\\\":\" -e \"\\\"n_rollouts\\\"\" -e \"\\\"overall_success_rate\\\"\" -e \"\\\"tau\\\":\" -e \"\\\"trigger_rate\\\"\" /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed42.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed45.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed46.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed47.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed48.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed49.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed51.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed54.json /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed42.json /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed43.json /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed44.json /root/acr-vla-conformal-refinement/logs/eval_spatial_k2mean_seed46.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_canonical-data-protocol_20260524T224440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "grep -H -e \"\\\"mode\\\"\" -e \"\\\"baseline_mode\\\"\" -e \"\\\"K\\\":\" -e \"\\\"n_rollouts\\\"\" -e \"\\\"overall_success_rate\\\"\" -e \"\\\"tau\\\":\" -e \"\\\"trigger_rate\\\"\" /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed42.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed45.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed46.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed47.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed48.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed49.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed51.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed54.json /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed42.json /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed43.json /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed44.json /root/acr-vla-conformal-refinement/logs/eval_spatial_k2mean_seed46.json"
  }
}
```

</details>

---

### Tool result

_source line 85 · 2026-05-24T22:54:53.179567+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed42.json:  \\\"mode\\\": \\\"vla_only\\\",\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed42.json:  \\\"baseline_mode\\\": \\\"single\\\",\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed42.json:  \\\"n_rollouts\\\": 10,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed42.json:  \\\"overall_success_rate\\\": 0.3,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed45.json:  \\\"mode\\\": \\\"vla_only\\\",\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed45.json:  \\\"baseline_mode\\\": \\\"single\\\",\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed45.json:  \\\"n_rollouts\\\": 10,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed45.json:  \\\"overall_success_rate\\\": 0.27,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed46.json:  \\\"mode\\\": \\\"vla_only\\\",\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed46.json:  \\\"baseline_mode\\\": \\\"single\\\",\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed46.json:  \\\"n_rollouts\\\": 10,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed46.json:  \\\"overall_success_rate\\\": 0.3,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed47.json:  \\\"mode\\\": \\\"vla_only\\\",\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed47.json:  \\\"baseline_mode\\\": \\\"single\\\",\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed47.json:  \\\"n_rollouts\\\": 10,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed47.json:  \\\"overall_success_rate\\\": 0.3,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed48.json:  \\\"mode\\\": \\\"vla_only\\\",\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_see
…[truncated 4709 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_canonical-data-protocol_20260524T224440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 86 · 2026-05-24T22:54:53.179721+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "grep -H -e \"\\\"mode\\\"\" -e \"\\\"baseline_mode\\\"\" -e \"\\\"K\\\":\" -e \"\\\"n_rollouts\\\"\" -e \"\\\"overall_success_rate\\\"\" -e \"\\\"tau\\\":\" -e \"\\\"trigger_rate\\\"\" /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed42.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed43.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed44.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed45.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed46.json /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed45.json /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed48.json /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed49.json /root/acr-vla-conformal-refinement/logs/eval_spatial_k2mean_seed45.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_canonical-data-protocol_20260524T224440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "grep -H -e \"\\\"mode\\\"\" -e \"\\\"baseline_mode\\\"\" -e \"\\\"K\\\":\" -e \"\\\"n_rollouts\\\"\" -e \"\\\"overall_success_rate\\\"\" -e \"\\\"tau\\\":\" -e \"\\\"trigger_rate\\\"\" /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed42.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed43.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed44.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed45.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed46.json /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed45.json /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed48.json /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed49.json /root/acr-vla-conformal-refinement/logs/eval_spatial_k2mean_seed45.json"
  }
}
```

</details>

---

### Tool result

_source line 87 · 2026-05-24T22:54:53.179900+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed42.json:  \\\"mode\\\": \\\"vla_only\\\",\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed42.json:  \\\"baseline_mode\\\": \\\"mean\\\",\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed42.json:  \\\"n_rollouts\\\": 20,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed42.json:  \\\"overall_success_rate\\\": 0.815,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed43.json:  \\\"mode\\\": \\\"vla_only\\\",\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed43.json:  \\\"baseline_mode\\\": \\\"single\\\",\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed43.json:  \\\"n_rollouts\\\": 20,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed43.json:  \\\"overall_success_rate\\\": 0.805,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed44.json:  \\\"mode\\\": \\\"vla_only\\\",\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed44.json:  \\\"baseline_mode\\\": \\\"single\\\",\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed44.json:  \\\"n_rollouts\\\": 20,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed44.json:  \\\"overall_success_rate\\\": 0.805,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed45.json:  \\\"mode\\\": \\\"vla_only\\\",\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed45.json:  \\\"baseline_mode\\\": \\\"single\\\",\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed45.json:  \\\"n_rollouts\\\": 20,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed45.json:  \\\"overall_success_rate\\\": 0.8,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed46.json:  \\\"mode\\\": \\\"vla_only\\\",\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only
…[truncated 3070 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_canonical-data-protocol_20260524T224440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 88 · 2026-05-24T22:54:53.180052+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-40593",
  "command": "grep -H -e \"\\\"mode\\\"\" -e \"\\\"baseline_mode\\\"\" -e \"\\\"K\\\":\" -e \"\\\"n_rollouts\\\"\" -e \"\\\"overall_success_rate\\\"\" -e \"\\\"tau\\\":\" -e \"\\\"trigger_rate\\\"\" /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed44.json /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed42.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_canonical-data-protocol_20260524T224440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-40593",
    "command": "grep -H -e \"\\\"mode\\\"\" -e \"\\\"baseline_mode\\\"\" -e \"\\\"K\\\":\" -e \"\\\"n_rollouts\\\"\" -e \"\\\"overall_success_rate\\\"\" -e \"\\\"tau\\\":\" -e \"\\\"trigger_rate\\\"\" /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed44.json /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed42.json"
  }
}
```

</details>

---

### Tool result

_source line 89 · 2026-05-24T22:54:53.180197+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed44.json:  \\\"mode\\\": \\\"vla_only\\\",\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed44.json:  \\\"baseline_mode\\\": \\\"single\\\",\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed44.json:  \\\"n_rollouts\\\": 20,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed44.json:  \\\"overall_success_rate\\\": 0.785,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed42.json:  \\\"mode\\\": \\\"adaptive_conformal_crm\\\",\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed42.json:  \\\"baseline_mode\\\": \\\"single\\\",\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed42.json:  \\\"n_rollouts\\\": 20,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed42.json:  \\\"overall_success_rate\\\": 0.79,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed42.json:    \\\"trigger_rate\\\": 0.1936721666027139,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed42.json:    \\\"tau\\\": 0.25,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.31}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_canonical-data-protocol_20260524T224440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 90 · 2026-05-24T22:54:53.180401+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-18228",
  "command": "grep -H -e \"\\\"mode\\\"\" -e \"\\\"baseline_mode\\\"\" -e \"\\\"K\\\":\" -e \"\\\"n_rollouts\\\"\" -e \"\\\"overall_success_rate\\\"\" -e \"\\\"tau\\\":\" -e \"\\\"trigger_rate\\\"\" /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed42.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed43.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed50.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed52.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed53.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_canonical-data-protocol_20260524T224440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-18228",
    "command": "grep -H -e \"\\\"mode\\\"\" -e \"\\\"baseline_mode\\\"\" -e \"\\\"K\\\":\" -e \"\\\"n_rollouts\\\"\" -e \"\\\"overall_success_rate\\\"\" -e \"\\\"tau\\\":\" -e \"\\\"trigger_rate\\\"\" /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed42.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed43.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed50.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed52.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed53.json"
  }
}
```

</details>

---

### Tool result

_source line 91 · 2026-05-24T22:54:53.180567+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed42.json:  \\\"mode\\\": \\\"vla_only\\\",\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed42.json:  \\\"baseline_mode\\\": \\\"single\\\",\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed42.json:  \\\"n_rollouts\\\": 20,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed42.json:  \\\"overall_success_rate\\\": 0.8,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed43.json:  \\\"mode\\\": \\\"vla_only\\\",\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed43.json:  \\\"baseline_mode\\\": \\\"single\\\",\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed43.json:  \\\"n_rollouts\\\": 10,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed43.json:  \\\"overall_success_rate\\\": 0.29,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed50.json:  \\\"mode\\\": \\\"vla_only\\\",\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed50.json:  \\\"baseline_mode\\\": \\\"single\\\",\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed50.json:  \\\"n_rollouts\\\": 10,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed50.json:  \\\"overall_success_rate\\\": 0.3,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed52.json:  \\\"mode\\\": \\\"vla_only\\\",\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed52.json:  \\\"baseline_mode\\\": \\\"single\\\",\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed52.json:  \\\"n_rollouts\\\": 10,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed52.json:  \\\"overall_success_rate\\\": 0.31,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed53.json:  \\\"mode\\\": \\\"vla_only\\\",\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_se
…[truncated 373 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_canonical-data-protocol_20260524T224440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 92 · 2026-05-24T22:54:53.180716+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-32758",
  "command": "grep -H -e \"\\\"mode\\\"\" -e \"\\\"baseline_mode\\\"\" -e \"\\\"K\\\":\" -e \"\\\"n_rollouts\\\"\" -e \"\\\"overall_success_rate\\\"\" -e \"\\\"tau\\\":\" -e \"\\\"trigger_rate\\\"\" /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed42.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed43.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed44.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed45.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed46.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed47.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed48.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed49.json /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed45.json /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed46.json /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed47.json /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_tau0.25_seed47.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_canonical-data-protocol_20260524T224440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-32758",
    "command": "grep -H -e \"\\\"mode\\\"\" -e \"\\\"baseline_mode\\\"\" -e \"\\\"K\\\":\" -e \"\\\"n_rollouts\\\"\" -e \"\\\"overall_success_rate\\\"\" -e \"\\\"tau\\\":\" -e \"\\\"trigger_rate\\\"\" /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed42.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed43.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed44.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed45.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed46.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed47.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed48.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed49.json /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed45.json /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed46.json /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed47.json /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_tau0.25_seed47.json"
  }
}
```

</details>

---

### Tool result

_source line 93 · 2026-05-24T22:54:53.180921+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed42.json:  \\\"mode\\\": \\\"vla_only\\\",\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed42.json:  \\\"baseline_mode\\\": \\\"single\\\",\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed42.json:  \\\"n_rollouts\\\": 20,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed42.json:  \\\"overall_success_rate\\\": 0.785,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed43.json:  \\\"mode\\\": \\\"vla_only\\\",\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed43.json:  \\\"baseline_mode\\\": \\\"single\\\",\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed43.json:  \\\"n_rollouts\\\": 20,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed43.json:  \\\"overall_success_rate\\\": 0.79,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed44.json:  \\\"mode\\\": \\\"vla_only\\\",\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed44.json:  \\\"baseline_mode\\\": \\\"mean\\\",\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed44.json:  \\\"n_rollouts\\\": 20,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed44.json:  \\\"overall_success_rate\\\": 0.81,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed45.json:  \\\"mode\\\": \\\"vla_only\\\",\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed45.json:  \\\"baseline_mode\\\": \\\"single\\\",\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed45.json:  \\\"n_rollouts\\\": 20,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed45.json:  \\\"overall_success_rate\\\": 0.77,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed46.json:  \\\"mode\\\": \\\"vla_only\\\",\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_s
…[truncated 5091 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_canonical-data-protocol_20260524T224440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 94 · 2026-05-24T22:54:53.181151+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 << 'EOF'\nimport numpy as np\nfrom scipy import stats\n\n# Comprehensive data collected from all 5 servers\n# Format: (seed, server, mode_file, mode_actual, baseline_mode, n_rollouts, SR, K_or_tau, mtime, notes)\nall_files = [\n    # bjb1-32546\n    (42, 'bjb1-32546', 'vla_only', 'vla_only',           'single', 10, 0.30, None, '2026-05-19', 'old openvla'),\n    (45, 'bjb1-32546', 'vla_only', 'vla_only',           'single', 10, 0.27, None, '2026-05-19', 'old openvla'),\n    (46, 'bjb1-32546', 'vla_only', 'vla_only',           'single', 10, 0.30, None, '2026-05-20', 'old openvla'),\n    (47, 'bjb1-32546', 'vla_only', 'vla_only',           'single', 10, 0.30, None, '2026-05-20', 'old openvla'),\n    (48, 'bjb1-32546', 'vla_only', 'vla_only',           'single', 10, 0.30, None, '2026-05-20', 'old openvla'),\n    (49, 'bjb1-32546', 'vla_only', 'vla_only',           'single', 10, 0.29, None, '2026-05-20', 'old openvla'),\n    (51, 'bjb1-32546', 'vla_only', 'vla_only',           'single', 10, 0.33, None, '2026-05-20', 'old openvla'),\n    (54, 'bjb1-32546', 'vla_only', 'vla_only',           'single', 10, 0.27, None, '2026-05-20', 'old openvla'),\n    (42, 'bjb1-32546', 'adaptive_conformal_crm', 'adapt','single', 20, 0.795, 0.25, '2026-05-25', 'new smolvla'),\n    (43, 'bjb1-32546', 'adaptive_conformal_crm', 'adapt','single', 20, 0.80,  0.25, '2026-05-23', 'new smolvla'),\n    (44, 'bjb1-32546', 'adaptive_conformal_crm', 'adapt','single', 20, 0.805, 0.25, '2026-05-23', 'new smolvla'),\n    (46, 'bjb1-32546', 'k2mean (vla_only mean)', 'vla_mean_K2', 'mean', 20, 0.80, None, '2026-05-24', 'K=2 mean baseline'),\n\n    # bjb2-28827\n    (42, 'bjb2-28827', 'vla_only', 'vla_mean_K2',        'mean',   20, 0.815, None, '2026-05-23', 'K=2 anomaly (file misnamed)'),\n    (43, 'bjb2-28827', 'vla_only', 'vla_only',           'single', 20, 0.805, None, '2026-05-23', 'new smolvla'),\n    (44, 'bjb2-28827', 'vla_only', 'vla_only',           'single', 20, 0.805, None, '2026-05-23', 'new smolvla'),\n    (45, 'bjb2-28827', 'vla_only', 'vla_only',           'single', 20, 0.80,  None, '2026-05-24', 'new smolvla'),\n    (46, 'bjb2-28827', 'vla_only', 'vla_only',           'single', 20, 0.805, None, '2026-05-24', 'new smolvla'),\n    (45, 'bjb2-28827', 'adaptive_conformal_crm', 'adapt','single', 20, 0.80,  0.25, '2026-05-24', 'new smolvla'),\n    (48, 'bjb2-28827', 'adaptive_conformal_crm', 'adapt','single', 20, 0.81,  0.25, '2026-05-25', 'new smolvla'),\n    (49, 'bjb2-28827', 'adaptive_conformal_crm', 'adapt','single', 20, 0.82,  0.25, '2026-05-25', 'new smolvla'),\n\n    # bjb2-40593\n    (44, 'bjb2-40593', 'vla_only', 'vla_only',           'single', 20, 0.785, None, '2026-05-23', 'new smolvla'),\n    (42, 'bjb2-40593', 'adaptive_conformal_crm', 'adapt','single', 20, 0.79,  0.25, '2026-05-25', 'new smolvla'),\n\n    # bjb1-18228\n    (42, 'bjb1-18228', 'vla_only', 'vla_only',           'single', 20, 0.80,  None, '2026-05-25', 'new smolvla'),\n    (43, 'bjb1-18228', 'vla_only', 'vla_only',           'single', 10, 0.29,  None, '2026-05-19', 'old openvla'),\n    (50, 'bjb1-18228', 'vla_only', 'vla_only',           'single', 10, 0.30,  None, '2026-05-20', 'old openvla'),\n    (52, 'bjb1-18228', 'vla_only', 'vla_only',           'single', 10, 0.31,  None, '2026-05-20', 'old openvla'),\n    (53, 'bjb1-18228', 'vla_only', 'vla_only',           'single', 10, 0.28,  None, '2026-05-20', 'old openvla'),\n\n    # cqa1-32758\n    (42, 'cqa1-32758', 'vla_only', 'vla_only',           'single', 20, 0.785, None, '2026-05-25', 'new smolvla'),\n    (43, 'cqa1-32758', 'vla_only', 'vla_only',           'single', 20, 0.79,  None, '2026-05-23', 'new smolvla'),\n    (44, 'cqa1-32758', 'vla_only', 'vla_mean_K2',        'mean',   20, 0.81,  None, '2026-05-23', 'K=2 anomaly (file misnamed)'),\n    (45, 'cqa1-32758', 'vla_only', 'vla_only',           'single', 20, 0.77,  None, '2026-05-24', 'new smolvla'),\n    (46, 'cqa1-32758', 'vla_only', 'vla_only',           'single', 20, 0.805, None, '2026-05-24', 'new smolvla'),\n    (47, 'cqa1-32758', 'vla_only', 'vla_only',           'single', 20, 0.81,  None, '2026-05-24', 'new smolvla'),\n    (48, 'cqa1-32758', 'vla_only', 'vla_only',           'single', 20, 0.795, None, '2026-05-25', 'new smolvla'),\n    (49, 'cqa1-32758', 'vla_only', 'vla_only',           'single', 20, 0.785, None, '2026-05-25', 'new smolvla'),\n    (45, 'cqa1-32758', 'adaptive_conformal_crm', 'adapt','single', 20, 0.80,  0.25, '2026-05-24', 'new smolvla'),\n    (46, 'cqa1-32758', 'adaptive_conformal_crm', 'adapt','single', 20, 0.80,  0.25, '2026-05-24', 'new smolvla'),\n    (47, 'cqa1-32758', 'adaptive_conformal_crm', 'adapt','single', 20, 0.815, 0.25, '2026-05-24', 'new smolvla'),\n    (47, 'cqa1-32758', 'adaptive_conformal_crm', 'adapt','single', 20, 0.79,  0.25, '2026-05-24', 'duplicate (tau0.25 no-norm filename)'),\n]\n\nprint(\"=\" * 110)\nprint(\"AUDIT MATRIX: Spatial Experiments (all servers, all files)\")\nprint(\"=\" * 110)\nprint(f\"{'seed':<4} | {'server':<11} | {'mode_actual':<14} | {'baseline':<7} | {'n_roll':<6} | {'SR':<6} | {'tau':<5} | {'date':<10} | {'notes':<35}\")\nprint(\"-\" * 110)\nfor row in sorted(all_files, key=lambda x: (x[0], x[1], x[3])):\n    seed, server, file_label, mode_actual, baseline, n, sr, tau, mtime, notes = row\n    tau_s = str(tau) if tau else '-'\n    print(f\"{seed:<4} | {server:<11} | {mode_actual:<14} | {baseline:<7} | {n:<6} | {sr:<6} | {tau_s:<5} | {mtime:<10} | {notes:<35}\")\n\n# ============================\n# Build canonical pairs\n# ============================\nprint(\"\\n\\n\" + \"=\" * 110)\nprint(\"CANONICAL PAIR ANALYSIS — same-server, n_rollouts=20, baseline_mode=single\")\nprint(\"=\" * 110)\n\n# Filter to new-smolvla family (n=20, single)\nnew_vla = {}\nnew_adapt = {}\nfor row in all_files:\n    seed, server, _, mode_actual, baseline, n, sr, tau, mtime, notes = row\n    if n != 20 or baseline != 'single':\n        continue\n    if mode_actual == 'vla_only':\n        new_vla[(seed, server)] = sr\n    elif mode_actual == 'adapt' and tau == 0.25:\n        # take the canonical norm0.2 version, NOT the duplicate\n        # for s47 on cqa1-32758, there's a duplicate; we keep the first (0.815)\n        if (seed, server) not in new_adapt:\n            new_adapt[(seed, server)] = sr\n\nprint(\"\\nVLA-only available (n=20, single):\", {k: v for k,v in sorted(new_vla.items())})\nprint(\"Adaptive available  (n=20, single, tau=0.25):\", {k: v for k,v in sorted(new_adapt.items())})\n\n# Find same-server pairs by intersection on (seed, server)\nprint(\"\\n--- Same-server pairs ---\")\npair_keys = sorted(set(new_vla.keys()) & set(new_adapt.keys()))\nprint(f\"{'seed':<4} | {'server':<11} | {'VLA':<6} | {'Adapt':<6} | {'Δ (pp)':<8}\")\nprint(\"-\" * 50)\ndeltas = []\nfor k in pair_keys:\n    v = new_vla[k]\n    a = new_adapt[k]\n    d = (a - v) * 100\n    print(f\"{k[0]:<4} | {k[1]:<11} | {v:<6} | {a:<6} | {d:+.2f}\")\n    deltas.append(d)\n\n# If multiple servers have data for same seed, prefer one server (cqa1-32758)\n# Build unique-seed pairs\nprint(\"\\n--- Unique seed pairs (preferring cqa1-32758) ---\")\nseen_seeds = {}\npriority = ['cqa1-32758', 'bjb2-28827', 'bjb1-32546', 'bjb2-40593', 'bjb1-18228']\nfor k in sorted(pair_keys, key=lambda x: (x[0], priority.index(x[1]))):\n    if k[0] not in seen_seeds:\n        seen_seeds[k[0]] = k\n\nprint(f\"{'seed':<4} | {'server':<11} | {'VLA':<6} | {'Adapt':<6} | {'Δ (pp)':<8}\")\nprint(\"-\" * 50)\nunique_deltas = []\nunique_pairs = []\nfor seed in sorted(seen_seeds):\n    k = seen_seeds[seed]\n    v = new_vla[k]\n    a = new_adapt[k]\n    d = (a - v) * 100\n    print(f\"{seed:<4} | {k[1]:<11} | {v:<6} | {a:<6} | {d:+.2f}\")\n    unique_deltas.append(d)\n    unique_pairs.append((seed, k[1], v, a, d))\n\n# ============================\n# Statistics\n# ============================\nprint(\"\\n--- Paired statistics (canonical pairs, same-server only) ---\")\ndeltas_arr = np.array(unique_deltas)\nn = len(deltas_arr)\nmean_d = deltas_arr.mean()\nsd_d = deltas_arr.std(ddof=1) if n > 1 else 0\nsem_d = sd_d / np.sqrt(n) if n > 1 else 0\nprint(f\"n = {n}\")\nprint(f\"Mean Δ = {mean_d:+.3f} pp\")\nif n > 1:\n    print(f\"SD Δ   = {sd_d:.3f} pp\")\n    print(f\"SEM Δ  = {sem_d:.3f} pp\")\n    ci95 = stats.t.ppf(0.975, n-1) * sem_d\n    print(f\"95% CI = [{mean_d - ci95:+.3f}, {mean_d + ci95:+.3f}] pp\")\n    t_stat, p_val = stats.ttest_1samp(deltas_arr, 0.0)\n    print(f\"\\nPaired t-test (one-sample on Δ):  t={t_stat:.3f},  df={n-1},  p={p_val:.4f}\")\n    if n >= 6:\n        w_stat, w_p = stats.wilcoxon(deltas_arr)\n        print(f\"Wilcoxon signed-rank:             W={w_stat:.3f},  p={w_p:.4f}\")\n    else:\n        print(\"Wilcoxon: n<6, results unreliable\")\n\n# ============================\n# Comparison with previous \"8-seed\" analysis (mixed servers)\n# ============================\nprint(\"\\n\\n\" + \"=\" * 110)\nprint(\"FOR REFERENCE — what spatial_per_task_breakdown.md previously used (cross-server allowed):\")\nprint(\"=\" * 110)\n# from breakdown md\nprev = [\n    (42, 'cqa1-32758', 'bjb1-32546', 0.785, 0.795),  # vla cqa, adapt bjb1\n    (43, 'cqa1-32758', 'bjb1-32546', 0.79,  0.80),\n    (44, 'bjb2-40593', 'bjb1-32546', 0.785, 0.805),\n    (45, 'cqa1-32758', 'cqa1-32758', 0.77,  0.80),   # same\n    (46, 'cqa1-32758', 'cqa1-32758', 0.805, 0.80),   # same\n    (47, 'cqa1-32758', 'cqa1-32758', 0.81,  0.815),  # same\n    (48, 'cqa1-32758', 'bjb2-28827', 0.795, 0.81),\n    (49, 'cqa1-32758', 'bjb2-28827', 0.785, 0.82),\n]\nprev_deltas = np.array([(a-v)*100 for s,vs,as_,v,a in prev])\nprev_n = len(prev_deltas)\nprev_t, prev_p = stats.ttest_1samp(prev_deltas, 0.0)\nprev_w, prev_wp = stats.wilcoxon(prev_deltas)\nprint(f\"\\n{'seed':<4} | {'VLA srv':<11} | {'Adapt srv':<11} | {'VLA':<6} | {'Adapt':<6} | {'Δ pp':<7} | same-srv\")\nprint(\"-\" * 75)\nfor s, vs, as_, v, a in prev:\n    print(f\"{s:<4} | {vs:<11} | {as_:<11} | {v:<6} | {a:<6} | {(a-v)*100:+.2f}  | {'YES' if vs==as_ else 'no'}\")\n\nprint(f\"\\nn={prev_n}, mean Δ={prev_deltas.mean():+.3f}pp, SD={prev_deltas.std(ddof=1):.3f}\")\nci95 = stats.t.ppf(0.975, prev_n-1) * prev_deltas.std(ddof=1)/np.sqrt(prev_n)\nprint(f\"95% CI = [{prev_deltas.mean()-ci95:+.3f}, {prev_deltas.mean()+ci95:+.3f}]\")\nprint(f\"Paired t-test (one-sample on Δ): t={prev_t:.3f}, df={prev_n-1}, p={prev_p:.4f}\")\nprint(f\"Wilcoxon signed-rank: W={prev_w:.3f}, p={prev_wp:.4f}\")\nEOF",
  "description": "Build audit matrix + canonical pairs + p-values"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_canonical-data-protocol_20260524T224440",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 << 'EOF'\nimport numpy as np\nfrom scipy import stats\n\n# Comprehensive data collected from all 5 servers\n# Format: (seed, server, mode_file, mode_actual, baseline_mode, n_rollouts, SR, K_or_tau, mtime, notes)\nall_files = [\n    # bjb1-32546\n    (42, 'bjb1-32546', 'vla_only', 'vla_only',           'single', 10, 0.30, None, '2026-05-19', 'old openvla'),\n    (45, 'bjb1-32546', 'vla_only', 'vla_only',           'single', 10, 0.27, None, '2026-05-19', 'old openvla'),\n    (46, 'bjb1-32546', 'vla_only', 'vla_only',           'single', 10, 0.30, None, '2026-05-20', 'old openvla'),\n    (47, 'bjb1-32546', 'vla_only', 'vla_only',           'single', 10, 0.30, None, '2026-05-20', 'old openvla'),\n    (48, 'bjb1-32546', 'vla_only', 'vla_only',           'single', 10, 0.30, None, '2026-05-20', 'old openvla'),\n    (49, 'bjb1-32546', 'vla_only', 'vla_only',           'single', 10, 0.29, None, '2026-05-20', 'old openvla'),\n    (51, 'bjb1-32546', 'vla_only', 'vla_only',           'single', 10, 0.33, None, '2026-05-20', 'old openvla'),\n    (54, 'bjb1-32546', 'vla_only', 'vla_only',           'single', 10, 0.27, None, '2026-05-20', 'old openvla'),\n    (42, 'bjb1-32546', 'adaptive_conformal_crm', 'adapt','single', 20, 0.795, 0.25, '2026-05-25', 'new smolvla'),\n    (43, 'bjb1-32546', 'adaptive_conformal_crm', 'adapt','single', 20, 0.80,  0.25, '2026-05-23', 'new smolvla'),\n    (44, 'bjb1-32546', 'adaptive_conformal_crm', 'adapt','single', 20, 0.805, 0.25, '2026-05-23', 'new smolvla'),\n    (46, 'bjb1-32546', 'k2mean (vla_only mean)', 'vla_mean_K2', 'mean', 20, 0.80, None, '2026-05-24', 'K=2 mean baseline'),\n\n    # bjb2-28827\n    (42, 'bjb2-28827', 'vla_only', 'vla_mean_K2',        'mean',   20, 0.815, None, '2026-05-23', 'K=2 anomaly (file misnamed)'),\n    (43, 'bjb2-28827', 'vla_only', 'vla_only',           'single', 20, 0.805, None, '2026-05-23', 'new smolvla'),\n    (44, 'bjb2-28827', 'vla_only', 'vla_only',           'single', 20, 0.805, None, '2026-05-23', 'new smolvla'),\n    (45, 'bjb2-28827', 'vla_only', 'vla_only',           'single', 20, 0.80,  None, '2026-05-24', 'new smolvla'),\n    (46, 'bjb2-28827', 'vla_only', 'vla_only',           'single', 20, 0.805, None, '2026-05-24', 'new smolvla'),\n    (45, 'bjb2-28827', 'adaptive_conformal_crm', 'adapt','single', 20, 0.80,  0.25, '2026-05-24', 'new smolvla'),\n    (48, 'bjb2-28827', 'adaptive_conformal_crm', 'adapt','single', 20, 0.81,  0.25, '2026-05-25', 'new smolvla'),\n    (49, 'bjb2-28827', 'adaptive_conformal_crm', 'adapt','single', 20, 0.82,  0.25, '2026-05-25', 'new smolvla'),\n\n    # bjb2-40593\n    (44, 'bjb2-40593', 'vla_only', 'vla_only',           'single', 20, 0.785, None, '2026-05-23', 'new smolvla'),\n    (42, 'bjb2-40593', 'adaptive_conformal_crm', 'adapt','single', 20, 0.79,  0.25, '2026-05-25', 'new smolvla'),\n\n    # bjb1-18228\n    (42, 'bjb1-18228', 'vla_only', 'vla_only',           'single', 20, 0.80,  None, '2026-05-25', 'new smolvla'),\n    (43, 'bjb1-18228', 'vla_only', 'vla_only',           'single', 10, 0.29,  None, '2026-05-19', 'old openvla'),\n    (50, 'bjb1-18228', 'vla_only', 'vla_only',           'single', 10, 0.30,  None, '2026-05-20', 'old openvla'),\n    (52, 'bjb1-18228', 'vla_only', 'vla_only',           'single', 10, 0.31,  None, '2026-05-20', 'old openvla'),\n    (53, 'bjb1-18228', 'vla_only', 'vla_only',           'single', 10, 0.28,  None, '2026-05-20', 'old openvla'),\n\n    # cqa1-32758\n    (42, 'cqa1-32758', 'vla_only', 'vla_only',           'single', 20, 0.785, None, '2026-05-25', 'new smolvla'),\n    (43, 'cqa1-32758', 'vla_only', 'vla_only',           'single', 20, 0.79,  None, '2026-05-23', 'new smolvla'),\n    (44, 'cqa1-32758', 'vla_only', 'vla_mean_K2',        'mean',   20, 0.81,  None, '2026-05-23', 'K=2 anomaly (file misnamed)'),\n    (45, 'cqa1-32758', 'vla_only', 'vla_only',           'single', 20, 0.77,  None, '2026-05-24', 'new smolvla'),\n    (46, 'cqa1-32758', 'vla_only', 'vla_only',           'single', 20, 0.805, None, '2026-05-24', 'new smolvla'),\n    (47, 'cqa1-32758', 'vla_only', 'vla_only',           'single', 20, 0.81,  None, '2026-05-24', 'new smolvla'),\n    (48, 'cqa1-32758', 'vla_only', 'vla_only',           'single', 20, 0.795, None, '2026-05-25', 'new smolvla'),\n    (49, 'cqa1-32758', 'vla_only', 'vla_only',           'single', 20, 0.785, None, '2026-05-25', 'new smolvla'),\n    (45, 'cqa1-32758', 'adaptive_conformal_crm', 'adapt','single', 20, 0.80,  0.25, '2026-05-24', 'new smolvla'),\n    (46, 'cqa1-32758', 'adaptive_conformal_crm', 'adapt','single', 20, 0.80,  0.25, '2026-05-24', 'new smolvla'),\n    (47, 'cqa1-32758', 'adaptive_conformal_crm', 'adapt','single', 20, 0.815, 0.25, '2026-05-24', 'new smolvla'),\n    (47, 'cqa1-32758', 'adaptive_conformal_crm', 'adapt','single', 20, 0.79,  0.25, '2026-05-24', 'duplicate (tau0.25 no-norm filename)'),\n]\n\nprint(\"=\" * 110)\nprint(\"AUDIT MATRIX: Spatial Experiments (all servers, all files)\")\nprint(\"=\" * 110)\nprint(f\"{'seed':<4} | {'server':<11} | {'mode_actual':<14} | {'baseline':<7} | {'n_roll':<6} | {'SR':<6} | {'tau':<5} | {'date':<10} | {'notes':<35}\")\nprint(\"-\" * 110)\nfor row in sorted(all_files, key=lambda x: (x[0], x[1], x[3])):\n    seed, server, file_label, mode_actual, baseline, n, sr, tau, mtime, notes = row\n    tau_s = str(tau) if tau else '-'\n    print(f\"{seed:<4} | {server:<11} | {mode_actual:<14} | {baseline:<7} | {n:<6} | {sr:<6} | {tau_s:<5} | {mtime:<10} | {notes:<35}\")\n\n# ============================\n# Build canonical pairs\n# ============================\nprint(\"\\n\\n\" + \"=\" * 110)\nprint(\"CANONICAL PAIR ANALYSIS — same-server, n_rollouts=20, baseline_mode=single\")\nprint(\"=\" * 110)\n\n# Filter to new-smolvla family (n=20, single)\nnew_vla = {}\nnew_adapt = {}\nfor row in all_files:\n    seed, server, _, mode_actual, baseline, n, sr, tau, mtime, notes = row\n    if n != 20 or baseline != 'single':\n        continue\n    if mode_actual == 'vla_only':\n        new_vla[(seed, server)] = sr\n    elif mode_actual == 'adapt' and tau == 0.25:\n        # take the canonical norm0.2 version, NOT the duplicate\n        # for s47 on cqa1-32758, there's a duplicate; we keep the first (0.815)\n        if (seed, server) not in new_adapt:\n            new_adapt[(seed, server)] = sr\n\nprint(\"\\nVLA-only available (n=20, single):\", {k: v for k,v in sorted(new_vla.items())})\nprint(\"Adaptive available  (n=20, single, tau=0.25):\", {k: v for k,v in sorted(new_adapt.items())})\n\n# Find same-server pairs by intersection on (seed, server)\nprint(\"\\n--- Same-server pairs ---\")\npair_keys = sorted(set(new_vla.keys()) & set(new_adapt.keys()))\nprint(f\"{'seed':<4} | {'server':<11} | {'VLA':<6} | {'Adapt':<6} | {'Δ (pp)':<8}\")\nprint(\"-\" * 50)\ndeltas = []\nfor k in pair_keys:\n    v = new_vla[k]\n    a = new_adapt[k]\n    d = (a - v) * 100\n    print(f\"{k[0]:<4} | {k[1]:<11} | {v:<6} | {a:<6} | {d:+.2f}\")\n    deltas.append(d)\n\n# If multiple servers have data for same seed, prefer one server (cqa1-32758)\n# Build unique-seed pairs\nprint(\"\\n--- Unique seed pairs (preferring cqa1-32758) ---\")\nseen_seeds = {}\npriority = ['cqa1-32758', 'bjb2-28827', 'bjb1-32546', 'bjb2-40593', 'bjb1-18228']\nfor k in sorted(pair_keys, key=lambda x: (x[0], priority.index(x[1]))):\n    if k[0] not in seen_seeds:\n        seen_seeds[k[0]] = k\n\nprint(f\"{'seed':<4} | {'server':<11} | {'VLA':<6} | {'Adapt':<6} | {'Δ (pp)':<8}\")\nprint(\"-\" * 50)\nunique_deltas = []\nunique_pairs = []\nfor seed in sorted(seen_seeds):\n    k = seen_seeds[seed]\n    v = new_vla[k]\n    a = new_adapt[k]\n    d = (a - v) * 100\n    print(f\"{seed:<4} | {k[1]:<11} | {v:<6} | {a:<6} | {d:+.2f}\")\n    unique_deltas.append(d)\n    unique_pairs.append((seed, k[1], v, a, d))\n\n# ============================\n# Statistics\n# ============================\nprint(\"\\n--- Paired statistics (canonical pairs, same-server only) ---\")\ndeltas_arr = np.array(unique_deltas)\nn = len(deltas_arr)\nmean_d = deltas_arr.mean()\nsd_d = deltas_arr.std(ddof=1) if n > 1 else 0\nsem_d = sd_d / np.sqrt(n) if n > 1 else 0\nprint(f\"n = {n}\")\nprint(f\"Mean Δ = {mean_d:+.3f} pp\")\nif n > 1:\n    print(f\"SD Δ   = {sd_d:.3f} pp\")\n    print(f\"SEM Δ  = {sem_d:.3f} pp\")\n    ci95 = stats.t.ppf(0.975, n-1) * sem_d\n    print(f\"95% CI = [{mean_d - ci95:+.3f}, {mean_d + ci95:+.3f}] pp\")\n    t_stat, p_val = stats.ttest_1samp(deltas_arr, 0.0)\n    print(f\"\\nPaired t-test (one-sample on Δ):  t={t_stat:.3f},  df={n-1},  p={p_val:.4f}\")\n    if n >= 6:\n        w_stat, w_p = stats.wilcoxon(deltas_arr)\n        print(f\"Wilcoxon signed-rank:             W={w_stat:.3f},  p={w_p:.4f}\")\n    else:\n        print(\"Wilcoxon: n<6, results unreliable\")\n\n# ============================\n# Comparison with previous \"8-seed\" analysis (mixed servers)\n# ============================\nprint(\"\\n\\n\" + \"=\" * 110)\nprint(\"FOR REFERENCE — what spatial_per_task_breakdown.md previously used (cross-server allowed):\")\nprint(\"=\" * 110)\n# from breakdown md\nprev = [\n    (42, 'cqa1-32758', 'bjb1-32546', 0.785, 0.795),  # vla cqa, adapt bjb1\n    (43, 'cqa1-32758', 'bjb1-32546', 0.79,  0.80),\n    (44, 'bjb2-40593', 'bjb1-32546', 0.785, 0.805),\n    (45, 'cqa1-32758', 'cqa1-32758', 0.77,  0.80),   # same\n    (46, 'cqa1-32758', 'cqa1-32758', 0.805, 0.80),   # same\n    (47, 'cqa1-32758', 'cqa1-32758', 0.81,  0.815),  # same\n    (48, 'cqa1-32758', 'bjb2-28827', 0.795, 0.81),\n    (49, 'cqa1-32758', 'bjb2-28827', 0.785, 0.82),\n]\nprev_deltas = np.array([(a-v)*100 for s,vs,as_,v,a in prev])\nprev_n = len(prev_deltas)\nprev_t, prev_p = stats.ttest_1samp(prev_deltas, 0.0)\nprev_w, prev_wp = stats.wilcoxon(prev_deltas)\nprint(f\"\\n{'seed':<4} | {'VLA srv':<11} | {'Adapt srv':<11} | {'VLA':<6} | {'Adapt':<6} | {'Δ pp':<7} | same-srv\")\nprint(\"-\" * 75)\nfor s, vs, as_, v, a in prev:\n    print(f\"{s:<4} | {vs:<11} | {as_:<11} | {v:<6} | {a:<6} | {(a-v)*100:+.2f}  | {'YES' if vs==as_ else 'no'}\")\n\nprint(f\"\\nn={prev_n}, mean Δ={prev_deltas.mean():+.3f}pp, SD={prev_deltas.std(ddof=1):.3f}\")\nci95 = stats.t.ppf(0.975, prev_n-1) * prev_deltas.std(ddof=1)/np.sqrt(prev_n)\nprint(f\"95% CI = [{prev_deltas.mean()-ci95:+.3f}, {prev_deltas.mean()+ci95:+.3f}]\")\nprint(f\"Paired t-test (one-sample on Δ): t={prev_t:.3f}, df={prev_n-1}, p={prev_p:.4f}\")\nprint(f\"Wilcoxon signed-rank: W={prev_w:.3f}, p={prev_wp:.4f}\")\nEOF",
    "description": "Build audit matrix + canonical pairs + p-values"
  }
}
```

</details>

---

### Tool result

_source line 95 · 2026-05-24T22:54:53.181475+00:00_

==============================================================================================================
AUDIT MATRIX: Spatial Experiments (all servers, all files)
==============================================================================================================
seed | server      | mode_actual    | baseline | n_roll | SR     | tau   | date       | notes                              
--------------------------------------------------------------------------------------------------------------
42   | bjb1-18228  | vla_only       | single  | 20     | 0.8    | -     | 2026-05-25 | new smolvla                        
42   | bjb1-32546  | adapt          | single  | 20     | 0.795  | 0.25  | 2026-05-25 | new smolvla                        
42   | bjb1-32546  | vla_only       | single  | 10     | 0.3    | -     | 2026-05-19 | old openvla                        
42   | bjb2-28827  | vla_mean_K2    | mean    | 20     | 0.815  | -     | 2026-05-23 | K=2 anomaly (file misnamed)        
42   | bjb2-40593  | adapt          | single  | 20     | 0.79   | 0.25  | 2026-05-25 | new smolvla                        
42   | cqa1-32758  | vla_only       | single  | 20     | 0.785  | -     | 2026-05-25 | new smolvla                        
43   | bjb1-18228  | vla_only       | single  | 10     | 0.29   | -     | 2026-05-19 | old openvla                        
43   | bjb1-32546  | adapt          | single  | 20     | 0.8    | 0.25  | 2026-05-23 | new smolvla                        
43   | bjb2-28827  | vla_only       | single  | 20     | 0.805  | -     | 2026-05-23 | new smolvla                        
43   | cqa1-32758  | vla_only       | single  | 20     | 0.79   | -     | 2026-05-23 | new smolvla                        
44   | bjb1-32546  | adapt          | single  | 20     | 0.805  | 0.25  | 2026-05-23 | new smolvla                        
44   | bjb2-28827  | vla_only       | single  | 20     | 0.805  | -     | 2026-05-23 | new smolvla                        
44   | b
…[truncated 6280 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_canonical-data-protocol_20260524T224440",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 96 · 2026-05-24T22:54:53.181663+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Read registry for all spatial experiments', 'activeForm': 'Reading registry for spatial experiments', 'status': 'completed'}, {'content': 'SSH each server to extract structured metadata from JSON files', 'activeForm': 'SSH each server to extract structured metadata', 'status': 'completed'}, {'content': 'Build audit matrix and canonical pairs', 'activeForm': 'Building audit matrix and canonical pairs', 'status': 'completed'}, {'content': 'Compute final p-values from canonical pairs', 'activeForm': 'Computing final p-values from canonical pairs', 'status': 'completed'}, {'content': 'Report audit matrix + yaml + p-values + gaps', 'activeForm': 'Reporting audit matrix + yaml + p-values + gaps', 'status': 'in_progress'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_canonical-data-protocol_20260524T224440",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Read registry for all spatial experiments', 'activeForm': 'Reading registry for spatial experiments', 'status': 'completed'}, {'content': 'SSH each server to extract structured metadata from JSON files', 'activeForm': 'SSH each server to extract structured metadata', 'status': 'completed'}, {'content': 'Build audit matrix and canonical pairs', 'activeForm': 'Building audit matrix and canonical pairs', 'status': 'completed'}, {'content': 'Compute final p-values from canonical pairs', 'activeForm': 'Computing final p-values from canonical pairs', 'status': 'completed'}, {'content': 'Report audit matrix + yaml + p-values + gaps', 'activeForm': 'Reporting audit matrix + yaml + p-values + gaps', 'status': 'in_progress'}]"
  }
}
```

</details>

---

### Tool result

_source line 97 · 2026-05-24T22:54:53.181836+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_canonical-data-protocol_20260524T224440",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 98 · 2026-05-24T22:54:53.182094+00:00_

# 1. 审计矩阵（任务 A）

**关键发现**：注册表 `server` 字段不可靠（很多是 `harvest` 记录的服务器，不代表当前位置）。直接 SSH 5 台服务器抓取 JSON 元数据后，整体只有两类有效数据：

- **新 smolvla family**：`n_rollouts=20`，`baseline_mode="single"`，2026-05-23 之后产出
- **旧 openvla family**：`n_rollouts=10`，无 Adaptive 模式，与新数据**不可比较**（不参与 paired test）

⚠️ 还发现 **2 个 K=2 mean 文件被误命名为 `vla_only`**（`baseline_mode: "mean"`），如不区分会污染数据：
- `bjb2-28827/eval_spatial_vla_only_seed42.json`：实际是 K=2 mean，SR=0.815
- `cqa1-32758/eval_spatial_vla_only_seed44.json`：实际是 K=2 mean，SR=0.81
- `bjb1-32546/eval_spatial_k2mean_seed46.json`：正确命名，K=2 mean，SR=0.80

注：用户提到 "s46 K=2 异常" 其实更准确说是 **s44 在 cqa1-32758 的 vla_only 文件实为 K=2**（这是被误用作 baseline 的真隐患）。s46 真正的 vla_only K=1 文件在多服务器都存在且数值一致（0.805），是干净的。s46 的 -0.5pp Δ 是真实结果而非 K 错配。

**完整审计矩阵**（新 smolvla family + 老 openvla family）：

```
seed | server      | mode_actual    | baseline | n_roll | SR     | tau  | date       | notes
-----|-------------|----------------|----------|--------|--------|------|------------|------------------
42   | bjb1-18228  | vla_only       | single   | 20     | 0.800  |  -   | 2026-05-25 | new smolvla
42   | bjb1-32546  | adaptive_crm   | single   | 20     | 0.795  | 0.25 | 2026-05-25 | new smolvla
42   | bjb1-32546  | vla_only       | single   | 10     | 0.300  |  -   | 2026-05-19 | OLD openvla (incompat)
42   | bjb2-28827  | vla_mean_K2 ⚠️ | mean     | 20     | 0.815  |  -   | 2026-05-23 | K=2 mean (file misnamed)
42   | bjb2-40593  | adaptive_crm   | single   | 20     | 0.790  | 0.25 | 2026-05-25 | new smolvla
42   | cqa1-32758  | vla_only       | single   | 20     | 0.785  |  -   | 2026-05-25 | new smolvla
43   | bjb1-32546  | adaptive_crm   | single   | 20     | 0.800  | 0.25 | 2026-05-23 | new smolvla
43   | bjb2-28827  | vla_only       | single   | 20     | 0.805  |  -   | 2026-05-23 | new smolvla
43   | cqa1-32758  | vla_only       | single   | 20     | 0.790  |  -   | 2026-05-23 | new smolvla
44   | bjb1-32546  | adaptive_crm   | single   | 20     | 0.805  | 0.25 | 2026-05-23 | new smolvla
44   | bjb2-28827  | vla_only       | single   | 20     | 0.805  |  -   | 2026-05-23 | new smolvla
44   | bjb2-40593  | vla_only       | single   | 20     | 0.785  |  -   | 2026-05-23 | new smolvla
44   | cqa1-32758  | vla_mean_K2 ⚠️ | mean     | 20     | 0.810  |  -   | 2026-05-23 | K=2 mean (file misnamed)
45   | bjb2-28827  | adaptive_crm   | single   | 20     | 0.800  | 0.25 | 2026-05-24 | new smolvla
45   | bjb2-28827  | vla_only       | single   | 20     | 0.800  |  -   | 2026-05-24 | new smolvla  ✓ pair
45   | cqa1-32758  | adaptive_crm   | single   | 20     | 0.800  | 0.25 | 2026-05-24 | new smolvla
45   | cqa1-32758  | vla_only       | single   | 20     | 0.770  |  -   | 2026-05-24 | new smolvla  ✓ pair
46   | bjb1-32546  | k2mean         | mean     | 20     | 0.800  |  -   | 2026-05-24 | K=2 mean (correctly named)
46   | bjb2-28827  | vla_only       | single   | 20     | 0.805  |  -   | 2026-05-24 | new smolvla
46   | cqa1-32758  | adaptive_crm   | single   | 20     | 0.800  | 0.25 | 2026-05-24 | new smolvla  ✓ pair
46   | cqa1-32758  | vla_only       | single   | 20     | 0.805  |  -   | 2026-05-24 | new smolvla  ✓ pair
47   | cqa1-32758  | adaptive_crm   | single   | 20     | 0.815  | 0.25 | 2026-05-24 | new smolvla  ✓ pair
47   | cqa1-32758  | adaptive_crm   | single   | 20     | 0.790  | 0.25 | 2026-05-24 | duplicate file (different filename)
47   | cqa1-32758  | vla_only       | single   | 20     | 0.810  |  -   | 2026-05-24 | new smolvla  ✓ pair
48   | bjb2-28827  | adaptive_crm   | single   | 20     | 0.810  | 0.25 | 2026-05-25 | new smolvla
48   | cqa1-32758  | vla_only       | single   | 20     | 0.795  |  -   | 2026-05-25 | new smolvla
49   | bjb2-28827  | adaptive_crm   | single   | 20     | 0.820  | 0.25 | 2026-05-25 | new smolvla
49   | cqa1-32758  | vla_only       | single   | 20     | 0.785  |  -   | 2026-05-25 | new smolvla
50-54| bjb1-*      | vla_only       | single   | 10     | 0.27-0.33 | - | 2026-05-20 | OLD openvla (incompat)
```

**用户提问的具体核查**：
- s42 Adaptive K=10 原始数据**没有被 K=1 覆盖**：bjb1-32546 上 2026-05-25 有 `eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed42.json`，SR=0.795；bjb2-40593 上也有 2026-05-25 的副本，SR=0.79
- s46 K=2 异常：用户混淆——s46 在 cqa1-32758/bjb2-28827 上的 vla_only 文件都是 `baseline_mode="single"`，**没问题**。真正的 K=2 误命名问题在 **s44 (cqa1-32758) 和 s42 (bjb2-28827)**

# 2. canonical_data_sources.yaml

```yaml
spatial_paired_data:
  selection_principle: |
    同服务器配对——每个 seed 的 VLA-only 和 Adaptive 必须来自同一台服务器，
    且必须满足 n_rollouts=20 + baseline_mode=single（排除 K=2 mean 误命名文件）。
    模型 family 固定为 smolvla (CRM checkpoint: crm_smolvla_3suite_v1)，
    Adaptive 参数固定为 mode=adaptive_conformal_crm, conformal_threshold=0.25, max_correction_norm=0.2。

  excluded_data:
    s46_k2_concern: "用户提及的 s46 K=2 异常实际不存在；bjb1-32546 的 k2mean_seed46.json 是单独的 K=2 实验文件，未被误用为 baseline"
    misnamed_k2_files:
      - file: bjb2-28827/eval_spatial_vla_only_seed42.json
        actual: vla_mean K=2 (baseline_mode=mean), SR=0.815
        action: 不得用作 s42 VLA-only baseline
      - file: cqa1-32758/eval_spatial_vla_only_seed44.json
        actual: vla_mean K=2 (baseline_mode=mean), SR=0.810
        action: 不得用作 s44 VLA-only baseline
    old_openvla_files:
      n_rollouts: 10
      seeds: [42-49, 50-54 on bjb1-32546/bjb1-18228]
      action: 与新 smolvla (n=20) 不可混用

  pairs:  # 严格同服务器
    s45_cqa:
      seed: 45
      server: cqa1-32758
      vla_only_file: logs/eval_spatial_vla_only_seed45.json
      vla_only_SR: 0.770
      adaptive_file: logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed45.json
      adaptive_SR: 0.800
      adaptive_tau: 0.25
      delta_pp: +3.00
    s45_bjb2:  # 备选/冗余
      seed: 45
      server: bjb2-28827
      vla_only_SR: 0.800
      adaptive_SR: 0.800
      delta_pp: 0.00
      note: |
        与 s45_cqa 同 seed 跨服务器对比：VLA SR 0.77 vs 0.80，Adapt SR 0.80 vs 0.80。
        说明同 seed 在两台 4090 集群上结果不一致（环境/数值非确定性），
        正好印证 reviewer 关于"跨服务器方差与改进幅度同量级"的担忧。
    s46_cqa:
      seed: 46
      server: cqa1-32758
      vla_only_file: logs/eval_spatial_vla_only_seed46.json
      vla_only_SR: 0.805
      adaptive_file: logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed46.json
      adaptive_SR: 0.800
      adaptive_tau: 0.25
      delta_pp: -0.50
    s47_cqa:
      seed: 47
      server: cqa1-32758
      vla_only_file: logs/eval_spatial_vla_only_seed47.json
      vla_only_SR: 0.810
      adaptive_file: logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed47.json
      adaptive_SR: 0.815
      adaptive_tau: 0.25
      delta_pp: +0.50
      note: 同目录另有 eval_spatial_adaptive_conformal_crm_tau0.25_seed47.json (SR=0.790)；
            选用带 norm0.2 命名的版本作为 canonical

  gaps:  # 需要补跑的实验
    - seed: 42
      has: ["adaptive on bjb1-32546", "adaptive on bjb2-40593",
            "vla_only on cqa1-32758", "vla_only on bjb1-18228"]
      needs: "vla_only on bjb1-32546 OR vla_only on bjb2-40593 OR adaptive on cqa1-32758/bjb1-18228"
      recommended: "Adaptive on cqa1-32758（与已有 VLA-only seed42 配对，cqa1 已有 GPU 空闲）"
    - seed: 43
      has: ["adaptive on bjb1-32546", "vla_only on bjb2-28827", "vla_only on cqa1-32758"]
      needs: "vla_only on bjb1-32546 OR adaptive on bjb2-28827/cqa1-32758"
      recommended: "Adaptive on cqa1-32758"
    - seed: 44
      has: ["adaptive on bjb1-32546", "vla_only on bjb2-28827", "vla_only on bjb2-40593"]
      needs: "vla_only on bjb1-32546 OR adaptive on bjb2-28827/bjb2-40593"
      recommended: "Adaptive on bjb2-28827（同服务器已有 vla_only s44）"
    - seed: 48
      has: ["adaptive on bjb2-28827", "vla_only on cqa1-32758"]
      needs: "vla_only on bjb2-28827 OR adaptive on cqa1-32758"
      recommended: "Adaptive on cqa1-32758"
    - seed: 49
      has: ["adaptive on bjb2-28827", "vla_only on cqa1-32758"]
      needs: "vla_only on bjb2-28827 OR adaptive on cqa1-32758"
      recommended: "Adaptive on cqa1-32758"

  statistics:
    n_valid_unique_seed_pairs: 3
    n_with_redundant_s45: 4
    mean_delta_pp: +1.00
    sd_delta_pp: 1.80
    ci95_pp: [-3.48, +5.48]
    paired_t_p_value: 0.4380   # n=3, df=2 → 统计功率不足
    wilcoxon_p_value: null     # n<6 不可靠
    cohens_dz: 0.55            # medium

  for_reference_cross_server:
    description: "spatial_per_task_breakdown.md 当前采用的 8-seed 跨服务器配对（违反 canonical 原则）"
    n: 8
    mean_delta_pp: +1.50
    paired_t_p_value: 0.0142
    wilcoxon_p_value: 0.0234
    warning: "5/8 pair 跨服务器，方差结构受服务器混淆影响；当前 p=0.0142 不能视为最终结果"
```

# 3. Final p-value 计算（任务 C）

**严格同服务器（n=3，cqa1-32758 only）：**

| 指标 | 值 |
|---|---|
| n（unique seeds） | 3 |
| Mean Δ | **+1.00pp** |
| SD Δ | 1.80pp |
| 95% CI | **[−3.48, +5.48] pp** |
| Paired t-test | t=0.961, df=2, **p=0.4380** |
| Wilcoxon | n<6，不可靠 |

**当前跨服务器 8-seed（违反 canonical 原则，仅供对照）：**

| 指标 | 值 |
|---|---|
| n | 8 |
| Mean Δ | +1.50pp |
| 95% CI | [+0.41, +2.60] pp |
| Paired t-test | t=3.240, df=7, **p=0.0142** |
| Wilcoxon | W=2.000, **p=0.0234** |

# 4. 缺口列表（补跑建议）

按优先级排列（每条都是单 GPU、~30min 任务）：

| 优先级 | seed | mode | server | 命令模板 |
|---|---|---|---|---|
| P0 | 42 | `adaptive_conformal_crm` | cqa1-32758 | `--mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark spatial --seed 42 --n_rollouts 20 --conformal_threshold 0.25 --max_correction_norm 0.2` |
| P0 | 43 | `adaptive_conformal_crm` | cqa1-32758 | 同上，`--seed 43` |
| P0 | 44 | `adaptive_conformal_crm` | bjb2-28827 | 同上，`--seed 44`（同服务器已有 vla_only s44） |
| P0 | 48 | `adaptive_conformal_crm` | cqa1-32758 | 同上，`--seed 48` |
| P0 | 49 | `adaptive_conformal_crm` | cqa1-32758 | 同上，`--seed 49` |

**补跑后预期**：n=8 同服务器对（cqa1: 42,43,45,46,47,48,49 + bjb2-28827: 44），可用 paired t-test + Wilcoxon。基于现有数据外推（mean Δ ≈ +1.0~1.5pp，SD ≈ 1.5），8 个同服 pair 应能给出 p ≈ 0.01~0.05。

**重要修订**：当前 `spatial_per_task_breakdown.md` 的 p=0.0142 由 5/8 跨服务器对支撑，不能作为最终 reviewer response。必须补跑 P0 列表的 5 个 Adaptive 实验才能给出真正符合 canonical 原则的统计结论。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_audit_canonical-data-protocol_20260524T224440"
}
```

</details>

---
