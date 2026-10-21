# analysis t20 a045 fdr verify

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_t20_a045_fdr_verify_20260520T201650_result.json`
- **Structured JSON:** [`fb019fe756d29beea7f6.json`](../../sessions/fb/fb019fe756d29beea7f6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data extracted. Here are the results:

---

## t20_a045_s42_fp32 Final Results

### PermG Forward (Per-Pair)
| Pair | p_raw | p_fdr | sig | sig_fdr |
|------|-------|-------|-----|---------|
| te→d1 | 0.0390 | **0.0520** | Y | **N** (borderline) |
| te→d2 | 0.0144 | 0.0288 | Y | Y |
| te→d3 | 0.0112 | 0.0288 | Y | Y |
| te→mauve | 0.3601 | 0.3741 | N | N |
| ece→d1 | 0.0218 | 0.0349 | Y | Y |
| ece→d2 | 0.0122 | 0.0288 | Y | Y |
| ece→d3 | 0.0064 | 0.0288 | Y | Y |
| ece→mauve | 0.3741 | 0.3741 | N | N |

**PermG uncorrected: 6/8** (not 5/8 as previously stated)
**PermG FDR: 5/8** (te→d1 drops out at p_fdr=0.052)
**PermG reverse: 0/8** (both uncorrected and FDR)

### Other Methods
| Method | Forward Count |
|--------|--------------|
| DiffXcorr FDR | 7/8 |
| ThresholdOnset | 4/8 |
| TY Granger | 2/8 |

### Consensus
| Pair | K | Methods |
|------|---|---------|
| te→d1 | 2 | diff, threshold |
| te→d2 | **4** | diff, threshold, perm, ty |
| te→d3 | 2 | diff, perm |
| te→mauve | 0 | — |
| ece→d1 | **3** | diff, threshold, perm |
| ece→d2 | **3** | diff, threshold, perm |
| ece→d3 | 2 | diff, perm |
| ece→mauve | 2 | naive, ty |

**K≥3: 3/8, K≥4: 1/8**

---

## Predict-Verify

```
=== Locked Prediction (v2, Power Theory √T) ===
t20_a045 PermG point prediction:  0/8  (rate=0.0001)
t20_a045 PermG median prediction: 0.015 (~0/8)
t20_a045 PermG 95% CI:           [0/8, 7/8]  (rate CI: [0.015, 0.828])

=== Observed ===
PermG FDR forward: 5/8  (rate=0.625)

=== Verdict ===
Point prediction (0/8) FALSIFIED.
Observed 5/8 within bootstrap 95% CI [0,7] but far above median.
```

**Interpretation:** √T Power Theory predicted α=0.45 stays sub-threshold at T=20 (z=-3.69, rate≈0). Observed 5/8 FDR-significant pairs. The phase boundary shifted left substantially more than the √T scaling predicted — the sigmoid's steep α_c=0.4755 estimate was too high, or the effective power gain exceeds √T. The wide CI ([0,7]) correctly captured the uncertainty near the phase transition, but the point estimate missed badly.

Note: the user's prior belief of "uncorrected 5/8" was actually **6/8 uncorrected, 5/8 FDR** — the te→d1 pair is the one that flips (p=0.039 → p_fdr=0.052).

---
