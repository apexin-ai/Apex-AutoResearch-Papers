# code exp 025 positive scenario

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp-025-positive-scenario_20260522T124553_result.json`
- **Structured JSON:** [`70216af82d78198859fa.json`](../../sessions/70/70216af82d78198859fa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All outputs generated. Here's the summary of results:

## Key Results (exp-025)

### Screening
- **0/16 combinations pass all conditions**. The bottleneck is κ(C_s) ≤ 1.25 — this requires FPR+FNR ≲ 0.20, which no real LLM achieves across all subgroups. Closest: Qwen2.5-7B True_short (κ=1.23), Mistral-7B True_short (κ=1.27).
- max(FPR,FNR) < 0.5 fails for 4 combos: gpt-4.1, gpt-4o, gpt-4-turbo (TweetEval), gpt-4o-mini (CivilComments)
- Budget passes for K=2 at both n=250 and n=500, and for K=4 at n=500

### Oracle Screening (excluding subgroups with max error ≥ 0.4)
- **EC-HTE (HB) beats Global in 41/52 comparisons** on aggregate RMSE
- **All 4 open-source LLMs** (Llama, Qwen, Mistral, Gemma) on TweetEval: HB wins consistently (32/32), with RMSE reductions of 0.001-0.008
- GPT-4o-mini/TweetEval and GPT-4-turbo/TweetEval also show HB advantages
- **HB loses** on GPT-3.5-turbo/TweetEval (very asymmetric FPR ~0.39) and GPT-4o/CivilComments (low P(Z=1)=0.3 amplifies correction noise)
- **Best case**: Qwen2.5-7B K=4 n=500 Z=0: RMSE reduction = 0.0075

### Output Files
- `results/exp_screening.csv` — 56 rows (16 combos × subgroups)
- `results/exp_oracle_screening.csv` — 1040 rows (MC-aggregated results)
- `results/exp_positive_scenario_summary.md` — full analysis report

---
