# eval smart compress m32 libero goal

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 0
- **Tool calls:** 5
- **Original source:** `logs/chats/worker_eval_smart_compress_m32_libero_goal_20260519T000106.jsonl`
- **Structured JSON:** [`b4cc52c865d0df6a93c1.json`](../../sessions/b4/b4cc52c865d0df6a93c1.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

11 recorded events

### Tool call

_source line 1 · 2026-05-19T00:02:00.512681+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__submit_training_job,mcp__agent-ml-research__ssh_read_only",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_smart_compress_m32_libero_goal_20260519T000106",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__submit_training_job,mcp__agent-ml-research__ssh_read_only",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-19T00:02:00.513019+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_smart_compress_m32_libero_goal_20260519T000106",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-19T00:02:00.513264+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-33015",
  "command": "ls -la /root/autodl-tmp/importance_margin_vla_compress/checkpoints/smart_compress_m32/checkpoint.pt",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_smart_compress_m32_libero_goal_20260519T000106",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-33015",
    "command": "ls -la /root/autodl-tmp/importance_margin_vla_compress/checkpoints/smart_compress_m32/checkpoint.pt",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-19T00:02:00.513431+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-33015",
  "command": "bash -c \"source /root/miniconda3/bin/activate && cd /root/autodl-tmp/importance_margin_vla_compress && python eval_smart_compress_libero.py --help\"",
  "account": "root",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_smart_compress_m32_libero_goal_20260519T000106",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-33015",
    "command": "bash -c \"source /root/miniconda3/bin/activate && cd /root/autodl-tmp/importance_margin_vla_compress && python eval_smart_compress_libero.py --help\"",
    "account": "root",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-19T00:02:00.513575+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"-rw-r--r-- 1 root root 1585968491 May 18 08:28 /root/autodl-tmp/importance_margin_vla_compress/checkpoints/smart_compress_m32/checkpoint.pt\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.09}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_smart_compress_m32_libero_goal_20260519T000106",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-19T00:02:00.513717+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"usage: eval_smart_compress_libero.py [-h] --n_queries N_QUERIES\\n                                     --checkpoint_path CHECKPOINT_PATH\\n                                     [--suite {libero_spatial,libero_object,libero_goal,libero_10,libero_90}]\\n                                     [--num_episodes NUM_EPISODES] [--gpu GPU]\\n                                     [--seed SEED]\\n                                     [--action_horizon ACTION_HORIZON]\\n                                     [--max_steps MAX_STEPS] [--output OUTPUT]\\n                                     [--task_ids TASK_IDS]\\n\\nLIBERO eval for SmartCompress models\\n\\noptions:\\n  -h, --help            show this help message and exit\\n  --n_queries N_QUERIES\\n                        M: number of compressed vision tokens\\n  --checkpoint_path CHECKPOINT_PATH\\n                        Path to checkpoint.pt\\n  --suite {libero_spatial,libero_object,libero_goal,libero_10,libero_90}\\n  --num_episodes NUM_EPISODES\\n  --gpu GPU\\n  --seed SEED\\n  --action_horizon ACTION_HORIZON\\n  --max_steps MAX_STEPS\\n  --output OUTPUT\\n  --task_ids TASK_IDS\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.79}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_smart_compress_m32_libero_goal_20260519T000106",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-19T00:02:00.513869+00:00_

called mcp__agent-ml-research__submit_training_job

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_training_job</summary>

```json
{
  "server": "cqa1-33015",
  "gpu_ids": "['cuda:0']",
  "exp_id": "eval_smart_compress_m32_libero_goal",
  "command": "bash -c \"source /root/miniconda3/bin/activate && cd /root/autodl-tmp/importance_margin_vla_compress && CUDA_VISIBLE_DEVICES=0 python -u eval_smart_compress_libero.py --n_queries 32 --checkpoint_path checkpoints/smart_compress_m32/checkpoint.pt --suite libero_goal --num_episodes 50 --gpu 0 --seed 42 --output eval_results/eval_smart_compress_m32_libero_goal.json 2>&1 | tee eval_smart_compress_m32_libero_goal.log\"",
  "project": "importance_margin_vla_compress",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_smart_compress_m32_libero_goal_20260519T000106",
  "tool": "mcp__agent-ml-research__submit_training_job",
  "tool_args": {
    "server": "cqa1-33015",
    "gpu_ids": "['cuda:0']",
    "exp_id": "eval_smart_compress_m32_libero_goal",
    "command": "bash -c \"source /root/miniconda3/bin/activate && cd /root/autodl-tmp/importance_margin_vla_compress && CUDA_VISIBLE_DEVICES=0 python -u eval_smart_compress_libero.py --n_queries 32 --checkpoint_path checkpoints/smart_compress_m32/checkpoint.pt --suite libero_goal --num_episodes 50 --gpu 0 --seed 42 --output eval_results/eval_smart_compress_m32_libero_goal.json 2>&1 | tee eval_smart_compress_m32_libero_goal.log\"",
    "project": "importance_margin_vla_compress",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-19T00:02:00.514022+00:00_

{"result":"{\"success\": true, \"data\": {\"pid\": \"571598\", \"log_file\": \"~/runs/importance_margin_vla_compress/eval_smart_compress_m32_libero_goal.log\", \"gpu_ids\": [\"cuda:0\"], \"server\": \"cqa1-33015\", \"account\": \"root\", \"cuda_visible_devices\": \"0\", \"backend\": \"tmux\", \"tmux_session\": \"eval_smart_compress_m32_libero_goal\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.39}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_smart_compress_m32_libero_goal_20260519T000106",
  "tool": "mcp__agent-ml-research__submit_training_job",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-19T00:02:00.514184+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-33015",
  "command": "bash -c \"sleep 15 && tail -50 /root/autodl-tmp/importance_margin_vla_compress/eval_smart_compress_m32_libero_goal.log\"",
  "account": "root",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_smart_compress_m32_libero_goal_20260519T000106",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-33015",
    "command": "bash -c \"sleep 15 && tail -50 /root/autodl-tmp/importance_margin_vla_compress/eval_smart_compress_m32_libero_goal.log\"",
    "account": "root",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-19T00:02:00.514340+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-19 08:01:37 [INFO] Suite: libero_goal | Device: cuda:0 | M=32 | Episodes/task: 50 | Max steps: 300\\n2026-05-19 08:01:37 [INFO] Loading model from checkpoints/smart_compress_m32/checkpoint.pt ...\\n2026-05-19 08:01:37 [INFO] JAX version 0.10.0 available.\\nLoading  HuggingFaceTB/SmolVLM2-500M-Video-Instruct weights ...\\nYou have video processor config saved in `preprocessor.json` file which is deprecated. Video processor configs should be saved in their own `video_preprocessor.json` file. You can rename the file or load and save the processor back which renames it automatically. Loading from `preprocessor.json` will be removed in v5.0.\\nReducing the number of VLM layers to 16 ...\\nLoading weights from local directory\\n2026-05-19 08:01:50 [INFO] Checkpoint loaded with strict match (no missing/unexpected keys)\\n2026-05-19 08:01:50 [INFO] SmartCompressWrapper loaded: M=32, compressor params=22179840\\n2026-05-19 08:01:50 [INFO] Model loaded in 13.2s\\n[robosuite WARNING] No private macro file found! (macros.py:53)\\n2026-05-19 08:01:51 [WARNING] No private macro file found!\\n[robosuite WARNING] It is recommended to use a private macro file (macros.py:54)\\n2026-05-19 08:01:51 [WARNING] It is recommended to use a private macro file\\n[robosuite WARNING] To setup, run: python /root/miniconda3/lib/python3.12/site-packages/robosuite/scripts/setup_macros.py (macros.py:55)\\n2026-05-19 08:01:51 [WARNING] To setup, run: python /root/miniconda3/lib/python3.12/site-packages/robosuite/scripts/setup_macros.py\\n2026-05-19 08:01:51 [INFO] No OpenGL_accelerate module loaded: No module named 'OpenGL_accelerate'\\n[info] using task orders [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\\n2026-05-19 08:01:51 [INFO] Suite 'libero_goal' has 10 tasks, evaluating 10: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\\n2026-05-19 08:01:51 [INFO] --- Task 0: open the middle drawer of the cabinet ---\\nLocal assets not found. Downloading from HuggingFace Hub
…[truncated 169 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_smart_compress_m32_libero_goal_20260519T000106",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-19T00:02:00.514519+00:00_

启动成功：

- **Checkpoint**: `checkpoint.pt` 已加载，strict match，无 missing/unexpected keys
- **SmartCompressWrapper loaded: M=32**, compressor params=22,179,840
- **Suite**: `libero_goal`, 10 tasks, 50 episodes/task, seed=42
- **Task 0** 已开始：`open the middle drawer of the cabinet`，assets 已下载

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_eval_smart_compress_m32_libero_goal_20260519T000106"
}
```

</details>

---
