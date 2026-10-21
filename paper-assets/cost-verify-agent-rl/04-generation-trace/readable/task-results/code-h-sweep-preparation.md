# code h sweep preparation

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_h_sweep_preparation_20260517T031717_result.json`
- **Structured JSON:** [`451813cb62d91152f8e7.json`](../../sessions/45/451813cb62d91152f8e7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

h-sweep 实验的 launch 脚本和配置文件**已全部就绪**，无需新建。

## 现有文件清单

| 文件 | 用途 |
|------|------|
| `RAGEN/config/_alfworld_hsweep_h2.yaml` | h=2, step_independent |
| `RAGEN/config/_alfworld_hsweep_h5.yaml` | h=5, step_independent |
| `RAGEN/config/_alfworld_hsweep_h10.yaml` | h=10, step_independent |
| `RAGEN/config/_alfworld_hsweep_h20.yaml` | h=20, step_independent |
| `RAGEN/config/_alfworld_hsweep_full.yaml` | h=full (episode-level baseline) |
| `scripts/launch_hsweep.sh` | Launch 脚本 |

## 配置核心参数确认

- `total_training_steps: 15`
- `test_freq: 5`, `save_freq: 5`
- `val_before_train: True`（step 0 有 val）
- `model_path`: `/root/autodl-tmp/checkpoints/qwen3_exp021_ragen_sft_v4`（与 exp029 同起点）
- `es_manager.val.env_groups: 32`（32 episodes eval，满足 C003 ≥16 要求）
- Hydra override 通过 `seed.train` 和 `trainer.experiment_name` 传入

## 使用方式

```bash
# 跑 h=5, seed=1
bash /root/cost-verify-agent-rl/scripts/launch_hsweep.sh 5 1

# 跑 h=full, seed=3
bash /root/cost-verify-agent-rl/scripts/launch_hsweep.sh full 3
```

脚本会自动设置 `TRAIN_SEED = seed * 10000`，W&B run name 为 `hsweep-h{H_VALUE}-seed{SEED}`，checkpoint 存储在 `/root/autodl-tmp/checkpoints/hsweep-h{H_VALUE}/`。

## 唯一需要注意的点

launch 脚本当前 seed 范围验证是 1-5（`if [ "$SEED" -lt 1 ] || [ "$SEED" -gt 5 ]`），任务要求 3 seeds × 5 h-values = 15 runs，用 seed 1/2/3 即可，无需修改脚本。

脚本语法检查通过（`bash -n` OK），参数验证正常（无参数/非法参数均正确报错）。可以在 exp029 结束后直接依次启动。

---
