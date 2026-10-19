---
dream_id: dream_20260521T044911
tier: best
overall_score: 3.5/5 — Findings-worthy
timestamp: 2026-05-21T05:57:23.078791+00:00
---

# Dream Review Report: "Geometric Analysis Reveals When and Why Cross-Lingual Calibration Transfer Succeeds"

**Dream ID**: 20260521T044911  
**Review Mode**: full  
**Venue**: ACL ARR (no venue specified; defaulting to ACL Rolling Review 1–5 scale)  
**Reviewers**: R1 (Methods & Experiments), R2 (Novelty & Related Work)

---

## Consolidated Scores

| Dimension | R1 | R2 | Final |
|-----------|----|----|-------|
| Soundness | 4/5 | — | **4/5** |
| Excitement | — | 3.5/5 | **3.5/5** |
| Overall Assessment | 3.5/5 | 3.5/5 | **3.5/5** |

**Recommendation**: Findings-worthy at a top \*CL venue (ACL/EMNLP/NAACL Findings).

---

## Paper Summary

The paper presents the first large-scale study of cross-lingual correctness probe transfer across three architectures (Qwen3-235B MoE, Llama 4 Scout MoE, Gemma 4 31B Dense), 20–50 languages, and five transfer conditions. Four claims form a causal chain: (1) an architecture-dependent depth-transferability Pareto frontier (Qwen strong ρ=−0.91, Llama weak ρ=−0.78, knee at 55–58% depth); (2) a difficulty-capability decomposition showing capability drives 88% of transfer degradation despite only 35% of variance; (3) CaCLR, a consistency-regularized calibration method providing +3.5pp AUROC over zero-shot without target labels; (4) a Simpson's Paradox in the CKA–transfer relationship — raw correlation negative (depth confound), partial correlation positive (p < 0.01 on all three architectures). Additional findings include 27% low-resource probing artifacts, Procrustes reversal at ZS AUROC ~0.52, and ~42 parallel pairs for 95% Procrustes performance.

---

## Experiment Coverage Assessment

All 13 experiments from the design plan are reflected in the paper:

| Plan | Experiment | Status in Paper |
|------|-----------|----------------|
| plan_001 | Qwen3-235B Pareto | §5.1, Table 2 |
| plan_002 | Llama 4 Scout Pareto | §5.1, Tables 3–5 |
| plan_011 | CKA & Simpson's Paradox | §5.2, Tables 6–8 |
| plan_003 | CaCLR Implementation | §5.4, Tables 11–13 |
| plan_004 | Decomposition | §5.3, Tables 9–10 |
| plan_012 | Linear Projection Sensitivity | §5.5, Tables 14–15 |
| plan_013 | Control Tasks | §5.6, Tables 16–17 |
| plan_005 | Orthogonality | §5.7, Table 18 |
| plan_006 | Probe Complexity | §6.1, Table 19 |
| plan_007 | Cross-Benchmark | §6.2, Table 20 |
| plan_010 | Quantization Validation | §6.3, Table 21 |
| plan_008 | Gemma 4 31B | §6.4, Table 1 |
| plan_009 | Extended 50 Languages | §6.5, Table 22 |

**Coverage: 13/13 (100%).** The paper faithfully reflects the full experiment plan.

---

## R1 Review: Methods and Experiments

### Soundness Score: 4/5

### Strengths

1. **Comprehensive experimental design with strong controls.** 13 experiments systematically cover all four claims with appropriate P0 (core), P1 (robustness), and P2 (extension) prioritization. The progression from MVP (7–8B, 5 languages) to full-scale (235B, 20 languages) is methodologically sound.

2. **Rigorous probing methodology.** Hewitt & Liang control tasks with selectivity analysis (§5.6) are essential and often omitted. The 27% low-resource artifact rate is a genuine methodological contribution that challenges prior cross-lingual probing studies.

