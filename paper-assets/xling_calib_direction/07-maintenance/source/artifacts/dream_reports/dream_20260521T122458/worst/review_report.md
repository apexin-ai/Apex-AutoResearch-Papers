---
dream_id: dream_20260521T122458
tier: worst
overall_score: Resubmit next cycle (Overall: 2, Soundness: 3, Excitement: 2)
timestamp: 2026-05-21T14:01:21.373138+00:00
---

# Review Report: Cross-Lingual Correctness Probe Transfer

**Venue**: EACL via ACL Rolling Review  
**Scoring rubric**: ACL ARR 1–5 scale (Soundness / Excitement / Overall)

---

## 1. Paper Summary

This paper presents the first large-scale study of cross-lingual correctness probe transfer, testing whether English-trained correctness directions in LLM representations generalize to 20 typologically diverse languages across three production architectures (Qwen3-235B MoE, Llama 4 Scout MoE, Gemma 4 31B Dense). The findings are predominantly negative: pilot-study patterns do not generalize, distributional matching methods (CaCLR, CORAL, high-dimensional MMD) all fail, CKA's Simpson's Paradox is a small-sample artifact, and difficulty–capability decomposition is indistinguishable from random projection. Two positive contributions remain: a control task methodology warning revealing 35% of cross-lingual probe results are capacity artifacts, and conditional linear projection guidance showing Procrustes alignment is the only viable label-free method (with ≥100 parallel pairs).

---

## 2. Strengths

**S1. Important negative results with broad field implications.** The systematic closure of distributional matching paths (MMD 1-D/50-D/100-D, CORAL 1-D/50-D) is thorough and convincing. By testing multiple distributional alignment methods across multiple dimensionalities, the paper forecloses the easy objection "just try a different kernel/higher dimension." The theoretical grounding via Zhao et al.'s conditional distribution mismatch argument is apt. This can genuinely save the community from pursuing dead-end research directions.

**S2. Control task methodology extension is the standout contribution.** Extending Hewitt & Liang's selectivity framework to cross-lingual probing for the first time, and finding a 35% overall artifact rate (LOW: 42%, MID: 31%), is a significant methodological contribution. The finding that MID-resource languages are also substantially affected (tr: 0.031, th: 0.028, vi: 0.042 selectivity) is non-obvious and challenges the assumption that artifact problems are confined to low-resource settings. The selectivity–AUROC correlation (ρ=0.65) is a sharp finding with clear implications: published positive cross-lingual probing results may partially reflect capacity artifacts.

**S3. Mean-shift impossibility proof is clean and mathematically rigorous.** Under StandardScaler + logistic regression, mean-shift adds a constant offset that preserves ranking, hence ΔAUROC ≡ 0 by construction. This is an elegant, brief proof that clarifies a methodological point. Verified across all 60 model–language combinations.

**S4. Comprehensive experimental coverage.** Three architectures spanning both MoE and dense paradigms, 20 languages across three resource tiers, five transfer conditions, and extensive ablations (β sweep, component ablation, multi-seed, mixed β criterion). The paper covers 13 distinct experimental plans comprehensively. The inclusion of Gemma 4 (BF16, unquantized) as a quantization-free control is a thoughtful design decision.

**S5. Honest and transparent framing.** The paper does not oversell its negative results. The abstract clearly states "predominantly negative but informative." The discussion section candidly explains why pilot results failed to generalize. This intellectual honesty is commendable and relatively rare.

**S6. CaCLR component ablation is a model of negative-result rigor.** Table 8 showing that BCE-only retraining ≈ ZS baseline, and every additional component (SB-ECE, MMD, CORAL) is net-negative, convincingly rules out hyperparameter tuning as an explanation. Multi-seed evaluation (std=0.003) and mixed β criterion further eliminate confounds.

---

## 3. Weaknesses

**W1. Broken LaTeX citations — critical formatting failure.** Multiple unresolved "??" citations appear on page 1 (Introduction): "internal representations **??**", "worse calibration **?**". Table cross-references also show "??" (§4 references "Tables ??, ??, ??"). This is a serious submission-readiness issue that suggests insufficient proofreading. For a venue submission, this alone would warrant desk rejection at many conferences.

