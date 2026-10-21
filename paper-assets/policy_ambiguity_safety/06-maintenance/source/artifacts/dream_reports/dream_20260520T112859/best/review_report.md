---
dream_id: dream_20260520T112859
tier: best
overall_score: 3.5 — Borderline Conference (strong Findings)
timestamp: 2026-05-20T12:13:00.555494+00:00
---

# Dream Review Report: "All Ambiguity Is Nocuous"

**Dream ID:** 20260520T112859 | **Mode:** full | **Venue:** EMNLP 2026 (ARR)

---

## 1. Paper Summary

This paper presents the first causal, type-granularity study of how linguistic ambiguity in natural-language policy specifications drives LLM agent safety violations. Using a matched-pair design across 300 clause pairs, 6 ambiguity types, 4 models (GPT-5.4, GPT-4.1, Qwen3-32B-AWQ, Qwen3-8B), and 2,400 agentic episodes on τ²-bench, the authors establish five claims: (C1) ambiguous clauses cause +33.6 pp violation increase; (C2) type does not differentially predict severity (binary detection suffices); (C3) visible conflicts yield fewer violations than invisible ambiguity (Δ=−11pp, p=0.015); (C4) stronger models show wider type-specific sensitivity ranges; (C5) 8 failure modes cluster by ambiguity type. The paper connects Berry & Kamsties' nocuous ambiguity theory to agent safety, arguing all policy ambiguity is nocuous for LLM agents.

---

## 2. Reviewer Panel

| Reviewer | Focus | Overall | Soundness | Excitement | Reproducibility | Confidence |
|----------|-------|---------|-----------|------------|-----------------|------------|
| R1 | Methods + Experiments | 3.5 | 3.5 | 3.5 | 3.0 | 4 |
| R2 | Novelty + Related Work | 3.0 | 3.5 | 3.5 | 3.0 | 4 |

---

## 3. Roundtable: Convergence Summary

### 3.1 Points of Strong Agreement (Both Reviewers)

1. **C2/C3 internal tension is the paper's core structural flaw.** C2 claims type does not predict severity (omnibus χ²(5)=5.20, p=0.39, V=0.066), yet C3 claims a significant CP-vs-scopal difference (Δ=−11pp, p=0.015). Both reviewers flagged this independently. After cross-sharing, R1 argued the tension is resolvable (omnibus vs. planned pairwise contrast answer different questions; the middle 4 types cluster at 40–42%, concentrating variability in the tails). R2 partially accepted this framing but maintained the TOST ±15pp equivalence margin is generous — a 15pp difference in violation rate is operationally meaningful. **Consensus:** The tension is manageable but requires explicit discussion in the paper. The authors should either (a) frame C2 as "no *large* type effect" rather than "type doesn't matter," or (b) explain that visibility cross-cuts the type taxonomy.

2. **Missing judge calibration against human ground truth.** The experiment plan included plan_009 (100 human-annotated episodes for LLM judge validation), but results are absent from the paper. The reported κ=0.91 measures LLM-LLM agreement, not accuracy. Both reviewers consider this the single most critical missing validation. Without it, the entire measurement chain from episode to violation label is unvalidated. **Consensus:** This is a fixable gap — reporting plan_009 results would substantially strengthen the paper.

3. **Title overclaims relative to evidence.** "All Ambiguity Is Nocuous" is a universal claim tested on 6 of 11+ ambiguity types, 2 domains, and synthetic injections. Elliptical, presuppositional, implicative, and idiomatic ambiguity are untested. R2 flagged this as major; R1 partially agreed. **Consensus:** Soften to "Policy Ambiguity Is Uniformly Nocuous" or add explicit caveats about scope.

4. **Thin reference list.** Only 8 references for a paper bridging CL, RE, and agent safety. Missing citations include: Willis et al. (2008) on automated ambiguity detection, Ezzini et al. (2022) TAPHSIR, Sclar et al. (2024) on prompt sensitivity, Frazier & Rayner (1982) for garden-path grounding, and recent agent safety benchmarks (AgentPex, ShieldAgent). Both reviewers agree this is below EMNLP standards.

5. **Missing figures.** The paper has zero visualizations across 8 pages despite the experiment plan describing 6+ figures (forest plot, heatmap, Sankey diagram, etc.). This weakens presentation of C4 (capability gradient) and C5 (failure mode clustering).

### 3.2 Points of Divergence

1. **Severity of C2/C3 tension.** R1 views it as a standard coarse-vs-fine analysis pattern (manageable with better framing). R2 views it as more damaging to the paper's internal coherence. After cross-sharing, both agreed it is fixable but currently unresolved.

