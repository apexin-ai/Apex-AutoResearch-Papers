# ops kill rave residual bjb1 45299

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill_rave_residual_bjb1_45299_20260520T062132_result.json`
- **Structured JSON:** [`9c7dd9828942b00f0567.json`](../../sessions/9c/9c7dd9828942b00f0567.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

RAVE 残留进程 879641 已不存在，无需手动清理。

当前 GPU 状态：

| GPU | PID | 进程 | 显存 |
|-----|-----|------|------|
| 0 | 888720 | python (C+G) | 3359 MiB |
| 0 | 888926 | python (G) | 515 MiB |
| 1 | **888926** | python (C) | 2742 MiB |

GPU 1 上只有 TCN s1 进程 (PID 888926)，已干净，无资源竞争。

---
