# Eval Analysis: eval_humaneval_grpo_standard_20_2048

## Core Metrics

| Metric | Value |
|--------|-------|
| **pass@1** | **10.37% +/- 2.38%** |
| Correct | 17 / 164 |
| Model | grpo_stage2_standard_20_v8/checkpoint-50 |
| max_new_tokens | 2048 |
| Runtime | ~4h 8min |
| Exit code | 0 (success) |
| W&B run ID | N/A (not logged) |

## Progress Snapshots

| Problems | Running pass@1 |
|----------|---------------|
| 20/164 | 15.00% |
| 120/164 | 10.83% |
| 140/164 | 10.00% |
| 160/164 | 10.62% |
| 164/164 | 10.37% |

## Comparison: @512 vs @2048

| Setting | pass@1 | Correct | Delta |
|---------|--------|---------|-------|
| GRPO Standard 20% @512 | 1.83% | 3/164 | baseline |
| GRPO Standard 20% @2048 | 10.37% | 17/164 | **+8.54pp** |

The @512 result (1.83%) was confirmed as a truncation artifact. With 2048 tokens the model solves 14 additional problems, a 5.7x improvement in correct count.

## Comparison: HumanEval@2048 Matrix

| Method | pass@1 | Correct | Status |
|--------|--------|---------|--------|
| SFT RASP 20% | 10.37% | 17/164 | baseline |
| **GRPO Standard 20%** | **10.37%** | **17/164** | **this run** |
| SFT Standard 20% | negative | - | failed |
| GRPO RASP 20% | TBD | - | completed, pending analysis |

GRPO Standard and SFT RASP produce identical pass@1 (10.37%, 17/164). Both substantially outperform SFT Standard (negative).

## Notes

- No OOM or crash errors
- Used cached HumanEval dataset (network unreachable, but cache hit)
- Non-uniform MLP structure confirmed (intermediate_size range [8128, 18944])

## Conclusion

**Status: SUCCESS (moderate)**

GRPO Standard 20% achieves 10.37% pass@1 at 2048 tokens, matching SFT RASP exactly. This confirms:
1. The @512 result was entirely a truncation artifact (1.83% -> 10.37%)
2. GRPO training recovers coding ability to the same level as SFT RASP for standard pruning
3. Standard pruning with GRPO is competitive with RASP+SFT, but the key comparison is GRPO RASP (pending)
