# diagnose gpu allocation check

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_gpu_allocation_check_20260515T011923_result.json`
- **Structured JSON:** [`7e06846894396df4c3a6.json`](../../sessions/7e/7e06846894396df4c3a6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 验证结果：GPU 隔离正确，无冲突

### 进程-GPU 映射

| 实验 | 父 PID | 实际 GPU PID | CUDA_VISIBLE_DEVICES | 物理 GPU | GPU UUID |
|------|--------|-------------|---------------------|---------|----------|
| exp_009a | 142508 | 142513 | **0** | GPU 0 | `GPU-f7b1...` |
| exp_008e_v3_s2 | 43437 | 43442 | **1** | GPU 1 | `GPU-7b49...` |

### GPU 利用率

| GPU | 利用率 | 显存使用 | 显存总量 |
|-----|--------|---------|---------|
| GPU 0 | 0% | 4722 MiB | 97887 MiB |
| GPU 1 | 5% | 4165 MiB | 97887 MiB |

- 另有一个 PID 908751 在 GPU 0 上占用 552 MiB（非实验进程，影响不大）

### 008e_v3_s2 训练进度

- metrics.jsonl 已有 **11 行**，最新 step = **8000**，train_return = 53.35
- 训练正常推进

### 结论

**不存在设备冲突。** 两个实验的 CUDA_VISIBLE_DEVICES 分别设为 0 和 1，nvidia-smi 确认它们分别运行在不同物理 GPU 上（不同 UUID），显存占用独立。监控 Worker 的冲突报告为误报。

---
