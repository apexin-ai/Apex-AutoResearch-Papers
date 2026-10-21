# analyze eval pi05 random k075 long seed43 strict w41

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 0
- **Tool calls:** 6
- **Original source:** `logs/chats/worker_analyze_eval_pi05_random_k075_long_seed43_strict_w41_20260527T184148.jsonl`
- **Structured JSON:** [`5a7c6fd9f63a12f64b84.json`](../../sessions/5a/5a7c6fd9f63a12f64b84.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

13 recorded events

### Tool call

_source line 1 · 2026-05-27T18:42:47.609454+00:00_

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
  "session": "worker_analyze_eval_pi05_random_k075_long_seed43_strict_w41_20260527T184148",
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

_source line 2 · 2026-05-27T18:42:47.609888+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_pi05_random_k075_long_seed43_strict_w41_20260527T184148",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-27T18:42:47.618327+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-41074",
  "command": "tail -80 ~/runs/importance_margin_vla_compress/eval_pi05_random_k075_long_seed43_strict_w41.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_pi05_random_k075_long_seed43_strict_w41_20260527T184148",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-41074",
    "command": "tail -80 ~/runs/importance_margin_vla_compress/eval_pi05_random_k075_long_seed43_strict_w41.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-27T18:42:47.618841+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-28 00:04:09,375 Vision tokens: 256/image, 3 slots -> 768 total\\n2026-05-28 00:04:09,375 Pruning: random, keep 192/256 tokens/image (576 total)\\n2026-05-28 00:04:10,084 Preprocessor/postprocessor loaded\\n[robosuite WARNING] No private macro file found! (__init__.py:7)\\n2026-05-28 00:04:10,105 No private macro file found!\\n[robosuite WARNING] It is recommended to use a private macro file (__init__.py:8)\\n2026-05-28 00:04:10,105 It is recommended to use a private macro file\\n[robosuite WARNING] To setup, run: python /root/miniconda3/lib/python3.12/site-packages/robosuite/scripts/setup_macros.py (__init__.py:9)\\n2026-05-28 00:04:10,105 To setup, run: python /root/miniconda3/lib/python3.12/site-packages/robosuite/scripts/setup_macros.py\\n2026-05-28 00:04:10,154 No OpenGL_accelerate module loaded: No module named 'OpenGL_accelerate'\\n[info] using task orders [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\\n2026-05-28 00:04:10,562 Suite: libero_10, 10 tasks, max_steps=520\\n[PRUNE-DIAG] random: n_keep=192/256, first_indices=[0, 1, 2, 4, 5]\\n2026-05-28 00:07:02,239   T0 [put both the alphabet soup and the tomat] ep=10: 9/10=90%\\n2026-05-28 00:10:13,109   T0 [put both the alphabet soup and the tomat] ep=20: 17/20=85%\\n2026-05-28 00:13:16,533   T0 [put both the alphabet soup and the tomat] ep=30: 25/30=83%\\n2026-05-28 00:16:17,569   T0 [put both the alphabet soup and the tomat] ep=40: 34/40=85%\\n2026-05-28 00:19:05,714   T0 [put both the alphabet soup and the tomat] ep=50: 43/50=86%\\n2026-05-28 00:19:05,714 Task 0: SR=86.0% | Total: 43/50=86.0% | Time: 14.9min\\n2026-05-28 00:22:12,847   T1 [put both the cream cheese box and the bu] ep=10: 7/10=70%\\n2026-05-28 00:25:03,081   T1 [put both the cream cheese box and the bu] ep=20: 15/20=75%\\n2026-05-28 00:27:59,948   T1 [put both the cream cheese box and the bu] ep=30: 23/30=77%\\n2026-05-28 00:31:18,358   T1 [put both the cream cheese box and the bu] ep=40: 28/40=
…[truncated 5001 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_pi05_random_k075_long_seed43_strict_w41_20260527T184148",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-27T18:42:47.619189+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_pi05_random_k075_long_seed43_strict_w41",
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
  "session": "worker_analyze_eval_pi05_random_k075_long_seed43_strict_w41_20260527T184148",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_pi05_random_k075_long_seed43_strict_w41",
    "field": "conclusion",
    "value": "success",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-27T18:42:47.619431+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_pi05_random_k075_long_seed43_strict_w41",
  "field": "metrics",
  "value": "{'overall_sr': 60.6, 'per_task': {'T0': 86, 'T1': 62, 'T2': 60, 'T3': 64, 'T4': 82, 'T5': 40, 'T6': 66, 'T7': 70, 'T8': 2, 'T9': 74}, 'seed': 43, 'episodes_per_task': 50}",
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_pi05_random_k075_long_seed43_strict_w41_20260527T184148",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_pi05_random_k075_long_seed43_strict_w41",
    "field": "metrics",
    "value": "{'overall_sr': 60.6, 'per_task': {'T0': 86, 'T1': 62, 'T2': 60, 'T3': 64, 'T4': 82, 'T5': 40, 'T6': 66, 'T7': 70, 'T8': 2, 'T9': 74}, 'seed': 43, 'episodes_per_task': 50}",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-27T18:42:47.619680+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_pi05_random_k075_long_seed43_strict_w41",
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
  "session": "worker_analyze_eval_pi05_random_k075_long_seed43_strict_w41_20260527T184148",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_pi05_random_k075_long_seed43_strict_w41",
    "field": "checkpoint_path",
    "value": "N/A (eval-only)",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-27T18:42:47.619950+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_pi05_random_k075_long_seed43_strict_w41\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-27T16:01:19.638Z\", \"updated_at\": \"2026-05-27T18:42:19.022Z\", \"hypothesis\": \"π0.5 Random k=0.75 Long strict seed43 — seed42=63.0% 的 seed 复制，生成 error bar。k=0.75 是 Random U-shape 的上升段关键点\", \"parent\": \"eval_pi05_random_k075_long_seed42_strict\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.75 --suite libero_10 --n_episodes 50 --seed 43 --gpu 0\\\"\", \"server\": \"westd-41074\", \"gpu\": [\"cuda:2\"], \"pid\": \"840142\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_random_k075_long_seed43_strict_w41.log\", \"submitted_at\": \"2026-05-27T16:02:28.595Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"server\": \"westd-41074\", \"gpu\": \"cuda:2\", \"pid\": \"840142\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_random_k075_long_seed43_strict_w41.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.75 --suite libero_10 --n_episodes 50 --seed 43 --gpu 0\\\"\", \"finished_at\": \"2026-05-27T18:38:54.936Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-27T18:39:22.920811+00:00\"}]}, \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.8395}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_pi05_random_k075_long_seed43_strict_w41_20260527T184148",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-27T18:42:47.621279+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_pi05_random_k075_long_seed43_strict_w41\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-27T16:01:19.638Z\", \"updated_at\": \"2026-05-27T18:42:22.606Z\", \"hypothesis\": \"π0.5 Random k=0.75 Long strict seed43 — seed42=63.0% 的 seed 复制，生成 error bar。k=0.75 是 Random U-shape 的上升段关键点\", \"parent\": \"eval_pi05_random_k075_long_seed42_strict\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.75 --suite libero_10 --n_episodes 50 --seed 43 --gpu 0\\\"\", \"server\": \"westd-41074\", \"gpu\": [\"cuda:2\"], \"pid\": \"840142\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_random_k075_long_seed43_strict_w41.log\", \"submitted_at\": \"2026-05-27T16:02:28.595Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"server\": \"westd-41074\", \"gpu\": \"cuda:2\", \"pid\": \"840142\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_random_k075_long_seed43_strict_w41.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.75 --suite libero_10 --n_episodes 50 --seed 43 --gpu 0\\\"\", \"finished_at\": \"2026-05-27T18:38:54.936Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-27T18:39:22.920811+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 60.6, \"per_task\": {\"T0\": 86, \"T1
…[truncated 210 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_pi05_random_k075_long_seed43_strict_w41_20260527T184148",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-27T18:42:47.621649+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_pi05_random_k075_long_seed43_strict_w41\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-27T16:01:19.638Z\", \"updated_at\": \"2026-05-27T18:42:26.211Z\", \"hypothesis\": \"π0.5 Random k=0.75 Long strict seed43 — seed42=63.0% 的 seed 复制，生成 error bar。k=0.75 是 Random U-shape 的上升段关键点\", \"parent\": \"eval_pi05_random_k075_long_seed42_strict\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.75 --suite libero_10 --n_episodes 50 --seed 43 --gpu 0\\\"\", \"server\": \"westd-41074\", \"gpu\": [\"cuda:2\"], \"pid\": \"840142\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_random_k075_long_seed43_strict_w41.log\", \"submitted_at\": \"2026-05-27T16:02:28.595Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"server\": \"westd-41074\", \"gpu\": \"cuda:2\", \"pid\": \"840142\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_random_k075_long_seed43_strict_w41.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.75 --suite libero_10 --n_episodes 50 --seed 43 --gpu 0\\\"\", \"finished_at\": \"2026-05-27T18:38:54.936Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-27T18:39:22.920811+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 60.6, \"per_task\": {\"T0\": 86, \"T1
…[truncated 252 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_pi05_random_k075_long_seed43_strict_w41_20260527T184148",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-27T18:42:47.621907+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_pi05_random_k075_long_seed43_strict_w41",
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
  "session": "worker_analyze_eval_pi05_random_k075_long_seed43_strict_w41_20260527T184148",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_pi05_random_k075_long_seed43_strict_w41",
    "field": "status",
    "value": "DONE",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-27T18:42:47.622246+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_pi05_random_k075_long_seed43_strict_w41\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-27T16:01:19.638Z\", \"updated_at\": \"2026-05-27T18:42:35.729Z\", \"hypothesis\": \"π0.5 Random k=0.75 Long strict seed43 — seed42=63.0% 的 seed 复制，生成 error bar。k=0.75 是 Random U-shape 的上升段关键点\", \"parent\": \"eval_pi05_random_k075_long_seed42_strict\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.75 --suite libero_10 --n_episodes 50 --seed 43 --gpu 0\\\"\", \"server\": \"westd-41074\", \"gpu\": [\"cuda:2\"], \"pid\": \"840142\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_random_k075_long_seed43_strict_w41.log\", \"submitted_at\": \"2026-05-27T16:02:28.595Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 9607.1, \"gpu_hours\": 2.67}, \"server\": \"westd-41074\", \"gpu\": \"cuda:2\", \"pid\": \"840142\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_random_k075_long_seed43_strict_w41.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.75 --suite libero_10 --n_episodes 50 --seed 43 --gpu 0\\\"\", \"finished_at\": \"2026-05-27T18:38:54.936Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-27T18:39:22.920811+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"ove
…[truncated 400 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_pi05_random_k075_long_seed43_strict_w41_20260527T184148",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-27T18:42:47.622553+00:00_

Registry 已更新为 DONE。

**汇总**：π0.5 Random k=0.75 Long seed43 = **60.6%**，seed42 = 63.0%，均值 **61.8% ± 1.2%**。

| Task | T0 | T1 | T2 | T3 | T4 | T5 | T6 | T7 | T8 | T9 | Overall |
|------|----|----|----|----|----|----|----|----|----|----|---------|
| seed43 | 86 | 62 | 60 | 64 | 82 | 40 | 66 | 70 | 2 | 74 | 60.6 |

T8 依然是瓶颈（2%），与 seed42 一致。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analyze_eval_pi05_random_k075_long_seed43_strict_w41_20260527T184148"
}
```

</details>

---
