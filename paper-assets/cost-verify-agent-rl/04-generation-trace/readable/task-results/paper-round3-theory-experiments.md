# paper round3 theory experiments

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_round3_theory_experiments_20260523T164735_result.json`
- **Structured JSON:** [`916b903ee86630a82dd8.json`](../../sessions/91/916b903ee86630a82dd8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All changes verified. Summary of edits:

**theoretical_analysis.tex:**
- Proposition 2: `=` → `\leq`, added "upper bounded by"
- Added tightness explanation after derivation
- "only 19.1%" → "upper bound of 19.1%" / "at most 19.1%" (4 locations)
- "Severity" paragraph: added `\leq` and "at most"
- Eq.6 caveat: added single-snapshot disclaimer after 1.32

**experiments.tex:**
- Section 4.1: "binary: R ∈ {0, r+}" → ternary reward with full description bridging theory/experiment
- Section 4.2: Cell C analysis sentence about non-additive M1-M2 interaction
- Table 1 caption: seed counts per cell + Table 2 cross-reference
- Section 4.4: complete rewrite distinguishing (1) sign-episode correlation, (2) credit agreement rate, (3) P(correct|update)
- Figure caption updated to match new terminology
- GitHub URL → "Code available upon acceptance"

**method.tex:**
- Added parenthetical noting penalty variant in experiments

---
