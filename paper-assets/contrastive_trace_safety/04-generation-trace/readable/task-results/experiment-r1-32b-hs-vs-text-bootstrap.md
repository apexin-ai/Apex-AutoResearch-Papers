# experiment r1 32b hs vs text bootstrap

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_r1_32b_hs_vs_text_bootstrap_20260517T030501_result.json`
- **Structured JSON:** [`baa42360a9c2815a2f6b.json`](../../sessions/ba/baa42360a9c2815a2f6b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果完整。汇总如下：

---

**R1-32B HS vs Text Paired Bootstrap (n=1000, layer=10, W=10):**

| Metric | HS | Text | Δ | p-value | Bonferroni α=0.017 |
|--------|-----|------|---|---------|-------------------|
| Balanced Accuracy | 79.4% | 71.1% | +8.4pp | 0.040 | FAIL |
| Precision | 61.0% | 51.6% | +9.4pp | 0.025 | FAIL |
| Pre-CP FPR | 24.2% | 32.6% | -8.4pp | 0.057 | FAIL |

所有三个指标在 Bonferroni 校正后均未达到显著性（α=0.017）。但在未校正 α=0.05 下，balanced accuracy (p=0.040) 和 precision (p=0.025) 显著。

主要限制：test split 仅 20 条 traces，统计功效不足。效应量方向一致且幅度较大（8-9pp），样本量不够检测到 Bonferroni 级别显著性。

结果已保存至 `artifacts/r1_32b_paired_bootstrap/results.json`。

---
