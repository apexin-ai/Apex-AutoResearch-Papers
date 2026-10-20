---
name: gen-depth-contamination research patterns
description: Experimental consensus, baselines, metrics, competitor landscape, and gaps from 21 model-collapse / contamination-detection papers (2019-2026).
---

## Experimental Design Consensus

**Replace vs Accumulate is the central axis.** Replace causes collapse; accumulate prevents divergence. Any collapse claim must specify paradigm. (7/10, 高, Schaeffer 2025, Kazdan 2025)

**Generation depth as x-axis.** 3-100 iterative gens; degradation within 3-5 is consensus. Dohmatob formalizes as linear error accumulation n*T0^(-c). (6/10, 高)

**Tail loss is the mechanism.** Dohmatob: tail cutting causes scaling plateaus; Shi: entropy collapse r=0.91; Shumailov: tail coverage vanishes. Theory, empirics, info-theory converging. (4/10, 高)

**Modality gap.** Image and text collapse studied independently; no cross-modal paper. (10/10, 高)

## Baselines & Metrics

**Collapse:** Perplexity/NLL (text), FID (image), diversity (MAUVE/Self-BLEU/entropy), precision/recall. Entropy rising as proxy. Scaling law exponents emerging (Dohmatob).

**Detection:** AUROC primary. Two tiers: dataset-level (CoDeC 99.9%) vs sample-level (Min-K%++ 78.3% WikiMIA). Benchmarks: WikiMIA, MIMIR, MAGE, RAID.

## Competitor Landscape

**Grey-box detection:** CoDeC (ICL-based, 99.9% dataset AUC, parameter-free) and Min-K%++ (z-score, ICLR'25 Spotlight, sample-level). Both need logit access.

**Black-box/supervised:** DivEye (surprisal, TMLR'26), Feature-augmented DeBERTa (Mady 2026), Disentangled representations (Pu 2026, +24.2%).

**Collapse mitigation:** SIR+detector beats oracle (Drayson), entropy-max selection (Shi, 41% FID gain), weak-signal boosting (Amin), surplexity (Gambetta), multi-reward curation (Falahati ICML'26), clean data grokking (Dohmatob).

**Data curation:** D4 (dedup+diversify, 18-20% at 6.7B), DSIR (importance resampling), DoReMi (DRO reweighting, 2.6x at 8B).

## Common Limitations

1. Scale gap: ≤7B; frontier unknown (7/21)
2. Fine-tuning proxy, not pre-training (4/21)
3. Logit access for detection (4/7)
4. Single-source loops ≠ multi-source web contamination (6/10)

## Research Gaps (0/21)

1. **Depth-aware detection:** difficulty as f(generation depth)
2. **Depth estimation:** how many generations deep
3. **Multi-source contamination:** multi-model, multi-domain
4. **Detection-curation co-optimization:** only Drayson connects, no joint objective
5. **Scaling theory + practical filtering:** bridging Dohmatob's theory with detection pipelines
