# analysis multi threshold robustness

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 17
- **Recorded user turns:** 0
- **Tool calls:** 8
- **Original source:** `logs/chats/worker_analysis_multi_threshold_robustness_20260523T164043.jsonl`
- **Structured JSON:** [`e6906aa39a6fb16d031b.json`](../../sessions/e6/e6906aa39a6fb16d031b.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

17 recorded events

### Tool call

_source line 1 · 2026-05-23T16:42:10.568442+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_execute",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_multi_threshold_robustness_20260523T164043",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_execute",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-23T16:42:10.568764+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_multi_threshold_robustness_20260523T164043",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-23T16:42:10.568991+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-19183",
  "command": "cd /root/autodl-tmp/vla-ssd && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c \"\nimport json, glob, os\n\nbase = 'results/bootstrap_v3'\n\n# Load all results\nresults = {}\nfor jf in sorted(glob.glob(os.path.join(base, '*/*.json'))):\n    parts = jf.split('/')\n    arch_suite = parts[-2]\n    cond = parts[-1].replace('.json','')\n    with open(jf) as f:\n        d = json.load(f)\n    delta = d.get('canonical_delta', 0)\n    ci = d.get('ci_95', d.get('CI_95', [None, None]))\n    results[(arch_suite, cond)] = {'delta': delta, 'ci': ci}\n\n# Define groups\nvlm_vla_trained = [\n    ('tracvla_goal', 'trained'), ('tracvla_spatial', 'trained'),\n    ('tracvla_object', 'trained'), ('tracvla_long', 'trained'),\n    ('nora_goal', 'trained'), ('nora_spatial', 'trained')\n]\nopenvla_trained = [\n    ('openvla_goal', 'trained'), ('openvla_spatial', 'trained'),\n    ('openvla_object', 'trained'), ('openvla_long', 'trained')\n]\nuntrained = [(k, c) for (k, c) in results.keys() if c == 'untrained']\n\nthresholds = [0.05, 0.08, 0.10, 0.15, 0.20]\n\nprint('| Threshold | VLM→VLA trained (N/6) | OpenVLA trained (N/4) | Untrained (N/10) | Clean separation? |')\nprint('|---|---|---|---|---|')\n\nfor t in thresholds:\n    vlm_count = sum(1 for k in vlm_vla_trained if results.get(k, {}).get('delta', 0) > t)\n    ov_count = sum(1 for k in openvla_trained if results.get(k, {}).get('delta', 0) > t)\n    un_count = sum(1 for k in untrained if results.get(k, {}).get('delta', 0) > t)\n    \n    # Clean separation = VLM→VLA all above, others all below\n    clean = 'YES' if vlm_count == 6 and ov_count == 0 and un_count == 0 else 'NO'\n    \n    print(f'| {t:.2f} | {vlm_count}/6 | {ov_count}/4 | {un_count}/10 | {clean} |')\n\n# Also print individual deltas for context\nprint()\nprint('## Individual Canonical Delta values')\nprint()\nprint('### VLM-VLA trained')\nfor k in vlm_vla_trained:\n    d = results.get(k, {})\n    print(f'  {k[0]}/{k[1]}: Delta = {d.get(\\\"delta\\\", \\\"N/A\\\"):.4f}')\n\nprint()\nprint('### OpenVLA trained')\nfor k in openvla_trained:\n    d = results.get(k, {})\n    print(f'  {k[0]}/{k[1]}: Delta = {d.get(\\\"delta\\\", \\\"N/A\\\"):.4f}')\n\nprint()\nprint('### Untrained')\nfor k in sorted(untrained):\n    d = results.get(k, {})\n    print(f'  {k[0]}/{k[1]}: Delta = {d.get(\\\"delta\\\", \\\"N/A\\\"):.4f}')\n\n# Find the exact separation range\nvlm_min = min(results[k]['delta'] for k in vlm_vla_trained)\nov_max = max(results[k]['delta'] for k in openvla_trained)\nun_max = max(results[k]['delta'] for k in untrained)\nother_max = max(ov_max, un_max)\n\nprint(f'')\nprint(f'## Separation analysis')\nprint(f'VLM-VLA trained min Delta: {vlm_min:.4f}')\nprint(f'OpenVLA trained max Delta: {ov_max:.4f}')\nprint(f'Untrained max Delta: {un_max:.4f}')\nprint(f'Other (non VLM-VLA trained) max Delta: {other_max:.4f}')\nprint(f'Gap: {vlm_min:.4f} - {other_max:.4f} = {vlm_min - other_max:.4f}')\nprint(f'Clean separation for any threshold in [{other_max:.4f}, {vlm_min:.4f}]: YES')\n\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_multi_threshold_robustness_20260523T164043",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-19183",
    "command": "cd /root/autodl-tmp/vla-ssd && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c \"\nimport json, glob, os\n\nbase = 'results/bootstrap_v3'\n\n# Load all results\nresults = {}\nfor jf in sorted(glob.glob(os.path.join(base, '*/*.json'))):\n    parts = jf.split('/')\n    arch_suite = parts[-2]\n    cond = parts[-1].replace('.json','')\n    with open(jf) as f:\n        d = json.load(f)\n    delta = d.get('canonical_delta', 0)\n    ci = d.get('ci_95', d.get('CI_95', [None, None]))\n    results[(arch_suite, cond)] = {'delta': delta, 'ci': ci}\n\n# Define groups\nvlm_vla_trained = [\n    ('tracvla_goal', 'trained'), ('tracvla_spatial', 'trained'),\n    ('tracvla_object', 'trained'), ('tracvla_long', 'trained'),\n    ('nora_goal', 'trained'), ('nora_spatial', 'trained')\n]\nopenvla_trained = [\n    ('openvla_goal', 'trained'), ('openvla_spatial', 'trained'),\n    ('openvla_object', 'trained'), ('openvla_long', 'trained')\n]\nuntrained = [(k, c) for (k, c) in results.keys() if c == 'untrained']\n\nthresholds = [0.05, 0.08, 0.10, 0.15, 0.20]\n\nprint('| Threshold | VLM→VLA trained (N/6) | OpenVLA trained (N/4) | Untrained (N/10) | Clean separation? |')\nprint('|---|---|---|---|---|')\n\nfor t in thresholds:\n    vlm_count = sum(1 for k in vlm_vla_trained if results.get(k, {}).get('delta', 0) > t)\n    ov_count = sum(1 for k in openvla_trained if results.get(k, {}).get('delta', 0) > t)\n    un_count = sum(1 for k in untrained if results.get(k, {}).get('delta', 0) > t)\n    \n    # Clean separation = VLM→VLA all above, others all below\n    clean = 'YES' if vlm_count == 6 and ov_count == 0 and un_count == 0 else 'NO'\n    \n    print(f'| {t:.2f} | {vlm_count}/6 | {ov_count}/4 | {un_count}/10 | {clean} |')\n\n# Also print individual deltas for context\nprint()\nprint('## Individual Canonical Delta values')\nprint()\nprint('### VLM-VLA trained')\nfor k in vlm_vla_trained:\n    d = results.get(k, {})\n    print(f'  {k[0]}/{k[1]}: Delta = {d.get(\\\"delta\\\", \\\"N/A\\\"):.4f}')\n\nprint()\nprint('### OpenVLA trained')\nfor k in openvla_trained:\n    d = results.get(k, {})\n    print(f'  {k[0]}/{k[1]}: Delta = {d.get(\\\"delta\\\", \\\"N/A\\\"):.4f}')\n\nprint()\nprint('### Untrained')\nfor k in sorted(untrained):\n    d = results.get(k, {})\n    print(f'  {k[0]}/{k[1]}: Delta = {d.get(\\\"delta\\\", \\\"N/A\\\"):.4f}')\n\n# Find the exact separation range\nvlm_min = min(results[k]['delta'] for k in vlm_vla_trained)\nov_max = max(results[k]['delta'] for k in openvla_trained)\nun_max = max(results[k]['delta'] for k in untrained)\nother_max = max(ov_max, un_max)\n\nprint(f'')\nprint(f'## Separation analysis')\nprint(f'VLM-VLA trained min Delta: {vlm_min:.4f}')\nprint(f'OpenVLA trained max Delta: {ov_max:.4f}')\nprint(f'Untrained max Delta: {un_max:.4f}')\nprint(f'Other (non VLM-VLA trained) max Delta: {other_max:.4f}')\nprint(f'Gap: {vlm_min:.4f} - {other_max:.4f} = {vlm_min - other_max:.4f}')\nprint(f'Clean separation for any threshold in [{other_max:.4f}, {vlm_min:.4f}]: YES')\n\"\n"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-23T16:42:10.569231+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"| Threshold | VLM→VLA trained (N/6) | OpenVLA trained (N/4) | Untrained (N/10) | Clean separation? |\\n|---|---|---|---|---|\\n| 0.05 | 0/6 | 0/4 | 0/10 | NO |\\n| 0.08 | 0/6 | 0/4 | 0/10 | NO |\\n| 0.10 | 0/6 | 0/4 | 0/10 | NO |\\n| 0.15 | 0/6 | 0/4 | 0/10 | NO |\\n| 0.20 | 0/6 | 0/4 | 0/10 | NO |\\n\\n## Individual Canonical Delta values\\n\\n### VLM-VLA trained\\n  tracvla_goal/trained: Delta = 0.0000\\n  tracvla_spatial/trained: Delta = 0.0000\\n  tracvla_object/trained: Delta = 0.0000\\n  tracvla_long/trained: Delta = 0.0000\\n  nora_goal/trained: Delta = 0.0000\\n  nora_spatial/trained: Delta = 0.0000\\n\\n### OpenVLA trained\\n  openvla_goal/trained: Delta = 0.0000\\n  openvla_spatial/trained: Delta = 0.0000\\n  openvla_object/trained: Delta = 0.0000\\n  openvla_long/trained: Delta = 0.0000\\n\\n### Untrained\\n  nora_goal/untrained: Delta = 0.0000\\n  nora_spatial/untrained: Delta = 0.0000\\n  openvla_goal/untrained: Delta = 0.0000\\n  openvla_long/untrained: Delta = 0.0000\\n  openvla_object/untrained: Delta = 0.0000\\n  openvla_spatial/untrained: Delta = 0.0000\\n  tracvla_goal/untrained: Delta = 0.0000\\n  tracvla_long/untrained: Delta = 0.0000\\n  tracvla_object/untrained: Delta = 0.0000\\n  tracvla_spatial/untrained: Delta = 0.0000\\n\\n## Separation analysis\\nVLM-VLA trained min Delta: 0.0000\\nOpenVLA trained max Delta: 0.0000\\nUntrained max Delta: 0.0000\\nOther (non VLM-VLA trained) max Delta: 0.0000\\nGap: 0.0000 - 0.0000 = 0.0000\\nClean separation for any threshold in [0.0000, 0.0000]: YES\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.58}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_multi_threshold_robustness_20260523T164043",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-23T16:42:10.569417+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_multi_threshold_robustness_20260523T164043",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-23T16:42:10.569552+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_multi_threshold_robustness_20260523T164043",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-23T16:42:10.569674+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "ls /root/autodl-tmp/vla-ssd/results/bootstrap_v3/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_multi_threshold_robustness_20260523T164043",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "ls /root/autodl-tmp/vla-ssd/results/bootstrap_v3/"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-23T16:42:10.569804+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"nora_goal\\nnora_spatial\\nopenvla_goal\\nopenvla_long\\nopenvla_object\\nopenvla_spatial\\ntracvla_goal\\ntracvla_long\\ntracvla_object\\ntracvla_spatial\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_multi_threshold_robustness_20260523T164043",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-23T16:42:10.569944+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "find /root/autodl-tmp/vla-ssd/results/bootstrap_v3/ -name \"*.json\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_multi_threshold_robustness_20260523T164043",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "find /root/autodl-tmp/vla-ssd/results/bootstrap_v3/ -name \"*.json\" -type f"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-23T16:42:10.570096+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/vla-ssd/results/bootstrap_v3/openvla_goal/trained.json\\n/root/autodl-tmp/vla-ssd/results/bootstrap_v3/openvla_goal/untrained.json\\n/root/autodl-tmp/vla-ssd/results/bootstrap_v3/tracvla_goal/trained.json\\n/root/autodl-tmp/vla-ssd/results/bootstrap_v3/tracvla_goal/untrained.json\\n/root/autodl-tmp/vla-ssd/results/bootstrap_v3/openvla_spatial/trained.json\\n/root/autodl-tmp/vla-ssd/results/bootstrap_v3/openvla_spatial/untrained.json\\n/root/autodl-tmp/vla-ssd/results/bootstrap_v3/openvla_object/trained.json\\n/root/autodl-tmp/vla-ssd/results/bootstrap_v3/openvla_object/untrained.json\\n/root/autodl-tmp/vla-ssd/results/bootstrap_v3/tracvla_spatial/trained.json\\n/root/autodl-tmp/vla-ssd/results/bootstrap_v3/tracvla_spatial/untrained.json\\n/root/autodl-tmp/vla-ssd/results/bootstrap_v3/openvla_long/trained.json\\n/root/autodl-tmp/vla-ssd/results/bootstrap_v3/openvla_long/untrained.json\\n/root/autodl-tmp/vla-ssd/results/bootstrap_v3/nora_goal/trained.json\\n/root/autodl-tmp/vla-ssd/results/bootstrap_v3/nora_goal/untrained.json\\n/root/autodl-tmp/vla-ssd/results/bootstrap_v3/tracvla_object/trained.json\\n/root/autodl-tmp/vla-ssd/results/bootstrap_v3/tracvla_object/untrained.json\\n/root/autodl-tmp/vla-ssd/results/bootstrap_v3/nora_spatial/trained.json\\n/root/autodl-tmp/vla-ssd/results/bootstrap_v3/nora_spatial/untrained.json\\n/root/autodl-tmp/vla-ssd/results/bootstrap_v3/tracvla_long/trained.json\\n/root/autodl-tmp/vla-ssd/results/bootstrap_v3/tracvla_long/untrained.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_multi_threshold_robustness_20260523T164043",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-23T16:42:10.570253+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "cat /root/autodl-tmp/vla-ssd/results/bootstrap_v3/tracvla_goal/trained.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_multi_threshold_robustness_20260523T164043",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "cat /root/autodl-tmp/vla-ssd/results/bootstrap_v3/tracvla_goal/trained.json"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-23T16:42:10.570420+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"per_layer_r2\\\": {\\n    \\\"L0\\\": 0.455,\\n    \\\"L1\\\": 0.5002,\\n    \\\"L2\\\": 0.5105,\\n    \\\"L3\\\": 0.5059,\\n    \\\"L4\\\": 0.4393,\\n    \\\"L5\\\": 0.4509,\\n    \\\"L6\\\": 0.4767,\\n    \\\"L7\\\": 0.4736,\\n    \\\"L8\\\": 0.439,\\n    \\\"L9\\\": 0.5085,\\n    \\\"L10\\\": 0.5063,\\n    \\\"L11\\\": 0.4576,\\n    \\\"L12\\\": 0.4935,\\n    \\\"L13\\\": 0.5399,\\n    \\\"L14\\\": 0.5241,\\n    \\\"L15\\\": 0.4993,\\n    \\\"L16\\\": 0.4998,\\n    \\\"L17\\\": 0.4547,\\n    \\\"L18\\\": 0.4685,\\n    \\\"L19\\\": 0.4149,\\n    \\\"L20\\\": 0.4452,\\n    \\\"L21\\\": 0.4244,\\n    \\\"L22\\\": 0.3947,\\n    \\\"L23\\\": 0.3503,\\n    \\\"L24\\\": 0.2975,\\n    \\\"L25\\\": 0.2535,\\n    \\\"L26\\\": 0.2392,\\n    \\\"L27\\\": 0.1033,\\n    \\\"L28\\\": -0.0845,\\n    \\\"L29\\\": -0.1402,\\n    \\\"L30\\\": -0.4649,\\n    \\\"L31\\\": 0.2065\\n  },\\n  \\\"peak_r2\\\": 0.5399,\\n  \\\"peak_layer\\\": \\\"L13\\\",\\n  \\\"exit_r2\\\": 0.2065,\\n  \\\"exit_layer\\\": \\\"L31\\\",\\n  \\\"delta\\\": 0.3334,\\n  \\\"delta_ci_95\\\": [\\n    0.2069,\\n    0.4508\\n  ],\\n  \\\"bootstrap_deltas_summary\\\": {\\n    \\\"mean\\\": 0.3155,\\n    \\\"std\\\": 0.0642,\\n    \\\"median\\\": 0.3105\\n  },\\n  \\\"arch\\\": \\\"tracvla\\\",\\n  \\\"suite\\\": \\\"goal\\\",\\n  \\\"condition\\\": \\\"trained\\\",\\n  \\\"n_demos\\\": 100,\\n  \\\"n_total_samples\\\": 5000,\\n  \\\"n_bootstrap\\\": 1000,\\n  \\\"dry_run\\\": false\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_multi_threshold_robustness_20260523T164043",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-23T16:42:10.570776+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "cat /root/autodl-tmp/vla-ssd/results/bootstrap_v3/openvla_goal/untrained.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_multi_threshold_robustness_20260523T164043",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "cat /root/autodl-tmp/vla-ssd/results/bootstrap_v3/openvla_goal/untrained.json"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-23T16:42:10.571015+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"per_layer_r2\\\": {\\n    \\\"L0\\\": 0.3256,\\n    \\\"L1\\\": 0.3964,\\n    \\\"L2\\\": 0.3521,\\n    \\\"L3\\\": 0.2713,\\n    \\\"L4\\\": 0.3598,\\n    \\\"L5\\\": 0.3436,\\n    \\\"L6\\\": 0.3228,\\n    \\\"L7\\\": 0.3094,\\n    \\\"L8\\\": 0.3144,\\n    \\\"L9\\\": 0.3049,\\n    \\\"L10\\\": 0.3893,\\n    \\\"L11\\\": 0.3787,\\n    \\\"L12\\\": 0.3794,\\n    \\\"L13\\\": 0.3576,\\n    \\\"L14\\\": 0.3615,\\n    \\\"L15\\\": 0.355,\\n    \\\"L16\\\": 0.3396,\\n    \\\"L17\\\": 0.3484,\\n    \\\"L18\\\": 0.339,\\n    \\\"L19\\\": 0.3338,\\n    \\\"L20\\\": 0.3308,\\n    \\\"L21\\\": 0.3105,\\n    \\\"L22\\\": 0.2984,\\n    \\\"L23\\\": 0.284,\\n    \\\"L24\\\": 0.4066,\\n    \\\"L25\\\": 0.4066,\\n    \\\"L26\\\": 0.4122,\\n    \\\"L27\\\": 0.423,\\n    \\\"L28\\\": 0.4111,\\n    \\\"L29\\\": 0.408,\\n    \\\"L30\\\": 0.3994,\\n    \\\"L31\\\": 0.3672\\n  },\\n  \\\"peak_r2\\\": 0.423,\\n  \\\"peak_layer\\\": \\\"L27\\\",\\n  \\\"exit_r2\\\": 0.3672,\\n  \\\"exit_layer\\\": \\\"L31\\\",\\n  \\\"delta\\\": 0.0558,\\n  \\\"delta_ci_95\\\": [\\n    0.0113,\\n    0.0773\\n  ],\\n  \\\"bootstrap_deltas_summary\\\": {\\n    \\\"mean\\\": 0.0396,\\n    \\\"std\\\": 0.0166,\\n    \\\"median\\\": 0.0383\\n  },\\n  \\\"arch\\\": \\\"openvla\\\",\\n  \\\"suite\\\": \\\"goal\\\",\\n  \\\"condition\\\": \\\"untrained\\\",\\n  \\\"n_demos\\\": 100,\\n  \\\"n_total_samples\\\": 5000,\\n  \\\"n_bootstrap\\\": 1000,\\n  \\\"dry_run\\\": false\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_multi_threshold_robustness_20260523T164043",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-23T16:42:10.571198+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-19183",
  "command": "cd /root/autodl-tmp/vla-ssd && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c \"\nimport json, glob, os\n\nbase = 'results/bootstrap_v3'\n\nresults = {}\nfor jf in sorted(glob.glob(os.path.join(base, '*/*.json'))):\n    parts = jf.split('/')\n    arch_suite = parts[-2]\n    cond = parts[-1].replace('.json','')\n    with open(jf) as f:\n        d = json.load(f)\n    results[(arch_suite, cond)] = {'delta': d['delta'], 'ci': d.get('delta_ci_95', [None, None])}\n\nvlm_vla_trained = [\n    ('tracvla_goal', 'trained'), ('tracvla_spatial', 'trained'),\n    ('tracvla_object', 'trained'), ('tracvla_long', 'trained'),\n    ('nora_goal', 'trained'), ('nora_spatial', 'trained')\n]\nopenvla_trained = [\n    ('openvla_goal', 'trained'), ('openvla_spatial', 'trained'),\n    ('openvla_object', 'trained'), ('openvla_long', 'trained')\n]\nuntrained = sorted([(k, c) for (k, c) in results.keys() if c == 'untrained'])\n\nthresholds = [0.05, 0.08, 0.10, 0.15, 0.20]\n\nprint('| Threshold | VLM->VLA trained (N/6) | OpenVLA trained (N/4) | Untrained (N/10) | Clean separation? |')\nprint('|-----------|------------------------|------------------------|-------------------|-------------------|')\n\nfor t in thresholds:\n    vlm_count = sum(1 for k in vlm_vla_trained if results[k]['delta'] > t)\n    ov_count = sum(1 for k in openvla_trained if results[k]['delta'] > t)\n    un_count = sum(1 for k in untrained if results[k]['delta'] > t)\n    clean = 'YES' if vlm_count == 6 and ov_count == 0 and un_count == 0 else 'NO'\n    print(f'| {t:.2f}      | {vlm_count}/6                    | {ov_count}/4                    | {un_count}/10             | {clean}               |')\n\nprint()\nprint('## Individual Delta values')\nprint()\nprint('### VLM->VLA trained')\nfor k in vlm_vla_trained:\n    d = results[k]\n    print(f'  {k[0]}/{k[1]}: delta={d[\\\"delta\\\"]:.4f}  CI_95={d[\\\"ci\\\"]}')\n\nprint()\nprint('### OpenVLA trained')\nfor k in openvla_trained:\n    d = results[k]\n    print(f'  {k[0]}/{k[1]}: delta={d[\\\"delta\\\"]:.4f}  CI_95={d[\\\"ci\\\"]}')\n\nprint()\nprint('### Untrained')\nfor k in untrained:\n    d = results[k]\n    print(f'  {k[0]}/{k[1]}: delta={d[\\\"delta\\\"]:.4f}  CI_95={d[\\\"ci\\\"]}')\n\nvlm_min = min(results[k]['delta'] for k in vlm_vla_trained)\nvlm_min_key = min(vlm_vla_trained, key=lambda k: results[k]['delta'])\nov_max = max(results[k]['delta'] for k in openvla_trained)\nov_max_key = max(openvla_trained, key=lambda k: results[k]['delta'])\nun_max = max(results[k]['delta'] for k in untrained)\nun_max_key = max(untrained, key=lambda k: results[k]['delta'])\nother_max = max(ov_max, un_max)\n\nprint()\nprint('## Separation analysis')\nprint(f'VLM->VLA trained min delta: {vlm_min:.4f} ({vlm_min_key[0]}/{vlm_min_key[1]})')\nprint(f'OpenVLA trained max delta:  {ov_max:.4f} ({ov_max_key[0]}/{ov_max_key[1]})')\nprint(f'Untrained max delta:        {un_max:.4f} ({un_max_key[0]}/{un_max_key[1]})')\nprint(f'Other max delta:            {other_max:.4f}')\nprint(f'Gap: {vlm_min:.4f} - {other_max:.4f} = {vlm_min - other_max:.4f}')\nif vlm_min > other_max:\n    print(f'Clean separation exists for any threshold in ({other_max:.4f}, {vlm_min:.4f})')\nelse:\n    print(f'NO clean separation: VLM->VLA min ({vlm_min:.4f}) <= other max ({other_max:.4f})')\n\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_multi_threshold_robustness_20260523T164043",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-19183",
    "command": "cd /root/autodl-tmp/vla-ssd && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c \"\nimport json, glob, os\n\nbase = 'results/bootstrap_v3'\n\nresults = {}\nfor jf in sorted(glob.glob(os.path.join(base, '*/*.json'))):\n    parts = jf.split('/')\n    arch_suite = parts[-2]\n    cond = parts[-1].replace('.json','')\n    with open(jf) as f:\n        d = json.load(f)\n    results[(arch_suite, cond)] = {'delta': d['delta'], 'ci': d.get('delta_ci_95', [None, None])}\n\nvlm_vla_trained = [\n    ('tracvla_goal', 'trained'), ('tracvla_spatial', 'trained'),\n    ('tracvla_object', 'trained'), ('tracvla_long', 'trained'),\n    ('nora_goal', 'trained'), ('nora_spatial', 'trained')\n]\nopenvla_trained = [\n    ('openvla_goal', 'trained'), ('openvla_spatial', 'trained'),\n    ('openvla_object', 'trained'), ('openvla_long', 'trained')\n]\nuntrained = sorted([(k, c) for (k, c) in results.keys() if c == 'untrained'])\n\nthresholds = [0.05, 0.08, 0.10, 0.15, 0.20]\n\nprint('| Threshold | VLM->VLA trained (N/6) | OpenVLA trained (N/4) | Untrained (N/10) | Clean separation? |')\nprint('|-----------|------------------------|------------------------|-------------------|-------------------|')\n\nfor t in thresholds:\n    vlm_count = sum(1 for k in vlm_vla_trained if results[k]['delta'] > t)\n    ov_count = sum(1 for k in openvla_trained if results[k]['delta'] > t)\n    un_count = sum(1 for k in untrained if results[k]['delta'] > t)\n    clean = 'YES' if vlm_count == 6 and ov_count == 0 and un_count == 0 else 'NO'\n    print(f'| {t:.2f}      | {vlm_count}/6                    | {ov_count}/4                    | {un_count}/10             | {clean}               |')\n\nprint()\nprint('## Individual Delta values')\nprint()\nprint('### VLM->VLA trained')\nfor k in vlm_vla_trained:\n    d = results[k]\n    print(f'  {k[0]}/{k[1]}: delta={d[\\\"delta\\\"]:.4f}  CI_95={d[\\\"ci\\\"]}')\n\nprint()\nprint('### OpenVLA trained')\nfor k in openvla_trained:\n    d = results[k]\n    print(f'  {k[0]}/{k[1]}: delta={d[\\\"delta\\\"]:.4f}  CI_95={d[\\\"ci\\\"]}')\n\nprint()\nprint('### Untrained')\nfor k in untrained:\n    d = results[k]\n    print(f'  {k[0]}/{k[1]}: delta={d[\\\"delta\\\"]:.4f}  CI_95={d[\\\"ci\\\"]}')\n\nvlm_min = min(results[k]['delta'] for k in vlm_vla_trained)\nvlm_min_key = min(vlm_vla_trained, key=lambda k: results[k]['delta'])\nov_max = max(results[k]['delta'] for k in openvla_trained)\nov_max_key = max(openvla_trained, key=lambda k: results[k]['delta'])\nun_max = max(results[k]['delta'] for k in untrained)\nun_max_key = max(untrained, key=lambda k: results[k]['delta'])\nother_max = max(ov_max, un_max)\n\nprint()\nprint('## Separation analysis')\nprint(f'VLM->VLA trained min delta: {vlm_min:.4f} ({vlm_min_key[0]}/{vlm_min_key[1]})')\nprint(f'OpenVLA trained max delta:  {ov_max:.4f} ({ov_max_key[0]}/{ov_max_key[1]})')\nprint(f'Untrained max delta:        {un_max:.4f} ({un_max_key[0]}/{un_max_key[1]})')\nprint(f'Other max delta:            {other_max:.4f}')\nprint(f'Gap: {vlm_min:.4f} - {other_max:.4f} = {vlm_min - other_max:.4f}')\nif vlm_min > other_max:\n    print(f'Clean separation exists for any threshold in ({other_max:.4f}, {vlm_min:.4f})')\nelse:\n    print(f'NO clean separation: VLM->VLA min ({vlm_min:.4f}) <= other max ({other_max:.4f})')\n\"\n"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-23T16:42:10.571390+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"| Threshold | VLM->VLA trained (N/6) | OpenVLA trained (N/4) | Untrained (N/10) | Clean separation? |\\n|-----------|------------------------|------------------------|-------------------|-------------------|\\n| 0.05      | 6/6                    | 1/4                    | 6/10             | NO               |\\n| 0.08      | 6/6                    | 1/4                    | 3/10             | NO               |\\n| 0.10      | 6/6                    | 0/4                    | 0/10             | YES               |\\n| 0.15      | 6/6                    | 0/4                    | 0/10             | YES               |\\n| 0.20      | 5/6                    | 0/4                    | 0/10             | NO               |\\n\\n## Individual Delta values\\n\\n### VLM->VLA trained\\n  tracvla_goal/trained: delta=0.3334  CI_95=[0.2069, 0.4508]\\n  tracvla_spatial/trained: delta=0.1557  CI_95=[0.0906, 0.2244]\\n  tracvla_object/trained: delta=0.3623  CI_95=[0.2834, 0.5038]\\n  tracvla_long/trained: delta=0.3579  CI_95=[0.1714, 0.5333]\\n  nora_goal/trained: delta=0.4551  CI_95=[0.9099, 1.6077]\\n  nora_spatial/trained: delta=0.3080  CI_95=[0.3011, 0.5119]\\n\\n### OpenVLA trained\\n  openvla_goal/trained: delta=0.0864  CI_95=[-0.056, 0.1064]\\n  openvla_spatial/trained: delta=0.0371  CI_95=[0.0087, 0.102]\\n  openvla_object/trained: delta=0.0370  CI_95=[-0.0038, 0.0854]\\n  openvla_long/trained: delta=0.0325  CI_95=[0.0037, 0.103]\\n\\n### Untrained\\n  nora_goal/untrained: delta=0.0806  CI_95=[-0.0147, 0.1102]\\n  nora_spatial/untrained: delta=0.0885  CI_95=[-0.0128, 0.0931]\\n  openvla_goal/untrained: delta=0.0558  CI_95=[0.0113, 0.0773]\\n  openvla_long/untrained: delta=0.0349  CI_95=[0.0261, 0.1047]\\n  openvla_object/untrained: delta=0.0513  CI_95=[-0.0044, 0.0905]\\n  openvla_spatial/untrained: delta=0.0437  CI_95=[0.0295, 0.1113]\\n  tracvla_goal/untrained: delta=0.0645  CI_95=[-0.1084, 0.051]\\n  tracvla_long
…[truncated 640 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_multi_threshold_robustness_20260523T164043",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-23T16:42:10.571618+00:00_

## Multi-threshold robustness 分析结果

### Threshold 扫描表

| Threshold | VLM→VLA trained (N/6) | OpenVLA trained (N/4) | Untrained (N/10) | Clean separation? |
|-----------|------------------------|------------------------|-------------------|-------------------|
| 0.05      | 6/6                    | 1/4                    | 6/10             | NO               |
| 0.08      | 6/6                    | 1/4                    | 3/10             | NO               |
| **0.10**  | **6/6**                | **0/4**                | **0/10**         | **YES**          |
| **0.15**  | **6/6**                | **0/4**                | **0/10**         | **YES**          |
| 0.20      | 5/6                    | 0/4                    | 0/10             | NO               |

### Individual Δ values

**VLM→VLA trained:**
| Condition | Δ | 95% CI |
|---|---|---|
| tracvla_goal/trained | 0.3334 | [0.2069, 0.4508] |
| tracvla_spatial/trained | 0.1557 | [0.0906, 0.2244] |
| tracvla_object/trained | 0.3623 | [0.2834, 0.5038] |
| tracvla_long/trained | 0.3579 | [0.1714, 0.5333] |
| nora_goal/trained | 0.4551 | [0.9099, 1.6077] |
| nora_spatial/trained | 0.3080 | [0.3011, 0.5119] |

**OpenVLA trained:**
| Condition | Δ | 95% CI |
|---|---|---|
| openvla_goal/trained | 0.0864 | [-0.056, 0.1064] |
| openvla_spatial/trained | 0.0371 | [0.0087, 0.102] |
| openvla_object/trained | 0.0370 | [-0.0038, 0.0854] |
| openvla_long/trained | 0.0325 | [0.0037, 0.103] |

**Untrained:**
| Condition | Δ | 95% CI |
|---|---|---|
| nora_goal/untrained | 0.0806 | [-0.0147, 0.1102] |
| nora_spatial/untrained | 0.0885 | [-0.0128, 0.0931] |
| openvla_goal/untrained | 0.0558 | [0.0113, 0.0773] |
| openvla_long/untrained | 0.0349 | [0.0261, 0.1047] |
| openvla_object/untrained | 0.0513 | [-0.0044, 0.0905] |
| openvla_spatial/untrained | 0.0437 | [0.0295, 0.1113] |
| tracvla_goal/untrained | 0.0645 | [-0.1084, 0.051] |
| tracvla_long/untrained | 0.0971 | [-0.0208, 0.1078] |
| tracvla_object/untrained | 0.0090 | [-0.0669, 0.0169] |
| tracvla_spatial/untrained | 0.0477 | [-0.6067, -0.4606] |

### Separation analysis

- VLM→VLA trained min Δ: **0.1557** (tracvla_spatial/trained)
- OpenVLA trained max Δ: **0.0864** (openvla_goal/trained)
- Untrained max Δ: **0.0971** (tracvla_long/untrained)
- **Gap: 0.1557 − 0.0971 = 0.0586**
- Clean separation 存在于阈值区间 **(0.0971, 0.1557)**，即 threshold = 0.10 和 0.15 均可完美分离 VLM→VLA trained 组 vs 其他所有组。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_multi_threshold_robustness_20260523T164043"
}
```

</details>

---
