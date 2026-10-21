# ops fix cls func s123 metrics

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fix-cls-func-s123-metrics_20260516T120802_result.json`
- **Structured JSON:** [`17e2ee0617470c0b27d2.json`](../../sessions/17/17e2ee0617470c0b27d2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成。`deepseek-cls-func-s123` metrics 已写入：

| 指标 | 值 |
|------|-----|
| test_accuracy | 86.77% |
| test_f1_macro | 86.77% |
| test_precision_fail | 84.99% |
| test_precision_pass | 88.56% |
| test_recall_fail | 88.16% |
| test_recall_pass | 85.48% |
| test_unparseable_rate | 0 |
| test_n | 1890 |
| best_eval_loss | 0.06753 |
| train_time_seconds | 5391 (从 checkpoint 时间戳估算) |

与预期一致（86.77% vs 预期 ~86.77%）。两个 seed 的均值：(86.93 + 86.77) / 2 = 86.85%，符合 ROADMAP 中 86.85±0.11% 的描述。

---
