# diagnose mvp pilot v4 loss

**collapse aware mixing** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_mvp_pilot_v4_loss_20260512T151829_result.json`
- **Structured JSON:** [`1db9178150329502b699.json`](../../sessions/1d/1db9178150329502b699.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

进程已终止。

---

## 诊断结论：**确认发散，训练已杀**

### 1. Loss 趋势（完整 12 个数据点）

| Step | Loss | 备注 |
|------|------|------|
| 50 | **4.36** | 正常 |
| 100 | 35.12 | 爆炸开始 |
| 150 | 45.27 | |
| 200 | 60.80 | grad_norm=113 |
| 250 | 137.07 | |
| 300-600 | 104-150 | 在高位震荡，无收敛趋势 |

### 2. 独立 PPL 评估（checkpoint-152, 50 holdout 序列）
- **Avg loss: 45.96** — 随机基线 (10.83) 的 4.2×
- **PPL: 9.16 × 10¹⁹**
- 每条序列 loss 均在 40-53，无异常值，全面崩溃

### 3. 判定：**发散（Diverging）**
- 训练进程 PID 28471 已 kill，确认终止
- 发散发生在 step 50→100 之间，LR warmup 到 peak (~1e-5) 时触发
- 可能原因：LR 过高或 warmup 太短导致梯度爆炸（step 200 grad_norm 达到 113）

---
