# analysis r2 mse correlation

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 79
- **Recorded user turns:** 0
- **Tool calls:** 39
- **Original source:** `logs/chats/worker_analysis_r2_mse_correlation_20260520T123229.jsonl`
- **Structured JSON:** [`6b34905c2ab2720db651.json`](../../sessions/6b/6b34905c2ab2720db651.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

79 recorded events

### Tool call

_source line 1 · 2026-05-20T12:38:38.683772+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r2_mse_correlation_20260520T123229",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-20T12:38:38.684139+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r2_mse_correlation_20260520T123229",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-20T12:38:38.684319+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "find /root/autodl-tmp/vla-ssd/results/ /root/vla-ssd/results/ -name \"*.json\" -path \"*mse*\" -o -name \"*.json\" -path \"*action_error*\" -o -name \"*.json\" -path \"*per_task*\" 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r2_mse_correlation_20260520T123229",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "find /root/autodl-tmp/vla-ssd/results/ /root/vla-ssd/results/ -name \"*.json\" -path \"*mse*\" -o -name \"*.json\" -path \"*action_error*\" -o -name \"*.json\" -path \"*per_task*\" 2>/dev/null"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-20T12:38:38.684466+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r2_mse_correlation_20260520T123229",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-20T12:38:38.684597+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "find /root/autodl-tmp/vla-ssd/results/ -name \"*.json\" -path \"*r2*\" 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r2_mse_correlation_20260520T123229",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "find /root/autodl-tmp/vla-ssd/results/ -name \"*.json\" -path \"*r2*\" 2>/dev/null"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-20T12:38:38.684723+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r2_mse_correlation_20260520T123229",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-20T12:38:38.684843+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "find /root/autodl-tmp/vla-ssd/results/ -path \"*ablation*\" -name \"*.json\" 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r2_mse_correlation_20260520T123229",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "find /root/autodl-tmp/vla-ssd/results/ -path \"*ablation*\" -name \"*.json\" 2>/dev/null"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-20T12:38:38.685021+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r2_mse_correlation_20260520T123229",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-20T12:38:38.685303+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "find /root/autodl-tmp/vla-ssd/results/ -path \"*functional*\" -name \"*.json\" 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r2_mse_correlation_20260520T123229",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "find /root/autodl-tmp/vla-ssd/results/ -path \"*functional*\" -name \"*.json\" 2>/dev/null"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-20T12:38:38.685494+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r2_mse_correlation_20260520T123229",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-20T12:38:38.685658+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "find /root/autodl-tmp/vla-ssd/results/ -name \"*.json\" -path \"*r2*\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r2_mse_correlation_20260520T123229",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "find /root/autodl-tmp/vla-ssd/results/ -name \"*.json\" -path \"*r2*\""
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-20T12:38:38.685802+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "find /root/autodl-tmp/vla-ssd/results/ -name \"*.json\" -path \"*ablation*\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r2_mse_correlation_20260520T123229",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "find /root/autodl-tmp/vla-ssd/results/ -name \"*.json\" -path \"*ablation*\""
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-20T12:38:38.685961+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/vla-ssd/results/functional_validation/r2_probe_15seeds.json\\n/root/autodl-tmp/vla-ssd/results/functional_validation/phi3v_r2_action_probe.json\\n/root/autodl-tmp/vla-ssd/results/per_task_r2_distribution.json\\n/root/autodl-tmp/vla-ssd/results/phi3v_r2_untrained_probe/phi3v_r2_untrained_probe.json\\n/root/autodl-tmp/vla-ssd/results/phi3v_r2_seed_expansion/phi3v_r2_seed_expansion.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.15}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r2_mse_correlation_20260520T123229",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-20T12:38:38.686104+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "find /root/autodl-tmp/vla-ssd/results/ -name \"*.json\" -path \"*functional*\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r2_mse_correlation_20260520T123229",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "find /root/autodl-tmp/vla-ssd/results/ -name \"*.json\" -path \"*functional*\""
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-20T12:38:38.686243+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/vla-ssd/results/rsa/perlayer_comparison_inst_ablation.json\\n/root/autodl-tmp/vla-ssd/results/ablations/rsa_cosine_metric.json\\n/root/autodl-tmp/vla-ssd/results/ablations/rsa_permutation_null.json\\n/root/autodl-tmp/vla-ssd/results/ablations/rsa_per_dof.json\\n/root/autodl-tmp/vla-ssd/results/ablations/probe_seed_robustness.json\\n/root/autodl-tmp/vla-ssd/results/ablations/demo_sensitivity_25.json\\n/root/autodl-tmp/vla-ssd/results/l1_head_ablation/test_results.json\\n/root/autodl-tmp/vla-ssd/results/l1_head_ablation/results.json\\n/root/autodl-tmp/vla-ssd/results/l1_head_ablation/test_v2.json\\n/root/autodl-tmp/vla-ssd/results/l1_head_ablation/results_v2.json\\n/root/autodl-tmp/vla-ssd/results/l1_head_ablation/results_v3_all32.json\\n/root/autodl-tmp/vla-ssd/results/l1_head_ablation/action_probe_results.json\\n/root/autodl-tmp/vla-ssd/results/l1_head_ablation/bootstrap_ci_results.json\\n/root/autodl-tmp/vla-ssd/results/l1_head_ablation/action_probe_50demos_control8.json\\n/root/autodl-tmp/vla-ssd/results/l1_head_ablation/action_probe_50demos.json\\n/root/autodl-tmp/vla-ssd/results/l1_head_ablation/ablation_50demos_combined.json\\n/root/autodl-tmp/vla-ssd/results/l1_head_ablation/specificity_bootstrap_30seeds.json\\n/root/autodl-tmp/vla-ssd/results/random_subset_ablation.json\\n/root/autodl-tmp/vla-ssd/results/action_trajectory_L8_ablation.json\\n/root/autodl-tmp/vla-ssd/results/action_trajectory_L13_ablation.json\\n/root/autodl-tmp/vla-ssd/results/matched_ablation_controls.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.53}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r2_mse_correlation_20260520T123229",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-20T12:38:38.686383+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/vla-ssd/results/functional_validation/action_probe_projector.json\\n/root/autodl-tmp/vla-ssd/results/functional_validation/action_delta_probe_projector.json\\n/root/autodl-tmp/vla-ssd/results/functional_validation/dino_action_probe.json\\n/root/autodl-tmp/vla-ssd/results/functional_validation/action_probe_v2.json\\n/root/autodl-tmp/vla-ssd/results/functional_validation/untrained_last_preaction_probe.json\\n/root/autodl-tmp/vla-ssd/results/functional_validation/bootstrap_trained_vs_untrained_lastpreaction.json\\n/root/autodl-tmp/vla-ssd/results/functional_validation/action_probe_clip.json\\n/root/autodl-tmp/vla-ssd/results/functional_validation/unified_action_probe.json\\n/root/autodl-tmp/vla-ssd/results/functional_validation/patch_mean_probe.json\\n/root/autodl-tmp/vla-ssd/results/functional_validation/fulllayer_action_probe.json\\n/root/autodl-tmp/vla-ssd/results/functional_validation/action_probe_libero_spatial.json\\n/root/autodl-tmp/vla-ssd/results/functional_validation/r2_probe_15seeds.json\\n/root/autodl-tmp/vla-ssd/results/functional_validation/phi3v_r2_action_probe.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r2_mse_correlation_20260520T123229",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-20T12:38:38.686517+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "find /root/autodl-tmp/vla-ssd/results/ -name \"*.json\" -path \"*per_task*\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r2_mse_correlation_20260520T123229",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "find /root/autodl-tmp/vla-ssd/results/ -name \"*.json\" -path \"*per_task*\""
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-20T12:38:38.686643+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/vla-ssd/results/per_task_mse_breakdown.json\\n/root/autodl-tmp/vla-ssd/results/per_task_r2_distribution.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r2_mse_correlation_20260520T123229",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-20T12:38:38.686762+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "find /root/autodl-tmp/vla-ssd/results/ -name \"*mse*\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r2_mse_correlation_20260520T123229",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "find /root/autodl-tmp/vla-ssd/results/ -name \"*mse*\""
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-20T12:38:38.686883+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/vla-ssd/results/per_task_mse_breakdown.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r2_mse_correlation_20260520T123229",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-20T12:38:38.687061+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "cat /root/autodl-tmp/vla-ssd/results/per_task_mse_breakdown.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r2_mse_correlation_20260520T123229",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "cat /root/autodl-tmp/vla-ssd/results/per_task_mse_breakdown.json"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-20T12:38:38.687235+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"tasks\\\": [\\n    {\\n      \\\"task_name\\\": \\\"open_the_middle_drawer_of_the_cabinet\\\",\\n      \\\"n_samples\\\": 500,\\n      \\\"original_mse\\\": 0.562126,\\n      \\\"top24_ablated_mse\\\": 0.54741,\\n      \\\"bottom24_ablated_mse\\\": 0.560036,\\n      \\\"delta_mse_top24\\\": -0.014716,\\n      \\\"delta_mse_bottom24\\\": -0.00209,\\n      \\\"delta_pct_top24\\\": -2.62,\\n      \\\"delta_pct_bottom24\\\": -0.37,\\n      \\\"wilcoxon_p_top24\\\": 0.351,\\n      \\\"wilcoxon_p_bottom24\\\": 0.7697\\n    },\\n    {\\n      \\\"task_name\\\": \\\"open_the_top_drawer_and_put_the_bowl_inside\\\",\\n      \\\"n_samples\\\": 500,\\n      \\\"original_mse\\\": 0.548375,\\n      \\\"top24_ablated_mse\\\": 0.55811,\\n      \\\"bottom24_ablated_mse\\\": 0.557744,\\n      \\\"delta_mse_top24\\\": 0.009735,\\n      \\\"delta_mse_bottom24\\\": 0.009369,\\n      \\\"delta_pct_top24\\\": 1.78,\\n      \\\"delta_pct_bottom24\\\": 1.71,\\n      \\\"wilcoxon_p_top24\\\": 0.2735,\\n      \\\"wilcoxon_p_bottom24\\\": 0.887\\n    },\\n    {\\n      \\\"task_name\\\": \\\"push_the_plate_to_the_front_of_the_stove\\\",\\n      \\\"n_samples\\\": 500,\\n      \\\"original_mse\\\": 0.38335,\\n      \\\"top24_ablated_mse\\\": 0.385142,\\n      \\\"bottom24_ablated_mse\\\": 0.400603,\\n      \\\"delta_mse_top24\\\": 0.001792,\\n      \\\"delta_mse_bottom24\\\": 0.017253,\\n      \\\"delta_pct_top24\\\": 0.47,\\n      \\\"delta_pct_bottom24\\\": 4.5,\\n      \\\"wilcoxon_p_top24\\\": 0.4474,\\n      \\\"wilcoxon_p_bottom24\\\": 0.029\\n    }\\n  ],\\n  \\\"cancellation_analysis\\\": {\\n    \\\"top24\\\": {\\n      \\\"has_sign_mixing\\\": true,\\n      \\\"task_delta_signs\\\": [\\n        \\\"-\\\",\\n        \\\"+\\\",\\n        \\\"~0\\\"\\n      ],\\n      \\\"overall_delta\\\": -0.001063,\\n      \\\"any_task_significant\\\": false,\\n      \\\"pattern\\\": \\\"Weak sign mixing: drawer -0.015, bowl +0.010, pla
…[truncated 918 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r2_mse_correlation_20260520T123229",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-20T12:38:38.687397+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "cat /root/autodl-tmp/vla-ssd/results/per_task_r2_distribution.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r2_mse_correlation_20260520T123229",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "cat /root/autodl-tmp/vla-ssd/results/per_task_r2_distribution.json"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-20T12:38:38.687721+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"method\\\": \\\"per_task_r2_distribution\\\",\\n  \\\"tasks\\\": [\\n    \\\"open the middle drawer of the cabinet\\\",\\n    \\\"open the top drawer and put the bowl inside\\\",\\n    \\\"push the plate to the front of the stove\\\",\\n    \\\"put the bowl on the plate\\\",\\n    \\\"put the bowl on the stove\\\",\\n    \\\"put the bowl on top of the cabinet\\\",\\n    \\\"put the cream cheese in the bowl\\\",\\n    \\\"put the wine bottle on the rack\\\",\\n    \\\"put the wine bottle on top of the cabinet\\\",\\n    \\\"turn on the stove\\\"\\n  ],\\n  \\\"n_tasks\\\": 10,\\n  \\\"mlp_probe_5demo\\\": {\\n    \\\"description\\\": \\\"MLP(4096,256,7) probe, 5 demos/task, per-task R2 distribution\\\",\\n    \\\"conditions\\\": {\\n      \\\"baseline\\\": {\\n        \\\"L1\\\": {\\n          \\\"per_task_R2\\\": {\\n            \\\"open the middle drawer of the cabinet\\\": 0.1971,\\n            \\\"open the top drawer and put the bowl inside\\\": 0.2649,\\n            \\\"push the plate to the front of the stove\\\": 0.1901,\\n            \\\"put the bowl on the plate\\\": 0.3754,\\n            \\\"put the bowl on the stove\\\": 0.2352,\\n            \\\"put the bowl on top of the cabinet\\\": 0.2561,\\n            \\\"put the cream cheese in the bowl\\\": 0.186,\\n            \\\"put the wine bottle on the rack\\\": 0.1894,\\n            \\\"put the wine bottle on top of the cabinet\\\": 0.2789,\\n            \\\"turn on the stove\\\": 0.3854\\n          },\\n          \\\"mean\\\": 0.2559,\\n          \\\"std\\\": 0.0701,\\n          \\\"min\\\": 0.186,\\n          \\\"max\\\": 0.3854,\\n          \\\"range\\\": 0.1994\\n        },\\n        \\\"L8\\\": {\\n          \\\"per_task_R2\\\": {\\n            \\\"open the middle drawer of the cabinet\\\": 0.4532,\\n            \\\"open the top drawer and put the bowl inside\\\": 0.3757,\\n            \\\"push the plate to the front of the stove\\\": 0.3
…[truncated 8402 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r2_mse_correlation_20260520T123229",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-20T12:38:38.687953+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "cat /root/autodl-tmp/vla-ssd/results/l1_head_ablation/ablation_50demos_combined.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r2_mse_correlation_20260520T123229",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "cat /root/autodl-tmp/vla-ssd/results/l1_head_ablation/ablation_50demos_combined.json"
  }
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-20T12:38:38.688096+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "cat /root/autodl-tmp/vla-ssd/results/l1_head_ablation/action_probe_50demos.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r2_mse_correlation_20260520T123229",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "cat /root/autodl-tmp/vla-ssd/results/l1_head_ablation/action_probe_50demos.json"
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-20T12:38:38.688312+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"means\\\": {\\n    \\\"baseline\\\": {\\n      \\\"L1\\\": 0.5567,\\n      \\\"L8\\\": 0.6199,\\n      \\\"L13\\\": 0.6763\\n    },\\n    \\\"ablate_control8\\\": {\\n      \\\"L1\\\": 0.5732,\\n      \\\"L8\\\": 0.6311,\\n      \\\"L13\\\": 0.6787\\n    },\\n    \\\"ablate_all24\\\": {\\n      \\\"L1\\\": 0.6153,\\n      \\\"L8\\\": 0.6377,\\n      \\\"L13\\\": 0.6762\\n    },\\n    \\\"ablate_all32\\\": {\\n      \\\"L1\\\": 0.5823,\\n      \\\"L8\\\": 0.6311,\\n      \\\"L13\\\": 0.6636\\n    }\\n  },\\n  \\\"bootstrap_ci\\\": {\\n    \\\"baseline\\\": {\\n      \\\"L1\\\": {\\n        \\\"ci_lo\\\": 0.5031997499999998,\\n        \\\"ci_hi\\\": 0.61418\\n      },\\n      \\\"L8\\\": {\\n        \\\"ci_lo\\\": 0.5679982499999999,\\n        \\\"ci_hi\\\": 0.67471\\n      },\\n      \\\"L13\\\": {\\n        \\\"ci_lo\\\": 0.6334595000000002,\\n        \\\"ci_hi\\\": 0.7226127499999998\\n      }\\n    },\\n    \\\"ablate_control8\\\": {\\n      \\\"L1\\\": {\\n        \\\"ci_lo\\\": 0.5152987500000001,\\n        \\\"ci_hi\\\": 0.6317999999999999\\n      },\\n      \\\"L8\\\": {\\n        \\\"ci_lo\\\": 0.5785172499999999,\\n        \\\"ci_hi\\\": 0.6834715\\n      },\\n      \\\"L13\\\": {\\n        \\\"ci_lo\\\": 0.63152,\\n        \\\"ci_hi\\\": 0.72624\\n      }\\n    },\\n    \\\"ablate_all24\\\": {\\n      \\\"L1\\\": {\\n        \\\"ci_lo\\\": 0.56369825,\\n        \\\"ci_hi\\\": 0.6666\\n      },\\n      \\\"L8\\\": {\\n        \\\"ci_lo\\\": 0.58909875,\\n        \\\"ci_hi\\\": 0.6888704999999999\\n      },\\n      \\\"L13\\\": {\\n        \\\"ci_lo\\\": 0.63306875,\\n        \\\"ci_hi\\\": 0.72317175\\n      }\\n    },\\n    \\\"ablate_all32\\\": {\\n      \\\"L1\\\": {\\n        \\\"ci_lo\\\": 0.528179,\\n        \\\"ci_hi\\\": 0.6386010000000001\\n      },\\n      \\\"L8\\\": {\\n        \\\"ci_lo\\\": 0.5786582499999999,\\n        \\\"ci_hi\\\": 0.68366175\\n      },\\n      \\\"L13\\\": {\
…[truncated 3364 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r2_mse_correlation_20260520T123229",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-20T12:38:38.688477+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "cat /root/autodl-tmp/vla-ssd/results/functional_validation/unified_action_probe.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r2_mse_correlation_20260520T123229",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "cat /root/autodl-tmp/vla-ssd/results/functional_validation/unified_action_probe.json"
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-20T12:38:38.688786+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"action_probe_R2\\\": {\\n    \\\"baseline\\\": {\\n      \\\"L1\\\": 0.5567,\\n      \\\"L8\\\": 0.6199,\\n      \\\"L13\\\": 0.6763\\n    },\\n    \\\"ablate_all24\\\": {\\n      \\\"L1\\\": 0.6153,\\n      \\\"L8\\\": 0.6377,\\n      \\\"L13\\\": 0.6762\\n    },\\n    \\\"ablate_all32\\\": {\\n      \\\"L1\\\": 0.5823,\\n      \\\"L8\\\": 0.6311,\\n      \\\"L13\\\": 0.6636\\n    }\\n  },\\n  \\\"bootstrap_paired_CI\\\": {\\n    \\\"baseline_vs_ablate_all24\\\": {\\n      \\\"L1\\\": {\\n        \\\"observed_diff\\\": 0.0585,\\n        \\\"CI_95\\\": [\\n          0.0418,\\n          0.0748\\n        ],\\n        \\\"p_value\\\": 0.0,\\n        \\\"baseline_mean_R2\\\": 0.5567,\\n        \\\"baseline_CI_95\\\": [\\n          0.5038,\\n          0.6144\\n        ],\\n        \\\"ablation_mean_R2\\\": 0.6153,\\n        \\\"ablation_CI_95\\\": [\\n          0.5634,\\n          0.6664\\n        ],\\n        \\\"n_tasks\\\": 10,\\n        \\\"per_task_diffs\\\": {\\n          \\\"open the middle drawer of the cabinet\\\": 0.0218,\\n          \\\"open the top drawer and put the bowl inside\\\": 0.0714,\\n          \\\"push the plate to the front of the stove\\\": 0.0404,\\n          \\\"put the bowl on the plate\\\": 0.084,\\n          \\\"put the bowl on the stove\\\": 0.0704,\\n          \\\"put the bowl on top of the cabinet\\\": 0.0966,\\n          \\\"put the cream cheese in the bowl\\\": 0.0901,\\n          \\\"put the wine bottle on the rack\\\": 0.0533,\\n          \\\"put the wine bottle on top of the cabinet\\\": 0.041,\\n          \\\"turn on the stove\\\": 0.0165\\n        }\\n      },\\n      \\\"L8\\\": {\\n        \\\"observed_diff\\\": 0.0177,\\n        \\\"CI_95\\\": [\\n          0.0087,\\n          0.0276\\n        ],\\n        \\\"p_value\\\": 0.0,\\n        \\\"baseline_mean_R2\\\": 0.62,\\n        \\\"baseline_CI_95\\\": [\\n          0.5675,\\n          0.6741\\n        ],\\n       
…[truncated 7844 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r2_mse_correlation_20260520T123229",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-20T12:38:38.689088+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"hyperparams\\\": {\\n    \\\"epochs\\\": 50,\\n    \\\"patience\\\": 5,\\n    \\\"lr\\\": 0.001,\\n    \\\"batch_size\\\": 256,\\n    \\\"hidden\\\": 256,\\n    \\\"seed\\\": 42,\\n    \\\"target\\\": \\\"next_action_a_{t+1}\\\",\\n    \\\"normalization\\\": \\\"z-score\\\",\\n    \\\"split\\\": \\\"80/20_per_task_by_demo_index\\\"\\n  },\\n  \\\"projector\\\": {\\n    \\\"mean_R2\\\": 0.6298085182905198,\\n    \\\"overall_R2\\\": 0.6991766095161438,\\n    \\\"per_task_R2\\\": {\\n      \\\"open_the_middle_drawer_of_the_cabinet\\\": 0.49730074405670166,\\n      \\\"open_the_top_drawer_and_put_the_bowl_inside\\\": 0.7499217689037323,\\n      \\\"push_the_plate_to_the_front_of_the_stove\\\": 0.5860892236232758,\\n      \\\"put_the_bowl_on_the_plate\\\": 0.5864041447639465,\\n      \\\"put_the_bowl_on_the_stove\\\": 0.6738172769546509,\\n      \\\"put_the_bowl_on_top_of_the_cabinet\\\": 0.6633979082107544,\\n      \\\"put_the_cream_cheese_in_the_bowl\\\": 0.6218974888324738,\\n      \\\"put_the_wine_bottle_on_the_rack\\\": 0.5312090218067169,\\n      \\\"put_the_wine_bottle_on_top_of_the_cabinet\\\": 0.6380730867385864,\\n      \\\"turn_on_the_stove\\\": 0.7499745190143585\\n    },\\n    \\\"per_dim_R2\\\": {\\n      \\\"dx\\\": 0.6506892442703247,\\n      \\\"dy\\\": 0.7160145938396454,\\n      \\\"dz\\\": 0.6620165109634399,\\n      \\\"drx\\\": 0.549751490354538,\\n      \\\"dry\\\": 0.3786472678184509,\\n      \\\"drz\\\": 0.7263338565826416,\\n      \\\"gripper\\\": 0.7167081236839294\\n    },\\n    \\\"gripper_acc\\\": 0.9221054283024788,\\n    \\\"epochs_trained\\\": 22,\\n    \\\"val_loss\\\": 0.3606724441051483\\n  },\\n  \\\"dino_cls\\\": {\\n    \\\"mean_R2\\\": 0.6342984035611152,\\n    \\\"overall_R2\\\": 0.7012259066104889,\\n    \\\"per_task_R2\\\": {\\n      \\\"open_the_middle_drawer_of_the_cabinet\\\": 0.4813086986541748,\\n      \\\"open_the_top_drawer_and_put_the_bowl_inside\\\": 0.71
…[truncated 6261 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r2_mse_correlation_20260520T123229",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-20T12:38:38.689315+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "find /root/autodl-tmp/vla-ssd/results/ -name \"*.json\" -path \"*eval*\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r2_mse_correlation_20260520T123229",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "find /root/autodl-tmp/vla-ssd/results/ -name \"*.json\" -path \"*eval*\""
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-20T12:38:38.689482+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r2_mse_correlation_20260520T123229",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-20T12:38:38.689622+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "find /root/autodl-tmp/vla-ssd/results/ -name \"*.json\" -path \"*success*\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r2_mse_correlation_20260520T123229",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "find /root/autodl-tmp/vla-ssd/results/ -name \"*.json\" -path \"*success*\""
  }
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-20T12:38:38.689749+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "ls /root/autodl-tmp/vla-ssd/results/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r2_mse_correlation_20260520T123229",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "ls /root/autodl-tmp/vla-ssd/results/"
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-20T12:38:38.689874+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r2_mse_correlation_20260520T123229",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-20T12:38:38.690075+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"ablations\\naction_baselines.json\\naction_metrics_extended.json\\naction_probe\\naction_trajectory_L13_ablation.json\\naction_trajectory_L13_ablation.log\\naction_trajectory_L8_ablation.json\\naction_trajectory_L8_ablation.log\\naction_trajectory_analysis.json\\naction_trajectory_analysis.log\\naction_trajectory_control.json\\naction_trajectory_control.log\\naction_trajectory_cpu_analysis.json\\naction_trajectory_extended_analysis.json\\nanalysis\\narchitecture_audit\\nattention\\nattention_decomposition.json\\nattention_normalization_entropy.json\\nbootstrap_ci_values.json\\ncka\\ncounterfactual_combined.json\\ncounterfactual_correct.json\\ncounterfactual_empty.json\\ncounterfactual_instruction.log\\ncounterfactual_paraphrased.json\\ncounterfactual_shuffled.json\\ncounterfactual_token_overlap.json\\ncounterfactual_wrong.json\\ncross_instruction\\ncross_instruction_dense\\ncross_instruction_finetuned\\ncross_instruction_spatial\\ndemo_sensitivity_25\\ndinov2\\ndinov2_libero_goal\\ndinov2_libero_goal_frame0\\ndinov2_libero_goal_linear\\ndinov2_libero_goal_pca1024\\ndinov2_shuffle\\ndose_response_cuda0.log\\ndose_response_cuda1.log\\ndose_response_curve_combined.json\\ndose_response_top12.json\\ndose_response_top16.json\\ndose_response_top20.json\\ndose_response_top24.json\\ndose_response_top28.json\\ndose_response_top32.json\\ndose_response_top4.json\\ndose_response_top8.json\\nfig_dose_response_curve.pdf\\nfig_dose_response_curve.png\\nfig_dose_response_draft.pdf\\nfig_dose_response_draft.png\\nfigure_data\\nfigures\\nfinetuned_probe_profile.log\\nfunctional_validation\\ngroundtruth_action_error.json\\ngroundtruth_action_error.log\\nl1_head_ablation\\nlibero_finetuned_attention.log\\nlibero_finetuned_attention_profile.json\\nlibero_finetuned_probe_profile.json\\nlinear_probe.log\\nlinear_probe_last_preaction.json\\nlinear_probe_results.json\\nllama2base_action_probe\\nloo_sensitivity.py\\nmatched_ablation_cont
…[truncated 1248 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r2_mse_correlation_20260520T123229",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-20T12:38:38.690246+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "cat /root/autodl-tmp/vla-ssd/results/groundtruth_action_error.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r2_mse_correlation_20260520T123229",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "cat /root/autodl-tmp/vla-ssd/results/groundtruth_action_error.json"
  }
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-20T12:38:38.690375+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "cat /root/autodl-tmp/vla-ssd/results/action_metrics_extended.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r2_mse_correlation_20260520T123229",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "cat /root/autodl-tmp/vla-ssd/results/action_metrics_extended.json"
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-20T12:38:38.690676+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"config\\\": {\\n    \\\"n_tasks\\\": 3,\\n    \\\"n_demos\\\": 10,\\n    \\\"n_timesteps\\\": 50,\\n    \\\"total_passes\\\": 4500,\\n    \\\"model\\\": \\\"openvla-7b\\\",\\n    \\\"unnorm_key\\\": \\\"bridge_orig\\\",\\n    \\\"top24_heads\\\": [\\n      0,\\n      1,\\n      2,\\n      4,\\n      7,\\n      8,\\n      10,\\n      11,\\n      12,\\n      14,\\n      15,\\n      16,\\n      17,\\n      18,\\n      19,\\n      20,\\n      22,\\n      23,\\n      25,\\n      26,\\n      27,\\n      29,\\n      30,\\n      31\\n    ],\\n    \\\"bottom24_heads\\\": [\\n      1,\\n      3,\\n      4,\\n      5,\\n      6,\\n      7,\\n      8,\\n      9,\\n      11,\\n      12,\\n      13,\\n      15,\\n      16,\\n      17,\\n      18,\\n      20,\\n      21,\\n      23,\\n      24,\\n      26,\\n      28,\\n      29,\\n      30,\\n      31\\n    ],\\n    \\\"tasks\\\": [\\n      \\\"open_the_middle_drawer_of_the_cabinet\\\",\\n      \\\"open_the_top_drawer_and_put_the_bowl_inside\\\",\\n      \\\"push_the_plate_to_the_front_of_the_stove\\\"\\n    ],\\n    \\\"note\\\": \\\"GT actions in LIBERO native space; model outputs use bridge_orig unnorm. Delta metrics cancel domain bias.\\\"\\n  },\\n  \\\"global_metrics\\\": {\\n    \\\"original\\\": {\\n      \\\"mse\\\": {\\n        \\\"mean\\\": 0.4979501858383766,\\n        \\\"std\\\": 0.19915986474044517\\n      },\\n      \\\"mae\\\": {\\n        \\\"mean\\\": 0.39345952361320385,\\n        \\\"std\\\": 0.07798226709814308\\n      },\\n      \\\"per_dim_mse\\\": {\\n        \\\"dx\\\": 0.2740072594718719,\\n        \\\"dy\\\": 0.07590344138801013,\\n        \\\"dz\\\": 0.19582658825589758,\\n        \\\"rx\\\": 0.003480265722698624,\\n        \\\"ry\\\": 0.008375430813774083,\\n        \\\"rz\\\": 0.0190559315178063,\\n        \\\"gripper\\\": 2.909002383698577\\n      },\\n      \\\"per_dim_mae\\\": {\\n        \\\"dx\\\": 0.4093814824658402,\\n        \
…[truncated 7860 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r2_mse_correlation_20260520T123229",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-20T12:38:38.691004+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"instruction_24h\\\": {\\n    \\\"per_dim_mae\\\": [\\n      0.0018907630960015738,\\n      0.0053060349467249435,\\n      0.007621298928714849,\\n      0.02059210950341174,\\n      0.030713564767946917,\\n      0.033881929667518705,\\n      0.2907168627450989\\n    ],\\n    \\\"per_dim_mae_std\\\": [\\n      0.003945774709271799,\\n      0.007996728850961761,\\n      0.00855598404937074,\\n      0.02115830546884926,\\n      0.02858547485740179,\\n      0.037737860644735575,\\n      0.44894904084862064\\n    ],\\n    \\\"per_dim_mae_labels\\\": [\\n      \\\"dx\\\",\\n      \\\"dy\\\",\\n      \\\"dz\\\",\\n      \\\"roll\\\",\\n      \\\"pitch\\\",\\n      \\\"yaw\\\",\\n      \\\"gripper\\\"\\n    ],\\n    \\\"cosine_similarity\\\": {\\n      \\\"status\\\": \\\"not_computable\\\",\\n      \\\"reason\\\": \\\"Raw per-sample action vectors not stored in JSON; only aggregated statistics available\\\"\\n    },\\n    \\\"per_task\\\": {\\n      \\\"open_the_middle_drawer_of_the_cabinet\\\": {\\n        \\\"per_dim_mae\\\": [\\n          0.0014037795379863059,\\n          0.004451050012665628,\\n          0.006329343725828563,\\n          0.019142500603928258,\\n          0.030247070985899276,\\n          0.03025989703622987,\\n          0.15281568627450998\\n        ],\\n        \\\"per_dim_mae_std\\\": [\\n          0.00311317121105672,\\n          0.007885665398470972,\\n          0.008240969667318977,\\n          0.019615421748166623,\\n          0.028676831314892466,\\n          0.033095946085946286,\\n          0.3590890901162581\\n        ]\\n      },\\n      \\\"open_the_top_drawer_and_put_the_bowl_inside\\\": {\\n        \\\"per_dim_mae\\\": [\\n          0.0017330280210831573,\\n          0.005302538340663201,\\n          0.007163902512666055,\\n          0.020680235506992665,\\n          0.03485707990039093,\\n          0.03459241025841939,\\n          0.3118901960784321\\n        ],\\n        
…[truncated 7426 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r2_mse_correlation_20260520T123229",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-20T12:38:38.691180+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "cat /root/autodl-tmp/vla-ssd/results/action_baselines.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r2_mse_correlation_20260520T123229",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "cat /root/autodl-tmp/vla-ssd/results/action_baselines.json"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-20T12:38:38.691450+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"copy_baseline\\\": {\\n    \\\"per_task\\\": {\\n      \\\"KITCHEN_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it\\\": {\\n        \\\"per_dim_r2\\\": [\\n          0.9833366531356645,\\n          0.9887299561344475,\\n          0.9845505010161877,\\n          0.9733266800677457,\\n          0.9655171605739561,\\n          0.9860680191422142,\\n          0.9349032346873726\\n        ],\\n        \\\"overall_r2\\\": 0.9737760292510853\\n      },\\n      \\\"KITCHEN_SCENE4_put_the_black_bowl_in_the_bottom_drawer_of_the_cabinet_and_close_it\\\": {\\n        \\\"per_dim_r2\\\": [\\n          0.97990959739998,\\n          0.9853026724483149,\\n          0.9832757770199817,\\n          0.9784709160091953,\\n          0.9683775261278218,\\n          0.991376799513957,\\n          0.9635978835978836\\n        ],\\n        \\\"overall_r2\\\": 0.9786158817310184\\n      },\\n      \\\"KITCHEN_SCENE6_put_the_yellow_and_white_mug_in_the_microwave_and_close_it\\\": {\\n        \\\"per_dim_r2\\\": [\\n          0.9811901353970697,\\n          0.9804987500646462,\\n          0.9708966495623188,\\n          0.9769552249312932,\\n          0.971385813467457,\\n          0.9935146063989967,\\n          0.9615538513086408\\n        ],\\n        \\\"overall_r2\\\": 0.9765707187329182\\n      },\\n      \\\"KITCHEN_SCENE8_put_both_moka_pots_on_the_stove\\\": {\\n        \\\"per_dim_r2\\\": [\\n          0.9852691303668937,\\n          0.9944626439681621,\\n          0.9863249178337707,\\n          0.9851900290158843,\\n          0.974531365086638,\\n          0.9957666334525208,\\n          0.9584796627750739\\n        ],\\n        \\\"overall_r2\\\": 0.9828606260712773\\n      },\\n      \\\"LIVING_ROOM_SCENE1_put_both_the_alphabet_soup_and_the_cream_cheese_box_in_the_basket\\\": {\\n        \\\"per_dim_r2\\\": [\\n          0.9694697805179923,\\n          0.9850500730416234,\\n          0.9807600770190139,\\n      
…[truncated 7093 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r2_mse_correlation_20260520T123229",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-20T12:38:38.691649+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "cat /root/autodl-tmp/vla-ssd/results/sr_corrected_3ep.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r2_mse_correlation_20260520T123229",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "cat /root/autodl-tmp/vla-ssd/results/sr_corrected_3ep.json"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-20T12:38:38.691798+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"config\\\": \\\"256x256_crop224_flip_native_predict\\\",\\n  \\\"task\\\": \\\"open_the_middle_drawer_of_the_cabinet\\\",\\n  \\\"instruction\\\": \\\"open the middle drawer of the cabinet\\\",\\n  \\\"episodes\\\": [\\n    {\\n      \\\"success\\\": false,\\n      \\\"reward\\\": 0.0,\\n      \\\"steps\\\": 400\\n    },\\n    {\\n      \\\"success\\\": false,\\n      \\\"reward\\\": 0.0,\\n      \\\"steps\\\": 400\\n    },\\n    {\\n      \\\"success\\\": false,\\n      \\\"reward\\\": 0.0,\\n      \\\"steps\\\": 400\\n    }\\n  ],\\n  \\\"sr\\\": 0.0\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r2_mse_correlation_20260520T123229",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-20T12:38:38.691951+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "cat /root/autodl-tmp/vla-ssd/results/task_complexity_routing.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r2_mse_correlation_20260520T123229",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "cat /root/autodl-tmp/vla-ssd/results/task_complexity_routing.json"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-20T12:38:38.692140+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"description\\\": \\\"Task complexity x routing dependence analysis. delta_R2 = baseline_R2 - ablated_R2 (L1, ablate_all24). All negative: ablation increased R2. |delta_R2| measures sensitivity to instruction routing.\\\",\\n  \\\"tasks\\\": [\\n    {\\n      \\\"name\\\": \\\"put the wine bottle on the rack\\\",\\n      \\\"baseline_r2\\\": 0.1894,\\n      \\\"ablated_r2\\\": 0.424,\\n      \\\"delta_r2\\\": -0.2346,\\n      \\\"abs_delta_r2\\\": 0.2346,\\n      \\\"group\\\": \\\"complex\\\"\\n    },\\n    {\\n      \\\"name\\\": \\\"put the bowl on top of the cabinet\\\",\\n      \\\"baseline_r2\\\": 0.2561,\\n      \\\"ablated_r2\\\": 0.4567,\\n      \\\"delta_r2\\\": -0.2006,\\n      \\\"abs_delta_r2\\\": 0.2006,\\n      \\\"group\\\": \\\"complex\\\"\\n    },\\n    {\\n      \\\"name\\\": \\\"put the bowl on the stove\\\",\\n      \\\"baseline_r2\\\": 0.2352,\\n      \\\"ablated_r2\\\": 0.395,\\n      \\\"delta_r2\\\": -0.1598,\\n      \\\"abs_delta_r2\\\": 0.1598,\\n      \\\"group\\\": \\\"complex\\\"\\n    },\\n    {\\n      \\\"name\\\": \\\"put the cream cheese in the bowl\\\",\\n      \\\"baseline_r2\\\": 0.186,\\n      \\\"ablated_r2\\\": 0.3454,\\n      \\\"delta_r2\\\": -0.1594,\\n      \\\"abs_delta_r2\\\": 0.1594,\\n      \\\"group\\\": \\\"simple\\\"\\n    },\\n    {\\n      \\\"name\\\": \\\"put the bowl on the plate\\\",\\n      \\\"baseline_r2\\\": 0.3754,\\n      \\\"ablated_r2\\\": 0.474,\\n      \\\"delta_r2\\\": -0.0986,\\n      \\\"abs_delta_r2\\\": 0.0986,\\n      \\\"group\\\": \\\"complex\\\"\\n    },\\n    {\\n      \\\"name\\\": \\\"open the top drawer and put the bowl inside\\\",\\n      \\\"baseline_r2\\\": 0.2649,\\n      \\\"ablated_r2\\\": 0.3403,\\n      \\\"delta_r2\\\": -0.0754,\\n      \\\"abs_delta_r2\\\": 0.0754,\\n      \\\"group\\\": \\\"complex\\\"\\n    },\\n    {\\n      \\\"name\\\": \\\"put the wine bottle on top of the cabinet\\\",\\n      \\\"baseline_
…[truncated 1358 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r2_mse_correlation_20260520T123229",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-20T12:38:38.692289+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "cat /root/autodl-tmp/vla-ssd/results/action_trajectory_analysis.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r2_mse_correlation_20260520T123229",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "cat /root/autodl-tmp/vla-ssd/results/action_trajectory_analysis.json"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-20T12:38:38.692524+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"config\\\": {\\n    \\\"n_tasks\\\": 5,\\n    \\\"n_demos_per_task\\\": 10,\\n    \\\"n_timesteps_per_demo\\\": 50,\\n    \\\"total_forward_passes\\\": 5000,\\n    \\\"model\\\": \\\"openvla-7b\\\",\\n    \\\"ablation\\\": \\\"L1_dominant_24_heads_zeroed\\\",\\n    \\\"ablated_heads\\\": [\\n      0,\\n      1,\\n      2,\\n      4,\\n      7,\\n      8,\\n      10,\\n      11,\\n      12,\\n      14,\\n      15,\\n      16,\\n      17,\\n      18,\\n      19,\\n      20,\\n      22,\\n      23,\\n      25,\\n      26,\\n      27,\\n      29,\\n      30,\\n      31\\n    ],\\n    \\\"unnorm_key\\\": \\\"bridge_orig\\\"\\n  },\\n  \\\"main_metrics\\\": {\\n    \\\"paired_action_mse\\\": {\\n      \\\"mean\\\": 0.04164548042967141,\\n      \\\"std\\\": 0.06394581517413622,\\n      \\\"t_stat\\\": 32.55658746950337,\\n      \\\"p_value\\\": 3.9875267301509806e-194,\\n      \\\"cohens_d\\\": 0.6511317493798869\\n    },\\n    \\\"per_dim_action_shift\\\": {\\n      \\\"means\\\": [\\n        0.0018907630960015738,\\n        0.0053060349467249435,\\n        0.007621298928714849,\\n        0.02059210950341174,\\n        0.030713564767946917,\\n        0.033881929667518705,\\n        0.2907168627450989\\n      ],\\n      \\\"stds\\\": [\\n        0.003945774709271799,\\n        0.007996728850961761,\\n        0.00855598404937074,\\n        0.02115830546884926,\\n        0.02858547485740179,\\n        0.037737860644735575,\\n        0.44894904084862064\\n      ],\\n      \\\"dim_names\\\": [\\n        \\\"dx\\\",\\n        \\\"dy\\\",\\n        \\\"dz\\\",\\n        \\\"rx\\\",\\n        \\\"ry\\\",\\n        \\\"rz\\\",\\n        \\\"gripper\\\"\\n      ]\\n    },\\n    \\\"token_divergence_rate\\\": 0.7230285714285715\\n  },\\n  \\\"secondary_metrics\\\": {\\n    \\\"kl_divergence\\\": {\\n      \\\"mean\\\": 5.07937479019165,\\n      \\\"std\\\": 4.961368560791016,\\n      \\\"per_token_position\\\": [\\n  
…[truncated 6448 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r2_mse_correlation_20260520T123229",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-20T12:38:38.692744+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "head -100 /root/autodl-tmp/vla-ssd/results/dose_response_top24.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r2_mse_correlation_20260520T123229",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "head -100 /root/autodl-tmp/vla-ssd/results/dose_response_top24.json"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-20T12:38:38.692946+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"paired_mse\\\": {\\n    \\\"mean\\\": 0.03824194281111133,\\n    \\\"std\\\": 0.06259905907278887,\\n    \\\"t_stat\\\": 23.652277120477233,\\n    \\\"p_value\\\": 2.3124438825919607e-105,\\n    \\\"cohens_d\\\": 0.6106991692401877,\\n    \\\"ci_95\\\": [\\n      0.578472176208276,\\n      0.6453009849211714\\n    ]\\n  },\\n  \\\"per_dim_shift\\\": {\\n    \\\"dx\\\": {\\n      \\\"mean\\\": 0.0020264886255825254,\\n      \\\"std\\\": 0.004405586184913804\\n    },\\n    \\\"dy\\\": {\\n      \\\"mean\\\": 0.005078928224616185,\\n      \\\"std\\\": 0.007846833659519195\\n    },\\n    \\\"dz\\\": {\\n      \\\"mean\\\": 0.006839640568091587,\\n      \\\"std\\\": 0.0077200397198871834\\n    },\\n    \\\"rx\\\": {\\n      \\\"mean\\\": 0.01958227916286113,\\n      \\\"std\\\": 0.01961555474299405\\n    },\\n    \\\"ry\\\": {\\n      \\\"mean\\\": 0.03157563598838038,\\n      \\\"std\\\": 0.02905062348917955\\n    },\\n    \\\"rz\\\": {\\n      \\\"mean\\\": 0.030789641336462847,\\n      \\\"std\\\": 0.03250205074800802\\n    },\\n    \\\"gripper\\\": {\\n      \\\"mean\\\": 0.2655686274509804,\\n      \\\"std\\\": 0.43856135199571405\\n    }\\n  },\\n  \\\"token_divergence_rate\\\": 0.707047619047619,\\n  \\\"kl_divergence\\\": {\\n    \\\"mean\\\": 5.245793342590332,\\n    \\\"std\\\": 5.2173871994018555\\n  },\\n  \\\"n_samples\\\": 1500,\\n  \\\"per_task\\\": {\\n    \\\"open_the_middle_drawer_of_the_cabinet\\\": {\\n      \\\"paired_mse_mean\\\": 0.022124778983381325,\\n      \\\"token_divergence_rate\\\": 0.6625714285714286,\\n      \\\"kl_mean\\\": 4.529465198516846,\\n      \\\"n_samples\\\": 500\\n    },\\n    \\\"open_the_top_drawer_and_put_the_bowl_inside\\\": {\\n      \\\"paired_mse_mean\\\": 0.04530116625384769,\\n      \\\"token_divergence_rate\\\": 0.7148571428571429,\\n      \\\"kl_mean\\\": 5.16898250579834,\\n      \\\"n_samples\\\": 500\\n    },\\n    \\\"push_the_plate_to_the_front_of
…[truncated 763 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r2_mse_correlation_20260520T123229",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-20T12:38:38.693112+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "head -100 /root/autodl-tmp/vla-ssd/results/counterfactual_wrong.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r2_mse_correlation_20260520T123229",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "head -100 /root/autodl-tmp/vla-ssd/results/counterfactual_wrong.json"
  }
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-20T12:38:38.693241+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "find /root/autodl-tmp/vla-ssd/results/ -name \"*.json\" -path \"*trajectory*\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r2_mse_correlation_20260520T123229",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "find /root/autodl-tmp/vla-ssd/results/ -name \"*.json\" -path \"*trajectory*\""
  }
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-20T12:38:38.693423+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"config\\\": {\\n    \\\"condition\\\": \\\"wrong\\\",\\n    \\\"n_tasks\\\": 3,\\n    \\\"n_demos_per_task\\\": 10,\\n    \\\"n_timesteps_per_demo\\\": 50,\\n    \\\"total_forward_passes\\\": 4500,\\n    \\\"model\\\": \\\"openvla-7b\\\",\\n    \\\"unnorm_key\\\": \\\"bridge_orig\\\",\\n    \\\"gpu\\\": 0,\\n    \\\"seed\\\": 42\\n  },\\n  \\\"global_metrics\\\": {\\n    \\\"paired_mse\\\": {\\n      \\\"mean\\\": 0.058455487649789965,\\n      \\\"std\\\": 0.0692544663275485,\\n      \\\"t_stat\\\": 32.679719283343246,\\n      \\\"p_value\\\": 2.553799316363148e-177,\\n      \\\"cohens_d\\\": 0.8437867236086318\\n    },\\n    \\\"per_dim_shift\\\": {\\n      \\\"means\\\": [\\n        0.005727999085688126,\\n        0.008830657024934012,\\n        0.009574907858035737,\\n        0.025024379181098264,\\n        0.036198595620543346,\\n        0.03649755558156977,\\n        0.40730980392156996\\n      ],\\n      \\\"stds\\\": [\\n        0.005973560517632025,\\n        0.008550926475140793,\\n        0.00835720194565921,\\n        0.02166607415178352,\\n        0.031215809187679588,\\n        0.03229350224391563,\\n        0.4869811885544372\\n      ],\\n      \\\"dim_names\\\": [\\n        \\\"dx\\\",\\n        \\\"dy\\\",\\n        \\\"dz\\\",\\n        \\\"rx\\\",\\n        \\\"ry\\\",\\n        \\\"rz\\\",\\n        \\\"gripper\\\"\\n      ]\\n    },\\n    \\\"token_divergence_rate\\\": 0.8951428571428571,\\n    \\\"kl_divergence\\\": {\\n      \\\"mean\\\": 8.32552719116211,\\n      \\\"std\\\": 5.004848003387451,\\n      \\\"per_token_position\\\": [\\n        4.15487813949585,\\n        8.225351333618164,\\n        10.143592834472656,\\n        10.94106388092041,\\n        11.698100090026855,\\n        10.461137771606445,\\n        2.654557228088379\\n      ]\\n    },\\n    \\\"wilcoxon_p\\\": 1.0089211937209574e-246,\\n    \\\"n_samples\\\": 1500\\n  },\\n  \\\"per_task\\\": {\\n    \\\"open_the
…[truncated 1147 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r2_mse_correlation_20260520T123229",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-20T12:38:38.693587+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/vla-ssd/results/action_trajectory_analysis.json\\n/root/autodl-tmp/vla-ssd/results/action_trajectory_control.json\\n/root/autodl-tmp/vla-ssd/results/action_trajectory_L8_ablation.json\\n/root/autodl-tmp/vla-ssd/results/action_trajectory_L13_ablation.json\\n/root/autodl-tmp/vla-ssd/results/action_trajectory_extended_analysis.json\\n/root/autodl-tmp/vla-ssd/results/trajectory_level_cohens_d.json\\n/root/autodl-tmp/vla-ssd/results/action_trajectory_cpu_analysis.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r2_mse_correlation_20260520T123229",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-20T12:38:38.693730+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "head -80 /root/autodl-tmp/vla-ssd/results/action_trajectory_extended_analysis.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r2_mse_correlation_20260520T123229",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "head -80 /root/autodl-tmp/vla-ssd/results/action_trajectory_extended_analysis.json"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-20T12:38:38.693906+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"temporal_coherence_proxy\\\": {\\n    \\\"method\\\": \\\"proxy (per-dim CV + cross-task I^2)\\\",\\n    \\\"note\\\": \\\"Exact within-demo autocorrelation requires per-timestep trajectory data not saved in JSON. These are indirect proxies.\\\",\\n    \\\"per_dim_cv\\\": [\\n      {\\n        \\\"dim\\\": \\\"dx\\\",\\n        \\\"inst_mean_shift\\\": 0.0018907630960015738,\\n        \\\"inst_std_shift\\\": 0.003945774709271799,\\n        \\\"inst_cv\\\": 2.0868689036802075,\\n        \\\"ctrl_mean_shift\\\": 0.00037120977075240174,\\n        \\\"ctrl_std_shift\\\": 0.0018871390276948216,\\n        \\\"ctrl_cv\\\": 5.083753651930542\\n      },\\n      {\\n        \\\"dim\\\": \\\"dy\\\",\\n        \\\"inst_mean_shift\\\": 0.0053060349467249435,\\n        \\\"inst_std_shift\\\": 0.007996728850961761,\\n        \\\"inst_cv\\\": 1.5071006752222016,\\n        \\\"ctrl_mean_shift\\\": 0.001246604812974087,\\n        \\\"ctrl_std_shift\\\": 0.004219931004787625,\\n        \\\"ctrl_cv\\\": 3.385139348788431\\n      },\\n      {\\n        \\\"dim\\\": \\\"dz\\\",\\n        \\\"inst_mean_shift\\\": 0.007621298928714849,\\n        \\\"inst_std_shift\\\": 0.00855598404937074,\\n        \\\"inst_cv\\\": 1.1226411835303123,\\n        \\\"ctrl_mean_shift\\\": 0.002426664148676048,\\n        \\\"ctrl_std_shift\\\": 0.00600886986156851,\\n        \\\"ctrl_cv\\\": 2.476185204634461\\n      },\\n      {\\n        \\\"dim\\\": \\\"rx\\\",\\n        \\\"inst_mean_shift\\\": 0.02059210950341174,\\n        \\\"inst_std_shift\\\": 0.02115830546884926,\\n        \\\"inst_cv\\\": 1.027495772851427,\\n        \\\"ctrl_mean_shift\\\": 0.007850111136374748,\\n        \\\"ctrl_std_shift\\\": 0.01622055322496688,\\n        \\\"ctrl_cv\\\": 2.066283259329457\\n      },\\n      {\\n        \\\"dim\\\": \\\"ry\\\",\\n        \\\"inst_mean_shift\\\": 0.030713564767946917,\\n        \\\"inst_std_shift\\\": 0.02858547485740179,\\n     
…[truncated 1593 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r2_mse_correlation_20260520T123229",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-20T12:38:38.694083+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "head -80 /root/autodl-tmp/vla-ssd/results/trajectory_level_cohens_d.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r2_mse_correlation_20260520T123229",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "head -80 /root/autodl-tmp/vla-ssd/results/trajectory_level_cohens_d.json"
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-20T12:38:38.694245+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"method\\\": \\\"demo-level aggregation, paired Cohen's d, bootstrap CI B=10000\\\",\\n  \\\"description\\\": \\\"Each demo's MSE is the mean of its 50 timestep-level MSEs. Cohen's d = mean(demo_mses) / std(demo_mses, ddof=1). Bootstrap CI: 10000 resamples of demo-level values.\\\",\\n  \\\"n_timesteps_per_demo\\\": 50,\\n  \\\"results\\\": [\\n    {\\n      \\\"experiment\\\": \\\"counterfactual\\\",\\n      \\\"condition\\\": \\\"counterfactual_empty\\\",\\n      \\\"token_level_d\\\": 0.968,\\n      \\\"trajectory_level_d\\\": 3.4378,\\n      \\\"ci_lower\\\": 2.9209,\\n      \\\"ci_upper\\\": 4.4475,\\n      \\\"n_demos\\\": 30,\\n      \\\"demo_mses\\\": [\\n        0.082062,\\n        0.068606,\\n        0.053453,\\n        0.091422,\\n        0.105778,\\n        0.087411,\\n        0.079496,\\n        0.080063,\\n        0.091432,\\n        0.088599,\\n        0.06874,\\n        0.097388,\\n        0.083217,\\n        0.083121,\\n        0.060285,\\n        0.088588,\\n        0.059896,\\n        0.08625,\\n        0.079877,\\n        0.060748,\\n        0.034709,\\n        0.048997,\\n        0.049401,\\n        0.043439,\\n        0.037609,\\n        0.049011,\\n        0.051957,\\n        0.068949,\\n        0.037481,\\n        0.048885\\n      ],\\n      \\\"inflation_factor\\\": 0.282\\n    },\\n    {\\n      \\\"experiment\\\": \\\"counterfactual\\\",\\n      \\\"condition\\\": \\\"counterfactual_paraphrased\\\",\\n      \\\"token_level_d\\\": 0.697,\\n      \\\"trajectory_level_d\\\": 2.1306,\\n      \\\"ci_lower\\\": 1.7399,\\n      \\\"ci_upper\\\": 2.8192,\\n      \\\"n_demos\\\": 30,\\n      \\\"demo_mses\\\": [\\n        0.035076,\\n        0.010262,\\n        0.039509,\\n        0.017612,\\n        0.020804,\\n        0.02749,\\n        0.027929,\\n        0.009308,\\n        0.01489,\\n        0.023217,\\n        0.043261,\\n        0.037765,\\n        0.045553,\\n        0.040398,
…[truncated 302 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r2_mse_correlation_20260520T123229",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-20T12:38:38.694465+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-19183",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c \"\nimport json, numpy as np\nfrom scipy.stats import spearmanr, kendalltau\n\n# ===== Load data =====\nwith open('/root/autodl-tmp/vla-ssd/results/action_trajectory_analysis.json') as f:\n    traj = json.load(f)\n\nwith open('/root/autodl-tmp/vla-ssd/results/per_task_r2_distribution.json') as f:\n    r2_dist = json.load(f)\n\nwith open('/root/autodl-tmp/vla-ssd/results/functional_validation/unified_action_probe.json') as f:\n    unified = json.load(f)\n\nwith open('/root/autodl-tmp/vla-ssd/results/l1_head_ablation/action_probe_50demos.json') as f:\n    ap50 = json.load(f)\n\n# ===== 5-task behavioral data =====\ntask_map = {\n    'open_the_middle_drawer_of_the_cabinet': 'open the middle drawer of the cabinet',\n    'open_the_top_drawer_and_put_the_bowl_inside': 'open the top drawer and put the bowl inside',\n    'push_the_plate_to_the_front_of_the_stove': 'push the plate to the front of the stove',\n    'put_the_bowl_on_the_plate': 'put the bowl on the plate',\n    'put_the_bowl_on_the_stove': 'put the bowl on the stove',\n}\n\n# Per-task behavioral: paired_mse and cohens_d from L1 instruction head ablation\ntasks_5 = list(task_map.keys())\npaired_mse = [traj['per_task'][t]['paired_mse']['mean'] for t in tasks_5]\ncohens_d = [traj['per_task'][t]['paired_mse']['cohens_d'] for t in tasks_5]\ntoken_div = [traj['per_task'][t]['token_divergence_rate'] for t in tasks_5]\nkl_div = [traj['per_task'][t]['kl_divergence']['mean'] for t in tasks_5]\n\n# Per-task R2 from baseline probes (5-demo, various layers)\ntasks_5_named = [task_map[t] for t in tasks_5]\nr2_baseline_L1 = [r2_dist['mlp_probe_5demo']['conditions']['baseline']['L1']['per_task_R2'][t] for t in tasks_5_named]\nr2_baseline_L8 = [r2_dist['mlp_probe_5demo']['conditions']['baseline']['L8']['per_task_R2'][t] for t in tasks_5_named]\nr2_baseline_L13 = [r2_dist['mlp_probe_5demo']['conditions']['baseline']['L13']['per_task_R2'][t] for t in tasks_5_named]\n\n# Per-task R2 from 50-demo probes (various readout sources)\ntasks_5_under = list(task_map.keys())\nr2_projector = [unified['projector']['per_task_R2'][t] for t in tasks_5_under]\nr2_dino = [unified['dino_cls']['per_task_R2'][t] for t in tasks_5_under]\nr2_vla_last = [unified['vla_last_preaction_L19']['per_task_R2'][t] for t in tasks_5_under]\n\n# Per-task R2 delta from ablation (all 10 tasks available, use 5)\nr2_delta_L1 = [ap50['bootstrap_paired_CI']['baseline_vs_ablate_all24']['L1']['per_task_diffs'][t] for t in tasks_5_named]\nr2_delta_L8 = [ap50['bootstrap_paired_CI']['baseline_vs_ablate_all24']['L8']['per_task_diffs'][t] for t in tasks_5_named]\n\nprint('=' * 70)\nprint('RANK CORRELATION: Probe R2 vs Per-Task Behavioral Outcomes (n=5)')\nprint('=' * 70)\n\n# Helper\ndef report(name_x, name_y, x, y):\n    rho, p_rho = spearmanr(x, y)\n    tau, p_tau = kendalltau(x, y)\n    print(f'  {name_x} vs {name_y}:')\n    print(f'    Spearman rho={rho:.4f}, p={p_rho:.4f}  |  Kendall tau={tau:.4f}, p={p_tau:.4f}')\n    for i, t in enumerate(tasks_5):\n        short = t.replace('_', ' ')[:40]\n        print(f'      {short:40s}  x={x[i]:.4f}  y={y[i]:.4f}')\n    print()\n\nprint()\nprint('--- (A) Baseline Probe R2 vs Paired MSE (ablation behavioral shift) ---')\nreport('R2_baseline_L1_5demo', 'paired_mse', r2_baseline_L1, paired_mse)\nreport('R2_baseline_L8_5demo', 'paired_mse', r2_baseline_L8, paired_mse)\nreport('R2_baseline_L13_5demo', 'paired_mse', r2_baseline_L13, paired_mse)\nreport('R2_projector_50demo', 'paired_mse', r2_projector, paired_mse)\nreport('R2_dino_50demo', 'paired_mse', r2_dino, paired_mse)\nreport('R2_vla_last_preaction_L19', 'paired_mse', r2_vla_last, paired_mse)\n\nprint('--- (B) Baseline Probe R2 vs Cohen d (ablation effect size) ---')\nreport('R2_baseline_L1_5demo', 'cohens_d', r2_baseline_L1, cohens_d)\nreport('R2_vla_last_preaction_L19', 'cohens_d', r2_vla_last, cohens_d)\n\nprint('--- (C) R2 Delta (ablation representational impact) vs Paired MSE ---')\nreport('R2_delta_L1_ablation', 'paired_mse', r2_delta_L1, paired_mse)\nreport('R2_delta_L8_ablation', 'paired_mse', r2_delta_L8, paired_mse)\n\nprint('--- (D) Baseline Probe R2 vs Token Divergence Rate ---')\nreport('R2_baseline_L1_5demo', 'token_div_rate', r2_baseline_L1, token_div)\nreport('R2_vla_last_preaction_L19', 'token_div_rate', r2_vla_last, token_div)\n\nprint('--- (E) Baseline Probe R2 vs KL Divergence ---')\nreport('R2_baseline_L1_5demo', 'kl_divergence', r2_baseline_L1, kl_div)\n\n# ===== Also compute with all 10 tasks where we can =====\nprint('=' * 70)\nprint('FULL 10-TASK ANALYSIS (representational metrics only)')\nprint('=' * 70)\n\nall_10_tasks = r2_dist['tasks']\nr2_all10_L1 = [r2_dist['mlp_probe_5demo']['conditions']['baseline']['L1']['per_task_R2'][t] for t in all_10_tasks]\nr2_all10_L8 = [r2_dist['mlp_probe_5demo']['conditions']['baseline']['L8']['per_task_R2'][t] for t in all_10_tasks]\nr2_all10_L13 = [r2_dist['mlp_probe_5demo']['conditions']['baseline']['L13']['per_task_R2'][t] for t in all_10_tasks]\n\n# R2 delta for all 10\nr2_delta_all10_L1 = [ap50['bootstrap_paired_CI']['baseline_vs_ablate_all24']['L1']['per_task_diffs'][t] for t in all_10_tasks]\n\n# All-10 unified probe R2\ntasks_10_under = [t.replace(' ', '_') for t in all_10_tasks]\nr2_proj_all10 = [unified['projector']['per_task_R2'][t] for t in tasks_10_under]\nr2_vla_all10 = [unified['vla_last_preaction_L19']['per_task_R2'][t] for t in tasks_10_under]\n\nprint()\nprint('--- Cross-layer R2 consistency (all 10 tasks) ---')\nreport_10 = lambda nx, ny, x, y: print(f'  {nx} vs {ny}: rho={spearmanr(x,y)[0]:.4f} (p={spearmanr(x,y)[1]:.4f}), tau={kendalltau(x,y)[0]:.4f} (p={kendalltau(x,y)[1]:.4f})')\nreport_10('R2_L1', 'R2_L8', r2_all10_L1, r2_all10_L8)\nreport_10('R2_L1', 'R2_L13', r2_all10_L1, r2_all10_L13)\nreport_10('R2_L8', 'R2_L13', r2_all10_L8, r2_all10_L13)\nreport_10('R2_projector', 'R2_vla_last_L19', r2_proj_all10, r2_vla_all10)\nreport_10('R2_L1', 'R2_delta_L1', r2_all10_L1, r2_delta_all10_L1)\n\nprint()\nprint('--- Per-task summary for all 10 tasks ---')\nprint(f'{\\\"Task\\\":50s} R2_L1  R2_L8  R2_L13  R2_proj  R2_vla  dR2_L1')\nfor i, t in enumerate(all_10_tasks):\n    short = t[:48]\n    print(f'{short:50s} {r2_all10_L1[i]:.3f}  {r2_all10_L8[i]:.3f}  {r2_all10_L13[i]:.3f}   {r2_proj_all10[i]:.3f}    {r2_vla_all10[i]:.3f}   {r2_delta_all10_L1[i]:.3f}')\n\n# Now try to also use 3-task MSE vs GT\nprint()\nprint('=' * 70)\nprint('3-TASK ANALYSIS: Probe R2 vs Model Action MSE (model-vs-GT)')\nprint('=' * 70)\nwith open('/root/autodl-tmp/vla-ssd/results/groundtruth_action_error.json') as f:\n    gt = json.load(f)\n\ntasks_3 = [t['task_name'] for t in gt['per_task']]\nmse_gt = [gt['per_task'][t]['original']['mse']['mean'] for t in tasks_3]\ntasks_3_named = [t.replace('_', ' ') for t in tasks_3]\nr2_3_L1 = [r2_dist['mlp_probe_5demo']['conditions']['baseline']['L1']['per_task_R2'][t] for t in tasks_3_named]\nr2_3_L8 = [r2_dist['mlp_probe_5demo']['conditions']['baseline']['L8']['per_task_R2'][t] for t in tasks_3_named]\nr2_3_L13 = [r2_dist['mlp_probe_5demo']['conditions']['baseline']['L13']['per_task_R2'][t] for t in tasks_3_named]\nr2_3_proj = [unified['projector']['per_task_R2'][t] for t in tasks_3]\nr2_3_vla = [unified['vla_last_preaction_L19']['per_task_R2'][t] for t in tasks_3]\n\nprint()\nfor i in range(3):\n    print(f'  {tasks_3_named[i]:50s} MSE={mse_gt[i]:.4f}  R2_L1={r2_3_L1[i]:.4f}  R2_L13={r2_3_L13[i]:.4f}  R2_proj={r2_3_proj[i]:.4f}')\nprint()\nprint('  NOTE: n=3, correlation statistics not meaningful')\n\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r2_mse_correlation_20260520T123229",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-19183",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c \"\nimport json, numpy as np\nfrom scipy.stats import spearmanr, kendalltau\n\n# ===== Load data =====\nwith open('/root/autodl-tmp/vla-ssd/results/action_trajectory_analysis.json') as f:\n    traj = json.load(f)\n\nwith open('/root/autodl-tmp/vla-ssd/results/per_task_r2_distribution.json') as f:\n    r2_dist = json.load(f)\n\nwith open('/root/autodl-tmp/vla-ssd/results/functional_validation/unified_action_probe.json') as f:\n    unified = json.load(f)\n\nwith open('/root/autodl-tmp/vla-ssd/results/l1_head_ablation/action_probe_50demos.json') as f:\n    ap50 = json.load(f)\n\n# ===== 5-task behavioral data =====\ntask_map = {\n    'open_the_middle_drawer_of_the_cabinet': 'open the middle drawer of the cabinet',\n    'open_the_top_drawer_and_put_the_bowl_inside': 'open the top drawer and put the bowl inside',\n    'push_the_plate_to_the_front_of_the_stove': 'push the plate to the front of the stove',\n    'put_the_bowl_on_the_plate': 'put the bowl on the plate',\n    'put_the_bowl_on_the_stove': 'put the bowl on the stove',\n}\n\n# Per-task behavioral: paired_mse and cohens_d from L1 instruction head ablation\ntasks_5 = list(task_map.keys())\npaired_mse = [traj['per_task'][t]['paired_mse']['mean'] for t in tasks_5]\ncohens_d = [traj['per_task'][t]['paired_mse']['cohens_d'] for t in tasks_5]\ntoken_div = [traj['per_task'][t]['token_divergence_rate'] for t in tasks_5]\nkl_div = [traj['per_task'][t]['kl_divergence']['mean'] for t in tasks_5]\n\n# Per-task R2 from baseline probes (5-demo, various layers)\ntasks_5_named = [task_map[t] for t in tasks_5]\nr2_baseline_L1 = [r2_dist['mlp_probe_5demo']['conditions']['baseline']['L1']['per_task_R2'][t] for t in tasks_5_named]\nr2_baseline_L8 = [r2_dist['mlp_probe_5demo']['conditions']['baseline']['L8']['per_task_R2'][t] for t in tasks_5_named]\nr2_baseline_L13 = [r2_dist['mlp_probe_5demo']['conditions']['baseline']['L13']['per_task_R2'][t] for t in tasks_5_named]\n\n# Per-task R2 from 50-demo probes (various readout sources)\ntasks_5_under = list(task_map.keys())\nr2_projector = [unified['projector']['per_task_R2'][t] for t in tasks_5_under]\nr2_dino = [unified['dino_cls']['per_task_R2'][t] for t in tasks_5_under]\nr2_vla_last = [unified['vla_last_preaction_L19']['per_task_R2'][t] for t in tasks_5_under]\n\n# Per-task R2 delta from ablation (all 10 tasks available, use 5)\nr2_delta_L1 = [ap50['bootstrap_paired_CI']['baseline_vs_ablate_all24']['L1']['per_task_diffs'][t] for t in tasks_5_named]\nr2_delta_L8 = [ap50['bootstrap_paired_CI']['baseline_vs_ablate_all24']['L8']['per_task_diffs'][t] for t in tasks_5_named]\n\nprint('=' * 70)\nprint('RANK CORRELATION: Probe R2 vs Per-Task Behavioral Outcomes (n=5)')\nprint('=' * 70)\n\n# Helper\ndef report(name_x, name_y, x, y):\n    rho, p_rho = spearmanr(x, y)\n    tau, p_tau = kendalltau(x, y)\n    print(f'  {name_x} vs {name_y}:')\n    print(f'    Spearman rho={rho:.4f}, p={p_rho:.4f}  |  Kendall tau={tau:.4f}, p={p_tau:.4f}')\n    for i, t in enumerate(tasks_5):\n        short = t.replace('_', ' ')[:40]\n        print(f'      {short:40s}  x={x[i]:.4f}  y={y[i]:.4f}')\n    print()\n\nprint()\nprint('--- (A) Baseline Probe R2 vs Paired MSE (ablation behavioral shift) ---')\nreport('R2_baseline_L1_5demo', 'paired_mse', r2_baseline_L1, paired_mse)\nreport('R2_baseline_L8_5demo', 'paired_mse', r2_baseline_L8, paired_mse)\nreport('R2_baseline_L13_5demo', 'paired_mse', r2_baseline_L13, paired_mse)\nreport('R2_projector_50demo', 'paired_mse', r2_projector, paired_mse)\nreport('R2_dino_50demo', 'paired_mse', r2_dino, paired_mse)\nreport('R2_vla_last_preaction_L19', 'paired_mse', r2_vla_last, paired_mse)\n\nprint('--- (B) Baseline Probe R2 vs Cohen d (ablation effect size) ---')\nreport('R2_baseline_L1_5demo', 'cohens_d', r2_baseline_L1, cohens_d)\nreport('R2_vla_last_preaction_L19', 'cohens_d', r2_vla_last, cohens_d)\n\nprint('--- (C) R2 Delta (ablation representational impact) vs Paired MSE ---')\nreport('R2_delta_L1_ablation', 'paired_mse', r2_delta_L1, paired_mse)\nreport('R2_delta_L8_ablation', 'paired_mse', r2_delta_L8, paired_mse)\n\nprint('--- (D) Baseline Probe R2 vs Token Divergence Rate ---')\nreport('R2_baseline_L1_5demo', 'token_div_rate', r2_baseline_L1, token_div)\nreport('R2_vla_last_preaction_L19', 'token_div_rate', r2_vla_last, token_div)\n\nprint('--- (E) Baseline Probe R2 vs KL Divergence ---')\nreport('R2_baseline_L1_5demo', 'kl_divergence', r2_baseline_L1, kl_div)\n\n# ===== Also compute with all 10 tasks where we can =====\nprint('=' * 70)\nprint('FULL 10-TASK ANALYSIS (representational metrics only)')\nprint('=' * 70)\n\nall_10_tasks = r2_dist['tasks']\nr2_all10_L1 = [r2_dist['mlp_probe_5demo']['conditions']['baseline']['L1']['per_task_R2'][t] for t in all_10_tasks]\nr2_all10_L8 = [r2_dist['mlp_probe_5demo']['conditions']['baseline']['L8']['per_task_R2'][t] for t in all_10_tasks]\nr2_all10_L13 = [r2_dist['mlp_probe_5demo']['conditions']['baseline']['L13']['per_task_R2'][t] for t in all_10_tasks]\n\n# R2 delta for all 10\nr2_delta_all10_L1 = [ap50['bootstrap_paired_CI']['baseline_vs_ablate_all24']['L1']['per_task_diffs'][t] for t in all_10_tasks]\n\n# All-10 unified probe R2\ntasks_10_under = [t.replace(' ', '_') for t in all_10_tasks]\nr2_proj_all10 = [unified['projector']['per_task_R2'][t] for t in tasks_10_under]\nr2_vla_all10 = [unified['vla_last_preaction_L19']['per_task_R2'][t] for t in tasks_10_under]\n\nprint()\nprint('--- Cross-layer R2 consistency (all 10 tasks) ---')\nreport_10 = lambda nx, ny, x, y: print(f'  {nx} vs {ny}: rho={spearmanr(x,y)[0]:.4f} (p={spearmanr(x,y)[1]:.4f}), tau={kendalltau(x,y)[0]:.4f} (p={kendalltau(x,y)[1]:.4f})')\nreport_10('R2_L1', 'R2_L8', r2_all10_L1, r2_all10_L8)\nreport_10('R2_L1', 'R2_L13', r2_all10_L1, r2_all10_L13)\nreport_10('R2_L8', 'R2_L13', r2_all10_L8, r2_all10_L13)\nreport_10('R2_projector', 'R2_vla_last_L19', r2_proj_all10, r2_vla_all10)\nreport_10('R2_L1', 'R2_delta_L1', r2_all10_L1, r2_delta_all10_L1)\n\nprint()\nprint('--- Per-task summary for all 10 tasks ---')\nprint(f'{\\\"Task\\\":50s} R2_L1  R2_L8  R2_L13  R2_proj  R2_vla  dR2_L1')\nfor i, t in enumerate(all_10_tasks):\n    short = t[:48]\n    print(f'{short:50s} {r2_all10_L1[i]:.3f}  {r2_all10_L8[i]:.3f}  {r2_all10_L13[i]:.3f}   {r2_proj_all10[i]:.3f}    {r2_vla_all10[i]:.3f}   {r2_delta_all10_L1[i]:.3f}')\n\n# Now try to also use 3-task MSE vs GT\nprint()\nprint('=' * 70)\nprint('3-TASK ANALYSIS: Probe R2 vs Model Action MSE (model-vs-GT)')\nprint('=' * 70)\nwith open('/root/autodl-tmp/vla-ssd/results/groundtruth_action_error.json') as f:\n    gt = json.load(f)\n\ntasks_3 = [t['task_name'] for t in gt['per_task']]\nmse_gt = [gt['per_task'][t]['original']['mse']['mean'] for t in tasks_3]\ntasks_3_named = [t.replace('_', ' ') for t in tasks_3]\nr2_3_L1 = [r2_dist['mlp_probe_5demo']['conditions']['baseline']['L1']['per_task_R2'][t] for t in tasks_3_named]\nr2_3_L8 = [r2_dist['mlp_probe_5demo']['conditions']['baseline']['L8']['per_task_R2'][t] for t in tasks_3_named]\nr2_3_L13 = [r2_dist['mlp_probe_5demo']['conditions']['baseline']['L13']['per_task_R2'][t] for t in tasks_3_named]\nr2_3_proj = [unified['projector']['per_task_R2'][t] for t in tasks_3]\nr2_3_vla = [unified['vla_last_preaction_L19']['per_task_R2'][t] for t in tasks_3]\n\nprint()\nfor i in range(3):\n    print(f'  {tasks_3_named[i]:50s} MSE={mse_gt[i]:.4f}  R2_L1={r2_3_L1[i]:.4f}  R2_L13={r2_3_L13[i]:.4f}  R2_proj={r2_3_proj[i]:.4f}')\nprint()\nprint('  NOTE: n=3, correlation statistics not meaningful')\n\"\n"
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-20T12:38:38.694793+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Encountered a bad command exit code!\\n\\nCommand: 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c \\\"\\\\nimport json, numpy as np\\\\nfrom scipy.stats import spearmanr, kendalltau\\\\n\\\\n# ===== Load data =====\\\\nwith open(\\\\'/root/autodl-tmp/vla-ssd/results/action_trajectory_analysis.json\\\\') as f:\\\\n    traj = json.load(f)\\\\n\\\\nwith open(\\\\'/root/autodl-tmp/vla-ssd/results/per_task_r2_distribution.json\\\\') as f:\\\\n    r2_dist = json.load(f)\\\\n\\\\nwith open(\\\\'/root/autodl-tmp/vla-ssd/results/functional_validation/unified_action_probe.json\\\\') as f:\\\\n    unified = json.load(f)\\\\n\\\\nwith open(\\\\'/root/autodl-tmp/vla-ssd/results/l1_head_ablation/action_probe_50demos.json\\\\') as f:\\\\n    ap50 = json.load(f)\\\\n\\\\n# ===== 5-task behavioral data =====\\\\ntask_map = {\\\\n    \\\\'open_the_middle_drawer_of_the_cabinet\\\\': \\\\'open the middle drawer of the cabinet\\\\',\\\\n    \\\\'open_the_top_drawer_and_put_the_bowl_inside\\\\': \\\\'open the top drawer and put the bowl inside\\\\',\\\\n    \\\\'push_the_plate_to_the_front_of_the_stove\\\\': \\\\'push the plate to the front of the stove\\\\',\\\\n    \\\\'put_the_bowl_on_the_plate\\\\': \\\\'put the bowl on the plate\\\\',\\\\n    \\\\'put_the_bowl_on_the_stove\\\\': \\\\'put the bowl on the stove\\\\',\\\\n}\\\\n\\\\n# Per-task behavioral: paired_mse and cohens_d from L1 instruction head ablation\\\\ntasks_5 = list(task_map.keys())\\\\npaired_mse = [traj[\\\\'per_task\\\\'][t][\\\\'paired_mse\\\\'][\\\\'mean\\\\'] for t in tasks_5]\\\\ncohens_d = [traj[\\\\'per_task\\\\'][t][\\\\'paired_mse\\\\'][\\\\'cohens_d\\\\'] for t in tasks_5]\\\\ntoken_div = [traj[\\\\'per_task\\\\'][t][\\\\'token_divergence_rate\\\\'] for t in tasks_5]\\\\nkl_div = [traj[\\\\'per_task\\\\'][t][\\\\'kl_divergence\\\\'][\\\\'mean\\\\'] for t in tasks_5]\\\\n\\\\n# Per-task R2 from baseline probes (5-d
…[truncated 8571 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r2_mse_correlation_20260520T123229",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-20T12:38:38.695034+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-19183",
  "command": "cat > /tmp/rank_corr.py << 'PYEOF'\nimport json, numpy as np\nfrom scipy.stats import spearmanr, kendalltau\n\n# ===== Load data =====\nwith open('/root/autodl-tmp/vla-ssd/results/action_trajectory_analysis.json') as f:\n    traj = json.load(f)\nwith open('/root/autodl-tmp/vla-ssd/results/per_task_r2_distribution.json') as f:\n    r2_dist = json.load(f)\nwith open('/root/autodl-tmp/vla-ssd/results/functional_validation/unified_action_probe.json') as f:\n    unified = json.load(f)\nwith open('/root/autodl-tmp/vla-ssd/results/l1_head_ablation/action_probe_50demos.json') as f:\n    ap50 = json.load(f)\nwith open('/root/autodl-tmp/vla-ssd/results/groundtruth_action_error.json') as f:\n    gt = json.load(f)\n\n# ===== Task name mappings =====\ntask_map = {\n    'open_the_middle_drawer_of_the_cabinet': 'open the middle drawer of the cabinet',\n    'open_the_top_drawer_and_put_the_bowl_inside': 'open the top drawer and put the bowl inside',\n    'push_the_plate_to_the_front_of_the_stove': 'push the plate to the front of the stove',\n    'put_the_bowl_on_the_plate': 'put the bowl on the plate',\n    'put_the_bowl_on_the_stove': 'put the bowl on the stove',\n}\n\ntasks_5 = list(task_map.keys())\ntasks_5_named = [task_map[t] for t in tasks_5]\n\n# ===== 5-task behavioral data =====\npaired_mse = [traj['per_task'][t]['paired_mse']['mean'] for t in tasks_5]\ncohens_d = [traj['per_task'][t]['paired_mse']['cohens_d'] for t in tasks_5]\ntoken_div = [traj['per_task'][t]['token_divergence_rate'] for t in tasks_5]\nkl_div = [traj['per_task'][t]['kl_divergence']['mean'] for t in tasks_5]\n\n# ===== Per-task R2 (representational metrics) =====\nr2_L1 = [r2_dist['mlp_probe_5demo']['conditions']['baseline']['L1']['per_task_R2'][t] for t in tasks_5_named]\nr2_L8 = [r2_dist['mlp_probe_5demo']['conditions']['baseline']['L8']['per_task_R2'][t] for t in tasks_5_named]\nr2_L13 = [r2_dist['mlp_probe_5demo']['conditions']['baseline']['L13']['per_task_R2'][t] for t in tasks_5_named]\nr2_proj = [unified['projector']['per_task_R2'][t] for t in tasks_5]\nr2_dino = [unified['dino_cls']['per_task_R2'][t] for t in tasks_5]\nr2_vla = [unified['vla_last_preaction_L19']['per_task_R2'][t] for t in tasks_5]\nr2_delta_L1 = [ap50['bootstrap_paired_CI']['baseline_vs_ablate_all24']['L1']['per_task_diffs'][t] for t in tasks_5_named]\nr2_delta_L8 = [ap50['bootstrap_paired_CI']['baseline_vs_ablate_all24']['L8']['per_task_diffs'][t] for t in tasks_5_named]\n\ndef report(name_x, name_y, x, y, show_data=True):\n    rho, p_rho = spearmanr(x, y)\n    tau, p_tau = kendalltau(x, y)\n    sig_s = '*' if p_rho < 0.05 else ''\n    sig_k = '*' if p_tau < 0.05 else ''\n    print(f'  {name_x} vs {name_y}:')\n    print(f'    Spearman rho={rho:+.4f} (p={p_rho:.4f}){sig_s}  |  Kendall tau={tau:+.4f} (p={p_tau:.4f}){sig_k}')\n    if show_data:\n        for i, t in enumerate(tasks_5):\n            short = t.replace('_', ' ')[:40]\n            print(f'      {short:40s}  x={x[i]:.4f}  y={y[i]:.4f}')\n    print()\n\nprint('=' * 70)\nprint('RANK CORRELATION: Probe R2 vs Behavioral Outcomes (n=5 tasks)')\nprint('=' * 70)\nprint()\n\nprint('--- (A) Baseline Probe R2 vs Paired MSE (ablation action shift) ---')\nreport('R2_baseline_L1_5demo', 'paired_mse', r2_L1, paired_mse)\nreport('R2_baseline_L8_5demo', 'paired_mse', r2_L8, paired_mse)\nreport('R2_baseline_L13_5demo', 'paired_mse', r2_L13, paired_mse)\nreport('R2_projector_50demo', 'paired_mse', r2_proj, paired_mse)\nreport('R2_dino_50demo', 'paired_mse', r2_dino, paired_mse)\nreport('R2_vla_last_L19_50demo', 'paired_mse', r2_vla, paired_mse)\n\nprint('--- (B) Baseline Probe R2 vs Cohen d (ablation effect size) ---')\nreport('R2_baseline_L1_5demo', 'cohens_d', r2_L1, cohens_d)\nreport('R2_projector_50demo', 'cohens_d', r2_proj, cohens_d)\nreport('R2_vla_last_L19_50demo', 'cohens_d', r2_vla, cohens_d)\n\nprint('--- (C) R2 Delta (abl. rep. impact) vs Paired MSE (abl. beh. impact) ---')\nreport('R2_delta_L1', 'paired_mse', r2_delta_L1, paired_mse)\nreport('R2_delta_L8', 'paired_mse', r2_delta_L8, paired_mse)\n\nprint('--- (D) Baseline Probe R2 vs Token Divergence Rate ---')\nreport('R2_baseline_L1_5demo', 'token_div_rate', r2_L1, token_div)\nreport('R2_vla_last_L19_50demo', 'token_div_rate', r2_vla, token_div)\n\nprint('--- (E) Baseline Probe R2 vs KL Divergence ---')\nreport('R2_baseline_L1_5demo', 'kl_divergence', r2_L1, kl_div)\n\n# ===== 10-task analysis =====\nprint('=' * 70)\nprint('FULL 10-TASK ANALYSIS (cross-representational consistency)')\nprint('=' * 70)\nall_10 = r2_dist['tasks']\nr2_10_L1 = [r2_dist['mlp_probe_5demo']['conditions']['baseline']['L1']['per_task_R2'][t] for t in all_10]\nr2_10_L8 = [r2_dist['mlp_probe_5demo']['conditions']['baseline']['L8']['per_task_R2'][t] for t in all_10]\nr2_10_L13 = [r2_dist['mlp_probe_5demo']['conditions']['baseline']['L13']['per_task_R2'][t] for t in all_10]\nt10_under = [t.replace(' ', '_') for t in all_10]\nr2_10_proj = [unified['projector']['per_task_R2'][t] for t in t10_under]\nr2_10_vla = [unified['vla_last_preaction_L19']['per_task_R2'][t] for t in t10_under]\nr2_10_delta = [ap50['bootstrap_paired_CI']['baseline_vs_ablate_all24']['L1']['per_task_diffs'][t] for t in all_10]\n\ndef rep10(nx, ny, x, y):\n    rho, p = spearmanr(x, y)\n    tau, pt = kendalltau(x, y)\n    s = '*' if p < 0.05 else ''\n    print(f'  {nx} vs {ny}: rho={rho:+.4f} (p={p:.4f}){s}, tau={tau:+.4f} (p={pt:.4f})')\n\nprint()\nprint('--- Cross-layer/cross-source R2 consistency ---')\nrep10('R2_L1_5d', 'R2_L8_5d', r2_10_L1, r2_10_L8)\nrep10('R2_L1_5d', 'R2_L13_5d', r2_10_L1, r2_10_L13)\nrep10('R2_L8_5d', 'R2_L13_5d', r2_10_L8, r2_10_L13)\nrep10('R2_proj_50d', 'R2_vla_L19_50d', r2_10_proj, r2_10_vla)\nrep10('R2_L1_5d', 'R2_proj_50d', r2_10_L1, r2_10_proj)\nrep10('R2_L1_5d', 'R2_delta_L1', r2_10_L1, r2_10_delta)\nprint()\n\nprint('--- Per-task summary table (all 10 tasks) ---')\nhdr = f'{\"Task\":50s} R2_L1  R2_L8 R2_L13 R2_proj R2_vla dR2_L1'\nprint(hdr)\nfor i, t in enumerate(all_10):\n    s = t[:48]\n    print(f'{s:50s} {r2_10_L1[i]:.3f}  {r2_10_L8[i]:.3f}  {r2_10_L13[i]:.3f}  {r2_10_proj[i]:.3f}  {r2_10_vla[i]:.3f}  {r2_10_delta[i]:+.3f}')\n\n# ===== 3-task model-vs-GT MSE =====\nprint()\nprint('=' * 70)\nprint('3-TASK: Probe R2 vs Model-vs-GT Action MSE')\nprint('=' * 70)\n\ntasks_3_data = gt['per_task']  # this is a dict keyed by task name\ntasks_3 = list(tasks_3_data.keys())\nmse_3 = [tasks_3_data[t]['original']['mse']['mean'] for t in tasks_3]\ntasks_3_sp = [t.replace('_', ' ') for t in tasks_3]\nr2_3_L1 = [r2_dist['mlp_probe_5demo']['conditions']['baseline']['L1']['per_task_R2'][t] for t in tasks_3_sp]\nr2_3_proj = [unified['projector']['per_task_R2'][t] for t in tasks_3]\nr2_3_vla = [unified['vla_last_preaction_L19']['per_task_R2'][t] for t in tasks_3]\n\nprint()\nfor i in range(3):\n    print(f'  {tasks_3_sp[i]:50s} MSE={mse_3[i]:.4f}  R2_L1={r2_3_L1[i]:.4f}  R2_proj={r2_3_proj[i]:.4f}  R2_vla={r2_3_vla[i]:.4f}')\nprint()\nprint('  n=3: correlation stats unreliable, showing data only.')\n\n# ===== Summary =====\nprint()\nprint('=' * 70)\nprint('SUMMARY')\nprint('=' * 70)\n\n# Count significant correlations\nsigs = []\npairs_A = [\n    ('R2_L1_5d', r2_L1, 'paired_mse', paired_mse),\n    ('R2_L8_5d', r2_L8, 'paired_mse', paired_mse),\n    ('R2_L13_5d', r2_L13, 'paired_mse', paired_mse),\n    ('R2_proj', r2_proj, 'paired_mse', paired_mse),\n    ('R2_dino', r2_dino, 'paired_mse', paired_mse),\n    ('R2_vla', r2_vla, 'paired_mse', paired_mse),\n    ('R2_L1_5d', r2_L1, 'cohens_d', cohens_d),\n    ('R2_proj', r2_proj, 'cohens_d', cohens_d),\n    ('R2_vla', r2_vla, 'cohens_d', cohens_d),\n    ('dR2_L1', r2_delta_L1, 'paired_mse', paired_mse),\n    ('dR2_L8', r2_delta_L8, 'paired_mse', paired_mse),\n]\nfor nx, x, ny, y in pairs_A:\n    rho, p = spearmanr(x, y)\n    sigs.append((nx, ny, rho, p))\n\nn_sig = sum(1 for _, _, _, p in sigs if p < 0.05)\nprint(f'  {n_sig}/{len(sigs)} correlations significant at p<0.05 (n=5 tasks)')\nprint()\nfor nx, ny, rho, p in sigs:\n    flag = '<-- SIG' if p < 0.05 else ''\n    print(f'  {nx:20s} vs {ny:12s}: rho={rho:+.3f} (p={p:.3f}) {flag}')\n\nprint()\nprint('  Minimum detectable |rho| for significance at p<0.05 (two-tailed, n=5): ~0.900')\nprint('  Power is very limited with n=5. Need n>=10 for moderate correlations.')\nPYEOF\nsource /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 /tmp/rank_corr.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r2_mse_correlation_20260520T123229",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-19183",
    "command": "cat > /tmp/rank_corr.py << 'PYEOF'\nimport json, numpy as np\nfrom scipy.stats import spearmanr, kendalltau\n\n# ===== Load data =====\nwith open('/root/autodl-tmp/vla-ssd/results/action_trajectory_analysis.json') as f:\n    traj = json.load(f)\nwith open('/root/autodl-tmp/vla-ssd/results/per_task_r2_distribution.json') as f:\n    r2_dist = json.load(f)\nwith open('/root/autodl-tmp/vla-ssd/results/functional_validation/unified_action_probe.json') as f:\n    unified = json.load(f)\nwith open('/root/autodl-tmp/vla-ssd/results/l1_head_ablation/action_probe_50demos.json') as f:\n    ap50 = json.load(f)\nwith open('/root/autodl-tmp/vla-ssd/results/groundtruth_action_error.json') as f:\n    gt = json.load(f)\n\n# ===== Task name mappings =====\ntask_map = {\n    'open_the_middle_drawer_of_the_cabinet': 'open the middle drawer of the cabinet',\n    'open_the_top_drawer_and_put_the_bowl_inside': 'open the top drawer and put the bowl inside',\n    'push_the_plate_to_the_front_of_the_stove': 'push the plate to the front of the stove',\n    'put_the_bowl_on_the_plate': 'put the bowl on the plate',\n    'put_the_bowl_on_the_stove': 'put the bowl on the stove',\n}\n\ntasks_5 = list(task_map.keys())\ntasks_5_named = [task_map[t] for t in tasks_5]\n\n# ===== 5-task behavioral data =====\npaired_mse = [traj['per_task'][t]['paired_mse']['mean'] for t in tasks_5]\ncohens_d = [traj['per_task'][t]['paired_mse']['cohens_d'] for t in tasks_5]\ntoken_div = [traj['per_task'][t]['token_divergence_rate'] for t in tasks_5]\nkl_div = [traj['per_task'][t]['kl_divergence']['mean'] for t in tasks_5]\n\n# ===== Per-task R2 (representational metrics) =====\nr2_L1 = [r2_dist['mlp_probe_5demo']['conditions']['baseline']['L1']['per_task_R2'][t] for t in tasks_5_named]\nr2_L8 = [r2_dist['mlp_probe_5demo']['conditions']['baseline']['L8']['per_task_R2'][t] for t in tasks_5_named]\nr2_L13 = [r2_dist['mlp_probe_5demo']['conditions']['baseline']['L13']['per_task_R2'][t] for t in tasks_5_named]\nr2_proj = [unified['projector']['per_task_R2'][t] for t in tasks_5]\nr2_dino = [unified['dino_cls']['per_task_R2'][t] for t in tasks_5]\nr2_vla = [unified['vla_last_preaction_L19']['per_task_R2'][t] for t in tasks_5]\nr2_delta_L1 = [ap50['bootstrap_paired_CI']['baseline_vs_ablate_all24']['L1']['per_task_diffs'][t] for t in tasks_5_named]\nr2_delta_L8 = [ap50['bootstrap_paired_CI']['baseline_vs_ablate_all24']['L8']['per_task_diffs'][t] for t in tasks_5_named]\n\ndef report(name_x, name_y, x, y, show_data=True):\n    rho, p_rho = spearmanr(x, y)\n    tau, p_tau = kendalltau(x, y)\n    sig_s = '*' if p_rho < 0.05 else ''\n    sig_k = '*' if p_tau < 0.05 else ''\n    print(f'  {name_x} vs {name_y}:')\n    print(f'    Spearman rho={rho:+.4f} (p={p_rho:.4f}){sig_s}  |  Kendall tau={tau:+.4f} (p={p_tau:.4f}){sig_k}')\n    if show_data:\n        for i, t in enumerate(tasks_5):\n            short = t.replace('_', ' ')[:40]\n            print(f'      {short:40s}  x={x[i]:.4f}  y={y[i]:.4f}')\n    print()\n\nprint('=' * 70)\nprint('RANK CORRELATION: Probe R2 vs Behavioral Outcomes (n=5 tasks)')\nprint('=' * 70)\nprint()\n\nprint('--- (A) Baseline Probe R2 vs Paired MSE (ablation action shift) ---')\nreport('R2_baseline_L1_5demo', 'paired_mse', r2_L1, paired_mse)\nreport('R2_baseline_L8_5demo', 'paired_mse', r2_L8, paired_mse)\nreport('R2_baseline_L13_5demo', 'paired_mse', r2_L13, paired_mse)\nreport('R2_projector_50demo', 'paired_mse', r2_proj, paired_mse)\nreport('R2_dino_50demo', 'paired_mse', r2_dino, paired_mse)\nreport('R2_vla_last_L19_50demo', 'paired_mse', r2_vla, paired_mse)\n\nprint('--- (B) Baseline Probe R2 vs Cohen d (ablation effect size) ---')\nreport('R2_baseline_L1_5demo', 'cohens_d', r2_L1, cohens_d)\nreport('R2_projector_50demo', 'cohens_d', r2_proj, cohens_d)\nreport('R2_vla_last_L19_50demo', 'cohens_d', r2_vla, cohens_d)\n\nprint('--- (C) R2 Delta (abl. rep. impact) vs Paired MSE (abl. beh. impact) ---')\nreport('R2_delta_L1', 'paired_mse', r2_delta_L1, paired_mse)\nreport('R2_delta_L8', 'paired_mse', r2_delta_L8, paired_mse)\n\nprint('--- (D) Baseline Probe R2 vs Token Divergence Rate ---')\nreport('R2_baseline_L1_5demo', 'token_div_rate', r2_L1, token_div)\nreport('R2_vla_last_L19_50demo', 'token_div_rate', r2_vla, token_div)\n\nprint('--- (E) Baseline Probe R2 vs KL Divergence ---')\nreport('R2_baseline_L1_5demo', 'kl_divergence', r2_L1, kl_div)\n\n# ===== 10-task analysis =====\nprint('=' * 70)\nprint('FULL 10-TASK ANALYSIS (cross-representational consistency)')\nprint('=' * 70)\nall_10 = r2_dist['tasks']\nr2_10_L1 = [r2_dist['mlp_probe_5demo']['conditions']['baseline']['L1']['per_task_R2'][t] for t in all_10]\nr2_10_L8 = [r2_dist['mlp_probe_5demo']['conditions']['baseline']['L8']['per_task_R2'][t] for t in all_10]\nr2_10_L13 = [r2_dist['mlp_probe_5demo']['conditions']['baseline']['L13']['per_task_R2'][t] for t in all_10]\nt10_under = [t.replace(' ', '_') for t in all_10]\nr2_10_proj = [unified['projector']['per_task_R2'][t] for t in t10_under]\nr2_10_vla = [unified['vla_last_preaction_L19']['per_task_R2'][t] for t in t10_under]\nr2_10_delta = [ap50['bootstrap_paired_CI']['baseline_vs_ablate_all24']['L1']['per_task_diffs'][t] for t in all_10]\n\ndef rep10(nx, ny, x, y):\n    rho, p = spearmanr(x, y)\n    tau, pt = kendalltau(x, y)\n    s = '*' if p < 0.05 else ''\n    print(f'  {nx} vs {ny}: rho={rho:+.4f} (p={p:.4f}){s}, tau={tau:+.4f} (p={pt:.4f})')\n\nprint()\nprint('--- Cross-layer/cross-source R2 consistency ---')\nrep10('R2_L1_5d', 'R2_L8_5d', r2_10_L1, r2_10_L8)\nrep10('R2_L1_5d', 'R2_L13_5d', r2_10_L1, r2_10_L13)\nrep10('R2_L8_5d', 'R2_L13_5d', r2_10_L8, r2_10_L13)\nrep10('R2_proj_50d', 'R2_vla_L19_50d', r2_10_proj, r2_10_vla)\nrep10('R2_L1_5d', 'R2_proj_50d', r2_10_L1, r2_10_proj)\nrep10('R2_L1_5d', 'R2_delta_L1', r2_10_L1, r2_10_delta)\nprint()\n\nprint('--- Per-task summary table (all 10 tasks) ---')\nhdr = f'{\"Task\":50s} R2_L1  R2_L8 R2_L13 R2_proj R2_vla dR2_L1'\nprint(hdr)\nfor i, t in enumerate(all_10):\n    s = t[:48]\n    print(f'{s:50s} {r2_10_L1[i]:.3f}  {r2_10_L8[i]:.3f}  {r2_10_L13[i]:.3f}  {r2_10_proj[i]:.3f}  {r2_10_vla[i]:.3f}  {r2_10_delta[i]:+.3f}')\n\n# ===== 3-task model-vs-GT MSE =====\nprint()\nprint('=' * 70)\nprint('3-TASK: Probe R2 vs Model-vs-GT Action MSE')\nprint('=' * 70)\n\ntasks_3_data = gt['per_task']  # this is a dict keyed by task name\ntasks_3 = list(tasks_3_data.keys())\nmse_3 = [tasks_3_data[t]['original']['mse']['mean'] for t in tasks_3]\ntasks_3_sp = [t.replace('_', ' ') for t in tasks_3]\nr2_3_L1 = [r2_dist['mlp_probe_5demo']['conditions']['baseline']['L1']['per_task_R2'][t] for t in tasks_3_sp]\nr2_3_proj = [unified['projector']['per_task_R2'][t] for t in tasks_3]\nr2_3_vla = [unified['vla_last_preaction_L19']['per_task_R2'][t] for t in tasks_3]\n\nprint()\nfor i in range(3):\n    print(f'  {tasks_3_sp[i]:50s} MSE={mse_3[i]:.4f}  R2_L1={r2_3_L1[i]:.4f}  R2_proj={r2_3_proj[i]:.4f}  R2_vla={r2_3_vla[i]:.4f}')\nprint()\nprint('  n=3: correlation stats unreliable, showing data only.')\n\n# ===== Summary =====\nprint()\nprint('=' * 70)\nprint('SUMMARY')\nprint('=' * 70)\n\n# Count significant correlations\nsigs = []\npairs_A = [\n    ('R2_L1_5d', r2_L1, 'paired_mse', paired_mse),\n    ('R2_L8_5d', r2_L8, 'paired_mse', paired_mse),\n    ('R2_L13_5d', r2_L13, 'paired_mse', paired_mse),\n    ('R2_proj', r2_proj, 'paired_mse', paired_mse),\n    ('R2_dino', r2_dino, 'paired_mse', paired_mse),\n    ('R2_vla', r2_vla, 'paired_mse', paired_mse),\n    ('R2_L1_5d', r2_L1, 'cohens_d', cohens_d),\n    ('R2_proj', r2_proj, 'cohens_d', cohens_d),\n    ('R2_vla', r2_vla, 'cohens_d', cohens_d),\n    ('dR2_L1', r2_delta_L1, 'paired_mse', paired_mse),\n    ('dR2_L8', r2_delta_L8, 'paired_mse', paired_mse),\n]\nfor nx, x, ny, y in pairs_A:\n    rho, p = spearmanr(x, y)\n    sigs.append((nx, ny, rho, p))\n\nn_sig = sum(1 for _, _, _, p in sigs if p < 0.05)\nprint(f'  {n_sig}/{len(sigs)} correlations significant at p<0.05 (n=5 tasks)')\nprint()\nfor nx, ny, rho, p in sigs:\n    flag = '<-- SIG' if p < 0.05 else ''\n    print(f'  {nx:20s} vs {ny:12s}: rho={rho:+.3f} (p={p:.3f}) {flag}')\n\nprint()\nprint('  Minimum detectable |rho| for significance at p<0.05 (two-tailed, n=5): ~0.900')\nprint('  Power is very limited with n=5. Need n>=10 for moderate correlations.')\nPYEOF\nsource /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 /tmp/rank_corr.py"
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-20T12:38:38.695328+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"======================================================================\\nRANK CORRELATION: Probe R2 vs Behavioral Outcomes (n=5 tasks)\\n======================================================================\\n\\n--- (A) Baseline Probe R2 vs Paired MSE (ablation action shift) ---\\n  R2_baseline_L1_5demo vs paired_mse:\\n    Spearman rho=-0.1000 (p=0.8729)  |  Kendall tau=+0.0000 (p=1.0000)\\n      open the middle drawer of the cabinet     x=0.1971  y=0.0224\\n      open the top drawer and put the bowl ins  x=0.2649  y=0.0446\\n      push the plate to the front of the stove  x=0.1901  y=0.0468\\n      put the bowl on the plate                 x=0.3754  y=0.0459\\n      put the bowl on the stove                 x=0.2352  y=0.0485\\n\\n  R2_baseline_L8_5demo vs paired_mse:\\n    Spearman rho=-0.5000 (p=0.3910)  |  Kendall tau=-0.4000 (p=0.4833)\\n      open the middle drawer of the cabinet     x=0.4532  y=0.0224\\n      open the top drawer and put the bowl ins  x=0.3757  y=0.0446\\n      push the plate to the front of the stove  x=0.3358  y=0.0468\\n      put the bowl on the plate                 x=0.4371  y=0.0459\\n      put the bowl on the stove                 x=0.3960  y=0.0485\\n\\n  R2_baseline_L13_5demo vs paired_mse:\\n    Spearman rho=-0.6000 (p=0.2848)  |  Kendall tau=-0.4000 (p=0.4833)\\n      open the middle drawer of the cabinet     x=0.5686  y=0.0224\\n      open the top drawer and put the bowl ins  x=0.5466  y=0.0446\\n      push the plate to the front of the stove  x=0.4092  y=0.0468\\n      put the bowl on the plate                 x=0.3887  y=0.0459\\n      put the bowl on the stove                 x=0.5352  y=0.0485\\n\\n  R2_projector_50demo vs paired_mse:\\n    Spearman rho=+0.3000 (p=0.6238)  |  Kendall tau=+0.2000 (p=0.8167)\\n      open the middle drawer of the cabinet     x=0.4973  y=0.0224\\n      open the top drawer and put the bowl ins  x=0.7499  y=0.0446\\n      push the plate to the
…[truncated 6477 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r2_mse_correlation_20260520T123229",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-20T12:38:38.695522+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "python3 -c \"import json; d=json.load(open('/root/autodl-tmp/vla-ssd/results/action_trajectory_L8_ablation.json')); print('L8 tasks:', list(d.get('per_task',{}).keys())); print('keys:', list(d.keys())[:10])\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r2_mse_correlation_20260520T123229",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "python3 -c \"import json; d=json.load(open('/root/autodl-tmp/vla-ssd/results/action_trajectory_L8_ablation.json')); print('L8 tasks:', list(d.get('per_task',{}).keys())); print('keys:', list(d.keys())[:10])\""
  }
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-20T12:38:38.695658+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r2_mse_correlation_20260520T123229",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-20T12:38:38.695783+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "python3 -c \"import json; d=json.load(open('/root/autodl-tmp/vla-ssd/results/counterfactual_combined.json')); print('keys:', list(d.keys())[:15]); print('conditions:', [k for k in d.keys() if 'condition' in k.lower() or 'per_task' in k.lower()])\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r2_mse_correlation_20260520T123229",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "python3 -c \"import json; d=json.load(open('/root/autodl-tmp/vla-ssd/results/counterfactual_combined.json')); print('keys:', list(d.keys())[:15]); print('conditions:', [k for k in d.keys() if 'condition' in k.lower() or 'per_task' in k.lower()])\""
  }
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-20T12:38:38.695907+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r2_mse_correlation_20260520T123229",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-20T12:38:38.696049+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "python3 -c \"import json; d=json.load(open('/root/autodl-tmp/vla-ssd/results/action_trajectory_L8_ablation.json')); print(list(d.get('per_task',{}).keys()))\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r2_mse_correlation_20260520T123229",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "python3 -c \"import json; d=json.load(open('/root/autodl-tmp/vla-ssd/results/action_trajectory_L8_ablation.json')); print(list(d.get('per_task',{}).keys()))\""
  }
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-20T12:38:38.696171+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r2_mse_correlation_20260520T123229",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-20T12:38:38.696288+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "python3 -c \"import json; d=json.load(open('/root/autodl-tmp/vla-ssd/results/counterfactual_combined.json')); print(list(d.keys())[:20])\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r2_mse_correlation_20260520T123229",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "python3 -c \"import json; d=json.load(open('/root/autodl-tmp/vla-ssd/results/counterfactual_combined.json')); print(list(d.keys())[:20])\""
  }
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-20T12:38:38.696406+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r2_mse_correlation_20260520T123229",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 71 · 2026-05-20T12:38:38.696543+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-19183",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c \"\nimport json\nd=json.load(open('/root/autodl-tmp/vla-ssd/results/action_trajectory_L8_ablation.json'))\nprint('L8 keys:', list(d.keys())[:10])\nprint('L8 per_task:', list(d.get('per_task',{}).keys()))\nd2=json.load(open('/root/autodl-tmp/vla-ssd/results/action_trajectory_L13_ablation.json'))\nprint('L13 per_task:', list(d2.get('per_task',{}).keys()))\nd3=json.load(open('/root/autodl-tmp/vla-ssd/results/counterfactual_combined.json'))\nprint('CF combined keys:', list(d3.keys())[:20])\n\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r2_mse_correlation_20260520T123229",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-19183",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c \"\nimport json\nd=json.load(open('/root/autodl-tmp/vla-ssd/results/action_trajectory_L8_ablation.json'))\nprint('L8 keys:', list(d.keys())[:10])\nprint('L8 per_task:', list(d.get('per_task',{}).keys()))\nd2=json.load(open('/root/autodl-tmp/vla-ssd/results/action_trajectory_L13_ablation.json'))\nprint('L13 per_task:', list(d2.get('per_task',{}).keys()))\nd3=json.load(open('/root/autodl-tmp/vla-ssd/results/counterfactual_combined.json'))\nprint('CF combined keys:', list(d3.keys())[:20])\n\"\n"
  }
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-20T12:38:38.696674+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"L8 keys: ['config', 'main_metrics', 'secondary_metrics', 'per_task']\\nL8 per_task: ['open_the_middle_drawer_of_the_cabinet', 'open_the_top_drawer_and_put_the_bowl_inside', 'push_the_plate_to_the_front_of_the_stove', 'put_the_bowl_on_the_plate', 'put_the_bowl_on_the_stove']\\nL13 per_task: ['open_the_middle_drawer_of_the_cabinet', 'open_the_top_drawer_and_put_the_bowl_inside', 'push_the_plate_to_the_front_of_the_stove', 'put_the_bowl_on_the_plate', 'put_the_bowl_on_the_stove']\\nCF combined keys: ['config', 'conditions', 'ranking_by_cohens_d']\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.53}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r2_mse_correlation_20260520T123229",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 73 · 2026-05-20T12:38:38.696853+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-19183",
  "command": "cat > /tmp/save_corr_results.py << 'PYEOF'\nimport json, numpy as np\nfrom scipy.stats import spearmanr, kendalltau\n\nwith open('/root/autodl-tmp/vla-ssd/results/action_trajectory_analysis.json') as f:\n    traj = json.load(f)\nwith open('/root/autodl-tmp/vla-ssd/results/per_task_r2_distribution.json') as f:\n    r2_dist = json.load(f)\nwith open('/root/autodl-tmp/vla-ssd/results/functional_validation/unified_action_probe.json') as f:\n    unified = json.load(f)\nwith open('/root/autodl-tmp/vla-ssd/results/l1_head_ablation/action_probe_50demos.json') as f:\n    ap50 = json.load(f)\n\ntask_map = {\n    'open_the_middle_drawer_of_the_cabinet': 'open the middle drawer of the cabinet',\n    'open_the_top_drawer_and_put_the_bowl_inside': 'open the top drawer and put the bowl inside',\n    'push_the_plate_to_the_front_of_the_stove': 'push the plate to the front of the stove',\n    'put_the_bowl_on_the_plate': 'put the bowl on the plate',\n    'put_the_bowl_on_the_stove': 'put the bowl on the stove',\n}\n\ntasks_5 = list(task_map.keys())\ntasks_5_named = [task_map[t] for t in tasks_5]\n\npaired_mse = [traj['per_task'][t]['paired_mse']['mean'] for t in tasks_5]\ncohens_d = [traj['per_task'][t]['paired_mse']['cohens_d'] for t in tasks_5]\ntoken_div = [traj['per_task'][t]['token_divergence_rate'] for t in tasks_5]\n\nr2_L1 = [r2_dist['mlp_probe_5demo']['conditions']['baseline']['L1']['per_task_R2'][t] for t in tasks_5_named]\nr2_L8 = [r2_dist['mlp_probe_5demo']['conditions']['baseline']['L8']['per_task_R2'][t] for t in tasks_5_named]\nr2_L13 = [r2_dist['mlp_probe_5demo']['conditions']['baseline']['L13']['per_task_R2'][t] for t in tasks_5_named]\nr2_proj = [unified['projector']['per_task_R2'][t] for t in tasks_5]\nr2_dino = [unified['dino_cls']['per_task_R2'][t] for t in tasks_5]\nr2_vla = [unified['vla_last_preaction_L19']['per_task_R2'][t] for t in tasks_5]\nr2_delta_L1 = [ap50['bootstrap_paired_CI']['baseline_vs_ablate_all24']['L1']['per_task_diffs'][t] for t in tasks_5_named]\n\n# Build results\ndef corr(x, y):\n    rho, p_rho = spearmanr(x, y)\n    tau, p_tau = kendalltau(x, y)\n    return {'spearman_rho': round(rho, 4), 'spearman_p': round(p_rho, 4),\n            'kendall_tau': round(tau, 4), 'kendall_p': round(p_tau, 4)}\n\nresults = {\n    'analysis': 'Probe R2 vs Per-Task Behavioral Outcomes Rank Correlation',\n    'n_tasks_behavioral': 5,\n    'n_tasks_representational': 10,\n    'limitation': 'Only 5 tasks have both R2 and behavioral (paired_mse) data. With n=5, minimum |rho| for p<0.05 is ~0.9.',\n    'per_task_data': {},\n    'correlations': {},\n    'cross_representational_10task': {},\n}\n\nfor i, t in enumerate(tasks_5):\n    results['per_task_data'][t] = {\n        'paired_mse': round(paired_mse[i], 6),\n        'cohens_d': round(cohens_d[i], 4),\n        'token_divergence_rate': round(token_div[i], 4),\n        'R2_baseline_L1_5demo': round(r2_L1[i], 4),\n        'R2_baseline_L8_5demo': round(r2_L8[i], 4),\n        'R2_baseline_L13_5demo': round(r2_L13[i], 4),\n        'R2_projector_50demo': round(r2_proj[i], 4),\n        'R2_dino_50demo': round(r2_dino[i], 4),\n        'R2_vla_last_L19_50demo': round(r2_vla[i], 4),\n        'R2_delta_L1_ablation': round(r2_delta_L1[i], 4),\n    }\n\npairs = [\n    ('R2_L1_5d', r2_L1, 'paired_mse', paired_mse),\n    ('R2_L8_5d', r2_L8, 'paired_mse', paired_mse),\n    ('R2_L13_5d', r2_L13, 'paired_mse', paired_mse),\n    ('R2_proj_50d', r2_proj, 'paired_mse', paired_mse),\n    ('R2_dino_50d', r2_dino, 'paired_mse', paired_mse),\n    ('R2_vla_50d', r2_vla, 'paired_mse', paired_mse),\n    ('R2_L1_5d', r2_L1, 'cohens_d', cohens_d),\n    ('R2_proj_50d', r2_proj, 'cohens_d', cohens_d),\n    ('R2_delta_L1', r2_delta_L1, 'paired_mse', paired_mse),\n]\n\nfor nx, x, ny, y in pairs:\n    results['correlations'][f'{nx}_vs_{ny}'] = corr(x, y)\n\n# 10-task cross-representational\nall_10 = r2_dist['tasks']\nr2_10_L1 = [r2_dist['mlp_probe_5demo']['conditions']['baseline']['L1']['per_task_R2'][t] for t in all_10]\nt10_u = [t.replace(' ', '_') for t in all_10]\nr2_10_proj = [unified['projector']['per_task_R2'][t] for t in t10_u]\nr2_10_vla = [unified['vla_last_preaction_L19']['per_task_R2'][t] for t in t10_u]\n\nresults['cross_representational_10task'] = {\n    'R2_proj_vs_R2_vla': corr(r2_10_proj, r2_10_vla),\n    'note': 'Only cross-representational (not rep-vs-behavioral) can use all 10 tasks'\n}\n\nresults['conclusion'] = {\n    'significant_correlations': '0/9 at p<0.05',\n    'fundamental_issue': 'n=5 tasks gives almost no statistical power (need |rho|>0.9 for significance)',\n    'point_estimates': 'rho ranges from -0.6 to +0.6 depending on R2 metric, no consistent pattern',\n    'cross_rep_consistency': 'R2_projector vs R2_vla_last_L19: rho=0.83 (p=0.003) across 10 tasks — different probes agree on task difficulty ranking',\n    'recommendation': 'Cannot claim \"representational metrics predict behavioral outcomes\" with current data. Need per-task behavioral data for all 10 tasks, or use a benchmark suite with more tasks (e.g., LIBERO-Long has 10 additional tasks).'\n}\n\nout_path = '/root/autodl-tmp/vla-ssd/results/probe_r2_vs_behavioral_rank_correlation.json'\nwith open(out_path, 'w') as f:\n    json.dump(results, f, indent=2)\nprint(f'Saved to {out_path}')\nPYEOF\nsource /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 /tmp/save_corr_results.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r2_mse_correlation_20260520T123229",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-19183",
    "command": "cat > /tmp/save_corr_results.py << 'PYEOF'\nimport json, numpy as np\nfrom scipy.stats import spearmanr, kendalltau\n\nwith open('/root/autodl-tmp/vla-ssd/results/action_trajectory_analysis.json') as f:\n    traj = json.load(f)\nwith open('/root/autodl-tmp/vla-ssd/results/per_task_r2_distribution.json') as f:\n    r2_dist = json.load(f)\nwith open('/root/autodl-tmp/vla-ssd/results/functional_validation/unified_action_probe.json') as f:\n    unified = json.load(f)\nwith open('/root/autodl-tmp/vla-ssd/results/l1_head_ablation/action_probe_50demos.json') as f:\n    ap50 = json.load(f)\n\ntask_map = {\n    'open_the_middle_drawer_of_the_cabinet': 'open the middle drawer of the cabinet',\n    'open_the_top_drawer_and_put_the_bowl_inside': 'open the top drawer and put the bowl inside',\n    'push_the_plate_to_the_front_of_the_stove': 'push the plate to the front of the stove',\n    'put_the_bowl_on_the_plate': 'put the bowl on the plate',\n    'put_the_bowl_on_the_stove': 'put the bowl on the stove',\n}\n\ntasks_5 = list(task_map.keys())\ntasks_5_named = [task_map[t] for t in tasks_5]\n\npaired_mse = [traj['per_task'][t]['paired_mse']['mean'] for t in tasks_5]\ncohens_d = [traj['per_task'][t]['paired_mse']['cohens_d'] for t in tasks_5]\ntoken_div = [traj['per_task'][t]['token_divergence_rate'] for t in tasks_5]\n\nr2_L1 = [r2_dist['mlp_probe_5demo']['conditions']['baseline']['L1']['per_task_R2'][t] for t in tasks_5_named]\nr2_L8 = [r2_dist['mlp_probe_5demo']['conditions']['baseline']['L8']['per_task_R2'][t] for t in tasks_5_named]\nr2_L13 = [r2_dist['mlp_probe_5demo']['conditions']['baseline']['L13']['per_task_R2'][t] for t in tasks_5_named]\nr2_proj = [unified['projector']['per_task_R2'][t] for t in tasks_5]\nr2_dino = [unified['dino_cls']['per_task_R2'][t] for t in tasks_5]\nr2_vla = [unified['vla_last_preaction_L19']['per_task_R2'][t] for t in tasks_5]\nr2_delta_L1 = [ap50['bootstrap_paired_CI']['baseline_vs_ablate_all24']['L1']['per_task_diffs'][t] for t in tasks_5_named]\n\n# Build results\ndef corr(x, y):\n    rho, p_rho = spearmanr(x, y)\n    tau, p_tau = kendalltau(x, y)\n    return {'spearman_rho': round(rho, 4), 'spearman_p': round(p_rho, 4),\n            'kendall_tau': round(tau, 4), 'kendall_p': round(p_tau, 4)}\n\nresults = {\n    'analysis': 'Probe R2 vs Per-Task Behavioral Outcomes Rank Correlation',\n    'n_tasks_behavioral': 5,\n    'n_tasks_representational': 10,\n    'limitation': 'Only 5 tasks have both R2 and behavioral (paired_mse) data. With n=5, minimum |rho| for p<0.05 is ~0.9.',\n    'per_task_data': {},\n    'correlations': {},\n    'cross_representational_10task': {},\n}\n\nfor i, t in enumerate(tasks_5):\n    results['per_task_data'][t] = {\n        'paired_mse': round(paired_mse[i], 6),\n        'cohens_d': round(cohens_d[i], 4),\n        'token_divergence_rate': round(token_div[i], 4),\n        'R2_baseline_L1_5demo': round(r2_L1[i], 4),\n        'R2_baseline_L8_5demo': round(r2_L8[i], 4),\n        'R2_baseline_L13_5demo': round(r2_L13[i], 4),\n        'R2_projector_50demo': round(r2_proj[i], 4),\n        'R2_dino_50demo': round(r2_dino[i], 4),\n        'R2_vla_last_L19_50demo': round(r2_vla[i], 4),\n        'R2_delta_L1_ablation': round(r2_delta_L1[i], 4),\n    }\n\npairs = [\n    ('R2_L1_5d', r2_L1, 'paired_mse', paired_mse),\n    ('R2_L8_5d', r2_L8, 'paired_mse', paired_mse),\n    ('R2_L13_5d', r2_L13, 'paired_mse', paired_mse),\n    ('R2_proj_50d', r2_proj, 'paired_mse', paired_mse),\n    ('R2_dino_50d', r2_dino, 'paired_mse', paired_mse),\n    ('R2_vla_50d', r2_vla, 'paired_mse', paired_mse),\n    ('R2_L1_5d', r2_L1, 'cohens_d', cohens_d),\n    ('R2_proj_50d', r2_proj, 'cohens_d', cohens_d),\n    ('R2_delta_L1', r2_delta_L1, 'paired_mse', paired_mse),\n]\n\nfor nx, x, ny, y in pairs:\n    results['correlations'][f'{nx}_vs_{ny}'] = corr(x, y)\n\n# 10-task cross-representational\nall_10 = r2_dist['tasks']\nr2_10_L1 = [r2_dist['mlp_probe_5demo']['conditions']['baseline']['L1']['per_task_R2'][t] for t in all_10]\nt10_u = [t.replace(' ', '_') for t in all_10]\nr2_10_proj = [unified['projector']['per_task_R2'][t] for t in t10_u]\nr2_10_vla = [unified['vla_last_preaction_L19']['per_task_R2'][t] for t in t10_u]\n\nresults['cross_representational_10task'] = {\n    'R2_proj_vs_R2_vla': corr(r2_10_proj, r2_10_vla),\n    'note': 'Only cross-representational (not rep-vs-behavioral) can use all 10 tasks'\n}\n\nresults['conclusion'] = {\n    'significant_correlations': '0/9 at p<0.05',\n    'fundamental_issue': 'n=5 tasks gives almost no statistical power (need |rho|>0.9 for significance)',\n    'point_estimates': 'rho ranges from -0.6 to +0.6 depending on R2 metric, no consistent pattern',\n    'cross_rep_consistency': 'R2_projector vs R2_vla_last_L19: rho=0.83 (p=0.003) across 10 tasks — different probes agree on task difficulty ranking',\n    'recommendation': 'Cannot claim \"representational metrics predict behavioral outcomes\" with current data. Need per-task behavioral data for all 10 tasks, or use a benchmark suite with more tasks (e.g., LIBERO-Long has 10 additional tasks).'\n}\n\nout_path = '/root/autodl-tmp/vla-ssd/results/probe_r2_vs_behavioral_rank_correlation.json'\nwith open(out_path, 'w') as f:\n    json.dump(results, f, indent=2)\nprint(f'Saved to {out_path}')\nPYEOF\nsource /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 /tmp/save_corr_results.py"
  }
}
```

</details>

---

### Tool result

_source line 74 · 2026-05-20T12:38:38.697066+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Saved to /root/autodl-tmp/vla-ssd/results/probe_r2_vs_behavioral_rank_correlation.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.16}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r2_mse_correlation_20260520T123229",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 75 · 2026-05-20T12:38:38.697217+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/vla-ssd/artifacts/*r2*"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r2_mse_correlation_20260520T123229",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/vla-ssd/artifacts/*r2*"
  }
}
```

</details>

---

### Tool result

_source line 76 · 2026-05-20T12:38:38.697342+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r2_mse_correlation_20260520T123229",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 77 · 2026-05-20T12:38:38.697520+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/*"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r2_mse_correlation_20260520T123229",
  "tool": "Glob",
  "tool_args": {
    "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/*"
  }
}
```

</details>

---

### Tool result

_source line 78 · 2026-05-20T12:38:38.697691+00:00_

artifacts/probe_design_plan.md
artifacts/_project/intermediate/probe_dryrun_dinov2_results.txt
artifacts/dinov2_baseline/data/dinov2_subtask_auc_results.txt
artifacts/mvp_probe_trained/report/mvp_probe_analysis.md
artifacts/_project/report/action_probe_design.md
artifacts/action_probe_design.md
artifacts/_project/report/literature_map_probing.md
artifacts/literature_map_probing.md
artifacts/_project/report/controlb_report.md
artifacts/_project/report/controlb_analysis.md
artifacts/mvp_controlb_trained/report/controlb_analysis.md
artifacts/controlb_analysis/controlb_analysis.md
artifacts/_project/report/libero_goal_feasibility.md
artifacts/libero_goal_feasibility.md
artifacts/_project/report/layer_stability_analysis.md
artifacts/layer_stability_analysis.md
artifacts/openvla_libero_goal_compat.md
artifacts/pipeline_audit_libero_goal.md
artifacts/patch_probes.py
artifacts/_project/report/literature_survey_instruction_probing.md
artifacts/literature_survey_instruction_probing.md
artifacts/literature_map.yaml
artifacts/pca_linear_probe_perlayer.py
artifacts/pca_linear_probe_gc.py
artifacts/rsa_analysis.py
artifacts/_project/chart/perlayer_rsa_comparison_chart_info.txt
artifacts/dream_reports/dream_20260515T222933/logs/phase1_attempt0.log
artifacts/_project/data/perlayer_rsa_summary.txt
artifacts/dream_reports/dream_20260515T222933/logs/phase2_best_attempt0.log
artifacts/dream_reports/dream_20260515T222933/logs/phase2_median_attempt0.log
artifacts/_project/intermediate/figure_data_manifest.txt
artifacts/dream_reports/dream_20260515T222933/logs/phase2_worst_attempt0.log
artifacts/dream_reports/dream_20260515T222933/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260515T222933/best/experiment_data.json
artifacts/dream_reports/dream_20260515T222933/best/paper_framing.md
artifacts/dream_reports/dream_20260515T222933/best/paper.tex
artifacts/dream_reports/dream_20260515T222933/best/paper.aux
artifacts/dream_reports/dream_20260515T222933/best/paper.out
artifacts/
…[truncated 4113 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r2_mse_correlation_20260520T123229",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 79 · 2026-05-20T12:38:38.697902+00:00_

## 汇报

### 数据盘点

| 数据类型 | 来源文件 | Task 覆盖 |
|---------|---------|----------|
| **Per-task R² (probe)** | `per_task_r2_distribution.json`, `unified_action_probe.json`, `action_probe_50demos.json` | **10 tasks** (LIBERO-Goal 全部) |
| **Per-task paired MSE (ablation行为偏移)** | `action_trajectory_analysis.json` | **5 tasks** |
| **Per-task model-vs-GT MSE** | `groundtruth_action_error.json` | **3 tasks** |
| **Per-task success rate** | `sr_corrected_3ep.json` | **1 task** |

**核心限制：behavioral outcome 数据最多只有 5 个 task。**

### Correlation 结果 (n=5 tasks)

**0/11 correlations 在 p<0.05 显著。**

| Representational Metric | Behavioral Metric | Spearman ρ | p-value |
|------------------------|-------------------|-----------|---------|
| R²_L1 (5-demo) | paired_mse | -0.10 | 0.873 |
| R²_L8 (5-demo) | paired_mse | -0.50 | 0.391 |
| R²_L13 (5-demo) | paired_mse | -0.60 | 0.285 |
| R²_projector (50-demo) | paired_mse | +0.30 | 0.624 |
| R²_dino (50-demo) | paired_mse | +0.60 | 0.285 |
| R²_vla_last_L19 (50-demo) | paired_mse | +0.40 | 0.505 |
| R²_L1 (5-demo) | Cohen's d | -0.10 | 0.873 |
| R²_projector | Cohen's d | +0.30 | 0.624 |
| R²_vla_last_L19 | Cohen's d | +0.40 | 0.505 |
| ΔR²_L1 (ablation) | paired_mse | +0.20 | 0.747 |
| ΔR²_L8 (ablation) | paired_mse | -0.60 | 0.285 |

### 10-task 交叉验证（representational only）

唯一显著结果：**R²_projector vs R²_vla_last_L19: ρ=+0.83, p=0.003** — 不同 probe readout 对 task 难度排序高度一致。

### 3-task model-vs-GT MSE（仅展示数据）

| Task | Model MSE | R²_L1 | R²_proj | R²_vla |
|------|-----------|-------|---------|--------|
| open middle drawer | 0.562 | 0.197 | 0.497 | 0.601 |
| top drawer + bowl | 0.548 | 0.265 | 0.750 | 0.752 |
| push plate | 0.383 | 0.190 | 0.586 | 0.710 |

MSE 最低的 push_plate 有中等 R² — 方向符合预期（低 MSE ↔ 高 R²），但 n=3 无法统计检验。

### 结论

**不能支持 "representational metrics predict behavioral outcomes" 的 claim。**

- n=5 tasks 时，Spearman 检验需要 |ρ|≥0.9 才能达到 p<0.05，统计功效极低
- 点估计在 -0.6 到 +0.6 之间摇摆，取决于选哪层/哪种 probe，无一致模式
- 跨 representation 的一致性（ρ=0.83）表明 probe 本身可靠，但缺少足够的 behavioral 数据来做闭环

### 要使这个分析可行

需要 **per-task behavioral data 覆盖全部 10 个 task**。两个方案：
1. **在全部 10 个 LIBERO-Goal task 上跑 `action_trajectory_analysis`**（当前只跑了 5 个）
2. **扩展到 LIBERO-Long**（再加 10 个 task，提高 n 到 20）

结果已保存至 `/root/autodl-tmp/vla-ssd/results/probe_r2_vs_behavioral_rank_correlation.json`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_r2_mse_correlation_20260520T123229"
}
```

</details>

---
