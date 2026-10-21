# eval collect cls func s123 results

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_collect-cls-func-s123-results_20260516T111459_result.json`
- **Structured JSON:** [`30552e00fc65b9f34436.json`](../../sessions/30/30552e00fc65b9f34436.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## DeepSeek CLS func seed123 Eval 结果

| Metric | seed123 | seed42 | Δ |
|--------|---------|--------|---|
| Accuracy | **86.77%** | 86.93% | -0.16pp |
| F1 macro | **86.77%** | 86.92% | -0.15pp |
| Precision (fail) | 85.0% | 86.4% | -1.4pp |
| Precision (pass) | 88.6% | 87.4% | +1.2pp |
| Recall (fail) | 88.2% | 86.5% | +1.7pp |
| Recall (pass) | 85.5% | 87.3% | -1.8pp |

两个 seed 的 accuracy/F1 差异 <0.2pp，性能高度一致。seed123 偏向预测 fail（recall_fail 高、recall_pass 低），seed42 更均衡。Unparseable = 0。

---
