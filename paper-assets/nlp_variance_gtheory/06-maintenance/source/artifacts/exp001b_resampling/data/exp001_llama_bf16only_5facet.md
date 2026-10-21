exp-001 Llama bf16-only 5-facet Matched Baseline

| Metric | bf16-5f baseline | Sample1 | Sample2 | Sample3 | Mean±Std | Delta |
|--------|----------------:|--------:|--------:|--------:|---------:|------:|
| item_id% | 74.00 | 75.88 | 75.38 | 72.18 | 74.48±2.01 | +0.48 |
| prompt×item% | 4.65 | 4.42 | 4.35 | 5.38 | 4.72±0.58 | +0.06 |
| seed×item% | 5.42 | 5.41 | 4.87 | 5.32 | 5.20±0.29 | -0.22 |
| temp×item% | 1.84 | 1.64 | 1.45 | 2.17 | 1.75±0.37 | -0.09 |
| G_item | 0.740 | 0.759 | 0.754 | 0.722 | 0.745±0.020 | +0.005 |

Delta decomposition:
- Precision facet removal: 74.00 - 61.08 = +12.92pp
- Item selection: 74.48 - 74.00 = +0.48pp (within sampling noise)

File: results/analysis/exp001_llama_bf16only_5facet.json