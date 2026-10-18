# analyze eval pi05 attn k075 long seed43 strict cqa1

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 17
- **Recorded user turns:** 0
- **Tool calls:** 8
- **Original source:** `logs/chats/worker_analyze_eval_pi05_attn_k075_long_seed43_strict_cqa1_20260527T222944.jsonl`
- **Structured JSON:** [`ff260be91e1ff693d9f1.json`](../../sessions/ff/ff260be91e1ff693d9f1.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

17 recorded events

### Tool call

_source line 1 · 2026-05-27T22:30:57.419092+00:00_

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
  "session": "worker_analyze_eval_pi05_attn_k075_long_seed43_strict_cqa1_20260527T222944",
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

_source line 2 · 2026-05-27T22:30:57.419455+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_pi05_attn_k075_long_seed43_strict_cqa1_20260527T222944",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-27T22:30:57.419629+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-33015",
  "command": "tail -100 ~/runs/importance_margin_vla_compress/eval_pi05_attn_k075_long_seed43_strict_cqa1.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_pi05_attn_k075_long_seed43_strict_cqa1_20260527T222944",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-33015",
    "command": "tail -100 ~/runs/importance_margin_vla_compress/eval_pi05_attn_k075_long_seed43_strict_cqa1.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-27T22:30:57.419850+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-28 02:10:55,511 Config: suite=libero_10, prune=attention, keep=0.75, eps=50, gpu=0\\n2026-05-28 02:10:55,512 Loading pi0.5 from /root/autodl-tmp/pi05_libero_finetuned ...\\n2026-05-28 02:10:56,330 JAX version 0.10.0 available.\\nThe PI05 model is a direct port of the OpenPI implementation. \\nThis implementation follows the original OpenPI structure for compatibility. \\nOriginal implementation: https://github.com/Physical-Intelligence/openpi\\n2026-05-28 02:13:14,440 Enabled gradient checkpointing for PI05Pytorch model\\nLoading model from: /root/autodl-tmp/pi05_libero_finetuned\\n✓ Loaded state dict from model.safetensors\\n2026-05-28 02:13:18,707 Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embedding.bias\\n2026-05-28 02:13:18,707 Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embedding.weight\\nAll keys loaded successfully!\\n2026-05-28 02:13:22,496 Patched embed_image\\n2026-05-28 02:13:22,510 Model: 4143.4M params\\n2026-05-28 02:13:22,510 Vision tokens: 256/image, 3 slots -> 768 total\\n2026-05-28 02:13:22,510 Baseline mode (no pruning), embed_prefix fixed\\n2026-05-28 02:13:22,510 Pruning: attention, keep 192/256 tokens/image (576 total, 2-layer probe)\\n2026-05-28 02:13:23,893 Preprocessor/postprocessor loaded\\n[robosuite WARNING] No private macro file found! (macros.py:53)\\n2026-05-28 02:13:23,928 No private macro file found!\\n[robosuite WARNING] It is recommended to use a private macro file (macros.py:54)\\n2026-05-28 02:13:23,928 It is recommended to use a private macro file\\n[robosuite WARNING] To setup, run: python /root/miniconda3/lib/python3.12/site-packages/robosuite/scripts/setup_macros.py (macros.py:55)\\n2026-05-28 02:13:23,928 To setup, run: python /root/miniconda3/lib/python3.12/site-packages/robosuite/scripts/setu
…[truncated 6390 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_pi05_attn_k075_long_seed43_strict_cqa1_20260527T222944",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-27T22:30:57.420049+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_pi05_attn_k075_long_seed43_strict_cqa1",
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
  "session": "worker_analyze_eval_pi05_attn_k075_long_seed43_strict_cqa1_20260527T222944",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_pi05_attn_k075_long_seed43_strict_cqa1",
    "field": "conclusion",
    "value": "success",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-27T22:30:57.420213+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_pi05_attn_k075_long_seed43_strict_cqa1",
  "field": "metrics",
  "value": "{'success_rate': 52, 'per_task': {'T0_alphabet_soup_tomato': 68, 'T1_cream_cheese_butter': 64, 'T2_stove_moka_pot': 64, 'T3_black_bowl_drawer': 40, 'T4_white_mug_left_plate': 36, 'T5_book_back_shelf': 44, 'T6_white_mug_plate': 82, 'T7_alphabet_soup_cream': 30, 'T8_moka_pots_stove': 10, 'T9_yellow_white_mug_microwave': 82}}",
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_pi05_attn_k075_long_seed43_strict_cqa1_20260527T222944",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_pi05_attn_k075_long_seed43_strict_cqa1",
    "field": "metrics",
    "value": "{'success_rate': 52, 'per_task': {'T0_alphabet_soup_tomato': 68, 'T1_cream_cheese_butter': 64, 'T2_stove_moka_pot': 64, 'T3_black_bowl_drawer': 40, 'T4_white_mug_left_plate': 36, 'T5_book_back_shelf': 44, 'T6_white_mug_plate': 82, 'T7_alphabet_soup_cream': 30, 'T8_moka_pots_stove': 10, 'T9_yellow_white_mug_microwave': 82}}",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-27T22:30:57.420363+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_pi05_attn_k075_long_seed43_strict_cqa1",
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
  "session": "worker_analyze_eval_pi05_attn_k075_long_seed43_strict_cqa1_20260527T222944",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_pi05_attn_k075_long_seed43_strict_cqa1",
    "field": "status",
    "value": "DONE",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-27T22:30:57.420487+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_pi05_attn_k075_long_seed43_strict_cqa1",
  "field": "log_path",
  "value": "~/runs/importance_margin_vla_compress/eval_pi05_attn_k075_long_seed43_strict_cqa1.log",
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_pi05_attn_k075_long_seed43_strict_cqa1_20260527T222944",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_pi05_attn_k075_long_seed43_strict_cqa1",
    "field": "log_path",
    "value": "~/runs/importance_margin_vla_compress/eval_pi05_attn_k075_long_seed43_strict_cqa1.log",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-27T22:30:57.420607+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_pi05_attn_k075_long_seed43_strict_cqa1",
  "field": "checkpoint_path",
  "value": "N/A (eval only)",
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_pi05_attn_k075_long_seed43_strict_cqa1_20260527T222944",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_pi05_attn_k075_long_seed43_strict_cqa1",
    "field": "checkpoint_path",
    "value": "N/A (eval only)",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-27T22:30:57.420766+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_pi05_attn_k075_long_seed43_strict_cqa1\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-27T18:10:09.805Z\", \"updated_at\": \"2026-05-27T22:30:19.136Z\", \"hypothesis\": \"π0.5 Attn k=0.75 Long strict seed43 — seed42=52.4% 的 seed 复制，验证 Attn cliff 后平台段 error bar（w27 不支持 attention，重新部署到 cqa1）\", \"parent\": \"eval_pi05_attn_k075_long_seed42_strict_cqa1\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode attention --keep_ratio 0.75 --suite libero_10 --n_episodes 50 --seed 43 --gpu 0\\\"\", \"server\": \"cqa1-33015\", \"gpu\": \"cuda:3\", \"pid\": \"588702\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_attn_k075_long_seed43_strict_cqa1.log\", \"submitted_at\": \"2026-05-27T18:10:53.074Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"libero_10\", \"data_count\": 500, \"model_name\": \"pi0.5\", \"seed\": 43, \"checkpoint_source\": \"pi0.5 pretrained\", \"eval_data\": \"libero_10 (Long)\"}, \"server\": \"cqa1-33015\", \"gpu\": \"cuda:3\", \"reproduce\": {\"finished_at\": \"2026-05-27T22:27:41.761Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-27T22:27:58.388059+00:00\"}]}, \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.9589}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_pi05_attn_k075_long_seed43_strict_cqa1_20260527T222944",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-27T22:30:57.420949+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_pi05_attn_k075_long_seed43_strict_cqa1\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-27T18:10:09.805Z\", \"updated_at\": \"2026-05-27T22:30:22.882Z\", \"hypothesis\": \"π0.5 Attn k=0.75 Long strict seed43 — seed42=52.4% 的 seed 复制，验证 Attn cliff 后平台段 error bar（w27 不支持 attention，重新部署到 cqa1）\", \"parent\": \"eval_pi05_attn_k075_long_seed42_strict_cqa1\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode attention --keep_ratio 0.75 --suite libero_10 --n_episodes 50 --seed 43 --gpu 0\\\"\", \"server\": \"cqa1-33015\", \"gpu\": \"cuda:3\", \"pid\": \"588702\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_attn_k075_long_seed43_strict_cqa1.log\", \"submitted_at\": \"2026-05-27T18:10:53.074Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"libero_10\", \"data_count\": 500, \"model_name\": \"pi0.5\", \"seed\": 43, \"checkpoint_source\": \"pi0.5 pretrained\", \"eval_data\": \"libero_10 (Long)\"}, \"server\": \"cqa1-33015\", \"gpu\": \"cuda:3\", \"reproduce\": {\"finished_at\": \"2026-05-27T22:27:41.761Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-27T22:27:58.388059+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 52, \"per_task\": {\"T0_alphabet_soup_tomato\": 68, \"T1_cream_cheese_butter\": 64, \"T2_stove_moka_pot\": 64, \"T3_black_bowl_drawer\": 40, \"T4_white_mug_left_plate\": 36, \"T5_book_back_shelf\": 44, \"T6_white_mug_plate\": 82, \"T7_alphabet_soup_cream\": 30, \"T8_moka_pots_stove\": 10, \"T9_yellow_white_mug_microwave\": 82}}}}, \"error\": null, \"me
…[truncated 42 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_pi05_attn_k075_long_seed43_strict_cqa1_20260527T222944",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-27T22:30:57.421103+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Cannot transition to DONE without output fields: ['checkpoint_path']. Set these fields first or pass them in spec.\", \"metadata\": {\"elapsed_seconds\": 2.3404}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_pi05_attn_k075_long_seed43_strict_cqa1_20260527T222944",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-27T22:30:57.421295+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_pi05_attn_k075_long_seed43_strict_cqa1\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-27T18:10:09.805Z\", \"updated_at\": \"2026-05-27T22:30:28.863Z\", \"hypothesis\": \"π0.5 Attn k=0.75 Long strict seed43 — seed42=52.4% 的 seed 复制，验证 Attn cliff 后平台段 error bar（w27 不支持 attention，重新部署到 cqa1）\", \"parent\": \"eval_pi05_attn_k075_long_seed42_strict_cqa1\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode attention --keep_ratio 0.75 --suite libero_10 --n_episodes 50 --seed 43 --gpu 0\\\"\", \"server\": \"cqa1-33015\", \"gpu\": \"cuda:3\", \"pid\": \"588702\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_attn_k075_long_seed43_strict_cqa1.log\", \"submitted_at\": \"2026-05-27T18:10:53.074Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"libero_10\", \"data_count\": 500, \"model_name\": \"pi0.5\", \"seed\": 43, \"checkpoint_source\": \"pi0.5 pretrained\", \"eval_data\": \"libero_10 (Long)\"}, \"server\": \"cqa1-33015\", \"gpu\": \"cuda:3\", \"reproduce\": {\"finished_at\": \"2026-05-27T22:27:41.761Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-27T22:27:58.388059+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 52, \"per_task\": {\"T0_alphabet_soup_tomato\": 68, \"T1_cream_cheese_butter\": 64, \"T2_stove_moka_pot\": 64, \"T3_black_bowl_drawer\": 40, \"T4_white_mug_left_plate\": 36, \"T5_book_back_shelf\": 44, \"T6_white_mug_plate\": 82, \"T7_alphabet_soup_cream\": 30, \"T8_moka_pots_stove\": 10, \"T9_yellow_white_mug_microwave\": 82}}, \"log_path\": \"~/runs/
…[truncated 147 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_pi05_attn_k075_long_seed43_strict_cqa1_20260527T222944",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-27T22:30:57.421485+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_pi05_attn_k075_long_seed43_strict_cqa1\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-27T18:10:09.805Z\", \"updated_at\": \"2026-05-27T22:30:33.877Z\", \"hypothesis\": \"π0.5 Attn k=0.75 Long strict seed43 — seed42=52.4% 的 seed 复制，验证 Attn cliff 后平台段 error bar（w27 不支持 attention，重新部署到 cqa1）\", \"parent\": \"eval_pi05_attn_k075_long_seed42_strict_cqa1\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode attention --keep_ratio 0.75 --suite libero_10 --n_episodes 50 --seed 43 --gpu 0\\\"\", \"server\": \"cqa1-33015\", \"gpu\": \"cuda:3\", \"pid\": \"588702\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_attn_k075_long_seed43_strict_cqa1.log\", \"submitted_at\": \"2026-05-27T18:10:53.074Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"libero_10\", \"data_count\": 500, \"model_name\": \"pi0.5\", \"seed\": 43, \"checkpoint_source\": \"pi0.5 pretrained\", \"eval_data\": \"libero_10 (Long)\"}, \"server\": \"cqa1-33015\", \"gpu\": \"cuda:3\", \"reproduce\": {\"finished_at\": \"2026-05-27T22:27:41.761Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-27T22:27:58.388059+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 52, \"per_task\": {\"T0_alphabet_soup_tomato\": 68, \"T1_cream_cheese_butter\": 64, \"T2_stove_moka_pot\": 64, \"T3_black_bowl_drawer\": 40, \"T4_white_mug_left_plate\": 36, \"T5_book_back_shelf\": 44, \"T6_white_mug_plate\": 82, \"T7_alphabet_soup_cream\": 30, \"T8_moka_pots_stove\": 10, \"T9_yellow_white_mug_microwave\": 82}}, \"log_path\": \"~/runs/
…[truncated 188 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_pi05_attn_k075_long_seed43_strict_cqa1_20260527T222944",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-27T22:30:57.421651+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_pi05_attn_k075_long_seed43_strict_cqa1",
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
  "session": "worker_analyze_eval_pi05_attn_k075_long_seed43_strict_cqa1_20260527T222944",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_pi05_attn_k075_long_seed43_strict_cqa1",
    "field": "status",
    "value": "DONE",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-27T22:30:57.421850+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_pi05_attn_k075_long_seed43_strict_cqa1\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-27T18:10:09.805Z\", \"updated_at\": \"2026-05-27T22:30:42.712Z\", \"hypothesis\": \"π0.5 Attn k=0.75 Long strict seed43 — seed42=52.4% 的 seed 复制，验证 Attn cliff 后平台段 error bar（w27 不支持 attention，重新部署到 cqa1）\", \"parent\": \"eval_pi05_attn_k075_long_seed42_strict_cqa1\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode attention --keep_ratio 0.75 --suite libero_10 --n_episodes 50 --seed 43 --gpu 0\\\"\", \"server\": \"cqa1-33015\", \"gpu\": \"cuda:3\", \"pid\": \"588702\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_attn_k075_long_seed43_strict_cqa1.log\", \"submitted_at\": \"2026-05-27T18:10:53.074Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"libero_10\", \"data_count\": 500, \"model_name\": \"pi0.5\", \"seed\": 43, \"checkpoint_source\": \"pi0.5 pretrained\", \"eval_data\": \"libero_10 (Long)\", \"wall_clock_seconds\": 15589.6, \"gpu_hours\": 4.33}, \"server\": \"cqa1-33015\", \"gpu\": \"cuda:3\", \"reproduce\": {\"finished_at\": \"2026-05-27T22:27:41.761Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-27T22:27:58.388059+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 52, \"per_task\": {\"T0_alphabet_soup_tomato\": 68, \"T1_cream_cheese_butter\": 64, \"T2_stove_moka_pot\": 64, \"T3_black_bowl_drawer\": 40, \"T4_white_mug_left_plate\": 36, \"T5_book_back_shelf\": 44, \"T6_white_mug_plate\": 82, \"T7_alphabet_soup_cream\": 30, \"T8_moka_pots_stove\": 10, \"T9_yellow_whi
…[truncated 337 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_pi05_attn_k075_long_seed43_strict_cqa1_20260527T222944",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-27T22:30:57.422043+00:00_

## 结果

**π0.5 Attn k=0.75 Long seed43: SR = 52.0%**

| Task | SR |
|------|-----|
| T0 alphabet_soup_tomato | 68% |
| T1 cream_cheese_butter | 64% |
| T2 stove_moka_pot | 64% |
| T3 black_bowl_drawer | 40% |
| T4 white_mug_left_plate | 36% |
| T5 book_back_shelf | 44% |
| T6 white_mug_plate | 82% |
| T7 alphabet_soup_cream | 30% |
| T8 moka_pots_stove | 10% |
| T9 yellow_white_mug_microwave | 82% |

### 与 seed42 对比

| | seed42 | seed43 | mean±std |
|--|--------|--------|----------|
| SR | 49.8% | 52.0% | **50.9%±1.1%** |

seed43 比 seed42 高 2.2pp，两个 seed 的 mean 为 50.9%±1.1%（较之前 ROADMAP 的 49.4%±0.4 上修）。error bar 很小，确认 Attn k=0.75 plateau 稳定在 ~51% 附近。无 error/warning，EXIT_CODE=0，运行时间 253.7min（~4.2h）。Registry 已更新为 DONE。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analyze_eval_pi05_attn_k075_long_seed43_strict_cqa1_20260527T222944"
}
```

</details>

---