**W2. Complete absence of figures.** The paper is entirely tables and text — no figures whatsoever across 11 pages. For a paper with rich multi-dimensional data (20 languages × 3 architectures × multiple layers × multiple conditions), visualization is essential. Pareto scatter plots, CKA heatmaps, selectivity heatmaps, saturation curves, and β sweep curves would dramatically improve readability and make the negative results more convincing. Readers cannot assess patterns like "non-monotonic depth–transfer relationships" or "MoE expert routing artifacts" from tables alone. The experiment design describes 15+ figures (Figures 1a–8c plus appendix figures) that are entirely missing from the paper.

**W3. Architecture confound in Pareto analysis (§5).** The paper tests 2 MoE models + 1 dense model and concludes "the Pareto tradeoff is architecture-conditional." But with n=2 MoE and n=1 dense, this is severely underpowered for a claim about architectural classes. The "MoE routing breaks Pareto" narrative is plausible but based on observing that both MoE models lack Pareto while the one dense model shows marginal Pareto — this could be a coincidence correlated with other architecture-specific factors (model family, training data, quantization scheme). The paper needed at least one more dense model (e.g., Llama 3.1 70B) to make the architecture-conditional claim credible.

**W4. Llama 4 Scout results underreported.** While Table 1 gives detailed per-language Qwen3-235B results and Table 2 provides the 3-architecture comparison summary, Llama 4 Scout's per-language depth–transfer Spearman correlations are summarized in only two sentences in §5.1 ("global ρ = −0.06, 0/20 per-language significant, 8/20 non-monotonic"). The full per-language table for Llama 4 Scout is absent. Given that the design doc specifies a full Table 2a for Llama 4 Scout, this omission leaves the reader unable to verify the claims or examine language-specific patterns.

**W5. Difficulty decomposition section (§8) is underpowered and brief.** The IRT difficulty probe achieves only R²=0.28, meaning the linear projection captures less than a third of difficulty variance. The "projecting out difficulty" approach was structurally unable to succeed — projecting out 28% of difficulty variance while likely damaging correctness signal is a known limitation of low-R² projections. The paper acknowledges this but treats it as a finding rather than a methodological limitation of the approach. A reader might reasonably argue that a better difficulty model (e.g., nonlinear) could yield different conclusions. The random-direction control (paired test p=0.38) is the right check but the section feels rushed at ~half a page.

**W6. Linear projection practical guidance is weak.** The paper's recommendation — "apply projection when ZS AUROC < 0.50 (likely beneficial), avoid when > 0.65 (likely harmful), validate in between" — is a conditional recommendation with a wide inconsistent zone (0.53–0.62, ±0.08 across languages). Table 13 shows Japanese (HIGH, 0.588) helped while Korean (MID, 0.589) hurt at nearly identical ZS AUROCs. This makes the "guidance" difficult to operationalize. The saturation analysis (≥100 pairs needed, not 50) is useful but the overall practical contribution is modest.

**W7. CKA analysis could be more nuanced.** The Simpson's Paradox falsification (§6) is well-executed, but the conclusion "CKA provides no explanatory power beyond depth" may be too strong. With partial correlations at n=20 per layer (same-layer analysis), statistical power is limited. Gemma4's partial ρ=+0.16 (p=0.09, bootstrap CI [-0.02, 0.33]) is tantalizing — the CI barely crosses zero. A Bayesian analysis or meta-analytic combination across architectures might reveal a small but genuine effect. The paper should at least acknowledge the power limitations rather than asserting a clean null.

**W8. Appendices are too compressed.** Appendix D (Extended Language Coverage, 52 languages) is a single paragraph. Appendix A (Probe Complexity) is one table + one sentence. These feel like placeholders rather than complete analyses. If the 52-language extension doesn't change conclusions, it's fine to be brief, but the paper promises it "strengthens the control task finding" without showing the supporting data.

**W9. Related work is thin.** Section 2 is approximately half a page covering five brief paragraphs. For a paper that claims field-level methodological implications, the related work should more thoroughly discuss: (1) existing cross-lingual probing literature that the 35% artifact rate puts in question — which specific papers? (2) other negative results papers in NLP probing (e.g., Belinkov's survey, Pimentel et al.'s information-theoretic perspective), (3) domain adaptation theory beyond the one-line Zhao et al. mention.

