# Statistical Robustness Analysis - exp-008

**P-values: exact two-tailed permutation test (n=5, 120 permutations)**

## Bootstrap CI (n=10000)

| Benchmark | obs rho | 95% Pct CI | P(rho<0) |
|-----------|---------|------------|----------|
| LAMBADA | -1.0000 | [-1.0000, 0.0000] | 0.887 |
| HellaSwag | +0.3000 | [-0.9000, 0.5000] | 0.438 |
| WinoGrande | +0.1000 | [-0.9000, 0.3000] | 0.232 |
| ARC-Easy | -0.7000 | [-0.9000, 0.0000] | 0.889 |
| ARC-Challenge | +0.6000 | [-0.2000, 0.7071] | 0.217 |
| MMLU | -0.7000 | [-0.8000, 0.6000] | 0.699 |

LAMBDA BCa CI: [-1.0000, -0.7000] (z0=-0.7746, a=0.0680)

## GDN Exclusion

| Benchmark | rho(3 arch) | rho(no GDN) | p_exact(no GDN) | mono |
|-----------|-------------|-------------|-----------------|------|
| LAMBADA | -1.0000 | -0.7000 | 0.2333 | N |
| HellaSwag | +0.3000 | +0.5000 | 0.4500 | N |
| WinoGrande | +0.1000 | +0.3000 | 0.6833 | N |
| ARC-Easy | -0.7000 | -0.9000 | 0.0833 | N |
| ARC-Challenge | +0.6000 | -0.2000 | 0.7833 | N |
| MMLU | -0.7000 | +0.6000 | 0.3500 | N |

## Multiple Comparison Correction (exact permutation p-values)

| Benchmark | p_exact | Bonferroni | BH-FDR | Bonf sig | BH sig |
|-----------|---------|------------|--------|----------|--------|
| LAMBADA | 0.0167 | 0.1000 | 0.1000 | N | N |
| HellaSwag | 0.6833 | 1.0000 | 0.8200 | N | N |
| WinoGrande | 0.9500 | 1.0000 | 0.9500 | N | N |
| ARC-Easy | 0.2333 | 1.0000 | 0.4667 | N | N |
| ARC-Challenge | 0.3500 | 1.0000 | 0.5250 | N | N |
| MMLU | 0.2333 | 1.0000 | 0.4667 | N | N |

**LAMBADA: Bonferroni adj-p = 0.1000, BH-FDR adj-p = 0.1000**

## Effect Sizes (pure vs h3-1)

| Benchmark | Cohen d | 95% CI | eta2 | omega2 |
|-----------|---------|--------|------|--------|
| LAMBADA | -0.207 | [-1.812, +1.398] | 0.0807 | -0.2628 |
| HellaSwag | -0.062 | [-1.663, +1.538] | 0.0674 | -0.2795 |
| WinoGrande | +0.029 | [-1.571, +1.630] | 0.0153 | -0.3446 |
| ARC-Easy | -0.561 | [-2.193, +1.070] | 0.1211 | -0.2118 |
| ARC-Challenge | -0.141 | [-1.743, +1.462] | 0.0624 | -0.2859 |
| MMLU | -0.346 | [-1.959, +1.266] | 0.3003 | 0.0190 |
