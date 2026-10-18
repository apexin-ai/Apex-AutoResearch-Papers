# analyze eval pi05 attention k07 long seed42 v2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 0
- **Tool calls:** 5
- **Original source:** `logs/chats/worker_analyze_eval_pi05_attention_k07_long_seed42_v2_20260526T231330.jsonl`
- **Structured JSON:** [`faa4123ec1853248ce73.json`](../../sessions/fa/faa4123ec1853248ce73.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

11 recorded events

### Tool call

_source line 1 · 2026-05-26T23:14:34.645987+00:00_

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
  "session": "worker_analyze_eval_pi05_attention_k07_long_seed42_v2_20260526T231330",
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

_source line 2 · 2026-05-26T23:14:34.646377+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_pi05_attention_k07_long_seed42_v2_20260526T231330",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-26T23:14:34.646560+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-33015",
  "command": "tail -100 /root/autodl-tmp/importance_margin_vla_compress/logs/eval_pi05_attention_k07_long_seed42.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_pi05_attention_k07_long_seed42_v2_20260526T231330",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-33015",
    "command": "tail -100 /root/autodl-tmp/importance_margin_vla_compress/logs/eval_pi05_attention_k07_long_seed42.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-26T23:14:34.646783+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-27 02:33:11,734 Config: suite=libero_10, prune=attention, keep=0.7, eps=50, gpu=0\\n2026-05-27 02:33:11,734 Loading pi0.5 from /root/autodl-tmp/pi05_libero_finetuned ...\\nThe PI05 model is a direct port of the OpenPI implementation. \\nThis implementation follows the original OpenPI structure for compatibility. \\nOriginal implementation: https://github.com/Physical-Intelligence/openpi\\n2026-05-27 02:35:25,127 Enabled gradient checkpointing for PI05Pytorch model\\nLoading model from: /root/autodl-tmp/pi05_libero_finetuned\\n✓ Loaded state dict from model.safetensors\\n2026-05-27 02:35:32,293 Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embedding.bias\\n2026-05-27 02:35:32,293 Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embedding.weight\\nAll keys loaded successfully!\\n2026-05-27 02:35:39,790 Patched embed_image\\n2026-05-27 02:35:39,807 Model: 4143.4M params\\n2026-05-27 02:35:39,807 Vision tokens: 256/image, 3 slots -> 768 total\\n2026-05-27 02:35:39,807 Baseline mode (no pruning), embed_prefix fixed\\n2026-05-27 02:35:39,807 Pruning: attention, keep 179/256 tokens/image (537 total, 2-layer probe)\\n2026-05-27 02:35:41,344 Preprocessor/postprocessor loaded\\n[robosuite WARNING] No private macro file found! (macros.py:53)\\n2026-05-27 02:35:41,401 No private macro file found!\\n[robosuite WARNING] It is recommended to use a private macro file (macros.py:54)\\n2026-05-27 02:35:41,401 It is recommended to use a private macro file\\n[robosuite WARNING] To setup, run: python /root/miniconda3/lib/python3.12/site-packages/robosuite/scripts/setup_macros.py (macros.py:55)\\n2026-05-27 02:35:41,401 To setup, run: python /root/miniconda3/lib/python3.12/site-packages/robosuite/scripts/setup_macros.py\\n2026-05-27 02:35:41,480 No OpenGL_accelerat
…[truncated 6292 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_pi05_attention_k07_long_seed42_v2_20260526T231330",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-26T23:14:34.646995+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_pi05_attention_k07_long_seed42_v2",
  "field": "metrics",
  "value": "{'overall_sr': 50.8, 'per_task': {'T0_alphabet_soup_tomato': 72, 'T1_cream_cheese_butter': 70, 'T2_stove_moka_pot': 58, 'T3_black_bowl_drawer': 46, 'T4_white_mug_plate': 36, 'T5_book_back': 32, 'T6_mug_plate_yellow': 58, 'T7_alphabet_soup_cream': 48, 'T8_moka_pots_stove': 6, 'T9_yellow_white_mug_microwave': 82}, 'suite': 'libero_10', 'prune_method': 'attention', 'keep_ratio': 0.7, 'seed': 42, 'episodes_per_task': 50}",
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_pi05_attention_k07_long_seed42_v2_20260526T231330",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_pi05_attention_k07_long_seed42_v2",
    "field": "metrics",
    "value": "{'overall_sr': 50.8, 'per_task': {'T0_alphabet_soup_tomato': 72, 'T1_cream_cheese_butter': 70, 'T2_stove_moka_pot': 58, 'T3_black_bowl_drawer': 46, 'T4_white_mug_plate': 36, 'T5_book_back': 32, 'T6_mug_plate_yellow': 58, 'T7_alphabet_soup_cream': 48, 'T8_moka_pots_stove': 6, 'T9_yellow_white_mug_microwave': 82}, 'suite': 'libero_10', 'prune_method': 'attention', 'keep_ratio': 0.7, 'seed': 42, 'episodes_per_task': 50}",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-26T23:14:34.647212+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_pi05_attention_k07_long_seed42_v2\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-26T20:01:56.100Z\", \"updated_at\": \"2026-05-26T23:14:03.009Z\", \"spec\": {\"command\": \"python -u eval_pi05_pruning_libero.py --prune_mode attention --keep_ratio 0.7 --suite libero_10 --n_episodes 50 --seed 42 --gpu 0\", \"server\": \"cqa1-33015\", \"gpu\": \"cuda:1\", \"pid\": 617728, \"data_path\": \"libero_10\", \"data_count\": 500, \"model_name\": \"pi0.5\", \"seed\": 42, \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_pi05_attention_k07_long_seed42.log\", \"checkpoint_source\": \"/root/autodl-tmp/pi05_libero_finetuned\", \"eval_data\": \"libero_10\"}, \"hypothesis\": \"π0.5 Attention k=0.7 Long seed42 v2 — Attn Long cliff curve 中间点。Attn k=0.75=51.8%, k=0.5=49.4%。k=0.7 补全 Attn Long curve\", \"reproduce\": {\"finished_at\": \"2026-05-26T22:51:38.247Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-26T22:51:52.306839+00:00\"}]}, \"metrics\": {\"overall_sr\": 50.8, \"per_task\": {\"T0_alphabet_soup_tomato\": 72, \"T1_cream_cheese_butter\": 70, \"T2_stove_moka_pot\": 58, \"T3_black_bowl_drawer\": 46, \"T4_white_mug_plate\": 36, \"T5_book_back\": 32, \"T6_mug_plate_yellow\": 58, \"T7_alphabet_soup_cream\": 48, \"T8_moka_pots_stove\": 6, \"T9_yellow_white_mug_microwave\": 82}, \"suite\": \"libero_10\", \"prune_method\": \"attention\", \"keep_ratio\": 0.7, \"seed\": 42, \"episodes_per_task\": 50}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.079}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_pi05_attention_k07_long_seed42_v2_20260526T231330",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-26T23:14:34.647383+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_pi05_attention_k07_long_seed42_v2",
  "field": "conclusion",
  "value": "success",
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_pi05_attention_k07_long_seed42_v2_20260526T231330",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_pi05_attention_k07_long_seed42_v2",
    "field": "conclusion",
    "value": "success",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-26T23:14:34.647518+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_pi05_attention_k07_long_seed42_v2",
  "field": "status",
  "value": "DONE",
  "project": "importance_margin_vla_compress",
  "spec": "{'checkpoint_path': 'N/A (eval only)', 'log_path': '/root/autodl-tmp/importance_margin_vla_compress/logs/eval_pi05_attention_k07_long_seed42.log'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_pi05_attention_k07_long_seed42_v2_20260526T231330",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_pi05_attention_k07_long_seed42_v2",
    "field": "status",
    "value": "DONE",
    "project": "importance_margin_vla_compress",
    "spec": "{'checkpoint_path': 'N/A (eval only)', 'log_path': '/root/autodl-tmp/importance_margin_vla_compress/logs/eval_pi05_attention_k07_long_seed42.log'}"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-26T23:14:34.647689+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_pi05_attention_k07_long_seed42_v2\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-26T20:01:56.100Z\", \"updated_at\": \"2026-05-26T23:14:12.363Z\", \"spec\": {\"command\": \"python -u eval_pi05_pruning_libero.py --prune_mode attention --keep_ratio 0.7 --suite libero_10 --n_episodes 50 --seed 42 --gpu 0\", \"server\": \"cqa1-33015\", \"gpu\": \"cuda:1\", \"pid\": 617728, \"data_path\": \"libero_10\", \"data_count\": 500, \"model_name\": \"pi0.5\", \"seed\": 42, \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_pi05_attention_k07_long_seed42.log\", \"checkpoint_source\": \"/root/autodl-tmp/pi05_libero_finetuned\", \"eval_data\": \"libero_10\"}, \"hypothesis\": \"π0.5 Attention k=0.7 Long seed42 v2 — Attn Long cliff curve 中间点。Attn k=0.75=51.8%, k=0.5=49.4%。k=0.7 补全 Attn Long curve\", \"reproduce\": {\"finished_at\": \"2026-05-26T22:51:38.247Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-26T22:51:52.306839+00:00\"}]}, \"metrics\": {\"overall_sr\": 50.8, \"per_task\": {\"T0_alphabet_soup_tomato\": 72, \"T1_cream_cheese_butter\": 70, \"T2_stove_moka_pot\": 58, \"T3_black_bowl_drawer\": 46, \"T4_white_mug_plate\": 36, \"T5_book_back\": 32, \"T6_mug_plate_yellow\": 58, \"T7_alphabet_soup_cream\": 48, \"T8_moka_pots_stove\": 6, \"T9_yellow_white_mug_microwave\": 82}, \"suite\": \"libero_10\", \"prune_method\": \"attention\", \"keep_ratio\": 0.7, \"seed\": 42, \"episodes_per_task\": 50}, \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 5.7474}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_pi05_attention_k07_long_seed42_v2_20260526T231330",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-26T23:14:34.647898+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_pi05_attention_k07_long_seed42_v2\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-26T20:01:56.100Z\", \"updated_at\": \"2026-05-26T23:14:15.748Z\", \"spec\": {\"command\": \"python -u eval_pi05_pruning_libero.py --prune_mode attention --keep_ratio 0.7 --suite libero_10 --n_episodes 50 --seed 42 --gpu 0\", \"server\": \"cqa1-33015\", \"gpu\": \"cuda:1\", \"pid\": 617728, \"data_path\": \"libero_10\", \"data_count\": 500, \"model_name\": \"pi0.5\", \"seed\": 42, \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_pi05_attention_k07_long_seed42.log\", \"checkpoint_source\": \"/root/autodl-tmp/pi05_libero_finetuned\", \"eval_data\": \"libero_10\", \"checkpoint_path\": \"N/A (eval only)\"}, \"hypothesis\": \"π0.5 Attention k=0.7 Long seed42 v2 — Attn Long cliff curve 中间点。Attn k=0.75=51.8%, k=0.5=49.4%。k=0.7 补全 Attn Long curve\", \"reproduce\": {\"finished_at\": \"2026-05-26T22:51:38.247Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-26T22:51:52.306839+00:00\"}]}, \"metrics\": {\"overall_sr\": 50.8, \"per_task\": {\"T0_alphabet_soup_tomato\": 72, \"T1_cream_cheese_butter\": 70, \"T2_stove_moka_pot\": 58, \"T3_black_bowl_drawer\": 46, \"T4_white_mug_plate\": 36, \"T5_book_back\": 32, \"T6_mug_plate_yellow\": 58, \"T7_alphabet_soup_cream\": 48, \"T8_moka_pots_stove\": 6, \"T9_yellow_white_mug_microwave\": 82}, \"suite\": \"libero_10\", \"prune_method\": \"attention\", \"keep_ratio\": 0.7, \"seed\": 42, \"episodes_per_task\": 50}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-26T23:14:15.748Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 8.5433}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_pi05_attention_k07_long_seed42_v2_20260526T231330",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-26T23:14:34.648098+00:00_

## 结果

**π0.5 Attention k=0.7 Long (libero_10) seed42: Overall SR = 50.8%**

Per-task breakdown:

| Task | SR |
|------|-----|
| T0 alphabet soup & tomato | 72% |
| T1 cream cheese & butter | 70% |
| T2 stove & moka pot | 58% |
| T3 black bowl drawer | 46% |
| T4 white mug & plate | 36% |
| T5 book placement | 32% |
| T6 mug & plate & yellow | 58% |
| T7 alphabet soup & cream | 48% |
| T8 moka pots stove | 6% |
| T9 yellow mug microwave | 82% |

### 更新后的 Attn Long cliff curve

| k | SR | Δ vs Full |
|---|-----|-----------|
| 0.95 | 77.0% | - |
| 0.90 | 63.8% | -13.2pp |
| 0.85 | 51.6% | -12.2pp |
| **0.75** | **51.8%** | +0.2pp |
| **0.70** | **50.8%** | -1.0pp |
| 0.50 | 49.4% | -1.4pp |

**关键发现**: k=0.7 (50.8%) 完美符合预期，确认 Attention pruning 在 k=0.85 以下进入平台期。从 k=0.85 到 k=0.5，SR 仅从 51.6% 缓降至 49.4%（仅 -2.2pp），cliff 明确在 k=0.9→0.85 区间（-12.2pp）。k=0.7 补全了曲线中间点，plateau 趋势清晰。

Registry 已更新为 DONE/success。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analyze_eval_pi05_attention_k07_long_seed42_v2_20260526T231330"
}
```

</details>

---
