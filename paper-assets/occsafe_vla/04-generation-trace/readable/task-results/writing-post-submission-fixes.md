# writing post submission fixes

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_writing_post-submission-fixes_20260528T150051_result.json`
- **Structured JSON:** [`fe1dce09337f175b49a9.json`](../../sessions/fe/fe1dce09337f175b49a9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Summary of changes:

**Task 1 (Factorial description):** Fixed "twelve conditions varying five factors" framing in abstract, introduction, method, and fig1 caption. Now accurately describes a 2×2 factorial core + single-factor ablations. Softened "cannot detect interactions" to "cannot decompose joint effects" to avoid contradiction with p=0.76 interaction result.

**Task 2 (Causal language):** Downgraded ~15 causal expressions ("reduces", "degrades", "harmful", "destabilizes", "detrimental", "damage") across all 6 tex files to associative language ("is associated with", "corresponds to", "deficit"). Added power analysis to limitations (estimated power ~0.35–0.45, ANOVA results should be interpreted as exploratory, n≥8 needed for confirmatory).

**Task 3 (Cohen's d → Hedges' g):** Replaced all Cohen's d values with Hedges' g across abstract, introduction, results, discussion, conclusion, limitations, and appendix. Correction factors: 0.800 (n₁+n₂=6), 0.842 (n₁+n₂=7), 0.870 (n₁+n₂=8). Updated pairwise table (10 entries), all inline effect sizes, table/figure captions, and methodology descriptions.

---
