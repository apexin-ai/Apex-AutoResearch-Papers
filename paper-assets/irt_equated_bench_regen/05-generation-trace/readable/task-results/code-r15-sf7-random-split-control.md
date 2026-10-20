# code r15 sf7 random split control

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_r15_sf7_random_split_control_20260522T124329_result.json`
- **Structured JSON:** [`355f344a44099bd09a13.json`](../../sessions/35/355f344a44099bd09a13.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All three deliverables are in place:

**Results summary:**
- **Within-2024 random split**: mean C% = 1.34% (95% CI: [1.13%, 1.54%])
- **Size-matched control (full sample, same 403 vs 404)**: mean C% = 1.40%
- **Temporal split**: 31.3% — **23× larger** than random baseline

The within-cohort and full-sample controls match almost exactly (1.34% vs 1.40%), confirming no cohort-specific structure drives C%. The ~1% level (vs 0.10% with larger groups) is the expected MH-DIF Type I rate at N≈400/group (80 models per stratum → noisier Δ_MH). The temporal split's 31.3% is unambiguously real, not artifact.

**Output files** in `artifacts/r15_random_split_control/`:
1. `random_split_report.md` — full report with comparison table
2. `random_split_results.csv` — 100 rows, per-rep C%
3. `random_split_analysis.py` — reproducible script

---
