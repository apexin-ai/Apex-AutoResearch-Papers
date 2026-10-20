# diagnose d129 random s43 failure

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_d129-random-s43-failure_20260518T000121_result.json`
- **Structured JSON:** [`0655c10a12841f19a5e1.json`](../../sessions/06/0655c10a12841f19a5e1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成：

- **根因**: 进程被外部信号杀死（SIGKILL/SIGTERM）。日志无 Python traceback、OOM、CUDA error，训练正常运行到 step 31 后日志截断。
- **重试 r2 状态**: PID 66669 正常运行，已到 step 31/500，开始产生非零 reward（step 29 prove_rate=0.125），训练正常推进中。

---
