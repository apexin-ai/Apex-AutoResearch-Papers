# code 14b paper text update

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_14b-paper-text-update_20260523T080501_result.json`
- **Structured JSON:** [`c78830600ba49e0511f0.json`](../../sessions/c7/c78830600ba49e0511f0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Both appendix references are about oracle analysis (single-seed estimate) and 4B comparisons (single seed) — not about 14B. No changes needed there.

All edits are complete. Summary of changes:

- **abstract.tex**: `[TOST_P]` → `0.0006`
- **experiments.tex Table 2**: CLS 14B std `0.80` → `0.81`, CWM 14B std `0.67` → `0.65`
- **experiments.tex text (line 97)**: Same std updates + `[TOST_P]` → `0.0006`
- **conclusion.tex**: `[TOST_P]` → `0.0006`

The other items in the checklist (seed descriptions, footnote removal, figure caption, limitations wording) were already updated in prior commits — no stale 14B single-seed/exploratory language remains in any `.tex` source file.

---
