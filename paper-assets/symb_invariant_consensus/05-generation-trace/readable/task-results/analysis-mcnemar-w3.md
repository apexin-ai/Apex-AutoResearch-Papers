# analysis mcnemar w3

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_mcnemar-w3_20260520T121432_result.json`
- **Structured JSON:** [`9d1e79c68cd63a30346a.json`](../../sessions/9d/9d1e79c68cd63a30346a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

**McNemar 2x2 Table (w=3)**

|  | Combo w=3 correct | Combo w=3 wrong |
|--|--|--|
| **SC correct** | 105 | 6 (b) |
| **SC wrong** | 15 (c) | 78 |

- **Discordant pairs**: 21 (b=6, c=15)
- **McNemar exact p = 0.0784** — 不显著 (α=0.05)
- **95% Bootstrap CI**: [+0.00pp, +8.82pp]

确认准确率：SC = 111/204 (0.5441), Combo w=3 = 120/204 (0.5882), Δ = +4.41pp

对比 w=1 (p=0.0391, b=1, c=8)：w=3 的 discordant pairs 更多 (21 vs 9)，但 b 也从 1 升到 6，使得 p 值从 0.039 升到 0.078，不再显著。w=3 虽然绝对提升更大 (+4.41pp vs +3.43pp)，但引入了更多 SC 对→combo 错的 flip (b=6)，稀释了统计信号。

---
