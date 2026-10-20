# analysis exp004 sensitivity analyses

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp004_sensitivity_analyses_20260521T120000_result.json`
- **Structured JSON:** [`b513099bc795f52ff8b5.json`](../../sessions/b5/b513099bc795f52ff8b5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Output looks correct. Results summary:

### (k) Fixed vs Random
- **All random G_item = 0.8200**, fixed(temp+ordering) **G_item = 0.8237**
- Difference: **+0.37 pp** (delta reduced 2.47%)
- Temperature:item_id (0.65%) and ordering:item_id (0.54%) are small — fixing them barely changes G_item

### (d) REML vs Henderson I
- For substantive components (>0.1% variance): **max diff = 0.43%**
- Near-perfect agreement confirms Henderson I is appropriate for this balanced design
- 3 boundary components (seed:ordering, seed, ordering — all Henderson I = 0, REML = 0)

### (i) Power Analysis
- Design is **massively overpowered**: even 0.01% interaction has 96.4% power
- MDE at 80% power: **0.007%** of total variance
- MDE at 95% power: **0.0095%** of total variance
- F_obs = 744.5, p ≈ 0 for observed model:item_id (33.64% of variance)

Output saved to `results/exp001_analysis/sensitivity_analyses.json`.

---
