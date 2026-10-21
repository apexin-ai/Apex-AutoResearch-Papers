# analysis train crm smolvla 3suite v1

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_train-crm-smolvla-3suite-v1_20260522T230913_result.json`
- **Structured JSON:** [`60bb59897c9fa79b069e.json`](../../sessions/60/60bb59897c9fa79b069e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据已收集。无 W&B run（日志中无 wandb URL），无 per-benchmark 独立指标（统一训练）。

## 训练结果汇总：`train-crm-smolvla-3suite-v1`

### Conclusion: **success**

### 基本信息
| 项目 | 值 |
|------|-----|
| 模型 | CRM (obs_only), 327,198 参数 |
| 数据 | 77,835 samples (object: 28,950 + spatial: 24,133 + goal: 24,752) |
| 训练配置 | 50 epochs, batch_size=32, lr=1e-3, cosine schedule |
| obs_dim | 960 (SmolVLA features) |
| 状态 | 50/50 epochs 完成, EXIT_CODE=0 |

### Loss 曲线
| Epoch | Train Loss | Val Loss | LR |
|-------|-----------|---------|-----|
| 1 | 0.02164 | 0.01213 | 9.99e-04 |
| 10 | 0.01491 | 0.00893 | 9.05e-04 |
| 20 | 0.01263 | 0.00746 | 6.55e-04 |
| 30 | 0.01097 | 0.00652 | 3.45e-04 |
| 40 | 0.00999 | 0.00600 | 9.55e-05 |
| **50** | **0.00969** | **0.00588** | 0 |

### Best Checkpoint
- **Best val_loss = 0.005878** (epoch 50, 最后一个 epoch)
- 训练最后 5 个 epoch 连续刷新 best（46→47→49→50），说明模型到最后仍在缓慢收敛

### Checkpoint 文件
```
/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/
  crm_best.pt          1.3M    ← 最佳模型
  checkpoint_epoch0046.pt  3.8M
  checkpoint_epoch0047.pt  3.8M
  checkpoint_epoch0048.pt  3.8M
  checkpoint_epoch0049.pt  3.8M
  checkpoint_epoch0050.pt  3.8M
```

### 分析

1. **收敛性**：良好。Train loss 从 0.0216 降至 0.0097（-55%），val loss 从 0.0121 降至 0.0059（-51%），最后几个 epoch 仍有微小改善。

2. **过拟合**：**无过拟合迹象**。Val loss (0.0059) 始终低于 train loss (0.0097)。这是因为训练使用了数据增强（aug_noise 0.02-0.1, aug_ratio=0.5），增强只作用于训练集，使训练更难。val/train loss 比值 ≈ 0.61，健康。

3. **局限**：日志未记录 per-benchmark（object/spatial/goal）独立指标，也无 W&B logging。后续评估需要单独跑 eval 脚本获取各 benchmark 的 conformal 覆盖率/set size 等指标。

---
