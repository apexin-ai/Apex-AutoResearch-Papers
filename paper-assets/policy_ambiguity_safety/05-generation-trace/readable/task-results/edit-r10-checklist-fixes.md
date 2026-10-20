# edit r10 checklist fixes

**Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_edit_r10_checklist_fixes_20260521T210253_result.json`
- **Structured JSON:** [`abb55ac32db6a6e8260e.json`](../../sessions/ab/abb55ac32db6a6e8260e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 6 edits complete. Summary:

| # | Location | Old | New |
|---|----------|-----|-----|
| 1 | D2 | `Per-type κ ranges from 0.479 (conditional_precedence) to 0.904 (incompleteness)` | `Per-type κ ranges from 0.479 (coreferential) to 0.904 (lexical)` |
| 2 | E2 | `Δ_perturb = 3.33pp` | `Δ_perturb = −0.67pp (n=300)` |
| 3a | A2 | `§Ethical Considerations notes that the study` | `As discussed in §Limitations and in this checklist response, the study` |
| 3b | B2 | `§Ethical Considerations discusses: (1)` | `As discussed in §Limitations and in this checklist response: (1)` |
| 4 | A1 | `(4) temperature=0 deterministic setting does not reflect stochastic deployment conditions; (5) API-accessed models are opaque — we cannot attribute behavioral differences to specific architectural choices vs. safety training differences.` | Same text with `(discussed in §Method)` appended to each point |
| 5 | D3 | `Annotators were trained on 20 pilot episodes with discussion of disagreements` | `Pilot testing was conducted to calibrate the annotation schema, with discussion of disagreements` |
| 6 | C1 | `Qwen3-235B-A22B (open-weight MoE, 235B total / 22B active)` | `Qwen3-235B (open-weight MoE, 235B total)` |

**Note on #3**: B3 does not contain a `§Ethical Considerations` reference — only A2 and B2 had one (2 occurrences, not 3). B3's text already stands without a section reference.

---
