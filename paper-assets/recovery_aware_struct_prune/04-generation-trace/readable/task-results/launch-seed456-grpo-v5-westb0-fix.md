# launch seed456 grpo v5 westb0 fix

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_launch_seed456_grpo_v5_westb0_fix_20260522T130528_result.json`
- **Structured JSON:** [`f8fad6209df0e8df5ed3.json`](../../sessions/f8/f8fad6209df0e8df5ed3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Training started successfully. Here's the summary:

---

**Kill 确认**: PID 205670 已 kill (SIGTERM, clean exit). 错误输出目录已清理。

**新 PID**: **209508** (bash wrapper 209503, python 实际进程 209508)

**nvidia-smi**:
- GPU 0: PID 209508 — **40,348 MiB** (train_grpo_v5.py, seed456)
- GPU 1: PID 202364 — 29,636 MiB (其他实验)

**超参数确认** (日志 21:09:56):
- `beta=0.01` ✓
- `loss_type=dapo` ✓
- `temperature=0.4` ✓
- `repetition_penalty=1.15`
- `format_reward=0.1`
- `optimizer: adamw_8bit`
- `max_steps=100`

**W&B run**: `grpo_sft_random_20` (run ID: `auv9riek`)

**磁盘**: `/root/autodl-tmp/` 239G/250G used (12G free) — 偏紧，但 GRPO checkpoint 应该够用。

训练已开始 (0/100 steps)，运行正常。

---
