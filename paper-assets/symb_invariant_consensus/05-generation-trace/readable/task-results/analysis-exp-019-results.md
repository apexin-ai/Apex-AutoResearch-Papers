# analysis exp 019 results

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp-019-results_20260517T091119_result.json`
- **Structured JSON:** [`fda39137e0f93b42b903.json`](../../sessions/fd/fda39137e0f93b42b903.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。报告已写入 `artifacts/exp019_analysis.md`。

## 结论：NEGATIVE

| | Value |
|--|-------|
| SICA | 74.00% (148/200) |
| SC | 72.00% (144/200) |
| Delta | **+2.00pp** |
| McNemar p (exact) | **0.424** |
| Bootstrap 95% CI | **[-1.50pp, +5.50pp]** (跨零) |

### 关键发现

1. **统计不显著**：p=0.424 远超 0.05 和 0.10 阈值，CI 跨零。D031 判定为 negative。

2. **效应缩水**：exp-011 (n=60) 的 +6.67pp 在扩大到 200 题后缩到 +2.00pp，缩水 70%。exp-011 的增益是小样本噪声。

3. **极少 discordant pairs**：200 题中只有 14 题 (7%) 两种方法不同。93% 的问题 SICA 和 SC 给出相同答案。

4. **SICA 仅充当 tiebreaker**：9 个 SICA wins 中 6 个发生在 SC 平票（3:3 或 6:6），且 5 个 SC wins 中 3 个也是平票但 SICA 选错了方向。

5. **54.5% 的问题 SC 全票一致**，SICA 无法改变结果。

**D031 决策：p >> 0.10，维持 Capability Trap analysis paper 方向。**

---
