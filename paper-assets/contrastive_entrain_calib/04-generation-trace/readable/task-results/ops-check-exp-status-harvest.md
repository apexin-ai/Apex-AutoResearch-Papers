# ops check exp status harvest

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-exp-status-harvest_20260525T204316_result.json`
- **Structured JSON:** [`4ef0c8c11be102e9830a.json`](../../sessions/4e/4ef0c8c11be102e9830a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp-003-s3 (R3-only GRPO seed 3)
- **状态**: 运行中
- **当前 step**: 952/8000 (12%)
- **速度**: ~25.5 s/step
- **已运行**: 3h14m
- **预估剩余**: ~49.7 小时
- **GPU**: cuda:1, 38134 MiB, 98% util
- **Checkpoints**: `/root/autodl-tmp/checkpoints/exp003_r3only_seed3/checkpoint-500` (resume 起点，当前仅此一个)
- **备注**: 全程 R3-only rewards（`d_syc not loaded` 是预期行为）

## exp-act-256-v2 (ACT consistency, 256 samples)
- **状态**: 运行中
- **当前 step**: 1670/8000 (21%)
- **速度**: ~6.9 s/step (每 10 步 ~69s)
- **已运行**: 3h15m (elapsed=11661s)
- **预估剩余**: ~12.1 小时
- **GPU**: cuda:0, 24198 MiB, 41% util
- **Checkpoints**: 
  - `/root/autodl-tmp/checkpoints/act_256_ablation/checkpoint-500`
  - `/root/autodl-tmp/checkpoints/act_256_ablation/checkpoint-1000`
  - `/root/autodl-tmp/checkpoints/act_256_ablation/checkpoint-1500` (刚保存)
- **最新 metrics**: sft_loss=0.0062, l2=0.0046, total=0.0066, lr=4.06e-05（loss 平稳下降）

---

**总结**: 两个实验都在正常运行。exp-act-256-v2 约明天凌晨完成；exp-003-s3 速度较慢（GRPO 生成开销），预计还需约 2 天。

---
