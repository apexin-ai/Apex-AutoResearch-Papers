# ops cuda0 check

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cuda0_check_20260522T084503_result.json`
- **Structured JSON:** [`fa7f560e1fa63693f195.json`](../../sessions/fa/fa7f560e1fa63693f195.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

### cuda:0 状态
- **显存**: 49175 MiB / 97887 MiB（50%）
- **Utilization**: 0%
- **无任何计算进程** — 49GB 是孤儿显存（之前某进程退出后未释放）

### cuda:1 状态
- **显存**: 71287 MiB / 97887 MiB（73%）
- **Utilization**: 100%
- **进程**: PID 782378，本项目的 gradient masking 实验
  - 命令: `train_sft.py --condition exception_only --gpu 0 --gradient_mask_ratio 0.998 --gradient_checkpointing --seed 42 --wandb_run_name gradient_masking_qwen7b_seed42`
  - 启动时间: 今天 16:04:50
  - tmux session: `gradient_masking_qwen7b_seed42`
  - 注意：脚本参数 `--gpu 0` 但实际通过 `CUDA_VISIBLE_DEVICES=1` 映射到物理 GPU 1

### cuda:0 孤儿显存
49GB 被占但没有对应进程，只能通过以下方式释放：
1. 重启实例（会中断 cuda:1 上正在跑的实验）
2. 等当前实验跑完后重启

### 建议
cuda:0 虽然可用（0% utilization），但 49GB 孤儿显存只剩 ~48GB 可用空间。对于 Qwen-7B 训练（需要 ~70GB）不够。**等 gradient masking 实验跑完后重启实例释放孤儿显存，之后 cuda:0 就有完整 97GB 可用。**

---
