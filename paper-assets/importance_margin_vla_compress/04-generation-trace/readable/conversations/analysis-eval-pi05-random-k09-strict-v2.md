# analysis eval pi05 random k09 strict v2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 0
- **Tool calls:** 6
- **Original source:** `logs/chats/worker_analysis_eval_pi05_random_k09_strict_v2_20260527T122207.jsonl`
- **Structured JSON:** [`5e6b24d201f2996821e0.json`](../../sessions/5e/5e6b24d201f2996821e0.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

13 recorded events

### Tool call

_source line 1 · 2026-05-27T12:23:20.791368+00:00_

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
  "session": "worker_analysis_eval_pi05_random_k09_strict_v2_20260527T122207",
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

_source line 2 · 2026-05-27T12:23:20.791891+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_pi05_random_k09_strict_v2_20260527T122207",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-27T12:23:20.792177+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-41074",
  "command": "tail -200 ~/runs/importance_margin_vla_compress/eval_pi05_random_k09_long_seed42_strict_v2.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_eval_pi05_random_k09_strict_v2_20260527T122207",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-41074",
    "command": "tail -200 ~/runs/importance_margin_vla_compress/eval_pi05_random_k09_long_seed42_strict_v2.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-27T12:23:20.792554+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-27 17:17:48,671 Config: suite=libero_10, prune=random, keep=0.9, eps=50, gpu=0\\n2026-05-27 17:17:48,671 Loading π0.5 from /root/autodl-tmp/pi05_libero_finetuned ...\\n2026-05-27 17:19:20,484 Enabled gradient checkpointing for PI05Pytorch model\\n2026-05-27 17:19:22,041 Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embedding.bias\\n2026-05-27 17:19:22,041 Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embedding.weight\\n2026-05-27 17:19:23,637 Patched embed_image\\n2026-05-27 17:19:23,643 Model: 4143.4M params\\n2026-05-27 17:19:23,644 Vision tokens: 256/image, 3 slots -> 768 total\\n2026-05-27 17:19:23,644 Pruning: random, keep 230/256 tokens/image (690 total)\\n2026-05-27 17:19:24,320 Preprocessor/postprocessor loaded\\n[robosuite WARNING] No private macro file found! (__init__.py:7)\\n2026-05-27 17:19:24,340 No private macro file found!\\n[robosuite WARNING] It is recommended to use a private macro file (__init__.py:8)\\n2026-05-27 17:19:24,340 It is recommended to use a private macro file\\n[robosuite WARNING] To setup, run: python /root/miniconda3/lib/python3.12/site-packages/robosuite/scripts/setup_macros.py (__init__.py:9)\\n2026-05-27 17:19:24,340 To setup, run: python /root/miniconda3/lib/python3.12/site-packages/robosuite/scripts/setup_macros.py\\n2026-05-27 17:19:24,392 No OpenGL_accelerate module loaded: No module named 'OpenGL_accelerate'\\n2026-05-27 17:19:24,762 Suite: libero_10, 10 tasks, max_steps=520\\n2026-05-27 17:23:18,692   T0 [put both the alphabet soup and the tomat] ep=10: 2/10=20%\\n2026-05-27 17:27:31,870   T0 [put both the alphabet soup and the tomat] ep=20: 2/20=10%\\n2026-05-27 17:31:46,544   T0 [put both the alphabet soup and the tomat] ep=30: 2/30=7%\\n2026-05-27 17:36:03,491   T0 [put both the alphabet soup a
…[truncated 6026 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_pi05_random_k09_strict_v2_20260527T122207",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-27T12:23:20.792895+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_pi05_random_k09_long_seed42_strict_v2",
  "field": "metrics",
  "value": "{'overall_sr': 34.2, 'per_task_sr': [10, 46, 40, 58, 16, 38, 2, 38, 6, 88], 'total_successes': 171, 'total_episodes': 500, 'eval_time_min': 177.3, 'per_task_raw': [[5, 50], [23, 50], [20, 50], [29, 50], [8, 50], [19, 50], [1, 50], [19, 50], [3, 50], [44, 50]]}",
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_eval_pi05_random_k09_strict_v2_20260527T122207",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_pi05_random_k09_long_seed42_strict_v2",
    "field": "metrics",
    "value": "{'overall_sr': 34.2, 'per_task_sr': [10, 46, 40, 58, 16, 38, 2, 38, 6, 88], 'total_successes': 171, 'total_episodes': 500, 'eval_time_min': 177.3, 'per_task_raw': [[5, 50], [23, 50], [20, 50], [29, 50], [8, 50], [19, 50], [1, 50], [19, 50], [3, 50], [44, 50]]}",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-27T12:23:20.793245+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_pi05_random_k09_long_seed42_strict_v2\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-27T09:17:50.924Z\", \"updated_at\": \"2026-05-27T12:22:38.755Z\", \"spec\": {\"command\": \"HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python eval_pi05_pruning_libero.py --suite libero_10 --prune_mode random --keep_ratio 0.9 --n_episodes 50 --gpu 0 --seed 42\", \"server\": \"westd-41074\", \"gpu\": \"cuda:0\", \"pid\": 356361, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_random_k09_long_seed42_strict_v2.log\", \"submitted_at\": \"2026-05-27T09:17:47.259Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/importance_margin_vla_compress\", \"data_count\": 500, \"model_name\": \"pi0.5\", \"seed\": 42, \"checkpoint_source\": \"pi0.5 pretrained\", \"eval_data\": \"libero_10 (Long)\"}, \"hypothesis\": \"π0.5 Random k=0.9 Long lenient 结果 ~32% 异常低（反单调性 D254：k=0.75=63%→k=0.85=45%→k=0.9=32%），strict 重跑验证是否为 success 条件污染或真实性能\", \"parent\": \"eval_pi05_random_k09_long_seed42_strict\", \"reproduce\": {\"finished_at\": \"2026-05-27T12:17:13.389Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-27T12:17:45.810329+00:00\"}]}, \"metrics\": {\"overall_sr\": 34.2, \"per_task_sr\": [10, 46, 40, 58, 16, 38, 2, 38, 6, 88], \"total_successes\": 171, \"total_episodes\": 500, \"eval_time_min\": 177.3, \"per_task_raw\": [[5, 50], [23, 50], [20, 50], [29, 50], [8, 50], [19, 50], [1, 50], [19, 50], [3, 50], [44, 50]]}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 5.0324}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_pi05_random_k09_strict_v2_20260527T122207",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-27T12:23:20.793520+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_pi05_random_k09_long_seed42_strict_v2",
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
  "session": "worker_analysis_eval_pi05_random_k09_strict_v2_20260527T122207",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_pi05_random_k09_long_seed42_strict_v2",
    "field": "conclusion",
    "value": "success",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-27T12:23:20.793747+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_pi05_random_k09_long_seed42_strict_v2",
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
  "session": "worker_analysis_eval_pi05_random_k09_strict_v2_20260527T122207",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_pi05_random_k09_long_seed42_strict_v2",
    "field": "checkpoint_path",
    "value": "N/A (eval only)",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-27T12:23:20.794037+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_pi05_random_k09_long_seed42_strict_v2\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-27T09:17:50.924Z\", \"updated_at\": \"2026-05-27T12:22:50.007Z\", \"spec\": {\"command\": \"HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python eval_pi05_pruning_libero.py --suite libero_10 --prune_mode random --keep_ratio 0.9 --n_episodes 50 --gpu 0 --seed 42\", \"server\": \"westd-41074\", \"gpu\": \"cuda:0\", \"pid\": 356361, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_random_k09_long_seed42_strict_v2.log\", \"submitted_at\": \"2026-05-27T09:17:47.259Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/importance_margin_vla_compress\", \"data_count\": 500, \"model_name\": \"pi0.5\", \"seed\": 42, \"checkpoint_source\": \"pi0.5 pretrained\", \"eval_data\": \"libero_10 (Long)\"}, \"hypothesis\": \"π0.5 Random k=0.9 Long lenient 结果 ~32% 异常低（反单调性 D254：k=0.75=63%→k=0.85=45%→k=0.9=32%），strict 重跑验证是否为 success 条件污染或真实性能\", \"parent\": \"eval_pi05_random_k09_long_seed42_strict\", \"reproduce\": {\"finished_at\": \"2026-05-27T12:17:13.389Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-27T12:17:45.810329+00:00\"}]}, \"metrics\": {\"overall_sr\": 34.2, \"per_task_sr\": [10, 46, 40, 58, 16, 38, 2, 38, 6, 88], \"total_successes\": 171, \"total_episodes\": 500, \"eval_time_min\": 177.3, \"per_task_raw\": [[5, 50], [23, 50], [20, 50], [29, 50], [8, 50], [19, 50], [1, 50], [19, 50], [3, 50], [44, 50]]}, \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 5.6615}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_pi05_random_k09_strict_v2_20260527T122207",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-27T12:23:20.794373+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_pi05_random_k09_long_seed42_strict_v2\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-27T09:17:50.924Z\", \"updated_at\": \"2026-05-27T12:22:54.743Z\", \"spec\": {\"command\": \"HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python eval_pi05_pruning_libero.py --suite libero_10 --prune_mode random --keep_ratio 0.9 --n_episodes 50 --gpu 0 --seed 42\", \"server\": \"westd-41074\", \"gpu\": \"cuda:0\", \"pid\": 356361, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_random_k09_long_seed42_strict_v2.log\", \"submitted_at\": \"2026-05-27T09:17:47.259Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/importance_margin_vla_compress\", \"data_count\": 500, \"model_name\": \"pi0.5\", \"seed\": 42, \"checkpoint_source\": \"pi0.5 pretrained\", \"eval_data\": \"libero_10 (Long)\"}, \"hypothesis\": \"π0.5 Random k=0.9 Long lenient 结果 ~32% 异常低（反单调性 D254：k=0.75=63%→k=0.85=45%→k=0.9=32%），strict 重跑验证是否为 success 条件污染或真实性能\", \"parent\": \"eval_pi05_random_k09_long_seed42_strict\", \"reproduce\": {\"finished_at\": \"2026-05-27T12:17:13.389Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-27T12:17:45.810329+00:00\"}]}, \"metrics\": {\"overall_sr\": 34.2, \"per_task_sr\": [10, 46, 40, 58, 16, 38, 2, 38, 6, 88], \"total_successes\": 171, \"total_episodes\": 500, \"eval_time_min\": 177.3, \"per_task_raw\": [[5, 50], [23, 50], [20, 50], [29, 50], [8, 50], [19, 50], [1, 50], [19, 50], [3, 50], [44, 50]]}, \"conclusion\": \"success\", \"checkpoint_path\": \"N/A (eval only)\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 6.8811}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_pi05_random_k09_strict_v2_20260527T122207",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-27T12:23:20.794613+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_pi05_random_k09_long_seed42_strict_v2",
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
  "session": "worker_analysis_eval_pi05_random_k09_strict_v2_20260527T122207",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_pi05_random_k09_long_seed42_strict_v2",
    "field": "status",
    "value": "DONE",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-27T12:23:20.794917+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_pi05_random_k09_long_seed42_strict_v2\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-27T09:17:50.924Z\", \"updated_at\": \"2026-05-27T12:23:05.276Z\", \"spec\": {\"command\": \"HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python eval_pi05_pruning_libero.py --suite libero_10 --prune_mode random --keep_ratio 0.9 --n_episodes 50 --gpu 0 --seed 42\", \"server\": \"westd-41074\", \"gpu\": \"cuda:0\", \"pid\": 356361, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_random_k09_long_seed42_strict_v2.log\", \"submitted_at\": \"2026-05-27T09:17:47.259Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/importance_margin_vla_compress\", \"data_count\": 500, \"model_name\": \"pi0.5\", \"seed\": 42, \"checkpoint_source\": \"pi0.5 pretrained\", \"eval_data\": \"libero_10 (Long)\", \"wall_clock_seconds\": 11118.0, \"gpu_hours\": 3.09}, \"hypothesis\": \"π0.5 Random k=0.9 Long lenient 结果 ~32% 异常低（反单调性 D254：k=0.75=63%→k=0.85=45%→k=0.9=32%），strict 重跑验证是否为 success 条件污染或真实性能\", \"parent\": \"eval_pi05_random_k09_long_seed42_strict\", \"reproduce\": {\"finished_at\": \"2026-05-27T12:17:13.389Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-27T12:17:45.810329+00:00\"}]}, \"metrics\": {\"overall_sr\": 34.2, \"per_task_sr\": [10, 46, 40, 58, 16, 38, 2, 38, 6, 88], \"total_successes\": 171, \"total_episodes\": 500, \"eval_time_min\": 177.3, \"per_task_raw\": [[5, 50], [23, 50], [20, 50], [29, 50], [8, 50], [19, 50], [1, 50], [19, 50], [3, 50], [44, 50]]}, \"conclusion\": \"success\", \"checkpoint_path\": \"N/A (eval only)\", \"completed_at\": \"2026-05-27T12:23:05.276Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 12.387}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_pi05_random_k09_strict_v2_20260527T122207",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-27T12:23:20.795241+00:00_

Registry 已更新至 DONE。

**结果摘要**：π0.5 Random k=0.9 Long strict v2 = **34.2%**（171/500），177.3 min，EXIT_CODE=0，完整完成。

确认 D263 的 34.2% 来自本次 v2 实验。反单调性曲线 strict 下依然成立：k=0.75(63%)→k=0.85(45%)→**k=0.9(34.2%)**→k=0.95(60.6%)，k=0.9 确实是 dip point。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_eval_pi05_random_k09_strict_v2_20260527T122207"
}
```

</details>

---
