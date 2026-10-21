# code prep hsweep h5 config

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prep-hsweep-h5-config_20260518T163053_result.json`
- **Structured JSON:** [`f66c66a5afba29bd3cf7.json`](../../sessions/f6/f66c66a5afba29bd3cf7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GPU 已改为 `2,3`，其他参数确认正确。

## 结果汇总

**Config 文件**：`/root/autodl-tmp/cost-verify-agent-rl/RAGEN/config/_alfworld_hsweep_h5.yaml`（已存在，无需新建）

**关键参数确认**：
| 参数 | 值 |
|---|---|
| `step_independent_history_length` | **5** |
| `context_window_mode` | `step_independent` |
| `total_training_steps` | 15 |
| `CUDA_VISIBLE_DEVICES` | **2,3**（已从 0,1 修改） |
| `experiment_name` | `hsweep-h5`（launch script 会追加 seed → `hsweep-h5-seed1`） |
| `checkpoint_dir` | `/root/autodl-tmp/checkpoints/hsweep-h5/` |
| `model_path` | `qwen3_exp021_ragen_sft_v4` |

**与 h=2 的差异**（仅 3 处，符合预期）：
1. `step_independent_history_length`: 2 → **5**
2. `experiment_name`: `hsweep-h2` → `hsweep-h5`
3. `local_log_dir` / `default_local_dir`: `hsweep-h2/` → `hsweep-h5/`
4. `CUDA_VISIBLE_DEVICES`: `0,1` → `2,3`（额外修改，因 h=5 跑 GPU 2,3）

**Pre-flight (C002)**：
- 入口点：`train.py` via `launch_hsweep.sh`（与既有 h-sweep 一致）
- 磁盘：35G 可用（87%），15 步足够
- Checkpoint 路径：`qwen3_exp021_ragen_sft_v4/` 存在
- Config 参数：与 h=2 同结构，仅 h 值不同

**启动命令**（g100 kill 后执行）：
```bash
cd /root/cost-verify-agent-rl/scripts && bash launch_hsweep.sh 5 1
```

注意：launch script 里没有覆盖 `CUDA_VISIBLE_DEVICES`，所以它会用 config 里的 `2,3`。如果以后需要在 GPU 0,1 上跑 h=5，记得改回。

---
