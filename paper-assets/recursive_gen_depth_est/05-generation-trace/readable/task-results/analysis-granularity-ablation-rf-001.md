# analysis granularity ablation rf 001

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_granularity_ablation_rf_001_20260515T092808_result.json`
- **Structured JSON:** [`ee57089c8b54febde9e9.json`](../../sessions/ee/ee57089c8b54febde9e9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。Registry 已更新为 DONE/success，memory.md 追加了 3 条洞察（D019-D021）。

**结果摘要**：

| Granularity | Mean Acc (9 cells) | 趋势 |
|---|---|---|
| Binary (d0 vs rest) | 99.5% ± 0.4% | 近完美 |
| 4-class (d0-d3) | 78.3% ± 4.8% | — |
| 3-class (d1-d3, 无d0) | 72.1% ± 6.7% | < 4-class (by design) |
| 6-class (d0-d5, 仅Pythia nuc) | 62.9% | 最低 |

**两个假设均确认**：
- 含 d0 的设置下 accuracy 严格单调下降（binary > 4-class > 6-class）
- d0v1 AUC ≥ 0.997 across all cells，boundary dilution 集中在深层相邻 pair（d2v3 AUC 从 4-class 0.804 降至 6-class 0.689，-14.3%）

---
