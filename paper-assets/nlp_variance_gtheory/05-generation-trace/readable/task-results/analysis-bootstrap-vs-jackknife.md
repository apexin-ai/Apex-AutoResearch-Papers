# analysis bootstrap vs jackknife

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_bootstrap_vs_jackknife_20260521T040103_result.json`
- **Structured JSON:** [`40575cebc0951f946416.json`](../../sessions/40/40575cebc0951f946416.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总耗时 825 秒（~13.8 分钟）。

## Bootstrap vs Jackknife (binary_correct):

| Component | Boot CI width | Jack CI width | Ratio |
|---|---|---|---|
| item_id | 10.02 | 10.33 | 0.97 |
| residual | 5.12 | 5.26 | 0.97 |
| seed:item_id | 2.40 | 2.37 | 1.01 |
| prompt_template:item_id | 2.33 | 2.23 | 1.04 |
| precision:item_id | 1.81 | 1.79 | 1.01 |
| temperature:item_id | 0.94 | 0.98 | 0.96 |
| precision | 1.35 | 1.33 | 1.01 |

**结论: Bootstrap robust** — ratio 范围 [0.96, 1.04]，所有组分的 bootstrap 与 jackknife CI 宽度几乎一致。Bootstrap 重复采样 item 带来的独立性违反对 CI 估计无实质影响。结果已保存至 `results/analysis/bootstrap_vs_jackknife.json`。

---
