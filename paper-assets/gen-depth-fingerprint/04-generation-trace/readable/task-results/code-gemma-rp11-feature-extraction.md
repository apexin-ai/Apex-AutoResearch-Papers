# code gemma rp11 feature extraction

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_gemma-rp11-feature-extraction_20260516T155959_result.json`
- **Structured JSON:** [`b77234bc80f7ed611345.json`](../../sessions/b7/b77234bc80f7ed611345.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。结果摘要：

- **生成数据**: `data/gemma-2-2b-rp11/generations_shard0.jsonl` — 4864 条，994 seeds × 5 depths
- **特征文件**: `data/gemma-2-2b-rp11/features_pythia410m.jsonl` — 4864 条
- **字段**: `seed_id, depth, entropy_mean, entropy_std, entropy_min, entropy_max, tail_decay, ttr, hapax_ratio`
- **tail_decay**: [-0.003935, 0.000000]，确认为负斜率
- **entropy_mean**: [0.0000, 10.0414]
- **ttr**: [0.0039, 1.0000]（低 ttr 值说明有退化文本，符合预期）
- **Depth 分布**: {0: 994, 1: 990, 2: 965, 3: 960, 4: 955}

---