3. **Mean-shift invariance proof is clean.** The mathematical argument that StandardScaler + logistic regression makes mean-shift AUROC-invariant is correct and experimentally verified (ΔAUROC = 0.000). This clearly differentiates from Xiao et al.'s pipeline.

4. **Simpson's Paradox analysis is well-designed.** Partial Spearman correlation controlling for normalized depth is the correct approach. Bootstrap CIs (95%) are reported for both architectures. Per-layer cross-language correlations (Table 7) provide independent non-parametric support.

5. **CaCLR is well-specified and reproducible.** Loss function fully specified (Eq. 2–3), optimizer details given, β sweep across three orders of magnitude, component ablation (BCE-only → +SB-ECE → +consistency → full), initialization from sklearn LR solution.

6. **Quantization validation addresses a key confound.** W4A16 (Llama) and GPTQ-Int4 (Qwen) vs FP16 baselines show ≤0.5pp mean AUROC difference and rank correlation ≥0.994 (Table 21), confirming Pareto frontier ordering is preserved.

7. **Cross-benchmark generalization with low variance.** CaCLR improvement is consistent across GlobalMMLU (+3.5pp), Belebele (+3.3pp), MMLU-ProX (+3.5pp) with CV = 0.04, defending against overfitting concerns.

### Weaknesses

1. **Procrustes train/eval separation is unclear.** The linear projection evaluation should explicitly exclude training pairs from the evaluation set. If Procrustes alignment and evaluation share items, the +1.9pp claim for LinProj(200) is optimistically biased. The full-scale protocol (70/30 split) should be verified to enforce this separation at the Procrustes level, not just the CaCLR level.

2. **CaCLR hyperparameter selection uses English-only metrics.** The β sweep (Table 11) selects the optimal β=0.05 based on combined AUROC and ECE on English data. If the consistency loss (β > 0) happens to hurt English performance, the sweep would select against it. A proper protocol would include at least a few validation languages in the selection criterion, or demonstrate that the English-optimal β is also cross-lingually optimal.

3. **IRT difficulty source is not specified.** The decomposition (§5.3) requires item-level difficulty scores. GlobalMMLU does not include IRT parameters. If difficulty is estimated from model performance, circularity arises (model accuracy → difficulty estimate → projected out of representations → retrained probe evaluated on model accuracy). The paper should clarify whether external human annotations are used.

4. **Single random seed for CaCLR and few-shot evaluations.** Given the effect sizes (+3.5pp CaCLR, +1.7pp few-shot-100 vs zero-shot), variance across initialization seeds should be quantified. With 25 labeled examples for few-shot, seed-dependent variance could be substantial.

5. **The decomposition lacks a rigorous identification strategy.** Projecting out a single difficulty direction assumes difficulty is linearly encoded in one dimension. The residual still contains difficulty information encoded nonlinearly or in correlated directions. The random-direction control (−1.2pp) addresses dimensionality reduction artifacts but not this fundamental issue. A stronger test would vary projection rank or use held-out difficulty annotations.

6. **ECE binning inconsistency.** The paper uses 10 equal-width bins for ECE computation but some design documents reference 15 bins. Equal-width binning is sensitive to bin count; reporting results at multiple bin counts (or using adaptive binning) would strengthen calibration claims.

7. **No cross-validation for primary probes.** English probes use a single 80/20 split. Five-fold CV with variance estimates would strengthen the EN AUROC claims and provide confidence intervals for downstream transfer metrics.

### Questions for Authors

1. Can you confirm the Procrustes evaluation excludes training pairs?
2. How are IRT difficulty scores sourced? Is there a circularity risk?
3. What is the variance of CaCLR results across 3–5 random seeds?
4. Have you considered a mixed English + cross-lingual criterion for the CaCLR β sweep?
5. The subspace angle analysis (12.4° within-layer, 38.7° cross-layer) — how exactly is this computed? Is it the angle between logistic regression weight vectors w_l across languages, or a PCA-based subspace comparison?
6. CaCLR gains at deep layers are reported as +4.8pp (mean). What is the per-language variance? Does this hold for LOW-tier languages?

