# Cross-Model Calibration Analysis (plan_019)

## Results Summary

| Model | Params | Accuracy | ECE | MCE | Brier Score | Mean Conf |
|-------|--------|----------|-----|-----|-------------|-----------|
| Qwen2.5-7B | 7B | 99.83% | 0.0027 | 0.8355* | 0.0013 | 0.9980 |
| DeepSeek-6.7B | 6.7B | 99.33% | 0.0049 | 0.4692* | 0.0059 | 0.9971 |
| CodeLlama-13B | 13B | 99.83% | 0.0020 | 0.0411 | 0.0013 | 0.9963 |
| Qwen2.5-1.5B | 1.5B | 99.83% | 0.0020 | 0.7549* | 0.0013 | 0.9982 |

*MCE inflated by single-sample bins.

## Key Findings

1. **ECE universally low**: All 4 models achieve ECE < 0.005 (3 of 4 below 0.003). Exception signal produces well-calibrated models regardless of architecture or size (1.5B–13B).

2. **MCE misleading**: High MCE driven by 1–2 samples in sparse low-confidence bins. CodeLlama-13B (MCE=0.041) has meaningful bin sizes; others have single-sample noise.

3. **Brier scores near theoretical minimum**: 0.0013–0.0059. DeepSeek slightly higher due to more errors (8 vs 2).

4. **99.2%+ predictions** in [0.95, 1.0] confidence bin with 100% accuracy across all models.

5. **Cross-model ECE range (0.002–0.005)** matches single-model exception_only (0.003 from plan_007) and far exceeds no_trace (0.172).

## Conclusion
Exception-only calibration is architecture-agnostic. ECE < 0.005 for all 4 models confirms the signal provides reliable confidence regardless of model family or scale.