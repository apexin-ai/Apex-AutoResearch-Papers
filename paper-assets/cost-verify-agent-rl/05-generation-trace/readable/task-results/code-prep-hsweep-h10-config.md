# code prep hsweep h10 config

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prep-hsweep-h10-config_20260518T163821_result.json`
- **Structured JSON:** [`5db2c3422a5e377ba334.json`](../../sessions/5d/5db2c3422a5e377ba334.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

无 hsweep checkpoint 目录，干净状态。

---

## 结果

**Config 路径**: `/root/cost-verify-agent-rl/RAGEN/config/_alfworld_hsweep_h10.yaml`
（autodl-tmp 副本已同步）

### 关键参数确认

| 参数 | 值 | 状态 |
|---|---|---|
| `step_independent_history_length` | 10 | OK |
| `CUDA_VISIBLE_DEVICES` | `"2,3"` | 已修改（原 "0,1"） |
| `total_training_steps` | 15 | OK |
| `experiment_name` | `hsweep-h10`（脚本覆盖为 `hsweep-h10-seed1`） | OK |
| `checkpoint_dir` | `/root/autodl-tmp/checkpoints/hsweep-h10/` | 无冲突 |
| `model_path` | `/root/autodl-tmp/checkpoints/qwen3_exp021_ragen_sft_v4` | 存在 |
| `val.env_groups` | 32 | 符合 C003 |
| seed | 由脚本注入 `seed.train=10000` | OK |

### 与 h=2 的差异

1. `step_independent_history_length`: 2 → **10**
2. `experiment_name`: hsweep-h2 → **hsweep-h10**
3. `local_log_dir` / `default_local_dir`: hsweep-h2 → **hsweep-h10**
4. `CUDA_VISIBLE_DEVICES`: "0,1" → **"2,3"**（h=2 仍为 0,1）

其余参数（model, lr, kl, gamma, rollout, algorithm, es_manager 等）完全一致。

### 启动命令（g100 kill 后执行）

```bash
cd /root/cost-verify-agent-rl/scripts && nohup bash launch_hsweep.sh 10 1 &
```

---
