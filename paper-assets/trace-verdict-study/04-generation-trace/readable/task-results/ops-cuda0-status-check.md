# ops cuda0 status check

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cuda0_status_check_20260522T090814_result.json`
- **Structured JSON:** [`95b611db1d90b1558af0.json`](../../sessions/95/95b611db1d90b1558af0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

**cuda:0** — 49175MiB / 97887MiB, **0% utilization**, 无进程。这仍是之前的孤儿显存（49GB），状态未变——并非 Director 说的 85GB/100%。

**cuda:1** — 71287MiB / 97887MiB, **98% utilization**。正在运行 `gradient_masking` 训练：
- PID: 782378
- 命令: `/root/miniconda3/bin/python train/train_sft.py --condition exception_only --gpu 0 --gradient_mask_ratio 0.998 --gradient_checkpointing --seed 42 --wandb_project trace-verdict-study --wandb_run_name gradient_masking_qwen7b_seed42 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/gradient_masking_qwen7b_seed42`
- 工作目录: `/root/trace-verdict-study`

注意：命令行参数写的是 `--gpu 0`，但实际跑在 **物理 GPU 1** 上（可能通过 `CUDA_VISIBLE_DEVICES` 映射）。

**总结**：Director 可能看反了两张卡。cuda:0 仍然是 49GB 孤儿显存 + 0% util；cuda:1 是 gradient_masking 训练在跑，状态正常。

---
