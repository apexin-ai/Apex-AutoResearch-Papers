# paper p0 patch drafts

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_p0-patch-drafts_20260514T190526_result.json`
- **Structured JSON:** [`05c57a13b6fad5fdcce6.json`](../../sessions/05/05c57a13b6fad5fdcce6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Patch document written to `artifacts/p0_patch_drafts.md`. Summary:

**12 locations identified** across 4 files (introduction.tex, analysis.tex, conclusion.tex, abstract.tex).

**Plan A** ({CONC} >= 0.50): 4 locations change (value swap only). Sub-case A2 (0.50-0.55) adds "effective" qualifier and L0 dominance emphasis since the gap to Yi-1.5's 0.49 narrows.

**Plan B** ({CONC} < 0.50): Concentration alone can't separate Qwen from the FAIL models (Mistral 0.42, Yi-1.5 0.49). Two viable options:
- **B1 (Dual Indicator)**: Add L0 dominance ratio as second criterion. Qwen (26×) vs Yi-1.5 (0.07×) separates cleanly. Preserves 5/5 classification claim → stronger for reviewers. Requires exact L0 dominance for Llama (currently only "较高").
- **B2 (Continuous Framing)**: Drop threshold, frame as qualitative three-factor guidance (concentration + shape + magnitude). Safest but weakens Contribution 3.

**Recommendation**: B1 if {CONC} is in [0.40, 0.50), B2 as fallback if L0 data is shaky.

---
