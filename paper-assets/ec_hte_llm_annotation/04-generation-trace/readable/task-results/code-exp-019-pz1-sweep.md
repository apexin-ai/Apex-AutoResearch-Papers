# code exp 019 pz1 sweep

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp-019-pz1-sweep_20260521T153115_result.json`
- **Structured JSON:** [`fdb465b12874641959dd.json`](../../sessions/fd/fdb465b12874641959dd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

exp-019 complete. Key results:

**Theorem 1 R²**: 0.976–0.998 across all (P(Z=1), K) settings — bias decomposition holds universally, not just at P(Z=1)=0.5. This directly addresses M2.

**RMSE ratio (HB/Global)**:
- **K=2**: HB wins everywhere (ratio 0.76–0.92), best advantage at P(Z=1)=0.2
- **K=4**: HB loses everywhere (ratio 1.06–1.68) — with 250 experts split across 4 subgroups, per-subgroup CM estimates are too noisy (especially the minority Z class at low P(Z=1)), and variance amplification from matrix inversion overwhelms the bias correction benefit

**Coverage**: HB maintains near-nominal 95% coverage (0.92–0.94) across all settings, while naive (0.65–0.79) and global_corrected (0.79–0.90) undercover substantially.

**Outputs**:
- Script: `exp019_pz1_sweep.py`
- CSV: `results/exp019_pz1_sweep_results.csv` (30k rows)
- Analysis: `results/exp019_pz1_sweep_analysis.md`
- Figures: `artifacts/pz1_sweep/` (4 plots)

---
