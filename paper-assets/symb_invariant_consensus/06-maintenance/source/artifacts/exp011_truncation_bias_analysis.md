# exp-011 Truncation Bias Analysis

**Experiment:** exp-011-llama8b-v3 (LLaMA-3.1-8B-Instruct, D012, K=12)
**Date:** 2026-05-17

## 1. Clarification: "44 Truncated Traces"

The 44 refers to **individual traces** (out of 720 total = 60 problems x 12 traces), not problems. Actual counts:

| Metric | Count | Rate |
|--------|-------|------|
| Truncated individual traces | 44/720 | 6.1% |
| Problems with >= 1 truncated trace | 16/60 | 26.7% |

## 2. Discordant vs Concordant Truncation Rates

|  | Truncated | Not Truncated | Truncation Rate |
|--|-----------|---------------|-----------------|
| Discordant (all 6) | 1 | 5 | 16.7% |
| -- SICA wins (5) | 1 | 4 | 20.0% |
| -- SC wins (1) | 0 | 1 | 0.0% |
| Concordant (all 54) | 15 | 39 | 27.8% |
| -- Both correct (35) | 10 | 25 | 28.6% |
| -- Both wrong (19) | 5 | 14 | 26.3% |

Discordant pairs have **lower** truncation rate (16.7%) than concordant pairs (27.8%).

## 3. Fisher Exact Tests

**Test 1: Truncation x Discordant (all)**

|  | Truncated | Not Truncated |
|--|-----------|---------------|
| Discordant | 1 | 5 |
| Concordant | 15 | 39 |

- Odds ratio: 0.52
- **p = 1.000** (not significant)

**Test 2: Truncation x SICA-wins-discordant vs Concordant**

|  | Truncated | Not Truncated |
|--|-----------|---------------|
| SICA wins | 1 | 4 |
| Concordant | 15 | 39 |

- Odds ratio: 0.65
- **p = 1.000** (not significant)

## 4. Discordant Pairs Detail

### SICA wins (5 problems, SICA correct / SC wrong)

| Idx | Problem ID | Trunc | Trunc w/ answer | GT | SICA | SC | Dataset |
|-----|-----------|-------|-----------------|-----|------|-----|---------|
| 1 | ProofWriter_RelNoneg-OWA-D5-1036_Q11 | 0/12 | -- | True | True | Unknown | PW |
| 24 | ProofWriter_RelNeg-OWA-D5-856_Q19 | 3/12 | 0 (none extracted) | Unknown | Unknown | False | PW |
| 32 | folio_002 | 0/12 | -- | True | True | False | FOLIO |
| 44 | folio_014 | 0/12 | -- | False | False | Unknown | FOLIO |
| 57 | folio_027 | 0/12 | -- | Unknown | Unknown | True | FOLIO |

### SC wins (1 problem, SC correct / SICA wrong)

| Idx | Problem ID | Trunc | GT | SICA | SC | Dataset |
|-----|-----------|-------|----|------|----|---------|
| 19 | ProofWriter_RelNoneg-OWA-D5-709_Q12 | 0/12 | False | Unknown | False | PW |

**4 out of 5 SICA-wins discordant pairs have zero truncated traces.** The one exception (problem 24) had 3 truncated traces, but none produced extractable answers, so they contributed neither to SC voting nor to SICA answer selection.

## 5. Truncated Traces Influence

| Metric | Value |
|--------|-------|
| Truncated traces with extractable answer | 7/44 (15.9%) |
| Truncated traces without answer | 37/44 (84.1%) |
| Answer extraction rate (non-truncated) | 638/676 (94.4%) |

Of the 7 truncated traces that produced answers: 5 matched SICA's answer, 5 matched SC's answer (overlap because SICA and SC often agree). **No directional bias toward either method.**

## 6. Constraint Contribution

9 out of 16 truncation-affected problems had constraints extracted from truncated traces. However, **all 9 are concordant pairs** (both SICA and SC agree). The only discordant+truncated problem (idx 24) had 0 constraints from truncated traces.

## 7. Conclusion

**Truncation bias does NOT threaten the validity of exp-011 results.** Evidence:

1. Discordant pairs have lower truncation than concordant pairs (16.7% vs 27.8%, p=1.0)
2. 4/5 SICA-wins discordant pairs have zero truncation
3. The 1 discordant pair with truncation (problem 24) had no extractable answers from truncated traces
4. 84.1% of truncated traces produce no answer, making them effectively invisible to both SC and SICA
5. No directional bias in the few truncated answers that were extracted

The +6.67pp SICA advantage (66.7% vs 60.0%) is driven by problems without truncation artifacts. The signal is real, not a truncation artifact.

**No rerun with increased max-tokens is needed** to validate the exp-011 comparison, though increasing max-tokens would improve overall answer extraction rate (currently 89.6%) and could improve absolute accuracy for both methods.
