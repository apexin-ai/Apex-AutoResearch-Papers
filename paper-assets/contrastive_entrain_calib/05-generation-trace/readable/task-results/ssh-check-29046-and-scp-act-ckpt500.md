# ssh check 29046 and scp act ckpt500

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check-29046-and-scp-act-ckpt500_20260522T060635_result.json`
- **Structured JSON:** [`529b50fa42bba2133471.json`](../../sessions/52/529b50fa42bba2133471.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

682M，完整匹配。汇总：

---

## 训练进度

| 实验 | 当前 step | 进度 | 速度 | 预计剩余 |
|------|----------|------|------|---------|
| **exp-003-s2** (R3-only seed2, GPU0) | **6690/8000** | 83.6% | ~26s/step | ~9.5h |
| **exp-004-s2** (ACT seed2, GPU1) | **720/8000** | 9.0% | ~9.5s/step | ~19.2h |

**GPU 状态：** GPU0 38049 MiB (0% util 瞬时), GPU1 23365 MiB (10% util)

## Checkpoint 情况

- **exp-004-s2 checkpoint-500**: 已存在 (682M, adapter LoRA checkpoint)
- **exp-003-s2**: 无 checkpoint 输出（输出目录 `exp-003-r3only-s2` 不存在，可能 checkpoint 存在其他路径或未配置 save）

## SCP 结果

checkpoint-500 已成功 SCP 到 28034：
`/root/autodl-tmp/checkpoints/exp004_s2/checkpoint-500/` (682M, 10 文件, 完整匹配源端)

---
