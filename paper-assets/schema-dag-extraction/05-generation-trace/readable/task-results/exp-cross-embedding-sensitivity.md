# exp cross embedding sensitivity

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_cross-embedding-sensitivity_20260516T050545_result.json`
- **Structured JSON:** [`91b60693b2bc45a7d1bc.json`](../../sessions/91/91b60693b2bc45a7d1bc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。结果摘要：

**Few-NERD（pairwise SCS vs confusion counts, n=1953 pairs）**
| Embedding | Pearson r | p-value | Spearman ρ | p-value |
|-----------|-----------|---------|------------|---------|
| Qwen3 | 0.138 | 1.0e-9 | 0.168 | 7.3e-14 |
| MiniLM | 0.172 | 2.0e-14 | 0.144 | 1.7e-10 |

两种 embedding 均高度显著，方向一致。信号对 embedding 选择鲁棒。

**FewRel BCS-accuracy regression（27 count_8 batches）**
| Embedding | slope | r | p |
|-----------|-------|------|------|
| MiniLM | -0.485 | -0.398 | 0.040 |
| Qwen3 | -0.542 | -0.185 | 0.356 |

Qwen3 方向一致（负斜率）但不显著，原因是 BCS range 被压缩（std=0.034 vs MiniLM std=0.081）。Qwen3 的 causal-LM embeddings 对短文本标签的 cosine similarity 几乎均匀分布在 0.82-0.95 之间，缺乏区分力。

**结论**：SCS-confusion 信号对 embedding 选择鲁棒（方向一致）。MiniLM sentence-transformer 是 BCS 计算的合适编码器（专门训练做语义相似度），Qwen3 因 range compression 不适合此用途。

---
