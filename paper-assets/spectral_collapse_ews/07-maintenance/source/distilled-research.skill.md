---
name: distilled-research
description: "Spectral collapse & model collapse research landscape: metrics, methods, gaps from 23 papers"
scope: project
version: 2
tags: [distilled, auto-generated]
distilled_from:
  paper_count: 23
  paper_keys: [tale_of_tails, self_consuming_mad, collapse_demystified, strong_model_collapse, mind_the_gap, spectral_collapse_plasticity, data_mixing_laws, aioli, false_promise, doremi, pythia, ai_models_collapse_nature, collapse_inevitable, sigma, collapse_or_thrive, beyond_collapse, knowledge_collapse, effective_rank, implicit_self_regularization, early_warning_signals, dl_early_warning, methods_detecting_ews, llm_self_consuming]
  last_distilled: "2026-05-24T09:00:00Z"
---

## Spectral Metric Zoo -- Disambiguate

5 definitions of "spectral collapse" in this corpus. Conflating them invites rejection.

| Definition | Object | Metric | Source |
|---|---|---|---|
| Width rank collapse | Attention eigenvalues | stable rank | Mind the Gap (ICML'25) |
| Hessian collapse | Loss Hessian | epsilon-rank(H) | Spectral Collapse Plasticity (NeurIPS'25) |
| Gram contraction | Embedding Gram matrix | spectral bounds | SIGMA (arXiv'26) |
| Heavy-tail shape | Weight SVD | power-law alpha | Martin & Mahoney (JMLR'21) |
| Effective dimensionality | Singular values | erank = exp(H(sigma)) | Roy & Vetterli (EUSIPCO'07) |

5/23 papers. High. Our project: weight SVD + Martin/Vetterli lineage, distinct from Hessian competitor.

## Model Collapse Theory Consensus

- **Linear in n**: E = E_clean + Delta + n*C (3/23: Tale of Tails, Demystified, Strong Collapse. High)
- **Even 1% synthetic harms**: zeta ~ Omega(p2^2 * c^2); p2 must -> 0 (2/23: Strong Collapse, Nature'24. High)
- **Tail truncation is mechanism**: top-p/temperature cuts heavy tails, breaks scaling laws (2/23: Tale of Tails, MAD. High)
- **Accumulation prevents collapse**: keep all generations -> bounded; replacement -> divergence (3/23: Collapse Inevitable, Collapse or Thrive, MAD. High)

## EWS from Ecology -> ML Transfer

Classical indicators: autocorrelation-at-lag-1, variance, spectral reddening, Kendall tau (Scheffer Nature'09, Dakos PLOS'12). LSTM beats classical on simulated bifurcations (Bury PNAS'21). 3/23, High.

**Core gap**: Zero papers apply EWS to weight spectrum time series. This is our novelty.

## Methodology & Evaluation Norms

- **Proof pipeline** (6/8 deep-read, High): theorem on tractable model -> synthetic Gaussian validation -> real model (LLM/ImageNet). RMT is shared theory; ridge regression the standard proxy.
- **Validation ladder**: Synthetic toy -> MNIST -> real-scale (6/8). Perplexity (LLM) / FID+P/R (images) / test error (theory) -- no universal collapse metric.
- **Reporting**: 3-5 seeds, mean +/- std or 95% CI (5/8).

## Competitive Map

- **Foundation** (build on): Tale of Tails, MAD, Demystified, Strong Collapse, Mind the Gap -- collapse theory
- **Competitor**: Spectral Collapse Plasticity (Hessian, continual learning), SIGMA (Gram, static) -- spectral monitoring but different objects/purposes
- **Complementary**: Data Mixing Laws, Aioli, DoReMi -- data-side; we do model-side monitoring

## Shared Limitations -> Our Openings

- "Theory limited to linear/kernel models" (4/8) -> extending spectral EWS to Transformers
- "Post-hoc or init-only analysis" (5/8) -> real-time monitoring during training
- "Single modality" (6/8) -> cross-architecture collapse comparison

## 3 Key Gaps

1. No real-time spectral EWS during training. Gap: 23/23.
2. EWS theory (ecology) never applied to DNN dynamics. Gap: all papers disconnected.
3. No Transformer spectral monitoring during training (Mind the Gap = init; Plasticity = MLP). Gap: 2 nearest miss.
