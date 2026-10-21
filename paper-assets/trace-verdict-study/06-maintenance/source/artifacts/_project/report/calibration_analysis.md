# Cross-Model Calibration Analysis (exception_only)

## Method

- **Condition**: exception_only (n=1190 test samples)
- **Metric extraction**: Forward pass through each model (base + LoRA adapter), extracting logits for "pass" and "fail" tokens at the last position, then softmax over the two classes
- **ECE**: 10-bin Expected Calibration Error (weighted average of |avg_confidence − avg_accuracy| per bin)
- **Brier Score**: mean((P(pass) − y)²) where y∈{0,1}

## Results

| Model | Accuracy | ECE ↓ | Brier Score ↓ | Mean Confidence |
|---|---|---|---|---|
| Qwen2.5-7B | 99.83% | 0.0017 | 0.0013 | 99.80% |
| DeepSeek-Coder-7B | 99.33% | 0.0048 | 0.0059 | 99.71% |
| CodeLlama-13B | 99.83% | 0.0020 | 0.0013 | 99.63% |
| Qwen2.5-1.5B | 99.83% | 0.0014 | 0.0013 | 99.82% |

## Key Observations

1. **All models are extremely well-calibrated** on exception_only. ECE ranges from 0.0014 (Qwen2.5-1.5B) to 0.0048 (DeepSeek-Coder-7B). For reference, ECE < 0.05 is generally considered well-calibrated.

2. **DeepSeek-Coder-7B is the least calibrated** with ECE 0.0048 and Brier 0.0059, consistent with it having the lowest accuracy (99.33%). It shows slight overconfidence: mean confidence 99.71% vs actual accuracy 99.33%.

3. **Qwen2.5-1.5B has the best calibration** despite being the smallest model (1.5B params). ECE=0.0014, Brier=0.0013, and mean confidence (99.82%) is very close to actual accuracy (99.83%).

4. **Calibration differences are marginal** across all 4 models. The task (exception_only) appears nearly saturated, leaving little room for miscalibration. Near-perfect accuracy with near-certainty is intrinsically well-calibrated.

## Data Source

- JSON results: `/root/trace-verdict-study/outputs/calibration_results.json`
- Script: `/root/trace-verdict-study/eval/calibration_eval.py`
- All predictions recomputed via forward-pass logit extraction (not from cached predictions)
