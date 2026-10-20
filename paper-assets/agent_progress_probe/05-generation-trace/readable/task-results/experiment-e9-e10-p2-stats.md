# experiment e9 e10 p2 stats

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_e9-e10-p2-stats_20260515T142705_result.json`
- **Structured JSON:** [`e982da48201da3d9013c.json`](../../sessions/e9/e982da48201da3d9013c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## E9: Multi-seed Statistical Tests

| Comparison | Δ | t | p | Cohen's d | Sig |
|---|---|---|---|---|---|
| Struct GB vs GRU Probe (in-domain) | +0.077 | 11.71 | 0.007 | 6.76 | ** |
| E5-large vs GRU Probe | +0.020 | 3.53 | 0.072 | 2.04 | ns |
| BGE-M3 vs GRU Probe | −0.010 | −0.29 | 0.801 | −0.17 | ns |
| E5-large vs BGE-M3 | +0.030 | 0.94 | 0.446 | 0.54 | ns |
| Cross-agent GB vs Probe zero-shot | +0.368 | 268.4 | <0.001 | 120.0 | *** |

**Gold set bootstrap (N=491):** GB vs MV (+4.2pp, p<0.001), GB vs Probe (+8.8pp, p<0.001), RF vs GB (−2.9pp, p<0.001), TWV-Probe vs GB (−2.3pp, p=0.056 ns).

**Key findings:**
- Structural GB significantly outperforms GRU Probe in-domain (p=0.007, d=6.76), but permutation test is non-significant (p=0.25) due to n=3 — low power caveat
- Encoder choice (E5/BGE-M3 vs nomic) shows no significant difference with n=3 seeds
- Cross-agent: GB (0.966) trivially dominates Probe zero-shot (0.598)
- GB cross-agent extremely stable: CV=0.32%, 5-seed std=0.003

## E10: Conf=1 Subset Evaluation

| Subset | Model | Macro-F1 | F1(stag) | F1(prog) | N |
|---|---|---|---|---|---|
| conf≥2 test | GB | 0.997 ± 0.001 | 0.996 ± 0.001 | 0.998 ± 0.001 | 3,081 |
| conf≥2 test | RF | 0.997 ± 0.001 | 0.996 ± 0.001 | 0.998 ± 0.001 | 3,081 |
| **conf=1** | **GB** | **0.846 ± 0.001** | **0.774 ± 0.001** | **0.917 ± 0.001** | **39,408** |
| **conf=1** | **RF** | **0.862 ± 0.003** | **0.801 ± 0.004** | **0.924 ± 0.002** | **39,408** |

**Key findings:**
- conf=1 performance drops ~15pp vs conf≥2 (GB: 0.997→0.846, RF: 0.997→0.862), p<0.001
- RF slightly but significantly beats GB on conf=1 (Δ=+1.7pp, p=0.011)
- conf=1 stag rate = 24.8% (vs 38.0% for conf≥2) — more class imbalance
- GB-RF agreement on conf=1: 97.6–98.3% — both models largely agree even on ambiguous cases
- Both models agree with silver MV labels ~88–89% of the time on conf=1

---
