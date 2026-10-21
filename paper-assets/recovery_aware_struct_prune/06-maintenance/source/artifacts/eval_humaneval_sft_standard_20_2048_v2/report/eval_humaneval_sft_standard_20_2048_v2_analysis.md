# HumanEval Evaluation: SFT Standard 20% (max_new_tokens=2048, v2)

## Key Metrics

| Metric | Value |
|---|---|
| pass@1 | 11.59% (0.1159) |
| correct / total | 19 / 164 |
| stderr | 0.0250 |
| avg_response_length | 1850.7 tokens |
| median_response_length | 2048 (max) |
| max_new_tokens | 2048 |

## HumanEval@2048 Comparison Table

| Model | pass@1 | correct/total |
|---|---|---|
| Unpruned | 45.12% | 74/164 |
| GRPO RASP 20% | 14.63% | 24/164 |
| **SFT Standard 20%** | **11.59%** | **19/164** |
| SFT RASP 20% | 10.37% | 17/164 |

## Observations

- SFT Standard 20% (11.59%) slightly outperforms SFT RASP 20% (10.37%), but the difference (1.22pp) is within 1 stderr and not statistically significant.
- Both SFT variants are substantially below GRPO RASP 20% (14.63%) and far below Unpruned (45.12%).
- Median response length = 2048 indicates most responses hit the token limit. Many failures are the model generating chain-of-thought reasoning text ("Okay, I need to write...") instead of directly outputting code, leading to SyntaxErrors when the output is executed.
- All pruned models show severe code generation degradation (~70-77% relative drop from unpruned).

## Impact on Claims

- **C1 (RASP recovery advantage):** SFT Standard slightly trails SFT RASP on MMLU/GSM8K but slightly leads on HumanEval. The differences are small and not significant. On HumanEval specifically, SFT Standard (11.59%) vs SFT RASP (10.37%) provides no evidence that RASP-aware recovery is superior for code generation. The overall cross-benchmark picture remains mixed.
- **C3 (GRPO superiority):** GRPO RASP 20% (14.63%) outperforms both SFT variants on HumanEval, consistent with C3. The GRPO advantage over SFT Standard is 3.04pp. GRPO's code generation advantage is consistent across recovery methods.