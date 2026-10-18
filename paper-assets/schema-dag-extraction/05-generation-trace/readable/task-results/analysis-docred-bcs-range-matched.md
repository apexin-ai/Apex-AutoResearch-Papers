# analysis docred bcs range matched

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_docred_bcs_range_matched_20260519T170948_result.json`
- **Structured JSON:** [`5b318b479a96c7025430.json`](../../sessions/5b/5b318b479a96c7025430.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果非常清晰：

```
=== Before Range Matching ===
count_16: n=55, BCS range=[0.380, 0.757], spread=0.377
  BCS effect = 15.95pp, ρ = -0.7623, slope = -0.7317
count_32: n=55, BCS range=[0.432, 0.695], spread=0.262
  BCS effect = 8.44pp,  ρ = -0.6929, slope = -0.6296
Interaction = 7.52pp, 95% CI: [1.49pp, 12.83pp]

=== After Range Matching (BCS ∈ [0.4325, 0.6950]) ===
count_16: n=29, BCS range=[0.478, 0.690], spread=0.212
  BCS effect = 9.37pp, ρ = -0.5958, slope = -1.3087
count_32: n=55, BCS range=[0.432, 0.695], spread=0.262
  BCS effect = 8.44pp, ρ = -0.6929, slope = -0.6296
Interaction = 0.93pp, 95% CI: [-7.13pp, 7.44pp]

=== Conclusion ===
Interaction change: 7.52pp → 0.93pp (Δ = -6.59pp)
```

**Reviewer 的担忧成立。** Range matching 后 interaction 从 7.52pp 降到 0.93pp（几乎为零），bootstrap CI 跨零 [-7.13pp, 7.44pp]。原始的 sub-additive interaction 基本是 BCS range restriction 的 artifact——count_16 有更宽的 BCS range（0.377 vs 0.262），使得 median split 能捕获更大的 BCS effect，而非 count 本身产生的调节效应。

值得注意的是 range-matched 后 count_16 的线性斜率（-1.31）反而比 count_32（-0.63）更陡，说明在可比 BCS 范围内，count_16 对 BCS 的敏感度更高而非更低。但这个差异的解读需谨慎，因为 count_16 只剩 29 个 batches（主要是 random 组）。

结果已保存到 `/root/schema-dag-extraction/analysis/bcs_range_matched_results.json`。

---
