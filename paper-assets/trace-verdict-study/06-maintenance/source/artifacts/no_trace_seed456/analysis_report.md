# no_trace_seed456 Analysis Report

## Experiment Info
- **Condition**: no_trace (implicit pathway: terminal execution state only, no diagnostic tokens)
- **Seed**: 456
- **Base model**: Qwen2.5-Coder-7B-Instruct (LoRA r=16, alpha=32)
- **Training**: 444 steps, 3 epochs, train_loss=0.178
- **Status**: Completed successfully (EXIT_CODE=0)

## Evaluation Metrics (n=1190)

| Metric | Value | 95% CI |
|--------|-------|--------|
| **Accuracy** | **75.04%** | [72.35%, 77.48%] |
| Majority baseline | 71.51% | — |
| Lift | +3.53pp | [+0.34pp, +6.97pp] |
| Pass Precision | 0.8805 | [0.8573, 0.9026] |
| Pass Recall | 0.7532 | [0.7238, 0.7819] |
| Pass F1 | 0.8119 | [0.7894, 0.8326] |
| **Fail Precision** | **0.5455** | [0.5044, 0.5906] |
| **Fail Recall** | **0.7434** | [0.7000, 0.7875] |
| **Fail F1** | **0.6292** | [0.5921, 0.6691] |

## 3-Seed Comparison (Qwen-7B no_trace)

| Metric | seed42 | seed123 | seed456 | Mean | Std |
|--------|--------|---------|---------|------|-----|
| Accuracy | 75.13% | 79.08% | 75.04% | **76.41%** | **2.30%** |
| Fail F1 | 62.72% | 68.44% | 62.92% | **64.69%** | **3.25%** |
| Pass F1 | 81.34% | 84.35% | 81.19% | **82.29%** | **1.79%** |
| Fail Precision | 54.73% | 60.00% | 54.55% | **56.42%** | **3.11%** |
| Fail Recall | 73.45% | 79.65% | 74.34% | **75.81%** | **3.33%** |
| Pass Precision | 87.76% | 90.68% | 88.05% | **88.83%** | **1.61%** |
| Pass Recall | 75.79% | 78.85% | 75.32% | **76.65%** | **1.92%** |

## Paths
- **Log**: `~/runs/trace-verdict-study/no_trace_seed456.log`
- **Checkpoint**: `/root/autodl-tmp/trace-verdict-study-checkpoints/no_trace_seed456/final/`
- **Eval results**: `/root/autodl-tmp/trace-verdict-study-checkpoints/no_trace_seed456/final/eval_results.json`
- **Predictions**: `/root/autodl-tmp/trace-verdict-study-checkpoints/no_trace_seed456/final/predictions.jsonl`

## Observations

1. **seed456 closely replicates seed42**: accuracy (75.04% vs 75.13%) and fail_f1 (62.92% vs 62.72%) are nearly identical, suggesting seed42 is representative of typical no_trace performance.

2. **seed123 is an outlier**: accuracy 79.08% and fail_f1 68.44% are both ~4pp above the other two seeds. This inflates the mean and drives the relatively high std.

3. **Moderate variance**: accuracy std=2.30%, fail_f1 std=3.25%. The no_trace condition shows non-trivial seed sensitivity, with seed123 benefiting from a favorable random initialization.

4. **Lift remains marginal**: all three seeds have lift over majority baseline between +3.5pp and +7.6pp, confirming that the implicit pathway (no diagnostic tokens) struggles to substantially outperform the majority class predictor.

## Conclusion: SUCCESS

The 3-seed statistics are established. The no_trace condition achieves **76.41% +/- 2.30% accuracy** and **64.69% +/- 3.25% fail_f1**, confirming the implicit pathway performance ceiling for the Qwen-7B model.
