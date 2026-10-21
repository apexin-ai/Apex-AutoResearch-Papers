# ops cuda0 orphan recovery

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cuda0_orphan_recovery_20260521T084409_result.json`
- **Structured JSON:** [`93fa3a3274236acf8afd.json`](../../sessions/93/93fa3a3274236acf8afd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**无法安全回收。** 原因：

PID 686085 同时持有 cuda:0 和 cuda:1，是同一个进程：

```
/root/miniconda3/bin/python train/train_sft.py --condition full_trace --gpu 0 --seed 123 ...
  --output_dir .../qwen7b_full_trace_seed123 --wandb_run_name qwen7b_full_trace_seed123_v2
```

- 运行时间：58 分钟，状态 `Sl`（正常运行中）
- cuda:0：49175 MiB 占用，0% 利用率（分配了显存但未计算）
- cuda:1：41191 MiB 占用，100% 利用率（活跃训练中）

这个进程指定了 `--gpu 0` 但实际在两块卡上都分配了显存，真正的训练计算跑在 cuda:1 上。cuda:0 的 49GB 是同一进程的 CUDA context/模型副本，kill 它会同时杀掉 cuda:1 上正在跑的训练。

**建议**：等 `qwen7b_full_trace_seed123_v2` 训练跑完后两块卡的显存会一起释放。如果后续要避免这个问题，需要在训练脚本里加 `CUDA_VISIBLE_DEVICES=0` 环境变量限制进程只看到一块卡，防止它在多卡上分配显存。

---
