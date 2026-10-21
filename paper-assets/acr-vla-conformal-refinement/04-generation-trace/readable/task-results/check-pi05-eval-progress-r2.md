# check pi05 eval progress r2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_pi05-eval-progress-r2_20260522T050305_result.json`
- **Structured JSON:** [`eafd0d8a3f3c1c1c31fd.json`](../../sessions/ea/eafd0d8a3f3c1c1c31fd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Eval 进度汇总

### bjb1-32546 — Object (运行 ~4h)

| Eval | 完成 tasks | 当前位置 | 总进度 | 预估剩余 |
|------|-----------|---------|-------|---------|
| seed42 | 2/10 | task 3 启动中（未输出 rollout） | ~40/200 (20%) | ~16h |
| seed43 | 2/10 | task 3 启动中（未输出 rollout） | ~40/200 (20%) | ~16h |
| seed44 | 1/10 | task 2, rollout 15/20 | ~35/200 (17.5%) | ~19h |

已完成 task 结果：
- Task 1 (alphabet_soup): 100% / 100% / 90%
- Task 2 (cream_cheese): 80% / 80% / 进行中

### bjb2-28827 — Spatial (运行 ~3h47m)

| Eval | 完成 tasks | 当前位置 | 总进度 | 预估剩余 |
|------|-----------|---------|-------|---------|
| seed42 | 2/10 | task 3 (table_center), rollout 5/20 | ~45/200 (22.5%) | ~13h |
| seed43 | 2/10 | task 3 (table_center), rollout 5/20 | ~45/200 (22.5%) | ~13h |
| seed44 | 2/10 | task 3 (table_center), rollout 5/20 | ~45/200 (22.5%) | ~13h |

已完成 task 结果：
- Task 1 (bowl_between): 90% / 85% / 85%
- Task 2 (bowl_next_to_ramekin): 95% / 95% / 90%

### 总结

6 个进程全部存活，进度 ~18-23%。从 1h 前的 ~5% 提升到 ~20%，速率正常（每 task ~2h）。Object 预计还需 ~16-19h，Spatial 预计 ~13h。最早完成的会是 Spatial 组（明天凌晨左右）。

---
