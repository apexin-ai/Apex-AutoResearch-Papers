# exp replace dup 69b interv

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_replace_dup_69b_interv_20260518T175646_result.json`
- **Structured JSON:** [`86efd3487dea637089cd.json`](../../sessions/86/86efd3487dea637089cd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验稳定运行约 4 分钟，日志持续增长（interv: 12.6K→19.4K, 6.9B: 5.4K→8K），无 OOM。

## 产出汇总

| 项目 | 结果 |
|---|---|
| **Kill** | cuda:0 (scale_14b_a050_s42_bf16 PID 15222) 和 cuda:2 (alpha_sweep_a010_s42_bf16 PID 16858) 已终止，GPU 释放 |
| **6.9B dry-run** | 38695 MiB / 97887 MiB (40%)，batch_size=4 + gradient_checkpointing + bf16 无 OOM |
| **batch_size** | 确认 `--batch_size 4`（参数名是 `--batch_size` 非 `--per_device_train_batch_size`） |
| **scale_69b_a100_s42** | PID 29028, cuda:0, 38695 MiB, 87-93% util |
| **interv_pred_s43_bf16** | PID 29174, cuda:2, 2503 MiB, 43-54% util |
| **Gen 1 训练** | 两个实验仍在 Gen 0 生成阶段（6.9B 生成 5k 样本较慢，预计需 15-30 分钟）|

其他实验（GPU 1/3/4/5）未受影响，正常运行。tmux server 在 kill 过程中崩溃，但所有进程已脱离 tmux 独立运行（新提交的两个实验通过 submit_training_job 重建了 tmux session）。

---
