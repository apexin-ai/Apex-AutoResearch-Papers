# analysis obs only r3 final

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_obs-only-r3-final_20260515T101716_result.json`
- **Structured JSON:** [`21bc4fb8d255c40c39a8.json`](../../sessions/21/21bc4fb8d255c40c39a8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
== obs-only-r3 Final Results (T6-T9) ==
T6 (next_to_cookie_box):     90% (9/10)
T7 (on_the_stove):            0% (0/10)
T8 (next_to_the_plate):      20% (2/10)
T9 (on_wooden_cabinet):       0% (0/10)
4-task avg: 27.5%

== GPU Status ==
cuda:0: in use  (4652/24564 MiB, 23% util)
cuda:1: in use  (2535/24564 MiB, 24% util)
cuda:2: in use  (5710/24564 MiB, 21% util)
cuda:3: free    (1/24564 MiB, 0% util)

== seed43 Failure ==
Log 只有 20 行，在 T1 rollout 5/10 处截断，无 EXIT_CODE、无 Traceback、无 OOM 信息。
进程在 T0 完成 (80%, 8/10) 后、T1 执行到一半时被外部终止（tmux session 被 kill 或手动中断）。
start_task=0，说明它是从头跑的全 10-task eval，不是从 T6 重启的。
```

---
