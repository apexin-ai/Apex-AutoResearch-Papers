# verify adaptive fix seed42 restart

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_adaptive_fix_seed42_restart_20260514T174310_result.json`
- **Structured JSON:** [`4ee4be21aac0e6b18487.json`](../../sessions/4e/4ee4be21aac0e6b18487.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**冲突发现：cuda:1 上有两个训练进程。**

### cuda:1 状态
| PID | 显存 | 运行时间 | 身份 |
|-----|------|---------|------|
| 123836 | 46514 MiB | 02:18 | **旧进程**（上一个 dispatch 遗留） |
| 125297 | 46514 MiB | ~01:24 | **新进程**（125292 的子 python 进程） |

两个进程都在 cuda:1 上跑同一个 adaptive_fix_seed42 任务。

### seed42 重启验证
- 参数解析通过，`--resume_from_checkpoint checkpoint-1500` 生效
- 进度条从 1501/6103 开始，当前推进到 **1538/6103**（~25%）
- 训练速度 ~1.1 s/it，adaptive weighting 指标正常输出

### seed123 / seed456
- PID 109362 (seed123, cuda:2): 存活，运行 3h19m
- PID 115071 (seed456, cuda:3): 存活，运行 2h26m

### 需要处理
**需要 kill PID 123836**（旧的 adaptive_fix_seed42 进程），否则两个进程抢 cuda:1 显存，训练会变慢甚至 OOM。

是否现在 kill 123836？

---
