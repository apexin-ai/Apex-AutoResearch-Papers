# analysis truncation bias exp011

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_truncation-bias-exp011_20260517T104437_result.json`
- **Structured JSON:** [`bf9c9c11d0aaa97a3350.json`](../../sessions/bf/bf9c9c11d0aaa97a3350.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。核心数据已经清楚，写总结。

## 分析结论

### Truncation 与 Discordant Pairs 无关联

6 个 discordant pairs 中，**5 个没有任何截断 trace**（truncated=0/12）。唯一有截断的 idx=24（3/12 truncated），其 3 条截断 trace 全部无法提取答案（empty），对 SC 和 SICA 投票均无贡献。

### 关键数据

| 指标 | 值 |
|---|---|
| 截断 trace 无答案率 | 84.1%（37/44） |
| 截断 trace 准确率（有答案的 7 条） | 28.6% |
| 非截断 trace 准确率 | 63.8% |
| 去掉截断 trace 后 SC 准确率 | 60.0%（不变） |
| Discordant pairs 含截断 | 1/6，且截断 trace 全部无答案 |

### 结论（<200字）

**不存在 truncation bias。** SICA 的 +6.67pp 增益与截断无关。6 个 discordant pairs 中 5 个完全没有截断 trace，唯一有截断的 idx=24 中 3 条截断 trace 全部无法提取答案，对投票无影响。去掉全部 44 条截断 trace 后 SC 准确率保持 60.0% 不变。截断 trace 的主要效应是丧失答案（84.1% 无答案率），而非引入噪声投票。SICA 的增益来源是约束权重对近似票数分裂（如 5:5:1:1）的有效区分，而非截断 artifact。论文叙事可安全使用 +6.67pp 数据，无需加 truncation caveat。

需要我把这个分析写入 artifacts 目录吗？

---
