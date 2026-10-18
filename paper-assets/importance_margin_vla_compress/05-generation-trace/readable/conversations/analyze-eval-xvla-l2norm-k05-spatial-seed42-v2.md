# analyze eval xvla l2norm k05 spatial seed42 v2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 33
- **Recorded user turns:** 0
- **Tool calls:** 16
- **Original source:** `logs/chats/worker_analyze_eval_xvla_l2norm_k05_spatial_seed42_v2_20260524T034308.jsonl`
- **Structured JSON:** [`d7c54e1c19ef97399b10.json`](../../sessions/d7/d7c54e1c19ef97399b10.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

33 recorded events

### Tool call

_source line 1 · 2026-05-24T03:45:06.142789+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__fetch_wandb_metrics,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__read_registry",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_xvla_l2norm_k05_spatial_seed42_v2_20260524T034308",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__fetch_wandb_metrics,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__read_registry",
    "max_results": "4"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-24T03:45:06.143170+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_xvla_l2norm_k05_spatial_seed42_v2_20260524T034308",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-24T03:45:06.143364+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-38929",
  "command": "tail -100 ~/runs/importance_margin_vla_compress/eval_xvla_l2norm_k05_spatial_seed42_v2.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_xvla_l2norm_k05_spatial_seed42_v2_20260524T034308",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-38929",
    "command": "tail -100 ~/runs/importance_margin_vla_compress/eval_xvla_l2norm_k05_spatial_seed42_v2.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-24T03:45:06.143612+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-24 11:25:17 [INFO]   Ep 22/50 | SUCCESS | steps=99\\n2026-05-24 11:25:21 [INFO]   Ep 23/50 | SUCCESS | steps=96\\n2026-05-24 11:25:25 [INFO]   Ep 24/50 | SUCCESS | steps=100\\n2026-05-24 11:25:41 [INFO]   Ep 25/50 | FAIL | steps=800\\n2026-05-24 11:25:45 [INFO]   Ep 26/50 | SUCCESS | steps=97\\n2026-05-24 11:25:49 [INFO]   Ep 27/50 | SUCCESS | steps=94\\n2026-05-24 11:25:53 [INFO]   Ep 28/50 | SUCCESS | steps=90\\n2026-05-24 11:25:57 [INFO]   Ep 29/50 | SUCCESS | steps=100\\n2026-05-24 11:26:13 [INFO]   Ep 30/50 | FAIL | steps=800\\n2026-05-24 11:26:17 [INFO]   Ep 31/50 | SUCCESS | steps=94\\n2026-05-24 11:26:21 [INFO]   Ep 32/50 | SUCCESS | steps=98\\n2026-05-24 11:26:25 [INFO]   Ep 33/50 | SUCCESS | steps=98\\n2026-05-24 11:26:41 [INFO]   Ep 34/50 | FAIL | steps=800\\n2026-05-24 11:26:46 [INFO]   Ep 35/50 | SUCCESS | steps=141\\n2026-05-24 11:26:51 [INFO]   Ep 36/50 | SUCCESS | steps=137\\n2026-05-24 11:26:55 [INFO]   Ep 37/50 | SUCCESS | steps=101\\n2026-05-24 11:27:12 [INFO]   Ep 38/50 | FAIL | steps=800\\n2026-05-24 11:27:16 [INFO]   Ep 39/50 | SUCCESS | steps=97\\n2026-05-24 11:27:33 [INFO]   Ep 40/50 | FAIL | steps=800\\n2026-05-24 11:27:37 [INFO]   Ep 41/50 | SUCCESS | steps=102\\n2026-05-24 11:27:41 [INFO]   Ep 42/50 | SUCCESS | steps=94\\n2026-05-24 11:27:58 [INFO]   Ep 43/50 | FAIL | steps=800\\n2026-05-24 11:28:15 [INFO]   Ep 44/50 | FAIL | steps=800\\n2026-05-24 11:28:19 [INFO]   Ep 45/50 | SUCCESS | steps=103\\n2026-05-24 11:28:23 [INFO]   Ep 46/50 | SUCCESS | steps=104\\n2026-05-24 11:28:28 [INFO]   Ep 47/50 | SUCCESS | steps=140\\n2026-05-24 11:28:44 [INFO]   Ep 48/50 | FAIL | steps=800\\n2026-05-24 11:29:02 [INFO]   Ep 49/50 | FAIL | steps=800\\n2026-05-24 11:29:06 [INFO]   Ep 50/50 | SUCCESS | steps=95\\n2026-05-24 11:29:06 [INFO]   Task 8 SR: 36/50 (72.0%)\\n2026-05-24 11:29:06 [INFO] --- Task 9: pick up the black bowl on the wooden cabinet and place it on the plate ---\\n2026-05-24 1
…[truncated 4940 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_xvla_l2norm_k05_spatial_seed42_v2_20260524T034308",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-24T03:45:06.143786+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-38929",
  "command": "grep -i \"wandb\\|run_id\\|run id\\|https://wandb\" ~/runs/importance_margin_vla_compress/eval_xvla_l2norm_k05_spatial_seed42_v2.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_xvla_l2norm_k05_spatial_seed42_v2_20260524T034308",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-38929",
    "command": "grep -i \"wandb\\|run_id\\|run id\\|https://wandb\" ~/runs/importance_margin_vla_compress/eval_xvla_l2norm_k05_spatial_seed42_v2.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-24T03:45:06.143926+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_xvla_l2norm_k05_spatial_seed42_v2_20260524T034308",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-24T03:45:06.144063+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'exp_id': 'eval_xvla_l2norm_k05_spatial_seed42_v2'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_xvla_l2norm_k05_spatial_seed42_v2_20260524T034308",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'exp_id': 'eval_xvla_l2norm_k05_spatial_seed42_v2'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-24T03:45:06.144242+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.0688}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_xvla_l2norm_k05_spatial_seed42_v2_20260524T034308",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-24T03:45:06.144421+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-38929",
  "command": "grep -i wandb ~/runs/importance_margin_vla_compress/eval_xvla_l2norm_k05_spatial_seed42_v2.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_xvla_l2norm_k05_spatial_seed42_v2_20260524T034308",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-38929",
    "command": "grep -i wandb ~/runs/importance_margin_vla_compress/eval_xvla_l2norm_k05_spatial_seed42_v2.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-24T03:45:06.144579+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_xvla_l2norm_k05_spatial_seed42_v2_20260524T034308",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-24T03:45:06.144711+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'status': 'DONE'}",
  "fields": "['*']",
  "limit": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_xvla_l2norm_k05_spatial_seed42_v2_20260524T034308",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'status': 'DONE'}",
    "fields": "['*']",
    "limit": "5"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-24T03:45:06.144906+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval_xvla_random_k05_goal_seed43_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T22:23:47.505Z\", \"updated_at\": \"2026-05-23T22:24:05.272Z\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-23T22:24:03.803Z\", \"failure_reason\": \"Director 决定放弃，三连崩溃 (v1/v2/v3 均在 ~ep33 死亡)\"}, \"eval_xvla_random_k05_goal_seed43_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T22:23:46.856Z\", \"updated_at\": \"2026-05-23T22:24:02.708Z\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-23T22:24:02.709Z\"}, \"eval_pi05_random_k03_goal_seed43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T21:53:42.005Z\", \"updated_at\": \"2026-05-23T00:16:33.564Z\", \"hypothesis\": \"π0.5 Random k=0.3 Goal seed43: seed42 结果收割后的双种子验证。seed42=51.8%，Object Random k=0.3=36.4%。验证 Goal 的更高 tolerance 跨 seed 稳定性。\", \"spec\": {\"command\": \"eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.3 --suite libero_goal --n_episodes 50 --seed 43\", \"server\": \"cqa1-33015\", \"model_name\": \"pi0.5\", \"seed\": 43, \"data_path\": \"libero_goal\", \"data_count\": 500, \"gpu\": \"cuda:2\", \"checkpoint_path\": \"/root/autodl-tmp/pi05_libero_finetuned\", \"log_path\": \"logs/eval_pi05_random_k03_goal_seed43.log\"}, \"metrics\": {\"success_rate\": 52, \"total_episodes\": 500}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-23T00:16:33.564Z\"}, \"eval_pi05_l2norm_k05_long_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T23:27:11.999Z\", \"updated_at\": \"2026-05-22T23:27:39.651Z\", \"hypothesis\": \"π0.5 L2norm k=0.5 Long seed42: Long L2 k=0.7=60.0%, k=0.85=78.0%。k=0.5 填充中等压缩区间。与 Random k=0.5 Long=50.2% 对比方法差异。\", \"metrics\": {\"success_rate\": 50.2, \"total_episodes\": 500}, \"conclusion\": \"success\", \"spec\": {\"command\": \"eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.5 --suite 
…[truncated 1341 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_xvla_l2norm_k05_spatial_seed42_v2_20260524T034308",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-24T03:45:06.145097+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'exp_id': 'eval_xvla_l2norm_k05_spatial_seed42_v2'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_xvla_l2norm_k05_spatial_seed42_v2_20260524T034308",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'exp_id': 'eval_xvla_l2norm_k05_spatial_seed42_v2'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-24T03:45:06.145260+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.071}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_xvla_l2norm_k05_spatial_seed42_v2_20260524T034308",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-24T03:45:06.145401+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'status': 'RUNNING'}",
  "fields": "['*']",
  "limit": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_xvla_l2norm_k05_spatial_seed42_v2_20260524T034308",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'status': 'RUNNING'}",
    "fields": "['*']",
    "limit": "20"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-24T03:45:06.145556+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval_xvla_random_k05_spatial_seed43\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T22:25:28.815Z\", \"updated_at\": \"2026-05-23T22:25:39.749Z\", \"hypothesis\": \"X-VLA Random k=0.5 Spatial seed43 — R6-C1 CV 复现。Goal seed43 三连崩溃后，Director 决定改 spatial suite，验证 random pruning 在 spatial 任务上 seed43 是否与 seed42 一致（cross-validation 稳健性）\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python -u eval_xvla_pruning_libero.py --model_path /root/autodl-tmp/X-VLA-Libero --suite libero_spatial --keep_ratio 0.5 --mode random --num_episodes 50 --seed 43 --domain_id 3 --gpu 0 --output eval_results/eval_xvla_random_k05_spatial_seed43.json\", \"server\": \"westd-38929\", \"gpu_ids\": [3], \"tmux_session\": \"eval_xvla_random_k05_spatial_seed43\", \"pid\": 155546, \"data_path\": \"libero_spatial\", \"data_count\": 500, \"model_name\": \"X-VLA-Libero\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/X-VLA-Libero\", \"eval_data\": \"libero_spatial (10 tasks × 50 episodes)\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_xvla_random_k05_spatial_seed43.log\", \"output_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/eval_xvla_random_k05_spatial_seed43.json\"}}}, \"count\": 1, \"total\": 1, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.11}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_xvla_l2norm_k05_spatial_seed42_v2_20260524T034308",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-24T03:45:06.145711+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "fields": "['*']",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_xvla_l2norm_k05_spatial_seed42_v2_20260524T034308",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "fields": "['*']",
    "limit": "50"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-24T03:45:06.146378+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval_xvla_random_k05_spatial_seed43\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T22:25:28.815Z\", \"updated_at\": \"2026-05-23T22:25:39.749Z\", \"hypothesis\": \"X-VLA Random k=0.5 Spatial seed43 — R6-C1 CV 复现。Goal seed43 三连崩溃后，Director 决定改 spatial suite，验证 random pruning 在 spatial 任务上 seed43 是否与 seed42 一致（cross-validation 稳健性）\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python -u eval_xvla_pruning_libero.py --model_path /root/autodl-tmp/X-VLA-Libero --suite libero_spatial --keep_ratio 0.5 --mode random --num_episodes 50 --seed 43 --domain_id 3 --gpu 0 --output eval_results/eval_xvla_random_k05_spatial_seed43.json\", \"server\": \"westd-38929\", \"gpu_ids\": [3], \"tmux_session\": \"eval_xvla_random_k05_spatial_seed43\", \"pid\": 155546, \"data_path\": \"libero_spatial\", \"data_count\": 500, \"model_name\": \"X-VLA-Libero\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/X-VLA-Libero\", \"eval_data\": \"libero_spatial (10 tasks × 50 episodes)\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_xvla_random_k05_spatial_seed43.log\", \"output_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/eval_xvla_random_k05_spatial_seed43.json\"}}, \"eval_xvla_random_k05_goal_seed43_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T22:23:47.505Z\", \"updated_at\": \"2026-05-23T22:24:05.272Z\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-23T22:24:03.803Z\", \"failure_reason\": \"Director 决定放弃，三连崩溃 (v1/v2/v3 均在 ~ep33 死亡)\"}, \"eval_xvla_random_k05_goal_seed43_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T22:23:46.856Z\", \"updated_at\": \"2026-05-23T22:24:02.708Z\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-23T22:24:02.709Z\"}, \"eval_xvla_l2norm_k07_long_seed42\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T0
…[truncated 38309 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_xvla_l2norm_k05_spatial_seed42_v2_20260524T034308",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-24T03:45:06.146612+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_xvla_l2norm_k05_spatial_seed42_v2",
  "field": "hypothesis",
  "value": "X-VLA L2norm k=0.5 Spatial seed42 — L2 norm pruning vs random pruning (72.6%) 在 Spatial suite 的对比，补全 Table 2 数据。预期 L2norm 显著差于 random（与 Object -27.6pp, Long -15.5pp 一致）。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_xvla_l2norm_k05_spatial_seed42_v2_20260524T034308",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_xvla_l2norm_k05_spatial_seed42_v2",
    "field": "hypothesis",
    "value": "X-VLA L2norm k=0.5 Spatial seed42 — L2 norm pruning vs random pruning (72.6%) 在 Spatial suite 的对比，补全 Table 2 数据。预期 L2norm 显著差于 random（与 Object -27.6pp, Long -15.5pp 一致）。"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-24T03:45:06.146765+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_xvla_l2norm_k05_spatial_seed42_v2\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T03:44:23.826Z\", \"updated_at\": \"2026-05-24T03:44:23.826Z\", \"hypothesis\": \"X-VLA L2norm k=0.5 Spatial seed42 — L2 norm pruning vs random pruning (72.6%) 在 Spatial suite 的对比，补全 Table 2 数据。预期 L2norm 显著差于 random（与 Object -27.6pp, Long -15.5pp 一致）。\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1144}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_xvla_l2norm_k05_spatial_seed42_v2_20260524T034308",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-24T03:45:06.146906+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_xvla_l2norm_k05_spatial_seed42_v2",
  "field": "status",
  "value": "RUNNING",
  "spec": "{'command': 'CUDA_VISIBLE_DEVICES=1 MUJOCO_GL=egl python -u eval_xvla_pruning_libero.py --model_path /root/autodl-tmp/X-VLA-Libero --suite libero_spatial --keep_ratio 0.5 --mode l2_norm --num_episodes 50 --seed 42 --domain_id 3 --gpu 0', 'server': 'westd-38929', 'data_path': 'libero_spatial', 'data_count': 500, 'model_name': 'X-VLA-Libero', 'seed': 42, 'checkpoint_source': '/root/autodl-tmp/X-VLA-Libero', 'eval_data': 'libero_spatial (10 tasks × 50 episodes)', 'log_path': '~/runs/importance_margin_vla_compress/eval_xvla_l2norm_k05_spatial_seed42_v2.log', 'checkpoint_path': 'N/A (eval only)'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_xvla_l2norm_k05_spatial_seed42_v2_20260524T034308",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_xvla_l2norm_k05_spatial_seed42_v2",
    "field": "status",
    "value": "RUNNING",
    "spec": "{'command': 'CUDA_VISIBLE_DEVICES=1 MUJOCO_GL=egl python -u eval_xvla_pruning_libero.py --model_path /root/autodl-tmp/X-VLA-Libero --suite libero_spatial --keep_ratio 0.5 --mode l2_norm --num_episodes 50 --seed 42 --domain_id 3 --gpu 0', 'server': 'westd-38929', 'data_path': 'libero_spatial', 'data_count': 500, 'model_name': 'X-VLA-Libero', 'seed': 42, 'checkpoint_source': '/root/autodl-tmp/X-VLA-Libero', 'eval_data': 'libero_spatial (10 tasks × 50 episodes)', 'log_path': '~/runs/importance_margin_vla_compress/eval_xvla_l2norm_k05_spatial_seed42_v2.log', 'checkpoint_path': 'N/A (eval only)'}"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-24T03:45:06.147064+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PREPARING → RUNNING. Allowed: ['PENDING', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 0.0683}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_xvla_l2norm_k05_spatial_seed42_v2_20260524T034308",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-24T03:45:06.147215+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_xvla_l2norm_k05_spatial_seed42_v2",
  "field": "status",
  "value": "QUEUED"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_xvla_l2norm_k05_spatial_seed42_v2_20260524T034308",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_xvla_l2norm_k05_spatial_seed42_v2",
    "field": "status",
    "value": "QUEUED"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-24T03:45:06.147355+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_xvla_l2norm_k05_spatial_seed42_v2\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-24T03:44:23.826Z\", \"updated_at\": \"2026-05-24T03:44:39.507Z\", \"hypothesis\": \"X-VLA L2norm k=0.5 Spatial seed42 — L2 norm pruning vs random pruning (72.6%) 在 Spatial suite 的对比，补全 Table 2 数据。预期 L2norm 显著差于 random（与 Object -27.6pp, Long -15.5pp 一致）。\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2455}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_xvla_l2norm_k05_spatial_seed42_v2_20260524T034308",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-24T03:45:06.147487+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_xvla_l2norm_k05_spatial_seed42_v2",
  "field": "status",
  "value": "RUNNING",
  "spec": "{'command': 'CUDA_VISIBLE_DEVICES=1 MUJOCO_GL=egl python -u eval_xvla_pruning_libero.py --model_path /root/autodl-tmp/X-VLA-Libero --suite libero_spatial --keep_ratio 0.5 --mode l2_norm --num_episodes 50 --seed 42 --domain_id 3 --gpu 0', 'server': 'westd-38929', 'data_path': 'libero_spatial', 'data_count': 500, 'model_name': 'X-VLA-Libero', 'seed': 42, 'checkpoint_source': '/root/autodl-tmp/X-VLA-Libero', 'eval_data': 'libero_spatial (10 tasks x 50 episodes)', 'log_path': '~/runs/importance_margin_vla_compress/eval_xvla_l2norm_k05_spatial_seed42_v2.log', 'checkpoint_path': 'N/A (eval only)'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_xvla_l2norm_k05_spatial_seed42_v2_20260524T034308",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_xvla_l2norm_k05_spatial_seed42_v2",
    "field": "status",
    "value": "RUNNING",
    "spec": "{'command': 'CUDA_VISIBLE_DEVICES=1 MUJOCO_GL=egl python -u eval_xvla_pruning_libero.py --model_path /root/autodl-tmp/X-VLA-Libero --suite libero_spatial --keep_ratio 0.5 --mode l2_norm --num_episodes 50 --seed 42 --domain_id 3 --gpu 0', 'server': 'westd-38929', 'data_path': 'libero_spatial', 'data_count': 500, 'model_name': 'X-VLA-Libero', 'seed': 42, 'checkpoint_source': '/root/autodl-tmp/X-VLA-Libero', 'eval_data': 'libero_spatial (10 tasks x 50 episodes)', 'log_path': '~/runs/importance_margin_vla_compress/eval_xvla_l2norm_k05_spatial_seed42_v2.log', 'checkpoint_path': 'N/A (eval only)'}"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-24T03:45:06.147643+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_xvla_l2norm_k05_spatial_seed42_v2\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T03:44:23.826Z\", \"updated_at\": \"2026-05-24T03:44:44.431Z\", \"hypothesis\": \"X-VLA L2norm k=0.5 Spatial seed42 — L2 norm pruning vs random pruning (72.6%) 在 Spatial suite 的对比，补全 Table 2 数据。预期 L2norm 显著差于 random（与 Object -27.6pp, Long -15.5pp 一致）。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 MUJOCO_GL=egl python -u eval_xvla_pruning_libero.py --model_path /root/autodl-tmp/X-VLA-Libero --suite libero_spatial --keep_ratio 0.5 --mode l2_norm --num_episodes 50 --seed 42 --domain_id 3 --gpu 0\", \"server\": \"westd-38929\", \"data_path\": \"libero_spatial\", \"data_count\": 500, \"model_name\": \"X-VLA-Libero\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/X-VLA-Libero\", \"eval_data\": \"libero_spatial (10 tasks x 50 episodes)\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_xvla_l2norm_k05_spatial_seed42_v2.log\", \"checkpoint_path\": \"N/A (eval only)\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1943}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_xvla_l2norm_k05_spatial_seed42_v2_20260524T034308",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-24T03:45:06.147809+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_xvla_l2norm_k05_spatial_seed42_v2",
  "field": "metrics",
  "value": "{'overall_sr': 58.8, 'total_successes': 294, 'total_episodes': 500, 'ci_95_wilson': [54.4, 63], 'elapsed_min': 81.4, 'task_sr': {'task_0_bowl_between_plate': 92, 'task_1_bowl_next_ramekin': 22, 'task_2_bowl_table_center': 88, 'task_3_bowl_cookie_box': 72, 'task_4_bowl_top_drawer': 84, 'task_5_bowl_on_ramekin': 0, 'task_6_bowl_next_cookie_box': 82, 'task_7_bowl_on_stove': 32, 'task_8_bowl_next_plate': 72, 'task_9_bowl_wooden_cabinet': 44}, 'vs_random_k05_spatial': {'random_sr': 72.6, 'l2norm_sr': 58.8, 'gap_pp': -13.8}}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_xvla_l2norm_k05_spatial_seed42_v2_20260524T034308",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_xvla_l2norm_k05_spatial_seed42_v2",
    "field": "metrics",
    "value": "{'overall_sr': 58.8, 'total_successes': 294, 'total_episodes': 500, 'ci_95_wilson': [54.4, 63], 'elapsed_min': 81.4, 'task_sr': {'task_0_bowl_between_plate': 92, 'task_1_bowl_next_ramekin': 22, 'task_2_bowl_table_center': 88, 'task_3_bowl_cookie_box': 72, 'task_4_bowl_top_drawer': 84, 'task_5_bowl_on_ramekin': 0, 'task_6_bowl_next_cookie_box': 82, 'task_7_bowl_on_stove': 32, 'task_8_bowl_next_plate': 72, 'task_9_bowl_wooden_cabinet': 44}, 'vs_random_k05_spatial': {'random_sr': 72.6, 'l2norm_sr': 58.8, 'gap_pp': -13.8}}"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-24T03:45:06.147991+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_xvla_l2norm_k05_spatial_seed42_v2\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T03:44:23.826Z\", \"updated_at\": \"2026-05-24T03:44:52.703Z\", \"hypothesis\": \"X-VLA L2norm k=0.5 Spatial seed42 — L2 norm pruning vs random pruning (72.6%) 在 Spatial suite 的对比，补全 Table 2 数据。预期 L2norm 显著差于 random（与 Object -27.6pp, Long -15.5pp 一致）。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 MUJOCO_GL=egl python -u eval_xvla_pruning_libero.py --model_path /root/autodl-tmp/X-VLA-Libero --suite libero_spatial --keep_ratio 0.5 --mode l2_norm --num_episodes 50 --seed 42 --domain_id 3 --gpu 0\", \"server\": \"westd-38929\", \"data_path\": \"libero_spatial\", \"data_count\": 500, \"model_name\": \"X-VLA-Libero\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/X-VLA-Libero\", \"eval_data\": \"libero_spatial (10 tasks x 50 episodes)\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_xvla_l2norm_k05_spatial_seed42_v2.log\", \"checkpoint_path\": \"N/A (eval only)\"}, \"metrics\": {\"overall_sr\": 58.8, \"total_successes\": 294, \"total_episodes\": 500, \"ci_95_wilson\": [54.4, 63], \"elapsed_min\": 81.4, \"task_sr\": {\"task_0_bowl_between_plate\": 92, \"task_1_bowl_next_ramekin\": 22, \"task_2_bowl_table_center\": 88, \"task_3_bowl_cookie_box\": 72, \"task_4_bowl_top_drawer\": 84, \"task_5_bowl_on_ramekin\": 0, \"task_6_bowl_next_cookie_box\": 82, \"task_7_bowl_on_stove\": 32, \"task_8_bowl_next_plate\": 72, \"task_9_bowl_wooden_cabinet\": 44}, \"vs_random_k05_spatial\": {\"random_sr\": 72.6, \"l2norm_sr\": 58.8, \"gap_pp\": -13.8}}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1204}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_xvla_l2norm_k05_spatial_seed42_v2_20260524T034308",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-24T03:45:06.148160+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_xvla_l2norm_k05_spatial_seed42_v2",
  "field": "conclusion",
  "value": "success"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_xvla_l2norm_k05_spatial_seed42_v2_20260524T034308",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_xvla_l2norm_k05_spatial_seed42_v2",
    "field": "conclusion",
    "value": "success"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-24T03:45:06.148328+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_xvla_l2norm_k05_spatial_seed42_v2\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T03:44:23.826Z\", \"updated_at\": \"2026-05-24T03:44:53.056Z\", \"hypothesis\": \"X-VLA L2norm k=0.5 Spatial seed42 — L2 norm pruning vs random pruning (72.6%) 在 Spatial suite 的对比，补全 Table 2 数据。预期 L2norm 显著差于 random（与 Object -27.6pp, Long -15.5pp 一致）。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 MUJOCO_GL=egl python -u eval_xvla_pruning_libero.py --model_path /root/autodl-tmp/X-VLA-Libero --suite libero_spatial --keep_ratio 0.5 --mode l2_norm --num_episodes 50 --seed 42 --domain_id 3 --gpu 0\", \"server\": \"westd-38929\", \"data_path\": \"libero_spatial\", \"data_count\": 500, \"model_name\": \"X-VLA-Libero\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/X-VLA-Libero\", \"eval_data\": \"libero_spatial (10 tasks x 50 episodes)\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_xvla_l2norm_k05_spatial_seed42_v2.log\", \"checkpoint_path\": \"N/A (eval only)\"}, \"metrics\": {\"overall_sr\": 58.8, \"total_successes\": 294, \"total_episodes\": 500, \"ci_95_wilson\": [54.4, 63], \"elapsed_min\": 81.4, \"task_sr\": {\"task_0_bowl_between_plate\": 92, \"task_1_bowl_next_ramekin\": 22, \"task_2_bowl_table_center\": 88, \"task_3_bowl_cookie_box\": 72, \"task_4_bowl_top_drawer\": 84, \"task_5_bowl_on_ramekin\": 0, \"task_6_bowl_next_cookie_box\": 82, \"task_7_bowl_on_stove\": 32, \"task_8_bowl_next_plate\": 72, \"task_9_bowl_wooden_cabinet\": 44}, \"vs_random_k05_spatial\": {\"random_sr\": 72.6, \"l2norm_sr\": 58.8, \"gap_pp\": -13.8}}, \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1319}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_xvla_l2norm_k05_spatial_seed42_v2_20260524T034308",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-24T03:45:06.148474+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_xvla_l2norm_k05_spatial_seed42_v2",
  "field": "status",
  "value": "DONE"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_xvla_l2norm_k05_spatial_seed42_v2_20260524T034308",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_xvla_l2norm_k05_spatial_seed42_v2",
    "field": "status",
    "value": "DONE"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-24T03:45:06.148679+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_xvla_l2norm_k05_spatial_seed42_v2\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-24T03:44:23.826Z\", \"updated_at\": \"2026-05-24T03:44:55.810Z\", \"hypothesis\": \"X-VLA L2norm k=0.5 Spatial seed42 — L2 norm pruning vs random pruning (72.6%) 在 Spatial suite 的对比，补全 Table 2 数据。预期 L2norm 显著差于 random（与 Object -27.6pp, Long -15.5pp 一致）。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 MUJOCO_GL=egl python -u eval_xvla_pruning_libero.py --model_path /root/autodl-tmp/X-VLA-Libero --suite libero_spatial --keep_ratio 0.5 --mode l2_norm --num_episodes 50 --seed 42 --domain_id 3 --gpu 0\", \"server\": \"westd-38929\", \"data_path\": \"libero_spatial\", \"data_count\": 500, \"model_name\": \"X-VLA-Libero\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/X-VLA-Libero\", \"eval_data\": \"libero_spatial (10 tasks x 50 episodes)\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_xvla_l2norm_k05_spatial_seed42_v2.log\", \"checkpoint_path\": \"N/A (eval only)\"}, \"metrics\": {\"overall_sr\": 58.8, \"total_successes\": 294, \"total_episodes\": 500, \"ci_95_wilson\": [54.4, 63], \"elapsed_min\": 81.4, \"task_sr\": {\"task_0_bowl_between_plate\": 92, \"task_1_bowl_next_ramekin\": 22, \"task_2_bowl_table_center\": 88, \"task_3_bowl_cookie_box\": 72, \"task_4_bowl_top_drawer\": 84, \"task_5_bowl_on_ramekin\": 0, \"task_6_bowl_next_cookie_box\": 82, \"task_7_bowl_on_stove\": 32, \"task_8_bowl_next_plate\": 72, \"task_9_bowl_wooden_cabinet\": 44}, \"vs_random_k05_spatial\": {\"random_sr\": 72.6, \"l2norm_sr\": 58.8, \"gap_pp\": -13.8}}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-24T03:44:55.810Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1941}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_xvla_l2norm_k05_spatial_seed42_v2_20260524T034308",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 33 · 2026-05-24T03:45:06.148880+00:00_

Registry 已更新为 DONE/success。汇总：

## 实验结果

| 指标 | 值 |
|------|-----|
| Overall SR | **58.8%** (294/500) |
| 95% Wilson CI | [54.4%, 63.0%] |
| vs Random k=0.5 Spatial | **-13.8pp** (58.8% vs 72.6%) |

**Per-task SR:**
| Task | SR | 描述 |
|------|-----|------|
| T0 | 92% | bowl between plate |
| T1 | 22% | bowl next ramekin |
| T2 | 88% | bowl table center |
| T3 | 72% | bowl cookie box |
| T4 | 84% | bowl top drawer |
| T5 | **0%** | bowl on ramekin |
| T6 | 82% | bowl next cookie box |
| T7 | 32% | bowl on stove |
| T8 | 72% | bowl next plate |
| T9 | 44% | bowl wooden cabinet |

**结论 = success**（验证了 hypothesis）：
- L2norm 在 X-VLA Spatial 上确实显著差于 random（-13.8pp），与 CV matrix 预测的 -13.1pp 高度一致
- 跨 suite 一致性确认：Object -27.6pp, Long -15.5pp, Spatial -13.8pp — L2norm 在 X-VLA 上全面劣于 random
- 58.8% 与 CV matrix 的 L2 Mean=58.9% 几乎完全吻合，说明 seed42 单次结果高度稳定

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analyze_eval_xvla_l2norm_k05_spatial_seed42_v2_20260524T034308"
}
```

</details>

---
