# eval k07 zero mask

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 0
- **Tool calls:** 6
- **Original source:** `logs/chats/worker_eval_k07_zero_mask_20260517T094321.jsonl`
- **Structured JSON:** [`0362b562295e2165a206.json`](../../sessions/03/0362b562295e2165a206.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

13 recorded events

### Tool call

_source line 1 · 2026-05-17T09:44:19.229934+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_execute",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_k07_zero_mask_20260517T094321",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_execute",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-17T09:44:19.230338+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_k07_zero_mask_20260517T094321",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-17T09:44:19.230532+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-27271",
  "command": "cd /root/autodl-tmp/importance_margin_vla_compress && ls -la checkpoints/libero_acis_stage1only_k07/stage1_done/checkpoint.pt 2>&1; echo \"---\"; ls configs/libero_acis_stage1only_k07.yaml 2>&1",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_k07_zero_mask_20260517T094321",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-27271",
    "command": "cd /root/autodl-tmp/importance_margin_vla_compress && ls -la checkpoints/libero_acis_stage1only_k07/stage1_done/checkpoint.pt 2>&1; echo \"---\"; ls configs/libero_acis_stage1only_k07.yaml 2>&1",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-17T09:44:19.230677+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"-rw-r--r-- 1 root root 920907737 May 17 15:56 checkpoints/libero_acis_stage1only_k07/stage1_done/checkpoint.pt\\n---\\nconfigs/libero_acis_stage1only_k07.yaml\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.49}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_k07_zero_mask_20260517T094321",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-17T09:44:19.230824+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-27271",
  "command": "cd /root/autodl-tmp/importance_margin_vla_compress && python eval_success_rate_libero.py --help 2>&1 | head -60",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_k07_zero_mask_20260517T094321",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-27271",
    "command": "cd /root/autodl-tmp/importance_margin_vla_compress && python eval_success_rate_libero.py --help 2>&1 | head -60",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-17T09:44:19.230963+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"bash: line 1: python: command not found\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.08}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_k07_zero_mask_20260517T094321",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-17T09:44:19.231085+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-27271",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && python eval_success_rate_libero.py --help 2>&1 | head -60",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_k07_zero_mask_20260517T094321",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-27271",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && python eval_success_rate_libero.py --help 2>&1 | head -60",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-17T09:44:19.231268+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"usage: eval_success_rate_libero.py [-h] --checkpoint CHECKPOINT\\n                                   [--config CONFIG]\\n                                   [--suite {libero_spatial,libero_object,libero_goal,libero_10,libero_90}]\\n                                   [--num_episodes NUM_EPISODES] [--gpu GPU]\\n                                   [--seed SEED]\\n                                   [--action_horizon ACTION_HORIZON]\\n                                   [--max_steps MAX_STEPS] [--output OUTPUT]\\n                                   [--mode {baseline,acis_prune,random_prune}]\\n                                   [--task_ids TASK_IDS]\\n                                   [--pruning-method {zero_mask,true_removal}]\\n\\nLIBERO success rate evaluation\\n\\noptions:\\n  -h, --help            show this help message and exit\\n  --checkpoint CHECKPOINT\\n                        Path to checkpoint.pt\\n  --config CONFIG       Path to YAML config\\n  --suite {libero_spatial,libero_object,libero_goal,libero_10,libero_90}\\n                        LIBERO suite name\\n  --num_episodes NUM_EPISODES\\n                        Episodes per task\\n  --gpu GPU\\n  --seed SEED\\n  --action_horizon ACTION_HORIZON\\n                        Actions to execute per chunk before re-planning\\n  --max_steps MAX_STEPS\\n                        Override max steps per episode (default: per-suite)\\n  --output OUTPUT       Output JSON path (default:\\n                        eval_results/libero_{suite}.json)\\n  --mode {baseline,acis_prune,random_prune}\\n  --task_ids TASK_IDS   Comma-separated task IDs to evaluate (default: all)\\n  --pruning-method {zero_mask,true_removal}\\n                        zero_mask: zero out pruned tokens; true_removal: drop\\n                        pruned tokens from sequence\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.72}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_k07_zero_mask_20260517T094321",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-17T09:44:19.231455+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-27271",
  "command": "cd /root/autodl-tmp/importance_margin_vla_compress && mkdir -p eval_results && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && tmux new-session -d -s eval_k07_zero_mask 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && CUDA_VISIBLE_DEVICES=1 python eval_success_rate_libero.py --checkpoint checkpoints/libero_acis_stage1only_k07/stage1_done/checkpoint.pt --config configs/libero_acis_stage1only_k07.yaml --suite libero_object --mode acis_prune --pruning-method zero_mask --num_episodes 50 --gpu 0 2>&1 | tee eval_results/eval_k07_zero_mask.log' && echo \"tmux session started\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_k07_zero_mask_20260517T094321",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-27271",
    "command": "cd /root/autodl-tmp/importance_margin_vla_compress && mkdir -p eval_results && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && tmux new-session -d -s eval_k07_zero_mask 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && CUDA_VISIBLE_DEVICES=1 python eval_success_rate_libero.py --checkpoint checkpoints/libero_acis_stage1only_k07/stage1_done/checkpoint.pt --config configs/libero_acis_stage1only_k07.yaml --suite libero_object --mode acis_prune --pruning-method zero_mask --num_episodes 50 --gpu 0 2>&1 | tee eval_results/eval_k07_zero_mask.log' && echo \"tmux session started\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-17T09:44:19.231589+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"tmux session started\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.17}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_k07_zero_mask_20260517T094321",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-17T09:44:19.231707+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-27271",
  "command": "tmux list-sessions 2>&1; echo \"---\"; ps aux | grep eval_success_rate | grep -v grep",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_k07_zero_mask_20260517T094321",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-27271",
    "command": "tmux list-sessions 2>&1; echo \"---\"; ps aux | grep eval_success_rate | grep -v grep",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-17T09:44:19.231834+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"eval_k07_zero_mask: 1 windows (created Sun May 17 17:44:06 2026)\\n---\\nroot     328498  0.0  0.0   6084  3852 ?        Ss   17:44   0:00 tmux new-session -d -s eval_k07_zero_mask source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && CUDA_VISIBLE_DEVICES=1 python eval_success_rate_libero.py --checkpoint checkpoints/libero_acis_stage1only_k07/stage1_done/checkpoint.pt --config configs/libero_acis_stage1only_k07.yaml --suite libero_object --mode acis_prune --pruning-method zero_mask --num_episodes 50 --gpu 0 2>&1 | tee eval_results/eval_k07_zero_mask.log\\nroot     328499  0.0  0.0   4364  3308 pts/0    Ss+  17:44   0:00 bash -c source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && CUDA_VISIBLE_DEVICES=1 python eval_success_rate_libero.py --checkpoint checkpoints/libero_acis_stage1only_k07/stage1_done/checkpoint.pt --config configs/libero_acis_stage1only_k07.yaml --suite libero_object --mode acis_prune --pruning-method zero_mask --num_episodes 50 --gpu 0 2>&1 | tee eval_results/eval_k07_zero_mask.log\\nroot     328503  413  0.1 24707112 1336672 pts/0 Rl+ 17:44   0:20 python eval_success_rate_libero.py --checkpoint checkpoints/libero_acis_stage1only_k07/stage1_done/checkpoint.pt --config configs/libero_acis_stage1only_k07.yaml --suite libero_object --mode acis_prune --pruning-method zero_mask --num_episodes 50 --gpu 0\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.81}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_k07_zero_mask_20260517T094321",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-17T09:44:19.232010+00:00_

已启动，确认进程正在运行。

**汇报：**

| 项目 | 状态 |
|------|------|
| Checkpoint | ✓ `checkpoints/libero_acis_stage1only_k07/stage1_done/checkpoint.pt` (920MB) |
| Config | ✓ `configs/libero_acis_stage1only_k07.yaml` |
| tmux session | `eval_k07_zero_mask` |
| PID | 328503 |
| GPU | CUDA_VISIBLE_DEVICES=1 |
| 参数 | `--suite libero_object --mode acis_prune --pruning-method zero_mask --num_episodes 50` |
| 预计完成 | ~40 分钟（约 18:25） |
| 日志 | `eval_results/eval_k07_zero_mask.log` |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_eval_k07_zero_mask_20260517T094321"
}
```

</details>

---
