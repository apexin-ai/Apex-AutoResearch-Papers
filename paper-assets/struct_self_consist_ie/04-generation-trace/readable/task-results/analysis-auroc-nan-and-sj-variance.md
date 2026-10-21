# analysis auroc nan and sj variance

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_auroc_nan_and_sj_variance_20260518T232350_result.json`
- **Structured JSON:** [`8a12dc1760ea88b76cf0.json`](../../sessions/8a/8a12dc1760ea88b76cf0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All done. Here's the complete report:

---

## Problem A: AUROC NaN — Root Cause + Fix

**Root cause**: The s789 script used `greedy_f1 > median` as the binary label. For FewNERD, **median greedy F1 = 1.0** (>50% instances have perfect extraction), so `greedy_f1 > 1.0` produces **zero positive labels**. sklearn `roc_auc_score` returns NaN with a warning (not raising), so the `except: auroc=0.5` never triggered. Additionally, the other seeds used a completely different AUROC definition (oracle-based sample-level) from `analyze_fewnerd_results.py`.

**Fix applied** to `analyze_fewnerd_s789.py`:
- Replaced broken `greedy_f1 > median` with oracle-based sample-level AUROC (Mann-Whitney U)
- Consistent with seed42/123/456 definition

| Signal | Before | After | seed42 ref |
|--------|--------|-------|------------|
| LP | NaN | 0.5994 | 0.5782 |
| SJ | NaN | 0.5139 | 0.5197 |
| FK | NaN | 0.5131 | 0.5210 |
| EM | NaN | 0.5033 | 0.5137 |
| VC | NaN | 0.5392 | 0.5354 |

**4-seed summary**: Does NOT reference NaN AUROC values — no downstream contamination.

---

## Problem B: SJ Selection Delta — Real Seed Variance

Using **identical code** for all 4 seeds (`debug_sj_variance.py`):

| Seed | SJ soft Δpp | SJ hard Δpp | LP Δpp |
|------|------------|-------------|--------|
| 42 | **-2.14** | -2.26 | +1.36 |
| 123 | **-2.91** | -3.34 | +1.44 |
| 456 | **-0.76** | -0.94 | +1.37 |
| 789 | **-6.24** | -6.22 | +1.36 |

- SJ soft delta: mean=-3.01, std=2.02, range=5.48pp
- LP delta: mean=+1.38, std=0.04 (very stable by comparison)
- Hard vs soft Jaccard difference: 0.02-0.43pp (negligible)

**Conclusion**: The 4pp gap between s789 (-6.2pp) and s42 (-2.1pp) is **real seed variance**. The s789 script used hard Jaccard (now fixed to soft), but this only accounted for ~0.02pp. SJ selection is intrinsically more variable than LP selection across seeds.

---

## Files Modified
- `code/analyze_fewnerd_s789.py` — AUROC fix + SJ soft Jaccard
- `output/fewnerd_seed789_merged/analysis.json` — regenerated
- `output/fewnerd_seed789_merged/full_signal_analysis.json` — regenerated

## New Files
- `code/debug_sj_variance.py` — unified 4-seed comparison script
- `output/debug_sj_variance_results.json` — 4-seed SJ delta results

---
