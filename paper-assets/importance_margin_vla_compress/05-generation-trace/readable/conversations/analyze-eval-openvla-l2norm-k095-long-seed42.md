# analyze eval openvla l2norm k095 long seed42

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 0
- **Tool calls:** 6
- **Original source:** `logs/chats/worker_analyze_eval_openvla_l2norm_k095_long_seed42_20260527T120425.jsonl`
- **Structured JSON:** [`7bec48db2a6e470edc16.json`](../../sessions/7b/7bec48db2a6e470edc16.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

13 recorded events

### Tool call

_source line 1 · 2026-05-27T12:05:36.483648+00:00_

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
  "session": "worker_analyze_eval_openvla_l2norm_k095_long_seed42_20260527T120425",
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

_source line 2 · 2026-05-27T12:05:36.484124+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_openvla_l2norm_k095_long_seed42_20260527T120425",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-27T12:05:36.484383+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-38929",
  "command": "tail -200 ~/runs/importance_margin_vla_compress/eval_openvla_l2norm_k095_long_seed42.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_openvla_l2norm_k095_long_seed42_20260527T120425",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-38929",
    "command": "tail -200 ~/runs/importance_margin_vla_compress/eval_openvla_l2norm_k095_long_seed42.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-27T12:05:36.484728+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"WARNING: All log messages before absl::InitializeLog() is called are written to STDERR\\nI0000 00:00:1779844322.933218  949447 port.cc:153] oneDNN custom operations are on. You may see slightly different numerical results due to floating-point round-off errors from different computation orders. To turn them off, set the environment variable `TF_ENABLE_ONEDNN_OPTS=0`.\\nI0000 00:00:1779844322.967385  949447 cpu_feature_guard.cc:227] This TensorFlow binary is optimized to use available CPU instructions in performance-critical operations.\\nTo enable the following instructions: AVX2 AVX512F AVX512_VNNI AVX512_BF16 AVX512_FP16 AVX_VNNI AMX_TILE AMX_INT8 AMX_BF16 FMA, in other operations, rebuild TensorFlow with the appropriate compiler flags.\\nWARNING: All log messages before absl::InitializeLog() is called are written to STDERR\\nI0000 00:00:1779844323.945951  949447 port.cc:153] oneDNN custom operations are on. You may see slightly different numerical results due to floating-point round-off errors from different computation orders. To turn them off, set the environment variable `TF_ENABLE_ONEDNN_OPTS=0`.\\n[*] Loading OpenVLA from: /root/autodl-tmp/models/openvla-7b-finetuned-libero-10\\n\\rLoading checkpoint shards:   0%|          | 0/4 [00:00<?, ?it/s]\\rLoading checkpoint shards:  25%|██▌       | 1/4 [00:00<00:00,  4.00it/s]\\rLoading checkpoint shards:  50%|█████     | 2/4 [00:00<00:00,  4.82it/s]\\rLoading checkpoint shards:  75%|███████▌  | 3/4 [00:00<00:00,  5.33it/s]\\rLoading checkpoint shards: 100%|██████████| 4/4 [00:00<00:00,  5.85it/s]\\rLoading checkpoint shards: 100%|██████████| 4/4 [00:00<00:00,  5.42it/s]\\n[*] Model loaded, GPU: 15.1 GB\\n[*] Vision tokens: 256, dim: 4096\\n[*] L2 norm pruning: k=0.95\\n[robosuite WARNING] No private macro file found! (macros.py:53)\\n[robosuite WARNING] It is recommended to use a private macro file (macros.py:54)\\n[robosuite WARNING] To setup, run: python /ro
