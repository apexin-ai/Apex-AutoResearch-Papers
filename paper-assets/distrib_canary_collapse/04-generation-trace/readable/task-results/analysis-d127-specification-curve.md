# analysis d127 specification curve

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_d127_specification_curve_20260520T095423_result.json`
- **Structured JSON:** [`36bb6aa99d52c1324f6d.json`](../../sessions/36/36bb6aa99d52c1324f6d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

D127 complete. Summary:

**Specification Curve: 1160 specs across 29 experiments, 536 significant (46.2%)**

### Key findings

| Method | Positive Rate | FP at α=0.00 |
|--------|-------------|--------------|
| Naive XCorr | 94.8% | **100%** |
| Diff XCorr (FDR) | 68.1% | 50% |
| Perm Granger (FDR) | 40.1% | **0%** |
| TY Granger | 19.8% | 12.5% |
| Threshold Onset | 8.2% | 37.5% |

**Perm Granger phase transition** (best-calibrated method, 0% FP at null):
- α < 0.50: ~0% detection (0/32 at α=0.25, 0/8 at α=0.30–0.45)
- α = 0.50: 81.2% detection
- α = 0.75: 87.5%
- α = 1.00: 65.3%

**Other contrasts**:
- α ≥ 0.50 vs < 0.50: 53.5% vs 35.8%
- Distinct vs Mauve downstream: 51.4% vs 30.7% (confirms mauve's known weakness)
- Token entropy vs ECE canary: 47.4% vs 45.0% (negligible difference)

### Outputs on westd-17855
- `artifacts/d127_spec_curve/d127_spec_curve.json` — full matrix + stats (391 KB)
- `artifacts/d127_spec_curve/spec_curve.png` — 5-method spec curve
- `artifacts/d127_spec_curve/spec_curve_calibrated.png` — 4-method curve excluding Naive XCorr
- `scripts/d127_spec_curve.py` — analysis script

---
