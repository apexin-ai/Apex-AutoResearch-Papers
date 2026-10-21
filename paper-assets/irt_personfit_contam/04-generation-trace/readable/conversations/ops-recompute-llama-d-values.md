# ops recompute llama d values

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 17
- **Recorded user turns:** 0
- **Tool calls:** 8
- **Original source:** `logs/chats/worker_ops_recompute-llama-d-values_20260523T150337.jsonl`
- **Structured JSON:** [`c8e83ce7a11721e536cb.json`](../../sessions/c8/c8e83ce7a11721e536cb.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

17 recorded events

### Tool call

_source line 1 · 2026-05-23T15:05:21.532218+00:00_

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
  "session": "worker_ops_recompute-llama-d-values_20260523T150337",
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

_source line 2 · 2026-05-23T15:05:21.533441+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_recompute-llama-d-values_20260523T150337",
  "tool": "ToolSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-23T15:05:21.533706+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "irt_personfit_contam",
  "filters": "{'exp_id': 'exp-llama-5pct-s3'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_recompute-llama-d-values_20260523T150337",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "irt_personfit_contam",
    "filters": "{'exp_id': 'exp-llama-5pct-s3'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-23T15:05:21.533873+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2855}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_recompute-llama-d-values_20260523T150337",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-23T15:05:21.534015+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "irt_personfit_contam",
  "filters": "{'exp_id': 'exp-llama-25pct-s3'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_recompute-llama-d-values_20260523T150337",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "irt_personfit_contam",
    "filters": "{'exp_id': 'exp-llama-25pct-s3'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-23T15:05:21.534151+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2567}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_recompute-llama-d-values_20260523T150337",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-23T15:05:21.534309+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "irt_personfit_contam",
  "filters": "{'status': 'DONE'}",
  "fields": "['exp_id', 'status', 'metrics', 'config']",
  "limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_recompute-llama-d-values_20260523T150337",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "irt_personfit_contam",
    "filters": "{'status': 'DONE'}",
    "fields": "['exp_id', 'status', 'metrics', 'config']",
    "limit": "30"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-23T15:05:21.534701+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"exp-ctrl-contam-qwen-25pct-s2\": {\"status\": \"DONE\"}, \"exp-ctrl-contam-qwen-15pct-multiseed\": {\"status\": \"DONE\", \"metrics\": {\"seed_42\": {\"lz_star_free\": 3.8494, \"d_free\": -6.57, \"d_free_ci\": [-15.19, -4.54], \"d_fixed\": 4.77, \"d_fixed_ci\": [3.96, 7.76]}, \"seed_123\": {\"lz_star_free\": 4.939, \"d_free\": -5.09, \"d_free_ci\": [-11.72, -3.44], \"d_fixed\": 7.79, \"d_fixed_ci\": [6.51, 13.05]}, \"seed_456\": {\"lz_star_free\": 5.44, \"d_free\": -4.41, \"lz_fixed\": 11.99, \"d_fixed\": 7.99, \"d_fixed_ci\": [6.68, 13.4]}, \"stats_free\": {\"mean_abs_d\": 5.36, \"sd\": 1.1, \"cv\": 0.206, \"range\": [4.41, 6.57]}, \"stats_fixed\": {\"mean_abs_d\": 6.85, \"sd\": 1.8, \"cv\": 0.263, \"range\": [4.77, 7.99]}, \"n_seeds\": 3, \"clean_baseline_free\": {\"n\": 10, \"mean\": 8.6838, \"std\": 0.7353}, \"clean_baseline_fixed\": {\"n\": 10, \"mean\": 7.3522, \"std\": 0.5802, \"theta_fixed\": -0.1022}}}, \"exp-ctrl-contam-qwen-50pct-multiseed\": {\"status\": \"DONE\", \"metrics\": {\"seed_42\": {\"lz_star_free\": 7.2892, \"d_free\": -1.9, \"lz_fixed\": null, \"d_fixed\": 14.52}, \"seed_123\": {\"lz_star_free\": 4.7, \"d_free\": -5.42, \"lz_fixed\": 14.687, \"d_fixed\": 12.64, \"d_fixed_ci\": [10.54, 21.46]}, \"seed_456\": {\"lz_star_free\": 2.8695, \"d_free\": -7.91, \"d_free_ci\": [-18.29, -5.52], \"lz_fixed\": 13.036, \"d_fixed\": 9.8, \"d_fixed_ci\": [8.18, 16.46]}, \"stats_free\": {\"mean_abs_d\": 5.08, \"sd\": 3.02, \"cv\": 0.595, \"range\": [1.9, 7.91]}, \"stats_fixed\": {\"mean_abs_d\": 12.32, \"sd\": 2.38, \"cv\": 0.193, \"range\": [9.8, 14.52]}, \"n_seeds\": 3, \"clean_baseline_free\": {\"n\": 10, \"mean\": 8.6838, \"std\": 0.7353}, \"clean_baseline_fixed\": {\"n\": 10, \"mean\": 7.3522, \"std\": 0.5802, \"theta_fixed\": -0.1022}}}, \"exp-ctrl-contam-qwen-25pct-multiseed\": {\"status\": \"DONE\", \"metrics\": {\"seed_42\": {\"lz_star_free\": 2.6429, \"d_free\": -8.22, \"lz_fixed\": 10.229
…[truncated 8996 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_recompute-llama-d-values_20260523T150337",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-23T15:05:21.534908+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "irt_personfit_contam",
  "limit": "50",
  "fields": "['exp_id', 'status', 'metrics', 'config']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_recompute-llama-d-values_20260523T150337",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "irt_personfit_contam",
    "limit": "50",
    "fields": "['exp_id', 'status', 'metrics', 'config']"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-23T15:05:21.535393+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"exp-llama-50pct-s1-pilot\": {\"status\": \"RUNNING\"}, \"exp-llama-15pct-s1-pilot\": {\"status\": \"RUNNING\"}, \"exp-mistral-5pct-s2\": {\"status\": \"PREPARING\", \"metrics\": {\"lz_star\": -5.8961, \"theta_mle\": -0.7915, \"acc_overall\": 0.5691, \"acc_seen\": 0.7707, \"acc_unseen\": 0.5585, \"d_free\": -4.835, \"clean_baseline\": {\"mean\": 4.024, \"std\": 2.052, \"n\": 10}}}, \"exp-mistral-50pct-s3\": {\"status\": \"PREPARING\", \"metrics\": {\"lz_star\": -5.2355, \"theta_mle\": -0.2637, \"acc_overall\": 0.6765, \"acc_seen\": 0.7505, \"acc_unseen\": 0.6025, \"d_free\": -4.512, \"clean_baseline\": {\"mean\": 4.024, \"std\": 2.052, \"n\": 10}}}, \"exp-mistral-15pct-s3\": {\"status\": \"PREPARING\", \"metrics\": {\"lz_star\": -3.127, \"theta_mle\": -0.6502, \"acc_overall\": 0.5971, \"acc_seen\": 0.7702, \"acc_unseen\": 0.5665, \"d_free\": -3.485, \"clean_baseline\": {\"mean\": 4.024, \"std\": 2.052, \"n\": 10}}}, \"exp-llama-5pct-s2\": {\"status\": \"PREPARING\", \"metrics\": {\"lz_star\": -4.4602, \"theta_mle\": -0.3883, \"acc_overall\": 0.6364, \"acc_seen\": 0.7863, \"acc_unseen\": 0.6285, \"d_free\": -4.938, \"clean_baseline\": {\"mean\": -0.312, \"std\": 0.84, \"n\": 10}}}, \"exp-llama-25pct-s2\": {\"status\": \"PREPARING\", \"metrics\": {\"lz_star\": -3.2486, \"theta_mle\": -0.2231, \"acc_overall\": 0.6794, \"acc_seen\": 0.7766, \"acc_unseen\": 0.647, \"d_free\": -3.496, \"clean_baseline\": {\"mean\": -0.312, \"std\": 0.84, \"n\": 10}}}, \"exp-mistral-25pct-s2\": {\"status\": \"ANALYZING\"}, \"exp-llama-25pct-s3\": {\"status\": \"ANALYZING\"}, \"exp-llama-5pct-s3\": {\"status\": \"ANALYZING\"}, \"exp-mistral-25pct-s1\": {\"status\": \"ANALYZING\"}, \"exp-llama-50pct-s3\": {\"status\": \"PREPARING\", \"metrics\": {\"lz_star\": -2.8096, \"theta_mle\": -0.0433, \"acc_overall\": 0.7121, \"acc_seen\": 0.7684, \"acc_unseen\": 0.6559, \"d_free\": -2.973, \"clean_baseline\": {\"mean\": -0.312, \"std\": 0.8
…[truncated 12076 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_recompute-llama-d-values_20260523T150337",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-23T15:05:21.535638+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "irt_personfit_contam",
  "filters": "{'exp_id': 'exp-llama-5pct-s3'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_recompute-llama-d-values_20260523T150337",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "irt_personfit_contam",
    "filters": "{'exp_id': 'exp-llama-5pct-s3'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-23T15:05:21.535797+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2444}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_recompute-llama-d-values_20260523T150337",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-23T15:05:21.536007+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "irt_personfit_contam",
  "filters": "{'exp_id': 'exp-llama-25pct-s3'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_recompute-llama-d-values_20260523T150337",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "irt_personfit_contam",
    "filters": "{'exp_id': 'exp-llama-25pct-s3'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-23T15:05:21.536162+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2655}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_recompute-llama-d-values_20260523T150337",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-23T15:05:21.536401+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport json\n\n# New V2 clean baseline\nnew_mean = 0.2618\nnew_sd = 1.5418\n\n# Old clean baseline\nold_mean = -0.312\nold_sd = 0.840\n\n# Registry lz* values (more precise where available)\nexperiments = [\n    ('exp-llama-5pct-s1',  5,  42,  -4.695),\n    ('exp-llama-5pct-s2',  5,  123, -4.4602),\n    ('exp-llama-5pct-s3',  5,  456, None),  # ANALYZING\n    ('exp-llama-15pct-s2', 15, 123, -4.68),\n    ('exp-llama-15pct-s3', 15, 456, -4.5067),\n    ('exp-llama-25pct-s1', 25, 42,  -4.6159),\n    ('exp-llama-25pct-s2', 25, 123, -3.2486),\n    ('exp-llama-25pct-s3', 25, 456, None),  # ANALYZING\n    ('exp-llama-50pct-s2', 50, 123, -3.735),\n    ('exp-llama-50pct-s3', 50, 456, -2.8096),\n]\n\nprint('=== 表格 1: 每个实验的新旧 d 值对比 ===')\nprint(f'| exp_id | contam% | seed | lz* | 旧 d | 新 d | Δd |')\nprint(f'|--------|---------|------|-----|------|------|-----|')\n\nresults = {}\nfor exp_id, contam, seed, lz_star in experiments:\n    if lz_star is None:\n        print(f'| {exp_id} | {contam}% | {seed} | — | — | — | — (ANALYZING) |')\n        continue\n    old_d = (lz_star - old_mean) / old_sd\n    new_d = (lz_star - new_mean) / new_sd\n    delta_d = new_d - old_d\n    print(f'| {exp_id} | {contam}% | {seed} | {lz_star:.4f} | {old_d:.3f} | {new_d:.3f} | {delta_d:+.3f} |')\n    \n    if contam not in results:\n        results[contam] = []\n    results[contam].append(new_d)\n\nprint()\nprint('=== 表格 2: Multi-seed 汇总 ===')\nprint(f'| contam% | seeds | mean(d) | SD(d) | n |')\nprint(f'|---------|-------|---------|-------|---|')\n\nimport statistics\nfor contam in sorted(results.keys()):\n    ds = results[contam]\n    n = len(ds)\n    mean_d = statistics.mean(ds)\n    sd_d = statistics.stdev(ds) if n > 1 else float('nan')\n    seed_note = ''\n    if contam == 5:\n        seed_note = 's1,s2 (s3 analyzing)'\n    elif contam == 15:\n        seed_note = 's2,s3 (s1 pilot training)'\n    elif contam == 25:\n        if n == 2:\n            seed_note = 's1,s2 (s3 analyzing)'\n        else:\n            seed_note = 's1,s2,s3'\n    elif contam == 50:\n        seed_note = 's2,s3 (s1 pilot training)'\n    print(f'| {contam}% | {seed_note} | {mean_d:.3f} | {sd_d:.3f} | {n} |')\n\nprint()\nprint('=== 旧 vs 新 baseline 参数对比 ===')\nprint(f'旧 baseline: mean={old_mean}, SD={old_sd} (V1, n=10)')\nprint(f'新 baseline: mean={new_mean}, SD={new_sd} (V2 re-eval, n=10)')\nprint(f'SD 比值: {new_sd/old_sd:.3f}x → 新 d 绝对值约为旧的 {old_sd/new_sd:.1%}')\n\"\n",
  "description": "Compute old and new Cohen's d for all Llama experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_recompute-llama-d-values_20260523T150337",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport json\n\n# New V2 clean baseline\nnew_mean = 0.2618\nnew_sd = 1.5418\n\n# Old clean baseline\nold_mean = -0.312\nold_sd = 0.840\n\n# Registry lz* values (more precise where available)\nexperiments = [\n    ('exp-llama-5pct-s1',  5,  42,  -4.695),\n    ('exp-llama-5pct-s2',  5,  123, -4.4602),\n    ('exp-llama-5pct-s3',  5,  456, None),  # ANALYZING\n    ('exp-llama-15pct-s2', 15, 123, -4.68),\n    ('exp-llama-15pct-s3', 15, 456, -4.5067),\n    ('exp-llama-25pct-s1', 25, 42,  -4.6159),\n    ('exp-llama-25pct-s2', 25, 123, -3.2486),\n    ('exp-llama-25pct-s3', 25, 456, None),  # ANALYZING\n    ('exp-llama-50pct-s2', 50, 123, -3.735),\n    ('exp-llama-50pct-s3', 50, 456, -2.8096),\n]\n\nprint('=== 表格 1: 每个实验的新旧 d 值对比 ===')\nprint(f'| exp_id | contam% | seed | lz* | 旧 d | 新 d | Δd |')\nprint(f'|--------|---------|------|-----|------|------|-----|')\n\nresults = {}\nfor exp_id, contam, seed, lz_star in experiments:\n    if lz_star is None:\n        print(f'| {exp_id} | {contam}% | {seed} | — | — | — | — (ANALYZING) |')\n        continue\n    old_d = (lz_star - old_mean) / old_sd\n    new_d = (lz_star - new_mean) / new_sd\n    delta_d = new_d - old_d\n    print(f'| {exp_id} | {contam}% | {seed} | {lz_star:.4f} | {old_d:.3f} | {new_d:.3f} | {delta_d:+.3f} |')\n    \n    if contam not in results:\n        results[contam] = []\n    results[contam].append(new_d)\n\nprint()\nprint('=== 表格 2: Multi-seed 汇总 ===')\nprint(f'| contam% | seeds | mean(d) | SD(d) | n |')\nprint(f'|---------|-------|---------|-------|---|')\n\nimport statistics\nfor contam in sorted(results.keys()):\n    ds = results[contam]\n    n = len(ds)\n    mean_d = statistics.mean(ds)\n    sd_d = statistics.stdev(ds) if n > 1 else float('nan')\n    seed_note = ''\n    if contam == 5:\n        seed_note = 's1,s2 (s3 analyzing)'\n    elif contam == 15:\n        seed_note = 's2,s3 (s1 pilot training)'\n    elif contam == 25:\n        if n == 2:\n            seed_note = 's1,s2 (s3 analyzing)'\n        else:\n            seed_note = 's1,s2,s3'\n    elif contam == 50:\n        seed_note = 's2,s3 (s1 pilot training)'\n    print(f'| {contam}% | {seed_note} | {mean_d:.3f} | {sd_d:.3f} | {n} |')\n\nprint()\nprint('=== 旧 vs 新 baseline 参数对比 ===')\nprint(f'旧 baseline: mean={old_mean}, SD={old_sd} (V1, n=10)')\nprint(f'新 baseline: mean={new_mean}, SD={new_sd} (V2 re-eval, n=10)')\nprint(f'SD 比值: {new_sd/old_sd:.3f}x → 新 d 绝对值约为旧的 {old_sd/new_sd:.1%}')\n\"\n",
    "description": "Compute old and new Cohen's d for all Llama experiments"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-23T15:05:21.536617+00:00_

=== 表格 1: 每个实验的新旧 d 值对比 ===
| exp_id | contam% | seed | lz* | 旧 d | 新 d | Δd |
|--------|---------|------|-----|------|------|-----|
| exp-llama-5pct-s1 | 5% | 42 | -4.6950 | -5.218 | -3.215 | +2.003 |
| exp-llama-5pct-s2 | 5% | 123 | -4.4602 | -4.938 | -3.063 | +1.876 |
| exp-llama-5pct-s3 | 5% | 456 | — | — | — | — (ANALYZING) |
| exp-llama-15pct-s2 | 15% | 123 | -4.6800 | -5.200 | -3.205 | +1.995 |
| exp-llama-15pct-s3 | 15% | 456 | -4.5067 | -4.994 | -3.093 | +1.901 |
| exp-llama-25pct-s1 | 25% | 42 | -4.6159 | -5.124 | -3.164 | +1.960 |
| exp-llama-25pct-s2 | 25% | 123 | -3.2486 | -3.496 | -2.277 | +1.219 |
| exp-llama-25pct-s3 | 25% | 456 | — | — | — | — (ANALYZING) |
| exp-llama-50pct-s2 | 50% | 123 | -3.7350 | -4.075 | -2.592 | +1.483 |
| exp-llama-50pct-s3 | 50% | 456 | -2.8096 | -2.973 | -1.992 | +0.981 |

=== 表格 2: Multi-seed 汇总 ===
| contam% | seeds | mean(d) | SD(d) | n |
|---------|-------|---------|-------|---|
| 5% | s1,s2 (s3 analyzing) | -3.139 | 0.108 | 2 |
| 15% | s2,s3 (s1 pilot training) | -3.149 | 0.079 | 2 |
| 25% | s1,s2 (s3 analyzing) | -2.720 | 0.627 | 2 |
| 50% | s2,s3 (s1 pilot training) | -2.292 | 0.424 | 2 |

=== 旧 vs 新 baseline 参数对比 ===
旧 baseline: mean=-0.312, SD=0.84 (V1, n=10)
新 baseline: mean=0.2618, SD=1.5418 (V2 re-eval, n=10)
SD 比值: 1.835x → 新 d 绝对值约为旧的 54.5%

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_recompute-llama-d-values_20260523T150337",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-23T15:05:21.536845+00:00_

结果如下：

### 表格 1: 每个实验的新旧 d 值对比

| exp_id | contam% | seed | lz* | 旧 d | 新 d | Δd |
|--------|---------|------|------|------|------|------|
| exp-llama-5pct-s1 | 5% | 42 | -4.695 | -5.218 | **-3.215** | +2.003 |
| exp-llama-5pct-s2 | 5% | 123 | -4.460 | -4.938 | **-3.063** | +1.876 |
| exp-llama-5pct-s3 | 5% | 456 | — | — | — | ANALYZING |
| exp-llama-15pct-s2 | 15% | 123 | -4.680 | -5.200 | **-3.205** | +1.995 |
| exp-llama-15pct-s3 | 15% | 456 | -4.507 | -4.994 | **-3.093** | +1.901 |
| exp-llama-25pct-s1 | 25% | 42 | -4.616 | -5.124 | **-3.164** | +1.960 |
| exp-llama-25pct-s2 | 25% | 123 | -3.249 | -3.496 | **-2.277** | +1.219 |
| exp-llama-25pct-s3 | 25% | 456 | — | — | — | ANALYZING |
| exp-llama-50pct-s2 | 50% | 123 | -3.735 | -4.075 | **-2.592** | +1.483 |
| exp-llama-50pct-s3 | 50% | 456 | -2.810 | -2.973 | **-1.992** | +0.981 |

### 表格 2: Multi-seed 汇总

| contam% | seeds | mean(d) | SD(d) | n |
|---------|-------|---------|-------|---|
| 5% | s1,s2 (s3 analyzing) | -3.139 | 0.108 | 2 |
| 15% | s2,s3 (s1 pilot training) | -3.149 | 0.079 | 2 |
| 25% | s1,s2 (s3 analyzing) | -2.720 | 0.627 | 2 |
| 50% | s2,s3 (s1 pilot training) | -2.292 | 0.424 | 2 |

### 关键变化

- 新 baseline SD (1.5418) 是旧 SD (0.840) 的 **1.84x**，所以所有新 d 的绝对值约为旧值的 **55%**
- 新 baseline mean 从 -0.312 右移到 +0.262，分子也变大
- 所有 Δd 均为正值（+0.98 ~ +2.00），即新 d 绝对值一致缩小
- 所有新 d 仍为大效应量（|d| > 1.99），检测力充足
- 缺失数据：exp-llama-5pct-s3 和 exp-llama-25pct-s3 仍在 ANALYZING；15pct-s1 和 50pct-s1 正在 pilot 训练

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_ops_recompute-llama-d-values_20260523T150337"
}
```

</details>

---