…[truncated 4161 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_openvla_l2norm_k095_long_seed42_20260527T120425",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-27T12:05:36.485062+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_openvla_l2norm_k095_long_seed42",
  "field": "metrics",
  "value": "{'overall_sr': 42.6, 'total': '213/500', 'per_task_sr': [64, 60, 54, 34, 38, 70, 26, 50, 14, 16], 'per_task_raw': ['32/50', '30/50', '27/50', '17/50', '19/50', '35/50', '13/50', '7/50', '8/50'], 'time_min': 648.8, 'vision_tokens': '256->243'}",
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_openvla_l2norm_k095_long_seed42_20260527T120425",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_openvla_l2norm_k095_long_seed42",
    "field": "metrics",
    "value": "{'overall_sr': 42.6, 'total': '213/500', 'per_task_sr': [64, 60, 54, 34, 38, 70, 26, 50, 14, 16], 'per_task_raw': ['32/50', '30/50', '27/50', '17/50', '19/50', '35/50', '13/50', '7/50', '8/50'], 'time_min': 648.8, 'vision_tokens': '256->243'}",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-27T12:05:36.487491+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_openvla_l2norm_k095_long_seed42\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-27T01:11:10.791Z\", \"updated_at\": \"2026-05-27T12:04:57.393Z\", \"hypothesis\": \"OpenVLA L2norm k=0.95 Long seed42 — Long L2norm curve 顶端缺口。L2norm k=0.9=43.6%, k=0.85=38.8%。k=0.95 补全曲线起始段\", \"spec\": {\"command\": \"python -u eval_openvla_l2norm_libero.py --mode l2norm_prune --k_ratio 0.95 --suite libero_10\", \"server\": \"westd-38929\", \"gpu\": [\"cuda:1\"], \"pid\": \"949438\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_openvla_l2norm_k095_long_seed42.log\", \"submitted_at\": \"2026-05-27T01:12:00.178Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"openvla-7b-finetuned-libero-10\", \"seed\": 42, \"data_path\": \"libero_10\", \"data_count\": 500}, \"reproduce\": {\"finished_at\": \"2026-05-27T12:01:40.023Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-27T12:02:08.177483+00:00\"}]}, \"metrics\": {\"overall_sr\": 42.6, \"total\": \"213/500\", \"per_task_sr\": [64, 60, 54, 34, 38, 70, 26, 50, 14, 16], \"per_task_raw\": [\"32/50\", \"30/50\", \"27/50\", \"17/50\", \"19/50\", \"35/50\", \"13/50\", \"7/50\", \"8/50\"], \"time_min\": 648.8, \"vision_tokens\": \"256->243\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 6.9471}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_openvla_l2norm_k095_long_seed42_20260527T120425",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-27T12:05:36.487768+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_openvla_l2norm_k095_long_seed42",
  "field": "log_path",
  "value": "~/runs/importance_margin_vla_compress/eval_openvla_l2norm_k095_long_seed42.log",
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_openvla_l2norm_k095_long_seed42_20260527T120425",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_openvla_l2norm_k095_long_seed42",
    "field": "log_path",
    "value": "~/runs/importance_margin_vla_compress/eval_openvla_l2norm_k095_long_seed42.log",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-27T12:05:36.487983+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_openvla_l2norm_k095_long_seed42",
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
  "session": "worker_analyze_eval_openvla_l2norm_k095_long_seed42_20260527T120425",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_openvla_l2norm_k095_long_seed42",
    "field": "checkpoint_path",
    "value": "N/A (eval only)",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-27T12:05:36.490249+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_openvla_l2norm_k095_long_seed42\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-27T01:11:10.791Z\", \"updated_at\": \"2026-05-27T12:05:09.473Z\", \"hypothesis\": \"OpenVLA L2norm k=0.95 Long seed42 — Long L2norm curve 顶端缺口。L2norm k=0.9=43.6%, k=0.85=38.8%。k=0.95 补全曲线起始段\", \"spec\": {\"command\": \"python -u eval_openvla_l2norm_libero.py --mode l2norm_prune --k_ratio 0.95 --suite libero_10\", \"server\": \"westd-38929\", \"gpu\": [\"cuda:1\"], \"pid\": \"949438\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_openvla_l2norm_k095_long_seed42.log\", \"submitted_at\": \"2026-05-27T01:12:00.178Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"openvla-7b-finetuned-libero-10\", \"seed\": 42, \"data_path\": \"libero_10\", \"data_count\": 500}, \"reproduce\": {\"finished_at\": \"2026-05-27T12:01:40.023Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-27T12:02:08.177483+00:00\"}]}, \"metrics\": {\"overall_sr\": 42.6, \"total\": \"213/500\", \"per_task_sr\": [64, 60, 54, 34, 38, 70, 26, 50, 14, 16], \"per_task_raw\": [\"32/50\", \"30/50\", \"27/50\", \"17/50\", \"19/50\", \"35/50\", \"13/50\", \"7/50\", \"8/50\"], \"time_min\": 648.8, \"vision_tokens\": \"256->243\"}, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_openvla_l2norm_k095_long_seed42.log\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 7.3954}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_openvla_l2norm_k095_long_seed42_20260527T120425",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-27T12:05:36.490636+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_openvla_l2norm_k095_long_seed42\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-27T01:11:10.791Z\", \"updated_at\": \"2026-05-27T12:05:17.510Z\", \"hypothesis\": \"OpenVLA L2norm k=0.95 Long seed42 — Long L2norm curve 顶端缺口。L2norm k=0.9=43.6%, k=0.85=38.8%。k=0.95 补全曲线起始段\", \"spec\": {\"command\": \"python -u eval_openvla_l2norm_libero.py --mode l2norm_prune --k_ratio 0.95 --suite libero_10\", \"server\": \"westd-38929\", \"gpu\": [\"cuda:1\"], \"pid\": \"949438\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_openvla_l2norm_k095_long_seed42.log\", \"submitted_at\": \"2026-05-27T01:12:00.178Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"openvla-7b-finetuned-libero-10\", \"seed\": 42, \"data_path\": \"libero_10\", \"data_count\": 500}, \"reproduce\": {\"finished_at\": \"2026-05-27T12:01:40.023Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-27T12:02:08.177483+00:00\"}]}, \"metrics\": {\"overall_sr\": 42.6, \"total\": \"213/500\", \"per_task_sr\": [64, 60, 54, 34, 38, 70, 26, 50, 14, 16], \"per_task_raw\": [\"32/50\", \"30/50\", \"27/50\", \"17/50\", \"19/50\", \"35/50\", \"13/50\", \"7/50\", \"8/50\"], \"time_min\": 648.8, \"vision_tokens\": \"256->243\"}, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_openvla_l2norm_k095_long_seed42.log\", \"checkpoint_path\": \"N/A (eval only)\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 7.9925}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_openvla_l2norm_k095_long_seed42_20260527T120425",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-27T12:05:36.490887+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_openvla_l2norm_k095_long_seed42",
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
  "session": "worker_analyze_eval_openvla_l2norm_k095_long_seed42_20260527T120425",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_openvla_l2norm_k095_long_seed42",
    "field": "conclusion",
    "value": "success",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-27T12:05:36.494548+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_openvla_l2norm_k095_long_seed42\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-27T01:11:10.791Z\", \"updated_at\": \"2026-05-27T12:05:24.413Z\", \"hypothesis\": \"OpenVLA L2norm k=0.95 Long seed42 — Long L2norm curve 顶端缺口。L2norm k=0.9=43.6%, k=0.85=38.8%。k=0.95 补全曲线起始段\", \"spec\": {\"command\": \"python -u eval_openvla_l2norm_libero.py --mode l2norm_prune --k_ratio 0.95 --suite libero_10\", \"server\": \"westd-38929\", \"gpu\": [\"cuda:1\"], \"pid\": \"949438\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_openvla_l2norm_k095_long_seed42.log\", \"submitted_at\": \"2026-05-27T01:12:00.178Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"openvla-7b-finetuned-libero-10\", \"seed\": 42, \"data_path\": \"libero_10\", \"data_count\": 500}, \"reproduce\": {\"finished_at\": \"2026-05-27T12:01:40.023Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-27T12:02:08.177483+00:00\"}]}, \"metrics\": {\"overall_sr\": 42.6, \"total\": \"213/500\", \"per_task_sr\": [64, 60, 54, 34, 38, 70, 26, 50, 14, 16], \"per_task_raw\": [\"32/50\", \"30/50\", \"27/50\", \"17/50\", \"19/50\", \"35/50\", \"13/50\", \"7/50\", \"8/50\"], \"time_min\": 648.8, \"vision_tokens\": \"256->243\"}, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_openvla_l2norm_k095_long_seed42.log\", \"checkpoint_path\": \"N/A (eval only)\", \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.7621}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_openvla_l2norm_k095_long_seed42_20260527T120425",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 3
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-27T12:05:36.494995+00:00_

Registry 已更新。结果总结：

**OpenVLA L2norm k=0.95 Long: Overall SR = 42.6% (213/500)**

| Task | SR |
|---|---|
| 1. alphabet soup + tomato sauce → basket | 64% |
| 2. cream cheese + butter → basket | 60% |
| 3. stove + moka pot | 54% |
| 4. black bowl → drawer | 34% |
| 5. mugs → plates | 38% |
| 6. book → caddy | 70% |
| 7. mug + pudding → plate | 26% |
| 8. alphabet soup + cream cheese → basket | 50% |
| 9. both moka pots → stove | 14% |
| 10. mug → microwave | 16% |

**对比：**
- Baseline (no pruning): **52.8%** → L2norm k=0.95 下降 10.2pp
- Attn k=0.95: **49.8%** → L2norm 比 Attn 低 7.2pp
- L2norm k=0.9: **43.6%** → k=0.95 反而略低 1pp（42.6% vs 43.6%），差异在噪声范围内

L2norm 在 Long suite 上整体弱于 Attn pruning，即使只剪 5% tokens (k=0.95) 也比 baseline 掉了 10pp。L2norm curve 起始段补全完成：k=0.95→42.6%, k=0.9→43.6%, k=0.85→38.8%。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analyze_eval_openvla_l2norm_k095_long_seed42_20260527T120425"
}
```

</details>

---
