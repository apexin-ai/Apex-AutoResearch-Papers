# check cqa1 seed1 crash

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_cqa1_seed1_crash_20260517T004008_result.json`
- **Structured JSON:** [`fcf56ab4b5daf29e45af.json`](../../sessions/fc/fcf56ab4b5daf29e45af.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练进程**没有崩溃**，仍在正常运行。

```
=== GPU 0 状态 ===
进程: alive (PID 45551, 启动于 05:34, 已运行 ~3h)
GPU 显存: 2744MiB / 24564MiB 占用中
GPU 利用率: 37%

=== 训练状态 ===
tmux session: libero_fullft_seed1 (created Sun May 17 05:34:16 2026)
命令: python train.py --config configs/libero_full_ft_seed1.yaml --gpu 0 --seed 1 --wandb_run libero_fullft_seed1
子进程: 4 个 worker (PIDs 47312-47315)，CPU 使用 ~99%（数据加载中）

=== 其他 GPU 状态 ===
GPU 1: 空闲
GPU 2: 4129MiB 占用, 98% 利用率 (libero_imm_fullft_k07 或 seed0)
GPU 3: 4131MiB 占用, 67% 利用率
```

训练没有崩溃，正在正常跑。GPU 0 显存占用较低 (2753MiB) 且利用率 37%，可能处于数据预处理/加载阶段，或者模型较小。需要我检查日志看当前训练到第几步了吗？

---
