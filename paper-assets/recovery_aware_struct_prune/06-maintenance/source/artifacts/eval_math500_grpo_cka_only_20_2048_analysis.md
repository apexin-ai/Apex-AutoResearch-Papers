# MATH-500 Evaluation: GRPO CKA-only 20% @2048

## Result

| Metric | Value |
|--------|-------|
| Accuracy | **29.2%** (146/500) |
| Samples | 500 |
| max_new_tokens | 2048 |
| Natural EOS | 390 (78%) |
| Truncated | 110 (22%) |
| SE | ±2.0% |

## Comparison (MATH-500 @2048)

| Model | Accuracy |
|-------|----------|
| Dense | 53.0% |
| **GRPO CKA-only 20%** | **29.2%** |
| SFT CKA-only 20% | 29.0% |
| GRPO Standard 20% | 26.4% |
| GRPO RASP 20% | 24.0% |
| SFT RASP 20% | 22.6% |

## Key Delta

- GRPO vs SFT for CKA-only: **+0.2pp** (29.2% - 29.0%)
- GRPO CKA-only vs GRPO Standard: **+2.8pp**
- GRPO CKA-only vs GRPO RASP: **+5.2pp**
