# SSR (Safe Success Rate) Analysis
# Computed 2026-05-27 by worker_analysis_ssr_computation_20260527T113223
# SSR = (success AND no_collision) / total_episodes

## Per-seed SSR Table

| Condition | TSR (ep-level) | CR (collision rate) | CAR (1-CR) | SSR | n_episodes |
|-----------|---------------|--------------------|-----------:|----:|----------:|
| Pi0.5 baseline | 71.5% | 71.5% | 28.5% | 28.0% | 200 |
| LoRA s0 30K | 51.5% | 43.0% | 57.0% | 29.5% | 200 |
| LoRA s1 30K | 51.5% | 47.5% | 52.5% | 27.0% | 200 |
| SDF lambda=0.005 s0 | 55.5% | 43.0% | 57.0% | 30.0% | 200 |
| SDF lambda=0.005 s1 | 50.5% | 46.0% | 54.0% | 24.0% | 200 |
| SDF lambda=0.005 s2 | 56.0% | 47.5% | 52.5% | 29.5% | 200 |
| SDF lambda=0.01 s0 | 52.5% | 43.0% | 57.0% | 32.5% | 200 |
| SDF lambda=0.01 s1 | 55.5% | 42.5% | 57.5% | 30.0% | 200 |
| SDF lambda=0.01 s2 | 53.5% | 45.5% | 54.5% | 28.0% | 200 |
| SDF lambda=0.1 s0 | — | — | — | — | JSON overwritten |
| SDF lambda=0.1 s1 | 49.0% | 41.5% | 58.5% | 26.5% | 200 |

## Condition Averages

| Condition | Avg TSR | Avg CAR | Avg SSR | SSR/TSR |
|-----------|---------|---------|---------|---------|
| Pi0.5 baseline | 71.5% | 28.5% | 28.0% | 0.392 |
| LoRA (3 seeds) | 49.7% | 54.83% | 27.7% | 0.557 |
| SDF lambda=0.005 (3 seeds) | 54.0% | 54.5% | 27.8% | 0.515 |
| SDF lambda=0.01 (3 seeds) | 53.8% | 56.3% | 30.2% | 0.561 |
| SDF lambda=0.1 (1 seed only) | 49.0% | 58.5% | 26.5% | 0.541 |

## Key Finding: SSR/TSR ratio refutes "reduced exposure"

Under "reduced exposure" hypothesis: model simply does fewer things → SSR/TSR ≈ constant.
Observed: SSR/TSR jumps from 0.39 (baseline) to ~0.55 (all trained models).
This means a higher fraction of successful episodes are collision-free after training.

## Caveats
- Worker's original "CAR" column was collision RATE (not avoidance rate). Corrected above.
- SDF lambda=0.1 s0 JSON overwritten by reeval_lora. Only 1 seed available for lambda=0.1.
- n=200 episodes per condition (50 per task × 4 tasks). SE of SSR ≈ 6.5pp → differences not individually significant.
- SSR/TSR ratio argument is more compelling than raw SSR comparison.
- Episode-level TSR differs from registry's task-averaged TSR (both valid, different aggregation).
