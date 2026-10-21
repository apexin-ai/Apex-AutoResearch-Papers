---
name: AI Text Detection & Generation Depth — Research Patterns
description: Distilled experimental conventions, baselines, metrics, and gaps from 25 papers on AI text detection, model collapse, and content diversity (2019-2026).
scope: project
version: 3
tags: [distilled, auto-generated]
distilled_from:
  paper_count: 25
  paper_keys: [monitoring_ai_review, min_k_percent, reliable_detection, detection_possibilities, detectgpt, intrinsic_dimension, dsir, watermark_llm, curious_decline, markovian_chains, paraphrase_evades, qurating, fast_detectgpt, gltr, diveye, curse_of_recursion, ood_baseline, synthid_text, nucleus_sampling, dna_gpt, uchendu_attribution, writing_diversity, strong_model_collapse, broken_telephone, binoculars]
  last_distilled: "2026-05-22T12:00:00Z"
---

## Evaluation Consensus

**Primary**: AUROC (10/25). **Supplement**: TPR@low-FPR (0.01%-1%) — Binoculars argues standard AUC hides low-FPR weakness. Cross-domain eval on 3+ datasets expected (XSum, WritingPrompts, PubMedQA). Robustness axes: paraphrasing, cross-model transfer, temperature, cross-lingual. 7/8 deep-read. **High.**

## Baselines

**Mandatory**: GPTZero (5/25), DetectGPT (5/25), Fast-DetectGPT. **Rising**: Binoculars, DivEye. **Declining**: supervised-only classifiers. 5-8 baselines typical. **High.**

## Method Trends

**Zero-shot > supervised** (7/25). Signals: (1) cond. prob curvature — Fast-DetectGPT, 340x speedup; (2) dual-model PPL ratio — Binoculars, >90% TPR@0.01%FPR; (3) regeneration divergence — DNA-GPT; (4) surprisal diversity — DivEye +33.2%. Perturbation-based declining (cost). Watermarking parallel track (SynthID at 20M scale). **High.**

## Foundational Findings

- **Recursive training degrades diversity irreversibly**: syntactic diversity collapses fastest; perplexity improves while diversity degrades; filtering amplifies loss (Curious Decline). 4/25. **High.**
- **1% synthetic data causes persistent collapse**: zeta=Omega(p2^2*c^2) irreducible; larger models amplify below interpolation threshold (Strong Model Collapse). 3/25. **High.**
- **RLHF causes homogenization**: base GPT-3 does NOT reduce diversity; InstructGPT DOES; 100% from model text (Writing Diversity). 2/25. **High.**
- **Inference-time distortion accumulates**: ~0.02 FActScore loss/iter; language-dependent; converges to floor (Broken Telephone). **Medium.**

## Competitor Signals

| Method | Signal | Weakness |
|--------|--------|----------|
| Fast-DetectGPT | Cond. prob curvature | No theory for why |
| DNA-GPT | Regeneration consistency | K API calls; memorization |
| Binoculars | PPL/X-PPL ratio | 58% FN on GPT-4 |
| DivEye | Surprisal diversity | Limited validation |
| Intrinsic Dim. | Embedding topology | Opaque features |

## Research Gaps (Our Opportunity)

1. **No paper studies detection as f(generation depth)** — all binary. 0/25. **High.**
2. **Collapse disconnected from detection** — diversity loss not leveraged as feature. **High.**
3. **Detection ignores diversity; diversity ignores detection** — two literatures don't cross-cite. **High.**
4. **Cross-lingual depth** unexplored (Broken Telephone hints). **Medium.**
5. **RLHF fingerprints across depths** unmeasured. **Medium.**
