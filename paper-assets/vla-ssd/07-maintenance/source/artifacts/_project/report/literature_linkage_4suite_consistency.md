# TracVLA 4-Suite Consistency: Literature Linkage Report

**Date**: 2026-05-21

---

## Summary (< 200 words)

**No direct competitor** reports cross-task/cross-suite attention head consistency in VLA models. The existing literature map (Grant 2026, Swann 2026, Haon 2025 等) focuses on behavioral intervention, SAE features, or activation steering — none tracks specific head indices across task suites.

**h13/h22 universal mixed heads** lack direct precedent. The closest references are: (1) **Olsson et al. 2022** — induction heads as universal circuits across model scales, but these are algorithmic (pattern-matching), not routing-functional; (2) **Basile et al. 2025** (Head Pursuit, NeurIPS 2025 spotlight) — shows consistent head specialization in multimodal transformers, editing 1% of heads controls output, but does not track same-index heads across tasks; (3) **Bali et al. 2026** — finds middle-layer heads are *least* stable across independent training runs, which actually *strengthens* our claim: h13/h22 consistency is a training-induced convergent property within a model, not a trivial artifact of initialization.

**3 papers recommended for literature_map.yaml** (see below). No paper discovers convergent routing with head identity preservation across task suites — this remains our unique contribution.

---

## Detailed Analysis

### 1. Direct Competitor Check

Scanned all 9 direct-competitor entries in literature_map.yaml. None reports:
- Cross-suite attention pattern consistency
- Specific head indices with consistent function across tasks
- Convergent routing (CF ordering, R² inverted-U, exit collapse) across suites

**GuidedVLA (Jia et al., May 2026)** is the only VLA paper explicitly about attention head specialization, but they *engineer* it (supervised auxiliary signals for object/spatial/temporal heads), not *discover* it emergently. This is a useful contrast: we show VLA training naturally produces convergent routing without explicit supervision.

### 2. h13/h22 Head Identity Preservation — Literature Support

| Reference | Finding | Relation to h13/h22 |
|-----------|---------|---------------------|
| Olsson et al. 2022 | Induction heads are universal circuits across model scales | Precedent for functional universality at head level, but algorithmic (copy mechanism), not routing |
| Basile et al. 2025 (Head Pursuit) | Consistent head specialization in multimodal transformers; 1% head editing controls output | Supports head-level functional specialization as real phenomenon; no same-index tracking across tasks |
| Bali et al. 2026 | Middle-layer heads least stable across training runs, most representationally distinct | **Key contrast**: instability across runs ≠ instability across tasks within a run. Our h13/h22 consistency is *within-model cross-task*, a distinct (stronger) claim |
| Bahador 2025 | ViT fine-tuning: deeper heads more important, intermediate heads monosemantic | Layer-level stratification consistent with our L1 instruction-dominant finding |
| Yang et al. 2026 (TAPPA, ICLR 2026) | Unifies attention patterns via temporal predictability; predictable vs unpredictable patterns | Theoretical framework for *why* certain heads develop consistent patterns |

**Bottom line**: Head specialization is well-established. Head identity preservation *across task suites within a fine-tuned VLA* is not. Our h13/h22 finding sits in a gap between "heads specialize" (known) and "the same heads specialize the same way across diverse tasks" (novel).

### 3. Convergent Routing Pattern — Novelty Position

The full convergent routing pattern (CF ordering + R² inverted-U + exit collapse + L1 instruction dominance) across 3 architectures × 4 suites has no precedent. The closest work:
- **Grant 2026**: Cross-architecture comparison but of *different* properties (vision dominance, language ignoring), not routing convergence
- **Bali 2026**: Cross-run stability, not cross-task consistency
- **Head Pursuit**: Cross-task head specialization in VLMs, not VLAs, and no routing pattern analysis

---

## Suggested literature_map.yaml Entries

### Entry 1: bali2026

```yaml
- id: bali2026
  title: "Quantifying LLM Attention-Head Stability: Implications for Circuit Universality"
  authors: "Karan Bali, Jack Stanley, Praneet Suresh, Danilo Bzdok"
  year: 2026
  venue: "arXiv preprint"
  arxiv_id: "2602.16740"
  category: method-component
  role: context
  key_findings: >
    Systematically quantifies attention head stability across independently initialized training runs.
    Middle-layer heads are least stable yet most representationally distinct. Deeper models show
    stronger mid-depth divergence. Weight decay improves stability. Residual stream comparatively stable.
  relevance_to_us: >
    Key contrast paper for h13/h22 universality claim. Their finding that heads are unstable across
    training runs strengthens our claim: h13/h22 cross-task consistency is a training-induced convergent
    property, not a trivial initialization artifact. Cross-run instability ≠ cross-task instability.
  novelty_gap: >
    Studies pre-trained LLMs across random seeds, not fine-tuned VLAs across task suites.
    No cross-task consistency analysis within a single trained model.
```

### Entry 2: basile2025_headpursuit

```yaml
- id: basile2025_headpursuit
  title: "Head Pursuit: Probing Attention Specialization in Multimodal Transformers"
  authors: "Lorenzo Basile, Valentino Maiorca, Diego Doimo, Francesco Locatello, Alberto Cazzaniga"
  year: 2025
  venue: "NeurIPS 2025 (Spotlight)"
  arxiv_id: "2510.21518"
  category: method-component
  role: methodology
  key_findings: >
    Consistent head specialization patterns in unimodal and multimodal transformers.
    Signal processing-based method (SOMP) identifies semantic specialization per head.
    Editing 1% of heads reliably suppresses/enhances targeted concepts.
    Validated across QA, toxicity, image classification, captioning.
  relevance_to_us: >
    Strongest methodological support for head-level specialization as real phenomenon.
    Their cross-task validation (QA + toxicity + vision tasks) parallels our cross-suite validation.
    However they do not track same-index heads across tasks — our h13/h22 identity preservation goes further.
  novelty_gap: >
    VLM focus, not VLA. No routing pattern analysis. No trained vs untrained comparison.
    Does not track whether same head indices serve same function across tasks.
```

### Entry 3: olsson2022_induction

```yaml
- id: olsson2022_induction
  title: "In-context Learning and Induction Heads"
  authors: "Catherine Olsson, Nelson Elhage, Neel Nanda, et al."
  year: 2022
  venue: "arXiv preprint (Anthropic)"
  arxiv_id: "2209.11895"
  category: method-component
  role: context
  key_findings: >
    Induction heads implement match-and-copy ([A][B]...[A]→[B]) and are mechanistic source of
    in-context learning. Emerge at same training point as ICL ability phase transition.
    Universal across model scales — canonical example of circuit-level universality.
  relevance_to_us: >
    Classic precedent for "specific heads with universal function across contexts."
    Our h13/h22 mixed heads are analogous: specific heads with consistent routing function across
    task suites. Induction heads = algorithmic universality; our finding = routing universality in VLAs.
  novelty_gap: >
    Purely LLM, not VLA. Induction is a copying mechanism, not multimodal routing.
    No cross-task consistency analysis in the fine-tuning setting.
```

---

## Action Items

1. **Add 3 entries above to literature_map.yaml** under appropriate categories (bali2026 + basile2025 → method-component; olsson2022 → method-component)
2. **Update categories index** to include new papers
3. **Paper framing**: The h13/h22 finding can be positioned as "convergent routing heads" — extending the induction head universality concept (Olsson 2022) from algorithmic circuits to multimodal routing in VLAs, with the Bali 2026 cross-run instability result as a foil that highlights the within-model cross-task nature of our claim
