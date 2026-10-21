# analyze eval pi05 random k085 spatial seed42 postfix v2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 17
- **Recorded user turns:** 0
- **Tool calls:** 8
- **Original source:** `logs/chats/worker_analyze_eval_pi05_random_k085_spatial_seed42_postfix_v2_20260524T050603.jsonl`
- **Structured JSON:** [`0268633b2657f383ad4c.json`](../../sessions/02/0268633b2657f383ad4c.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

17 recorded events

### Tool call

_source line 1 · 2026-05-24T05:08:15.378676+00:00_

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
  "session": "worker_analyze_eval_pi05_random_k085_spatial_seed42_postfix_v2_20260524T050603",
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

_source line 2 · 2026-05-24T05:08:15.379022+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_pi05_random_k085_spatial_seed42_postfix_v2_20260524T050603",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-24T05:08:15.379234+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-33015",
  "command": "tail -100 /root/autodl-tmp/importance_margin_vla_compress/logs/eval_pi05_random_k085_spatial_seed42_postfix_v2.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_pi05_random_k085_spatial_seed42_postfix_v2_20260524T050603",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-33015",
    "command": "tail -100 /root/autodl-tmp/importance_margin_vla_compress/logs/eval_pi05_random_k085_spatial_seed42_postfix_v2.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-24T05:08:15.379558+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-24 10:17:59,096 Config: suite=libero_spatial, prune=random, keep=0.85, eps=50, gpu=0\\n2026-05-24 10:17:59,097 Loading pi0.5 from /root/autodl-tmp/pi05_libero_finetuned ...\\nThe PI05 model is a direct port of the OpenPI implementation. \\nThis implementation follows the original OpenPI structure for compatibility. \\nOriginal implementation: https://github.com/Physical-Intelligence/openpi\\n2026-05-24 10:20:11,333 Enabled gradient checkpointing for PI05Pytorch model\\nLoading model from: /root/autodl-tmp/pi05_libero_finetuned\\n✓ Loaded state dict from model.safetensors\\n2026-05-24 10:20:17,431 Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embedding.bias\\n2026-05-24 10:20:17,431 Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embedding.weight\\nAll keys loaded successfully!\\n2026-05-24 10:20:20,868 Patched embed_image\\n2026-05-24 10:20:20,880 Model: 4143.4M params\\n2026-05-24 10:20:20,880 Vision tokens: 256/image, 3 slots -> 768 total\\n2026-05-24 10:20:20,880 Pruning: random, keep 217/256 tokens/image (651 total)\\n2026-05-24 10:20:22,621 Preprocessor/postprocessor loaded\\n[robosuite WARNING] No private macro file found! (macros.py:53)\\n2026-05-24 10:20:22,663 No private macro file found!\\n[robosuite WARNING] It is recommended to use a private macro file (macros.py:54)\\n2026-05-24 10:20:22,663 It is recommended to use a private macro file\\n[robosuite WARNING] To setup, run: python /root/miniconda3/lib/python3.12/site-packages/robosuite/scripts/setup_macros.py (macros.py:55)\\n2026-05-24 10:20:22,663 To setup, run: python /root/miniconda3/lib/python3.12/site-packages/robosuite/scripts/setup_macros.py\\n2026-05-24 10:20:22,724 No OpenGL_accelerate module loaded: No module named 'OpenGL_accelerate'\\n[info] using task orders [0, 1, 2
…[truncated 6223 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_pi05_random_k085_spatial_seed42_postfix_v2_20260524T050603",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-24T05:08:15.379900+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_pi05_random_k085_spatial_seed42_postfix_v2",
  "field": "metrics",
  "value": "{'overall_sr': 60.8, 'per_task_sr': {'T0_pick_up_black_bowl_between_plate': 84, 'T1_pick_up_black_bowl_next_to_ramekin': 68, 'T2_pick_up_black_bowl_from_table_center': 92, 'T3_pick_up_black_bowl_on_cookie_box': 16, 'T4_pick_up_black_bowl_in_top_drawer': 66, 'T5_pick_up_black_bowl_on_ramekin': 28, 'T6_pick_up_black_bowl_next_to_cookie': 44, 'T7_pick_up_black_bowl_on_stove': 76, 'T8_pick_up_black_bowl_next_to_plate': 82, 'T9_pick_up_black_bowl_on_wooden_cab': 52}, 'total_episodes': 500, 'total_success': 304, 'baseline_spatial_k1': 78, 'delta_vs_baseline': -17.2}",
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_pi05_random_k085_spatial_seed42_postfix_v2_20260524T050603",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_pi05_random_k085_spatial_seed42_postfix_v2",
    "field": "metrics",
    "value": "{'overall_sr': 60.8, 'per_task_sr': {'T0_pick_up_black_bowl_between_plate': 84, 'T1_pick_up_black_bowl_next_to_ramekin': 68, 'T2_pick_up_black_bowl_from_table_center': 92, 'T3_pick_up_black_bowl_on_cookie_box': 16, 'T4_pick_up_black_bowl_in_top_drawer': 66, 'T5_pick_up_black_bowl_on_ramekin': 28, 'T6_pick_up_black_bowl_next_to_cookie': 44, 'T7_pick_up_black_bowl_on_stove': 76, 'T8_pick_up_black_bowl_next_to_plate': 82, 'T9_pick_up_black_bowl_on_wooden_cab': 52}, 'total_episodes': 500, 'total_success': 304, 'baseline_spatial_k1': 78, 'delta_vs_baseline': -17.2}",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-24T05:08:15.380130+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_pi05_random_k085_spatial_seed42_postfix_v2\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T02:17:26.991Z\", \"updated_at\": \"2026-05-24T05:07:05.825Z\", \"hypothesis\": \"π0.5 Spatial Random k=0.85 post-fix — CPU RNG bug 修复后重跑 Spatial 基线，测试 disruption peak 是否在 Spatial suite 复现\", \"spec\": {\"command\": \"eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.85 --suite libero_spatial --n_episodes 50 --seed 42 --gpu 0\", \"server\": \"cqa1-33015\", \"gpu\": [\"cuda:1\"], \"pid\": \"697975\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_pi05_random_k085_spatial_seed42_postfix_v2.log\", \"submitted_at\": \"2026-05-24T02:17:56.270Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"gpu_id\": 1, \"data_path\": \"libero_spatial\", \"data_count\": 500, \"model_name\": \"pi05_libero_finetuned\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/pi05_libero_finetuned\", \"checkpoint_path\": \"N/A (eval only)\", \"eval_data\": \"libero_spatial (10 tasks x 50 episodes)\"}, \"reproduce\": {\"finished_at\": \"2026-05-24T05:00:52.023Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-24T05:01:10.926339+00:00\"}]}, \"metrics\": {\"overall_sr\": 60.8, \"per_task_sr\": {\"T0_pick_up_black_bowl_between_plate\": 84, \"T1_pick_up_black_bowl_next_to_ramekin\": 68, \"T2_pick_up_black_bowl_from_table_center\": 92, \"T3_pick_up_black_bowl_on_cookie_box\": 16, \"T4_pick_up_black_bowl_in_top_drawer\": 66, \"T5_pick_up_black_bowl_on_ramekin\": 28, \"T6_pick_up_black_bowl_next_to_cookie\": 44, \"T7_pick_up_black_bowl_on_stove\": 76, \"T8_pick_up_black_bowl_next_to_plate\": 82, \"T9_pick_up_black_bowl_on_wooden_cab\": 52}, \"total_episodes\": 500, \"total_success\": 304, \"baseline_spatial_k1\": 78, \"delta_vs_baseline\": -17.2}}}, \"error\": null
…[truncated 49 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_pi05_random_k085_spatial_seed42_postfix_v2_20260524T050603",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-24T05:08:15.380327+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_pi05_random_k085_spatial_seed42_postfix_v2",
  "field": "conclusion",
  "value": "success — Spatial suite 无 disruption peak。Random k=0.85 SR=60.8% vs baseline k=1.0 SR=78%，降幅 17.2pp，属中度退化而非崩塌（对比 Object suite 同参数从 ~82% 崩至 5.6%）。Spatial 对 random pruning 更鲁棒，但仍有显著性能损失，尤其 T3(16%)、T5(28%) 退化严重。",
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_pi05_random_k085_spatial_seed42_postfix_v2_20260524T050603",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_pi05_random_k085_spatial_seed42_postfix_v2",
    "field": "conclusion",
    "value": "success — Spatial suite 无 disruption peak。Random k=0.85 SR=60.8% vs baseline k=1.0 SR=78%，降幅 17.2pp，属中度退化而非崩塌（对比 Object suite 同参数从 ~82% 崩至 5.6%）。Spatial 对 random pruning 更鲁棒，但仍有显著性能损失，尤其 T3(16%)、T5(28%) 退化严重。",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-24T05:08:15.380477+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid conclusion 'success — Spatial suite 无 disruption peak。Random k=0.85 SR=60.8% vs baseline k=1.0 SR=78%，降幅 17.2pp，属中度退化而非崩塌（对比 Object suite 同参数从 ~82% 崩至 5.6%）。Spatial 对 random pruning 更鲁棒，但仍有显著性能损失，尤其 T3(16%)、T5(28%) 退化严重。'. Valid: ['failed', 'killed', 'negative', 'success']\", \"metadata\": {\"elapsed_seconds\": 7.3733}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_pi05_random_k085_spatial_seed42_postfix_v2_20260524T050603",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-24T05:08:15.380797+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_pi05_random_k085_spatial_seed42_postfix_v2",
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
  "session": "worker_analyze_eval_pi05_random_k085_spatial_seed42_postfix_v2_20260524T050603",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_pi05_random_k085_spatial_seed42_postfix_v2",
    "field": "conclusion",
    "value": "success",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-24T05:08:15.381094+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_pi05_random_k085_spatial_seed42_postfix_v2\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T02:17:26.991Z\", \"updated_at\": \"2026-05-24T05:07:30.698Z\", \"hypothesis\": \"π0.5 Spatial Random k=0.85 post-fix — CPU RNG bug 修复后重跑 Spatial 基线，测试 disruption peak 是否在 Spatial suite 复现\", \"spec\": {\"command\": \"eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.85 --suite libero_spatial --n_episodes 50 --seed 42 --gpu 0\", \"server\": \"cqa1-33015\", \"gpu\": [\"cuda:1\"], \"pid\": \"697975\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_pi05_random_k085_spatial_seed42_postfix_v2.log\", \"submitted_at\": \"2026-05-24T02:17:56.270Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"gpu_id\": 1, \"data_path\": \"libero_spatial\", \"data_count\": 500, \"model_name\": \"pi05_libero_finetuned\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/pi05_libero_finetuned\", \"checkpoint_path\": \"N/A (eval only)\", \"eval_data\": \"libero_spatial (10 tasks x 50 episodes)\"}, \"reproduce\": {\"finished_at\": \"2026-05-24T05:00:52.023Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-24T05:01:10.926339+00:00\"}]}, \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.733}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_pi05_random_k085_spatial_seed42_postfix_v2_20260524T050603",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-24T05:08:15.381335+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_pi05_random_k085_spatial_seed42_postfix_v2",
  "field": "status",
  "value": "DONE",
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_pi05_random_k085_spatial_seed42_postfix_v2_20260524T050603",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_pi05_random_k085_spatial_seed42_postfix_v2",
    "field": "status",
    "value": "DONE",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-24T05:08:15.381482+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Cannot transition ANALYZING → DONE(success) without metrics. Set metrics first, or use conclusion=negative/failed.\", \"metadata\": {\"elapsed_seconds\": 6.0424}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_pi05_random_k085_spatial_seed42_postfix_v2_20260524T050603",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-24T05:08:15.381634+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_pi05_random_k085_spatial_seed42_postfix_v2",
  "field": "metrics",
  "value": "{'overall_sr': 60.8, 'per_task_sr': {'T0': 84, 'T1': 68, 'T2': 92, 'T3': 16, 'T4': 66, 'T5': 28, 'T6': 44, 'T7': 76, 'T8': 82, 'T9': 52}, 'total_episodes': 500, 'total_success': 304, 'baseline_spatial_k1': 78, 'delta_vs_baseline': -17.2}",
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_pi05_random_k085_spatial_seed42_postfix_v2_20260524T050603",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_pi05_random_k085_spatial_seed42_postfix_v2",
    "field": "metrics",
    "value": "{'overall_sr': 60.8, 'per_task_sr': {'T0': 84, 'T1': 68, 'T2': 92, 'T3': 16, 'T4': 66, 'T5': 28, 'T6': 44, 'T7': 76, 'T8': 82, 'T9': 52}, 'total_episodes': 500, 'total_success': 304, 'baseline_spatial_k1': 78, 'delta_vs_baseline': -17.2}",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-24T05:08:15.381820+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_pi05_random_k085_spatial_seed42_postfix_v2\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T02:17:26.991Z\", \"updated_at\": \"2026-05-24T05:07:50.463Z\", \"hypothesis\": \"π0.5 Spatial Random k=0.85 post-fix — CPU RNG bug 修复后重跑 Spatial 基线，测试 disruption peak 是否在 Spatial suite 复现\", \"spec\": {\"command\": \"eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.85 --suite libero_spatial --n_episodes 50 --seed 42 --gpu 0\", \"server\": \"cqa1-33015\", \"gpu\": [\"cuda:1\"], \"pid\": \"697975\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_pi05_random_k085_spatial_seed42_postfix_v2.log\", \"submitted_at\": \"2026-05-24T02:17:56.270Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"gpu_id\": 1, \"data_path\": \"libero_spatial\", \"data_count\": 500, \"model_name\": \"pi05_libero_finetuned\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/pi05_libero_finetuned\", \"checkpoint_path\": \"N/A (eval only)\", \"eval_data\": \"libero_spatial (10 tasks x 50 episodes)\"}, \"reproduce\": {\"finished_at\": \"2026-05-24T05:00:52.023Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-24T05:01:10.926339+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 60.8, \"per_task_sr\": {\"T0\": 84, \"T1\": 68, \"T2\": 92, \"T3\": 16, \"T4\": 66, \"T5\": 28, \"T6\": 44, \"T7\": 76, \"T8\": 82, \"T9\": 52}, \"total_episodes\": 500, \"total_success\": 304, \"baseline_spatial_k1\": 78, \"delta_vs_baseline\": -17.2}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.5707}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_pi05_random_k085_spatial_seed42_postfix_v2_20260524T050603",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-24T05:08:15.381969+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_pi05_random_k085_spatial_seed42_postfix_v2",
  "field": "status",
  "value": "DONE",
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_pi05_random_k085_spatial_seed42_postfix_v2_20260524T050603",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_pi05_random_k085_spatial_seed42_postfix_v2",
    "field": "status",
    "value": "DONE",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-24T05:08:15.382170+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_pi05_random_k085_spatial_seed42_postfix_v2\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-24T02:17:26.991Z\", \"updated_at\": \"2026-05-24T05:07:57.868Z\", \"hypothesis\": \"π0.5 Spatial Random k=0.85 post-fix — CPU RNG bug 修复后重跑 Spatial 基线，测试 disruption peak 是否在 Spatial suite 复现\", \"spec\": {\"command\": \"eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.85 --suite libero_spatial --n_episodes 50 --seed 42 --gpu 0\", \"server\": \"cqa1-33015\", \"gpu\": [\"cuda:1\"], \"pid\": \"697975\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_pi05_random_k085_spatial_seed42_postfix_v2.log\", \"submitted_at\": \"2026-05-24T02:17:56.270Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"gpu_id\": 1, \"data_path\": \"libero_spatial\", \"data_count\": 500, \"model_name\": \"pi05_libero_finetuned\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/pi05_libero_finetuned\", \"checkpoint_path\": \"N/A (eval only)\", \"eval_data\": \"libero_spatial (10 tasks x 50 episodes)\", \"wall_clock_seconds\": 10201.6, \"gpu_hours\": 2.83}, \"reproduce\": {\"finished_at\": \"2026-05-24T05:00:52.023Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-24T05:01:10.926339+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 60.8, \"per_task_sr\": {\"T0\": 84, \"T1\": 68, \"T2\": 92, \"T3\": 16, \"T4\": 66, \"T5\": 28, \"T6\": 44, \"T7\": 76, \"T8\": 82, \"T9\": 52}, \"total_episodes\": 500, \"total_success\": 304, \"baseline_spatial_k1\": 78, \"delta_vs_baseline\": -17.2}, \"completed_at\": \"2026-05-24T05:07:57.868Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 10.959}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_pi05_random_k085_spatial_seed42_postfix_v2_20260524T050603",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-24T05:08:15.382486+00:00_

Registry updated to DONE. 

```
RESULT:
- overall_sr: 60.8%
- per_task: T0=84%, T1=68%, T2=92%, T3=16%, T4=66%, T5=28%, T6=44%, T7=76%, T8=82%, T9=52%
- total_episodes: 500 (10 tasks × 50 eps, all complete)
- anomalies: 无
- comparison: baseline(k=1.0)=78%, this(k=0.85)=60.8%, delta=-17.2pp
- disruption_peak_in_spatial: NO
```

**结论 (success)**：Spatial suite 无 disruption peak。Random k=0.85 从 78% 降至 60.8%（-17.2pp），属中度退化，远非 Object suite 的灾难性崩塌（82% → 5.6%，-76pp）。

值得注意：T3(16%) 和 T5(28%) 退化严重，说明 random pruning 对某些需要精细空间定位的 task 仍有显著影响，但整体不构成 disruption peak 现象。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analyze_eval_pi05_random_k085_spatial_seed42_postfix_v2_20260524T050603"
}
```

</details>

---
