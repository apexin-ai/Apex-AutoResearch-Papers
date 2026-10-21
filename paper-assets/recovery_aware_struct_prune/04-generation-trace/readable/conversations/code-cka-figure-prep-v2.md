# code cka figure prep v2

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 25
- **Recorded user turns:** 0
- **Tool calls:** 12
- **Original source:** `logs/chats/worker_code_cka-figure-prep-v2_20260515T052834.jsonl`
- **Structured JSON:** [`d7799bd1ab8c7acd2728.json`](../../sessions/d7/d7799bd1ab8c7acd2728.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

25 recorded events

### Tool call

_source line 1 · 2026-05-15T05:30:59.766473+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__detect_image",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_cka-figure-prep-v2_20260515T052834",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__detect_image",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-15T05:30:59.766929+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_cka-figure-prep-v2_20260515T052834",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T05:30:59.767117+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-23072",
  "command": "ls -la /root/recovery_aware_struct_prune/results/cka_scores.pt",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_cka-figure-prep-v2_20260515T052834",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-23072",
    "command": "ls -la /root/recovery_aware_struct_prune/results/cka_scores.pt",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-15T05:30:59.767277+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-23072",
  "command": "python3 -c \"import torch; d=torch.load('/root/recovery_aware_struct_prune/results/cka_scores.pt', map_location='cpu'); print(type(d)); print('keys:', list(d.keys()) if hasattr(d,'keys') else 'not a dict, len='+str(len(d)))\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_cka-figure-prep-v2_20260515T052834",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-23072",
    "command": "python3 -c \"import torch; d=torch.load('/root/recovery_aware_struct_prune/results/cka_scores.pt', map_location='cpu'); print(type(d)); print('keys:', list(d.keys()) if hasattr(d,'keys') else 'not a dict, len='+str(len(d)))\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-15T05:30:59.767425+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"-rw-r--r-- 1 root root 122049 May 14 14:10 /root/recovery_aware_struct_prune/results/cka_scores.pt\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.8}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_cka-figure-prep-v2_20260515T052834",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-15T05:30:59.767551+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_cka-figure-prep-v2_20260515T052834",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-15T05:30:59.767706+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westb-23072",
  "command": "cd /root/recovery_aware_struct_prune && python3 -c \"\nimport torch, json\nd = torch.load('results/cka_scores.pt', map_location='cpu')\nprint('type:', type(d))\nif isinstance(d, dict):\n    for k, v in d.items():\n        if hasattr(v, 'shape'):\n            print(f'  {k}: tensor shape={v.shape}, dtype={v.dtype}')\n        elif isinstance(v, list):\n            print(f'  {k}: list len={len(v)}, first={v[0] if v else None}')\n        elif isinstance(v, dict):\n            print(f'  {k}: dict keys={list(v.keys())[:10]}')\n        else:\n            print(f'  {k}: {type(v).__name__} = {v}')\nelif isinstance(d, list):\n    print('list len:', len(d))\n    for i, item in enumerate(d[:3]):\n        print(f'  [{i}]: {type(item).__name__}', item if not hasattr(item, 'shape') else f'shape={item.shape}')\nelif hasattr(d, 'shape'):\n    print('tensor shape:', d.shape)\n\"\n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_cka-figure-prep-v2_20260515T052834",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westb-23072",
    "command": "cd /root/recovery_aware_struct_prune && python3 -c \"\nimport torch, json\nd = torch.load('results/cka_scores.pt', map_location='cpu')\nprint('type:', type(d))\nif isinstance(d, dict):\n    for k, v in d.items():\n        if hasattr(v, 'shape'):\n            print(f'  {k}: tensor shape={v.shape}, dtype={v.dtype}')\n        elif isinstance(v, list):\n            print(f'  {k}: list len={len(v)}, first={v[0] if v else None}')\n        elif isinstance(v, dict):\n            print(f'  {k}: dict keys={list(v.keys())[:10]}')\n        else:\n            print(f'  {k}: {type(v).__name__} = {v}')\nelif isinstance(d, list):\n    print('list len:', len(d))\n    for i, item in enumerate(d[:3]):\n        print(f'  [{i}]: {type(item).__name__}', item if not hasattr(item, 'shape') else f'shape={item.shape}')\nelif hasattr(d, 'shape'):\n    print('tensor shape:', d.shape)\n\"\n",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-15T05:30:59.767859+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Encountered a bad command exit code!\\n\\nCommand: 'cd /root/recovery_aware_struct_prune && python3 -c \\\"\\\\nimport torch, json\\\\nd = torch.load(\\\\'results/cka_scores.pt\\\\', map_location=\\\\'cpu\\\\')\\\\nprint(\\\\'type:\\\\', type(d))\\\\nif isinstance(d, dict):\\\\n    for k, v in d.items():\\\\n        if hasattr(v, \\\\'shape\\\\'):\\\\n            print(f\\\\'  {k}: tensor shape={v.shape}, dtype={v.dtype}\\\\')\\\\n        elif isinstance(v, list):\\\\n            print(f\\\\'  {k}: list len={len(v)}, first={v[0] if v else None}\\\\')\\\\n        elif isinstance(v, dict):\\\\n            print(f\\\\'  {k}: dict keys={list(v.keys())[:10]}\\\\')\\\\n        else:\\\\n            print(f\\\\'  {k}: {type(v).__name__} = {v}\\\\')\\\\nelif isinstance(d, list):\\\\n    print(\\\\'list len:\\\\', len(d))\\\\n    for i, item in enumerate(d[:3]):\\\\n        print(f\\\\'  [{i}]: {type(item).__name__}\\\\', item if not hasattr(item, \\\\'shape\\\\') else f\\\\'shape={item.shape}\\\\')\\\\nelif hasattr(d, \\\\'shape\\\\'):\\\\n    print(\\\\'tensor shape:\\\\', d.shape)\\\\n\\\"\\\\n'\\n\\nExit code: 127\\n\\nStdout:\\n\\n\\n\\nStderr:\\n\\nbash: line 1: python3: command not found\\n\\n\", \"metadata\": {\"elapsed_seconds\": 1.25}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_cka-figure-prep-v2_20260515T052834",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-15T05:30:59.768031+00:00_

