# Bootstrap CI Results (1000 resamples, item-level, Henderson I)

| Benchmark | G_item | 95% CI | item_id% CI | model:item% CI |
|-----------|--------|--------|-------------|----------------|
| MMLU | 0.896 | [0.874, 0.914] | [33.1, 42.2] | [26.8, 33.3] |
| ARC | 0.892 | [0.852, 0.919] | — | — |
| HellaSwag | 0.872 | [0.842, 0.896] | — | — |
| GSM8K | 0.863 | [0.832, 0.887] | [13.3, 20.0] | [13.3, 15.8] |
| MATH | 0.888 | [0.868, 0.903] | [20.7, 27.2] | [14.7, 17.7] |

Files: server `results/exp004_8model_analysis/bootstrap_ci_{bm}.json` + local `artifacts/exp004/data/bootstrap_ci_{bm}.json`