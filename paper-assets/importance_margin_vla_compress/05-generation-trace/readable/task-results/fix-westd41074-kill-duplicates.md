# fix westd41074 kill duplicates

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_westd41074_kill_duplicates_20260527T093723_result.json`
- **Structured JSON:** [`edafa8fbe5d9d91cefa9.json`](../../sessions/ed/edafa8fbe5d9d91cefa9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清理完成：

- **PID 371486 / 371488** 已 kill，GPU0 和 GPU1 各释放 ~9.7GB 显存
- **PID 356361**（random k=0.9，已运行 ~20min）正常运行，pruning 230/256 tokens
- **PID 356612**（random k=0.5，已运行 ~20min）正常运行，pruning 128/256 tokens
- GPU2/GPU3 上的进程（262137/262473）未受影响

---
