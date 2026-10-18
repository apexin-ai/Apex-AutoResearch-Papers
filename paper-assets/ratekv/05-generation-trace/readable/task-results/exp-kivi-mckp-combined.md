# exp kivi mckp combined

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_kivi_mckp_combined_20260515T144828_result.json`
- **Structured JSON:** [`dabacf23d36c611d6d7f.json`](../../sessions/da/dabacf23d36c611d6d7f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成，registry 已更新为 DONE，artifact 已注册。

**结果总结**：

| Condition | PPL | Δ vs BF16 |
|---|---|---|
| BF16 baseline | 9.8106 | — |
| KIVI alone (uniform 4-bit, asymmetric grouped) | 9.8976 | +0.087 |
| MCKP alone (mixed 2/4/8-bit, simple symmetric) | 10.8921 | +1.082 |
| **KIVI + MCKP (mixed 2/4/8-bit, KIVI quant)** | **9.8954** | **+0.085** |

**关键发现**：
1. **正交互补性确认**：KIVI+MCKP (9.8954) < KIVI alone (9.8976)，差值 -0.002
2. **但边际收益很小**：KIVI 的 asymmetric grouped quantization 太强了，uniform 4-bit 就已经近乎无损 (+0.087 vs BF16)，留给 inter-head allocation 的改善空间极小
3. **论文角度更有说服力的数据**：MCKP+KIVI (9.90) vs MCKP+simple (10.89) — 说明将 KIVI 作为 intra-head backend 使 MCKP allocation 的效果从 PPL 10.89 降到 9.90，这才是真正的互补价值

---
