# ops nvidia smi check

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_nvidia_smi_check_20260518T061540_result.json`
- **Structured JSON:** [`361927540dff8720a222.json`](../../sessions/36/361927540dff8720a222.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Results

### Server 1: cqa1-33015 (4× RTX 4090D)

| GPU | PID | Process | Memory | Util |
|-----|-----|---------|--------|------|
| 0 | 1720 | python | 3808 MiB | 45% |
| 1 | — | idle | 0 MiB | 0% |
| 2 | — | idle | 0 MiB | 0% |
| 3 | — | idle | 0 MiB | 0% |

**Flag:** PID mismatch — expected PID 1715, found PID **1720**. Otherwise the pattern matches (GPU 0 active, GPUs 1-3 idle).

### Server 2: westd-27271 (2× RTX PRO 6000 Blackwell)

| GPU | PID | Process | Memory | Util |
|-----|-----|---------|--------|------|
| 0 | — | idle | 1 MiB | 0% |
| 1 | 1881 | python | 16089 MiB | 1% |

All matches expected. GPU 0 idle, GPU 1 running PID 1881 as expected. No unregistered processes.

---
