# analyze crm loss perdof

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_crm-loss-perdof_20260522T062411_result.json`
- **Structured JSON:** [`9d2e8b1a1b44a833e863.json`](../../sessions/9d/9d2e8b1a1b44a833e863.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。以下是分析报告：

---

## `crm-loss-perdof` 实验分析报告

### 训练状态
- **状态**: 正常完成 (50/50 epochs, EXIT_CODE=0)
- **收敛**: val_loss 每个 epoch 持续下降，至最后一个 epoch 仍在改善

### 关键指标
| 指标 | 值 |
|------|-----|
| Best val_loss | **0.000124** (epoch 50) |
| Final train_loss | 0.000141 |
| DOF 权重范围 | 0.0107 – 3.7318 (~350x) |
| 数据量 | 14,570 samples |
| 模型参数 | 337,438 |
| Checkpoint | `/root/autodl-tmp/checkpoints/crm_loss_variants/perdof_weighted/crm_best.pt` |

### 四变体 val_loss 对比
| Loss Type | val_loss | 状态 |
|-----------|----------|------|
| **perdof_weighted** | **0.000124** | 完成 |
| mse (baseline) | 0.002080 | 完成 |
| combined | 0.005302 | 运行中 (epoch 48) |
| conformal_guided | 0.013343 | 完成 |

### 重要注意
**loss 值不可直接跨变体比较。** perdof_weighted 使用逆方差加权（rotation/gripper 权重高达 3.73x，translation 低至 0.01x），这从根本上改变了 loss 的尺度。数值上的 16.8x 差异部分来自加权本身对 loss scale 的压缩。

### 结论: **success**（训练层面）
训练正常收敛，per-DOF 加权机制按预期工作——高精度 DOF（旋转/夹爪）获得更多优化权重。最终是否优于 uniform MSE 需要 **downstream robot evaluation（success rate）** 做决定性比较。

---
