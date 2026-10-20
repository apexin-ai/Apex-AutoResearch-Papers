# analysis eval grpo g8 bf16 results

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 0
- **Tool calls:** 5
- **Original source:** `logs/chats/worker_analysis_eval_grpo_g8_bf16_results_20260515T175633.jsonl`
- **Structured JSON:** [`4c61b5fec62bdcc0b32e.json`](../../sessions/4c/4c61b5fec62bdcc0b32e.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

11 recorded events

### Tool call

_source line 1 · 2026-05-15T17:57:12.274916+00:00_

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
  "session": "worker_analysis_eval_grpo_g8_bf16_results_20260515T175633",
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

_source line 2 · 2026-05-15T17:57:12.275289+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_grpo_g8_bf16_results_20260515T175633",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T17:57:12.275484+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "tail -100 ~/runs/faith-evidence-ie/eval_grpo_g8_bf16.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_eval_grpo_g8_bf16_results_20260515T175633",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "tail -100 ~/runs/faith-evidence-ie/eval_grpo_g8_bf16.log",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-15T17:57:12.275624+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "tmux list-sessions 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_eval_grpo_g8_bf16_results_20260515T175633",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "tmux list-sessions 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-15T17:57:12.275855+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-15 23:45:45,711 INFO Loaded 37785 training triples for Ign-F1\\n2026-05-15 23:45:45,851 INFO Metrics → /root/autodl-tmp/eval_results/grpo_g8_bf16/checkpoint-80/metrics.json\\n2026-05-15 23:45:45,980 INFO Predictions → /root/autodl-tmp/eval_results/grpo_g8_bf16/checkpoint-80/predictions.json\\n\\n==================================================\\n  F1:          0.4456\\n  Ign-F1:      0.4456\\n  Evi-F1:      0.8034\\n  EDCR:        0.6409\\n  Format OK:   984/985 (99.9%)\\n  Truncated:   50/985\\n  Predictions: 10581\\n==================================================\\n2026-05-15 23:45:51,176 INFO Detected adapter at /root/autodl-tmp/grpo_ced_g8_bf16/checkpoint-90, base: /root/autodl-tmp/models/Qwen3-4B\\n2026-05-15 23:45:51,176 INFO Loading tokenizer: /root/autodl-tmp/models/Qwen3-4B\\n2026-05-15 23:45:51,491 INFO Loading model: /root/autodl-tmp/models/Qwen3-4B\\n`torch_dtype` is deprecated! Use `dtype` instead!\\n2026-05-15 23:45:51,697 INFO We will use 90% of the memory on device 0 for storing the model, and 10% for the buffer to avoid OOM. You can set `max_memory` in to a higher value to use more memory (at your own risk).\\n\\rLoading checkpoint shards:   0%|          | 0/3 [00:00<?, ?it/s]\\rLoading checkpoint shards:  33%|███▎      | 1/3 [00:00<00:01,  1.29it/s]\\rLoading checkpoint shards:  67%|██████▋   | 2/3 [00:01<00:00,  1.23it/s]\\rLoading checkpoint shards: 100%|██████████| 3/3 [00:01<00:00,  1.83it/s]\\n2026-05-15 23:45:53,374 INFO Loading & merging SFT adapter: /root/autodl-tmp/sft_output\\n2026-05-15 23:45:56,528 INFO Loading LoRA adapter: /root/autodl-tmp/grpo_ced_g8_bf16/checkpoint-90\\n2026-05-15 23:45:58,025 INFO Loaded 998 documents from /root/autodl-tmp/data/docred/dev.json\\n2026-05-15 23:45:58,119 INFO Processed 12275 relation samples from 998 documents (5445 samples without hard negatives)\\n2026-05-15 23:45:58,521 INFO Prepared 985 eval documents, 12275 gold triples\\n\\rIn
…[truncated 6455 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_grpo_g8_bf16_results_20260515T175633",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-15T17:57:12.276030+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_grpo_g8_bf16_results_20260515T175633",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-15T17:57:12.276173+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "tmux list-sessions",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_eval_grpo_g8_bf16_results_20260515T175633",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "tmux list-sessions",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-15T17:57:12.276335+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: 'tmux' is not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_grpo_g8_bf16_results_20260515T175633",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-15T17:57:12.276462+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "cat /root/autodl-tmp/eval_results/grpo_g8_bf16/summary.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_eval_grpo_g8_bf16_results_20260515T175633",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "cat /root/autodl-tmp/eval_results/grpo_g8_bf16/summary.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-15T17:57:12.276607+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"checkpoint-80\\\": {\\n    \\\"step\\\": 80,\\n    \\\"f1\\\": 0.44558883317522696,\\n    \\\"ign_f1\\\": 0.44558883317522696,\\n    \\\"evi_f1\\\": 0.8033558667310478,\\n    \\\"edcr\\\": 0.6408720522367924,\\n    \\\"format_ok_rate\\\": 0.9989847715736041\\n  },\\n  \\\"checkpoint-90\\\": {\\n    \\\"step\\\": 90,\\n    \\\"f1\\\": 0.4523133756813984,\\n    \\\"ign_f1\\\": 0.4523133756813984,\\n    \\\"evi_f1\\\": 0.8051589682063588,\\n    \\\"edcr\\\": 0.6414106331819396,\\n    \\\"format_ok_rate\\\": 0.9979695431472081\\n  },\\n  \\\"checkpoint-100\\\": {\\n    \\\"step\\\": 100,\\n    \\\"f1\\\": 0.45494376439766926,\\n    \\\"ign_f1\\\": 0.45494376439766926,\\n    \\\"evi_f1\\\": 0.8086379135012263,\\n    \\\"edcr\\\": 0.6318226386316592,\\n    \\\"format_ok_rate\\\": 1.0\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.32}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_grpo_g8_bf16_results_20260515T175633",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-15T17:57:12.276799+00:00_

评估**全部正常完成**，EXIT_CODE=0，3 个 checkpoint 都已评估。

### 结果汇总

| Metric | ckpt-80 | ckpt-90 | ckpt-100 |
|--------|---------|---------|----------|
| **Rel-F1** | 0.4456 | 0.4523 | **0.4549** |
| **Ign-F1** | 0.4456 | 0.4523 | **0.4549** |
| **Evi-F1** | 0.8034 | 0.8052 | **0.8086** |
| **EDCR** | **0.6409** | 0.6414 | 0.6318 |
| **Format OK** | 99.9% | 99.8% | **100.0%** |
| **Truncated** | 50/985 | 61/985 | 61/985 |

**Best by F1: checkpoint-100** (F1=0.4549, Evi-F1=0.8086)。

趋势：F1 和 Evi-F1 从 ckpt-80 到 100 单调上升，EDCR 在 ckpt-100 略降（0.6409→0.6318）。Format OK 逐步改善到 100%。

需要我更新 registry 状态吗？

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_eval_grpo_g8_bf16_results_20260515T175633"
}
```

</details>

---
