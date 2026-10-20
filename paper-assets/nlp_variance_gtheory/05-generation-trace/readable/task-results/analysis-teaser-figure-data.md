# analysis teaser figure data

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_teaser_figure_data_20260522T135127_result.json`
- **Structured JSON:** [`a4d453d5b3f7e22d19f0.json`](../../sessions/a4/a4d453d5b3f7e22d19f0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

JSON 已保存到 `artifacts/exp004/data/teaser_figure_data.json`。

关键结果：

| 指标 | 值 |
|------|-----|
| **Accuracy range** | **8.5 pp** (65.5% → 74.0%) |
| Mean ± std | 70.9% ± 1.7% |
| IQR (p25–p75) | 70.0% – 72.0% |
| 90% interval (p5–p95) | 67.7% – 73.0% |

**Marginal effects（按 facet mean 的 spread）：**
- **Seed**: 2.2 pp spread（69.8%–72.0%，最大 facet effect）
- **Prompt template**: 1.7 pp spread（70.3%–72.0%）
- **Temperature**: 0.9 pp spread（70.5% vs 71.3%）
- **Ordering**: 0.4 pp spread（70.7%–71.1%，最小）

**极端条件：**
- Best: temp=0.0, prompt=2, seed=42, ordering=3 → 74.0%
- Worst: temp=0.7, prompt=3, seed=42, ordering=4 → 65.5%

---
