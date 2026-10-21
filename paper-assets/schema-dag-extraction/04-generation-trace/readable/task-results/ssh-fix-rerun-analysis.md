# ssh fix rerun analysis

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_fix-rerun-analysis_20260515T023655_result.json`
- **Structured JSON:** [`abbc22eb9b1d3d43271c.json`](../../sessions/ab/abbc22eb9b1d3d43271c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部结果如下：

```
=== CLEAN DATA ANALYSIS (text_match reeval) ===

PRIMARY: r(recall, BCS)
  count_6:  r=0.2754, p=0.1644, n=27, verdict=FAIL
  count_12: r=0.2219, p=0.2660, n=27, verdict=FAIL
  partial:  r=0.2522, p=0.0658, n=54, verdict=FAIL

SECONDARY: r(F1, BCS)
  count_6:  r=0.1754, p=0.3814, n=27, verdict=FAIL
  count_12: r=0.5012, p=0.0077, n=27, verdict=PASS
  partial:  r=0.3025, p=0.0262, n=54, verdict=PASS

MECHANISTIC: confusion_rate (wrong_type/total_fp)
  count_6  high_bcs: 1.57%   low_bcs: 0.88%   ratio=1.7x
  count_12 high_bcs: 3.04%   low_bcs: 1.31%   ratio=2.4x

EXTREME BATCHES:
  count_6  high: 7.28%  low: 0.14%  ratio=27.5x
  count_12 high: 4.80%  low: 0.61%  ratio=9.9x
```

**D004 判定：**

| Criterion | Requirement | Result | Verdict |
|-----------|------------|--------|---------|
| Primary: r(recall, BCS) | \|r\|≥0.3, p<0.05 | 最高 r=0.275 (count_6), p=0.164 | **FAIL** |
| Secondary: r(F1, BCS) | — | count_12 r=0.501 p=0.008 PASS; partial r=0.303 p=0.026 PASS | mixed |
| Mechanistic: confusion_rate | high > low | 全部方向正确，极端 batch 27.5x | **PASS** |

**结论：** Primary criterion (recall vs BCS) 全部 FAIL — clean data 下 recall 与 BCS 的 correlation 方向正确（正相关）但效应量不足且不显著。F1 在 count_12 和 partial 上通过。Mechanistic 方向完全正确（high-BCS batch 产生更多 wrong_type 混淆）。

与之前错误数据对比：recall partial 从 r=0.252 变成 r=0.252（几乎不变），F1 count_12 从 r=0.501 变成 r=0.501（不变）— 说明 text_match 修正对 correlation pattern 影响极小，之前的结论方向没有翻转。

---
