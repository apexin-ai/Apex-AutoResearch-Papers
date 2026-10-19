# analysis mvp 001 gate recheck

**Shifting the Cross-Lingual Calibration Pareto Frontier: Probe-Based Calibration Transfer via CaCLR** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_mvp_001_gate_recheck_20260520T182750_result.json`
- **Structured JSON:** [`7762eb5377c54a0873d2.json`](../../sessions/77/7762eb5377c54a0873d2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
=== Updated MVP Gate Check ===

P1 (EN AUROC≥0.60 & ECE<0.15):
  Original: AUROC=0.7486, ECE=0.1982 → FAIL
  After temp scaling: AUROC=0.7486, ECE=0.0888 → PASS
  Temperature T=5.36

P2 (ZS≥0.58 & p<0.05, ≥3/5): [unchanged] PASS (4/5)

P3 (Layer delta≥5pp): [unchanged] PASS (13.7pp)

P4 (Mean-shift ΔECE≤-2pp, ≥3/5):
  Best layer per language chosen by highest zero_shot AUROC:
  zh (L24): ZS_ECE=0.2541  MS_ECE=0.2505  ΔECE= -0.36pp  ΔBrier= -0.54pp → ✗
  ar (L24): ZS_ECE=0.3128  MS_ECE=0.3122  ΔECE= -0.06pp  ΔBrier= -0.02pp → ✗
  hi (L20): ZS_ECE=0.3642  MS_ECE=0.3863  ΔECE= +2.22pp  ΔBrier= +1.86pp → ✗
  sw (L20): ZS_ECE=0.4364  MS_ECE=0.5007  ΔECE= +6.44pp  ΔBrier= +5.92pp → ✗
  ko (L24): ZS_ECE=0.2927  MS_ECE=0.2928  ΔECE= +0.01pp  ΔBrier= +0.01pp → ✗
  Count: 0/5 → FAIL
  (ΔBrier also shows no systematic improvement — only zh has marginal gain)

Hard Fails: F1/F2/F3 [unchanged, all ok]

OVERALL: PARTIAL (3/4 gates pass; P4 fails — mean-shift does not improve calibration)
```

---
