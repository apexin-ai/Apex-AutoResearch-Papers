# ops cleanup gpu bjb1

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cleanup_gpu_bjb1_20260514T011255_result.json`
- **Structured JSON:** [`38999d673be003c1f7d0.json`](../../sessions/38/38999d673be003c1f7d0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清理完毕。

**被 kill 的进程：**
| PID | 命令 |
|-----|------|
| 85028 | tmux session (exp_006_fixed_dt2) |
| 85029 | bash wrapper (exp_006_fixed_dt2) |
| 85033 | timeout wrapper (exp_006_fixed_dt2) |
| 85034 | `python dreamer.py ... --logdir logdir/fixed_dt2_v1_s1` |
| 90358 | timeout wrapper (fixed_dt4_v2_s1) |
| 90359 | `python dreamer.py ... --logdir logdir/fixed_dt4_v2_s1` |

**保留的进程：** exp009_dryrun（PID 101810/101815/101816，短期测试，timeout 120s）

**GPU 显存释放状态：**
- GPU 0: 3 MiB, 0% 利用率
- GPU 1: 3 MiB, 0% 利用率

**ALL_CLEAN** — 两块 GPU 显存已完全释放。

---
