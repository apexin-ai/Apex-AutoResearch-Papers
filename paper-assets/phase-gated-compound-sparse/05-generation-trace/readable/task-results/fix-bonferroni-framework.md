# fix bonferroni framework

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_bonferroni_framework_20260515T082745_result.json`
- **Structured JSON:** [`84b7a4e9f29f748cb428.json`](../../sessions/84/84b7a4e9f29f748cb428.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

D066 complete. Final checklist:

- [x] `n500_unified_final.csv` has 16 rows (incl. DS s030)
- [x] New columns: `bonf_p_k48`, `bonf_p_k4`, `fdr_p_bh`, `significance_raw`, `significance`
- [x] DS rand s025 bonf_p_k4=0.0058 (**), s030 bonf_p_k4=0.0059 (**) — significance restored
- [x] `n500_unified_final.json` synced with new fields, old `bonferroni_p` removed
- [x] `n500_full_statistics.md` regenerated with family-wise Bonferroni + FDR columns
- [x] Registry `c2_n500_deepseek` metrics updated (rand_s025/s030 bonf_p → k=4 values, note "D066 revision")
- [x] Registry `c2_qw_n500_r3` metrics updated (consistent with k=4 scheme)
- [x] Artifact registered: `art_20260515_008bca`

Correction scheme applied: family-wise Bonferroni (per-condition k=4, within-dz k=6, imp-vs-rand k=4, cross-model k=8) + BH-FDR global across 48 tests. Paper Agent blocker resolved.

---
