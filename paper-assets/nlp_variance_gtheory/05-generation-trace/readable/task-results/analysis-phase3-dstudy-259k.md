# analysis phase3 dstudy 259k

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_phase3_dstudy_259k_20260521T215534_result.json`
- **Structured JSON:** [`72a8a4fc748b38cfc92e.json`](../../sessions/72/72a8a4fc748b38cfc92e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果摘要：

**6-facet (259,200 records)**
- G_at_200 = 0.9361 (matches expected 0.9361)
- n_{G≥0.80} = 55, n_{G≥0.90} = 123, n_{G≥0.95} = 260
- Top variance: item_id 58.39%, residual 23.11%

**BF16 5-facet (86,400 records)**
- G_at_200 = 0.9578 (matches expected 0.9578)
- n_{G≥0.80} = 36, n_{G≥0.90} = 80, n_{G≥0.95} = 168
- Top variance: item_id 70.94%, residual 13.61%

JSON 已写入 `results/exp001_analysis/dstudy_henderson_i_259k.json`，脚本在 `scripts/exp001_analysis/dstudy_henderson_i.py`。

---
