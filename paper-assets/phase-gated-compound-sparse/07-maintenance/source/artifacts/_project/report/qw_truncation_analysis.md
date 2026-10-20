# QW Truncation Analysis (R9 Worker D)

## Truncation Rates

| Dataset | Model | Truncated | Rate | Avg Length |
|---------|-------|-----------|------|------------|
| GSM8K | DS | 15/50 | 30% | 1332.5 |
| GSM8K | **QW** | **50/50** | **100%** | **2047.0** |
| MATH-500 n=50 | DS | 19/50 | 38% | 1242.8 |
| MATH-500 n=50 | QW | 12/50 | 24% | 1057.8 |
| MATH-500 n=500 | DS | 205/500 | 41% | 1396.8 |
| MATH-500 n=500 | QW | 139/500 | 27.8% | 1174.0 |

Note: truncation counts identical across strategies/sparsity — generation by dense model, masking only affects PPL.

## Technical Explanation
QW (chat model) lacks `<think>→answer` structured termination → verbose formatting fills 2047 budget on all GSM8K problems. DS (reasoning model) has compact CoT, only complex problems truncate.

## Paper Footnote (ready for Paper Agent)
"QW random s030 GSM8K data marked unreliable due to systematic generation truncation: Qwen2.5-7B-Instruct lacks natural generation termination points, hitting max_new_tokens=2047 on all 50 GSM8K problems (100% truncation vs DeepSeek-R1-Distill's 30%), causing phase segmentation to operate on artificially equal-length sequences and producing spurious phase structure with extreme outlier interaction indices (gradient=92.9, 95% CI: [3.8, 258.8])."
