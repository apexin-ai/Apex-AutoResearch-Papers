# research prep ced s43 s45

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_prep_ced_s43_s45_20260515T235511_result.json`
- **Structured JSON:** [`d1e1cfbd39238c15f26a.json`](../../sessions/d1/d1e1cfbd39238c15f26a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

信息收集完毕。汇总报告：

---

## CED RSFT 训练报告

### 现有状态

| 目录 | seed | 状态 |
|------|------|------|
| `rsft_output/` | 42 | 完成 |
| `rsft_output_s43/` | 43 | **已完成** (exit_code=0, 1h56m) |
| `rsft_output_s44/` | 44 | 完成 |
| `rsft_output_s45/` | 45 | **不存在，需补跑** |

**注意：s43 已经训练完成。** 如果确认 s43 无问题，只需跑 s45。

### 训练数据
- 路径：`/root/autodl-tmp/rsft_filtered/rsft_train.jsonl`
- 样本数：2718
- CED scores: min=0.000, max=0.997, mean=0.668

### 超参数（从 s43/s44 log 和 adapter_config.json 复原）

| 参数 | 值 |
|------|----|
| base_model | /root/autodl-tmp/models/Qwen3-4B |
| sft_adapter | /root/autodl-tmp/sft_output |
| lr | 2e-5 |
| epochs | 3 |
| per_device_batch | 4 |
| grad_accum | 4 |
| warmup_steps | 100 |
| save_steps | 50 |
| save_total_limit | 5 |
| max_length | 2048 |
| lora_rank | 64 |
| lora_alpha | 128 |
| lora_dropout | 0.05 |
| bf16 | True |
| weighted_sampling | True |
| eval_data_dir | /root/autodl-tmp/data/docred |
| eval_max_docs | 50 |
| quantize | 未使用 |

### 训练命令

**CED RSFT s45**（只需跑这一个）：
```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/freige && CUDA_VISIBLE_DEVICES=0 python -m freige.training.rsft_trainer \
  --rsft_data_path /root/autodl-tmp/rsft_filtered/rsft_train.jsonl \
  --output_dir /root/autodl-tmp/rsft_output_s45 \
  --seed 45 \
  --weighted_sampling \
  --eval_data_dir /root/autodl-tmp/data/docred \
  --wandb_run_name rsft_ced_s45 \
  --bf16"
```

**CED RSFT s43**（如需重跑）：
```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/freige && CUDA_VISIBLE_DEVICES=0 python -m freige.training.rsft_trainer \
  --rsft_data_path /root/autodl-tmp/rsft_filtered/rsft_train.jsonl \
  --output_dir /root/autodl-tmp/rsft_output_s43 \
  --seed 43 \
  --weighted_sampling \
  --eval_data_dir /root/autodl-tmp/data/docred \
  --wandb_run_name rsft_ced_s43 \
  --bf16"
```

### 预计训练时间
~2小时/run（s43 耗时 1h56m，s44 耗时 1h53m），单 GPU。

### 输出目录命名
沿用现有模式：`rsft_output_s45`。

---
