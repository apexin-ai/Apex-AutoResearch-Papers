LOMO Matched Spec (Henderson I with model:X interactions)

Full 4-model校验：item_id=42.07%, model:item=33.64%, G_item=0.8200 — 与 dataset_a4 完全一致

| Dropped | item_id% | model:item% | G_item |
|---------|----------|-------------|--------|
| (full 4-model) | 42.07 | 33.64 | 0.8200 |
| Gemma-2-9B | 40.51 | 33.67 | 0.7668 |
| Llama-3.1-8B | 39.32 | 36.92 | 0.7474 |
| Mistral-7B | 44.90 | 32.19 | 0.7929 |
| Qwen3-8B | 42.80 | 31.67 | 0.7860 |

Stability: item_id spread=5.58pp, model:item spread=5.25pp, G_item spread=0.0455
File on server: results/analysis/lomo_matched_spec.json