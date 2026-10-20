# Experiment Analysis: deepseek_full_trace_tail1024_seed42

## Core Metrics

| Metric | Value |
|--------|-------|
| Accuracy | 96.47% |
| 95% CI | [95.4%, 97.5%] |
| Majority baseline | 71.5% (always predict 'pass') |
| Lift over majority | +25.0pp |
| Train loss | 0.0999 |
| Eval loss (epoch 2) | 0.1450 |
| Eval loss (epoch 3) | 0.1694 |
| Total steps | 444 (3 epochs) |
| Training time | ~1h 37min |

### Per-class Metrics

| Class | Precision | Recall | F1 |
|-------|-----------|--------|-----|
| pass | 0.964 [0.951, 0.976] | 0.987 [0.979, 0.994] | 0.976 [0.968, 0.983] |
| fail | 0.966 [0.945, 0.984] | 0.909 [0.875, 0.938] | 0.936 [0.917, 0.955] |

## Comparison with Baselines

| Condition | Accuracy | 95% CI |
|-----------|----------|--------|
| DeepSeek tail-2048 | ~97.0% | - |
| **DeepSeek tail-1024** | **96.47%** | **[95.4%, 97.5%]** |
| DeepSeek tail-512 | 93.9% | [92.6%, 95.3%] |
| DeepSeek tail-256 | 76.4% | - |
| Qwen-7B tail-1024 | 96.47% | - |
| Qwen-7B tail-512 | 93.61% | - |

## Hypothesis Judgment

**Hypothesis**: "DeepSeek tail-1024 may be lower than tail-512 (as with Qwen-7B non-monotonicity), because 1024 tokens include noisy intermediate states; if non-monotonicity also appears, it confirms cross-architecture."

**Verdict: REJECTED**

DeepSeek tail-1024 achieves 96.47%, which is **2.57pp higher** than tail-512 (93.9%). The CI lower bound of tail-1024 (95.4%) exceeds the CI upper bound of tail-512 (95.3%), confirming a statistically significant improvement.

The truncation curve for DeepSeek is monotonically increasing:
- tail-256 (76.4%) < tail-512 (93.9%) < tail-1024 (96.47%) < tail-2048 (~97.0%)

Non-monotonicity is NOT confirmed cross-architecture. DeepSeek benefits monotonically from longer context, unlike the Qwen-7B pattern.

Interestingly, DeepSeek tail-1024 (96.47%) matches Qwen-7B tail-1024 (96.47%) exactly, suggesting a performance ceiling around this accuracy level for 1024-token traces regardless of architecture.

## Conclusion

**Result: SUCCESS (positive result, hypothesis rejected)**

The experiment provides clear evidence that tail-truncation performance is monotonic for DeepSeek-Coder-6.7B. The non-monotonicity observed in Qwen-7B is architecture-specific, not a universal property of trace truncation.

## Paths

- **Checkpoint**: `/root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_full_trace_tail1024_seed42/final`
- **Log**: `/root/runs/trace-verdict-study/deepseek_full_trace_tail1024_seed42.log`
- **Predictions**: `/root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_full_trace_tail1024_seed42/final/predictions.jsonl`
- **Eval results JSON**: `/root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_full_trace_tail1024_seed42/final/eval_results.json`
