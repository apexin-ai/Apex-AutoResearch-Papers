# MDE Analysis: Spider SQL Experiment (n=196)

## Experiment Facts
- **Dataset**: Spider SQL, n=196 instances, model=GPT-5.5, N=8 samples, T=1.0
- **Observed**: greedy_acc=76.53%, mv_acc=77.04%, **MV gain=+0.51pp**
- **Degeneracy**: 87.24% (only ~25 non-degenerate instances)
- **Metric**: Execution accuracy (binary), not F1

## MDE Results

### Continuous framework (paired t-test)
At n=196, α=0.05, power=0.80:

| σ_diff | MDE |
|--------|-----|
| 0.05 | 1.00pp |
| 0.10 | 2.00pp |
| 0.15 | 3.00pp |
| 0.20 | 4.00pp |

### Binary framework (McNemar)
Since SQL uses binary accuracy, the appropriate framework uses discordant pair rate:

| Discordant rate | σ_diff | MDE |
|-----------------|--------|-----|
| 5% | 0.224 | 4.47pp |
| 10% | 0.316 | 6.33pp |
| 12.76% (= 1 - degeneracy) | 0.357 | 7.15pp |

## Power at Observed Effect (δ=0.51pp)

| σ_diff | Achieved power |
|--------|---------------|
| 0.10 | 10.6% |
| 0.125 | 8.2% |
| 0.15 | 6.9% |
| Binary (p_disc=12.76%) | 3.9% |

**The experiment has only 4-11% power to detect the observed +0.51pp effect (need 80%).**

## Required Sample Sizes (α=0.05, power=0.80, σ=0.125)

| Target effect | Required n |
|--------------|-----------|
| 0.5pp | 4,906 |
| 1.0pp | 1,227 |
| 1.5pp | 546 |
| 2.0pp | 307 |
| 3.0pp | 137 |

## Comparison with NER Effects

| Experiment | Observed MV gain | MDE@σ=0.10 | Powered? |
|-----------|-----------------|------------|---------|
| Spider SQL (n=196) | +0.51pp | 2.00pp | NO |
| CoNLL NER (n=3453) | +0.15pp | 0.48pp | NO |
| FewNERD Sonnet 4 (n=200) | +1.58pp | 1.98pp | NO |
| FewNERD DeepSeek (n=200) | +2.51pp | 1.98pp | MAYBE |
| FewNERD Gemini (n=200) | +1.45pp | 1.98pp | NO |
| FewNERD GPT-5.5 (n=200) | +1.39pp | 1.98pp | NO |

## Conclusions

1. **n=196 is severely underpowered** for the observed +0.51pp MV gain. MDE = 2-3pp (continuous) or 4-7pp (binary), far above the observed effect.
2. **87% degeneracy compounds the problem**: effective informative sample size is ~25, not 196.
3. **To detect 1pp effect** with 80% power: need n ≈ 1,227 (at σ=0.125).
4. **Most NER experiments (n=200) are also underpowered**, except DeepSeek (+2.51pp) which is borderline.
5. The small sample size limitation is **acknowledged but not fatal** for the paper's argument — the SQL experiment demonstrates the *framework's applicability* to a new task, and the directionally positive result (+0.51pp) is consistent with NER findings even if not individually significant.
