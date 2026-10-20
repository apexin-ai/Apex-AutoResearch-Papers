# exp-046: Mistral-7B-Instruct-v0.3 on ProofWriter-600 (SICA vs SC)

## Experiment Config

| Parameter | Value |
|-----------|-------|
| Model | Mistral-7B-Instruct-v0.3 |
| Dataset | ProofWriter-600 (OWA-D5) |
| K (samples) | 12 |
| Temperature | 0.7 |
| Seed | 42 |
| Inference | vLLM |
| Wall time | 291.9 min (17511.2s) |

## Main Results

| Metric | Value |
|--------|-------|
| **SC accuracy** | **39.33%** (236/600) |
| **SICA accuracy** | **36.50%** (219/600) |
| **delta (SICA - SC)** | **-2.83pp** |
| McNemar chi2 | 6.7209 |
| McNemar p-value | 0.0095 |
| Extraction rate | 91.49% |
| Contradiction rate | 5.35% |
| Problems with contradictions | 482/600 (80.33%) |
| Total constraints extracted | 53,972 |
| Unique constraints | 27,335 |

## McNemar Contingency Table

|  | SC correct | SC wrong |
|--|-----------|----------|
| **SICA correct** | 206 | 13 |
| **SICA wrong** | 30 | 351 |

Discordant pairs: b=13, c=30. SC wins on 30 problems where SICA fails; SICA wins on only 13 where SC fails. The difference is statistically significant (p=0.0095).

## Per-Level Breakdown

| Level | SICA (%) | SC (%) | n |
|-------|----------|--------|---|
| OWA-D5 | 36.50 | 39.33 | 600 |

Note: All 600 problems are D5 (depth-5). No D0-D4 depth stratification available in this dataset split.

## Comparison with exp-033 (Mistral-7B on FOLIO-204)

| | exp-033 (FOLIO-204) | exp-046 (PW-600) | Difference |
|--|---------------------|-------------------|------------|
| SC accuracy | 54.41% | 39.33% | -15.08pp |
| SICA accuracy | 59.31% | 36.50% | -22.81pp |
| delta (SICA-SC) | **+4.90pp** | **-2.83pp** | direction flipped |
| McNemar p | (not recorded) | 0.0095 | |
| Contradiction rate | (not recorded) | 5.35% | |

## Key Observations

1. **SICA hurts on ProofWriter-D5.** Unlike FOLIO where SICA improved over SC by +4.90pp, on ProofWriter-D5 SICA is significantly worse (-2.83pp, p<0.01). The effect direction is flipped.

2. **Overall accuracy is low.** Both methods achieve under 40% on PW-D5, indicating Mistral-7B struggles heavily with depth-5 logical reasoning chains. The base model capability may be insufficient for constraint extraction to add value.

3. **High contradiction rate (80.33% of problems).** 482/600 problems had at least some contradictory constraints detected, yet the overall contradiction_rate per constraint is only 5.35%. This suggests the constraint extraction is noisy on ProofWriter's formal rule-based problems.

4. **Extraction rate is decent (91.49%).** The pipeline successfully extracts constraints from most traces, so the issue is not extraction failure but constraint quality.

5. **Hypothesis: task structure mismatch.** ProofWriter has deterministic, rule-following reasoning where the correct chain is unique. SICA's constraint-based reweighting may amplify noise when the model cannot reliably identify the correct reasoning path, whereas SC's simple majority vote is more robust to uniform noise across traces.

## W&B

No W&B run was logged for this experiment.
