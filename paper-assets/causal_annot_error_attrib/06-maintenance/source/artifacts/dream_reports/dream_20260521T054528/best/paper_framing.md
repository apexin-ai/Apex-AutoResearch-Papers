# Paper Framing — causal_annot_error_attrib

## Target Venue
- Primary: AAAI 2027 (abstract: 2026-07-21, paper: 2026-07-28)
- Secondary: ARR October 2026 (~2026-10-15, commit to NAACL 2027 / ACL 2027)
- Tertiary: ICWSM 2027 Round 2 (2026-09-15)

## Title
Multi-Class Annotation Errors Are Not Created Equal: Bias Taxonomy, Sensitivity Analysis, and Correction Guidance for LLM-Annotated Causal Studies

## Core Claims (3 条)

1. **Multi-class bias taxonomy**: For K≥3 annotation variables, the direction and magnitude of downstream bias depend on the interaction between the K×K confusion matrix structure and the DAG topology — breaking guarantees that hold in the binary case. We provide closed-form bias expressions for K=3 and matrix-form expressions with interpretability tools for general K, across 7 canonical social-science DAG topologies (confounding, exposure, mediation, collider, M-bias, instrument, front-door).

2. **Annotation Sensitivity Values (ASVs)**: A sensitivity analysis framework for annotation-induced bias. ASVs quantify the minimum degree of annotation error amplification needed to overturn a downstream conclusion, parameterized by a reference confusion matrix and amplification factor δ. Three complementary ASV types — magnitude (E-value-style robustness reporting, all topologies), significance (hypothesis testing filter, effective for attenuating topologies), and sign-flip (direction reversal warning, primarily exposure DAG) — because no single sensitivity metric suffices across all causal designs. The choice of appropriate ASV type is itself topology-dependent, reinforcing Claim 1. ASVs reveal a striking sensitivity ranking: IV estimates are maximally fragile (any annotation error exceeds threshold), while M-bias is immune (misclassification actually reduces spurious associations). Unlike E-values, ASVs incorporate study precision (sample-dependent), providing actionable guidance: for a given τ and σ, the critical sample size N* is analytically computable. Formal proofs (envelope monotonicity + sharpness) for 3 priority topologies; MC-validated for all 7.

3. **Correction guidance framework**: A principled decision framework mapping {DAG topology × error structure × ASV} to the appropriate correction method (DSL, PPI++, MLA, MC-SIMEX, naive plug-in). Key findings from 210-configuration MC validation (7 topo × 6 C × 5 methods × 1000 sims): (a) Frisch-Waugh theorem makes naive_plugin/MLA fundamentally ineffective for T-coefficient bias in 4/7 topologies (bias reduction = 0.0%, exact); (b) DSL is topology-limited — effective only for confounding (50%) and mediation (70%), catastrophically harmful elsewhere (mbias -768%, IV -187%); (c) PPI++ is the only universally reliable method (93.8% grand mean bias reduction, 96.8% coverage) but requires gold-standard labels; (d) correction method effectiveness is itself topology-dependent, reinforcing Claim 1. Dependence-aware multi-LLM correction remains an open problem.

## Story Spine

- **Problem**: LLMs are rapidly replacing human annotators in CSS, but Baumann et al. (2025) show 31–50% of downstream conclusions are already incorrect — critically, even annotators with F1 > 0.93 produce > 50% error risk in downstream causal estimates. Researchers lack diagnostic tools to answer: (a) which annotation error structures propagate bias under their causal design, and (b) how robust their conclusions are to annotation error. Kim et al. (ICML 2025) show cross-model errors are highly correlated (60% agreement when both err), meaning ensembles cannot escape systematic bias — researchers MUST analyze the error structure of their chosen annotator, which is exactly what our tools enable. The field's reliance on classification F1 as a proxy for downstream validity is fundamentally broken; our framework provides the missing link from annotation quality metrics to causal estimate reliability.

- **Existing approaches & gaps**: Wood-Doughty et al. (2018) apply DAG reasoning to text classifier errors but produce no formal bias theorems (binary only). TeBlunthuis et al. (2024) provide the most complete binary treatment with MLA correction but are limited to K=2, single classifier. Lee & Wood-Doughty (2024) extend to categorical + LLM classifiers but cover only 1 DAG topology (unobserved confounding), with no systematic taxonomy or sensitivity analysis. VanderWeele & Li (2019) provide sensitivity bounds but only for binary risk ratios. Jerzak et al. (EMNLP 2025) benchmark correction methods but treat error as monolithic — if different confusion matrix structures produce qualitatively different bias in different DAG topologies, unconditional benchmarking is itself misleading.

