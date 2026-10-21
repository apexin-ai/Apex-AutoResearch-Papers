# analysis plan 004 v2 results

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_plan-004-v2-results_20260515T031001_result.json`
- **Structured JSON:** [`59a82f5bf099db99fbb5.json`](../../sessions/59/59a82f5bf099db99fbb5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。核心发现：

**排序**（lower PPL = better）：all (2.335) > size_matched (2.367) > depth01 (2.387) > binary_filtered (2.389) > depth0_only (2.682)

**关键结论**：

1. **"Depth-aware curation helps" 不成立。** 在同等数据量（3951 samples）下，随机采样（size_matched）的 PPL 比 depth01 低 0.020、比 binary_filtered 低 0.022。两种 filtering 策略都不如随机。

2. **数据量是主导因素。** all (12299 samples) 比 size_matched (3951) 低 0.032 PPL——这是实验中最大的效应，且方向明确。

3. **统计显著性的 caveat：** 虽然所有对比的 bootstrap CI 都不跨 0，但这是因为 seed 间方差极小（<0.001），而非样本量充足。n=3 的 bootstrap 只有 8 种 resample 模式，CI 的"紧"是假象。

4. **实际差异很小：** 三个 size-matched variant 之间总 spread 仅 0.022 PPL，难以支撑任何 filtering 优于 random 的 claim。

报告已保存到服务器 `artifacts/plan-004-v2/downstream_analysis.txt` 并注册。

---
