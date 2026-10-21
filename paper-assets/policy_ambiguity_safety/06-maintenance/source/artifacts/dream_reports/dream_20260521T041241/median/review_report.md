---
dream_id: dream_20260521T041241
tier: median
overall_score: 3.5 — Borderline Conference
timestamp: 2026-05-21T05:18:18.453970+00:00
---

# Dream Review Report: "Not All Policy Ambiguity Is Equal"

**Dream ID:** 20260521T041241
**Review mode:** simple (1 reviewer, full coverage)
**Target venue:** EMNLP 2026 (ARR)

---

## Summary

This paper presents a matched-pair causal study of how six types of policy ambiguity (organized in a two-layer taxonomy) drive safety violations across five architecturally diverse LLM agents (~3,000 episodes). The core finding is a +28.7 pp increase in violation rates from ambiguity (+21.5 pp net of prompt sensitivity), with a significant model×type interaction: authorization-scope vulnerability spans 42 pp across models while conditional-precedence varies only 2 pp. Error analysis reveals "Ambiguity Blindness" — agents recognize ambiguity in only 9.2% of cases. The paper proposes a "Differential Nocuity" framework connecting Berry & Kamsties' ambiguity theory to modern agent safety.

---

## Scores

| Dimension | Score | Justification |
|-----------|-------|---------------|
| **Overall Assessment** | **3.5** | Borderline conference. Strong design and timely question, but perturbation control weakness, limited domains, and reproducibility gaps prevent clear Main accept. |
| **Soundness** | **3.5** | Rigorous matched-pair design with appropriate statistics, but perturbation control is underpowered and cross-judge asymmetry is underanalyzed. |
| **Excitement** | **3.5** | Important and timely question; model×type interaction is genuinely novel. Core binary effect somewhat expected; novelty is in the granularity. |
| **Reproducibility** | **2.5** | Models named and statistics detailed, but clause pairs not released, judge prompts not provided, τ²-bench integration details sparse. |
| **Confidence** | **4** | Familiar with agent safety, ambiguity in RE, and the statistical methods used. |

---

## Strengths

**S1. Rigorous causal design (Major).** The matched-pair methodology — where each clause has an ambiguous and unambiguous variant embedded in an otherwise identical policy — is a significant step up from prior work (e.g., DRIP-R measures interpretation divergence, not causal safety impact). The 300-pair × 5-model design yields nearly 3,000 episodes, providing substantial statistical power.

**S2. Comprehensive controls and validation (Major).** The paper includes perturbation control (§4.4), realism validation against DRIP-R (Table 2), judge calibration with human ground truth (§4.3, κ=0.74), test-retest reliability (ICC=0.882), and bootstrap stability analysis (Appendix D). This battery of controls is unusually thorough for this area.

**S3. Honest, calibrated reporting (Major).** The paper appropriately downgrades C3 (layer effect) from a confirmed finding to a "suggestive tendency" (§7.2). The perturbation control result (Δ_perturb=7.2pp, CI not containing zero) is reported transparently with net-effect framing. The Limitations section (§7.4) is thorough.

**S4. Novel model×type interaction finding (Major).** The C4 finding — that authorization-scope vulnerability varies 42 pp across models while conditional-precedence varies only 2 pp — is genuinely novel and practically actionable. The Fleiss κ=0.33 (models agree THAT ambiguity hurts but disagree on WHICH clauses) is an important nuance.

**S5. Useful conceptual framework.** "Differential Nocuity" and the distinction between systematic nocuity (24% convergent-wrong) and divergent nocuity extends Berry & Kamsties in a meaningful way for the LLM era.

**S6. Breadth of model coverage.** Five models spanning three providers, two architecture families (dense + MoE), and varied safety training approaches (Claude, GPT-5.4, GPT-4.1, Qwen3-235B, DeepSeek-V3). This is substantially more diverse than typical 1-2 model studies.

**S7. Ambiguity Blindness is a striking and well-documented finding.** The 9.2% awareness rate with 84.1% surface adoption across 358 traces provides concrete evidence that agents cannot self-detect ambiguity, motivating external detection mechanisms.

---

## Weaknesses

### Major

