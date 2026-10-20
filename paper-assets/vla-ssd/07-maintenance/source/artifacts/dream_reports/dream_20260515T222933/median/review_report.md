---
dream_id: dream_20260515T222933
tier: median
overall_score: 5 - marginally below acceptance threshold
timestamp: 2026-05-15T23:04:14.062576+00:00
---

# Dream Review Report: "Where Do Action-Relevant Representations Come From in Vision-Language-Action Models?"

**Venue:** CoRL 2026 | **Review mode:** full | **Reviewers:** R1 (Methods+Experiments), R2 (Novelty+Related Work)

---

## 1. Paper Summary

This paper performs Representational Similarity Analysis (RSA) on OpenVLA, decomposing the contributions of the frozen SigLIP vision encoder, the learned MLP projector, and the Llama-2 LLM backbone to action-relevant representational structure. Using a 2×2 factorial design (trained/untrained × with/without instruction) across two LIBERO benchmarks, the authors report three findings: (1) SigLIP+projector achieves the highest RSA alignment with action structure (ρ=0.615), far exceeding the full VLA (ρ≈0.488) and DINOv2 (ρ=0.388); (2) LLM processing reduces action alignment by Δρ≈0.13 with non-monotonic per-layer degradation; (3) neither fine-tuning nor instruction content meaningfully alters the LLM's representational geometry. Results are verified with CKA (Kendall τ=0.87) and replicated on LIBERO-Spatial.

---

## 2. Consolidated Strengths

**S1. First quantitative component-level representational decomposition of a VLA.** No prior work has measured RSA/CKA alignment with action structure at the projector output, per-LLM-layer, and standalone vision encoder levels within a single VLA. This goes beyond the behavioral observations of Grant et al. (2026), Hou et al. (2026), and Fei et al. (2025) by pinpointing *where* in the architecture action-relevant structure resides. [R1, R2]

**S2. The trained-vs-untrained comparison is the paper's most genuinely novel contribution.** Demonstrating that a randomly initialized LLM produces nearly identical representational degradation trajectories is a finding that cannot be derived from behavioral studies. This "architecture-intrinsic degradation" insight is new and non-obvious. [R2]

**S3. Clean 2×2 factorial design with proper statistical methodology.** Bootstrap 95% CIs for all pairwise comparisons, convergence of four conditions within a 0.009-wide band — this is more rigorous than many empirical papers at CoRL. [R1, R2]

**S4. Thorough five-condition instruction ablation.** Testing real instructions against random English words, wrong-task instructions, and a fixed nonsense string, with convergence analysis, goes beyond prior behavioral-level instruction studies. The ratio argument (Δ_inst/Δ_arch ≈ 0.17) is well-constructed. [R1, R2]

**S5. Dual-metric verification and cross-benchmark replication.** CKA verification with honest discussion of the gap attenuation (0.06 vs 0.127) and the rotation-like transformation interpretation. LIBERO-Spatial replication with qualitatively identical conclusions. [R1, R2]

**S6. Honest limitations section.** The authors explicitly acknowledge single-architecture scope, LIBERO-only benchmarks, and the gap between representational geometry and functional use. [R1, R2]

---

## 3. Consolidated Weaknesses

### Major

**W1. No functional/behavioral validation — the critical missing experiment.** [R1, R2 — unanimous]
The paper never connects RSA values to task performance. SigLIP+projector achieves ρ=0.615 (highest RSA), but there is no evidence that a policy using projector-output features outperforms one using LLM-layer features. Without this causal bridge, the "degradation" framing remains an interpretation of geometric correlation, not a demonstrated functional property. A single experiment — a linear action predictor on projector output vs. LLM hidden states, compared against task success — would either validate or invalidate the entire narrative. Its absence is conspicuous and undermines all three practical implications in Section 5.

**W2. Headline finding is largely confirmatory of concurrent work.** [R2, acknowledged by R1 in discussion]
Grant et al. (2026) demonstrated across *six* VLA architectures that the visual pathway dominates action generation. Hou et al. (2026, LangGap) showed VLAs achieve >95% while ignoring language. Fei et al. (2025) demonstrated instruction insensitivity. The central conclusion — "vision encoder matters most, LLM and instructions don't" — is an emerging consensus. The representational precision is a step forward, but the conclusion itself is not new. For CoRL's acceptance rate, a paper whose headline result confirms what 3+ concurrent papers already show faces a high bar.

