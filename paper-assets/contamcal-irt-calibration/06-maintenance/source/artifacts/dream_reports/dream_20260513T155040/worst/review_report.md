---
dream_id: dream_20260513T155040
tier: worst
overall_score: 4/10 — Reject
timestamp: 2026-05-13T16:47:27.837478+00:00
---

# Dream Review Report: Empirical Identifiability Boundaries for Contamination-Aware IRT Calibration of LLM Benchmarks

**Venue:** AAAI 2027 (calibrated to AAAI-26: 1–10 scale, 17.6% acceptance rate)
**Review Mode:** Full (2 Reviewers, 4-Step Roundtable)
**Date:** 2026-05-13

---

## Reviewer Assignments

- **R1 (Methods + Experiments):** Methodological soundness, experimental design, statistical rigor, reproducibility
- **R2 (Novelty + Related Work):** Novelty assessment, literature positioning, significance, narrative clarity

---

## Step 1: Independent Reviews

### Reviewer 1 (R1): Methods + Experiments

#### Strengths

**S1. Honest negative-result framing with rigorous self-diagnosis.** The paper transparently reports that 4PL+γ MAE of 7.8pp does not significantly outperform linear regression's 7.2pp (p=0.23, Table 6), and that calibration is actively harmful for RL models (MAE 10.5pp vs uncalibrated 9.8pp, negative regret reduction −0.03, Table 16). This level of honesty is commendable and rare.

**S2. Comprehensive multi-dimensional identifiability analysis.** The paper establishes boundaries along 5 axes: signal AUC (Table 2), model count (Table 11: N≥80 for significance), model scale (Tables 14–15: degradation from 3B to 72B), prior sensitivity (Table 10: 30% variation), and training regime (Tables 12–13: RL causes 27% AUC reduction). The synthesis in Table 19 is actionable.

**S3. Rigorous controlled experimental setup.** SFT injection covering 3 scales × 5 dosage levels × 4 benchmarks with dual-track validation (controlled SFT + ecological RL study) is sound methodology. The specificity check (near-zero γ on clean benchmarks) is a thoughtful control.

**S4. The catch-22 insight is novel and impactful.** Signal AUC positively correlates with dosage — signals are strongest when contamination is most obvious and calibration least needed (100% dosage), while near-random (AUC 0.51–0.54) when calibration would be most valuable (5% dosage). This is a fundamental contribution to the contamination detection literature.

#### Weaknesses

**W1 (Major). The additive γ specification is structurally misspecified, and the identifiability boundaries may be artifacts of this choice.** The model uses γ·s_ij as a single scalar additive term, but Table 1 directly contradicts the additive assumption: inflation at 100% dosage ranges from +3.9pp (HumanEval, 3B) to +11.5pp (MMLU, 0.5B) — a 3× range. Inflation is inversely related to model scale, demonstrating that γ interacts with θ. This θ–γ interaction means the high posterior correlation (0.52–0.58) reported as "identifiability failure" may partly be model misspecification. The paper does not test multiplicative, interaction, or item-specific γ formulations. **The central contribution — identifiability boundaries — may be specific to this misspecified model rather than fundamental limits.**

**W2 (Major). MCMC diagnostics indicate unreliable posterior inference.** R̂_max = 1.08, 3.2% divergent transitions, ESS_min = 180. Stan recommendations require R̂ < 1.01, divergent fraction < 0.1%, ESS > 400/chain. These violations suggest pathological posterior geometry (ridges/funnels) due to near-non-identifiability. The reported posteriors and CIs may be unreliable. No reparameterization, non-centered formulation, or alternative samplers are attempted.

**W3 (Major). Single model family (Qwen2.5) limits generalizability.** All controlled experiments use Qwen2.5. Different model families (Llama, Mistral, Gemma) may have different memorization patterns and signal AUC profiles, potentially shifting identifiability boundaries. The paper claims to establish general "identifiability boundaries" but validates on a single architecture.

**W4. RRF fusion provides no benefit over the best single signal.** RRF AUC 0.70 vs Embedding Retrieval 0.72 at 100% dosage (Tables 4–5). Signal correlation r=0.58 explains this. The paper still frames RRF as a contribution despite it actively degrading performance.

**W5. exp-004 (standalone identifiability simulation sweep) is not presented.** The experimental plan calls for a 144-condition systematic sweep, but Table 19 instead synthesizes boundaries across experiments where multiple factors vary simultaneously. This conflates the effects of different factors rather than isolating each.

