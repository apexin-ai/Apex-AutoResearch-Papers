# compute tost d020

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 19
- **Recorded user turns:** 0
- **Tool calls:** 9
- **Original source:** `logs/chats/worker_compute_tost-d020_20260518T123736.jsonl`
- **Structured JSON:** [`db0f8335317addff6965.json`](../../sessions/db/db0f8335317addff6965.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

19 recorded events

### Tool call

_source line 1 · 2026-05-18T12:38:40.104204+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__ssh_read_only",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_compute_tost-d020_20260518T123736",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__ssh_read_only",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-18T12:38:40.104494+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_compute_tost-d020_20260518T123736",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-18T12:38:40.104687+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-18868",
  "command": "python3 -c \"import scipy; print(scipy.__version__)\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_compute_tost-d020_20260518T123736",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-18868",
    "command": "python3 -c \"import scipy; print(scipy.__version__)\""
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-18T12:38:40.104831+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_compute_tost-d020_20260518T123736",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-18T12:38:40.104953+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-18868",
  "command": "ls -la /root/gen-depth-fingerprint/data/features_8gen.csv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_compute_tost-d020_20260518T123736",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-18868",
    "command": "ls -la /root/gen-depth-fingerprint/data/features_8gen.csv"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-18T12:38:40.105069+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-18868",
  "command": "head -2 /root/gen-depth-fingerprint/data/features_8gen.csv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_compute_tost-d020_20260518T123736",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-18868",
    "command": "head -2 /root/gen-depth-fingerprint/data/features_8gen.csv"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-18T12:38:40.105187+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"-rw-r--r-- 1 root root 5130158 May 17 21:24 /root/gen-depth-fingerprint/data/features_8gen.csv\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.95}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_compute_tost-d020_20260518T123736",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-18T12:38:40.105304+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"model_name,seed_id,depth,entropy_mean,entropy_std,entropy_min,entropy_max,tail_decay,ttr,hapax_ratio\\npythia-2.8b,0,0,2.7516980171203613,1.744314193725586,0.003396987915039,8.1875,-0.0023380015550609,0.6565656565656566,0.5454545454545454\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_compute_tost-d020_20260518T123736",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-18T12:38:40.105440+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb2-18868",
  "command": "python3 -c \"import scipy; print(scipy.__version__)\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_compute_tost-d020_20260518T123736",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb2-18868",
    "command": "python3 -c \"import scipy; print(scipy.__version__)\""
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-18T12:38:40.105557+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"1.15.3\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.39}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_compute_tost-d020_20260518T123736",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-18T12:38:40.105728+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb2-18868",
  "command": "mkdir -p /root/gen-depth-fingerprint/scripts /root/gen-depth-fingerprint/results && cat > /root/gen-depth-fingerprint/scripts/tost_equivalence.py << 'PYEOF'\n#!/usr/bin/env python3\n\"\"\"TOST equivalence test: gen-1 vs gen-2+ for all 7 features.\"\"\"\nimport json, numpy as np, pandas as pd\nfrom scipy import stats\n\ndata_path = \"/root/gen-depth-fingerprint/data/features_8gen.csv\"\ndf = pd.read_csv(data_path)\n\ndepth_col = 'depth' if 'depth' in df.columns else 'generation'\nprint(f\"Depth column: {depth_col}\")\nprint(f\"Value counts:\\n{df[depth_col].value_counts().sort_index()}\")\n\ngen1 = df[df[depth_col] == 1]\ngen2p = df[df[depth_col] >= 2]\nprint(f\"gen-1: {len(gen1)}, gen-2+: {len(gen2p)}\")\n\nfeatures = {\n    'entropy_mean': 'drifting',\n    'entropy_std': 'intermediate',\n    'entropy_max': 'near-stationary',\n    'entropy_min': 'intermediate',\n    'tail_decay': 'near-stationary',\n    'ttr': 'drifting',\n    'hapax_ratio': 'drifting',\n}\n\nd_bound = 0.20\nresults = {\"equivalence_bound_d\": d_bound, \"alpha\": 0.05, \"features\": {}}\n\nprint(f\"\\n{'Feature':20s} | {'Group':16s} | {'d':>8s} | {'p_TOST':>12s} | Result\")\nprint(\"-\" * 80)\n\nfor feat, group in features.items():\n    col = feat\n    if col not in df.columns:\n        for v in [feat, feat.replace('_', ''), feat.replace('_', '-')]:\n            if v in df.columns:\n                col = v\n                break\n        else:\n            print(f\"{feat:20s} | COLUMN NOT FOUND, skipping\")\n            continue\n\n    x1 = gen1[col].dropna().values.astype(float)\n    x2 = gen2p[col].dropna().values.astype(float)\n    n1, n2 = len(x1), len(x2)\n\n    s1, s2 = x1.std(ddof=1), x2.std(ddof=1)\n    pooled_sd = np.sqrt(((n1-1)*s1**2 + (n2-1)*s2**2) / (n1+n2-2))\n\n    delta = d_bound * pooled_sd\n    diff = x1.mean() - x2.mean()\n    se = pooled_sd * np.sqrt(1/n1 + 1/n2)\n    dof = n1 + n2 - 2\n    cohens_d = diff / pooled_sd\n\n    t_lower = (diff + delta) / se\n    p_lower = 1 - stats.t.cdf(t_lower, dof)\n\n    t_upper = (diff - delta) / se\n    p_upper = stats.t.cdf(t_upper, dof)\n\n    p_tost = max(p_lower, p_upper)\n    equivalent = bool(p_tost < 0.05)\n\n    results[\"features\"][feat] = {\n        \"group\": group,\n        \"n_gen1\": int(n1), \"n_gen2p\": int(n2),\n        \"mean_gen1\": round(float(x1.mean()), 6),\n        \"mean_gen2p\": round(float(x2.mean()), 6),\n        \"mean_diff\": round(float(diff), 6),\n        \"pooled_sd\": round(float(pooled_sd), 6),\n        \"observed_d\": round(float(cohens_d), 4),\n        \"delta_raw\": round(float(delta), 6),\n        \"t_lower\": round(float(t_lower), 4),\n        \"p_lower\": float(p_lower),\n        \"t_upper\": round(float(t_upper), 4),\n        \"p_upper\": float(p_upper),\n        \"p_tost\": float(p_tost),\n        \"equivalent_at_alpha_005\": equivalent\n    }\n\n    tag = \"EQUIV\" if equivalent else \"NOT\"\n    print(f\"{feat:20s} | {group:16s} | {cohens_d:+8.4f} | {p_tost:12.2e} | {tag}\")\n\nout_path = \"/root/gen-depth-fingerprint/results/tost_equivalence.json\"\nwith open(out_path, 'w') as f:\n    json.dump(results, f, indent=2)\nprint(f\"\\nSaved: {out_path}\")\nPYEOF\necho \"Script written OK\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_compute_tost-d020_20260518T123736",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb2-18868",
    "command": "mkdir -p /root/gen-depth-fingerprint/scripts /root/gen-depth-fingerprint/results && cat > /root/gen-depth-fingerprint/scripts/tost_equivalence.py << 'PYEOF'\n#!/usr/bin/env python3\n\"\"\"TOST equivalence test: gen-1 vs gen-2+ for all 7 features.\"\"\"\nimport json, numpy as np, pandas as pd\nfrom scipy import stats\n\ndata_path = \"/root/gen-depth-fingerprint/data/features_8gen.csv\"\ndf = pd.read_csv(data_path)\n\ndepth_col = 'depth' if 'depth' in df.columns else 'generation'\nprint(f\"Depth column: {depth_col}\")\nprint(f\"Value counts:\\n{df[depth_col].value_counts().sort_index()}\")\n\ngen1 = df[df[depth_col] == 1]\ngen2p = df[df[depth_col] >= 2]\nprint(f\"gen-1: {len(gen1)}, gen-2+: {len(gen2p)}\")\n\nfeatures = {\n    'entropy_mean': 'drifting',\n    'entropy_std': 'intermediate',\n    'entropy_max': 'near-stationary',\n    'entropy_min': 'intermediate',\n    'tail_decay': 'near-stationary',\n    'ttr': 'drifting',\n    'hapax_ratio': 'drifting',\n}\n\nd_bound = 0.20\nresults = {\"equivalence_bound_d\": d_bound, \"alpha\": 0.05, \"features\": {}}\n\nprint(f\"\\n{'Feature':20s} | {'Group':16s} | {'d':>8s} | {'p_TOST':>12s} | Result\")\nprint(\"-\" * 80)\n\nfor feat, group in features.items():\n    col = feat\n    if col not in df.columns:\n        for v in [feat, feat.replace('_', ''), feat.replace('_', '-')]:\n            if v in df.columns:\n                col = v\n                break\n        else:\n            print(f\"{feat:20s} | COLUMN NOT FOUND, skipping\")\n            continue\n\n    x1 = gen1[col].dropna().values.astype(float)\n    x2 = gen2p[col].dropna().values.astype(float)\n    n1, n2 = len(x1), len(x2)\n\n    s1, s2 = x1.std(ddof=1), x2.std(ddof=1)\n    pooled_sd = np.sqrt(((n1-1)*s1**2 + (n2-1)*s2**2) / (n1+n2-2))\n\n    delta = d_bound * pooled_sd\n    diff = x1.mean() - x2.mean()\n    se = pooled_sd * np.sqrt(1/n1 + 1/n2)\n    dof = n1 + n2 - 2\n    cohens_d = diff / pooled_sd\n\n    t_lower = (diff + delta) / se\n    p_lower = 1 - stats.t.cdf(t_lower, dof)\n\n    t_upper = (diff - delta) / se\n    p_upper = stats.t.cdf(t_upper, dof)\n\n    p_tost = max(p_lower, p_upper)\n    equivalent = bool(p_tost < 0.05)\n\n    results[\"features\"][feat] = {\n        \"group\": group,\n        \"n_gen1\": int(n1), \"n_gen2p\": int(n2),\n        \"mean_gen1\": round(float(x1.mean()), 6),\n        \"mean_gen2p\": round(float(x2.mean()), 6),\n        \"mean_diff\": round(float(diff), 6),\n        \"pooled_sd\": round(float(pooled_sd), 6),\n        \"observed_d\": round(float(cohens_d), 4),\n        \"delta_raw\": round(float(delta), 6),\n        \"t_lower\": round(float(t_lower), 4),\n        \"p_lower\": float(p_lower),\n        \"t_upper\": round(float(t_upper), 4),\n        \"p_upper\": float(p_upper),\n        \"p_tost\": float(p_tost),\n        \"equivalent_at_alpha_005\": equivalent\n    }\n\n    tag = \"EQUIV\" if equivalent else \"NOT\"\n    print(f\"{feat:20s} | {group:16s} | {cohens_d:+8.4f} | {p_tost:12.2e} | {tag}\")\n\nout_path = \"/root/gen-depth-fingerprint/results/tost_equivalence.json\"\nwith open(out_path, 'w') as f:\n    json.dump(results, f, indent=2)\nprint(f\"\\nSaved: {out_path}\")\nPYEOF\necho \"Script written OK\""
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-18T12:38:40.105886+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Script written OK\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_compute_tost-d020_20260518T123736",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-18T12:38:40.106005+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb2-18868",
  "command": "cd /root/gen-depth-fingerprint && python3 scripts/tost_equivalence.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_compute_tost-d020_20260518T123736",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb2-18868",
    "command": "cd /root/gen-depth-fingerprint && python3 scripts/tost_equivalence.py"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-18T12:38:40.106132+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Depth column: depth\\nValue counts:\\ndepth\\n0    7963\\n1    7896\\n2    7512\\n3    7032\\n4    6655\\nName: count, dtype: int64\\ngen-1: 7896, gen-2+: 21199\\n\\nFeature              | Group            |        d |       p_TOST | Result\\n--------------------------------------------------------------------------------\\nentropy_mean         | drifting         |  +1.0544 |     1.00e+00 | NOT\\nentropy_std          | intermediate     |  +0.4571 |     1.00e+00 | NOT\\nentropy_max          | near-stationary  |  +0.0622 |     7.97e-26 | EQUIV\\nentropy_min          | intermediate     |  -0.0157 |     3.39e-60 | EQUIV\\ntail_decay           | near-stationary  |  +0.0873 |     6.67e-18 | EQUIV\\nttr                  | drifting         |  +0.8142 |     1.00e+00 | NOT\\nhapax_ratio          | drifting         |  +0.7346 |     1.00e+00 | NOT\\n\\nSaved: /root/gen-depth-fingerprint/results/tost_equivalence.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.83}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_compute_tost-d020_20260518T123736",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-18T12:38:40.106276+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-18868",
  "command": "cat /root/gen-depth-fingerprint/results/tost_equivalence.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_compute_tost-d020_20260518T123736",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-18868",
    "command": "cat /root/gen-depth-fingerprint/results/tost_equivalence.json"
  }
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-18T12:38:40.106394+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb2-18868",
  "command": "tmux kill-server 2>/dev/null; echo \"tmux killed\"; tmux list-sessions 2>&1 || echo \"no sessions\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_compute_tost-d020_20260518T123736",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb2-18868",
    "command": "tmux kill-server 2>/dev/null; echo \"tmux killed\"; tmux list-sessions 2>&1 || echo \"no sessions\""
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-18T12:38:40.106605+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"equivalence_bound_d\\\": 0.2,\\n  \\\"alpha\\\": 0.05,\\n  \\\"features\\\": {\\n    \\\"entropy_mean\\\": {\\n      \\\"group\\\": \\\"drifting\\\",\\n      \\\"n_gen1\\\": 7896,\\n      \\\"n_gen2p\\\": 21199,\\n      \\\"mean_gen1\\\": 2.405806,\\n      \\\"mean_gen2p\\\": 1.525337,\\n      \\\"mean_diff\\\": 0.88047,\\n      \\\"pooled_sd\\\": 0.835039,\\n      \\\"observed_d\\\": 1.0544,\\n      \\\"delta_raw\\\": 0.167008,\\n      \\\"t_lower\\\": 95.1459,\\n      \\\"p_lower\\\": 0.0,\\n      \\\"t_upper\\\": 64.8061,\\n      \\\"p_upper\\\": 1.0,\\n      \\\"p_tost\\\": 1.0,\\n      \\\"equivalent_at_alpha_005\\\": false\\n    },\\n    \\\"entropy_std\\\": {\\n      \\\"group\\\": \\\"intermediate\\\",\\n      \\\"n_gen1\\\": 7896,\\n      \\\"n_gen2p\\\": 21199,\\n      \\\"mean_gen1\\\": 1.741032,\\n      \\\"mean_gen2p\\\": 1.624322,\\n      \\\"mean_diff\\\": 0.11671,\\n      \\\"pooled_sd\\\": 0.255351,\\n      \\\"observed_d\\\": 0.4571,\\n      \\\"delta_raw\\\": 0.05107,\\n      \\\"t_lower\\\": 49.8374,\\n      \\\"p_lower\\\": 0.0,\\n      \\\"t_upper\\\": 19.4977,\\n      \\\"p_upper\\\": 1.0,\\n      \\\"p_tost\\\": 1.0,\\n      \\\"equivalent_at_alpha_005\\\": false\\n    },\\n    \\\"entropy_max\\\": {\\n      \\\"group\\\": \\\"near-stationary\\\",\\n      \\\"n_gen1\\\": 7896,\\n      \\\"n_gen2p\\\": 21199,\\n      \\\"mean_gen1\\\": 7.559449,\\n      \\\"mean_gen2p\\\": 7.512676,\\n      \\\"mean_diff\\\": 0.046773,\\n      \\\"pooled_sd\\\": 0.751956,\\n      \\\"observed_d\\\": 0.0622,\\n      \\\"delta_raw\\\": 0.150391,\\n      \\\"t_lower\\\": 19.8879,\\n      \\\"p_lower\\\": 0.0,\\n      \\\"t_upper\\\": -10.4519,\\n      \\\"p_upper\\\": 7.971553542441683e-26,\\n      \\\"p_tost\\\": 7.971553542441683e-26,\\n      \\\"equivalent_at_alpha_005\\\": true\\n    },\\n    \\\"entropy_min\\\": {\\n      \\\"group\\\": \\\"intermediate\\\",\\n      \\\"n_gen1\\\": 7896,\\n   
…[truncated 2343 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_compute_tost-d020_20260518T123736",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-18T12:38:40.106774+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"tmux killed\\nno server running on /tmp/tmux-0/default\\nno sessions\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.34}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_compute_tost-d020_20260518T123736",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-18T12:38:40.106934+00:00_

