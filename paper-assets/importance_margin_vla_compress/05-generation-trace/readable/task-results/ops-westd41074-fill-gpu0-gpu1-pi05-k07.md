# ops westd41074 fill gpu0 gpu1 pi05 k07

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd41074-fill-gpu0-gpu1-pi05-k07_20260521T093000_result.json`
- **Structured JSON:** [`b6f3c1bc8c97ecc0c2e7.json`](../../sessions/b6/b6f3c1bc8c97ecc0c2e7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

L2norm k=0.7 已成功启动（PID 68573 on GPU 0, 10487 MiB），正在初始化 LIBERO 环境。

---

## 产出汇总

### 1. 部署实验

| GPU | PID | 实验 | 显存 | 状态 |
|-----|-----|------|------|------|
| 0 | 68573 | **π0.5 L2norm k=0.7** seed42 | 10487 MiB | 刚启动，初始化 suite |
| 1 | — | **空闲** | — | — |
| 2 | 68539 | M96 VTC 训练 | 28546 MiB | step 52650/100K |
| 3 | 51513 | **π0.5 random k=0.7** seed42 | 10487 MiB | T0=90%, T1=82%, T2 进行中 |
| 3 | 59671 | M64v6 VTC 训练 | 27464 MiB | step 400/100K |

### 2. 启动验证

- **L2norm k=0.7**: 模型加载完成，Suite libero_object 10 tasks 已初始化 ✅
- **Random k=0.7** (已有): 活跃评估中，当前 86/100=86.0% ✅

### 3. VTC 训练状态

- **M96** (PID 68539, GPU 2): 正常训练中，step 52650/100K (52.6%), loss ~2.7, sps=0.5, 运行 1d5h50m。nvidia-smi 显示 0% GPU util 是瞬时快照，日志确认持续训练中。
- **M64v6** (PID 59671, GPU 3): 正常训练中，step 400/100K, loss 16.2→3.4（快速下降期），sps=0.6，启动约 15 分钟。日志在 `logs/train_m64v6.log`（不是 v5/v6 命名模式）。stdout 输出到 pipe 而非文件，但 log 文件有记录。
- **Reviewer 报告的 0% GPU util**：两个训练进程的 CPU 使用率很高（M96: 333%, M64v6: 1555%），日志持续更新 — 很可能是 nvidia-smi 采样时恰好在做 CPU 侧计算（数据加载/预处理），并非卡死。

### 4. 情况 A 执行

PID 51513 (random k=0.7) 在 GPU 3 上正常运行，已跑 20 分钟且成绩优秀（86%）。因此 GPU 0 部署了 L2norm k=0.7，GPU 1 保持空闲。两个实验均已注册到 registry 为 RUNNING 状态。

---
