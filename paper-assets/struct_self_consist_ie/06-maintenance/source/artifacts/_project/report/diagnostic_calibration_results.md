## Diagnostic Calibration Results (7 dataset-model combinations)

| Combination | Degen% | ρ(LP,F1) | LP Range | Delta (pp) |
|---|---|---|---|---|
| SciERC-Qwen8B | 17.8 | 0.180 | 0.0401 | +0.615 |
| CoNLL-Qwen8B | 47.4 | 0.329 | 0.0932 | -0.921 |
| FewNERD-Qwen8B | 13.8 | 0.511 | 0.0662 | +1.355 |
| CoNLL-LLaMA | 86.5 | 0.196 | 0.0076 | +0.144 |
| SciERC-LLaMA | 19.1 | 0.167 | 0.0589 | +0.168 |
| SciERC-Qwen4B | 10.4 | 0.189 | 0.0555 | -2.230 |
| CoNLL-Qwen4B | 90.6 | 0.242 | 0.0000 | +0.089 |

Individual ρ with LP delta ≈ 0 (p>0.75). LOO R²=-3.72. Sign accuracy 28.6%.
Key blocker: SciERC-Qwen4B satisfies low-degen + positive-ρ but LP delta = -2.23pp.

⚠️ Pending unified_metrics revalidation.