2. **Pre-registration status of C3.** R1 raised concern that the visibility hypothesis emerged from diag_001 (post-diagnostic), suggesting C3 was exploratory promoted to core claim. If so, p=0.015 should be interpreted more cautiously and might not survive multiple comparison correction (0.015 × 15 = 0.225 under Bonferroni). R2 countered that the theoretical motivation from garden-path literature justifies treating it as a planned contrast. **Unresolved** — authors should clarify.

3. **Overall assessment gap (3.5 vs 3.0).** R1 considers the paper borderline Conference (strong Findings at minimum); R2 considers it borderline Findings. The gap reflects R2's heavier weighting of the title overclaim, thin related work, and ecological validity concerns. After cross-sharing, R1 maintained 3.5; R2 expressed willingness to move to 2.5–3.0 depending on judge calibration.

### 3.3 Novel Concern from Cross-Sharing

**Prompt sensitivity confound** (raised by R2, endorsed by R1 as "the strongest point in either review"): The +33.6pp effect is attributed entirely to ambiguity, but without a control condition using non-ambiguity perturbations (e.g., synonym substitution, clause reordering), the paper cannot cleanly distinguish ambiguity-specific harm from general prompt brittleness. R1 noted that C5's type-specific failure modes (scope misapplication, referent misidentification, etc.) provide qualitative evidence against generic noise, partially mitigating this concern. **Consensus:** A small non-ambiguity perturbation control arm (even 50 clauses) would substantially strengthen the causal claim.

---

## 4. Consolidated Strengths

- **Clean matched-pair causal design** isolating ambiguity effect via minimal edits, with linguistic property controls (length CV=0.11, FK, parse depth, TTR). Genuine improvement over DRIP-R's observational approach.
- **Well-structured five-claim hierarchy** (C1→C2→C3→C4→C5) forming a coherent progressive narrative where each claim adds a non-redundant layer.
- **Informative null finding (C2)** with pre-commitment, TOST equivalence testing, and clear practical interpretation (binary detection suffices).
- **Visibility finding (C3)** is genuinely novel and theoretically motivated. The trace-level evidence (conflict acknowledgment 61% vs 4%) provides direct mechanistic support.
- **Comprehensive model coverage** (2 API + 2 open-source, two capability tiers). Binary effect holding within 3pp across all four models (30.3–35.3pp).
- **Error analysis depth** — 8-category failure taxonomy with strong diagonal type-clustering and entropy analysis connecting to C4. Provides the linguistic depth EMNLP reviewers expect.
- **Thorough robustness checks** — reliability ICC=0.82, realism validation (KS p>0.22, discriminator 58%), bootstrap CIs throughout, signal-to-noise ratio 5.3×.

---

## 5. Consolidated Weaknesses

### Major

| ID | Issue | R1 | R2 | Fixable? |
|----|-------|----|----|----------|
| W1 | **C2/C3 internal tension unresolved** — omnibus null (p=0.39) contradicts significant CP-scopal pairwise (p=0.015). TOST margin ±15pp is generous. | M1 | Major | Yes — reframe C2, justify TOST margin |
| W2 | **Missing judge calibration** — plan_009 (100 human-annotated episodes) absent from paper. κ=0.91 is LLM-LLM agreement, not validated accuracy. | M2 | Endorsed | Yes — report plan_009 results |
| W3 | **Title overclaims** — universal "All Ambiguity" claim tested on 6 types, 2 domains, synthetic injection. | Partial | Major | Yes — soften title |
| W4 | **Prompt sensitivity confound** — no non-ambiguity perturbation control to distinguish ambiguity-specific harm from general prompt brittleness. | Endorsed | Raised | Partially — C5 type-specific failure modes mitigate |
| W5 | **C3 pre-registration status unclear** — may be exploratory finding promoted to core claim post-diagnostic. p=0.015 may not survive correction. | M3 | Partial | Yes — clarify in paper |
| W6 | **Incompleteness confound** — unambiguous variants add information, not just resolve ambiguity. Effect size (32.8pp) may be inflated. | M4 | Minor | Partially — quantify info delta |

### Minor

| ID | Issue |
|----|-------|
| W7 | No figures in 8-page paper (both reviewers) |
| W8 | Thin reference list — 8 citations, missing key works in ambiguity detection, prompt sensitivity, garden-path, agent safety (both reviewers) |
| W9 | No Claude models tested (both reviewers) |
| W10 | Two-domain limitation (retail + airline, both customer-service) — limits universality claim |
| W11 | Classifier PoC lacks baselines (no zero-shot LLM comparison, no existing ambiguity detector comparison) |
| W12 | Conservative refusal (5%) coded in failure taxonomy despite being described as "non-violation" — internal inconsistency (R1) |
| W13 | Ecological validity — single injected clause differs from naturally ambiguous document (R2) |

---

## 6. Questions for Authors (Priority-Ordered)

