# train imm fullft seed0 cqa1

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_imm_fullft_seed0_cqa1_20260516T225210_result.json`
- **Structured JSON:** [`df2e0271e46168c5c2b0.json`](../../sessions/df/df2e0271e46168c5c2b0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练已成功启动并运行。

## 确认结果

**配置文件**: `configs/libero_imm_twostage_fullft_seed0.yaml`
- `baseline_checkpoint`: `checkpoints/libero_full_ft_seed0/step_099999/checkpoint.pt`
- `output_dir`: `checkpoints/libero_imm_twostage_fullft_seed0`
- seed=0 通过 CLI `--seed 0` 传入

**GPU 状态**: cuda:2 使用 2881 MiB，正常

**训练状态**: Stage 1 已开始
- step=50/10000, margin_loss=0.2983, lr=3.06e-05, grad=8.04, sps=3.6
- ACIS 参数: 3.46M trainable (0.76%), expert 全冻结

---
