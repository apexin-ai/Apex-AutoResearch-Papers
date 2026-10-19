## D1 Layer Sweep — Static Probe Results

**Experiment**: diag_d1_layer_sweep
**Date**: 2026-05-16
**Data**: 209 jailbreak traces with commitment points
**Split**: 125 train / 41 val / 43 test (trace-level, seed=42)
**Model**: LogisticRegression(C=1.0, max_iter=1000, class_weight='balanced')

### Results Table

| Idx | Layer | Step Acc | F1     | Cross Rate | Lead Mean | Lead Median |
|-----|-------|----------|--------|------------|-----------|-------------|
| 0   | 12    | 0.8033   | 0.6379 | 0.3023     | 6.46      | 6.00        |
| 1   | 13    | 0.8082   | 0.6452 | 0.3023     | 8.85      | 8.00        |
| 2   | 14    | 0.8114   | 0.6455 | 0.1860     | 8.38      | 6.00        |
| 3   | 15    | 0.7869   | 0.6086 | 0.2326     | 13.50     | 7.00        |
| 4   | 16    | 0.8000   | 0.6236 | 0.2093     | 9.78      | 8.00        |
| 5   | 17    | 0.8054   | 0.6419 | 0.1860     | 6.38      | 5.00        |
| 6   | 18    | 0.7978   | 0.6256 | 0.2093     | 8.67      | 5.00        |
| 7   | 19    | 0.7924   | 0.6340 | 0.3023     | 8.00      | 6.00        |
| 8   | 20    | 0.7831   | 0.6202 | 0.2791     | 10.00     | 6.50        |
| 9   | 21    | 0.7946   | 0.6357 | 0.3023     | 11.38     | 5.00        |
| 10  | 22    | 0.7902   | 0.6323 | 0.3023     | 7.85      | 6.00        |
| 11  | 23    | 0.8044   | 0.6504 | 0.3256     | 8.07      | 6.00        |
| 12  | 24    | 0.7978   | 0.6366 | 0.2791     | 8.33      | 7.00        |

### Key Findings

- **Best layer**: 14 (index 2), accuracy = 0.8114, F1 = 0.6455
- **Default layer 20**: accuracy = 0.7831 (slightly below average)
- **Layer variance**: All layers between 78.3%-81.1% — very small spread (~3pp)
- **Crossing rate**: 19-33% of test traces have early crossing (k=5 consecutive)
- **Lead time**: When crossing detected, mean ~6-13 steps ahead of commitment

### Conclusion

**Signal MODERATE** — no layer exceeds 85% accuracy threshold. The commitment signal is present but weak with a simple linear probe. Layer choice matters little (~3pp range); the bottleneck is likely model capacity, not layer selection. Layer 14 is marginally best but the improvement over layer 20 is not significant (~2.8pp).

Implications:
1. A nonlinear or temporal probe may be needed to capture the commitment signal better
2. Multi-layer fusion could help (since different layers seem to capture slightly different aspects)
3. The 74.5%/25.5% class imbalance is handled by balanced weights but may still affect crossing detection
