# analysis cwm8b seed123

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_cwm8b-seed123_20260512T110030_result.json`
- **Structured JSON:** [`132a497245ebf74082e0.json`](../../sessions/13/132a497245ebf74082e0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**结论: SUCCESS** — seed123 成功复现 seed42 结果。

关键数据：

| 指标 | seed123 | seed42 | 差值 |
|------|---------|--------|------|
| accuracy | 86.98% | 87.67% | -0.69pp |
| pass_f1 | 86.83% | 87.57% | -0.74pp |
| fail_f1 | 87.13% | 87.77% | -0.64pp |
| exact_match | 84.13% | 84.39% | -0.26pp |

所有指标差异 <1pp，属于正常 seed 方差。CWM vs CLS 的 ~3.5pp gap 在两个 seed 下均稳定存在。训练正常完成（3 epoch, EXIT_CODE=0），checkpoint 完整。

分析已写入 `artifacts/cwm8b_seed123_analysis.txt`。

---
