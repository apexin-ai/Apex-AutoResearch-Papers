# setup phase2 stage2 auto trigger

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_setup_phase2_stage2_auto_trigger_20260527T190854_result.json`
- **Structured JSON:** [`535bb56a5175376f80cd.json`](../../sessions/53/535bb56a5175376f80cd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告：

| 项目 | 值 |
|------|-----|
| **Sentinel PID** | 872754 |
| **监控的 Stage 1 PID** | 856552 (step 7429/10000, ~3.3h 后完成) |
| **Stage 1 checkpoint** | `/root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/phase2_stage1_seed0_l005/10000` |
| **Stage 2 checkpoint dir** | `.../a1_sdf_pi05_object_pudding/a1_sdf_pi05_object_pudding_seed0_l0/` |
| **Stage 2 命令** | `python scripts/train_a1_sdf_aux_pi05.py --scene object_pudding --seed 0 --lambda_sdf 0 --gpu 1 --num_train_steps 30000 --resume` |
| **Stage 2 训练 log** | `/tmp/phase2_stage2_seed0.log` |
| **Sentinel log** | `/root/autodl-tmp/auto_stage2_sentinel.log` |

Sentinel 逻辑：
- 每 60s 检查 Stage 1 PID 存活
- Stage 1 退出后验证 `10000/model.safetensors` 存在（异常退出不启动 Stage 2）
- 将 10K checkpoint + wandb_id.txt + best 复制到 Stage 2 目录
- 启动 Stage 2（`WANDB_MODE=disabled`, cuda:1）

---
