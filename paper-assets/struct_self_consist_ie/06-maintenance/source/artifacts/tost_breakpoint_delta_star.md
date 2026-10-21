# TOST Breakpoint δ*

**Definition**: δ* = max(|CI_lower|, |CI_upper|) of the 90% CI of the paired mean difference (selection F1 − greedy F1). This is the smallest equivalence margin δ at which TOST (α=0.05) would confirm equivalence.

**Method**: Paired t-distribution 90% CI = mean_Δ ± t_{0.05, n−1} × SE, where SE = std_Δ / √n.

**Data source**: exp_012_rerun_1024 (Qwen2.5-7B-Instruct LoRA, N=8 samples, T=1.0). TOST worker log 2026-05-15.

## NER (SciERC, n=529)

| Signal | mean_Δ (pp) | 90% CI lower (pp) | 90% CI upper (pp) | δ* (pp) |
|--------|-------------|--------------------|--------------------|---------|
| LP     | +0.62       | −0.56              | +1.80              | 1.80    |
| SJ     | +0.11       | −1.06              | +1.28              | 1.28    |
| EM     | −0.79       | −2.07              | +0.49              | 2.07    |
| VC     | −1.02       | −2.29              | +0.25              | 2.29    |
| FK     | −1.80       | −3.38              | −0.22              | 3.38    |

## RE (SciERC, n=397)

| Signal | mean_Δ (pp) | 90% CI lower (pp) | 90% CI upper (pp) | δ* (pp) |
|--------|-------------|--------------------|--------------------|---------|
| LP     | −0.94       | −2.86              | +0.98              | 2.86    |
| SJ     | −1.88       | −3.76              | +0.00              | 3.76    |
| FK     | −2.18       | −4.22              | −0.14              | 4.22    |
| EM     | −3.16       | −5.17              | −1.15              | 5.17    |
| VC     | −4.51       | −6.53              | −2.49              | 6.53    |

## Summary

All δ* ∈ [1.28, 6.53] pp.

- **NER**: δ* ∈ [1.28, 3.38] pp. All 5 signals confirm equivalence at δ=5pp (current paper uses δ=2pp). At δ=2pp, only SJ (1.28) and LP (1.80) pass; EM (2.07), VC (2.29), FK (3.38) require larger margins.
- **RE**: δ* ∈ [2.86, 6.53] pp. At δ=5pp (current paper), LP (2.86), SJ (3.76), FK (4.22) pass; EM (5.17) and VC (6.53) fail. VC has the largest δ* due to systematic negative bias (−4.5pp).

### Implications for paper's TOST parameters

| Paper setting       | NER δ=2pp              | RE δ=5pp               |
|---------------------|------------------------|------------------------|
| Signals that pass   | SJ (1.28), LP (1.80)   | LP (2.86), SJ (3.76), FK (4.22) |
| Borderline          | EM (2.07)              | EM (5.17)              |
| Signals that fail   | VC (2.29), FK (3.38)   | VC (6.53)              |
