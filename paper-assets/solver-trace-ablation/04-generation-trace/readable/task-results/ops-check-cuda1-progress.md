# ops check cuda1 progress

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-cuda1-progress_20260515T010232_result.json`
- **Structured JSON:** [`48a25e3b2c2f689fdc71.json`](../../sessions/48/48a25e3b2c2f689fdc71.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**exp1-random-b03-s44-r2 状态：**

- **进程存活**：PID 51297，已运行 21h28m
- **当前进度**：step 136/500（27.2%），最新 timestamp 01:03:53 UTC
- **指标**：prove_rate=0.75, isr_mean=0.040, parse_rate=1.0
- **速度**：~20s/step → 预计剩余 ~2h 完成（约 UTC 03:10）
- **GPU 占用**：
  - cuda:0 — PID 58051, 85050 MiB（另一个训练）
  - cuda:1 — PID 51297, 80318 MiB（本实验）

两张 GPU 均在使用，无冲突。

---
