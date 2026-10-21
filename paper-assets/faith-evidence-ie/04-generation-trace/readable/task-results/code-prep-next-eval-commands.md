# code prep next eval commands

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prep-next-eval-commands_20260515T230421_result.json`
- **Structured JSON:** [`10ceae878c0d1f90dee8.json`](../../sessions/10/10ceae878c0d1f90dee8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部路径已确认。汇总如下：

---

## 各命令状态

### 1. eval_flat_nli_seed44 — **READY** (checkpoint 已存在)

Checkpoint: `/root/autodl-tmp/rsft_output_flat_nli_s44/checkpoint-507` ✅

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && CUDA_VISIBLE_DEVICES=&lt;GPU> HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_flat_nli_s44/checkpoint-507 --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/docred --split dev --batch_size 16 --max_new_tokens 1024 --seed 44 --output_dir /root/autodl-tmp/eval_results/rsft_flat_nli_s44_eval --no-quantize
```

### 2. eval_flat_nli_seed45 — **READY** (checkpoint 已存在)

Checkpoint: `/root/autodl-tmp/rsft_output_flat_nli_s45/checkpoint-507` ✅

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && CUDA_VISIBLE_DEVICES=&lt;GPU> HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_flat_nli_s45/checkpoint-507 --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/docred --split dev --batch_size 16 --max_new_tokens 1024 --seed 45 --output_dir /root/autodl-tmp/eval_results/rsft_flat_nli_s45_eval --no-quantize
```

### 3. reeval_rsft_topk3 — **READY，路径已修正**

你给的路径 `rsft_output_topk3/checkpoint-507` **不存在**。实际路径是：
- `/root/autodl-tmp/rsft_topk3_output/checkpoint-1509` ✅ (topk3 训练步数不同，最终 checkpoint 是 1509)

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && CUDA_VISIBLE_DEVICES=&lt;GPU> HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_topk3_output/checkpoint-1509 --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/docred --split dev --batch_size 16 --max_new_tokens 1024 --seed 42 --output_dir /root/autodl-tmp/eval_results/rsft_topk3_reeval --no-quantize
```

### 4. seed46 训练 — **READY**

训练数据: `/root/autodl-tmp/rsft_filtered_flat_nli/rsft_train.jsonl` (2691 行) ✅

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && CUDA_VISIBLE_DEVICES=&lt;GPU> HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 python -m freige.training.rsft_trainer --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --rsft_data_path /root/autodl-tmp/rsft_filtered_flat_nli/rsft_train.jsonl --output_dir /root/autodl-tmp/rsft_output_flat_nli_s46 --learning_rate 2e-5 --num_epochs 3 --per_device_batch_size 1 --gradient_accumulation_steps 16 --lora_rank 64 --lora_alpha 128 --eval_data_dir /root/autodl-tmp/data/docred --wandb_run_name plan_001_flat_nli_seed46 --seed 46
```

---

## GPU 状态（C001 约束）

| GPU | 显存占用 | 可用于 eval? |
|-----|---------|-------------|
| 0 | 19175 / 32607 MiB | ❌ |
| 1 | 16925 / 32607 MiB | ❌ |
| 2 | 19745 / 32607 MiB | ❌ |
| 3 | 30708 / 32607 MiB | ❌ |

**当前 4 卡全部被占用，无法提交 eval。** 需要等当前训练完成释放 GPU 后再提交。所有命令中 `CUDA_VISIBLE_DEVICES=&lt;GPU>` 需在提交时替换为空闲 GPU 编号。

---
