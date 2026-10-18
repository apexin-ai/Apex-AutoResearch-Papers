# analyze eval pi05 attn k095 long seed44 strict w41

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 5
- **Recorded user turns:** 0
- **Tool calls:** 2
- **Original source:** `logs/chats/worker_analyze_eval_pi05_attn_k095_long_seed44_strict_w41_20260528T002932.jsonl`
- **Structured JSON:** [`a9d991390d26b3d0e340.json`](../../sessions/a9/a9d991390d26b3d0e340.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

5 recorded events

### Tool call

_source line 1 · 2026-05-28T00:30:02.732338+00:00_

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
  "session": "worker_analyze_eval_pi05_attn_k095_long_seed44_strict_w41_20260528T002932",
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

_source line 2 · 2026-05-28T00:30:02.733341+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_pi05_attn_k095_long_seed44_strict_w41_20260528T002932",
  "tool": "ToolSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-28T00:30:02.733615+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-41074",
  "command": "tail -100 ~/runs/importance_margin_vla_compress/eval_pi05_attn_k095_long_seed44_strict_w41.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_pi05_attn_k095_long_seed44_strict_w41_20260528T002932",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-41074",
    "command": "tail -100 ~/runs/importance_margin_vla_compress/eval_pi05_attn_k095_long_seed44_strict_w41.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-28T00:30:02.733964+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-28 06:02:08,466 Config: suite=libero_10, prune=attention, keep=0.95, eps=50, gpu=0\\n2026-05-28 06:02:08,466 Loading π0.5 from /root/autodl-tmp/pi05_libero_finetuned ...\\nThe PI05 model is a direct port of the OpenPI implementation. \\nThis implementation follows the original OpenPI structure for compatibility. \\nOriginal implementation: https://github.com/Physical-Intelligence/openpi\\n2026-05-28 06:03:43,975 Enabled gradient checkpointing for PI05Pytorch model\\nLoading model from: /root/autodl-tmp/pi05_libero_finetuned\\n✓ Loaded state dict from model.safetensors\\n2026-05-28 06:03:45,658 Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embedding.bias\\n2026-05-28 06:03:45,658 Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embedding.weight\\nAll keys loaded successfully!\\n2026-05-28 06:03:47,437 Patched embed_image\\n2026-05-28 06:03:47,444 Model: 4143.4M params\\n2026-05-28 06:03:47,444 Vision tokens: 256/image, 3 slots -> 768 total\\n2026-05-28 06:03:47,444 Pruning: attention, keep 243/256 tokens/image (729 total, 2-layer probe)\\n2026-05-28 06:03:48,149 Preprocessor/postprocessor loaded\\n[robosuite WARNING] No private macro file found! (__init__.py:7)\\n2026-05-28 06:03:48,169 No private macro file found!\\n[robosuite WARNING] It is recommended to use a private macro file (__init__.py:8)\\n2026-05-28 06:03:48,169 It is recommended to use a private macro file\\n[robosuite WARNING] To setup, run: python /root/miniconda3/lib/python3.12/site-packages/robosuite/scripts/setup_macros.py (__init__.py:9)\\n2026-05-28 06:03:48,169 To setup, run: python /root/miniconda3/lib/python3.12/site-packages/robosuite/scripts/setup_macros.py\\n2026-05-28 06:03:48,222 No OpenGL_accelerate module loaded: No module named 'OpenGL_accelerate'\\n[info] using ta
…[truncated 6115 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_pi05_attn_k095_long_seed44_strict_w41_20260528T002932",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 5 · 2026-05-28T00:30:02.734316+00:00_

```
RESULT: eval_pi05_attn_k095_long_seed44_strict_w41
Overall SR: 77.8%
Per-task: [T0: 92%, T1: 96%, T2: 76%, T3: 100%, T4: 84%, T5: 96%, T6: 14%, T7: 86%, T8: 38%, T9: 96%]
Status: success
Notes: 无异常，10/10 tasks 全部完成，总耗时 128.8min
3-seed stats: seed42=78.4%, seed43=77.2%, seed44=77.8%, mean=77.8%±0.5pp
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analyze_eval_pi05_attn_k095_long_seed44_strict_w41_20260528T002932"
}
```

</details>

---
