# ssh e2e pipeline verify

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_e2e-pipeline-verify_20260515T040551_result.json`
- **Structured JSON:** [`d0982793f4e7d5b5714c.json`](../../sessions/d0/d0982793f4e7d5b5714c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 端到端验证结果

### 阶段 1: merge_shards.py — **通过**
- 5 个源文件合并：root 2416 + 4 shard 共 20968 → 去重后 **20648 records, 2581 unique docs**
- last-wins 去重正常：344 records 被 shard 版本覆盖
- JSONL 格式正确，字段完整（doc_id, generation_idx, prompt, output, parsed_triples, gold_triples, sents）

### 阶段 2: rsft_score_filter.py — **通过**
- CPU NLI 80 条记录 ~4 分钟完成
- format_reward=1.0 (全部格式正确), f1_mean=0.584, ced_mean=0.534
- top_k=1: 10/80 选中（10 docs 各 1 条），selected combined_score mean=0.758
- 输出 rsft_train.jsonl 有 `input`/`output`/`ced_score` 字段，与 rsft_trainer 兼容
- rsft_report.json 统计完整

### 阶段 3: rsft_trainer.py — **通过（含 2 个修复）**
- **修复 1**: 添加 `--max_steps` 参数（argparse + SFTConfig 传递）
- **修复 2**: `parse_model_output(item["doc_id"], text)` → `parse_model_output(text)` + 手动加 doc_id
- 训练 2 步：train_loss=1.25, eval_loss=1.37
- 模型加载流程验证：base → merge SFT adapter → fresh LoRA → train → save
- 输出 adapter 完整（adapter_config.json + adapter_model.safetensors）

### 阶段 4: eval/inference.py — **已就绪**
- 支持 `--sft_adapter`（先 merge）+ `--model_path`（再加 LoRA），完美覆盖 RSFT 双层 adapter
- 自动检测 `adapter_config.json` 判断是 adapter 还是完整模型
- 输出 metrics.json + predictions.json

---

## 生成完成后的完整执行命令序列

```bash
# 环境设置（每次 SSH 后执行一次）
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
export HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1
cd /root/autodl-tmp

# Step 1: 合并 shards
python -m freige.training.merge_shards \
    --shard_dir /root/autodl-tmp/rsft_generations \
    --output /root/autodl-tmp/rsft_generations_merged.jsonl

# Step 2: CED 打分 + 筛选（GPU 空闲后用 GPU，否则 --nli_device cpu）
python -m freige.training.rsft_score_filter \
    --input_dir /root/autodl-tmp/rsft_generations \
    --output_path /root/autodl-tmp/rsft_filtered \
    --selection_strategy top_k --top_k 1 \
    --nli_device cuda:0

# Step 3: RSFT 训练（单卡）
CUDA_VISIBLE_DEVICES=0 python -m freige.training.rsft_trainer \
    --base_model /root/autodl-tmp/models/Qwen3-4B \
    --sft_adapter /root/autodl-tmp/sft_output \
    --rsft_data_path /root/autodl-tmp/rsft_filtered/rsft_train.jsonl \
    --output_dir /root/autodl-tmp/rsft_output \
    --learning_rate 2e-5 \
    --num_epochs 3 \
    --per_device_batch_size 4 \
    --gradient_accumulation_steps 4 \
    --lora_rank 64 --lora_alpha 128 \
    --quantize \
    --eval_data_dir /root/autodl-tmp/data/docred \
    --eval_max_docs 50 \
    --seed 42

# Step 4: 评测（生成完成后可立即执行）
# RSFT 模型 eval
CUDA_VISIBLE_DEVICES=0 python -m freige.eval.inference \
    --model_path /root/autodl-tmp/rsft_output \
    --base_model /root/autodl-tmp/models/Qwen3-4B \
    --sft_adapter /root/autodl-tmp/sft_output \
    --data_path /root/autodl-tmp/data/docred \
    --output_dir /root/autodl-tmp/rsft_eval_results \
    --split dev

# SFT baseline eval（对比用）
CUDA_VISIBLE_DEVICES=0 python -m freige.eval.inference \
    --model_path /root/autodl-tmp/sft_output \
    --base_model /root/autodl-tmp/models/Qwen3-4B \
    --data_path /root/autodl-tmp/data/docred \
    --output_dir /root/autodl-tmp/sft_eval_results \
    --split dev
```

---
