# code check progress

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_check-progress_20260514T082641_result.json`
- **Structured JSON:** [`f19cbe1d7e721fd6d5df.json`](../../sessions/f1/f19cbe1d7e721fd6d5df.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已写入 `artifacts/check_progress.sh` 并设为可执行。`register_artifact` 工具不在当前可用工具列表中，无法自动注册——需要你手动注册或通过其他方式处理。

脚本包含 5 个检查模块：rep 进度（含进度条）、GPU 状态、日志尾部、ETA 估算、进程存活检查。在服务器上直接 `bash check_progress.sh` 运行即可。

---
