# ssh dcol midtraining check

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_dcol_midtraining_check_20260514T223230_result.json`
- **Structured JSON:** [`bf296016dda5546496e5.json`](../../sessions/bf/bf296016dda5546496e5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## DCOL 训练中期检查结果

### 进度
- **当前**: Epoch 6/10, step 280/2187
- **已运行**: 2h13m
- **进程状态**: PID 193684 正常运行

### GPU 状态
| GPU | 利用率 | 显存 |
|-----|--------|------|
| cuda:0 | 100% | 58.7G / 95.6G |
| cuda:1 | 58% | 9.7G / 95.6G |

### Epoch 级 Loss/Acc 趋势

| Epoch | Train Loss | Train Acc | Val Loss | Val Acc | Val MAE | 耗时 |
|-------|-----------|-----------|----------|---------|---------|------|
| 1 | 1.5623 | 0.2929 | 1.3186 | 0.4217 | 1.0767 | 28m |
| 2 | 1.4057 | 0.3063 | 1.2982 | 0.4308 | 1.0601 | 25m |
| 3 | 1.3523 | 0.3121 | 1.2752 | 0.4325 | 1.0573 | 25m |
| 4 | 1.3345 | 0.3122 | 1.2711 | 0.4305 | 1.0605 | 25m |
| 5 | 1.3227 | 0.3170 | **1.2659** | **0.4347** | **1.0547** | 26m |
| 6 | (训练中) step 280/2187, loss≈1.323 | | | | | |

### 判断

- **趋势**: Loss 持续下降，val_acc 持续改善（0.4217→0.4347），无异常震荡或 NaN
- **收敛信号**: Epoch 3-5 改善速度明显放缓，train loss 从 1.56→1.32 的大幅下降已趋平，后续 epoch 边际收益递减
- **Epoch 4 轻微回退**: val_acc 0.4325→0.4305，但 Epoch 5 恢复并创新高，属正常波动
- **Checkpoint**: best_model.pt 于 Epoch 5 结束时保存（val_acc=0.4347）
- **预计剩余时间**: 还剩 ~4.4 个 epoch（Epoch 6 剩 87% + Epoch 7-10），约 **1h50m**
- **无异常**: contrastive loss (cl) 稳定下降 0.033→0.027，lr 按计划衰减

---
