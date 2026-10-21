# ops cuda0 check

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cuda0_check_20260522T084725_result.json`
- **Structured JSON:** [`4d28e66485dbd2fceaae.json`](../../sessions/4d/4d28e66485dbd2fceaae.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告：

### 1. cuda:0 状态
- **显存**: 49175 MiB / 97887 MiB（约 50%）
- **Utilization**: **0%**
- **温度**: 29°C, P8 功耗状态 (34W/600W)
- **无计算进程在 cuda:0 上运行**

cuda:0 显存被占了约 49GB 但 GPU-Util 为 0%，且 nvidia-smi 未列出任何 cuda:0 上的进程。这通常是因为 **cuda:1 上的进程（PID 782378）在启动时也在 cuda:0 上分配了部分显存**（PyTorch 默认行为，即使 `--gpu 0` 指定的是逻辑 GPU）。

### 2. cuda:0 占用进程
nvidia-smi 显示 cuda:0 上**没有 compute 进程**。唯一的 GPU 进程是 PID 782378，挂在 cuda:1。

### 3. cuda:1 上的进程（gradient_masking 实验）
- **PID**: 782378
- **进程**: `/root/miniconda3/bin/python train/train_sft.py`
- **参数**: `--condition exception_only --gpu 0 --gradient_mask_ratio 0.998 --gradient_checkpointing --seed 42 --wandb_run_name gradient_masking_qwen7b_seed42`
- **显存**: 71278 MiB（在物理 GPU 1 上）
- **GPU-Util**: 100%, 70°C, 488W
- **tmux session**: `gradient_masking_qwen7b_seed42`（创建于 16:04）
- **运行时长**: ~43 分钟

### 4. 结论
- **cuda:0 空闲可用**，0% utilization，无活跃计算进程。49GB 显存占用可能是 PyTorch CUDA context 的副作用。
- **cuda:1 上 gradient_masking 实验正常运行中**，GPU 满载。

---
