# code agnews mc simulation

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_agnews-mc-simulation_20260524T153816_result.json`
- **Structured JSON:** [`6476f84ac82b1749318d.json`](../../sessions/64/6476f84ac82b1749318d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All outputs generated. Here's the summary:

**Files produced:**
- `artifacts/exp-agnews/data/run_agnews_hetero_tau.py` — script
- `artifacts/exp-agnews/data/agnews_raw.csv` — 9600 rows
- `artifacts/exp-agnews/data/agnews_summary.csv` — 12 rows
- `artifacts/exp-agnews/data/agnews_analysis.md` — full analysis

**Key results (N=5000, 100 MC, AG News Business vs non-Business):**

| n_expert | |Bias| Global | |Bias| EC-HTE | Winner |
|----------|-------------|-------------|--------|
| 250 | 0.0515 | 0.0531 | Global |
| 500 | 0.0524 | 0.0323 | **EC-HTE** |
| 1000 | 0.0528 | 0.0166 | **EC-HTE** |

- EC-HTE wins on |Bias| at 2/3 budget levels (n_expert ≥ 500)
- Global wins RMSE at all levels (EC-HTE has higher variance with stratified estimation)
- Sign reversal rates near zero across all methods (all true CATEs are positive)
- Bias identity R² = -1.3156: the symmetric π_s=(FPR+FNR)/2 approximation doesn't hold well here because FPR and FNR are highly asymmetric (e.g., long_complex: 0.25 vs 0.38), though Global's bias still clearly scales with Δτ across subgroups
- π̄ = 0.1950, Δπ = 0.2150

---
