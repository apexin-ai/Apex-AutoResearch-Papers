# 3-Seed NER N=16 Full 5-Signal Summary

Dataset: SciERC NER | N=16 samples | Temperature=1.0 | Seeds: 42, 123, 456

## Table 1: Spearman ρ (Full Split, n=529)

| Signal      | seed42 | seed123 | seed456 | Mean±SD         | CV    |
|-------------|--------|---------|---------|-----------------|-------|
| SJ          | 0.428  | 0.424   | 0.384   | 0.412±0.025     | 6.0%  |
| FK          | 0.281  | 0.275   | 0.223   | 0.260±0.032     | 12.2% |
| logprob     | 0.219  | 0.251   | 0.232   | 0.234±0.016     | 6.8%  |
| EM          | 0.335  | 0.337   | 0.316   | 0.329±0.011     | 3.5%  |
| voting_conf | 0.441  | 0.413   | 0.411   | 0.422±0.017     | 3.9%  |

## Table 2: Spearman ρ (Conditional Split, greedy F1>0)

| Signal      | seed42 (n=477) | seed123 (n=477) | seed456 (n=479) | Mean±SD         | CV    |
|-------------|----------------|-----------------|-----------------|-----------------|-------|
| SJ          | 0.369          | 0.376           | 0.349           | 0.365±0.014     | 3.7%  |
| FK          | 0.193          | 0.178           | 0.157           | 0.176±0.019     | 10.5% |
| logprob     | 0.156          | 0.173           | 0.171           | 0.167±0.009     | 5.5%  |
| EM          | 0.415          | 0.404           | 0.406           | 0.408±0.006     | 1.5%  |
| voting_conf | 0.353          | 0.339           | 0.346           | 0.346±0.007     | 2.0%  |

## Table 3: AUROC (Full Split)

| Signal      | seed42 | seed123 | seed456 | Mean±SD         |
|-------------|--------|---------|---------|-----------------|
| SJ          | 0.737  | 0.736   | 0.711   | 0.728±0.015     |
| FK          | 0.610  | 0.627   | 0.577   | 0.605±0.025     |
| logprob     | 0.587  | 0.606   | 0.594   | 0.596±0.010     |
| EM          | 0.790  | 0.781   | 0.768   | 0.780±0.011     |
| voting_conf | 0.734  | 0.717   | 0.712   | 0.721±0.012     |

## Table 4: AUROC (Conditional Split)

| Signal      | seed42 | seed123 | seed456 | Mean±SD         |
|-------------|--------|---------|---------|-----------------|
| SJ          | 0.719  | 0.721   | 0.699   | 0.713±0.013     |
| FK          | 0.589  | 0.605   | 0.561   | 0.585±0.023     |
| logprob     | 0.569  | 0.584   | 0.576   | 0.577±0.008     |
| EM          | 0.797  | 0.787   | 0.780   | 0.788±0.009     |
| voting_conf | 0.712  | 0.698   | 0.694   | 0.701±0.010     |

## Table 5: Structural > Surface 判定 (SJ vs FK, Full ρ)

| Seed    | SJ ρ  | FK ρ  | Δ(SJ−FK) | Structural > Surface? |
|---------|-------|-------|-----------|-----------------------|
| seed42  | 0.428 | 0.281 | +0.147    | YES                   |
| seed123 | 0.424 | 0.275 | +0.149    | YES                   |
| seed456 | 0.384 | 0.223 | +0.160    | YES                   |
| **Mean**| 0.412 | 0.260 | +0.152    | **ALL 3/3 PASS**      |

## Analysis

### Seed Robustness Ranking (by CV of Full ρ)
1. **EM** — CV=3.5% (most stable)
2. **voting_conf** — CV=3.9%
3. **SJ** — CV=6.0%
4. **logprob** — CV=6.8%
5. **FK** — CV=12.2% (least stable)

In conditional split, EM is even more stable (CV=1.5%).

### SJ ρ Variability
- Mean=0.412, SD=0.025, CV=6.0%
- seed42–seed123 Δ=0.004 (near-identical, consistent with ROADMAP)
- seed456 drops to 0.384 (Δ=0.044 from seed42)
- ROADMAP reported "Δ<0.004" based on 2 seeds — 3rd seed reveals more variance than anticipated

### Signal Rankings by Mean ρ
- **Full**: voting_conf (0.422) > SJ (0.412) > EM (0.329) > FK (0.260) > logprob (0.234)
- **Conditional**: EM (0.408) > SJ (0.365) > voting_conf (0.346) > FK (0.176) > logprob (0.167)

### Signal Rankings by Mean AUROC
- **Full**: EM (0.780) > SJ (0.728) > voting_conf (0.721) > FK (0.605) > logprob (0.596)
- **Conditional**: EM (0.788) > SJ (0.713) > voting_conf (0.701) > FK (0.585) > logprob (0.577)

### Key Findings
1. **Structural > Surface holds across all 3 seeds** — SJ consistently beats FK by ρ Δ≈0.15
2. **EM is the most seed-robust signal** (lowest CV across both splits and both metrics), but it's a discrete signal with limited dynamic range
3. **voting_conf ranks #1 in full ρ**, slightly above SJ — both are structural consistency measures
4. **EM dominates AUROC** across all splits, suggesting it's the best binary discriminator for perfect-F1 instances
5. **FK and logprob are consistently weakest** — surface-level signals have both lower correlation and lower stability
