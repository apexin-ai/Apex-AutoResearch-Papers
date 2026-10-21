# analyze eval pi05 attn k09 long seed44 strict w38

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 5
- **Recorded user turns:** 0
- **Tool calls:** 2
- **Original source:** `logs/chats/worker_analyze_eval_pi05_attn_k09_long_seed44_strict_w38_20260528T002938.jsonl`
- **Structured JSON:** [`90d12df53d99671d3dcf.json`](../../sessions/90/90d12df53d99671d3dcf.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

5 recorded events

### Tool call

_source line 1 · 2026-05-28T00:30:07.552182+00:00_

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
  "session": "worker_analyze_eval_pi05_attn_k09_long_seed44_strict_w38_20260528T002938",
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

_source line 2 · 2026-05-28T00:30:07.556691+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_pi05_attn_k09_long_seed44_strict_w38_20260528T002938",
  "tool": "ToolSearch",
  "elapsed_ms": 4
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-28T00:30:07.556964+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-33015",
  "command": "tail -100 ~/runs/importance_margin_vla_compress/eval_pi05_attn_k09_long_seed44_strict_w38.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_pi05_attn_k09_long_seed44_strict_w38_20260528T002938",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-33015",
    "command": "tail -100 ~/runs/importance_margin_vla_compress/eval_pi05_attn_k09_long_seed44_strict_w38.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-28T00:30:07.557328+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-28 04:29:40,693 Config: suite=libero_10, prune=attention, keep=0.9, eps=50, gpu=0\\n2026-05-28 04:29:40,693 Loading pi0.5 from /root/autodl-tmp/pi05_libero_finetuned ...\\n2026-05-28 04:29:41,423 JAX version 0.10.0 available.\\nThe PI05 model is a direct port of the OpenPI implementation. \\nThis implementation follows the original OpenPI structure for compatibility. \\nOriginal implementation: https://github.com/Physical-Intelligence/openpi\\n2026-05-28 04:31:52,701 Enabled gradient checkpointing for PI05Pytorch model\\nLoading model from: /root/autodl-tmp/pi05_libero_finetuned\\n✓ Loaded state dict from model.safetensors\\n2026-05-28 04:31:59,358 Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embedding.bias\\n2026-05-28 04:31:59,358 Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embedding.weight\\nAll keys loaded successfully!\\n2026-05-28 04:32:03,711 Patched embed_image\\n2026-05-28 04:32:03,726 Model: 4143.4M params\\n2026-05-28 04:32:03,726 Vision tokens: 256/image, 3 slots -> 768 total\\n2026-05-28 04:32:03,726 Baseline mode (no pruning), embed_prefix fixed\\n2026-05-28 04:32:03,726 Pruning: attention, keep 230/256 tokens/image (690 total, 2-layer probe)\\n2026-05-28 04:32:05,537 Preprocessor/postprocessor loaded\\n[robosuite WARNING] No private macro file found! (macros.py:53)\\n2026-05-28 04:32:05,588 No private macro file found!\\n[robosuite WARNING] It is recommended to use a private macro file (macros.py:54)\\n2026-05-28 04:32:05,588 It is recommended to use a private macro file\\n[robosuite WARNING] To setup, run: python /root/miniconda3/lib/python3.12/site-packages/robosuite/scripts/setup_macros.py (macros.py:55)\\n2026-05-28 04:32:05,588 To setup, run: python /root/miniconda3/lib/python3.12/site-packages/robosuite/scripts/setup
…[truncated 6391 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_pi05_attn_k09_long_seed44_strict_w38_20260528T002938",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 5 · 2026-05-28T00:30:07.559557+00:00_

```
RESULT: eval_pi05_attn_k09_long_seed44_strict_w38
Overall SR: 64.0%
Per-task: [T0:48%, T1:88%, T2:46%, T3:92%, T4:60%, T5:88%, T6:62%, T7:50%, T8:16%, T9:90%]
Status: success (EXIT_CODE=0)
Notes: 无异常，运行耗时 231.9min
3-seed stats: seed42=64.0%, seed43=62.8%, seed44=64.0%, mean=63.6%±0.6pp
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analyze_eval_pi05_attn_k09_long_seed44_strict_w38_20260528T002938"
}
```

</details>

---
