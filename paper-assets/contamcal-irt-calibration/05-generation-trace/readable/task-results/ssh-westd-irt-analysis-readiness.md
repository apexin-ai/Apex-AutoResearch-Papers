# ssh westd irt analysis readiness

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_westd-irt-analysis-readiness_20260519T122447_result.json`
- **Structured JSON:** [`951f3d4130fc545d88e8.json`](../../sessions/95/951f3d4130fc545d88e8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Report: IRT Analysis Readiness on westd-29999

### Eval Data Availability (Phase 2 v2)

Location: `/root/autodl-tmp/exp001/eval_results_v2/`

| Family   | d000 | d005 | d025 | d050 | d100 |
|----------|------|------|------|------|------|
| qwen7b   | OK   | OK   | OK   | OK   | OK   |
| qwen14b  | OK   | OK   | OK   | OK   | OK (new, not in summary CSV) |
| gemma2   | OK   | OK   | OK   | OK   | OK   |
| phi4     | OK   | OK   | OK   | OK   | OK (new, not in summary CSV) |
| olmo2    | OK (new) | **EMPTY** | OK (new) | **EMPTY** | OK (new) |

- **phase2_summary.csv** is stale (generated before olmo2/phi4_d100/qwen14b_d100 data landed)
- **olmo2_d005 and olmo2_d050** directories exist but are empty (no eval_results.json)
- All other 23/25 cells have complete data with per-item correctness (`correctness_matrix.json`, `item_responses.json`)

### Analysis Scripts

**exp001/** (Phase 2 analysis):
- `analyze_phase2.py` — loads v2 results, builds summary CSV, dose-response plots
- `fit_irt_dose_response.py` — 2PL IRT fitting (scipy MLE), theta estimation, dose-response curves, TOST equivalence tests
- `convert_lm_eval_to_irt.py` — converts lm_eval JSONL output to IRT-compatible format

**exp006/** (Bayesian IRT with Stan, most mature):
- `run_irt_stan.py` — CmdStanPy 4PL+gamma Bayesian IRT pipeline
- `run_irt_calibration.py` — IRT calibration runner
- `run_pooled_4bench_irt.py`, `run_stratified_irt.py`, `run_pooled_rrf_irt.py` — pooled/stratified variants
- `run_mmlu_domain_gamma_*.py` — domain-level gamma analysis
- `run_cross_family_*.py` — cross-family validation
- `baselines.py`, `evaluate_calibration.py` — baseline methods and calibration evaluation
- `power_analysis.py`, `tost_equivalence.py`, `compute_ci_coverage.py` — statistical analysis

**Stan models** (6 compiled models in `/root/contamcal-irt-calibration/stan_models/`):
- `contam_irt_2pl_gamma` (+ tight/loose prior variants)
- `contam_irt_4pl_simple` (+ wider variant)
- `contam_irt_4pl`
- `vanilla_2pl` (+ noll variant), `vanilla_4pl`

**Existing IRT results**: `irt_dose_response.csv` already has theta estimates for 4 families (olmo2 only has d100). This is also stale.

### What's Missing

1. **olmo2_d005 and olmo2_d050 eval results** — these 2 cells need to be run before olmo2 can be included in IRT fitting with full dose-response coverage
2. **phase2_summary.csv needs regeneration** — currently missing phi4_d100, qwen14b_d100, and 3 olmo2 entries that now have data
3. **irt_dose_response.csv needs regeneration** — was fit without the newly available data (olmo2 d000/d025, phi4_d100, qwen14b_d100)

With 23/25 cells available, IRT fitting can run for 4 families (qwen7b, qwen14b, gemma2, phi4) immediately. OLMo2 needs d005 and d050 evals first.

---
