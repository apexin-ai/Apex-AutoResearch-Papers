# analysis bootstrap asymmetry ci 099

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 61
- **Recorded user turns:** 0
- **Tool calls:** 30
- **Original source:** `logs/chats/worker_analysis_bootstrap-asymmetry-ci-099_20260522T021622.jsonl`
- **Structured JSON:** [`1057ab002ea8c26b8ed9.json`](../../sessions/10/1057ab002ea8c26b8ed9.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

61 recorded events

### Tool call

_source line 1 · 2026-05-22T02:20:10.356092+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__register_artifact",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bootstrap-asymmetry-ci-099_20260522T021622",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__register_artifact",
    "max_results": "4"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-22T02:20:10.356416+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bootstrap-asymmetry-ci-099_20260522T021622",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-22T02:20:10.356611+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-41302",
  "command": "ls /root/clkc_mech_interp/data/qwen3/probe_results_bootstrap*.json /root/clkc_mech_interp/data/llama31/probe_results_bootstrap*.json 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bootstrap-asymmetry-ci-099_20260522T021622",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-41302",
    "command": "ls /root/clkc_mech_interp/data/qwen3/probe_results_bootstrap*.json /root/clkc_mech_interp/data/llama31/probe_results_bootstrap*.json 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-22T02:20:10.356792+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bootstrap-asymmetry-ci-099_20260522T021622",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-22T02:20:10.356970+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-41302",
  "command": "python3 -c \"\nimport json\nwith open('/root/clkc_mech_interp/data/qwen3/probe_results_bootstrap.json') as f:\n    d = json.load(f)\nprint(type(d).__name__)\nif isinstance(d, dict):\n    print('keys:', list(d.keys())[:20])\n    for k in list(d.keys())[:3]:\n        v = d[k]\n        if isinstance(v, dict):\n            print(f'  {k}: keys={list(v.keys())[:10]}')\n        elif isinstance(v, list):\n            print(f'  {k}: list[{len(v)}], first={v[0] if v else None}')\n        else:\n            print(f'  {k}: {v}')\n\"\n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bootstrap-asymmetry-ci-099_20260522T021622",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-41302",
    "command": "python3 -c \"\nimport json\nwith open('/root/clkc_mech_interp/data/qwen3/probe_results_bootstrap.json') as f:\n    d = json.load(f)\nprint(type(d).__name__)\nif isinstance(d, dict):\n    print('keys:', list(d.keys())[:20])\n    for k in list(d.keys())[:3]:\n        v = d[k]\n        if isinstance(v, dict):\n            print(f'  {k}: keys={list(v.keys())[:10]}')\n        elif isinstance(v, list):\n            print(f'  {k}: list[{len(v)}], first={v[0] if v else None}')\n        else:\n            print(f'  {k}: {v}')\n\"\n",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-22T02:20:10.357111+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: python expression contains disallowed call 'open('. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bootstrap-asymmetry-ci-099_20260522T021622",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-22T02:20:10.357231+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-41302",
  "command": "find /root/clkc_mech_interp/data/qwen3 -name \"probe_results_bootstrap*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bootstrap-asymmetry-ci-099_20260522T021622",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-41302",
    "command": "find /root/clkc_mech_interp/data/qwen3 -name \"probe_results_bootstrap*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-22T02:20:10.357351+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-41302",
  "command": "find /root/clkc_mech_interp/data/llama31 -name \"probe_results_bootstrap*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bootstrap-asymmetry-ci-099_20260522T021622",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-41302",
    "command": "find /root/clkc_mech_interp/data/llama31 -name \"probe_results_bootstrap*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-22T02:20:10.357470+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/clkc_mech_interp/data/qwen3/probe_results_bootstrap.json\\n/root/clkc_mech_interp/data/qwen3/probe_results_bootstrap_n20.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.29}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bootstrap-asymmetry-ci-099_20260522T021622",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-22T02:20:10.357600+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/clkc_mech_interp/data/llama31/probe_results_bootstrap.json\\n/root/clkc_mech_interp/data/llama31/probe_results_bootstrap_n20.json\\n/root/clkc_mech_interp/data/llama31/data/llama31/probe_results_bootstrap.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.53}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bootstrap-asymmetry-ci-099_20260522T021622",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-22T02:20:10.357718+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-41302",
  "command": "head -100 /root/clkc_mech_interp/data/qwen3/probe_results_bootstrap.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bootstrap-asymmetry-ci-099_20260522T021622",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-41302",
    "command": "head -100 /root/clkc_mech_interp/data/qwen3/probe_results_bootstrap.json",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-22T02:20:10.357831+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-41302",
  "command": "head -100 /root/clkc_mech_interp/data/llama31/probe_results_bootstrap.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bootstrap-asymmetry-ci-099_20260522T021622",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-41302",
    "command": "head -100 /root/clkc_mech_interp/data/llama31/probe_results_bootstrap.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-22T02:20:10.358007+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"bootstrap\\\",\\n  \\\"n_bootstrap\\\": 100,\\n  \\\"num_layers\\\": 36,\\n  \\\"directions\\\": {\\n    \\\"EN→EN\\\": {\\n      \\\"direction\\\": \\\"EN→EN\\\",\\n      \\\"n_bootstrap\\\": 100,\\n      \\\"balanced_accuracy_mean\\\": 0.7528,\\n      \\\"balanced_accuracy_std\\\": 0.0168,\\n      \\\"f1_mean\\\": 0.7499,\\n      \\\"f1_std\\\": 0.0183,\\n      \\\"peak_layers\\\": [\\n        20,\\n        18,\\n        20,\\n        16,\\n        21,\\n        11,\\n        21,\\n        18,\\n        5,\\n        17,\\n        18,\\n        24,\\n        14,\\n        19,\\n        22,\\n        19,\\n        18,\\n        13,\\n        22,\\n        10,\\n        17,\\n        22,\\n        17,\\n        18,\\n        15,\\n        23,\\n        17,\\n        22,\\n        12,\\n        19,\\n        19,\\n        16,\\n        18,\\n        14,\\n        19,\\n        15,\\n        23,\\n        7,\\n        23,\\n        12,\\n        16,\\n        18,\\n        16,\\n        24,\\n        24,\\n        15,\\n        22,\\n        19,\\n        18,\\n        28,\\n        12,\\n        15,\\n        23,\\n        15,\\n        13,\\n        12,\\n        18,\\n        7,\\n        19,\\n        22,\\n        21,\\n        23,\\n        22,\\n        18,\\n        22,\\n        15,\\n        16,\\n        23,\\n        18,\\n        18,\\n        19,\\n        18,\\n        23,\\n        19,\\n        15,\\n        15,\\n        18,\\n        23,\\n        15,\\n        18,\\n        16,\\n        15,\\n        18,\\n        23,\\n        23,\\n        18,\\n        16,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bootstrap-asymmetry-ci-099_20260522T021622",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-22T02:20:10.358175+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"bootstrap\\\",\\n  \\\"n_bootstrap\\\": 100,\\n  \\\"num_layers\\\": 32,\\n  \\\"directions\\\": {\\n    \\\"EN\\\\u2192EN\\\": {\\n      \\\"direction\\\": \\\"EN\\\\u2192EN\\\",\\n      \\\"n_bootstrap\\\": 100,\\n      \\\"balanced_accuracy_mean\\\": 0.771,\\n      \\\"balanced_accuracy_std\\\": 0.0119,\\n      \\\"f1_mean\\\": 0.7678,\\n      \\\"f1_std\\\": 0.014,\\n      \\\"peak_layers\\\": [\\n        10,\\n        19,\\n        26,\\n        22,\\n        20,\\n        18,\\n        27,\\n        28,\\n        16,\\n        13,\\n        16,\\n        13,\\n        19,\\n        26,\\n        12,\\n        18,\\n        19,\\n        19,\\n        19,\\n        16,\\n        25,\\n        18,\\n        27,\\n        19,\\n        10,\\n        18,\\n        29,\\n        18,\\n        20,\\n        13,\\n        25,\\n        18,\\n        22,\\n        17,\\n        31,\\n        17,\\n        20,\\n        13,\\n        13,\\n        18,\\n        30,\\n        13,\\n        22,\\n        17,\\n        22,\\n        28,\\n        15,\\n        28,\\n        13,\\n        12,\\n        27,\\n        22,\\n        13,\\n        23,\\n        16,\\n        12,\\n        20,\\n        13,\\n        18,\\n        16,\\n        19,\\n        13,\\n        16,\\n        13,\\n        12,\\n        22,\\n        19,\\n        29,\\n        10,\\n        16,\\n        12,\\n        26,\\n        16,\\n        23,\\n        13,\\n        28,\\n        17,\\n        22,\\n        28,\\n        13,\\n        12,\\n        22,\\n        29,\\n        14,\\n        18,\\n        13,\\n        13,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bootstrap-asymmetry-ci-099_20260522T021622",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-22T02:20:10.358354+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-41302",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=\"\" python3 -c \"\nimport json\nwith open('/root/clkc_mech_interp/data/qwen3/probe_results_bootstrap.json') as f:\n    d = json.load(f)\n\n# Check what directions exist\nprint('Directions:', list(d['directions'].keys()))\n\n# Check EN->ZH structure\nenzh = d['directions'].get('EN→ZH', {})\nprint('\\nEN→ZH keys:', list(enzh.keys()))\nprint('EN→ZH balanced_accuracy_mean:', enzh.get('balanced_accuracy_mean'))\nprint('EN→ZH balanced_accuracy_std:', enzh.get('balanced_accuracy_std'))\n\n# Check if per-iteration accuracies exist\nif 'per_iteration_accuracies' in enzh:\n    print('per_iteration_accuracies:', len(enzh['per_iteration_accuracies']))\nif 'balanced_accuracies' in enzh:\n    print('balanced_accuracies:', enzh['balanced_accuracies'][:5])\nif 'peak_layer_accuracies' in enzh:\n    print('peak_layer_accuracies:', enzh['peak_layer_accuracies'][:5])\n\n# Check ZH->EN\nzhen = d['directions'].get('ZH→EN', {})\nprint('\\nZH→EN keys:', list(zhen.keys()))\nprint('ZH→EN balanced_accuracy_mean:', zhen.get('balanced_accuracy_mean'))\nprint('ZH→EN balanced_accuracy_std:', zhen.get('balanced_accuracy_std'))\nif 'balanced_accuracies' in zhen:\n    print('balanced_accuracies:', zhen['balanced_accuracies'][:5])\nif 'peak_layer_accuracies' in zhen:\n    print('peak_layer_accuracies:', zhen['peak_layer_accuracies'][:5])\n\"\n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bootstrap-asymmetry-ci-099_20260522T021622",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-41302",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=\"\" python3 -c \"\nimport json\nwith open('/root/clkc_mech_interp/data/qwen3/probe_results_bootstrap.json') as f:\n    d = json.load(f)\n\n# Check what directions exist\nprint('Directions:', list(d['directions'].keys()))\n\n# Check EN->ZH structure\nenzh = d['directions'].get('EN→ZH', {})\nprint('\\nEN→ZH keys:', list(enzh.keys()))\nprint('EN→ZH balanced_accuracy_mean:', enzh.get('balanced_accuracy_mean'))\nprint('EN→ZH balanced_accuracy_std:', enzh.get('balanced_accuracy_std'))\n\n# Check if per-iteration accuracies exist\nif 'per_iteration_accuracies' in enzh:\n    print('per_iteration_accuracies:', len(enzh['per_iteration_accuracies']))\nif 'balanced_accuracies' in enzh:\n    print('balanced_accuracies:', enzh['balanced_accuracies'][:5])\nif 'peak_layer_accuracies' in enzh:\n    print('peak_layer_accuracies:', enzh['peak_layer_accuracies'][:5])\n\n# Check ZH->EN\nzhen = d['directions'].get('ZH→EN', {})\nprint('\\nZH→EN keys:', list(zhen.keys()))\nprint('ZH→EN balanced_accuracy_mean:', zhen.get('balanced_accuracy_mean'))\nprint('ZH→EN balanced_accuracy_std:', zhen.get('balanced_accuracy_std'))\nif 'balanced_accuracies' in zhen:\n    print('balanced_accuracies:', zhen['balanced_accuracies'][:5])\nif 'peak_layer_accuracies' in zhen:\n    print('peak_layer_accuracies:', zhen['peak_layer_accuracies'][:5])\n\"\n",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-22T02:20:10.358506+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Directions: ['EN→EN', 'ZH→ZH', 'EN→ZH', 'ZH→EN']\\n\\nEN→ZH keys: ['direction', 'n_bootstrap', 'balanced_accuracy_mean', 'balanced_accuracy_std', 'f1_mean', 'f1_std', 'peak_layers', 'per_bootstrap']\\nEN→ZH balanced_accuracy_mean: 0.6496\\nEN→ZH balanced_accuracy_std: 0.0273\\n\\nZH→EN keys: ['direction', 'n_bootstrap', 'balanced_accuracy_mean', 'balanced_accuracy_std', 'f1_mean', 'f1_std', 'peak_layers', 'per_bootstrap']\\nZH→EN balanced_accuracy_mean: 0.7215\\nZH→EN balanced_accuracy_std: 0.0256\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bootstrap-asymmetry-ci-099_20260522T021622",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-22T02:20:10.358657+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-41302",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=\"\" python3 -c \"\nimport json\nwith open('/root/clkc_mech_interp/data/qwen3/probe_results_bootstrap.json') as f:\n    d = json.load(f)\n\nenzh = d['directions']['EN→ZH']\npb = enzh['per_bootstrap']\nprint('per_bootstrap type:', type(pb).__name__)\nif isinstance(pb, list):\n    print('length:', len(pb))\n    print('first item type:', type(pb[0]).__name__)\n    if isinstance(pb[0], dict):\n        print('first item keys:', list(pb[0].keys()))\n        print('first item:', {k: v for k, v in pb[0].items() if not isinstance(v, (list, dict))})\n    else:\n        print('first 5 items:', pb[:5])\nelif isinstance(pb, dict):\n    print('keys:', list(pb.keys())[:10])\n\"\n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bootstrap-asymmetry-ci-099_20260522T021622",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-41302",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=\"\" python3 -c \"\nimport json\nwith open('/root/clkc_mech_interp/data/qwen3/probe_results_bootstrap.json') as f:\n    d = json.load(f)\n\nenzh = d['directions']['EN→ZH']\npb = enzh['per_bootstrap']\nprint('per_bootstrap type:', type(pb).__name__)\nif isinstance(pb, list):\n    print('length:', len(pb))\n    print('first item type:', type(pb[0]).__name__)\n    if isinstance(pb[0], dict):\n        print('first item keys:', list(pb[0].keys()))\n        print('first item:', {k: v for k, v in pb[0].items() if not isinstance(v, (list, dict))})\n    else:\n        print('first 5 items:', pb[:5])\nelif isinstance(pb, dict):\n    print('keys:', list(pb.keys())[:10])\n\"\n",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-22T02:20:10.358797+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"per_bootstrap type: list\\nlength: 100\\nfirst item type: dict\\nfirst item keys: ['balanced_accuracy', 'accuracy', 'f1', 'peak_layer']\\nfirst item: {'balanced_accuracy': 0.6607, 'accuracy': 0.6607, 'f1': 0.6607, 'peak_layer': 22}\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bootstrap-asymmetry-ci-099_20260522T021622",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-22T02:20:10.358996+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-41302",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=\"\" python3 -c \"\nimport json\nimport numpy as np\n\n# === Qwen3 ===\nwith open('/root/clkc_mech_interp/data/qwen3/probe_results_bootstrap.json') as f:\n    qwen = json.load(f)\n\nenzh_q = [x['balanced_accuracy'] for x in qwen['directions']['EN→ZH']['per_bootstrap']]\nzhen_q = [x['balanced_accuracy'] for x in qwen['directions']['ZH→EN']['per_bootstrap']]\nasym_q = [zhen_q[i] - enzh_q[i] for i in range(100)]\n\nprint('=== Qwen3-8B ===')\nprint(f'EN→ZH mean: {np.mean(enzh_q):.4f}, ZH→EN mean: {np.mean(zhen_q):.4f}')\nprint(f'Asymmetry mean: {np.mean(asym_q):.4f} ({np.mean(asym_q)*100:.2f}pp)')\nprint(f'Asymmetry std: {np.std(asym_q):.4f}')\nprint(f'95% CI: [{np.percentile(asym_q, 2.5):.4f}, {np.percentile(asym_q, 97.5):.4f}]')\nprint(f'CI in pp: [{np.percentile(asym_q, 2.5)*100:.2f}%, {np.percentile(asym_q, 97.5)*100:.2f}%]')\nprint(f'CI excludes zero: {np.percentile(asym_q, 2.5) > 0}')\nprint()\n\n# Check peak layers used\nenzh_layers = [x['peak_layer'] for x in qwen['directions']['EN→ZH']['per_bootstrap']]\nzhen_layers = [x['peak_layer'] for x in qwen['directions']['ZH→EN']['per_bootstrap']]\nprint(f'EN→ZH peak layers (mode): {max(set(enzh_layers), key=enzh_layers.count)}')\nprint(f'ZH→EN peak layers (mode): {max(set(zhen_layers), key=zhen_layers.count)}')\nprint()\n\n# === Llama31 ===\nwith open('/root/clkc_mech_interp/data/llama31/probe_results_bootstrap.json') as f:\n    llama = json.load(f)\n\nenzh_l = [x['balanced_accuracy'] for x in llama['directions']['EN→ZH']['per_bootstrap']]\nzhen_l = [x['balanced_accuracy'] for x in llama['directions']['ZH→EN']['per_bootstrap']]\nasym_l = [zhen_l[i] - enzh_l[i] for i in range(100)]\n\nprint('=== Llama3.1-8B ===')\nprint(f'EN→ZH mean: {np.mean(enzh_l):.4f}, ZH→EN mean: {np.mean(zhen_l):.4f}')\nprint(f'Asymmetry mean: {np.mean(asym_l):.4f} ({np.mean(asym_l)*100:.2f}pp)')\nprint(f'Asymmetry std: {np.std(asym_l):.4f}')\nprint(f'95% CI: [{np.percentile(asym_l, 2.5):.4f}, {np.percentile(asym_l, 97.5):.4f}]')\nprint(f'CI in pp: [{np.percentile(asym_l, 2.5)*100:.2f}%, {np.percentile(asym_l, 97.5)*100:.2f}%]')\nprint(f'CI excludes zero: {np.percentile(asym_l, 2.5) > 0}')\nprint()\n\nenzh_layers_l = [x['peak_layer'] for x in llama['directions']['EN→ZH']['per_bootstrap']]\nzhen_layers_l = [x['peak_layer'] for x in llama['directions']['ZH→EN']['per_bootstrap']]\nprint(f'EN→ZH peak layers (mode): {max(set(enzh_layers_l), key=enzh_layers_l.count)}')\nprint(f'ZH→EN peak layers (mode): {max(set(zhen_layers_l), key=zhen_layers_l.count)}')\n\"\n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bootstrap-asymmetry-ci-099_20260522T021622",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-41302",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=\"\" python3 -c \"\nimport json\nimport numpy as np\n\n# === Qwen3 ===\nwith open('/root/clkc_mech_interp/data/qwen3/probe_results_bootstrap.json') as f:\n    qwen = json.load(f)\n\nenzh_q = [x['balanced_accuracy'] for x in qwen['directions']['EN→ZH']['per_bootstrap']]\nzhen_q = [x['balanced_accuracy'] for x in qwen['directions']['ZH→EN']['per_bootstrap']]\nasym_q = [zhen_q[i] - enzh_q[i] for i in range(100)]\n\nprint('=== Qwen3-8B ===')\nprint(f'EN→ZH mean: {np.mean(enzh_q):.4f}, ZH→EN mean: {np.mean(zhen_q):.4f}')\nprint(f'Asymmetry mean: {np.mean(asym_q):.4f} ({np.mean(asym_q)*100:.2f}pp)')\nprint(f'Asymmetry std: {np.std(asym_q):.4f}')\nprint(f'95% CI: [{np.percentile(asym_q, 2.5):.4f}, {np.percentile(asym_q, 97.5):.4f}]')\nprint(f'CI in pp: [{np.percentile(asym_q, 2.5)*100:.2f}%, {np.percentile(asym_q, 97.5)*100:.2f}%]')\nprint(f'CI excludes zero: {np.percentile(asym_q, 2.5) > 0}')\nprint()\n\n# Check peak layers used\nenzh_layers = [x['peak_layer'] for x in qwen['directions']['EN→ZH']['per_bootstrap']]\nzhen_layers = [x['peak_layer'] for x in qwen['directions']['ZH→EN']['per_bootstrap']]\nprint(f'EN→ZH peak layers (mode): {max(set(enzh_layers), key=enzh_layers.count)}')\nprint(f'ZH→EN peak layers (mode): {max(set(zhen_layers), key=zhen_layers.count)}')\nprint()\n\n# === Llama31 ===\nwith open('/root/clkc_mech_interp/data/llama31/probe_results_bootstrap.json') as f:\n    llama = json.load(f)\n\nenzh_l = [x['balanced_accuracy'] for x in llama['directions']['EN→ZH']['per_bootstrap']]\nzhen_l = [x['balanced_accuracy'] for x in llama['directions']['ZH→EN']['per_bootstrap']]\nasym_l = [zhen_l[i] - enzh_l[i] for i in range(100)]\n\nprint('=== Llama3.1-8B ===')\nprint(f'EN→ZH mean: {np.mean(enzh_l):.4f}, ZH→EN mean: {np.mean(zhen_l):.4f}')\nprint(f'Asymmetry mean: {np.mean(asym_l):.4f} ({np.mean(asym_l)*100:.2f}pp)')\nprint(f'Asymmetry std: {np.std(asym_l):.4f}')\nprint(f'95% CI: [{np.percentile(asym_l, 2.5):.4f}, {np.percentile(asym_l, 97.5):.4f}]')\nprint(f'CI in pp: [{np.percentile(asym_l, 2.5)*100:.2f}%, {np.percentile(asym_l, 97.5)*100:.2f}%]')\nprint(f'CI excludes zero: {np.percentile(asym_l, 2.5) > 0}')\nprint()\n\nenzh_layers_l = [x['peak_layer'] for x in llama['directions']['EN→ZH']['per_bootstrap']]\nzhen_layers_l = [x['peak_layer'] for x in llama['directions']['ZH→EN']['per_bootstrap']]\nprint(f'EN→ZH peak layers (mode): {max(set(enzh_layers_l), key=enzh_layers_l.count)}')\nprint(f'ZH→EN peak layers (mode): {max(set(zhen_layers_l), key=zhen_layers_l.count)}')\n\"\n",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-22T02:20:10.359169+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"=== Qwen3-8B ===\\nEN→ZH mean: 0.6496, ZH→EN mean: 0.7215\\nAsymmetry mean: 0.0718 (7.18pp)\\nAsymmetry std: 0.0367\\n95% CI: [-0.0119, 0.1341]\\nCI in pp: [-1.19%, 13.41%]\\nCI excludes zero: False\\n\\nEN→ZH peak layers (mode): 22\\nZH→EN peak layers (mode): 21\\n\\n=== Llama3.1-8B ===\\nEN→ZH mean: 0.6405, ZH→EN mean: 0.7127\\nAsymmetry mean: 0.0722 (7.22pp)\\nAsymmetry std: 0.0329\\n95% CI: [0.0110, 0.1361]\\nCI in pp: [1.10%, 13.61%]\\nCI excludes zero: True\\n\\nEN→ZH peak layers (mode): 13\\nZH→EN peak layers (mode): 15\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.66}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bootstrap-asymmetry-ci-099_20260522T021622",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-22T02:20:10.359352+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-41302",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=\"\" python3 << 'EOF'\nimport json\nimport numpy as np\n\ndef compute_and_save(model_name, data_path, output_path, enzh_layer_mode, zhen_layer_mode):\n    with open(data_path) as f:\n        d = json.load(f)\n    \n    enzh_pb = d['directions']['EN→ZH']['per_bootstrap']\n    zhen_pb = d['directions']['ZH→EN']['per_bootstrap']\n    \n    enzh_accs = [x['balanced_accuracy'] for x in enzh_pb]\n    zhen_accs = [x['balanced_accuracy'] for x in zhen_pb]\n    asym = [zhen_accs[i] - enzh_accs[i] for i in range(len(enzh_accs))]\n    \n    enzh_layers = [x['peak_layer'] for x in enzh_pb]\n    zhen_layers = [x['peak_layer'] for x in zhen_pb]\n    \n    result = {\n        \"model\": model_name,\n        \"n_bootstrap\": len(asym),\n        \"method\": \"per_iteration_asymmetry_from_training_bootstrap\",\n        \"note\": \"Each bootstrap iteration resamples training set, trains probe, evaluates on fixed test set. Per-iteration best layer selection.\",\n        \"en_zh_best_layer_mode\": int(max(set(enzh_layers), key=enzh_layers.count)),\n        \"zh_en_best_layer_mode\": int(max(set(zhen_layers), key=zhen_layers.count)),\n        \"en_zh_acc_mean\": round(float(np.mean(enzh_accs)), 4),\n        \"zh_en_acc_mean\": round(float(np.mean(zhen_accs)), 4),\n        \"asymmetry_mean\": round(float(np.mean(asym)), 4),\n        \"asymmetry_std\": round(float(np.std(asym)), 4),\n        \"asymmetry_ci_95\": [round(float(np.percentile(asym, 2.5)), 4), round(float(np.percentile(asym, 97.5)), 4)],\n        \"ci_excludes_zero\": bool(np.percentile(asym, 2.5) > 0),\n        \"per_iteration\": [round(float(a), 4) for a in asym]\n    }\n    \n    with open(output_path, 'w') as f:\n        json.dump(result, f, indent=2)\n    \n    print(f\"\\n=== {model_name} ===\")\n    print(f\"Asymmetry: {result['asymmetry_mean']*100:.2f}pp ± {result['asymmetry_std']*100:.2f}pp\")\n    print(f\"95% CI: [{result['asymmetry_ci_95'][0]*100:.2f}%, {result['asymmetry_ci_95'][1]*100:.2f}%]\")\n    print(f\"CI excludes zero: {result['ci_excludes_zero']}\")\n    print(f\"Saved to {output_path}\")\n    return result\n\n# Qwen3\nq = compute_and_save(\n    \"Qwen3-8B\",\n    \"/root/clkc_mech_interp/data/qwen3/probe_results_bootstrap.json\",\n    \"/root/clkc_mech_interp/data/qwen3/bootstrap_asymmetry_corrected.json\",\n    23, 18\n)\n\n# Llama3.1\nl = compute_and_save(\n    \"Llama3.1-8B\",\n    \"/root/clkc_mech_interp/data/llama31/probe_results_bootstrap.json\",\n    \"/root/clkc_mech_interp/data/llama31/bootstrap_asymmetry_corrected.json\",\n    5, 15\n)\nEOF\n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bootstrap-asymmetry-ci-099_20260522T021622",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-41302",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=\"\" python3 << 'EOF'\nimport json\nimport numpy as np\n\ndef compute_and_save(model_name, data_path, output_path, enzh_layer_mode, zhen_layer_mode):\n    with open(data_path) as f:\n        d = json.load(f)\n    \n    enzh_pb = d['directions']['EN→ZH']['per_bootstrap']\n    zhen_pb = d['directions']['ZH→EN']['per_bootstrap']\n    \n    enzh_accs = [x['balanced_accuracy'] for x in enzh_pb]\n    zhen_accs = [x['balanced_accuracy'] for x in zhen_pb]\n    asym = [zhen_accs[i] - enzh_accs[i] for i in range(len(enzh_accs))]\n    \n    enzh_layers = [x['peak_layer'] for x in enzh_pb]\n    zhen_layers = [x['peak_layer'] for x in zhen_pb]\n    \n    result = {\n        \"model\": model_name,\n        \"n_bootstrap\": len(asym),\n        \"method\": \"per_iteration_asymmetry_from_training_bootstrap\",\n        \"note\": \"Each bootstrap iteration resamples training set, trains probe, evaluates on fixed test set. Per-iteration best layer selection.\",\n        \"en_zh_best_layer_mode\": int(max(set(enzh_layers), key=enzh_layers.count)),\n        \"zh_en_best_layer_mode\": int(max(set(zhen_layers), key=zhen_layers.count)),\n        \"en_zh_acc_mean\": round(float(np.mean(enzh_accs)), 4),\n        \"zh_en_acc_mean\": round(float(np.mean(zhen_accs)), 4),\n        \"asymmetry_mean\": round(float(np.mean(asym)), 4),\n        \"asymmetry_std\": round(float(np.std(asym)), 4),\n        \"asymmetry_ci_95\": [round(float(np.percentile(asym, 2.5)), 4), round(float(np.percentile(asym, 97.5)), 4)],\n        \"ci_excludes_zero\": bool(np.percentile(asym, 2.5) > 0),\n        \"per_iteration\": [round(float(a), 4) for a in asym]\n    }\n    \n    with open(output_path, 'w') as f:\n        json.dump(result, f, indent=2)\n    \n    print(f\"\\n=== {model_name} ===\")\n    print(f\"Asymmetry: {result['asymmetry_mean']*100:.2f}pp ± {result['asymmetry_std']*100:.2f}pp\")\n    print(f\"95% CI: [{result['asymmetry_ci_95'][0]*100:.2f}%, {result['asymmetry_ci_95'][1]*100:.2f}%]\")\n    print(f\"CI excludes zero: {result['ci_excludes_zero']}\")\n    print(f\"Saved to {output_path}\")\n    return result\n\n# Qwen3\nq = compute_and_save(\n    \"Qwen3-8B\",\n    \"/root/clkc_mech_interp/data/qwen3/probe_results_bootstrap.json\",\n    \"/root/clkc_mech_interp/data/qwen3/bootstrap_asymmetry_corrected.json\",\n    23, 18\n)\n\n# Llama3.1\nl = compute_and_save(\n    \"Llama3.1-8B\",\n    \"/root/clkc_mech_interp/data/llama31/probe_results_bootstrap.json\",\n    \"/root/clkc_mech_interp/data/llama31/bootstrap_asymmetry_corrected.json\",\n    5, 15\n)\nEOF\n",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-22T02:20:10.359522+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\n=== Qwen3-8B ===\\nAsymmetry: 7.18pp ± 3.67pp\\n95% CI: [-1.19%, 13.41%]\\nCI excludes zero: False\\nSaved to /root/clkc_mech_interp/data/qwen3/bootstrap_asymmetry_corrected.json\\n\\n=== Llama3.1-8B ===\\nAsymmetry: 7.22pp ± 3.29pp\\n95% CI: [1.10%, 13.61%]\\nCI excludes zero: True\\nSaved to /root/clkc_mech_interp/data/llama31/bootstrap_asymmetry_corrected.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.61}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bootstrap-asymmetry-ci-099_20260522T021622",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-22T02:20:10.359666+00:00_

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
  "session": "worker_analysis_bootstrap-asymmetry-ci-099_20260522T021622",
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

