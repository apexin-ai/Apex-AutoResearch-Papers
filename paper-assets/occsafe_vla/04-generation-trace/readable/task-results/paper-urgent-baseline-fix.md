# paper urgent baseline fix

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_urgent-baseline-fix_20260527T024502_result.json`
- **Structured JSON:** [`ce9862221b9e9900c89d.json`](../../sessions/ce/ce9862221b9e9900c89d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Not a git repository — can't produce a diff. The edits are complete and verified via grep.

**Summary of all changes made across 6 files:**

| File | Changes |
|------|---------|
| **main.tex** | Abstract: removed "at most 1 of 12", binomial test claim ("11/12 ≤ Vanilla; p≈0.003"), and "directional consistency" sentence. Central finding rewritten to: gradient flow ON degrades CAR, gradient OFF recovers baseline. |
| **introduction.tex** | L3/L10: 78.0% → 74.5%. L16: removed binomial claim and "at most 1 of 12" language. L20 (C1): "does not improve under any of 12" → "with gradient flow degrades…while detach recovers baseline". |
| **method.tex** | Updated "LN cells and additional Vanilla seeds are in progress" → "LN cells remain at n=1" (Vanilla now has 3 seeds). |
| **results.tex** | Baseline updated v2: 0.768 → 0.745±0.024 (3 seeds). Table 1 Vanilla row: 1 seed → 3 seeds, 0.768 → 0.745±0.024. ΔCARs recalculated: Detach OCC +2.2, Detach+LN +2.0, Full OCC+LN −0.5, Full OCC −2.0. Narrative updated (Detach variants now exceed baseline). Deleted η²=0.37 and d=1.41 parenthetical. Removed "all twelve conditions at or below Vanilla" / binomial sign-test passage. |
| **discussion.tex** | "all tested configurations perform at or below" → "gradient flow configurations degrade safety below". |
| **conclusion.tex** | Removed "all twelve configurations perform at or below the no-auxiliary-head baseline". Removed Δ=−4.2pp/−2.5pp values. Rewritten to: gradient flow degrades, detach recovers. |
| **appendix.tex** | L108: "Vanilla 0.768" → "Vanilla 0.745". L132: replaced binomial/"all twelve" claim with gradient flow consistency evidence. |

---
