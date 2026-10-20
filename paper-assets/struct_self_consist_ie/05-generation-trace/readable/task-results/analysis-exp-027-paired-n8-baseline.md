# analysis exp 027 paired n8 baseline

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_027_paired_n8_baseline_20260517T054603_result.json`
- **Structured JSON:** [`676cf6daa4d935146acd.json`](../../sessions/67/676cf6daa4d935146acd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。结果如下：

## Paired Comparison: Same 4,351 Instances (gold-filtered from 5000 matched)

| Metric | N=8 | N=16 | Paired Δ |
|--------|-----|------|----------|
| Degeneracy | 11.08% | 4.53% | -6.55pp |
| Greedy F1 | 0.7478 | 0.7476 | -0.02pp |
| LP Sel F1 | 0.7614 | 0.7664 | +0.50pp |
| **LP Δ vs Greedy** | **+1.37pp** | **+1.88pp** | **+0.52pp** |
| Oracle F1 | 0.8692 | 0.9019 | +3.27pp |
| LP ρ (Spearman) | 0.6226 | 0.6248 | +0.0022 |

## Key Statistical Results

**N=8 LP Selection Bootstrap:**
- +1.37pp, 95% CI [0.88, 1.86], p < 0.001 — significant at N=8 too

**Paired Bootstrap (N=16 LP Δ − N=8 LP Δ):**
- **+0.52pp, 95% CI [0.17, 0.87], p = 0.0034** — **LP selection scales with N (statistically significant)**

## Interpretation

1. LP selection is already significant at N=8 (+1.37pp), confirming the method works even with fewer samples.
2. Doubling from N=8 to N=16 yields an additional +0.52pp on the same instances, with CI excluding zero (p=0.003).
3. Greedy is stable across N (≈0 diff, as expected from T=0 decoding).
4. Degeneracy drops by 6.5pp (11% → 4.5%) with more samples — more diversity at N=16.
5. 6/8 entity types show improvement; `location` and `person` (high-degeneracy types) show marginal regression.

Saved to: `output/exp_027_fewnerd_n16/paired_n8_baseline.json`

---
