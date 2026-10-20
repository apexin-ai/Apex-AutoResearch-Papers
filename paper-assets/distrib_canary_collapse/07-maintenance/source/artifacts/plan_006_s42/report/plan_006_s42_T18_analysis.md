# plan_006_s42 T=18 Extended Generation Analysis

## Configuration
- Model: EleutherAI/pythia-410m
- Dataset: WikiText-103 (full, not 5k subset)
- α (synthetic_ratio): 1.0
- Seed: 42
- steps_per_gen: 10000, batch_size: 4, lr: 5e-5, max_length: 512
- Completed: gen_0–gen_17 (T=18), gen_18-20 timeout (D034: T=18 sufficient)
- GPU hours: 12.0h on A100

## Full 18-Generation Drift Trajectory

| Gen | token_entropy | distinct_1 | distinct_2 | distinct_3 | ece | perplexity | self_bleu | eff_rank | mauve |
|-----|--------------|------------|------------|------------|-----|------------|-----------|----------|-------|
| 0 | 3.2342 | 0.0982 | 0.5178 | 0.8127 | 0.0108 | 26.95 | 0.0102 | 46.61 | 0.0341 |
| 1 | 1.5253 | 0.0975 | 0.5141 | 0.8104 | 0.3268 | 185.68 | 0.0103 | 66.77 | 0.0323 |
| 2 | 1.2962 | 0.0846 | 0.4390 | 0.7141 | 0.3781 | 380.41 | 0.0114 | 79.39 | 0.0336 |
| 3 | 1.2141 | 0.0798 | 0.4025 | 0.6606 | 0.3986 | 568.76 | 0.0124 | 90.86 | 0.0335 |
| 4 | 1.2192 | 0.0782 | 0.3890 | 0.6390 | 0.4093 | 734.41 | 0.0130 | 94.68 | 0.0322 |
| 5 | 1.1711 | 0.0780 | 0.3867 | 0.6358 | 0.4223 | 930.22 | 0.0132 | 94.21 | 0.0329 |
| 6 | 1.1343 | 0.0780 | 0.3865 | 0.6353 | 0.4322 | 1187.47 | 0.0132 | 96.77 | 0.0330 |
| 7 | 1.1313 | 0.0780 | 0.3865 | 0.6352 | 0.4371 | 1389.60 | 0.0132 | 98.95 | 0.0328 |
| 8 | 1.1402 | 0.0780 | 0.3865 | 0.6351 | 0.4384 | 1566.03 | 0.0132 | 96.50 | 0.0318 |
| 9 | 1.1456 | 0.0779 | 0.3860 | 0.6342 | 0.4406 | 1786.72 | 0.0132 | 99.19 | 0.0323 |
| 10 | 1.1468 | 0.0779 | 0.3860 | 0.6343 | 0.4443 | 2032.49 | 0.0132 | 101.80 | 0.0318 |
| 11 | 1.1360 | 0.0779 | 0.3863 | 0.6348 | 0.4493 | 2306.49 | 0.0132 | 104.52 | 0.0327 |
| 12 | 1.1498 | 0.0779 | 0.3859 | 0.6339 | 0.4502 | 2479.56 | 0.0132 | 101.99 | 0.0321 |
| 13 | 1.1523 | 0.0777 | 0.3838 | 0.6299 | 0.4505 | 2579.57 | 0.0131 | 103.26 | 0.0325 |
| 14 | 1.1397 | 0.0773 | 0.3798 | 0.6222 | 0.4540 | 2846.24 | 0.0131 | 105.49 | 0.0337 |
| 15 | 1.1506 | 0.0770 | 0.3753 | 0.6151 | 0.4550 | 2923.24 | 0.0130 | 104.76 | 0.0329 |
| 16 | 1.2079 | 0.0761 | 0.3665 | 0.5966 | 0.4500 | 3145.47 | 0.0134 | 96.83 | 0.0315 |
| 17 | 1.1819 | 0.0756 | 0.3617 | 0.5865 | 0.4454 | 3367.66 | 0.0138 | 99.15 | 0.0321 |

## Three-Phase Collapse Dynamics

### Phase 1: Rapid Collapse (gen_0→5)
- distinct_1: 0.0982→0.0780 (-20.6%)
- distinct_2: 0.5178→0.3867 (-25.3%)
- distinct_3: 0.8127→0.6358 (-21.8%)
- token_entropy: 3.234→1.171 (-63.8%, with 52.8% drop at gen_0→1 alone)
- ECE: 0.0108→0.4223 (+3810%)
- perplexity: 26.95→930.22 (+3353%)

### Phase 2: Apparent Plateau (gen_5→12)
- distinct_1/2/3: <0.3% total change (near-flat)
- token_entropy: oscillates in 1.13-1.15 band
- ECE: 0.422→0.450 (+6.6%, slow drift)
- perplexity: 930→2480 (+167%, still growing while diversity is stable)
- Key observation: diversity-perplexity decoupling — model quality degrades but output diversity appears saturated

### Phase 3: Secondary Decline (gen_13→17)
- distinct_1: 0.0779→0.0756 (-2.7%)
- distinct_2: 0.3859→0.3617 (-5.8%)
- distinct_3: 0.6339→0.5865 (-6.9%)
- Breakpoint at gen_13: distinct_2 drops from 0.3859 to 0.3838
- Acceleration at gen_16-17: distinct_3 drops 0.019 and 0.010 in consecutive generations
- ECE slightly reverses (0.4505→0.4454), decoupling from diversity
- **This phase is invisible in T=10 data**

## T=10 vs T=18 Comparison

| Metric | T=10 drift (gen0→9) | T=18 drift (gen0→17) | Additional drift gen10→17 |
|--------|---------------------|----------------------|--------------------------|
| distinct_1 | -20.7% | -23.0% | -2.3pp |
| distinct_2 | -25.5% | -30.1% | -4.6pp |
| distinct_3 | -22.0% | -27.8% | -5.8pp |
| token_entropy | -64.6% | -63.4% | saturated |
| ECE | +3979% | +4024% | saturated |
| perplexity | +6531% | +12395% | +5864pp (still growing) |

## Implications

1. **For statistical power**: T=18 corresponds to TY Granger power ~0.28-0.41 (plan_009 bootstrap at T=20), substantially better than T=10's 0.05-0.21
2. **For paper narrative**: Three-phase collapse supports a richer story than simple monotonic decay
3. **Perplexity non-saturation**: 18 generations still insufficient for perplexity plateau — growth rate ~200/gen remains roughly constant
4. **Metric-dependent saturation**: token_entropy and ECE saturate by gen_5-6; diversity saturates gen_5-12 then resumes decline; perplexity never saturates
5. **Caution (C001)**: Single seed — Phase 3 secondary decline must be confirmed with multi-seed before citing in paper
