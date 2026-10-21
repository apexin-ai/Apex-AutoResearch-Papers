# analyze eval openvla random k05 long seed42 v2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 17
- **Recorded user turns:** 0
- **Tool calls:** 8
- **Original source:** `logs/chats/worker_analyze_eval_openvla_random_k05_long_seed42_v2_20260526T151649.jsonl`
- **Structured JSON:** [`3694e005be9f76204170.json`](../../sessions/36/3694e005be9f76204170.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

17 recorded events

### Tool call

_source line 1 · 2026-05-26T15:18:27.770703+00:00_

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
  "session": "worker_analyze_eval_openvla_random_k05_long_seed42_v2_20260526T151649",
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

_source line 2 · 2026-05-26T15:18:27.771041+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_openvla_random_k05_long_seed42_v2_20260526T151649",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-26T15:18:27.771245+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-38929",
  "command": "tail -200 /root/runs/importance_margin_vla_compress/eval_openvla_random_k05_long_seed42_v2.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_openvla_random_k05_long_seed42_v2_20260526T151649",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-38929",
    "command": "tail -200 /root/runs/importance_margin_vla_compress/eval_openvla_random_k05_long_seed42_v2.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-26T15:18:27.771477+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"WARNING: All log messages before absl::InitializeLog() is called are written to STDERR\\nI0000 00:00:1779771796.365611  279274 port.cc:153] oneDNN custom operations are on. You may see slightly different numerical results due to floating-point round-off errors from different computation orders. To turn them off, set the environment variable `TF_ENABLE_ONEDNN_OPTS=0`.\\nI0000 00:00:1779771796.396307  279274 cpu_feature_guard.cc:227] This TensorFlow binary is optimized to use available CPU instructions in performance-critical operations.\\nTo enable the following instructions: AVX2 AVX512F AVX512_VNNI AVX512_BF16 AVX512_FP16 AVX_VNNI AMX_TILE AMX_INT8 AMX_BF16 FMA, in other operations, rebuild TensorFlow with the appropriate compiler flags.\\nWARNING: All log messages before absl::InitializeLog() is called are written to STDERR\\nI0000 00:00:1779771797.268169  279274 port.cc:153] oneDNN custom operations are on. You may see slightly different numerical results due to floating-point round-off errors from different computation orders. To turn them off, set the environment variable `TF_ENABLE_ONEDNN_OPTS=0`.\\n[*] Loading OpenVLA from: /root/autodl-tmp/models/openvla-7b-finetuned-libero-10\\n\\rLoading checkpoint shards:   0%|          | 0/4 [00:00<?, ?it/s]\\rLoading checkpoint shards:  25%|██▌       | 1/4 [00:00<00:00,  4.18it/s]\\rLoading checkpoint shards:  50%|█████     | 2/4 [00:00<00:00,  5.22it/s]\\rLoading checkpoint shards:  75%|███████▌  | 3/4 [00:00<00:00,  5.64it/s]\\rLoading checkpoint shards: 100%|██████████| 4/4 [00:00<00:00,  5.58it/s]\\rLoading checkpoint shards: 100%|██████████| 4/4 [00:00<00:00,  5.40it/s]\\n[*] Model loaded, GPU: 15.1 GB\\n[*] Vision tokens: 256, dim: 4096\\n[*] Random pruning: k=0.5\\n[robosuite WARNING] No private macro file found! (macros.py:53)\\n[robosuite WARNING] It is recommended to use a private macro file (macros.py:54)\\n[robosuite WARNING] To setup, run: python /root
