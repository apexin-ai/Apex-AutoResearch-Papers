# analyze eval pi05 random k085 long seed44 strict w41

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 5
- **Recorded user turns:** 0
- **Tool calls:** 2
- **Original source:** `logs/chats/worker_analyze_eval_pi05_random_k085_long_seed44_strict_w41_20260527T234745.jsonl`
- **Structured JSON:** [`4f0d413549f8c55af4e8.json`](../../sessions/4f/4f0d413549f8c55af4e8.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

5 recorded events

### Tool call

_source line 1 · 2026-05-27T23:48:12.753450+00:00_

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
  "session": "worker_analyze_eval_pi05_random_k085_long_seed44_strict_w41_20260527T234745",
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

_source line 2 · 2026-05-27T23:48:12.753775+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_pi05_random_k085_long_seed44_strict_w41_20260527T234745",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-27T23:48:12.753944+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-41074",
  "command": "tail -100 ~/runs/importance_margin_vla_compress/eval_pi05_random_k085_long_seed44_strict_w41.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_pi05_random_k085_long_seed44_strict_w41_20260527T234745",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-41074",
    "command": "tail -100 ~/runs/importance_margin_vla_compress/eval_pi05_random_k085_long_seed44_strict_w41.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-27T23:48:12.754183+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-28 04:51:17,582 Config: suite=libero_10, prune=random, keep=0.85, eps=50, gpu=0\\n2026-05-28 04:51:17,582 Loading π0.5 from /root/autodl-tmp/pi05_libero_finetuned ...\\nThe PI05 model is a direct port of the OpenPI implementation. \\nThis implementation follows the original OpenPI structure for compatibility. \\nOriginal implementation: https://github.com/Physical-Intelligence/openpi\\n2026-05-28 04:52:51,383 Enabled gradient checkpointing for PI05Pytorch model\\nLoading model from: /root/autodl-tmp/pi05_libero_finetuned\\n✓ Loaded state dict from model.safetensors\\n2026-05-28 04:52:54,204 Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embedding.bias\\n2026-05-28 04:52:54,205 Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embedding.weight\\nAll keys loaded successfully!\\n2026-05-28 04:52:56,031 Patched embed_image\\n2026-05-28 04:52:56,037 Model: 4143.4M params\\n2026-05-28 04:52:56,037 Vision tokens: 256/image, 3 slots -> 768 total\\n2026-05-28 04:52:56,038 Pruning: random, keep 217/256 tokens/image (651 total)\\n2026-05-28 04:52:56,788 Preprocessor/postprocessor loaded\\n[robosuite WARNING] No private macro file found! (__init__.py:7)\\n2026-05-28 04:52:56,808 No private macro file found!\\n[robosuite WARNING] It is recommended to use a private macro file (__init__.py:8)\\n2026-05-28 04:52:56,808 It is recommended to use a private macro file\\n[robosuite WARNING] To setup, run: python /root/miniconda3/lib/python3.12/site-packages/robosuite/scripts/setup_macros.py (__init__.py:9)\\n2026-05-28 04:52:56,808 To setup, run: python /root/miniconda3/lib/python3.12/site-packages/robosuite/scripts/setup_macros.py\\n2026-05-28 04:52:56,856 No OpenGL_accelerate module loaded: No module named 'OpenGL_accelerate'\\n[info] using task orders [0, 1, 2, 3
…[truncated 6049 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_pi05_random_k085_long_seed44_strict_w41_20260527T234745",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 5 · 2026-05-27T23:48:12.754567+00:00_

实验正常完成（EXIT_CODE=0），无错误。

- **overall_success_rate: 44.2%** (221/500)

**per_task_rates:**

| Task | Description | SR |
|------|------------|-----|
| T0 | put both the alphabet soup and the tomat... | 34.0% |
| T1 | put both the cream cheese box and the bu... | 52.0% |
| T2 | turn on the stove and put the moka pot o... | 54.0% |
| T3 | put the black bowl in the bottom drawer | 72.0% |
| T4 | put the white mug on the left plate and... | 12.0% |
| T5 | pick up the book and place it in the bac... | 34.0% |
| T6 | put the white mug on the plate and put t... | 50.0% |
| T7 | put both the alphabet soup and the cream... | 48.0% |
| T8 | put both moka pots on the stove | 20.0% |
| T9 | put the yellow and white mug in the micr... | 66.0% |

**异常/警告:** 仅有 robosuite private macro 和 OpenGL_accelerate 的常规警告，无实质性问题。

**3-seed 汇总:**
- seed42: 44.0%, seed43: 47.2%, seed44: 44.2%
- **3-seed mean: 45.1% ± 1.5pp**

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analyze_eval_pi05_random_k085_long_seed44_strict_w41_20260527T234745"
}
```

</details>

---
