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
