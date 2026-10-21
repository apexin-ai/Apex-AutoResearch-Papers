# CoNLL 2003 Entity Construction — 2-seed Analysis

## Setup
- Model: Qwen2.5-3B finetuned (exp_002), N=8 samples, θ=2/N=0.25
- Seeds: 123, 456
- Instances: 2756 per seed (gold entities non-empty)
- Construction methods: MV (uniform weights) and LP (softmax logprob weights)

## Per-seed Results

| Seed | Greedy F1 | MV Constr F1 | MV Δ (pp) | LP Constr F1 | LP Δ (pp) |
|------|-----------|-------------|-----------|-------------|-----------|
| 123  | 90.77     | 89.78       | -0.99     | 90.39       | -0.38     |
| 456  | 90.70     | 89.49       | -1.21     | 89.89       | -0.81     |

## Aggregate (2-seed)

| Method | Mean Δ ± σ (pp) | Pooled Δ (pp) | Pooled 95% CI | Pooled p |
|--------|-----------------|---------------|---------------|----------|
| MV     | -1.10 ± 0.11    | -1.10         | [-1.44, -0.74] | 1.0000  |
| LP     | -0.59 ± 0.22    | -0.59         | [-0.89, -0.30] | 1.0000  |

## Degeneracy

| Seed | All-identical instances | Percentage |
|------|----------------------|------------|
| 123  | 1667 / 2756          | 60.5%      |
| 456  | 1662 / 2756          | 60.3%      |

## Conclusion

Construction consistently degrades F1 on CoNLL across both seeds (MV: -1.10pp, LP: -0.59pp). This is consistent with the paper's seed-42 result (-0.39pp LP). The ~60% degeneracy rate confirms that the finetuned model's high confidence produces near-identical samples, making construction ineffective — it can only hurt by introducing noise from the minority of diverse samples. The pooled p-values (1.0) indicate construction is significantly worse than greedy with overwhelming confidence.
