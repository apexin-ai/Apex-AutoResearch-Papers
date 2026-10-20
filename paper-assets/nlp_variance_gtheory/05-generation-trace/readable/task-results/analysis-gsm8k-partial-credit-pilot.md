# analysis gsm8k partial credit pilot

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_gsm8k_partial_credit_pilot_20260522T135301_result.json`
- **Structured JSON:** [`40db422fd30d8ac8c195.json`](../../sessions/40/40db422fd30d8ac8c195.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Results saved. Summary:

**Binary vs Partial-Credit Variance Decomposition (Llama-3.1-8B, GSM8K, n=57,600)**

| Component | Binary % | Partial % | Δ |
|---|---|---|---|
| prompt_template | 25.49 | 1.16 | **-24.33** |
| item_id | 19.98 | 12.74 | -7.24 |
| prompt_template:item_id | 18.24 | 24.84 | +6.60 |
| temperature:item_id | 5.62 | 10.44 | +4.82 |
| seed:item_id | 2.33 | 4.67 | +2.34 |
| residual | 28.16 | 45.96 | **+17.79** |
| **G_item** | **0.759** | **0.553** | **-0.206** |

Item-mean rank correlation: ρ = 0.26 (p < 0.001).

Key findings for Reviewer Q5 response:

1. **Scoring rubric drastically reshapes variance structure.** The prompt_template main effect drops from 25.5% → 1.2% — binary scoring inflates prompt effects because it captures "which items flip correct/incorrect" rather than reasoning quality.

2. **G_item drops 0.21** — reliability of item discrimination is substantially lower under partial credit, meaning the same measurement design that yields adequate reliability under binary scoring may be insufficient for finer-grained assessment.

3. **Item rankings change substantially** (ρ = 0.26) — items ranked as "hard" under binary aren't necessarily the ones where models produce poor reasoning.

4. **Residual balloons** (+17.8pp) — partial credit reveals unmodeled variance that binary scoring masks via floor/ceiling effects.

---
