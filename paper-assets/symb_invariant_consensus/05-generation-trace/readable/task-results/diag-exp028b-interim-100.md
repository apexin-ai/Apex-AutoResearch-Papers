# diag exp028b interim 100

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_exp028b-interim-100_20260518T232503_result.json`
- **Structured JSON:** [`7e7786361874f6ded1b3.json`](../../sessions/7e/7e7786361874f6ded1b3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**exp-028b 状态报告 (Qwen3-14B thinking, FOLIO-204)**

| 指标 | 值 |
|---|---|
| 进度 | **71 / 204** (34.8%) |
| SC accuracy | 85.92% (61/71) |
| SICA accuracy | 88.73% (63/71) |
| **delta** | **+2.82pp** |
| Discordant pairs | b=2 (SICA wins), c=0 (SC wins) |
| Override precision | **100%** (2/2) |
| Extraction rate | 92.0% |
| Contradiction rate | 1.03% |
| 已运行 | 2.8h, 143.3s/problem |
| **ETA** | **~5.3h** (约 12:45 服务器时间) |

对比上次 (60题): 新增 11 题, SC 85.92% vs 83.05% (+2.87pp), SICA 88.73% vs 86.44% (+2.29pp), delta 从 +3.39pp 收窄到 +2.82pp。两个指标都在上升，delta 略收窄但 SICA 仍稳定领先，override precision 保持 100%。实验正常运行中。

---
