# diagnose repo level cwm 8b conda

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_repo-level-cwm-8b-conda_20260514T141833_result.json`
- **Structured JSON:** [`7db581d3838824d251d5.json`](../../sessions/7d/7db581d3838824d251d5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断报告：`repo-level-cwm-8b-conda`

### 失败根因

```
RuntimeError: DataLoader worker (pid 241561) is killed by signal: Terminated.
```

DataLoader worker 收到 **SIGTERM**（非 OOM 的 SIGKILL），发生在 **eval 阶段**（evaluation_loop 迭代 dataloader 时，eval progress 39% = 3669/9335 samples）。

SIGTERM 说明是外部进程主动发送的终止信号，而非内存不足被内核杀死。结合两个 8B 实验在 **< 10s 内同时崩溃**，确认是 **服务器级事件**（实例被回收/抢占、资源管理器强制终止等），不是代码 bug。

### 训练进度

| 指标 | 值 |
|------|-----|
| 总步数 | 6633 |
| 崩溃时步数 | **1300**（正在做 step 1300 的 eval） |
| 进度 | **~20%** |
| Epoch | ~0.54（eval）/ ~0.59（train） |
| 最后 train loss | 0.5461 (grad_norm=11.74) |
| 最后 eval loss | **0.3565**（step 1300 eval） |
| 运行时间 | ~8h21m |

### 已保存 Checkpoints

| Checkpoint | 时间 |
|------------|------|
| checkpoint-400 | May 14 16:32 |
| checkpoint-900 | May 14 19:49 |
| checkpoint-1000 | May 14 20:29 |
| checkpoint-1100 | May 14 21:08 |
| **checkpoint-1200** | **May 14 21:47** |

最新 checkpoint-1200 文件完整（adapter_model.safetensors 58MB + optimizer.pt 117MB + scheduler/rng/trainer_state 均在）。

### 磁盘状态

| 分区 | 容量 | 已用 | 可用 | 使用率 |
|------|------|------|------|--------|
| /root/autodl-tmp | 250G | 133G | 118G | 54% |
| / | 30G | 20G | 11G | 64% |

**磁盘充足，非磁盘满导致。**

### 与 CLS 8B 是否同一根因

**是。** 两个实验在几乎同一时刻被 SIGTERM 终止，且都不是 OOM/CUDA error/磁盘满，确认是同一个服务器级外部事件。

### 恢复方案

可以从 **checkpoint-1200** 恢复，损失约 100 步（~20 分钟训练时间）：

```bash
python3 train_repo_cwm.py \
  --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/ \
  --device cuda:0 \
  --batch_size 1 \
  --grad_accumulation 32 \
  --seed 42 \
  --no_wandb \
  --output_dir /root/autodl-tmp/checkpoints_repo_cwm_8b_conda/ \
  --resume_from_checkpoint /root/autodl-tmp/checkpoints_repo_cwm_8b_conda/checkpoint-1200
```

恢复前建议先确认服务器实例状态稳定（检查是否为竞价实例被回收，或是否有维护通知）。

---
