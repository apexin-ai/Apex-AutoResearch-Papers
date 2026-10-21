# analysis mmlu 15b data summary

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_mmlu_15b_data_summary_20260524T070611_result.json`
- **Structured JSON:** [`0353c51b0857b424ff9c.json`](../../sessions/03/0353c51b0857b424ff9c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data collected. Here's the formatted output for Paper Agent:

---

## Table 1: MMLU 5-shot Accuracy (Qwen2.5-7B-Instruct, seed 42)

| Model | MMLU 5-shot Acc | Δ vs Base |
|-------|----------------|-----------|
| Base (Qwen2.5-7B) | 0.7423 | — |
| TG+PCGrad (v9) | 0.7386 | −0.0038 |
| Soft-Switch (v8b) | 0.7375 | −0.0048 |
| LoRA-Only | 0.7357 | −0.0066 |
| Turn-Gate (v7) | 0.7347 | −0.0077 |
| Uniform-Gate | 0.7346 | −0.0078 |

All variants within ~0.8pp of base — no meaningful general knowledge degradation. Sample size: 14,042 per model.

---

## Table 2: Qwen2.5-1.5B Cross-Model Eval (AR, n=50 conversations)

| Model | β | AR GAR (mid_turns_avg) | PPL (median) | PPL (mean) |
|-------|---|------------------------|--------------|------------|
| Base  | 0 | 0.01672 | 1.909 | 1.882 |
| TG    | 0 | 0.02333 | 1.897 | 1.871 |
| Base  | 3 | 0.12015 | 2.216 | 5,707,633\* |
| TG    | 3 | 0.11426 | 1.975 | 1.992 |
| Base  | 5 | 0.65712 | 2.804 | 2.848 |
| TG    | 5 | 0.71501 | 2.624 | 2.688 |

\*Base β=3 mean PPL inflated by one catastrophic outlier (conv #11: PPL=279,673,896). Median is the correct summary statistic here.

**Wilcoxon signed-rank tests (from summary_ci_wilcoxon.json):**

| β | W | p-value | effect size r | N |
|---|---|---------|---------------|---|
| 0 | 190 | 0.0045 | 0.447 | 39 |
| 3 | 300 | 0.8146 | 0.042 | 35 |
| 5 | 55  | <0.001 | 0.749 | 39 |

β=0: TG significantly higher GAR (p<0.01, medium effect).
β=3: No significant difference.
β=5: TG significantly higher GAR (p<0.001, large effect).

---

## Table 3: 1.5B Phase 1 GAR Diagnostic (TF mode, base model only)

Per-turn GAR decay across 5 topics:

| Turn | Avg GAR |
|------|---------|
| 1 | 0.03358 |
| 2 | 0.01158 |
| 3 | 0.01236 |
| 4 | 0.00761 |
| 5 | 0.00802 |
| 6 | 0.00286 |
| 7 | 0.00493 |
| 8 | 0.00500 |
| 9 | 0.00395 |
| 10 | 0.00354 |

**mid_turns_avg_gar:** 0.006797
**relative_drop (turn1→mid):** 79.8%
**pass:** true (>50% decay confirms GAR diagnostic pattern holds at 1.5B scale)

Per-topic breakdown:

| Topic | Turn 1 GAR | Turn 10 GAR |
|-------|-----------|-------------|
| knowledge_qa | 0.05357 | 0.00774 |
| coding_help | 0.02432 | 0.00256 |
| creative_writing | 0.02384 | 0.00208 |
| math_reasoning | 0.01076 | 0.00223 |
| debate | 0.05541 | 0.00310 |

---

**Note:** No TF GAR evaluation exists for the TG-finetuned 1.5B model — the phase 1 diagnostic only covers the base checkpoint.

---