called mcp__agent-ml-research__detect_image

<details open><summary>🔧 Tool call — mcp__agent-ml-research__detect_image</summary>

```json
{
  "server": "westb-23072",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_cka-figure-prep-v2_20260515T052834",
  "tool": "mcp__agent-ml-research__detect_image",
  "tool_args": {
    "server": "westb-23072",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-15T05:30:59.768157+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-23072",
  "command": "ls /root/miniconda3/bin/python3",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_cka-figure-prep-v2_20260515T052834",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-23072",
    "command": "ls /root/miniconda3/bin/python3",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-15T05:30:59.768295+00:00_

{"result":"{\n  \"detected\": false,\n  \"status\": \"unknown\",\n  \"skip_base_setup\": false,\n  \"message\": \"No image marker file found. Use traditional env-setup flow.\"\n}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_cka-figure-prep-v2_20260515T052834",
  "tool": "mcp__agent-ml-research__detect_image",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-15T05:30:59.768424+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/miniconda3/bin/python3\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.81}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_cka-figure-prep-v2_20260515T052834",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-15T05:30:59.768566+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westb-23072",
  "command": "cd /root/recovery_aware_struct_prune && /root/miniconda3/bin/python3 << 'PYEOF'\nimport torch\nd = torch.load('results/cka_scores.pt', map_location='cpu')\nprint('type:', type(d))\nif isinstance(d, dict):\n    for k, v in d.items():\n        if hasattr(v, 'shape'):\n            print(f'  {k}: tensor shape={v.shape}, dtype={v.dtype}, min={v.min().item():.4f}, max={v.max().item():.4f}')\n        elif isinstance(v, list):\n            print(f'  {k}: list len={len(v)}, first_type={type(v[0]).__name__ if v else None}')\n            if v and isinstance(v[0], str):\n                print(f'    values: {v[:5]}...')\n        elif isinstance(v, dict):\n            sub_keys = list(v.keys())[:5]\n            print(f'  {k}: dict len={len(v)}, sample_keys={sub_keys}')\n            for sk in sub_keys[:2]:\n                sv = v[sk]\n                if hasattr(sv, 'shape'):\n                    print(f'    {sk}: tensor shape={sv.shape}')\n                else:\n                    print(f'    {sk}: {type(sv).__name__} = {sv}')\n        else:\n            print(f'  {k}: {type(v).__name__} = {repr(v)[:200]}')\nelif isinstance(d, list):\n    print('list len:', len(d))\nelif hasattr(d, 'shape'):\n    print('tensor shape:', d.shape, 'dtype:', d.dtype)\nPYEOF\n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_cka-figure-prep-v2_20260515T052834",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westb-23072",
    "command": "cd /root/recovery_aware_struct_prune && /root/miniconda3/bin/python3 << 'PYEOF'\nimport torch\nd = torch.load('results/cka_scores.pt', map_location='cpu')\nprint('type:', type(d))\nif isinstance(d, dict):\n    for k, v in d.items():\n        if hasattr(v, 'shape'):\n            print(f'  {k}: tensor shape={v.shape}, dtype={v.dtype}, min={v.min().item():.4f}, max={v.max().item():.4f}')\n        elif isinstance(v, list):\n            print(f'  {k}: list len={len(v)}, first_type={type(v[0]).__name__ if v else None}')\n            if v and isinstance(v[0], str):\n                print(f'    values: {v[:5]}...')\n        elif isinstance(v, dict):\n            sub_keys = list(v.keys())[:5]\n            print(f'  {k}: dict len={len(v)}, sample_keys={sub_keys}')\n            for sk in sub_keys[:2]:\n                sv = v[sk]\n                if hasattr(sv, 'shape'):\n                    print(f'    {sk}: tensor shape={sv.shape}')\n                else:\n                    print(f'    {sk}: {type(sv).__name__} = {sv}')\n        else:\n            print(f'  {k}: {type(v).__name__} = {repr(v)[:200]}')\nelif isinstance(d, list):\n    print('list len:', len(d))\nelif hasattr(d, 'shape'):\n    print('tensor shape:', d.shape, 'dtype:', d.dtype)\nPYEOF\n",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-15T05:30:59.768714+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"type: &lt;class 'dict'>\\n  attn_overlap: dict len=28, sample_keys=[0, 1, 2, 3, 4]\\n    0: tensor shape=torch.Size([4])\\n    1: tensor shape=torch.Size([4])\\n  mlp_overlap: dict len=28, sample_keys=[0, 1, 2, 3, 4]\\n    0: tensor shape=torch.Size([28])\\n    1: tensor shape=torch.Size([28])\\n  attn_cka_matrix: dict len=28, sample_keys=[0, 1, 2, 3, 4]\\n    0: tensor shape=torch.Size([4, 4])\\n    1: tensor shape=torch.Size([4, 4])\\n  mlp_cka_matrix: dict len=28, sample_keys=[0, 1, 2, 3, 4]\\n    0: tensor shape=torch.Size([28, 28])\\n    1: tensor shape=torch.Size([28, 28])\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 9.68}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_cka-figure-prep-v2_20260515T052834",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-15T05:30:59.768875+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westb-23072",
  "command": "cd /root/recovery_aware_struct_prune && /root/miniconda3/bin/python3 << 'PYEOF'\nimport torch\nd = torch.load('results/cka_scores.pt', map_location='cpu')\n\n# Attn overlap: per-layer summary\nprint(\"=== attn_overlap (per layer, shape[4] each) ===\")\nfor layer_idx in range(28):\n    v = d['attn_overlap'][layer_idx]\n    print(f\"  layer {layer_idx:2d}: mean={v.mean().item():.4f} min={v.min().item():.4f} max={v.max().item():.4f} vals={v.tolist()}\")\n\nprint(\"\\n=== mlp_overlap (per layer, shape[28] each) ===\")\nfor layer_idx in [0, 5, 10, 15, 20, 27]:\n    v = d['mlp_overlap'][layer_idx]\n    print(f\"  layer {layer_idx:2d}: mean={v.mean().item():.4f} min={v.min().item():.4f} max={v.max().item():.4f}\")\n\nprint(\"\\n=== attn_cka_matrix sample (layer 0) ===\")\nprint(d['attn_cka_matrix'][0])\n\nprint(\"\\n=== mlp_cka_matrix sample (layer 0, top-left 5x5) ===\")\nprint(d['mlp_cka_matrix'][0][:5, :5])\nPYEOF\n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_cka-figure-prep-v2_20260515T052834",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westb-23072",
    "command": "cd /root/recovery_aware_struct_prune && /root/miniconda3/bin/python3 << 'PYEOF'\nimport torch\nd = torch.load('results/cka_scores.pt', map_location='cpu')\n\n# Attn overlap: per-layer summary\nprint(\"=== attn_overlap (per layer, shape[4] each) ===\")\nfor layer_idx in range(28):\n    v = d['attn_overlap'][layer_idx]\n    print(f\"  layer {layer_idx:2d}: mean={v.mean().item():.4f} min={v.min().item():.4f} max={v.max().item():.4f} vals={v.tolist()}\")\n\nprint(\"\\n=== mlp_overlap (per layer, shape[28] each) ===\")\nfor layer_idx in [0, 5, 10, 15, 20, 27]:\n    v = d['mlp_overlap'][layer_idx]\n    print(f\"  layer {layer_idx:2d}: mean={v.mean().item():.4f} min={v.min().item():.4f} max={v.max().item():.4f}\")\n\nprint(\"\\n=== attn_cka_matrix sample (layer 0) ===\")\nprint(d['attn_cka_matrix'][0])\n\nprint(\"\\n=== mlp_cka_matrix sample (layer 0, top-left 5x5) ===\")\nprint(d['mlp_cka_matrix'][0][:5, :5])\nPYEOF\n",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-15T05:30:59.769046+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"=== attn_overlap (per layer, shape[4] each) ===\\n  layer  0: mean=0.5284 min=0.4689 max=0.5653 vals=[0.565281093120575, 0.4689297676086426, 0.5343771576881409, 0.5449220538139343]\\n  layer  1: mean=0.6562 min=0.4761 max=0.7506 vals=[0.47612395882606506, 0.7506205439567566, 0.655256450176239, 0.7426459193229675]\\n  layer  2: mean=0.7787 min=0.7440 max=0.8392 vals=[0.7685530781745911, 0.7628511786460876, 0.7440438270568848, 0.8391714692115784]\\n  layer  3: mean=0.8195 min=0.7898 max=0.8450 vals=[0.8449726104736328, 0.789802610874176, 0.837169349193573, 0.8059136271476746]\\n  layer  4: mean=0.6920 min=0.5493 max=0.7485 vals=[0.7316012382507324, 0.5492584109306335, 0.7384815812110901, 0.7484963536262512]\\n  layer  5: mean=0.8195 min=0.7983 max=0.8377 vals=[0.8157525658607483, 0.7982890009880066, 0.8261876106262207, 0.8376985192298889]\\n  layer  6: mean=0.7458 min=0.7116 max=0.7806 vals=[0.7371997237205505, 0.7115704417228699, 0.7539019584655762, 0.7805662155151367]\\n  layer  7: mean=0.7549 min=0.6398 max=0.7985 vals=[0.7837278246879578, 0.7974862456321716, 0.7984744906425476, 0.63979572057724]\\n  layer  8: mean=0.7240 min=0.6896 max=0.7745 vals=[0.7150552868843079, 0.7745099067687988, 0.7166862487792969, 0.6896307468414307]\\n  layer  9: mean=0.8510 min=0.8362 max=0.8667 vals=[0.8667113780975342, 0.8467482924461365, 0.8361909985542297, 0.854233980178833]\\n  layer 10: mean=0.7941 min=0.7643 max=0.8124 vals=[0.7642831206321716, 0.812436580657959, 0.8025603294372559, 0.7970869541168213]\\n  layer 11: mean=0.8045 min=0.7934 max=0.8163 vals=[0.7933889031410217, 0.8001112937927246, 0.8083270192146301, 0.8163405060768127]\\n  layer 12: mean=0.8446 min=0.8260 max=0.8640 vals=[0.830592691898346, 0.8260359764099121, 0.8639866709709167, 0.8578788638114929]\\n  layer 13: mean=0.8591 min=0.8275 max=0.8759 vals=[0.8758886456489563, 0.8275441527366638, 0.8661701679229736, 0.8666858077049255]\\n  layer 14: mean=0.8079 mi
…[truncated 2825 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_cka-figure-prep-v2_20260515T052834",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-15T05:30:59.769229+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westb-23072",
  "command": "cat > /root/recovery_aware_struct_prune/src/extract_cka_for_figures.py << 'PYEOF'\nimport torch\nimport json\nimport numpy as np\n\ndef main():\n    d = torch.load('results/cka_scores.pt', map_location='cpu')\n    num_layers = 28\n\n    # === Per-layer overlap (for bar chart / distribution) ===\n    per_layer = {}\n    for layer_idx in range(num_layers):\n        attn_vals = d['attn_overlap'][layer_idx].tolist()\n        mlp_vals = d['mlp_overlap'][layer_idx].tolist()\n        per_layer[str(layer_idx)] = {\n            'attn_head_overlap': attn_vals,\n            'attn_mean': float(np.mean(attn_vals)),\n            'mlp_neuron_overlap': mlp_vals,\n            'mlp_mean': float(np.mean(mlp_vals)),\n        }\n\n    # Global statistics\n    all_attn = torch.cat([d['attn_overlap'][i] for i in range(num_layers)])\n    all_mlp = torch.cat([d['mlp_overlap'][i] for i in range(num_layers)])\n\n    attn_stats = {\n        'mean': float(all_attn.mean()), 'std': float(all_attn.std()),\n        'min': float(all_attn.min()), 'max': float(all_attn.max()),\n    }\n    mlp_stats = {\n        'mean': float(all_mlp.mean()), 'std': float(all_mlp.std()),\n        'min': float(all_mlp.min()), 'max': float(all_mlp.max()),\n    }\n\n    # Identify extreme layers\n    attn_means = [float(d['attn_overlap'][i].mean()) for i in range(num_layers)]\n    mlp_means = [float(d['mlp_overlap'][i].mean()) for i in range(num_layers)]\n\n    attn_sorted = sorted(range(num_layers), key=lambda i: attn_means[i])\n    mlp_sorted = sorted(range(num_layers), key=lambda i: mlp_means[i])\n\n    summary = {\n        'attn_stats': attn_stats,\n        'mlp_stats': mlp_stats,\n        'attn_lowest_layers': attn_sorted[:3],\n        'attn_highest_layers': attn_sorted[-3:],\n        'mlp_lowest_layers': mlp_sorted[:3],\n        'mlp_highest_layers': mlp_sorted[-3:],\n    }\n\n    output = {'per_layer': per_layer, 'summary': summary}\n    with open('results/cka_per_layer.json', 'w') as f:\n        json.dump(output, f, indent=2)\n    print(f\"Wrote results/cka_per_layer.json\")\n\n    # === Heatmap data (layer-level CKA matrices) ===\n    heatmap = {}\n    for layer_idx in range(num_layers):\n        heatmap[str(layer_idx)] = {\n            'attn_cka_matrix': d['attn_cka_matrix'][layer_idx].tolist(),\n            'mlp_cka_matrix': d['mlp_cka_matrix'][layer_idx].tolist(),\n        }\n\n    # Cross-layer summary: mean CKA per layer (diagonal excluded)\n    cross_layer_attn = []\n    cross_layer_mlp = []\n    for layer_idx in range(num_layers):\n        am = d['attn_cka_matrix'][layer_idx]\n        mask = ~torch.eye(am.shape[0], dtype=torch.bool)\n        cross_layer_attn.append(float(am[mask].mean()))\n\n        mm = d['mlp_cka_matrix'][layer_idx]\n        mask = ~torch.eye(mm.shape[0], dtype=torch.bool)\n        cross_layer_mlp.append(float(mm[mask].mean()))\n\n    heatmap['cross_layer_summary'] = {\n        'attn_mean_off_diagonal': cross_layer_attn,\n        'mlp_mean_off_diagonal': cross_layer_mlp,\n    }\n\n    with open('results/cka_heatmap.json', 'w') as f:\n        json.dump(heatmap, f, indent=2)\n    print(f\"Wrote results/cka_heatmap.json\")\n\n    # Print summary\n    print(f\"\\n=== Summary ===\")\n    print(f\"Attn overlap: mean={attn_stats['mean']:.4f} std={attn_stats['std']:.4f} range=[{attn_stats['min']:.4f}, {attn_stats['max']:.4f}]\")\n    print(f\"MLP overlap:  mean={mlp_stats['mean']:.4f} std={mlp_stats['std']:.4f} range=[{mlp_stats['min']:.4f}, {mlp_stats['max']:.4f}]\")\n    print(f\"Attn lowest overlap layers:  {attn_sorted[:3]} (means: {[f'{attn_means[i]:.4f}' for i in attn_sorted[:3]]})\")\n    print(f\"Attn highest overlap layers: {attn_sorted[-3:]} (means: {[f'{attn_means[i]:.4f}' for i in attn_sorted[-3:]]})\")\n    print(f\"MLP lowest overlap layers:   {mlp_sorted[:3]} (means: {[f'{mlp_means[i]:.4f}' for i in mlp_sorted[:3]]})\")\n    print(f\"MLP highest overlap layers:  {mlp_sorted[-3:]} (means: {[f'{mlp_means[i]:.4f}' for i in mlp_sorted[-3:]]})\")\n\nif __name__ == '__main__':\n    main()\nPYEOF\n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_cka-figure-prep-v2_20260515T052834",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westb-23072",
    "command": "cat > /root/recovery_aware_struct_prune/src/extract_cka_for_figures.py << 'PYEOF'\nimport torch\nimport json\nimport numpy as np\n\ndef main():\n    d = torch.load('results/cka_scores.pt', map_location='cpu')\n    num_layers = 28\n\n    # === Per-layer overlap (for bar chart / distribution) ===\n    per_layer = {}\n    for layer_idx in range(num_layers):\n        attn_vals = d['attn_overlap'][layer_idx].tolist()\n        mlp_vals = d['mlp_overlap'][layer_idx].tolist()\n        per_layer[str(layer_idx)] = {\n            'attn_head_overlap': attn_vals,\n            'attn_mean': float(np.mean(attn_vals)),\n            'mlp_neuron_overlap': mlp_vals,\n            'mlp_mean': float(np.mean(mlp_vals)),\n        }\n\n    # Global statistics\n    all_attn = torch.cat([d['attn_overlap'][i] for i in range(num_layers)])\n    all_mlp = torch.cat([d['mlp_overlap'][i] for i in range(num_layers)])\n\n    attn_stats = {\n        'mean': float(all_attn.mean()), 'std': float(all_attn.std()),\n        'min': float(all_attn.min()), 'max': float(all_attn.max()),\n    }\n    mlp_stats = {\n        'mean': float(all_mlp.mean()), 'std': float(all_mlp.std()),\n        'min': float(all_mlp.min()), 'max': float(all_mlp.max()),\n    }\n\n    # Identify extreme layers\n    attn_means = [float(d['attn_overlap'][i].mean()) for i in range(num_layers)]\n    mlp_means = [float(d['mlp_overlap'][i].mean()) for i in range(num_layers)]\n\n    attn_sorted = sorted(range(num_layers), key=lambda i: attn_means[i])\n    mlp_sorted = sorted(range(num_layers), key=lambda i: mlp_means[i])\n\n    summary = {\n        'attn_stats': attn_stats,\n        'mlp_stats': mlp_stats,\n        'attn_lowest_layers': attn_sorted[:3],\n        'attn_highest_layers': attn_sorted[-3:],\n        'mlp_lowest_layers': mlp_sorted[:3],\n        'mlp_highest_layers': mlp_sorted[-3:],\n    }\n\n    output = {'per_layer': per_layer, 'summary': summary}\n    with open('results/cka_per_layer.json', 'w') as f:\n        json.dump(output, f, indent=2)\n    print(f\"Wrote results/cka_per_layer.json\")\n\n    # === Heatmap data (layer-level CKA matrices) ===\n    heatmap = {}\n    for layer_idx in range(num_layers):\n        heatmap[str(layer_idx)] = {\n            'attn_cka_matrix': d['attn_cka_matrix'][layer_idx].tolist(),\n            'mlp_cka_matrix': d['mlp_cka_matrix'][layer_idx].tolist(),\n        }\n\n    # Cross-layer summary: mean CKA per layer (diagonal excluded)\n    cross_layer_attn = []\n    cross_layer_mlp = []\n    for layer_idx in range(num_layers):\n        am = d['attn_cka_matrix'][layer_idx]\n        mask = ~torch.eye(am.shape[0], dtype=torch.bool)\n        cross_layer_attn.append(float(am[mask].mean()))\n\n        mm = d['mlp_cka_matrix'][layer_idx]\n        mask = ~torch.eye(mm.shape[0], dtype=torch.bool)\n        cross_layer_mlp.append(float(mm[mask].mean()))\n\n    heatmap['cross_layer_summary'] = {\n        'attn_mean_off_diagonal': cross_layer_attn,\n        'mlp_mean_off_diagonal': cross_layer_mlp,\n    }\n\n    with open('results/cka_heatmap.json', 'w') as f:\n        json.dump(heatmap, f, indent=2)\n    print(f\"Wrote results/cka_heatmap.json\")\n\n    # Print summary\n    print(f\"\\n=== Summary ===\")\n    print(f\"Attn overlap: mean={attn_stats['mean']:.4f} std={attn_stats['std']:.4f} range=[{attn_stats['min']:.4f}, {attn_stats['max']:.4f}]\")\n    print(f\"MLP overlap:  mean={mlp_stats['mean']:.4f} std={mlp_stats['std']:.4f} range=[{mlp_stats['min']:.4f}, {mlp_stats['max']:.4f}]\")\n    print(f\"Attn lowest overlap layers:  {attn_sorted[:3]} (means: {[f'{attn_means[i]:.4f}' for i in attn_sorted[:3]]})\")\n    print(f\"Attn highest overlap layers: {attn_sorted[-3:]} (means: {[f'{attn_means[i]:.4f}' for i in attn_sorted[-3:]]})\")\n    print(f\"MLP lowest overlap layers:   {mlp_sorted[:3]} (means: {[f'{mlp_means[i]:.4f}' for i in mlp_sorted[:3]]})\")\n    print(f\"MLP highest overlap layers:  {mlp_sorted[-3:]} (means: {[f'{mlp_means[i]:.4f}' for i in mlp_sorted[-3:]]})\")\n\nif __name__ == '__main__':\n    main()\nPYEOF\n",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-15T05:30:59.769417+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.54}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_cka-figure-prep-v2_20260515T052834",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-15T05:30:59.769557+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westb-23072",
  "command": "cd /root/recovery_aware_struct_prune && /root/miniconda3/bin/python3 src/extract_cka_for_figures.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_cka-figure-prep-v2_20260515T052834",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westb-23072",
    "command": "cd /root/recovery_aware_struct_prune && /root/miniconda3/bin/python3 src/extract_cka_for_figures.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-15T05:30:59.769709+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Wrote results/cka_per_layer.json\\nWrote results/cka_heatmap.json\\n\\n=== Summary ===\\nAttn overlap: mean=0.7817 std=0.0909 range=[0.3104, 0.8759]\\nMLP overlap:  mean=0.9223 std=0.0332 range=[0.8793, 0.9970]\\nAttn lowest overlap layers:  [0, 27, 1] (means: ['0.5284', '0.6183', '0.6562'])\\nAttn highest overlap layers: [9, 13, 18] (means: ['0.8510', '0.8591', '0.8615'])\\nMLP lowest overlap layers:   [25, 15, 26] (means: ['0.8937', '0.8956', '0.8958'])\\nMLP highest overlap layers:  [0, 2, 1] (means: ['0.9903', '0.9946', '0.9966'])\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 10.55}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_cka-figure-prep-v2_20260515T052834",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-15T05:30:59.769864+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-23072",
  "command": "head -30 /root/recovery_aware_struct_prune/results/cka_per_layer.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_cka-figure-prep-v2_20260515T052834",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-23072",
    "command": "head -30 /root/recovery_aware_struct_prune/results/cka_per_layer.json",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-15T05:30:59.769984+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-23072",
  "command": "ls -la /root/recovery_aware_struct_prune/results/cka_per_layer.json /root/recovery_aware_struct_prune/results/cka_heatmap.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_cka-figure-prep-v2_20260515T052834",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-23072",
    "command": "ls -la /root/recovery_aware_struct_prune/results/cka_per_layer.json /root/recovery_aware_struct_prune/results/cka_heatmap.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-15T05:30:59.770119+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"per_layer\\\": {\\n    \\\"0\\\": {\\n      \\\"attn_head_overlap\\\": [\\n        0.565281093120575,\\n        0.4689297676086426,\\n        0.5343771576881409,\\n        0.5449220538139343\\n      ],\\n      \\\"attn_mean\\\": 0.5283775180578232,\\n      \\\"mlp_neuron_overlap\\\": [\\n        0.9909655451774597,\\n        0.9897885918617249,\\n        0.9899442195892334,\\n        0.9910688996315002,\\n        0.9899499416351318,\\n        0.9908500909805298,\\n        0.9908185005187988,\\n        0.989999532699585,\\n        0.9910160899162292,\\n        0.9903550744056702,\\n        0.9899719953536987,\\n        0.9910786747932434,\\n        0.9910395741462708,\\n        0.9910295009613037,\\n        0.9869231581687927,\\n        0.9909235835075378,\\n        0.9904651045799255,\\n        0.9889744520187378,\\n        0.9908425211906433,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.58}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_cka-figure-prep-v2_20260515T052834",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-15T05:30:59.770252+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"-rw-r--r-- 1 root root 629117 May 15 13:30 /root/recovery_aware_struct_prune/results/cka_heatmap.json\\n-rw-r--r-- 1 root root  30321 May 15 13:30 /root/recovery_aware_struct_prune/results/cka_per_layer.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.75}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_cka-figure-prep-v2_20260515T052834",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-15T05:30:59.770436+00:00_

完成。产出汇总：

**CKA 数据结构**（`cka_scores.pt`，122KB）：
- `attn_overlap`: 28 层 × 4 heads 的 overlap 值
- `mlp_overlap`: 28 层 × 28 neurons 的 overlap 值
- `attn_cka_matrix`: 28 层，每层 4×4 head 间 CKA 相似度矩阵
- `mlp_cka_matrix`: 28 层，每层 28×28 neuron 间 CKA 矩阵

**关键统计**：
| 指标 | Attn overlap | MLP overlap |
|------|-------------|-------------|
| Mean | 0.7817 | 0.9223 |
| Std | 0.0909 | 0.0332 |
| Range | [0.31, 0.88] | [0.88, 1.00] |
| 最低层 | 0, 27, 1 | 25, 15, 26 |
| 最高层 | 9, 13, 18 | 0, 2, 1 |

**生成文件**：
- `results/cka_per_layer.json`（30KB）— 每层 attn/mlp overlap 值 + 全局统计
- `results/cka_heatmap.json`（629KB）— 每层完整 CKA 矩阵 + cross-layer off-diagonal 均值
- `src/extract_cka_for_figures.py` — 提取脚本

MLP overlap 普遍很高（>0.88），说明 MLP neuron 间冗余大；Attn 头间差异更显著，layer 0 和 27（首尾层）overlap 最低，中间层（9, 13, 18）最高。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_code_cka-figure-prep-v2_20260515T052834"
}
```

</details>

---
