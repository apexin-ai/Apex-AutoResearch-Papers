# analysis aime30 v2 partial

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_aime30_v2_partial_20260515T154822_result.json`
- **Structured JSON:** [`693262ff9dd5e39362f2.json`](../../sessions/69/693262ff9dd5e39362f2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析报告已保存到 `artifacts/aime30_v2_partial_analysis.md`。

## 核心结论

**矛盾检测信号：弱阳性。** 机制在工作，但尚未产生实际价值。

具体数据：

| | AIME (4题) | MATH smoke (5题) |
|--|-----------|-----------------|
| 矛盾检出题比 | **50%** (2/4) | 20% (1/5) |
| 唯一约束/题 | **18.7** | 6.8 |
| 排除率 | 10.7% | 8.8% |
| SICA≠SC | **0/4** | 0/5 |

AIME 确实比 MATH 产生更多矛盾（验证了难题假设），但 **SICA 和 SC 在全部 9 题上答案完全一致**。原因是 SC 投票太集中（12/12 或 11/12 unanimous），排除几个约束不足以翻转答案。

**Problem II_02 完全失败**：0 约束、0 投票，疑似答案提取问题，需排查。

**对 v3 判断**：前 4 题是 AIME II 最简单的，QwQ 正确率 3/4。后面的难题 SC 分布应更分散，才是 SICA 差异化的关键战场。v3 全量跑是必要的。

---
