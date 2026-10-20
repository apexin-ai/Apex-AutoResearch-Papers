# Experiment Analysis: qwen15b_loop_only_seed123

## Experiment Info

| Field | Value |
|-------|-------|
| exp_id | qwen15b_loop_only_seed123 |
| model | Qwen2.5-Coder-1.5B-Instruct |
| condition | loop_only |
| seed | 123 |
| parent | qwen15b_loop_only_seed42 |
| server | westd-11235 |
| train_samples | 4,720 |
| test_samples | 1,190 |
| train_runtime | 2,659.7s (~44.3 min) |
| conclusion | **success** |

## Metrics

| Metric | seed123 | seed42 | delta |
|--------|---------|--------|-------|
| accuracy | **81.09%** | 78.32% | +2.77pp |
| pass_precision | 0.8366 | — | — |
| pass_recall | 0.9142 | — | — |
| pass_f1 | 0.8737 | 0.8526 | +0.0211 |
| fail_precision | 0.7192 | — | — |
| fail_recall | 0.5516 | — | — |
| fail_f1 | 0.6244 | 0.5905 | +0.0339 |
| train_loss | 0.0843 | — | — |
| majority_baseline | 71.51% | — | — |
| lift_over_majority | +9.58pp | — | — |

### 95% Bootstrap Confidence Intervals (seed123)

| Metric | Lower | Upper |
|--------|-------|-------|
| accuracy | 78.82% | 83.28% |
| pass_f1 | 0.8568 | 0.8894 |
| fail_f1 | 0.5763 | 0.6687 |

## Qwen-1.5B loop_only: 2-Seed Aggregation

| Metric | seed42 | seed123 | mean | std |
|--------|--------|---------|------|-----|
| accuracy | 78.32% | 81.09% | **79.71%** | ±1.96pp |
| pass_f1 | 0.8526 | 0.8737 | **0.8632** | ±0.0149 |
| fail_f1 | 0.5905 | 0.6244 | **0.6075** | ±0.0240 |

## Cross-Model Comparison (loop_only condition)

| Model | Seeds | Accuracy (mean±std) | fail_f1 |
|-------|-------|---------------------|---------|
| **Qwen-7B** | 3 | **86.05±0.52%** | — |
| DeepSeek | 2 | 81.26±0.00% | — |
| **Qwen-1.5B** | 2 | **79.71±1.96%** | 0.6075 |
| CodeLlama-13B | 2 | 76.56±0.71% | — |

### Observations

1. **Cross-seed stability**: seed123 (81.09%) vs seed42 (78.32%) differ by 2.77pp, within the ±5pp threshold. Hypothesis confirmed.
2. **Higher variance than 7B**: Qwen-1.5B std=1.96pp vs Qwen-7B std=0.52pp, suggesting smaller models are more sensitive to seed. A 3rd seed would better characterize this.
3. **Scale ordering preserved**: 7B (86.05%) > 1.5B (79.71%), a ~6.3pp gap on loop_only. However, 1.5B still outperforms CodeLlama-13B (76.56%), indicating Qwen architecture efficiency at smaller scales.
4. **Competitive with DeepSeek**: Qwen-1.5B (79.71%) is close to DeepSeek (81.26%), despite DeepSeek being a larger model, though the 1.5B variance is wider.
5. **fail_f1 improvement**: seed123 (0.6244) is notably better than seed42 (0.5905) on minority-class detection, driving the accuracy gain.