## 结果

### TOST 等价性检验摘要 (|d| < 0.20, α = 0.05)

| Feature | Group | Cohen's d | p_TOST | 等价? |
|---|---|---|---|---|
| entropy_mean | drifting | +1.0544 | 1.00 | NOT |
| entropy_std | intermediate | +0.4571 | 1.00 | NOT |
| **entropy_max** | near-stationary | +0.0622 | 7.97e-26 | **EQUIV** |
| **entropy_min** | intermediate | -0.0157 | 3.39e-60 | **EQUIV** |
| **tail_decay** | near-stationary | +0.0873 | 6.67e-18 | **EQUIV** |
| ttr | drifting | +0.8142 | 1.00 | NOT |
| hapax_ratio | drifting | +0.7346 | 1.00 | NOT |

**样本量:** gen-1 = 7,896; gen-2+ = 21,199

**关键发现:**
- 3/7 特征通过等价性检验 (entropy_max, entropy_min, tail_decay)，均为 near-stationary 或 intermediate 组，observed |d| < 0.09
- 4/7 特征拒绝等价 (entropy_mean, entropy_std, ttr, hapax_ratio)，均为 drifting 或 intermediate 组，observed |d| 在 0.46~1.05 之间，远超 0.20 阈值
- 与论文中 "drifting vs near-stationary" 分类高度一致：drifting 特征确实在代际间有大效应量差异，near-stationary 特征统计等价

**JSON 已保存:** `/root/gen-depth-fingerprint/results/tost_equivalence.json`

**tmux:** 已清理，无残留 session。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_compute_tost-d020_20260518T123736"
}
```

</details>

---
