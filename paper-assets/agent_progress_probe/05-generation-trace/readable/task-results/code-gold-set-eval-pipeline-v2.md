# code gold set eval pipeline v2

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_gold-set-eval-pipeline-v2_20260514T224916_result.json`
- **Structured JSON:** [`395eb696812f7ad99750.json`](../../sessions/39/395eb696812f7ad99750.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All new functions present. Summary of changes:

**P0-1: Inter-Annotator Agreement**
- `_fleiss_kappa()` — manual implementation with formula citation (Fleiss 1971)
- `compute_inter_annotator_agreement()` — handles 1/2/3+ annotators, κ ≥ 0.8 gate, warns but doesn't abort
- Called in main() after gold load, before model evaluation
- Result written to `inter_annotator_agreement` field in output JSON

**P0-2: Bootstrap CIs + McNemar**
- `_paired_bootstrap_ci()` — 1000 resamples, returns (mean_diff, ci_lower, ci_upper)
- `_mcnemar_test()` — continuity-corrected, uses scipy.stats.chi2
- `compute_pairwise_comparisons()` — all model pairs via `itertools.combinations`
- All evaluate functions now return `pred_map` for McNemar input
- Results written to `pairwise_comparisons` field in output JSON

**Minor fix 1: LLM pseudo-probability**
- Reliability diagram key changed from `"LLM-as-Judge"` to `"LLM-as-Judge (pseudo-probability)"`

**Minor fix 2: Structural feature assertion**
- Added `STRUCTURAL_FEATURE_NAMES` (30 names from `non_nlp_baseline.py`)
- Added assertions: `vec.shape[0] == 30` and `len(STRUCTURAL_FEATURE_NAMES) == 30`

READY — all reviewer gaps addressed.

---
