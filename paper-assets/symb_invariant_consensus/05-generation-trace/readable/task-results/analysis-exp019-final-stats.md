# analysis exp019 final stats

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp019-final-stats_20260517T091335_result.json`
- **Structured JSON:** [`1186afd405d3bf11dd00.json`](../../sessions/11/1186afd405d3bf11dd00.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp-019 完整统计结果

### 核心指标

| 指标 | 值 |
|---|---|
| n | 200 |
| SICA accuracy | **74.00%** (148/200) |
| SC accuracy | 72.00% (144/200) |
| Delta | **+2.00pp** |

### 统计显著性

| 检验 | 结果 |
|---|---|
| McNemar p-value | **0.4240** (不显著) |
| Discordant pairs | 14 total: 9 SICA-wins, 5 SC-wins |
| Bootstrap 95% CI | **[-1.50, +5.50]** (包含 0) |
| Bootstrap P(delta≤0) | 0.1724 |

### Pipeline 统计

| 指标 | 值 |
|---|---|
| Multi-candidate rate | 7.0% (14/200) |
| Constraints extracted (mean) | 19.9, unique after dedup: 6.2 |
| Traces with constraints | 9.6/12 |
| MaxSAT satisfied (mean) | 5.4, excluded: 0.9 |
| MaxSAT solve time | mean 1.58ms, max 37.50ms |
| Wall time | 50.4 min total, 15.1s/problem |

### Flip 分析

| 类别 | 数量 |
|---|---|
| Both correct | 139 |
| Both wrong | 47 |
| SICA only correct | 9 |
| SC only correct | 5 |
| Net flip | +4 |

### 低置信度子集（SICA 优势集中区域）

| SC margin | n | SICA | SC | Delta |
|---|---|---|---|---|
| ≤ 0.20 | 33 | 45.5% | 33.3% | **+12.1pp** |
| ≤ 0.34 | 51 | 43.1% | 35.3% | **+7.8pp** |
| ≤ 0.50 | 78 | 56.4% | 51.3% | **+5.1pp** |
| Unanimous (=1.0) | 109 | 86.2% | 86.2% | 0.0pp |
| Non-unanimous (<1) | 91 | 59.3% | 54.9% | **+4.4pp** |

### 结论

**结果未达统计显著**。McNemar p=0.424 远高于 0.05，Bootstrap CI [-1.50, +5.50] 包含 0。核心原因：discordant pairs 仅 14 对（7%），统计功效不足。

但子集分析显示 SICA 的优势集中在 SC 低置信度区域：当 SC vote margin ≤ 0.20 时，SICA 领先 +12.1pp (33 题)。Unanimous 子集上两者完全一致（86.2%），说明 SICA 只在 SC 不确定时介入并改善结果。

---
