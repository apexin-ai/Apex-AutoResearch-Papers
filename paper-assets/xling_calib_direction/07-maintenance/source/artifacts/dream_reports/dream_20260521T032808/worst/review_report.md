---
dream_id: dream_20260521T032808
tier: worst
overall_score: 3 — Weak Reject
timestamp: 2026-05-21T04:29:06.702830+00:00
---

# Review Report: Stress-Testing Probe-Based Calibration Beyond English

## Paper Summary

This paper presents the first systematic evaluation of cross-lingual correctness probe transfer for LLM calibration, spanning 52 languages, three architectures (Qwen3-235B MoE, Llama 4 Scout MoE, Gemma 4 31B Dense), and five transfer strategies (zero-shot, mean-shift, linear projection, CaCLR, few-shot). The key findings are: (1) the depth–transferability Pareto frontier is architecture-dependent, significant only on the dense model and collapsing on both MoE architectures; (2) CaCLR (MMD-based distributional matching) is inert across all configurations; (3) 38% of language–layer probing combinations are capacity artifacts (72% for low-resource languages); and (4) only 18/51 target languages (35%) meet a joint viability criterion (AUROC>0.60 and selectivity>0.05). Few-shot target-language probes (25–100 examples) are the only consistently effective path forward.

---

## Strengths

**S1. Important and timely research question.** All prior probe-based calibration work (Burns et al. 2023; Miao et al. 2026; Miao & Ungar 2026) is English-only. The paper asks the natural next question—does this extend cross-lingually?—and provides a systematic, honest answer. The community needs this kind of stress-testing before the probe-calibration paradigm is assumed to generalize.

**S2. Thorough experimental coverage.** The paper covers 13 distinct experimental analyses across 3 architectures, 52 languages, 3 benchmarks, and 5 transfer methods. The inclusion of quantization validation (§5.11), cross-benchmark generalization (§5.10), and probe complexity ablation (§5.8) demonstrates careful attention to potential confounds. The scope is genuinely impressive for a single paper.

**S3. Control task analysis is a real contribution.** Extending Hewitt & Liang's (2019) control task framework to multilingual probing and discovering that 72% of low-resource language–layer combinations are capacity artifacts is the paper's strongest finding. This is not merely a replication—the dramatic amplification of artifacts in the multilingual setting (72% vs. ~25% for English) is both surprising and consequential. Table 9 and Table 10 are compelling.

**S4. CKA depth confound is a useful methodological warning.** The paper's demonstration that naively correlating CKA with transfer degradation produces a significant spurious correlation (pooled ρ=−0.28/−0.35, both p<0.01) that vanishes under partial correlation controlling for depth (r=0.04/0.08, both n.s.) is a cautionary finding that the representation similarity literature should heed (§5.5, Table 11).

**S5. Honest framing of negative results.** The paper does not oversell. The discussion acknowledges limitations (MCQA-only, correlational MoE claim, translation quality confound) and the viability boundary is presented as "a boundary condition the field must acknowledge" rather than a fatal indictment. The tone is appropriate.

---

## Weaknesses

**W1. No methodological novelty—the paper applies existing tools to a new setting.** The probing framework, CaCLR loss, control tasks, CKA analysis, and linear projection are all drawn directly from prior work. The sole "new" element is combining them in a cross-lingual evaluation. While empirical contributions have value, at a top ML venue the bar requires either (a) a novel method that partially solves the identified problem, or (b) a surprising theoretical insight explaining why the problem exists. The paper offers neither. The "constructive paths forward" (§6: few-shot, multilingual training, dense models) are all obvious; none are actually developed or evaluated beyond the basic few-shot experiment.

**W2. Many negative results are predictable from prior theory.** CaCLR's failure is essentially a direct consequence of Zhao et al. (2019), which the paper itself cites: marginal distribution matching fails when conditional distributions P(Y|X) differ across domains. Since cross-lingual representations have different conditional distributions almost by definition, CaCLR's inertness is theoretically expected. The Pareto frontier collapse on MoE can be anticipated from the known input-dependence of expert routing. The paper would be substantially stronger if it derived these predictions before testing them, rather than framing them as empirical discoveries.

