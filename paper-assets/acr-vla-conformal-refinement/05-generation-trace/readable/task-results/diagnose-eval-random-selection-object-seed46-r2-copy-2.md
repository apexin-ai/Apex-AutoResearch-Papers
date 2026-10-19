# diagnose eval random selection object seed46 r2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval-random-selection-object-seed46-r2_20260519T174856_result.json`
- **Structured JSON:** [`bbddf96b0ac72914363f.json`](../../sessions/bb/bbddf96b0ac72914363f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

**根因**：robosuite/MuJoCo C 后端间歇性 segfault。seed46 完成 6/10 任务后进程被外部信号杀死（无 Python traceback），非代码 bug。seed42 同代码路径完整跑完 10 任务并输出 JSON，`select_action_random` 逻辑极简无问题。磁盘和 GPU 资源均正常。

**结论**：可直接重试，无需修复。

---
