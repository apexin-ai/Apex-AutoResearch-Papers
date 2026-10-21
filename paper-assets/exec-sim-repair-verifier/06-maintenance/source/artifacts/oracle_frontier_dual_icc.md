# Oracle Frontier: Majority Voting with Dual ICC

## Model
Beta-binomial majority voting: K correlated models, each with base accuracy p, inter-model ICC = ρ.

P(majority correct) = Σ_{j≥⌈K/2⌉} BetaBinom(j; K, α, β),  where α = p(1−ρ)/ρ, β = (1−p)(1−ρ)/ρ.

## Main Table (p = 0.8751, CLS 8B function-level accuracy)

| K | Independent (ICC=0) | Function-level (ICC=0.191) | Repo-level (ICC=0.3146) | Δ(func−indep) | Δ(repo−indep) |
|--:|--------------------:|---------------------------:|------------------------:|---------------:|--------------:|
| 1 | 87.51% | 87.51% | 87.51% | 0.00 pp | 0.00 pp |
| 3 | 95.71% | 92.02% | 90.44% | −3.69 pp | −5.27 pp |
| 5 | 98.40% | 93.65% | 91.46% | −4.75 pp | −6.94 pp |
| 7 | 99.38% | 94.48% | 91.97% | −4.90 pp | −7.41 pp |
| 9 | 99.75% | 94.98% | 92.28% | −4.77 pp | −7.48 pp |
| 11 | 99.90% | 95.31% | 92.48% | −4.59 pp | −7.42 pp |

Asymptotic (K=101): ICC=0 → 100.00%, ICC=0.191 → 96.77%, ICC=0.3146 → 93.39%.

## Marginal Gain per +2 Models

| K→K+2 | ICC=0 | ICC=0.191 | ICC=0.3146 |
|------:|------:|----------:|-----------:|
| 1→3 | +8.20 pp | +4.51 pp | +2.93 pp |
| 3→5 | +2.69 pp | +1.63 pp | +1.02 pp |
| 5→7 | +0.98 pp | +0.83 pp | +0.51 pp |
| 7→9 | +0.37 pp | +0.50 pp | +0.31 pp |
| 9→11 | +0.15 pp | +0.33 pp | +0.21 pp |

## Interpretation

1. ICC significantly dampens majority voting gains. At K=11, the gap between independent and repo-level ICC is 7.42 pp (99.90% vs 92.48%).
2. Repo-level ICC=0.3146 shows consistently 1.5-3 pp lower accuracy than function-level ICC=0.191, confirming that higher within-problem correlation reduces ensemble diversity.
3. Diminishing returns set in quickly: 60-70% of the total gain is captured at K=3 for both ICC levels.
4. The asymptotic ceiling under repo-level ICC (93.39%) is 3.38 pp below function-level ICC (96.77%), representing a hard information-theoretic limit on majority voting at higher complexity.

## Note on Empirical Calibration

The paper reports empirical K=3 majority voting accuracy of 86.83% (vs theoretical 92.02% at ICC=0.191). This gap suggests that the effective inter-model ICC (seed-to-seed correlation) is substantially higher than the within-instance test-case ICC of 0.191. The ICC values used here are test-case correlation parameters; inter-model correlation in practice is likely higher, making these estimates optimistic upper bounds.
