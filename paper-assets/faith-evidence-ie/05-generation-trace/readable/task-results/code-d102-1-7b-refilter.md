# code d102 1 7b refilter

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d102_1_7b_refilter_20260518T053353_result.json`
- **Structured JSON:** [`ddbb0404d2a1a8342829.json`](../../sessions/dd/ddbb0404d2a1a8342829.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All info gathered. Here's the summary:

---

## 结果

**1.7B CED scores 文件**: `/root/autodl-tmp/freige/outputs/rsft_scored_1_7b/rsft_scores.jsonl` (24216 records, 原 k=3)

**re-filter k=1 输出**:
- 路径: `/root/autodl-tmp/freige/outputs/rsft_scored_1_7b_k1/rsft_train.jsonl`
- **k=1 样本数: 3021**（从 k=3 的 9042 中每个 doc 取 combined_score 最高的 1 个）
- unique docs: 3021
- combined_score: mean=0.7602, median=0.7640
- f1_reward: mean=0.7105, median=0.7273

**推荐 1.7B k=1 训练命令 (seed42)**:

```bash
CUDA_VISIBLE_DEVICES=X HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 \
python -m freige.training.rsft_trainer \
  --base_model /root/autodl-tmp/models/Qwen/Qwen3-1.7B \
  --sft_adapter /root/autodl-tmp/sft_output_qwen3_1_7b_bf16 \
  --rsft_data_path /root/autodl-tmp/freige/outputs/rsft_scored_1_7b_k1/rsft_train.jsonl \
  --output_dir /root/autodl-tmp/rsft_output_qwen3_1_7b_k1 \
  --num_epochs 3 \
  --per_device_batch_size 4 \
  --gradient_accumulation_steps 4 \
  --learning_rate 2e-5 \
  --warmup_steps 100 \
  --seed 42 \
  --bf16 \
  --wandb_project freige-rsft \
  --wandb_run_name rsft_qwen3_1_7b_k1_s42
```

注意：需先 `nvidia-smi` 确认目标 GPU 显存空闲（C001），并显式设 `CUDA_VISIBLE_DEVICES`（C002/C003）。SFT adapter 路径用了 `sft_output_qwen3_1_7b_bf16`（与原 k=3 run 的 base model 匹配）。

---
