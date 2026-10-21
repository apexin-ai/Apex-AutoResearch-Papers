# analysis no trace seed42 v4

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_no_trace_seed42_v4_20260514T223531_result.json`
- **Structured JSON:** [`a7c56664ecb06b5ac770.json`](../../sessions/a7/a7c56664ecb06b5ac770.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。汇总如下：

## no_trace_seed42_v4 结果

| 指标 | 值 | v3 对比 |
|---|---|---|
| **Accuracy** | 75.1% (95% CI: 72.8%–77.5%) | 75.1% ✓ 一致 |
| **Majority baseline** | 71.5% | 同 |
| **Lift** | +3.6pp (95% CI: +0.4pp–+7.1pp) | +3.6pp ✓ 一致 |
| train_loss | 0.1800 | 0.18 |
| eval_loss | 0.6454 | 0.645 |
| eval_mean_token_accuracy | 0.8897 | 0.89 |

**Per-class:**

| | Precision | Recall | F1 |
|---|---|---|---|
| pass | 0.88 | 0.76 | 0.81 |
| fail | 0.55 | 0.73 | 0.63 |

**Checkpoint:** `/root/autodl-tmp/trace-verdict-study-checkpoints/no_trace/final/`

v4 结果与 v3 完全一致——符合预期，因为 no_trace 条件下 label 只有 "pass"/"fail" 单词，不会被截断，所以 v4 的 label 截断修复对此条件无影响。Baseline 正常建立，lift 统计显著（CI 下界 +0.4pp > 0）。

---
