# diagnose eval pi05 random k05 result

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_pi05_random_k05_result_20260521T090610_result.json`
- **Structured JSON:** [`ccfba305b132352f0cd4.json`](../../sessions/cc/ccfba305b132352f0cd4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。

## 总结

### π0.5 Random k=0.5 最终结果

**Overall SR: 69.4%** (347/500 episodes, 10 tasks × 50 eps)

**D132 crossover 在 π0.5 上强烈成立：**

| Method | SR | 相对 Baseline |
|--------|-----|--------------|
| Baseline (no prune) | 98.2% | 100% |
| **Random k=0.5** | **69.4%** | **70.7%** |
| L2norm k=0.5 | 33.4% | 34.0% |

Random 以 **+36.0pp** 大幅超过 L2norm。L2norm 在 2 个 task 上完全崩溃 (0% SR)，而 random 最低也有 54%。这说明 L2norm 的"重要性"排序在 π0.5 (低 CV=0.055) 上不仅无效，反而有系统性地丢弃关键 token。

### π0.5 Random k=0.3 状态
PID 914719 仍在运行 (已运行 1h42m)，结果待收集。

---
