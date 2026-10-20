# analysis pilot constraint filtering

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_pilot-constraint-filtering_20260517T052909_result.json`
- **Structured JSON:** [`3c237846657e0584e8f1.json`](../../sessions/3c/3c237846657e0584e8f1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。

## pilot-constraint-filtering 结果

| T | avg constraints | SICA | SC | gap |
|---|---|---|---|---|
| 1 (no filter) | 22.3 | 76.74% | 74.42% | +2.33pp |
| 2 | 18.5 | 76.74% | 74.42% | +2.33pp |
| 3 | 16.3 | 76.74% | 74.42% | +2.33pp |
| 5 | 13.7 | 74.42% | 74.42% | 0.00pp |
| 7 | 9.7 | 74.42% | 74.42% | 0.00pp |

**Conclusion: NEGATIVE**

- n=43, 无显著性检验。+2.33pp = 1题翻转，无统计意义。
- T=1,2,3 结果完全一致：温和过滤不改变任何判定，说明"噪声约束"本身就不影响 MaxSAT 输出。
- T≥5 过度过滤，SICA 退化为 SC。
- 问题不在约束质量，而在 SICA 机制本身对聚合决策无增量贡献。Constraint filtering 不是 rescue path。

---
