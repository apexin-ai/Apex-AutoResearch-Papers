# launch mf3 westb0 v2

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_launch_mf3_westb0_v2_20260522T080559_result.json`
- **Structured JSON:** [`2a5c023e89f8f6447711.json`](../../sessions/2a/2a5c023e89f8f6447711.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**GPU 0 当前被 SFT recovery 占用**（PID 162850，`sft_recovery.py`，模型 `pruned_rasp_alpha3p0_20`，输出 `sft_rasp_alpha3p0_20`），显存 51.5 GiB。

GPU 0 不空闲，无法立即启动 MF3 GRPO。选项：

1. **等 SFT 跑完后启动** — 我可以监控日志看进度
2. **杀掉 SFT 进程腾出 GPU 0** — 需要你确认
3. **用其他服务器的空闲 GPU** — 如 westd-29022

怎么处理？

---
