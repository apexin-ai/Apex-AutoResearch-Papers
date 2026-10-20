# paper round5 patch

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_round5_patch_20260516T195753_result.json`
- **Structured JSON:** [`eabafc577fadf8352b45.json`](../../sessions/ea/eabafc577fadf8352b45.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All changes complete. Summary of modifications:

**`appendix_discussion.tex`**:
- Expanded FT ablation table from 2 columns (DR, R-F1) to 7 columns (DR, RV, ET, CF, PF, E-F1, R-F1) with full data for all 8 rows
- Added F1 cost negligibility statement (max ΔR-F1 = -0.30pp)
- Added new `\paragraph{Residual DR Error Analysis}` with root cause taxonomy (39% entity type errors, 33% schema gaps, 17% relation errors, 11% direction reversal) and dataset-specific insights

**`main.tex`** (Limitations section):
- Added cross-reference `(Appendix~\ref{app:residual-dr-analysis})` to the error analysis

**`paper_tables_draft.tex`**:
- Replaced TBD → 10.21 / -8.3, removed RUNNING, updated caption

**Output**: `artifacts/_project/report/patch_summary_round5.md`

---
