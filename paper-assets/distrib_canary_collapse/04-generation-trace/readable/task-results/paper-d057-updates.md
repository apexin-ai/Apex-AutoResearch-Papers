# paper d057 updates

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_d057_updates_20260518T003621_result.json`
- **Structured JSON:** [`dcb4b7815da269420a2b.json`](../../sessions/dc/dcb4b7815da269420a2b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All modifications complete. Summary:

**Modification 1 (Method text)**: Replaced BH FDR statement in experiments.tex with new 4-sentence description: independent testing at p<0.05, permutation exact p-values, cross-method consensus K≥4/5 as multiplicity control. All other FDR/BH references across the paper (experiments.tex, method.tex, abstract.tex, discussion.tex, introduction.tex, appendix.tex) updated for consistency.

**Modification 2 (Table 7 headers)**: Caption updated from "BH-corrected FDR significance" to "significance (permutation p<0.05)".

**Modification 3 (Table 7 data)**:
- OPT-1.3B: Naive=8, Diff=8, Thresh=8, PG_fwd=6, PG_rev=0, TY=6, K≥4=6
- C4 s42: Naive=8, Diff=8, Thresh=6, PG_fwd=8, PG_rev=3, TY=4, K≥4=7
- Scale row verified correct (unchanged)
- Footnote updated to explain the single non-consensus pair

**Modification 4 (C4 ECE)**: Replaced 8-sentence bidirectionality paragraph with 4-sentence version noting s42 reverse significance (3/8) did not replicate in s43 (0/8), indicating seed-specific noise.

**Modification 5 (Scale)**: Verified existing text already matches D057 values (K≥4=5/8, Thresh=8/8, TY=0/8).

Verification: 0 em-dashes, 0 LaTeX errors, only 2 appropriate FDR mentions remain (our rationale text + intro's criticism of prior work).

---
