# code mixed depth corpus b

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_mixed_depth_corpus_b_20260517T035401_result.json`
- **Structured JSON:** [`2d30f5cc6b66f98dd133.json`](../../sessions/2d/2d30f5cc6b66f98dd133.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成。

## 结果总结

**mixed_depth_corpus_001** — Hypothesis **CONFIRMED**

| 指标 | Mixed (50/30/15/5%) | Balanced (25/25/25/25%) | Δ |
|------|-----|-----|---|
| Overall accuracy | 0.855 | 0.781 | +7.36pp (weighting artifact) |
| **Macro-recall** | 0.765 | 0.781 | **-1.62pp** ✓ |

Per-class recall 差异（max 2.43pp on d1）来自不同 held-out 样本的抽样噪声，而非分类器行为变化。RF 是确定性 per-sample 分类器，对同一输入无论 corpus 组成如何都给出相同预测。

Overall accuracy 差异的本质：mixed corpus 中 d0 占 50%，d0 recall 99%，所以 weighted accuracy 被拉高。这是指标定义问题，不是分类器问题。用 macro-recall 衡量，差异仅 -1.62pp，在 2pp 阈值内。

---