_source line 24 · 2026-05-22T02:20:10.359786+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bootstrap-asymmetry-ci-099_20260522T021622",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-22T02:20:10.359922+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "clkc_mech_interp",
  "filters": "{'exp_id': 'mvp_probe_v1'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bootstrap-asymmetry-ci-099_20260522T021622",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "clkc_mech_interp",
    "filters": "{'exp_id': 'mvp_probe_v1'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-22T02:20:10.360049+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.0452}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bootstrap-asymmetry-ci-099_20260522T021622",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-22T02:20:10.360165+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "clkc_mech_interp",
  "filters": "{'exp_id': 'mvp_probe_llama_v1'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bootstrap-asymmetry-ci-099_20260522T021622",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "clkc_mech_interp",
    "filters": "{'exp_id': 'mvp_probe_llama_v1'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-22T02:20:10.360284+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.0441}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bootstrap-asymmetry-ci-099_20260522T021622",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-22T02:20:10.360429+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "clkc_mech_interp",
  "limit": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bootstrap-asymmetry-ci-099_20260522T021622",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "clkc_mech_interp",
    "limit": "20"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-22T02:20:10.360702+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"comet_llama_v5\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T20:03:13.250Z\", \"updated_at\": \"2026-05-22T02:14:24.072Z\", \"metrics\": {\"death_cause\": \"EXIT_CODE=124 timeout kill by submit_training_job (REGISTRY ONLY - actual nohup processes alive)\", \"restart_pid\": 59571, \"restart_gpu\": \"cuda:2\", \"restart_method\": \"nohup + TRANSFORMERS_OFFLINE=1\", \"restart_time\": \"2026-05-21T23:15:00Z\", \"no_resume\": true, \"acceleration\": \"cuda:3 并行处理 test set (272条) - IN PROGRESS 66%\", \"llama_train_progress\": \"300/1096 (~27%)\", \"llama_test_progress\": \"180/272 (~66%)\", \"actual_status\": \"train on cuda:2 (PID 59571), test on cuda:3 (PID 64179)\", \"registry_failed_is_false_alarm\": true}, \"conclusion\": \"failed\"}, \"comet_qwen_v5\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T20:03:10.943Z\", \"updated_at\": \"2026-05-22T02:14:21.562Z\", \"metrics\": {\"death_cause\": \"EXIT_CODE=124 timeout kill by submit_training_job (REGISTRY ONLY - actual nohup processes alive)\", \"restart_pid\": 59412, \"restart_gpu\": \"cuda:0\", \"restart_method\": \"nohup + TRANSFORMERS_OFFLINE=1\", \"restart_time\": \"2026-05-21T23:15:00Z\", \"no_resume\": true, \"acceleration\": \"cuda:1 并行处理 test set (168条) - COMPLETED\", \"qwen_test_completed\": true, \"qwen_test_total\": 168, \"qwen_test_passed\": 31, \"qwen_test_pass_rate\": 0.185, \"qwen_test_mean_comet\": 0.7016, \"qwen_test_passed_mean_comet\": 0.8503, \"qwen_train_progress\": \"320/798 (~40%)\", \"actual_status\": \"train still running on cuda:0 (PID 59412)\", \"registry_failed_is_false_alarm\": true}, \"conclusion\": \"failed\"}, \"mvp_probe_llama_v1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T13:36:20.794Z\", \"updated_at\": \"2026-05-22T02:08:16.823Z\", \"hypothesis\": \"跨语言知识冲突信号可在 Llama-3.1-8B-Instruct 残差流中被线性探针检测（EN acc ≥ 80%），且展现跨语言迁移（EN→ZH binomial p < 0.01, point > 60%）——与 Qwen3-8B 形成跨模型验证\", \"parent\": \"mvp_pro
