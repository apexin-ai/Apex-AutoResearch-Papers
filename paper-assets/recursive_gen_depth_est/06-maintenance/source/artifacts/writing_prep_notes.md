# Writing Prep Notes — EMNLP ARR May 25
**Generated: 2026-05-15 | DDL: 2026-05-25 (10 days)**

## Related Work Section — Skeleton

### §2.1 Model Collapse & Recursive Generation
**Narrative**: Recursive training on synthetic data causes distribution degradation. Prior work characterizes *that* collapse happens; we address *measuring how deep*.

| Ref | Role |
|-----|------|
| Shumailov et al. (Nature 2024) | Foundational: tail erosion across recursive generations |
| Alemohammad et al. (ICLR 2024) | MAD framework: precision/recall tradeoff in autophagous loops |
| Dohmatob et al. (ICML 2024) | "Tale of Tails": tail narrowing (temp) vs tail cutting (top-k/top-p) |
| Dohmatob & Feng (ICLR 2025) | Strong collapse: even 0.1% synthetic fraction causes degradation |
| Gerstgrasser et al. (2024) | Data accumulation prevents collapse — important caveat for us |
| Drayson et al. (EMNLP 2025) | Detection-as-filter prevents collapse; per-generation analysis |
| Marchi et al. (ICASSP 2025) | T≠1 causes asymptotic degeneration — theoretical backing for our temp finding |

**Key transition sentence**: "These works assume depth is known a priori. We formalize depth *estimation* from text alone."

### §2.2 AI Text Detection
**Narrative**: Binary → continuous → ordinal progression. We sit at the ordinal end.

| Ref | Role |
|-----|------|
| Gehrmann et al. (ACL 2019) | GLTR: foundational statistical features (perplexity, rank, entropy) |
| Holtzman et al. (ICLR 2020) | Nucleus sampling + unreliable tail concept |
| Binoculars, Hans et al. (ICML 2024) | State-of-art zero-shot binary detection |
| Fast-DetectGPT, Bao et al. (ICLR 2024) | Efficient zero-shot binary via curvature |
| DivEye, Basani & Chen (ICLR 2026) | Surprisal diversity features — closest feature overlap |
| LOKI (ICLR 2025) | Multimodal detection benchmark |
| EditLens, Thai et al. (ICLR 2026) | Continuous editing extent — closest conceptual neighbor |
| Kirchenbauer et al. (ICML 2023) | Watermarking (proactive, requires generator cooperation) |

**Key transition**: "Binary detectors discard ordinal information; EditLens estimates single-pass editing, not recursive depth. We address a complementary axis."

### §2.3 Decoding Strategies & Text Properties
**Narrative**: Strategy shapes text statistics — critical for our 3-strategy benchmark.

| Ref | Role |
|-----|------|
| Holtzman et al. (ICLR 2020) | Nucleus sampling proposal |
| Finlayson et al. (ICLR 2024) | Truncation vs scaling: mechanistic difference |
| Garces Arias et al. (COLING 2025) | Model-dependent optimal decoding — validates our D006 |
| Wiher et al. (TACL 2022) | Task-dependent strategy effects |
| Basu et al. (ICLR 2021) | Mirostat: perplexity-sampling non-linearity |

### §2.4 Ordinal Classification Methods
**Narrative**: Brief — methods are tools, not contributions.

| Ref | Role |
|-----|------|
| CORAL, Cao et al. (2020) | Rank-consistent ordinal regression baseline |
| CLOC, Pitawela et al. (CVPR 2025) | Contrastive ordinal learning — DCOL basis |

---

## Per-Claim Citation Support

### Claim 1: Ordinal depth estimation is feasible (70-85% accuracy)
- **Task novelty**: No direct competitor (literature scan confirms)
- **Method**: CORAL (Cao 2020), RF baselines, DivEye features (Basani 2026)
- **Context**: vs binary detectors (Binoculars, Fast-DetectGPT, GLTR)

### Claim 2: Depth Degradation Atlas (PRIMARY)
- **(a) p90_ppl/var_surprisal as dominant features**: DivEye (feature overlap), GLTR (feature lineage)
- **(b) Non-uniform inter-depth distances**: Shumailov (tail erosion monotonic), Dohmatob (scaling law changes)
- **(c) EDD boundary**: Novel — no prior work defines this metric
- **(d) Strategy-dependent trajectory reversal**: Garces Arias (model-dependent strategies), Dohmatob "Tale of Tails" (tail narrowing vs cutting)
- **(e) Accelerated convergence (covariate shift)**: Marchi (T≠1 degeneration), Sugiyama (covariate shift theory), Holtzman (unreliable tail)

### Claim 3 (Discussion): Depth-graduated curation
- **Motivation**: DSIR (Xie 2023), QuRating (Wettig 2024)
- **Context**: Gerstgrasser (accumulation prevents collapse), Falahati (curated data doesn't collapse)

### DCOL Section (negative result or bonus)
- **Method basis**: CLOC (Pitawela, CVPR 2025)
- **If negative**: Frame as "contrastive ordinal learning limitations for text depth" — cite CLOC's success on image ordinal tasks to contrast

---

## Figures Checklist (Dream D002: ≥4 figures)

1. **Fig 1**: Atlas heatmap — 3×3 grid, feature×depth trajectory
2. **Fig 2**: AUC decay curves across depth pairs + EDD threshold line (T=0.75)
3. **Fig 3**: Feature trajectory panel — top-5 features × depth, stratified by model
4. **Fig 4**: Confusion matrix heatmap (best config: OLMo temp09)
5. **Fig 5** (optional): Cross-strategy covariate shift visualization (temp09 feature distributions overlaid on nucleus/topk)

---

## Missing / Action Items

- [ ] Verify Marchi et al. (2024) arXiv number: 2404.02325
- [ ] Get full author list for knowledge_collapse2025 and synthetic_eggs2026
- [ ] Check if Gerstgrasser et al. has been published at a venue (was arXiv in 2024)
- [ ] Finalize DCOL section framing based on v6 RoBERTa results
- [ ] Cross-reference all 33 entries against final .bib file
- [ ] Ensure ≥25 unique references in final bibliography