**W3. The central "viability boundary" is confounded by evaluation data quality.** The paper acknowledges in the limitations that "low-resource non-viability may partly reflect GlobalMMLU translation quality rather than representational limitations." This is not a minor caveat—it is a fundamental confound. If low-resource languages in GlobalMMLU have poor translations introducing systematic patterns that probes can exploit (contributing to capacity artifacts) or failing to provide a clean correctness signal (contributing to low AUROC), then the 35% viability rate may be an artifact of the evaluation data, not a property of the models' representations. The cross-benchmark generalization to Belebele and MMLU-ProX (§5.10) partially addresses this, but these benchmarks share similar translation pipelines and low-resource coverage issues. A validation on naturally-authored (non-translated) multilingual data would be needed to disentangle this.

**W4. Statistical power issues are severe for some analyses.** Llama 4 Scout has only 12 probed layers, meaning Spearman ρ per language is computed on n=12 points. At this sample size, |ρ|>0.58 is needed for significance—the paper correctly reports this but still draws substantive conclusions from the Scout results (e.g., "Pareto collapses on MoE"). With n=12, the absence of significant ρ is expected even if a real effect exists. The architecture contrast would be more convincing if both MoE models had comparable sampling density to the dense model.

**W5. Dense vs. MoE comparison is underpowered (n=2 MoE vs. n=1 dense).** The claim that MoE routing "disrupts the monotonic depth–transfer relationship" is based on comparing 2 MoE models against 1 dense model. This is correlational evidence at best. The two MoE models also differ in many other dimensions (parameter count, training data, quantization scheme, layer count) that could explain the Pareto collapse. A stronger design would include multiple dense models and ideally a dense/MoE pair from the same model family.

**W6. Difficulty decomposition adds little.** Section 5.6 reports that projecting out the difficulty direction yields Δ AUROC = +0.005, far smaller than few-shot (+0.032). The difficulty-vs-random gap is significant in only 4/10 languages. This analysis occupies space but doesn't meaningfully advance the paper's claims—it could be cut or relegated to an appendix without loss.

**W7. Paper is overloaded with results subsections.** Sections 5.1–5.12 present 12 distinct analyses, many with small marginal contributions (§5.6 difficulty decomposition, §5.7 orthogonality, §5.8 LR vs MLP, §5.11 quantization). The breadth comes at the cost of depth—several important findings (control task artifacts, Pareto architecture-dependence) deserve more thorough treatment. The paper reads as a collection of experiments rather than a coherent narrative building toward a central insight.

---

## Detailed Comments

1. **Abstract**: The abstract is dense but effective. Consider leading with the viability boundary finding rather than the Pareto frontier—the former is the more impactful contribution.

2. **§3.3 Mean-shift**: The proof that mean-shift produces ΔAUROC≡0 under standardized LR is elegant and should be stated more prominently—it saves the reader from wondering why mean-shift is even tested.

3. **Table 1**: This is the most important table in the paper—placing it on page 4 (before Methods are fully described) is disorienting. Consider moving it to the Results section.

4. **§5.3 CaCLR**: The explanation of *why* MMD fails (operating on 1-D probe logits, matching marginals not conditionals) is strong. However, this analysis could have been done a priori before running the expensive β sweep. The paper would benefit from acknowledging that CaCLR's 1-D logit formulation was arguably doomed from the start.

5. **§5.4 Capacity artifacts**: This is the paper's strongest section. The selectivity heatmap (Table 9) is striking. One concern: the 0.05 selectivity threshold is borrowed from Hewitt & Liang but was calibrated for English syntactic probing. Is this threshold appropriate for multilingual correctness probing? A sensitivity analysis around the threshold (e.g., 0.03, 0.05, 0.10) would strengthen the claim.

6. **§5.5 CKA**: The partial correlation analysis is the right test to run. The "Simpson's paradox" framing is apt. However, the same-layer analysis (Table showing only 5/36 significant) actually suggests CKA has some between-language signal at fixed depth—this nuance gets lost in the section's negative framing.

7. **§5.9 Linear projection**: Tables 16–17 are informative. The finding that low-resource languages show *negative* Δ at 50 pairs is important—it means well-intentioned alignment can actively harm performance for the languages that need it most.

