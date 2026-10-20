# monitor full gpu status

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_full-gpu-status_20260514T022119_result.json`
- **Structured JSON:** [`0ef93efb24f56779bb2e.json`](../../sessions/0e/0ef93efb24f56779bb2e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 训练状态总览

### GPU 占用

| GPU | 利用率 | 显存占用 | 温度 |
|-----|--------|----------|------|
| 0 | 99% | 46.5/97.9 GB | 57°C |
| 1 | 99% | 44.1/97.9 GB | 57°C |
| 2 | 64% | 44.1/97.9 GB | 58°C |
| 3 | 99% | 44.1/97.9 GB | 59°C |

### 实验状态

| 实验 | GPU | PID | 状态 | 进度 | 当前 Loss | 总 Steps | 最新 Checkpoint | 预计剩余 |
|------|-----|-----|------|------|-----------|----------|-----------------|----------|
| uniform_seed42 | cuda:1 | 47603 | **运行中** (2h57m) | 5497/6103 (90%) | 7.8111 | 6103 | ckpt-5000 (1.2G) | ~21 min |
| uniform_seed123 | cuda:2 | 47749 | **运行中** (2h57m) | 5475/6103 (90%) | 8.0342 | 6103 | ckpt-5000 (1.2G) | ~22 min |
| uniform_seed456 | cuda:3 | 47890 | **运行中** (2h57m) | 5482/6103 (90%) | 7.3564 | 6103 | ckpt-5000 (1.2G) | ~22 min |
| grid_b_seed42 | cuda:0 | 50134 | **运行中** (2h31m) | 4245/6103 (70%) | 9.671 | 6103/b值 | ckpt-4000 (1.2G) | 见下方 |

### grid_b 详情

- **当前 b 值**: b=0.5（6 个值中的第 1 个）
- b 值队列: **0.5** (进行中) → 1.0 → 1.5 → 2.0 → 3.0 → 5.0
- 当前 b=0.5 剩余: ~1858 steps ≈ **66 min**
- 后续 5 个 b 值各约 3.6h，**总剩余约 19 小时**

### Checkpoint 磁盘

| 目录 | 大小 | 保留的 Checkpoint |
|------|------|--------------------|
| uniform_seed42 | 2.3G | ckpt-4500, ckpt-5000 |
| uniform_seed123 | 2.3G | ckpt-4500, ckpt-5000 |
| uniform_seed456 | 2.3G | ckpt-4500, ckpt-5000 |
| grid_b0_5_seed42 | 2.3G | ckpt-3500, ckpt-4000 |

### 要点

1. **3 个 uniform 实验均未完成**，都在 90% 左右，约 20 分钟后全部完成
2. **grid_b 刚完成第 1 个 b 值的 70%**，整个 grid 搜索预计还需 ~19 小时
3. 所有日志中**未出现 "Training completed" 标记**
4. save_total_limit=2 生效，每个实验保留 2 个 checkpoint

---
