---
name: distilled-writing
description: "Writing patterns for spectral/model collapse papers: narrative, figures, tables from 8 deep-read papers"
scope: project
version: 2
tags: [distilled, auto-generated]
distilled_from:
  paper_count: 23
  paper_keys: [tale_of_tails, self_consuming_mad, collapse_demystified, strong_model_collapse, mind_the_gap, spectral_collapse_plasticity, data_mixing_laws, aioli, false_promise, doremi, pythia, ai_models_collapse_nature, collapse_inevitable, sigma, collapse_or_thrive, beyond_collapse, knowledge_collapse, effective_rank, implicit_self_regularization, early_warning_signals, dl_early_warning, methods_detecting_ews, llm_self_consuming]
  last_distilled: "2026-05-24T09:00:00Z"
---

## Story Types (8/8, High)

- **Unified framework** (3/8): Tale of Tails, Plasticity, Aioli -- "disparate phenomena are one structure"
- **Breaking assumptions** (3/8): MAD, Mind the Gap, Strong Collapse -- "community assumed X; we prove not-X"
- **Simplification** (2/8): Demystified, Data Mixing Laws -- "alarming -> tractable math"

Our paper is cross-domain transfer (EWS ecology -> DNN) -- absent from corpus, a narrative differentiator.

## Hook Patterns (8/8, High)

Crisis framing dominates (5/8). Overused -- differentiate via cross-domain EWS angle. Others: aspiration gap (Plasticity), negative result (Aioli), technical puzzle (Mind the Gap).

## Intro Conventions (8/8, High)

3-8 paragraphs, median 5. End with numbered contributions (6/8), 2-4 items. Q1/Q2 "contract with reader" technique (Strong Collapse, Aioli) is effective: pose sharp questions, answer definitively.

## Figure 1 = Visual Thesis (8/8, High)

| Type | Count | Example |
|---|---|---|
| Problem illustration | 3/8 | MAD (artifact grid), Mind the Gap (eigenvalue scatter) |
| Method overview | 2/8 | Data Mixing Laws (pipeline), Aioli (3-panel thesis) |
| Teaser result | 2/8 | Demystified (theory vs data), Strong Collapse (Pareto) |
| Motivation | 1/8 | Plasticity (2D toy landscape) |

## Figure Density & Table Usage (8/8, High)

- **Figures**: 3-31 range, median ~7 in main text. Theory papers: 4-7. Empirical: 3-10.
- **Zero tables in theory papers** (6/8) -- all results as theorems + validation plots. The 2 exceptions (Data Mixing Laws, Aioli) are empirical systems papers using tables for method unification or baseline comparison.
- **If our paper is theory-leaning, tables are optional.**

## Viz Conventions (8/8, High)

- **Log-log plots** for scaling laws: dashed=theory, solid=empirical (3/8)
- **Multi-panel layouts** universal: 2-4 panels, each varying one dimension
- **Eigenspectrum density** for spectral papers: show spectrum shape evolution (2/8)
- **No bar charts**: 0/8 use bars for main results -- line plots dominate
- **Theory-experiment overlay** on same axes (4/8): the standard "our theory works" proof

## Figure Narrative Flow (6/8, High)

Consensus: **phenomenon -> theory -> validation -> nuance/mitigation** (4-stage).

## 5 Imitable Techniques

1. **Progressive complexity** (Tale of Tails): simplest model -> add realism. Apply: EWS on toy -> kernel -> LLM.
2. **Biological analogy** (MAD): "Model Autophagy Disorder" = mad cow. Acronym = adjective. Apply: cross-domain metaphor for spectral EWS.
3. **Q1/Q2 contract** (Strong Collapse): sharp questions, definitive answers. Apply: "Can EWS predict collapse? How early?"
4. **Warm-up then generalize** (Demystified): simple case -> full RMT. Apply: EWS on ridge -> deep nets.
5. **Negative result hook** (Aioli): "nothing beats baseline" -> "why?" -> framework. Apply: "existing metrics fail to predict X" -> EWS.
