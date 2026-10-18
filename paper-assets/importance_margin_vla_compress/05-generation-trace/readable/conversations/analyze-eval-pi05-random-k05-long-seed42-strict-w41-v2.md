# analyze eval pi05 random k05 long seed42 strict w41 v2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 0
- **Tool calls:** 6
- **Original source:** `logs/chats/worker_analyze_eval_pi05_random_k05_long_seed42_strict_w41_v2_20260527T120416.jsonl`
- **Structured JSON:** [`357f7fbd52b86a3e1926.json`](../../sessions/35/357f7fbd52b86a3e1926.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

13 recorded events

### Tool call

_source line 1 · 2026-05-27T12:05:14.483022+00:00_

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
  "session": "worker_analyze_eval_pi05_random_k05_long_seed42_strict_w41_v2_20260527T120416",
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

_source line 2 · 2026-05-27T12:05:14.483492+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_pi05_random_k05_long_seed42_strict_w41_v2_20260527T120416",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-27T12:05:14.483756+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-41074",
  "command": "tail -200 ~/runs/importance_margin_vla_compress/eval_pi05_random_k05_long_seed42_strict_w41_v2.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_pi05_random_k05_long_seed42_strict_w41_v2_20260527T120416",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-41074",
    "command": "tail -200 ~/runs/importance_margin_vla_compress/eval_pi05_random_k05_long_seed42_strict_w41_v2.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-27T12:05:14.484107+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-27 17:17:58,421 Config: suite=libero_10, prune=random, keep=0.5, eps=50, gpu=0\\n2026-05-27 17:17:58,421 Loading π0.5 from /root/autodl-tmp/pi05_libero_finetuned ...\\n2026-05-27 17:19:31,658 Enabled gradient checkpointing for PI05Pytorch model\\n2026-05-27 17:19:33,628 Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embedding.bias\\n2026-05-27 17:19:33,628 Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embedding.weight\\n2026-05-27 17:19:35,532 Patched embed_image\\n2026-05-27 17:19:35,538 Model: 4143.4M params\\n2026-05-27 17:19:35,538 Vision tokens: 256/image, 3 slots -> 768 total\\n2026-05-27 17:19:35,538 Pruning: random, keep 128/256 tokens/image (384 total)\\n2026-05-27 17:19:36,289 Preprocessor/postprocessor loaded\\n[robosuite WARNING] No private macro file found! (__init__.py:7)\\n2026-05-27 17:19:36,309 No private macro file found!\\n[robosuite WARNING] It is recommended to use a private macro file (__init__.py:8)\\n2026-05-27 17:19:36,309 It is recommended to use a private macro file\\n[robosuite WARNING] To setup, run: python /root/miniconda3/lib/python3.12/site-packages/robosuite/scripts/setup_macros.py (__init__.py:9)\\n2026-05-27 17:19:36,309 To setup, run: python /root/miniconda3/lib/python3.12/site-packages/robosuite/scripts/setup_macros.py\\n2026-05-27 17:19:36,361 No OpenGL_accelerate module loaded: No module named 'OpenGL_accelerate'\\n2026-05-27 17:19:36,753 Suite: libero_10, 10 tasks, max_steps=520\\n2026-05-27 17:22:45,387   T0 [put both the alphabet soup and the tomat] ep=10: 6/10=60%\\n2026-05-27 17:25:54,789   T0 [put both the alphabet soup and the tomat] ep=20: 14/20=70%\\n2026-05-27 17:29:11,832   T0 [put both the alphabet soup and the tomat] ep=30: 21/30=70%\\n2026-05-27 17:32:29,772   T0 [put both the alphabet sou
…[truncated 6050 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_pi05_random_k05_long_seed42_strict_w41_v2_20260527T120416",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-27T12:05:14.484456+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_pi05_random_k05_long_seed42_strict_w41_v2",
  "field": "metrics",
  "value": "{'overall_sr': 49.8, 'per_task_sr': [70, 40, 68, 74, 50, 30, 40, 62, 8, 56], 'total_successes': 249, 'total_episodes': 500, 'eval_time_min': 159.3}",
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_pi05_random_k05_long_seed42_strict_w41_v2_20260527T120416",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_pi05_random_k05_long_seed42_strict_w41_v2",
    "field": "metrics",
    "value": "{'overall_sr': 49.8, 'per_task_sr': [70, 40, 68, 74, 50, 30, 40, 62, 8, 56], 'total_successes': 249, 'total_episodes': 500, 'eval_time_min': 159.3}",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-27T12:05:14.484715+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_pi05_random_k05_long_seed42_strict_w41_v2",
  "field": "log_path",
  "value": "~/runs/importance_margin_vla_compress/eval_pi05_random_k05_long_seed42_strict_w41_v2.log",
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_pi05_random_k05_long_seed42_strict_w41_v2_20260527T120416",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_pi05_random_k05_long_seed42_strict_w41_v2",
    "field": "log_path",
    "value": "~/runs/importance_margin_vla_compress/eval_pi05_random_k05_long_seed42_strict_w41_v2.log",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-27T12:05:14.484935+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_pi05_random_k05_long_seed42_strict_w41_v2",
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
  "session": "worker_analyze_eval_pi05_random_k05_long_seed42_strict_w41_v2_20260527T120416",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_pi05_random_k05_long_seed42_strict_w41_v2",
    "field": "checkpoint_path",
    "value": "N/A (eval only)",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-27T12:05:14.485217+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_pi05_random_k05_long_seed42_strict_w41_v2\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-27T09:18:00.185Z\", \"updated_at\": \"2026-05-27T12:04:43.074Z\", \"spec\": {\"command\": \"HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python eval_pi05_pruning_libero.py --suite libero_10 --prune_mode random --keep_ratio 0.5 --n_episodes 50 --gpu 0 --seed 42\", \"server\": \"westd-41074\", \"gpu\": \"cuda:1\", \"pid\": 356612, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_random_k05_long_seed42_strict_w41_v2.log\", \"submitted_at\": \"2026-05-27T09:17:56.982Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/importance_margin_vla_compress\", \"data_count\": 500, \"model_name\": \"pi0.5\", \"seed\": 42, \"checkpoint_source\": \"pi0.5 pretrained\", \"eval_data\": \"libero_10 (Long)\"}, \"hypothesis\": \"π0.5 Random k=0.5 Long strict 重跑，排除 cqa1 lenient 评估条件污染，同时作为 k=0.5 backup 数据点\", \"parent\": \"eval_pi05_random_k05_long_seed42_strict_w41\", \"reproduce\": {\"finished_at\": \"2026-05-27T12:00:08.931Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-27T12:00:26.801348+00:00\"}]}, \"metrics\": {\"overall_sr\": 49.8, \"per_task_sr\": [70, 40, 68, 74, 50, 30, 40, 62, 8, 56], \"total_successes\": 249, \"total_episodes\": 500, \"eval_time_min\": 159.3}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 5.1461}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_pi05_random_k05_long_seed42_strict_w41_v2_20260527T120416",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-27T12:05:14.485518+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_pi05_random_k05_long_seed42_strict_w41_v2\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-27T09:18:00.185Z\", \"updated_at\": \"2026-05-27T12:04:46.826Z\", \"spec\": {\"command\": \"HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python eval_pi05_pruning_libero.py --suite libero_10 --prune_mode random --keep_ratio 0.5 --n_episodes 50 --gpu 0 --seed 42\", \"server\": \"westd-41074\", \"gpu\": \"cuda:1\", \"pid\": 356612, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_random_k05_long_seed42_strict_w41_v2.log\", \"submitted_at\": \"2026-05-27T09:17:56.982Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/importance_margin_vla_compress\", \"data_count\": 500, \"model_name\": \"pi0.5\", \"seed\": 42, \"checkpoint_source\": \"pi0.5 pretrained\", \"eval_data\": \"libero_10 (Long)\"}, \"hypothesis\": \"π0.5 Random k=0.5 Long strict 重跑，排除 cqa1 lenient 评估条件污染，同时作为 k=0.5 backup 数据点\", \"parent\": \"eval_pi05_random_k05_long_seed42_strict_w41\", \"reproduce\": {\"finished_at\": \"2026-05-27T12:00:08.931Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-27T12:00:26.801348+00:00\"}]}, \"metrics\": {\"overall_sr\": 49.8, \"per_task_sr\": [70, 40, 68, 74, 50, 30, 40, 62, 8, 56], \"total_successes\": 249, \"total_episodes\": 500, \"eval_time_min\": 159.3}, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_random_k05_long_seed42_strict_w41_v2.log\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.7412}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_pi05_random_k05_long_seed42_strict_w41_v2_20260527T120416",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-27T12:05:14.485823+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_pi05_random_k05_long_seed42_strict_w41_v2\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-27T09:18:00.185Z\", \"updated_at\": \"2026-05-27T12:04:51.463Z\", \"spec\": {\"command\": \"HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python eval_pi05_pruning_libero.py --suite libero_10 --prune_mode random --keep_ratio 0.5 --n_episodes 50 --gpu 0 --seed 42\", \"server\": \"westd-41074\", \"gpu\": \"cuda:1\", \"pid\": 356612, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_random_k05_long_seed42_strict_w41_v2.log\", \"submitted_at\": \"2026-05-27T09:17:56.982Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/importance_margin_vla_compress\", \"data_count\": 500, \"model_name\": \"pi0.5\", \"seed\": 42, \"checkpoint_source\": \"pi0.5 pretrained\", \"eval_data\": \"libero_10 (Long)\"}, \"hypothesis\": \"π0.5 Random k=0.5 Long strict 重跑，排除 cqa1 lenient 评估条件污染，同时作为 k=0.5 backup 数据点\", \"parent\": \"eval_pi05_random_k05_long_seed42_strict_w41\", \"reproduce\": {\"finished_at\": \"2026-05-27T12:00:08.931Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-27T12:00:26.801348+00:00\"}]}, \"metrics\": {\"overall_sr\": 49.8, \"per_task_sr\": [70, 40, 68, 74, 50, 30, 40, 62, 8, 56], \"total_successes\": 249, \"total_episodes\": 500, \"eval_time_min\": 159.3}, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_random_k05_long_seed42_strict_w41_v2.log\", \"checkpoint_path\": \"N/A (eval only)\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 5.7271}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_pi05_random_k05_long_seed42_strict_w41_v2_20260527T120416",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-27T12:05:14.486059+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_pi05_random_k05_long_seed42_strict_w41_v2",
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
  "session": "worker_analyze_eval_pi05_random_k05_long_seed42_strict_w41_v2_20260527T120416",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_pi05_random_k05_long_seed42_strict_w41_v2",
    "field": "conclusion",
    "value": "success",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-27T12:05:14.486357+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_pi05_random_k05_long_seed42_strict_w41_v2\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-27T09:18:00.185Z\", \"updated_at\": \"2026-05-27T12:05:03.920Z\", \"spec\": {\"command\": \"HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python eval_pi05_pruning_libero.py --suite libero_10 --prune_mode random --keep_ratio 0.5 --n_episodes 50 --gpu 0 --seed 42\", \"server\": \"westd-41074\", \"gpu\": \"cuda:1\", \"pid\": 356612, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_random_k05_long_seed42_strict_w41_v2.log\", \"submitted_at\": \"2026-05-27T09:17:56.982Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/importance_margin_vla_compress\", \"data_count\": 500, \"model_name\": \"pi0.5\", \"seed\": 42, \"checkpoint_source\": \"pi0.5 pretrained\", \"eval_data\": \"libero_10 (Long)\"}, \"hypothesis\": \"π0.5 Random k=0.5 Long strict 重跑，排除 cqa1 lenient 评估条件污染，同时作为 k=0.5 backup 数据点\", \"parent\": \"eval_pi05_random_k05_long_seed42_strict_w41\", \"reproduce\": {\"finished_at\": \"2026-05-27T12:00:08.931Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-27T12:00:26.801348+00:00\"}]}, \"metrics\": {\"overall_sr\": 49.8, \"per_task_sr\": [70, 40, 68, 74, 50, 30, 40, 62, 8, 56], \"total_successes\": 249, \"total_episodes\": 500, \"eval_time_min\": 159.3}, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_random_k05_long_seed42_strict_w41_v2.log\", \"checkpoint_path\": \"N/A (eval only)\", \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 7.325}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_pi05_random_k05_long_seed42_strict_w41_v2_20260527T120416",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-27T12:05:14.486662+00:00_

Registry 已更新。

## 结果总结

**π0.5 Random k=0.5 Long (strict) Overall SR = 49.8%**

Per-task: 70, 40, 68, 74, 50, 30, 40, 62, 8, 56

### 极端压缩点 k=0.5 三方法 strict 对比（Long suite）

| 方法 | Overall SR |
|------|-----------|
| L2norm | 50.0% |
| **Random** | **49.8%** |
| Attn | 49.8% |

三种方法在 k=0.5 处几乎完全一致（50.0% vs 49.8% vs 49.8%），差异在噪声范围内。这符合极端压缩下方法差异消失的预期——丢弃一半 token 后，无论用什么策略选择保留哪些，性能都坍缩到同一水平。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analyze_eval_pi05_random_k05_long_seed42_strict_w41_v2_20260527T120416"
}
```

</details>

---
