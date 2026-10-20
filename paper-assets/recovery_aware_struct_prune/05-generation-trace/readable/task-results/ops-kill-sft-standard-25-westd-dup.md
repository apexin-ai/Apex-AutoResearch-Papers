# ops kill sft standard 25 westd dup

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill_sft_standard_25_westd_dup_20260516T070223_result.json`
- **Structured JSON:** [`20d01d36f18ad8e7e400.json`](../../sessions/20/20d01d36f18ad8e7e400.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

westd-11672 上没有 sft_standard_25 / sft_recovery 的重复进程。当前运行的是：

- **eval_sft_rasp_25**（PID 92690）：在 cuda:0 上跑 `eval_gsm8k.py`，评估 sft_rasp_25 模型，已运行约 44 分钟，GPU 利用率 98%。
- **cuda:1**：空闲，0MB 显存占用。

sft_standard_25 的重复副本看起来已经不存在了（可能已自行退出或被之前 kill 掉了）。无需额外操作。

---