**W10. No statistical correction for multiple comparisons.** The paper conducts many parallel statistical tests (20 languages × 3 architectures × multiple conditions) but does not mention any correction for multiple comparisons (e.g., Bonferroni, FDR). The claim that "1/20 languages reaches significance" (Table 1) should be contextualized — at α=0.05 with 20 independent tests, ~1 false positive is expected by chance. Hindi's p=0.046 may well be a false positive.

---

## 4. Questions for the Authors

**Q1.** The mean-shift impossibility (§4) relies on StandardScaler + logistic regression. How does mean-shift behave under other preprocessing pipelines (e.g., min-max scaling, no scaling, PCA-reduced features)? The paper mentions distinguishing from Xiao et al.'s pipeline but doesn't test alternative preprocessings.

**Q2.** For the control task analysis (§9), how were random labels generated? Was the control task permutation repeated multiple times, or is the permuted AUROC based on a single permutation? Bootstrap confidence intervals on selectivity would strengthen the artifact rate claims.

**Q3.** The β sweep (Table 6) shows monotonic degradation with increasing β. Did you explore annealing β during training (e.g., starting at 0 and increasing), which is standard practice in domain adaptation? The current sweep uses fixed β throughout training.

**Q4.** For the subspace angle analysis (Table 5), what is the dimensionality of the "correctness direction"? Is this a single vector (the LR weight vector), or a subspace? If single-vector, the angles 15°–65° have a very different interpretation than for multi-dimensional subspaces.

**Q5.** The paper uses GlobalMMLU for all languages. Are the translations machine-translated or human-translated? Translation quality could be a major confound for the LOW-resource artifact rates — if LOW-resource translations are noisy, the probe's inability to distinguish correctness may reflect translation quality rather than representation structure.

---

## 5. Missing References and Related Work

- The paper cites "Burns et al." and "Miao et al." but with broken references ("??"). These must be resolved.
- Missing discussion of Pimentel et al. (2020) "Information-Theoretic Probing with Minimum Description Length" — relevant to the control task methodology.
- No mention of Conneau et al.'s extensive cross-lingual probing work (e.g., "What you can cram into a single vector") which established many of the cross-lingual probing paradigms this paper critiques.
- Domain adaptation theory (§2) cites Ben-David et al. and Zhao et al. but omits Ganin et al. (domain-adversarial networks) and Long et al. (deep adaptation networks) — these are the methods most analogous to CaCLR's approach.
- The probe-based calibration paragraph should cite Kadavath et al. (2022) on LLM self-knowledge and Li et al. on inference-time intervention, which are closely related to correctness direction extraction.

---

## 6. Experiment Coverage Assessment

All 13 planned experiments are represented in the paper, but with uneven depth:

| Experiment | Coverage | Adequacy |
|---|---|---|
| Qwen3 Pareto (plan_001) | Full table + analysis | ✓ Adequate |
| Llama4 Pareto (plan_002) | Text summary only, no per-language table | ✗ Insufficient |
| Gemma4 Pareto (plan_008) | Summary table + comparison | ✓ Adequate |
| CaCLR (plan_003) | Three tables, thorough ablation | ✓✓ Strong |
| Decomposition (plan_004) | One table, half page | ~ Compressed |
| Orthogonality (plan_005) | One paragraph in §11.1 | ✗ Minimal |
| Probe complexity (plan_006) | Appendix table | ✓ Adequate for appendix |
| Benchmarks (plan_007) | Appendix table | ✓ Adequate for appendix |
| 52 languages (plan_009) | One paragraph | ✗ Minimal |
| Quantization (plan_010) | Appendix table | ✓ Adequate for appendix |
| CKA (plan_011) | Two tables + analysis | ✓ Adequate |
| Linear projection (plan_012) | Two tables + analysis | ✓ Adequate |
| Control tasks (plan_013) | Two tables + analysis | ✓✓ Strong |

**Critical gap**: 15+ figures described in the design doc are entirely absent from the paper. The paper is figure-free, which dramatically reduces its visual communication and persuasive power.

---

## 7. Scores

### Soundness: 3 (Acceptable)

