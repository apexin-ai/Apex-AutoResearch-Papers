# ops fetch qwen7b complete metrics

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fetch-qwen7b-complete-metrics_20260519T121502_result.json`
- **Structured JSON:** [`43a928fd14068847ed0f.json`](../../sessions/43/43a928fd14068847ed0f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。完整 metrics 如下：

## exp_code_qwen7b 完整结果 (K\* = 2)

### Pairwise AUC (5-fold CV)

| Pair | AUC | 95% CI | Folds |
|------|-----|--------|-------|
| 0v1 | 0.9051 | ±0.0043 | 0.9073, 0.9012, 0.9120, 0.9049, 0.9003 |
| 1v2 | 0.7276 | ±0.0055 | 0.7377, 0.7254, 0.7240, 0.7220, 0.7289 |
| 2v3 | 0.5368 | ±0.0145 | 0.5179, 0.5332, 0.5275, 0.5462, 0.5593 |
| 3v4 | 0.5090 | ±0.0055 | 0.5029, 0.5054, 0.5085, 0.5092, 0.5191 |
| 4v5 | 0.5139 | ±0.0128 | 0.5016, 0.5317, 0.5264, 0.5090, 0.5007 |

### Pairwise JSD

| Pair | JSD |
|------|-----|
| 0v1 | 0.061265 |
| 1v2 | 0.042256 |
| 2v3 | 0.004130 |
| 3v4 | 0.003198 |
| 4v5 | 0.003393 |

### Ordinal Classification (6-class)
- MAE = 1.2651
- Accuracy = 0.3423

### Top-10 Features
1. freq_entropy (9730.0)
2. surp_d2_mean (9236.2)
3. surp_d1_mean (9126.2)
4. surp_d1_skew (8833.4)
5. surp_std (8110.2)
6. freq_kurtosis (7838.6)
7. surp_mean (7586.0)
8. surp_kurt (6769.2)
9. hapax_ratio (6636.4)
10. ttr (6332.6)

Registry 已更新：conclusion=success, metrics 已录入完整数据。

---
