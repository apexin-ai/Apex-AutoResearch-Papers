# deepseek_ae_only_seed123 Analysis

## Eval Metrics

| Metric | Value | 95% CI |
|--------|-------|--------|
| **Accuracy** | **98.32%** | [97.56%, 98.99%] |
| Majority baseline | 71.51% | [69.16%, 73.87%] |
| Lift over majority | +26.81pp | [+24.37pp, +29.24pp] |
| Pass Precision | 0.9837 | [0.9748, 0.9919] |
| Pass Recall | 0.9929 | [0.9871, 0.9977] |
| Pass F1 | 0.9883 | [0.9827, 0.9932] |
| **Fail Precision** | **0.9819** | [0.9672, 0.9943] |
| **Fail Recall** | **0.9587** | [0.9362, 0.9785] |
| **Fail F1** | **0.9701** | [0.9560, 0.9829] |
| N | 1190 | - |

## Training Summary

| Metric | Value |
|--------|-------|
| Train loss (final) | 0.0702 |
| Eval loss (epoch 2) | 0.1648 |
| Eval loss (epoch 3) | 0.1907 |
| Train runtime | 8844s (~2h 27m) |
| Epochs | 3 |
| Total steps | 444 |

Eval loss increased from epoch 2 to 3 (0.1648 → 0.1907), mild overfitting in final epoch.

## Cross-seed Comparison (DeepSeek ae_only)

| Seed | Accuracy | Fail F1 | Fail Recall |
|------|----------|---------|-------------|
| seed42 | 98.74% | 0.977 | 0.959 |
| seed123 | 98.32% | 0.970 | 0.959 |
| **Diff** | **-0.42pp** | **-0.007** | **0.000** |

Delta within CI overlap. Cross-seed variance is low (~0.3% std).

## Cross-model Comparison (ae_only condition)

| Model | Mean Accuracy | Seeds |
|-------|---------------|-------|
| Qwen-7B | 99.64% ± 0.49% | 42, 123 |
| Qwen-1.5B | 99.08% | 42 only |
| CodeLlama-13B | 99.08% ± 0.00% | 42, 123 |
| **DeepSeek-6.7B** | **98.53% ± 0.30%** | **42, 123** |

DeepSeek ae_only is the lowest among all models but still comfortably above 98% threshold. All models confirm ae_only as Tier 1 (near-ceiling accuracy).

## Checkpoint

- Path: `/root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_ae_only_seed123/final/`
- Adapter: `adapter_model.safetensors` (153M)
- Files: adapter_config.json, tokenizer, training_args.bin, eval_results.json, predictions.jsonl
- Status: complete

## Conclusion: **SUCCESS**

98.32% accuracy exceeds the 98% threshold. Cross-seed consistency confirmed (0.42pp delta with seed42). ae_only remains Tier 1 across all four model scales.
