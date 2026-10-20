# 4PL vs 3PL vs 2PL Detection Sensitivity Ablation

## Setup

- N_persons = 500, N_sims = 10, seed = 42
- Max items per benchmark = 2000 (sampled if larger)
- Contamination levels: [0, 5, 10, 15, 25, 50, 75, 90, 100]
- Data generation: always 4PL (ground truth)
- Detection: lz* computed under 4PL / 3PL(d=1) / 2PL(c=0.25,d=1)

## d-parameter distribution (full item sets)

| Benchmark | N items | mean(d) | std(d) | % d<0.95 | % d<0.90 | % d<0.80 |
|-----------|---------|---------|--------|----------|----------|----------|
| MMLU | 14042 | 0.8921 | 0.1499 | 46.1% | 28.4% | 16.7% |
| HELLASWAG | 10042 | 0.9304 | 0.1109 | 34.2% | 16.8% | 7.9% |
| GSM8K | 1319 | 0.9167 | 0.1297 | 38.4% | 20.3% | 10.6% |
| ARC_C | 295 | 0.9481 | 0.0901 | 24.1% | 10.5% | 4.7% |
| HUMANEVAL | 164 | 0.8957 | 0.1393 | 50.6% | 28.0% | 14.6% |

## False alarm rate (contam=0%)

Expected: ~5% (two-sided α=0.05)

| Benchmark | 4PL | 3PL | 2PL |
|-----------|-----|-----|-----|
| MMLU | 0.0508 | 0.0616 | 0.9986 |
| HELLASWAG | 0.0448 | 0.0714 | 0.9962 |
| GSM8K | 0.0456 | 0.1652 | 0.9568 |
| ARC_C | 0.0460 | 0.0474 | 0.5004 |
| HUMANEVAL | 0.0506 | 0.0570 | 0.5244 |

## Detection power at 25% contamination

| Benchmark | 4PL | 3PL | 2PL | Δ(4PL-3PL) | Δ(3PL-2PL) |
|-----------|-----|-----|-----|------------|------------|
| MMLU | 0.7760 | 0.3294 | 0.9892 | +0.4466 | -0.6598 |
| HELLASWAG | 0.5344 | 0.2796 | 0.9784 | +0.2548 | -0.6988 |
| GSM8K | 0.7302 | 0.3336 | 0.5756 | +0.3966 | -0.2420 |
| ARC_C | 0.1318 | 0.0910 | 0.3204 | +0.0408 | -0.2294 |
| HUMANEVAL | 0.3184 | 0.1646 | 0.1356 | +0.1538 | +0.0290 |

## Power gain: 4PL vs 3PL (averaged over contamination levels)

| Benchmark | Mean Δpower | Max Δpower |
|-----------|-------------|------------|
| MMLU | +0.2729 | +0.4902 |
| HELLASWAG | +0.2612 | +0.5962 |
| GSM8K | +0.2027 | +0.3966 |
| ARC_C | +0.1483 | +0.5464 |
| HUMANEVAL | +0.1368 | +0.3064 |

## Power gain: 3PL vs 2PL (averaged over contamination levels)

| Benchmark | Mean Δpower | Max Δpower |
|-----------|-------------|------------|
| MMLU | -0.5222 | +0.0000 |
| HELLASWAG | -0.5615 | +0.0000 |
| GSM8K | -0.1880 | +0.3258 |
| ARC_C | -0.1982 | +0.0000 |
| HUMANEVAL | -0.0396 | +0.2334 |

## d-bucket analysis (4PL vs 3PL power at 50% contamination)

| Benchmark | d<0.8 | 0.8≤d<0.9 | 0.9≤d<0.95 | d≥0.95 |
|-----------|-------|-----------|------------|--------|
| MMLU | +0.6116 | +0.2608 | +0.1640 | -0.0116 |
| HELLASWAG | +0.5776 | +0.1308 | +0.1456 | -0.0164 |
| GSM8K | +0.3988 | +0.0744 | +0.0636 | +0.0256 |
| ARC_C | +0.0752 | +0.0136 | +0.0264 | +0.0104 |
| HUMANEVAL | +0.0684 | +0.0236 | -0.0068 | -0.0020 |

## Full power table

