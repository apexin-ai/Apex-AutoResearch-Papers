# code exp downsample cls func

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp-downsample-cls-func_20260519T032233_result.json`
- **Structured JSON:** [`4fe0530735b3a19628ad.json`](../../sessions/4f/4fe0530735b3a19628ad.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息已就绪。以下是完整结果：

---

## 1. Downsample 结果

| | Instances | Problem IDs |
|---|---|---|
| 原始 CLS function-level | 15,290 | 906 |
| Downsample 后 | 8,051 | 475 (52.4%) |
| TRAJ function-level (目标) | 8,052 | — |

标签分布：pass=4,174 / fail=3,877（基本均衡）。输出在 `data/train_downsampled.jsonl`。

## 2. 训练命令

```bash
cd /home/sonny/exec-sim-repair-verifier

CUDA_VISIBLE_DEVICES=0 HF_HUB_OFFLINE=1 /root/miniconda3/bin/python train_unified.py \
  --model_name_or_path /root/autodl-tmp/models/Qwen/Qwen3-4B \
  --data_dir data/ \
  --task cls \
  --train_file train_downsampled.jsonl \
  --val_file val.jsonl \
  --output_dir /root/autodl-tmp/checkpoints_cls_downsample_qwen3_4b/ \
  --run_name cls-downsample-qwen3-4b-lora \
  --epochs 3 \
  --batch_size 2 \
  --grad_accumulation 16 \
  --lr 2e-4 \
  --lora_rank 16 \
  --lora_alpha 32 \
  --max_seq_length 2048 \
  --seed 42 \
  --wandb_project exec-sim-repair-verifier
```

超参与原 CLS 完全一致（LoRA r=16, alpha=32, 3 epochs, lr=2e-4, bf16）。

## 3. Eval 命令（训练完成后）

```bash
CUDA_VISIBLE_DEVICES=0 HF_HUB_OFFLINE=1 /root/miniconda3/bin/python eval_verifier.py \
  --data_dir data/ \
  --checkpoint_dir /root/autodl-tmp/checkpoints_cls_downsample_qwen3_4b/best \
  --model_name /root/autodl-tmp/models/Qwen/Qwen3-4B \
  --output artifacts/eval_cls_downsample_qwen3_4b.json \
  --batch_size 16 \
  --max_seq_length 2048 \
  --save_predictions
```

## 4. 预估训练时间

- 8,051 samples / (batch_size=2 × grad_accum=16) = 252 steps/epoch × 3 epochs ≈ 756 total steps
- Qwen3-4B LoRA 在 5090 上约 2-3 min/epoch（function-level 数据短，2048 seq len）
- 预估：**~30-50 分钟**

## 5. 阻塞问题

**4 张 GPU 全被 eval 任务占满：**
- GPU 0: Qwen3-8B CWM repo eval (PID 778334)
- GPU 1: DeepSeek 3-shot baseline eval (PID 788573)
- GPU 2: DeepSeek CWM repo eval (PID 734440, 从 May 18 开始)
- GPU 3: DeepSeek CWM repo s123 eval (PID 668680, 从 May 18 开始)

需要等某张 GPU 空出后再启动训练。GPU 2/3 的 eval 已跑超过 24 小时，可能快结束或已卡住。要不要我检查一下它们的进度？

---
