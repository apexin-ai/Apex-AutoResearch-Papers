# ops check exp008v3 training detail

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-exp008v3-training-detail_20260519T113811_result.json`
- **Structured JSON:** [`6878193dd92e249df17d.json`](../../sessions/68/6878193dd92e249df17d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp-008v3 训练状态报告

### 进度
- **当前 step**: ~894 / 8000 (**11.2%**)
- **已运行**: 4h 56m
- **ETA**: ~41h (预计 5/21 中午前后完成)
- **速度**: ~21-22s/step

### 指标趋势 (step 800-894)

| Step | R1 mean | R3 mean | Combined mean |
|------|---------|---------|---------------|
| 800  | 0.50-0.63 | — | 0.44-0.50 |
| 820  | 0.25-0.38 | — | 0.62-0.65 |
| 840  | 0.25-0.75 | — | 0.53-0.65 |
| 860  | 0.38-0.75 | — | 0.56-0.66 |
| 880  | 0.63-0.75 | — | 0.40-0.72 |
| 890  | 0.75 | 0.50-0.74 | 0.56-0.74 |
| 894  | 0.88 | 0.25-0.50 | 0.41-0.59 |

- **R1 (Binary Probe)**: 波动较大 (0.25-1.0)，近期趋势向好，最新几步多在 0.75-1.0 范围，**符合预期 (>0.3)**
- **R2**: 恒为 0.0（正常，这个阶段未激活）
- **R3**: 0.25-0.74 范围波动
- **Combined**: 0.40-0.74，整体在 0.5 附近震荡
- **Loss**: 0.0（GRPO 典型表现）
- **Entropy**: 0.58（健康，未崩塌）

### GPU 状态
- GPU 1: **100%** 利用率, 31432 MiB
- GPU 2: **100%** 利用率, 30670 MiB
- 双卡满载运行，正常

### Checkpoints
- `/root/contrastive_entrain_calib/checkpoints/exp008v3_binary_probe_grpo/checkpoint-500`
- `probe_step500.pt` (probe 模块单独保存)
- 目前仅保存了 step 500 的 checkpoint，下一个预计在 step 1000

### 异常信号
- **无异常**。R1 波动大是 binary probe reward 的固有特性（batch 内只有几个样本，0/0.25/0.5/0.75/1.0 离散值）。宏观趋势向上，entropy 健康，训练稳定。

---
