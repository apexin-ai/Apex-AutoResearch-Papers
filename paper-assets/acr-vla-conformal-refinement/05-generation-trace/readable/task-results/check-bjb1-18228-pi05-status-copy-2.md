# check bjb1 18228 pi05 status

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_bjb1-18228-pi05-status_20260525T040449_result.json`
- **Structured JSON:** [`1f42fdc74d9cb102704b.json`](../../sessions/1f/1f42fdc74d9cb102704b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## bjb1-18228 状态汇报

### GPU 占用

| GPU | 型号 | 利用率 | 显存占用 | 进程 |
|-----|------|--------|----------|------|
| 0 | RTX 4090 | 10% | 580/24564 MiB | — (非 GPU 计算进程) |
| 1 | RTX 4090 | 0% | 0/24564 MiB | **空闲** |
| 2 | RTX 4090 | 0% | 0/24564 MiB | **空闲** |
| 3 | RTX 4090 | 24% | 9883/24564 MiB | precompute_pi05_long (PID 114507) |

### π0.5 CRM 3-suite 训练（PID 326315，GPU 0）

- **进度**: Epoch 49/50，batch 250/684 — **即将完成**（还剩约 1.5 个 epoch）
- **Loss**: train_loss=0.0072, val_loss=0.0042（epoch 48 刷新 best）
- **Checkpoint**: `crm_best.pt` 已生成（May 25 11:58），最新 checkpoint 到 epoch 48
- 有 2 个子进程（PID 444876, 444877）是 DataLoader workers

### π0.5 precompute-long（PID 114507，GPU 3）

- **进度**: 102900/136090（**75.6%**）
- **速度**: 1.95s/sample
- **ETA**: ~64618s ≈ **约 18 小时**（预计 May 26 06:00 左右完成）

### 空闲 GPU

**GPU 1、GPU 2 完全空闲**，可立即使用。

---
