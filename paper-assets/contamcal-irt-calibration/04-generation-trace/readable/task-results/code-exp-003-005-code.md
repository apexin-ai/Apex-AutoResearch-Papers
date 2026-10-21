# code exp 003 005 code

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp-003-005-code_20260513T174924_result.json`
- **Structured JSON:** [`d45f50b44ea7b58e50d6.json`](../../sessions/d4/d45f50b44ea7b58e50d6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Both scripts pass `--help` verification. Here's a summary of what was created:

**exp-003 (`artifacts/exp003_rrf_ablation/`)**:
- `analyze_rrf_ablation.py` — Computes AUC-ROC for: full RRF, single-signal baselines, drop-one-signal, logistic regression (5-fold CV), k sensitivity (20/40/60/80/100), and all 2- and 3-signal subsets. Outputs JSON results + LaTeX table.
- `run_exp003.sh` — Shell orchestration with configurable `SIGNAL_DIR`, `LABELS_DIR`, `BENCHMARKS`, `DOSAGE`.

**exp-005 (`artifacts/exp005_noise_propagation/`)**:
- `run_noise_propagation.py` — Generates synthetic 4PL IRT data across 5 σ_e levels × 5 seeds, fits both ME and simple Stan models, extracts 95% CI widths, checks monotonicity via Spearman correlation. Saves results incrementally.
- `run_exp005.sh` — Shell orchestration with configurable Stan model paths, seed count, and data dimensions.

---
