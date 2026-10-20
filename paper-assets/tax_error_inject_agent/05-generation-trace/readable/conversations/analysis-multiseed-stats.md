# analysis multiseed stats

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 41
- **Recorded user turns:** 0
- **Tool calls:** 20
- **Original source:** `logs/chats/worker_analysis_multiseed-stats_20260514T214124.jsonl`
- **Structured JSON:** [`8a0a529645b19ecb4bb9.json`](../../sessions/8a/8a0a529645b19ecb4bb9.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

41 recorded events

### Tool call

_source line 1 · 2026-05-14T21:44:14.275173+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__save_project_file",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_multiseed-stats_20260514T214124",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__save_project_file",
    "max_results": "4"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-14T21:44:14.275510+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_multiseed-stats_20260514T214124",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-14T21:44:14.275747+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "ls /root/autodl-tmp/tax_error_inject_agent/scripts/analyze* /root/autodl-tmp/tax_error_inject_agent/eval/analyze* 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_multiseed-stats_20260514T214124",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "ls /root/autodl-tmp/tax_error_inject_agent/scripts/analyze* /root/autodl-tmp/tax_error_inject_agent/eval/analyze* 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-14T21:44:14.275949+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_multiseed-stats_20260514T214124",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-14T21:44:14.276151+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "find /root/autodl-tmp/tax_error_inject_agent -name \"eval_results\" -type d",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_multiseed-stats_20260514T214124",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "find /root/autodl-tmp/tax_error_inject_agent -name \"eval_results\" -type d",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-14T21:44:14.276349+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "find /root/autodl-tmp/tax_error_inject_agent -name \"*.json\" -path \"*/eval*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_multiseed-stats_20260514T214124",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "find /root/autodl-tmp/tax_error_inject_agent -name \"*.json\" -path \"*/eval*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-14T21:44:14.276565+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/tax_error_inject_agent/eval_results\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.96}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_multiseed-stats_20260514T214124",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-14T21:44:14.276820+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/tax_error_inject_agent/eval/eval_tasks_47.json\\n/root/autodl-tmp/tax_error_inject_agent/eval_results/vanilla_react_baseline.json\\n/root/autodl-tmp/tax_error_inject_agent/eval_results/mini_vanilla_clean.json\\n/root/autodl-tmp/tax_error_inject_agent/eval_results/mini_taxei_clean.json\\n/root/autodl-tmp/tax_error_inject_agent/eval_results/pipeline_test.json\\n/root/autodl-tmp/tax_error_inject_agent/eval_results/adapter_test.json\\n/root/autodl-tmp/tax_error_inject_agent/eval_results/gate1_injection_validity.json\\n/root/autodl-tmp/tax_error_inject_agent/eval_results/gate2_recovery_quality.json\\n/root/autodl-tmp/tax_error_inject_agent/eval_results/v3_vanilla.json\\n/root/autodl-tmp/tax_error_inject_agent/eval_results/v3_random.json\\n/root/autodl-tmp/tax_error_inject_agent/eval_results/v3_taxei.json\\n/root/autodl-tmp/tax_error_inject_agent/eval_results/v4_vanilla_eval.json\\n/root/autodl-tmp/tax_error_inject_agent/eval_results/gate3_judgment.json\\n/root/autodl-tmp/tax_error_inject_agent/eval_results/v4_taxei_eval.json\\n/root/autodl-tmp/tax_error_inject_agent/eval_results/v4_random_eval.json\\n/root/autodl-tmp/tax_error_inject_agent/eval_results/dryrun_injected_vanilla.json\\n/root/autodl-tmp/tax_error_inject_agent/eval_results/dryrun_recovery.json\\n/root/autodl-tmp/tax_error_inject_agent/eval_results/v4_vanilla_seed0_eval.json\\n/root/autodl-tmp/tax_error_inject_agent/eval_results/v4_vanilla_seed123_eval.json\\n/root/autodl-tmp/tax_error_inject_agent/eval_results/v4_random_seed0_eval.json\\n/root/autodl-tmp/tax_error_inject_agent/eval_results/v4_taxei_seed0_eval.json\\n/root/autodl-tmp/tax_error_inject_agent/eval_results/v4_vanilla_recovery_eval.json\\n/root/autodl-tmp/tax_error_inject_agent/eval_results/v4_taxei_recovery_eval.json\\n/root/autodl-tmp/tax_error_inject_agent/eval_results/v4_random_recovery_eval.json\\n/root/autodl-tmp/tax_error_inject_agent/eval_results/v4_taxei_recovery_eval
…[truncated 115 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_multiseed-stats_20260514T214124",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-14T21:44:14.277106+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "ls /root/autodl-tmp/tax_error_inject_agent/scripts/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_multiseed-stats_20260514T214124",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "ls /root/autodl-tmp/tax_error_inject_agent/scripts/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-14T21:44:14.277327+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"__pycache__\\nanalyze_gate3.py\\nanalyze_multiseed.py\\nrun_injected_eval.sh\\nrun_multiseed_eval.sh\\nrun_v3_eval.sh\\nrun_v4_eval.sh\\nverify_gate1.py\\nverify_gate2.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.31}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_multiseed-stats_20260514T214124",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-14T21:44:14.277553+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/tax_error_inject_agent/eval_results/v4_vanilla_eval.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_multiseed-stats_20260514T214124",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat /root/autodl-tmp/tax_error_inject_agent/eval_results/v4_vanilla_eval.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-14T21:44:14.278136+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"model\\\": \\\"checkpoints/mini_vanilla_sft_v4/v0-20260514-201441/checkpoint-1635\\\",\\n  \\\"eval_split\\\": \\\"valid_unseen\\\",\\n  \\\"inject\\\": false,\\n  \\\"total_episodes\\\": 47,\\n  \\\"success_rate\\\": 0.617,\\n  \\\"timestamp\\\": \\\"2026-05-14T14:45:16.148812+00:00\\\",\\n  \\\"by_task_type\\\": {\\n    \\\"look_at_obj_in_light\\\": {\\n      \\\"total\\\": 6,\\n      \\\"success\\\": 5,\\n      \\\"rate\\\": 0.833\\n    },\\n    \\\"pick_and_place_simple\\\": {\\n      \\\"total\\\": 8,\\n      \\\"success\\\": 5,\\n      \\\"rate\\\": 0.625\\n    },\\n    \\\"pick_clean_then_place_in_recep\\\": {\\n      \\\"total\\\": 11,\\n      \\\"success\\\": 5,\\n      \\\"rate\\\": 0.455\\n    },\\n    \\\"pick_cool_then_place_in_recep\\\": {\\n      \\\"total\\\": 7,\\n      \\\"success\\\": 4,\\n      \\\"rate\\\": 0.571\\n    },\\n    \\\"pick_heat_then_place_in_recep\\\": {\\n      \\\"total\\\": 8,\\n      \\\"success\\\": 6,\\n      \\\"rate\\\": 0.75\\n    },\\n    \\\"pick_two_obj_and_place\\\": {\\n      \\\"total\\\": 7,\\n      \\\"success\\\": 4,\\n      \\\"rate\\\": 0.571\\n    }\\n  },\\n  \\\"episodes\\\": [\\n    {\\n      \\\"task_name\\\": \\\"look_at_obj_in_light-AlarmClock-None-DeskLamp-308\\\",\\n      \\\"task_type\\\": \\\"look_at_obj_in_light\\\",\\n      \\\"task_desc\\\": \\\"Hold the clock and turn on the lamp.\\\",\\n      \\\"success\\\": true,\\n      \\\"steps\\\": 10,\\n      \\\"injected\\\": false,\\n      \\\"operator\\\": \\\"none\\\"\\n    },\\n    {\\n      \\\"task_name\\\": \\\"look_at_obj_in_light-Book-None-DeskLamp-308\\\",\\n      \\\"task_type\\\": \\\"look_at_obj_in_light\\\",\\n      \\\"task_desc\\\": \\\"Look at a book by the light of a lamp.\\\",\\n      \\\"success\\\": false,\\n      \\\"steps\\\": 50,\\n      \\\"injected\\\": false,\\n      \\\"operator\\\": \\\"none\\\"\\n    },\\n    {\\n      \\\"task_name\\\": \\\"look_at_obj_in_ligh
…[truncated 8611 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_multiseed-stats_20260514T214124",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-14T21:44:14.278405+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/tax_error_inject_agent/eval_results/v4_taxei_eval.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_multiseed-stats_20260514T214124",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat /root/autodl-tmp/tax_error_inject_agent/eval_results/v4_taxei_eval.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-14T21:44:14.278987+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"model\\\": \\\"checkpoints/mini_taxei_sft_v4/v1-20260514-213102/checkpoint-3387\\\",\\n  \\\"eval_split\\\": \\\"valid_unseen\\\",\\n  \\\"inject\\\": false,\\n  \\\"total_episodes\\\": 47,\\n  \\\"success_rate\\\": 0.617,\\n  \\\"timestamp\\\": \\\"2026-05-14T16:34:41.278910+00:00\\\",\\n  \\\"by_task_type\\\": {\\n    \\\"look_at_obj_in_light\\\": {\\n      \\\"total\\\": 6,\\n      \\\"success\\\": 6,\\n      \\\"rate\\\": 1.0\\n    },\\n    \\\"pick_and_place_simple\\\": {\\n      \\\"total\\\": 8,\\n      \\\"success\\\": 5,\\n      \\\"rate\\\": 0.625\\n    },\\n    \\\"pick_clean_then_place_in_recep\\\": {\\n      \\\"total\\\": 11,\\n      \\\"success\\\": 6,\\n      \\\"rate\\\": 0.545\\n    },\\n    \\\"pick_cool_then_place_in_recep\\\": {\\n      \\\"total\\\": 7,\\n      \\\"success\\\": 3,\\n      \\\"rate\\\": 0.429\\n    },\\n    \\\"pick_heat_then_place_in_recep\\\": {\\n      \\\"total\\\": 8,\\n      \\\"success\\\": 7,\\n      \\\"rate\\\": 0.875\\n    },\\n    \\\"pick_two_obj_and_place\\\": {\\n      \\\"total\\\": 7,\\n      \\\"success\\\": 2,\\n      \\\"rate\\\": 0.286\\n    }\\n  },\\n  \\\"episodes\\\": [\\n    {\\n      \\\"task_name\\\": \\\"look_at_obj_in_light-AlarmClock-None-DeskLamp-308\\\",\\n      \\\"task_type\\\": \\\"look_at_obj_in_light\\\",\\n      \\\"task_desc\\\": \\\"Hold the clock and turn on the lamp.\\\",\\n      \\\"success\\\": true,\\n      \\\"steps\\\": 5,\\n      \\\"injected\\\": false,\\n      \\\"operator\\\": \\\"none\\\"\\n    },\\n    {\\n      \\\"task_name\\\": \\\"look_at_obj_in_light-Book-None-DeskLamp-308\\\",\\n      \\\"task_type\\\": \\\"look_at_obj_in_light\\\",\\n      \\\"task_desc\\\": \\\"Look at a book by the light of a lamp.\\\",\\n      \\\"success\\\": true,\\n      \\\"steps\\\": 25,\\n      \\\"injected\\\": false,\\n      \\\"operator\\\": \\\"none\\\"\\n    },\\n    {\\n      \\\"task_name\\\": \\\"look_at_obj_in_light-Bow
…[truncated 8614 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_multiseed-stats_20260514T214124",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-14T21:44:14.279261+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/tax_error_inject_agent/eval_results/v4_random_eval.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_multiseed-stats_20260514T214124",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat /root/autodl-tmp/tax_error_inject_agent/eval_results/v4_random_eval.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-14T21:44:14.279848+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"model\\\": \\\"checkpoints/mini_random_sft_v4/v1-20260514-213104/checkpoint-3387\\\",\\n  \\\"eval_split\\\": \\\"valid_unseen\\\",\\n  \\\"inject\\\": false,\\n  \\\"total_episodes\\\": 47,\\n  \\\"success_rate\\\": 0.66,\\n  \\\"timestamp\\\": \\\"2026-05-14T16:36:22.326477+00:00\\\",\\n  \\\"by_task_type\\\": {\\n    \\\"look_at_obj_in_light\\\": {\\n      \\\"total\\\": 6,\\n      \\\"success\\\": 6,\\n      \\\"rate\\\": 1.0\\n    },\\n    \\\"pick_and_place_simple\\\": {\\n      \\\"total\\\": 8,\\n      \\\"success\\\": 4,\\n      \\\"rate\\\": 0.5\\n    },\\n    \\\"pick_clean_then_place_in_recep\\\": {\\n      \\\"total\\\": 11,\\n      \\\"success\\\": 6,\\n      \\\"rate\\\": 0.545\\n    },\\n    \\\"pick_cool_then_place_in_recep\\\": {\\n      \\\"total\\\": 7,\\n      \\\"success\\\": 4,\\n      \\\"rate\\\": 0.571\\n    },\\n    \\\"pick_heat_then_place_in_recep\\\": {\\n      \\\"total\\\": 8,\\n      \\\"success\\\": 7,\\n      \\\"rate\\\": 0.875\\n    },\\n    \\\"pick_two_obj_and_place\\\": {\\n      \\\"total\\\": 7,\\n      \\\"success\\\": 4,\\n      \\\"rate\\\": 0.571\\n    }\\n  },\\n  \\\"episodes\\\": [\\n    {\\n      \\\"task_name\\\": \\\"look_at_obj_in_light-AlarmClock-None-DeskLamp-308\\\",\\n      \\\"task_type\\\": \\\"look_at_obj_in_light\\\",\\n      \\\"task_desc\\\": \\\"Hold the clock and turn on the lamp.\\\",\\n      \\\"success\\\": true,\\n      \\\"steps\\\": 9,\\n      \\\"injected\\\": false,\\n      \\\"operator\\\": \\\"none\\\"\\n    },\\n    {\\n      \\\"task_name\\\": \\\"look_at_obj_in_light-Book-None-DeskLamp-308\\\",\\n      \\\"task_type\\\": \\\"look_at_obj_in_light\\\",\\n      \\\"task_desc\\\": \\\"Look at a book by the light of a lamp.\\\",\\n      \\\"success\\\": true,\\n      \\\"steps\\\": 16,\\n      \\\"injected\\\": false,\\n      \\\"operator\\\": \\\"none\\\"\\n    },\\n    {\\n      \\\"task_name\\\": \\\"look_at_obj_in_light-Bowl-
…[truncated 8614 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_multiseed-stats_20260514T214124",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-14T21:44:14.280178+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/tax_error_inject_agent/scripts/analyze_multiseed.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_multiseed-stats_20260514T214124",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat /root/autodl-tmp/tax_error_inject_agent/scripts/analyze_multiseed.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-14T21:44:14.280637+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"# Multi-seed experiment analysis for D010 Phase 1\\n# Input: eval_results/v4_{variant}_eval.json (seed=42), v4_{variant}_seed{X}_eval.json\\n# Output: terminal summary + outputs/multiseed_analysis.json\\n\\nimport argparse\\nimport json\\nimport os\\nimport sys\\nfrom pathlib import Path\\n\\nimport numpy as np\\n\\n\\nVARIANTS = {\\n    \\\"vanilla\\\": {\\\"seeds\\\": [42, 0, 123], \\\"samples\\\": 4358},\\n    \\\"taxei\\\":   {\\\"seeds\\\": [42, 0],          \\\"samples\\\": 9029},\\n    \\\"random\\\":  {\\\"seeds\\\": [42, 0],          \\\"samples\\\": 9029},\\n}\\n\\nTASK_TYPES = [\\n    \\\"look_at_obj_in_light\\\",\\n    \\\"pick_and_place_simple\\\",\\n    \\\"pick_clean_then_place_in_recep\\\",\\n    \\\"pick_cool_then_place_in_recep\\\",\\n    \\\"pick_heat_then_place_in_recep\\\",\\n    \\\"pick_two_obj_and_place\\\",\\n]\\n\\nCOMPARISONS = [\\n    (\\\"taxei\\\", \\\"vanilla\\\"),\\n    (\\\"taxei\\\", \\\"random\\\"),\\n    (\\\"random\\\", \\\"vanilla\\\"),\\n]\\n\\n\\ndef find_eval_file(eval_dir: Path, variant: str, seed: int) -> Path | None:\\n    if seed == 42:\\n        p = eval_dir / f\\\"v4_{variant}_eval.json\\\"\\n    else:\\n        p = eval_dir / f\\\"v4_{variant}_seed{seed}_eval.json\\\"\\n    return p if p.exists() else None\\n\\n\\ndef load_results(eval_dir: Path) -> dict:\\n    data = {}\\n    for variant, info in VARIANTS.items():\\n        data[variant] = {}\\n        for seed in info[\\\"seeds\\\"]:\\n            fp = find_eval_file(eval_dir, variant, seed)\\n            if fp is None:\\n                print(f\\\"  [WARN] Missing: {variant} seed={seed}\\\", file=sys.stderr)\\n                continue\\n            with open(fp) as f:\\n                data[variant][seed] = json.load(f)\\n    return data\\n\\n\\ndef bootstrap_ci(values: np.ndarray, n_boot: int = 1000, ci: float = 0.95, rng_seed: int = 42) -> tuple:\\n    rng = np.random.RandomState(rng_seed)\\n    n = len(value
…[truncated 7363 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_multiseed-stats_20260514T214124",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-14T21:44:14.280897+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/tax_error_inject_agent/eval_results/v4_vanilla_seed0_eval.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_multiseed-stats_20260514T214124",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat /root/autodl-tmp/tax_error_inject_agent/eval_results/v4_vanilla_seed0_eval.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-14T21:44:14.281458+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"model\\\": \\\"/root/autodl-tmp/tax_error_inject_agent/checkpoints/mini_vanilla_sft_v4_seed0/v0-20260515-014317/checkpoint-1635\\\",\\n  \\\"eval_split\\\": \\\"valid_unseen\\\",\\n  \\\"inject\\\": false,\\n  \\\"inject_mode\\\": \\\"none\\\",\\n  \\\"total_episodes\\\": 47,\\n  \\\"success_rate\\\": 0.681,\\n  \\\"timestamp\\\": \\\"2026-05-14T19:00:55.659210+00:00\\\",\\n  \\\"by_task_type\\\": {\\n    \\\"look_at_obj_in_light\\\": {\\n      \\\"total\\\": 6,\\n      \\\"success\\\": 5,\\n      \\\"rate\\\": 0.833\\n    },\\n    \\\"pick_and_place_simple\\\": {\\n      \\\"total\\\": 8,\\n      \\\"success\\\": 5,\\n      \\\"rate\\\": 0.625\\n    },\\n    \\\"pick_clean_then_place_in_recep\\\": {\\n      \\\"total\\\": 11,\\n      \\\"success\\\": 6,\\n      \\\"rate\\\": 0.545\\n    },\\n    \\\"pick_cool_then_place_in_recep\\\": {\\n      \\\"total\\\": 7,\\n      \\\"success\\\": 4,\\n      \\\"rate\\\": 0.571\\n    },\\n    \\\"pick_heat_then_place_in_recep\\\": {\\n      \\\"total\\\": 8,\\n      \\\"success\\\": 7,\\n      \\\"rate\\\": 0.875\\n    },\\n    \\\"pick_two_obj_and_place\\\": {\\n      \\\"total\\\": 7,\\n      \\\"success\\\": 5,\\n      \\\"rate\\\": 0.714\\n    }\\n  },\\n  \\\"episodes\\\": [\\n    {\\n      \\\"task_name\\\": \\\"look_at_obj_in_light-AlarmClock-None-DeskLamp-308\\\",\\n      \\\"task_type\\\": \\\"look_at_obj_in_light\\\",\\n      \\\"task_desc\\\": \\\"Hold the clock and turn on the lamp.\\\",\\n      \\\"success\\\": true,\\n      \\\"steps\\\": 13,\\n      \\\"injected\\\": false,\\n      \\\"operator\\\": \\\"none\\\",\\n      \\\"inject_mode\\\": \\\"none\\\"\\n    },\\n    {\\n      \\\"task_name\\\": \\\"look_at_obj_in_light-Book-None-DeskLamp-308\\\",\\n      \\\"task_type\\\": \\\"look_at_obj_in_light\\\",\\n      \\\"task_desc\\\": \\\"Look at a book by the light of a lamp.\\\",\\n      \\\"success\\\": false,\\n      \\\"steps\\\": 50,\\n      \\
…[truncated 8752 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_multiseed-stats_20260514T214124",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-14T21:44:14.281753+00:00_

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
  "session": "worker_analysis_multiseed-stats_20260514T214124",
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

_source line 22 · 2026-05-14T21:44:14.282306+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"model\\\": \\\"checkpoints/mini_vanilla_sft_v4_seed123/v1-20260515-022602/checkpoint-1635\\\",\\n  \\\"eval_split\\\": \\\"valid_unseen\\\",\\n  \\\"inject\\\": false,\\n  \\\"inject_mode\\\": \\\"none\\\",\\n  \\\"total_episodes\\\": 47,\\n  \\\"success_rate\\\": 0.66,\\n  \\\"timestamp\\\": \\\"2026-05-14T19:39:11.185689+00:00\\\",\\n  \\\"by_task_type\\\": {\\n    \\\"look_at_obj_in_light\\\": {\\n      \\\"total\\\": 6,\\n      \\\"success\\\": 5,\\n      \\\"rate\\\": 0.833\\n    },\\n    \\\"pick_and_place_simple\\\": {\\n      \\\"total\\\": 8,\\n      \\\"success\\\": 6,\\n      \\\"rate\\\": 0.75\\n    },\\n    \\\"pick_clean_then_place_in_recep\\\": {\\n      \\\"total\\\": 11,\\n      \\\"success\\\": 5,\\n      \\\"rate\\\": 0.455\\n    },\\n    \\\"pick_cool_then_place_in_recep\\\": {\\n      \\\"total\\\": 7,\\n      \\\"success\\\": 4,\\n      \\\"rate\\\": 0.571\\n    },\\n    \\\"pick_heat_then_place_in_recep\\\": {\\n      \\\"total\\\": 8,\\n      \\\"success\\\": 7,\\n      \\\"rate\\\": 0.875\\n    },\\n    \\\"pick_two_obj_and_place\\\": {\\n      \\\"total\\\": 7,\\n      \\\"success\\\": 4,\\n      \\\"rate\\\": 0.571\\n    }\\n  },\\n  \\\"episodes\\\": [\\n    {\\n      \\\"task_name\\\": \\\"look_at_obj_in_light-AlarmClock-None-DeskLamp-308\\\",\\n      \\\"task_type\\\": \\\"look_at_obj_in_light\\\",\\n      \\\"task_desc\\\": \\\"Hold the clock and turn on the lamp.\\\",\\n      \\\"success\\\": true,\\n      \\\"steps\\\": 13,\\n      \\\"injected\\\": false,\\n      \\\"operator\\\": \\\"none\\\",\\n      \\\"inject_mode\\\": \\\"none\\\"\\n    },\\n    {\\n      \\\"task_name\\\": \\\"look_at_obj_in_light-Book-None-DeskLamp-308\\\",\\n      \\\"task_type\\\": \\\"look_at_obj_in_light\\\",\\n      \\\"task_desc\\\": \\\"Look at a book by the light of a lamp.\\\",\\n      \\\"success\\\": false,\\n      \\\"steps\\\": 50,\\n      \\\"injected\\\": false,\\n      \\\"opera
…[truncated 8761 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_multiseed-stats_20260514T214124",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-14T21:44:14.282571+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/tax_error_inject_agent/eval_results/v4_taxei_seed0_eval.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_multiseed-stats_20260514T214124",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat /root/autodl-tmp/tax_error_inject_agent/eval_results/v4_taxei_seed0_eval.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-14T21:44:14.283135+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"model\\\": \\\"checkpoints/mini_taxei_sft_v4_seed0/v0-20260515-014320/checkpoint-3387\\\",\\n  \\\"eval_split\\\": \\\"valid_unseen\\\",\\n  \\\"inject\\\": false,\\n  \\\"inject_mode\\\": \\\"none\\\",\\n  \\\"total_episodes\\\": 47,\\n  \\\"success_rate\\\": 0.468,\\n  \\\"timestamp\\\": \\\"2026-05-14T19:43:11.801605+00:00\\\",\\n  \\\"by_task_type\\\": {\\n    \\\"look_at_obj_in_light\\\": {\\n      \\\"total\\\": 6,\\n      \\\"success\\\": 5,\\n      \\\"rate\\\": 0.833\\n    },\\n    \\\"pick_and_place_simple\\\": {\\n      \\\"total\\\": 8,\\n      \\\"success\\\": 3,\\n      \\\"rate\\\": 0.375\\n    },\\n    \\\"pick_clean_then_place_in_recep\\\": {\\n      \\\"total\\\": 11,\\n      \\\"success\\\": 5,\\n      \\\"rate\\\": 0.455\\n    },\\n    \\\"pick_cool_then_place_in_recep\\\": {\\n      \\\"total\\\": 7,\\n      \\\"success\\\": 2,\\n      \\\"rate\\\": 0.286\\n    },\\n    \\\"pick_heat_then_place_in_recep\\\": {\\n      \\\"total\\\": 8,\\n      \\\"success\\\": 4,\\n      \\\"rate\\\": 0.5\\n    },\\n    \\\"pick_two_obj_and_place\\\": {\\n      \\\"total\\\": 7,\\n      \\\"success\\\": 3,\\n      \\\"rate\\\": 0.429\\n    }\\n  },\\n  \\\"episodes\\\": [\\n    {\\n      \\\"task_name\\\": \\\"look_at_obj_in_light-AlarmClock-None-DeskLamp-308\\\",\\n      \\\"task_type\\\": \\\"look_at_obj_in_light\\\",\\n      \\\"task_desc\\\": \\\"Hold the clock and turn on the lamp.\\\",\\n      \\\"success\\\": true,\\n      \\\"steps\\\": 5,\\n      \\\"injected\\\": false,\\n      \\\"operator\\\": \\\"none\\\",\\n      \\\"inject_mode\\\": \\\"none\\\"\\n    },\\n    {\\n      \\\"task_name\\\": \\\"look_at_obj_in_light-Book-None-DeskLamp-308\\\",\\n      \\\"task_type\\\": \\\"look_at_obj_in_light\\\",\\n      \\\"task_desc\\\": \\\"Look at a book by the light of a lamp.\\\",\\n      \\\"success\\\": false,\\n      \\\"steps\\\": 50,\\n      \\\"injected\\\": false,\\n      \\\"operator\\
…[truncated 8761 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_multiseed-stats_20260514T214124",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-14T21:44:14.283390+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/tax_error_inject_agent/eval_results/v4_random_seed0_eval.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_multiseed-stats_20260514T214124",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat /root/autodl-tmp/tax_error_inject_agent/eval_results/v4_random_seed0_eval.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-14T21:44:14.283968+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"model\\\": \\\"checkpoints/mini_random_sft_v4_seed0/v0-20260515-014329/checkpoint-3387\\\",\\n  \\\"eval_split\\\": \\\"valid_unseen\\\",\\n  \\\"inject\\\": false,\\n  \\\"inject_mode\\\": \\\"none\\\",\\n  \\\"total_episodes\\\": 47,\\n  \\\"success_rate\\\": 0.553,\\n  \\\"timestamp\\\": \\\"2026-05-14T19:43:05.464648+00:00\\\",\\n  \\\"by_task_type\\\": {\\n    \\\"look_at_obj_in_light\\\": {\\n      \\\"total\\\": 6,\\n      \\\"success\\\": 5,\\n      \\\"rate\\\": 0.833\\n    },\\n    \\\"pick_and_place_simple\\\": {\\n      \\\"total\\\": 8,\\n      \\\"success\\\": 4,\\n      \\\"rate\\\": 0.5\\n    },\\n    \\\"pick_clean_then_place_in_recep\\\": {\\n      \\\"total\\\": 11,\\n      \\\"success\\\": 6,\\n      \\\"rate\\\": 0.545\\n    },\\n    \\\"pick_cool_then_place_in_recep\\\": {\\n      \\\"total\\\": 7,\\n      \\\"success\\\": 4,\\n      \\\"rate\\\": 0.571\\n    },\\n    \\\"pick_heat_then_place_in_recep\\\": {\\n      \\\"total\\\": 8,\\n      \\\"success\\\": 4,\\n      \\\"rate\\\": 0.5\\n    },\\n    \\\"pick_two_obj_and_place\\\": {\\n      \\\"total\\\": 7,\\n      \\\"success\\\": 3,\\n      \\\"rate\\\": 0.429\\n    }\\n  },\\n  \\\"episodes\\\": [\\n    {\\n      \\\"task_name\\\": \\\"look_at_obj_in_light-AlarmClock-None-DeskLamp-308\\\",\\n      \\\"task_type\\\": \\\"look_at_obj_in_light\\\",\\n      \\\"task_desc\\\": \\\"Hold the clock and turn on the lamp.\\\",\\n      \\\"success\\\": true,\\n      \\\"steps\\\": 8,\\n      \\\"injected\\\": false,\\n      \\\"operator\\\": \\\"none\\\",\\n      \\\"inject_mode\\\": \\\"none\\\"\\n    },\\n    {\\n      \\\"task_name\\\": \\\"look_at_obj_in_light-Book-None-DeskLamp-308\\\",\\n      \\\"task_type\\\": \\\"look_at_obj_in_light\\\",\\n      \\\"task_desc\\\": \\\"Look at a book by the light of a lamp.\\\",\\n      \\\"success\\\": false,\\n      \\\"steps\\\": 50,\\n      \\\"injected\\\": false,\\n      \\\"operator\\\
…[truncated 8761 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_multiseed-stats_20260514T214124",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-14T21:44:14.284270+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/tax_error_inject_agent/eval_results/v4_vanilla_recovery_eval.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_multiseed-stats_20260514T214124",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat /root/autodl-tmp/tax_error_inject_agent/eval_results/v4_vanilla_recovery_eval.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-14T21:44:14.284798+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"model\\\": \\\"/root/autodl-tmp/tax_error_inject_agent/checkpoints/mini_vanilla_sft_v4/v0-20260514-201441/checkpoint-1635\\\",\\n  \\\"model_variant\\\": \\\"vanilla\\\",\\n  \\\"inject\\\": true,\\n  \\\"seed\\\": 42,\\n  \\\"total_episodes\\\": 47,\\n  \\\"success_rate\\\": 0.617,\\n  \\\"recovery_rate\\\": 0.617,\\n  \\\"detection_rate\\\": 0.0,\\n  \\\"timestamp\\\": \\\"2026-05-14T19:45:46.465973+00:00\\\",\\n  \\\"by_operator\\\": {\\n    \\\"C1_context_truncation\\\": {\\n      \\\"total\\\": 12,\\n      \\\"recovered\\\": 9,\\n      \\\"detected\\\": 0,\\n      \\\"recovery_rate\\\": 0.75,\\n      \\\"detection_rate\\\": 0.0\\n    },\\n    \\\"C4_observation_masking\\\": {\\n      \\\"total\\\": 11,\\n      \\\"recovered\\\": 6,\\n      \\\"detected\\\": 0,\\n      \\\"recovery_rate\\\": 0.545,\\n      \\\"detection_rate\\\": 0.0\\n    },\\n    \\\"P1_step_order_swap\\\": {\\n      \\\"total\\\": 12,\\n      \\\"recovered\\\": 7,\\n      \\\"detected\\\": 0,\\n      \\\"recovery_rate\\\": 0.583,\\n      \\\"detection_rate\\\": 0.0\\n    },\\n    \\\"P2_sub_goal_deletion\\\": {\\n      \\\"total\\\": 12,\\n      \\\"recovered\\\": 7,\\n      \\\"detected\\\": 0,\\n      \\\"recovery_rate\\\": 0.583,\\n      \\\"detection_rate\\\": 0.0\\n    }\\n  },\\n  \\\"by_task_type\\\": {\\n    \\\"look_at_obj_in_light\\\": {\\n      \\\"total\\\": 6,\\n      \\\"success\\\": 5,\\n      \\\"detected\\\": 0,\\n      \\\"rate\\\": 0.833\\n    },\\n    \\\"pick_and_place_simple\\\": {\\n      \\\"total\\\": 8,\\n      \\\"success\\\": 5,\\n      \\\"detected\\\": 0,\\n      \\\"rate\\\": 0.625\\n    },\\n    \\\"pick_clean_then_place_in_recep\\\": {\\n      \\\"total\\\": 11,\\n      \\\"success\\\": 5,\\n      \\\"detected\\\": 0,\\n      \\\"rate\\\": 0.455\\n    },\\n    \\\"pick_cool_then_place_in_recep\\\": {\\n      \\\"total\\\": 7,\\n      \\\"success\\\": 4,\\n      \\\"detected\\\": 0,\\n      \\\"r
…[truncated 8323 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_multiseed-stats_20260514T214124",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-14T21:44:14.285067+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/tax_error_inject_agent/eval_results/v4_taxei_recovery_eval.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_multiseed-stats_20260514T214124",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat /root/autodl-tmp/tax_error_inject_agent/eval_results/v4_taxei_recovery_eval.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-14T21:44:14.285624+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"model\\\": \\\"/root/autodl-tmp/tax_error_inject_agent/checkpoints/mini_taxei_sft_v4/v1-20260514-213102/checkpoint-3387\\\",\\n  \\\"model_variant\\\": \\\"taxei\\\",\\n  \\\"inject\\\": true,\\n  \\\"seed\\\": 42,\\n  \\\"total_episodes\\\": 47,\\n  \\\"success_rate\\\": 0.596,\\n  \\\"recovery_rate\\\": 0.596,\\n  \\\"detection_rate\\\": 0.0,\\n  \\\"timestamp\\\": \\\"2026-05-14T20:49:14.687239+00:00\\\",\\n  \\\"by_operator\\\": {\\n    \\\"C1_context_truncation\\\": {\\n      \\\"total\\\": 12,\\n      \\\"recovered\\\": 8,\\n      \\\"detected\\\": 0,\\n      \\\"recovery_rate\\\": 0.667,\\n      \\\"detection_rate\\\": 0.0\\n    },\\n    \\\"C4_observation_masking\\\": {\\n      \\\"total\\\": 11,\\n      \\\"recovered\\\": 7,\\n      \\\"detected\\\": 0,\\n      \\\"recovery_rate\\\": 0.636,\\n      \\\"detection_rate\\\": 0.0\\n    },\\n    \\\"P1_step_order_swap\\\": {\\n      \\\"total\\\": 12,\\n      \\\"recovered\\\": 7,\\n      \\\"detected\\\": 0,\\n      \\\"recovery_rate\\\": 0.583,\\n      \\\"detection_rate\\\": 0.0\\n    },\\n    \\\"P2_sub_goal_deletion\\\": {\\n      \\\"total\\\": 12,\\n      \\\"recovered\\\": 6,\\n      \\\"detected\\\": 0,\\n      \\\"recovery_rate\\\": 0.5,\\n      \\\"detection_rate\\\": 0.0\\n    }\\n  },\\n  \\\"by_task_type\\\": {\\n    \\\"look_at_obj_in_light\\\": {\\n      \\\"total\\\": 6,\\n      \\\"success\\\": 6,\\n      \\\"detected\\\": 0,\\n      \\\"rate\\\": 1.0\\n    },\\n    \\\"pick_and_place_simple\\\": {\\n      \\\"total\\\": 8,\\n      \\\"success\\\": 4,\\n      \\\"detected\\\": 0,\\n      \\\"rate\\\": 0.5\\n    },\\n    \\\"pick_clean_then_place_in_recep\\\": {\\n      \\\"total\\\": 11,\\n      \\\"success\\\": 6,\\n      \\\"detected\\\": 0,\\n      \\\"rate\\\": 0.545\\n    },\\n    \\\"pick_cool_then_place_in_recep\\\": {\\n      \\\"total\\\": 7,\\n      \\\"success\\\": 3,\\n      \\\"detected\\\": 0,\\n      \\\"rate\\\": 
…[truncated 8298 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_multiseed-stats_20260514T214124",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-14T21:44:14.285900+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/tax_error_inject_agent/eval_results/v4_random_recovery_eval.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_multiseed-stats_20260514T214124",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat /root/autodl-tmp/tax_error_inject_agent/eval_results/v4_random_recovery_eval.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-14T21:44:14.286440+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"model\\\": \\\"checkpoints/mini_random_sft_v4/v1-20260514-213104/checkpoint-3387\\\",\\n  \\\"model_variant\\\": \\\"random\\\",\\n  \\\"inject\\\": true,\\n  \\\"seed\\\": 42,\\n  \\\"total_episodes\\\": 47,\\n  \\\"success_rate\\\": 0.638,\\n  \\\"recovery_rate\\\": 0.638,\\n  \\\"detection_rate\\\": 0.0,\\n  \\\"timestamp\\\": \\\"2026-05-14T21:32:54.702364+00:00\\\",\\n  \\\"by_operator\\\": {\\n    \\\"C1_context_truncation\\\": {\\n      \\\"total\\\": 12,\\n      \\\"recovered\\\": 8,\\n      \\\"detected\\\": 0,\\n      \\\"recovery_rate\\\": 0.667,\\n      \\\"detection_rate\\\": 0.0\\n    },\\n    \\\"C4_observation_masking\\\": {\\n      \\\"total\\\": 11,\\n      \\\"recovered\\\": 6,\\n      \\\"detected\\\": 0,\\n      \\\"recovery_rate\\\": 0.545,\\n      \\\"detection_rate\\\": 0.0\\n    },\\n    \\\"P1_step_order_swap\\\": {\\n      \\\"total\\\": 12,\\n      \\\"recovered\\\": 9,\\n      \\\"detected\\\": 0,\\n      \\\"recovery_rate\\\": 0.75,\\n      \\\"detection_rate\\\": 0.0\\n    },\\n    \\\"P2_sub_goal_deletion\\\": {\\n      \\\"total\\\": 12,\\n      \\\"recovered\\\": 7,\\n      \\\"detected\\\": 0,\\n      \\\"recovery_rate\\\": 0.583,\\n      \\\"detection_rate\\\": 0.0\\n    }\\n  },\\n  \\\"by_task_type\\\": {\\n    \\\"look_at_obj_in_light\\\": {\\n      \\\"total\\\": 6,\\n      \\\"success\\\": 5,\\n      \\\"detected\\\": 0,\\n      \\\"rate\\\": 0.833\\n    },\\n    \\\"pick_and_place_simple\\\": {\\n      \\\"total\\\": 8,\\n      \\\"success\\\": 4,\\n      \\\"detected\\\": 0,\\n      \\\"rate\\\": 0.5\\n    },\\n    \\\"pick_clean_then_place_in_recep\\\": {\\n      \\\"total\\\": 11,\\n      \\\"success\\\": 6,\\n      \\\"detected\\\": 0,\\n      \\\"rate\\\": 0.545\\n    },\\n    \\\"pick_cool_then_place_in_recep\\\": {\\n      \\\"total\\\": 7,\\n      \\\"success\\\": 4,\\n      \\\"detected\\\": 0,\\n      \\\"rate\\\": 0.571\\n    },\\n    \\\"pick_heat_
…[truncated 8292 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_multiseed-stats_20260514T214124",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-14T21:44:14.286723+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/tax_error_inject_agent/eval_results/v4_taxei_recovery_eval_r2.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_multiseed-stats_20260514T214124",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat /root/autodl-tmp/tax_error_inject_agent/eval_results/v4_taxei_recovery_eval_r2.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-14T21:44:14.287255+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"model\\\": \\\"checkpoints/mini_taxei_sft_v4/v1-20260514-213102/checkpoint-3387\\\",\\n  \\\"model_variant\\\": \\\"taxei\\\",\\n  \\\"inject\\\": true,\\n  \\\"seed\\\": 42,\\n  \\\"total_episodes\\\": 47,\\n  \\\"success_rate\\\": 0.596,\\n  \\\"recovery_rate\\\": 0.596,\\n  \\\"detection_rate\\\": 0.0,\\n  \\\"timestamp\\\": \\\"2026-05-14T21:32:28.154456+00:00\\\",\\n  \\\"by_operator\\\": {\\n    \\\"C1_context_truncation\\\": {\\n      \\\"total\\\": 12,\\n      \\\"recovered\\\": 8,\\n      \\\"detected\\\": 0,\\n      \\\"recovery_rate\\\": 0.667,\\n      \\\"detection_rate\\\": 0.0\\n    },\\n    \\\"C4_observation_masking\\\": {\\n      \\\"total\\\": 11,\\n      \\\"recovered\\\": 7,\\n      \\\"detected\\\": 0,\\n      \\\"recovery_rate\\\": 0.636,\\n      \\\"detection_rate\\\": 0.0\\n    },\\n    \\\"P1_step_order_swap\\\": {\\n      \\\"total\\\": 12,\\n      \\\"recovered\\\": 7,\\n      \\\"detected\\\": 0,\\n      \\\"recovery_rate\\\": 0.583,\\n      \\\"detection_rate\\\": 0.0\\n    },\\n    \\\"P2_sub_goal_deletion\\\": {\\n      \\\"total\\\": 12,\\n      \\\"recovered\\\": 6,\\n      \\\"detected\\\": 0,\\n      \\\"recovery_rate\\\": 0.5,\\n      \\\"detection_rate\\\": 0.0\\n    }\\n  },\\n  \\\"by_task_type\\\": {\\n    \\\"look_at_obj_in_light\\\": {\\n      \\\"total\\\": 6,\\n      \\\"success\\\": 6,\\n      \\\"detected\\\": 0,\\n      \\\"rate\\\": 1.0\\n    },\\n    \\\"pick_and_place_simple\\\": {\\n      \\\"total\\\": 8,\\n      \\\"success\\\": 4,\\n      \\\"detected\\\": 0,\\n      \\\"rate\\\": 0.5\\n    },\\n    \\\"pick_clean_then_place_in_recep\\\": {\\n      \\\"total\\\": 11,\\n      \\\"success\\\": 6,\\n      \\\"detected\\\": 0,\\n      \\\"rate\\\": 0.545\\n    },\\n    \\\"pick_cool_then_place_in_recep\\\": {\\n      \\\"total\\\": 7,\\n      \\\"success\\\": 3,\\n      \\\"detected\\\": 0,\\n      \\\"rate\\\": 0.429\\n    },\\n    \\\"pick_heat_then_
…[truncated 8306 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_multiseed-stats_20260514T214124",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-14T21:44:14.287592+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090",
  "command": "cd /root/autodl-tmp/tax_error_inject_agent && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python scripts/analyze_multiseed.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_multiseed-stats_20260514T214124",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cd /root/autodl-tmp/tax_error_inject_agent && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python scripts/analyze_multiseed.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-14T21:44:14.287848+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Scanning /root/autodl-tmp/tax_error_inject_agent/eval_results ...\\n\\n======================================================================\\nMULTI-SEED ANALYSIS — D010 Phase 1\\n======================================================================\\n\\nVariant      Seeds     Mean      Std             95% CI      Min      Max\\n----------------------------------------------------------------------\\nvanilla          3    65.3%     3.3% [ 61.7%,  68.1%]    61.7%    68.1%\\n  seed=0     68.1%\\n  seed=123   66.0%\\n  seed=42    61.7%\\ntaxei            2    54.2%    10.5% [ 46.8%,  61.7%]    46.8%    61.7%\\n  seed=0     46.8%\\n  seed=42    61.7%\\nrandom           2    60.7%     7.6% [ 55.3%,  66.0%]    55.3%    66.0%\\n  seed=0     55.3%\\n  seed=42    66.0%\\n\\nComparison                    Diff    p-value   Sig?\\n-------------------------------------------------------\\ntaxei vs vanilla           -11.0%     0.0317      *\\ntaxei vs random             -6.4%     0.2436       \\nrandom vs vanilla            -4.6%     0.3042       \\n\\nTask Type                                  vanilla          taxei         random\\n-----------------------------------------------------------------------------\\nlook at obj in light                 83.3%±0.0%   91.6%±11.8%  91.6%±11.8%\\npick and place simple                66.7%±7.2%   50.0%±17.7%  50.0%      \\npick clean then place in recep       48.5%±5.2%   50.0%±6.4%   54.5%      \\npick cool then place in recep        57.1%        35.8%±10.1%  57.1%      \\npick heat then place in recep        83.3%±7.2%   68.8%±26.5%  68.8%±26.5%\\npick two obj and place               61.9%±8.3%   35.8%±10.1%  50.0%±10.0%\\n\\nResults saved to /root/autodl-tmp/tax_error_inject_agent/outputs/multiseed_analysis.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.81}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_multiseed-stats_20260514T214124",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-14T21:44:14.288186+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/multiseed_analysis_report.md",
  "content": "# TaxEI Multi-Seed Statistical Analysis Report\n\n**Date**: 2026-05-14  \n**Project**: tax_error_inject_agent  \n**Eval Set**: valid_unseen (47 tasks, 6 task types)  \n**Seeds**: Vanilla (42, 0, 123), TaxEI (42, 0), Random (42, 0)\n\n---\n\n## 1. Overall Clean Eval Results\n\n| Method | Seeds | Mean | Std | 95% CI | Min | Max |\n|--------|-------|------|-----|--------|-----|-----|\n| **Vanilla** | 3 | **65.3%** | 3.3% | [61.7%, 68.1%] | 61.7% | 68.1% |\n| **Random** | 2 | 60.7% | 7.6% | [55.3%, 66.0%] | 55.3% | 66.0% |\n| **TaxEI** | 2 | 54.2% | 10.5% | [46.8%, 61.7%] | 46.8% | 61.7% |\n\n### Per-Seed Breakdown\n\n| Method | seed=42 | seed=0 | seed=123 |\n|--------|---------|--------|----------|\n| Vanilla | 61.7% (29/47) | 68.1% (32/47) | 66.0% (31/47) |\n| TaxEI | 61.7% (29/47) | 46.8% (22/47) | — |\n| Random | 66.0% (31/47) | 55.3% (26/47) | — |\n\n---\n\n## 2. Pairwise Statistical Tests (Paired Permutation Test, n=10000)\n\n| Comparison | Diff | p-value | Significant? |\n|------------|------|---------|--------------|\n| TaxEI vs Vanilla | **-11.0%** | **0.0317** | **Yes (p<0.05)** |\n| TaxEI vs Random | -6.4% | 0.2436 | No |\n| Random vs Vanilla | -4.6% | 0.3042 | No |\n\n**Key finding**: TaxEI performs *significantly worse* than Vanilla (p=0.032). The taxonomy-guided error injection training not only fails to improve performance but actively degrades it. Random error injection also trends worse than Vanilla but the difference is not statistically significant.\n\n---\n\n## 3. Per-Task-Type Breakdown (Clean Eval)\n\n### Mean ± Std across seeds\n\n| Task Type | N | Vanilla | TaxEI | Random |\n|-----------|---|---------|-------|--------|\n| look_at_obj_in_light | 6 | 83.3% ± 0.0% | 91.7% ± 11.8% | 91.7% ± 11.8% |\n| pick_and_place_simple | 8 | 66.7% ± 7.2% | 50.0% ± 17.7% | 50.0% ± 0.0% |\n| pick_clean_then_place_in_recep | 11 | 48.5% ± 5.2% | 50.0% ± 6.4% | 54.5% ± 0.0% |\n| pick_cool_then_place_in_recep | 7 | 57.1% ± 0.0% | 35.8% ± 10.1% | 57.1% ± 0.0% |\n| pick_heat_then_place_in_recep | 8 | 83.3% ± 7.2% | 68.8% ± 26.5% | 68.8% ± 26.5% |\n| pick_two_obj_and_place | 7 | 61.9% ± 8.3% | 35.8% ± 10.1% | 50.0% ± 10.0% |\n\n### Per-Seed Detail\n\n#### Vanilla\n| Task Type | seed=42 | seed=0 | seed=123 |\n|-----------|---------|--------|----------|\n| look_at_obj_in_light | 83.3% (5/6) | 83.3% (5/6) | 83.3% (5/6) |\n| pick_and_place_simple | 62.5% (5/8) | 62.5% (5/8) | 75.0% (6/8) |\n| pick_clean_then_place_in_recep | 45.5% (5/11) | 54.5% (6/11) | 45.5% (5/11) |\n| pick_cool_then_place_in_recep | 57.1% (4/7) | 57.1% (4/7) | 57.1% (4/7) |\n| pick_heat_then_place_in_recep | 75.0% (6/8) | 87.5% (7/8) | 87.5% (7/8) |\n| pick_two_obj_and_place | 57.1% (4/7) | 71.4% (5/7) | 57.1% (4/7) |\n\n#### TaxEI\n| Task Type | seed=42 | seed=0 |\n|-----------|---------|--------|\n| look_at_obj_in_light | 100.0% (6/6) | 83.3% (5/6) |\n| pick_and_place_simple | 62.5% (5/8) | 37.5% (3/8) |\n| pick_clean_then_place_in_recep | 54.5% (6/11) | 45.5% (5/11) |\n| pick_cool_then_place_in_recep | 42.9% (3/7) | 28.6% (2/7) |\n| pick_heat_then_place_in_recep | 87.5% (7/8) | 50.0% (4/8) |\n| pick_two_obj_and_place | 28.6% (2/7) | 42.9% (3/7) |\n\n#### Random\n| Task Type | seed=42 | seed=0 |\n|-----------|---------|--------|\n| look_at_obj_in_light | 100.0% (6/6) | 83.3% (5/6) |\n| pick_and_place_simple | 50.0% (4/8) | 50.0% (4/8) |\n| pick_clean_then_place_in_recep | 54.5% (6/11) | 54.5% (6/11) |\n| pick_cool_then_place_in_recep | 57.1% (4/7) | 57.1% (4/7) |\n| pick_heat_then_place_in_recep | 87.5% (7/8) | 50.0% (4/8) |\n| pick_two_obj_and_place | 57.1% (4/7) | 42.9% (3/7) |\n\n---\n\n## 4. Recovery Eval Results (seed=42, injected errors)\n\n| Metric | Vanilla | TaxEI | Random |\n|--------|---------|-------|--------|\n| **Recovery Rate** | 61.7% (29/47) | 59.6% (28/47) | **63.8%** (30/47) |\n| **Detection Rate** | 0.0% (0/47) | 0.0% (0/47) | 0.0% (0/47) |\n\n### By Error Operator\n\n| Operator | N | Vanilla | TaxEI | Random |\n|----------|---|---------|-------|--------|\n| C1_context_truncation | 12 | **75.0%** | 66.7% | 66.7% |\n| C4_observation_masking | 11 | 54.5% | **63.6%** | 54.5% |\n| P1_step_order_swap | 12 | 58.3% | 58.3% | **75.0%** |\n| P2_sub_goal_deletion | 12 | 58.3% | 50.0% | 58.3% |\n\n### Recovery by Task Type (seed=42, injected)\n\n| Task Type | Vanilla | TaxEI | Random |\n|-----------|---------|-------|--------|\n| look_at_obj_in_light | 83.3% (5/6) | 100.0% (6/6) | 83.3% (5/6) |\n| pick_and_place_simple | 62.5% (5/8) | 50.0% (4/8) | 50.0% (4/8) |\n| pick_clean_then_place_in_recep | 45.5% (5/11) | 54.5% (6/11) | 54.5% (6/11) |\n| pick_cool_then_place_in_recep | 57.1% (4/7) | 42.9% (3/7) | 57.1% (4/7) |\n| pick_heat_then_place_in_recep | 75.0% (6/8) | 87.5% (7/8) | 87.5% (7/8) |\n| pick_two_obj_and_place | 57.1% (4/7) | 28.6% (2/7) | 57.1% (4/7) |\n\n---\n\n## 5. Key Findings Summary\n\n### 5.1 Core Hypothesis Rejected\n\n**TaxEI does not improve agent robustness.** Across all evaluation dimensions:\n\n1. **Clean performance**: TaxEI (54.2%) is significantly worse than Vanilla (65.3%), p=0.032. The 11 percentage point gap is the largest observed difference.\n\n2. **Error recovery**: TaxEI (59.6%) performs comparably or slightly worse than both Vanilla (61.7%) and Random (63.8%). No method achieves meaningful error detection (0% across the board).\n\n3. **High variance**: TaxEI shows the highest seed-to-seed variance (std=10.5%), suggesting the augmented training data introduces instability rather than robustness.\n\n### 5.2 Taxonomy Specificity Provides No Advantage\n\n- Random error injection (60.7%) outperforms taxonomy-guided injection (54.2%) on clean eval, though not significantly (p=0.24).\n- On recovery, Random (63.8%) marginally beats both TaxEI (59.6%) and Vanilla (61.7%).\n- The taxonomy's structured error types (context truncation, observation masking, step reordering, sub-goal deletion) confer no detectable advantage over random perturbation.\n\n### 5.3 Error Detection is Completely Non-functional\n\nAll three methods achieve exactly 0% error detection across all 47 tasks, all 4 error operators. The SFT training paradigm (regardless of augmentation strategy) does not produce agents capable of recognizing injected errors.\n\n### 5.4 Task-Type Patterns\n\n- **look_at_obj_in_light**: Easiest category across all methods (83-100%). High ceiling limits differentiation.\n- **pick_two_obj_and_place**: TaxEI suffers most here (28.6-42.9% vs Vanilla 57.1-71.4%). Multi-step coordination tasks are most vulnerable to training data corruption.\n- **pick_cool_then_place_in_recep**: TaxEI shows notable degradation (28.6-42.9% vs Vanilla's consistent 57.1%).\n- **pick_heat_then_place_in_recep**: High variance for both TaxEI and Random across seeds (50-87.5%).\n\n### 5.5 Implications for Negative Result Paper\n\n1. **Training data contamination > augmentation benefit**: Adding error-recovery demonstrations to training data degrades the base policy more than it teaches recovery skills.\n2. **SFT is insufficient for error awareness**: Behavioral cloning from demonstrations (even error-recovery demonstrations) does not produce metacognitive error detection abilities.\n3. **The \"exposure ≠ immunity\" finding**: Exposing the agent to structured errors during training does not build robustness; it corrupts the learned policy.\n4. **Seed sensitivity reveals fragility**: The high variance of TaxEI (±10.5%) compared to Vanilla (±3.3%) indicates that error-augmented training amplifies rather than dampens stochastic sensitivity.\n\n---\n\n## 6. Experimental Configuration\n\n| Parameter | Value |\n|-----------|-------|\n| Base model | Qwen2.5 (SFT) |\n| Environment | ALFWorld (TextWorld) |\n| Training samples (Vanilla) | 4,358 |\n| Training samples (TaxEI/Random) | 9,029 |\n| Eval set | valid_unseen, 47 tasks |\n| Max steps per episode | 50 |\n| Error operators | C1 (context truncation), C4 (observation masking), P1 (step reorder), P2 (sub-goal deletion) |\n| Seeds tested | Vanilla: {42, 0, 123}, TaxEI/Random: {42, 0} |\n| Statistical test | Paired permutation test (n=10,000) |\n| Confidence intervals | Bootstrap (n=1,000) |\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_multiseed-stats_20260514T214124",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/multiseed_analysis_report.md",
    "content": "# TaxEI Multi-Seed Statistical Analysis Report\n\n**Date**: 2026-05-14  \n**Project**: tax_error_inject_agent  \n**Eval Set**: valid_unseen (47 tasks, 6 task types)  \n**Seeds**: Vanilla (42, 0, 123), TaxEI (42, 0), Random (42, 0)\n\n---\n\n## 1. Overall Clean Eval Results\n\n| Method | Seeds | Mean | Std | 95% CI | Min | Max |\n|--------|-------|------|-----|--------|-----|-----|\n| **Vanilla** | 3 | **65.3%** | 3.3% | [61.7%, 68.1%] | 61.7% | 68.1% |\n| **Random** | 2 | 60.7% | 7.6% | [55.3%, 66.0%] | 55.3% | 66.0% |\n| **TaxEI** | 2 | 54.2% | 10.5% | [46.8%, 61.7%] | 46.8% | 61.7% |\n\n### Per-Seed Breakdown\n\n| Method | seed=42 | seed=0 | seed=123 |\n|--------|---------|--------|----------|\n| Vanilla | 61.7% (29/47) | 68.1% (32/47) | 66.0% (31/47) |\n| TaxEI | 61.7% (29/47) | 46.8% (22/47) | — |\n| Random | 66.0% (31/47) | 55.3% (26/47) | — |\n\n---\n\n## 2. Pairwise Statistical Tests (Paired Permutation Test, n=10000)\n\n| Comparison | Diff | p-value | Significant? |\n|------------|------|---------|--------------|\n| TaxEI vs Vanilla | **-11.0%** | **0.0317** | **Yes (p<0.05)** |\n| TaxEI vs Random | -6.4% | 0.2436 | No |\n| Random vs Vanilla | -4.6% | 0.3042 | No |\n\n**Key finding**: TaxEI performs *significantly worse* than Vanilla (p=0.032). The taxonomy-guided error injection training not only fails to improve performance but actively degrades it. Random error injection also trends worse than Vanilla but the difference is not statistically significant.\n\n---\n\n## 3. Per-Task-Type Breakdown (Clean Eval)\n\n### Mean ± Std across seeds\n\n| Task Type | N | Vanilla | TaxEI | Random |\n|-----------|---|---------|-------|--------|\n| look_at_obj_in_light | 6 | 83.3% ± 0.0% | 91.7% ± 11.8% | 91.7% ± 11.8% |\n| pick_and_place_simple | 8 | 66.7% ± 7.2% | 50.0% ± 17.7% | 50.0% ± 0.0% |\n| pick_clean_then_place_in_recep | 11 | 48.5% ± 5.2% | 50.0% ± 6.4% | 54.5% ± 0.0% |\n| pick_cool_then_place_in_recep | 7 | 57.1% ± 0.0% | 35.8% ± 10.1% | 57.1% ± 0.0% |\n| pick_heat_then_place_in_recep | 8 | 83.3% ± 7.2% | 68.8% ± 26.5% | 68.8% ± 26.5% |\n| pick_two_obj_and_place | 7 | 61.9% ± 8.3% | 35.8% ± 10.1% | 50.0% ± 10.0% |\n\n### Per-Seed Detail\n\n#### Vanilla\n| Task Type | seed=42 | seed=0 | seed=123 |\n|-----------|---------|--------|----------|\n| look_at_obj_in_light | 83.3% (5/6) | 83.3% (5/6) | 83.3% (5/6) |\n| pick_and_place_simple | 62.5% (5/8) | 62.5% (5/8) | 75.0% (6/8) |\n| pick_clean_then_place_in_recep | 45.5% (5/11) | 54.5% (6/11) | 45.5% (5/11) |\n| pick_cool_then_place_in_recep | 57.1% (4/7) | 57.1% (4/7) | 57.1% (4/7) |\n| pick_heat_then_place_in_recep | 75.0% (6/8) | 87.5% (7/8) | 87.5% (7/8) |\n| pick_two_obj_and_place | 57.1% (4/7) | 71.4% (5/7) | 57.1% (4/7) |\n\n#### TaxEI\n| Task Type | seed=42 | seed=0 |\n|-----------|---------|--------|\n| look_at_obj_in_light | 100.0% (6/6) | 83.3% (5/6) |\n| pick_and_place_simple | 62.5% (5/8) | 37.5% (3/8) |\n| pick_clean_then_place_in_recep | 54.5% (6/11) | 45.5% (5/11) |\n| pick_cool_then_place_in_recep | 42.9% (3/7) | 28.6% (2/7) |\n| pick_heat_then_place_in_recep | 87.5% (7/8) | 50.0% (4/8) |\n| pick_two_obj_and_place | 28.6% (2/7) | 42.9% (3/7) |\n\n#### Random\n| Task Type | seed=42 | seed=0 |\n|-----------|---------|--------|\n| look_at_obj_in_light | 100.0% (6/6) | 83.3% (5/6) |\n| pick_and_place_simple | 50.0% (4/8) | 50.0% (4/8) |\n| pick_clean_then_place_in_recep | 54.5% (6/11) | 54.5% (6/11) |\n| pick_cool_then_place_in_recep | 57.1% (4/7) | 57.1% (4/7) |\n| pick_heat_then_place_in_recep | 87.5% (7/8) | 50.0% (4/8) |\n| pick_two_obj_and_place | 57.1% (4/7) | 42.9% (3/7) |\n\n---\n\n## 4. Recovery Eval Results (seed=42, injected errors)\n\n| Metric | Vanilla | TaxEI | Random |\n|--------|---------|-------|--------|\n| **Recovery Rate** | 61.7% (29/47) | 59.6% (28/47) | **63.8%** (30/47) |\n| **Detection Rate** | 0.0% (0/47) | 0.0% (0/47) | 0.0% (0/47) |\n\n### By Error Operator\n\n| Operator | N | Vanilla | TaxEI | Random |\n|----------|---|---------|-------|--------|\n| C1_context_truncation | 12 | **75.0%** | 66.7% | 66.7% |\n| C4_observation_masking | 11 | 54.5% | **63.6%** | 54.5% |\n| P1_step_order_swap | 12 | 58.3% | 58.3% | **75.0%** |\n| P2_sub_goal_deletion | 12 | 58.3% | 50.0% | 58.3% |\n\n### Recovery by Task Type (seed=42, injected)\n\n| Task Type | Vanilla | TaxEI | Random |\n|-----------|---------|-------|--------|\n| look_at_obj_in_light | 83.3% (5/6) | 100.0% (6/6) | 83.3% (5/6) |\n| pick_and_place_simple | 62.5% (5/8) | 50.0% (4/8) | 50.0% (4/8) |\n| pick_clean_then_place_in_recep | 45.5% (5/11) | 54.5% (6/11) | 54.5% (6/11) |\n| pick_cool_then_place_in_recep | 57.1% (4/7) | 42.9% (3/7) | 57.1% (4/7) |\n| pick_heat_then_place_in_recep | 75.0% (6/8) | 87.5% (7/8) | 87.5% (7/8) |\n| pick_two_obj_and_place | 57.1% (4/7) | 28.6% (2/7) | 57.1% (4/7) |\n\n---\n\n## 5. Key Findings Summary\n\n### 5.1 Core Hypothesis Rejected\n\n**TaxEI does not improve agent robustness.** Across all evaluation dimensions:\n\n1. **Clean performance**: TaxEI (54.2%) is significantly worse than Vanilla (65.3%), p=0.032. The 11 percentage point gap is the largest observed difference.\n\n2. **Error recovery**: TaxEI (59.6%) performs comparably or slightly worse than both Vanilla (61.7%) and Random (63.8%). No method achieves meaningful error detection (0% across the board).\n\n3. **High variance**: TaxEI shows the highest seed-to-seed variance (std=10.5%), suggesting the augmented training data introduces instability rather than robustness.\n\n### 5.2 Taxonomy Specificity Provides No Advantage\n\n- Random error injection (60.7%) outperforms taxonomy-guided injection (54.2%) on clean eval, though not significantly (p=0.24).\n- On recovery, Random (63.8%) marginally beats both TaxEI (59.6%) and Vanilla (61.7%).\n- The taxonomy's structured error types (context truncation, observation masking, step reordering, sub-goal deletion) confer no detectable advantage over random perturbation.\n\n### 5.3 Error Detection is Completely Non-functional\n\nAll three methods achieve exactly 0% error detection across all 47 tasks, all 4 error operators. The SFT training paradigm (regardless of augmentation strategy) does not produce agents capable of recognizing injected errors.\n\n### 5.4 Task-Type Patterns\n\n- **look_at_obj_in_light**: Easiest category across all methods (83-100%). High ceiling limits differentiation.\n- **pick_two_obj_and_place**: TaxEI suffers most here (28.6-42.9% vs Vanilla 57.1-71.4%). Multi-step coordination tasks are most vulnerable to training data corruption.\n- **pick_cool_then_place_in_recep**: TaxEI shows notable degradation (28.6-42.9% vs Vanilla's consistent 57.1%).\n- **pick_heat_then_place_in_recep**: High variance for both TaxEI and Random across seeds (50-87.5%).\n\n### 5.5 Implications for Negative Result Paper\n\n1. **Training data contamination > augmentation benefit**: Adding error-recovery demonstrations to training data degrades the base policy more than it teaches recovery skills.\n2. **SFT is insufficient for error awareness**: Behavioral cloning from demonstrations (even error-recovery demonstrations) does not produce metacognitive error detection abilities.\n3. **The \"exposure ≠ immunity\" finding**: Exposing the agent to structured errors during training does not build robustness; it corrupts the learned policy.\n4. **Seed sensitivity reveals fragility**: The high variance of TaxEI (±10.5%) compared to Vanilla (±3.3%) indicates that error-augmented training amplifies rather than dampens stochastic sensitivity.\n\n---\n\n## 6. Experimental Configuration\n\n| Parameter | Value |\n|-----------|-------|\n| Base model | Qwen2.5 (SFT) |\n| Environment | ALFWorld (TextWorld) |\n| Training samples (Vanilla) | 4,358 |\n| Training samples (TaxEI/Random) | 9,029 |\n| Eval set | valid_unseen, 47 tasks |\n| Max steps per episode | 50 |\n| Error operators | C1 (context truncation), C4 (observation masking), P1 (step reorder), P2 (sub-goal deletion) |\n| Seeds tested | Vanilla: {42, 0, 123}, TaxEI/Random: {42, 0} |\n| Statistical test | Paired permutation test (n=10,000) |\n| Confidence intervals | Bootstrap (n=1,000) |\n"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-14T21:44:14.288576+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/multiseed_analysis_report.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_multiseed-stats_20260514T214124",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-14T21:44:14.288820+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "Multi-Seed Statistical Analysis Report",
  "type": "report",
  "description": "Complete multi-seed statistical analysis: clean eval (3 methods × 2-3 seeds), recovery eval (by operator/task type), pairwise permutation tests, per-task-type breakdowns. Key finding: TaxEI significantly worse than Vanilla (p=0.032), 0% detection rate across all methods.",
  "project": "tax_error_inject_agent",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/multiseed_analysis_report.md",
  "tags": "['statistics', 'multiseed', 'negative-result', 'final-analysis']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_multiseed-stats_20260514T214124",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "Multi-Seed Statistical Analysis Report",
    "type": "report",
    "description": "Complete multi-seed statistical analysis: clean eval (3 methods × 2-3 seeds), recovery eval (by operator/task type), pairwise permutation tests, per-task-type breakdowns. Key finding: TaxEI significantly worse than Vanilla (p=0.032), 0% detection rate across all methods.",
    "project": "tax_error_inject_agent",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/multiseed_analysis_report.md",
    "tags": "['statistics', 'multiseed', 'negative-result', 'final-analysis']"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-14T21:44:14.289100+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260514_927896\", \"name\": \"Multi-Seed Statistical Analysis Report\", \"type\": \"report\", \"description\": \"Complete multi-seed statistical analysis: clean eval (3 methods × 2-3 seeds), recovery eval (by operator/task type), pairwise permutation tests, per-task-type breakdowns. Key finding: TaxEI significantly worse than Vanilla (p=0.032), 0% detection rate across all methods.\", \"path\": \"projects/tax_error_inject_agent/artifacts/_project/report/multiseed_analysis_report.md\", \"url\": null, \"project\": \"tax_error_inject_agent\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-14T21:44:04.143441+00:00\", \"tags\": [\"statistics\", \"multiseed\", \"negative-result\", \"final-analysis\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_multiseed-stats_20260514T214124",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 41 · 2026-05-14T21:44:14.289376+00:00_

报告已生成并注册。核心数据摘要：

**Clean Eval（跨种子）**
- Vanilla: 65.3% ± 3.3% （最优）
- Random: 60.7% ± 7.6%
- TaxEI: 54.2% ± 10.5% （最差）

**统计检验**
- TaxEI vs Vanilla: **-11.0%, p=0.032**（显著更差）
- TaxEI vs Random: -6.4%, p=0.24（不显著）
- Random vs Vanilla: -4.6%, p=0.30（不显著）

**Recovery Eval（seed=42）**
- 三种方法恢复率相近（59.6%-63.8%），**检测率全部为 0%**

**对 negative paper 的支撑**：TaxEI 在所有维度被否定——不仅没有提升鲁棒性，还显著损害了基础性能（p<0.05）。高方差（±10.5% vs ±3.3%）表明错误注入训练增加了不稳定性。完整报告在 `artifacts/multiseed_analysis_report.md`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_multiseed-stats_20260514T214124"
}
```

</details>

---
