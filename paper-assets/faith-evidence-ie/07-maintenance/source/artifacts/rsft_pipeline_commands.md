# RSFT 下游流水线预验证报告

## 1. 脚本存在性确认

| 脚本 | 实际路径 | 状态 |
|------|---------|------|
| merge_shards.py | `freige/training/merge_shards.py` | ✅ 存在 |
| rsft_score_filter.py | `freige/training/rsft_score_filter.py` | ✅ 存在 |
| rsft_trainer.py | `freige/training/rsft_trainer.py` | ✅ 存在 |
| inference.py (eval) | `freige/eval/inference.py` | ✅ 存在 |
| batch_eval.py | `freige/eval/batch_eval.py` | ✅ 存在（多checkpoint批量评测用） |

**注意**: 脚本在 `freige/training/` 和 `freige/eval/` 下，不在 `freige/freige/` 下。

## 2. Shard 数据现状

| 文件 | 行数 |
|------|------|
| shard_0/generations.jsonl | 4,464 |
| shard_1/generations.jsonl | 4,800 |
| shard_2/generations.jsonl | 4,832 |
| shard_3/generations.jsonl | 4,104 |
| root generations.jsonl（旧单卡） | 2,416 |
| **总计** | **20,616** |

## 3. 输入/输出格式对齐验证

### generations.jsonl 字段
```
doc_id, generation_idx, prompt, output, raw_text, format_ok, truncated, gold_triples, sents, parsed_triples
```

### rsft_score_filter.py
- **输入**: `--input_dir` 目录，内部 `load_generations()` 自动合并 root + shard_*/generations.jsonl（last-wins 去重）
- **需要字段**: parsed_triples, gold_triples, sents, format_ok, prompt, output, doc_id, generation_idx → ✅ 全部对齐
- **输出**: `rsft_train.jsonl`，字段: input, output, ced_score, doc_id, generation_idx, format_reward, f1_reward, combined_score

### rsft_trainer.py
- **输入**: `--rsft_data_path` JSONL
- **需要字段**: input, output, ced_score → ✅ 与 score_filter 输出对齐

### inference.py (eval)
- **输入**: adapter 路径 + base model + SFT adapter
- **输出**: metrics.json (F1, Ign-F1, Evi-F1, EDCR) + predictions.json

## 4. 依赖确认

| 依赖 | 状态 |
|------|------|
| NLI 模型 (cross-encoder/nli-deberta-v3-base) | ✅ 已缓存于 `/root/autodl-tmp/.hf_cache/hub/models--cross-encoder--nli-deberta-v3-base` |
| SFT adapter | ✅ `/root/autodl-tmp/sft_output/` (adapter_config.json + adapter_model.safetensors) |
| Qwen3-4B base model | ✅ `/root/autodl-tmp/models/Qwen3-4B` |
| DocRED 数据 | ✅ `/root/autodl-tmp/data/docred/` (dev.json, test.json, train_annotated.json) |

## 5. 关键发现

1. **rsft_score_filter 内置 shard 合并**：`load_generations()` 自动加载 root + shard_*/generations.jsonl 并去重。不需要先运行 merge_shards.py。但建议仍先 merge 留一份干净的合并文件备查。
2. **rsft_trainer 默认值已满足约束**：lora_rank=64, lora_alpha=128, bf16=True, quantize=False（store_true 默认 False），无需额外参数。
3. **inference.py quantize 默认 True**：必须显式传 `--no-quantize`。

## 6. 完整执行命令（copy-paste ready）

所有命令从 `/root/autodl-tmp/` 运行。

### Step 0: 合并 shards（可选，留备份）

```bash
cd /root/autodl-tmp && \
HF_HOME=/root/autodl-tmp/.hf_cache \
python -m freige.training.merge_shards \
    --shard_dir /root/autodl-tmp/rsft_generations \
    --output /root/autodl-tmp/rsft_generations/generations_merged.jsonl
```

### Step 1: CED 打分 + 筛选 top 25%

```bash
cd /root/autodl-tmp && \
HF_HOME=/root/autodl-tmp/.hf_cache \
python -m freige.training.rsft_score_filter \
    --input_dir /root/autodl-tmp/rsft_generations \
    --output_path /root/autodl-tmp/rsft_filtered \
    --selection_strategy top_pct \
    --top_pct 25
```

NLI 模型默认 `cross-encoder/nli-deberta-v3-base`，HF_HOME 指向缓存目录会自动加载。

### Step 2: RSFT 训练（bf16 LoRA，禁止 quantize）

```bash
cd /root/autodl-tmp && \
HF_HOME=/root/autodl-tmp/.hf_cache \
python -m freige.training.rsft_trainer \
    --rsft_data_path /root/autodl-tmp/rsft_filtered/rsft_train.jsonl \
    --output_dir /root/autodl-tmp/rsft_output \
    --lora_rank 64 \
    --lora_alpha 128 \
    --bf16 \
    --eval_data_dir /root/autodl-tmp/data/docred \
    --weighted_sampling
```

默认参数: lr=2e-5, epochs=3, batch_size=4, grad_accum=4, warmup=100, save_steps=50。
不传 `--quantize`（默认 False）。

### Step 3: Eval

```bash
cd /root/autodl-tmp && \
HF_HOME=/root/autodl-tmp/.hf_cache \
python -m freige.eval.inference \
    --model_path /root/autodl-tmp/rsft_output \
    --sft_adapter /root/autodl-tmp/sft_output \
    --base_model /root/autodl-tmp/models/Qwen3-4B \
    --data_path /root/autodl-tmp/data/docred \
    --no-quantize \
    --output_dir /root/autodl-tmp/eval_results/rsft
```

## 7. 潜在问题

1. **shard_3 行数偏少 (4,104 vs ~4,700)**：可能尚未完成。执行前确认 4 个 shard 的 generation 进程已全部结束。
2. **rsft_output 目录命名**：SFT adapter 在 `/root/autodl-tmp/sft_output`，RSFT 训练输出用 `/root/autodl-tmp/rsft_output`，不会冲突。
3. **AutoDL 磁盘**: RSFT 训练会保存 checkpoints，确保 `/root/autodl-tmp/` 有足够空间（LoRA adapter ~200MB/checkpoint × save_total_limit=5）。
