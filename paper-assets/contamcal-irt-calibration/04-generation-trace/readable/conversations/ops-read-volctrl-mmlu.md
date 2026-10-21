# ops read volctrl mmlu

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 9
- **Recorded user turns:** 0
- **Tool calls:** 4
- **Original source:** `logs/chats/worker_ops_read-volctrl-mmlu_20260523T064208.jsonl`
- **Structured JSON:** [`cceb12d088f00db49a3c.json`](../../sessions/cc/cceb12d088f00db49a3c.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

9 recorded events

### Tool call

_source line 1 · 2026-05-23T06:43:02.597771+00:00_

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
  "session": "worker_ops_read-volctrl-mmlu_20260523T064208",
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

_source line 2 · 2026-05-23T06:43:02.598095+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_read-volctrl-mmlu_20260523T064208",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-23T06:43:02.598258+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "ls -la /root/autodl-tmp/exp001/eval_results/Falcon3-7B-Base_volume_control_s42_aligned/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_read-volctrl-mmlu_20260523T064208",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "ls -la /root/autodl-tmp/exp001/eval_results/Falcon3-7B-Base_volume_control_s42_aligned/"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-23T06:43:02.598434+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 1420\\ndrwxr-xr-x   2 root root      77 May 23 14:27 .\\ndrwxr-xr-x 107 root root    8192 May 23 14:09 ..\\n-rw-r--r--   1 root root  109377 May 23 14:27 arc_challenge_results.json\\n-rw-r--r--   1 root root 1328519 May 23 14:22 mmlu_results.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.16}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_read-volctrl-mmlu_20260523T064208",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-23T06:43:02.598567+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "head -100 /root/autodl-tmp/exp001/eval_results/Falcon3-7B-Base_volume_control_s42_aligned/mmlu_results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_read-volctrl-mmlu_20260523T064208",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "head -100 /root/autodl-tmp/exp001/eval_results/Falcon3-7B-Base_volume_control_s42_aligned/mmlu_results.json"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-23T06:43:02.598770+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"benchmark\\\": \\\"mmlu\\\",\\n  \\\"accuracy\\\": 0.6066799601196411,\\n  \\\"correct\\\": 8519,\\n  \\\"total\\\": 14042,\\n  \\\"per_item\\\": [\\n    {\\n      \\\"index\\\": 0,\\n      \\\"correct\\\": false,\\n      \\\"pred\\\": \\\"D\\\",\\n      \\\"gold\\\": \\\"B\\\"\\n    },\\n    {\\n      \\\"index\\\": 1,\\n      \\\"correct\\\": false,\\n      \\\"pred\\\": \\\"A\\\",\\n      \\\"gold\\\": \\\"C\\\"\\n    },\\n    {\\n      \\\"index\\\": 2,\\n      \\\"correct\\\": false,\\n      \\\"pred\\\": \\\"C\\\",\\n      \\\"gold\\\": \\\"D\\\"\\n    },\\n    {\\n      \\\"index\\\": 3,\\n      \\\"correct\\\": false,\\n      \\\"pred\\\": \\\"A\\\",\\n      \\\"gold\\\": \\\"B\\\"\\n    },\\n    {\\n      \\\"index\\\": 4,\\n      \\\"correct\\\": true,\\n      \\\"pred\\\": \\\"B\\\",\\n      \\\"gold\\\": \\\"B\\\"\\n    },\\n    {\\n      \\\"index\\\": 5,\\n      \\\"correct\\\": true,\\n      \\\"pred\\\": \\\"A\\\",\\n      \\\"gold\\\": \\\"A\\\"\\n    },\\n    {\\n      \\\"index\\\": 6,\\n      \\\"correct\\\": true,\\n      \\\"pred\\\": \\\"A\\\",\\n      \\\"gold\\\": \\\"A\\\"\\n    },\\n    {\\n      \\\"index\\\": 7,\\n      \\\"correct\\\": false,\\n      \\\"pred\\\": \\\"A\\\",\\n      \\\"gold\\\": \\\"D\\\"\\n    },\\n    {\\n      \\\"index\\\": 8,\\n      \\\"correct\\\": true,\\n      \\\"pred\\\": \\\"B\\\",\\n      \\\"gold\\\": \\\"B\\\"\\n    },\\n    {\\n      \\\"index\\\": 9,\\n      \\\"correct\\\": true,\\n      \\\"pred\\\": \\\"C\\\",\\n      \\\"gold\\\": \\\"C\\\"\\n    },\\n    {\\n      \\\"index\\\": 10,\\n      \\\"correct\\\": false,\\n      \\\"pred\\\": \\\"A\\\",\\n      \\\"gold\\\": \\\"C\\\"\\n    },\\n    {\\n      \\\"index\\\": 11,\\n      \\\"correct\\\": true,\\n      \\\"pred\\\": \\\"C\\\",\\n      \\\"gold\\\": \\\"C\\\"\\n    },\\n    {\\n      \\\"index\\\": 12,\\n      \\\"correct\\\": false,\\n      \\\"pred\\\": \\\"C\\\",\\n      \\
…[truncated 518 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_read-volctrl-mmlu_20260523T064208",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-23T06:43:02.598975+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_falcon3_volctrl_s42",
  "field": "metrics",
  "value": "{'mmlu_5shot': 60.67, 'arc_challenge_25shot': 83.28}",
  "project": "contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_read-volctrl-mmlu_20260523T064208",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_falcon3_volctrl_s42",
    "field": "metrics",
    "value": "{'mmlu_5shot': 60.67, 'arc_challenge_25shot': 83.28}",
    "project": "contamcal-irt-calibration"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-23T06:43:02.599135+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_falcon3_volctrl_s42\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T06:06:48.118Z\", \"updated_at\": \"2026-05-23T06:42:55.180Z\", \"hypothesis\": \"Volume-matched control eval: if Falcon3 d100 Benefit (+4.19pp) is driven by data quantity rather than contamination content, volume-matched control should show similar gains. Comparing d000/volctrl/d100 isolates the contamination effect.\", \"parent\": \"sft_falcon3_7b_volume_control\", \"spec\": {\"command\": \"lm_eval MMLU+ARC+GSM8K on Falcon3-7B volume_control adapter\", \"server\": \"cqa1-21977\", \"data_path\": \"volume_control.jsonl\", \"data_count\": 66533, \"model_name\": \"Falcon3-7B-Base\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Falcon3-7B-Base_volume_control/lora_adapter/\", \"eval_data\": \"MMLU+ARC+GSM8K\"}, \"metrics\": {\"mmlu_5shot\": 60.67, \"arc_challenge_25shot\": 83.28}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.6988}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_read-volctrl-mmlu_20260523T064208",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 9 · 2026-05-23T06:43:02.599307+00:00_

Registry 已更新。

**MMLU 5-shot = 60.67%**

| 条件 | MMLU | vs d000 |
|------|------|---------|
| d000 (clean baseline) | 58.77% | — |
| volume control (等量非污染数据) | 60.67% | +1.90pp |
| d100 (100%污染数据) | 62.96% | +4.19pp |

volume control 贡献了 d100 总增益的约 45% (1.90/4.19)，剩余 ~55% (+2.29pp) 可归因于污染内容本身。Quantity confound 存在但只能解释不到一半的效应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_ops_read-volctrl-mmlu_20260523T064208"
}
```

</details>

---
