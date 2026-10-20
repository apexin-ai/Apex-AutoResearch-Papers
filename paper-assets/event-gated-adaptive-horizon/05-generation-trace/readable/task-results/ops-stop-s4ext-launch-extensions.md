# ops stop s4ext launch extensions

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_stop-s4ext-launch-extensions_20260519T090137_result.json`
- **Structured JSON:** [`19d6286940659d3d6cee.json`](../../sessions/19/19d6286940659d3d6cee.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个任务全部完成。

**任务 A** — `exp_023_cheetah_baseline_s4_extended` 已通过 Ctrl-C 停止（tmux session `exp_023_s4_ext` 已退出），registry 更新为 DONE/success，metrics 已录入。

**任务 B** — `exp_001_baseline_s3_extended` 在 cuda:0 运行中，seed=3，从 120K step resume，目标 505K。tmux session: `exp_s3_ext`。

**任务 C** — `exp_001_baseline_s4_extended` 在 cuda:1 运行中，seed=4，从 112K step resume，目标 505K。tmux session: `exp_s4_ext`。与 `exp_s2_ext` 共享 cuda:1。

当前服务器 tmux sessions: `exp_s2_ext`（cuda:1）、`exp_s3_ext`（cuda:0）、`exp_s4_ext`（cuda:1）。

---
