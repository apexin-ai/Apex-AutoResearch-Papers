# Experiment Analysis: deepseek_gradient_masking_seed42

## Experiment Setup

| Field | Value |
|-------|-------|
| **exp_id** | deepseek_gradient_masking_seed42 |
| **Model** | deepseek-ai/deepseek-coder-6.7b-instruct |
| **Condition** | exception_only |
| **Gradient mask ratio** | 0.998 (keep 0.2% of trace tokens) |
| **Seed** | 42 |
| **Train samples** | 4,720 |
| **Eval samples** | 1,190 |
| **Training steps** | 444 (3 epochs) |
| **Training time** | 1h 43min (6,205s) |
| **Checkpoint** | /root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_gradient_masking_seed42/final |

## Core Metrics

| Metric | Value |
|--------|-------|
| **Accuracy** | **99.33%** (95% CI: [98.8%, 99.7%]) |
| Majority baseline | 71.5% |
| Lift over majority | +27.8pp |
| eval_loss (epoch 3) | 0.0529 |
| train_loss | 0.9961 |

### Per-class Metrics

| Class | Precision | Recall | F1 |
|-------|-----------|--------|----|
| pass | 1.00 | 0.99 | 1.00 |
| fail | 0.98 | 1.00 | 0.99 |

## Comparison with DeepSeek Baseline (no gradient masking)

| Experiment | Accuracy | Dilution |
|-----------|----------|----------|
| DeepSeek exception_only seed42 (baseline) | 99.33% | — |
| DeepSeek exception_only seed123 (baseline) | 99.50% | — |
| DeepSeek exception_only seed456 (baseline) | 99.33% | — |
| **Baseline mean** | **99.39%** | — |
| **DeepSeek gradient_masking seed42** | **99.33%** | **0.06%** |

Dilution = baseline_mean − masked_accuracy = 99.39% − 99.33% = **0.06%**

This is essentially zero and well within the ≤4% bound.

## Cross-Architecture Comparison (Gradient Masking)

| Architecture | Gradient Masking Accuracy | Baseline Mean | Dilution |
|-------------|--------------------------|---------------|----------|
| Qwen-7B seed42 | 99.33% | 99.33% | 0.00% |
| Qwen-7B seed123 | 99.33% | 99.33% | 0.00% |
| Qwen-7B seed456 | 99.33% | 99.33% | 0.00% |
| **DeepSeek-6.7B seed42** | **99.33%** | **99.39%** | **0.06%** |

All architectures show negligible dilution (≤0.06%) under 99.8% gradient masking, confirming the result is architecture-independent.

## Conclusion: **SUCCESS**

- **Accuracy 99.33% ≥ 98.5% threshold** → hypothesis confirmed
- **Dilution 0.06% ≤ 4% bound** → gradient masking has no meaningful impact on performance
- **Cross-architecture validation**: DeepSeek-6.7B replicates the Qwen-7B finding that 99.8% gradient masking preserves full classification accuracy
- **Implication**: The degradation observed with full_trace conditions is explained by content quality (noise/irrelevance in trace tokens), not by gradient dilution from trace token gradients. This holds across both Qwen-7B and DeepSeek-6.7B architectures.
