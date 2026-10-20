# eval collect traj s42 results

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_collect-traj-s42-results_20260516T130320_result.json`
- **Structured JSON:** [`7c8b79dfac062fc92f1c.json`](../../sessions/7c/7c8b79dfac062fc92f1c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果如下：

| 指标 | 值 |
|------|-----|
| **Accuracy** | **83.14%** |
| n_samples | 1032 |
| Precision (resolved) | 89.00% |
| Recall (resolved) | 72.65% |
| F1 (resolved) | 80.00% |
| Precision (unresolved) | 79.56% |
| Recall (unresolved) | 92.22% |
| F1 (unresolved) | 85.43% |
| Unparseable | 8 (0.78%) |
| Per-test consistency | 77.42% |

对比：CLS 86.85%、CWM 86.83%，**Traj 83.14% 低了约 3.7pp**。模型倾向于预测 unresolved（recall 92.2%），对 resolved 的 recall 偏低（72.65%）。

---
