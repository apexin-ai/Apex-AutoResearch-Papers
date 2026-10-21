---
name: LLM Evaluation Variance — Research Patterns
description: Experimental consensus on variance sources, decomposition methods, and gaps in LLM evaluation reproducibility (25 papers, 2018-2026)
scope: project
version: 2
tags: [distilled, auto-generated]
distilled_from:
  paper_count: 25
  paper_keys: [sclar2024formatting, zhou2026irt, saleva2025beyond, pezeshkpour2024ordering, polo2024tinybenchmarks, magnusson2023reproducibility, shanmugavelu2024floating, lalor2019irt, rodriguez2021leaderboards, henderson2018deep, madaan2024quantifying, song2025exploring, zhang2025tbik, li2025atlas, biderman2024lessons, hua2025flaw, mesting2026hidden, brittlebench2026, yuan2025layercast, kunievsky2025intent, thinkingmachines2025batch, messina2026background, generalizit2024, bui2025seeds, sameprompt2026]
  last_distilled: "2026-05-22T00:00:00Z"
---

## Variance Source Taxonomy

**Prompt/Format Sensitivity** (8/25, HIGH): Formatting→76pp spread (Sclar ICLR'24); option ordering→13-85% fluctuation (Pezeshkpour NAACL'24); perturbations flip rankings 63% of cases (Brittlebench); format performance correlates weakly across models. Eval setup (template, few-shot, framework version) compounds this (Biderman'24).

**Infrastructure Nondeterminism** (5/25, HIGH): BF16→9% accuracy variation, FP32→~0% (Yuan). FP non-associativity: 1000 identical runs→1000 unique weights (Shanmugavelu SC'24). Batch-size kernel selection is primary source, not thread-level FP (ThinkingMachines). T=0 background temp varies by provider: Claude~0, GPT~0.075 (Messina TMLR'26). TBIK guarantees bit-wise reproducibility across TP sizes (Zhang'25).

**Evaluation Method Artifacts** (4/25, HIGH): Heuristic eval inflates measured sensitivity; LLM-judge raises ARC-C Spearman 0.30→0.95 (Hua EMNLP'25). Standard CIs omit 40-60% of uncertainty; naive 95% CIs→79% coverage (Mesting TEE). Code sharing strongest reproducibility predictor (+8%) yet only 46% share (Magnusson ACL'23).

**Data/Item Heterogeneity** (6/25, HIGH): Between-language SD 8.9-12.0 dwarfs within-language 0.7-1.5 (Saleva IJCNLP'25). 3-6% of items have negative discrimination (Li ATLAS). Difficulty ceilings insufficient for top models; guessing 0.20-0.26 in MCQ (Zhou AAAI'26). Seed variance affects both fine-tuning (Bui'25) and RL training (Henderson AAAI'18).

## Dominant Method Families

**IRT/Psychometric** (8/25, rising 2019→2026, HIGH): Trajectory: artificial crowds for IRT (Lalor'19) → IRT leaderboards (Rodriguez'21) → efficient benchmarking via 100 IRT-selected items within 2% error (Polo ICML'24) → adaptive testing with 90% item reduction (Li ATLAS) → neural IRT diagnosing benchmark deficiencies (Zhou AAAI'26). MCQ-to-completion reformulation reduces variance more than IRT item analysis for ~7B models (Madaan'24).

**G-Theory** (3/25, emerging, MEDIUM): TEE framework decomposes judge/prompt/temp facets via REML + D-study (Mesting'26). GeneralizIT: first Python-native G-theory toolkit. Song'25 applies G-theory to LLM-as-judge writing assessment. Only framework that naturally models multi-facet interactions—severely underutilized.

## Critical Gaps — Our Niche

1. **No cross-source interaction**: Papers isolate one variance source; format × seed × precision × judge interactions unstudied (0/25). HIGH.
2. **G-theory underutilized**: Only 3/25 despite being the natural multi-facet framework. HIGH.
3. **Generative tasks neglected**: Most work targets MCQ/classification; open-ended generation variance under-studied (noted in 6/25 limitations). HIGH.
4. **Training↔eval variance disconnected**: Infra papers and eval papers operate in separate communities (0/25 bridges both). MEDIUM.
5. **No standardized variance reporting protocol**: Henderson'18 called for this in RL; 8 years later NLP still lacks one. MEDIUM.
