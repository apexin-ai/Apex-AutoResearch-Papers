# analysis quant dummy regression

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_quant-dummy-regression_20260524T184151_result.json`
- **Structured JSON:** [`71c40d462771f90bd849.json`](../../sessions/71/71c40d462771f90bd849.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

JSON written (3100 lines). Results summary:

| K | K_eff sig | K_eff β_std mean | Interaction sig | Int direction | quant_frac sig | η_max sig |
|---|-----------|------------------|-----------------|---------------|----------------|-----------|
| 3 | 6/12 | +0.392 | 5/12 | negative | 6/12 | 7/12 |
| 5 | 6/12 | +0.341 | 2/12 | mixed | 2/12 | 11/12 |
| 7 | 4/12 | +0.270 | 0/12 | mixed | 0/12 | 12/12 |

**Key findings:**

1. **K_eff survives quant_frac control**: Significant in 6/12 (K=3), 6/12 (K=5), 4/12 (K=7) conditions via wild cluster bootstrap. Quantization composition does not eliminate the K_eff effect.

2. **Interaction K_eff×quant_frac**: Significant at K=3 (5/12, negative direction) but drops to 0/12 at K=7. At larger panels, quantization fraction does not modulate the K_eff effect.

3. **Predictor shift does NOT survive**: K_eff sig count decreases 6→6→4 (vs the original increasing pattern). However, this is confounded by high VIF (100-1000+) for quant_frac/interaction terms at large K, which inflates SEs for all coefficients.

4. **VIF diagnostic**: quant_frac and interaction VIFs are extreme (36-1086) due to inherent collinearity of the uncentered interaction. K_eff VIF is moderate (6-20). The extreme VIF for quant_frac/interaction makes those coefficient estimates unreliable, but the K_eff bootstrap test remains interpretable since the restricted model (without K_eff) is well-defined.

5. **η_max dominance grows**: η_max sig goes 7/12 → 11/12 → 12/12, confirming its increasing importance at larger K — consistent with the original analysis.

---
