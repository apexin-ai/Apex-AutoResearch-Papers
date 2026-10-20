# Cross-Model Calibration Report (plan_019)

## Condition: exception_only
N = 1190 test samples per model

| Model | Accuracy | ECE | MCE | Brier Score | Mean Conf |
|-------|----------|-----|-----|-------------|-----------|
| Qwen-7B | 0.9983 | 0.0027 | 0.8355 | 0.0013 | 0.9980 |
| DeepSeek-6.7B | 0.9933 | 0.0049 | 0.4692 | 0.0059 | 0.9971 |
| CodeLlama-13B | 0.9983 | 0.0020 | 0.0411 | 0.0013 | 0.9963 |
| Qwen-1.5B | 0.9983 | 0.0020 | 0.7549 | 0.0013 | 0.9982 |

## Key Findings

1. **ECE universally low**: All 4 models achieve ECE < 0.005, indicating excellent calibration across architectures and scales (1.5B-13B).
2. **Brier scores minimal**: Range 0.0013-0.0059, confirming high predictive quality.
3. **MCE inflated by sparse bins**: High MCE values (e.g., Qwen-7B 0.84, Qwen-1.5B 0.75) stem from 1-2 samples in low-confidence bins where individual misclassifications dominate. Not practically meaningful.
4. **DeepSeek slight outlier**: Higher ECE (0.0049) and Brier (0.0059) vs others, consistent with its slightly lower accuracy (99.33% vs 99.83%).
5. **CodeLlama best calibrated**: Lowest MCE (0.041) because its few uncertain samples cluster in the 0.7-0.75 bin (8 samples, 75% acc), avoiding extreme single-sample gaps.

## Reliability Distribution

Nearly all predictions (>99%) fall in the (0.95, 1.0] confidence bin with 100% accuracy — models are very confident and very correct on exception_only.
