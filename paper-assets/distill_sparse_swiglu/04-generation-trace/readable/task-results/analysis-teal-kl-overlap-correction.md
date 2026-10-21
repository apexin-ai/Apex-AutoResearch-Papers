# analysis teal kl overlap correction

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_teal_kl_overlap_correction_20260517T044656_result.json`
- **Structured JSON:** [`8660cf89f0b2e351cd4d.json`](../../sessions/86/8660cf89f0b2e351cd4d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。结果摘要：

**Null Baseline (Permutation Test)**
| | KL-only-pruned | Random subset (null) |
|---|---|---|
| Mean \|act\| | 0.0596 | 0.0366 |
| Z-score | 7260.3 | |
| P-value | ≈ 0 | |

**Percentile Rank Method**
- Median: **78.6th** percentile (IQR: 64.4-89.1%)
- KL-only-pruned neurons 系统性地位于 token 内 magnitude 分布的高位

**Per-Layer**
- 31/32 层在 p<0.001 下显著（empirical 1000 permutations 验证）
- 唯一例外：Layer 31（最后一层），z=-186.5，KL-only neurons 反而 magnitude 更低
- Percentile rank 范围：69.5%-87.5%

**结论**：1.48x magnitude ratio 不是 selection bias artifact。KL distillation 确实系统性地 prune 了高 magnitude neurons（TEAL 会保留它们）。

脚本：`/root/distill_sparse_swiglu/scripts/teal_kl_overlap_corrected.py`
输出：`/root/distill_sparse_swiglu/artifacts/teal_kl_overlap_corrected.json`

---
