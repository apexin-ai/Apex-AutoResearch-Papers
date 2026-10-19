# diagnosis spatial norm02 seed44 check

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnosis_spatial-norm02-seed44-check_20260519T142255_result.json`
- **Structured JSON:** [`22bf20890622efd03adc.json`](../../sessions/22/22bf20890622efd03adc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Cron 已不存在（可能已被触发后自动清理）。

---

**诊断报告：eval-obs-only-spatial-norm02-seed44**

| 项目 | 结果 |
|------|------|
| 状态 | 成功完成 |
| Overall SR | **0.36** (36/100) |
| 模式 | crm_obs_only, spatial, K=10, seed=44, norm=0.2 |

**Per-task 成绩：**

| Task | SR |
|------|-----|
| bowl_next_to_ramekin | 1.0 |
| bowl_next_to_cookie_box | 1.0 |
| bowl_between_plate_and_ramekin | 0.9 |
| bowl_on_cookie_box | 0.4 |
| bowl_next_to_plate | 0.2 |
| bowl_in_top_drawer | 0.1 |
| bowl_from_table_center | 0.0 |
| bowl_on_ramekin | 0.0 |
| bowl_on_stove | 0.0 |
| bowl_on_wooden_cabinet | 0.0 |

**已执行操作：** metrics/checkpoint_path/log_path/hypothesis 写入 registry → status=DONE(success)。Cron 已清理。

---
