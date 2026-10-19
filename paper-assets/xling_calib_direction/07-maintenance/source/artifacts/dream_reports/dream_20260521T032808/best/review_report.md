---
dream_id: dream_20260521T032808
tier: best
overall_score: 4 — Weak Accept
timestamp: 2026-05-21T04:25:02.827229+00:00
---

# Review Report: CaCLR: Zero-Label Cross-Lingual Calibration via Correctness-Direction Alignment in Large Language Models

## Summary

This paper presents the first systematic study of cross-lingual correctness-probe calibration, making four contributions: (1) discovering an architecture-dependent depth–transferability Pareto frontier across 3 architectures and 20 languages, (2) decomposing correctness transfer into difficulty-shared and capability-specific components, (3) proposing CaCLR (BCE + SB-ECE + MMD on probe logits) for zero-label cross-lingual calibration, and (4) extending the correctness–confidence orthogonality finding to 20 languages. Experiments cover 3 models (Qwen3-235B, Llama 4 Scout, Gemma 4 31B), 3 benchmarks (GlobalMMLU, Belebele, MMLU-ProX), with extension to 53 languages.

---

## Strengths

**S1: Well-defined and important problem.** Cross-lingual calibration is practically important, and the observation that all existing probe-based calibration methods operate exclusively in English is a clear, well-motivated gap. The paper precisely characterizes what transfers, what doesn't, and why.

**S2: The Pareto frontier concept is the paper's strongest contribution.** The depth–transferability tradeoff is a genuine, reproducible discovery with actionable implications: deeper layers yield better English probes but degrade cross-lingual transfer. Quantifying this via per-language Spearman ρ (ranging from −0.82 for yo to −0.41 for es on Qwen3) and showing architecture dependence (ρ = −0.65 Qwen3 vs −0.33 Llama 4 vs −0.52 Gemma 4) provides a useful framework for practitioners.

**S3: Exceptional experimental thoroughness.** All 13 planned experiments from the design are represented in the paper: Pareto frontiers on 2 primary architectures, CaCLR with full ablation and β sensitivity, difficulty decomposition, orthogonality, probe complexity comparison, 3 benchmarks, quantization validation, CKA geometric analysis, linear projection sample efficiency, control tasks, a third architecture, and extended language coverage (53 languages). This breadth is commendable.

**S4: CKA geometric analysis provides compelling mechanistic insight.** The CKA cliff in Qwen3 at L64 (68% depth, CKA drop from 0.72 to 0.41) directly explains why Qwen3 has a strong Pareto while Llama 4's gradual CKA decline produces a weaker tradeoff. The subspace angle analysis (correctness ~12° vs global ~39°, ratio 3.15×) provides geometric intuition for why transfer works at all. Partial correlation controlling for depth (r = 0.42, p = 0.008) is the right statistical test.

**S5: Strong statistical methodology throughout.** Paired permutation tests, bootstrap CIs, Cohen's d, control tasks (Hewitt & Liang), random-direction projection controls, and quantization validation. The paper consistently avoids claiming significance without appropriate testing.

**S6: CaCLR ablation is well-designed.** Table 5 cleanly isolates each component's contribution. The finding that SB-ECE alone slightly decreases AUROC (−0.4 pp) but synergizes with MMD (full model +3.5 pp) is non-obvious and well-documented. The β sensitivity sweep (Table 6) identifies the sweet spot and the inverted-U shape is interpretable.

---

## Weaknesses

**W1: "Zero-label" framing is misleading (Major).** The title and abstract emphasize "zero-label cross-lingual calibration," but CaCLR requires parallel inputs — the same items translated into each target language — to compute MMD on probe logits. Having parallel test items for 20+ languages is a non-trivial data requirement. "Zero correctness-label" would be more accurate. This matters because CaCLR's claimed advantage over linear projection (50 pairs) is the absence of paired correctness labels, yet both methods require parallel inputs. The practical gap between "I have parallel inputs" and "I have parallel inputs with 50 correctness labels" is small.

**W2: CaCLR's practical niche is narrow (Major).** CaCLR (0.763 AUROC) is outperformed by linear projection with just 50 parallel pairs (0.790), and even by few-shot with 25 target labels (0.745 is close, 100 labels gives 0.774). Since CaCLR itself requires ~630 parallel items per language for MMD, any practitioner with this data could trivially obtain 50 correctness labels (just run the model and compare to ground truth on 50 items). The equivalence to ~35 pairs of linear projection (Section 4.10) makes CaCLR look like a less efficient version of a simpler method. The paper frames these as "complementary," but the practical scenario where you have 630+ parallel items but zero correctness labels is unclear.

**W3: Moderate effect sizes (Major).** CaCLR's primary improvements are +3.5 pp AUROC over zero-shot and −3.4 pp ECE vs temperature scaling (0.121 vs 0.155). While statistically significant (p = 0.003, d = 0.52), the practical significance is debatable. The headline "22% ECE reduction" uses a relative metric that inflates the impression — the absolute ECE of 0.121 is still quite high. A downstream evaluation showing that better-calibrated probes lead to better decisions (e.g., selective prediction, abstention) would strengthen the case.

