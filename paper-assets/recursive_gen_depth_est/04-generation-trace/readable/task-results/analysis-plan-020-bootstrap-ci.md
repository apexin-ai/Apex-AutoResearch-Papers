# analysis plan 020 bootstrap ci

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_plan_020_bootstrap_ci_20260522T093949_result.json`
- **Structured JSON:** [`4d96d044def9e47fe8ad.json`](../../sessions/4d/4d96d044def9e47fe8ad.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

B=10000 bootstrap CI 已完成，结果保存到 `results/bootstrap_ci_table1.json`。

汇总对比：

| Cell | Acc% | 95% CI (B=10k) | ±(B=10k) | ±(B=1k) | Δ |
|------|------|----------------|----------|---------|---|
| pythia_nucleus | 78.7 | [78.15, 79.21] | ±0.53 | ±0.6 | -0.07 |
| pythia_temp09 | 76.7 | [76.20, 77.28] | ±0.54 | ±0.6 | -0.06 |
| pythia_topk50 | 68.8 | [68.24, 69.42] | ±0.59 | ±0.6 | -0.01 |
| olmo_nucleus | 78.9 | [78.39, 79.45] | ±0.53 | ±0.6 | -0.07 |
| olmo_temp09 | 82.1 | [81.61, 82.62] | ±0.50 | ±0.5 | +0.00 |
| olmo_topk50 | 74.5 | [73.95, 75.04] | ±0.54 | ±0.6 | -0.06 |
| gpt2xl_nucleus | 84.1 | [83.61, 84.61] | ±0.50 | ±0.5 | +0.00 |
| gpt2xl_temp09 | 85.9 | [85.40, 86.32] | ±0.46 | ±0.4 | +0.06 |
| gpt2xl_topk50 | 75.9 | [75.39, 76.49] | ±0.55 | ±0.6 | -0.05 |

B=10000 vs B=1000 的 CI half-width 差异极小（|Δ| ≤ 0.07），说明 B=1000 时 CI 已经收敛。论文中可直接更新为 B=10000 的值，CI 范围 ±0.46 ~ ±0.59。完整数据含 LR accuracy CI 和 pairwise AUC CI 在 `artifacts/bootstrap_ci_table1.json`。

---
