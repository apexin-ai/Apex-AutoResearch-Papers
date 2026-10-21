# analysis cross domain and mitigation

**Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_cross_domain_and_mitigation_20260522T161021_result.json`
- **Structured JSON:** [`ef0027fe0da3b2d7de3a.json`](../../sessions/ef/ef0027fe0da3b2d7de3a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All four files produced:

**Part A: Cross-Domain**
- `analysis_cross_domain.json` — full statistics
- `analysis_cross_domain_summary.md` — narrative report

Key findings:
- C1 effect replicates in both domains (airline Δ=44pp, retail Δ=34pp, both p < 10⁻⁴⁹)
- But domain **significantly moderates** the effect (interaction p = 0.007) — airline amplifies the ambiguity effect
- Type ranking correlation ρ = 0.49, not significant — type ordering diverges across domains
- Conditional_precedence (+19pp, p=0.003) and lexical (+15pp, p=0.016) drive the domain difference

**Part B: 5-Model Mitigation**
- `analysis_mitigation_5model.json` — full statistics
- `analysis_mitigation_5model_summary.md` — narrative report

Key findings:
- Auth_scope has largest mean Δ (−18pp) but high cross-model variance; Claude shows no change (floor effect from safety training)
- Lexical and conditional_precedence are the most reliably mitigated (all 5 models improve, binomial p = 0.031)
- Incompleteness is least responsive (mean −3.3pp, CI crosses zero, DeepSeek worsens)
- Vulnerability-responsiveness correlation is not significant (r = −0.21, p = 0.30)
- DeepSeek-V3 is the only model with degradation cells (incompleteness +4pp, scopal +2pp)

---
