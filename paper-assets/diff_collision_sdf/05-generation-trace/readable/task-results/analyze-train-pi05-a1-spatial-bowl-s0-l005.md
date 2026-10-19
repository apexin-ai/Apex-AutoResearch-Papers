# analyze train pi05 a1 spatial bowl s0 l005

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_train_pi05_a1_spatial_bowl_s0_l005_20260526T223049_result.json`
- **Structured JSON:** [`045fa20765b154f03e33.json`](../../sessions/04/045fa20765b154f03e33.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练结果汇总：

| 项目 | 值 |
|------|-----|
| **completion** | ✅ 完成全部 30K 步 |
| **final_step** | 30000 |
| **final_loss (total)** | 0.0137 (wandb summary: 0.01585) |
| **final_action_loss** | 0.0135 (wandb summary: 0.01562) |
| **final_sdf_loss** | 0.0327 (wandb summary: 0.03258) |
| **final_ee_loss** | 0.0068 (wandb summary: 0.00603) |
| **best_loss** | 0.01063 @ step 28000 |
| **lambda_sdf** | 0.005 ✅ 正确应用，全程恒定 |
| **checkpoint_path** | `/root/autodl-tmp/checkpoints/a1_sdf_pi05_spatial_bowl/a1_sdf_pi05_spatial_bowl_seed0_l005/30000/` (7.2GB) |
| **保留的 checkpoints** | 29999, 30000, best (step 28000) |
| **log_path** | `~/runs/diff_collision_sdf/train_pi05_a1_spatial_bowl_s0_l005.log` |
| **wandb offline run** | `/root/colliforce-vla/wandb/offline-run-20260526_020142-bwvsek6c/` (21MB) |
| **总训练时长** | ~28h26m (从 resume 起算), ~4.65s/it |
| **EXIT_CODE** | 0 |
| **conclusion** | **success** — 训练正常完成，30K 步全部跑完，loss 曲线单调下降，无异常 |

值得注意：
- checkpoint 保留策略自动清理了旧 checkpoint（26000、28000 被删除），仅保留 29999、30000 和 best
- best checkpoint 出现在 step 28000（loss=0.01063），最终 step 30000 的 loss 略高（0.01585），属于正常波动
- eikonal loss 收敛到极小值 (1e-05)，SDF 正则化正常工作

---