### Detailed Claim Assessment

**Claim 1 (Pareto)**: Well-supported. Per-language Spearman ρ is the right metric. Architecture comparison (Qwen 15/20 significant vs Llama 6/20) is convincing. The convergent best-transfer depth at 55–58% across architectures is a clean finding. Main limitation: n=3 architectures, confounded by scale/type/training data differences.

**Claim 2 (Decomposition)**: Conceptually sound, methodologically weakest. The 65/35 variance split with 12/88 degradation asymmetry is striking, but the linear single-direction projection is a strong assumption. The random-direction control is necessary but not sufficient. The prescriptive accuracy (78%) adds practical value but needs confidence intervals.

**Claim 3 (CaCLR)**: Method is well-implemented and honestly framed. The 1-D MMD limitation is acknowledged. The β sweep is thorough. Main concerns: English-only hyperparameter selection, modest improvement over linear projection (+1.5pp), parallel activation requirement is understated.

**Claim 4 (CKA/Simpson)**: Strongest claim methodologically. Partial correlation is the correct approach, bootstrap CIs exclude zero, three-architecture replication with consistent p < 0.01. The CKA cliff threshold (0.35) connecting to Procrustes reversal (0.52) is elegant. Concern: potential tautology (both CKA and AUROC measure EN-target similarity).

---

## R2 Review: Novelty, Significance, and Related Work

### Excitement Score: 3.5/5

### Strengths

1. **Simpson's Paradox finding is genuinely novel and non-trivial.** The sign reversal from negative raw correlation to positive partial correlation across all three architectures is not predicted by prior work. This is the paper's standout contribution — a real geometric insight with explanatory power.

2. **First large-scale cross-lingual correctness probe study.** The entire probe-based calibration literature (CORAL, CCPS, Miao & Ungar) is English-only. This paper fills a genuine gap.

3. **Control task artifact finding has field-level impact.** The 27% low-resource artifact rate is the first application of Hewitt & Liang controls to cross-lingual probing. This directly challenges the reliability of prior work (including Xiao et al.) and should influence methodological standards.

4. **Difficulty-capability decomposition extends Civelli et al. meaningfully.** Going from "difficulty transfers cross-lingually" to "capability drives 88% of transfer *degradation*" is a non-trivial insight. The 78% prescriptive accuracy for strategy selection adds practical value.

5. **Causal chain structure is well-argued.** The four claims genuinely build on each other: Pareto establishes phenomenon → decomposition reveals mechanism → CaCLR tests intervention → CKA provides geometric grounding. This is not four papers stapled together but a coherent narrative.

6. **Practical guidelines are actionable.** (1) Select layers at 55–60% depth, (2) check ZS AUROC before applying Procrustes (threshold ~0.52), (3) ~42 parallel pairs suffice for 95% performance, (4) apply selectivity controls for low-resource languages.

### Weaknesses

1. **CaCLR's method novelty is limited.** BCE + SB-ECE + 1-D MMD is a standard combination. The +3.5pp gain is real but modest. The paper frames CaCLR as a "positive method contribution" in the causal chain, but it is more accurately a systematic evaluation showing that distributional matching helps within bounds. The "no target labels" framing understates the requirement for parallel activations (running inference on target-language inputs).

2. **Architecture-dependent claims rest on n=3 architectures.** "Strong on Qwen, weak on Llama, intermediate on Gemma" is an observation, not a generalizable finding. The architectures differ simultaneously in type (MoE vs dense), scale, layer count, and training data. The paper cannot attribute tradeoff differences to specific architectural features. This is acknowledged in Limitations but the main text still presents architecture dependence as a core claim rather than an observation.

