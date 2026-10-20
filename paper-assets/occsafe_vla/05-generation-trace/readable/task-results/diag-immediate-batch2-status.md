# diag immediate batch2 status

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_immediate_batch2_status_20260520T140707_result.json`
- **Structured JSON:** [`282dd73bc88e41c846b7.json`](../../sessions/28/282dd73bc88e41c846b7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Batch 2 提取状态

**5/9 tasks 完成，4 个仍在提取中。未就绪。**

### 已完成 (5)
| Task | Status |
|------|--------|
| between_plate_and_ramekin | COMPLETE (50/50) |
| from_table_center | COMPLETE (50/50) |
| in_the_top_drawer | COMPLETE (50/50) |
| next_to_the_plate | COMPLETE (50/50) |
| on_the_cookie_box | COMPLETE (50/50) |

### 进行中 (4)
| Task | PID | Demos done | Progress |
|------|-----|-----------|----------|
| next_to_ramekin (task 1) | 6450 | ~34/50 | demo_34 提取中 |
| next_to_cookie_box (task 5) | 6451 | ~37/50 | demo_36 刚完成 |
| on_ramekin (task 6) | 6452 | ~35/50 | demo_34 刚完成 |
| on_stove (task 7) | 6453 | ~33/50 | demo_33 提取中 |

### 速度与预估
- 速率：~1.3s/frame，~120 frames/demo → **~2.6 min/demo**
- 剩余最多的 task 7 还需 ~17 demos → **~44 min**
- 最快的 task 5 还需 ~13 demos → **~34 min**

**预估全部完成时间：约 22:55 CST（~45 分钟后）。**

---
