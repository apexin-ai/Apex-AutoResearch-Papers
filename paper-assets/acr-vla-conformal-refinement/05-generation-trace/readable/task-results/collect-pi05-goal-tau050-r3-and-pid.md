# collect pi05 goal tau050 r3 and pid

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_collect_pi05-goal-tau050-r3-and-pid_20260527T233812_result.json`
- **Structured JSON:** [`59d08c3ded04c43ddbbe.json`](../../sessions/59/59d08c3ded04c43ddbbe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个任务完成。

## 汇总

**Task 1: pi05-tau-sweep-goal-tau050-s42-r3** → DONE (success)
- SR = **87%**, trigger_rate = **2.06%**
- 日志无 OOM/CUDA error
- 确认 r2 的 0% SR 是 anomaly（初始化故障），τ=0.50 实际表现与 τ=0.70 持平（均 87%）
- Per-task: bowl_on_stove/cream_cheese/turn_on_stove/bowl_on_plate 全 100%；wine_bottle_on_rack 最低 60%

**Task 2: pi05-crm-always-on-object-s43** → PID **190565** 已写入 registry spec
- 进程在 cuda:0 上运行中，spec 已完整恢复

---
