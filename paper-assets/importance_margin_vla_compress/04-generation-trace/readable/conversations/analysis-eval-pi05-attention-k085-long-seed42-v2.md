# analysis eval pi05 attention k085 long seed42 v2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 17
- **Recorded user turns:** 0
- **Tool calls:** 8
- **Original source:** `logs/chats/worker_analysis_eval_pi05_attention_k085_long_seed42_v2_20260526T163015.jsonl`
- **Structured JSON:** [`97fa3704c6de1267e2ba.json`](../../sessions/97/97fa3704c6de1267e2ba.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

17 recorded events

### Tool call

_source line 1 · 2026-05-26T16:31:41.970731+00:00_

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
  "session": "worker_analysis_eval_pi05_attention_k085_long_seed42_v2_20260526T163015",
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

_source line 2 · 2026-05-26T16:31:41.973363+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_pi05_attention_k085_long_seed42_v2_20260526T163015",
  "tool": "ToolSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-26T16:31:41.973681+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-33015",
  "command": "tail -100 ~/runs/importance_margin_vla_compress/eval_pi05_attention_k085_long_seed42_v2.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_eval_pi05_attention_k085_long_seed42_v2_20260526T163015",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-33015",
    "command": "tail -100 ~/runs/importance_margin_vla_compress/eval_pi05_attention_k085_long_seed42_v2.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-26T16:31:41.974048+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-26 20:03:21,567 Config: suite=libero_10, prune=attention, keep=0.85, eps=50, gpu=0\\n2026-05-26 20:03:21,567 Loading pi0.5 from /root/autodl-tmp/pi05_libero_finetuned ...\\nThe PI05 model is a direct port of the OpenPI implementation. \\nThis implementation follows the original OpenPI structure for compatibility. \\nOriginal implementation: https://github.com/Physical-Intelligence/openpi\\n2026-05-26 20:05:39,484 Enabled gradient checkpointing for PI05Pytorch model\\nLoading model from: /root/autodl-tmp/pi05_libero_finetuned\\n✓ Loaded state dict from model.safetensors\\n2026-05-26 20:05:44,251 Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embedding.bias\\n2026-05-26 20:05:44,251 Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embedding.weight\\nAll keys loaded successfully!\\n2026-05-26 20:05:47,755 Patched embed_image\\n2026-05-26 20:05:47,769 Model: 4143.4M params\\n2026-05-26 20:05:47,769 Vision tokens: 256/image, 3 slots -> 768 total\\n2026-05-26 20:05:47,769 Baseline mode (no pruning), embed_prefix fixed\\n2026-05-26 20:05:47,770 Pruning: attention, keep 217/256 tokens/image (651 total, 2-layer probe)\\n2026-05-26 20:05:49,077 Preprocessor/postprocessor loaded\\n[robosuite WARNING] No private macro file found! (macros.py:53)\\n2026-05-26 20:05:49,113 No private macro file found!\\n[robosuite WARNING] It is recommended to use a private macro file (macros.py:54)\\n2026-05-26 20:05:49,113 It is recommended to use a private macro file\\n[robosuite WARNING] To setup, run: python /root/miniconda3/lib/python3.12/site-packages/robosuite/scripts/setup_macros.py (macros.py:55)\\n2026-05-26 20:05:49,113 To setup, run: python /root/miniconda3/lib/python3.12/site-packages/robosuite/scripts/setup_macros.py\\n2026-05-26 20:05:49,184 No OpenGL_accelera
…[truncated 6305 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_pi05_attention_k085_long_seed42_v2_20260526T163015",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-26T16:31:41.974372+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-33015",
  "command": "grep -i \"wandb\\|w&b\\|run_id\" ~/runs/importance_margin_vla_compress/eval_pi05_attention_k085_long_seed42_v2.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_eval_pi05_attention_k085_long_seed42_v2_20260526T163015",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-33015",
    "command": "grep -i \"wandb\\|w&b\\|run_id\" ~/runs/importance_margin_vla_compress/eval_pi05_attention_k085_long_seed42_v2.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-26T16:31:41.974592+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_pi05_attention_k085_long_seed42_v2_20260526T163015",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-26T16:31:41.974808+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-33015",
  "command": "grep -i wandb ~/runs/importance_margin_vla_compress/eval_pi05_attention_k085_long_seed42_v2.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_eval_pi05_attention_k085_long_seed42_v2_20260526T163015",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-33015",
    "command": "grep -i wandb ~/runs/importance_margin_vla_compress/eval_pi05_attention_k085_long_seed42_v2.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-26T16:31:41.975014+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.39}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_pi05_attention_k085_long_seed42_v2_20260526T163015",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-26T16:31:41.976817+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_pi05_attention_k085_long_seed42_v2",
  "field": "metrics",
  "value": "{'overall_sr': 51.6, 'total_episodes': 500, 'per_task': {'T0_alphabet_soup_tomato': 20, 'T1_cream_cheese_butter': 54, 'T2_stove_moka_pot': 32, 'T3_black_bowl_drawer': 60, 'T4_white_mug_left_plate': 48, 'T5_book_back_shelf': 90, 'T6_white_mug_plate': 68, 'T7_alphabet_soup_cream': 46, 'T8_moka_pots_stove': 6, 'T9_yellow_white_mug_microwave': 92}}",
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_eval_pi05_attention_k085_long_seed42_v2_20260526T163015",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_pi05_attention_k085_long_seed42_v2",
    "field": "metrics",
    "value": "{'overall_sr': 51.6, 'total_episodes': 500, 'per_task': {'T0_alphabet_soup_tomato': 20, 'T1_cream_cheese_butter': 54, 'T2_stove_moka_pot': 32, 'T3_black_bowl_drawer': 60, 'T4_white_mug_left_plate': 48, 'T5_book_back_shelf': 90, 'T6_white_mug_plate': 68, 'T7_alphabet_soup_cream': 46, 'T8_moka_pots_stove': 6, 'T9_yellow_white_mug_microwave': 92}}",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-26T16:31:41.977175+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_pi05_attention_k085_long_seed42_v2\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-26T12:03:20.348Z\", \"updated_at\": \"2026-05-26T16:30:48.750Z\", \"spec\": {\"command\": \"HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl CUDA_VISIBLE_DEVICES=3 /root/miniconda3/bin/python -u /root/autodl-tmp/importance_margin_vla_compress/eval_pi05_pruning_libero.py --prune_mode attention --keep_ratio 0.85 --suite libero_10 --n_episodes 50 --seed 42 --gpu 0\", \"server\": \"cqa1-33015\", \"gpu\": \"cuda:3\", \"pid\": 337364, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_attention_k085_long_seed42_v2.log\", \"submitted_at\": \"2026-05-26T12:03:18.408Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"libero_10\", \"data_count\": 50, \"model_name\": \"pi0.5\", \"seed\": 42, \"checkpoint_path\": \"N/A (eval only)\", \"checkpoint_source\": \"/root/autodl-tmp/pi05_libero_finetuned\", \"eval_data\": \"libero_10\"}, \"hypothesis\": \"π0.5 Attention k=0.85 Long seed42 — Attn Long cliff curve 中间点。Attn k=0.9=63.8%, k=0.75=51.8%。k=0.85 填补两者之间数据缺口（v1 进程静默死亡，v2 改用绝对路径 python 重试）\", \"parent\": \"eval_pi05_attention_k09_long_seed42\", \"reproduce\": {\"finished_at\": \"2026-05-26T16:27:34.539Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-26T16:27:49.989596+00:00\"}]}, \"metrics\": {\"overall_sr\": 51.6, \"total_episodes\": 500, \"per_task\": {\"T0_alphabet_soup_tomato\": 20, \"T1_cream_cheese_butter\": 54, \"T2_stove_moka_pot\": 32, \"T3_black_bowl_drawer\": 60, \"T4_white_mug_left_plate\": 48, \"T5_book_back_shelf\": 90, \"T6_white_mug_plate\": 68, \"T7_alphabet_soup_cream\": 46, \"T8_moka_pots_stove\": 6, \"T9_yellow_white_mug_microwave\": 92}}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.3119}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_pi05_attention_k085_long_seed42_v2_20260526T163015",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-26T16:31:41.977455+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_pi05_attention_k085_long_seed42_v2",
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
  "session": "worker_analysis_eval_pi05_attention_k085_long_seed42_v2_20260526T163015",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_pi05_attention_k085_long_seed42_v2",
    "field": "conclusion",
    "value": "success",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-26T16:31:41.977747+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_pi05_attention_k085_long_seed42_v2\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-26T12:03:20.348Z\", \"updated_at\": \"2026-05-26T16:30:56.959Z\", \"spec\": {\"command\": \"HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl CUDA_VISIBLE_DEVICES=3 /root/miniconda3/bin/python -u /root/autodl-tmp/importance_margin_vla_compress/eval_pi05_pruning_libero.py --prune_mode attention --keep_ratio 0.85 --suite libero_10 --n_episodes 50 --seed 42 --gpu 0\", \"server\": \"cqa1-33015\", \"gpu\": \"cuda:3\", \"pid\": 337364, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_attention_k085_long_seed42_v2.log\", \"submitted_at\": \"2026-05-26T12:03:18.408Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"libero_10\", \"data_count\": 50, \"model_name\": \"pi0.5\", \"seed\": 42, \"checkpoint_path\": \"N/A (eval only)\", \"checkpoint_source\": \"/root/autodl-tmp/pi05_libero_finetuned\", \"eval_data\": \"libero_10\"}, \"hypothesis\": \"π0.5 Attention k=0.85 Long seed42 — Attn Long cliff curve 中间点。Attn k=0.9=63.8%, k=0.75=51.8%。k=0.85 填补两者之间数据缺口（v1 进程静默死亡，v2 改用绝对路径 python 重试）\", \"parent\": \"eval_pi05_attention_k09_long_seed42\", \"reproduce\": {\"finished_at\": \"2026-05-26T16:27:34.539Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-26T16:27:49.989596+00:00\"}]}, \"metrics\": {\"overall_sr\": 51.6, \"total_episodes\": 500, \"per_task\": {\"T0_alphabet_soup_tomato\": 20, \"T1_cream_cheese_butter\": 54, \"T2_stove_moka_pot\": 32, \"T3_black_bowl_drawer\": 60, \"T4_white_mug_left_plate\": 48, \"T5_book_back_shelf\": 90, \"T6_white_mug_plate\": 68, \"T7_alphabet_soup_cream\": 46, \"T8_moka_pots_stove\": 6, \"T9_yellow_white_mug_microwave\": 92}}, \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elaps
…[truncated 24 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_pi05_attention_k085_long_seed42_v2_20260526T163015",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-26T16:31:41.977991+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_pi05_attention_k085_long_seed42_v2",
  "field": "log_path",
  "value": "~/runs/importance_margin_vla_compress/eval_pi05_attention_k085_long_seed42_v2.log",
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_eval_pi05_attention_k085_long_seed42_v2_20260526T163015",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_pi05_attention_k085_long_seed42_v2",
    "field": "log_path",
    "value": "~/runs/importance_margin_vla_compress/eval_pi05_attention_k085_long_seed42_v2.log",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-26T16:31:41.978432+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_pi05_attention_k085_long_seed42_v2\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-26T12:03:20.348Z\", \"updated_at\": \"2026-05-26T16:31:06.752Z\", \"spec\": {\"command\": \"HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl CUDA_VISIBLE_DEVICES=3 /root/miniconda3/bin/python -u /root/autodl-tmp/importance_margin_vla_compress/eval_pi05_pruning_libero.py --prune_mode attention --keep_ratio 0.85 --suite libero_10 --n_episodes 50 --seed 42 --gpu 0\", \"server\": \"cqa1-33015\", \"gpu\": \"cuda:3\", \"pid\": 337364, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_attention_k085_long_seed42_v2.log\", \"submitted_at\": \"2026-05-26T12:03:18.408Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"libero_10\", \"data_count\": 50, \"model_name\": \"pi0.5\", \"seed\": 42, \"checkpoint_path\": \"N/A (eval only)\", \"checkpoint_source\": \"/root/autodl-tmp/pi05_libero_finetuned\", \"eval_data\": \"libero_10\"}, \"hypothesis\": \"π0.5 Attention k=0.85 Long seed42 — Attn Long cliff curve 中间点。Attn k=0.9=63.8%, k=0.75=51.8%。k=0.85 填补两者之间数据缺口（v1 进程静默死亡，v2 改用绝对路径 python 重试）\", \"parent\": \"eval_pi05_attention_k09_long_seed42\", \"reproduce\": {\"finished_at\": \"2026-05-26T16:27:34.539Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-26T16:27:49.989596+00:00\"}]}, \"metrics\": {\"overall_sr\": 51.6, \"total_episodes\": 500, \"per_task\": {\"T0_alphabet_soup_tomato\": 20, \"T1_cream_cheese_butter\": 54, \"T2_stove_moka_pot\": 32, \"T3_black_bowl_drawer\": 60, \"T4_white_mug_left_plate\": 48, \"T5_book_back_shelf\": 90, \"T6_white_mug_plate\": 68, \"T7_alphabet_soup_cream\": 46, \"T8_moka_pots_stove\": 6, \"T9_yellow_white_mug_microwave\": 92}}, \"conclusion\": \"success\", \"log_path\": \"~/runs/importance_margin_
…[truncated 125 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_pi05_attention_k085_long_seed42_v2_20260526T163015",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-26T16:31:41.978705+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_pi05_attention_k085_long_seed42_v2",
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
  "session": "worker_analysis_eval_pi05_attention_k085_long_seed42_v2_20260526T163015",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_pi05_attention_k085_long_seed42_v2",
    "field": "status",
    "value": "DONE",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-26T16:31:41.979027+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_pi05_attention_k085_long_seed42_v2\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-26T12:03:20.348Z\", \"updated_at\": \"2026-05-26T16:31:18.486Z\", \"spec\": {\"command\": \"HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl CUDA_VISIBLE_DEVICES=3 /root/miniconda3/bin/python -u /root/autodl-tmp/importance_margin_vla_compress/eval_pi05_pruning_libero.py --prune_mode attention --keep_ratio 0.85 --suite libero_10 --n_episodes 50 --seed 42 --gpu 0\", \"server\": \"cqa1-33015\", \"gpu\": \"cuda:3\", \"pid\": 337364, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_attention_k085_long_seed42_v2.log\", \"submitted_at\": \"2026-05-26T12:03:18.408Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"libero_10\", \"data_count\": 50, \"model_name\": \"pi0.5\", \"seed\": 42, \"checkpoint_path\": \"N/A (eval only)\", \"checkpoint_source\": \"/root/autodl-tmp/pi05_libero_finetuned\", \"eval_data\": \"libero_10\", \"wall_clock_seconds\": 16080.1, \"gpu_hours\": 4.47}, \"hypothesis\": \"π0.5 Attention k=0.85 Long seed42 — Attn Long cliff curve 中间点。Attn k=0.9=63.8%, k=0.75=51.8%。k=0.85 填补两者之间数据缺口（v1 进程静默死亡，v2 改用绝对路径 python 重试）\", \"parent\": \"eval_pi05_attention_k09_long_seed42\", \"reproduce\": {\"finished_at\": \"2026-05-26T16:27:34.539Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-26T16:27:49.989596+00:00\"}]}, \"metrics\": {\"overall_sr\": 51.6, \"total_episodes\": 500, \"per_task\": {\"T0_alphabet_soup_tomato\": 20, \"T1_cream_cheese_butter\": 54, \"T2_stove_moka_pot\": 32, \"T3_black_bowl_drawer\": 60, \"T4_white_mug_left_plate\": 48, \"T5_book_back_shelf\": 90, \"T6_white_mug_plate\": 68, \"T7_alphabet_soup_cream\": 46, \"T8_moka_pots_stove\": 6, \"T9_yellow_white_mug_microwave\": 92}}, \"conclusion\": \"suc
…[truncated 274 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_pi05_attention_k085_long_seed42_v2_20260526T163015",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-26T16:31:41.979387+00:00_

Registry 全部更新完毕。

**结果汇总：**

| 指标 | 值 |
|------|-----|
| **Overall SR** | **51.6%** (258/500) |
| Total episodes | 500 (10 tasks × 50 eps) |
| 运行时间 | 260.4 min (~4.47 GPU hours) |
| W&B | 无 |
| 异常 | 无 |

**Per-task SR：**

| Task | SR |
|------|-----|
| T0 alphabet_soup_tomato | 20% |
| T1 cream_cheese_butter | 54% |
| T2 stove_moka_pot | 32% |
| T3 black_bowl_drawer | 60% |
| T4 white_mug_left_plate | 48% |
| T5 book_back_shelf | 90% |
| T6 white_mug_plate | 68% |
| T7 alphabet_soup_cream | 46% |
| T8 moka_pots_stove | 6% |
| T9 yellow_white_mug_microwave | 92% |

**Cliff curve 定位：** Attn k=0.85 Long SR=51.6%，与 k=0.75 (51.8%) 几乎持平，说明 cliff 发生在 k=0.85~0.9 之间（k=0.9=63.8% → k=0.85=51.6% 骤降 12.2pp）。与 ROADMAP D245 记录的 51.6% 一致。Conclusion: success, status: DONE。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_eval_pi05_attention_k085_long_seed42_v2_20260526T163015"
}
```

</details>

---
