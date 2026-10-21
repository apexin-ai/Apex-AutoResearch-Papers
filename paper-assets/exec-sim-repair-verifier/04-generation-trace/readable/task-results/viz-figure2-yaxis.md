# viz figure2 yaxis

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_viz_figure2-yaxis_20260522T170212_result.json`
- **Structured JSON:** [`973fc40a141bf8b50b58.json`](../../sessions/97/973fc40a141bf8b50b58.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Done. Summary:

**Figure 2 — fixed:**
- Regenerated `fig2_scaling_gap.pdf` with y-axis starting at 0% (was 55%)
- Removed "Note: $y$-axis begins at 55%" from caption in `main.tex` line 57
- Script `plot_figure2_v2.py` already had the correct `set_ylim(0, 105)` — just needed regeneration and file copy
- Artifact registered: `art_20260522_43ba07`

**Figure 3 — no change needed:**
- Script: `artifacts/fig3_oracle_stratified.py`, y-axis range `(-5, 50)`
- This is an advantage plot in percentage points (not accuracy %), with near-zero/negative values at T=1. Starting at -5 is appropriate for this data type
- Caption in `appendix.tex` line 34 already discloses "y-axis does not start at zero"
- Unlike Figure 2's 55% truncation on accuracy, this is not visually misleading — the reviewer concern was specific to the accuracy scale

---
