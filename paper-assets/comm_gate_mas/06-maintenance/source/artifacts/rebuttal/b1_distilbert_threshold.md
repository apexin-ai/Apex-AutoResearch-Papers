# DistilBERT Confidence Threshold Sensitivity

| Threshold | Baseline Acc | Pruned Acc | Delta (pp) | Suppress % |
|-----------|-------------|------------|------------|------------|
| 0.3 | 83.67% | 82.33% | -1.34 | 0.0% |
| 0.4 | 83.67% | 82.67% | -1.00 | 0.0% |
| 0.5 | 81.67% | 81.33% | -0.34 | 0.0% |
| 0.6 | 81.00% | 81.67% | +0.67 | 0.0% |
| 0.7 | 81.33% | 81.67% | +0.34 | 0.0% |

Delta range: 2.01pp across thresholds [0.3-0.7]

**Rebuttal conclusion**: DistilBERT classifier pruning is robust to confidence threshold (accuracy delta varies by 2.01pp across threshold range [0.3-0.7]).
