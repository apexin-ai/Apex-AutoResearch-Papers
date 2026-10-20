# experiment residual v2

**Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_residual_v2_20260522T232336_result.json`
- **Structured JSON:** [`a81f0e5665cd6bde79d7.json`](../../sessions/a8/a81f0e5665cd6bde79d7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Analysis complete. Key findings:

**Overall**: ICC(1) = 0.749 — 75% of variance is systematic (clause-driven), only 25% is stochastic (run-to-run noise). 86.5% of cells are unanimous across 5 reps.

**By condition**:
- **Ambiguous**: ICC = 0.78, violation rate 27.6%, stochastic share 21.8%
- **Unambiguous**: ICC = 0.40, violation rate 4.0%, stochastic share 59.6% (floor effect — low base rate means most variance is noise)

**By ambiguity type** (ICC, violation rate):
- **Incompleteness**: 0.90, 22.5% — most deterministic
- **Conditional precedence**: 0.86, 21.9%
- **Scopal**: 0.73, 23.9%
- **Lexical**: 0.70, 17.5%
- **Coreferential**: 0.34, 8.8% — noisier
- **Authorization scope**: −0.01, 1.1% — near-zero violations, essentially floor

**Residual decomposition**: Of the original 60.8% residual variance, ~15.2pp is genuine stochasticity and ~45.6pp is systematic-but-unmeasured factors (likely prompt phrasing, scenario details, model-specific sensitivities).

---
