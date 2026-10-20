# ops check 14b progress 17855

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-14b-progress-17855_20260522T173935_result.json`
- **Structured JSON:** [`088f998d22735d07a61e.json`](../../sessions/08/088f998d22735d07a61e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 6 个进程存活，无完成实验。汇总：

| exp_id | 已完成gen/总gen | 进程状态 | 完成? | 预估剩余 |
|--------|----------------|---------|------|---------|
| t10_a075_v2 | 8/10 (训练gen_8) | ALIVE 4h33m | ❌ | ~2h |
| **t10_a060_v2** | **9/10 (训练gen_9)** | ALIVE 4h31m | ❌ | **~1h 即将完成** |
| t10_a045 | 4/10 (训练gen_4) | ALIVE 4h33m | ❌ | ~6-7h |
| t15_a060_v2 | 8/15 (训练gen_8) | ALIVE 4h32m | ❌ | ~8h |
| t15_a050_v3 | 7/15 (训练gen_7) | ALIVE 4h32m | ❌ | ~9h |
| t15_a045 | 5/15 (训练gen_5) | ALIVE 4h31m | ❌ | ~11h |

速率约 1-1.5h/gen（1.4B pythia, 5000 steps/gen）。

**最快完成**：t10_a060_v2 仅差 1 gen，约 1 小时内完成。t10_a075_v2 次之，约 2 小时。T=15 系列今晚能跑完。

---
