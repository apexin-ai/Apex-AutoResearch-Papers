# Paper Framing: Property-Guided Per-Sample Filtering (PGPF)

**Status**: Draft — Phase 0 complete, updating based on results
**Target**: AAAI 2027 (abstract Jul 25, paper Aug 1)

---

## 1. Core Insight

Kovac et al. (EMNLP 2025) showed that three per-sample properties — lexical conformity, semantic novelty, and quality — predict the magnitude of model collapse in recursive synthetic training via regression analysis, but left these as diagnostic indicators with no operational use. PGPF bridges this diagnostic-to-operational gap: it is the first method to convert these predictive properties into actionable per-sample filtering criteria, demonstrating that manipulating the factors that predict collapse can mitigate it — a qualitative shift from "X predicts Y" to "manipulating X mitigates Y."

Positioning: empirical contribution, not a methodological breakthrough.

---

## 2. Core Claims

**C1.** PGPF filtering outperforms confidence-based filtering (Self-Verification, NeurIPS 2025) across recursive synthetic training generations.
[Requires experiments: Phase 1 three-generation filtered comparison, extended 10-generation case study]

**C2.** Augmenting confidence-based filtering with lexical conformity (LC) and semantic novelty (SN) provides complementary filtering signals that confidence alone cannot capture. The property space is effectively 3-dimensional: Quality (base PPL) and Confidence (ft log-prob) are rank-redundant (Phase 0: Spearman ρ = -0.998), while LC and SN are orthogonal to both (all |r|, |ρ| < 0.35).
[Supported by: Phase 0 correlation analysis ✓. Requires: Phase 1 PGPF-S vs Confidence-only comparison, Oracle single-scalar baseline]

**C3.** Optimal thresholds for each property evolve across generations, with property importance shifting as collapse progresses. *(Note: LC dynamic range was narrow in Phase 0 [0, 0.021]; C3's LC-specific sub-claims are conditional on Phase 1 confirming LC has meaningful filtering power.)*
[Requires experiments: PGPF-L threshold trajectory analysis, counterfactual ablation (disable one property per generation)]

**Wording constraints:**
- Use "dominant factor" / "primary predictor" — never "causal bottleneck"
- Use "generation-adaptive threshold optimization" — never "bilevel optimization"

---

## 3. Anticipated Reviewer Concerns + Mitigation

| Concern | Response Strategy | Supporting Experiment |
|---------|-------------------|----------------------|
| "Straightforward application" — novelty too low | Threshold trajectory analysis reveals surprising non-monotonic dynamics; counterfactual ablation shows property importance shifts across generations — these findings are non-obvious from Kovac et al.'s static regression | Threshold trajectory analysis + counterfactual ablation |
| "Properties may be highly correlated" — C2 may not hold | Phase 0 confirmed: Quality ≈ -Confidence (ρ=-0.998, mathematical inevitability of PPL vs log-prob). Honest disclosure + reframe to 3 effective dimensions. LC and SN genuinely orthogonal (|r|, |ρ| < 0.35) | Phase 0 ✓ |
| "Missing random filtering baseline" | Already included — Random baseline matched on retention rate isolates filtering signal from data reduction | MVP baseline #2 |
| "5 generations insufficient to claim collapse mitigation" | Extended 10-generation case study; quantify collapse magnitude at gen-5 to show effect size is already substantial | Extended experiments |
| "Computational overhead — is multi-property filtering worth it?" | Report wall-clock time and FLOPs for all variants; PGPF-S (static) is the practical recommendation with negligible overhead; PGPF-L (learned) is positioned as an analysis tool | Wall-clock + FLOPs comparison |
| "Metrics robustness — sensitive to k in top-k?" | k-sensitivity ablation with k ∈ {10, 25, 50, 100}; anchor semantic novelty computation to fixed gen-0 centroid to prevent drift | k-sensitivity ablation |
| "Model scale too small to generalize" | Kovac et al. used the same scale for their diagnostic analysis; we provide fair same-scale validation of their findings in an operational setting. Scaling is future work, explicitly acknowledged | Cite Kovac et al. scale precedent |
| "This is just hyperparameter search" | Generation-adaptive threshold optimization is framed as a practical engineering choice, not a novel optimization algorithm; the contribution is the filtering framework and empirical findings, not the search procedure | Framing only — no extra experiment needed |

---

## 4. Baselines

### MVP Phase (5 baselines)

| # | Baseline | Purpose |
|---|----------|---------|
| 1 | No Filter | Unmitigated collapse trajectory |
| 2 | Random (same retention rate) | Controls for data reduction effect |
| 3 | Confidence-only (Self-Verification, NeurIPS 2025) | Primary competing method — single-dimensional filtering |
| 4 | PGPF-S (static thresholds) | Practical recommendation — fixed thresholds across generations |
| 5 | Lexical-only | Ablation — strongest single property alone |

### Research Phase (3 additional)

| # | Baseline | Purpose |
|---|----------|---------|
| 6 | Oracle single-scalar | Kovac regression coefficients weight three properties into one scalar — tests C2 |
| 7 | Facility Location subset selection | Representative coreset method — structural alternative to property filtering |
| 8 | Kovac single-best-property | Best individual property from Kovac et al.'s regression — tests multi-property advantage |

---

## 5. Paper Positioning

**Contribution type:** Empirical method + analysis (not a pure method paper)

**Dual positioning:**
- **PGPF-S** = practical recommendation (static thresholds, negligible overhead, plug-and-play)
- **PGPF-L** = analysis tool (generation-adaptive thresholds, produces threshold trajectory insights)

### Differentiation

| vs. | Key Distinction |
|-----|-----------------|
| Self-Verification (NeurIPS 2025) | Augmenting confidence with collapse-predictive properties (LC, SN) vs. confidence alone |
| Shi et al. (NeurIPS 2025 Spotlight) | LLM text domain vs. vision/diffusion models |
| LSF / Cai et al. (AAAI 2026) | Collapse-specific properties grounded in predictive analysis vs. generic latent-space filtering |
| EUDS / QuaDMix / D3 | Recursive multi-generation evaluation vs. single-round data selection |
| Kovac et al. (EMNLP 2025) | Operational filter that mitigates collapse vs. diagnostic regression analysis that predicts it |
