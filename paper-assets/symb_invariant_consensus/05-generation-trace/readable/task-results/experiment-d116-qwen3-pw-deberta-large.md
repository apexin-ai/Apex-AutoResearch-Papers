# experiment d116 qwen3 pw deberta large

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_d116-qwen3-pw-deberta-large_20260520T204022_result.json`
- **Structured JSON:** [`6d21ab297fe4bd0482d8.json`](../../sessions/6d/6d21ab297fe4bd0482d8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果完整写入。总结：

**D116 Qwen3-14B ProofWriter DeBERTa-large Combo 结果**

| 指标 | 值 |
|------|-----|
| DeBERTa-large standalone | **55.00%** (330/600) ✓ 与 Dir-J3 一致 |
| SC baseline | 85.00% (510/600) |
| Combo w=1 | 85.83% (+0.83pp, p=0.125) |
| Combo w=3 | 86.00% (+1.00pp, p=0.146) |
| Combo w=5 | **86.83% (+1.83pp, p=0.052)** |

与 Dir-K (deberta-base) 对比：
- deberta-base standalone: 36.17% → deberta-large: **55.00%** (+18.83pp)
- deberta-base combo w=5: 85.50% (+0.50pp) → deberta-large combo w=5: **86.83% (+1.83pp)**
- 互补性更强：NLI_right_SC_wrong 从 40 升到 **61**
- w=5 时 p=0.052 接近显著

结果已保存至 `/root/symb_invariant_consensus/results/d116_qwen3_pw_deberta_large/results.json`。

---
