# experiment d134 cil

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_d134-cil_20260521T084126_result.json`
- **Structured JSON:** [`411416960116394e89b2.json`](../../sessions/41/411416960116394e89b2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

CIL computation complete. Summary of results:

**8 pairs computed, 2 pairs missing (LLaMA-8B and Qwen3-14B data on westd-16639).**

| Generator | Verifier | Dataset | CIL (bits) | Combo Gain w3 |
|---|---|---|---|---|
| Mistral-7B | DeBERTa-MNLI | PW-600 | **+1.67** | +6.67 pp |
| Mistral-7B | BART-MNLI | PW-600 | **+1.86** | +5.17 pp |
| Mistral-7B | RoBERTa-MNLI | PW-600 | **+1.42** | +4.17 pp |
| Qwen2.5-14B | DeBERTa-MNLI | PW-600 | **-0.08** | +0.83 pp |
| Mistral-7B | DeBERTa-MNLI | FOLIO-204 | **-0.47** | +4.41 pp |
| Mistral-7B | SICA | FOLIO-204 | **-2.93** | +4.90 pp |
| Qwen2.5-14B | SICA | PW-600 | **-3.53** | +0.50 pp |
| Mistral-7B | SICA | PW-600 | **-4.61** | -2.83 pp |

**Correlation: Spearman ρ = 0.762 (p = 0.028), Pearson r = 0.734 (p = 0.038)** — statistically significant.

Key findings:
- **Cross-architecture NLI verifiers have positive CIL (+1.4 to +1.9)** when paired with weak Mistral on PW-600 — when Mistral is wrong, DeBERTa is correct 75% of the time (vs only 24% when Mistral is right). This is the complementary signal that drives combo gain.
- **SICA has strongly negative CIL (-2.9 to -4.6)** — expected, since SICA is built from the same generator traces, so errors are highly correlated.
- **As generator gets stronger (Qwen2.5-14B), CIL drops to ~0** — DeBERTa's advantage over the generator vanishes, explaining why combo gain shrinks.
- The FOLIO-204 anomaly: negative CIL (-0.47) but positive combo gain (+4.41 pp) — likely a small-sample effect (n=93 wrong) or the weighted voting mechanism recovers differently than raw CIL predicts.

---