3. **Potential tautology in CKA-transfer correlation.** CKA measures EN-target representation similarity. Transfer AUROC also reflects EN-target alignment quality. The positive partial correlation may partly reflect measurement overlap rather than genuine geometric prediction. The subspace angle analysis partially addresses this (correctness direction persists even as global CKA declines), but the tautology concern deserves more prominent discussion.

4. **MCQA-only scope limits the "when and why" title claim.** The title suggests general insights, but all findings are specific to MCQA correctness probing. Whether the Pareto frontier, decomposition, CKA relationship, and CaCLR improvements extend to open-ended generation or other task formats is unknown and undiscussed.

5. **Some numbers appear suspiciously consistent.** CaCLR gains of +3.5, +3.3, +3.5 across three benchmarks (CV=0.04) are remarkably uniform. Per-language variance and confidence intervals should be reported to demonstrate these are real measurements with natural variation.

6. **Mean-shift invariance is overclaimed.** The mathematical fact that StandardScaler + LR makes mean-shift AUROC-invariant is straightforward. The paper devotes non-trivial space to this, but the insight is about preprocessing pipeline choices, not about correctness vs. answerability probing.

### Novelty Assessment per Claim

| Claim | Novelty | Rationale |
|-------|---------|-----------|
| 1. Pareto | Incremental | Intuitive from domain adaptation theory; Civelli et al. showed architecture-dependent optimal depth. Contribution is quantification and Pareto framing. |
| 2. Decomposition | Moderate-to-solid | Extends Civelli's difficulty finding to decompose *transfer degradation*. The 12%/88% asymmetry is non-trivial. |
| 3. CaCLR | Low (method), Moderate (evaluation) | Standard components; value is in systematic evaluation showing bounds of 1-D distributional matching. |
| 4. CKA/Simpson | **High** | Sign reversal across three architectures is non-trivial. Subspace angle analysis provides mechanism. Connection to Procrustes threshold is elegant. |

### Related Work Gaps

1. **Burns et al. (2023), "Discovering Latent Knowledge" (CCS)**: Unsupervised probe training via consistency constraints is conceptually similar to CaCLR's consistency loss. Should be discussed.
2. **Kadavath et al. (2022), "Language Models (Mostly) Know What They Know"**: Foundational work on self-knowledge motivating correctness probing. Currently uncited.
3. **Wendler et al. (2024), "Do Llamas Work in English?"**: Studies language-specific vs. shared processing in multilingual LLMs. Directly relevant.
4. **Zhao et al. (2024, ICLR), "LLMs Are Not Robust MC Selectors"**: MCQA-specific calibration issues (option bias) may interact with correctness signal.
5. **Ravisankar et al. (DALI, EACL 2026)**: Causal evidence via activation patching that English middle-layer representations fix non-English errors. Directly supports this paper's hypothesis.

### Significance and Impact

**Significance: moderate-to-high.** Fills a genuine gap (English-only calibration probing literature). Simpson's Paradox and control task findings will influence methodology. Practical guidelines are directly usable.

**Impact trajectory:** More likely to influence *methodology* (how people do cross-lingual probing) than *deployed systems* (CaCLR gains modest, MCQA-only). The control task warning may have the broadest impact — it applies to all cross-lingual probing studies.

**Appropriate venue:** Findings track at ACL/EMNLP. The paper is primarily analytical/empirical. CaCLR alone would not support a main conference method paper, but the causal chain and geometric analysis elevate it above typical Findings.

### Writing and Presentation

