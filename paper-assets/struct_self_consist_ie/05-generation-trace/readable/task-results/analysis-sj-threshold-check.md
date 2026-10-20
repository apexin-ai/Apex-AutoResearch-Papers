# analysis sj threshold check

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_sj_threshold_check_20260515T032543_result.json`
- **Structured JSON:** [`a8c6f1a35905dacbe380.json`](../../sessions/a8/a8c6f1a35905dacbe380.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

### 代码确认
- **没有任何 minimum similarity threshold**。`linear_sum_assignment(-cost)` 直接做最大化匹配，sim=0 的 pair 也会被 match。

### 数据统计（Qwen SciERC N=8, 551 instances）

| 区间 | 数量 | 占比 |
|------|------|------|
| sim = 0（完全不重叠） | 644 | 1.7% |
| sim < 0.1 | 653 | 1.7% |
| sim < 0.5 | 1,280 | 3.4% |
| **sim >= 0.5** | **36,381** | **96.6%** |

分布高度集中在 [0.9, 1.0]（93.0%），说明绝大多数 matched pair 是近乎完全重叠的。sim=0 的 644 个 pair 占比很小（1.7%），影响有限。

按 entity type 看，**OtherScientificTerm** 的 sim=0 比例最高（3.1%, 355/11569），可能因为该类型边界模糊、提取变异大。

总体 mean_sim=0.9595, median=1.0, std=0.1645。

结果已保存到 `/root/autodl-tmp/struct_self_consist_ie/output/review_round2/sj_threshold_analysis.json`。

---
