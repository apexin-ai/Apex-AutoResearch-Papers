---
round: 26
review_mode: fresh
overall_score: 3.5 borderline conference
timestamp: 2026-05-23T12:03:05.786985+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: True
---

# Consolidated Review Report — Round 26 (Fresh)

**Paper**: "Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on LLM Agent Safety"
**Venue**: EMNLP 2026 via ARR May cycle
**Reviewers**: 2 (R1: 方法严谨性, R2: 新颖性与完整性)
**Date**: 2026-05-23

---

## Summary

This paper uses a matched-pair causal design to study how policy ambiguity affects safety violations in LLM agents. Using 300 clause pairs across a six-type taxonomy on τ²-bench with five models (2,997 episodes), the authors show ambiguous clauses increase violations by +34.0pp (+31.0pp confound-free). The core finding is a "type-mechanism dissociation": ambiguity type predicts failure mechanism (Cramér's V=0.45) but not violation rate (V=0.14). Error analysis reveals "disambiguation neglect" (4.6% awareness) and "systematic nocuity" (77% permissive bias, convergent errors).

---

## Strengths

**S1. Matched-pair causal design is methodologically strong.** Rare in agent safety literature. Perturbation controls (Δ_perturb = -0.67pp, CI [-8.0, 6.67]) convincingly exclude surface-level rewriting as alternative explanation. 300 clause pairs × 5 models with 96% initial annotator agreement provides solid internal validity.

**S2. Comprehensive statistical analysis and transparency.** TOST equivalence testing across 7 margins, bootstrap cluster analysis, ICC variance decomposition, cross-benchmark replication (SOPBench), cross-architecture replication (Gemini, LLaMA), and 15 pages of appendices addressing nearly all foreseeable reviewer questions.

**S3. Type-mechanism dissociation has practical value.** Even with reliability caveats, the directional finding that type predicts mechanism more strongly than severity is actionable: clause-level auditing > type-level risk classification.

**S4. Real-world grounding.** Prevalence audit (24 production documents, 407 clauses, 55–87% ambiguous) establishes practical relevance. SOPBench cross-benchmark replication confirms directional consistency.

**S5. Confound handling is honest.** Incompleteness information-addition confound is explicitly identified, separately analyzed (Appendix F), and the confound-free effect (31.0pp) is reported alongside the full effect (34.0pp).

---

## Weaknesses

### Must-Fix (3 issues — affect acceptance decision)

**MF1. [consensus, critical] Type-mechanism dissociation (Contribution 2) reliability is insufficiently supported.**
- Location: §6.1, Appendix AE
- The core evidence for V=0.45 rests entirely on LLM-coded failure mechanism labels, while human annotation agreement is κ=0.15 (near chance). The paper acknowledges this is an "upper bound" (§6.1) but still presents it as a headline contribution and abstract number. The contrast with violation severity agreement (κ=0.653) is stark: the same annotators reliably identify *whether* agents violate but cannot agree on *how* they fail, suggesting the failure mechanism taxonomy's construct validity is itself problematic. LLM coding consistency may reflect systematic classification preferences (e.g., routing incompleteness to "gap-filling") rather than genuine type-mechanism association.
- **Cross-response**: Both reviewers independently AGREE this is Must-Fix. R1 adds the κ=0.653 vs κ=0.15 contrast as direct evidence of construct validity problems. R2 initially raised it; R1 converges via the construct validity route.
- **Action required**: (a) §6 must devote a full paragraph (not parenthetical) to discussing κ=0.15 and its implications; (b) downgrade type-mechanism dissociation from "contribution" to "exploratory finding"; (c) abstract V=0.45 needs "LLM-coded" qualifier; (d) report V computed from human annotations as a floor estimate.

**MF2. [R1 Must-Fix, R2 partial agree] SESOI ±15pp lacks principled domain justification — but scope is narrower than initially argued.**
- Location: §4.6, Table 3
- The TOST equivalence structure (mid-tier cluster, incompleteness separation) depends on ±15pp. For safety-critical applications, 14.9pp additional violation rate at scale could mean hundreds of unsafe actions. At ±10pp, only 3/15 type pairs reach equivalence.
- **Cross-response refinement**: R2 correctly notes that C2's *core* evidence — Cramér's V=0.45 (type→mechanism) vs V=0.14 (type→violation rate) — does not depend on any TOST threshold. V=0.14 is computed directly from the contingency table. TOST supports the *auxiliary* claim that types form equivalence clusters in violation rate, not the headline dissociation. Therefore, SESOI affects the granularity of the type ordering, not the directional dissociation conclusion.
- **Action required**: (a) Provide safety-domain justification for ±15pp, or adopt ±10pp as primary with ±15pp as sensitivity; (b) in presentation, clearly separate the V comparison (threshold-independent) from the TOST equivalence structure (threshold-dependent); (c) scope C2 equivalence claims to the chosen margin.

**MF3. [consensus] Incompleteness confound control is methodologically insufficient.**
- Location: §4.5, Appendix F
- Token count as a proxy for information content has a fundamental flaw: a short phrase like "non-refundable" carries high policy information in few tokens, while lengthy clarifications may add minimal semantic content. The regression assumes linear token-count mediation, but the actual confound concerns information *type* (policy-relevant vs. disambiguating), not *quantity*.
- **Cross-response**: Both reviewers fully AGREE. R2 adds that incompleteness confound may partially explain the synthetic-to-natural effect gap (34pp vs 12.7pp).
- **Action required**: (a) Add a control condition with equal-length non-disambiguating policy text; or (b) exclude incompleteness from primary causal claims and treat as observational evidence, using confound-free 31.0pp as the headline effect.

### Should-Fix (9 issues — affect scoring)

**SF1. [R2 Must-Fix → R1 REBUT → consensus Should-Fix] "Nocuous" terminology semantic inversion needs stronger justification.**
Berry et al. (2004) define nocuous = divergent interpretation; this paper finds convergent error. R2 elevated to Must-Fix; R1 REBUT argues the semantic extension is defensible — Berry's core meaning is "harmful" (vs. innocuous), and §6.3 explicitly addresses the inversion. Both agree Introduction should handle this earlier (currently first discussed in §6.3, too late). R1: "标题的功能是引起注意和传达核心 message（'policy ambiguity is harmful'），§6.3 的详细论证足以为熟悉 Berry et al. 的读者消解歧义。" **Consensus**: Should-Fix — expand Introduction treatment; consider whether "systematically harmful" or "convergently nocuous" would be more precise.

**SF2. [R1 Should-Fix → R2 REBUT] Authorization scope: discuss construct difficulty rather than remove.**
κ=0.385 (lowest), 52pp cross-model range (largest), drives C4 interaction, ρ=0.09 cross-judge-group discordance. R1 suggested presenting five-type taxonomy as primary. R2 REBUT: "将一个'难以可靠标注'的类型从 taxonomy 中移除是方法论上的倒退：如果某种歧义在实践中特别难以诊断，这恰恰是需要被 taxonomy 保留并研究的类型。" Paper already provides Appendix O (sans-auth analysis). **Consensus**: Retain in taxonomy but add 1-2 sentences in §5.2 main text discussing construct difficulty and its implications for interpreting auth scope results.

**SF3. [consensus] Synthetic-to-natural effect gap (34pp vs 12.7pp) and cross-domain ρ=0.26 need main text discussion.**
Both reviewers AGREE. The three-factor explanation (measurement grain, baseline compression, interaction depth) is in appendix only. ρ=0.26 (effectively zero for type rankings across domains) is only in Appendix Z but directly impacts taxonomy diagnostic claims. R2 adds that incompleteness confound may partially explain the gap. **Action**: Move both to Discussion §7; Conclusion should state type-level findings are domain-contingent.

**SF4. [R2 Should-Fix → R1 partial REBUT] Incremental contribution over DRIP-R (2026) needs explicit articulation.**
DRIP-R already establishes "ambiguity hurts agents" on 400 scenarios × 5 RE types. R1 REBUT argues the three differentiators are substantive: different outcome variable (safety violations vs decision quality), matched-pair causal design (excludes scenario-level confounds), and novel phenomena (type-mechanism dissociation, convergent nocuity). R1: "因果设计是实质性方法论进步，不应被简化为 '重复已知结论'。" But both agree the paper should explicitly answer: "what does the causal design change vs DRIP-R's correlational evidence?" **Action**: Add direct comparison paragraph in §2 or §7.

**SF5. [R2 Should-Fix, R1 AGREE] 'Ambiguity' broad usage creates tension with NLP community standards.**
Both AGREE. §3 "Scope of 'ambiguity'" argues functional equivalence only. R1 agrees on Poesio & Artstein (2005) citation but REBUTS renaming to "policy underspecification" (would lose lexical/scopal types that *are* linguistic ambiguity). **Consensus**: Reference underspecification/vagueness distinction; add "policy specification" qualifier; keep "ambiguity" as term.

**SF6. [R1 Should-Fix, R2 AGREE] Temperature=0 limits variance decomposition interpretation.**
Both AGREE. R2 adds nuance: ICC(1)=0.749 already shows 25.1% within-cell stochastic variance at temperature=0; this would increase further at temperature>0, reducing systematic component's share. R2: "但核心方向性结论（ambiguity increases violations, type predicts mechanism > rate）在合理 temperature 范围内应仍然成立。" **Action**: §5.1 variance decomposition paragraph should note temperature=0 constraint; not a fundamental threat but important scope condition.

**SF7. [R2 Should-Fix, R1 AGREE] Taxonomy 11→6 selection criteria need transparent reporting.**
Both AGREE. Ellipsis exclusion attributed to "RE attestation" but likely driven by minimal-pair construction difficulty. R1: "如果一种歧义类型无法构造最小对，排除它是合理的方法论决策，但应透明陈述为实际约束。" **Action**: Appendix M should honestly attribute practical constraints where they apply.

**SF8. [consensus] Abstract information density is excessive.**
Both AGREE. ~190 words with 8+ quantitative figures. R1 suggests keeping 3-4 core numbers. **Action**: Reduce to overall effect, confound-free effect, SOPBench replication, and type-mechanism V contrast.

**SF9. [R1 Must-Fix → R2 REBUT → consensus Should-Fix] Cross-provider reproducibility: add explicit cross-provider metric.**
R1 argued ICC(1)=0.919 limited to OpenAI family is a Must-Fix. R2 REBUT with three arguments: (1) ICC is methodologically a within-family nesting metric — computing it across providers may violate variance structure assumptions; (2) Kendall's W=0.396 (p=0.072) already serves as a cross-provider concordance metric; (3) all 5 models show significant effects, Appendix E confirms on 2 additional providers. R2: "将 GPT-5.4、Claude Sonnet 4.6、Qwen3-235B 放入同一 ICC 模型，其 variance structure 的假设可能不成立。" **Consensus**: Downgrade to Should-Fix. Add explicit cross-provider metric (Kendall's W or Krippendorff's α) in appendix; relabel §4.4 claim scope.

### Minor (6 issues)

- M1. "Confound-free" terminology used inconsistently: Abstract "confound-free types" (excluding incompleteness) vs. Limitations "+34.0pp confound-free" (after perturbation controls). Both reviewers flagged.
- M2. Table 2 footnote markers (†, ‡) are small and easily missed.
- M3. "Confound-free types" first appears in §5.1 without inline definition.
- M4. Replication results (Gemini, LLaMA): R2 suggests main text mention; R1 REBUTS (8-page constraint). Consensus: add one sentence pointing to Appendix E.
- M5. Violation severity κ=0.653 vs failure mechanism κ=0.15 contrast is itself a finding worth main text mention in §6.1.
- M6. Pages 5-6 are continuous text without display items; consider summary table for key statistics.

---

## Reviewer Consensus (post-cross-response)

Both reviewers explicitly AGREE on:
1. **Type-mechanism dissociation evidence is weak** — two independent attack vectors (R1: TOST threshold dependency; R2: human κ=0.15) converge on the same conclusion
2. **Incompleteness confound** — token count is a poor proxy for information content; both fully agree
3. **Effect gap (34pp→12.7pp) needs main text discussion** — both agree
4. **"Nocuous" terminology needs attention** — R1 from accessibility angle, R2 from semantic accuracy; mutual reinforcement
5. **"Confound-free" terminology is inconsistent** — both flagged independently
6. **Abstract overloaded** — both agree
7. **Taxonomy 11→6 selection needs transparency** — both agree
8. **Core strengths**: matched-pair design, statistical rigor, confound honesty, prevalence audit

## Reviewer Divergence (post-cross-response)

1. **Authorization scope treatment**: R1 recommends removal to 5-type taxonomy; R2 REBUTS — low κ reflects construct difficulty, not invalidity. **Resolution**: SF2 — retain but discuss difficulty in main text.
2. **ICC cross-provider severity**: R1 Must-Fix; R2 REBUT — Kendall's W already provides cross-provider evidence, ICC is methodologically within-family. **Resolution**: SF9 — add explicit metric but not blocking.
3. **"Nocuous" severity**: R2 Must-Fix; R1 REBUT — semantic extension is defensible, §6.3 addresses it. **Resolution**: SF1 — expand Introduction treatment.
4. **DRIP-R incremental**: R2 questions sufficiency; R1 partially REBUTS — causal design is substantive upgrade. **Resolution**: SF4 — articulate what causal design changes.
5. **SESOI scope**: R1 says C2 "completely depends" on TOST; R2 correctly narrows — V=0.14 is threshold-independent. **Resolution**: MF2 scope refined.

---

## Questions for Authors

Q1. What is Cramér's V(type→mechanism) computed from human annotations? Even with low κ=0.15, this provides a floor estimate for the true dissociation strength.

Q2. In unambiguous conditions, what is agents' "false positive" ambiguity awareness rate? If agents rarely discuss ambiguity in either condition, the 4.6% may reflect general low metacognition rather than ambiguity-specific neglect.

Q3. For authorization scope (κ=0.385), at what agreement threshold would the type be excluded from the taxonomy rather than treated as a "difficult construct"?

Q4. Could a control condition for incompleteness be designed — adding equal-length non-disambiguating policy text — without requiring new experiments?

Q5. DRIP-R's correlational design leaves which specific confounds unaddressed that your causal design resolves? Can you articulate one concrete example where the causal conclusion differs from what correlation alone would support?

---

## Missing References

1. **Poesio & Artstein (2005)** — "Annotating (Anaphoric) Ambiguity." Relevant to §3's discussion of ambiguity vs. underspecification vs. vagueness. Both reviewers agree this is needed.
2. **Bai et al. (2022)** — "Constitutional AI." Relevant context for the 77% permissive bias finding in §6.3. R1 agrees; provides mechanism explanation for why models default to permissive interpretation.
3. **Zhou et al. (2023)** — "Instruction-Following Evaluation for Large Language Models" (IFEval). R1 REBUTS relevance — paper already cites more directly relevant agent safety benchmarks. **Optional, not required.**

---

## External Review

**Status**: Not requested (project not configured for external review).

---

## Visual Layout Check (non-scoring)

Visual check completed (3 warnings, 16 info items, 0 critical):
- ⚠️ **Pages 5-6**: Continuous 2 pages of pure text (Methods 4.3-4.6 + Results 5.1-5.2) without display items. Dense quantitative results in prose are reviewer-unfriendly.
- ⚠️ **Page 8**: Extremely crowded — Figures 2, 3, 4 + Discussion + Conclusion all compressed into one page. Axis labels at readability edge when printed.
- ⚠️ **Page 23**: Final appendix page ~85% blank.
- ✅ Main text exactly 8 pages (EMNLP compliant). Limitations p9 (compliant). Double-blind correct. No overflows or LaTeX errors.

---

## Overall Assessment

**Score: 3.5 (Borderline Conference)**
**Confidence: 4/5**

Both reviewers independently rate 3.5 (Borderline Conference) with high confidence. Cross-response discussion refines but does not change the overall assessment.

This paper makes a methodologically rigorous contribution to an important and timely problem. The matched-pair causal design is rare in agent safety literature, and the experimental execution (5 models, 2,997 episodes, 15-page appendix) demonstrates high scientific standards.

Three Must-Fix issues prevent a confident Conference recommendation:

1. **Type-mechanism dissociation reliability** (MF1): Both reviewers agree this is the paper's most novel claim but also its weakest evidential link. Two independent attack vectors — human κ=0.15 (R2) and TOST threshold dependency for the equivalence half (R1) — converge. The κ=0.653 vs κ=0.15 contrast (same annotators: reliable on *whether*, near-random on *how*) is particularly damaging.

2. **SESOI justification** (MF2): Affects the TOST equivalence structure, though the core V comparison is threshold-independent (per R2's cross-response). Still needs domain grounding.

3. **Incompleteness confound** (MF3): Both reviewers fully agree. Token count is an inadequate proxy. The highest-risk type's effect remains partially confounded.

Cross-provider reproducibility (originally MF4) was downgraded to SF9 after R2's methodological argument that Kendall's W already provides cross-provider evidence and ICC is inherently a within-family metric.

**Recommendation path**:
- **Findings (3.0-3.5)**: Achievable now. Downgrade dissociation to exploratory, use 31.0pp as headline, add domain qualifiers.
- **Conference (4.0)**: Requires MF1 (dissociation reliability discussion), MF2 (principled SESOI or scoped claims), MF3 (better incompleteness control or exclusion from causal claims), plus SF1-SF4.

**Current recommendation**: Findings-acceptable. Conference-borderline, conditional on Must-Fix resolution.

---

## Detailed Comments

### §1 Introduction
- Contribution (2) should carry a reliability caveat referencing §6's LLM-coding limitation (MF1).
- "We show that LLM agents invert this pattern, exhibiting convergent rather than divergent misinterpretation" — needs expansion as the foundation for the title's "nocuous" claim (SF1).

### §3 Taxonomy
- "Scope of 'ambiguity'" paragraph needs Poesio & Artstein (2005) reference and systematic engagement with ambiguity/underspecification distinction (SF5).
- Li et al. 11→6 mapping should honestly attribute practical constraints (SF7).

### §4 Method
- §4.6 SESOI: "pragmatic default" needs either domain grounding or explicit scoping of downstream claims (MF2).
- Cross-judge design asymmetry (3 vs 2 models per judge) should be explicitly noted.

### §5 Results
- §5.1: "confound-free types" needs inline definition (M3).
- Variance decomposition should note temperature=0 constraint (SF6).
- Clearly separate V comparison (threshold-free) from TOST equivalence structure (threshold-dependent) in C2 presentation (MF2).

### §6 Error Analysis
- κ=0.15 implications for Contribution 2 need a full paragraph, not parenthetical (MF1).
- κ=0.653 vs κ=0.15 contrast deserves explicit main text discussion (M5).
- Disambiguation neglect: add unambiguous-condition baseline (Q2).

### §7 Discussion
- Three-factor explanation for effect gap and ρ=0.26 cross-domain type ranking must appear here (SF3).
- Authorization scope construct difficulty needs 1-2 sentences (SF2).
- DRIP-R differentiation should be explicit (SF4).
- Permissive bias (77%) should reference Constitutional AI literature (missing ref #2).

### §8 Conclusion
- "clause-level policy auditing is the actionable intervention" depends on dissociation (MF1 concern); add appropriate hedging.
- "type-level findings are domain-contingent" should be stated (SF3).

### Limitations
- Add one sentence on type-mechanism dissociation's dependence on LLM coding labels (MF1).