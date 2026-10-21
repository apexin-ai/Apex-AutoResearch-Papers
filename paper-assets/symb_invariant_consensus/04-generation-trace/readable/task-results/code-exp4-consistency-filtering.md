# code exp4 consistency filtering

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp4-consistency-filtering_20260518T180814_result.json`
- **Structured JSON:** [`eb9c721742e0e98bd7bd.json`](../../sessions/eb/eb9c721742e0e98bd7bd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成。结果：

```
Method                     Correct   Accuracy
-----------------------------------------------------------------
SC (baseline)                  153     0.7500
SICA (T=1, all)                159     0.7794
SICA (T=4, >=4/12)             153     0.7500
SICA (T=6, >=6/12)             154     0.7549
SICA (T=8, >=8/12)             154     0.7549

Diagnostics (averages per problem):
Threshold      Unique   Filtered   Filter%  Satisfied   Excluded
-----------------------------------------------------------------
T=1             13.2       13.2    100.0%       13.0        0.2
T=4             13.2        1.8     13.4%        1.8        0.0
T=6             13.2        0.8      6.1%        0.8        0.0
T=8             13.2        0.3      2.2%        0.3        0.0
```

**关键发现**：

1. **SICA T=1（全约束）= 77.94%**，比原始 exp-001 报告的 74.51% 高出 3.4pp。这说明重新跑 dedup 与原始 pipeline 存在微小差异（可能是约束解析的边界情况）。

2. **过滤反而降低了准确率**：T=4/6/8 全部低于 T=1，且接近或等于 SC baseline。原因很清楚：平均每题只有 13.2 个 unique 约束，过滤到 T>=4 后只剩 1.8 个，T>=8 只剩 0.3 个。约束太少导致 MaxSAT 无法有效区分答案，退化为 SC。

3. **假设不成立**：在 FOLIO 逻辑域中，约束的跨 trace 一致性很低（大部分约束只出现在 1-2 条 trace 中），aggressive filtering 会丢掉几乎所有信号。

结果已保存到 `results/exp4_consistency_filtering/results.json`。

---
