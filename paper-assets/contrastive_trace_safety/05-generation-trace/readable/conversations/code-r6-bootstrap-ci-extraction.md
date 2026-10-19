# code r6 bootstrap ci extraction

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 7
- **Recorded user turns:** 0
- **Tool calls:** 3
- **Original source:** `logs/chats/worker_code_r6_bootstrap_ci_extraction_20260518T024936.jsonl`
- **Structured JSON:** [`25cd039a14e9dbcce1da.json`](../../sessions/25/25cd039a14e9dbcce1da.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

7 recorded events

### Tool call

_source line 1 · 2026-05-18T02:50:10.682076+00:00_

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
  "session": "worker_code_r6_bootstrap_ci_extraction_20260518T024936",
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

_source line 2 · 2026-05-18T02:50:10.682420+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_r6_bootstrap_ci_extraction_20260518T024936",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-18T02:50:10.682596+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-rtx6000",
  "command": "cd /root/autodl-tmp/contrastive_trace_safety && cat artifacts/exp_r3_bootstrap_10k/results.json | python3 -m json.tool | head -200",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_r6_bootstrap_ci_extraction_20260518T024936",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-rtx6000",
    "command": "cd /root/autodl-tmp/contrastive_trace_safety && cat artifacts/exp_r3_bootstrap_10k/results.json | python3 -m json.tool | head -200",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-18T02:50:10.682898+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"bash: line 1: python3: command not found\\n\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.87}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_r6_bootstrap_ci_extraction_20260518T024936",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-18T02:50:10.683256+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-rtx6000",
  "command": "cd /root/autodl-tmp/contrastive_trace_safety && source /root/miniconda3/bin/activate && cat artifacts/exp_r3_bootstrap_10k/results.json | python3 -m json.tool | head -200",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_r6_bootstrap_ci_extraction_20260518T024936",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-rtx6000",
    "command": "cd /root/autodl-tmp/contrastive_trace_safety && source /root/miniconda3/bin/activate && cat artifacts/exp_r3_bootstrap_10k/results.json | python3 -m json.tool | head -200",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-18T02:50:10.683558+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n    \\\"n_resamples\\\": 10000,\\n    \\\"seed\\\": 42,\\n    \\\"elapsed_seconds\\\": 243.6,\\n    \\\"tests\\\": [\\n        {\\n            \\\"model\\\": \\\"r1_8b\\\",\\n            \\\"metric\\\": \\\"bal_acc\\\",\\n            \\\"delta\\\": 0.17958910090938204,\\n            \\\"ci_95\\\": [\\n                0.11683529774041068,\\n                0.24201725735307214\\n            ],\\n            \\\"p_old_1k\\\": 0.001,\\n            \\\"p_new_10k\\\": 0.0,\\n            \\\"holm_rank\\\": 1,\\n            \\\"holm_threshold\\\": 0.004167,\\n            \\\"pass\\\": true\\n        },\\n        {\\n            \\\"model\\\": \\\"r1_8b\\\",\\n            \\\"metric\\\": \\\"precision\\\",\\n            \\\"delta\\\": 0.27858808251186934,\\n            \\\"ci_95\\\": [\\n                0.18540519846555728,\\n                0.37810872241201826\\n            ],\\n            \\\"p_old_1k\\\": 0.001,\\n            \\\"p_new_10k\\\": 0.0,\\n            \\\"holm_rank\\\": 2,\\n            \\\"holm_threshold\\\": 0.004545,\\n            \\\"pass\\\": true\\n        },\\n        {\\n            \\\"model\\\": \\\"r1_8b\\\",\\n            \\\"metric\\\": \\\"pre_cp_fpr\\\",\\n            \\\"delta\\\": -0.12545892180728604,\\n            \\\"ci_95\\\": [\\n                -0.1795174778341794,\\n                -0.07410375559111361\\n            ],\\n            \\\"p_old_1k\\\": 0.044,\\n            \\\"p_new_10k\\\": 0.0,\\n            \\\"holm_rank\\\": 3,\\n            \\\"holm_threshold\\\": 0.005,\\n            \\\"pass\\\": true\\n        },\\n        {\\n            \\\"model\\\": \\\"ot_7b\\\",\\n            \\\"metric\\\": \\\"precision\\\",\\n            \\\"delta\\\": 0.21894260796680878,\\n            \\\"ci_95\\\": [\\n                0.14414931578743703,\\n                0.29612074801930044\\n            ],\\n            \\\"p_old_1k\\\": 0.001,\\n            \\\"p_new_10k\\\": 0.0,\\n     
…[truncated 5178 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_r6_bootstrap_ci_extraction_20260518T024936",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-18T02:50:10.683889+00:00_

JSON 已有 percentile-based 95% CI。提取 precision metric 结果：

| Model | Precision Δ (HS − Text) | 95% CI lower | 95% CI upper | p-value |
|---------|------------------------|-------------|-------------|---------|
| R1-8B | +0.2786 | +0.1854 | +0.3781 | <0.0001 |
| OT-7B | +0.2189 | +0.1441 | +0.2961 | <0.0001 |
| QwQ-32B | +0.2349 | +0.1287 | +0.3510 | <0.0001 |
| R1-32B | +0.1544 | +0.0867 | +0.2262 | <0.0001 |

**R1-32B 分析**: delta 最小 (+0.154)，但 CI 下界 +0.087，远离 0，统计显著性没有问题。CI 宽度 0.140，与其他模型相当。

补充信息：
- 所有 12 项 Holm-Bonferroni 校正测试通过 (12/12 pass)
- p 值均为 0.0（10000 次 resampling 中零次出现反向结果）
- QwQ-32B 的 CI 最宽（0.222），R1-32B 次之（0.140），OT-7B 最窄（0.152）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_code_r6_bootstrap_ci_extraction_20260518T024936"
}
```

</details>

---
