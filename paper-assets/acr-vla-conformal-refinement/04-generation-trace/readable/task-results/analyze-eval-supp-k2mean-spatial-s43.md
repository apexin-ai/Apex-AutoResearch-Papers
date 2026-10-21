# analyze eval supp k2mean spatial s43

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval-supp-k2mean-spatial-s43_20260523T112439_result.json`
- **Structured JSON:** [`4ec84ed0742d7d120ab4.json`](../../sessions/4e/4ec84ed0742d7d120ab4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## eval-supp-k2mean-spatial-s43 结果

**SR = 78.0%** (156/200)

### Per-task

| Task | SR |
|------|-----|
| on_cookie_box | 100% |
| between_plate_ramekin | 95% |
| next_to_ramekin | 95% |
| table_center | 95% |
| next_to_cookie_box | 95% |
| on_wooden_cabinet | 85% |
| on_stove | 75% |
| top_drawer | 70% |
| next_to_plate | 70% |
| on_ramekin | **0%** |

### 结论

- K=2 mean Spatial: s42=81.5%, **s43=78.0%**，两 seed 均值 **79.75%**
- VLA-only baseline (s42) = 78.5%
- on_ramekin 任务两个 seed 均为 0%，是主要拉低项
- K=2 mean 在 Spatial 上相对 VLA-only 仅有微弱改进（+1.25pp 均值），且 seed 间方差较大（3.5pp）

Registry 已更新为 DONE(success)，cron 已删除。

---
