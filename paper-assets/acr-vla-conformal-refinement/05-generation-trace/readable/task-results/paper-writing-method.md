# paper writing method

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_writing_method_20260518T093817_result.json`
- **Structured JSON:** [`81574d8ba48bba8a4e3e.json`](../../sessions/81/81574d8ba48bba8a4e3e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Method section rewritten and verified. Key changes from the old version:

1. **Selection: L2 distance to mean** replaces Mahalanobis nonconformity scoring. Removed all shrinkage covariance estimation from selection (eq:shrinkage, eq:mahal deleted).
2. **CRM input corrected**: z_obs is 960D (not 990D), concatenated with a_base (30D) for total 990D input. CRM receives the selected action, not just the observation.
3. **Parameter count**: 327,198 (~327K), not 330K.
4. **Primary ε = 0.2**, not 0.1.
5. **CRM framed as correction module**, not selection/ranking. Explicit statement that CRM never sees individual candidates.
6. **obs_only clarified**: does not use any conformal features. Name "Conformal Residual Module" acknowledged as historical from perdof variant.
7. **Ledoit-Wolf and Braun/CGS citations** moved to perdof conditioning paragraph only.
8. **Conditioning variants** given correct input dimensions (990/1030/991) and param counts (327K/337K/327K).
9. All prohibited style patterns verified absent (no dashes, no -ing endings, no AI vocabulary).

---
