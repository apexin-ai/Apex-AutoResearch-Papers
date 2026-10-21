# analysis eval mag obsonly norm003 b2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval-mag-obsonly-norm003-b2_20260516T004840_result.json`
- **Structured JSON:** [`3e5183b875439dfe0354.json`](../../sessions/3e/3e5183b875439dfe0354.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已完成，JSON 和 registry 数据一致。Registry 已经是 DONE + success 状态，无需更新。

## eval-mag-obsonly-norm003-b2 最终结果

**Overall SR: 34%** (34/100)

| Task | SR |
|------|-----|
| next_to_ramekin | **1.0** |
| between_plate_and_ramekin | 0.9 |
| next_to_cookie_box | 0.8 |
| on_cookie_box | 0.3 |
| next_to_plate | 0.3 |
| in_top_drawer | 0.1 |
| from_table_center | 0.0 |
| on_ramekin | 0.0 |
| on_stove | 0.0 |
| on_wooden_cabinet | 0.0 |

相比 8/10 partial（SR=38.75%），新增两个 task：
- **next_to_plate**: 0.3
- **on_wooden_cabinet**: 0.0

最终 10-task SR 从 partial 的 38.75% 降至 **34%**。Registry 已由 hook 自动更新为 DONE/success。

---
