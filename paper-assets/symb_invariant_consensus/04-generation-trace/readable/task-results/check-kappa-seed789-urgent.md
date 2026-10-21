# check kappa seed789 urgent

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_kappa-seed789-urgent_20260524T064339_result.json`
- **Structured JSON:** [`e4bf636cb13a8ee93750.json`](../../sessions/e4/e4bf636cb13a8ee93750.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

计算完成。结果如下：

## Mistral-7B seed789 FOLIO-204 真实值

从 `results/multi_seed/mistral_folio_seed789/results.json` 的 `sc_vote_distribution` 直接计算 Fleiss' kappa：

| 指标 | 值 |
|------|-----|
| **Fleiss' κ** | **0.4943** |
| **K_eff** | **1.86** |
| SC acc | 59.31% |
| SICA acc | 56.86% |
| N | 204 |
| K_mean | 9.98 |
| p_True / p_False / p_Unknown | 0.2569 / 0.2358 / 0.5074 |

main 和 backup 两份 results.json 内容完全一致。

**结论：κ 既不是 0.41 也不是 0.45，而是 0.4943。K_eff 既不是 2.17 也不是 2.03，而是 1.86。**

注意：这个值和 unified 文件（`fleiss_kappa_unified_16639.json`）中 seed123/456 的计算方法可能有差异——unified 文件里 exp052(seed123) κ=0.4572、exp053(seed456) κ=0.4565 是从 exp 目录计算的，而 multi_seed 目录的数据与 exp 目录不完全相同（multi_seed/seed456 只有 93 个问题）。seed789 从未被加入 unified 文件。

---
