# Experiment Analysis: qwen15b_full_trace_tail1024_seed42

## Configuration
- **Model**: Qwen2.5-Coder-1.5B-Instruct (LoRA)
- **Condition**: full_trace_tail_1024
- **Seed**: 42
- **Train samples**: 4720 | **Test samples**: 1190
- **Epochs**: 3 | **Steps**: 444
- **Training time**: ~17.5 min

## Core Metrics

| Metric | Value |
|--------|-------|
| **Accuracy** | **96.6%** |
| **95% CI** | **[95.5%, 97.6%]** |
| Majority baseline | 71.5% (always predict 'pass') |
| Lift over majority | +25.0pp |
| Train loss | 0.1187 |
| Eval loss | 0.1983 |
| Eval mean token accuracy | 0.9604 |

## Per-class Metrics

| Class | Precision | Recall | F1 |
|-------|-----------|--------|-----|
| pass | 0.964 [0.951, 0.976] | 0.988 [0.981, 0.995] | 0.976 [0.969, 0.983] |
| fail | 0.969 [0.949, 0.987] | 0.909 [0.875, 0.938] | 0.938 [0.917, 0.957] |

## Comparison with Baselines

| Experiment | Accuracy | 95% CI |
|------------|----------|--------|
| **Qwen-1.5B tail-1024 (this)** | **96.6%** | **[95.5%, 97.6%]** |
| Qwen-1.5B tail-512 | 95.6% | [94.5%, 96.8%] |
| Qwen-1.5B tail-256 | 72.6% | (approx majority baseline) |
| Qwen-7B tail-2048 | 97.3% | - |
| Qwen-7B tail-1024 | 96.47% | - |
| Qwen-7B tail-512 | 93.61% | - |
| DeepSeek tail-512 | 93.9% | - |

### 1.5B Truncation Length Scaling
- tail-256: 72.6% (no learning)
- tail-512: 95.6%
- tail-1024: 96.6% (+1.0pp over tail-512)

### Cross-model Comparison at tail-1024
- Qwen-1.5B: 96.6%
- Qwen-7B: 96.47%
- Essentially identical performance at this context length.

## Hypothesis Evaluation

**Hypothesis**: "1.5B tail-1024 may be lower than tail-512 (95.6%), confirming non-monotonicity in smaller models due to noisy intermediate states in medium-length traces."

**Verdict: REJECTED**

tail-1024 (96.6%) is +1.0pp HIGHER than tail-512 (95.6%). The CIs overlap ([95.5%, 97.6%] vs [94.5%, 96.8%]), so the difference is not statistically significant, but the direction is monotonically improving (more context = equal or better performance).

The 1.5B model shows monotonic improvement with context length: tail-256 (72.6%) << tail-512 (95.6%) < tail-1024 (96.6%). Non-monotonicity is NOT observed.

Notable: the 1.5B tail-1024 (96.6%) matches the 7B tail-1024 (96.47%), suggesting that at this context length, model size provides no additional benefit.

## Conclusion

**Status: SUCCESS** (strong positive result)

The experiment yields two findings:
1. Longer context is monotonically beneficial for 1.5B (no non-monotonicity), rejecting the hypothesis that noisy intermediate states degrade performance.
2. 1.5B achieves parity with 7B at tail-1024, indicating diminishing returns from model scale when sufficient trace context is provided.

The 1.5B scaling curve (tail-256 -> tail-512 -> tail-1024) shows a saturation pattern approaching ~97%, suggesting that tail-1024 captures most of the useful signal in execution traces for this task.

## Paths
- **Checkpoint**: `/root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_full_trace_tail1024_seed42/final`
- **Log**: `/root/trace-verdict-study/logs/qwen15b_tail1024_seed42.log`
- **Predictions**: `/root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_full_trace_tail1024_seed42/final/predictions.jsonl`
- **Eval results**: `/root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_full_trace_tail1024_seed42/final/eval_results.json`
