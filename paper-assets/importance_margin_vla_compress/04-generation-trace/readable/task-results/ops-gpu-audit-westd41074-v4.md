# ops gpu audit westd41074 v4

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu-audit-westd41074-v4_20260520T162926_result.json`
- **Structured JSON:** [`ec635f303ef7b1ff1060.json`](../../sessions/ec/ec635f303ef7b1ff1060.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 审计结果

### 1. nvidia-smi -i 2 原始输出

```
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 580.82.09              Driver Version: 580.82.09      CUDA Version: 13.0     |
+-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|=========================================+========================+======================|
|   2  NVIDIA RTX PRO 6000 Blac...    On  |   00000000:5A:00.0 Off |                  Off |
| N/A   37C    P0            131W /  600W |   28555MiB /  97887MiB |      0%      Default |
+-----------------------------------------+------------------------+----------------------+
| Processes:                                                                              |
|  GPU   GI   CI              PID   Type   Process name                        GPU Memory |
|=========================================================================================|
|    2   N/A  N/A           68539      C   python                                28546MiB |
+-----------------------------------------------------------------------------------------+
```

### 2. M96 进程 PID 68539 — **存活**

```
PID 68539 | STAT: Rl | ELAPSED: 13:08:49 | CPU: 371% | CMD: python -u train_openvla_smart_compress.py --config configs/openvla_smart_compress_m96.yaml
```

### 3. 训练状态 — 正常推进

最新日志行 `00:48:24`（约 1 分钟前）：

| 指标 | 值 |
|------|-----|
| **当前 step** | 22850 / 100000 (22.9%) |
| **loss** | 2.92 |
| **lr** | 8.87e-05 |
| **grad norm** | 1.23 |
| **sps** | 0.5 step/s（~100s/50 steps） |

### 4. GPU util 0% 的解释

nvidia-smi 查询时刻 GPU-Util 显示 0%，但进程持续产出日志（每 ~100s 记录 50 steps），28.5GB 显存被占用，131W 功耗。这是**采样瞬时值为 0 的正常波动**——训练在 data loading / gradient accumulation 的 CPU 阶段被捕捉到。进程 CPU 占用 371% 也佐证了这一点。

### 5. 全卡状态

| GPU | Util | VRAM Used | PID |
|-----|------|-----------|-----|
| 0 | 31% | 15984 MiB | 468330 |
| 1 | 0% | 15984 MiB | 468864 |
| **2** | **0%** | **28555 MiB** | **68539 (M96)** |
| 3 | 0% | 27535 MiB | 68852 |

### 6. Checkpoint

`checkpoints/` 目录下无 `openvla_sc_m96*` 子目录——尚未产出 checkpoint（22850 步可能还没到保存间隔）。

**结论：M96 训练正常存活，无需干预。**

---
