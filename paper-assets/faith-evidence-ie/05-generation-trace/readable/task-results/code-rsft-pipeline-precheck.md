# code rsft pipeline precheck

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_rsft_pipeline_precheck_20260515T040427_result.json`
- **Structured JSON:** [`4d69132fe0c92bb56e91.json`](../../sessions/4d/4d69132fe0c92bb56e91.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证完成。以下是汇总：

---

## RSFT 下游 Pipeline 就绪性报告

### 1. 脚本存在性

| 脚本 | 路径 | 状态 |
|------|------|------|
| merge_shards.py | `freige/training/merge_shards.py` | **就绪** |
| rsft_score_filter.py | `freige/training/rsft_score_filter.py` | **就绪** |
| rsft_trainer.py | `freige/training/rsft_trainer.py` | **就绪** |
| ced_reward.py | `freige/rewards/ced_reward.py` | **就绪** |

### 2. 格式对齐（生成→打分→训练）

**生成输出字段** (每行 JSONL):
`doc_id`, `generation_idx`, `prompt`, `output`, `raw_text`, `parsed_triples`, `format_ok`, `truncated`, `gold_triples`, `sents`

**打分脚本 `load_generations`**:
- 自带 shard 合并逻辑（根目录 + `shard_*/generations.jsonl`，last-wins 去重）
- 读取 `doc_id`, `generation_idx`, `parsed_triples`, `gold_triples`, `sents`, `prompt`, `output`, `format_ok` — **全部匹配**

**打分输出 → 训练输入**:
- `format_sft_training_data` 输出 `{input, output, ced_score, doc_id, ...}`
- `rsft_trainer.load_rsft_data` 读取 `input`（user message）、`output`（assistant response）、`ced_score`（加权采样）— **完全对齐**

### 3. 关键发现

**merge_shards.py 可选**：`rsft_score_filter.py` 的 `load_generations` 已内置 shard 合并 + 去重，可以跳过 merge_shards 直接打分：
```bash
cd /root/autodl-tmp && python -m freige.training.rsft_score_filter \
    --input_dir /root/autodl-tmp/rsft_generations \
    --output_path /root/autodl-tmp/rsft_filtered \
    --nli_model_path cross-encoder/nli-deberta-v3-base
```

**NLI 模型**：`/root/autodl-tmp/models/nli-deberta-v3-base` 不存在，但 HF cache 中有（`/root/autodl-tmp/.hf_cache/hub/models--cross-encoder--nli-deberta-v3-base`）。只要 `HF_HOME=/root/autodl-tmp/.hf_cache`，用默认名 `cross-encoder/nli-deberta-v3-base` 即可自动加载。docstring 里的路径示例是过时的。

**rsft_trainer 关键超参**:
- base model: `/root/autodl-tmp/models/Qwen3-4B`
- SFT adapter: `/root/autodl-tmp/sft_output`（默认值，已存在）
- QLoRA: r=32, alpha=64, dropout=0.05, 4bit nf4
- lr=1e-4, epochs=3, batch=2, grad_accum=8, warmup=50
- 支持 CED score 加权采样（`--weighted_sampling`）
- wandb 集成（有 WANDB_API_KEY 时自动开启）
- 支持 accelerate 多卡

### 4. Dry-run 结果

无法在 `ssh_read_only` 中执行 import 测试（需 cwd 为 `/root/autodl-tmp` 且要激活 conda）。但生成任务当前正在运行并成功使用 `freige` 包，说明包结构和依赖已就绪。

### 5. 问题清单

**无阻塞性问题。** Pipeline 代码完整，格式对齐，可直接执行。

唯一注意事项：打分时确保 `HF_HOME=/root/autodl-tmp/.hf_cache` 环境变量已设置，否则 NLI 模型会尝试重新下载。

---
