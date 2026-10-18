# analyze eval pi05 random k075 long strict

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 21
- **Recorded user turns:** 0
- **Tool calls:** 10
- **Original source:** `logs/chats/worker_analyze_eval_pi05_random_k075_long_strict_20260527T084042.jsonl`
- **Structured JSON:** [`554c0cc1d0247d312671.json`](../../sessions/55/554c0cc1d0247d312671.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

21 recorded events

### Tool call

_source line 1 · 2026-05-27T08:42:04.029447+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__read_registry",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_pi05_random_k075_long_strict_20260527T084042",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__read_registry",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-27T08:42:04.029797+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_pi05_random_k075_long_strict_20260527T084042",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-27T08:42:04.029985+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-41074",
  "command": "tail -100 ~/runs/importance_margin_vla_compress/eval_pi05_random_k075_long_seed42_strict.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_pi05_random_k075_long_strict_20260527T084042",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-41074",
    "command": "tail -100 ~/runs/importance_margin_vla_compress/eval_pi05_random_k075_long_seed42_strict.log",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-27T08:42:04.030123+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-41074",
  "command": "grep -c \"success_rate\" ~/runs/importance_margin_vla_compress/eval_pi05_random_k075_long_seed42_strict.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_pi05_random_k075_long_strict_20260527T084042",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-41074",
    "command": "grep -c \"success_rate\" ~/runs/importance_margin_vla_compress/eval_pi05_random_k075_long_seed42_strict.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-27T08:42:04.030391+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-27 13:36:49,977 Config: suite=libero_10, prune=random, keep=0.75, eps=50, gpu=0\\n2026-05-27 13:36:49,977 Loading π0.5 from /root/autodl-tmp/pi05_libero_finetuned ...\\n2026-05-27 13:38:25,331 Enabled gradient checkpointing for PI05Pytorch model\\n2026-05-27 13:38:26,942 Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embedding.bias\\n2026-05-27 13:38:26,942 Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embedding.weight\\n2026-05-27 13:38:28,989 Patched embed_image\\n2026-05-27 13:38:28,995 Model: 4143.4M params\\n2026-05-27 13:38:28,995 Vision tokens: 256/image, 3 slots -> 768 total\\n2026-05-27 13:38:28,995 Pruning: random, keep 192/256 tokens/image (576 total)\\n2026-05-27 13:38:29,724 Preprocessor/postprocessor loaded\\n[robosuite WARNING] No private macro file found! (__init__.py:7)\\n2026-05-27 13:38:29,744 No private macro file found!\\n[robosuite WARNING] It is recommended to use a private macro file (__init__.py:8)\\n2026-05-27 13:38:29,744 It is recommended to use a private macro file\\n[robosuite WARNING] To setup, run: python /root/miniconda3/lib/python3.12/site-packages/robosuite/scripts/setup_macros.py (__init__.py:9)\\n2026-05-27 13:38:29,744 To setup, run: python /root/miniconda3/lib/python3.12/site-packages/robosuite/scripts/setup_macros.py\\n2026-05-27 13:38:29,793 No OpenGL_accelerate module loaded: No module named 'OpenGL_accelerate'\\n2026-05-27 13:38:30,189 Suite: libero_10, 10 tasks, max_steps=520\\n2026-05-27 13:41:17,024   T0 [put both the alphabet soup and the tomat] ep=10: 9/10=90%\\n2026-05-27 13:44:20,079   T0 [put both the alphabet soup and the tomat] ep=20: 17/20=85%\\n2026-05-27 13:47:01,985   T0 [put both the alphabet soup and the tomat] ep=30: 26/30=87%\\n2026-05-27 13:49:55,254   T0 [put both the alphabet so
…[truncated 6057 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_pi05_random_k075_long_strict_20260527T084042",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-27T08:42:04.030559+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-41074",
  "command": "grep -i \"Average\\|Final\\|overall\\|success_rate\\|Summary\" ~/runs/importance_margin_vla_compress/eval_pi05_random_k075_long_seed42_strict.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_pi05_random_k075_long_strict_20260527T084042",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-41074",
    "command": "grep -i \"Average\\|Final\\|overall\\|success_rate\\|Summary\" ~/runs/importance_margin_vla_compress/eval_pi05_random_k075_long_seed42_strict.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-27T08:42:04.030712+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"0\\n\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.51}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_pi05_random_k075_long_strict_20260527T084042",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-27T08:42:04.030839+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_pi05_random_k075_long_strict_20260527T084042",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-27T08:42:04.030970+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-41074",
  "command": "nvidia-smi --query-gpu=index,utilization.gpu,memory.used,memory.total --format=csv,noheader",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_pi05_random_k075_long_strict_20260527T084042",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-41074",
    "command": "nvidia-smi --query-gpu=index,utilization.gpu,memory.used,memory.total --format=csv,noheader",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-27T08:42:04.031186+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"0, 0 %, 1 MiB, 97887 MiB\\n1, 0 %, 1 MiB, 97887 MiB\\n2, 32 %, 10942 MiB, 97887 MiB\\n3, 27 %, 10796 MiB, 97887 MiB\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.59}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_pi05_random_k075_long_strict_20260527T084042",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-27T08:42:04.031378+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_pi05_random_k075_long_seed42_strict",
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
  "session": "worker_analyze_eval_pi05_random_k075_long_strict_20260527T084042",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_pi05_random_k075_long_seed42_strict",
    "field": "status",
    "value": "DONE",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-27T08:42:04.031515+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Cannot transition to DONE without a 'conclusion' field. Set conclusion first.\", \"metadata\": {\"elapsed_seconds\": 4.4541}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_pi05_random_k075_long_strict_20260527T084042",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-27T08:42:04.031638+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_pi05_random_k075_long_seed42_strict",
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
  "session": "worker_analyze_eval_pi05_random_k075_long_strict_20260527T084042",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_pi05_random_k075_long_seed42_strict",
    "field": "conclusion",
    "value": "success",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-27T08:42:04.031799+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_pi05_random_k075_long_seed42_strict\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 1, \"created_at\": \"2026-05-27T05:15:32.754Z\", \"updated_at\": \"2026-05-27T08:41:25.302Z\", \"hypothesis\": \"π0.5 Random k=0.75 Long strict — cqa1 宽松条件值 62.4% 可能被污染。strict 重跑获取真实值。验证 V-shape 现象是否在 strict 条件下依然存在。\", \"parent\": \"eval_pi05_random_k085_long_seed42_strict\", \"reproduce\": {\"finished_at\": \"2026-05-27T08:16:22.591Z\"}, \"failure_reason\": \"EXIT_CODE=143 (SIGTERM — graceful kill)\", \"completed_at\": \"2026-05-27T05:35:30.461Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"failed\"}, \"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-27T08:16:55.580925+00:00\"}]}, \"spec\": {\"command\": \"python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.75 --suite libero_10 --n_episodes 50 --seed 42 --gpu 0\", \"server\": \"westd-41074\", \"gpu_id\": 1, \"pid\": 177597, \"data_path\": \"libero_10\", \"data_count\": \"10 tasks x 50 episodes\", \"model_name\": \"pi05_libero_finetuned\", \"seed\": 42, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_random_k075_long_seed42_strict.log\", \"checkpoint_path\": \"N/A (eval only)\", \"checkpoint_source\": \"/root/autodl-tmp/pi05_libero_finetuned\", \"eval_data\": \"libero_10\"}, \"gpu\": \"cuda:1\", \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 7.3841}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_pi05_random_k075_long_strict_20260527T084042",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-27T08:42:04.031950+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_pi05_random_k075_long_seed42_strict",
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
  "session": "worker_analyze_eval_pi05_random_k075_long_strict_20260527T084042",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_pi05_random_k075_long_seed42_strict",
    "field": "status",
    "value": "DONE",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-27T08:42:04.032081+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_pi05_random_k075_long_seed42_strict",
  "field": "metrics",
  "value": "{'success_rate': 63, 'per_task_sr': [84, 72, 78, 74, 64, 48, 62, 54, 12, 82], 'total_success': 315, 'total_episodes': 500, 'eval_time_min': 156.9}",
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_pi05_random_k075_long_strict_20260527T084042",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_pi05_random_k075_long_seed42_strict",
    "field": "metrics",
    "value": "{'success_rate': 63, 'per_task_sr': [84, 72, 78, 74, 64, 48, 62, 54, 12, 82], 'total_success': 315, 'total_episodes': 500, 'eval_time_min': 156.9}",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-27T08:42:04.032246+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Cannot transition ANALYZING → DONE(success) without metrics. Set metrics first, or use conclusion=negative/failed.\", \"metadata\": {\"elapsed_seconds\": 3.6358}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_pi05_random_k075_long_strict_20260527T084042",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-27T08:42:04.032408+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_pi05_random_k075_long_seed42_strict\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 1, \"created_at\": \"2026-05-27T05:15:32.754Z\", \"updated_at\": \"2026-05-27T08:41:37.523Z\", \"hypothesis\": \"π0.5 Random k=0.75 Long strict — cqa1 宽松条件值 62.4% 可能被污染。strict 重跑获取真实值。验证 V-shape 现象是否在 strict 条件下依然存在。\", \"parent\": \"eval_pi05_random_k085_long_seed42_strict\", \"reproduce\": {\"finished_at\": \"2026-05-27T08:16:22.591Z\"}, \"failure_reason\": \"EXIT_CODE=143 (SIGTERM — graceful kill)\", \"completed_at\": \"2026-05-27T05:35:30.461Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"failed\"}, \"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-27T08:16:55.580925+00:00\"}]}, \"spec\": {\"command\": \"python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.75 --suite libero_10 --n_episodes 50 --seed 42 --gpu 0\", \"server\": \"westd-41074\", \"gpu_id\": 1, \"pid\": 177597, \"data_path\": \"libero_10\", \"data_count\": \"10 tasks x 50 episodes\", \"model_name\": \"pi05_libero_finetuned\", \"seed\": 42, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_random_k075_long_seed42_strict.log\", \"checkpoint_path\": \"N/A (eval only)\", \"checkpoint_source\": \"/root/autodl-tmp/pi05_libero_finetuned\", \"eval_data\": \"libero_10\"}, \"gpu\": \"cuda:1\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 63, \"per_task_sr\": [84, 72, 78, 74, 64, 48, 62, 54, 12, 82], \"total_success\": 315, \"total_episodes\": 500, \"eval_time_min\": 156.9}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.3966}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_pi05_random_k075_long_strict_20260527T084042",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-27T08:42:04.032593+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_pi05_random_k075_long_seed42_strict",
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
  "session": "worker_analyze_eval_pi05_random_k075_long_strict_20260527T084042",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_pi05_random_k075_long_seed42_strict",
    "field": "status",
    "value": "DONE",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-27T08:42:04.032792+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_pi05_random_k075_long_seed42_strict\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-27T05:15:32.754Z\", \"updated_at\": \"2026-05-27T08:41:48.399Z\", \"hypothesis\": \"π0.5 Random k=0.75 Long strict — cqa1 宽松条件值 62.4% 可能被污染。strict 重跑获取真实值。验证 V-shape 现象是否在 strict 条件下依然存在。\", \"parent\": \"eval_pi05_random_k085_long_seed42_strict\", \"reproduce\": {\"finished_at\": \"2026-05-27T08:16:22.591Z\"}, \"failure_reason\": \"EXIT_CODE=143 (SIGTERM — graceful kill)\", \"completed_at\": \"2026-05-27T05:35:30.461Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"failed\"}, \"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-27T08:16:55.580925+00:00\"}]}, \"spec\": {\"command\": \"python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.75 --suite libero_10 --n_episodes 50 --seed 42 --gpu 0\", \"server\": \"westd-41074\", \"gpu_id\": 1, \"pid\": 177597, \"data_path\": \"libero_10\", \"data_count\": \"10 tasks x 50 episodes\", \"model_name\": \"pi05_libero_finetuned\", \"seed\": 42, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_random_k075_long_seed42_strict.log\", \"checkpoint_path\": \"N/A (eval only)\", \"checkpoint_source\": \"/root/autodl-tmp/pi05_libero_finetuned\", \"eval_data\": \"libero_10\"}, \"gpu\": \"cuda:1\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 63, \"per_task_sr\": [84, 72, 78, 74, 64, 48, 62, 54, 12, 82], \"total_success\": 315, \"total_episodes\": 500, \"eval_time_min\": 156.9}}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 13.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_pi05_random_k075_long_strict_20260527T084042",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-27T08:42:04.032983+00:00_

Registry 已更新为 DONE/success。

## 结果汇总

**eval_pi05_random_k075_long_seed42_strict — SR = 63.0%**

| Task | SR |
|------|-----|
| T0 alphabet soup + tomato | 84% |
| T1 cream cheese + butter | 72% |
| T2 stove + moka pot | 78% |
| T3 black bowl → drawer | 74% |
| T4 white mug + plate | 64% |
| T5 book → back | 48% |
| T6 white mug + plate (v2) | 62% |
| T7 alphabet soup + cream | 54% |
| T8 both moka pots → stove | 12% |
| T9 yellow mug → microwave | 82% |

尽管 EXIT_CODE=143 出现在前次 retry，第二次运行实际 EXIT_CODE=0，全部 500 episodes 完成。

**westd-41074 GPU 状态：**
- GPU 0, 1: 空闲 (0%, 1 MiB)
- GPU 2, 3: 占用中 (~30%, ~11 GB)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analyze_eval_pi05_random_k075_long_strict_20260527T084042"
}
```

</details>

---
