---
dream_id: dream_20260521T213023
tier: best
overall_score: 3.0 — Findings Accept
timestamp: 2026-05-21T22:23:11.007148+00:00
---

# DREAM Review Report — Full Roundtable

**Paper**: "Differential Depth Response: Fingerprinting Generation Depth in Non-Paraphrastic LLM Chains"
**Venue**: EMNLP 2026 (ARR)
**Review mode**: Full (2 Reviewers, 4-step roundtable)
**Dream ID**: 20260521T213023

---

## Converged Scores

| Dimension | R1 (Methods) | R2 (Novelty) | Converged |
|-----------|:---:|:---:|:---:|
| **Overall Assessment** | 3.0 | 3.0 | **3.0** (Findings) |
| **Soundness** | 3.5 | 3.5 | **3.5** |
| **Excitement** | 3.0 | 2.5 | **2.5** |
| **Reproducibility** | 3.0 | 3.5 | **3.0** |
| **Confidence** | 4.0 | 3.5 | **4.0** |

**Verdict**: Solid Findings paper. Well-executed empirical study with comprehensive coverage. Lacks the methodological novelty or broad practical impact for Main conference (~21% acceptance). The combination of new task formulation + thorough DDR characterization + honest negative finding is sufficient for Findings.

---

## Reviewer 1: Methods & Experiments

### Strengths (ranked)

**S1. Exceptional experimental breadth.** 15 distinct experiments covering feature ablation, cross-generator LOGO, reference model independence, baselines, cross-model chains, prompt types, paraphrastic comparison, downstream utility, multi-domain, ordinal resolution, human editing robustness, end-to-end classifier, LD-Score, length confound, and large-scale generators. This is among the most thorough empirical studies one could design for this problem. Every major potential confound or criticism is proactively addressed.

**S2. LOGO evaluation protocol is well-chosen.** Leave-one-generator-out cross-validation is the right test for cross-generator generalization claims. The 5-generator, 3-family setup provides meaningful diversity, and the family-out delta of 0.011 pp is a strong result.

**S3. Reference model independence (Table 6) is a strong falsification test.** Testing 3 reference models from 3 different families (Pythia-410M, OLMo-2-1B, Qwen3-0.6B) and finding universally negative entropy drift is methodologically rigorous. This directly addresses the concern that DDR might be a Pythia artifact.

**S4. Cross-model chains (+13.6pp) is the standout practical result.** The finding that heterogeneous generator chains produce *stronger* depth signals than single-model chains is both surprising and practically important — it directly addresses the ecological validity concern.

**S5. TOST for downstream utility is methodologically superior.** Using equivalence testing (TOST at ±2% margin) rather than standard t-test for the negative finding is the right statistical approach. With seed variance <0.002, a t-test would misleadingly find "significant" differences.

**S6. Honest treatment of negative findings builds credibility.** The downstream utility null result, 5-class ceiling, paraphrastic scope boundary, and QLoRA cross-generator degradation are all transparently reported with appropriate framing.

### Weaknesses (ranked)

**W1. DDR R² analysis needs statistical clarification (moderate).** Table 2 reports R² values for 7 features across depth 0–4. It is unclear whether R² is computed from (a) per-sample linear regression (thousands of data points), or (b) regression on 5 depth-level means. If (b), R² with n=5 is statistically unreliable — any monotonic trend will yield high R². The "two orders of magnitude" gap (0.88–0.95 vs 0.02–0.03) is visually convincing but needs p-values or confidence intervals on the R² estimates. The paper should specify exactly how these are computed and provide significance tests.

**W2. XGBoost hyperparameters not specified (moderate, reproducibility).** The paper says "We use XGBoost as the classifier" but provides no hyperparameters (learning rate, max depth, n_estimators, etc.). Were these tuned? If so, was tuning done within the CV loop to avoid leakage? This is a reproducibility gap.

**W3. Baseline comparison has a fairness concern (moderate).** Repurposing FastDetectGPT (0.627) and Binoculars (0.579) as ordinal depth predictors is informative but somewhat unfair — these methods were designed for binary real/fake detection, not ordinal depth estimation. The paper acknowledges this ("optimized for binary detection, not ordinal depth estimation," line 300) but the Table 4 presentation still invites unfavorable comparison. Avg-LogProb (0.765) is the most meaningful baseline.

