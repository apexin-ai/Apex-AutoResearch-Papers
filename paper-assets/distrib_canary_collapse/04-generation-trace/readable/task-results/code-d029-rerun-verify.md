# code d029 rerun verify

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d029_rerun_verify_20260515T095455_result.json`
- **Structured JSON:** [`9133d804f9be3f805f98.json`](../../sessions/91/9133d804f9be3f805f98.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

D029 verification complete. Summary:

- **Code fix confirmed**: `threshold_onset` reads `significant`, all other methods read `significant_fdr`
- **sig_count_seed changes**:
  - `permutation_granger`: 34 → **27** (-7)
  - `toda_yamamoto`: 26 → **24** (-2)
  - `threshold_onset`: 35 → 35 (unchanged, correct)
- **6 robust pairs unchanged**: token_entropy→distinct_{1,2,3}, ece→distinct_{1,2,3}
- **Consensus FPR = 0.0%**
- All 3 JSON files regenerated (17:55) and synced to local artifacts
- Verification report written to `artifacts/analysis/consensus_framework/d029_rerun_verification.md`

---
