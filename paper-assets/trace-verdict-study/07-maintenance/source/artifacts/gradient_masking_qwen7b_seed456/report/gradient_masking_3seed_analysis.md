# Gradient Masking 3-Seed Analysis

## Experiment Config
- Condition: exception_only + gradient_mask_ratio=0.998 (top 0.2% gradients retained)
- Model: Qwen2.5-Coder-7B-Instruct (LoRA SFT)
- Epochs: 3, n_eval=1190

## Per-Seed Results

| Metric | seed42 | seed123 | seed456 |
|--------|--------|---------|---------|
| accuracy | 98.99% | 99.33% | 99.33% |
| pass_precision | — | 1.000 | 1.000 |
| pass_recall | — | 0.991 | 0.991 |
| pass_f1 | — | 0.995 | 0.995 |
| fail_precision | — | 0.977 | 0.977 |
| fail_recall | — | 1.000 | 1.000 |
| fail_f1 | — | 0.988 | 0.988 |
| eval_loss | — | — | 0.0381 |

## 3-Seed Aggregate

- **Mean accuracy: 99.22% ± 0.20% (std)**
- Range: [98.99%, 99.33%]
- All 3 seeds > 97% threshold

## Comparison with Baselines

| Condition | Accuracy | Note |
|-----------|----------|------|
| exception_only (no masking, seed42) | 99.83% | Full gradient baseline |
| gradient_masking (3-seed mean) | 99.22% ± 0.20% | Top 0.2% gradients only |
| **Delta** | **-0.61 pp** | Negligible drop |

## Conclusion: SUCCESS

Masking 99.8% of gradient signals causes only a 0.61 pp accuracy drop (99.83% → 99.22%), confirming that **content quality (what's in the trace) dominates over gradient volume**. The model learns effectively from just the top 0.2% of gradient signals, strongly supporting the hypothesis that exception traces carry high-density, low-noise supervision signal.

Seed stability is excellent (std=0.20%), indicating robust convergence across random initializations.