**W3. "LLM degrades action-relevant structure" framing is interpretively problematic.** [R1, R2 — unanimous]
Two complementary concerns:
- (R1) The non-monotonic per-layer profile (Spearman ρ=−0.62, bump at L12-16 with Δ≈0.06) partially undermines the "degradation" narrative. The bump suggests the LLM *can* recover action structure at intermediate layers — the paper acknowledges this but the framing doesn't fully incorporate it.
- (R2) The LLM is *designed* to transform representations toward next-token prediction. Lower RSA is expected architectural behavior, not pathology. The paper does not consider that the LLM may contribute information in dimensions orthogonal to what RSA captures: sequential dependencies, multi-step planning, discrete mode selection, or sparse but causally important features (cf. Haon et al. 2025 activation steering).

**W4. The learned projector confounds the "frozen vision encoder" narrative.** [R1]
The paper attributes the high projector-output RSA (0.615) to the "frozen SigLIP encoder," but the projector MLP is *learned* during fine-tuning. If projector weights are identical between trained and untrained models (the paper uses pretrained VLM weights for "untrained," which include the original projector), this needs explicit clarification. Otherwise, the projector's learned transformation — not SigLIP's frozen features — may be responsible for the high alignment, which would substantially change the interpretation.

**W5. Single architecture, single ecosystem — claims exceed scope.** [R1, R2]
The title and framing generalize to "VLAs" but only OpenVLA (SigLIP + token concatenation + Llama-2-7B) is tested. Architecturally distinct VLAs (pi0/pi0.5 with flow matching, RT-2 with cross-attention, models with jointly trained vision encoders) could exhibit fundamentally different patterns. Cross-attention architectures could selectively attend to action-relevant features without disrupting geometry. All benchmarks are within LIBERO (simulation, single robot morphology, one-task-per-layout where language is unnecessary by design), further limiting generalizability.

### Minor

