# Token Overlap Analysis: EN-ZH

**Date**: 2026-05-22
**Task**: Compute token overlap between EN and ZH prompts for two models

## Data

| Model | EN prompts | ZH prompts | EN files | ZH files |
|-------|-----------|-----------|----------|----------|
| Qwen3-8B | 966 | 966 | en_conflict_{train,test}_verified.jsonl | zh_conflict_{train,test}.jsonl |
| Llama-3.1-8B-Instruct | 1368 | 1368 | en_conflict_{train,test}_verified.jsonl | zh_conflict_{train,test}.jsonl |

Prompt = question + context fields concatenated.

## Results

### Qwen3-8B (vocab size: 151,643)

| Metric | Value |
|--------|-------|
| Unique EN token IDs | 13,836 |
| Unique ZH token IDs | 10,140 |
| Intersection (EN∩ZH) | 2,264 |
| Union (EN∪ZH) | 21,712 |
| **Jaccard** (∩/∪) | **0.1043** |
| Overlap/EN (∩/EN) | 0.1636 |
| Overlap/ZH (∩/ZH) | 0.2233 |
| EN-only tokens | 11,572 |
| ZH-only tokens | 7,876 |
| Overlap as % of vocab | 1.49% |

### Llama-3.1-8B-Instruct (vocab size: 128,000)

| Metric | Value |
|--------|-------|
| Unique EN token IDs | 16,394 |
| Unique ZH token IDs | 7,020 |
| Intersection (EN∩ZH) | 3,077 |
| Union (EN∪ZH) | 20,337 |
| **Jaccard** (∩/∪) | **0.1513** |
| Overlap/EN (∩/EN) | 0.1877 |
| Overlap/ZH (∩/ZH) | 0.4383 |
| EN-only tokens | 13,317 |
| ZH-only tokens | 3,943 |
| Overlap as % of vocab | 2.40% |

## Key Observations

1. **Llama 的 ZH→EN overlap 显著高于 Qwen (43.8% vs 22.3%)**：Llama tokenizer 缺乏专用中文 token，将中文文本拆成更多 byte-level 或共享 subword token，导致 ZH token 集合更小（7,020 vs 10,140）且与 EN 重叠更大。

2. **Qwen 的 ZH token 集合更大且更独立**：Qwen tokenizer 有专门的中文 token（vocab 151K vs 128K），ZH 使用了 10,140 个 unique token，EN-ZH 分离度更高。

3. **对跨语言探针迁移的含义**：
   - Llama 的高 token overlap 可能有利于 EN→ZH 探针迁移（共享更多 token-level 表示）
   - Qwen 的低 overlap 意味着跨语言迁移必须更多依赖语义层面（higher layers）而非 token 层面的共享表示

## Script

`/root/clkc_mech_interp/src/token_overlap.py`