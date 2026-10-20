# analysis gpqa ds importance s015

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_gpqa_ds_importance_s015_20260516T201020_result.json`
- **Structured JSON:** [`7d38823322adbe84e3a2.json`](../../sessions/7d/7d38823322adbe84e3a2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。

## 结果

**Conclusion: SUCCESS**

| Phase Segment | II Median (s=0.15) | 95% CI |
|---|---|---|
| high_sparsity | 0.0128 | [0.0115, 0.0139] |
| mid_sparsity | 0.1024 | [0.0927, 0.1151] |
| low_sparsity | 0.9602 | [0.8929, 1.0331] |

关键发现：
- 3-segment quantile phase decomposition 在 GPQA Diamond 上有效分层，severity 呈严格单调递减（low > mid > high，75x ratio）
- 所有相邻段 95% CI 无重叠，统计显著
- 198 题全部正常处理，无 error，12.4h 完成
- Verdict: PASS

Registry 已更新为 DONE/success，分析报告已注册为 artifact。

---
