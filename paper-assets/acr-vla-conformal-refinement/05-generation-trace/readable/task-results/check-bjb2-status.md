# check bjb2 status

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_bjb2-status_20260515T012920_result.json`
- **Structured JSON:** [`2fc979edfbac67699371.json`](../../sessions/2f/2fc979edfbac67699371.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已完成。结果：

**T10 (pick_up_black_bowl_on_wooden_cabinet): 10% (1/10)**

### eval-vla-mean-spatial 完整 10 tasks 汇总

| Task | Success Rate |
|------|-------------|
| T1 | 70% (7/10) |
| T2 | 100% (10/10) |
| T3 | 0% (0/10) |
| T4 | 30% (3/10) |
| T5 | 0% (0/10) |
| T6 | 0% (0/10) |
| T7 | 80% (8/10) |
| T8 | 0% (0/10) |
| T9 | 30% (3/10) |
| T10 | 10% (1/10) |
| **Overall** | **32/100 = 32.0%** |

注意：之前 9 tasks 用的是 n_rollouts=9（每 task 跑了约 9-10 次得到 31/90=34.4%），但 T10 跑了 n_rollouts=10。如果之前每 task 也是 10 rollouts，则总数应为 31+1=32/100=32.0%。

**GPU 状态：完全空闲**（0% 利用率，0/24564 MiB 显存），可立即使用。

---
