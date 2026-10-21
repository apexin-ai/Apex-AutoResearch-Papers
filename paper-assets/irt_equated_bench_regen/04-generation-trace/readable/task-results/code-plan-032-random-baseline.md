# code plan 032 random baseline

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan_032_random_baseline_20260521T134427_result.json`
- **Structured JSON:** [`63073db33224ac84961a.json`](../../sessions/63/63073db33224ac84961a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All outputs generated and verified. Summary:

**Every DIF removal metric is significantly different from random (all |z| > 3):**

| Metric | DIF | Random (20 trials) | z |
|--------|-----|---------------------|---|
| rank_change σ | 127.1 | 60.2 ± 7.8 | **+8.5** |
| mean \|rank change\| | 74.7 | 36.0 ± 3.6 | **+10.7** |
| % \|Δ\| ≥ 100 | 24.8% | 8.5% ± 2.0% | **+8.2** |
| cohort 2023 mean Δ | **−22.6** | +0.4 ± 4.1 | **−5.6** |
| cohort 2024 mean Δ | **+73.6** | +2.8 ± 21.2 | **+3.3** |
| cohort asymmetry gap | **+96.2** | +2.4 ± 21.6 | **+4.4** |

The critical finding: random removal produces near-zero cohort bias (both cohorts ~0), confirming the **cohort-asymmetric rank shift is specific to DIF-flagged items**, not an artifact of removing 31% of items. DIF removal also produces ~2× more rank disruption than random, indicating C-flagged items concentrate information that differentially affects model rankings.

Output files in `artifacts/plan_032_dif_cleaned_mmlu/`:
- `plan_032_random_baseline.py` — the script
- `random_baseline_summary.csv` — per-trial metrics (20 rows)
- `dif_vs_random_comparison.csv` — DIF vs random with z-scores
- `random_baseline_report.md` — standalone report section
- Section also appended to `plan_032_report.md`

---
