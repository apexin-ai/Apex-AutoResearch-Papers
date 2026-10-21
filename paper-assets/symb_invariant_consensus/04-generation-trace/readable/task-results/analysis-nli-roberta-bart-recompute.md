# analysis nli roberta bart recompute

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_nli-roberta-bart-recompute_20260521T055056_result.json`
- **Structured JSON:** [`29e19d2aa34342bf3b1b.json`](../../sessions/29/29e19d2aa34342bf3b1b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总结果：

### 验证通过
- SC baseline (alpha) = **236/600 (39.33%)** ✓
- DeBERTa w=3 combo = **276/600 (46.00%)** ✓ 与之前重算匹配

### RoBERTa-MNLI (standalone 37.67%, 226/600)
| w | Combo | Correct | Gain | McNemar p |
|---|-------|---------|------|-----------|
| 1 | 39.17% | 235 | -0.17pp | 1.000 |
| 3 | 43.50% | 261 | **+4.17pp** | **0.0026** |
| 5 | 43.67% | 262 | +4.33pp | 0.037 |

### BART-MNLI (standalone 46.17%, 277/600)
| w | Combo | Correct | Gain | McNemar p |
|---|-------|---------|------|-----------|
| 1 | 39.33% | 236 | 0.0pp | 1.000 |
| 3 | 44.50% | 267 | **+5.17pp** | **0.0002** |
| 5 | 45.67% | 274 | +6.33pp | 0.003 |

### Exact Permutation Spearman (gap vs gain)

**PW 6-point** (all w=3):
- rho = **1.000** (perfect), exact p_two = **0.00278** (2/720), p_one = **0.00139** (1/720)

**All 9-point** (6 PW + 3 FOLIO):
- rho = **0.836**, exact p_two = **0.00703**, p_one = **0.00354**

两个 Spearman 在 alpha=0.01 下均显著。PW6 达到完美秩相关——更大的 capability gap 严格对应更大的 combo gain。

---
