# eval urgent status 28034

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_urgent-status-28034_20260522T161846_result.json`
- **Structured JSON:** [`e1a2f8201eb5ac75295e.json`](../../sessions/e1/e1a2f8201eb5ac75295e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
=== westd-28034 ===
GPU0: 17660/32607 MiB  40%  eval exp004-s2-ckpt4000
GPU1: 26421/32607 MiB  50%  eval exp004s2-act-ckpt3500
GPU2:     2/32607 MiB   0%  空闲
GPU3: 16884/32607 MiB  49%  eval exp003s2-r3only-ckpt8000

D058 实验:
exp-003-len512:      未启动, 无进程, 无 log
exp-004-reduced-lora: 未启动, 无进程, 无 log
exp-003-s3:          未启动, 无进程, 无 log

Eval 进程 (3个 tmux session):
- eval_r3s2_ckpt8000  (cuda:3) — exp003s2_r3only/checkpoint-8000, PID 22138, 启动 May22 23:58
- eval_acts2_ckpt4000 (cuda:0) — exp004s2_act/checkpoint-4000,   PID 22909, 启动 00:04
- eval_acts2_ckpt3500 (cuda:1) — exp004s2_act/checkpoint-3500,   PID 24053, 启动 00:15
```

**D058 三个新实验均未启动**，服务器上没有对应进程也没有训练 log。GPU2 完全空闲，GPU0/1/3 被三个 eval 任务占用。

---
