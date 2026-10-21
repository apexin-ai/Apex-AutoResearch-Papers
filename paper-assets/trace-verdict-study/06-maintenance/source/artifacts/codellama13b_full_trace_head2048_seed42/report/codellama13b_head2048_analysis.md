# CodeLlama-13B Head-2048 Experiment Analysis

## Result
- **Accuracy: 79.92%** (95% CI: 77.6% - 82.3%)
- Majority baseline: 71.51%
- Lift: +8.4pp

## Per-class Metrics
| Class | Precision | Recall | F1 |
|-------|-----------|--------|------|
| pass | 0.857 | 0.864 | 0.860 |
| fail | 0.651 | 0.637 | 0.644 |

## Training Details
- train_loss: 0.0452, eval_loss: 0.111 (epoch 3)
- 444 steps, 3 epochs, ~3.7 GPU hours
- n_test: 1190

## Hypothesis Verification
Accuracy 79.92% falls within the predicted 75-82% band. **Hypothesis confirmed.**

## Cross-model Head-2048 Comparison (updated)
| Model | head-2048 | tail-2048 | Gap |
|-------|-----------|-----------|-----|
| Qwen-7B | 81.76% | 97.3% | 15.5pp |
| CodeLlama-13B | **79.92%** | ? | ? |
| DeepSeek-6.7B | 78.7% | 94.96% | 16.3pp |
| Qwen-1.5B | 75.29% | 97.90% | 22.6pp |

All 4 models cluster tightly in the 75-82% range for head-2048, confirming that head truncation captures limited diagnostic signal regardless of model architecture or scale. The signal positional concentration pattern is robust across model families.
