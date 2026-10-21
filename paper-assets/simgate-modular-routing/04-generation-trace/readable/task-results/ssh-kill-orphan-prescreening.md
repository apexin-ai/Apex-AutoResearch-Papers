# ssh kill orphan prescreening

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_kill-orphan-prescreening_20260513T234316_result.json`
- **Structured JSON:** [`8e0f3960c90335f9a5fe.json`](../../sessions/8e/8e0f3960c90335f9a5fe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 prescreening 孤儿进程已清除。确认结果：

- **无 prescreening 残留** — grep 输出中不含任何 prescreening 相关进程
- **plan-001b 进程正常运行**：
  - gpu0-v2 (PID 852800) — 正常
  - gpu1 (PID 773114) — 正常
- **GPU 占用正常**：
  - GPU 0: PID 853847, 28004 MiB (VLLM)
  - GPU 1: PID 774317, 28004 MiB (VLLM)

---
