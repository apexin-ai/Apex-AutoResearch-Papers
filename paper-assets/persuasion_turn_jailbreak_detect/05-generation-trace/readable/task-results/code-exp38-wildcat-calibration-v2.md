# code exp38 wildcat calibration v2

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp38-wildcat-calibration-v2_20260521T013619_result.json`
- **Structured JSON:** [`ed46d8dd8c21d0b83591.json`](../../sessions/ed/ed46d8dd8c21d0b83591.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Experiment complete. Here's the summary:

## exp38_wildcat_calibration — Results (NEGATIVE)

| Metric | Value |
|--------|-------|
| ROC AUC | 0.700 ± 0.054 |
| Default t=0.5 FPR | 79.1% ± 9.8% |
| Optimal threshold (TPR≥95%) FPR | **62.7% ± 10.0%** |
| Optimal threshold (TPR≥90%) FPR | **58.7% ± 9.1%** |
| Temperature (LOO-226) | T = 20–40 (severe overconfidence) |
| Temp-scaled FPR@TPR95 | 62.7% (identical — ROC invariant) |
| Temp-scaled FPR@TPR90 | 58.3% |

**Per-seed AUC**: seed42=0.768, seed123=0.697, seed456=0.635

### Key findings

1. **AUC=0.70** — the model has limited ability to distinguish WildChat benign from jailbreak. This is the fundamental ceiling.
2. **Threshold adjustment** drops FPR from 79% → 63% (at TPR≥0.95), a ~16pp improvement but still far from the <25% target.
3. **Temperature scaling** does NOT change operating-point FPR because ROC is invariant to monotonic score transforms. The learned T=20–40 confirms the model is severely overconfident (all probabilities clustered near 1.0).
4. **Conclusion: NEGATIVE** — WildChat high FPR is genuine domain shift, not a calibration artifact. Post-hoc threshold/temperature calibration is insufficient.

### Output artifacts
- Results JSON: `results/exp38_wildcat_calibration.json`
- Figures: `results/exp38_roc/` (roc_curve, roc_comparison, prob_distributions — PDF+PNG)
- Script: `scripts/exp38_wildcat_calibration.py`

Registry updated to **DONE (negative)**.

---
