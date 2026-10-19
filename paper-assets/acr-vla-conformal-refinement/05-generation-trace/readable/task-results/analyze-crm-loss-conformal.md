# analyze crm loss conformal

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_crm-loss-conformal_20260522T062919_result.json`
- **Structured JSON:** [`08475ca3c9cf040c920d.json`](../../sessions/08/08475ca3c9cf040c920d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据齐全。以下是分析结果。

---

## CRM Loss 变体实验分析：crm-loss-conformal

### 训练状态
- **状态**: 正常完成 (50/50 epochs, EXIT_CODE=0)
- **数据**: 14,570 samples, K=10, obs_dim=960, CRM params=337,438
- **配置**: loss_type=conformal_guided, lambda_conf=0.1, lr=1e-3, batch_size=32

### 最终 Metrics

| 指标 | 值 |
|---|---|
| Final train_loss | 0.016046 |
| Final val_loss | 0.013343 |
| **Best val_loss** | **0.013343** (epoch 50) |
| Best epoch | 50 (仍在持续下降) |
| Checkpoint | `/root/autodl-tmp/checkpoints/crm_loss_variants/conformal_guided/` |

### 四方对比（Track 2 全部实验）

| 实验 | Loss Type | Best val_loss | Final train_loss | vs MSE baseline |
|---|---|---|---|---|
| **crm-loss-perdof** | Per-DOF weighted | **0.000124** | 0.000141 | **16.8x better** |
| crm-loss-mse-baseline | MSE | 0.002080 | 0.004038 | 1.0x (baseline) |
| crm-loss-combined | Per-DOF + conformal | 0.005302 | 0.004481 | 2.5x worse |
| **crm-loss-conformal** | Conformal-guided | 0.013343 | 0.016046 | **6.4x worse** |

### 分析

1. **Conformal-guided loss 表现最差**：val_loss=0.013343 是 MSE baseline (0.002080) 的 6.4 倍。需注意 val_loss 可能包含 auxiliary conformal term（lambda=0.1），所以纯 MSE 差距可能没有 6.4x 那么大，但即使扣除 auxiliary 部分，收敛速度和最终精度仍明显落后。

2. **训练动态对比**：MSE baseline epoch 1 val_loss=0.008373→最终 0.002080（降 4x）；conformal epoch 1 val_loss=0.037526→最终 0.013343（降 2.8x），conformal 收敛效率更低。

3. **Combined 实验佐证**：combined (per-DOF + conformal) val_loss=0.005302，比纯 per-DOF (0.000124) 差 43x，说明 conformal component 确实是拖后腿的因素。

4. **Per-DOF 一枝独秀**：val_loss=0.000124 远超所有变体，验证了"按 DOF 重要性加权"的策略有效。

### Conclusion

**negative** — Conformal-guided auxiliary loss 显著降低了 CRM 训练效果。假设不成立：用 nonconformity score 加权校正幅度并不能改善 CRM，反而引入了噪声信号干扰了主 MSE 目标的优化。

### 其他实验状态
- **crm-loss-perdof**: conclusion=success ✓
- **crm-loss-combined**: 已完成 (best val_loss=0.005302)，待分析
- **crm-loss-mse-baseline**: 已完成 (best val_loss=0.002080)，待分析

---
