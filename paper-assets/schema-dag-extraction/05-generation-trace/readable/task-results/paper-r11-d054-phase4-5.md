# paper r11 d054 phase4 5

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_r11-d054-phase4-5_20260517T100338_result.json`
- **Structured JSON:** [`a6e45ca8a5fd5b4aca81.json`](../../sessions/a6/a6e45ca8a5fd5b4aca81.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Both compile cleanly. Summary of all changes:

**Phase 4a+4b**: results.tex line 87 — expanded "TOST" to "Two One-Sided Tests (TOST)" with `\citep{lakens-2017-equivalence}`, rewrote to specify ±3pp as primary margin with ±2pp sensitivity analysis pointer.

**Phase 4c**: main.tex appendix §prompt_variants — added Bonferroni/directional-consistency sentence citing `rothman-1990` (already in bib). Rothman-1990 verified real.

**Phase 5a**: experimental_setup.tex — "eliminates model-level randomness" → "substantially reduces model-level randomness (residual SD = 0.88 pp...)". Also updated main.tex variance decomposition section for consistency ("deterministic" → "nearly deterministic").

**Phase 5b**: supplementary.tex — replaced 449-line duplicate appendix with 1-page declaration pointing to main paper appendix.

**Phase 5c**: Added `levy-2024-same-task` (ACL 2024, verified) and `dror-2018-significance` (ACL 2018, verified) to references.bib. Cited Levy in discussion.tex (prompt length), Dror in Limitations multiple-comparisons paragraph. GenRES/ULTRA not found as specific relevant 2025 papers; skipped.

**Phase 5d**: Causal language scan found 2 instances of "causes" in related_work.tex and sdgd_negative.tex — replaced with "is associated with ... collapsing". Title "Shape" left as deliberate framing. All other matches are allowed exceptions (schema-driven, Causal mechanism, U-shaped).

---