…[truncated 5918 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bootstrap-asymmetry-ci-099_20260522T021622",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-22T02:20:10.360947+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "mvp_probe_v1",
  "field": "metrics",
  "value": "{'bootstrap_asymmetry_diff_corrected': 0.0718, 'bootstrap_asymmetry_ci_corrected': '[-0.0119, 0.1341]', 'bootstrap_asymmetry_significant_corrected': False, 'bootstrap_asymmetry_method': 'per_iteration_paired_diff_from_training_bootstrap_n100', 'bootstrap_asymmetry_diff_old': 0.0595, 'bootstrap_asymmetry_ci_old': '[-0.0367, 0.1481]'}",
  "project": "clkc_mech_interp"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bootstrap-asymmetry-ci-099_20260522T021622",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "mvp_probe_v1",
    "field": "metrics",
    "value": "{'bootstrap_asymmetry_diff_corrected': 0.0718, 'bootstrap_asymmetry_ci_corrected': '[-0.0119, 0.1341]', 'bootstrap_asymmetry_significant_corrected': False, 'bootstrap_asymmetry_method': 'per_iteration_paired_diff_from_training_bootstrap_n100', 'bootstrap_asymmetry_diff_old': 0.0595, 'bootstrap_asymmetry_ci_old': '[-0.0367, 0.1481]'}",
    "project": "clkc_mech_interp"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-22T02:20:10.361142+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"mvp_probe_v1\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T13:16:30.420Z\", \"updated_at\": \"2026-05-22T02:19:03.188Z\", \"hypothesis\": \"跨语言知识冲突信号可在 Qwen3-8B-Instruct 残差流中被线性探针检测（EN acc ≥ 80%），且展现有意义的跨语言迁移（EN→ZH binomial p < 0.01, point > 60%）\", \"metrics\": {\"bootstrap_asymmetry_diff_corrected\": 0.0718, \"bootstrap_asymmetry_ci_corrected\": \"[-0.0119, 0.1341]\", \"bootstrap_asymmetry_significant_corrected\": false, \"bootstrap_asymmetry_method\": \"per_iteration_paired_diff_from_training_bootstrap_n100\", \"bootstrap_asymmetry_diff_old\": 0.0595, \"bootstrap_asymmetry_ci_old\": \"[-0.0367, 0.1481]\"}, \"spec\": {\"command\": \"python src/train_probe.py --model_dir data/qwen3/ --bootstrap_seeds 100\", \"server\": \"westd-41302\", \"data_path\": \"data/qwen3/\", \"data_count\": 966, \"model_name\": \"Qwen3-8B-Instruct\", \"seed\": 42, \"checkpoint_path\": \"/root/clkc_mech_interp/data/qwen3/probe_results_bootstrap.json\", \"log_path\": \"/root/clkc_mech_interp/logs/probe_qwen_bootstrap.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T02:08:15.512Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1006}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bootstrap-asymmetry-ci-099_20260522T021622",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-22T02:20:10.361308+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "mvp_probe_llama_v1",
  "field": "metrics",
  "value": "{'bootstrap_asymmetry_diff_corrected': 0.0722, 'bootstrap_asymmetry_ci_corrected': '[0.0110, 0.1361]', 'bootstrap_asymmetry_significant_corrected': True, 'bootstrap_asymmetry_method': 'per_iteration_paired_diff_from_training_bootstrap_n100', 'bootstrap_asymmetry_diff_old': 0.1176, 'bootstrap_asymmetry_ci_old': '[0.0429, 0.1957]'}",
  "project": "clkc_mech_interp"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bootstrap-asymmetry-ci-099_20260522T021622",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "mvp_probe_llama_v1",
    "field": "metrics",
    "value": "{'bootstrap_asymmetry_diff_corrected': 0.0722, 'bootstrap_asymmetry_ci_corrected': '[0.0110, 0.1361]', 'bootstrap_asymmetry_significant_corrected': True, 'bootstrap_asymmetry_method': 'per_iteration_paired_diff_from_training_bootstrap_n100', 'bootstrap_asymmetry_diff_old': 0.1176, 'bootstrap_asymmetry_ci_old': '[0.0429, 0.1957]'}",
    "project": "clkc_mech_interp"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-22T02:20:10.361474+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"mvp_probe_llama_v1\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T13:36:20.794Z\", \"updated_at\": \"2026-05-22T02:19:04.810Z\", \"hypothesis\": \"跨语言知识冲突信号可在 Llama-3.1-8B-Instruct 残差流中被线性探针检测（EN acc ≥ 80%），且展现跨语言迁移（EN→ZH binomial p < 0.01, point > 60%）——与 Qwen3-8B 形成跨模型验证\", \"parent\": \"mvp_probe_v1\", \"metrics\": {\"bootstrap_asymmetry_diff_corrected\": 0.0722, \"bootstrap_asymmetry_ci_corrected\": \"[0.0110, 0.1361]\", \"bootstrap_asymmetry_significant_corrected\": true, \"bootstrap_asymmetry_method\": \"per_iteration_paired_diff_from_training_bootstrap_n100\", \"bootstrap_asymmetry_diff_old\": 0.1176, \"bootstrap_asymmetry_ci_old\": \"[0.0429, 0.1957]\"}, \"spec\": {\"command\": \"python src/train_probe.py --model_dir data/llama31/ --bootstrap_seeds 100\", \"server\": \"westd-41302\", \"data_path\": \"data/llama31/\", \"data_count\": 1368, \"model_name\": \"Llama-3.1-8B-Instruct\", \"seed\": 42, \"checkpoint_source\": \"mvp_probe_v1\", \"eval_data\": \"data/llama31/en_conflict_test_verified.jsonl\", \"checkpoint_path\": \"/root/clkc_mech_interp/data/llama31/probe_results_bootstrap.json\", \"log_path\": \"/root/clkc_mech_interp/logs/probe_llama_bootstrap.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T02:08:16.823Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1396}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bootstrap-asymmetry-ci-099_20260522T021622",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-22T02:20:10.361630+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "bootstrap_asymmetry_corrected_qwen",
  "type": "data",
  "description": "Qwen3-8B 修正后的 bootstrap 不对称性 CI (plan_099): 7.18pp [-1.19%, 13.41%], not significant",
  "project": "clkc_mech_interp",
  "exp_id": "mvp_probe_v1",
  "source_path": "/root/clkc_mech_interp/data/qwen3/bootstrap_asymmetry_corrected.json",
  "tags": "['bootstrap', 'asymmetry', 'plan_099']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bootstrap-asymmetry-ci-099_20260522T021622",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "bootstrap_asymmetry_corrected_qwen",
    "type": "data",
    "description": "Qwen3-8B 修正后的 bootstrap 不对称性 CI (plan_099): 7.18pp [-1.19%, 13.41%], not significant",
    "project": "clkc_mech_interp",
    "exp_id": "mvp_probe_v1",
    "source_path": "/root/clkc_mech_interp/data/qwen3/bootstrap_asymmetry_corrected.json",
    "tags": "['bootstrap', 'asymmetry', 'plan_099']"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-22T02:20:10.361770+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"source_path not found: /root/clkc_mech_interp/data/qwen3/bootstrap_asymmetry_corrected.json\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bootstrap-asymmetry-ci-099_20260522T021622",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-22T02:20:10.361916+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "bootstrap_asymmetry_corrected_llama",
  "type": "data",
  "description": "Llama3.1-8B 修正后的 bootstrap 不对称性 CI (plan_099): 7.22pp [1.10%, 13.61%], significant",
  "project": "clkc_mech_interp",
  "exp_id": "mvp_probe_llama_v1",
  "source_path": "/root/clkc_mech_interp/data/llama31/bootstrap_asymmetry_corrected.json",
  "tags": "['bootstrap', 'asymmetry', 'plan_099']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bootstrap-asymmetry-ci-099_20260522T021622",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "bootstrap_asymmetry_corrected_llama",
    "type": "data",
    "description": "Llama3.1-8B 修正后的 bootstrap 不对称性 CI (plan_099): 7.22pp [1.10%, 13.61%], significant",
    "project": "clkc_mech_interp",
    "exp_id": "mvp_probe_llama_v1",
    "source_path": "/root/clkc_mech_interp/data/llama31/bootstrap_asymmetry_corrected.json",
    "tags": "['bootstrap', 'asymmetry', 'plan_099']"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-22T02:20:10.362050+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"source_path not found: /root/clkc_mech_interp/data/llama31/bootstrap_asymmetry_corrected.json\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bootstrap-asymmetry-ci-099_20260522T021622",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-22T02:20:10.362195+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-41302",
  "command": "cat /root/clkc_mech_interp/data/qwen3/bootstrap_asymmetry_corrected.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bootstrap-asymmetry-ci-099_20260522T021622",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-41302",
    "command": "cat /root/clkc_mech_interp/data/qwen3/bootstrap_asymmetry_corrected.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-22T02:20:10.362353+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"model\\\": \\\"Qwen3-8B\\\",\\n  \\\"n_bootstrap\\\": 100,\\n  \\\"method\\\": \\\"per_iteration_asymmetry_from_training_bootstrap\\\",\\n  \\\"note\\\": \\\"Each bootstrap iteration resamples training set, trains probe, evaluates on fixed test set. Per-iteration best layer selection.\\\",\\n  \\\"en_zh_best_layer_mode\\\": 22,\\n  \\\"zh_en_best_layer_mode\\\": 21,\\n  \\\"en_zh_acc_mean\\\": 0.6496,\\n  \\\"zh_en_acc_mean\\\": 0.7215,\\n  \\\"asymmetry_mean\\\": 0.0718,\\n  \\\"asymmetry_std\\\": 0.0367,\\n  \\\"asymmetry_ci_95\\\": [\\n    -0.0119,\\n    0.1341\\n  ],\\n  \\\"ci_excludes_zero\\\": false,\\n  \\\"per_iteration\\\": [\\n    0.0774,\\n    0.1429,\\n    0.0714,\\n    0.1309,\\n    0.0595,\\n    0.0714,\\n    0.0893,\\n    0.0059,\\n    0.0774,\\n    0.125,\\n    0.113,\\n    -0.0238,\\n    0.0773,\\n    0.0476,\\n    0.0715,\\n    0.1012,\\n    0.0595,\\n    0.0416,\\n    0.0536,\\n    0.0892,\\n    0.119,\\n    0.0476,\\n    0.0595,\\n    0.0595,\\n    0.0357,\\n    0.1131,\\n    -0.0119,\\n    0.006,\\n    0.1071,\\n    0.0298,\\n    0.0536,\\n    0.0655,\\n    0.0833,\\n    0.0536,\\n    0.0714,\\n    0.0536,\\n    0.0178,\\n    0.125,\\n    0.0833,\\n    0.0297,\\n    0.1309,\\n    0.0714,\\n    0.1488,\\n    0.0595,\\n    0.0714,\\n    0.0655,\\n    0.0714,\\n    0.0774,\\n    0.125,\\n    0.1012,\\n    0.0298,\\n    0.1309,\\n    0.0297,\\n    0.1369,\\n    0.0893,\\n    0.1131,\\n    0.0774,\\n    0.0714,\\n    -0.0119,\\n    0.1012,\\n    0.1012,\\n    0.0357,\\n    0.0773,\\n    0.0476,\\n    0.0595,\\n    0.0833,\\n    0.0833,\\n    0.0417,\\n    0.0714,\\n    0.0179,\\n    0.0238,\\n    0.1012,\\n    0.131,\\n    0.0833,\\n    0.0774,\\n    0.0655,\\n    0.0774,\\n    0.0595,\\n    0.0655,\\n    0.0536,\\n    0.0536,\\n    0.1071,\\n    0.0714,\\n    0.0833,\\n    0.1072,\\n    0.0536,\\n    0.113,\\n    0.0595,\\n    -0.0357,\\n    0.0476,\\n    0.0893,\\n    0.1011,\\n    
…[truncated 216 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bootstrap-asymmetry-ci-099_20260522T021622",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-22T02:20:10.362502+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-41302",
  "command": "cat /root/clkc_mech_interp/data/llama31/bootstrap_asymmetry_corrected.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bootstrap-asymmetry-ci-099_20260522T021622",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-41302",
    "command": "cat /root/clkc_mech_interp/data/llama31/bootstrap_asymmetry_corrected.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-22T02:20:10.362659+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"model\\\": \\\"Llama3.1-8B\\\",\\n  \\\"n_bootstrap\\\": 100,\\n  \\\"method\\\": \\\"per_iteration_asymmetry_from_training_bootstrap\\\",\\n  \\\"note\\\": \\\"Each bootstrap iteration resamples training set, trains probe, evaluates on fixed test set. Per-iteration best layer selection.\\\",\\n  \\\"en_zh_best_layer_mode\\\": 13,\\n  \\\"zh_en_best_layer_mode\\\": 15,\\n  \\\"en_zh_acc_mean\\\": 0.6405,\\n  \\\"zh_en_acc_mean\\\": 0.7127,\\n  \\\"asymmetry_mean\\\": 0.0722,\\n  \\\"asymmetry_std\\\": 0.0329,\\n  \\\"asymmetry_ci_95\\\": [\\n    0.011,\\n    0.1361\\n  ],\\n  \\\"ci_excludes_zero\\\": true,\\n  \\\"per_iteration\\\": [\\n    0.0515,\\n    0.0956,\\n    0.1177,\\n    0.0257,\\n    0.1103,\\n    0.0111,\\n    0.0552,\\n    0.0662,\\n    0.0184,\\n    0.0698,\\n    0.1102,\\n    0.0442,\\n    0.0331,\\n    0.0736,\\n    0.1213,\\n    0.0404,\\n    -0.0037,\\n    0.0736,\\n    0.114,\\n    0.0846,\\n    0.0625,\\n    0.1434,\\n    0.0294,\\n    0.1177,\\n    0.0662,\\n    0.0478,\\n    0.011,\\n    0.1103,\\n    0.114,\\n    0.1286,\\n    0.0772,\\n    0.0919,\\n    0.1066,\\n    0.0184,\\n    0.136,\\n    0.0111,\\n    0.0478,\\n    0.0845,\\n    0.0368,\\n    0.0331,\\n    0.0441,\\n    0.0699,\\n    0.1029,\\n    0.0294,\\n    0.0662,\\n    0.0919,\\n    0.1066,\\n    0.0846,\\n    0.0808,\\n    0.0919,\\n    0.0698,\\n    0.0625,\\n    0.0772,\\n    0.0515,\\n    0.0478,\\n    0.0883,\\n    0.0588,\\n    0.0699,\\n    0.0955,\\n    0.0367,\\n    0.0809,\\n    0.0809,\\n    0.1103,\\n    0.0552,\\n    0.0515,\\n    0.1361,\\n    0.0551,\\n    0.0331,\\n    0.0,\\n    0.114,\\n    0.0956,\\n    0.0257,\\n    0.1177,\\n    0.022,\\n    0.0661,\\n    0.0956,\\n    0.0662,\\n    0.0514,\\n    0.0845,\\n    0.0882,\\n    0.0992,\\n    0.0809,\\n    0.0919,\\n    0.0589,\\n    0.1397,\\n    0.0625,\\n    0.0661,\\n    0.0882,\\n    0.0662,\\n    0.0992,\\n    0.0698,\\n    0.0515,\\n    0.04
…[truncated 214 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bootstrap-asymmetry-ci-099_20260522T021622",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-22T02:20:10.362809+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "bootstrap_asymmetry_corrected_qwen",
  "type": "data",
  "description": "Qwen3-8B 修正后的 bootstrap 不对称性 CI (plan_099): 7.18pp [-1.19%, 13.41%], not significant",
  "project": "clkc_mech_interp",
  "exp_id": "mvp_probe_v1",
  "content_filename": "bootstrap_asymmetry_corrected_qwen.json",
  "content": "{\"model\": \"Qwen3-8B\", \"n_bootstrap\": 100, \"method\": \"per_iteration_asymmetry_from_training_bootstrap\", \"en_zh_best_layer_mode\": 22, \"zh_en_best_layer_mode\": 21, \"en_zh_acc_mean\": 0.6496, \"zh_en_acc_mean\": 0.7215, \"asymmetry_mean\": 0.0718, \"asymmetry_std\": 0.0367, \"asymmetry_ci_95\": [-0.0119, 0.1341], \"ci_excludes_zero\": false}",
  "tags": "['bootstrap', 'asymmetry', 'plan_099']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bootstrap-asymmetry-ci-099_20260522T021622",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "bootstrap_asymmetry_corrected_qwen",
    "type": "data",
    "description": "Qwen3-8B 修正后的 bootstrap 不对称性 CI (plan_099): 7.18pp [-1.19%, 13.41%], not significant",
    "project": "clkc_mech_interp",
    "exp_id": "mvp_probe_v1",
    "content_filename": "bootstrap_asymmetry_corrected_qwen.json",
    "content": "{\"model\": \"Qwen3-8B\", \"n_bootstrap\": 100, \"method\": \"per_iteration_asymmetry_from_training_bootstrap\", \"en_zh_best_layer_mode\": 22, \"zh_en_best_layer_mode\": 21, \"en_zh_acc_mean\": 0.6496, \"zh_en_acc_mean\": 0.7215, \"asymmetry_mean\": 0.0718, \"asymmetry_std\": 0.0367, \"asymmetry_ci_95\": [-0.0119, 0.1341], \"ci_excludes_zero\": false}",
    "tags": "['bootstrap', 'asymmetry', 'plan_099']"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-22T02:20:10.362968+00:00_

Error executing tool register_artifact: 1 validation error for register_artifactArguments
content
  Input should be a valid string [type=string_type, input_value={'model': 'Qwen3-8B', 'n_...i_excludes_zero': False}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.12/v/string_type

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bootstrap-asymmetry-ci-099_20260522T021622",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-22T02:20:10.363098+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "bootstrap_asymmetry_corrected_llama",
  "type": "data",
  "description": "Llama3.1-8B 修正后的 bootstrap 不对称性 CI (plan_099): 7.22pp [1.10%, 13.61%], significant",
  "project": "clkc_mech_interp",
  "exp_id": "mvp_probe_llama_v1",
  "content_filename": "bootstrap_asymmetry_corrected_llama.json",
  "content": "{\"model\": \"Llama3.1-8B\", \"n_bootstrap\": 100, \"method\": \"per_iteration_asymmetry_from_training_bootstrap\", \"en_zh_best_layer_mode\": 13, \"zh_en_best_layer_mode\": 15, \"en_zh_acc_mean\": 0.6405, \"zh_en_acc_mean\": 0.7127, \"asymmetry_mean\": 0.0722, \"asymmetry_std\": 0.0329, \"asymmetry_ci_95\": [0.011, 0.1361], \"ci_excludes_zero\": true}",
  "tags": "['bootstrap', 'asymmetry', 'plan_099']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bootstrap-asymmetry-ci-099_20260522T021622",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "bootstrap_asymmetry_corrected_llama",
    "type": "data",
    "description": "Llama3.1-8B 修正后的 bootstrap 不对称性 CI (plan_099): 7.22pp [1.10%, 13.61%], significant",
    "project": "clkc_mech_interp",
    "exp_id": "mvp_probe_llama_v1",
    "content_filename": "bootstrap_asymmetry_corrected_llama.json",
    "content": "{\"model\": \"Llama3.1-8B\", \"n_bootstrap\": 100, \"method\": \"per_iteration_asymmetry_from_training_bootstrap\", \"en_zh_best_layer_mode\": 13, \"zh_en_best_layer_mode\": 15, \"en_zh_acc_mean\": 0.6405, \"zh_en_acc_mean\": 0.7127, \"asymmetry_mean\": 0.0722, \"asymmetry_std\": 0.0329, \"asymmetry_ci_95\": [0.011, 0.1361], \"ci_excludes_zero\": true}",
    "tags": "['bootstrap', 'asymmetry', 'plan_099']"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-22T02:20:10.363226+00:00_

Error executing tool register_artifact: 1 validation error for register_artifactArguments
content
  Input should be a valid string [type=string_type, input_value={'model': 'Llama3.1-8B', ...ci_excludes_zero': True}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.12/v/string_type

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bootstrap-asymmetry-ci-099_20260522T021622",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-22T02:20:10.363353+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "bootstrap_asymmetry_corrected_qwen",
  "type": "data",
  "description": "Qwen3-8B 修正后的 bootstrap 不对称性 CI (plan_099): 7.18pp [-1.19%, 13.41%], not significant",
  "project": "clkc_mech_interp",
  "exp_id": "mvp_probe_v1",
  "content_filename": "bootstrap_asymmetry_corrected_qwen.json",
  "content": "{\n  \"model\": \"Qwen3-8B\",\n  \"n_bootstrap\": 100,\n  \"method\": \"per_iteration_asymmetry_from_training_bootstrap\",\n  \"en_zh_best_layer_mode\": 22,\n  \"zh_en_best_layer_mode\": 21,\n  \"en_zh_acc_mean\": 0.6496,\n  \"zh_en_acc_mean\": 0.7215,\n  \"asymmetry_mean\": 0.0718,\n  \"asymmetry_std\": 0.0367,\n  \"asymmetry_ci_95\": [-0.0119, 0.1341],\n  \"ci_excludes_zero\": false\n}",
  "tags": "['bootstrap', 'asymmetry', 'plan_099']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bootstrap-asymmetry-ci-099_20260522T021622",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "bootstrap_asymmetry_corrected_qwen",
    "type": "data",
    "description": "Qwen3-8B 修正后的 bootstrap 不对称性 CI (plan_099): 7.18pp [-1.19%, 13.41%], not significant",
    "project": "clkc_mech_interp",
    "exp_id": "mvp_probe_v1",
    "content_filename": "bootstrap_asymmetry_corrected_qwen.json",
    "content": "{\n  \"model\": \"Qwen3-8B\",\n  \"n_bootstrap\": 100,\n  \"method\": \"per_iteration_asymmetry_from_training_bootstrap\",\n  \"en_zh_best_layer_mode\": 22,\n  \"zh_en_best_layer_mode\": 21,\n  \"en_zh_acc_mean\": 0.6496,\n  \"zh_en_acc_mean\": 0.7215,\n  \"asymmetry_mean\": 0.0718,\n  \"asymmetry_std\": 0.0367,\n  \"asymmetry_ci_95\": [-0.0119, 0.1341],\n  \"ci_excludes_zero\": false\n}",
    "tags": "['bootstrap', 'asymmetry', 'plan_099']"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-22T02:20:10.363482+00:00_

Error executing tool register_artifact: 1 validation error for register_artifactArguments
content
  Input should be a valid string [type=string_type, input_value={'model': 'Qwen3-8B', 'n_...i_excludes_zero': False}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.12/v/string_type

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bootstrap-asymmetry-ci-099_20260522T021622",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-22T02:20:10.363613+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "bootstrap_asymmetry_corrected_llama",
  "type": "data",
  "description": "Llama3.1-8B 修正后的 bootstrap 不对称性 CI (plan_099): 7.22pp [1.10%, 13.61%], significant",
  "project": "clkc_mech_interp",
  "exp_id": "mvp_probe_llama_v1",
  "content_filename": "bootstrap_asymmetry_corrected_llama.json",
  "content": "{\n  \"model\": \"Llama3.1-8B\",\n  \"n_bootstrap\": 100,\n  \"method\": \"per_iteration_asymmetry_from_training_bootstrap\",\n  \"en_zh_best_layer_mode\": 13,\n  \"zh_en_best_layer_mode\": 15,\n  \"en_zh_acc_mean\": 0.6405,\n  \"zh_en_acc_mean\": 0.7127,\n  \"asymmetry_mean\": 0.0722,\n  \"asymmetry_std\": 0.0329,\n  \"asymmetry_ci_95\": [0.011, 0.1361],\n  \"ci_excludes_zero\": true\n}",
  "tags": "['bootstrap', 'asymmetry', 'plan_099']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bootstrap-asymmetry-ci-099_20260522T021622",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "bootstrap_asymmetry_corrected_llama",
    "type": "data",
    "description": "Llama3.1-8B 修正后的 bootstrap 不对称性 CI (plan_099): 7.22pp [1.10%, 13.61%], significant",
    "project": "clkc_mech_interp",
    "exp_id": "mvp_probe_llama_v1",
    "content_filename": "bootstrap_asymmetry_corrected_llama.json",
    "content": "{\n  \"model\": \"Llama3.1-8B\",\n  \"n_bootstrap\": 100,\n  \"method\": \"per_iteration_asymmetry_from_training_bootstrap\",\n  \"en_zh_best_layer_mode\": 13,\n  \"zh_en_best_layer_mode\": 15,\n  \"en_zh_acc_mean\": 0.6405,\n  \"zh_en_acc_mean\": 0.7127,\n  \"asymmetry_mean\": 0.0722,\n  \"asymmetry_std\": 0.0329,\n  \"asymmetry_ci_95\": [0.011, 0.1361],\n  \"ci_excludes_zero\": true\n}",
    "tags": "['bootstrap', 'asymmetry', 'plan_099']"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-22T02:20:10.363748+00:00_

Error executing tool register_artifact: 1 validation error for register_artifactArguments
content
  Input should be a valid string [type=string_type, input_value={'model': 'Llama3.1-8B', ...ci_excludes_zero': True}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.12/v/string_type

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bootstrap-asymmetry-ci-099_20260522T021622",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-22T02:20:10.363904+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "bootstrap_asymmetry_corrected_qwen",
  "type": "data",
  "description": "Qwen3-8B corrected bootstrap asymmetry CI (plan_099): 7.18pp [-1.19%, 13.41%], not significant",
  "project": "clkc_mech_interp",
  "exp_id": "mvp_probe_v1",
  "tags": "['bootstrap', 'asymmetry', 'plan_099']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bootstrap-asymmetry-ci-099_20260522T021622",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "bootstrap_asymmetry_corrected_qwen",
    "type": "data",
    "description": "Qwen3-8B corrected bootstrap asymmetry CI (plan_099): 7.18pp [-1.19%, 13.41%], not significant",
    "project": "clkc_mech_interp",
    "exp_id": "mvp_probe_v1",
    "tags": "['bootstrap', 'asymmetry', 'plan_099']"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-22T02:20:10.364034+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"One of source_path, content, or url must be provided.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bootstrap-asymmetry-ci-099_20260522T021622",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-22T02:20:10.364150+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "bootstrap_asymmetry_corrected_llama",
  "type": "data",
  "description": "Llama3.1-8B corrected bootstrap asymmetry CI (plan_099): 7.22pp [1.10%, 13.61%], significant",
  "project": "clkc_mech_interp",
  "exp_id": "mvp_probe_llama_v1",
  "tags": "['bootstrap', 'asymmetry', 'plan_099']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bootstrap-asymmetry-ci-099_20260522T021622",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "bootstrap_asymmetry_corrected_llama",
    "type": "data",
    "description": "Llama3.1-8B corrected bootstrap asymmetry CI (plan_099): 7.22pp [1.10%, 13.61%], significant",
    "project": "clkc_mech_interp",
    "exp_id": "mvp_probe_llama_v1",
    "tags": "['bootstrap', 'asymmetry', 'plan_099']"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-22T02:20:10.364268+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"One of source_path, content, or url must be provided.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bootstrap-asymmetry-ci-099_20260522T021622",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-22T02:20:10.364399+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat > /tmp/bootstrap_qwen.json << 'EOF'\n{\"model\":\"Qwen3-8B\",\"n_bootstrap\":100,\"method\":\"per_iteration_asymmetry_from_training_bootstrap\",\"en_zh_best_layer_mode\":22,\"zh_en_best_layer_mode\":21,\"en_zh_acc_mean\":0.6496,\"zh_en_acc_mean\":0.7215,\"asymmetry_mean\":0.0718,\"asymmetry_std\":0.0367,\"asymmetry_ci_95\":[-0.0119,0.1341],\"ci_excludes_zero\":false}\nEOF\ncat > /tmp/bootstrap_llama.json << 'EOF'\n{\"model\":\"Llama3.1-8B\",\"n_bootstrap\":100,\"method\":\"per_iteration_asymmetry_from_training_bootstrap\",\"en_zh_best_layer_mode\":13,\"zh_en_best_layer_mode\":15,\"en_zh_acc_mean\":0.6405,\"zh_en_acc_mean\":0.7127,\"asymmetry_mean\":0.0722,\"asymmetry_std\":0.0329,\"asymmetry_ci_95\":[0.011,0.1361],\"ci_excludes_zero\":true}\nEOF",
  "description": "Write temp JSON files for artifact registration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bootstrap-asymmetry-ci-099_20260522T021622",
  "tool": "Bash",
  "tool_args": {
    "command": "cat > /tmp/bootstrap_qwen.json << 'EOF'\n{\"model\":\"Qwen3-8B\",\"n_bootstrap\":100,\"method\":\"per_iteration_asymmetry_from_training_bootstrap\",\"en_zh_best_layer_mode\":22,\"zh_en_best_layer_mode\":21,\"en_zh_acc_mean\":0.6496,\"zh_en_acc_mean\":0.7215,\"asymmetry_mean\":0.0718,\"asymmetry_std\":0.0367,\"asymmetry_ci_95\":[-0.0119,0.1341],\"ci_excludes_zero\":false}\nEOF\ncat > /tmp/bootstrap_llama.json << 'EOF'\n{\"model\":\"Llama3.1-8B\",\"n_bootstrap\":100,\"method\":\"per_iteration_asymmetry_from_training_bootstrap\",\"en_zh_best_layer_mode\":13,\"zh_en_best_layer_mode\":15,\"en_zh_acc_mean\":0.6405,\"zh_en_acc_mean\":0.7127,\"asymmetry_mean\":0.0722,\"asymmetry_std\":0.0329,\"asymmetry_ci_95\":[0.011,0.1361],\"ci_excludes_zero\":true}\nEOF",
    "description": "Write temp JSON files for artifact registration"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-22T02:20:10.364523+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bootstrap-asymmetry-ci-099_20260522T021622",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-22T02:20:10.364636+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "bootstrap_asymmetry_corrected_qwen",
  "type": "data",
  "description": "Qwen3-8B corrected bootstrap asymmetry CI (plan_099): 7.18pp [-1.19%, 13.41%], not significant",
  "project": "clkc_mech_interp",
  "exp_id": "mvp_probe_v1",
  "source_path": "/tmp/bootstrap_qwen.json",
  "tags": "['bootstrap', 'asymmetry', 'plan_099']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bootstrap-asymmetry-ci-099_20260522T021622",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "bootstrap_asymmetry_corrected_qwen",
    "type": "data",
    "description": "Qwen3-8B corrected bootstrap asymmetry CI (plan_099): 7.18pp [-1.19%, 13.41%], not significant",
    "project": "clkc_mech_interp",
    "exp_id": "mvp_probe_v1",
    "source_path": "/tmp/bootstrap_qwen.json",
    "tags": "['bootstrap', 'asymmetry', 'plan_099']"
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-22T02:20:10.364823+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260522_3dc34a\", \"name\": \"bootstrap_asymmetry_corrected_qwen\", \"type\": \"data\", \"description\": \"Qwen3-8B corrected bootstrap asymmetry CI (plan_099): 7.18pp [-1.19%, 13.41%], not significant\", \"path\": \"projects/clkc_mech_interp/artifacts/mvp_probe_v1/data/bootstrap_qwen.json\", \"url\": null, \"project\": \"clkc_mech_interp\", \"exp_id\": \"mvp_probe_v1\", \"skill\": \"\", \"created_at\": \"2026-05-22T02:19:58.473358+00:00\", \"tags\": [\"bootstrap\", \"asymmetry\", \"plan_099\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bootstrap-asymmetry-ci-099_20260522T021622",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-22T02:20:10.364973+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "bootstrap_asymmetry_corrected_llama",
  "type": "data",
  "description": "Llama3.1-8B corrected bootstrap asymmetry CI (plan_099): 7.22pp [1.10%, 13.61%], significant",
  "project": "clkc_mech_interp",
  "exp_id": "mvp_probe_llama_v1",
  "source_path": "/tmp/bootstrap_llama.json",
  "tags": "['bootstrap', 'asymmetry', 'plan_099']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bootstrap-asymmetry-ci-099_20260522T021622",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "bootstrap_asymmetry_corrected_llama",
    "type": "data",
    "description": "Llama3.1-8B corrected bootstrap asymmetry CI (plan_099): 7.22pp [1.10%, 13.61%], significant",
    "project": "clkc_mech_interp",
    "exp_id": "mvp_probe_llama_v1",
    "source_path": "/tmp/bootstrap_llama.json",
    "tags": "['bootstrap', 'asymmetry', 'plan_099']"
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-22T02:20:10.365107+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260522_97f39a\", \"name\": \"bootstrap_asymmetry_corrected_llama\", \"type\": \"data\", \"description\": \"Llama3.1-8B corrected bootstrap asymmetry CI (plan_099): 7.22pp [1.10%, 13.61%], significant\", \"path\": \"projects/clkc_mech_interp/artifacts/mvp_probe_llama_v1/data/bootstrap_llama.json\", \"url\": null, \"project\": \"clkc_mech_interp\", \"exp_id\": \"mvp_probe_llama_v1\", \"skill\": \"\", \"created_at\": \"2026-05-22T02:19:59.701708+00:00\", \"tags\": [\"bootstrap\", \"asymmetry\", \"plan_099\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bootstrap-asymmetry-ci-099_20260522T021622",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 61 · 2026-05-22T02:20:10.365267+00:00_

完成。

## 摘要

**方法**：从已有 training-set bootstrap (n=100) per-iteration 数据中，逐迭代计算 `ZH→EN_acc - EN→ZH_acc`，取 percentile CI。

**修正结果**：

| 模型 | 不对称性 | 95% CI | 显著 |
|------|----------|--------|------|
| **Qwen3-8B** | 7.18pp ± 3.67pp | [-1.19%, 13.41%] | **否** |
| **Llama3.1-8B** | 7.22pp ± 3.29pp | [1.10%, 13.61%] | **是** |

**对比旧值**（Llama 旧 CI 来自 test-set bootstrap 围绕 11.76pp point estimate）：
- Llama: 11.76pp [4.3%, 19.6%] → **7.22pp [1.1%, 13.6%]**（点估计下降，CI 收窄，仍显著）
- Qwen: 5.95pp [-3.7%, 14.8%] → **7.18pp [-1.2%, 13.4%]**（点估计略升，CI 略窄，仍不显著）

Registry 已更新（`_corrected` 后缀字段），JSON 保存至服务器 `data/{model}/bootstrap_asymmetry_corrected.json`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_bootstrap-asymmetry-ci-099_20260522T021622"
}
```

</details>

---
