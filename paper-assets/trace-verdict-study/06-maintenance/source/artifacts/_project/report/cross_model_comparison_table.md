# Cross-Model Comparison: 4 Models x 4 Conditions

## Results Table (Accuracy %)

| Model | Params | no_trace | full_trace | exception_only | vota |
|-------|--------|----------|------------|----------------|------|
| Qwen-1.5B | 1.5B | 67.31 | 77.06 | 99.83 | 99.58 |
| DeepSeek-Coder | 6.7B | 73.36 | 79.16 | 99.33 | 84.45* |
| Qwen-2.5 | 7B | 75.13 | 81.76 | 99.83 | 99.41 |
| CodeLlama | 13B | 76.50 | N/A | 99.83 | 98.57 |

\* DeepSeek VOTA impacted by training-time truncation (max_length=2048 insufficient for VoTA traces with 6.7B tokenizer). Intact samples achieve 100% accuracy.

## CSV Format

```csv
model,params_B,no_trace,full_trace,exception_only,vota
Qwen-1.5B,1.5,67.31,77.06,99.83,99.58
DeepSeek-Coder-6.7B,6.7,73.36,79.16,99.33,84.45
Qwen-2.5-7B,7,75.13,81.76,99.83,99.41
CodeLlama-13B,13,76.50,,99.83,98.57
```

## Scale Monotonicity Analysis

### no_trace condition: Model size vs. accuracy

| Model | Params | Accuracy | Delta from previous |
|-------|--------|----------|---------------------|
| Qwen-1.5B | 1.5B | 67.31% | — |
| DeepSeek-Coder | 6.7B | 73.36% | +6.05 |
| Qwen-2.5 | 7B | 75.13% | +1.77 |
| CodeLlama | 13B | 76.50% | +1.37 |

**Finding**: Strict monotonic relationship confirmed — 1.5B < 6.7B < 7B < 13B. Larger models are consistently better at verdict classification without trace information. The marginal gain diminishes with scale (6.05 -> 1.77 -> 1.37), suggesting diminishing returns from model capacity alone.

### exception_only condition: Scale-invariance test

| Model | Params | Accuracy | Errors (out of 1190) |
|-------|--------|----------|---------------------|
| DeepSeek-Coder | 6.7B | 99.33% | 8 |
| Qwen-1.5B | 1.5B | 99.83% | 2 |
| Qwen-2.5 | 7B | 99.83% | 2 |
| CodeLlama | 13B | 99.83% | 2 |

**Finding**: Scale-invariant. All models achieve >= 99.33% with exception_only traces, regardless of parameter count. Even the smallest model (1.5B) matches the largest (13B) at 99.83%. This confirms that exception traces provide sufficient signal for near-perfect classification — the task becomes trivial once the right information is present.

## Key Insights

1. **Information > Scale**: The gap between no_trace and exception_only (22-33 pp) dwarfs the gap between the smallest and largest model within no_trace (9.19 pp). Providing the right trace information matters far more than model capacity.

2. **VoTA robustness varies by architecture**: 3/4 models achieve >98.5% with VoTA, but DeepSeek's 84.45% is an outlier caused by tokenizer-specific truncation during training (not a fundamental limitation of the method).

3. **Practical ceiling**: exception_only achieves the same ~99.83% accuracy across model families and sizes, establishing this as the effective performance ceiling for the verdict classification task.

4. **full_trace provides modest gains over no_trace**: +5.8 to +10.0 pp depending on model — useful but far below the exception_only shortcut.
