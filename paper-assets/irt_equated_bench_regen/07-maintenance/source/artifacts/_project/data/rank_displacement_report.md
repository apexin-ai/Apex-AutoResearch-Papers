# Rank Displacement by ETS Threshold

Models: 5227, Items: 12508, Random trials: 20

## Results

| Threshold | Flagged | % | Avg Disp | Max Disp | Flip Rate | Rand Avg Disp | Rand Flip | Z (Disp) | Z (Flip) |
|-----------|---------|---|----------|----------|-----------|---------------|-----------|----------|----------|
| 1.0 | 6120 | 48.9% | 80.8 | 1003 | 0.0216 | 54.1 | 0.0142 | 3.9 | 4.1 |
| 1.5 | 3918 | 31.3% | 74.7 | 847 | 0.0200 | 35.5 | 0.0093 | 18.7 | 18.7 |
| 2.0 | 2294 | 18.3% | 60.6 | 834 | 0.0161 | 26.5 | 0.0068 | 13.1 | 13.9 |
| 2.5 | 1278 | 10.2% | 54.7 | 789 | 0.0141 | 19.8 | 0.0050 | 18.4 | 17.6 |

## Interpretation

- **Avg Disp**: mean absolute rank change per model after removing C-flagged items
- **Flip Rate**: fraction of model pairs whose relative ordering changes (from Kendall tau)
- **Z-score**: how many SDs the DIF-based removal exceeds random removal of equal count
- Z > 2 indicates DIF-flagged items cause significantly more ranking instability than random items
