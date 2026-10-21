# Entropy-Conditioned Analysis: exp-038 (Qwen2.5-14B LogiQA-200)

**Overall**: SICA=78.0%, SC=78.5%, Delta=-0.5pp, n=200

## Main Table

| Entropy Bin | n (%) | SC Acc | SICA Acc | Delta (pp) | Override n | Override Precision |
|---|---|---|---|---|---|---|
| Low [0, 0.5) | 150 (75.0%) | 84.0% | 84.0% | +0.0 | 0 | N/A |
| Med [0.5, 1.0) | 34 (17.0%) | 67.6% | 64.7% | -2.9 | 1 | 0.0% (0/1) |
| High [1.0, +inf) | 16 (8.0%) | 50.0% | 50.0% | +0.0 | 2 | 50.0% (1/2) |

## Additional Stats

- **Unanimous rate**: 126/200 = 63.0%
- **Avg majority fraction**: 0.913
- **Dedup ratio** (unique/total constraints): 5348/6852 = 0.781

## Entropy Distribution

| Entropy Range | Count |
|---|---|
| [0.00, 0.25) | 126 |
| [0.25, 0.50) | 24 |
| [0.50, 0.75) | 11 |
| [0.75, 1.00) | 23 |
| [1.00, 1.25) | 6 |
| [1.25, 1.50) | 8 |
| [1.50, 1.75) | 2 |

Mean=0.290, Median=0.000, Std=0.435, Max=1.730

## Override Analysis

- **Low entropy**: 0 overrides (SICA never disagrees with SC)
- **Med entropy**: 1 override, all bad (SC right -> SICA wrong)
- **High entropy**: 2 overrides, 1 good + 1 bad = net zero

Total overrides: **3 out of 200** problems (1.5%)

## Cross-Experiment Comparison

| Metric | Qwen14B FOLIO-204 (exp-026) | Mistral-7B FOLIO-204 (exp-033) | Qwen14B LogiQA-200 (exp-038) |
|---|---|---|---|
| Overall SICA | 85.3% | 70.1% | 78.0% |
| Overall SC | 84.8% | 67.2% | 78.5% |
| Overall Delta | +0.5pp | +2.9pp | -0.5pp |
| Low entropy n% | ~90% | 64.2% | 75.0% |
| Low entropy delta | +0.0pp | +0.0pp | +0.0pp |
| High entropy n% | 10.3% | 35.8% | 8.0% |
| High entropy delta | +4.8pp | +9.6pp | +0.0pp |
| Unanimous rate | - | - | 63.0% |

## Key Findings

1. **Low entropy = no difference**: Consistent with FOLIO findings. When SC votes are near-unanimous, SICA adds nothing (and correctly avoids overriding).

2. **High entropy provides no benefit on LogiQA**: Unlike FOLIO where high-entropy bins showed +4.8pp (Qwen) and +9.6pp (Mistral), LogiQA shows +0.0pp. Only 2 overrides in this bin, with 1 good and 1 bad canceling out.

3. **Extremely few overrides**: Only 3/200 (1.5%) problems have SICA != SC. On FOLIO, SICA overrode more frequently. This suggests the constraint extraction on LogiQA is less effective at producing discriminative signals.

4. **Mass distribution**: 75% low-entropy (between FOLIO-Mistral's 64% and FOLIO-Qwen's 90%). Only 8% high-entropy problems, a small pool where SICA could theoretically help.

5. **Net negative**: The single bad override in the medium-entropy bin accounts for the overall -0.5pp delta. SICA's constraint signal on LogiQA is too weak to overcome SC.
