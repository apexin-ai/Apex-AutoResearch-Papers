# figure fig1 8model stacked bar

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_figure_fig1_8model_stacked_bar_20260522T001703_result.json`
- **Structured JSON:** [`d97454c8561cc343ff36.json`](../../sessions/d9/d97454c8561cc343ff36.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

图表生成成功。

**输出路径**:
- PDF: `/root/nlp_variance_gtheory/results/exp004_8model_analysis/fig1_variance_decomposition.pdf` (29KB)
- PNG: `/root/nlp_variance_gtheory/results/exp004_8model_analysis/fig1_variance_decomposition.png` (110KB)

**各 benchmark 数值 (item_id / model:item / model / prompt / residual / other)**:

| Benchmark | Item | Model×Item | Model | Prompt | Residual | Other |
|-----------|------|-----------|-------|--------|----------|-------|
| MMLU (MC) | 37.9% | 30.2% | 2.8% | 2.5% | 25.0% | 1.5% |
| ARC (MC) | 37.9% | 33.7% | 3.1% | 9.5% | 15.4% | 0.4% |
| HellaSwag (MC) | 34.3% | 36.0% | 5.4% | 2.3% | 21.4% | 0.6% |
| GSM8K (FF) | 16.9% | 14.6% | 10.7% | 17.0% | 39.9% | 1.0% |
| MATH (FF) | 24.0% | 17.3% | 8.5% | 5.4% | 43.9% | 0.9% |

"Prompt" 组 = prompt_template + model:prompt_template + prompt_template:item_id。MC 组 item_id 占 34–38%，FF 组降至 17–24%，residual 反升至 40–44%。

---
