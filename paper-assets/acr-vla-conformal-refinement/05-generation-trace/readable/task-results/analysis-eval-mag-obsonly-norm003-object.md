# analysis eval mag obsonly norm003 object

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval-mag-obsonly-norm003-object_20260516T053656_result.json`
- **Structured JSON:** [`b243d7917817edbd605b.json`](../../sessions/b2/b243d7917817edbd605b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新完毕。

## 结果摘要

**Overall SR: 16.0%** (16/100)

| 对比 | 数值 | Delta |
|------|------|-------|
| vs argmin baseline (12%) | +4pp | ✓ 超过 baseline |
| vs norm=0.1 (19%) | -3pp | 低于 |
| vs norm=0.2 (22%) | -6pp | 低于 |
| vs spatial norm=0.03 (34-44%) | -18~28pp | 远低于 |

**结论**: norm=0.03 在 object benchmark 上 beats argmin baseline（16% > 12%），标记 success。但在 object domain 上表现弱于更大 norm（0.1/0.2），且远不如 spatial benchmark 上的同 norm 结果。Object domain 的 magnitude curve 呈单调递增趋势（0.03→0.1→0.2 = 16%→19%→22%），说明 object 任务需要更大幅度的修正才能生效。

---
