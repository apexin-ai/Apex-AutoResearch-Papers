Model-as-Fixed G-Study (MF2 Defense)

| Design | G_item | 95% CI |
|--------|--------|--------|
| Model=random | 0.820 | [0.782, 0.861] |
| Model=fixed (per-model avg) | 0.963 | [0.957, 0.969] |
| Model=fixed (remove m:i) | 0.981 | [0.975, 0.985] |

Per-model G_item: Gemma 0.971, Llama 0.958, Mistral 0.956, Qwen 0.968
Mean Spearman ρ across models = 0.642 → model:item interaction non-negligible
File: results/analysis/model_as_fixed_gstudy.json