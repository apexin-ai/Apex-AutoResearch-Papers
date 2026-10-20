# code ced scoring readiness

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_ced_scoring_readiness_20260516T145621_result.json`
- **Structured JSON:** [`094151ac42d7cc5ddb1d.json`](../../sessions/09/094151ac42d7cc5ddb1d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据格式确认完毕。每个 doc 有多条 generation（每条一行 JSONL，包含 `generation_idx`）。候选生成仍在进行中（基于 train_annotated.json 的 3053 docs）。

## CED Scoring Pipeline 就绪性报告

### 1. CED scoring 模块

**脚本**: `freige/training/rsft_score_filter.py` (604 行)
- 模块导入和 `--help` 均通过 ✅
- 三种奖励: format_reward, f1_reward, ced_reward
- 输出: `rsft_train.jsonl`（SFT 训练数据）+ `rsft_scores.jsonl` + `rsft_report.json`

### 2. 参数列表

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `--input_dir` | str | **必填** | 含 generations.jsonl 的目录 |
| `--output_path` | str | **必填** | 输出目录 |
| `--nli_model_path` | str | `cross-encoder/nli-deberta-v3-base` | NLI 模型 |
| `--nli_device` | str | auto | 设备 |
| `--tau` | float | 0.5 | CED 阈值 |
| `--scoring_mode` | str | `ced` | `ced` 或 `flat_nli` |
| `--selection_strategy` | str | `top_pct` | `threshold`/`top_k`/`top_pct` |
| `--top_k` | int | 2 | 每个 doc 取 top-K |
| `--top_pct` | int | 25 | 每个 doc 取 top N% |
| `--format/f1/ced_weight` | float | 0.2/0.4/0.4 | 组合分数权重 |
| `--format/f1/ced_threshold` | float | 0.5/0.1/0.0 | 最低阈值 |

### 3. NLI 模型
✅ 完整: `/root/autodl-tmp/.hf_cache/models--cross-encoder--nli-deberta-v3-base/snapshots/6c749ce3425cd33b46d187e45b92bbf96ee12ec7/`（含 model.safetensors, tokenizer 等 7 个文件）

### 4. 候选生成进度（基于 train_annotated 3053 docs）

| 模型 | 完成 docs | generations 行数 | 文件大小 | 进度 |
|------|-----------|-----------------|---------|------|
| Qwen3-8B | 251 | 1992 | 20MB | ~8.2% |
| Qwen3-1.7B | 319 | 2520 | 24MB | ~10.4% |
| LLaMA-3.1-8B | 64 | 512 | 4.7MB | ~2.1% |

每个 doc 约 8 条 generation（N=8 candidates）。**三个进程仍在运行中，距离完成还需较长时间。**

### 5. 建议的完整命令（候选完成后执行）

```bash
# Qwen3-8B（需按 C002 约束设置 CUDA_VISIBLE_DEVICES）
CUDA_VISIBLE_DEVICES=X source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
cd /root/autodl-tmp && python -m freige.training.rsft_score_filter \
    --input_dir /root/autodl-tmp/freige/outputs/rsft_candidates_8b \
    --output_path /root/autodl-tmp/freige/outputs/rsft_scored_8b \
    --nli_model_path /root/autodl-tmp/.hf_cache/models--cross-encoder--nli-deberta-v3-base/snapshots/6c749ce3425cd33b46d187e45b92bbf96ee12ec7 \
    --selection_strategy top_k --top_k 2

# Qwen3-1.7B
CUDA_VISIBLE_DEVICES=X source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
cd /root/autodl-tmp && python -m freige.training.rsft_score_filter \
    --input_dir /root/autodl-tmp/freige/outputs/rsft_candidates_1_7b \
    --output_path /root/autodl-tmp/freige/outputs/rsft_scored_1_7b \
    --nli_model_path /root/autodl-tmp/.hf_cache/models--cross-encoder--nli-deberta-v3-base/snapshots/6c749ce3425cd33b46d187e45b92bbf96ee12ec7 \
    --selection_strategy top_k --top_k 2

# LLaMA-3.1-8B
CUDA_VISIBLE_DEVICES=X source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
cd /root/autodl-tmp && python -m freige.training.rsft_score_filter \
    --input_dir /root/autodl-tmp/freige/outputs/rsft_candidates_llama_8b \
    --output_path /root/autodl-tmp/freige/outputs/rsft_scored_llama_8b \
    --nli_model_path /root/autodl-tmp/.hf_cache/models--cross-encoder--nli-deberta-v3-base/snapshots/6c749ce3425cd33b46d187e45b92bbf96ee12ec7 \
    --selection_strategy top_k --top_k 2
```

### 6. 潜在问题

- **候选生成远未完成**：3 个模型分别只完成 8-10%，LLaMA 仅 2%。需要等待生成完成后才能启动 scoring。
- **NLI 模型用 GPU**：DeBERTa-v3-base 很小（~400MB），可以和生成进程共享 GPU，但需注意显存。也可用 `--nli_device cpu` 避免 GPU 冲突。
- **NLI 模型路径**：默认值是 HF hub ID `cross-encoder/nli-deberta-v3-base`，但建议传本地 snapshot 路径避免网络下载。

---
