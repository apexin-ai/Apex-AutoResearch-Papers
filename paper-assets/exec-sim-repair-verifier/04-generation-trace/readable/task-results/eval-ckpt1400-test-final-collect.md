# eval ckpt1400 test final collect

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_ckpt1400-test-final-collect_20260515T060842_result.json`
- **Structured JSON:** [`5655a98d03e02c02a5e2.json`](../../sessions/56/5655a98d03e02c02a5e2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。结果汇总：

## ckpt-1400 test@8192 结果

| 指标 | 值 |
|------|-----|
| **Accuracy** | **85.47%** |
| F1 macro | 78.90% |
| F1 fail | 67.13% |
| F1 pass | 90.67% |
| Precision fail | 86.43% |
| Recall fail | 54.88% |
| Precision pass | 85.27% |
| Recall pass | 96.81% |
| Majority baseline | 72.96% |
| Gap vs majority | +12.51pp |
| Unparseable | 0 |
| Total samples | 9,784 |

## 对比 & 状态

**ckpt-1400 是 test 最高 checkpoint**，超过 ckpt-400 (84.79%) +0.68pp。

| Checkpoint | Accuracy | F1 macro | F1 fail |
|-----------|----------|----------|---------|
| **ckpt-1400** | **85.47%** | **78.90%** | 67.13% |
| ckpt-400 | 84.79% | 81.18% | 72.93% |
| ckpt-800 | 83.53% | 78.97% | 69.17% |
| ckpt-1200 | 83.84% | 77.47% | 65.49% |
| ckpt-1000 | 83.52% | 77.50% | 65.85% |
| ckpt-600 | 79.05% | 75.12% | 65.24% |

注意：ckpt-1400 accuracy 最高但 F1 fail 只有 67.13%（recall_fail=54.9%），远低于 ckpt-400 的 72.93%。ckpt-400 在 F1 macro 和 F1 fail 上仍是最优。

**cuda:0 已释放**（0 MiB / 0% utilization）。

---
