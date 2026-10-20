# code rsft generation scoring

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_rsft-generation-scoring_20260514T231542_result.json`
- **Structured JSON:** [`e79e53023b37f7d0ee5c.json`](../../sessions/e7/e79e53023b37f7d0ee5c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个脚本已完成并部署到服务器 `/root/autodl-tmp/freige/training/`:

**`rsft_generate.py`** — 批量生成候选输出
- 加载 base model + SFT adapter (merge & unload)，与 inference.py 一致
- 对每个 DocRED 文档生成 N 个候选 (temperature sampling)
- 支持 batch 推理 + OOM 自动降级到单条
- 断点续传 (progress.json 记录已完成 doc_id)
- 输出 JSONL 含 parsed_triples、format_ok、gold_triples、sents（供 score_filter 直接使用）

**`rsft_score_filter.py`** — CED 打分 + 筛选
- 三种 reward 完全复用现有逻辑：format_reward (grpo_trainer)、f1_reward (grpo_trainer)、ced_reward (CEDRewardWrapper 的逐 triple 打分逻辑)
- combined_score = 0.2×format + 0.4×f1 + 0.4×ced
- 三种筛选策略：threshold / top_k / top_pct（默认 top_pct=25%，按 doc 分组）
- 输出 rsft_train.json (SFT messages 格式) + rsft_scores.jsonl + rsft_report.json

运行示例:
```bash
# Step 1: 生成
python -m freige.training.rsft_generate \
    --data_path /root/autodl-tmp/data/docred \
    --output_dir /root/autodl-tmp/rsft_generations \
    --num_generations 8 --batch_size 2

# Step 2: 打分筛选
python -m freige.training.rsft_score_filter \
    --input_dir /root/autodl-tmp/rsft_generations \
    --output_path /root/autodl-tmp/rsft_filtered \
    --selection_strategy top_pct --top_pct 25
```

---
