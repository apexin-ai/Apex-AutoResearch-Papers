# Commitment Point Distribution Analysis

## Dataset Summary (r1-8b subset)

| Category | Count |
|----------|-------|
| Jailbreak with commitment point | 209 |
| Jailbreak without commitment point | 56 |
| Safe traces | 59 |
| **Coverage** | **78.9%** (209/265) |

## Commitment Point Statistics

| Metric | Value |
|--------|-------|
| Mean (absolute step) | 34.4 |
| Median (absolute step) | 34.0 |
| Std | 21.0 |
| Min | 1 |
| Max | 93 |
| Relative position (mean) | 70.5% |
| Relative position (median) | 86.1% |
| Relative position (std) | 32.0% |

## Relative Position Distribution

| Bucket | Count | Percentage |
|--------|-------|-----------|
| [0%-25%) | 38 | 18.2% |
| [25%-50%) | 6 | 2.9% |
| [50%-75%) | 32 | 15.3% |
| [75%-90%) | 46 | 22.0% |
| [90%-100%) | 87 | 41.6% |

## Step Label Balance

- Pre-commitment steps: 7,199 (74.5%)
- Post-commitment steps: 2,468 (25.5%)

## Data Split

- Train: 125 traces
- Val: 41 traces
- Test: 43 traces
- Avg trace length (with CP): 46.3 steps

## Key Observations

1. **Coverage > 70% confirmed**: 78.9% of jailbreak traces have a valid commitment point.
2. **Bimodal distribution**: CP clusters in early ([0-25%): 18.2%) and late ([90-100%): 41.6%) positions. The middle range is sparse.
3. **44% of traces have CP in last 5 steps** — for these, temporal probe detection lead time will be minimal. The remaining 56% provide meaningful runway for early detection.
4. **Class imbalance**: 74.5% pre vs 25.5% post — may need class weighting or focal loss during probe training.
5. **Median relative position (86.1%) vs mean (70.5%)**: the mean is pulled down by the 18.2% of traces with very early CPs (likely traces where the model abandons safety reasoning almost immediately).