**W6. Related Work is thin with significant omissions.** [R2]
Only 9 references across 4 short paragraphs. Missing 7+ directly relevant papers including:
- Haon et al. (CoRL 2025): mechanistic interpretability for steering VLAs — same venue, same model, same benchmark
- Lu et al. (2025): linear probing on OpenVLA hidden layers achieving >90% accuracy — methodologically closest prior work
- Rizzardo et al. (2026): feature observability/controllability in VLAs
- Swann et al. (2026): SAE-based OpenVLA interpretability
- Molinari et al. (2025): emergent world representations in OpenVLA
- Fang et al. (2026): LIBERO-CF counterfactual benchmark
- Karamcheti et al. (2024): Prismatic VLMs (OpenVLA's architectural foundation)
- Broader frozen-encoder VLM literature (LLaVA, InstructBLIP) to determine if findings are VLA-specific or general multimodal LLM properties

**W7. Underspecified RDM construction.** [R1]
The paper does not report: number of observations (N) used for RDM computation, token aggregation method (mean pooling, CLS token, last token?), whether RDMs are computed per-task or pooled across tasks, or how action structure RDMs are constructed from continuous 7-DoF action vectors.

**W8. SigLIP vs. DINOv2 comparison has an uncontrolled pretraining confound.** [R2]
SigLIP is a vision-language contrastive model; DINOv2 is self-supervised. The RSA gap (0.227) could reflect language-aware pretraining rather than anything VLA-specific. Testing CLIP ViT-L would disambiguate whether the recommendation is "use language-supervised encoders" vs. "use better encoders generally."

**W9. CKA gap attenuation (0.06 vs 0.127) raises questions about "degradation" magnitude.** [R1]
The paper's interpretation (CKA absorbs rotation-like transformations) is reasonable but cuts both ways: if the "degradation" is primarily rotation and CKA sees only half the effect, the functional significance of the RSA-measured drop is unclear.

---

## 4. Key Questions to Authors

**Q1 (Functional validation).** Can you train a simple action predictor (linear probe or MLP) on projector output vs. LLM hidden states and show it matches or exceeds task performance? This single experiment would convert the "degradation" narrative from correlational to causal.

**Q2 (Reconciliation with causal evidence).** Haon et al. (CoRL 2025) found sparse semantic directions in OpenVLA's LLM layers that are *causally* linked to action selection via activation steering. How do you reconcile their finding with your claim that the LLM "degrades" action-relevant structure? Could the LLM transform distributed geometric structure into sparse but functionally critical features that RSA cannot detect?

**Q3 (LIBERO language confound).** LIBERO assigns one task per layout, making language unnecessary by design (Grant et al. 2026). Would you expect the instruction invariance finding to hold on LIBERO-CF (Fang et al. 2026) where counterfactual task assignments force language dependence?

**Q4 (Projector confound).** What are the projector weights in the "untrained" condition? Are they randomly initialized or pretrained (from the VLM's original projector)? If pretrained, the high projector-output RSA may reflect the VLM's learned multimodal alignment rather than SigLIP's frozen visual features.

**Q5 (RDM specification).** How many observations (N) are used for RDM computation? What token aggregation method is used for the high-dimensional LLM hidden states? How are action RDMs constructed from continuous 7-DoF action vectors (Euclidean distance, cosine, task-conditional)?

---

## 5. Experiment Coverage Assessment

Comparing against the experiment design reference (review_context.yaml):

| Experiment | In Paper? | Coverage |
|---|---|---|
| Per-layer RSA degradation curve | Yes (Appendix A, Table 6) | Full — all 32 layers + projector, three-phase narrative |
| Random instruction control | Yes (Table 2) | Full — 5 conditions × 2 models, ratio argument |
| CKA verification | Yes (Tables 3-4) | Full — condition ordering, per-layer reversals, gap attenuation discussion |
| LIBERO-Spatial extension | Yes (Table 5) | Full — cross-benchmark comparison with gap analysis |

All four planned experiments are present. The paper covers the experiment plan comprehensively.

---

## 6. Roundtable Discussion Summary

### Step 2: Cross-Sharing
R1 and R2 were shared each other's reviews. Key cross-pollination:
- R1 acknowledged R2's novelty concerns — the confirmatory nature of the headline finding relative to concurrent work is a valid concern R1 had underweighted
- R2 acknowledged R1's projector confound point as a methodological issue they had not identified
- Both converged on the functional validation gap as the single most damaging weakness

### Step 3: Convergence
**Points of agreement:**
- Experimental methodology is strong (2×2 factorial, bootstrap CIs, CKA, cross-benchmark)
- The trained≈untrained finding is the most genuinely novel element
- The absence of functional/behavioral validation is the critical gap
- The "LLM degrades" framing is interpretively problematic from complementary angles
- Single-architecture/single-ecosystem scope limits the contribution
- The paper is currently below the CoRL acceptance threshold

**Remaining disagreement:**
- R1 (score 5) places more weight on the experimental rigor and the trained≈untrained insight
- R2 (score 4) places more weight on the novelty deficit and thin related work
- After discussion, both agree on a consolidated score of 5 (marginally below threshold), with R2 noting that addressing the related work omissions alone could shift their view

### Step 4: Consolidated Assessment

**Overall Score: 5/10 (marginally below acceptance threshold)**

**Confidence: 4/5**

**Meta-assessment:** This paper asks the right question at the right time and answers it with commendable experimental rigor. The 2×2 factorial design, five-condition instruction control, dual-metric verification, and cross-benchmark replication represent genuine methodological care. The trained≈untrained finding (architecture-intrinsic degradation) is the most novel contribution and deserves to be the paper's central claim rather than supporting evidence.

However, the paper falls short of the CoRL 2026 acceptance threshold for three compounding reasons: (1) the headline conclusion confirms what 3+ concurrent papers have established behaviorally, making the novelty increment narrow; (2) the complete absence of functional validation (does higher RSA → better task performance?) leaves the "degradation" narrative as correlational interpretation rather than demonstrated fact; and (3) the single-architecture (OpenVLA), single-ecosystem (LIBERO) scope cannot support the generality of the claims. The thin related work section (9 references, missing 7+ directly relevant papers including one at CoRL 2025 on the same model/benchmark) suggests insufficient engagement with a rapidly evolving literature.

**Path to acceptance:** (a) Add a linear probe experiment comparing projector-output vs. LLM-layer features for action prediction — this is the make-or-break experiment; (b) reframe the trained≈untrained finding as the primary contribution; (c) scope claims to OpenVLA specifically; (d) substantially expand related work to engage with concurrent interpretability literature; (e) test on at least one non-LIBERO benchmark where language is genuinely required.