# ssh kill dup cuda2

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_kill-dup-cuda2_20260522T193926_result.json`
- **Structured JSON:** [`5ba491d9165ad507082a.json`](../../sessions/5b/5ba491d9165ad507082a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

PID 1979 已成功 kill。

**GPU 2 剩余进程：**
- PID 108611 — `exp-004-reduced-lora-ckpt500` eval，占用 12912 MiB

**其他 eval 进程（非 GPU 2）：**
- PID 22131 / tmux session — `exp003s2_r3only_ckpt8000` eval on CUDA:3
- PID 171442 — `exp-004-reduced-lora-ckpt1000` eval on CUDA:3

GPU 2 上只剩 ckpt500 的 eval 在跑，重复进程已清除。

---
