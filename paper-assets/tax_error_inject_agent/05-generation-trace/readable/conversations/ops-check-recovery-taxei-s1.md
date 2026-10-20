# ops check recovery taxei s1

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 0
- **Tool calls:** 6
- **Original source:** `logs/chats/worker_ops_check-recovery-taxei-s1_20260516T091606.jsonl`
- **Structured JSON:** [`f98dd5de8bb8827b70f6.json`](../../sessions/f9/f98dd5de8bb8827b70f6.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

13 recorded events

### Tool call

_source line 1 · 2026-05-16T09:16:50.141050+00:00_

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
  "session": "worker_ops_check-recovery-taxei-s1_20260516T091606",
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

_source line 2 · 2026-05-16T09:16:50.141480+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_check-recovery-taxei-s1_20260516T091606",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-16T09:16:50.141758+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "tmux list-sessions 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_check-recovery-taxei-s1_20260516T091606",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "tmux list-sessions 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-16T09:16:50.141963+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_check-recovery-taxei-s1_20260516T091606",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-16T09:16:50.142103+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "ls -la /root/autodl-tmp/tax_error_inject_agent/eval_results/v4_taxei_recovery_eval_s1.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_check-recovery-taxei-s1_20260516T091606",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "ls -la /root/autodl-tmp/tax_error_inject_agent/eval_results/v4_taxei_recovery_eval_s1.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-16T09:16:50.142237+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"-rw-r--r-- 1 root root 493738 May 16 17:05 /root/autodl-tmp/tax_error_inject_agent/eval_results/v4_taxei_recovery_eval_s1.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.06}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_check-recovery-taxei-s1_20260516T091606",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-16T09:16:50.142381+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "python3 -c \"import json; d=json.load(open('/root/autodl-tmp/tax_error_inject_agent/eval_results/v4_taxei_recovery_eval_s1.json')); [print(f'  {k}: {v}') for k,v in d.items() if k!='episodes']\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_check-recovery-taxei-s1_20260516T091606",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "python3 -c \"import json; d=json.load(open('/root/autodl-tmp/tax_error_inject_agent/eval_results/v4_taxei_recovery_eval_s1.json')); [print(f'  {k}: {v}') for k,v in d.items() if k!='episodes']\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-16T09:16:50.142508+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_check-recovery-taxei-s1_20260516T091606",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-16T09:16:50.142689+00:00_

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
  "session": "worker_ops_check-recovery-taxei-s1_20260516T091606",
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

_source line 10 · 2026-05-16T09:16:50.142815+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_check-recovery-taxei-s1_20260516T091606",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-16T09:16:50.142952+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090",
  "command": "python3 -c \"\nimport json\nd=json.load(open('/root/autodl-tmp/tax_error_inject_agent/eval_results/v4_taxei_recovery_eval_s1.json'))\nfor k,v in d.items():\n    if k!='episodes':\n        print(f'  {k}: {v}')\n\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_check-recovery-taxei-s1_20260516T091606",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090",
    "command": "python3 -c \"\nimport json\nd=json.load(open('/root/autodl-tmp/tax_error_inject_agent/eval_results/v4_taxei_recovery_eval_s1.json'))\nfor k,v in d.items():\n    if k!='episodes':\n        print(f'  {k}: {v}')\n\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-16T09:16:50.143103+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"  model: /root/autodl-tmp/tax_error_inject_agent/checkpoints/mini_taxei_sft_v4_seed1/v0-20260515-214035/checkpoint-3387\\n  model_variant: taxei\\n  inject: True\\n  seed: 42\\n  total_episodes: 47\\n  success_rate: 0.617\\n  recovery_rate: 0.617\\n  detection_rate: 0.0\\n  timestamp: 2026-05-16T09:05:39.223532+00:00\\n  by_operator: {'C1_context_truncation': {'total': 12, 'recovered': 9, 'detected': 0, 'recovery_rate': 0.75, 'detection_rate': 0.0}, 'C4_observation_masking': {'total': 11, 'recovered': 7, 'detected': 0, 'recovery_rate': 0.636, 'detection_rate': 0.0}, 'P1_step_order_swap': {'total': 12, 'recovered': 7, 'detected': 0, 'recovery_rate': 0.583, 'detection_rate': 0.0}, 'P2_sub_goal_deletion': {'total': 12, 'recovered': 6, 'detected': 0, 'recovery_rate': 0.5, 'detection_rate': 0.0}}\\n  by_task_type: {'look_at_obj_in_light': {'total': 6, 'success': 5, 'detected': 0, 'rate': 0.833}, 'pick_and_place_simple': {'total': 8, 'success': 4, 'detected': 0, 'rate': 0.5}, 'pick_clean_then_place_in_recep': {'total': 11, 'success': 5, 'detected': 0, 'rate': 0.455}, 'pick_cool_then_place_in_recep': {'total': 7, 'success': 3, 'detected': 0, 'rate': 0.429}, 'pick_heat_then_place_in_recep': {'total': 8, 'success': 7, 'detected': 0, 'rate': 0.875}, 'pick_two_obj_and_place': {'total': 7, 'success': 5, 'detected': 0, 'rate': 0.714}}\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.33}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_check-recovery-taxei-s1_20260516T091606",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-16T09:16:50.143323+00:00_

Eval 已完成。结果：

**=== Recovery TaxEI s1 ===**

| 指标 | 值 |
|------|-----|
| **recovery_rate** | **0.617** (29/47) |
| **detection_rate** | **0.0** (0/47) |
| seed | 42 |
| model | checkpoint-3387 (v4 seed1) |

**Per-operator recovery rate:**

| Operator | Total | Recovered | Rate |
|----------|-------|-----------|------|
| C1_context_truncation | 12 | 9 | **0.750** |
| C4_observation_masking | 11 | 7 | **0.636** |
| P1_step_order_swap | 12 | 7 | **0.583** |
| P2_sub_goal_deletion | 12 | 6 | **0.500** |

**Per-task recovery rate:**

| Task Type | Total | Rate |
|-----------|-------|------|
| pick_heat_then_place | 8 | 0.875 |
| look_at_obj_in_light | 6 | 0.833 |
| pick_two_obj_and_place | 7 | 0.714 |
| pick_and_place_simple | 8 | 0.500 |
| pick_clean_then_place | 11 | 0.455 |
| pick_cool_then_place | 7 | 0.429 |

detection_rate 为 0 — 模型从未主动检测到错误注入，但仍有 61.7% 的 episode 通过隐式恢复完成了任务。C1（上下文截断）最容易恢复，P2（子目标删除）最难。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_ops_check-recovery-taxei-s1_20260516T091606"
}
```

</details>

---
