# ssh cleanup 30476 kill restart

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_cleanup_30476_kill_restart_20260517T190209_result.json`
- **Structured JSON:** [`9b1701600b6974062b5a.json`](../../sessions/9b/9b1701600b6974062b5a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清理完成。最终状态：

| GPU | 状态 | 实验 | PID |
|-----|------|------|-----|
| cuda:0 | 运行中 (100%, 74989MiB) | grid_b0_1_seed42 | 34716 |
| cuda:1 | 运行中 (85%, 74989MiB) | grid_b0_3_seed123_r2 | 42432 |
| cuda:2 | 运行中 (99%, 46505MiB) | rho02_adaptive_tau08_seed42 | 41387 |
| cuda:3 | **空闲** (0%, 0MiB) | 已清理，等 batchsize16 worker | — |

- grid_b0_1_seed42 存活正常运行，进度 ~46%，无需重启
- 已 kill PID 43465 (random_reweight 重复) 和 43543+43554 (grid_b0_3_seed456_r2 及其子进程)
- cuda:1、cuda:2 未触碰

---