- **Our framing**: Multi-class annotation errors are not created equal. The same confusion matrix that produces innocuous residual bias in one DAG topology can produce direction-reversing toxic bias in another. We provide the first systematic characterization of this interaction (the taxonomy), a tool to quantify robustness (ASVs), and guidance for when/how to correct (the framework). This is not a new correction method — it is the missing diagnostic layer that tells researchers which correction is appropriate, or whether correction is needed at all.

- **Headline result template**: "Across 7 DAG topologies with K=3, our bias expressions correctly predict bias direction and magnitude within 95% MC confidence intervals. ASVs reveal a striking sensitivity spectrum: IV estimates are maximally fragile (any annotation error exceeds robustness thresholds), while M-bias associations are immune (misclassification reduces spurious bias). Empirical validation on 3 CSS tasks (K=2, 3, 10) annotated by 4 LLMs confirms the theoretical predictions: IV bias ranges from 30% at K=10 to 252% at K=3 across annotation settings, F1 does not predict downstream safety (F1=0.72 but IV bias>100%), and 55.4% of HumAID scenarios are ASV-unsafe, requiring correction or sensitivity reporting."

## Core Insight (Lead Finding) — DUAL VERSION, gate on plan_001

### Version A (≥1 topology shows direction reversal under K≥3 non-differential exposure misclassification)
The binary guarantee that "non-differential exposure misclassification biases toward the null" (Bross 1954) breaks in the multi-class case. For specific confusion matrix structures in specific DAG topologies, K≥3 non-differential error can amplify or reverse effect estimates. Brenner (1993) identified this possibility for polytomous confounder misclassification ("bias can go in either direction"); we provide the first systematic characterization across 7 DAG topologies with exact conditions for each {C structure × topology} cell. Furthermore, binarizing a K-class variable to "escape" into the binary regime is itself hazardous — collapsing introduces new, direction-unpredictable bias (MVP evidence: Δ up to 0.103).

