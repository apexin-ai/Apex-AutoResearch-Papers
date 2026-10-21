# code r7 k ablation optimal w

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_r7_k_ablation_optimal_w_20260518T051421_result.json`
- **Structured JSON:** [`f547783299d139413fa4.json`](../../sessions/f5/f547783299d139413fa4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。结果已保存到 `artifacts/exp_r7_k_ablation_optimal_w/results.json`。

以下是对比表：

## R1-8B (L14, W=15) vs W=1

| K | Precision | Bal_Acc | Coverage | Lead Time | Safe FPR |
|---|-----------|---------|----------|-----------|----------|
| | **W=15 / W=1** | **W=15 / W=1** | **W=15 / W=1** | **W=15 / W=1** | **W=15 / W=1** |
| 1 | 0.6727 / 0.6926 | 0.7531 / 0.7783 | 0.9535 / 1.0000 | 3.46 / 8.67 | 0.8644 / 1.0000 |
| 3 | — | — | 0.7674 / 0.7442 | -0.42 / 0.03 | 0.6949 / 0.8136 |
| 5 | — | — | 0.6047 / 0.4651 | -0.81 / -2.00 | 0.5932 / 0.6271 |
| 7 | — | — | 0.3953 / 0.3488 | 2.00 / -1.20 | 0.5085 / 0.3898 |
| 10 | — | — | 0.2326 / 0.1395 | 6.90 / -11.50 | 0.3559 / 0.2203 |

## OT-7B (L16, W=3) vs W=1

| K | Precision | Bal_Acc | Coverage | Lead Time | Safe FPR |
|---|-----------|---------|----------|-----------|----------|
| | **W=3 / W=1** | **W=3 / W=1** | **W=3 / W=1** | **W=3 / W=1** | **W=3 / W=1** |
| 1 | 0.4646 / 0.4250 | 0.6876 / 0.6795 | 1.0000 / 1.0000 | 26.32 / 30.57 | 0.8413 / 0.9206 |
| 3 | — | — | 0.7872 / 0.7872 | 11.03 / 9.22 | 0.3651 / 0.4127 |
| 5 | — | — | 0.5319 / 0.5106 | 6.12 / 3.00 | 0.3333 / 0.1905 |
| 7 | — | — | 0.3404 / 0.2979 | 4.25 / 7.14 | 0.2381 / 0.1587 |
| 10 | — | — | 0.2128 / 0.2128 | 7.30 / 4.40 | 0.1429 / 0.0794 |

## QwQ-32B (L60, W=3) vs W=1

| K | Precision | Bal_Acc | Coverage | Lead Time | Safe FPR |
|---|-----------|---------|----------|-----------|----------|
| | **W=3 / W=1** | **W=3 / W=1** | **W=3 / W=1** | **W=3 / W=1** | **W=3 / W=1** |
| 1 | 0.6515 / 0.6582 | 0.7332 / 0.7473 | 1.0000 / 1.0000 | 3.89 / 9.32 | 0.9750 / 1.0000 |
| 3 | — | — | 0.9474 / 0.9474 | 2.17 / 2.44 | 0.8000 / 0.7750 |
| 5 | — | — | 0.7895 / 0.7895 | -0.40 / 0.40 | 0.7250 / 0.6500 |
| 7 | — | — | 0.5263 / 0.5789 | -2.00 / -2.82 | 0.5000 / 0.3500 |
| 10 | — | — | 0.3158 / 0.3158 | -7.83 / -11.50 | 0.3750 / 0.2500 |

**要点**：
- R1-8B W=15 用了 SGDClassifier（因为 61440 维特征 LogisticRegression 太慢），step-level 性能略低于 W=1 的 LR，但 coverage 在高 K 值时更好
- OT-7B W=3 的 coverage 和 W=1 接近，Safe FPR 在低 K 值时更优（K=1: 0.84 vs 0.92）
- QwQ-32B W=3 和 W=1 趋势非常相似，Safe FPR 在高 K 值时稍高

---
