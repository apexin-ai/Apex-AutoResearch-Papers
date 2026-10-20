# analysis gpt4o br computation

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_gpt4o-br-computation_20260521T143241_result.json`
- **Structured JSON:** [`20d0672f10a6bdf78eb0.json`](../../sessions/20/20d0672f10a6bdf78eb0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

gpt-4o FOLIO-204 的 BR + Process-κ 计算完成，结果：

| 指标 | 值 |
|---|---|
| 完成题数 | 161/204 |
| SC accuracy | 73.91% |
| SICA accuracy | 72.05% |
| Δ (SICA-SC) | -1.86pp |
| SICA 判错数 | 45 |
| **Mean BR** | **2.94** (25 finite, 20 undefined/∞) |
| Median BR | 1.91 |
| Weighted BR | 3.07 |
| **Process-κ (TF-IDF cosine)** | **0.7884** |
| **Answer Fleiss' κ** | **0.8009** |

20/45 SICA 错题的 gold answer 在 `sica_scores` 中权重为 0（完全没有约束支持 gold），导致 BR 为 ∞。有限 BR 的 25 题中 mean=2.94，说明错误约束权重平均是正确约束的近 3 倍。

已注册 artifact `art_20260521_c3dc84`。

---
