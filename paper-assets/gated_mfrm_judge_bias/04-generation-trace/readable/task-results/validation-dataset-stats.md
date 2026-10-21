# validation dataset stats

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_validation_dataset-stats_20260525T203822_result.json`
- **Structured JSON:** [`4b1ac8e8f1ba6cb07549.json`](../../sessions/4b/4b1ac8e8f1ba6cb07549.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Results are clear. Here's the verification summary:

```
Item 1 (Fill rate): [MATCH] 论文=~58%, 实际=57.6% (36274/63000, N=18, I=500, J=7, ties discarded)

Item 2 (Judge coverage): [PARTIAL MISMATCH]
  Sonnet:  论文≈79%, 实际=78.4% (392/500 raw) → MATCH
  Gemini:  论文≈63%, 实际=59.8% (299/500 raw) → MISMATCH (差 ~3pp)
  
  注意：Gemini 有大量 failed 记录。198/299 items 有 ok 状态，101 items 全部 failed。
  如果论文的"coverage"指 status=ok，Gemini 只有 39.6%，更不匹配。
  如果指 raw（曾尝试评判），是 59.8%，仍差 3pp。

Item 3 (Exposure coverage): [MATCH]
  论文=46% → 实际=231/500=46.2% ✓
  论文=73% → 实际=231/317=72.9% ✓
  论文=231 exposed-only → 实际=231 ✓
  Filtered set = 317 items (exposure CSV 行数) ✓
```

**需要关注的问题**：Gemini coverage 59.8% vs 论文 63%。可能原因：
1. 论文写作时数据版本不同（后续 retry 增加或减少了成功数）
2. 论文对 coverage 有不同定义（如只算 J=6 子集中的相对比例）
3. 论文 ~63% 是近似值但实际误差偏大

---
