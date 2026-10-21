# paper integrate review data

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_integrate_review_data_20260515T031735_result.json`
- **Structured JSON:** [`001308dd28bf49813805.json`](../../sessions/00/001308dd28bf49813805.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Good — the file ends cleanly. Let me now do the verification checklist.

**Data verification** (all numbers traced to task data):

Data 1 (Bootstrap CI):
- Individual ρ values (+0.379, +0.360, +0.295, +0.267, +0.205) match existing Table 1 and task data
- CIs ([+0.299,+0.456], [+0.277,+0.437], [+0.212,+0.371], [+0.176,+0.354], [+0.119,+0.291]) match task data rounded to 3dp
- Pairwise Δρ (+0.155, +0.019, -0.065) and CIs match task data rounded to 3dp
- Significance flags (Yes, No, Yes†) match task data

Data 2 (Selection F1):
- All 4 configs × 7 columns verified against task data (3dp rounding, round-half-up)

Data 3 (WNUT-17):
- All 5 signals × 5 columns verified; p-values rounded appropriately
- Logprob negative ρ (-0.410) mentioned in experiments.tex line 79

**Cross-reference verification**:
- `\ref{tab:bootstrap_signal_ci}` → `\label{tab:bootstrap_signal_ci}` (appendix line 202)
- `\ref{app:bootstrap_signal}` → `\label{app:bootstrap_signal}` (appendix line 191)
- `\ref{tab:wnut}` → `\label{tab:wnut}` (appendix line 147, pre-existing)
- `\ref{tab:cross_selection}` → `\label{tab:cross_selection}` (appendix line 170, label preserved)

**Consistency check**:
- "all six tested configurations" (experiments.tex line 130) = 4 in extended table + 2 in Table 2 (Qwen SciERC NER/RE)
- WNUT conditional ρ ≤ 0.35 bound (experiments.tex line 80) still holds with logprob conditional ρ = 0.350
- No existing correct data was modified

Summary of changes:
- **experiments.tex**: Added bootstrap CI appendix reference (line 66), added logprob negative ρ on WNUT-17 (line 79)
- **appendix.tex**: Updated WNUT table with full p-values and correct n=689 (lines 143-159), replaced compact cross-selection table with detailed per-signal F1 table* (lines 161-181), added new Bootstrap CI section with individual CIs and pairwise Δρ table (lines 191-229)

---
