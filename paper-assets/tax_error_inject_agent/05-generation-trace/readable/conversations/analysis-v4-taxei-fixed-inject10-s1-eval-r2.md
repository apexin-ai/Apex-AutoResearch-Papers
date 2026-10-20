# analysis v4 taxei fixed inject10 s1 eval r2

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 17
- **Recorded user turns:** 0
- **Tool calls:** 8
- **Original source:** `logs/chats/worker_analysis_v4-taxei-fixed-inject10-s1-eval-r2_20260515T210526.jsonl`
- **Structured JSON:** [`0c42ed6f2ad81ffbbeb1.json`](../../sessions/0c/0c42ed6f2ad81ffbbeb1.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

17 recorded events

### Tool call

_source line 1 · 2026-05-15T21:06:22.530368+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__read_registry",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_v4-taxei-fixed-inject10-s1-eval-r2_20260515T210526",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__read_registry",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-15T21:06:22.530756+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_v4-taxei-fixed-inject10-s1-eval-r2_20260515T210526",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T21:06:22.530948+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/tax_error_inject_agent/eval_results/v4_taxei_fixed_inject10_s1_eval.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_v4-taxei-fixed-inject10-s1-eval-r2_20260515T210526",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat /root/autodl-tmp/tax_error_inject_agent/eval_results/v4_taxei_fixed_inject10_s1_eval.json",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-15T21:06:22.531097+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'exp_id': 'v4-taxei-fixed-inject10-s1-eval-r2'}",
  "project": "tax_error_inject_agent",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_v4-taxei-fixed-inject10-s1-eval-r2_20260515T210526",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'exp_id': 'v4-taxei-fixed-inject10-s1-eval-r2'}",
    "project": "tax_error_inject_agent",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-15T21:06:22.531468+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"model\\\": \\\"checkpoints/v4_taxei_fixed_inject10_s1/v0-20260516-015427/checkpoint-1635\\\",\\n  \\\"eval_split\\\": \\\"valid_unseen\\\",\\n  \\\"inject\\\": false,\\n  \\\"inject_mode\\\": \\\"none\\\",\\n  \\\"total_episodes\\\": 47,\\n  \\\"success_rate\\\": 0.511,\\n  \\\"timestamp\\\": \\\"2026-05-15T21:03:14.557377+00:00\\\",\\n  \\\"by_task_type\\\": {\\n    \\\"look_at_obj_in_light\\\": {\\n      \\\"total\\\": 6,\\n      \\\"success\\\": 4,\\n      \\\"rate\\\": 0.667\\n    },\\n    \\\"pick_and_place_simple\\\": {\\n      \\\"total\\\": 8,\\n      \\\"success\\\": 4,\\n      \\\"rate\\\": 0.5\\n    },\\n    \\\"pick_clean_then_place_in_recep\\\": {\\n      \\\"total\\\": 11,\\n      \\\"success\\\": 5,\\n      \\\"rate\\\": 0.455\\n    },\\n    \\\"pick_cool_then_place_in_recep\\\": {\\n      \\\"total\\\": 7,\\n      \\\"success\\\": 2,\\n      \\\"rate\\\": 0.286\\n    },\\n    \\\"pick_heat_then_place_in_recep\\\": {\\n      \\\"total\\\": 8,\\n      \\\"success\\\": 6,\\n      \\\"rate\\\": 0.75\\n    },\\n    \\\"pick_two_obj_and_place\\\": {\\n      \\\"total\\\": 7,\\n      \\\"success\\\": 3,\\n      \\\"rate\\\": 0.429\\n    }\\n  },\\n  \\\"episodes\\\": [\\n    {\\n      \\\"task_name\\\": \\\"look_at_obj_in_light-AlarmClock-None-DeskLamp-308\\\",\\n      \\\"task_type\\\": \\\"look_at_obj_in_light\\\",\\n      \\\"task_desc\\\": \\\"Hold the clock and turn on the lamp.\\\",\\n      \\\"success\\\": true,\\n      \\\"steps\\\": 7,\\n      \\\"injected\\\": false,\\n      \\\"operator\\\": \\\"none\\\",\\n      \\\"inject_mode\\\": \\\"none\\\"\\n    },\\n    {\\n      \\\"task_name\\\": \\\"look_at_obj_in_light-Book-None-DeskLamp-308\\\",\\n      \\\"task_type\\\": \\\"look_at_obj_in_light\\\",\\n      \\\"task_desc\\\": \\\"Look at a book by the light of a lamp.\\\",\\n      \\\"success\\\": false,\\n      \\\"steps\\\": 50,\\n      \\\"injected\\\": false,\\n      \\\"operator
