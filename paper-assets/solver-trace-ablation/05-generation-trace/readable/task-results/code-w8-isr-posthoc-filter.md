# code w8 isr posthoc filter

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_w8-isr-posthoc-filter_20260520T100131_result.json`
- **Structured JSON:** [`f62c87a32cc69e4edbb3.json`](../../sessions/f6/f62c87a32cc69e4edbb3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Report written to `artifacts/isr_posthoc_filter_analysis.md`.

Key findings:
- **CE (s42)**: ISR filter removes most CE at τ≥0.1 (mean ISR=0.107), but collateral damage to genuine proofs is heavy — 6/9 genuine lost at τ=0.3.
- **TS (s44)**: ISR filter is structurally blind — all 97 TS samples have ISR≥0.5 (Prover9 marks 1/2 components as necessary in P→P tautologies), so no threshold ≤0.5 filters any of them.
- **Bottom line**: Single ISR threshold cannot serve as a post-hoc quality gate. TS occupies the same ISR band as genuine proofs. Effective filtering requires mode-specific classifiers (structural tautology detection, conclusion-in-premises check) rather than a scalar threshold.

---
