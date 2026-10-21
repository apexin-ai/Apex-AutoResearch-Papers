# infra vanilla training health

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_vanilla-training-health_20260520T091006_result.json`
- **Structured JSON:** [`31aab726ba7552e65b33.json`](../../sessions/31/31aab726ba7552e65b33.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 健康检查报告

### 进程状态：3/3 存活

| Run | GPU | Seed | 当前 Step | 总 Steps | 已运行 | 平均速度 |
|-----|-----|------|-----------|----------|--------|----------|
| vanilla_s0 | GPU 0 | 42 | 1845 | 50005 | 1h25m | 2.78 s/it |
| vanilla_s1 | GPU 1 | 43 | 1855 | 50005 | 1h25m | 2.76 s/it |
| vanilla_s2 | GPU 2 | 44 | 1922 | 50005 | 1h26m | 2.68 s/it |

### GPU 状态

| GPU | 显存占用 | 利用率 | 温度 |
|-----|----------|--------|------|
| 0 | 67.9 / 97.9 GB | 0%* | 44°C |
| 1 | 62.8 / 97.9 GB | 0%* | 42°C |
| 2 | 62.2 / 97.9 GB | 0%* | 44°C |
| 3 | 空闲 | 0% | 31°C |

*nvidia-smi 是瞬时快照，训练在推进说明 GPU 实际有工作。速度波动大（1~5 s/it）暗示**数据加载 I/O 瓶颈**，GPU 在等数据。

### 异常检查
- **NaN / OOM / Killed：无**
- 只有 TensorFlow CropAndResize 的 PredictCost warning（无害，来自数据管线）

### Loss
**日志中无 loss 值**。WANDB_MODE=disabled，tqdm 进度条也没有 loss 后缀。当前无法追踪训练质量。

### Checkpoint
**尚未保存任何 checkpoint**（save_freq=10000，当前才 ~1900 步）。首次保存预计在 step 10000（约 6h 后）。

### 关键风险：timeout 不足

训练命令有 `timeout 64800`（18 小时）限制：
- 按当前 ~2.75 s/it，18h 内最多跑 **~23,600 步**
- 50,005 步需要 **~38 小时**
- 训练将在 **May 21 ~09:45** 被 kill，只完成约 **47%**

需要处理 timeout 问题，否则 3 个 run 都会中途被杀。

---
