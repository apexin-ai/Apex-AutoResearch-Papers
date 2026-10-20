# ssh power analysis delta tau

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_power_analysis_delta_tau_20260523T012958_result.json`
- **Structured JSON:** [`f9e06ec79256880efe80.json`](../../sessions/f9/f9e06ec79256880efe80.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
Power Analysis for Δτ = 0.071:

Bootstrap empirical std (N=8): 0.0360
Scaling assumption: std(N) = std(8) * sqrt(8/N)

Minimum N for 80% power (α=0.05, two-sided): 17

Power table:
  N=  8: std=0.0360, power=0.505  <-- current
  N= 10: std=0.0322, power=0.597
  N= 12: std=0.0294, power=0.676
  N= 15: std=0.0263, power=0.771
  N= 20: std=0.0228, power=0.877
  N= 25: std=0.0204, power=0.937
  N= 30: std=0.0186, power=0.969
  N= 40: std=0.0161, power=0.993
  N= 50: std=0.0144, power=0.999

Note: The exact Kendall τ variance formula gives much larger std values (0.289 at N=8 vs 0.036),
confirming that the bootstrap std reflects the variance of the *difference* in posterior-mean τ
(not a single τ), which is heavily reduced by the paired/dependent structure.
The 1/sqrt(N) scaling is an approximation — actual scaling depends on how adding models
affects the posterior mean correlation structure. This estimate is likely optimistic
(true minimum N may be somewhat higher).
```

**Minimum N = 17 target models** to detect Δτ=0.071 at 80% power. Current N=8 only has ~50% power, explaining the non-significant result. Doubling to N≈20 would give ~88% power with comfortable margin.

---
