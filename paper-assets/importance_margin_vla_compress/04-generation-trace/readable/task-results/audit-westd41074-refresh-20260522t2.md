# audit westd41074 refresh 20260522T2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_westd41074_refresh_20260522T2_20260522T203133_result.json`
- **Structured JSON:** [`2358de3afe3e32eb8b0d.json`](../../sessions/23/2358de3afe3e32eb8b0d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-41074 审计报告

### 四卡状态

| GPU | 显存 | 利用率 | 进程 | 实验 | 进度 |
|-----|------|--------|------|------|------|
| cuda:0 | 10.9/97.9 GB | 24% | PID 3789 (1h21m) | π0.5 Random k=0.85 Long seed42 | Task 4/10 (T4 ep30, 当前56.0%) |
| cuda:1 | 10.5/97.9 GB | 49% | PID 3863 (1h21m) | π0.5 Random k=0.7 Long seed42 | Task 5/10 (T5 ep20, 当前76.0%) |
| cuda:2 | 10.6/97.9 GB | 12% | PID 57623 (24m) | π0.5 Random k=0.5 Long seed42 | Task 1/10 (T1 ep20, 72.0%) |
| cuda:3 | 27.5/97.9 GB | 0% | PID 59671 (1d11h) | OpenVLA SC M64 v6 训练 | **Step 73750/100000 (73.8%)** |

**全部 GPU 占满，无法部署新实验。**

### 收割结果

新完成 1 个实验，已注册：

| 实验 | Suite | SR | 备注 |
|------|-------|-----|------|
| **L2Norm k=0.9 Long seed42** | libero_10 | **81.0%** | T6=10% 拖后腿，其余 task 84-100% |

### M64 v6 训练进度

- Step 73750/100000 (73.8%), loss ~2.5-2.9, lr=1.85e-05, sps=0.6
- 每 50 step ≈ 1.4min → 剩余 ~26250 步 ≈ **12.3 小时**完成（约明天 16:45）
- 训练稳定，无异常

### Tmux Sessions

- `eval_pi05_random_k085_long_seed42` — 活跃 (cuda:0)
- `eval_pi05_random_k07_long_seed42` — 活跃 (cuda:1)
- `smolvla_spatial` — **空闲**（已完成）
- `xvla_long` — **空闲**（已完成）
- `train_m64v6` — 活跃 (cuda:3)

PID 57623 (Random k=0.5 Long) 是通过 nohup 启动的，没有对应 tmux session。

### 待部署队列

GPU 释放后（预计各 Long eval 还需 ~1.5-2h）按优先级部署：
1. π0.5 Long Random k=0.3 seed42
2. π0.5 Long L2norm k=0.7 seed42
3. π0.5 Long L2norm k=0.5 seed42

---
