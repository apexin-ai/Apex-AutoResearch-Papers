# Analysis: qwen15b_full_trace_tail1024_seed42

## Experiment Setup
- **Model**: Qwen2.5-Coder-1.5B-Instruct (LoRA)
- **Condition**: full_trace, truncation=tail, max_tokens=1024
- **Seed**: 42
- **Training**: 3 epochs, 444 steps, train_loss=0.1187
- **Test samples**: 1190

## Results

| Metric | Value |
|--------|-------|
| Accuracy | 96.6% (95% CI: 95.5%-97.6%) |
| Pass F1 | 0.98 (P=0.96, R=0.99) |
| Fail F1 | 0.94 (P=0.97, R=0.91) |
| Majority baseline | 71.5% |
| Lift over majority | +25.0pp |
| Eval loss | 0.1983 |
| Mean token accuracy | 96.04% |

## Cross-condition Comparison (Qwen-1.5B tail truncation)

| Condition | Accuracy | Fail F1 |
|-----------|----------|---------|
| tail-512 | 95.6% | — |
| **tail-1024** | **96.6%** | **0.94** |
| tail-2048 (full) | ~96.6% | — |

Monotonic improvement from tail-512 to tail-1024 (+1.0pp), then plateau at tail-2048.

## Cross-model Comparison (tail-1024)

| Model | Accuracy |
|-------|----------|
| **Qwen-1.5B** | **96.6%** |
| Qwen-7B | ~96.5% |
| DeepSeek | 96.47% |

Qwen-1.5B matches or slightly exceeds larger models at tail-1024.

## Hypothesis Verification

**Hypothesis**: "1.5B tail-1024 可能低于 tail-512 (95.6%), 如同 7B non-monotonicity; 因中等长度 trace 包含 noisy intermediate states"

**Result**: FALSIFIED. Accuracy is 96.6%, which is 1.0pp above tail-512 (95.6%). Qwen-1.5B does NOT exhibit the non-monotonic pattern hypothesized. The improvement from tail-512 to tail-1024 is monotonic, with diminishing returns beyond tail-1024 (plateau at tail-2048).

## Conclusion

**Success**. The experiment achieved 96.6% accuracy, consistent with the D066 corrected estimate. The 1.5B model shows monotonic context-length scaling for tail truncation, unlike the hypothesized non-monotonicity. This suggests the noisy-intermediate-states concern does not materialize for 1.5B models with tail truncation up to 1024 tokens.

## Paths
- Checkpoint: /root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_full_trace_tail1024_seed42/final
- Log: ~/runs/trace-verdict-study/qwen15b_full_trace_tail1024_seed42.log
- Predictions: /root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_full_trace_tail1024_seed42/final/predictions.jsonl
- Eval results: /root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_full_trace_tail1024_seed42/final/eval_results.json