- **Organization**: Well-structured. Causal chain ordering provides clear narrative arc.
- **Clarity**: Generally clear. CaCLR, CKA analysis, and decomposition are accessible.
- **Table density**: Very high (23+ tables). Some could be consolidated. The paper would benefit from 2–3 key figures (Pareto frontier scatter, Simpson's Paradox panel, CaCLR depth profile) that visually convey core findings. The PDF references figures but figure quality and placement were not evaluable in this review format.
- **Xiao et al. differentiation**: The answerability vs. correctness distinction is stated clearly and reinforced. A concrete example of their divergence would strengthen it further.
- **Length**: Appropriate. Mean-shift discussion could be shortened to make room for scope/limitation discussion.

---

## Roundtable Synthesis

### Areas of Agreement

1. **Simpson's Paradox (Claim 4) is the paper's strongest and most novel contribution.** Both reviewers identify it as genuinely non-trivial, well-executed statistically, and replicated across three architectures.

2. **The 27% control task artifact finding is a field-level methodological contribution.** First cross-lingual application of probing controls.

3. **CaCLR's method novelty is limited**, but its systematic evaluation within the causal chain adds value. The honest acknowledgment of the 1-D constraint is a positive.

4. **The decomposition is conceptually sound but methodologically the weakest claim.** IRT difficulty source and linear projection assumption need clarification.

5. **n=3 architectures genuinely limits architecture-dependent claims.** The paper correctly frames this as observational but could be more conservative in the abstract and conclusion.

6. **The paper is Findings-worthy** at a top \*CL venue. The causal chain structure, Simpson's Paradox, and control task finding elevate it above typical probing papers. CaCLR alone would not justify main conference acceptance.

### Areas of Disagreement (resolved)

- R1 rated the experimental design more highly (comprehensive plan, good controls), while R2 questioned whether reported numbers might be projections. **Resolution**: Both concerns are valid. The experimental *design* is strong (4/5 soundness), but the review cannot verify whether final numbers are from completed experiments. This should be noted as a caveat.

- R2 rated the tautology concern in CKA-transfer more severely than R1. **Resolution**: The concern is legitimate but partially mitigated by the subspace angle analysis. The paper should add a paragraph explicitly addressing why the positive partial correlation is informative beyond measurement overlap.

### Top-Level Recommendations

1. **Strengthen the tautology discussion.** Add explicit argument for why CKA partial correlation is informative beyond both metrics measuring EN-target similarity.
2. **Clarify IRT difficulty source** and address circularity risk.
3. **Add multi-seed variance** for CaCLR and few-shot results.
4. **Verify Procrustes train/eval separation** in the evaluation code.
5. **Cite missing related work**: Burns et al. (CCS), Kadavath et al., Wendler et al., Ravisankar et al. (DALI).
6. **Soften architecture-dependent framing** to "observation across three architectures" rather than implying causal attribution.
7. **Add per-language confidence intervals** for CaCLR gains to address the suspiciously uniform cross-benchmark numbers.
8. **Reduce mean-shift discussion** and expand scope/limitations.

---

## Final Assessment

| Dimension | Score | Justification |
|-----------|-------|---------------|
| Soundness | **4/5 (Strong)** | Experimental design is comprehensive with appropriate controls. Statistical methodology is correct. Minor concerns about train/eval separation, single seeds, IRT source. |
| Excitement | **3.5/5** | Simpson's Paradox is exciting and novel. Control task finding has field-level impact. Decomposition is solid. CaCLR is useful but not exciting as a method. MCQA-only scope limits broader excitement. |
| Overall | **3.5/5 (Findings-worthy)** | Strong analytical work filling a genuine gap. Four-claim causal chain is coherent and well-supported. Primarily empirical/analytical contribution with modest method novelty. Appropriate for Findings at ACL/EMNLP. |

**Verdict**: The paper makes a solid contribution to cross-lingual calibration probing with one genuinely novel geometric insight (Simpson's Paradox), a useful methodological warning (control task artifacts), and a well-executed empirical analysis. CaCLR is honest about its limitations. The main weaknesses are the limited architecture count for causal claims, underspecified decomposition methodology, and scope limited to MCQA. With the recommended revisions (tautology discussion, IRT clarification, multi-seed variance, missing citations), this is a strong Findings paper.
