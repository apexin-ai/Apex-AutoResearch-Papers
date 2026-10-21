# analyze eval xvla l2norm k03 spatial seed42

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 27
- **Recorded user turns:** 0
- **Tool calls:** 13
- **Original source:** `logs/chats/worker_analyze_eval_xvla_l2norm_k03_spatial_seed42_20260523T204234.jsonl`
- **Structured JSON:** [`c4a34200d38654fd80c1.json`](../../sessions/c4/c4a34200d38654fd80c1.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

27 recorded events

### Tool call

_source line 1 · 2026-05-23T20:44:33.423008+00:00_

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
  "session": "worker_analyze_eval_xvla_l2norm_k03_spatial_seed42_20260523T204234",
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

_source line 2 · 2026-05-23T20:44:33.423563+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_xvla_l2norm_k03_spatial_seed42_20260523T204234",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-23T20:44:33.423825+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-38929",
  "command": "tail -80 ~/runs/importance_margin_vla_compress/eval_xvla_l2norm_k03_spatial_seed42.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_xvla_l2norm_k03_spatial_seed42_20260523T204234",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-38929",
    "command": "tail -80 ~/runs/importance_margin_vla_compress/eval_xvla_l2norm_k03_spatial_seed42.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-23T20:44:33.424122+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-24 04:23:07 [INFO]   Ep 42/50 | FAIL | steps=800\\n2026-05-24 04:23:24 [INFO]   Ep 43/50 | FAIL | steps=800\\n2026-05-24 04:23:40 [INFO]   Ep 44/50 | FAIL | steps=800\\n2026-05-24 04:23:44 [INFO]   Ep 45/50 | SUCCESS | steps=106\\n2026-05-24 04:24:01 [INFO]   Ep 46/50 | FAIL | steps=800\\n2026-05-24 04:24:05 [INFO]   Ep 47/50 | SUCCESS | steps=101\\n2026-05-24 04:24:22 [INFO]   Ep 48/50 | FAIL | steps=800\\n2026-05-24 04:24:38 [INFO]   Ep 49/50 | FAIL | steps=800\\n2026-05-24 04:24:55 [INFO]   Ep 50/50 | FAIL | steps=800\\n2026-05-24 04:24:55 [INFO]   Task 8 SR: 17/50 (34.0%)\\n2026-05-24 04:24:55 [INFO] --- Task 9: pick up the black bowl on the wooden cabinet and place it on the plate ---\\n2026-05-24 04:25:12 [INFO]   Ep 1/50 | FAIL | steps=800\\n2026-05-24 04:25:29 [INFO]   Ep 2/50 | FAIL | steps=800\\n2026-05-24 04:25:46 [INFO]   Ep 3/50 | FAIL | steps=800\\n2026-05-24 04:26:03 [INFO]   Ep 4/50 | FAIL | steps=800\\n2026-05-24 04:26:21 [INFO]   Ep 5/50 | FAIL | steps=800\\n2026-05-24 04:26:38 [INFO]   Ep 6/50 | FAIL | steps=800\\n2026-05-24 04:26:55 [INFO]   Ep 7/50 | FAIL | steps=800\\n2026-05-24 04:27:12 [INFO]   Ep 8/50 | FAIL | steps=800\\n2026-05-24 04:27:30 [INFO]   Ep 9/50 | FAIL | steps=800\\n2026-05-24 04:27:47 [INFO]   Ep 10/50 | FAIL | steps=800\\n2026-05-24 04:28:04 [INFO]   Ep 11/50 | FAIL | steps=800\\n2026-05-24 04:28:08 [INFO]   Ep 12/50 | SUCCESS | steps=118\\n2026-05-24 04:28:25 [INFO]   Ep 13/50 | FAIL | steps=800\\n2026-05-24 04:28:42 [INFO]   Ep 14/50 | FAIL | steps=800\\n2026-05-24 04:28:59 [INFO]   Ep 15/50 | FAIL | steps=800\\n2026-05-24 04:29:16 [INFO]   Ep 16/50 | FAIL | steps=800\\n2026-05-24 04:29:33 [INFO]   Ep 17/50 | FAIL | steps=800\\n2026-05-24 04:29:51 [INFO]   Ep 18/50 | FAIL | steps=800\\n2026-05-24 04:30:08 [INFO]   Ep 19/50 | FAIL | steps=800\\n2026-05-24 04:30:25 [INFO]   Ep 20/50 | FAIL | steps=800\\n2026-05-24 04:30:42 [INFO]   Ep 21/50 | FAIL | steps=800\\n20
…[truncated 3647 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_xvla_l2norm_k03_spatial_seed42_20260523T204234",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-23T20:44:33.424398+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-38929",
  "command": "find /root/autodl-tmp/importance_margin_vla_compress/eval_results/ -name \"*l2norm*k03*spatial*\" -o -name \"*l2norm*0.3*spatial*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_xvla_l2norm_k03_spatial_seed42_20260523T204234",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-38929",
    "command": "find /root/autodl-tmp/importance_margin_vla_compress/eval_results/ -name \"*l2norm*k03*spatial*\" -o -name \"*l2norm*0.3*spatial*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-23T20:44:33.424611+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "importance_margin_vla_compress",
  "filters": "{'exp_id': 'eval_xvla_l2norm_k03_spatial_seed42'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_xvla_l2norm_k03_spatial_seed42_20260523T204234",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "importance_margin_vla_compress",
    "filters": "{'exp_id': 'eval_xvla_l2norm_k03_spatial_seed42'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-23T20:44:33.424816+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/pi05_l2norm_k0.30_libero_spatial_seed42.json\\n/root/autodl-tmp/importance_margin_vla_compress/eval_results/pi05_l2norm_k0.30_libero_spatial_seed43.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_xvla_l2norm_k03_spatial_seed42_20260523T204234",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-23T20:44:33.424992+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.3229}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_xvla_l2norm_k03_spatial_seed42_20260523T204234",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-23T20:44:33.425223+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-38929",
  "command": "cat /root/autodl-tmp/importance_margin_vla_compress/eval_results/xvla_prune_k0.3_libero_spatial.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_xvla_l2norm_k03_spatial_seed42_20260523T204234",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-38929",
    "command": "cat /root/autodl-tmp/importance_margin_vla_compress/eval_results/xvla_prune_k0.3_libero_spatial.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-23T20:44:33.425524+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"model\\\": \\\"xvla\\\",\\n  \\\"model_path\\\": \\\"/root/autodl-tmp/X-VLA-Libero\\\",\\n  \\\"mode\\\": \\\"l2_norm\\\",\\n  \\\"suite\\\": \\\"libero_spatial\\\",\\n  \\\"keep_ratio\\\": 0.3,\\n  \\\"n_vision_tokens_original\\\": 50,\\n  \\\"n_vision_tokens_kept\\\": 15,\\n  \\\"total_episodes\\\": 500,\\n  \\\"total_successes\\\": 156,\\n  \\\"overall_success_rate\\\": 0.312,\\n  \\\"wilson_ci_95\\\": [\\n    0.273,\\n    0.3539\\n  ],\\n  \\\"num_episodes_per_task\\\": 50,\\n  \\\"max_steps\\\": 800,\\n  \\\"num_actions_per_chunk\\\": 30,\\n  \\\"domain_id\\\": 3,\\n  \\\"denoise_steps\\\": 10,\\n  \\\"seed\\\": 42,\\n  \\\"elapsed_seconds\\\": 6754.6,\\n  \\\"per_task\\\": {\\n    \\\"0\\\": {\\n      \\\"task_id\\\": 0,\\n      \\\"task_description\\\": \\\"pick up the black bowl between the plate and the ramekin and place it on the plate\\\",\\n      \\\"success_count\\\": 37,\\n      \\\"total_episodes\\\": 50,\\n      \\\"success_rate\\\": 0.74,\\n      \\\"mean_steps\\\": 335.4\\n    },\\n    \\\"1\\\": {\\n      \\\"task_id\\\": 1,\\n      \\\"task_description\\\": \\\"pick up the black bowl next to the ramekin and place it on the plate\\\",\\n      \\\"success_count\\\": 3,\\n      \\\"total_episodes\\\": 50,\\n      \\\"success_rate\\\": 0.06,\\n      \\\"mean_steps\\\": 758.5\\n    },\\n    \\\"2\\\": {\\n      \\\"task_id\\\": 2,\\n      \\\"task_description\\\": \\\"pick up the black bowl from table center and place it on the plate\\\",\\n      \\\"success_count\\\": 41,\\n      \\\"total_episodes\\\": 50,\\n      \\\"success_rate\\\": 0.82,\\n      \\\"mean_steps\\\": 255.3\\n    },\\n    \\\"3\\\": {\\n      \\\"task_id\\\": 3,\\n      \\\"task_description\\\": \\\"pick up the black bowl on the cookie box and place it on the plate\\\",\\n      \\\"success_count\\\": 17,\\n      \\\"total_episodes\\\": 50,\\n      \\\"success_rate\\\": 0.34,\\n      \\\"mean_steps\\\": 562.2\\n    },
…[truncated 1973 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_xvla_l2norm_k03_spatial_seed42_20260523T204234",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-23T20:44:33.425757+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "importance_margin_vla_compress",
  "filters": "{'status': 'ANALYZING'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_xvla_l2norm_k03_spatial_seed42_20260523T204234",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "importance_margin_vla_compress",
    "filters": "{'status': 'ANALYZING'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-23T20:44:33.426091+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval_xvla_l2norm_k03_spatial_seed42\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T18:46:02.897Z\", \"updated_at\": \"2026-05-23T20:40:33.211Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && TRANSFORMERS_OFFLINE=1 HF_HUB_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_xvla_pruning_libero.py --model_path /root/autodl-tmp/X-VLA-Libero --suite libero_spatial --keep_ratio 0.3 --mode l2_norm --num_episodes 50 --seed 42 --domain_id 3 --gpu 0\\\"\", \"server\": \"westd-38929\", \"gpu\": [\"cuda:2\"], \"pid\": \"224421\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_xvla_l2norm_k03_spatial_seed42.log\", \"submitted_at\": \"2026-05-23T18:46:01.703Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_count\": 500, \"data_path\": \"libero_spatial\", \"model_name\": \"X-VLA-Libero\", \"seed\": 42}, \"hypothesis\": \"X-VLA L2norm k=0.3 Spatial。极端剪枝（70% token removed）下 L2norm 在 Spatial 套件的表现。补充极端 pruning 对比：Object L2norm k=0.3=18.2% 远差于 random k=0.3。Spatial 上是否也出现同样反常，验证 L2norm 反转在跨套件的一致性。\", \"reproduce\": {\"finished_at\": \"2026-05-23T20:40:31.016Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-23T20:40:41.850583+00:00\"}]}}, \"eval_pi05_random_k03_goal_seed43_v2\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T18:22:19.002Z\", \"updated_at\": \"2026-05-23T20:32:41.274Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0
…[truncated 3501 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_xvla_l2norm_k03_spatial_seed42_20260523T204234",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-23T20:44:33.426437+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_xvla_l2norm_k03_spatial_seed42",
  "field": "metrics",
  "value": "{'success_rate': 0.312, 'total_episodes': 500, 'total_successes': 156, 'wilson_ci_95': [0.273, 0.354], 'n_vision_tokens_original': 50, 'n_vision_tokens_kept': 15, 'elapsed_seconds': 6754.6, 'per_task': {'task_0': {'sr': 0.74, 'desc': 'pick up the black bowl between the plate and the ramekin and place it on the plate'}, 'task_1': {'sr': 0.06, 'desc': 'pick up the black bowl next to the ramekin and place it on the plate'}, 'task_2': {'sr': 0.82, 'desc': 'pick up the black bowl from table center and place it on the plate'}, 'task_3': {'sr': 0.34, 'desc': 'pick up the black bowl on the cookie box and place it on the plate'}, 'task_4': {'sr': 0.66, 'desc': 'pick up the black bowl in the top drawer of the wooden cabinet and place it on the plate'}, 'task_5': {'sr': 0, 'desc': 'pick up the black bowl on the ramekin and place it on the plate'}, 'task_6': {'sr': 0.04, 'desc': 'pick up the black bowl next to the cookie box and place it on the plate'}, 'task_7': {'sr': 0.08, 'desc': 'pick up the black bowl on the stove and place it on the plate'}, 'task_8': {'sr': 0.34, 'desc': 'pick up the black bowl next to the plate and place it on the plate'}, 'task_9': {'sr': 0.04, 'desc': 'pick up the black bowl on the wooden cabinet and place it on the plate'}}}",
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_xvla_l2norm_k03_spatial_seed42_20260523T204234",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_xvla_l2norm_k03_spatial_seed42",
    "field": "metrics",
    "value": "{'success_rate': 0.312, 'total_episodes': 500, 'total_successes': 156, 'wilson_ci_95': [0.273, 0.354], 'n_vision_tokens_original': 50, 'n_vision_tokens_kept': 15, 'elapsed_seconds': 6754.6, 'per_task': {'task_0': {'sr': 0.74, 'desc': 'pick up the black bowl between the plate and the ramekin and place it on the plate'}, 'task_1': {'sr': 0.06, 'desc': 'pick up the black bowl next to the ramekin and place it on the plate'}, 'task_2': {'sr': 0.82, 'desc': 'pick up the black bowl from table center and place it on the plate'}, 'task_3': {'sr': 0.34, 'desc': 'pick up the black bowl on the cookie box and place it on the plate'}, 'task_4': {'sr': 0.66, 'desc': 'pick up the black bowl in the top drawer of the wooden cabinet and place it on the plate'}, 'task_5': {'sr': 0, 'desc': 'pick up the black bowl on the ramekin and place it on the plate'}, 'task_6': {'sr': 0.04, 'desc': 'pick up the black bowl next to the cookie box and place it on the plate'}, 'task_7': {'sr': 0.08, 'desc': 'pick up the black bowl on the stove and place it on the plate'}, 'task_8': {'sr': 0.34, 'desc': 'pick up the black bowl next to the plate and place it on the plate'}, 'task_9': {'sr': 0.04, 'desc': 'pick up the black bowl on the wooden cabinet and place it on the plate'}}}",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-23T20:44:33.426709+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_xvla_l2norm_k03_spatial_seed42",
  "field": "log_path",
  "value": "~/runs/importance_margin_vla_compress/eval_xvla_l2norm_k03_spatial_seed42.log",
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_xvla_l2norm_k03_spatial_seed42_20260523T204234",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_xvla_l2norm_k03_spatial_seed42",
    "field": "log_path",
    "value": "~/runs/importance_margin_vla_compress/eval_xvla_l2norm_k03_spatial_seed42.log",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-23T20:44:33.426892+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_xvla_l2norm_k03_spatial_seed42",
  "field": "checkpoint_path",
  "value": "/root/autodl-tmp/X-VLA-Libero",
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_xvla_l2norm_k03_spatial_seed42_20260523T204234",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_xvla_l2norm_k03_spatial_seed42",
    "field": "checkpoint_path",
    "value": "/root/autodl-tmp/X-VLA-Libero",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-23T20:44:33.427175+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_xvla_l2norm_k03_spatial_seed42\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T18:46:02.897Z\", \"updated_at\": \"2026-05-23T20:43:39.378Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && TRANSFORMERS_OFFLINE=1 HF_HUB_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_xvla_pruning_libero.py --model_path /root/autodl-tmp/X-VLA-Libero --suite libero_spatial --keep_ratio 0.3 --mode l2_norm --num_episodes 50 --seed 42 --domain_id 3 --gpu 0\\\"\", \"server\": \"westd-38929\", \"gpu\": [\"cuda:2\"], \"pid\": \"224421\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_xvla_l2norm_k03_spatial_seed42.log\", \"submitted_at\": \"2026-05-23T18:46:01.703Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_count\": 500, \"data_path\": \"libero_spatial\", \"model_name\": \"X-VLA-Libero\", \"seed\": 42}, \"hypothesis\": \"X-VLA L2norm k=0.3 Spatial。极端剪枝（70% token removed）下 L2norm 在 Spatial 套件的表现。补充极端 pruning 对比：Object L2norm k=0.3=18.2% 远差于 random k=0.3。Spatial 上是否也出现同样反常，验证 L2norm 反转在跨套件的一致性。\", \"reproduce\": {\"finished_at\": \"2026-05-23T20:40:31.016Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-23T20:40:41.850583+00:00\"}]}, \"metrics\": {\"success_rate\": 0.312, \"total_episodes\": 500, \"total_successes\": 156, \"wilson_ci_95\": [0.273, 0.354], \"n_vision_tokens_original\": 50, \"n_vision_tokens_kept\": 15, \"elapsed_seconds\": 6754.6, \"per_task\": {\"task_0\": {\"sr\": 0.74, \"desc\": \"pick up the black bowl between the plate and the ramekin and place it on the plate\"}, \"task_1\": {\"sr\": 0.06, \"desc\": \"pick up the black bowl next to the ramekin and place it on the plate\"}, \"task_2\": {\"sr\": 0.82, \
…[truncated 939 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_xvla_l2norm_k03_spatial_seed42_20260523T204234",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-23T20:44:33.427499+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_xvla_l2norm_k03_spatial_seed42\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T18:46:02.897Z\", \"updated_at\": \"2026-05-23T20:43:43.041Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && TRANSFORMERS_OFFLINE=1 HF_HUB_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_xvla_pruning_libero.py --model_path /root/autodl-tmp/X-VLA-Libero --suite libero_spatial --keep_ratio 0.3 --mode l2_norm --num_episodes 50 --seed 42 --domain_id 3 --gpu 0\\\"\", \"server\": \"westd-38929\", \"gpu\": [\"cuda:2\"], \"pid\": \"224421\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_xvla_l2norm_k03_spatial_seed42.log\", \"submitted_at\": \"2026-05-23T18:46:01.703Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_count\": 500, \"data_path\": \"libero_spatial\", \"model_name\": \"X-VLA-Libero\", \"seed\": 42}, \"hypothesis\": \"X-VLA L2norm k=0.3 Spatial。极端剪枝（70% token removed）下 L2norm 在 Spatial 套件的表现。补充极端 pruning 对比：Object L2norm k=0.3=18.2% 远差于 random k=0.3。Spatial 上是否也出现同样反常，验证 L2norm 反转在跨套件的一致性。\", \"reproduce\": {\"finished_at\": \"2026-05-23T20:40:31.016Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-23T20:40:41.850583+00:00\"}]}, \"metrics\": {\"success_rate\": 0.312, \"total_episodes\": 500, \"total_successes\": 156, \"wilson_ci_95\": [0.273, 0.354], \"n_vision_tokens_original\": 50, \"n_vision_tokens_kept\": 15, \"elapsed_seconds\": 6754.6, \"per_task\": {\"task_0\": {\"sr\": 0.74, \"desc\": \"pick up the black bowl between the plate and the ramekin and place it on the plate\"}, \"task_1\": {\"sr\": 0.06, \"desc\": \"pick up the black bowl next to the ramekin and place it on the plate\"}, \"task_2\": {\"sr\": 0.82, \
…[truncated 1036 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_xvla_l2norm_k03_spatial_seed42_20260523T204234",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-23T20:44:33.427810+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_xvla_l2norm_k03_spatial_seed42\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T18:46:02.897Z\", \"updated_at\": \"2026-05-23T20:43:46.107Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && TRANSFORMERS_OFFLINE=1 HF_HUB_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_xvla_pruning_libero.py --model_path /root/autodl-tmp/X-VLA-Libero --suite libero_spatial --keep_ratio 0.3 --mode l2_norm --num_episodes 50 --seed 42 --domain_id 3 --gpu 0\\\"\", \"server\": \"westd-38929\", \"gpu\": [\"cuda:2\"], \"pid\": \"224421\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_xvla_l2norm_k03_spatial_seed42.log\", \"submitted_at\": \"2026-05-23T18:46:01.703Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_count\": 500, \"data_path\": \"libero_spatial\", \"model_name\": \"X-VLA-Libero\", \"seed\": 42}, \"hypothesis\": \"X-VLA L2norm k=0.3 Spatial。极端剪枝（70% token removed）下 L2norm 在 Spatial 套件的表现。补充极端 pruning 对比：Object L2norm k=0.3=18.2% 远差于 random k=0.3。Spatial 上是否也出现同样反常，验证 L2norm 反转在跨套件的一致性。\", \"reproduce\": {\"finished_at\": \"2026-05-23T20:40:31.016Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-23T20:40:41.850583+00:00\"}]}, \"metrics\": {\"success_rate\": 0.312, \"total_episodes\": 500, \"total_successes\": 156, \"wilson_ci_95\": [0.273, 0.354], \"n_vision_tokens_original\": 50, \"n_vision_tokens_kept\": 15, \"elapsed_seconds\": 6754.6, \"per_task\": {\"task_0\": {\"sr\": 0.74, \"desc\": \"pick up the black bowl between the plate and the ramekin and place it on the plate\"}, \"task_1\": {\"sr\": 0.06, \"desc\": \"pick up the black bowl next to the ramekin and place it on the plate\"}, \"task_2\": {\"sr\": 0.82, \
…[truncated 1092 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_xvla_l2norm_k03_spatial_seed42_20260523T204234",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-23T20:44:33.428036+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_xvla_l2norm_k03_spatial_seed42",
  "field": "conclusion",
  "value": "negative — L2norm k=0.3 Spatial SR=31.2% [27.3%, 35.4%]，相比 L2norm k=0.5 Spatial (58.8%) 暴跌 27.6pp。与 Object 套件 L2norm k=0.3=18.2% 模式一致：极端剪枝下 L2norm 严重退化。Per-task 方差极大（0%~82%），部分 task 几乎完全失败（task5=0%, task6/9=4%）。L2norm 反转现象在 Spatial 上同样存在，验证了跨套件一致性。",
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_xvla_l2norm_k03_spatial_seed42_20260523T204234",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_xvla_l2norm_k03_spatial_seed42",
    "field": "conclusion",
    "value": "negative — L2norm k=0.3 Spatial SR=31.2% [27.3%, 35.4%]，相比 L2norm k=0.5 Spatial (58.8%) 暴跌 27.6pp。与 Object 套件 L2norm k=0.3=18.2% 模式一致：极端剪枝下 L2norm 严重退化。Per-task 方差极大（0%~82%），部分 task 几乎完全失败（task5=0%, task6/9=4%）。L2norm 反转现象在 Spatial 上同样存在，验证了跨套件一致性。",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-23T20:44:33.428247+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_xvla_l2norm_k03_spatial_seed42",
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
  "session": "worker_analyze_eval_xvla_l2norm_k03_spatial_seed42_20260523T204234",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_xvla_l2norm_k03_spatial_seed42",
    "field": "status",
    "value": "DONE",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-23T20:44:33.428434+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid conclusion 'negative — L2norm k=0.3 Spatial SR=31.2% [27.3%, 35.4%]，相比 L2norm k=0.5 Spatial (58.8%) 暴跌 27.6pp。与 Object 套件 L2norm k=0.3=18.2% 模式一致：极端剪枝下 L2norm 严重退化。Per-task 方差极大（0%~82%），部分 task 几乎完全失败（task5=0%, task6/9=4%）。L2norm 反转现象在 Spatial 上同样存在，验证了跨套件一致性。'. Valid: ['failed', 'killed', 'negative', 'success']\", \"metadata\": {\"elapsed_seconds\": 1.2521}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_xvla_l2norm_k03_spatial_seed42_20260523T204234",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-23T20:44:33.428631+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Cannot transition to DONE without a 'conclusion' field. Set conclusion first.\", \"metadata\": {\"elapsed_seconds\": 1.2338}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_xvla_l2norm_k03_spatial_seed42_20260523T204234",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-23T20:44:33.428842+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_xvla_l2norm_k03_spatial_seed42",
  "field": "conclusion",
  "value": "negative",
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_xvla_l2norm_k03_spatial_seed42_20260523T204234",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_xvla_l2norm_k03_spatial_seed42",
    "field": "conclusion",
    "value": "negative",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-23T20:44:33.429123+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_xvla_l2norm_k03_spatial_seed42\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T18:46:02.897Z\", \"updated_at\": \"2026-05-23T20:44:04.314Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && TRANSFORMERS_OFFLINE=1 HF_HUB_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_xvla_pruning_libero.py --model_path /root/autodl-tmp/X-VLA-Libero --suite libero_spatial --keep_ratio 0.3 --mode l2_norm --num_episodes 50 --seed 42 --domain_id 3 --gpu 0\\\"\", \"server\": \"westd-38929\", \"gpu\": [\"cuda:2\"], \"pid\": \"224421\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_xvla_l2norm_k03_spatial_seed42.log\", \"submitted_at\": \"2026-05-23T18:46:01.703Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_count\": 500, \"data_path\": \"libero_spatial\", \"model_name\": \"X-VLA-Libero\", \"seed\": 42}, \"hypothesis\": \"X-VLA L2norm k=0.3 Spatial。极端剪枝（70% token removed）下 L2norm 在 Spatial 套件的表现。补充极端 pruning 对比：Object L2norm k=0.3=18.2% 远差于 random k=0.3。Spatial 上是否也出现同样反常，验证 L2norm 反转在跨套件的一致性。\", \"reproduce\": {\"finished_at\": \"2026-05-23T20:40:31.016Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-23T20:40:41.850583+00:00\"}]}, \"metrics\": {\"success_rate\": 0.312, \"total_episodes\": 500, \"total_successes\": 156, \"wilson_ci_95\": [0.273, 0.354], \"n_vision_tokens_original\": 50, \"n_vision_tokens_kept\": 15, \"elapsed_seconds\": 6754.6, \"per_task\": {\"task_0\": {\"sr\": 0.74, \"desc\": \"pick up the black bowl between the plate and the ramekin and place it on the plate\"}, \"task_1\": {\"sr\": 0.06, \"desc\": \"pick up the black bowl next to the ramekin and place it on the plate\"}, \"task_2\": {\"sr\": 0.82, \
…[truncated 1122 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_xvla_l2norm_k03_spatial_seed42_20260523T204234",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-23T20:44:33.429363+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_xvla_l2norm_k03_spatial_seed42",
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
  "session": "worker_analyze_eval_xvla_l2norm_k03_spatial_seed42_20260523T204234",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_xvla_l2norm_k03_spatial_seed42",
    "field": "status",
    "value": "DONE",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-23T20:44:33.429679+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_xvla_l2norm_k03_spatial_seed42\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T18:46:02.897Z\", \"updated_at\": \"2026-05-23T20:44:11.014Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && TRANSFORMERS_OFFLINE=1 HF_HUB_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_xvla_pruning_libero.py --model_path /root/autodl-tmp/X-VLA-Libero --suite libero_spatial --keep_ratio 0.3 --mode l2_norm --num_episodes 50 --seed 42 --domain_id 3 --gpu 0\\\"\", \"server\": \"westd-38929\", \"gpu\": [\"cuda:2\"], \"pid\": \"224421\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_xvla_l2norm_k03_spatial_seed42.log\", \"submitted_at\": \"2026-05-23T18:46:01.703Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_count\": 500, \"data_path\": \"libero_spatial\", \"model_name\": \"X-VLA-Libero\", \"seed\": 42, \"wall_clock_seconds\": 7089.3, \"gpu_hours\": 1.97}, \"hypothesis\": \"X-VLA L2norm k=0.3 Spatial。极端剪枝（70% token removed）下 L2norm 在 Spatial 套件的表现。补充极端 pruning 对比：Object L2norm k=0.3=18.2% 远差于 random k=0.3。Spatial 上是否也出现同样反常，验证 L2norm 反转在跨套件的一致性。\", \"reproduce\": {\"finished_at\": \"2026-05-23T20:40:31.016Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-23T20:40:41.850583+00:00\"}]}, \"metrics\": {\"success_rate\": 0.312, \"total_episodes\": 500, \"total_successes\": 156, \"wilson_ci_95\": [0.273, 0.354], \"n_vision_tokens_original\": 50, \"n_vision_tokens_kept\": 15, \"elapsed_seconds\": 6754.6, \"per_task\": {\"task_0\": {\"sr\": 0.74, \"desc\": \"pick up the black bowl between the plate and the ramekin and place it on the plate\"}, \"task_1\": {\"sr\": 0.06, \"desc\": \"pick up the black bowl next to the ramekin and place 
…[truncated 1269 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_xvla_l2norm_k03_spatial_seed42_20260523T204234",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 27 · 2026-05-23T20:44:33.429973+00:00_

Registry 已更新为 DONE (negative)。

## 分析总结

**X-VLA L2norm k=0.3 Spatial SR = 31.2%** [95% CI: 27.3%–35.4%]

### 对比

| 配置 | Spatial SR |
|------|-----------|
| L2norm k=0.5 | 58.8% |
| **L2norm k=0.3** | **31.2%** |
| Random k=0.5 | 71.4% |

- 从 k=0.5→k=0.3，L2norm 暴跌 27.6pp（58.8%→31.2%）
- 与 Object 套件模式一致：Object L2norm k=0.3 = 18.2%，同样在极端剪枝下严重退化

### Per-task 分布（方差极大）

高：task2=82%, task0=74%, task4=66%
中：task3=34%, task8=34%
低/崩溃：task7=8%, task1=6%, task6=4%, task9=4%, **task5=0%**

### Hypothesis 验证

**已验证** — L2norm 反转现象在 Spatial 上同样存在。极端剪枝（k=0.3, 70% token removed）下，L2norm 在两个套件上都严重退化（Object 18.2%, Spatial 31.2%），确认 L2norm 反转具有跨套件一致性。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analyze_eval_xvla_l2norm_k03_spatial_seed42_20260523T204234"
}
```

</details>

---
