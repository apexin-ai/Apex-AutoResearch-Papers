# analysis n6 multi metric ensemble

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_n6_multi_metric_ensemble_20260519T161804_result.json`
- **Structured JSON:** [`aefd0e9588d0cbf2ef58.json`](../../sessions/ae/aefd0e9588d0cbf2ef58.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 4 models completed successfully. Results:

**Key findings:**

| Model | Best Single | Ensemble | Delta | Text | Ens-Text |
|-------|------------|----------|-------|------|----------|
| R1-8B | 0.6040 | 0.5651 | -0.039 | 0.3718 | +0.193 |
| OT-7B | 0.4731 | **0.5060** | **+0.033** | 0.2360 | +0.270 |
| QwQ-32B | 0.5777 | 0.5775 | -0.000 | 0.3741 | +0.203 |
| R1-32B | 0.5833 | 0.5810 | -0.002 | 0.4764 | +0.105 |

**Ensemble vs Text**: Significant on all 4 models (p<0.05 for precision across all, 11/12 HB-correctable). The HS ensemble dominates text by +10-27pp precision.

**Ensemble vs best single layer**: Ensemble is comparable to or slightly below the best single layer on 3/4 models (R1-8B, QwQ-32B, R1-32B) — this is expected since ensemble smooths toward the mean. On OT-7B, ensemble actually *beats* the best single layer (+3.3pp precision), showing the variance reduction benefit.

**Layer sensitivity mitigation**: Ensemble consistently falls within or above the single-layer range, eliminating the worst-case penalty. For QwQ-32B, the single-layer precision range was 4.3pp (0.535-0.578) — ensemble lands at 0.578, near the top.

3rd candidates found:
- R1-8B: L20 (FPR-best from val sweep)
- OT-7B: L18 (FPR-best from random-CP data)
- QwQ-32B: L63 (paper's threshold consensus)
- R1-32B: L44 (FPR-best from val sweep)

Outputs saved to `artifacts/n6_multi_metric_ensemble/results.json` and `report.txt`.

---