#### Minor Issues
- The 15pp "practical utility threshold" for CI width is stated without justification
- No multiple testing correction across 6 methods × 4 benchmarks
- ConStat has a circularity concern: paraphrase-based SFT injection means ConStat's original-vs-paraphrase gap is partially tautological
- Missing DCR baseline in reported results despite it being a key comparator
- Calling Self-Critique "stable" at AUC 0.57 under RL is misleading (barely above chance)

#### R1 Scores
| Criterion | Score |
|-----------|-------|
| Soundness | 4/10 |
| Experimental Quality | 6/10 |
| Clarity | 6/10 |
| **Overall** | **4/10** |
| Confidence | 4/5 |

**R1 Recommendation:** Reject. The catch-22 insight and signal survival analysis are publishable contributions, but the headline claim — identifiability boundaries — is undermined by model misspecification (W1) and unreliable posterior inference (W2).

---

### Reviewer 2 (R2): Novelty + Related Work

#### Strengths

**S1. Valuable reframing of the research question.** The shift from "calibration solves contamination" to "when is calibration solvable?" fills a genuine gap. The field has many proposed fixes but little understanding of operating conditions. This is intellectually honest and well-motivated.

**S2. Signal survival analysis under RL is a strong empirical finding.** Demonstrating that RL degrades all 4 signals below the identifiability threshold (avg AUC drop from 0.72 to 0.56) — and that this is systematic rather than signal-specific — is an important finding with immediate practical implications.

**S3. Principled connection to educational measurement literature.** The three structural differences identified when adapting item compromise IRT to LLMs (single model vs. independent examinees, continuous vs. binary exposure, regime-conditional ability) are non-trivial and correctly identified.

**S4. Methodological transparency.** The paper honestly reports that 4PL+γ does not outperform linear regression, γ is unidentifiable at ≤25% dosage, and calibration is harmful for RL models. This candor is unusual and valuable.

#### Weaknesses

**W1 (Major). The reference list is unacceptably thin (12 references) for a top venue.** Key missing citations include:
- *Explanatory IRT / Latent Regression IRT*: De Boeck & Wilson (2004), Adams et al. (1997) — the theoretical foundation for covariate-augmented IRT
- *IRT identifiability theory*: San Martín et al. (2009), Maris & Bechger (2009) — formal identifiability conditions
- *RRF*: Cormack, Clarke & Buettcher (2009) — the fusion method used without citation
- *Additional contamination detection*: KDS (Dong et al., 2024), contamination surveys (Balloccu et al., 2024)
- *IRT for LLMs*: TinyBenchmarks (Polo et al., 2024), STIRT (Gu et al., 2024)
- *Bayesian workflow validation*: SBC (Talts et al., 2018)
- *Dynamic benchmarks*: LiveBench — competing paradigm not discussed
- At minimum, the paper needs 30+ references with proper positioning.

**W2. Methodological novelty is limited to synthesis of known components.** RRF is standard rank fusion. 4PL IRT is textbook psychometrics. Adding a covariate to IRT is standard (explanatory IRT). The three claimed adaptations from educational measurement are more incremental than presented: (a) fixed-effects IRT is well-known (Mislevy, 1986), (b) continuous covariates in IRT are standard, (c) interaction modeling is standard. The primary novelty is empirical, not methodological.

**W3. Identifiability thresholds lack theoretical grounding.** AUC ≥ 0.70 and N ≥ 80 are derived from simulation rather than theory. The Fisher Information matrix could provide closed-form identifiability conditions. The 30% prior sensitivity suggests the AUC threshold itself may be prior-dependent. The paper does not distinguish structural identifiability (parameters uniquely determined) from practical identifiability (estimation quality sufficient for decisions).

**W4. Limited ecological validity of SFT injection.** Real-world contamination occurs through pretraining, not SFT. The dynamics differ: pretraining exposure is diffuse (mixed with billions of tokens), while SFT is concentrated. The RL observational study acknowledges being "directional only" with uninformative CIs.

**W5. Limited constructive contribution.** The paper's strongest finding is that calibration mostly does not work. While documenting failure modes is valuable, the paper could do more: under what conditions would calibration become viable? Could the identifiability analysis guide design of better detection signals? The measurement error model extension is mentioned but under-developed.

