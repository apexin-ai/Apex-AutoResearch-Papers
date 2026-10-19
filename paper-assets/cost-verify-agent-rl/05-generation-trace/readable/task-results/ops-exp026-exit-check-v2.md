# ops exp026 exit check v2

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_exp026_exit_check_v2_20260515T105923_result.json`
- **Structured JSON:** [`0c70e2ee5770fec5eb02.json`](../../sessions/0c/0c70e2ee5770fec5eb02.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
Process: ALIVE (PID 778562: 21h07m, PID 781795: 20h51m)
tmux: (check blocked by ssh_read_only metachar filter)
GPU: both in heavy use — GPU 0: 96%, 14789 MiB; GPU 1: 96%, 14789 MiB
Steps completed: unknown (progress bar uses \r, log only captured initial "0/150")
Exit type: STILL RUNNING
Errors found: 0 traceback, 0 exception, 0 killed, 1 "oom" (config string match, not actual OOM)
Log lines: 5036, all recent lines are benign anchor_obs warnings (18:58:41 timestamp)
Initial val metrics: success=6.25%, action_is_valid=63.1%, action_is_effective=87.9%
Key training metrics (pg_loss/entropy): not yet logged to file (only in wandb)
```

**误报。** 两个进程均存活 21+ 小时，双 GPU 96% 利用率，无 crash/error。日志中的 `Training Progress: 0%` 是因为 tqdm 用 `\r` 覆盖行，log 文件只捕获了初始状态。实际训练进度需查 wandb。

---