**W4. Scale limitation is significant for 2026 (moderate).** Primary evaluation uses 0.6B–2.8B models. The 8B extension (Appendix E, held-out F1=0.683) shows moderate degradation. In 2026, where frontier models are 70B+ and instruct-tuned models dominate, the practical scope of these findings is narrow. The paper honestly acknowledges "base models only" as a limitation but this constrains the generalizability claim ("intrinsic property of autoregressive generation").

**W5. Feature ablation vs LOGO interaction unclear (minor).** Table 1 reports "5-fold cross-validation" for feature ablation, while Table 3 uses LOGO. Are these different evaluation setups? If so, are the results comparable? The paper doesn't clarify whether feature ablation was done within a LOGO fold or as a separate within-distribution experiment.

**W6. Chain construction prompts not provided (minor, reproducibility).** Three prompt types are described briefly (continuation: "Continue the following text:", elaboration: "Elaborate on the following:", rewriting: "Write a new passage inspired by:") but exact prompts are not given. Since prompt wording can affect generation behavior, these should be included for reproducibility.

**W7. Single reference model size (minor).** The paper tests 3 reference model *families* but all at small scale (410M, 1B, 0.6B). Does DDR change with a 7B+ reference model? This is left unexplored.

### Questions for Authors
1. How exactly are R² values in Table 2 computed? Per-sample regression or depth-level means?
2. Were XGBoost hyperparameters tuned? If so, was tuning done within the CV loop?
3. What is the minimum text length required for reliable feature extraction? Are shorter texts filtered?

---

## Reviewer 2: Novelty & Related Work

### Strengths (ranked)

**S1. New task formulation addresses a real gap.** "Generation depth classification" (gen-0/gen-1/gen-2+) is a genuinely new problem formulation. The observation that binary detection conflates qualitatively different material (gen-1 retains source properties while gen-2+ shows compressed vocabulary) is well-motivated and timely given web-scale recursive contamination concerns.

**S2. DDR is a clean, interpretable empirical finding.** The drifting/stationary feature partition with a two-orders-of-magnitude R² gap is a clear, memorable result. The "location shift preserving shape" interpretation provides mechanistic intuition without overclaiming formal guarantees.

**S3. Three-axis independence strengthens the structural claim.** Testing DDR across generator families, reference models, and prompt types provides convergent evidence that DDR is not an artifact of any specific experimental choice. This multi-axis validation is methodologically sophisticated.

**S4. "Diagnostic not curative" is intellectual honesty, not weakness.** The downstream utility null result (TOST-confirmed equivalence) is presented as a principled scope boundary rather than buried. This framing builds trust and clarifies the contribution's boundaries.

**S5. Cross-model chain result connects to realistic deployment.** The +13.6pp uplift under heterogeneous generation is the paper's most practically relevant finding and effectively argues that controlled single-model evaluation *understates* real-world applicability.

### Weaknesses (ranked)

**W1. Limited technique novelty (significant).** The features (TTR, hapax ratio, entropy statistics) are all well-established in stylometry and AI text detection. The classifier (XGBoost) is standard. The evaluation protocol (LOGO) is borrowed. The novelty is entirely in the *framing* (task formulation + DDR characterization), not in any new method. For EMNLP Main, this is a concern — the paper reads as "we applied known tools to a new problem and observed interesting patterns."

**W2. Practical utility is narrow (significant).** Three scope limitations compound: (1) base models only — instruct models "substantially degrade depth signal" (Limitations, line 426), (2) non-paraphrastic chains only — paraphrastic chains converge at depth ~2, (3) diagnostic only — depth-aware data curation doesn't help downstream quality. In 2026, where most deployed LLMs are instruction-tuned and many AI-generated texts undergo paraphrastic editing, the applicable domain is quite narrow.

