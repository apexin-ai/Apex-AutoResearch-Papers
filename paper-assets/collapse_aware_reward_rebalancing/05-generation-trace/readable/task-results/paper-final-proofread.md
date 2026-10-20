# paper final proofread

**Does Reward Curation Kill Diversity? Systematic Evidence of Surprising Resilience in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_final_proofread_20260517T113547_result.json`
- **Structured JSON:** [`22f397066117e7ca0a48.json`](../../sessions/22/22f397066117e7ca0a48.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All edits verified. Here's the checklist summary:

---

### Proofread Checklist Summary

| # | Check | Findings | Status |
|---|-------|----------|--------|
| 1 | Grammar + spelling | 1 issue: Self-BLEU range "0.004–0.009" → "0.002–0.009" in results.tex (min Self-BLEU is 0.0024 for C2 Gen 1) | Fixed |
| 2 | Pronoun/demonstrative reference | 0 issues. All `this/that/it/these/those` have clear antecedents (e.g., "this stability", "this embedding-level stability", "this disconnect", "this correlation") | Clean |
| 3 | Em-dash / en-dash | 0 found in any root tex file | Clean |
| 4 | -ing trailing phrases | 7 fixed across 3 files: `related_work.tex` (1), `analysis.tex` (5 body + 1 caption). Rewrites used "which confirms/suggests", "and thereby reinforce", "and produces", split to new sentence | Fixed |
| 5 | Abbreviation definitions | 1 issue: "Full-FT" first used in introduction.tex without definition → added "full fine-tuning (Full-FT)". All others (LoRA, RLHF, NND, TTR, pp) properly defined at first use | Fixed |
| 6 | Abstract word count | 222 words (within 150–250) | OK |
| 7 | Number consistency | All Vendi Scores match registry for C1, C3→paper C5, C5→paper C6, C7, C8, C4→paper C3. All Δ% calculations verified correct. **Note**: C2 (paper) shows values 107.21/107.26/107.25 but registry says C2 has no metrics (failed/killed run); these may come from a rerun not reflected in the registry listing. C4 (paper, Full-FT 2e-5 curated) values not in registry listing but internally consistent | Verified |
| 8 | Transition words | 0 consecutive Furthermore/Moreover/Additionally found | Clean |

---
