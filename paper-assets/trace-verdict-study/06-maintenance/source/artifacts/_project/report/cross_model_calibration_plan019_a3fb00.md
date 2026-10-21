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
1. ECE universally low (< 0.005) across 4 architectures/scales
2. Brier scores minimal (0.0013-0.0059)
3. MCE inflated by sparse bins (1-2 samples), not practically meaningful
4. DeepSeek slight outlier (higher ECE/Brier), consistent with 99.33% vs 99.83% accuracy
5. CodeLlama best calibrated (lowest MCE 0.041)

Remote paths:
- JSON: /root/trace-verdict-study/artifacts/cross_model_calibration_plan019.json
- MD: /root/trace-verdict-study/artifacts/cross_model_calibration_plan019.md