# analysis o3 data cleaning

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_o3-data-cleaning_20260521T175447_result.json`
- **Structured JSON:** [`16ba81fc39b5633e4792.json`](../../sessions/16/16ba81fc39b5633e4792.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总结果：

## o3 FOLIO 数据清洗报告

| 指标 | 值 |
|---|---|
| 总题数 | 204 |
| 有效题数 (n_valid>0) | **196** |
| 排除题数 (n_valid=0) | **8** |
| SC@K_effective accuracy | **0.8265 (162/196)** |
| 有效 trace 数 min | 1 |
| 有效 trace 数 max | 12 |
| 有效 trace 数 mean | 9.88 |
| 有效 trace 数 median | 12.0 |
| 有效 trace 数 stdev | 3.16 |

**有效 trace 数分布：**

| n_valid | 题数 |
|---|---|
| 1 | 4 |
| 2 | 5 |
| 3 | 6 |
| 4 | 5 |
| 5 | 4 |
| 6 | 10 |
| 7 | 9 |
| 8 | 6 |
| 9 | 11 |
| 10 | 10 |
| 11 | 17 |
| 12 | 109 (55.6%) |

**Trace 级别统计：**
- 总 API 调用：2448 (204×12)
- 有效 trace：1937
- 空 trace：511 (20.87%)

**排除题的 gold 分布：** True×5, False×3, Unknown×0 — 排除偏向 True/False，Unknown 未受影响。

**Per-label accuracy (effective 196题)：**
- True: 52/67 = 77.6%
- False: 46/60 = 76.7%
- Unknown: 64/69 = 92.8%

**论文 clean 数据描述建议：** 我方验证的 SC accuracy = 0.8265 与 results.json header 一致，说明原始计算已正确排除了 n_valid=0 的题目。论文中可报告为 "SC@12 on 196/204 questions (8 excluded due to all-empty API responses) = 82.65%"，并注明空 trace 率 20.87%。109/196 (55.6%) 的题拿到了满 12 条有效 trace，数据质量整体可用。

---
