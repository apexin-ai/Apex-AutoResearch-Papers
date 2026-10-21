# exp-033 Analysis: Mistral-7B-Instruct-v0.3 SICA vs SC on FOLIO-204

## Experiment Config
- **Model**: Mistral-7B-Instruct-v0.3 (vLLM)
- **Dataset**: FOLIO-204 (full validation set)
- **K**: 12, **T**: 0.7, **seed**: 42
- **Server**: westd-25068
- **Wall time**: 4744.9s (~79 min)
- **Status**: incomplete (198/204 problems, 97.1% coverage), process terminated mid-execution (no completion marker in log, log ends at HTTP requests). Summary section in JSON is stale snapshot from n=188; actual results array contains 198 entries.

## Key Metrics (n=198)

| Metric | Value |
|--------|-------|
| **SICA accuracy** | 59.09% (117/198) |
| **SC accuracy** | 54.04% (107/198) |
| **Delta (SICA - SC)** | **+5.05pp** |
| Extraction rate | 97.10% |
| C0 (zero-constraint problems) | 1/198 (0.5%) |
| Contradiction rate | 3.52% |
| Problems with contradictions | 124/198 (62.6%) |
| Same answer (SICA = SC) | 181/198 (91.4%) |

## Statistical Significance

**McNemar's test (discordant pairs):**

| | SC correct | SC wrong |
|---|---|---|
| **SICA correct** | 105 | 12 |
| **SICA wrong** | 2 | 79 |

- Discordant pairs: sica_only=12, sc_only=2 (total=14)
- Chi-squared (uncorrected): (12-2)^2 / 14 = **7.14**, p = 0.0075
- Chi-squared (Yates corrected): (|12-2|-1)^2 / 14 = **5.79**, p ~ 0.016
- Exact binomial test (two-sided): P(X >= 12 | n=14, p=0.5) * 2 = **0.013**
- **Conclusion: statistically significant at p < 0.05 (all three tests)**

## Comparison with Prior Experiments

| Experiment | Model | Dataset | n | SC acc | SICA acc | Delta | Significant? |
|---|---|---|---|---|---|---|---|
| exp-001 | Qwen2.5-14B-Instruct | FOLIO-204 | 204 | 74.51% | 74.75% | +0.25pp | No |
| exp-010 (pilot) | Mistral-7B-Instruct-v0.3 | FOLIO-60 | 60 | ~53% | ~53% | 0pp | No |
| **exp-033** | **Mistral-7B-Instruct-v0.3** | **FOLIO-204** | **198** | **54.04%** | **59.09%** | **+5.05pp** | **Yes (p=0.013)** |

## Hypothesis Evaluation

**Original hypothesis**: Capability trap persists across model families. Mistral-7B should show delta ~ 0, confirming that weak models extract low-quality constraints that fail to improve over SC.

**Actual result**: SICA significantly outperforms SC by +5.05pp (p=0.013). This **contradicts** the capability trap hypothesis as stated.

## Interpretation

1. **SICA helps more on weak models**: Mistral-7B SC accuracy is low (54%) compared to Qwen2.5-14B (74.5%). When SC has low agreement/confidence, SICA's constraint-weighted voting provides additional discriminative signal that shifts answers in the right direction.

2. **Discordant pair asymmetry is strong**: 12 problems corrected by SICA vs only 2 lost. SICA is not randomly perturbing answers; it systematically improves on SC errors.

3. **Pilot inconsistency**: The pilot exp-010 (n=60) showed delta=0, but the full dataset shows +5.05pp. The pilot sample was likely unrepresentative, or the effect requires larger n to surface.

4. **Capability trap needs refinement**: The raw capability trap hypothesis ("weak model = bad constraints = no improvement") is too simplistic. The data suggests a more nuanced picture where SICA's benefit depends on the gap between SC agreement level and ground truth, not just constraint quality in isolation.

## Result Classification

**NEGATIVE for capability trap hypothesis / POSITIVE for SICA method**

The cross-family capability trap is NOT confirmed. SICA shows statistically significant improvement over SC on Mistral-7B, the weakest model tested so far. This complicates the paper narrative but strengthens the method's empirical case.

## Caveats
- 6/204 problems missing (3% incomplete). Unlikely to change significance.
- Summary fields in exp033_results.json are stale (from n=188 checkpoint). The per-problem results array (n=198) is authoritative.
- 12 JSON parse warnings in log, all handled gracefully.
- No errors or tracebacks in log.

## Raw Summary (from JSON, stale at n=188)
```json
{
  "n_problems": 188,
  "sica_accuracy": 0.6011,
  "sc_accuracy": 0.5479,
  "extraction_rate": 0.9699,
  "contradiction_rate": 0.0342,
  "k": 12,
  "mode": "vllm",
  "total_wall_time_s": 4519.4
}
```
Note: actual n=198 from results array; summary was not updated before process terminated.
