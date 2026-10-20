# RE Non-zero F1 Conditional Selection (n=397 RE Basis)

## Data
- Source: `exp_012_rerun_1024/samples.jsonl` (Qwen SciERC joint N=8 seed=42 max_tokens=1024)
- Total instances: 551
- **RE basis (gold relations > 0): 397** ✓

## Subset Breakdown (within n=397)

| Subset | n | % |
|--------|---|---|
| Non-zero greedy RE F1 | 238 | 59.9% |
| Zero greedy RE F1 | 159 | 40.1% |
| Zero subset with oracle > 0 | 76/159 | 47.8% |

## Non-zero Greedy RE F1 Subset (n=238)

Greedy RE F1: **0.6743** | Oracle RE F1: **0.7574**

| Signal | Selected F1 | Gain vs Greedy | p-value |
|--------|------------|----------------|---------|
| LP | 0.5995 | -0.0748 | 1.000 |
| FK | 0.6063 | -0.0680 | 1.000 |
| SJ | 0.6035 | -0.0708 | 1.000 |
| VC | 0.5737 | -0.1005 | 1.000 |
| EM | 0.5828 | -0.0914 | 1.000 |

**All 5 signals perform worse than greedy** on the non-zero subset. No signal achieves positive selection gain (p=1.0 for all).

## Full RE Basis (n=397)

Greedy RE F1: **0.4042** | Oracle RE F1: **0.5850**

| Signal | Selected F1 | Gain vs Greedy | p-value |
|--------|------------|----------------|---------|
| LP | 0.3948 | -0.0094 | 1.000 |
| FK | 0.3872 | -0.0171 | 1.000 |
| SJ | 0.3855 | -0.0188 | 1.000 |
| VC | 0.3592 | -0.0451 | 1.000 |
| EM | 0.3718 | -0.0324 | 1.000 |

**All 5 signals also negative on full n=397.** Gains are smaller in magnitude than the non-zero subset because the zero-greedy instances (where signals can only improve) dilute the negative signal.

## Zero Greedy RE F1 Subset (n=159)

Greedy RE F1: **0.0000** | Oracle RE F1: **0.3270**

| Signal | Selected F1 | Gain vs Greedy | p-value |
|--------|------------|----------------|---------|
| LP | 0.0884 | +0.0884 | 0.000* |
| FK | 0.0591 | +0.0591 | 0.000* |
| SJ | 0.0591 | +0.0591 | 0.000* |
| VC | 0.0380 | +0.0380 | 0.008* |
| EM | 0.0560 | +0.0560 | 0.001* |

All signals significant (trivially, since greedy=0 and any non-zero selection is positive).

## Key Takeaways

1. **On instances where greedy already extracts some correct relations (n=238), no consistency signal can beat greedy for RE.** All signals select worse samples, with losses of 7-10 F1 points.
2. **On full n=397**, the net effect is still negative for all signals. The gains from the zero subset are overwhelmed by losses on the non-zero subset.
3. **Oracle gap is large** (greedy 0.4042 → oracle 0.5850 on n=397), confirming that better samples exist in the N=8 pool — the signals just can't find them for RE.
4. **LP is the least harmful** signal on both subsets (smallest negative gain), consistent with it being the best single signal for RE overall.

## Artifacts
- Script: `output/review_round4/analyze_re_nonzero_selection.py`
- JSON results: `output/review_round4/re_nonzero_results_n397.json`
