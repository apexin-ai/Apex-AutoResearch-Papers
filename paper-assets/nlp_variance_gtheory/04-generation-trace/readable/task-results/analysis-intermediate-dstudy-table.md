# analysis intermediate dstudy table

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_intermediate_dstudy_table_20260522T104120_result.json`
- **Structured JSON:** [`200eb2161ff14a9146da.json`](../../sessions/20/200eb2161ff14a9146da.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

JSON saved. Here's the D-study results table:

| Design | Prompts | Seeds | Temps | Orderings | Conditions | σ²(δ) | G@200 | n(G≥0.80) |
|---|---|---|---|---|---|---|---|---|
| Single-condition (typical) | 1 | 1 | 1 | 1 | 1 | 0.0877 | **0.592** | 552 |
| Minimal upgrade | 2 | 1 | 1 | 1 | 2 | 0.0566 | 0.692 | 357 |
| Easy upgrade | 2 | 2 | 1 | 1 | 4 | 0.0389 | 0.766 | 245 |
| Moderate | 3 | 3 | 1 | 1 | 9 | 0.0282 | 0.818 | 178 |
| Standard | 4 | 4 | 2 | 1 | 32 | 0.0192 | 0.869 | 121 |
| Enhanced | 6 | 6 | 1 | 2 | 72 | 0.0188 | 0.871 | 119 |
| Full multi-facet | 6 | 6 | 3† | 4 | 1296 | 0.0087 | **0.936** | 55 |

†Full multi-facet includes all 3 precision levels (FP16/BF16/FP32) × 3 temperatures; for practical designs (rows 1–6), precision is fixed at 1 level.

Key observations:
- Just adding 1 extra prompt template (Minimal upgrade, 2× cost) raises G from 0.59 → 0.69
- The **Easy upgrade** (2 prompts × 2 seeds, 4× cost) reaches G=0.77 — the biggest ROI point
- **Moderate** (3×3, 9× cost) crosses the G=0.80 threshold at 200 items
- Standard and Enhanced give nearly identical G (~0.87) despite very different condition counts (32 vs 72), because prompt and seed interactions dominate — temperature and ordering contribute much less
- Going from Enhanced to Full multi-facet (adding all precision/temp levels) provides the last jump to 0.936 but requires 1296 conditions per item

Both anchors validated: single-condition G@200 = 0.5917 ✓, full multi-facet G@200 = 0.9361 ✓. Monotonicity holds across all rows.

---
