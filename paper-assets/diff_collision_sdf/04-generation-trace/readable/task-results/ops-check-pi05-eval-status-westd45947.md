# ops check pi05 eval status westd45947

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_pi05_eval_status_westd45947_20260522T203620_result.json`
- **Structured JSON:** [`7b722924fdfe64ec9ba2.json`](../../sessions/7b/7b722924fdfe64ec9ba2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇总

### Pi0.5 Eval (libero_spatial, 50 episodes/task) — 仍在运行

**进度**: 9/10 tasks 完成，455/500 episodes，当前跑最后一个 task (episode ~6/50)。预计 ~5 分钟完成。

已完成 task-level 结果：

| Task | Name | TSR |
|------|------|-----|
| 0 | pick up the black bowl between the plate and the ramekin... | **100%** |
| 1 | pick up the black bowl next to the ramekin... | **98%** |
| 2 | pick up the black bowl from table center... | **100%** |
| 3 | pick up the black bowl on the cookie box... | **100%** |
| 4 | pick up the black bowl in the top drawer... | **98%** |
| 5 | pick up the black bowl on the ramekin... | **88%** |
| 6 | pick up the black bowl next to the cookie box... | **100%** |
| 7 | pick up the black bowl on the stove... | **100%** |
| 8 | pick up the black bowl next to the plate... | **100%** |
| 9 | pick up the black bowl on the wooden cabinet... | 进行中 |

**当前 Overall TSR: 98.2%** (445/453 successes)

### A3 Spatial Training (cuda:0) — 已完成

- 训练到 step 30000，final loss=0.02036，action_loss=0.01708
- Best checkpoint: step 30000, loss=0.01552
- Checkpoints 保存在 `/root/autodl-tmp/checkpoints/a3_grad_refine_spatial_bowl/a3_grad_refine_spatial_bowl_seed0/`（best, 29999, 30000）
- wandb offline run 需要 sync

建议等 ~5 分钟后再查一次 Pi0.5 完整结果。

---
