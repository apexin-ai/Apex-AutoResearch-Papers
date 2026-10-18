# analysis eval pi05 l2norm k095 long strict

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 9
- **Recorded user turns:** 0
- **Tool calls:** 4
- **Original source:** `logs/chats/worker_analysis_eval_pi05_l2norm_k095_long_strict_20260527T095613.jsonl`
- **Structured JSON:** [`a267eb09aaaab42e4f6b.json`](../../sessions/a2/a267eb09aaaab42e4f6b.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

9 recorded events

### Tool call

_source line 1 · 2026-05-27T09:57:06.207879+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__fetch_wandb_metrics,mcp__agent-ml-research__update_registry",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_eval_pi05_l2norm_k095_long_strict_20260527T095613",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__fetch_wandb_metrics,mcp__agent-ml-research__update_registry",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-27T09:57:06.208232+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_pi05_l2norm_k095_long_strict_20260527T095613",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-27T09:57:06.208425+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-41074",
  "command": "tail -100 /root/runs/importance_margin_vla_compress/eval_pi05_l2norm_k095_long_seed42_strict.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_eval_pi05_l2norm_k095_long_strict_20260527T095613",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-41074",
    "command": "tail -100 /root/runs/importance_margin_vla_compress/eval_pi05_l2norm_k095_long_seed42_strict.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-27T09:57:06.208676+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-27 15:31:44,751 Config: suite=libero_10, prune=l2norm, keep=0.95, eps=50, gpu=0\\n2026-05-27 15:31:44,751 Loading π0.5 from /root/autodl-tmp/pi05_libero_finetuned ...\\nThe PI05 model is a direct port of the OpenPI implementation. \\nThis implementation follows the original OpenPI structure for compatibility. \\nOriginal implementation: https://github.com/Physical-Intelligence/openpi\\n2026-05-27 15:33:18,946 Enabled gradient checkpointing for PI05Pytorch model\\nLoading model from: /root/autodl-tmp/pi05_libero_finetuned\\n✓ Loaded state dict from model.safetensors\\n2026-05-27 15:33:21,343 Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embedding.bias\\n2026-05-27 15:33:21,343 Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embedding.weight\\nAll keys loaded successfully!\\n2026-05-27 15:33:23,270 Patched embed_image\\n2026-05-27 15:33:23,277 Model: 4143.4M params\\n2026-05-27 15:33:23,277 Vision tokens: 256/image, 3 slots -> 768 total\\n2026-05-27 15:33:23,277 Pruning: l2norm, keep 243/256 tokens/image (729 total)\\n2026-05-27 15:33:24,033 Preprocessor/postprocessor loaded\\n[robosuite WARNING] No private macro file found! (__init__.py:7)\\n2026-05-27 15:33:24,055 No private macro file found!\\n[robosuite WARNING] It is recommended to use a private macro file (__init__.py:8)\\n2026-05-27 15:33:24,055 It is recommended to use a private macro file\\n[robosuite WARNING] To setup, run: python /root/miniconda3/lib/python3.12/site-packages/robosuite/scripts/setup_macros.py (__init__.py:9)\\n2026-05-27 15:33:24,055 To setup, run: python /root/miniconda3/lib/python3.12/site-packages/robosuite/scripts/setup_macros.py\\n2026-05-27 15:33:24,103 No OpenGL_accelerate module loaded: No module named 'OpenGL_accelerate'\\n[info] using task orders [0, 1, 2, 3
…[truncated 6081 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_pi05_l2norm_k095_long_strict_20260527T095613",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-27T09:57:06.208892+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_pi05_l2norm_k095_long_seed42_strict",
  "field": "metrics",
  "value": "{'overall_sr': 86.2, 'task_sr': {'T0': 92, 'T1': 96, 'T2': 96, 'T3': 100, 'T4': 98, 'T5': 98, 'T6': 48, 'T7': 90, 'T8': 46, 'T9': 98}}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_eval_pi05_l2norm_k095_long_strict_20260527T095613",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_pi05_l2norm_k095_long_seed42_strict",
    "field": "metrics",
    "value": "{'overall_sr': 86.2, 'task_sr': {'T0': 92, 'T1': 96, 'T2': 96, 'T3': 100, 'T4': 98, 'T5': 98, 'T6': 48, 'T7': 90, 'T8': 46, 'T9': 98}}"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-27T09:57:06.209058+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_pi05_l2norm_k095_long_seed42_strict\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-27T09:56:56.494Z\", \"updated_at\": \"2026-05-27T09:56:56.495Z\", \"metrics\": {\"overall_sr\": 86.2, \"task_sr\": {\"T0\": 92, \"T1\": 96, \"T2\": 96, \"T3\": 100, \"T4\": 98, \"T5\": 98, \"T6\": 48, \"T7\": 90, \"T8\": 46, \"T9\": 98}}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3518}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_pi05_l2norm_k095_long_strict_20260527T095613",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-27T09:57:06.209227+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_pi05_l2norm_k095_long_seed42_strict",
  "field": "conclusion",
  "value": "success"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_eval_pi05_l2norm_k095_long_strict_20260527T095613",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_pi05_l2norm_k095_long_seed42_strict",
    "field": "conclusion",
    "value": "success"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-27T09:57:06.209373+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_pi05_l2norm_k095_long_seed42_strict\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-27T09:56:56.494Z\", \"updated_at\": \"2026-05-27T09:56:59.367Z\", \"metrics\": {\"overall_sr\": 86.2, \"task_sr\": {\"T0\": 92, \"T1\": 96, \"T2\": 96, \"T3\": 100, \"T4\": 98, \"T5\": 98, \"T6\": 48, \"T7\": 90, \"T8\": 46, \"T9\": 98}}, \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2079}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_pi05_l2norm_k095_long_strict_20260527T095613",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 9 · 2026-05-27T09:57:06.209535+00:00_

Registry 已更新。

**结果：overall_sr = 86.2%**

- 原值（cqa1 宽松条件）：87.0%
- Strict 重跑：86.2%
- Δ = -0.8pp，与 Attn 系列 strict 偏差模式一致（Attn k=0.95 Δ=0pp，k=0.9 Δ=-0.2pp）
- 结论：**success** — L2norm k=0.95 Long 的 87.0% 基本可信，strict 条件下仅微降 0.8pp

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_eval_pi05_l2norm_k095_long_strict_20260527T095613"
}
```

</details>

---
