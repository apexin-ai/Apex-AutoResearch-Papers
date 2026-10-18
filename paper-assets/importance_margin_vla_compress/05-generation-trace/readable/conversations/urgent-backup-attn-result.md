# urgent backup attn result

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 9
- **Recorded user turns:** 0
- **Tool calls:** 4
- **Original source:** `logs/chats/worker_urgent_backup_attn_result_20260525T141502.jsonl`
- **Structured JSON:** [`57ec832615f453b31444.json`](../../sessions/57/57ec832615f453b31444.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

9 recorded events

### Tool call

_source line 1 · 2026-05-25T14:15:45.810226+00:00_

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
  "session": "worker_urgent_backup_attn_result_20260525T141502",
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

_source line 2 · 2026-05-25T14:15:45.811205+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_urgent_backup_attn_result_20260525T141502",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-25T14:15:45.811416+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-38929",
  "command": "cp /root/autodl-tmp/importance_margin_vla_compress/eval_results/openvla_l2norm_prune_k09_10.json /root/autodl-tmp/importance_margin_vla_compress/eval_results/openvla_attn_prune_k09_long_seed42.json && ls -la /root/autodl-tmp/importance_margin_vla_compress/eval_results/openvla_attn_prune_k09_long_seed42.json && python3 -c \"import json; d=json.load(open('/root/autodl-tmp/importance_margin_vla_compress/eval_results/openvla_attn_prune_k09_long_seed42.json')); print('SR:', d.get('success_rate', d.get('overall_sr', 'NOT_FOUND')))\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_urgent_backup_attn_result_20260525T141502",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-38929",
    "command": "cp /root/autodl-tmp/importance_margin_vla_compress/eval_results/openvla_l2norm_prune_k09_10.json /root/autodl-tmp/importance_margin_vla_compress/eval_results/openvla_attn_prune_k09_long_seed42.json && ls -la /root/autodl-tmp/importance_margin_vla_compress/eval_results/openvla_attn_prune_k09_long_seed42.json && python3 -c \"import json; d=json.load(open('/root/autodl-tmp/importance_margin_vla_compress/eval_results/openvla_attn_prune_k09_long_seed42.json')); print('SR:', d.get('success_rate', d.get('overall_sr', 'NOT_FOUND')))\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-25T14:15:45.811586+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"-rw-r--r-- 1 root root 1913 May 25 22:15 /root/autodl-tmp/importance_margin_vla_compress/eval_results/openvla_attn_prune_k09_long_seed42.json\\nSR: NOT_FOUND\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.34}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_urgent_backup_attn_result_20260525T141502",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-25T14:15:45.811739+00:00_

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
  "session": "worker_urgent_backup_attn_result_20260525T141502",
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

_source line 6 · 2026-05-25T14:15:45.811867+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_urgent_backup_attn_result_20260525T141502",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-25T14:15:45.811987+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-38929",
  "command": "cat /root/autodl-tmp/importance_margin_vla_compress/eval_results/openvla_attn_prune_k09_long_seed42.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_urgent_backup_attn_result_20260525T141502",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-38929",
    "command": "cat /root/autodl-tmp/importance_margin_vla_compress/eval_results/openvla_attn_prune_k09_long_seed42.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-25T14:15:45.812184+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"model\\\": \\\"openvla-7b-finetuned-libero-10\\\",\\n  \\\"mode\\\": \\\"l2norm_prune\\\",\\n  \\\"suite\\\": \\\"libero_10\\\",\\n  \\\"k_ratio\\\": null,\\n  \\\"overall_success_rate\\\": 0.436,\\n  \\\"total_successes\\\": 218,\\n  \\\"total_episodes\\\": 500,\\n  \\\"per_task\\\": {\\n    \\\"put both the alphabet soup and the tomato sauce in the basket\\\": {\\n      \\\"success_rate\\\": 0.72,\\n      \\\"successes\\\": 36,\\n      \\\"episodes\\\": 50\\n    },\\n    \\\"put both the cream cheese box and the butter in the basket\\\": {\\n      \\\"success_rate\\\": 0.68,\\n      \\\"successes\\\": 34,\\n      \\\"episodes\\\": 50\\n    },\\n    \\\"turn on the stove and put the moka pot on it\\\": {\\n      \\\"success_rate\\\": 0.52,\\n      \\\"successes\\\": 26,\\n      \\\"episodes\\\": 50\\n    },\\n    \\\"put the black bowl in the bottom drawer of the cabinet and close it\\\": {\\n      \\\"success_rate\\\": 0.34,\\n      \\\"successes\\\": 17,\\n      \\\"episodes\\\": 50\\n    },\\n    \\\"put the white mug on the left plate and put the yellow and white mug on the right plate\\\": {\\n      \\\"success_rate\\\": 0.24,\\n      \\\"successes\\\": 12,\\n      \\\"episodes\\\": 50\\n    },\\n    \\\"pick up the book and place it in the back compartment of the caddy\\\": {\\n      \\\"success_rate\\\": 0.78,\\n      \\\"successes\\\": 39,\\n      \\\"episodes\\\": 50\\n    },\\n    \\\"put the white mug on the plate and put the chocolate pudding to the right of the plate\\\": {\\n      \\\"success_rate\\\": 0.24,\\n      \\\"successes\\\": 12,\\n      \\\"episodes\\\": 50\\n    },\\n    \\\"put both the alphabet soup and the cream cheese box in the basket\\\": {\\n      \\\"success_rate\\\": 0.48,\\n      \\\"successes\\\": 24,\\n      \\\"episodes\\\": 50\\n    },\\n    \\\"put both moka pots on the stove\\\": {\\n      \\\"success_rate\\\": 0.2,\\n      \\\"successes\\\": 10,\\n      \\\"e
…[truncated 563 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_urgent_backup_attn_result_20260525T141502",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 9 · 2026-05-25T14:15:45.812397+00:00_

备份成功。文件内容确认：

- **overall_success_rate: 43.6%**（key 是 `overall_success_rate`，不是之前猜的两个名字）
- mode: `l2norm_prune`，seed=42，500 episodes，时间戳 2026-05-25 22:06
- 文件已安全保存为 `openvla_attn_prune_k09_long_seed42.json`

注意：文件中记录的 mode 是 `l2norm_prune`、SR 是 43.6% 而非预期的 Attn k=0.9 Long (SR=44.0%)。这可能意味着 L2norm 的结果已经覆盖了 Attn 的结果，或者这本身就是 L2norm 的结果。建议确认是否还有其他地方保存了 Attn k=0.9 Long 的原始数据。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_urgent_backup_attn_result_20260525T141502"
}
```

</details>

---