1. **Judge calibration (W2):** Was the planned human calibration study (100 episodes) conducted? If so, what was the LLM judge's precision/recall against human labels? If not, what is the basis for trusting the κ=0.91 as measuring genuine violation detection accuracy?

2. **C2/C3 reconciliation (W1):** How do you reconcile the C2 null (type doesn't predict severity) with C3 (CP and scopal significantly differ)? Was C3 pre-registered as an independent planned contrast, or was it selected post-hoc from the pairwise matrix after the diagnostic study?

3. **TOST margin justification (W1):** Why ±15pp for the equivalence margin? A 15pp difference in safety violation rates is operationally meaningful. Would C2 hold with a tighter margin (e.g., ±10pp)?

4. **Prompt sensitivity (W4):** How do you distinguish ambiguity-specific harm from general prompt brittleness? Have you considered a control arm with non-ambiguity perturbations of similar surface magnitude?

5. **Berry & Kamsties operationalization:** You measure agent-vs-intent deviation, but Berry & Kamsties define nocuity as inter-reader divergence. Did you test whether different models adopt different readings of the same ambiguous clause (true nocuity), or only whether each model deviates from ground truth?

---

## 7. Experimental Coverage Assessment

| Experiment | Reported? | Adequacy |
|------------|-----------|----------|
| Clause generation (plan_001) | Yes (Appendix B) | Adequate |
| API study (plan_002) | Yes (Tables 1,3,4) | Adequate |
| Local study (plan_003) | Yes (Tables 1,3,4) | Adequate |
| Full analysis (plan_004) | Yes (Tables 1–4) | Adequate |
| Error analysis (plan_005) | Yes (Tables 5–6, §6) | Adequate — but missing failure mode × type cross-tabulation table |
| Reliability (plan_006) | Yes (Appendix C) | Adequate |
| Realism validation (plan_007) | Yes (Appendix D) | Adequate |
| Classifier PoC (plan_008) | Yes (Table 7) | Adequate but lacks baselines |
| **Judge calibration (plan_009)** | **NOT REPORTED** | **Critical gap** |

---

## 8. Consolidated Scores

| Dimension | Score | Justification |
|-----------|-------|---------------|
| **Soundness** | **3.5** | Core matched-pair design is solid, C1 is robust (signal-to-noise 5.3×), C5 provides mechanistic depth. Weakened by: unresolved C2/C3 tension, missing human judge calibration, generous TOST margin, unclear C3 pre-registration status, prompt sensitivity confound. |
| **Excitement** | **3.5** | Timely research question bridging CL and agent safety. C3 (visibility) and C5 (failure taxonomy) are genuinely interesting. C1 binary effect is expected but magnitude is noteworthy. C4 capability gradient adds analytical value. Scope limited by 2 domains and synthetic ambiguity. |
| **Reproducibility** | **3.0** | τ²-bench is public, statistical plan is clear, bootstrap CIs reported. Weakened by: clause pairs not released, cross-judge prompt not provided, API models non-deterministic and time-varying, vLLM configuration underspecified, no code/data release commitment. |
| **Overall Assessment** | **3.5** | **Borderline Conference.** The paper makes a clear empirical contribution on a timely topic with a well-designed causal study and a satisfying five-claim architecture. C3 (visibility) and C5 (error taxonomy) are the most distinctive contributions. However, the C2/C3 tension, missing judge calibration, title overclaim, thin references, and absent figures prevent confident Main recommendation. This is a strong Findings paper that could reach Main (4.0) with targeted revisions: (1) report judge calibration, (2) reframe C2/C3 relationship, (3) soften title, (4) expand references, (5) add figures. |
| **Confidence** | **4** | Both reviewers conducted thorough independent reviews and cross-shared. Key concerns are convergent. Main uncertainty: whether plan_009 was conducted but omitted vs. never run. |

---

## 9. Revision Roadmap (Priority Order)

1. **[Critical]** Report judge calibration results (plan_009) or conduct human annotation validation.
2. **[High]** Explicitly address C2/C3 relationship — reframe C2 as "no large type effect" or explain visibility as orthogonal dimension; tighten TOST margin; clarify C3 pre-registration status.
3. **[High]** Soften title to match evidence scope (6 tested types, 2 domains).
4. **[High]** Expand reference list — add ambiguity detection, prompt sensitivity, garden-path, and agent safety benchmark citations.
5. **[Medium]** Add figures — at minimum: forest plot (C1), heatmap (C4), visibility mechanism illustration (C3).
6. **[Medium]** Discuss prompt sensitivity confound explicitly; consider adding a small non-ambiguity perturbation control.
7. **[Low]** Add classifier baselines (zero-shot LLM detection); quantify incompleteness information asymmetry; address Claude model gap.
