# ops cuda0 check

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cuda0_check_20260522T084608_result.json`
- **Structured JSON:** [`d5b00baf64d7b9281cca.json`](../../sessions/d5/d5b00baf64d7b9281cca.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告：

### 1. cuda:0 状态
- **显存**：49,175 MiB / 97,887 MiB（~50%）
- **GPU-Util**：0%
- **温度**：29°C，功耗 34W/600W
- **无进程在 cuda:0 上运行**。cuda:0 处于空闲状态，显存占用可能是之前实验的残留（未释放的缓存）或系统预留。

### 2. cuda:1 上的进程
- **PID**: 782378
- **命令**: `/root/miniconda3/bin/python train/train_sft.py --condition exception_only --gpu 0 --gradient_mask_ratio 0.998 --gradient_checkpointing --seed 42 --wandb_run_name gradient_masking_qwen7b_seed42`
- **实验**: `gradient_masking_qwen7b_seed42`
- **显存**: 71,278 MiB / 97,887 MiB
- **GPU-Util**: 100%，温度 71°C，功耗 485W/600W
- **CPU**: 102%，运行约 42 分钟（16:04 启动）

### 3. tmux sessions
- 唯一 session: `gradient_masking_qwen7b_seed42`（创建于 16:04:50）

### 4. gradient_masking 在 cuda:1 上的状态
**正常运行中。** 进程通过 `CUDA_VISIBLE_DEVICES=1` 映射到物理 GPU 1（代码内 `--gpu 0` 指的是可见设备中的第 0 个，即物理 cuda:1）。GPU 利用率 100%，显存占用 71GB，一切正常。

**结论**：cuda:0 空闲无进程，49GB 显存占用可能是缓存残留。cuda:1 正在全速跑 gradient_masking 实验。

---
