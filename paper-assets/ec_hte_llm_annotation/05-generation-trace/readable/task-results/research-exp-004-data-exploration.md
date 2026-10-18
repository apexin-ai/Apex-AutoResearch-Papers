# research exp 004 data exploration

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_exp-004-data-exploration_20260520T232548_result.json`
- **Structured JSON:** [`93f467574ff2c48d677b.json`](../../sessions/93/93f467574ff2c48d677b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Report written to `/home/ubuntu/ec_hte_llm_annotation/results/ucb_hate_speech_exploration.md`.

**Summary of key findings:**

- **135,556 annotations** across 39,565 comments by 7,912 annotators. Rich target demographics (race, religion, gender, etc.) and annotator demographics (race, gender, ideology, age, education, income).

- **Recommended mapping (Scheme A)**: T = `target_race_black`, Y = `hatespeech` ordinal (per-annotation), Z = LLM-annotated dehumanization level, S = annotator race (White/Black/Other). Min cell size = 743. Observable Z×S interaction in CATE estimates — Black annotators perceive more dehumanization in anti-Black content (26.9% at max vs 21.9% for White), creating a natural LLM misclassification heterogeneity story.

- **Pattern consistency is feasible**: An LLM trained on majority-perspective data would under-classify dehumanization from Black annotators' perspective. Global correction spreads this majority bias; EC-HTE preserves subgroup-specific corrections. No ground truth CATE needed — method divergence itself is the demonstration.

- **Key caveat**: `hate_speech_score` is per-comment (Rasch aggregated), so ordinal labels must be used as Y for annotator-level heterogeneity. Scheme B (gender) is not recommended due to negligible treatment effect.

---
