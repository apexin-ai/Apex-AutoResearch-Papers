# launch grpo random seed456 westb0

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_launch_grpo_random_seed456_westb0_20260522T120101_result.json`
- **Structured JSON:** [`858e33a140c6a9c5c22d.json`](../../sessions/85/858e33a140c6a9c5c22d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**无法启动 GRPO，sft_random_20 模型不可用。**

现状：
- **westb-23072**: `sft_random_20` 目录不存在（只有 `grpo_random_20/completions` 残留）
- **westd-32935**: 从 westb SCP 时无法解析主机名
- **westd-29022**: 连接失败（端口不通，可能已关机）

GPU/磁盘状态：
- **cuda:0**: 空闲（0MiB / 97887MiB）
- **cuda:1**: 被占用（16547MiB, 99% util, PID 179898）
- **磁盘**: `/root/autodl-tmp/` 29GB free（250G 总量）

需要你提供 sft_random_20 模型的可用来源，或者确认 westd 服务器状态后重试。

---
