# ops extract vanilla seed123 metrics

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 7
- **Recorded user turns:** 0
- **Tool calls:** 3
- **Original source:** `logs/chats/worker_ops_extract-vanilla-seed123-metrics_20260514T204319.jsonl`
- **Structured JSON:** [`767615edf8c28d2922eb.json`](../../sessions/76/767615edf8c28d2922eb.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

7 recorded events

### Tool call

_source line 1 · 2026-05-14T20:43:55.734041+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__update_registry",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_extract-vanilla-seed123-metrics_20260514T204319",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__update_registry",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-14T20:43:55.734314+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_extract-vanilla-seed123-metrics_20260514T204319",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-14T20:43:55.734467+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/tax_error_inject_agent/eval_results/v4_vanilla_seed123_eval.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_extract-vanilla-seed123-metrics_20260514T204319",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat /root/autodl-tmp/tax_error_inject_agent/eval_results/v4_vanilla_seed123_eval.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-14T20:43:55.734859+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"model\\\": \\\"checkpoints/mini_vanilla_sft_v4_seed123/v1-20260515-022602/checkpoint-1635\\\",\\n  \\\"eval_split\\\": \\\"valid_unseen\\\",\\n  \\\"inject\\\": false,\\n  \\\"inject_mode\\\": \\\"none\\\",\\n  \\\"total_episodes\\\": 47,\\n  \\\"success_rate\\\": 0.66,\\n  \\\"timestamp\\\": \\\"2026-05-14T19:39:11.185689+00:00\\\",\\n  \\\"by_task_type\\\": {\\n    \\\"look_at_obj_in_light\\\": {\\n      \\\"total\\\": 6,\\n      \\\"success\\\": 5,\\n      \\\"rate\\\": 0.833\\n    },\\n    \\\"pick_and_place_simple\\\": {\\n      \\\"total\\\": 8,\\n      \\\"success\\\": 6,\\n      \\\"rate\\\": 0.75\\n    },\\n    \\\"pick_clean_then_place_in_recep\\\": {\\n      \\\"total\\\": 11,\\n      \\\"success\\\": 5,\\n      \\\"rate\\\": 0.455\\n    },\\n    \\\"pick_cool_then_place_in_recep\\\": {\\n      \\\"total\\\": 7,\\n      \\\"success\\\": 4,\\n      \\\"rate\\\": 0.571\\n    },\\n    \\\"pick_heat_then_place_in_recep\\\": {\\n      \\\"total\\\": 8,\\n      \\\"success\\\": 7,\\n      \\\"rate\\\": 0.875\\n    },\\n    \\\"pick_two_obj_and_place\\\": {\\n      \\\"total\\\": 7,\\n      \\\"success\\\": 4,\\n      \\\"rate\\\": 0.571\\n    }\\n  },\\n  \\\"episodes\\\": [\\n    {\\n      \\\"task_name\\\": \\\"look_at_obj_in_light-AlarmClock-None-DeskLamp-308\\\",\\n      \\\"task_type\\\": \\\"look_at_obj_in_light\\\",\\n      \\\"task_desc\\\": \\\"Hold the clock and turn on the lamp.\\\",\\n      \\\"success\\\": true,\\n      \\\"steps\\\": 13,\\n      \\\"injected\\\": false,\\n      \\\"operator\\\": \\\"none\\\",\\n      \\\"inject_mode\\\": \\\"none\\\"\\n    },\\n    {\\n      \\\"task_name\\\": \\\"look_at_obj_in_light-Book-None-DeskLamp-308\\\",\\n      \\\"task_type\\\": \\\"look_at_obj_in_light\\\",\\n      \\\"task_desc\\\": \\\"Look at a book by the light of a lamp.\\\",\\n      \\\"success\\\": false,\\n      \\\"steps\\\": 50,\\n      \\\"injected\\\": false,\\n      \\\"opera
…[truncated 8761 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_extract-vanilla-seed123-metrics_20260514T204319",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-14T20:43:55.735073+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "v4-vanilla-seed123-eval",
  "field": "metrics",
  "value": "{'eval_success_rate': 0.66, 'eval_successes': 31, 'eval_total': 47, 'vs_seed42_pp': 4.3, 'vs_seed0_pp': -2.1, 'per_task': {'look_at_obj_in_light': {'success': 5, 'total': 6, 'rate': 0.833}, 'pick_and_place_simple': {'success': 6, 'total': 8, 'rate': 0.75}, 'pick_clean_then_place_in_recep': {'success': 5, 'total': 11, 'rate': 0.455}, 'pick_cool_then_place_in_recep': {'success': 4, 'total': 7, 'rate': 0.571}, 'pick_heat_then_place_in_recep': {'success': 7, 'total': 8, 'rate': 0.875}, 'pick_two_obj_and_place': {'success': 4, 'total': 7, 'rate': 0.571}}}",
  "project": "tax_error_inject_agent"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_extract-vanilla-seed123-metrics_20260514T204319",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "v4-vanilla-seed123-eval",
    "field": "metrics",
    "value": "{'eval_success_rate': 0.66, 'eval_successes': 31, 'eval_total': 47, 'vs_seed42_pp': 4.3, 'vs_seed0_pp': -2.1, 'per_task': {'look_at_obj_in_light': {'success': 5, 'total': 6, 'rate': 0.833}, 'pick_and_place_simple': {'success': 6, 'total': 8, 'rate': 0.75}, 'pick_clean_then_place_in_recep': {'success': 5, 'total': 11, 'rate': 0.455}, 'pick_cool_then_place_in_recep': {'success': 4, 'total': 7, 'rate': 0.571}, 'pick_heat_then_place_in_recep': {'success': 7, 'total': 8, 'rate': 0.875}, 'pick_two_obj_and_place': {'success': 4, 'total': 7, 'rate': 0.571}}}",
    "project": "tax_error_inject_agent"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-14T20:43:55.735254+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"v4-vanilla-seed123-eval\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T18:30:26.635Z\", \"updated_at\": \"2026-05-14T20:43:48.780Z\", \"hypothesis\": \"v4 Vanilla SFT seed=123 eval — multi-seed verification, 4358 samples, comparing with seed=42 baseline (61.7%)\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python3 eval/recovery.py --model_path checkpoints/mini_vanilla_sft_v4_seed123/v1-20260515-022602/checkpoint-1635 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --no_inject --output eval_results/v4_vanilla_seed123_eval.json --device cuda:0\", \"server\": \"autodl-5090\", \"model_name\": \"Qwen3-8B + LoRA (vanilla v4 seed=123)\", \"seed\": 123, \"checkpoint_source\": \"checkpoints/mini_vanilla_sft_v4_seed123/v1-20260515-022602/checkpoint-1635\", \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/checkpoints/mini_vanilla_sft_v4_seed123/v1-20260515-022602/checkpoint-1635\", \"log_path\": \"/tmp/v4_vanilla_seed123_eval.log\", \"eval_data\": \"47 ALFWorld tasks (clean, no injection)\", \"parent\": \"v4-vanilla-seed123\", \"data_path\": \"eval/valid_unseen\", \"data_count\": 47}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T20:37:11.382Z\", \"metrics\": {\"eval_success_rate\": 0.66, \"eval_successes\": 31, \"eval_total\": 47, \"vs_seed42_pp\": 4.3, \"vs_seed0_pp\": -2.1, \"per_task\": {\"look_at_obj_in_light\": {\"success\": 5, \"total\": 6, \"rate\": 0.833}, \"pick_and_place_simple\": {\"success\": 6, \"total\": 8, \"rate\": 0.75}, \"pick_clean_then_place_in_recep\": {\"success\": 5, \"total\": 11, \"rate\": 0.455}, \"pick_cool_then_place_in_recep\": {\"success\": 4, \"total\": 7, \"rate\": 0.571}, \"pick_heat_then_place_in_recep\": {\"success\": 7, \"total\": 8, \"rate\": 0.875}, \"pick_two_obj_and_place\": {\"success\": 4, \"total\": 7, \"rate\": 0.571}}}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1415}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_extract-vanilla-seed123-metrics_20260514T204319",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-14T20:43:55.735442+00:00_

Registry 已更新。汇总：

**v4-vanilla-seed123-eval: 31/47 = 66.0%**

| seed | success_rate | vs seed42 |
|------|-------------|-----------|
| 42 | 61.7% (29/47) | baseline |
| 0 | 68.1% (32/47) | +6.4pp |
| 123 | 66.0% (31/47) | +4.3pp |

三 seed 均值：**65.3%**

分任务类型：
- pick_heat_then_place: 87.5% (最高)
- look_at_obj_in_light: 83.3%
- pick_and_place_simple: 75.0%
- pick_cool_then_place: 57.1%
- pick_two_obj_and_place: 57.1%
- pick_clean_then_place: 45.5% (最低)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_ops_extract-vanilla-seed123-metrics_20260514T204319"
}
```

</details>

---
