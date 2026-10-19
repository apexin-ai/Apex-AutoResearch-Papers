# D012 Mid-Eval Results (Step 10K) — Complete 4-Task

## Overall
| Model | TSR | CAR | frozen_rate | D012 Gate |
|-------|-----|-----|------------|-----------|
| Baseline (Pi0.5) | 74.7% | 26.8% | — | — |
| s0_l005 (λ=0.005) | 47% | 58% | 0% | FAIL (TSR<50%) |
| s0_l01 (λ=0.01) | 49% | 56.5% | 0% | FAIL (TSR<50%) |

## Per-Task
| Task | Baseline TSR/CAR | l005 TSR/CAR | l01 TSR/CAR |
|------|-----------------|-------------|------------|
| 0 orange_juice | 70.7%/10.0% | 18%/62% | 26%/56% |
| 1 choc_pudding | 86.0%/56.0% | 70%/72% | 72%/70% |
| 2 salad_dressing | 66.0%/12.0% | 40%/72% | 46%/72% |
| 3 bbq_sauce | 76.0%/29.3% | 60%/26% | 52%/28% |

## Key Findings
1. CAR passes 33% threshold; TSR fails 50% by 1-3%
2. Task 0 main drag (TSR 18-26%)
3. Task 3 anomaly: CAR decreased from baseline
4. Lambda has minimal effect
5. frozen_rate = 0% (genuine collision avoidance)

serve_policy cleaned up, training continues.
