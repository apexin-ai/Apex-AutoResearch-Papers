# analysis selection f1 table2

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_selection_f1_table2_20260515T152953_result.json`
- **Structured JSON:** [`6408867a8ee3f5671cbd.json`](../../sessions/64/6408867a8ee3f5671cbd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。完整结果 JSON 已保存到服务器 `output/review_round2/selection_f1_table2.json`。

## SciERC NER Selection F1 (N=8, T=1.0, Unified Pipeline)

| Method | seed42 F1 | seed123 F1 | Mean ± σ | ΔF1 vs Greedy | p-value |
|--------|-----------|------------|----------|---------------|---------|
| Greedy | 0.6439 | 0.6457 | 0.6448 ± 0.0013 | — | — |
| Random | 0.6077 | 0.6125 | 0.6101 ± 0.0034 | -3.5 pp | — |
| LP | 0.6501 | 0.6436 | 0.6468 ± 0.0046 | +0.2 pp | 0.289 |
| SJ | 0.6450 | 0.6475 | 0.6462 ± 0.0017 | +0.1 pp | 0.675 |
| EM | 0.6362 | 0.6381 | 0.6371 ± 0.0013 | -0.8 pp | 0.450 |
| VC | 0.6256 | 0.6204 | 0.6230 ± 0.0037 | -2.2 pp | 0.259 |
| FK | 0.6448 | 0.6468 | 0.6458 ± 0.0014 | +0.1 pp | 0.793 |
| Oracle | 0.7758 | 0.7805 | 0.7781 ± 0.0033 | +13.3 pp | — |

**关键发现：** 没有信号在 instance-level sign test 下显著优于 greedy（所有 p > 0.05）。大量 ties（~75-80% 实例 signal 选择和 greedy 给出相同 F1），导致有效比较样本量很小。LP 是最佳信号（+0.2 pp），但方差最大。Oracle 显示 +13.3 pp 的理论上限空间。

**验证点：** n_valid=529（551-22 gold-empty）✓，per_instance_f1 via evaluation.py ✓，FK/SJ via consistency.py ✓。p-value 用 Fisher's method 合并两个 seed 的 binomial sign test。

---
