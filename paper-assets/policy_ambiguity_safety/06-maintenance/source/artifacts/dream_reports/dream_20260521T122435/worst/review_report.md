---
dream_id: dream_20260521T122435
tier: worst
overall_score: 2.5 — Borderline Findings
timestamp: 2026-05-21T13:22:12.469874+00:00
---

# Dream Review Report

## Paper
**Measuring Policy Ambiguity's Causal Impact on Agent Safety: A Matched-Pair Framework with Judge Calibration**

## Summary
This paper studies how six types of policy ambiguity (3 specification-level, 3 linguistic-level) affect safety violations in LLM agents. Using 300 matched ambiguous/unambiguous clause pairs injected into τ²-bench, the authors collect 2,997 episodes across 5 models. A 100-episode human calibration study reveals systematic LLM-judge overestimation (F1=0.64, κ=0.56 vs. humans), leading to corrected claims: the headline effect drops from +34pp to +19.5pp (still p<0.0001), one claim is dropped entirely (layer effect), and others are weakened. The paper positions itself primarily as a methodology contribution (matched-pair design + judge calibration pipeline).

---

## Scores

| Dimension | Score |
|-----------|-------|
| **Soundness** | 3.5 / 5 |
| **Excitement** | 2.5 / 5 |
| **Reproducibility** | 3.0 / 5 |
| **Overall Assessment** | 2.5 (Borderline Findings) |

**Confidence:** 4 / 5

---

## Strengths

### S1: Rigorous causal design with perturbation controls
The matched-pair framework is well-constructed. The perturbation control (Δ_perturb = −0.67pp, CI contains 0, ratio=0.02) provides strong evidence that the observed effect is ambiguity-specific rather than prompt sensitivity. This is the paper's strongest methodological feature and clearly separates it from prior observational studies of agent safety.

### S2: Honest judge calibration and self-correction
The reliability–accuracy dissociation (ICC=0.919 vs. F1=0.64; LLM-LLM κ=0.91 vs. LLM-human κ=0.56) is a genuinely important finding. The authors discover that their own evaluation pipeline is biased and transparently report the corrected (deflated) numbers, dropping C3 entirely and weakening C4. This intellectual honesty is commendable and the dissociation finding has implications beyond this paper for all LLM-as-judge agent safety studies.

### S3: Scale and model diversity
2,997 episodes across 5 architecturally diverse models (2 proprietary frontier, 1 proprietary mid-tier, 1 MoE open-source, 1 dense open-source) with a 6-type ambiguity taxonomy provides meaningful breadth. The 7/7 consistency of the C1 effect direction (5 target models + 2 judge models) strengthens the robustness claim.

### S4: Well-structured presentation
The paper is clearly written and logically organized. The separation between raw and corrected results is consistently maintained. Tables are informative and the claim status summary (Table 14) provides a transparent audit trail of how judge calibration changes each finding.

### S5: Reliability stratification of qualitative findings
Table 11's stratification of qualitative findings by human-anchor reliability (robust → unreliable) is methodologically careful. Restricting paper claims to robust-level findings (ambiguity blindness κ=0.71, layer mechanism κ=0.64) while demoting unreliable fine-grained coding to appendix is the right approach.

---

## Weaknesses

### W1 (Major): Correction methodology underspecified
The paper reports "human-calibrated corrections" applied to raw violation rates but never specifies the mathematical procedure. With 100 episodes stratified by type × model × condition, some cells contain ~1–2 episodes. How are per-type correction factors (e.g., auth_scope −21.6pp, cond_prec −10.8pp) derived from so few samples per cell? Is it additive correction, multiplicative, or model-based? Are corrections applied uniformly across models or per-model? This is the most critical methodological gap — the entire Results section depends on these corrections, yet they are not reproducible from the paper as written.

### W2 (Major): Thin calibration sample for the claims made
100 episodes with 2 annotators is a minimum viable calibration. The paper applies per-type corrections derived from this sample (Table 6) and makes per-type × per-model claims (Table 9), but the stratification leaves very few episodes per cell. For 6 types × 5 models × 2 conditions = 60 cells from 100 episodes, most cells have 1–2 episodes. The corrected 5×6 matrix (Table 9) implies a precision of correction that the calibration sample cannot support. The Limitations section acknowledges this ("may not fully capture per-type × per-model interaction effects") but the main text presents corrected per-cell values without uncertainty estimates on the corrections themselves.

### W3 (Major): Token delta confound inadequately addressed
Specification-layer clauses require substantially more tokens to disambiguate (mean Δt=33.6) than linguistic-layer clauses (mean Δt=11.9). The logistic regression shows token_delta is borderline significant (p=0.052). This 3:1 asymmetry in disambiguation length is a systematic confound: longer disambiguations provide more information, potentially making the spec/ling comparison uninterpretable. The now-dropped layer effect (C3) may have been partly a token-delta artifact, and type-level comparisons within the hierarchy (C2) are contaminated by this variable. The paper does not control for token delta at the type level (e.g., by including it as a covariate in the per-type analysis).

### W4 (Moderate): Effect size deflation undermines excitement
The corrected C1 (+19.5pp, OR=6.2) is less than 60% of the raw estimate (+34pp, OR=15.1). While still significant, this leaves open the question: would a larger human calibration sample shrink it further? The paper provides no sensitivity analysis or confidence interval on the correction magnitude itself. Additionally, C3 is entirely dropped, C4's model×type interaction goes from p<0.0001 to p=0.028 with substantially shrunk effect ranges, and C2's V drops from 0.137 to 0.112 (small effect). The paper effectively has 2.5 surviving claims out of 5, which weakens the overall contribution.