**W1. Perturbation control undermines the headline causal claim.** The abstract leads with "+28.7 pp increase" and calls it "the largest causal estimate in the agent safety literature." But Δ_perturb=7.2pp with CI [1.5, 12.9] not containing zero means a non-trivial portion (~25%) of the raw effect is attributable to surface sensitivity, not ambiguity per se. The net Δ=21.5pp is still large, but:
- The abstract should foreground the net effect, not the raw effect.
- The perturbation control uses only 30 pairs × 3 models (178 episodes) — underpowered. The CI spans 11.4pp. If Δ_perturb is closer to 12.9pp (upper bound), the net effect drops to ~15.8pp.
- The paper should report the net effect CI, not just the raw CI. Since Δ_net = Δ_ambiguity - Δ_perturb, its uncertainty is wider than either component alone.
- **Recommendation:** Report Δ_net with propagated uncertainty in the abstract; expand perturbation pairs (the context file suggests this too).

**W2. Domain generalizability is narrow.** Both domains (retail, airline) are customer service via τ²-bench. The paper claims "the largest causal estimate in the agent safety literature" but this is only demonstrated in customer-service settings. Healthcare, finance, and legal domains — where policy ambiguity is arguably more consequential — are untested. The 14.2pp airline-vs-retail delta in unauthorized escalation rates (mentioned in context but absent from paper) suggests domain effects may be substantial.

**W3. Cross-judge asymmetry is underanalyzed.** Claude episodes are judged by GPT-5.4; GPT-5.4 episodes are judged by GPT-4.1. If GPT-5.4 is systematically more lenient toward Claude (or harsher), this biases the model comparison. The paper discloses the asymmetry (§4.3) but does not analyze whether judge identity affects model rankings. A sensitivity analysis (e.g., comparing the subset judged by GPT-5.4 vs. GPT-4.1 on overlapping types) would address this.

**W4. Reproducibility concerns.** The paper does not mention releasing the 300 clause pairs, the judge prompts, or the full episode traces. Without these artifacts, the study is essentially non-replicable. The τ²-bench integration details (how clauses are embedded, system prompt structure, tool definitions) are also sparse. For a study where the *specific wording* of clauses is the independent variable, artifact release is critical.

### Minor

**W5. Token delta confound partially unresolved.** Spec-layer disambiguation requires ~34 tokens vs. ~13 for ling-layer (p<0.001). The logistic regression controls for token_delta (coef=0.018, p=0.005), but this is a continuous control for what may be a structural confound. If longer disambiguations correlate with harder-to-process clauses (not just more ambiguous ones), the spec/ling gap and type hierarchy may be inflated for high-token-delta types. The paper acknowledges this but could do more (e.g., analyzing the residual type effect after partialing out token delta).

**W6. Error analysis coding reliability is moderate.** Cross-coding κ=0.548 and human validation agreement of 70.8% on 24 traces are adequate but not strong. The paper reports detailed per-type failure mode percentages (Table 7) to single-digit precision, which overstates the reliability of these estimates. The caveat in §6 ("should be interpreted as approximate") is appropriate but easily overlooked given the precision of Table 7.

**W7. DeBERTa PoC is too thin for inclusion.** N=10 per type in the test set means per-type F1 estimates have huge confidence intervals. The r=0.91 correlation between per-type F1 and token delta is computed on 6 data points — statistically meaningless. This appendix adds little beyond "a classifier can be trained" and could be cut to save space for more important content (e.g., expanding the perturbation control analysis).

**W8. Missing Responsible NLP Research Checklist.** EMNLP 2026 mandates Sections A–E of the checklist. The paper has a Limitations section (§7.4) but the full checklist is not visible. Incomplete or missing checklist is a desk-reject signal.

**W9. No examples of clause pairs.** The paper describes the clause generation process but provides zero examples of actual ambiguous/unambiguous pairs. Even 2–3 examples would greatly improve the reader's understanding of what "authorization-scope ambiguity" vs. "coreferential ambiguity" looks like in practice.

---

## Experiment Coverage Assessment

Comparing against the experiment design reference (review_context.yaml):

