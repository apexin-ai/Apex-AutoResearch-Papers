# Few-shot Baseline Summary

## Comparison with SFT Baselines

| Experiment | Model | Condition | Shots | Accuracy | P(fail) | R(fail) | F1(fail) | Errors |
|---|---|---|---|---|---|---|---|---|
| fewshot_gpt4o_exception_only_0shot | gpt-4o | exception_only | 0 | 87.98% | 70.94% | 97.94% | 82.28% | 0 |
| fewshot_gpt4o_exception_only_3shot | gpt-4o | exception_only | 3 | 86.81% | 70.50% | 92.33% | 79.95% | 0 |
| fewshot_gpt4o_no_trace_0shot | gpt-4o | no_trace | 0 | 84.45% | 68.60% | 83.78% | 75.43% | 0 |
| fewshot_gpt41_exception_only_0shot | gpt-4.1 | exception_only | 0 | 82.18% | 62.88% | 91.45% | 74.52% | 0 |
| fewshot_gpt41_exception_only_3shot | gpt-4.1 | exception_only | 3 | 81.93% | 62.60% | 90.86% | 74.13% | 0 |
| fewshot_gpt41_no_trace_0shot | gpt-4.1 | no_trace | 0 | 77.31% | 57.55% | 77.58% | 66.08% | 0 |

## SFT Baselines (Qwen-7B)

| Condition | Accuracy |
|---|---|
| exception_only | 99.83% |
| no_trace | 75.13% |

## Key Findings

1. **SFT dominates on exception_only**: SFT Qwen-7B (99.83%) >> best few-shot GPT-4o (87.98%), gap = 11.85pp
2. **Frontier LLM wins on no_trace**: GPT-4o (84.45%) > SFT Qwen-7B (75.13%), gap = +9.32pp
3. **GPT-4o > GPT-4.1** across all conditions (5-7pp gap)
4. **3-shot does not help** — slightly worse than 0-shot for both models
5. **0 errors, 0 unparseables** across all 7140 API calls