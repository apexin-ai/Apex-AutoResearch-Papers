# ops eval tail1024 retry

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_eval_tail1024_retry_20260518T060709_result.json`
- **Structured JSON:** [`0ccaf97b4b00bc147996.json`](../../sessions/0c/0ccaf97b4b00bc147996.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**codellama13b_full_trace_tail1024_seed42_v2 eval 结果：**

| Metric | Value | 95% CI |
|---|---|---|
| **Accuracy** | **87.6%** | [85.6%, 89.3%] |
| Majority baseline | 71.5% | (always predict 'pass') |
| **Lift** | **+16.1pp** | [+14.1pp, +18.1pp] |
| n_test | 1190 | |

Per-class:

| Class | Precision | Recall | F1 |
|---|---|---|---|
| pass | 0.85 | **1.00** | 0.92 |
| fail | **1.00** | 0.56 | 0.72 |

模型对 pass 的 recall 为 1.0（从不漏判 pass），对 fail 的 precision 为 1.0（预测 fail 时从不误判），但 fail recall 只有 0.56（约 44% 的 fail 样本被误判为 pass）。eval_results.json 和 predictions.jsonl 已保存。

---
