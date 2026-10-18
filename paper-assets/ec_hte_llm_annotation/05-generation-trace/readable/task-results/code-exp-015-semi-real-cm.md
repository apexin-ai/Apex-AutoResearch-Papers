# code exp 015 semi real cm

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp-015-semi-real-cm_20260521T125022_result.json`
- **Structured JSON:** [`bf2604c673ea76fe35d4.json`](../../sessions/bf/bf2604c673ea76fe35d4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 3 output files generated. Here's the summary:

**exp-015 completed** (278s, 100 MC seeds × 3 n_expert configs = 300 runs).

### Key findings

The results show an interesting pattern under **realistic asymmetric CMs**:

| n_expert | Method | Avg RMSE | Avg Coverage |
|----------|--------|----------|-------------|
| 100 | naive | 0.1230 | 0.879 |
| 100 | global_corrected | 0.2631 | 0.885 |
| 100 | hb_ec_hte | 0.7842 | 0.744 |
| 250 | global_corrected | 0.2318 | 0.909 |
| 250 | hb_ec_hte | 0.4113 | 0.834 |
| 500 | global_corrected | 0.1963 | 0.922 |
| 500 | hb_ec_hte | 0.2599 | 0.890 |

Under these **highly asymmetric real CMs** (e.g., S0 has FPR=0.054 but FNR=0.526), the HB EC-HTE estimator struggles — especially at small n_expert. The strong asymmetry (FNR >> FPR) combined with low P(Z=1)=0.18 means very few Z=1 expert labels are available per subgroup, making the Gibbs sampler's per-subgroup CM estimates noisy. Global correction outperforms HB at all sample sizes. As n_expert grows to 500, HB improves substantially but still doesn't beat global correction on average.

**Output files:**
- `results/exp015_semi_real_raw.csv` (9,600 rows)
- `results/exp015_semi_real_summary.csv` (96 rows)
- `results/exp015_semi_real_analysis.md`

---
