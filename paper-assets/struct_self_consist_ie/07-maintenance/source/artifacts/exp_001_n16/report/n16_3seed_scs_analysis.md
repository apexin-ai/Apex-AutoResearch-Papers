# N=16 Three-Seed SCS Analysis (Qwen SciERC)

Config: Qwen2.5-7B-Instruct, SciERC, N=16 samples, T=1.0, max_tokens=1024, seeds={42, 123, 456}.
NER instances: 529 (gold entities non-empty). RE instances: 397 (gold relations non-empty).

## Table A: Per-seed Spearman ρ — NER (vs greedy NER F1)

| Signal | seed=42 | seed=123 | seed=456 | mean | σ |
|--------|---------|----------|----------|------|---|
| SJ     | 0.3984  | 0.4234   | 0.4098   | 0.4105 | 0.0102 |
| FK     | 0.2876  | 0.2899   | 0.2723   | 0.2833 | 0.0079 |
| VC     | 0.3993  | 0.3835   | 0.4449   | 0.4092 | 0.0260 |
| EM     | 0.3386  | 0.3437   | 0.3363   | 0.3395 | 0.0031 |
| LP     | 0.2373  | 0.2391   | 0.2415   | 0.2393 | 0.0017 |

## Table A2: Per-seed Spearman ρ — RE (vs greedy RE F1)

| Signal | seed=42 | seed=123 | seed=456 | mean | σ |
|--------|---------|----------|----------|------|---|
| SJ     | 0.2766  | 0.2672   | 0.2835   | 0.2758 | 0.0067 |
| FK     | 0.2808  | 0.3154   | 0.2929   | 0.2964 | 0.0143 |
| VC     | 0.3801  | 0.3522   | 0.3892   | 0.3738 | 0.0158 |
| EM     | 0.1475  | 0.1575   | 0.1469   | 0.1506 | 0.0049 |
| LP     | 0.2931  | 0.3071   | 0.3298   | 0.3100 | 0.0152 |

## Table B: Per-seed AUROC — NER (above-median NER F1)

| Signal | seed=42 | seed=123 | seed=456 | mean | σ |
|--------|---------|----------|----------|------|---|
| SJ     | 0.6965  | 0.7131   | 0.6997   | 0.7031 | 0.0072 |
| FK     | 0.6323  | 0.6393   | 0.6261   | 0.6326 | 0.0054 |
| VC     | 0.7039  | 0.6947   | 0.7141   | 0.7042 | 0.0079 |
| EM     | 0.6773  | 0.6787   | 0.6651   | 0.6737 | 0.0061 |
| LP     | 0.6215  | 0.6261   | 0.6204   | 0.6227 | 0.0025 |

## Table B2: Per-seed AUROC — RE (above-median RE F1)

| Signal | seed=42 | seed=123 | seed=456 | mean | σ |
|--------|---------|----------|----------|------|---|
| SJ     | 0.6372  | 0.6425   | 0.6710   | 0.6502 | 0.0149 |
| FK     | 0.6514  | 0.6579   | 0.6777   | 0.6623 | 0.0112 |
| VC     | 0.6989  | 0.6846   | 0.7029   | 0.6955 | 0.0079 |
| EM     | 0.5557  | 0.5905   | 0.6013   | 0.5825 | 0.0194 |
| LP     | 0.6552  | 0.6466   | 0.6710   | 0.6576 | 0.0101 |

## Table C: Three-Seed Summary (mean ± σ)

### Spearman ρ

| Signal | NER ρ (mean ± σ) | RE ρ (mean ± σ) |
|--------|-------------------|-----------------|
| VC     | **0.4092 ± 0.0260** | **0.3738 ± 0.0158** |
| SJ     | **0.4105 ± 0.0102** | 0.2758 ± 0.0067 |
| EM     | 0.3395 ± 0.0031 | 0.1506 ± 0.0049 |
| FK     | 0.2833 ± 0.0079 | 0.2964 ± 0.0143 |
| LP     | 0.2393 ± 0.0017 | 0.3100 ± 0.0152 |

### AUROC

| Signal | NER AUROC (mean ± σ) | RE AUROC (mean ± σ) |
|--------|----------------------|---------------------|
| VC     | **0.7042 ± 0.0079** | **0.6955 ± 0.0079** |
| SJ     | **0.7031 ± 0.0072** | 0.6502 ± 0.0149 |
| EM     | 0.6737 ± 0.0061 | 0.5825 ± 0.0194 |
| FK     | 0.6326 ± 0.0054 | 0.6623 ± 0.0112 |
| LP     | 0.6227 ± 0.0025 | 0.6576 ± 0.0101 |

## Table D: Ranking Consistency

### NER ρ ranking per seed

