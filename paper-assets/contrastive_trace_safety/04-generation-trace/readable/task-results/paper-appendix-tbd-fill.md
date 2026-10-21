# paper appendix tbd fill

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_appendix_tbd_fill_20260517T015959_result.json`
- **Structured JSON:** [`7dc04ac5dcc4d75e4f59.json`](../../sessions/7d/7dc04ac5dcc4d75e4f59.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

No paper directory on the server. The local `docs/paper/sections/appendix.tex` is the authoritative copy.

**Summary of changes made to `docs/paper/sections/appendix.tex`:**

1. **Window Ablation Table (lines 31-70):** Replaced the condensed endpoint-only table with a full 7×3 table containing all real exp_007 data for R1-8B, R1-32B, and QwQ-32B. All values converted from raw proportions to percentages matching the established format (1dp for acc/precision/coverage, 2dp for FPR).

2. **Narrative paragraphs (lines 72-80):** Updated to accurately reflect the real data patterns:
   - R1-8B: "general upward trend" (not "monotonic") with noted dip at W=5
   - R1-32B: peaks at W=10 (73.7%), declines after (correct)
   - QwQ-32B: "broadly increasing with local non-monotonicity" (peaks at W=5, dips, recovers at W=25)
   - Added W=15 selection justification: "good balance of accuracy and FPR reduction while maintaining reasonable coverage across models"

3. **QwQ selectivity:** Already corrected to 15.3pp (layer 2) by a prior edit - no [TBD] remained there.

4. **No remaining [TBD] markers** in the file (confirmed via grep).

---
