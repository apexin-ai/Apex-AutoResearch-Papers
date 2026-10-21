# code r15 boundary analysis

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_r15-boundary-analysis_20260520T050800_result.json`
- **Structured JSON:** [`a4731c8cc6e71f443b5f.json`](../../sessions/a4/a4731c8cc6e71f443b5f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Output written and verified at `/root/autodl-tmp/outputs/classifier_validation/boundary_analysis.json`.

**Results: 20/20 correct classifications at decision boundaries.**

Key findings:
- **CE (10/10)**: Even the shortest conclusion (`T(a)`, 4 chars) is unambiguously hacking — the conclusion appears as a standalone premise with no NL source. Several cases (folio_592, folio_833) show the model embedding conclusions that contradict the NL premises.
- **Genuine (5/5)**: All 5 lowest-ISR samples (ISR=0.22) use an identical degenerate template from a mode-collapsed model (d129_1.7b_random_b01_s43). The template's conclusion `∀x(P(x)→¬Q(x))` always differs from premise `∀x(P(x)→Q(x))` by one negation, so CE never triggers. Classifier correctly separates poor quality (low ISR) from structural hacking.
- **TS (5/5)**: 3 of 5 supplementary TS cases generate tautological proofs for statements whose correct answer is "false" — TS confirms any queried statement regardless of truth value. Diverse predicate patterns (named, abbreviated, multi-arg, compound entity) all detected correctly.

---
