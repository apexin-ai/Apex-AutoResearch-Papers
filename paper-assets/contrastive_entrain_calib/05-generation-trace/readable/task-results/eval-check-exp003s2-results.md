# eval check exp003s2 results

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_check-exp003s2-results_20260525T133531_result.json`
- **Structured JSON:** [`603070f331a479c26240.json`](../../sessions/60/603070f331a479c26240.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

当前状态：

- **ckpt2500 eval**：80/362 完成（~22%），PID 33822 仍在运行。已杀掉重复进程，GPU 0 现在只有一个 eval 占用。
- **ckpt3000 eval**：等 ckpt2500 完成后自动启动（在同一个 chained 命令中）。
- **GPU 0**：之前两个进程共用，现在只有一个，速度会加快。

按之前速率（20 samples / ~5 min），剩余 282 samples 约需 **~70 分钟**完成 ckpt2500。之后 ckpt3000 还需 **~90 分钟**。两个 eval 全部完成预计需要 **~2.5 小时**（约 UTC 00:00 左右）。

需要我稍后再来检查结果并更新 registry 吗？

---
