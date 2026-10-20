# code check llama8b 10k done

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_check_llama8b_10k_done_20260522T191635_result.json`
- **Structured JSON:** [`6a6acfb8c76683668667.json`](../../sessions/6a/6a6acfb8c76683668667.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All tasks complete. Here's the final summary:

---

## exp_llama8b_10k Bootstrap CI Results

| Metric | Value |
|--------|-------|
| OOF AUC (GroupKFold-5) | 0.5880 |
| 95% CI | [0.5809, 0.5950] |
| 99.5% Bonferroni CI | [0.5776, 0.5978] |
| Bonferroni pass (CI lower > 0.60) | **False** |
| Permutation p-value | 0.0001 |
| Bootstrap iterations | 10,000 |
| Permutation iterations | 10,000 |

## 10K vs 5K Comparison

| Metric | 5K | 10K | Delta |
|--------|-----|-----|-------|
| K* | 2 | 2 | same |
| 1v2 AUC (pipeline) | 0.6123 | 0.6316 | +0.0193 |
| 1v2 OOF AUC (bootstrap) | — | 0.5880 | — |
| CI lower (95%) | 0.6028 | 0.5809 | -0.0219 |
| Bonferroni pass | — | False | — |

**关键发现**: 尽管 pipeline 的 pairwise AUC 从 5K 的 0.6123 提升到 10K 的 0.6316，但 GroupKFold OOF AUC 仅 0.5880，低于 0.60 阈值。Bonferroni 99.5% CI lower bound = 0.5776，未能越过 θ=0.60 门槛。permutation p=0.0001 表明 AUC 显著高于随机，但效应量不足以通过 Bonferroni 校正后的阈值。pipeline AUC 和 OOF AUC 之间的差距（0.6316 vs 0.5880）提示可能存在过拟合或特征泄漏问题。

---
