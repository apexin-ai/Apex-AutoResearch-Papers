# analysis eval pi05 attn k09 long seed46 strict cqa1

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 7
- **Recorded user turns:** 0
- **Tool calls:** 3
- **Original source:** `logs/chats/worker_analysis_eval_pi05_attn_k09_long_seed46_strict_cqa1_20260528T105411.jsonl`
- **Structured JSON:** [`e25a99bd7149633f17e7.json`](../../sessions/e2/e25a99bd7149633f17e7.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

7 recorded events

### Tool call

_source line 1 · 2026-05-28T10:54:40.289442+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__fetch_wandb_metrics",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_eval_pi05_attn_k09_long_seed46_strict_cqa1_20260528T105411",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__fetch_wandb_metrics",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-28T10:54:40.289893+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_pi05_attn_k09_long_seed46_strict_cqa1_20260528T105411",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-28T10:54:40.290186+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-33015",
  "command": "tail -100 ~/runs/importance_margin_vla_compress/eval_pi05_attn_k09_long_seed46_strict_cqa1.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_eval_pi05_attn_k09_long_seed46_strict_cqa1_20260528T105411",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-33015",
    "command": "tail -100 ~/runs/importance_margin_vla_compress/eval_pi05_attn_k09_long_seed46_strict_cqa1.log",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-28T10:54:40.290438+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__list_wandb_runs",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_eval_pi05_attn_k09_long_seed46_strict_cqa1_20260528T105411",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__list_wandb_runs",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-28T10:54:40.290790+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-28 14:25:51,443 Config: suite=libero_10, prune=attention, keep=0.9, eps=50, gpu=0\\n2026-05-28 14:25:51,444 Loading pi0.5 from /root/autodl-tmp/pi05_libero_finetuned ...\\n2026-05-28 14:25:52,160 JAX version 0.10.0 available.\\nThe PI05 model is a direct port of the OpenPI implementation. \\nThis implementation follows the original OpenPI structure for compatibility. \\nOriginal implementation: https://github.com/Physical-Intelligence/openpi\\n2026-05-28 14:27:56,408 Enabled gradient checkpointing for PI05Pytorch model\\nLoading model from: /root/autodl-tmp/pi05_libero_finetuned\\n✓ Loaded state dict from model.safetensors\\n2026-05-28 14:28:01,398 Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embedding.bias\\n2026-05-28 14:28:01,398 Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embedding.weight\\nAll keys loaded successfully!\\n2026-05-28 14:28:04,935 Patched embed_image\\n2026-05-28 14:28:04,948 Model: 4143.4M params\\n2026-05-28 14:28:04,948 Vision tokens: 256/image, 3 slots -> 768 total\\n2026-05-28 14:28:04,948 Baseline mode (no pruning), embed_prefix fixed\\n2026-05-28 14:28:04,948 Pruning: attention, keep 230/256 tokens/image (690 total, 2-layer probe)\\n2026-05-28 14:28:06,387 Preprocessor/postprocessor loaded\\n[robosuite WARNING] No private macro file found! (macros.py:53)\\n2026-05-28 14:28:06,424 No private macro file found!\\n[robosuite WARNING] It is recommended to use a private macro file (macros.py:54)\\n2026-05-28 14:28:06,424 It is recommended to use a private macro file\\n[robosuite WARNING] To setup, run: python /root/miniconda3/lib/python3.12/site-packages/robosuite/scripts/setup_macros.py (macros.py:55)\\n2026-05-28 14:28:06,424 To setup, run: python /root/miniconda3/lib/python3.12/site-packages/robosuite/scripts/setup
…[truncated 6391 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_pi05_attn_k09_long_seed46_strict_cqa1_20260528T105411",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-28T10:54:40.291022+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_pi05_attn_k09_long_seed46_strict_cqa1_20260528T105411",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-28T10:54:40.291325+00:00_

实验已完成，日志完整，无报错。

```
=== RESULT ===
exp_id: eval_pi05_attn_k09_long_seed46_strict_cqa1
overall_success_rate: 65.4%
per_task: [T0: 44%, T1: 94%, T2: 46%, T3: 92%, T4: 68%, T5: 88%, T6: 54%, T7: 68%, T8: 10%, T9: 90%]
status: success
notes: EXIT_CODE=0, 总耗时263.2min。历史seeds: s42=64.0%, s43=62.8%, s44=63.4%, s46=65.4%。结果文件已保存至 eval_results/pi05_attention_k0.90_libero_10_seed46.json
=== END ===
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_eval_pi05_attn_k09_long_seed46_strict_cqa1_20260528T105411"
}
```

</details>

---
