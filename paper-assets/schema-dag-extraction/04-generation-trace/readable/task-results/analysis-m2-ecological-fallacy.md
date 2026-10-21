# analysis m2 ecological fallacy

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_m2_ecological_fallacy_20260522T091157_result.json`
- **Structured JSON:** [`6bcaffda34c83a9c7b0d.json`](../../sessions/6b/6bcaffda34c83a9c7b0d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。核心结论：

**Ecological fallacy 结构上不适用。** BCS 是 contextual variable（Level-2），每个 batch 内所有 instance 共享同一个 BCS 值，within-batch BCS 方差恰好为零。经典 ecological fallacy 要求 X 是 individual-level 变量的聚合（如个人收入→地区平均收入），但 BCS 不是——它是不可分解的 batch-level 构念。

关键数据：

| 指标 | 值 |
|------|-----|
| ICC（type-level, Qwen3） | 0.146 |
| ICC（instance-level, Gemini Flash） | 0.035 |
| Batch-level semipartial R²(BCS\|count) | 0.138 |
| Type-level semipartial R²(BCS\|count) | 0.012 |
| Type-level β(BCS), cluster-robust | −0.485, p < .001 |
| Within-batch BCS variance | 0.000 |
| Effect direction reversal? | 无 |

低 ICC 是预期中的——binary correctness 的 instance-level 变异主要由实例本身难度决定，而非 batch 组成。BCS 的 claim 本身就是 batch-level 的（"batch composition affects batch performance"），batch-level 分析就是正确的分析粒度。

---