### Version B (no direction reversal found across topologies)
Multi-class annotation error is structurally irreducible to the binary case: the downstream bias magnitude depends on the full K×K confusion matrix in ways that binary sensitivity/specificity cannot predict, and binarizing a K-class variable introduces new bias (MVP evidence: Δ up to 0.103). While non-differential error preserves bias direction across tested topologies (a useful practitioners' guarantee), the magnitude varies dramatically with confusion matrix structure (0.13–0.30 in confounding DAG alone), and this variation is topology-dependent. ASVs provide the missing robustness measure for this quantitative — not directional — uncertainty.

**Gate**: RESOLVED → Version A. Two topologies show τ-specific direction reversal: exposure (~83-100% sign flip) and IV (~52% sign flip, Wald denominator mechanism). 5/7 topologies have structural guarantee τ_sign_flip=0% across K={3,5,7}. See D003, D004, D010.

## MVP Evidence

**Confounding DAG + K=3** (confounder misclassification):
- Theoretical bias expressions match MC perfectly (6/6 structures within 95% CI) — framework validated
- Binary collapse ≠ multi-class: Δ up to 0.103 (near-permutation C), proving K=3 retains more confounding control than binarization
- 100k random C search: confounding DAG bias is monotonically toward OVB — this topology is "well-behaved" (predictable direction)
- NOTE: Confounding DAG tests residual confounding, NOT bias-toward-null (Bross 1954). Criterion 2 (away-from-null bias) holds for binary too in this topology. See M001.

**Exposure DAG K=3** (exposure misclassification — D002/D004 CONFIRMED):
- 100k random C: 85% violate bias-toward-null, 83.4% sign reversal, 14.1% amplification
- K=2 control: 6/6 toward null (binary guarantee holds)
- Worst case: β₁=1.0 → γ̂₁=-0.84 (sign reversal, 0.84× magnitude); β₂=-0.5 → γ̂₂=-1.41 (2.83× amplification)
- Mechanism: near-permutation C causes label swap → effect direction flips (structurally impossible in K=2)
- **Two-DAG contrast**: confounding (monotonic, predictable) vs exposure (unpredictable, topology-dependent) — validates core claim

**Dirichlet subspace analysis** (practical relevance validation):
- diag≥0.5: 32.5% violation, 21.6% sign reversal, 11.3% amplification
- diag≥0.7 (typical LLM accuracy): **13.7% violation**, 2.1% sign reversal, **11.7% amplification**
- diag≥0.9 (high-accuracy LLM): **11.9% violation**, 0% sign reversal, **11.9% amplification**
- Key pattern: sign reversal vanishes at high accuracy, but **amplification persists at ~12% regardless of accuracy**
- Implication: even 90%+ accuracy LLMs face non-trivial effect amplification risk — no "safe accuracy threshold" exists

**IV Dirichlet subspace analysis** (Dream feedback, 2026-05-21):
- Full: 100% violation, 51.7% sign flip, 48.3% amplification
- diag≥0.5: 100% violation, **0% sign flip**, 100% amplification, worst 28.6×
- diag≥0.7: 100% violation, 0% sign flip, 100% amplification, worst 2.4×
- diag≥0.9: 100% violation, 0% sign flip, 100% amplification, worst 1.2×
- Key contrast with exposure: IV sign flip vanishes at diag≥0.5 (exposure persists at 2.1% at diag≥0.7), but IV amplification is **universal** (100% at all thresholds, vs exposure 11.7% at diag≥0.7)
- Mechanism: Wald denominator monotonically contracts; diagonal dominance prevents zero-crossing (no sign flip) but not contraction (amplification)

## Venue Fit Risks

- **AAAI**: Broad AI audience — emphasize general methodology for "automated annotation measurement error," not LLM-specific. Frame as extending classical measurement error theory to modern automated labeling.
- **ARR/NAACL**: NLP audience — CSS track is natural fit. May want more empirical NLP experiments. Balance theory with practical LLM annotation scenarios.
- **Cross-discipline bridge**: Epidemiology (measurement error theory) × NLP (annotation errors). Epi reviewers check proof rigor; NLP reviewers check empirical relevance. Must serve both.

## Anticipated Reviewer Concerns & Planned Responses

1. **"Trivial extension of binary to multi-class"** → Brenner (1993) proved direction reversal; our taxonomy provides the first systematic characterization across 7 topologies. Binarizing K-class introduces NEW unpredictable bias (MVP evidence). The complexity jump is structural: binary has 2 free parameters (sensitivity, specificity) → scalar bias; K=5 has 20 free parameters → matrix-valued bias requiring eigendecomposition for interpretation. [Experiments: plan_001, plan_008]

2. **"Lee & Wood-Doughty (2024) already did categorical"** → They cover 1 topology (unobserved confounding) on 1 dataset (MIMIC). We cover 7 topologies with systematic taxonomy + ASVs + correction guidance. Their work is a stepping stone; ours is the full framework. [Experiments: plan_001]

3. **"Why these 7 DAG topologies?"** → These are the canonical CSS causal designs used by Hernán & Cole (2009) and TeBlunthuis et al. (2024). They cover the major roles an annotated variable can play: exposure (treatment), confounder, mediator, collider, instrument, front-door criterion variable. [Experiments: plan_001]

4. **"K≥5 expressions aren't actionable"** → Three interpretability tools: (a) eigendecomposition summaries identifying dominant bias modes, (b) worst-case scalar bounds, (c) diagnostic visualizations. [Experiments: plan_002]

5. **"ASV sharpness only proved for 3 topologies"** → Honest scoping reflecting algebraic complexity. Remaining 3 validated via MC with numerical sharpness evidence. Full proofs identified as immediate future work. [Experiments: plan_004, plan_005]

6. **"Correlated multi-LLM errors?"** → Kim et al. (ICML 2025) actually STRENGTHENS our case: if ensembles can't fix errors (60% agreement when both err), error structure analysis is the only viable approach. Multi-annotator correction with dependence is identified as an open problem. [Framework discussion]

7. **"Empirical validation scope"** → 3 CSS tasks (HumAID K=10, VAST K=3, Civil Comments K=2) × 4 LLMs (Llama-4-Maverick, Qwen3-235B, DeepSeek-Chat, Qwen2.5-7B) × 7 topologies = 14 configs. D016 confirms: topology ranking matches theory across all K values; IV bias co-varies with annotation setting (K=3 IV bias 252% vs K=10 30%, confounded with dataset/model differences); 7B vs 235B bias ratio 1.24 (model scale not dominant). 0 sign flips across all 98 scenarios. Note: VAST/Civil Comments use 7B local model (API 402 blocker), creating a model-tier asymmetry acknowledged in Limitations. [Experiments: plan_003, plan_006]
