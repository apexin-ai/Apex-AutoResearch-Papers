---
dream_id: dream_20260521T122458
tier: best
overall_score: borderline accept
timestamp: 2026-05-21T13:48:25.242144+00:00
---

# Review Report: Cross-Lingual Correctness Probes Reveal Architecture-Dependent Depth–Transfer Tradeoffs

**Venue**: ACL ARR (no venue specified; using ACL ARR 1–5 scale per [official review form](https://aclrollingreview.org/reviewform))

---

## Scores

| Dimension | Score | Label |
|-----------|-------|-------|
| **Soundness** | 4 | Strong: This study provides sufficient support for all of its claims. |
| **Excitement** | 4 | Exciting: I would mention this paper to others and/or make an effort to attend its presentation. |
| **Overall Assessment** | 4 | Conference: I think this paper could be accepted to an \*ACL conference. |
| **Confidence** | 4 | High |

---

## Paper Summary

This paper presents the first large-scale study of cross-lingual correctness probe transfer, spanning three architectures (Qwen3-235B MoE, Llama 4 Scout MoE, Gemma 4 31B Dense), 20 typologically diverse languages, and five transfer conditions. Four linked findings form a causal chain: (1) a positive depth–transfer trend with an architecture-dependent local Pareto tradeoff at deep layers; (2) a difficulty–capability decomposition revealing that the non-transferable capability component drives 86% of transfer degradation; (3) CaCLR, a calibration-aware regularization method that shifts the Pareto frontier by +3.3 pp AUROC without target-language labels; and (4) a Simpson's Paradox in the CKA–transfer relationship, where the sign of the correlation reverses when controlling for depth. Additional analyses include probing control tasks, linear projection sample efficiency, cross-benchmark generalization, quantization validation, and 52-language extension.

---

## Strengths

### S1. Unprecedented Scale and Systematic Design
The study is genuinely the first to examine correctness probe transfer at this scale: 3 architectures × 20 languages × 12–24 layers × 5 transfer conditions. The architecture selection is thoughtful — two MoE models (Qwen3, Llama4) plus one dense model (Gemma4) eliminate MoE routing as a necessary condition for the observed phenomena. Gemma 4 running in BF16 provides an unquantized anchor that removes quantization as a confound. This design directly addresses the most obvious reviewer objection ("is this just a MoE artifact?").

### S2. Coherent Causal Narrative
The four claims form a genuinely compelling logical chain: discover the phenomenon (Pareto tradeoff) → explain its mechanism (difficulty transfers, capability doesn't) → fix it (CaCLR targets the capability component) → provide geometric grounding (Simpson's Paradox). Each claim builds on the previous one, and the connections are not post-hoc rationalizations — CaCLR's depth profile (§5.3, Table 11 in appendix: +1.2 pp at 30% depth vs. +4.8 pp at 72% depth) directly mirrors the capability degradation profile from the decomposition (§5.2, Table 3 in review context: 0.5 pp at 20–30% depth vs. 8.8 pp at 75–90%). This cross-validation between independent analyses is strong evidence.

### S3. Rigorous Experimental Controls
The paper goes well beyond the minimum:
- **Probing control tasks** (Hewitt & Liang, 2019) quantify a 10% cross-lingual artifact rate, heavily concentrated in LOW-resource languages at deep layers. This is a field-level contribution — most cross-lingual probing studies do not run selectivity checks.
- **Random direction control** for the decomposition (−1.5 pp, vs. +4.5 pp for difficulty projection) confirms genuine structure.
- **Quantization validation** (rank correlation >0.995, CKA distortion <0.02) preempts a standard concern.
- **Multi-seed robustness** for CaCLR (±0.35 pp) and linear projection (±0.28 pp).

### S4. Practical Utility
The practitioner recommendations (§7) are specific and actionable: probe at 50–60% depth, use CaCLR with β=0.05 when parallel activations are available, fall back to ~40 parallel pairs for linear projection, apply Procrustes only when ZS AUROC < 0.52. The Procrustes reversal threshold (0.52 AUROC ↔ 0.35 CKA) connecting two independent analyses provides geometric consistency that strengthens both findings.

### S5. Simpson's Paradox Finding
The sign reversal from raw negative correlation (ρ = −0.38 to −0.42) to positive partial correlation (ρ = +0.41 to +0.48, all p<0.01) controlling for depth is non-trivial and genuinely surprising. This is replicated across all three architectures with bootstrap CIs excluding zero. The subspace angle analysis (12.8° within-layer vs. 37.5° cross-layer vs. 87.1° random) provides mechanistic grounding — the correctness direction is near-universal within layers but rotates substantially across layers, explaining why pooled CKA fails as a transfer predictor.

### S6. Complete Experiment Coverage
Cross-checking against the full experimental design, ALL planned experiments are reported: three full Pareto frontiers (§5.1), difficulty–capability decomposition (§5.2), CaCLR with ablations (§5.3), CKA/Simpson's analysis (§5.4), probing controls (§6.1), linear projection sensitivity (§6.2), orthogonality (§6.3), probe complexity (§6.4), cross-benchmark generalization (§6.5), quantization validation (§6.6), and extended 52-language coverage (§6.7). This is comprehensive.

---

## Weaknesses

### W1. No Figures in Current Draft (Major)
The paper contains zero figures — only tables. For a paper whose core contributions are geometric (Pareto frontiers, CKA heatmaps, Simpson's Paradox sign reversal, subspace angles, depth profiles), this is a critical omission. The planned visualizations described in the experimental design (Pareto frontier overlays, Simpson's Paradox 2-panel scatter, CKA × layer × language heatmaps, β sweep curves, depth profile comparisons) would dramatically improve readability and persuasiveness. A reader cannot currently assess the Pareto frontier shape, the CKA cliff steepness, or the Simpson's Paradox visual without reconstructing them mentally from tables. **This must be addressed before submission.**

### W2. "Causal Chain" Language is Overclaimed (Moderate)
The abstract and introduction frame the four findings as a "causal chain," but the evidence is correlational/observational:
- The decomposition (Claim 2) is a statistical projection, not a causal intervention. Projecting out the difficulty direction and observing improved ZS transfer does not establish that the capability component *causes* transfer degradation — it shows they are correlated after removing shared variance.
- The claim that "CaCLR's consistency loss directly targets the capability component" (Claim 3 linking to Claim 2) is inferred from parallel depth profiles, not from directly measuring CaCLR's effect on the capability vs. difficulty components.
- Recommend softening "causal chain" to "explanatory chain" or "linked findings" throughout. Alternatively, adding an explicit intervention experiment (e.g., training CaCLR on difficulty-projected residuals and showing diminished improvement) would strengthen the causal claim.

### W3. Architecture Attribution Confounded (Moderate)
The paper claims "architecture-dependent" tradeoff strength (Qwen3: 15/20 languages, Llama4: 10/20, Gemma4: 12/20) and attributes differences to MoE routing, model depth, and training recipes. However, the three models differ in many dimensions simultaneously: model family, parameter count (22B/17B/31B active), training data, tokenizer, number of layers (94/48/60), and quantization scheme. The current design cannot disentangle which factor drives the observed differences. The Limitations section acknowledges this ("cannot support causal attribution to specific architectural features"), but the main body's language ("Qwen3's steeper CKA cliff" attributed to "MoE routing") is stronger than the evidence supports. Consider adding explicit hedging in §5.1 and §5.4 when discussing inter-architecture differences.

### W4. CaCLR's "Zero Target-Language Labels" Framing Slightly Misleading (Minor)
The headline claim ("requiring zero target-language labels") is technically true but understates the data requirements. CaCLR requires parallel activations from GlobalMMLU translations (mean 2,800 items per language, range 1,900–4,100). While these are not *labels*, they are curated parallel data that may not exist for truly low-resource languages. The paper's own results show CaCLR hurts Yoruba (the lowest-resource language) due to translation quality. The abstract and conclusion should clarify this requirement more prominently.

### W5. Compressed Presentation of Additional Analyses (Minor)
Sections 6.1–6.7 cover seven distinct analyses in approximately 2 pages. While each is internally sound, the compression means:
- Linear projection sample efficiency (§6.2) reports the saturation curve and Procrustes reversal without showing the data (no table or figure in the main body).
- Correctness–confidence orthogonality (§6.3) and probe complexity (§6.4) are 4–5 sentences each with no tables.
- The 52-language extension (§6.7) — arguably one of the strongest universality claims — gets only 4 lines.

Consider either (a) promoting 1–2 of these to main-body results sections with proper figures/tables, or (b) moving them to a structured appendix with full tables. Currently they risk appearing as unsupported assertions.

### W6. Low-Resource Results Should Be More Explicitly Qualified (Minor)
The 28% artifact rate for LOW-resource languages (Table 8) is appropriately reported, but LOW-resource data still contributes to aggregate statistics throughout (e.g., "mean 20-language AUROC," "62% Pareto prevalence," Simpson's Paradox partial correlations). The paper states the core analyses are "primarily driven by HIGH and MID patterns" (§6.1), but does not report HIGH+MID-only versions of the key metrics. Providing these (even in a footnote) would strengthen the claim that the core findings are not contaminated.

### W7. MCQA-Only Evaluation (Minor, Acknowledged)
All experiments use MCQA (GlobalMMLU, Belebele, MMLU-ProX). Cross-benchmark generalization (§6.5, Table 9) is reassuring (CV=0.04), but all three benchmarks are MCQA with similar item structure. Extension to open-ended generation, where "correctness" is less cleanly defined, remains an open question. The Limitations section acknowledges this, so no action needed beyond noting it.

---

## Questions for Authors

1. **Decomposition causality**: Have you considered training CaCLR on the difficulty-projected residuals (§3.2) and measuring whether the improvement disappears? This would directly test whether CaCLR targets the capability component as claimed.

2. **HIGH+MID-only aggregate metrics**: What are the mean EN–ZS gap, Pareto prevalence, and Simpson's Paradox partial correlations when restricted to HIGH+MID languages (excluding the 4 LOW-resource languages with 28% artifact rate)?

3. **Mean-shift mathematical proof**: You claim ΔAUROC ≡ 0 under StandardScaler + LR and state this was "mathematically proven." Can you provide the proof or a citation? This is a strong claim that, if correct, distinguishes your setting from Xiao et al.'s.

4. **CaCLR vs. few-shot-100 fairness**: Few-shot-100 requires 100 labeled examples per language, while CaCLR uses ~2,800 parallel (unlabeled) items. Is this a fair comparison in terms of total annotation effort? How does CaCLR perform with a matched number of parallel items (e.g., 100)?

5. **Appendices A and B**: These appear as section headers with tables but no figures. Are the referenced main-body figures (mentioned as "Table 2 shows the Qwen3 Pareto frontier") intended to appear in a revision?

---

## Minor Issues

- **Table numbering**: Tables in the appendix are numbered 10–11, but the main body ends at Table 9. Tables in appendices are conventionally numbered as Table A1/B1 or continue but with clear appendix labeling.
- **Reference [9] (Miao & Ungar, 2026)**: Listed as "arXiv preprint." If this is unpublished concurrent work, clarify the relationship and whether findings were independently derived.
- **"Correctness probes" vs. "knowledge-boundary probes"**: The distinction from Xiao et al. [14] (answerability/input-level vs. correctness/output-dependent) is clearly stated in §2 but could be reinforced in §1 where [14] is first cited.
- **Section 7 "Why Mean-Shift Fails"**: This is a strong, clean theoretical result. Consider promoting it from Discussion to a lemma/proposition in §3 with a brief proof sketch.

---

## Detailed Experiment Coverage Assessment

| Planned Experiment | Paper Section | Tables | Status |
|---|---|---|---|
| Qwen3 Pareto Frontier (plan_001) | §5.1 | Table 1, 2, App. A (Table 10) | ✅ Full |
| Llama4 Pareto Frontier (plan_002) | §5.1 | Table 1 | ✅ Summary |
| Gemma4 Pareto Frontier (plan_008) | §5.1 | Table 1 | ✅ Summary |
| CKA / Simpson's Paradox (plan_011) | §5.4 | Tables 6, 7 | ✅ Full |
| CaCLR (plan_003) | §5.3 | Tables 4, 5, App. B (Table 11) | ✅ Full |
| Decomposition (plan_004) | §5.2 | Table 3 | ✅ Full |
| Linear Projection / Procrustes (plan_012) | §6.2 | — | ⚠️ No table |
| Control Tasks (plan_013) | §6.1 | Table 8 | ✅ Full |
| Orthogonality (plan_005) | §6.3 | — | ⚠️ Text only |
| Probe Complexity (plan_006) | §6.4 | — | ⚠️ Text only |
| Cross-Benchmark (plan_007) | §6.5 | Table 9 | ✅ Full |
| Quantization (plan_010) | §6.6 | — | ⚠️ Text only |
| Extended 52 Languages (plan_009) | §6.7 | — | ⚠️ Text only |

**Coverage**: 13/13 experiments reported. 8/13 have dedicated tables. 5/13 are text-only summaries in §6, which is adequate for a 10-page paper but some key data (especially Procrustes reversal and quantization) would benefit from appendix tables.

---

## Overall Assessment

This is a strong empirical contribution that opens a new research direction: systematic study of cross-lingual correctness probe transfer. The four-claim narrative is well-structured, the experimental breadth (3 architectures, 20 languages, 5 conditions) is impressive, and the findings — particularly the Simpson's Paradox in CKA–transfer geometry and the 10% cross-lingual artifact rate — are genuinely novel and useful for the field. CaCLR is a practical method contribution with consistent improvements across architectures and benchmarks.

The main weaknesses are (1) the complete absence of figures, which is a critical gap for a paper about geometric phenomena, and (2) overclaimed causal language that should be softened. Both are addressable in revision. The architecture attribution confound is inherent to the study design and honestly acknowledged in Limitations.

**Recommendation**: Accept to main conference contingent on adding figures and softening causal framing. The core findings are sound, novel, and impactful.
