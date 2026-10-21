# Experiment Analysis: qwen15b_ae_only_seed42

## Summary

| Field | Value |
|-------|-------|
| Model | Qwen2.5-Coder-1.5B-Instruct |
| Condition | ae_only |
| Seed | 42 |
| Server | westd-11235 |
| Training | 3 epochs, 444 steps, 52 min |
| Test samples | 1190 |
| Conclusion | **SUCCESS** |

## Metrics

| Metric | Value | 95% CI |
|--------|-------|--------|
| **Accuracy** | **99.08%** | [98.49%, 99.58%] |
| Majority baseline | 71.51% | [69.16%, 73.87%] |
| Lift over baseline | +27.56pp | [+25.13pp, +30.17pp] |
| Train loss | 0.0702 | — |
| Eval loss | 0.1973 | — |

### Per-class Metrics

| Class | Precision | Recall | F1 |
|-------|-----------|--------|----|
| pass | 1.000 | 0.987 | 0.994 |
| fail | 0.969 | 1.000 | 0.984 |

## Cross-model Comparison (ae_only condition)

| Model | Params | Accuracy | Pass F1 | Fail F1 |
|-------|--------|----------|---------|---------|
| Qwen-7B | 7B | 99.92% | — | — |
| CodeLlama-13B (seed42) | 13B | 99.08% | — | — |
| CodeLlama-13B (seed123) | 13B | 99.25% | — | — |
| DeepSeek | — | 98.74% | — | — |
| **Qwen-1.5B (this)** | **1.5B** | **99.08%** | **0.994** | **0.984** |

## Cross-condition Comparison (Qwen-1.5B)

| Condition | Accuracy |
|-----------|----------|
| exception_only | 99.83% |
| **ae_only** | **99.08%** |

## Analysis

1. **Hypothesis confirmed**: Qwen-1.5B achieves 99.08% accuracy on ae_only, well above the 95% threshold. Tier 1 ae_only remains effective even at the smallest scale tested (1.5B).

2. **Scale-invariance**: The 1.5B model matches the 13B CodeLlama (99.08%) exactly, and trails the 7B Qwen by only 0.84pp. The ae_only signal is robust across 1.5B–13B.

3. **Error pattern**: Perfect fail recall (1.000) with slightly lower pass recall (0.987) — the model never misses a failure, but occasionally misclassifies a passing trace as fail. This is the preferred error direction for CI/testing use cases.

4. **vs exception_only**: ae_only (99.08%) is 0.75pp below exception_only (99.83%) on the same 1.5B model. Both are in the ceiling region; the gap is within CI overlap.

## Artifacts

- Checkpoint: `/root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_ae_only_seed42/final`
- Log: `~/runs/trace-verdict-study/qwen15b_ae_only_seed42.log`
- Predictions: `/root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_ae_only_seed42/final/predictions.jsonl`
- Eval results: `/root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_ae_only_seed42/final/eval_results.json`
