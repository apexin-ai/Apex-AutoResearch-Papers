# submit 1 7b isr b01

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_submit_1_7b-isr-b01_20260516T211151_result.json`
- **Structured JSON:** [`d4a7203017690bbf6792.json`](../../sessions/d4/d4a7203017690bbf6792.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练已成功启动并在运行中。

**汇报：**

- **tmux session**: `isr_b01_1_7b`
- **PID**: 960894（GPU-0，`GPU-bee2603b-...`）
- **GPU 显存占用**: 39588 MiB / 97887 MiB（GPU-0）
- **训练状态**: 已开始跑 step，step 1 reward=0.54, step 2 reward=0.0，约 9-14s/it，预估总时间 ~1.5h
- **配置确认**: `CUDA_VISIBLE_DEVICES=0`，数据 `train_500_seed42.jsonl`，`additive_bonus` mode，β=0.1，500 steps

GPU-1 上 `isr_1_7b` session 也在正常运行（PID 921785, 42566 MiB）。两卡互不干扰。

---