#### Missing Related Work (Specific)
1. Explanatory IRT: De Boeck & Wilson (2004), Adams et al. (1997)
2. IRT identifiability: San Martín et al. (2009), Maris & Bechger (2009)
3. RRF: Cormack, Clarke & Buettcher (2009) — used without citation
4. KDS: Dong et al. (2024) — prominent signal not included
5. Contamination surveys: Balloccu et al. (2024)
6. SBC: Talts et al. (2018)
7. LiveBench/dynamic benchmarks: competing paradigm
8. Task Contamination: Li et al. (2024)

#### R2 Scores
| Criterion | Score |
|-----------|-------|
| Novelty | 5/10 |
| Significance | 6/10 |
| Related Work | 3/10 |
| Clarity | 7/10 |
| **Overall** | **5/10** |
| Confidence | 4/5 |

**R2 Recommendation:** Borderline reject. The reframing is valuable and the empirical analysis is thorough, but the thin related work seriously undermines scholarly positioning, the methodological novelty is incremental, and the identifiability thresholds lack theoretical grounding.

---

## Step 2: Cross-Sharing

**R1 → R2:** "My biggest concern is W1 — the additive γ specification is contradicted by the paper's own data. The 3× range in inflation across scale/benchmark means the model is structurally misspecified. The identifiability boundaries may be artifacts of this misspecification, not fundamental limits. Also, the MCMC diagnostics are seriously problematic — R̂ 1.08 and 3.2% divergences mean we can't trust the posteriors."

**R2 → R1:** "I agree the model misspecification is concerning. From my perspective, the bigger issue is that the paper doesn't cite the explanatory IRT literature that directly underpins their approach — they present standard IRT-with-covariate as novel when it's textbook. And with only 12 references, they miss the IRT identifiability theory (San Martín, Maris & Bechger) that could formalize their empirical thresholds. The lack of theoretical grounding means even if the model were correct, we wouldn't know if AUC 0.70 is a fundamental boundary or a parameter-specific artifact."

---

## Step 3: Convergence

### Points of Agreement
1. **The reframing is genuinely valuable.** Both reviewers acknowledge that "when is calibration solvable?" is an important and timely question that the community needs to grapple with.
2. **Signal survival analysis and catch-22 insight are strong contributions.** These empirical findings are novel and have immediate practical implications.
3. **Honesty about negative results is commendable.** The paper's transparency is unusual and valuable.
4. **Execution falls short of AAAI standards across multiple dimensions:**
   - Model misspecification (R1-W1) undermines the central identifiability boundary claim
   - Thin related work (R2-W1, 12 refs) undermines scholarly positioning
   - No theoretical grounding for thresholds (R2-W3)
   - MCMC convergence issues (R1-W2) undermine uncertainty quantification
   - Single model family (R1-W3) limits generalizability

### Points of Disagreement and Resolution
- **R1 (4/10) is more critical than R2 (5/10).** R1 weights model misspecification more heavily ("boundaries may be artifacts"), while R2 gives more credit for the empirical breadth.
- **Resolution:** R2 accepts that R1's model misspecification concern (W1) strengthens the novelty concern — if the boundaries are model-specific rather than fundamental, the contribution is even more limited than an empirical negative result. Both converge toward 4–5.
- **Final consensus:** The paper has several publishable insights (catch-22, signal survival, scale-identifiability tension) but the headline claim — identifiability boundaries — is undercut by (a) model misspecification, (b) missing theoretical grounding, and (c) insufficient related work. At AAAI's 17.6% acceptance rate, this is below threshold.

---

## Step 4: Consolidated Assessment

### Overall Scores

| Dimension | Score | Notes |
|-----------|-------|-------|
| Soundness | 4/10 | Additive γ misspecified; MCMC diagnostics problematic; posteriors unreliable |
| Novelty | 5/10 | Valuable reframing, but methodology is synthesis of known components |
| Significance | 5/10 | Important negative results, but limited constructive contribution |
| Experimental Quality | 6/10 | Comprehensive breadth (13 experiments), but single model family and no standalone identifiability simulation |
| Related Work | 3/10 | 12 references is unacceptable; missing explanatory IRT, identifiability theory, RRF citation, and multiple relevant works |
| Clarity | 6/10 | Good narrative structure; some misleading labeling ("stable" for AUC 0.57); 19 tables feel cramped |
| **Overall** | **4/10** | **Reject** |
| Confidence | 4/5 | Both reviewers have domain expertise in IRT, Bayesian methods, and contamination detection |