8. **§5.12 Extended language coverage**: Table 20 is the paper's headline result but appears on the last content page with minimal discussion. This deserves more prominence.

9. **Missing experiments/analyses**: 
   - No analysis of *which* items probes get wrong cross-lingually (error analysis)
   - No evaluation of whether combining viable languages' probes could help marginal languages
   - No investigation of whether the viability boundary correlates with model pretraining data distribution

10. **References**: The reference list is appropriately sized (15 entries) for the paper length. All key prior works appear cited. Xiao et al. (2025) on knowledge-boundary probes is correctly distinguished from correctness probes.

---

## Questions for Authors

1. Have you considered testing on a non-translated multilingual benchmark (e.g., naturally-authored QA data) to disentangle the translation quality confound from the representational viability boundary?

2. For the control task analysis, what happens if you use MDL-based probing (Voita & Titov 2020) instead of the selectivity threshold? MDL may provide a more principled separation of memorization from genuine signal.

3. The paper notes MoE routing as the mechanism for Pareto collapse, but doesn't directly test this (e.g., by analyzing expert activation overlap between English and target languages). Could you provide evidence that languages sharing more experts with English show stronger Pareto trends?

4. Why was CaCLR restricted to operating on 1-D probe logits rather than on the full representation space? A version operating on higher-dimensional projections might perform differently.

---

## Experiment Coverage Assessment

Comparing against the full experimental design, the paper covers all 13 planned experiments:
- Plans 001–002 (Pareto frontiers): §5.1, Tables 1–3 ✓
- Plan 003 (CaCLR): §5.3, Tables 6–8 ✓
- Plan 004 (Difficulty decomposition): §5.6, Table 13 ✓
- Plan 005 (Orthogonality): §5.7, Table 14 ✓
- Plan 006 (LR vs MLP): §5.8, Table 15 ✓
- Plan 007 (Cross-benchmark): §5.10, Table 18 ✓
- Plan 008 (Gemma dense): Appendix B, Table 1 ✓
- Plan 009 (52 languages): §5.12, Table 20 ✓
- Plan 010 (Quantization): §5.11, Table 19 ✓
- Plan 011 (CKA): §5.5, Tables 11–12 ✓
- Plan 012 (Linear projection efficiency): §5.9, Tables 16–17 ✓
- Plan 013 (Control tasks): §5.4, Tables 9–10 ✓

Coverage is comprehensive. The Gemma dense results (plan_008) are compressed into an appendix, which is reasonable for a camera-ready extension. The 52-language extension (plan_009) appears only as a classification table (Table 20) without detailed per-language results—more detail in supplementary would strengthen the claim.

---

## Minor Issues

- Table numbering in the PDF text doesn't always match the actual table numbers (e.g., the text references "Table 20" for viability classification but it appears to be the last table)
- The paper switches between "19 target languages" and "20 languages" (including English)—be consistent
- §3.3: "ΔAUROC≡0 mathematically" deserves a footnote or one-line proof
- The 52-language extended evaluation lacks a per-family breakdown that would be informative given the typological diversity claim

---

## Overall Assessment

**Score: 3 / 6 (Weak Reject)**

**Confidence: 4 / 5**

The paper tackles an important question—whether probe-based calibration extends beyond English—and provides a thorough empirical answer. The control task artifact finding (72% for low-resource) and the CKA depth confound are genuine contributions. However, the paper falls below the acceptance bar for a top ML venue for three reasons: (1) it applies existing methods to a new setting without proposing any novel technique that advances the state of the art; (2) several of the negative results (CaCLR inertness, MoE routing disruption) are predictable from prior theory rather than empirically surprising; and (3) the central viability boundary claim has an unresolved confound with evaluation data quality that limits the strength of the headline finding. The paper would benefit from either (a) proposing and validating a novel transfer method that pushes the viability boundary, or (b) providing theoretical analysis that explains *why* the boundary falls where it does and makes testable predictions. As currently written, it is a solid empirical survey that would be a strong fit for a Findings track or workshop paper but lacks the novelty or surprise factor for a top venue main conference.