| Seed | Ranking |
|------|---------|
| 42   | VC (0.399) ≈ SJ (0.398) > EM > FK > LP |
| 123  | SJ (0.423) > VC (0.384) > EM > FK > LP |
| 456  | VC (0.445) > SJ (0.410) > EM > FK > LP |

Rank order (1=best): SJ gets {2, 1, 2}, VC gets {1, 2, 1}. Bottom 3 (EM > FK > LP) perfectly stable.

### RE ρ ranking per seed

| Seed | Ranking |
|------|---------|
| 42   | VC > LP > FK > SJ > EM |
| 123  | VC > FK > LP > SJ > EM |
| 456  | VC > LP > FK > SJ > EM |

VC consistently #1, EM consistently #5, SJ consistently #4. Only FK/LP swap at #2-3 in seed=123.

### Kendall's W (concordance coefficient)

| Subtask | W | Interpretation |
|---------|---|----------------|
| NER     | 0.956 | Near-perfect agreement (only SJ/VC swap) |
| RE      | 0.956 | Near-perfect agreement (only FK/LP swap) |

## Table E: N=8 vs N=16 Comparison (Qwen SciERC, ρ mean)

### NER ρ

| Signal | N=8 mean | N=16 mean | Δ | Δ% |
|--------|----------|-----------|---|-----|
| SJ     | 0.3641   | 0.4105    | **+0.0464** | +12.7% |
| FK     | 0.2536   | 0.2833    | +0.0297 | +11.7% |
| VC     | 0.3861   | 0.4092    | +0.0231 | +6.0% |
| EM     | 0.3071   | 0.3395    | +0.0324 | +10.6% |
| LP     | 0.2167   | 0.2393    | +0.0226 | +10.4% |

### RE ρ

| Signal | N=8 mean | N=16 mean | Δ | Δ% |
|--------|----------|-----------|---|-----|
| SJ     | 0.2485   | 0.2758    | +0.0273 | +11.0% |
| FK     | 0.2903   | 0.2964    | +0.0061 | +2.1% |
| VC     | 0.3088   | 0.3738    | **+0.0650** | +21.1% |
| EM     | 0.1353   | 0.1506    | +0.0153 | +11.3% |
| LP     | 0.2970   | 0.3100    | +0.0130 | +4.4% |

### Cross-seed σ comparison

| Signal | NER σ(N=8) | NER σ(N=16) | RE σ(N=8) | RE σ(N=16) |
|--------|------------|-------------|-----------|------------|
| SJ     | 0.0179     | 0.0102      | 0.0015    | 0.0067     |
| FK     | 0.0157     | 0.0079      | 0.0121    | 0.0143     |
| VC     | 0.0187     | 0.0260      | 0.0244    | 0.0158     |
| EM     | 0.0076     | 0.0031      | 0.0157    | 0.0049     |
| LP     | 0.0125     | 0.0017      | 0.0218    | 0.0152     |

### Ranking shift N=8 → N=16

| Subtask | N=8 ranking | N=16 ranking | Changed? |
|---------|------------|--------------|----------|
| NER     | VC > SJ > EM > FK > LP | VC ≈ SJ > EM > FK > LP | SJ closes gap with VC |
| RE      | VC > LP > FK > SJ > EM | VC > LP > FK > SJ > EM | Identical |

## Key Findings

1. **SJ overtakes VC in NER ρ (by mean)**: At N=16, SJ mean ρ = 0.411 vs VC = 0.409. They are essentially tied, but SJ has lower σ (0.010 vs 0.026). At N=8, VC led by 0.022. SJ benefits most from additional samples due to its pairwise soft-Jaccard formulation gaining more signal from C(16,2)=120 pairs vs C(8,2)=28.

2. **VC dominates RE**: VC ρ = 0.374 is the only signal above 0.35 in RE, with a large margin over #2 LP (0.310). The N=8→N=16 improvement for VC-RE is the largest observed (+0.065, +21%).

3. **All signals improve with N=16**: Every signal's mean ρ increases from N=8 to N=16. NER improvements range +6–13%, RE improvements +2–21%.

4. **Cross-seed stability generally improves**: LP σ drops from 0.0125 to 0.0017 (NER), EM from 0.0076 to 0.0031. Exception: VC-NER σ increases from 0.0187 to 0.0260, and SJ-RE σ increases from 0.0015 to 0.0067.

5. **RE signal ranking stabilizes at N=16**: N=8 had minor RE ranking instability (VC/LP/FK swapping). N=16 produces the same RE ranking across 2/3 seeds, with only seed=123 swapping FK↔LP.

6. **Structural > logprob claim strengthened for NER**: All structural signals (SJ, FK, EM, VC) beat LP in all NER seeds. The gap widens at N=16 (SJ-LP gap: 0.147→0.171). For RE, LP still beats SJ and FK individually, but VC consistently dominates LP.
