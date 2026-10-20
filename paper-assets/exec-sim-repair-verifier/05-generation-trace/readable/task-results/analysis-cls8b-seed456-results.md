# analysis cls8b seed456 results

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_cls8b-seed456-results_20260512T152754_result.json`
- **Structured JSON:** [`be25eea3c469d30b2986.json`](../../sessions/be/be25eea3c469d30b2986.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。

## cls8b-seed456 完整 metrics

| Metric | Value |
|--------|-------|
| overall_accuracy | **88.31** |
| pass_f1 | 88.20 |
| fail_f1 | 88.41 |
| pass_precision | 92.29 |
| pass_recall | 84.46 |
| fail_precision | 84.72 |
| fail_recall | 92.43 |
| train_loss | 0.3105 |
| eval_loss | 0.0928 |
| unparseable | 0 |
| test_set_size | 1890 |

注：eval json 中无 exact_match_rate 字段。

## cls8b vs cwm8b seed456 对比

| Metric | cls8b | cwm8b | Δ |
|--------|-------|-------|---|
| overall_accuracy | 88.31 | 86.24 | **+2.07pp** |
| pass_f1 | 88.20 | 85.96 | +2.24pp |
| fail_f1 | 88.41 | 86.51 | +1.90pp |

## 3 matched 8B pairs 汇总

| Seed | CLS acc | CWM acc | Gap |
|------|---------|---------|-----|
| 42 | 89.52 | 86.72 | +2.81pp |
| 123 | 88.89 | 86.47 | +2.42pp |
| 456 | 88.31 | 86.24 | +2.07pp |
| **Mean** | **88.91** | **86.48** | **+2.43pp** |

CLS 在全部 3 个 seed 上一致优于 CWM，gap 范围 +2.07 ~ +2.81pp，均值 +2.43pp。趋势稳定，seed456 gap 最小但方向一致。

---