### Consolidated Recommendation: **Reject**

### Key Reasons for Rejection

1. **The central claim is undermined by model misspecification.** The paper claims to establish "identifiability boundaries" for contamination-aware IRT, but the additive γ model is contradicted by the paper's own data (Table 1: inflation ranges 3× across scale/benchmark). The boundaries may be artifacts of this model choice, not fundamental limits.

2. **Unreliable posterior inference.** MCMC diagnostics (R̂ 1.08, 3.2% divergences, ESS 180) are far outside acceptable Stan thresholds. No reparameterization is attempted. The Bayesian uncertainty quantification — a core feature of the framework — cannot be trusted.

3. **Inadequate scholarly positioning.** 12 references for a paper spanning IRT, contamination detection, Bayesian computation, and LLM evaluation is far below AAAI standards. Missing the explanatory IRT literature that directly underpins the method, the IRT identifiability theory that could formalize the thresholds, and the RRF fusion citation.

4. **No theoretical grounding for thresholds.** AUC ≥ 0.70 and N ≥ 80 are purely empirical, with 30% prior sensitivity suggesting they may be prior-dependent. Fisher Information analysis could provide formal conditions but is absent.

5. **Limited generalizability.** Single model family (Qwen2.5) for all controlled experiments. SFT injection as contamination proxy has limited ecological validity for pretraining contamination.

### What Would Strengthen the Paper

1. **Address model misspecification (highest priority):** Test multiplicative or interaction γ formulations (e.g., γ_j · f(θ_j) · s_ij). If identifiability boundaries shift substantially, the current boundaries are model-specific; if they don't, the finding is more robust.

2. **Fix MCMC convergence:** Non-centered parameterization, reparameterized models, or alternative inference (variational, ADVI) to achieve R̂ < 1.01 and <0.1% divergences.

3. **Expand related work to 30+ references:** Must include explanatory IRT (De Boeck & Wilson 2004), IRT identifiability theory (San Martín et al. 2009), RRF (Cormack et al. 2009), SBC (Talts et al. 2018), and broader contamination detection literature.

4. **Add theoretical grounding:** Fisher Information-based identifiability conditions, or at minimum derive approximate analytical relationships between signal AUC, N, and parameter recoverability.

5. **Multi-family validation:** Test on at least one additional model family (e.g., Llama) to demonstrate boundary generalizability.

6. **Run exp-004 standalone:** Present the 144-condition identifiability simulation as a self-contained experiment rather than synthesizing across confounded experiments.

### Salvageable Contributions

Despite the overall negative assessment, several components are individually publishable and should be preserved in a revision:
- The catch-22 insight (signal quality anticorrelated with calibration need)
- Signal survival analysis under RL (systematic degradation across all signals)
- The scale-identifiability inverse relationship (larger models fundamentally harder)
- The concrete decision rule (when to attempt vs. when not to attempt calibration)

### Experiment Coverage Assessment

All 13 planned experiments from the experimental design appear in the paper:
| Experiment | Paper Section | Coverage |
|------------|--------------|----------|
| exp-001 (SFT injection) | §4.1 | ✓ Full |
| exp-002 (Signal pipeline) | §4.2 | ✓ Full |
| exp-003 (RRF aggregation) | §4.3 | ✓ Full |
| exp-004 (Identifiability simulation) | §5 (synthesized) | △ Partial — not standalone |
| exp-005 (Noise propagation) | §4.5 | ✓ Full |
| exp-006 (IRT calibration + baselines) | §4.4 | ✓ Full |
| exp-007 (7B scale bridging) | §4.9 | ✓ Full |
| exp-008 (Signal survival) | §4.8 | ✓ Full |
| exp-009 (RL observational) | §4.10 | ✓ Full |
| exp-010 (Prior sensitivity) | §4.6 | ✓ Full |
| exp-011 (Few-examinee regime) | §4.7 | ✓ Full |
| exp-012 (72B observational) | §4.9 | ✓ Full |
| exp-013 (Closed-weight 2-signal) | §4.11 | ✓ Full |

Coverage: 12/13 fully covered, 1/13 partially covered (exp-004 synthesized rather than standalone).

---

*Review conducted by 2-reviewer DREAM roundtable (R1: Methods+Experiments, R2: Novelty+Related Work) with full 4-step protocol.*