**W3. Missing key citations (moderate).** 
- **Alemohammad et al. (2023), "Self-Consuming Generative Models Go MAD"** and the follow-up (2024) study self-consuming generative loops — the exact setup this paper constructs. This is a significant omission.
- The connection to **Dohmatob et al. (2024)** "curse of recursion" deserves more than a citation — their theoretical framework predicts exactly the distributional compression that DDR measures. The paper should discuss whether DDR's drifting/stationary partition has theoretical grounding in their scaling law analysis.
- **Guo et al. (2024)** "curious decline of linguistic diversity" is cited but inadequately discussed — their large-scale finding of vocabulary impoverishment is the exact phenomenon DDR's surface features capture.

**W4. Related work section is thin (moderate).** At approximately one column, the related work covers four areas but with insufficient depth. For a paper positioning itself at the intersection of AI text detection, model collapse, data quality, and stylometry, the related work should engage more deeply with each area, especially:
- How DDR relates to model collapse *theory* (not just empirical findings)
- How vocabulary impoverishment measures compare to prior stylometric applications
- How the ordinal depth formulation relates to existing authorship verification / source attribution work

**W5. "Structural regularity" language risks overclaiming (minor).** The paper uses "structural regularity" (abstract, contribution 2) and "intrinsic property of autoregressive generation" (abstract). While the 3-axis independence evidence is compelling, the claim is purely empirical — no formal proof or theoretical derivation is provided for WHY DDR occurs. The location-shift interpretation is a plausible hypothesis, not a proven mechanism. Recommendation: soften to "robust empirical regularity" or add explicit caveat.

**W6. The paper doesn't discuss adversarial robustness beyond editing (minor).** What happens if someone deliberately tries to defeat depth classification? The human editing experiment (Appendix C) tests passive editing, not adversarial evasion. For a detection-adjacent contribution, this is a gap worth acknowledging.

### Questions for Authors
1. How does DDR relate to the theoretical model collapse framework of Dohmatob et al. (2024)? Can the drifting/stationary partition be derived from their scaling laws?
2. What specific aspects of instruction tuning degrade depth signal? Is it RLHF, SFT, or both?
3. Could ensemble methods combining DDR features with existing detectors improve binary detection?

---

## Roundtable Convergence Notes

### Points of Agreement (R1 + R2)

1. **Experimental coverage is exceptional** — all 15 planned experiments are present in the paper, covering every major generalization and robustness axis. This is the paper's strongest asset.

2. **DDR is a real phenomenon** — the drifting/stationary partition with consistent direction across generators, reference models, and prompt types is convincing empirical evidence.

3. **The paper is well-written** — dense but readable in 8 pages, logically structured, claims generally well-calibrated.

4. **Scale and scope limitations are real** — base models ≤2.8B (with 8B extension) and non-paraphrastic chains only significantly narrow the practical applicability.

5. **Score convergence at 3.0 Overall** — both reviewers agree this is a solid Findings paper but lacks the novelty, impact, or methodological contribution for Main conference.

### Points of Partial Disagreement

1. **Excitement** (R1: 3.0, R2: 2.5, converged: 2.5): R1 finds the cross-model chain result and DDR characterization more exciting than R2. R2 weighs technique novelty more heavily. Converged at 2.5 — interesting empirical finding but not exciting methodologically.

2. **Impact of "diagnostic not curative"**: R1 views this as a strength (intellectual honesty); R2 views it as narrowing practical significance. Converged: both perspectives are valid — it's a strength in credibility but a weakness in impact.

3. **Missing citations severity**: R2 flags Alemohammad et al. as significant; R1 considers it important but not fatal. Converged: should be added in revision but not grounds for rejection.

---

## Experiment Coverage Assessment

All 15 experiments from the design specification are present in the paper:

