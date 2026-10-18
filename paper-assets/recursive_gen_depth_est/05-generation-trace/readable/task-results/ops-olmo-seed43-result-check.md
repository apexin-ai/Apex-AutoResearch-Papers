# ops olmo seed43 result check

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_olmo_seed43_result_check_20260518T173047_result.json`
- **Structured JSON:** [`3dd3e2fe9f5592396a64.json`](../../sessions/3d/3dd3e2fe9f5592396a64.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`olmo_seed43_001` 已完成，全部 8 步执行完毕（pipeline.log 最后一行 `=== Pipeline complete ===`）。

## 结果汇总

| 指标 | 值 |
|---|---|
| **4-class accuracy** | **82.11%** (95% CI: 81.77–82.54%) |
| baseline accuracy | 78.2% |
| **delta vs baseline** | **+3.91pp** |
| d1 vs d2 AUC | 0.9089 |

### Per-class recall

| Class | Recall |
|---|---|
| d0 (human) | 99.6% |
| d1 | 87.8% |
| d2 | 63.7% |
| d3 | 77.4% |

### 5-fold CV

Fold accuracies: 82.0%, 82.2%, 81.6%, 83.0%, 81.9% — 方差很小，结果稳定。

### Top 5 features

1. `p90_ppl`
2. `var_surprisal`
3. `p75_ppl`
4. `mean_surprisal`
5. `mean_ppl`

d2 recall 偏低 (63.7%) 是主要瓶颈，d0 和 d1 区分很好。跟之前其他 seed 的 pattern 一致：perplexity 分位数和 surprisal 方差是最强特征。

---
