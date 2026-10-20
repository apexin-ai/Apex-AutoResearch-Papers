# monitor ced training progress

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_ced-training-progress_20260516T004756_result.json`
- **Structured JSON:** [`c2df889d48f26bdf52ea.json`](../../sessions/c2/c2df889d48f26bdf52ea.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I have all the information. Here's the report:

---

## 训练进度

| 实验 | PID | GPU | Step | 进度 | 速度 | ETA (UTC) |
|------|-----|-----|------|------|------|-----------|
| rsft_ced_s43_train_r3 | 277310 | cuda:1 | 170/510 | 33% (epoch 1 完成，正在 eval) | ~5.7s/step | ~09:42 (~54min) |
| rsft_ced_s45_train_r4 | 279526 | cuda:2 | 140/510 | 27% (epoch 1 进行中) | ~5.6s/step | ~09:09 (~35min) |

s45 无 in-training eval（命令中没有 `--eval_data_dir`），所以比 s43 快。

## Checkpoint 路径

训练完成后（参考已有 rsft_output/rsft_output_s43/rsft_output_s44 的结构，总步数 510，save_steps=50）：
- **s43**: `/root/autodl-tmp/rsft_output_ced_s43/checkpoint-510`
- **s45**: `/root/autodl-tmp/rsft_output_ced_s45/checkpoint-510`

## GPU 占用情况

当前 4 卡全满：
- cuda:0 — eval_flat_nli_s44 (RUNNING)
- cuda:1 — rsft_ced_s43_train_r3 (RUNNING)
- cuda:2 — rsft_ced_s45_train_r4 (RUNNING)
- cuda:3 — eval_flat_nli_seed45 (RUNNING)

CED eval 需等训练完成释放 GPU。提交前必须 `nvidia-smi` 确认目标 GPU 显存 < 2GB（C001）。

## Eval 命令模板

**CED s43 eval**（训练完成后，替换 X 为空闲 GPU 编号）：
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && CUDA_VISIBLE_DEVICES=X HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_ced_s43/checkpoint-510 --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 43 --output_dir /root/autodl-tmp/eval_results/rsft_ced_s43 --no-quantize
```

**CED s45 eval**（训练完成后，替换 X 为空闲 GPU 编号）：
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && CUDA_VISIBLE_DEVICES=X HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_ced_s45/checkpoint-510 --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 45 --output_dir /root/autodl-tmp/eval_results/rsft_ced_s45 --no-quantize
```

关键参数：`--sft_adapter`（必带）、`--no-quantize`、`batch_size=4`（32GB OOM 防护）、cwd=`/root/autodl-tmp`、`CUDA_VISIBLE_DEVICES=X`（C002）。

---
