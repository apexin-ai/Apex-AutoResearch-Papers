# fix registry pid status

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_registry_pid_status_20260518T031051_result.json`
- **Structured JSON:** [`0a450d23ee58365d1ed7.json`](../../sessions/0a/0a450d23ee58365d1ed7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。7 个实验均为 RUNNING 状态，registry 信息汇总：

| 实验 | 服务器 | GPU | PID | 状态 |
|---|---|---|---|---|
| contamination_60_adaptive_seed456 | westd-41312 | cuda:0 | 158632 | RUNNING |
| contamination_60_uniform_seed456 | westd-41312 | cuda:1 | 158709 | RUNNING |
| grid_b0_1_seed123 | westd-41312 | cuda:2 | 158918 | RUNNING |
| grid_b0_1_seed456 | **westd-41312** (已修正) | cuda:3 | 159304 | RUNNING |
| grid_b0_2_seed456 | westd-30476 | cuda:0 | 76271 | RUNNING |
| grid_b0_2_seed123 | westd-30476 | cuda:1 | 77244 | RUNNING |
| contamination_60_uniform_seed123 | westd-30476 | cuda:3 | 66327 | RUNNING (已有) |

grid_b0_1_seed456 的 server 已从错误的 westd-30476 修正为 westd-41312。

---
