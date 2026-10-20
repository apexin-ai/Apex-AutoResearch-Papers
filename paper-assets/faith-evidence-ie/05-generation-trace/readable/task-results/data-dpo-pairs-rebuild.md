# data dpo pairs rebuild

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_dpo-pairs-rebuild_20260523T020420_result.json`
- **Structured JSON:** [`4e6e37dd69b634b73fd5.json`](../../sessions/4e/4e6e37dd69b634b73fd5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

---

## 报告

### 1. 原始 DPO 超参（来源：代码默认值）

wandb list_wandb_runs 接口有 bug（`wandb_project` 参数不匹配），无法查询历史 run。以下为 `dpo_trainer.py` 和 `dpo_data_builder.py` 中的 argparse 默认值：

**DPO Data Builder:**
| 参数 | 值 |
|------|-----|
| rank_by | `ced_reward` |
| pair_k | `1` |
| min_margin | `0.05` |
| require_format_ok | `True` |

**DPO Trainer:**
| 参数 | 值 |
|------|-----|
| beta | `0.1` |
| loss_type | `sigmoid` |
| label_smoothing | `0.0` |
| learning_rate | `5e-6` |
| num_epochs | `3` |
| per_device_batch_size | `2` |
| gradient_accumulation_steps | `8` |
| warmup_steps | `50` |
| max_length | `2048` |
| lora_rank | `64` |
| lora_alpha | `128` |
| lora_dropout | `0.05` |
| base_model | `Qwen3-4B` |
| sft_adapter | `/root/autodl-tmp/sft_output` |

### 2. DPO Pairs 构建结果

- **输入**: 24216 generation records（4 shards 合并），24216 scores
- **输出**: **2977 DPO pairs**（3026 docs 中 1 doc 仅单条生成，48 pairs 低于 min_margin 被过滤）
- **Margin 统计**: mean=0.400, std=0.183, median=0.366, range=[0.056, 0.997]
- **Chosen CED**: mean=0.724, median=0.740
- **Rejected CED**: mean=0.325, median=0.329
- **样本格式**: `{doc_id, input, chosen, rejected, chosen_score, rejected_score, chosen_ced, rejected_ced, margin}`
- **路径**: `/root/autodl-tmp/dpo_data_rebuilt/dpo_pairs.jsonl`

### 3. 数据准备完成

### 4. 建议的 DPO 训练命令

**1 epoch:**
```bash
CUDA_VISIBLE_DEVICES=X source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/freige && python -m freige.training.dpo_trainer \
    --dpo_data_path /root/autodl-tmp/dpo_data_rebuilt/dpo_pairs.jsonl \
    --output_dir /root/autodl-tmp/dpo_output_rebuilt_1ep \
    --num_epochs 1 \
    --beta 0.1 \
    --loss_type sigmoid \
    --learning_rate 5e-6 \
    --per_device_batch_size 2 \
    --gradient_accumulation_steps 8 \
    --lora_rank 64 \
    --lora_alpha 128 \
    --wandb_project freige-dpo \
    --wandb_run_name dpo_rebuilt_1ep
```

**3 epoch:**
```bash
CUDA_VISIBLE_DEVICES=X source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/freige && python -m freige.training.dpo_trainer \
    --dpo_data_path /root/autodl-tmp/dpo_data_rebuilt/dpo_pairs.jsonl \
    --output_dir /root/autodl-tmp/dpo_output_rebuilt_3ep \
    --num_epochs 3 \
    --beta 0.1 \
    --loss_type sigmoid \
    --learning_rate 5e-6 \
    --per_device_batch_size 2 \
    --gradient_accumulation_steps 8 \
    --lora_rank 64 \
    --lora_alpha 128 \
    --wandb_project freige-dpo \
    --wandb_run_name dpo_rebuilt_3ep
```

（`X` 需替换为空闲 GPU 编号，提交前 `nvidia-smi` 确认显存 < 2GB — C001）

---
