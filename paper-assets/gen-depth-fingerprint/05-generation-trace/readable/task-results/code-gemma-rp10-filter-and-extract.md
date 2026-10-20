# code gemma rp10 filter and extract

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_gemma-rp10-filter-and-extract_20260516T120943_result.json`
- **Structured JSON:** [`0b97f5f5761fbf0dafcb.json`](../../sessions/0b/0b97f5f5761fbf0dafcb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。结果：

### Phase 1: Soft Filter

| Depth | 原始 | 保留 | 移除率 |
|-------|------|------|--------|
| 0 | 994 | 994 | 0.0% |
| 1 | 993 | 19 | 98.1% |
| 2 | 990 | 16 | 98.4% |
| 3 | 990 | 15 | 98.5% |
| 4 | 990 | 17 | 98.3% |
| **Total** | **4957** | **1061** | **78.6%** |

**与预期不符**：Gemma-2-2B rp=1.0 在 depth ≥ 1 时严重退化（repeated_4gram_ratio > 0.5 的样本占 ~98%）。Depth-0（原始人类文本）完全未受影响。这说明 Gemma-2-2B 无 repetition penalty 时在递归生成中几乎全面崩溃。

### Phase 2: 3-ref Feature Extraction

| 文件 | 行数 |
|------|------|
| `features_pythia410m.jsonl` | 1061 |
| `features_olmo2-1b.jsonl` | 1061 |
| `features_qwen3-06b.jsonl` | 1061 |

特征字段：`seed_id, depth, entropy_mean, entropy_std, entropy_min, entropy_max, tail_decay, ttr, hapax_ratio`

90th percentile NLL thresholds (from depth-0):
- Pythia-410M: 6.5664
- OLMo-2-1B: (logged in first run)
- Qwen3-0.6B: 6.2773

**注意**：过滤后仅剩 67 条 depth > 0 样本，下游分类实验可能需要考虑是否对 Gemma 使用不同 filter 阈值或完全跳过 filter。

---
