# ops exp021 check results

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_exp021-check-results_20260524T061107_result.json`
- **Structured JSON:** [`371ee423c56f7c2c4365.json`](../../sessions/37/371ee423c56f7c2c4365.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### exp_021 — 已完成 ✓
GPT-2-medium real-data control (r=1.0, seed 42, 3 generations)

| Gen | r_eff | PPL | D-4 | σ₁ | train_loss |
|-----|-------|-----|------|------|-----------|
| 0 | 23.09 | 15.45 | 0.913 | 6598.1 | — |
| 1 | 121.17 | 11.47 | 0.884 | 1454.9 | 2.560 |
| 2 | 113.30 | 11.30 | 0.870 | 1886.9 | 2.478 |
| 3 | 134.49 | 11.21 | 0.860 | 1688.8 | 2.432 |

关键发现：纯真实数据微调下 PPL **持续下降**（15.45→11.21），D-4 仅轻微下降（0.913→0.860），r_eff 从基线的 23 跳到 ~120 后**保持稳定**。没有崩溃。这与 exp_020 的纯合成数据条件形成鲜明对比。

无 HellaSwag、无 SLV 指标（实验脚本未计算）。

---

### exp_020 — 仍在运行
GPT-2-medium pure collapse (r=0.0, seed 42, 9 generations)，当前 **Gen 9 生成合成样本中 (4480/50000)**。

已完成 Gen 0-8 的结果：

| Gen | r_eff | PPL | D-4 | train_loss |
|-----|-------|-----|------|-----------|
| 0 | 23.09 | 15.45 | 0.913 | — |
| 1 | 155.22 | 16.42 | 0.891 | 2.358 |
| 2 | 185.37 | 18.94 | 0.868 | 2.119 |
| 3 | 184.86 | 23.33 | 0.837 | 2.052 |
| 4 | 169.56 | 32.11 | 0.764 | 1.993 |
| 5 | 151.94 | 49.35 | 0.658 | 1.913 |
| 6 | 136.09 | 76.81 | 0.559 | 1.821 |
| 7 | 121.29 | 123.66 | 0.501 | 1.740 |
| 8 | 110.92 | 198.01 | 0.460 | 1.706 |
| 9 | 进行中... | | | |

清晰的崩溃轨迹：PPL 从 15→198（12.8x 恶化），D-4 从 0.91→0.46。Gen 9 还需要完成样本生成（~45k 剩余）+ 训练 + 评估，预计 **1-2 小时**完成。

---
