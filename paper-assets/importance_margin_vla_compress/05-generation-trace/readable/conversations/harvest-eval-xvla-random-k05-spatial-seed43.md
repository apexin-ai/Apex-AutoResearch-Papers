# harvest eval xvla random k05 spatial seed43

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 0
- **Tool calls:** 5
- **Original source:** `logs/chats/worker_harvest_eval_xvla_random_k05_spatial_seed43_20260524T012028.jsonl`
- **Structured JSON:** [`7fba4c19d8b8b2bb90d9.json`](../../sessions/7f/7fba4c19d8b8b2bb90d9.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

11 recorded events

### Tool call

_source line 1 · 2026-05-24T01:21:39.982889+00:00_

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
  "session": "worker_harvest_eval_xvla_random_k05_spatial_seed43_20260524T012028",
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

_source line 2 · 2026-05-24T01:21:39.983253+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_eval_xvla_random_k05_spatial_seed43_20260524T012028",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-24T01:21:39.983455+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-38929",
  "command": "tail -100 /root/autodl-tmp/importance_margin_vla_compress/logs/eval_xvla_random_k05_spatial_seed43.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_eval_xvla_random_k05_spatial_seed43_20260524T012028",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-38929",
    "command": "tail -100 /root/autodl-tmp/importance_margin_vla_compress/logs/eval_xvla_random_k05_spatial_seed43.log",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-24T01:21:39.983596+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-38929",
  "command": "cat /root/autodl-tmp/importance_margin_vla_compress/eval_results/eval_xvla_random_k05_spatial_seed43.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_eval_xvla_random_k05_spatial_seed43_20260524T012028",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-38929",
    "command": "cat /root/autodl-tmp/importance_margin_vla_compress/eval_results/eval_xvla_random_k05_spatial_seed43.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-24T01:21:39.983798+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-24 07:19:24 [INFO]   Ep 21/50 | FAIL | steps=800\\n2026-05-24 07:19:27 [INFO]   Ep 22/50 | SUCCESS | steps=98\\n2026-05-24 07:19:31 [INFO]   Ep 23/50 | SUCCESS | steps=90\\n2026-05-24 07:19:35 [INFO]   Ep 24/50 | SUCCESS | steps=94\\n2026-05-24 07:19:39 [INFO]   Ep 25/50 | SUCCESS | steps=98\\n2026-05-24 07:19:43 [INFO]   Ep 26/50 | SUCCESS | steps=96\\n2026-05-24 07:19:46 [INFO]   Ep 27/50 | SUCCESS | steps=88\\n2026-05-24 07:19:50 [INFO]   Ep 28/50 | SUCCESS | steps=95\\n2026-05-24 07:19:54 [INFO]   Ep 29/50 | SUCCESS | steps=100\\n2026-05-24 07:20:05 [INFO]   Ep 30/50 | SUCCESS | steps=501\\n2026-05-24 07:20:11 [INFO]   Ep 31/50 | SUCCESS | steps=223\\n2026-05-24 07:20:15 [INFO]   Ep 32/50 | SUCCESS | steps=95\\n2026-05-24 07:20:19 [INFO]   Ep 33/50 | SUCCESS | steps=98\\n2026-05-24 07:20:23 [INFO]   Ep 34/50 | SUCCESS | steps=98\\n2026-05-24 07:20:40 [INFO]   Ep 35/50 | FAIL | steps=800\\n2026-05-24 07:20:44 [INFO]   Ep 36/50 | SUCCESS | steps=94\\n2026-05-24 07:20:48 [INFO]   Ep 37/50 | SUCCESS | steps=100\\n2026-05-24 07:20:52 [INFO]   Ep 38/50 | SUCCESS | steps=93\\n2026-05-24 07:20:56 [INFO]   Ep 39/50 | SUCCESS | steps=88\\n2026-05-24 07:21:00 [INFO]   Ep 40/50 | SUCCESS | steps=93\\n2026-05-24 07:21:03 [INFO]   Ep 41/50 | SUCCESS | steps=91\\n2026-05-24 07:21:21 [INFO]   Ep 42/50 | FAIL | steps=800\\n2026-05-24 07:21:24 [INFO]   Ep 43/50 | SUCCESS | steps=89\\n2026-05-24 07:21:28 [INFO]   Ep 44/50 | SUCCESS | steps=102\\n2026-05-24 07:21:32 [INFO]   Ep 45/50 | SUCCESS | steps=96\\n2026-05-24 07:21:36 [INFO]   Ep 46/50 | SUCCESS | steps=93\\n2026-05-24 07:21:40 [INFO]   Ep 47/50 | SUCCESS | steps=91\\n2026-05-24 07:21:56 [INFO]   Ep 48/50 | FAIL | steps=800\\n2026-05-24 07:22:00 [INFO]   Ep 49/50 | SUCCESS | steps=91\\n2026-05-24 07:22:04 [INFO]   Ep 50/50 | SUCCESS | steps=94\\n2026-05-24 07:22:04 [INFO]   Task 8 SR: 46/50 (92.0%)\\n2026-05-24 07:22:04 [INFO] --- Task 9: pick up the black bowl
…[truncated 5032 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_eval_xvla_random_k05_spatial_seed43_20260524T012028",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-24T01:21:39.983963+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-38929",
  "command": "nvidia-smi --query-gpu=index,name,utilization.gpu,memory.used,memory.total --format=csv,noheader",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_eval_xvla_random_k05_spatial_seed43_20260524T012028",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-38929",
    "command": "nvidia-smi --query-gpu=index,name,utilization.gpu,memory.used,memory.total --format=csv,noheader",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-24T01:21:39.984192+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"model\\\": \\\"xvla\\\",\\n  \\\"model_path\\\": \\\"/root/autodl-tmp/X-VLA-Libero\\\",\\n  \\\"mode\\\": \\\"random\\\",\\n  \\\"suite\\\": \\\"libero_spatial\\\",\\n  \\\"keep_ratio\\\": 0.5,\\n  \\\"n_vision_tokens_original\\\": 50,\\n  \\\"n_vision_tokens_kept\\\": 25,\\n  \\\"total_episodes\\\": 500,\\n  \\\"total_successes\\\": 363,\\n  \\\"overall_success_rate\\\": 0.726,\\n  \\\"wilson_ci_95\\\": [\\n    0.6853,\\n    0.7633\\n  ],\\n  \\\"num_episodes_per_task\\\": 50,\\n  \\\"max_steps\\\": 800,\\n  \\\"num_actions_per_chunk\\\": 30,\\n  \\\"domain_id\\\": 3,\\n  \\\"denoise_steps\\\": 10,\\n  \\\"seed\\\": 43,\\n  \\\"elapsed_seconds\\\": 3860.3,\\n  \\\"per_task\\\": {\\n    \\\"0\\\": {\\n      \\\"task_id\\\": 0,\\n      \\\"task_description\\\": \\\"pick up the black bowl between the plate and the ramekin and place it on the plate\\\",\\n      \\\"success_count\\\": 50,\\n      \\\"total_episodes\\\": 50,\\n      \\\"success_rate\\\": 1.0,\\n      \\\"mean_steps\\\": 81.2\\n    },\\n    \\\"1\\\": {\\n      \\\"task_id\\\": 1,\\n      \\\"task_description\\\": \\\"pick up the black bowl next to the ramekin and place it on the plate\\\",\\n      \\\"success_count\\\": 19,\\n      \\\"total_episodes\\\": 50,\\n      \\\"success_rate\\\": 0.38,\\n      \\\"mean_steps\\\": 551.8\\n    },\\n    \\\"2\\\": {\\n      \\\"task_id\\\": 2,\\n      \\\"task_description\\\": \\\"pick up the black bowl from table center and place it on the plate\\\",\\n      \\\"success_count\\\": 44,\\n      \\\"total_episodes\\\": 50,\\n      \\\"success_rate\\\": 0.88,\\n      \\\"mean_steps\\\": 177.5\\n    },\\n    \\\"3\\\": {\\n      \\\"task_id\\\": 3,\\n      \\\"task_description\\\": \\\"pick up the black bowl on the cookie box and place it on the plate\\\",\\n      \\\"success_count\\\": 46,\\n      \\\"total_episodes\\\": 50,\\n      \\\"success_rate\\\": 0.92,\\n      \\\"mean_steps\\\": 143.3\\n    },\
…[truncated 1975 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_eval_xvla_random_k05_spatial_seed43_20260524T012028",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-24T01:21:39.984365+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"0, NVIDIA RTX PRO 6000 Blackwell Server Edition, 82 %, 4872 MiB, 97887 MiB\\n1, NVIDIA RTX PRO 6000 Blackwell Server Edition, 0 %, 1 MiB, 97887 MiB\\n2, NVIDIA RTX PRO 6000 Blackwell Server Edition, 47 %, 4856 MiB, 97887 MiB\\n3, NVIDIA RTX PRO 6000 Blackwell Server Edition, 1 %, 4938 MiB, 97887 MiB\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.63}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_eval_xvla_random_k05_spatial_seed43_20260524T012028",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-24T01:21:39.984576+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_xvla_random_k05_spatial_seed43",
  "field": "status",
  "value": "DONE",
  "project": "importance_margin_vla_compress",
  "spec": "{'log_path': '/root/autodl-tmp/importance_margin_vla_compress/logs/eval_xvla_random_k05_spatial_seed43.log', 'checkpoint_path': 'N/A'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_eval_xvla_random_k05_spatial_seed43_20260524T012028",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_xvla_random_k05_spatial_seed43",
    "field": "status",
    "value": "DONE",
    "project": "importance_margin_vla_compress",
    "spec": "{'log_path': '/root/autodl-tmp/importance_margin_vla_compress/logs/eval_xvla_random_k05_spatial_seed43.log', 'checkpoint_path': 'N/A'}"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-24T01:21:39.984804+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_xvla_random_k05_spatial_seed43\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T22:30:07.182Z\", \"updated_at\": \"2026-05-24T01:21:13.962Z\", \"hypothesis\": \"Random token pruning at 50% keep ratio on X-VLA will degrade spatial task performance, serving as a lower-bound baseline for comparing against importance-based pruning methods\", \"spec\": {\"command\": \"python -u eval_xvla_pruning_libero.py --model_path /root/autodl-tmp/X-VLA-Libero --suite libero_spatial --keep_ratio 0.5 --mode random --num_episodes 50 --seed 43 --domain_id 3 --gpu 0 --output eval_results/eval_xvla_random_k05_spatial_seed43.json\", \"server\": \"westd-38929\", \"gpu\": [\"cuda:3\"], \"pid\": \"155546\", \"data_path\": \"libero_spatial\", \"data_count\": 500, \"model_name\": \"X-VLA-Libero\", \"seed\": 43, \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_xvla_random_k05_spatial_seed43.log\", \"checkpoint_path\": \"N/A\"}, \"reproduce\": {\"finished_at\": \"2026-05-23T23:38:46.087Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-23T23:38:57.228Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-23T23:39:15.083334+00:00\"}]}, \"metrics\": {\"overall_SR\": 0.726, \"total_successes\": 363, \"total_episodes\": 500, \"wilson_ci_95\": [0.685, 0.763], \"per_task\": {\"T0_bowl_between_plate_ramekin\": 1, \"T1_bowl_next_ramekin\": 0.38, \"T2_bowl_table_center\": 0.88, \"T3_bowl_cookie_box\": 0.92, \"T4_bowl_top_drawer\": 0.88, \"T5_bowl_on_ramekin\": 0, \"T6_bowl_next_cookie_box\": 0.94, \"T7_bowl_stove\": 0.68, \"T8_bowl_next_plate\": 0.92, \"T9_bowl_wooden_cabinet\": 0.66}}, \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_xvla_random_k05_spatial_seed43.log\", \"checkpoint_path\": \"n/a (inference-
…[truncated 130 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_eval_xvla_random_k05_spatial_seed43_20260524T012028",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-24T01:21:39.985045+00:00_

Registry updated. Results summary:

| Metric | Value |
|--------|-------|
| **Overall SR** | **72.6%** (363/500) |
| **95% Wilson CI** | [68.5%, 76.3%] |
| **Elapsed** | 64.3 min |
| **Conclusion** | success (hypothesis confirmed: random pruning degrades spatial performance) |

**Per-task SR**: T0=100%, T1=38%, T2=88%, T3=92%, T4=88%, T5=0%, T6=94%, T7=68%, T8=92%, T9=66%

**Consistency with seed42** (71.4%): seed43=72.6%, within CI — highly consistent.

**westd-38929 GPU status** (4× RTX PRO 6000 Blackwell, 96GB each):

| GPU | Util | VRAM Used | Status |
|-----|------|-----------|--------|
| 0 | 82% | 4.9/96 GB | active |
| 1 | 0% | 0/96 GB | **free** |
| 2 | 47% | 4.9/96 GB | active |
| 3 | 1% | 4.9/96 GB | mostly idle |

GPU 1 is completely free. GPUs 0/2/3 have ~5GB residual memory — likely leftover from eval (no child process running per task description), could be freed by killing the tmux session.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_harvest_eval_xvla_random_k05_spatial_seed43_20260524T012028"
}
```

</details>

---
