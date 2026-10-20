# analysis exp001 bf16 5facet baseline

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp001_bf16_5facet_baseline_20260521T084612_result.json`
- **Structured JSON:** [`1d46a649e59510360d0f.json`](../../sessions/1d/1d46a649e59510360d0f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。核心发现：

### 对比表

| Metric | bf16-5f baseline | Sample1 | Sample2 | Sample3 | Mean±Std | Delta |
|--------|----------------:|--------:|--------:|--------:|---------:|------:|
| item_id% | **74.00** | 75.88 | 75.38 | 72.18 | 74.48±2.01 | +0.48 |
| prompt×item% | 4.65 | 4.42 | 4.35 | 5.38 | 4.72±0.58 | +0.06 |
| seed×item% | 5.42 | 5.41 | 4.87 | 5.32 | 5.20±0.29 | -0.22 |
| temp×item% | 1.84 | 1.64 | 1.45 | 2.17 | 1.75±0.37 | -0.09 |
| order×item% | 0.84 | 0.54 | 0.50 | 0.63 | 0.56±0.07 | -0.29 |
| G_item | **0.7400** | 0.7590 | 0.7540 | 0.7220 | 0.745±0.020 | +0.005 |

### Delta 分解

之前 6-facet→exp-001b 的 13.4pp 差异现在被分解为：

- **Precision facet 移除效应**: 74.00 − 61.08 = **+12.92 pp** (6-facet → bf16-5f)
- **Item 选择效应**: 74.48 − 74.00 = **+0.48 pp** (bf16-5f → exp-001b mean)

结论：几乎全部差异来自 precision facet 的移除（12.92pp），item 选择效应仅 0.48pp，在 exp-001b 三个 sample 的 ±2.01 标准差范围内。bf16 matched baseline 的 G_item=0.740 与 exp-001b 均值 0.745 几乎一致，确认 exp-001b 的 resampling 结果是可靠的。

输出已保存到 `results/analysis/exp001_llama_bf16only_5facet.json`。

---