| # | Experiment | Paper Location | Covered |
|---|-----------|----------------|:-------:|
| 1 | Feature ablation + DDR trend | Tables 1–2, §5.1 | ✓ |
| 2 | Cross-generator LOGO | Table 3, §5.2 | ✓ |
| 3 | Reference model independence | Table 6, §5.4 | ✓ |
| 4 | Downstream utility | Table 10, §5.7 | ✓ |
| 5 | Prompt type comparison | Table 8, §5.6 | ✓ |
| 6 | Paraphrastic comparison | Table 9, §5.6 | ✓ |
| 7 | Cross-model chains | Table 7, §5.5 | ✓ |
| 8 | Multi-domain | Table 11, Appendix A | ✓ |
| 9 | Finer-grained ordinal | Table 12, Appendix B | ✓ |
| 10 | Human edit robustness | Table 13, Appendix C | ✓ |
| 11 | LD-Score feature | Appendix F | ✓ |
| 12 | End-to-end classifier | Table 14, Appendix D | ✓ |
| 13 | Text length control | Appendix G | ✓ |
| 14 | Large-scale generator | Table 15, Appendix E | ✓ |
| 15 | Ordinal baseline comparison | Tables 4–5, §5.3 | ✓ |

**Coverage**: 15/15 (100%). All results align with the "best" tier expected outcomes.

---

## Actionable Revision Recommendations (Priority-Ranked)

### Must-Fix (before resubmission)

**1. Clarify DDR R² computation (W1-R1).** Add a sentence in §5.1 specifying whether R² is from per-sample regression or depth-level means. If per-sample, report p-values or CIs for the regression coefficients. If depth-level means (n=5), acknowledge the limitation and supplement with per-sample Spearman ρ (which the paper already computes elsewhere).

**2. Add missing citations (W3-R2).** 
- Alemohammad et al. (2023/2024) — self-consuming generative models
- Expand discussion of Dohmatob et al. (2024) — relate DDR to their theoretical framework
- Expand discussion of Guo et al. (2024) — connect vocabulary impoverishment finding

**3. Specify XGBoost hyperparameters (W2-R1).** Add to §3.4 or supplementary material: learning rate, max depth, n_estimators, and whether hyperparameter tuning was performed (and if so, whether within the CV loop).

### Should-Fix (strengthens paper)

**4. Expand related work (W4-R2).** Add ~0.5 column to engage with model collapse theory, self-consuming loops, and the relationship between DDR features and prior stylometric applications.

**5. Soften "structural regularity" language (W5-R2).** Change "structural regularity" to "robust empirical regularity" or add explicit caveat that the characterization is empirical, not theoretically derived.

**6. Clarify feature ablation setup (W5-R1).** Specify whether Table 1's 5-fold CV is within-distribution or within a LOGO fold, and how it relates to the LOGO results in Table 3.

**7. Provide exact prompts (W6-R1).** Include the full prompt templates for continuation, elaboration, and inspired rewriting in supplementary material.

### Nice-to-Have (if space permits)

**8. Discuss adversarial robustness (W6-R2).** Acknowledge that human editing robustness (Appendix C) tests passive editing, not adversarial evasion, as a limitation.

**9. Reference model scale experiment.** Test a larger reference model (e.g., Pythia-2.8B or Qwen3-1.7B as reference) to check whether DDR features change with reference model capacity.

**10. Baseline framing (W3-R1).** Add a note in §5.3 that FastDetectGPT and Binoculars were designed for binary detection and their ordinal repurposing is an imperfect comparison; Avg-LogProb is the most meaningful single-feature baseline.

---

## Summary Assessment

This is a well-executed empirical study that introduces a meaningful task formulation (generation depth classification) and provides thorough characterization of a real phenomenon (DDR). The experimental coverage is exceptional — 15 experiments across 7 appendices proactively address nearly every potential reviewer concern. The honest treatment of negative findings (downstream utility, paraphrastic scope, 5-class ceiling) builds credibility.

The main limitations are: (1) low technique novelty — all components (features, classifier, evaluation) are standard; (2) narrow practical scope — base models, non-paraphrastic chains, diagnostic only; (3) some clarity and citation gaps. These prevent the paper from reaching Main conference but the breadth and rigor of the empirical contribution make it a solid Findings paper.

**Final recommendation**: Findings accept (Overall Assessment 3.0). With the must-fix revisions (R² clarification, missing citations, hyperparameters), the paper would be a comfortable Findings acceptance. The cross-model chain result and DDR characterization are the strongest selling points.