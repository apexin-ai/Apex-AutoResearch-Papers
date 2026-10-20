# research ced scoring compat

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_ced_scoring_compat_20260516T124141_result.json`
- **Structured JSON:** [`658c4dff837b009ec01d.json`](../../sessions/65/658c4dff837b009ec01d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已收集到所有必要信息。汇报如下：

---

## CED Scoring Pipeline 兼容性确认

### 1. CED scoring 与生成模型无关

**是的，完全无关。** CED scoring pipeline 的输入是纯文本：
- `claim`: 由 (head, relation, tail) 通过 verbalization template 生成的自然语言句子
- `cited_evidence_sents`: 模型输出中引用的文档句子（文本列表）
- `hard_negative_sents`: 文档中未被引用的其他句子

不需要生成模型的 weights、tokenizer 或任何模型特定信息。只要 candidates 能被 parse 成 `[{"head": ..., "relation": ..., "tail": ..., "evidence": [...]}]` 格式，CED 就能打分。

### 2. CED 使用的 NLI 模型

- **默认模型**: `cross-encoder/nli-deberta-v3-base`（HuggingFace hub ID，定义在 `rewards/ced_reward.py:22`）
- **ced_reranker.py 示例中用**: `/root/autodl-tmp/models/deberta-v3-large-zeroshot-v2.0`
- **rsft_score_filter.py 示例中用**: `/root/autodl-tmp/models/nli-deberta-v3-base`
- 实际磁盘上 `/root/autodl-tmp/models/` 目录下目前**没有** deberta 模型（只有 Meta-Llama-3.1-8B、Qwen3-4B 等），HF cache 里也没有。使用前需要下载。

### 3. CED scoring 完整流程

```
rsft_generate.py (生成 N 个 candidates per doc)
    → generations.jsonl
        → rsft_score_filter.py (CED 打分 + 筛选)
            → rsft_train.jsonl (高质量样本)
                → rsft_trainer.py (SFT 训练，支持 CED score 加权采样)
```

关键脚本用法：
```bash
# Step 1: 打分筛选
python -m freige.training.rsft_score_filter \
    --input_dir /root/autodl-tmp/rsft_generations \
    --output_path /root/autodl-tmp/rsft_filtered \
    --nli_model_path cross-encoder/nli-deberta-v3-base \
    --scoring_mode ced  # 或 flat_nli
    --selection_strategy top_pct --top_pct 25

# Step 2: 独立 reranking 评估
python -m freige.eval.ced_reranker \
    --base_model <任意生成模型> \
    --nli_model_path cross-encoder/nli-deberta-v3-base \
    --num_generations 8 --temperature 0.7
```

### 4. 对 LLaMA/8B/1.7B candidates 的适配

**无需任何适配。** 只要满足：
1. 生成输出能被 `parse_model_output()` 解析为标准 triple 格式（JSON list with head/relation/tail/evidence fields）
2. evidence 字段是文档中的句子 ID 列表

这些条件由 prompt 格式保证，与底层生成模型无关。Qwen3-4B、LLaMA-3.1-8B、SmolLM-1.7B 都用同一个 system prompt 和输出格式，CED 直接兼容。

---