| Experiment | In paper? | Coverage quality |
|-----------|-----------|-----------------|
| Clause generation (plan_001) | Yes (§4.1) | Good — revision rates, format mix reported |
| Mini-pilot (plan_001b) | No | Not mentioned — acceptable to omit for space |
| Full API study (plan_002) | Yes (§5) | Good |
| Full open-source study (plan_003) | Yes (§5) | Good |
| Full analysis (plan_004) | Yes (§5) | Good — C1-C4 all reported |
| Error analysis (plan_005) | Yes (§6) | Good — lexical model-family split included |
| Reliability (plan_006) | Yes (§4.5, App B) | Good |
| Realism validation (plan_007) | Yes (§4.1, Table 2) | Good |
| Judge calibration (plan_009) | Yes (§4.3) | Adequate — per-severity F1 mentioned but not tabled in main text |
| Perturbation control (plan_010) | Yes (§4.4, App A) | Good but underpowered |
| Classifier PoC (plan_008) | Yes (App C) | Thin — see W7 |

**Notable omissions from paper vs. context:**
- Airline vs. retail domain comparison (14.2pp delta in unauthorized escalation) — not reported; would strengthen domain-sensitivity discussion
- Per-model perturbation sensitivity breakdown is in Appendix A but not analyzed for implications (Claude most robust at +4.8pp, GPT-5.4 most sensitive at +8.3pp — this mirrors the overall model ranking and could be discussed)
- The context file's narrative guidance about softening auth_scope safety-training explanations was followed in the paper (good)

---

## Writing Quality

**Organization:** Clean and logical. The flow from taxonomy (§3) → method (§4) → results (§5) → error analysis (§6) → discussion (§7) works well. The decision to move C3 layer effect into Discussion rather than Results is appropriate.

**Clarity:** Generally good. Tables are well-formatted and informative. The paper packs substantial content into 8 pages without feeling rushed.

**Page budget:** 8 pages main text + ~2 pages appendix + references. Within EMNLP limits. The appendix space could be better allocated (cut/shrink PoC classifier, expand perturbation control analysis).

**Minor issues:** 
- Abstract is dense — could foreground the net effect (21.5pp) rather than burying it after the raw effect
- "Systematic Nocuity" in §7.1 is an interesting observation (24% convergent-wrong) but is introduced without formal analysis — feels underdeveloped
- The title change from "Profiles" to "Patterns" (per context guidance) is appropriate

---

## Limitations Honesty

The Limitations section (§7.4) covers: domain coverage, synthetic ambiguity, LLM-as-judge noise, perturbation control CI, and spec-layer reliability. This is thorough and honest. Two items could be added:
1. The cross-judge asymmetry issue (W3)
2. The inability to distinguish safety training effects from prompt format differences in the model×type interaction (partially mentioned in §5.3 but not in Limitations)

---

## Questions for Authors

1. Can you provide the Δ_net CI with propagated uncertainty from both the ambiguity and perturbation estimates?
2. Will the 300 clause pairs and judge prompts be released? This is critical for reproducibility.
3. Have you tested whether judge identity (GPT-5.4 vs. GPT-4.1 as judge) systematically affects violation rate estimates?
4. The 14.2pp airline-vs-retail gap in unauthorized escalation (from your error analysis) — why was this omitted? It's relevant to domain generalizability.
5. For the DeBERTa PoC, the r=0.91 on 6 points is not meaningful. Would you consider either expanding this analysis or removing it?

---

## Overall Assessment

This is a well-designed and honestly reported study that addresses an important question at the intersection of NLP, requirements engineering, and agent safety. The matched-pair causal design, five-model coverage, and comprehensive control battery are commendable. The Differential Nocuity framework and model×type interaction finding are genuine contributions.

However, the perturbation control result (CI not containing zero) weakens the headline causal claim more than the current framing suggests. The narrow domain coverage (two customer-service domains), reproducibility gaps (no artifact release mentioned), and some underanalyzed confounds (cross-judge asymmetry, token delta) prevent a clear Main track recommendation.

**Verdict:** Borderline conference / strong Findings. With revisions to foreground the net effect, expand the perturbation control, commit to artifact release, and add the checklist, this could reach Main track. As submitted, it is a solid Findings paper.

**Overall Assessment: 3.5 (Borderline Conference)**
