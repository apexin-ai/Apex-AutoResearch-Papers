# ops check tail experiments

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_tail_experiments_20260517T073420_result.json`
- **Structured JSON:** [`adf417eae33fdce37099.json`](../../sessions/ad/adf417eae33fdce37099.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验均已**训练完成 + eval 完成**。

## 状态报告

| 指标 | full_trace_tail (2048) | full_trace_tail_512 |
|---|---|---|
| **状态** | 完成 | 完成 |
| **Accuracy** | **97.3%** [96.4%, 98.2%] | **93.6%** [92.2%, 95.0%] |
| Majority baseline | 71.5% | 71.5% |
| Lift | +25.8pp | +22.1pp |
| Pass P / R / F1 | 0.98 / 0.99 / 0.98 | 0.98 / 0.93 / 0.95 |
| Fail P / R / F1 | 0.97 / 0.94 / 0.95 | 0.85 / 0.94 / 0.89 |
| 测试样本 | 1190 | 1190 |

关键发现：
- tail-2048 比 tail-512 高 **3.7pp** accuracy（97.3% vs 93.6%），CI 无重叠，差异显著
- 性能差距主要在 fail 类的 precision：0.97 vs 0.85（512 截断丢失了过多诊断信息，导致更多 pass 样本被误判为 fail）
- tail-2048 的 fail recall 也更高（0.94 vs 0.94 持平），但 precision 差距大
- GPU 0 仍占用 49GB 显存但无活跃进程，可能是残留显存未释放

---
