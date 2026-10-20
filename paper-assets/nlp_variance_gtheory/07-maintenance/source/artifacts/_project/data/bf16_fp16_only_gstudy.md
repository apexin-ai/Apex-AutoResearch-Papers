BF16-vs-FP16 Sensitivity Analysis (Dream #3 Response)

Data: 525,400 records, 3 models (Llama/Mistral/Qwen), BF16+FP16 only (no FP32)

Precision-related variance components:
| Component | 3-Precision (%) | BF16+FP16 (%) | Delta |
|---|---|---|---|
| precision | 0.4033 | 0.0006 | -0.4027 |
| precision×item | 1.3036 | 0.0412 | -1.2623 |
| model×precision | 0.1995 | 0.0009 | -0.1986 |

Key: FP32 is sole driver of precision variance. BF16≈FP16 (0.23pp diff).
File on server: results/analysis/bf16_fp16_only_gstudy.json