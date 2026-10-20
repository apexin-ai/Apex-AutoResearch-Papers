# computation fleiss kappa exp033

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_computation_fleiss-kappa-exp033_20260519T033107_result.json`
- **Structured JSON:** [`673fe92b6338ac5aed9a.json`](../../sessions/67/673fe92b6338ac5aed9a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

计算完成。结果已保存到 `/root/symb_invariant_consensus/results/fleiss_kappa_exp033.json`。

## exp-033 (Mistral-7B FOLIO-204, K=12)

| 指标 | 值 |
|---|---|
| **Fleiss' κ** | **0.5006** |
| **Effective K** | **4.999** |
| Unanimous rate | 27.5% |
| Mean max agreement | 78.8% |
| Mean valid votes/q | 10.01 (部分 trace 未产出有效答案) |
| Category distribution | True 26.7%, False 23.4%, Unknown 49.9% |

## exp-046 (Mistral-7B PW-600, K=12)

| 指标 | 值 |
|---|---|
| **Fleiss' κ** | **0.2102** |
| **Effective K** | **7.485** |
| Unanimous rate | 20.0% |
| Mean max agreement | 76.6% |
| Category distribution | True 14.4%, False 14.4%, Unknown 71.2% |

**解读**：exp-033 的 κ=0.50 属于 moderate agreement (Landis & Koch 标准)，Effective K ≈ 5，说明 12 条 traces 中约 5 条提供了独立信息。exp-046 在更难的 PW-600 上 κ=0.21 (fair agreement)，traces 间一致性更低，Effective K ≈ 7.5。注意约 16.6% (exp-033) 和 21.0% (exp-046) 的 traces 未产出有效答案（空 answer），计算时已排除这些无效投票。

---