**W4: Confounded architecture comparison (Moderate).** The three architectures differ simultaneously in type (MoE vs dense), total parameters (235B vs 109B vs 31B), active parameters, layer count (94 vs 48 vs 60), quantization precision, and training data. The paper acknowledges this in Limitations but still frames interpretations like "MoE routing sharpens the Pareto tradeoff" (Section 4.7) and "cliff MoE > dense > gradual MoE" as if these were established findings rather than speculation from n = 3 confounded observations. The ordering ρ_Qwen > ρ_Gemma > ρ_Llama could equally be driven by model scale, training data quality, or layer count.

**W5: MCQA-only evaluation (Moderate).** All experiments use multiple-choice QA formats. Correctness in MCQA is a clean binary signal, but real-world calibration needs extend to open-ended generation, where "correctness" is harder to define and calibration arguably matters more. The paper's conclusions about "output-based calibration limits" (Section 4.6) may not generalize beyond MCQA. The Limitations paragraph acknowledges this in one sentence, but the abstract and contributions make unqualified claims.

**W6: Orthogonality contribution is incremental (Minor).** Miao & Ungar (2026) established correctness–confidence orthogonality in English. Extending this to 20 languages with cosine < 0.06 is confirmatory, not surprising — the paper itself argues this is an "architectural property" independent of input language. If true, cross-lingual persistence is the expected outcome, not a discovery. This is worth a paragraph in the results, not a numbered contribution.

**W7: Difficulty-capability decomposition has limited statistical power (Minor).** The decomposition uses only 10 languages × 8 layers. The two categories (capability-dominated = zh/es/fr/de/ru/ko; difficulty-dominated = hi/tr/sw/bn) largely correspond to the high-resource / low-resource split already known from the Pareto analysis. The "82% prediction accuracy" is on N = 10 languages — one misclassification changes this to 72%. The prescriptive value is asserted but not validated on held-out languages.

**W8: No comparison with alternative alignment methods (Minor).** CaCLR uses MMD with Gaussian RBF kernel. The domain adaptation literature offers many alternatives: CORAL loss (second-order alignment), adversarial discriminators (DANN), optimal transport, contrastive alignment. The paper cites domain adaptation theory (Ben-David et al., 2010; Zhao et al., 2019) but tests only one alignment loss. Even testing CORAL (which is trivial to implement) would contextualize CaCLR's design choices.

---

## Missing Experiments / Coverage Gaps

All 13 planned experiments are represented in the paper. The coverage is comprehensive.

One notable gap: failure case analysis for languages below the 0.60 threshold (am, yo, my). The paper notes these failures but doesn't analyze whether the correctness direction is not extractable in these languages vs. whether transfer specifically breaks down. CaCLR's per-language performance on these failing languages is not separately reported.

---

## Questions for Authors

1. CaCLR requires ~630 parallel items per language. In what practical scenario would a user have this data but be unable to obtain even 50 correctness labels (which would allow linear projection to outperform CaCLR)?
2. The context YAML notes ~8% semantic drift in am/yo/my translations. How sensitive is MMD alignment to translation quality? Have you tested with degraded translations?
3. Why not compare CaCLR against CORAL loss or adversarial alignment, given the explicit framing around domain adaptation theory?
4. The probe operates in 1D logit space. Have you attempted MMD on higher-dimensional intermediate representations before projection?
5. What happens when CaCLR is applied at the Pareto-optimal depth (L56) rather than EN-optimal (L72)? Table 4 uses Pareto-optimal layers — does CaCLR at L72 combined with depth selection yield additional gains?

---

## Minor Issues

- The paper uses both "Llama 4 Scout 109B" and "Llama 4" inconsistently.
- Section 4.8 (cross-benchmark generalization) is very brief given the effort of running on 3 benchmarks. The per-language rank correlations (ρ = 0.89–0.93) are mentioned but the actual per-language data is not shown.
- Appendix E (Linear Projection Sample Efficiency: Llama 4) has Table 19 but no accompanying text or analysis.
- Some appendices (B: Probe Complexity) appear to have only a table with no prose.

---

## Overall Assessment

**Score: 4 — Weak Accept**

This is a thorough and methodologically sound empirical study that addresses a genuine gap in the literature. The Pareto frontier discovery (Contribution 1) is the paper's strongest offering — it's a clear, reproducible finding with practical value, and the CKA geometric analysis provides compelling mechanistic explanation. The experimental coverage is exceptional for a conference paper.

However, the proposed method (CaCLR) has moderate effect sizes (+3.5 pp AUROC), a narrow practical niche (outperformed by linear projection with minimal data, while requiring similar parallel data), and a somewhat misleading "zero-label" framing. The orthogonality extension is incremental, and the architecture comparison is confounded. The MCQA-only evaluation limits the scope of the conclusions.

The paper would benefit from: (1) more transparent framing of CaCLR's data requirements versus its baselines, (2) comparison with at least one alternative alignment objective, (3) downstream task evaluation showing practical impact of improved calibration, and (4) explicit qualification of claims to the MCQA setting.

**Recommendation:** The paper is above the acceptance threshold based on the quality of the Pareto frontier analysis, CKA geometric insights, and experimental rigor. CaCLR as a method contribution is less compelling on its own. If the authors address the framing issues (W1) and add an alternative alignment comparison (W8), this would be a solid accept.

**Confidence: 4/5** — I am confident in my assessment. The paper is in my area of expertise (representation probing, calibration, cross-lingual transfer). The main uncertainty is whether the practical niche for CaCLR is larger than I estimate.