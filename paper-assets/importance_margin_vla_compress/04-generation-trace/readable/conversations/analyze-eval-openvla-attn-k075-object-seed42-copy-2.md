# analyze eval openvla attn k075 object seed42

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 0
- **Tool calls:** 5
- **Original source:** `logs/chats/worker_analyze_eval_openvla_attn_k075_object_seed42_20260526T231335.jsonl`
- **Structured JSON:** [`16119faa58386822e950.json`](../../sessions/16/16119faa58386822e950.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

11 recorded events

### Tool call

_source line 1 · 2026-05-26T23:14:39.948465+00:00_

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
  "session": "worker_analyze_eval_openvla_attn_k075_object_seed42_20260526T231335",
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

_source line 2 · 2026-05-26T23:14:39.948979+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_openvla_attn_k075_object_seed42_20260526T231335",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-26T23:14:39.949265+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-41074",
  "command": "tail -100 ~/runs/importance_margin_vla_compress/eval_openvla_attn_k075_object_seed42.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_openvla_attn_k075_object_seed42_20260526T231335",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-41074",
    "command": "tail -100 ~/runs/importance_margin_vla_compress/eval_openvla_attn_k075_object_seed42.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-26T23:14:39.949582+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[*] Loading OpenVLA from: /root/autodl-tmp/openvla-libero-object\\n\\rLoading checkpoint shards:   0%|          | 0/4 [00:00<?, ?it/s]\\rLoading checkpoint shards:  25%|██▌       | 1/4 [00:00<00:00,  5.16it/s]\\rLoading checkpoint shards:  75%|███████▌  | 3/4 [00:00<00:00,  8.29it/s]\\rLoading checkpoint shards: 100%|██████████| 4/4 [00:00<00:00,  8.43it/s]\\rLoading checkpoint shards: 100%|██████████| 4/4 [00:00<00:00,  8.02it/s]\\n[*] Model loaded, GPU: 15.1 GB\\n[*] Vision tokens: 256, dim: 4096\\n[*] Attention pruning: k=0.75\\n[robosuite WARNING] No private macro file found! (__init__.py:7)\\n[robosuite WARNING] It is recommended to use a private macro file (__init__.py:8)\\n[robosuite WARNING] To setup, run: python /root/miniconda3/lib/python3.12/site-packages/robosuite/scripts/setup_macros.py (__init__.py:9)\\n[info] using task orders [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\\n[*] libero_object: 10 tasks x 50 episodes = 500 total\\n\\n[Task 1/10] pick up the alphabet soup and place it in the basket\\n[Attn Pruning] 256 -> 192 vision tokens (k=0.75), importance range=[0.7166, 1.7250]\\n  Ep 10/50 task_sr=5/10 (0.7 eps/min)\\n  Ep 20/50 task_sr=11/20 (1.0 eps/min)\\n  Ep 30/50 task_sr=17/30 (1.2 eps/min)\\n  Ep 40/50 task_sr=24/40 (1.3 eps/min)\\n  Ep 50/50 task_sr=28/50 (1.4 eps/min)\\n  => Task SR: 0.560 (28/50)\\n\\n[Task 2/10] pick up the cream cheese and place it in the basket\\n  Ep 10/50 task_sr=1/10 (1.4 eps/min)\\n  Ep 20/50 task_sr=2/20 (1.4 eps/min)\\n  Ep 30/50 task_sr=4/30 (1.5 eps/min)\\n  Ep 40/50 task_sr=9/40 (1.5 eps/min)\\n  Ep 50/50 task_sr=14/50 (1.5 eps/min)\\n  => Task SR: 0.280 (14/50)\\n\\n[Task 3/10] pick up the salad dressing and place it in the basket\\n  Ep 10/50 task_sr=7/10 (1.6 eps/min)\\n  Ep 20/50 task_sr=15/20 (1.6 eps/min)\\n  Ep 30/50 task_sr=21/30 (1.7 eps/min)\\n  Ep 40/50 task_sr=26/40 (1.7 eps/min)\\n  Ep 50/50 task_sr=35/50 (1.7 eps/min)\\n  => Task SR: 0.700 (35/50)\\n\\n[Ta
…[truncated 2596 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_openvla_attn_k075_object_seed42_20260526T231335",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-26T23:14:39.949903+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_openvla_attn_k075_object_seed42",
  "field": "metrics",
  "value": "{'overall_sr': 53.2, 'total_success': 266, 'total_episodes': 500, 'per_task_sr': {'alphabet_soup': 56, 'cream_cheese': 28, 'salad_dressing': 70, 'bbq_sauce': 34, 'ketchup': 76, 'tomato_sauce': 30, 'butter': 28, 'milk': 54, 'chocolate_pudding': 86, 'orange_juice': 70}, 'eval_time_min': 272}",
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_openvla_attn_k075_object_seed42_20260526T231335",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_openvla_attn_k075_object_seed42",
    "field": "metrics",
    "value": "{'overall_sr': 53.2, 'total_success': 266, 'total_episodes': 500, 'per_task_sr': {'alphabet_soup': 56, 'cream_cheese': 28, 'salad_dressing': 70, 'bbq_sauce': 34, 'ketchup': 76, 'tomato_sauce': 30, 'butter': 28, 'milk': 54, 'chocolate_pudding': 86, 'orange_juice': 70}, 'eval_time_min': 272}",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-26T23:14:39.953285+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_openvla_attn_k075_object_seed42\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-26T16:38:05.844Z\", \"updated_at\": \"2026-05-26T23:14:09.271Z\", \"hypothesis\": \"OpenVLA Attention k=0.75 Object seed42 — Object Attn cliff curve 中间点。Attn k=0.9=61.4%, k=0.85=55.0%, k=0.7=43.8%。k=0.75 精确定位 Attention pruning 在 Object suite 上的 cliff 位置，区分平缓退化还是断崖式下降\", \"server\": \"westd-41074\", \"gpu_ids\": [\"cuda:2\"], \"gpu\": \"cuda:2\", \"spec\": {\"command\": \"MUJOCO_GL=egl python -u /root/autodl-tmp/importance_margin_vla_compress/eval_openvla_l2norm_libero.py --mode attention_prune --k_ratio 0.75 --suite libero_object --num_episodes 50 --seed 42 --model_path /root/autodl-tmp/openvla-libero-object --unnorm_key libero_object\", \"server\": \"westd-41074\", \"gpu\": \"cuda:2\", \"pid\": 755977, \"data_path\": \"libero_object\", \"data_count\": 50, \"model_name\": \"openvla-libero-object\", \"seed\": 42, \"checkpoint_path\": \"N/A (eval only)\", \"checkpoint_source\": \"/root/autodl-tmp/openvla-libero-object\", \"eval_data\": \"libero_object\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_openvla_attn_k075_object_seed42.log\"}, \"pid\": \"755977\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_openvla_attn_k075_object_seed42.log\", \"reproduce\": {\"command\": \"MUJOCO_GL=egl python -u /root/autodl-tmp/importance_margin_vla_compress/eval_openvla_l2norm_libero.py --mode attention_prune --k_ratio 0.75 --suite libero_object --num_episodes 50 --seed 42 --model_path /root/autodl-tmp/openvla-libero-object --unnorm_key libero_object\", \"finished_at\": \"2026-05-26T21:14:05.906Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-26T21:14:20.875797+00:00\"}]}, \"metrics\": {\"overall_sr\": 53.2, \"total_success\": 266, \"total_episodes\": 500, \"per_task_sr\": {\"alphabet_soup\": 56, \"cream_cheese\": 28,
…[truncated 253 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_openvla_attn_k075_object_seed42_20260526T231335",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 3
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-26T23:14:39.953662+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_openvla_attn_k075_object_seed42",
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
  "session": "worker_analyze_eval_openvla_attn_k075_object_seed42_20260526T231335",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_openvla_attn_k075_object_seed42",
    "field": "conclusion",
    "value": "success",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-26T23:14:39.953899+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_openvla_attn_k075_object_seed42",
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
  "session": "worker_analyze_eval_openvla_attn_k075_object_seed42_20260526T231335",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_openvla_attn_k075_object_seed42",
    "field": "status",
    "value": "DONE",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-26T23:14:39.954199+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_openvla_attn_k075_object_seed42\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-26T16:38:05.844Z\", \"updated_at\": \"2026-05-26T23:14:20.552Z\", \"hypothesis\": \"OpenVLA Attention k=0.75 Object seed42 — Object Attn cliff curve 中间点。Attn k=0.9=61.4%, k=0.85=55.0%, k=0.7=43.8%。k=0.75 精确定位 Attention pruning 在 Object suite 上的 cliff 位置，区分平缓退化还是断崖式下降\", \"server\": \"westd-41074\", \"gpu_ids\": [\"cuda:2\"], \"gpu\": \"cuda:2\", \"spec\": {\"command\": \"MUJOCO_GL=egl python -u /root/autodl-tmp/importance_margin_vla_compress/eval_openvla_l2norm_libero.py --mode attention_prune --k_ratio 0.75 --suite libero_object --num_episodes 50 --seed 42 --model_path /root/autodl-tmp/openvla-libero-object --unnorm_key libero_object\", \"server\": \"westd-41074\", \"gpu\": \"cuda:2\", \"pid\": 755977, \"data_path\": \"libero_object\", \"data_count\": 50, \"model_name\": \"openvla-libero-object\", \"seed\": 42, \"checkpoint_path\": \"N/A (eval only)\", \"checkpoint_source\": \"/root/autodl-tmp/openvla-libero-object\", \"eval_data\": \"libero_object\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_openvla_attn_k075_object_seed42.log\"}, \"pid\": \"755977\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_openvla_attn_k075_object_seed42.log\", \"reproduce\": {\"command\": \"MUJOCO_GL=egl python -u /root/autodl-tmp/importance_margin_vla_compress/eval_openvla_l2norm_libero.py --mode attention_prune --k_ratio 0.75 --suite libero_object --num_episodes 50 --seed 42 --model_path /root/autodl-tmp/openvla-libero-object --unnorm_key libero_object\", \"finished_at\": \"2026-05-26T21:14:05.906Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-26T21:14:20.875797+00:00\"}]}, \"metrics\": {\"overall_sr\": 53.2, \"total_success\": 266, \"total_episodes\": 500, \"per_task_sr\": {\"alphabet_soup\": 56, \"cream_cheese\": 28,
…[truncated 282 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_openvla_attn_k075_object_seed42_20260526T231335",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-26T23:14:39.954572+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_openvla_attn_k075_object_seed42\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-26T16:38:05.844Z\", \"updated_at\": \"2026-05-26T23:14:24.524Z\", \"hypothesis\": \"OpenVLA Attention k=0.75 Object seed42 — Object Attn cliff curve 中间点。Attn k=0.9=61.4%, k=0.85=55.0%, k=0.7=43.8%。k=0.75 精确定位 Attention pruning 在 Object suite 上的 cliff 位置，区分平缓退化还是断崖式下降\", \"server\": \"westd-41074\", \"gpu_ids\": [\"cuda:2\"], \"gpu\": \"cuda:2\", \"spec\": {\"command\": \"MUJOCO_GL=egl python -u /root/autodl-tmp/importance_margin_vla_compress/eval_openvla_l2norm_libero.py --mode attention_prune --k_ratio 0.75 --suite libero_object --num_episodes 50 --seed 42 --model_path /root/autodl-tmp/openvla-libero-object --unnorm_key libero_object\", \"server\": \"westd-41074\", \"gpu\": \"cuda:2\", \"pid\": 755977, \"data_path\": \"libero_object\", \"data_count\": 50, \"model_name\": \"openvla-libero-object\", \"seed\": 42, \"checkpoint_path\": \"N/A (eval only)\", \"checkpoint_source\": \"/root/autodl-tmp/openvla-libero-object\", \"eval_data\": \"libero_object\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_openvla_attn_k075_object_seed42.log\"}, \"pid\": \"755977\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_openvla_attn_k075_object_seed42.log\", \"reproduce\": {\"command\": \"MUJOCO_GL=egl python -u /root/autodl-tmp/importance_margin_vla_compress/eval_openvla_l2norm_libero.py --mode attention_prune --k_ratio 0.75 --suite libero_object --num_episodes 50 --seed 42 --model_path /root/autodl-tmp/openvla-libero-object --unnorm_key libero_object\", \"finished_at\": \"2026-05-26T21:14:05.906Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-26T21:14:20.875797+00:00\"}]}, \"metrics\": {\"overall_sr\": 53.2, \"total_success\": 266, \"total_episodes\": 500, \"per_task_sr\": {\"alphabet_soup\": 56, \"cream_cheese\": 28, \"sa
…[truncated 376 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_openvla_attn_k075_object_seed42_20260526T231335",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-26T23:14:39.954904+00:00_

Registry 已更新。结果汇总：

**Overall SR: 53.2%** (266/500)

| Task | SR |
|---|---|
| chocolate_pudding | 86.0% |
| ketchup | 76.0% |
| salad_dressing | 70.0% |
| orange_juice | 70.0% |
| alphabet_soup | 56.0% |
| milk | 54.0% |
| bbq_sauce | 34.0% |
| tomato_sauce | 30.0% |
| cream_cheese | 28.0% |
| butter | 28.0% |

**Object Attn cliff curve 更新：**

| k | SR | Δ |
|---|---|---|
| 0.90 | 61.4% | — |
| 0.85 | 55.0% | -6.4pp |
| **0.75** | **53.2%** | **-1.8pp** |
| 0.70 | 43.8% | -9.4pp |
| 0.50 | 40.6% | -3.2pp |

Cliff 定位清晰：k=0.85→0.75 仅下降 1.8pp（平缓区），k=0.75→0.70 骤降 9.4pp（断崖）。**Cliff 位于 k=0.70~0.75 之间**，k=0.75 是安全压缩的下界——保留 75% attention tokens 仍能维持接近 k=0.85 的性能。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analyze_eval_openvla_attn_k075_object_seed42_20260526T231335"
}
```

</details>

---
