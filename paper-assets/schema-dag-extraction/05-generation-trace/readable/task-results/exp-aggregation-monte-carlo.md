# exp aggregation monte carlo

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_aggregation_monte_carlo_20260516T114958_result.json`
- **Structured JSON:** [`24355962e0d931f85e49.json`](../../sessions/24/24355962e0d931f85e49.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

## 结果总结

**Simulation 确认 pair→batch aggregation 解释了 R² 放大。**

| 指标 | 值 |
|------|-----|
| Pair-level R² (nonzero pairs, ρ=0.272) | 0.074 |
| Simulated batch R² (MC 10K iter) | **0.219** [0.092, 0.361] |
| Observed batch R² (computed BCS) | **0.218** |
| Amplification factor | ~3× |
| Effective Factor (EF) | 3.35 |

**机制**：8 types 构成的 batch 中 28 个 pair 的 SCS 值正相关（共享 type 的 pair 间 ρ_SCS=0.35），平均后 signal variance 仅降至 1/EF ≈ 1/3.35（而非 1/28），noise 独立故降至 1/28。信噪比放大 → R² 从 0.074 升至 0.219。

**公式**：`R²_batch = SNR × EF / (SNR × EF + 1)`，其中 SNR = R²_pair/(1-R²_pair)

**论文影响**：
- "14-35× amplification" 这个说法需要修正。实际 R²-to-R² 放大倍数是 **~3×**（0.074→0.22）。原文的 14-35× 是 pair-r² (0.015) vs batch-R² (0.22-0.53) 的比值，混用了不同的 pair-level 度量。
- 建议改写为：「The ~3× amplification from pair-level R²=0.074 to batch-level R²=0.22 is consistent with the analytical aggregation formula (EF≈3.4), where signal correlation within batches preserves variance while noise averages out.」

---
