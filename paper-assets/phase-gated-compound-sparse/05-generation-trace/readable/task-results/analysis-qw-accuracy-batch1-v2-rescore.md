# analysis qw accuracy batch1 v2 rescore

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_qw_accuracy_batch1_v2_rescore_20260516T002516_result.json`
- **Structured JSON:** [`329108461e679bc91676.json`](../../sessions/32/329108461e679bc91676.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

### v2 rescore 影响
**v2 matcher 对所有文件的评分结果零变化。** 对 batch1（dense/s015/s020/s025/s030）和 batch2（dense/s015/s030 的 `_n51_100` 文件）全部重新跑了 v2 answer matcher，0 个答案判定翻转。

注意：s020 batch2 的 `_n51_100` 原始文件（22/50=0.44）和 `_b2_fix` 文件（23/50=0.46）的差异不是 matcher 造成的——是 re-evaluation（重新生成）导致的。最终数字用 `_b2_fix`。

### 完整 QW accuracy dose curve (n=100)

| condition | batch1 (n=50) | batch2 (n=50) | combined (n=100) |
|-----------|--------------|--------------|-----------------|
| dense     | 16/50 = 0.32 | 24/50 = 0.48 | **40/100 = 0.40** |
| s015      | 17/50 = 0.34 | 19/50 = 0.38 | **36/100 = 0.36** |
| s020      | 13/50 = 0.26 | 23/50 = 0.46 | **36/100 = 0.36** |
| s025      | 16/50 = 0.32 | 17/50 = 0.34 | **33/100 = 0.33** |
| s030      |  7/50 = 0.14 | 12/50 = 0.24 | **19/100 = 0.19** |

### 单调性
Combined dose curve **非严格单调递减**：s015 和 s020 并列 0.36。从 s020 开始严格递减（0.36 → 0.33 → 0.19）。整体趋势是 non-increasing。

JSON 已保存到服务器 `analysis_output/qw_accuracy_dose_curve_final.json`。

---
