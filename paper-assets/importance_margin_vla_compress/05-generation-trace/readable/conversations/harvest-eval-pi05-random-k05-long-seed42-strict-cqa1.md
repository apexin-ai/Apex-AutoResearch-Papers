# harvest eval pi05 random k05 long seed42 strict cqa1

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 21
- **Recorded user turns:** 0
- **Tool calls:** 10
- **Original source:** `logs/chats/worker_harvest_eval_pi05_random_k05_long_seed42_strict_cqa1_20260527T133212.jsonl`
- **Structured JSON:** [`8c6aac667bbc7fa0fc88.json`](../../sessions/8c/8c6aac667bbc7fa0fc88.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

21 recorded events

### Tool call

_source line 1 · 2026-05-27T13:34:03.717662+00:00_

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
  "session": "worker_harvest_eval_pi05_random_k05_long_seed42_strict_cqa1_20260527T133212",
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

_source line 2 · 2026-05-27T13:34:03.718124+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_eval_pi05_random_k05_long_seed42_strict_cqa1_20260527T133212",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-27T13:34:03.718415+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-33015",
  "command": "tail -200 ~/runs/importance_margin_vla_compress/eval_pi05_random_k05_long_seed42_strict.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_eval_pi05_random_k05_long_seed42_strict_cqa1_20260527T133212",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-33015",
    "command": "tail -200 ~/runs/importance_margin_vla_compress/eval_pi05_random_k05_long_seed42_strict.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-27T13:34:03.718766+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-27 16:33:07,623 Config: suite=libero_10, prune=random, keep=0.5, eps=50, gpu=0\\n2026-05-27 16:33:07,623 Loading pi0.5 from /root/autodl-tmp/pi05_libero_finetuned ...\\n2026-05-27 16:33:08,359 JAX version 0.10.0 available.\\nThe PI05 model is a direct port of the OpenPI implementation. \\nThis implementation follows the original OpenPI structure for compatibility. \\nOriginal implementation: https://github.com/Physical-Intelligence/openpi\\n2026-05-27 16:35:45,042 Enabled gradient checkpointing for PI05Pytorch model\\nLoading model from: /root/autodl-tmp/pi05_libero_finetuned\\n✓ Loaded state dict from model.safetensors\\n2026-05-27 16:35:51,846 Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embedding.bias\\n2026-05-27 16:35:51,846 Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embedding.weight\\nAll keys loaded successfully!\\n2026-05-27 16:35:56,611 Patched embed_image\\n2026-05-27 16:35:56,626 Model: 4143.4M params\\n2026-05-27 16:35:56,626 Vision tokens: 256/image, 3 slots -> 768 total\\n2026-05-27 16:35:56,626 Pruning: random, keep 128/256 tokens/image (384 total)\\n2026-05-27 16:35:58,535 Preprocessor/postprocessor loaded\\n[robosuite WARNING] No private macro file found! (macros.py:53)\\n2026-05-27 16:35:58,579 No private macro file found!\\n[robosuite WARNING] It is recommended to use a private macro file (macros.py:54)\\n2026-05-27 16:35:58,579 It is recommended to use a private macro file\\n[robosuite WARNING] To setup, run: python /root/miniconda3/lib/python3.12/site-packages/robosuite/scripts/setup_macros.py (macros.py:55)\\n2026-05-27 16:35:58,579 To setup, run: python /root/miniconda3/lib/python3.12/site-packages/robosuite/scripts/setup_macros.py\\n2026-05-27 16:35:58,653 No OpenGL_accelerate module loaded: No module named 'Open
…[truncated 6226 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_eval_pi05_random_k05_long_seed42_strict_cqa1_20260527T133212",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-27T13:34:03.719075+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_pi05_random_k05_long_seed42_strict",
  "field": "status",
  "value": "PENDING",
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_eval_pi05_random_k05_long_seed42_strict_cqa1_20260527T133212",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_pi05_random_k05_long_seed42_strict",
    "field": "status",
    "value": "PENDING",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-27T13:34:03.719370+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_pi05_random_k05_long_seed42_strict\", \"experiment\": {\"status\": \"PENDING\", \"retry_count\": 0, \"created_at\": \"2026-05-27T07:08:23.304Z\", \"updated_at\": \"2026-05-27T13:32:44.409Z\", \"hypothesis\": \"π0.5 Random k=0.5 Long strict cqa1 — cqa1 宽松条件值 50.2% 的 strict 重跑。极端压缩点三方法对比：L2norm=50.0%, Attn=49.8%, Random=?\", \"parent\": \"eval_pi05_random_k075_long_seed42_strict\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && CUDA_VISIBLE_DEVICES=1 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.5 --suite libero_10 --n_episodes 50 --seed 42 --gpu 0\\\"\", \"server\": \"cqa1-33015\", \"gpu\": [\"cuda:1\"], \"pid\": \"118726\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_random_k05_long_seed42_strict.log\", \"submitted_at\": \"2026-05-27T08:33:04.941Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"reproduce\": {\"finished_at\": \"2026-05-27T13:05:03.069Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-27T13:05:15.394964+00:00\"}]}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 10.2848, \"warnings\": [\"report refresh failed: 'str' object has no attribute 'keys'\"]}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_eval_pi05_random_k05_long_seed42_strict_cqa1_20260527T133212",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-27T13:34:03.719621+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_pi05_random_k05_long_seed42_strict",
  "field": "status",
  "value": "QUEUED",
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_eval_pi05_random_k05_long_seed42_strict_cqa1_20260527T133212",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_pi05_random_k05_long_seed42_strict",
    "field": "status",
    "value": "QUEUED",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-27T13:34:03.719875+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_pi05_random_k05_long_seed42_strict\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-27T07:08:23.304Z\", \"updated_at\": \"2026-05-27T13:32:57.530Z\", \"hypothesis\": \"π0.5 Random k=0.5 Long strict cqa1 — cqa1 宽松条件值 50.2% 的 strict 重跑。极端压缩点三方法对比：L2norm=50.0%, Attn=49.8%, Random=?\", \"parent\": \"eval_pi05_random_k075_long_seed42_strict\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && CUDA_VISIBLE_DEVICES=1 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.5 --suite libero_10 --n_episodes 50 --seed 42 --gpu 0\\\"\", \"server\": \"cqa1-33015\", \"gpu\": [\"cuda:1\"], \"pid\": \"118726\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_random_k05_long_seed42_strict.log\", \"submitted_at\": \"2026-05-27T08:33:04.941Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"reproduce\": {\"finished_at\": \"2026-05-27T13:05:03.069Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-27T13:05:15.394964+00:00\"}]}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 12.06, \"warnings\": [\"report refresh failed: 'str' object has no attribute 'keys'\"]}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_eval_pi05_random_k05_long_seed42_strict_cqa1_20260527T133212",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-27T13:34:03.720108+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_pi05_random_k05_long_seed42_strict",
  "field": "status",
  "value": "RUNNING",
  "project": "importance_margin_vla_compress",
  "spec": "{'command': 'bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && CUDA_VISIBLE_DEVICES=1 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.5 --suite libero_10 --n_episodes 50 --seed 42 --gpu 0\"', 'server': 'cqa1-33015', 'data_path': 'libero_10', 'data_count': 500, 'model_name': 'pi0.5', 'seed': 42, 'checkpoint_source': '/root/autodl-tmp/pi05_libero_finetuned', 'eval_data': 'libero_10'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_eval_pi05_random_k05_long_seed42_strict_cqa1_20260527T133212",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_pi05_random_k05_long_seed42_strict",
    "field": "status",
    "value": "RUNNING",
    "project": "importance_margin_vla_compress",
    "spec": "{'command': 'bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && CUDA_VISIBLE_DEVICES=1 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.5 --suite libero_10 --n_episodes 50 --seed 42 --gpu 0\"', 'server': 'cqa1-33015', 'data_path': 'libero_10', 'data_count': 500, 'model_name': 'pi0.5', 'seed': 42, 'checkpoint_source': '/root/autodl-tmp/pi05_libero_finetuned', 'eval_data': 'libero_10'}"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-27T13:34:03.720427+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_pi05_random_k05_long_seed42_strict\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-27T07:08:23.304Z\", \"updated_at\": \"2026-05-27T13:33:16.384Z\", \"hypothesis\": \"π0.5 Random k=0.5 Long strict cqa1 — cqa1 宽松条件值 50.2% 的 strict 重跑。极端压缩点三方法对比：L2norm=50.0%, Attn=49.8%, Random=?\", \"parent\": \"eval_pi05_random_k075_long_seed42_strict\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && CUDA_VISIBLE_DEVICES=1 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.5 --suite libero_10 --n_episodes 50 --seed 42 --gpu 0\\\"\", \"server\": \"cqa1-33015\", \"gpu\": [\"cuda:1\"], \"pid\": \"118726\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_random_k05_long_seed42_strict.log\", \"submitted_at\": \"2026-05-27T08:33:04.941Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"libero_10\", \"data_count\": 500, \"model_name\": \"pi0.5\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/pi05_libero_finetuned\", \"eval_data\": \"libero_10\"}, \"reproduce\": {\"finished_at\": \"2026-05-27T13:05:03.069Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-27T13:05:15.394964+00:00\"}]}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 11.128, \"warnings\": [\"report refresh failed: 'str' object has no attribute 'keys'\"]}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_eval_pi05_random_k05_long_seed42_strict_cqa1_20260527T133212",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-27T13:34:03.720715+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_pi05_random_k05_long_seed42_strict",
  "field": "metrics",
  "value": "{'avg_success_rate': 50.2, 'total_episodes': 500, 'total_success': 251, 'elapsed_min': 268.9, 'per_task': {'T0_alphabet_soup_tomato': 84, 'T1_cream_cheese_butter': 32, 'T2_stove_moka_pot': 64, 'T3_black_bowl_drawer': 72, 'T4_white_mug_left_plate': 74, 'T5_book_back_shelf': 38, 'T6_white_mug_plate': 30, 'T7_alphabet_soup_cream': 54, 'T8_moka_pots_stove': 4, 'T9_yellow_white_mug_microwave': 50}}",
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_eval_pi05_random_k05_long_seed42_strict_cqa1_20260527T133212",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_pi05_random_k05_long_seed42_strict",
    "field": "metrics",
    "value": "{'avg_success_rate': 50.2, 'total_episodes': 500, 'total_success': 251, 'elapsed_min': 268.9, 'per_task': {'T0_alphabet_soup_tomato': 84, 'T1_cream_cheese_butter': 32, 'T2_stove_moka_pot': 64, 'T3_black_bowl_drawer': 72, 'T4_white_mug_left_plate': 74, 'T5_book_back_shelf': 38, 'T6_white_mug_plate': 30, 'T7_alphabet_soup_cream': 54, 'T8_moka_pots_stove': 4, 'T9_yellow_white_mug_microwave': 50}}",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-27T13:34:03.720948+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_pi05_random_k05_long_seed42_strict",
  "field": "log_path",
  "value": "/root/runs/importance_margin_vla_compress/eval_pi05_random_k05_long_seed42_strict.log",
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_eval_pi05_random_k05_long_seed42_strict_cqa1_20260527T133212",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_pi05_random_k05_long_seed42_strict",
    "field": "log_path",
    "value": "/root/runs/importance_margin_vla_compress/eval_pi05_random_k05_long_seed42_strict.log",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-27T13:34:03.721177+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_pi05_random_k05_long_seed42_strict",
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
  "session": "worker_harvest_eval_pi05_random_k05_long_seed42_strict_cqa1_20260527T133212",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_pi05_random_k05_long_seed42_strict",
    "field": "checkpoint_path",
    "value": "N/A (eval only)",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-27T13:34:03.721464+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_pi05_random_k05_long_seed42_strict\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-27T07:08:23.304Z\", \"updated_at\": \"2026-05-27T13:33:32.511Z\", \"hypothesis\": \"π0.5 Random k=0.5 Long strict cqa1 — cqa1 宽松条件值 50.2% 的 strict 重跑。极端压缩点三方法对比：L2norm=50.0%, Attn=49.8%, Random=?\", \"parent\": \"eval_pi05_random_k075_long_seed42_strict\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && CUDA_VISIBLE_DEVICES=1 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.5 --suite libero_10 --n_episodes 50 --seed 42 --gpu 0\\\"\", \"server\": \"cqa1-33015\", \"gpu\": [\"cuda:1\"], \"pid\": \"118726\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_random_k05_long_seed42_strict.log\", \"submitted_at\": \"2026-05-27T08:33:04.941Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"libero_10\", \"data_count\": 500, \"model_name\": \"pi0.5\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/pi05_libero_finetuned\", \"eval_data\": \"libero_10\"}, \"reproduce\": {\"finished_at\": \"2026-05-27T13:05:03.069Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-27T13:05:15.394964+00:00\"}]}, \"metrics\": {\"avg_success_rate\": 50.2, \"total_episodes\": 500, \"total_success\": 251, \"elapsed_min\": 268.9, \"per_task\": {\"T0_alphabet_soup_tomato\": 84, \"T1_cream_cheese_butter\": 32, \"T2_stove_moka_pot\": 64, \"T3_black_bowl_drawer\": 72, \"T4_white_mug_left_plate\": 74, \"T5_book_back_shelf\": 38, \"T6_white_mug_plate\": 30, \"T7_alphabet_soup_cream\": 54, \"T8_moka_pots_stove\": 4, \"T9_yellow_white_mug_microwave\": 50}}}}, \"erro
…[truncated 57 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_eval_pi05_random_k05_long_seed42_strict_cqa1_20260527T133212",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-27T13:34:03.721776+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_pi05_random_k05_long_seed42_strict\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-27T07:08:23.304Z\", \"updated_at\": \"2026-05-27T13:33:35.933Z\", \"hypothesis\": \"π0.5 Random k=0.5 Long strict cqa1 — cqa1 宽松条件值 50.2% 的 strict 重跑。极端压缩点三方法对比：L2norm=50.0%, Attn=49.8%, Random=?\", \"parent\": \"eval_pi05_random_k075_long_seed42_strict\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && CUDA_VISIBLE_DEVICES=1 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.5 --suite libero_10 --n_episodes 50 --seed 42 --gpu 0\\\"\", \"server\": \"cqa1-33015\", \"gpu\": [\"cuda:1\"], \"pid\": \"118726\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_random_k05_long_seed42_strict.log\", \"submitted_at\": \"2026-05-27T08:33:04.941Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"libero_10\", \"data_count\": 500, \"model_name\": \"pi0.5\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/pi05_libero_finetuned\", \"eval_data\": \"libero_10\"}, \"reproduce\": {\"finished_at\": \"2026-05-27T13:05:03.069Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-27T13:05:15.394964+00:00\"}]}, \"metrics\": {\"avg_success_rate\": 50.2, \"total_episodes\": 500, \"total_success\": 251, \"elapsed_min\": 268.9, \"per_task\": {\"T0_alphabet_soup_tomato\": 84, \"T1_cream_cheese_butter\": 32, \"T2_stove_moka_pot\": 64, \"T3_black_bowl_drawer\": 72, \"T4_white_mug_left_plate\": 74, \"T5_book_back_shelf\": 38, \"T6_white_mug_plate\": 30, \"T7_alphabet_soup_cream\": 54, \"T8_moka_pots_stove\": 4, \"T9_yellow_white_mug_microwave\": 50}}, \"log_pa
…[truncated 162 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_eval_pi05_random_k05_long_seed42_strict_cqa1_20260527T133212",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-27T13:34:03.722092+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_pi05_random_k05_long_seed42_strict\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-27T07:08:23.304Z\", \"updated_at\": \"2026-05-27T13:33:39.249Z\", \"hypothesis\": \"π0.5 Random k=0.5 Long strict cqa1 — cqa1 宽松条件值 50.2% 的 strict 重跑。极端压缩点三方法对比：L2norm=50.0%, Attn=49.8%, Random=?\", \"parent\": \"eval_pi05_random_k075_long_seed42_strict\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && CUDA_VISIBLE_DEVICES=1 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.5 --suite libero_10 --n_episodes 50 --seed 42 --gpu 0\\\"\", \"server\": \"cqa1-33015\", \"gpu\": [\"cuda:1\"], \"pid\": \"118726\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_random_k05_long_seed42_strict.log\", \"submitted_at\": \"2026-05-27T08:33:04.941Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"libero_10\", \"data_count\": 500, \"model_name\": \"pi0.5\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/pi05_libero_finetuned\", \"eval_data\": \"libero_10\"}, \"reproduce\": {\"finished_at\": \"2026-05-27T13:05:03.069Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-27T13:05:15.394964+00:00\"}]}, \"metrics\": {\"avg_success_rate\": 50.2, \"total_episodes\": 500, \"total_success\": 251, \"elapsed_min\": 268.9, \"per_task\": {\"T0_alphabet_soup_tomato\": 84, \"T1_cream_cheese_butter\": 32, \"T2_stove_moka_pot\": 64, \"T3_black_bowl_drawer\": 72, \"T4_white_mug_left_plate\": 74, \"T5_book_back_shelf\": 38, \"T6_white_mug_plate\": 30, \"T7_alphabet_soup_cream\": 54, \"T8_moka_pots_stove\": 4, \"T9_yellow_white_mug_microwave\": 50}}, \"log_pa
…[truncated 203 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_eval_pi05_random_k05_long_seed42_strict_cqa1_20260527T133212",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-27T13:34:03.722369+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_pi05_random_k05_long_seed42_strict",
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
  "session": "worker_harvest_eval_pi05_random_k05_long_seed42_strict_cqa1_20260527T133212",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_pi05_random_k05_long_seed42_strict",
    "field": "conclusion",
    "value": "success",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-27T13:34:03.722781+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_pi05_random_k05_long_seed42_strict\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-27T07:08:23.304Z\", \"updated_at\": \"2026-05-27T13:33:46.494Z\", \"hypothesis\": \"π0.5 Random k=0.5 Long strict cqa1 — cqa1 宽松条件值 50.2% 的 strict 重跑。极端压缩点三方法对比：L2norm=50.0%, Attn=49.8%, Random=?\", \"parent\": \"eval_pi05_random_k075_long_seed42_strict\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && CUDA_VISIBLE_DEVICES=1 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.5 --suite libero_10 --n_episodes 50 --seed 42 --gpu 0\\\"\", \"server\": \"cqa1-33015\", \"gpu\": [\"cuda:1\"], \"pid\": \"118726\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_random_k05_long_seed42_strict.log\", \"submitted_at\": \"2026-05-27T08:33:04.941Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"libero_10\", \"data_count\": 500, \"model_name\": \"pi0.5\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/pi05_libero_finetuned\", \"eval_data\": \"libero_10\"}, \"reproduce\": {\"finished_at\": \"2026-05-27T13:05:03.069Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-27T13:05:15.394964+00:00\"}]}, \"metrics\": {\"avg_success_rate\": 50.2, \"total_episodes\": 500, \"total_success\": 251, \"elapsed_min\": 268.9, \"per_task\": {\"T0_alphabet_soup_tomato\": 84, \"T1_cream_cheese_butter\": 32, \"T2_stove_moka_pot\": 64, \"T3_black_bowl_drawer\": 72, \"T4_white_mug_left_plate\": 74, \"T5_book_back_shelf\": 38, \"T6_white_mug_plate\": 30, \"T7_alphabet_soup_cream\": 54, \"T8_moka_pots_stove\": 4, \"T9_yellow_white_mug_microwave\": 50}}, \"log_pa
…[truncated 233 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_eval_pi05_random_k05_long_seed42_strict_cqa1_20260527T133212",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-27T13:34:03.723032+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_pi05_random_k05_long_seed42_strict",
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
  "session": "worker_harvest_eval_pi05_random_k05_long_seed42_strict_cqa1_20260527T133212",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_pi05_random_k05_long_seed42_strict",
    "field": "status",
    "value": "DONE",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-27T13:34:03.723370+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_pi05_random_k05_long_seed42_strict\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-27T07:08:23.304Z\", \"updated_at\": \"2026-05-27T13:33:52.811Z\", \"hypothesis\": \"π0.5 Random k=0.5 Long strict cqa1 — cqa1 宽松条件值 50.2% 的 strict 重跑。极端压缩点三方法对比：L2norm=50.0%, Attn=49.8%, Random=?\", \"parent\": \"eval_pi05_random_k075_long_seed42_strict\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && CUDA_VISIBLE_DEVICES=1 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.5 --suite libero_10 --n_episodes 50 --seed 42 --gpu 0\\\"\", \"server\": \"cqa1-33015\", \"gpu\": [\"cuda:1\"], \"pid\": \"118726\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_random_k05_long_seed42_strict.log\", \"submitted_at\": \"2026-05-27T08:33:04.941Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"libero_10\", \"data_count\": 500, \"model_name\": \"pi0.5\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/pi05_libero_finetuned\", \"eval_data\": \"libero_10\", \"wall_clock_seconds\": 18047.9, \"gpu_hours\": 5.01}, \"reproduce\": {\"finished_at\": \"2026-05-27T13:05:03.069Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-27T13:05:15.394964+00:00\"}]}, \"metrics\": {\"avg_success_rate\": 50.2, \"total_episodes\": 500, \"total_success\": 251, \"elapsed_min\": 268.9, \"per_task\": {\"T0_alphabet_soup_tomato\": 84, \"T1_cream_cheese_butter\": 32, \"T2_stove_moka_pot\": 64, \"T3_black_bowl_drawer\": 72, \"T4_white_mug_left_plate\": 74, \"T5_book_back_shelf\": 38, \"T6_white_mug_plate\": 30, \"T7_alphabet_soup_cream\": 54, \"T8_moka_pots_stove\": 4
…[truncated 464 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_eval_pi05_random_k05_long_seed42_strict_cqa1_20260527T133212",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-27T13:34:03.723683+00:00_

Registry 已更新至 DONE (success)。

**结果汇总：π0.5 Random k=0.5 Long strict (cqa1)**
- **SR = 50.2%** (251/500), 耗时 268.9 min, EXIT_CODE=0
- Per-task: T0=84%, T1=32%, T2=64%, T3=72%, T4=74%, T5=38%, T6=30%, T7=54%, T8=4%, T9=50%
- 与 D261 (westd-41074 v2) 的 49.8% 非常接近，差异仅 0.4pp，结果一致性好
- k=0.5 极端压缩点三方法对比：L2norm=50.0%, Attn=49.8%, Random=50.2%，三者几乎无差异

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_harvest_eval_pi05_random_k05_long_seed42_strict_cqa1_20260527T133212"
}
```

</details>

---
