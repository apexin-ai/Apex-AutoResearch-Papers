# ssh sequence entropy vs lp rank

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_sequence_entropy_vs_lp_rank_20260522T012722_result.json`
- **Structured JSON:** [`fa41b96627d583bbb419.json`](../../sessions/fa/fa41b96627d583bbb419.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。结果：

**Spearman ρ(mean_LP_rank, cumulative_LP_rank)**
- Mean: 0.8493, Median: 1.0000, Std: 0.3514

**Threshold**
- ρ > 0.95: 69.2%
- ρ < 0.90: 22.7%

**Rank-1 Disagreement**: 10.6% 的 instance 中 best sample 不同

**Token Count Variance 分层**（关键发现）：
- Low CV (<0.05): ρ=0.999, rank-1 差异 0.1% — 几乎完全等价
- Mid CV (0.05-0.10): ρ=0.981, rank-1 差异 2.2%
- **High CV (>0.10): ρ=0.765, rank-1 差异 16.4%** — 显著不同
- Token CV 与 ρ 的相关系数 r=-0.553 (p≈0)

**结论：NON-TRIVIALLY DIFFERENT。** 当 sample 间 token count 变化小时两者等价，但 63% 的 instance 属于 high CV (>0.10)，在这些 case 里 ranking 显著不同。mean LP 和 cumulative LP 不是 trivially rank-equivalent，使用 mean LP 而非 sequence entropy 是有实质区别的选择，不只是简化。

---
