# ops diagnose and resubmit full trace multiseed

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_diagnose_and_resubmit_full_trace_multiseed_20260521T073512_result.json`
- **Structured JSON:** [`6d5a372f34bb0721cbf7.json`](../../sessions/6d/6d5a372f34bb0721cbf7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。GPU 0 有 49GB 残留显存需要清理。

## 诊断报告

### 1. 配置对比

| 参数 | seed42_v5 (成功) | seed123/456 (OOM) |
|------|:-:|:-:|
| **gradient_checkpointing** | **True** | **False** (默认) |
| per_device_train_batch_size | 4 | 4 |
| gradient_accumulation_steps | 8 | 8 |
| max_length | 2048 | 2048 |
| bf16 | True | True |
| learning_rate | 2e-4 | 2e-4 |
| num_train_epochs | 3 | 3 |
| LoRA r/alpha/dropout | 16/32/0.05 | 16/32/0.05 |

### 2. OOM 根因

**seed123/456 启动时漏了 `--gradient_checkpointing` 标志。**

脚本 `train_sft.py` 中 `--gradient_checkpointing` 是 `action="store_true"`，默认 False。seed42_v5 显式传了此参数，seed123/456 没传。

无 gradient checkpointing 时，7B 模型前向传播保存全部中间激活，batch_size=4 × max_length=2048 下显存需求远超单卡 98GB：
- seed123 在 LoRA dropout 层 OOM（46GB 时 → 可能只跑到中间层）
- seed456 在 logits contiguous 时 OOM（95GB → 前向刚跑完）

### 3. GPU 状态

- GPU 0: 49175 MiB 残留显存（无进程），需重置
- GPU 1: 干净（0 MiB）

需先清理 GPU 0 残留显存再跑训练。

### 4. 修正后的训练命令

**seed123**（GPU 0）:
```bash
CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python /root/trace-verdict-study/train/train_sft.py \
  --condition full_trace \
  --seed 123 \
  --gradient_checkpointing \
  --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/qwen7b_full_trace_seed123 \
  --wandb_run_name full_trace_seed123 \
  --gpu 0
```

**seed456**（GPU 1）:
```bash
CUDA_VISIBLE_DEVICES=1 /root/miniconda3/bin/python /root/trace-verdict-study/train/train_sft.py \
  --condition full_trace \
  --seed 456 \
  --gradient_checkpointing \
  --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/qwen7b_full_trace_seed456 \
  --wandb_run_name full_trace_seed456 \
  --gpu 1
```

两个命令可同时在不同 GPU 上并行运行。提交前需先清理 GPU 0 的 49GB 残留显存（`nvidia-smi --gpu-reset -i 0` 或 kill 残留 CUDA context）。

---
