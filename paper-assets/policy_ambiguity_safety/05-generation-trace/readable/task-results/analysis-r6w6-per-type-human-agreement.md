# analysis r6w6 per type human agreement

**Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_r6w6_per_type_human_agreement_20260521T150951_result.json`
- **Structured JSON:** [`6a98209602121decfed7.json`](../../sessions/6a/6a98209602121decfed7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

200/200 matched, output saved. Key findings:

- **Overall κ = 0.735** [0.616, 0.852], agreement 91%
- **Authorization scope κ = 0.644** — lower than the other-types mean (0.730), but **not the lowest**: coreferential (0.479) and scopal (0.636) are comparable or lower, though both have wide CIs
- The LLM systematically rates violations higher than humans (25% vs 18% violation rate), especially for authorization_scope (35% vs 21%) and coreferential (24% vs 9%)
- **Lexical** has the highest agreement (κ = 0.904); **conditional_precedence** is also strong (κ = 0.837)

Result file: `round6_supplementary/per_type_human_agreement.json`

---
