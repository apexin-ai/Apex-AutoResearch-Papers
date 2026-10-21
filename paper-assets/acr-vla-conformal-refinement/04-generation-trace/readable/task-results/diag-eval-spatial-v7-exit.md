# diag eval spatial v7 exit

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_eval-spatial-v7-exit_20260514T014047_result.json`
- **Structured JSON:** [`1bef2adb424f0843f1af.json`](../../sessions/1b/1bef2adb424f0843f1af.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成。

**eval-spatial-v7-full 结果：成功完成**

| 指标 | 值 |
|------|------|
| **Overall success rate** | **30.0% (30/100)** |
| Mode | vla_only, K=1 |
| Benchmark | LIBERO spatial, 10 tasks × 10 rollouts |

**逐任务成绩：**

| Task | Success Rate |
|------|-------------|
| next_to_ramekin | **100%** |
| next_to_cookie_box | **90%** |
| between_plate_and_ramekin | 60% |
| next_to_plate | 30% |
| on_cookie_box | 20% |
| from_table_center | 0% |
| in_top_drawer | 0% |
| on_ramekin | 0% |
| on_stove | 0% |
| on_wooden_cabinet | 0% |

SmolVLA baseline 在简单的"旁边"类任务上表现尚可（90-100%），但在需要精确空间理解的任务（"上面"、"里面"、"中间"）上完全失败（0%），整体 30%。这为 ACR conformal refinement 提供了 baseline 对照。

---
