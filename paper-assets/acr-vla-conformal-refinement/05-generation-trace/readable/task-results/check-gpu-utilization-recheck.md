# check gpu utilization recheck

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_gpu-utilization-recheck_20260521T154131_result.json`
- **Structured JSON:** [`d144c3b2c8cc6964105d.json`](../../sessions/d1/d144c3b2c8cc6964105d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

### bjb2-28827（6 GPU，Spatial precompute shard 0-5）

| GPU | 利用率 | 显存 | 状态 |
|-----|--------|------|------|
| 0 | 21% | 9883/24564 MiB | shard 0 运行中 |
| 1 | 21% | 9883/24564 MiB | shard 1 运行中 |
| 2 | 20% | 9883/24564 MiB | shard 2 运行中 |
| 3 | 20% | 9883/24564 MiB | shard 3 运行中 |
| 4 | 21% | 9883/24564 MiB | shard 4 运行中 |
| 5 | 19% | 9883/24564 MiB | shard 5 运行中 |

**6 个 train_crm 进程全部存活**，CPU 均在 154%+。利用率 19-21% 属于 I/O bound，正常。

### bjb2-40593（1 GPU，Object precompute shard 0）

| GPU | 利用率 | 显存 | 状态 |
|-----|--------|------|------|
| 0 | 14% | 9839/24564 MiB | shard 0 运行中 |

**进程存活**（PID 872656，CPU 140%）。

**注意**：旧任务（`runs/` 下的日志，num_shards=7）在 2900/7251 时被 SIGHUP 终止（EXIT_CODE=129）。当前跑的是**新任务**（num_shards=10，日志写到 `/root/precompute_pi05_shard0.log`），进度 **3600/7251**，预计剩余 ~12200s（~3.4h），速度 3.34s/sample。

### 结论

两台服务器全部正常运行，无进程死亡。GPU 利用率偏低（14-21%）为 I/O bound 导致，可接受。

---
