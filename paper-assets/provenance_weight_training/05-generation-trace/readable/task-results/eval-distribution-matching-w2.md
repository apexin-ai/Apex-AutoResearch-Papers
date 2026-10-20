# eval distribution matching w2

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_distribution_matching_w2_20260519T073140_result.json`
- **Structured JSON:** [`958f019cdc910be055c4.json`](../../sessions/95/958f019cdc910be055c4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验完成。结果摘要：

| Eval Set | Adaptive PPL | Uniform PPL | Δ | Tokens |
|---|---|---|---|---|
| **FineWeb holdout** | **17.65** | 17.69 | -0.04 (adaptive 微弱领先) | 4.1M |
| **OpenWebText** | 18.42 | **18.37** | +0.06 (uniform 更好) | 6.8M |
| **Wikipedia** | 15.47 | **15.34** | +0.14 (uniform 更好) | 27.0M |

**结论：审稿人的质疑成立。** Adaptive weighting 的 PPL 优势仅限于 FineWeb holdout（且差异极小，-0.04）。在完全独立的 OpenWebText 和 Wikipedia eval set 上，uniform weighting 反而略好。这与 tautological distribution matching 的预期一致：adaptive 增大 human-authored 权重 → FineWeb human-heavy eval 上自然更好，但在其他分布上没有泛化。

实验已注册为 `w2_distribution_matching_eval`（conclusion: negative），artifact 已保存。

---
