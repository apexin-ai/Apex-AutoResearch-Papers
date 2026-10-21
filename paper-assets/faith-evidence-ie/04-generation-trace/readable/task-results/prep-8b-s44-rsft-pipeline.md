# prep 8b s44 rsft pipeline

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_8b_s44_rsft_pipeline_20260518T203131_result.json`
- **Structured JSON:** [`0807e4a04f0379994bc4.json`](../../sessions/08/0807e4a04f0379994bc4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息收集完毕。以下是汇总报告：

---

## 8B SFT s44 RSFT Pipeline 准备情况

### 1. Checkpoint 路径
- **8B s44 SFT**: `/root/autodl-tmp/sft_output_qwen3_8b_s44`
  - LoRA adapter (r=64, alpha=128), base=Qwen3-8B, adapter_model.safetensors 698MB
  - 有 checkpoint-190 和 checkpoint-570

### 2. 现有脚本与问题

| 步骤 | 脚本 | 状态 |
|------|------|------|
| Candidate Generation | **无** | 需要新建 |
| CED Scoring | **无** | 需要新建 |
| RSFT Training | `scripts/seed_expansion/train_8b_s44.sh` | **需要修改** |
| RSFT Eval | `scripts/seed_expansion/eval_8b_s44.sh` | **需要修改** |

**关键问题**: 现有的 `train_8b_s44.sh` 和 `eval_8b_s44.sh` 是按"seed expansion"设计的，复用 s42 的 SFT adapter 和 s42 的 scored data，只改 RSFT training seed：
- `--sft_adapter /root/autodl-tmp/sft_output_qwen3_8b_bf16` ← s42 SFT，不是 s44
- `--rsft_data_path /root/autodl-tmp/rsft_scored_qwen3_8b_k1/rsft_train.jsonl` ← s42 生成的 3018 条数据

如果要做完整 RSFT pipeline（s44 SFT 生成候选 → CED 打分 → RSFT 训练），需要：

### 3. 缺失脚本 / 需修改项

**Step 1 — Candidate Generation（需新建脚本）**
```bash
python -m freige.training.rsft_generate \
    --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B \
    --sft_adapter /root/autodl-tmp/sft_output_qwen3_8b_s44 \
    --data_path /root/autodl-tmp/data/docred \
    --output_dir /root/autodl-tmp/rsft_generations_qwen3_8b_s44 \
    --num_generations 8 --temperature 0.7 --batch_size 4
```

**Step 2 — CED Scoring（需新建脚本）**
```bash
python -m freige.training.rsft_score_filter \
    --input_dir /root/autodl-tmp/rsft_generations_qwen3_8b_s44 \
    --output_path /root/autodl-tmp/rsft_scored_qwen3_8b_s44_k1 \
    --selection_strategy top_k --top_k 1 \
    --nli_model_path cross-encoder/nli-deberta-v3-base
```

**Step 3 — RSFT Training（修改现有脚本）**
- `--sft_adapter` 改为 `/root/autodl-tmp/sft_output_qwen3_8b_s44`
- `--rsft_data_path` 改为 `/root/autodl-tmp/rsft_scored_qwen3_8b_s44_k1/rsft_train.jsonl`

**Step 4 — RSFT Eval（修改现有脚本）**
- `--sft_adapter` 改为 `/root/autodl-tmp/sft_output_qwen3_8b_s44`
- `--model_path` 改为新的 RSFT 输出路径

### 4. 数据依赖
| 依赖 | 路径 | 状态 |
|------|------|------|
| DocRED train data | `/root/autodl-tmp/data/docred` | ✅ 已有 |
| NLI model (CED) | `cross-encoder/nli-deberta-v3-base` | ✅ HF cache 中有 |
| Base model | `/root/autodl-tmp/models/Qwen/Qwen3-8B` | ✅ 已有 |
| s44 SFT adapter | `/root/autodl-tmp/sft_output_qwen3_8b_s44` | ✅ 训练完成 |

参考 s42 pipeline: 8 gens × 3027 docs = 24216 candidates → top_k=1 筛选后 3018 条训练数据。

### 5. GPU 时间预估
| 步骤 | 预估时间 | 备注 |
|------|----------|------|
| Candidate Generation | 2-4h | 8B 模型 × 8 gens × ~3027 docs |
| CED Scoring | 30-60min | NLI deberta-v3-base 很小 |
| RSFT Training | ~48min | 参考 README |
| RSFT Eval | ~15-20min | |

### 6. GPU 状态
- **GPU 0**: 空闲（0 MiB）← 可用
- GPU 1: 10413 MiB 占用
- GPU 2: 10413 MiB 占用
- GPU 3: 10855 MiB 占用

### 结论
需要新建 2 个脚本（generation + scoring）、修改 2 个现有脚本（training + eval）。Python 模块 `rsft_generate.py` 和 `rsft_score_filter.py` 已就绪，无需改代码。数据和模型依赖全部满足。GPU 0 可用于启动。

---
