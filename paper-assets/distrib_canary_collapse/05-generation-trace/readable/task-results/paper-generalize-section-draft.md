# paper generalize section draft

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_generalize_section_draft_20260517T104153_result.json`
- **Structured JSON:** [`17d9969a809fcda159e9.json`](../../sessions/17/17d9969a809fcda159e9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Draft written to `artifacts/generalization_draft.tex`. Contents:

**Tables:**
- `tab:generalization` — expanded 5-method panel with forward/reverse PermG split, rows for Pythia-1B/WikiText, OPT-1.3B/WikiText, Pythia-1B/C4, plus existing GPT-2m baseline
- `tab:generalization_drift` — metric drift profile for each condition, enabling cross-condition comparison

**VERSION A** (all conditions confirm): 5 paragraphs covering design rationale, scale/architecture/domain invariance, and cross-condition consistency. Framing: "general property of autoregressive collapse."

**VERSION B** (partial results): 4 paragraphs with the same design intro but pivoting to boundary-condition framing. Turns partial failure into a positive narrative ("the framework correctly identifies weaker signals as sub-threshold").

**Decision rule** in end-of-file notes: VERSION A if all conditions show PermG fwd >= 4/8 + rev <= 1/8 + consensus >= 4/8; VERSION B otherwise.

All placeholders are `\textbf{XX}` or `\textbf{[TBD]}`. Zero em-dashes, zero -ing phrase endings. Ready to fill once Phase 2 experiments complete.

---