The main claims are supported by the data presented. The mean-shift proof is mathematically clean. The CaCLR ablation is thorough and convincing. The control task methodology is properly executed. However: (1) broken citations undermine presentation quality, (2) the architecture-conditional Pareto claim is underpowered (n=2 MoE + n=1 dense), (3) no multiple comparison correction despite extensive parallel testing, (4) decomposition analysis is structurally underpowered (R²=0.28 difficulty probe). The negative results are generally convincing but some secondary claims need more careful statistical treatment.

### Excitement: 2 (Potentially Interesting)

The paper does not resonate strongly but has elements that would interest parts of the *ACL community. The control task finding (35% artifact rate in cross-lingual probing, extending to MID-resource languages) is the most exciting contribution and has genuine field-level implications. However: (1) negative results papers inherently have lower novelty — the paper mostly confirms that methods don't work, (2) the positive contributions (control task warning, conditional linear projection) are relatively narrow, (3) the Pareto and CKA analyses confirm expected failures (MoE routing breaks dense-model assumptions) without yielding surprising insights, (4) the practical guidance from linear projection is too conditional to be immediately useful. The paper would benefit from more deeply developing the control task finding as the central contribution rather than giving equal space to multiple negative results.

### Overall: 2 (Resubmit next cycle)

The paper has a valuable core contribution (control task methodology warning) embedded in a collection of negative results that individually lack sufficient novelty for a main conference paper. The critical formatting issues (broken citations, zero figures) indicate the paper is not submission-ready. Specific recommendations for resubmission:

1. **Fix all broken citations immediately** — this is a hard requirement.
2. **Add figures** — at minimum: Pareto scatter, CKA partial residual scatter, selectivity heatmap, β sweep curve, saturation curve. The paper's persuasive power depends on visualization.
3. **Foreground the control task contribution** — restructure to make §9 the central section with expanded analysis (e.g., which specific published results are called into question? What is the recommended selectivity threshold?).
4. **Add a second dense architecture** to support the architecture-conditional Pareto claim, or soften the claim to "observed in our sample."
5. **Expand related work** to properly contextualize the field-level implications.
6. **Apply multiple comparison corrections** or explicitly discuss why they're not needed.
7. **Flesh out appendices D** (52 languages) with actual tables/figures or remove the claim that it "strengthens" the finding.

### Confidence: 4 (High)

I am confident in this assessment. The paper's domain (cross-lingual probing, internal representations, probe-based calibration) is within my expertise. The statistical methodology and experimental design are assessable from the presented data. My main uncertainty is whether the broken citations/missing figures reflect a genuine submission (in which case the paper needs significant revision) or a compilation error (in which case only the content issues matter — still a borderline Findings paper at best).

---

## 8. Minor Issues

- §3.4: "AUROC > 0.58" pass threshold is not motivated — why 0.58 specifically?
- Table 1 caption says "Only 1/20 languages reaches significance" but doesn't note this is expected under the null (α=0.05 × 20 tests ≈ 1 false positive).
- §7.1: "Parallel set sizes range from 618 to 2,852 per language" — this 4.6× variation could introduce heterogeneous power across languages. Was this analyzed?
- §10.2: "Japanese (HIGH, 0.588) is helped while Korean (MID, 0.589) is hurt" — this example is compelling but anecdotal. Is there a systematic feature (beyond resource tier and ZS AUROC) that predicts the effect direction?
- §11.1: The orthogonality analysis is too brief to be informative. Either expand or remove.
- The paper title promises "Conditional Solutions" but the actual solutions (linear projection with caveats) are quite thin relative to the promise.

---

## 9. Recommendation Summary

**Accept as-is**: No  
**Accept with minor revisions**: No  
**Accept as Findings**: Not in current state (broken citations, no figures)  
**Resubmit after revision**: Yes — fix formatting, add figures, foreground control task contribution  
**Reject**: No — the core content has value

The paper contains one genuinely strong contribution (control task methodology warning for cross-lingual probing) and several competent but unsurprising negative results. In its current form, the presentation issues (broken citations, zero figures, compressed appendices) prevent acceptance. With substantial revision focusing on the control task finding as the primary contribution, supported by proper visualization, this could be a solid Findings paper at EACL.