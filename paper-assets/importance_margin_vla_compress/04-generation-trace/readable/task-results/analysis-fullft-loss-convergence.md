# analysis fullft loss convergence

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_fullft_loss_convergence_20260518T115159_result.json`
- **Structured JSON:** [`c2ee5b3f8e69c6ab3de0.json`](../../sessions/c2/c2ee5b3f8e69c6ab3de0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据已全部收集完毕。

## libero_full_ft baseline 收敛分析

### Train Loss（每步瞬时值，噪声大）

| Step | Train Loss | LR |
|------|-----------|-----|
| 50K | 0.0594 | 5.20e-05 |
| 60K | 0.0271 | 3.68e-05 |
| 70K | 0.0675 | 2.30e-05 |
| 80K | 0.0241 | 1.20e-05 |
| 85K | 0.0158 | 7.92e-06 |
| 90K | 0.0394 | 4.93e-06 |
| 95K | 0.0858 | 3.11e-06 |
| 100K | 0.0408 | 2.50e-06 |

### Eval Loss（每 5K 步评估）

| Step | Eval Loss |
|------|-----------|
| 45K | 0.0579 |
| 50K | 0.0746 |
| 55K | 0.0837 |
| 60K | 0.0959 |
| 65K | 0.0648 |
| 70K | 0.0612 |
| 75K | 0.0607 |
| **80K** | **0.0874** |
| **85K** | **0.0676** |
| **90K** | **0.0591** |
| **95K** | **0.0781** |
| **final** | **0.0781** |

### 判断：**已收敛**

1. **Train loss plateau**: wandb sparkline尾部为 `▂▁▁▂`，已完全走平。80K-100K 区间的瞬时值在 0.02-0.09 波动，无下降趋势。

2. **Eval loss plateau**: 从 step 45K（0.0579）到 100K（0.0781），eval loss 一直在 0.057-0.096 区间内无方向性波动。
   - 60K-80K 均值：~0.074
   - 80K-100K 均值：~0.073
   - 两个窗口几乎一致，无改善。

3. **无 overfitting 迹象**: eval loss 没有上升趋势，只是随机波动（eval set 较小导致方差大）。

4. **LR 已衰减到底**: cosine schedule 从 1e-4 衰减到 2.5e-6，LR 空间已耗尽。

**结论：44.8% baseline 是在充分训练后的结果，不存在因训练不足导致 baseline 偏弱的问题。** 后续实验解读中可以放心引用这个 baseline。

---
