# diagnose goal vla s47 r3 crash

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_goal-vla-s47-r3-crash_20260524T112412_result.json`
- **Structured JSON:** [`fc19c0eeabc814e5fcd1.json`](../../sessions/fc/fc19c0eeabc814e5fcd1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**诊断结论：实验已正常完成，无需重启。**

- **原因**：进程不是崩溃，而是正常执行完毕后退出。PID 消失是因为任务已完成。
- **结果**：overall success rate = **82.5%** (165/200)，结果已保存到 `logs/eval_goal_vla_only_seed47.json`（写入时间 May 24 19:20）
- **Per-task 结果**：
  - turn_on_the_stove: 100% (20/20)
  - put_the_bowl_on_the_stove: 100% (20/20)
  - put_the_wine_bottle_on_top_of_the_cabinet: 90%
  - push_the_plate_to_the_front_of_the_stove: 90%
  - put_the_bowl_on_the_plate: 90%
  - put_the_bowl_on_top_of_the_cabinet: 85%
  - open_the_middle_drawer_of_the_cabinet: 80%
  - put_the_wine_bottle_on_the_rack: 80%
  - open_the_top_drawer_and_put_the_bowl_inside: 55%
  - put_the_cream_cheese_in_the_bowl: 55%

不需要重启，cuda:2 当前空闲可用于其他任务。

---
