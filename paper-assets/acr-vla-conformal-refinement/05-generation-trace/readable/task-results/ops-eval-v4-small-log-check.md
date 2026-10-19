# ops eval v4 small log check

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_eval-v4-small-log-check_20260515T050353_result.json`
- **Structured JSON:** [`00b509424688d9b4c5c2.json`](../../sessions/00/00b509424688d9b4c5c2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验的 registry 已经由之前的 Worker 正确更新，无需再改。以下是验证结果：

---

### eval-acr-spatial-v4-small (D018)

- **状态**: DONE / failed
- **死因**: Task 8 (on_stove) env init hang 8+ 小时后被 kill
- **进程**: PID 253085 已死，无 sentinel
- **完成度**: 7/10 tasks，running avg **42.9% (30/70)**

| Task | Success Rate |
|------|-------------|
| between_plate_and_ramekin | 60% (6/10) |
| next_to_ramekin | **100%** (10/10) |
| from_table_center | 10% (1/10) |
| on_cookie_box | 40% (4/10) |
| in_top_drawer | 0% (0/10) |
| on_ramekin | 0% (0/10) |
| next_to_cookie_box | **90%** (9/10) |

---

### eval-acr-spatial-v4-obs-only-r2 (D020)

- **状态**: DONE / failed
- **死因**: Task 7 (next_to_cookie_box) rollout 处理中被 kill（实际日志显示 rollout 5/10 时 5/5 成功，进程仍在推进，非 hang）
- **进程**: PID 270097 已死，无 sentinel
- **完成度**: 6/10 tasks，running avg **40.0% (24/60)**
- Task 7 有未完成的 partial 数据：5/5 at rollout 5/10

| Task | Success Rate |
|------|-------------|
| between_plate_and_ramekin | **90%** (9/10) |
| next_to_ramekin | **100%** (10/10) |
| from_table_center | 0% (0/10) |
| on_cookie_box | 40% (4/10) |
| in_top_drawer | 10% (1/10) |
| on_ramekin | 0% (0/10) |

---

Registry 两条均已是 DONE/failed，metrics 和 failure_reason 与日志一致，无需更新。

---
