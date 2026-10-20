# check gpu and adaptive fix progress

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_gpu_and_adaptive_fix_progress_20260514T171906_result.json`
- **Structured JSON:** [`0bf0a26140ab33a864c3.json`](../../sessions/0b/0bf0a26140ab33a864c3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 状态 (nvidia-smi)

| GPU | PID | 显存使用 | GPU-Util | 温度 |
|-----|-----|---------|----------|------|
| 0 | 112475 (python) | 46.5G / 95.6G | 99% | 56°C |
| 1 | 108213 (python) | 75.0G / 95.6G | 68% | 62°C |
| 2 | 109362 (python) | 75.0G / 95.6G | 100% | 60°C |
| 3 | 115071 (python) | 75.0G / 95.6G | 85% | 65°C |

注意：GPU 0 的 PID 从 50134 变为 112475，说明 grid_b_batch 可能已重启或进入了新的 b 值子进程。

## adaptive_fix 训练进度

日志中 tqdm 总步数为 **8477**（非 6103，可能配置不同或含 warmup/eval 迭代）：

| exp_id | current / total | 进度 | speed | ETA |
|--------|----------------|------|-------|-----|
| adaptive_fix_seed42 (GPU 1) | 7755 / 8477 | 91% | ~3.2 it/s | **~3.8 min** |
| adaptive_fix_seed123 (GPU 2) | 5999 / 8477 | 71% | ~3.2 it/s | **~12.9 min** |
| adaptive_fix_seed456 (GPU 3) | 7871 / 8477 | 93% | ~3.25 it/s | **~3.1 min** |

seed456 和 seed42 即将完成（~3-4 min），seed123 还需 ~13 min。

## grid_b_seed42_batch 进度 (GPU 0)

当前 b 值: **3.0**, step: **4241 / 6103** (69%), 速度 2.12 s/it, ETA **~66 min**

已完成的 b 值（从 output 目录看）：b=0.5, 1.0, 1.5, 2.0 (seed42) 均有完整输出。b=3.0 正在训练中（只有 checkpoint-500，无 final model）。

## 已完成未收割

**无。** 三组 adaptive_fix 均仍在训练中：
- seed42: checkpoint-500, checkpoint-1000 已保存，训练继续中
- seed123: checkpoint-500, checkpoint-1000 已保存，训练继续中
- seed456: checkpoint-500 已保存，训练继续中

seed456 和 seed42 预计 ~3-4 分钟内完成，届时可收割。

---
