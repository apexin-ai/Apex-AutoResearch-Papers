# analyze train pi05 a1 obj s2 l01 high

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_train_pi05_a1_obj_s2_l01_high_20260528T005705_result.json`
- **Structured JSON:** [`275530f5e943fa60ebf8.json`](../../sessions/27/275530f5e943fa60ebf8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报如下：

---

## 训练完成确认

| 项目 | 值 |
|------|---|
| **Final step** | 30000/30000 (100%) |
| **Final loss** | 0.0104 (action=0.0069, sdf=0.0336, ee=0.0096) |
| **Best loss** | 0.0104 @ step 30000 |
| **Training time** | 33h51m |
| **Checkpoint** | `/root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/a1_sdf_pi05_object_pudding_seed2_l1/30000` |
| **EXIT_CODE** | 0 (正常退出) |

## W&B

训练命令使用了 `WANDB_MODE=disabled`，无在线 W&B 数据。本地 wandb_id: `w5enizos`（未同步）。

## Eval 状态

**Sentinel 自动触发成功。** Eval 已在 westd-45947 cuda:0 上运行（PID 568277），启动于 08:53 local / 00:53 UTC。

- 脚本：`auto_eval_s2.sh` → `eval_safelibero.py`
- 配置：safelibero_object, level II, 4 tasks x 50 episodes, seed=7
- 日志：`/root/autodl-tmp/eval_results/eval_sdf_s2_l1_30k_auto.log`
- 进度：Task 0 (orange_juice) Episode 10/50 已完成（截至检查时刻）
- **预计完成时间：~40-60min（约 09:40-10:00 UTC），在 DDL 12:00 UTC 前**

## Registry 已更新

- `train_pi05_a1_obj_s2_l01_high` → DONE (success)
- `eval_pi05_a1_30k_s2_l01_high` → RUNNING (自动创建)

---
