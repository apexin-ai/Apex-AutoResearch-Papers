# analysis calibration baseline

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_calibration_baseline_20260517T141557_result.json`
- **Structured JSON:** [`4deb1c64adebf2b2a795.json`](../../sessions/4d/4deb1c64adebf2b2a795.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Done. Here's the report:

## Summary Table

| Dataset | Greedy | Raw LP | Platt LP | MF-Platt | TempScale | Oracle |
|---------|--------|--------|----------|----------|-----------|--------|
| SciERC  | 0.6436 | 0.6495 | 0.6495   | 0.6386   | 0.6495    | 0.7775 |
| CoNLL   | 0.9087 | 0.8975 | 0.8975   | 0.9007   | 0.8975    | 0.9614 |
| Few-NERD| 0.7712 | 0.7845 | 0.7845   | 0.7782   | 0.7845    | 0.9134 |

## Key Finding

**Standard Platt/TempScale cannot improve LP-based selection.** Both are monotonic transforms of LP, so argmax is preserved. They improve *calibration quality* (ECE drops from 0.26-0.39 → 0.01-0.08) but cannot change which sample is selected.

## Multi-feature Platt (LP + n_tokens + n_entities)

This non-monotonic variant *can* change selection but shows no significant improvement:
- SciERC: -0.011 (p=0.72)
- CoNLL: +0.003 (p=0.31)  
- Few-NERD: -0.006 (p=0.83)

None reach statistical significance. On CoNLL it shows a marginal improvement (+0.32pp) but still well short of significance.

## Calibration Quality (ECE)

| Dataset | Raw LP | Platt | MF-Platt | TempScale |
|---------|--------|-------|----------|-----------|
| SciERC  | 0.260  | 0.048 | 0.024    | 0.288     |
| CoNLL   | 0.392  | 0.012 | 0.006    | 0.423     |
| Few-NERD| 0.262  | 0.080 | 0.064    | 0.300     |

Platt dramatically improves probability estimates (ECE), just not selection.

## Learned Parameters

- **Platt slopes** are large (7.6 - 31.2), reflecting that LP has very narrow range
- **MF-Platt coefs**: LP is dominant (0.88-1.73), n_entities has negative weight (-0.20 to -0.86, penalizing over-generation), n_tokens effect is mixed
- **TempScale τ**: hits boundary on SciERC/CoNLL (148.4), meaningful only on Few-NERD (1.20)

## Conclusion for the paper

Calibration is a natural baseline but fundamentally limited for sample selection: since LP-based selection uses within-instance argmax, any monotonic calibration is equivalent to raw LP. Even multi-feature calibration that breaks monotonicity provides no significant gain, confirming that the challenge is not about probability calibration but about the weak correlation between LP ranking and quality ranking within instances.

**Outputs:**
- `scripts/calibration_baseline.py`
- `output/calibration_baseline_results.json`

---