### W5 (Moderate): Cross-judge asymmetry is a systematic confound
GPT-5.4 judges Claude episodes (F1=0.67, more accurate), while GPT-4.1 judges GPT-5.4 episodes (F1=0.61, less accurate). This means Claude's violation rates are measured more accurately than GPT-5.4's. The paper discloses this and mentions "per-judge correction factors" but does not detail how this asymmetry is resolved. Claude's notably low auth_scope rate (6%) could partly reflect more accurate judging rather than genuine model robustness.

### W6 (Minor): Domain limitation
Only two domains (retail, airline) within τ²-bench. Policy ambiguity in higher-stakes domains (medical, financial, legal) may exhibit different patterns. The ecological validity of customer-service scenarios for safety-critical claims is limited.

### W7 (Minor): Adjudication process not described
Two human annotators with κ=0.79 — how are disagreements resolved for the gold-standard labels? Majority vote with 2 annotators is just picking one. Is there an adjudication protocol? This matters because the entire correction pipeline depends on these 100 gold labels.

---

## Detailed Comments

1. **Abstract**: Claims "first matched-pair causal study" — this should be hedged or the scope narrowed to "first for policy ambiguity in LLM agents." Matched-pair designs are not new in NLP evaluation.

2. **§3 Taxonomy**: The "disambiguation channel asymmetry" (spec-layer unresolvable, ling-layer sometimes resolvable) is an interesting theoretical claim but is undermined by the corrected non-significant layer effect (C3 dropped). The taxonomy section should be revised to not set up expectations for a finding that doesn't survive correction.

3. **§4.1**: The 92% overall pass rate with auth_scope at 88% and coreferential at 86% suggests these types have inherent construct validity issues. How much of the downstream measurement difficulty (judge F1 lowest for these types) traces back to clause quality rather than judge limitations?

4. **§5.2**: The inflation mechanism explanation — that LLM judges lack the concept of "reasonable ambiguity resolution" — is insightful but speculative. Is there direct evidence from judge chain-of-thought that judges reference ground truth when evaluating ambiguous episodes? Or is this inferred from the FPR pattern?

5. **§6.1**: The logistic regression coefficients should report the full model, not just two predictors. What other covariates were included? Was type included as a fixed effect? Model as random effect?

6. **§6.2**: TOST equivalence tests at ±15pp finding 7/15 equivalent means that even with a generous equivalence margin, almost half the type pairs are not interchangeable. Combined with V=0.112, the type hierarchy claim is weak. The paper should state more clearly that the practical differentiation among mid-tier types is unreliable.

7. **§8**: The classifier section (DeBERTa + GPT-4.1) feels tangential. Binary F1=0.74–0.81 is a preliminary result that adds little to the paper's methodology story. Consider dropping to appendix or cutting entirely to save space for more important material (e.g., correction methodology details).

8. **Missing**: No Responsible NLP Research Checklist visible in the paper. For EMNLP 2026, this is mandatory (Sections A–E). Omission risks desk reject.

9. **Missing**: No Ethics section. The paper involves human annotation (2 annotators, 100 episodes) — IRB status, annotator compensation, and informed consent should be disclosed.

10. **References**: Several references use shorthand ("τ²-bench, 2024", "AgentPex, 2024") without proper author attribution. These need full bibliographic entries.

---

## Experiment Coverage Assessment

Comparing against the full experiment design:
- **Clause generation (plan_001)**: ✓ Covered (Table 1)
- **Mini-pilot (plan_001b)**: ✓ Briefly mentioned
- **Perturbation control (plan_010/014)**: ✓ Well covered (Table 3)
- **Full study API (plan_002)**: ✓ Covered (Table 7)
- **Full study open-source (plan_003)**: ✓ Covered (Table 7)
- **Full analysis (plan_004)**: ✓ Covered throughout §6
- **Error analysis (plan_005)**: ✓ Covered (§7), with appropriate reliability caveats
- **Reliability test (plan_006)**: ✓ Covered (§4.6)
- **Realism validation (plan_007)**: ✓ Covered (Table 2)
- **Judge calibration (plan_009)**: ✓ Extensively covered (§5)
- **Classifier PoC (plan_008/012)**: ✓ Covered (§8)

All experiments are represented. The paper handles the correction cascade well — the narrative is internally consistent.

---

## Questions for Authors

1. Can you specify the exact correction procedure (additive/multiplicative, per-type vs. aggregate, confidence intervals on corrections)?
2. What is the annotator adjudication protocol for disagreements in the 100-episode calibration set?
3. Have you conducted a sensitivity analysis: if the true correction is ±5pp from your estimate, how do C1 and C2 change?
4. Could you include token delta as a covariate in the per-type χ² analysis to disentangle disambiguation length from ambiguity type?

---

## Overall Assessment Justification

**Score: 2.5 (Borderline Findings)**

The paper addresses a timely and relevant question (policy ambiguity → agent safety) with a rigorous experimental design (matched-pair + perturbation control). The judge calibration finding (reliability-accuracy dissociation) is a genuinely useful contribution to the LLM-as-judge literature.

However, several factors prevent a stronger recommendation:
- The correction methodology is underspecified (W1), which is critical because every result depends on it
- The calibration sample is thin relative to the per-type/per-model claims made (W2)
- The corrected effects, while still significant, are substantially deflated — the paper loses C3 entirely and C4 is weakened to p=0.028 (W4)
- The token delta confound is not adequately controlled (W3)
- The paper pivots to "methodology contribution" framing, but the methodology itself (matched-pair design) is straightforward rather than novel — the novelty is in its application to this specific problem

The paper would benefit from: (1) fully specifying the correction procedure with uncertainty estimates, (2) a sensitivity analysis on correction magnitude, (3) controlling for token delta in type-level analyses, and (4) addressing the mandatory EMNLP checklist requirements. With these revisions, the paper could be a solid Findings contribution.