…[truncated 8761 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_v4-taxei-fixed-inject10-s1-eval-r2_20260515T210526",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-15T21:06:22.531725+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.267}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_v4-taxei-fixed-inject10-s1-eval-r2_20260515T210526",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-15T21:06:22.531923+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "v4-taxei-fixed-inject10-s1-eval-r2",
  "field": "metrics",
  "value": "{'success_rate': 0.511, 'successes': 24, 'total': 47, 'by_task_type': {'look_at_obj_in_light': {'total': 6, 'success': 4, 'rate': 0.667}, 'pick_and_place_simple': {'total': 8, 'success': 4, 'rate': 0.5}, 'pick_clean_then_place_in_recep': {'total': 11, 'success': 5, 'rate': 0.455}, 'pick_cool_then_place_in_recep': {'total': 7, 'success': 2, 'rate': 0.286}, 'pick_heat_then_place_in_recep': {'total': 8, 'success': 6, 'rate': 0.75}, 'pick_two_obj_and_place': {'total': 7, 'success': 3, 'rate': 0.429}}}",
  "project": "tax_error_inject_agent"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_v4-taxei-fixed-inject10-s1-eval-r2_20260515T210526",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "v4-taxei-fixed-inject10-s1-eval-r2",
    "field": "metrics",
    "value": "{'success_rate': 0.511, 'successes': 24, 'total': 47, 'by_task_type': {'look_at_obj_in_light': {'total': 6, 'success': 4, 'rate': 0.667}, 'pick_and_place_simple': {'total': 8, 'success': 4, 'rate': 0.5}, 'pick_clean_then_place_in_recep': {'total': 11, 'success': 5, 'rate': 0.455}, 'pick_cool_then_place_in_recep': {'total': 7, 'success': 2, 'rate': 0.286}, 'pick_heat_then_place_in_recep': {'total': 8, 'success': 6, 'rate': 0.75}, 'pick_two_obj_and_place': {'total': 7, 'success': 3, 'rate': 0.429}}}",
    "project": "tax_error_inject_agent"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-15T21:06:22.532116+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"v4-taxei-fixed-inject10-s1-eval-r2\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T20:54:05.248Z\", \"updated_at\": \"2026-05-15T21:05:58.075Z\", \"spec\": {\"parent\": \"v4-taxei-fixed-inject10-s1\", \"checkpoint_source\": \"v4-taxei-fixed-inject10-s1\", \"eval_data\": \"eval_tasks_47.json\", \"data_count\": 47, \"model_name\": \"Qwen3-8B + LoRA (taxei fixed inject10 s1)\", \"seed\": 42, \"data_path\": \"eval/eval_tasks_47.json\"}, \"hypothesis\": \"v4 TaxEI 10% seed=1 eval (r2, dedicated GPU) — 47 ALFWorld clean tasks.\", \"reproduce\": {\"finished_at\": \"2026-05-15T21:04:33.190Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T21:04:36.432028+00:00\"}]}, \"metrics\": {\"success_rate\": 0.511, \"successes\": 24, \"total\": 47, \"by_task_type\": {\"look_at_obj_in_light\": {\"total\": 6, \"success\": 4, \"rate\": 0.667}, \"pick_and_place_simple\": {\"total\": 8, \"success\": 4, \"rate\": 0.5}, \"pick_clean_then_place_in_recep\": {\"total\": 11, \"success\": 5, \"rate\": 0.455}, \"pick_cool_then_place_in_recep\": {\"total\": 7, \"success\": 2, \"rate\": 0.286}, \"pick_heat_then_place_in_recep\": {\"total\": 8, \"success\": 6, \"rate\": 0.75}, \"pick_two_obj_and_place\": {\"total\": 7, \"success\": 3, \"rate\": 0.429}}}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4982}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_v4-taxei-fixed-inject10-s1-eval-r2_20260515T210526",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-15T21:06:22.532336+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "v4-taxei-fixed-inject10-s1-eval-r2",
  "field": "checkpoint_path",
  "value": "/root/autodl-tmp/tax_error_inject_agent/eval_results/v4_taxei_fixed_inject10_s1_eval.json",
  "project": "tax_error_inject_agent"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_v4-taxei-fixed-inject10-s1-eval-r2_20260515T210526",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "v4-taxei-fixed-inject10-s1-eval-r2",
    "field": "checkpoint_path",
    "value": "/root/autodl-tmp/tax_error_inject_agent/eval_results/v4_taxei_fixed_inject10_s1_eval.json",
    "project": "tax_error_inject_agent"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-15T21:06:22.532513+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"v4-taxei-fixed-inject10-s1-eval-r2\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T20:54:05.248Z\", \"updated_at\": \"2026-05-15T21:06:03.379Z\", \"spec\": {\"parent\": \"v4-taxei-fixed-inject10-s1\", \"checkpoint_source\": \"v4-taxei-fixed-inject10-s1\", \"eval_data\": \"eval_tasks_47.json\", \"data_count\": 47, \"model_name\": \"Qwen3-8B + LoRA (taxei fixed inject10 s1)\", \"seed\": 42, \"data_path\": \"eval/eval_tasks_47.json\"}, \"hypothesis\": \"v4 TaxEI 10% seed=1 eval (r2, dedicated GPU) — 47 ALFWorld clean tasks.\", \"reproduce\": {\"finished_at\": \"2026-05-15T21:04:33.190Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T21:04:36.432028+00:00\"}]}, \"metrics\": {\"success_rate\": 0.511, \"successes\": 24, \"total\": 47, \"by_task_type\": {\"look_at_obj_in_light\": {\"total\": 6, \"success\": 4, \"rate\": 0.667}, \"pick_and_place_simple\": {\"total\": 8, \"success\": 4, \"rate\": 0.5}, \"pick_clean_then_place_in_recep\": {\"total\": 11, \"success\": 5, \"rate\": 0.455}, \"pick_cool_then_place_in_recep\": {\"total\": 7, \"success\": 2, \"rate\": 0.286}, \"pick_heat_then_place_in_recep\": {\"total\": 8, \"success\": 6, \"rate\": 0.75}, \"pick_two_obj_and_place\": {\"total\": 7, \"success\": 3, \"rate\": 0.429}}}, \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/eval_results/v4_taxei_fixed_inject10_s1_eval.json\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5214}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_v4-taxei-fixed-inject10-s1-eval-r2_20260515T210526",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-15T21:06:22.532720+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "v4-taxei-fixed-inject10-s1-eval-r2",
  "field": "log_path",
  "value": "/root/runs/tax_error_inject_agent/v4-taxei-fixed-inject10-s1-eval-r2.log",
  "project": "tax_error_inject_agent"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_v4-taxei-fixed-inject10-s1-eval-r2_20260515T210526",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "v4-taxei-fixed-inject10-s1-eval-r2",
    "field": "log_path",
    "value": "/root/runs/tax_error_inject_agent/v4-taxei-fixed-inject10-s1-eval-r2.log",
    "project": "tax_error_inject_agent"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-15T21:06:22.532891+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"v4-taxei-fixed-inject10-s1-eval-r2\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T20:54:05.248Z\", \"updated_at\": \"2026-05-15T21:06:04.155Z\", \"spec\": {\"parent\": \"v4-taxei-fixed-inject10-s1\", \"checkpoint_source\": \"v4-taxei-fixed-inject10-s1\", \"eval_data\": \"eval_tasks_47.json\", \"data_count\": 47, \"model_name\": \"Qwen3-8B + LoRA (taxei fixed inject10 s1)\", \"seed\": 42, \"data_path\": \"eval/eval_tasks_47.json\"}, \"hypothesis\": \"v4 TaxEI 10% seed=1 eval (r2, dedicated GPU) — 47 ALFWorld clean tasks.\", \"reproduce\": {\"finished_at\": \"2026-05-15T21:04:33.190Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T21:04:36.432028+00:00\"}]}, \"metrics\": {\"success_rate\": 0.511, \"successes\": 24, \"total\": 47, \"by_task_type\": {\"look_at_obj_in_light\": {\"total\": 6, \"success\": 4, \"rate\": 0.667}, \"pick_and_place_simple\": {\"total\": 8, \"success\": 4, \"rate\": 0.5}, \"pick_clean_then_place_in_recep\": {\"total\": 11, \"success\": 5, \"rate\": 0.455}, \"pick_cool_then_place_in_recep\": {\"total\": 7, \"success\": 2, \"rate\": 0.286}, \"pick_heat_then_place_in_recep\": {\"total\": 8, \"success\": 6, \"rate\": 0.75}, \"pick_two_obj_and_place\": {\"total\": 7, \"success\": 3, \"rate\": 0.429}}}, \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/eval_results/v4_taxei_fixed_inject10_s1_eval.json\", \"log_path\": \"/root/runs/tax_error_inject_agent/v4-taxei-fixed-inject10-s1-eval-r2.log\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4506}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_v4-taxei-fixed-inject10-s1-eval-r2_20260515T210526",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-15T21:06:22.533042+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "v4-taxei-fixed-inject10-s1-eval-r2",
  "field": "conclusion",
  "value": "success",
  "project": "tax_error_inject_agent"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_v4-taxei-fixed-inject10-s1-eval-r2_20260515T210526",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "v4-taxei-fixed-inject10-s1-eval-r2",
    "field": "conclusion",
    "value": "success",
    "project": "tax_error_inject_agent"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-15T21:06:22.533201+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"v4-taxei-fixed-inject10-s1-eval-r2\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T20:54:05.248Z\", \"updated_at\": \"2026-05-15T21:06:07.589Z\", \"spec\": {\"parent\": \"v4-taxei-fixed-inject10-s1\", \"checkpoint_source\": \"v4-taxei-fixed-inject10-s1\", \"eval_data\": \"eval_tasks_47.json\", \"data_count\": 47, \"model_name\": \"Qwen3-8B + LoRA (taxei fixed inject10 s1)\", \"seed\": 42, \"data_path\": \"eval/eval_tasks_47.json\"}, \"hypothesis\": \"v4 TaxEI 10% seed=1 eval (r2, dedicated GPU) — 47 ALFWorld clean tasks.\", \"reproduce\": {\"finished_at\": \"2026-05-15T21:04:33.190Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T21:04:36.432028+00:00\"}]}, \"metrics\": {\"success_rate\": 0.511, \"successes\": 24, \"total\": 47, \"by_task_type\": {\"look_at_obj_in_light\": {\"total\": 6, \"success\": 4, \"rate\": 0.667}, \"pick_and_place_simple\": {\"total\": 8, \"success\": 4, \"rate\": 0.5}, \"pick_clean_then_place_in_recep\": {\"total\": 11, \"success\": 5, \"rate\": 0.455}, \"pick_cool_then_place_in_recep\": {\"total\": 7, \"success\": 2, \"rate\": 0.286}, \"pick_heat_then_place_in_recep\": {\"total\": 8, \"success\": 6, \"rate\": 0.75}, \"pick_two_obj_and_place\": {\"total\": 7, \"success\": 3, \"rate\": 0.429}}}, \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/eval_results/v4_taxei_fixed_inject10_s1_eval.json\", \"log_path\": \"/root/runs/tax_error_inject_agent/v4-taxei-fixed-inject10-s1-eval-r2.log\", \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5009}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_v4-taxei-fixed-inject10-s1-eval-r2_20260515T210526",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-15T21:06:22.533339+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "v4-taxei-fixed-inject10-s1-eval-r2",
  "field": "status",
  "value": "DONE",
  "project": "tax_error_inject_agent"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_v4-taxei-fixed-inject10-s1-eval-r2_20260515T210526",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "v4-taxei-fixed-inject10-s1-eval-r2",
    "field": "status",
    "value": "DONE",
    "project": "tax_error_inject_agent"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-15T21:06:22.533516+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"v4-taxei-fixed-inject10-s1-eval-r2\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T20:54:05.248Z\", \"updated_at\": \"2026-05-15T21:06:11.418Z\", \"spec\": {\"parent\": \"v4-taxei-fixed-inject10-s1\", \"checkpoint_source\": \"v4-taxei-fixed-inject10-s1\", \"eval_data\": \"eval_tasks_47.json\", \"data_count\": 47, \"model_name\": \"Qwen3-8B + LoRA (taxei fixed inject10 s1)\", \"seed\": 42, \"data_path\": \"eval/eval_tasks_47.json\"}, \"hypothesis\": \"v4 TaxEI 10% seed=1 eval (r2, dedicated GPU) — 47 ALFWorld clean tasks.\", \"reproduce\": {\"finished_at\": \"2026-05-15T21:04:33.190Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T21:04:36.432028+00:00\"}]}, \"metrics\": {\"success_rate\": 0.511, \"successes\": 24, \"total\": 47, \"by_task_type\": {\"look_at_obj_in_light\": {\"total\": 6, \"success\": 4, \"rate\": 0.667}, \"pick_and_place_simple\": {\"total\": 8, \"success\": 4, \"rate\": 0.5}, \"pick_clean_then_place_in_recep\": {\"total\": 11, \"success\": 5, \"rate\": 0.455}, \"pick_cool_then_place_in_recep\": {\"total\": 7, \"success\": 2, \"rate\": 0.286}, \"pick_heat_then_place_in_recep\": {\"total\": 8, \"success\": 6, \"rate\": 0.75}, \"pick_two_obj_and_place\": {\"total\": 7, \"success\": 3, \"rate\": 0.429}}}, \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/eval_results/v4_taxei_fixed_inject10_s1_eval.json\", \"log_path\": \"/root/runs/tax_error_inject_agent/v4-taxei-fixed-inject10-s1-eval-r2.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T21:06:11.418Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.9648}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_v4-taxei-fixed-inject10-s1-eval-r2_20260515T210526",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-15T21:06:22.533772+00:00_

Registry 已更新为 DONE。汇总如下：

## v4-taxei-fixed-inject10-s1-eval-r2 结果

**Overall: 24/47 = 51.1%**

| Task Type | Success | Rate |
|-----------|---------|------|
| pick_heat_then_place | 6/8 | 75.0% |
| look_at_obj_in_light | 4/6 | 66.7% |
| pick_and_place_simple | 4/8 | 50.0% |
| pick_clean_then_place | 5/11 | 45.5% |
| pick_two_obj_and_place | 3/7 | 42.9% |
| pick_cool_then_place | 2/7 | 28.6% |

## 与已知 10% inject 结果对比

| 方法 | s42 | s0 | s1 (本次) | s123 |
|------|-----|-----|-----------|------|
| **TaxEI 10%** | 61.7% | 70.2% | **51.1%** | 55.3% |
| **Random 10%** | 68.1% | 66.0% | — | 55.3% |

s1 = 51.1% 是 TaxEI 10% 四个 seed 中最低的，比 s42 低 10.6pp，比 s0 低 19.1pp。seed 间方差较大（51.1%–70.2%），说明 TaxEI 10% 在低数据量下对 seed 敏感。当前 s1 结果也低于 Random 10% 的两个已知 seed（68.1%, 66.0%）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_v4-taxei-fixed-inject10-s1-eval-r2_20260515T210526"
}
```

</details>

---
