# exp plan002 full study api v2

**Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_plan002_full_study_api_v2_20260520T144938_result.json`
- **Structured JSON:** [`f8d087b56607b8d99d0b.json`](../../sessions/f8/f8d087b56607b8d99d0b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data collected. Here's the complete results summary:

---

## Full Study Results (plan_002, Run 2)

**Data**: 1,200 episodes (600 per model), 1,200 judgments, **0 errors**

### 1. Binary Effect (C1): Ambiguous vs Unambiguous

| | Ambiguous | Unambiguous | Difference | p |
|---|---|---|---|---|
| **Global** | 40.8% | 4.3% | **+36.5pp** | <0.0001 |
| gpt-5.4 | 41.0% | 2.7% | +38.3pp | <0.0001 |
| gpt-4.1 | 40.7% | 6.0% | +34.7pp | <0.0001 |

### 2. McNemar Matched-Pair

- **Method**: chi-square (continuity corrected)
- **Statistic**: 207.53, **p < 0.0001**
- **Odds Ratio**: 44.8 (95% CI: [18.47, 108.69])
- Discordant pairs: 229/600 (b=224 amb-only, c=5 una-only)
- Mantel-Haenszel OR (stratified by type): 443.0

### 3. Per-Type Violation Rates

| Type | Ambiguous | Unambiguous | D | Fisher p |
|---|---|---|---|---|
| authorization_scope | 55.0% | 2.0% | +53.0pp | <0.0001 |
| incompleteness | 52.0% | 3.0% | +49.0pp | <0.0001 |
| scopal | 40.0% | 4.0% | +36.0pp | <0.0001 |
| conditional_precedence | 35.0% | 0.0% | +35.0pp | <0.0001 |
| lexical | 38.0% | 8.0% | +30.0pp | <0.0001 |
| coreferential | 25.0% | 9.0% | +16.0pp | 0.0042 |

### 4. Type Effect (C2)

- **Omnibus chi-square**: 25.61, **p = 0.0001**, dof=5
- **Cramer's V**: 0.207 (small-medium effect)

### 5. TOST Equivalence

- **±15pp**: 3/15 pairs equivalent (auth_scope~incompleteness, cond_prec~lexical, lexical~scopal)
- **±10pp**: 0/15 pairs equivalent
- Types are **not** uniformly equivalent — significant heterogeneity exists

### 6. Bootstrap CIs (BCa, 10K resamples)

- **Global amb vs unamb**: D = 0.365, 95% CI [0.320, 0.405]
- Per-type CIs all exclude 0 (all significant)
- **Model pair** gpt-4.1 vs gpt-5.4: D = 0.015, CI [-0.032, 0.062] (includes 0, no difference)

### 7. Model Effect

- gpt-4.1: 23.3% overall, gpt-5.4: 21.8%
- **chi-square p = 0.581**, Cramer's V = 0.016 — **no significant model difference**
- Ambiguous-only: p = 1.000

### 8. Power Analysis

- **C2 design MDE** (N=1200, 6 types): Cramer's V = 0.103
- **Observed V**: 0.207 — well above MDE
- **Power at observed**: 98.7% — **well-powered**
- Underpowered warning: False

### 9. Information Delta (per-type token diff, unamb − amb)

| Type | Mean Δ tokens | Median |
|---|---|---|
| authorization_scope | +36.1 | 36 |
| incompleteness | +34.6 | 34 |
| lexical | +25.7 | 25.5 |
| scopal | +17.8 | 16 |
| conditional_precedence | +17.5 | 16 |
| coreferential | +7.8 | 8 |

**Logistic regression**: `condition_amb` coef = 2.77 (p < 0.001), `token_delta` coef = 0.019 (p = 0.070, marginal). Token length difference alone doesn't explain the effect — ambiguity condition is the dominant predictor (pseudo R² = 0.216).

### 10. Fleiss κ (Inter-Model Agreement)

- **κ = 0.496** (moderate agreement), SE = 0.060, z = 8.31, p < 0.001
- 300 clauses rated by 2 models
- Category proportions: violated 40.8%, not violated 59.2%

---
