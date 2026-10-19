# LLM Activation Sparsity — Writing Patterns (8 deep-read papers, 2024–2026)

## Story Type

**化繁为简** (5/8): Frame method as simpler solution to overcomplicated landscape. TEAL: "magnitude thresholding, no training." R-Sparse: "sparse+low-rank, training-free." **突破局限** (3/8): Identify specific failure and fix it. SPON fixes accuracy loss; Polar Sparsity fixes batch scaling. Source: cross-paper. Confidence: high.

## Introduction

**4 paragraphs** (4/8): P1=problem+hook, P2=gap, P3=method+insight, P4=contributions. TEAL/Compact LM exemplify — under 1 page. **Numbered contribution list at intro end** (6/8), 3–4 items typical. Confidence: high.

**Hook patterns**: Memory-bound inference (4/8, safest); visual-first with Figure 1 in intro (2/8, SPON/Polar Sparsity — effective when observation is visually compelling); contrarian framing (1/8, ReLU Strikes Back). Confidence: high.

## Figure 1

**Motivation figure** (3/8, dominant): Show problem empirically — heatmap (R-Sparse), decay curve (SPON), latency breakdown (Polar Sparsity). **Method+teaser combo** (2/8): architecture left, result bar right (IF-Pruning). **Teaser result** (2/8): upfront perf comparison (Compact LM). Field prefers figures that make reader *see* the problem before reading about it. Confidence: high.

## Result Tables

Rows=methods by_category, cols=benchmarks. Bold best, single-run (8/8 unanimous). 3–8 baselines. **Include one catastrophic failure baseline**: TEAL shows ReLUfication PPL>1e4; R-Sparse shows 35% accuracy. This "devastating contrast" appears in 3/8 papers. Confidence: high.

## Signature Visualizations

**Sparsity-accuracy line plot** (4/8): X=sparsity%, Y=accuracy/PPL. The field's canonical figure type. Shows degradation curve and identifies operating point. Source: TEAL, R-Sparse, Polar Sparsity. Confidence: high.

**Ablation tables**: full_numbers (6/8); checkmark_grid rare (2/8); delta_from_base: 0/8. Confidence: high.

## Techniques to Imitate

1. **Distributional analysis** (2/8): TEAL's Laplacian analysis transforms "why would this work?" into inevitability. R-Sparse's contribution heatmap makes decomposition obvious. When method seems too simple, show structural reason it must work.

2. **Honest limitation figures** (2/8): TEAL dedicates Figs 8–9 to batch size and prefill limits. Builds trust.

3. **Best practices checklist** (1/8): Compact LM's "10 best practices" transforms empirical study into memorable guide. Effective with many ablation dimensions.

## Figure Budget

Median 9 figures. Main paper 4–6, rest in appendix. IF-Pruning: ICML with only 3 figures. Tables: 2–4 main, ablation in appendix. Split: main="what works", appendix="how we know."