…[truncated 4135 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_openvla_random_k05_long_seed42_v2_20260526T151649",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-26T15:18:27.771697+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_openvla_random_k05_long_seed42_v2",
  "field": "metrics",
  "value": "{'overall_sr': 0.186, 'total_episodes': 500, 'total_success': 93, 'task_sr': {'task01_alphabet_soup_tomato_sauce_basket': 0.3, 'task02_cream_cheese_butter_basket': 0.26, 'task03_stove_moka_pot': 0.22, 'task04_black_bowl_drawer': 0.02, 'task05_white_mug_left_yellow_mug_right': 0.06, 'task06_book_caddy': 0.44, 'task07_white_mug_plate_chocolate_pudding': 0.26, 'task08_alphabet_soup_cream_cheese_basket': 0.16, 'task09_moka_pots_stove': 0.08, 'task10_yellow_white_mug_microwave': 0.06}}",
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_openvla_random_k05_long_seed42_v2_20260526T151649",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_openvla_random_k05_long_seed42_v2",
    "field": "metrics",
    "value": "{'overall_sr': 0.186, 'total_episodes': 500, 'total_success': 93, 'task_sr': {'task01_alphabet_soup_tomato_sauce_basket': 0.3, 'task02_cream_cheese_butter_basket': 0.26, 'task03_stove_moka_pot': 0.22, 'task04_black_bowl_drawer': 0.02, 'task05_white_mug_left_yellow_mug_right': 0.06, 'task06_book_caddy': 0.44, 'task07_white_mug_plate_chocolate_pudding': 0.26, 'task08_alphabet_soup_cream_cheese_basket': 0.16, 'task09_moka_pots_stove': 0.08, 'task10_yellow_white_mug_microwave': 0.06}}",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-26T15:18:27.771915+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_openvla_random_k05_long_seed42_v2\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-26T05:02:35.826Z\", \"updated_at\": \"2026-05-26T15:17:23.164Z\", \"hypothesis\": \"OpenVLA Random k=0.5 Long v2 — extreme pruning（修复模型路径后重跑）。k=0.7 Long 在跑。k=0.5 测试 50% 压缩下 Long 性能\", \"parent\": \"eval_openvla_random_k05_long_seed42\", \"spec\": {\"command\": \"python -u eval_openvla_l2norm_libero.py --mode random_prune --k_ratio 0.5 --suite libero_10 --num_episodes 50 --seed 42 --model_path /root/autodl-tmp/models/openvla-7b-finetuned-libero-10 --unnorm_key libero_10\", \"server\": \"westd-38929\", \"gpu\": \"cuda:1\", \"pid\": 279274, \"log_path\": \"/root/runs/importance_margin_vla_compress/eval_openvla_random_k05_long_seed42_v2.log\", \"submitted_at\": \"2026-05-26T05:03:13.521Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/importance_margin_vla_compress\", \"data_count\": 500, \"model_name\": \"openvla-7b-finetuned-libero-10\", \"seed\": 42, \"checkpoint_source\": \"openvla-7b-finetuned-libero-10\", \"eval_data\": \"libero_10\"}, \"reproduce\": {\"finished_at\": \"2026-05-26T15:12:22.667Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-26T15:12:40.041394+00:00\"}]}, \"metrics\": {\"overall_sr\": 0.186, \"total_episodes\": 500, \"total_success\": 93, \"task_sr\": {\"task01_alphabet_soup_tomato_sauce_basket\": 0.3, \"task02_cream_cheese_butter_basket\": 0.26, \"task03_stove_moka_pot\": 0.22, \"task04_black_bowl_drawer\": 0.02, \"task05_white_mug_left_yellow_mug_right\": 0.06, \"task06_book_caddy\": 0.44, \"task07_white_mug_plate_chocolate_pudding\": 0.26, \"task08_alphabet_soup_cream_cheese_basket\": 0.16, \"task09_moka_pots_stove\": 0.08, \"task10_yellow_white_mug_microwave\": 0.06}}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 7.7
…[truncated 7 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_openvla_random_k05_long_seed42_v2_20260526T151649",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-26T15:18:27.772080+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_openvla_random_k05_long_seed42_v2",
  "field": "log_path",
  "value": "/root/runs/importance_margin_vla_compress/eval_openvla_random_k05_long_seed42_v2.log",
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_openvla_random_k05_long_seed42_v2_20260526T151649",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_openvla_random_k05_long_seed42_v2",
    "field": "log_path",
    "value": "/root/runs/importance_margin_vla_compress/eval_openvla_random_k05_long_seed42_v2.log",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-26T15:18:27.772285+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_openvla_random_k05_long_seed42_v2\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-26T05:02:35.826Z\", \"updated_at\": \"2026-05-26T15:17:36.429Z\", \"hypothesis\": \"OpenVLA Random k=0.5 Long v2 — extreme pruning（修复模型路径后重跑）。k=0.7 Long 在跑。k=0.5 测试 50% 压缩下 Long 性能\", \"parent\": \"eval_openvla_random_k05_long_seed42\", \"spec\": {\"command\": \"python -u eval_openvla_l2norm_libero.py --mode random_prune --k_ratio 0.5 --suite libero_10 --num_episodes 50 --seed 42 --model_path /root/autodl-tmp/models/openvla-7b-finetuned-libero-10 --unnorm_key libero_10\", \"server\": \"westd-38929\", \"gpu\": \"cuda:1\", \"pid\": 279274, \"log_path\": \"/root/runs/importance_margin_vla_compress/eval_openvla_random_k05_long_seed42_v2.log\", \"submitted_at\": \"2026-05-26T05:03:13.521Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/importance_margin_vla_compress\", \"data_count\": 500, \"model_name\": \"openvla-7b-finetuned-libero-10\", \"seed\": 42, \"checkpoint_source\": \"openvla-7b-finetuned-libero-10\", \"eval_data\": \"libero_10\"}, \"reproduce\": {\"finished_at\": \"2026-05-26T15:12:22.667Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-26T15:12:40.041394+00:00\"}]}, \"metrics\": {\"overall_sr\": 0.186, \"total_episodes\": 500, \"total_success\": 93, \"task_sr\": {\"task01_alphabet_soup_tomato_sauce_basket\": 0.3, \"task02_cream_cheese_butter_basket\": 0.26, \"task03_stove_moka_pot\": 0.22, \"task04_black_bowl_drawer\": 0.02, \"task05_white_mug_left_yellow_mug_right\": 0.06, \"task06_book_caddy\": 0.44, \"task07_white_mug_plate_chocolate_pudding\": 0.26, \"task08_alphabet_soup_cream_cheese_basket\": 0.16, \"task09_moka_pots_stove\": 0.08, \"task10_yellow_white_mug_microwave\": 0.06}}, \"log_path\": \"/root/runs/importance_margin_vla_compress/
…[truncated 111 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_openvla_random_k05_long_seed42_v2_20260526T151649",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-26T15:18:27.772448+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_openvla_random_k05_long_seed42_v2",
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
  "session": "worker_analyze_eval_openvla_random_k05_long_seed42_v2_20260526T151649",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_openvla_random_k05_long_seed42_v2",
    "field": "conclusion",
    "value": "negative",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-26T15:18:27.772598+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_openvla_random_k05_long_seed42_v2",
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
  "session": "worker_analyze_eval_openvla_random_k05_long_seed42_v2_20260526T151649",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_openvla_random_k05_long_seed42_v2",
    "field": "status",
    "value": "DONE",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-26T15:18:27.772769+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_openvla_random_k05_long_seed42_v2\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-26T05:02:35.826Z\", \"updated_at\": \"2026-05-26T15:17:47.577Z\", \"hypothesis\": \"OpenVLA Random k=0.5 Long v2 — extreme pruning（修复模型路径后重跑）。k=0.7 Long 在跑。k=0.5 测试 50% 压缩下 Long 性能\", \"parent\": \"eval_openvla_random_k05_long_seed42\", \"spec\": {\"command\": \"python -u eval_openvla_l2norm_libero.py --mode random_prune --k_ratio 0.5 --suite libero_10 --num_episodes 50 --seed 42 --model_path /root/autodl-tmp/models/openvla-7b-finetuned-libero-10 --unnorm_key libero_10\", \"server\": \"westd-38929\", \"gpu\": \"cuda:1\", \"pid\": 279274, \"log_path\": \"/root/runs/importance_margin_vla_compress/eval_openvla_random_k05_long_seed42_v2.log\", \"submitted_at\": \"2026-05-26T05:03:13.521Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/importance_margin_vla_compress\", \"data_count\": 500, \"model_name\": \"openvla-7b-finetuned-libero-10\", \"seed\": 42, \"checkpoint_source\": \"openvla-7b-finetuned-libero-10\", \"eval_data\": \"libero_10\"}, \"reproduce\": {\"finished_at\": \"2026-05-26T15:12:22.667Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-26T15:12:40.041394+00:00\"}]}, \"metrics\": {\"overall_sr\": 0.186, \"total_episodes\": 500, \"total_success\": 93, \"task_sr\": {\"task01_alphabet_soup_tomato_sauce_basket\": 0.3, \"task02_cream_cheese_butter_basket\": 0.26, \"task03_stove_moka_pot\": 0.22, \"task04_black_bowl_drawer\": 0.02, \"task05_white_mug_left_yellow_mug_right\": 0.06, \"task06_book_caddy\": 0.44, \"task07_white_mug_plate_chocolate_pudding\": 0.26, \"task08_alphabet_soup_cream_cheese_basket\": 0.16, \"task09_moka_pots_stove\": 0.08, \"task10_yellow_white_mug_microwave\": 0.06}}, \"log_path\": \"/root/runs/importance_margin_vla_compress/
…[truncated 141 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_openvla_random_k05_long_seed42_v2_20260526T151649",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-26T15:18:27.772925+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Cannot transition to DONE without output fields: ['checkpoint_path']. Set these fields first or pass them in spec.\", \"metadata\": {\"elapsed_seconds\": 5.2517}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_openvla_random_k05_long_seed42_v2_20260526T151649",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-26T15:18:27.773067+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_openvla_random_k05_long_seed42_v2",
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
  "session": "worker_analyze_eval_openvla_random_k05_long_seed42_v2_20260526T151649",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_openvla_random_k05_long_seed42_v2",
    "field": "checkpoint_path",
    "value": "N/A (eval-only)",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-26T15:18:27.773256+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_openvla_random_k05_long_seed42_v2\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-26T05:02:35.826Z\", \"updated_at\": \"2026-05-26T15:18:03.644Z\", \"hypothesis\": \"OpenVLA Random k=0.5 Long v2 — extreme pruning（修复模型路径后重跑）。k=0.7 Long 在跑。k=0.5 测试 50% 压缩下 Long 性能\", \"parent\": \"eval_openvla_random_k05_long_seed42\", \"spec\": {\"command\": \"python -u eval_openvla_l2norm_libero.py --mode random_prune --k_ratio 0.5 --suite libero_10 --num_episodes 50 --seed 42 --model_path /root/autodl-tmp/models/openvla-7b-finetuned-libero-10 --unnorm_key libero_10\", \"server\": \"westd-38929\", \"gpu\": \"cuda:1\", \"pid\": 279274, \"log_path\": \"/root/runs/importance_margin_vla_compress/eval_openvla_random_k05_long_seed42_v2.log\", \"submitted_at\": \"2026-05-26T05:03:13.521Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/importance_margin_vla_compress\", \"data_count\": 500, \"model_name\": \"openvla-7b-finetuned-libero-10\", \"seed\": 42, \"checkpoint_source\": \"openvla-7b-finetuned-libero-10\", \"eval_data\": \"libero_10\"}, \"reproduce\": {\"finished_at\": \"2026-05-26T15:12:22.667Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-26T15:12:40.041394+00:00\"}]}, \"metrics\": {\"overall_sr\": 0.186, \"total_episodes\": 500, \"total_success\": 93, \"task_sr\": {\"task01_alphabet_soup_tomato_sauce_basket\": 0.3, \"task02_cream_cheese_butter_basket\": 0.26, \"task03_stove_moka_pot\": 0.22, \"task04_black_bowl_drawer\": 0.02, \"task05_white_mug_left_yellow_mug_right\": 0.06, \"task06_book_caddy\": 0.44, \"task07_white_mug_plate_chocolate_pudding\": 0.26, \"task08_alphabet_soup_cream_cheese_basket\": 0.16, \"task09_moka_pots_stove\": 0.08, \"task10_yellow_white_mug_microwave\": 0.06}}, \"log_path\": \"/root/runs/importance_margin_vla_compress/
…[truncated 183 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_openvla_random_k05_long_seed42_v2_20260526T151649",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-26T15:18:27.773420+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_openvla_random_k05_long_seed42_v2",
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
  "session": "worker_analyze_eval_openvla_random_k05_long_seed42_v2_20260526T151649",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_openvla_random_k05_long_seed42_v2",
    "field": "status",
    "value": "DONE",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-26T15:18:27.773621+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_openvla_random_k05_long_seed42_v2\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-26T05:02:35.826Z\", \"updated_at\": \"2026-05-26T15:18:10.408Z\", \"hypothesis\": \"OpenVLA Random k=0.5 Long v2 — extreme pruning（修复模型路径后重跑）。k=0.7 Long 在跑。k=0.5 测试 50% 压缩下 Long 性能\", \"parent\": \"eval_openvla_random_k05_long_seed42\", \"spec\": {\"command\": \"python -u eval_openvla_l2norm_libero.py --mode random_prune --k_ratio 0.5 --suite libero_10 --num_episodes 50 --seed 42 --model_path /root/autodl-tmp/models/openvla-7b-finetuned-libero-10 --unnorm_key libero_10\", \"server\": \"westd-38929\", \"gpu\": \"cuda:1\", \"pid\": 279274, \"log_path\": \"/root/runs/importance_margin_vla_compress/eval_openvla_random_k05_long_seed42_v2.log\", \"submitted_at\": \"2026-05-26T05:03:13.521Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/importance_margin_vla_compress\", \"data_count\": 500, \"model_name\": \"openvla-7b-finetuned-libero-10\", \"seed\": 42, \"checkpoint_source\": \"openvla-7b-finetuned-libero-10\", \"eval_data\": \"libero_10\", \"wall_clock_seconds\": 36896.9, \"gpu_hours\": 10.25}, \"reproduce\": {\"finished_at\": \"2026-05-26T15:12:22.667Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-26T15:12:40.041394+00:00\"}]}, \"metrics\": {\"overall_sr\": 0.186, \"total_episodes\": 500, \"total_success\": 93, \"task_sr\": {\"task01_alphabet_soup_tomato_sauce_basket\": 0.3, \"task02_cream_cheese_butter_basket\": 0.26, \"task03_stove_moka_pot\": 0.22, \"task04_black_bowl_drawer\": 0.02, \"task05_white_mug_left_yellow_mug_right\": 0.06, \"task06_book_caddy\": 0.44, \"task07_white_mug_plate_chocolate_pudding\": 0.26, \"task08_alphabet_soup_cream_cheese_basket\": 0.16, \"task09_moka_pots_stove\": 0.08, \"task10_yellow_white_mug_microwave\": 0.06}}, \"log_pa
…[truncated 333 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_openvla_random_k05_long_seed42_v2_20260526T151649",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-26T15:18:27.773824+00:00_

Registry 已更新。结果汇总：

**Overall SR: 18.6% (93/500)** — conclusion: **negative**

对比 baseline (k=1.0) 46.8%，random k=0.5 下降 **28.2 个百分点（-60%相对降幅）**。

| Task | SR |
|------|----|
| T1 alphabet soup + tomato sauce → basket | 30.0% |
| T2 cream cheese + butter → basket | 26.0% |
| T3 stove + moka pot | 22.0% |
| T4 black bowl → drawer | 2.0% |
| T5 white mug left + yellow mug right | 6.0% |
| T6 book → caddy | 44.0% |
| T7 white mug plate + chocolate pudding | 26.0% |
| T8 alphabet soup + cream cheese → basket | 16.0% |
| T9 moka pots → stove | 8.0% |
| T10 yellow white mug → microwave | 6.0% |

OpenVLA Long cliff curve 目前：k=1.0 → 46.8%, k=0.7 → 38.8%, k=0.5 → 18.6%。k=0.5 到 k=0.7 之间存在明显的性能悬崖，随机剪枝在 50% 压缩率下性能崩塌严重。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analyze_eval_openvla_random_k05_long_seed42_v2_20260526T151649"
}
```

</details>

---
