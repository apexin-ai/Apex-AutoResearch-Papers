# paper c6 nve critical fixes

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_c6-nve-critical-fixes_20260518T114916_result.json`
- **Structured JSON:** [`ecce7d385afc74aebb48.json`](../../sessions/ec/ecce7d385afc74aebb48.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All edits complete. Summary of changes:

**Fix 1 (NVE value conflicts)**: The old incorrect values (0.53×, 5.00×, 0.61×) were not present in any current paper files. No changes needed.

**Fix 2 (Complete results table)**: 
- Added 008e\_v3 s3 (eval 92.7, NVE 4.02×, CIVO collapse) and s4 (eval 899.3, NVE 0.99×, Healthy) to `appendix.tex` complete\_results table
- Updated "24 configurations" to "26 configurations"
- Verified s1 NVE = 0.94× (already correct)

**Fix 3 (NVE sensitivity tables)**:
- Added s3 and s4 to `tab:nve_raw` (sorted by descending NVE)
- Recalculated both B1 and B2 sensitivity tables for n=10 with exact Clopper-Pearson CIs
- B2: AUROC 0.933 → 0.958, accuracy 87.5% (7/8) → 90.0% (9/10), F1 85.7% → 88.9%
- B1: n\_pos 2 → 3, CI [63.1, 100] → [69.2, 100]
- Updated summary table (`nve_sensitivity_table.tex`)
- Updated all references in `method.md`, `experimental_setup.md`, and `limitations.md`

---
