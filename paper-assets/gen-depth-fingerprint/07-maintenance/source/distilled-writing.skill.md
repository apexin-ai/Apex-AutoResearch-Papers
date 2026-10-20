---
name: AI Text Detection & Generation Depth — Writing Patterns
description: Distilled narrative strategies, figure/table conventions from 8 deep-read papers on AI text detection and model collapse (ICLR/ICML/ACL 2024-2025).
scope: project
version: 3
tags: [distilled, auto-generated]
distilled_from:
  paper_count: 25
  paper_keys: [monitoring_ai_review, min_k_percent, reliable_detection, detection_possibilities, detectgpt, intrinsic_dimension, dsir, watermark_llm, curious_decline, markovian_chains, paraphrase_evades, qurating, fast_detectgpt, gltr, diveye, curse_of_recursion, ood_baseline, synthid_text, nucleus_sampling, dna_gpt, uchendu_attribution, writing_diversity, strong_model_collapse, broken_telephone, binoculars]
  last_distilled: "2026-05-22T12:00:00Z"
---

## Story Types

**突破局限型** (4/8): eliminate prior methods, reveal hidden dimension. **化繁为简型** (3/8): complex to simple principle. **跨界迁移型** (1/8): analogy-driven (Broken Telephone). **High.**

## Intro Patterns

**4 paragraphs** most common (4/8). 2-paragraph for simple-method papers (Binoculars, Writing Diversity). 5-paragraph for theory papers (Strong Model Collapse, QuRating). **Hooks**: societal urgency (3/8), bold contradiction (1/8), data crisis (1/8). **Elimination ladder** (2/8): each paragraph kills a method class. **Contributions**: 3 numbered items (3/8); research questions for empirical (1/8); implicit for simplicity papers (2/8). **High.**

## Named-Problem Technique

"Capybara problem" (Binoculars), "Strong" naming (Strong Model Collapse), "Broken telephone" analogy create citeable anchors. 3/8, high payoff. **Medium.**

## Figure 1

**Method overview** (4/8): pipeline diagram. **Motivation evidence** (2/8): distribution plot showing the signal. **Teaser result** (2/8): headline performance upfront. Choose teaser when result IS the surprise. **High.**

## Result Visualization

- **Log-scale FPR ROC** mandatory for detection (2/8). Standard AUC hides low-FPR weakness.
- **Qualitative text table before metrics** (3/8): degradation examples as Table 1 (Curious Decline URLs, Broken Telephone lorry->car, Binoculars capybara). Makes metrics visceral.
- **Line plots** for iterative (5/8). **Bar charts** for cross-method (4/8). **Theory-experiment overlays** for theory papers.
- **High.**

## Table Conventions

- Rows=methods, cols=datasets x metrics (4/8). Bold best (3/8). Symbolic markers for density.
- Single-run in main; std/CI in appendix (5/8).
- **Main:appendix split** standard: 2-3 main + extensive appendix (DNA-GPT 3+13). Core claims in main.
- Theory papers skip tables entirely (Strong Model Collapse: 0 tables).
- 3-8 baselines in main table (median 5). **High.**

## Figure Narrative Arc

**Standard**: method->evidence->results->robustness->ablation (4/8). **Inverted**: result-first when surprise (Binoculars). **Deepening**: what->where->why (Writing Diversity). **Theory flow**: claim->framework->validate->extend. **High.**

## Ablation Presentation

- Full numbers dominate (6/8); checkmark grid rare. **Embedded in main results** (3/8): mitigation lines alongside decline curves saves space.
- **Compute equivalence** framing more compelling than raw deltas (QuRating). **Medium.**
