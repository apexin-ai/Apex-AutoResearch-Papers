# code cross llm heatmap

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_cross-llm-heatmap_20260523T144832_result.json`
- **Structured JSON:** [`2d2c6000cb4f108cb4a6.json`](../../sessions/2d/2d2c6000cb4f108cb4a6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All outputs generated. Here's the summary:

**Heatmap findings:**
- **TweetEval (9 LLMs × 4 subgroups):** GPT-3.5-turbo is the most heterogeneous (error range 0.194 across subgroups, up to 0.49 on Hash_Medium). Open-source models (Mistral, Qwen, Llama) have lower and more uniform error rates (0.12–0.28).
- **CivilComments (3 LLMs × 4 subgroups):** GPT-4o shows the most subgroup heterogeneity (range 0.103). GPT-4o-mini has uniformly high error rates (0.35–0.43).

**Rank correlation findings:**
- **TweetEval mean ρ = 0.244**, range [−0.80, 1.00]. 61% of LLM pairs have ρ < 0.5.
- Most dissimilar: GPT-3.5-turbo vs Gemma/Mistral (ρ = −0.80) — completely opposite error patterns.
- Clear split: GPT-family models correlate with each other; open-source models correlate with each other; cross-family correlations are low/negative.
- **CivilComments mean ρ = 0.200**, GPT-4o vs GPT-4o-mini ρ = −0.40.

**Files produced:**
- `cross_llm_heatmap.pdf/.png` — side-by-side error-rate heatmaps
- `cross_llm_rank_corr_heatmap.pdf/.png` — pairwise Spearman ρ matrices
- `cross_llm_rank_correlation.csv` — raw ρ values
- `cross_llm_heatmap_report.txt` — full summary

---
