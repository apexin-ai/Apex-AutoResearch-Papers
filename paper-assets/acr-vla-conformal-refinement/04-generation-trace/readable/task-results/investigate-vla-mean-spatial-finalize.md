# investigate vla mean spatial finalize

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_investigate_vla-mean-spatial-finalize_20260514T221220_result.json`
- **Structured JSON:** [`bc8429e42d02f405bc87.json`](../../sessions/bc/bc8429e42d02f405bc87.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新完毕。总结：

**eval-vla-mean-spatial** → conclusion: **success**

| Task | 成绩 |
|------|------|
| T1 between_plate_ramekin | 70% (7/10) |
| T2 next_to_ramekin | 100% (10/10) |
| T3 from_table_center | 0% (0/10) |
| T4 on_cookie_box | 30% (3/10) |
| T5 in_top_drawer | 0% (0/10) |
| T6 on_ramekin | 0% (0/10) |
| T7 next_to_cookie_box | 80% (8/10) |
| T8 on_stove | 0% (0/10) |
| T9 next_to_plate | 30% (3/10) |
| T10 on_wooden_shelf | **未运行** |

**9 tasks 总计: 31/90 = 34.4%**。进程在 T9 完成后被静默杀死（日志无错误/traceback），T10 从未开始。bjb2-40593 的 GPU 0 现已被 eval-acr-spatial-v4-obs-only 占用。

---
