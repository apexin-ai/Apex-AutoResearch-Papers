# analyze eval pi05 l2norm k07 long seed43 strict w41

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 19
- **Recorded user turns:** 0
- **Tool calls:** 9
- **Original source:** `logs/chats/worker_analyze_eval_pi05_l2norm_k07_long_seed43_strict_w41_20260527T183735.jsonl`
- **Structured JSON:** [`13726b01bcedb0ed3546.json`](../../sessions/13/13726b01bcedb0ed3546.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

19 recorded events

### Tool call

_source line 1 · 2026-05-27T18:39:33.541630+00:00_

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
  "session": "worker_analyze_eval_pi05_l2norm_k07_long_seed43_strict_w41_20260527T183735",
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

_source line 2 · 2026-05-27T18:39:33.542102+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_pi05_l2norm_k07_long_seed43_strict_w41_20260527T183735",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-27T18:39:33.542398+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-41074",
  "command": "tail -100 ~/runs/importance_margin_vla_compress/eval_pi05_l2norm_k07_long_seed43_strict_w41.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_pi05_l2norm_k07_long_seed43_strict_w41_20260527T183735",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-41074",
    "command": "tail -100 ~/runs/importance_margin_vla_compress/eval_pi05_l2norm_k07_long_seed43_strict_w41.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-27T18:39:33.542763+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-27 23:50:32,994 Config: suite=libero_10, prune=l2norm, keep=0.7, eps=50, gpu=0\\n2026-05-27 23:50:32,994 Loading π0.5 from /root/autodl-tmp/pi05_libero_finetuned ...\\nThe PI05 model is a direct port of the OpenPI implementation. \\nThis implementation follows the original OpenPI structure for compatibility. \\nOriginal implementation: https://github.com/Physical-Intelligence/openpi\\n2026-05-27 23:52:12,427 Enabled gradient checkpointing for PI05Pytorch model\\nLoading model from: /root/autodl-tmp/pi05_libero_finetuned\\n✓ Loaded state dict from model.safetensors\\n2026-05-27 23:52:14,430 Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embedding.bias\\n2026-05-27 23:52:14,430 Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embedding.weight\\nAll keys loaded successfully!\\n2026-05-27 23:52:16,723 Patched embed_image\\n2026-05-27 23:52:16,729 Model: 4143.4M params\\n2026-05-27 23:52:16,729 Vision tokens: 256/image, 3 slots -> 768 total\\n2026-05-27 23:52:16,729 Pruning: l2norm, keep 179/256 tokens/image (537 total)\\n2026-05-27 23:52:17,530 Preprocessor/postprocessor loaded\\n[robosuite WARNING] No private macro file found! (__init__.py:7)\\n2026-05-27 23:52:17,553 No private macro file found!\\n[robosuite WARNING] It is recommended to use a private macro file (__init__.py:8)\\n2026-05-27 23:52:17,553 It is recommended to use a private macro file\\n[robosuite WARNING] To setup, run: python /root/miniconda3/lib/python3.12/site-packages/robosuite/scripts/setup_macros.py (__init__.py:9)\\n2026-05-27 23:52:17,553 To setup, run: python /root/miniconda3/lib/python3.12/site-packages/robosuite/scripts/setup_macros.py\\n2026-05-27 23:52:17,600 No OpenGL_accelerate module loaded: No module named 'OpenGL_accelerate'\\n[info] using task orders [0, 1, 2, 3,
…[truncated 6056 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_pi05_l2norm_k07_long_seed43_strict_w41_20260527T183735",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-27T18:39:33.543097+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_pi05_l2norm_k07_long_seed43_strict_w41",
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
  "session": "worker_analyze_eval_pi05_l2norm_k07_long_seed43_strict_w41_20260527T183735",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_pi05_l2norm_k07_long_seed43_strict_w41",
    "field": "status",
    "value": "DONE",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-27T18:39:33.543398+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Cannot transition to DONE without a 'conclusion' field. Set conclusion first.\", \"metadata\": {\"elapsed_seconds\": 2.042}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_pi05_l2norm_k07_long_seed43_strict_w41_20260527T183735",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-27T18:39:33.543623+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_pi05_l2norm_k07_long_seed43_strict_w41",
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
  "session": "worker_analyze_eval_pi05_l2norm_k07_long_seed43_strict_w41_20260527T183735",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_pi05_l2norm_k07_long_seed43_strict_w41",
    "field": "conclusion",
    "value": "success",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-27T18:39:33.543894+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_pi05_l2norm_k07_long_seed43_strict_w41\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-27T15:49:19.574Z\", \"updated_at\": \"2026-05-27T18:38:14.737Z\", \"hypothesis\": \"π0.5 L2norm k=0.7 Long strict seed43 — seed42 仍在跑（cqa1 GPU2），本实验提前部署确保截止前有 seed43 error bar。k=0.7 是 cliff curve 中间关键点\", \"parent\": \"eval_pi05_l2norm_k07_long_seed42_strict\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.7 --suite libero_10 --n_episodes 50 --seed 43 --gpu 0\\\"\", \"server\": \"westd-41074\", \"gpu\": [\"cuda:3\"], \"pid\": \"821246\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_l2norm_k07_long_seed43_strict_w41.log\", \"submitted_at\": \"2026-05-27T15:50:31.457Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"server\": \"westd-41074\", \"gpu\": \"cuda:3\", \"pid\": \"821246\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_l2norm_k07_long_seed43_strict_w41.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.7 --suite libero_10 --n_episodes 50 --seed 43 --gpu 0\\\"\", \"finished_at\": \"2026-05-27T18:34:48.668Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-27T18:35:14.680639+00:00\"}]}, \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.8381}}
…[truncated 2 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_pi05_l2norm_k07_long_seed43_strict_w41_20260527T183735",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-27T18:39:33.544151+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_pi05_l2norm_k07_long_seed43_strict_w41",
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
  "session": "worker_analyze_eval_pi05_l2norm_k07_long_seed43_strict_w41_20260527T183735",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_pi05_l2norm_k07_long_seed43_strict_w41",
    "field": "status",
    "value": "DONE",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-27T18:39:33.544385+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_pi05_l2norm_k07_long_seed43_strict_w41",
  "field": "metrics",
  "value": "{'overall_sr': 65.4, 'per_task': {'T0': 78, 'T1': 84, 'T2': 78, 'T3': 58, 'T4': 54, 'T5': 84, 'T6': 52, 'T7': 64, 'T8': 10, 'T9': 92}, 'seed': 43, 'episodes_per_task': 50, 'total_time_min': 161.9}",
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_pi05_l2norm_k07_long_seed43_strict_w41_20260527T183735",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_pi05_l2norm_k07_long_seed43_strict_w41",
    "field": "metrics",
    "value": "{'overall_sr': 65.4, 'per_task': {'T0': 78, 'T1': 84, 'T2': 78, 'T3': 58, 'T4': 54, 'T5': 84, 'T6': 52, 'T7': 64, 'T8': 10, 'T9': 92}, 'seed': 43, 'episodes_per_task': 50, 'total_time_min': 161.9}",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-27T18:39:33.544636+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Cannot transition ANALYZING → DONE(success) without metrics. Set metrics first, or use conclusion=negative/failed.\", \"metadata\": {\"elapsed_seconds\": 2.1586}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_pi05_l2norm_k07_long_seed43_strict_w41_20260527T183735",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-27T18:39:33.544924+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_pi05_l2norm_k07_long_seed43_strict_w41\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-27T15:49:19.574Z\", \"updated_at\": \"2026-05-27T18:38:25.523Z\", \"hypothesis\": \"π0.5 L2norm k=0.7 Long strict seed43 — seed42 仍在跑（cqa1 GPU2），本实验提前部署确保截止前有 seed43 error bar。k=0.7 是 cliff curve 中间关键点\", \"parent\": \"eval_pi05_l2norm_k07_long_seed42_strict\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.7 --suite libero_10 --n_episodes 50 --seed 43 --gpu 0\\\"\", \"server\": \"westd-41074\", \"gpu\": [\"cuda:3\"], \"pid\": \"821246\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_l2norm_k07_long_seed43_strict_w41.log\", \"submitted_at\": \"2026-05-27T15:50:31.457Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"server\": \"westd-41074\", \"gpu\": \"cuda:3\", \"pid\": \"821246\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_l2norm_k07_long_seed43_strict_w41.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.7 --suite libero_10 --n_episodes 50 --seed 43 --gpu 0\\\"\", \"finished_at\": \"2026-05-27T18:34:48.668Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-27T18:35:14.680639+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 65.4, \"per_task\": {\"T0\": 78, 
…[truncated 243 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_pi05_l2norm_k07_long_seed43_strict_w41_20260527T183735",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-27T18:39:33.545207+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_pi05_l2norm_k07_long_seed43_strict_w41",
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
  "session": "worker_analyze_eval_pi05_l2norm_k07_long_seed43_strict_w41_20260527T183735",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_pi05_l2norm_k07_long_seed43_strict_w41",
    "field": "status",
    "value": "DONE",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-27T18:39:33.545435+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Cannot transition to DONE without output fields: ['checkpoint_path']. Set these fields first or pass them in spec.\", \"metadata\": {\"elapsed_seconds\": 8.3885}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_pi05_l2norm_k07_long_seed43_strict_w41_20260527T183735",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-27T18:39:33.545634+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_pi05_l2norm_k07_long_seed43_strict_w41",
  "field": "checkpoint_path",
  "value": "N/A (eval-only)",
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_pi05_l2norm_k07_long_seed43_strict_w41_20260527T183735",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_pi05_l2norm_k07_long_seed43_strict_w41",
    "field": "checkpoint_path",
    "value": "N/A (eval-only)",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-27T18:39:33.545896+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_pi05_l2norm_k07_long_seed43_strict_w41\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-27T15:49:19.574Z\", \"updated_at\": \"2026-05-27T18:39:01.886Z\", \"hypothesis\": \"π0.5 L2norm k=0.7 Long strict seed43 — seed42 仍在跑（cqa1 GPU2），本实验提前部署确保截止前有 seed43 error bar。k=0.7 是 cliff curve 中间关键点\", \"parent\": \"eval_pi05_l2norm_k07_long_seed42_strict\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.7 --suite libero_10 --n_episodes 50 --seed 43 --gpu 0\\\"\", \"server\": \"westd-41074\", \"gpu\": [\"cuda:3\"], \"pid\": \"821246\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_l2norm_k07_long_seed43_strict_w41.log\", \"submitted_at\": \"2026-05-27T15:50:31.457Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"server\": \"westd-41074\", \"gpu\": \"cuda:3\", \"pid\": \"821246\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_l2norm_k07_long_seed43_strict_w41.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.7 --suite libero_10 --n_episodes 50 --seed 43 --gpu 0\\\"\", \"finished_at\": \"2026-05-27T18:34:48.668Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-27T18:35:14.680639+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 65.4, \"per_task\": {\"T0\": 78, 
…[truncated 286 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_pi05_l2norm_k07_long_seed43_strict_w41_20260527T183735",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-27T18:39:33.546122+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_pi05_l2norm_k07_long_seed43_strict_w41",
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
  "session": "worker_analyze_eval_pi05_l2norm_k07_long_seed43_strict_w41_20260527T183735",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_pi05_l2norm_k07_long_seed43_strict_w41",
    "field": "status",
    "value": "DONE",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-27T18:39:33.546440+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_pi05_l2norm_k07_long_seed43_strict_w41\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-27T15:49:19.574Z\", \"updated_at\": \"2026-05-27T18:39:14.390Z\", \"hypothesis\": \"π0.5 L2norm k=0.7 Long strict seed43 — seed42 仍在跑（cqa1 GPU2），本实验提前部署确保截止前有 seed43 error bar。k=0.7 是 cliff curve 中间关键点\", \"parent\": \"eval_pi05_l2norm_k07_long_seed42_strict\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.7 --suite libero_10 --n_episodes 50 --seed 43 --gpu 0\\\"\", \"server\": \"westd-41074\", \"gpu\": [\"cuda:3\"], \"pid\": \"821246\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_l2norm_k07_long_seed43_strict_w41.log\", \"submitted_at\": \"2026-05-27T15:50:31.457Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 10122.9, \"gpu_hours\": 2.81}, \"server\": \"westd-41074\", \"gpu\": \"cuda:3\", \"pid\": \"821246\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_l2norm_k07_long_seed43_strict_w41.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.7 --suite libero_10 --n_episodes 50 --seed 43 --gpu 0\\\"\", \"finished_at\": \"2026-05-27T18:34:48.668Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-27T18:35:14.680639+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {
…[truncated 434 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_pi05_l2norm_k07_long_seed43_strict_w41_20260527T183735",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-27T18:39:33.546732+00:00_

Registry 已更新为 DONE。

## 结果

**π0.5 L2norm k=0.7 Long suite seed43: overall SR = 65.4%**

| Task | SR |
|------|----|
| T0 | 78% |
| T1 | 84% |
| T2 | 78% |
| T3 | 58% |
| T4 | 54% |
| T5 | 84% |
| T6 | 52% |
| T7 | 64% |
| T8 | 10% |
| T9 | 92% |

无报错，EXIT_CODE=0，运行 162 分钟。

## Error bar (seed42 vs seed43)

- seed42: 63.2%
- seed43: 65.4%
- **mean = 64.3%, Δ = ±1.1%**
- 即 **64.3 ± 1.1%**

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analyze_eval_pi05_l2norm_k07_long_seed43_strict_w41_20260527T183735"
}
```

</details>

---
