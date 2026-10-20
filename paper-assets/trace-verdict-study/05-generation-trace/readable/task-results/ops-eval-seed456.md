# ops eval seed456

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_eval-seed456_20260522T161749_result.json`
- **Structured JSON:** [`d07c1228238e1e293647.json`](../../sessions/d0/d07c1228238e1e293647.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

评估完成。seed456 结果：

| 指标 | seed456 | seed42 | seed123 |
|------|---------|--------|---------|
| **Accuracy** | **99.33%** | 98.99% | 99.33% |
| Pass P / R / F1 | 1.00 / 0.99 / 1.00 | — | — |
| Fail P / R / F1 | 0.98 / 1.00 / 0.99 | — | — |
| n_test | 1190 | — | — |

seed456 accuracy = 99.33%，与 seed123 持平，高于 seed42 (98.99%)。三个 seed 均值约 99.22%，方差极小，gradient_masking 方法稳定性良好。

---
