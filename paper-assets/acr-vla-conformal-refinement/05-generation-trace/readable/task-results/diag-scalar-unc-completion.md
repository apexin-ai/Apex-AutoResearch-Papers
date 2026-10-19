# diag scalar unc completion

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_scalar-unc-completion_20260514T022012_result.json`
- **Structured JSON:** [`9dc2c1c99eaf9888120a.json`](../../sessions/9d/9dc2c1c99eaf9888120a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**crm-train-a4-scalar-unc 训练成功完成。** Registry 已更新为 DONE/success。

结果汇总：

| 指标 | 值 |
|------|-----|
| best_val_loss | **0.008379** (epoch 48) |
| final_val_loss | 0.008384 (epoch 50) |
| total_epochs | 50/50 |
| checkpoint | `/root/autodl-tmp/checkpoints/crm/scalar_unc/crm_best.pt` |

Ablation 对比：

| 模型 | val_loss | 说明 |
|------|----------|------|
| full CRM (40D per-DOF) | 0.009046 | baseline |
| **scalar_unc (3D)** | **0.008379** | 比 full CRM 更低 |
| obs_only (无 uncertainty) | 0.018312 | 无不确定性 |

意外发现：scalar_unc (0.008379) 比 full CRM (0.009046) val_loss 更低，差异约 7.4%。这与原假设（scalar 应比 per-DOF 差）相反——3D scalar uncertainty 在这个设置下反而略优于 40D per-DOF uncertainty，可能说明 40D 输入存在过参数化/噪声放大问题。

---