| Benchmark | Param | 0% | 5% | 10% | 15% | 25% | 50% | 75% | 90% | 100% |
|-----------|-------|------|------|------|------|------|------|------|------|------|
| MMLU | 4PL | 0.051 | 0.153 | 0.325 | 0.490 | 0.776 | 0.879 | 0.839 | 0.879 | 1.000 |
| MMLU | 3PL | 0.062 | 0.114 | 0.184 | 0.244 | 0.329 | 0.389 | 0.407 | 0.490 | 1.000 |
| MMLU | 2PL | 0.999 | 0.998 | 0.998 | 0.997 | 0.989 | 0.811 | 0.757 | 0.786 | 1.000 |
| HELLASWAG | 4PL | 0.045 | 0.115 | 0.220 | 0.315 | 0.534 | 0.864 | 0.831 | 0.855 | 1.000 |
| HELLASWAG | 3PL | 0.071 | 0.110 | 0.170 | 0.206 | 0.280 | 0.332 | 0.288 | 0.258 | 1.000 |
| HELLASWAG | 2PL | 0.996 | 0.995 | 0.990 | 0.991 | 0.978 | 0.799 | 0.715 | 0.668 | 1.000 |
| GSM8K | 4PL | 0.046 | 0.147 | 0.316 | 0.480 | 0.730 | 0.840 | 0.812 | 0.815 | 1.000 |
| GSM8K | 3PL | 0.165 | 0.156 | 0.186 | 0.235 | 0.334 | 0.518 | 0.601 | 0.489 | 1.000 |
| GSM8K | 2PL | 0.957 | 0.931 | 0.898 | 0.842 | 0.576 | 0.221 | 0.275 | 0.280 | 1.000 |
| ARC_C | 4PL | 0.046 | 0.059 | 0.071 | 0.099 | 0.132 | 0.277 | 0.505 | 0.628 | 1.000 |
| ARC_C | 3PL | 0.047 | 0.059 | 0.064 | 0.082 | 0.091 | 0.120 | 0.089 | 0.082 | 1.000 |
| ARC_C | 2PL | 0.500 | 0.489 | 0.452 | 0.396 | 0.320 | 0.200 | 0.148 | 0.167 | 1.000 |
| HUMANEVAL | 4PL | 0.051 | 0.077 | 0.122 | 0.191 | 0.318 | 0.560 | 0.510 | 0.479 | 1.000 |
| HUMANEVAL | 3PL | 0.057 | 0.057 | 0.076 | 0.097 | 0.165 | 0.295 | 0.300 | 0.173 | 1.000 |
| HUMANEVAL | 2PL | 0.524 | 0.459 | 0.377 | 0.275 | 0.136 | 0.061 | 0.091 | 0.081 | 1.000 |

## Key findings

### 1. 4PL significantly outperforms 3PL in contamination detection

The d parameter provides substantial detection power gains across all benchmarks:
- **MMLU**: +27.3pp mean power gain (max +49.0pp)
- **HellaSwag**: +26.1pp mean power gain (max +59.6pp)
- **GSM8K**: +20.3pp mean power gain (max +39.7pp)
- **ARC_C**: +14.8pp mean power gain (max +54.6pp)
- **HumanEval**: +13.7pp mean power gain (max +30.6pp)

### 2. False alarm rates confirm proper calibration

- **4PL**: FAR ≈ 5% across all benchmarks (well-calibrated)
- **3PL**: FAR slightly inflated (4.7–16.5%), worst on GSM8K (16.5%) due to d-misspecification
- **2PL**: FAR catastrophically inflated (50–100%) due to fixed c=0.25 mismatching true item-specific guessing parameters. **2PL power numbers are not interpretable** — the model rejects nearly all responses even without contamination.

### 3. d-parameter impact is strongest for items with low d

d-bucket analysis at 50% contamination (4PL - 3PL power difference):
- **d < 0.8**: +6.8pp to +61.2pp advantage (largest effect)
- **0.8 ≤ d < 0.9**: +1.4pp to +26.1pp
- **0.9 ≤ d < 0.95**: −0.7pp to +16.4pp
- **d ≥ 0.95**: −1.6pp to +2.6pp (negligible)

This confirms the hypothesis: the 4PL upper asymptote d captures ceiling effects in LLM response patterns. When items have d substantially below 1.0 (46% of MMLU, 51% of HumanEval), ignoring this parameter (3PL assumption d=1) causes model misspecification that reduces contamination detection sensitivity.

### 4. Practical implication

For LLM benchmark contamination detection, the 4PL parameterization is essential — not merely a refinement. The d parameter captures the empirical reality that many benchmark items have upper asymptotes well below 1.0, meaning even the most capable LLMs cannot achieve perfect accuracy on these items. Contamination detection methods that assume d=1 (standard 3PL) systematically underestimate the anomalousness of suspiciously correct responses on such items.