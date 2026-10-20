---
dream_id: dream_20260515T020837
tier: median
overall_score: borderline accept
timestamp: 2026-05-15T03:02:57.584607+00:00
---

# Dream Review Report: "Error Injection Helps Tool-Use but Hurts Planning"

**Venue**: Insights from Negative Results in NLP @ EMNLP 2026
**Review Mode**: Full (2 Reviewers + Roundtable)
**Scoring Scale**: ARR (Soundness/Excitement/Overall 1-5)

---

## Venue Calibration

The Insights from Negative Results in NLP workshop accepts short papers (up to 4 pages + references) reporting negative or unexpected results with important implications for future research, highlighting methodological issues or pervasive misunderstandings. The workshop uses ARR-style scoring. Acceptance rate is estimated at ~40-50% for workshop papers. The review evaluates whether the negative result is (1) genuine, (2) well-established methodologically, and (3) informative for the community.

---

## Reviewer Assignments

- **R1**: Methods + Experiments
- **R2**: Novelty + Related Work

---

## Step 1: Independent Reviews

### R1 (Methods + Experiments)

**Scores**: Soundness 3/5 | Excitement 3/5 | Overall 3/5 | Confidence 4/5

**Strengths**:
- Clean controlled comparison: same-source dual-formatting (TaxEI vs Random differ only in taxonomy label presence) eliminates confounds. Textbook controlled design.
- Transparent statistical reporting: all per-seed results shown, p-values reported honestly, hierarchical claims structure ranks findings by robustness rather than cherry-picking.
- Pre-registered termination criteria: the decision to frame as negative result followed explicit pre-set criteria, reducing post-hoc narrative flexibility.
- Per-operator locality gradient (C4 +3.1pp → C1 -2.1pp → P1 -5.5pp → P2 -8.3pp) provides the most compelling mechanistic evidence for the task-structure hypothesis.
- Qualitative failure analysis with "error echo" examples (Table 7) provides concrete mechanistic evidence compensating for quantitative limitations.
- Comprehensive cost-benefit analysis (Table 9) makes practical implications clear.

**Weaknesses**:
- **"Constant taxonomy penalty" overclaim**: The paper claims ~6.4pp constant penalty across dose levels in Section 3.2. Given 47 tasks and discrete resolution (3/47 ≈ 6.38pp), this consistency is likely a discretization artifact driven by different task subsets at each dose level, not a systematic effect. The paper should present this as coincidental rather than systematic.
- **Single-seed dose-response**: The dose-response ablation uses only seed=42, yet 3-seed SD reaches 8.6pp. Each point estimate has an implicit confidence interval wider than the reported effects. The "threshold-plateau" shape could be noise.
- **Missing formal variance tests**: The variance gradient is the primary finding, but no Levene's test, F-test, or bootstrap variance-ratio test is reported. The primary claim lacks its own direct statistical test.
- **v3 vs v4 vanilla discrepancy**: The same method at seed=42 produces 74.5% (v3) vs 61.7% (v4) — a 12.8pp swing not discussed in the paper. This undercuts confidence in reported numbers.
- **Detection rate (0%) is underdeveloped**: Either the detection metric is poorly designed (binary flagging only) or the finding is informative — either way it deserves more than two sentences.
- **Page budget strain**: Six supplementary experiments in a 4-page workshop paper means each gets superficial treatment. Several (training dynamics, recovery prompting) contribute marginal evidence that could be cut to deepen treatment of stronger findings.

**Questions for Authors**:
1. Why not report a formal variance test (Levene's, bootstrap variance-ratio) for the primary finding?
2. How do you reconcile the "constant ~6.4pp taxonomy penalty" with the fact that different task subsets drive the gap at each dose level?
3. Which supplementary experiments have completed full multi-seed evaluation vs. partial/single-seed runs?

---

### R2 (Novelty + Related Work)

**Scores**: Soundness 3/5 | Excitement 3/5 | Overall 3/5 | Confidence 4/5

**Strengths**:
- The research question ("does error injection transfer from tool-use to planning?") is well-motivated and timely given PALADIN's recent success. Not the highest tier of novelty (testing generalization of technique X to domain Y), but the analytical depth of the negative result elevates it.
- The "task structure as moderating variable" framework (Table 13) is the paper's strongest novelty claim. The four-dimensional comparison (observability, recovery space, locality, feedback) is a useful conceptual contribution.
- The per-operator gradient mirroring the cross-environment gradient is genuinely insightful — it connects micro-level (within-ALFWorld operators) to macro-level (tool-use vs planning) in a coherent framework.
- The variance gradient finding has practical methodological value: it highlights the inadequacy of single-seed evaluation for error injection methods.
- The hierarchical claims structure (primary/secondary/exploratory) is honest and appropriate for underpowered studies.

**Weaknesses**:
- **PALADIN comparison is fundamentally confounded**: PALADIN uses recovery-paired trajectories (error + paired recovery demonstration), while TaxEI injects standalone error trajectories without paired recovery. This is arguably the most important methodological difference and is not adequately highlighted. The negative result may reflect the absence of recovery pairing rather than (or in addition to) task structure. The paper should test error injection WITH recovery pairing in ALFWorld to disentangle these factors.
- **Thin related work coverage** (only ~8 references for a workshop paper):
  - Missing **Reflexion** (Shinn et al. 2023): uses self-reflection on failures to achieve ~97% on ALFWorld. Directly relevant — inference-time self-reflection succeeds where training-time injection fails.
  - Missing **adversarial training literature** (Madry et al. 2018): well-documented accuracy-robustness tradeoffs and catastrophic overfitting parallel the dose-response findings.
  - Missing **curriculum learning** (Bengio et al. 2009): the dose-response threshold is exactly what curriculum learning theory predicts about difficult example proportion.
  - Missing **data mixing laws** (Ye et al. ICLR 2025): "critical proportion for catastrophic forgetting" is conceptually identical to TaxEI's threshold.
  - Missing **ETO/Agent-R/AgentRefine**: alternative agent-failure-learning approaches that should be positioned against.
- **Title/abstract misaligned with primary finding**: The title emphasizes "hurts planning" (a mean effect claim, p≈0.32) while the hierarchical structure correctly identifies variance increase as the primary finding. These should be aligned.
- **Paper length exceeds venue limits**: 9 pages with 13 tables for a 4-page workshop paper. Must be cut substantially; most supplementary experiments would need to move to appendix.
- **Task-structural framework is post-hoc and descriptive**: The four dimensions in Table 13 are not independently measured or quantified. A truly predictive framework would generate testable predictions about new domains.
- **EEF contrast underexploited**: The paper should develop a 2×2 framework: {positive signal, negative signal} × {tool-use, planning}. PALADIN = negative + tool-use (works); EEF = positive from failures + planning (works); TaxEI = negative + planning (fails). This would sharpen the argument considerably.

**Questions for Authors**:
1. PALADIN pairs each error trajectory with a recovery demonstration. Have you considered that the negative result reflects the absence of recovery pairing rather than task structure? Would you test recovery-paired injection in ALFWorld?
2. Why does the paper not discuss Reflexion, which achieves high performance on ALFWorld through inference-time failure reflection — the exact domain where TaxEI fails?
3. Can you formalize the task-structural framework enough to generate testable predictions for new domains (e.g., "error injection should help in domain X because...")?

---

## Step 2: Cross-Sharing

R1's key points shared with R2:
- The clean same-source dual-formatting design is a genuine methodological strength
- The dose-response "constant penalty" is likely a discretization artifact (3/47 ≈ 6.38pp)
- Formal variance tests are missing for the primary claim
- Training pipeline shows concerning v3→v4 instability (12.8pp swing at same seed)

R2's key points shared with R1:
- The PALADIN comparison is confounded not just by domain but by methodology (recovery-paired vs standalone)
- Major related work gaps weaken the theoretical positioning
- The paper is 2× over the venue page limit
- The title/abstract emphasize a secondary claim (mean degradation) over the primary claim (variance)

---

## Step 3: Convergence

### Points of Agreement (both reviewers)

1. **All scores converge: Soundness 3, Excitement 3, Overall 3**. The paper has a sound core design but multiple execution issues preventing higher scores.

2. **The per-operator locality gradient is the paper's best contribution**. The C4→C1→P1→P2 gradient connecting error locality to TaxEI effect direction is the most compelling evidence for the task-structure hypothesis. P2's near-significant effect (p≈0.06) is the strongest individual finding.

3. **The "constant taxonomy penalty" claim must be corrected**. Both reviewers independently flagged this as an overclaim. The ~6.4pp consistency across dose levels is a discrete-resolution artifact, not evidence of a systematic additive penalty.

4. **Single-seed dose-response is a significant limitation**. With 3-seed SD up to 8.6pp, single-seed point estimates have implicit confidence intervals wider than the reported effects. The "threshold-plateau" shape may be noise.

5. **Formal variance tests are missing for the primary claim**. The variance gradient is presented as the primary finding but lacks its own direct statistical test (Levene's, F-test, bootstrap).

6. **Paper length far exceeds venue limits**. 9 pages / 13 tables for a 4-page workshop paper requires substantial cutting.

7. **The qualitative failure analysis and error echo examples are high-value**. Both reviewers agree these provide mechanistic insight that compensates for quantitative limitations.

### Points of Productive Disagreement

1. **Relative importance of the PALADIN confound**: R2 views the recovery-pairing confound (PALADIN uses error+recovery pairs; TaxEI uses standalone errors) as potentially more important than task structure in explaining the negative result. R1 acknowledges the confound but considers the within-environment per-operator gradient (which holds task structure constant while varying error locality) as partial evidence that task structure matters independently. **Resolution**: Both agree the paper should explicitly discuss the recovery-pairing confound as an alternative explanation and ideally test recovery-paired injection in ALFWorld.

2. **Severity of related work gaps**: R2 considers the thin bibliography (8 references, missing Reflexion, adversarial training, curriculum learning) a significant weakness. R1 considers it less critical for a workshop paper. **Resolution**: At minimum, Reflexion and one adversarial/curriculum learning reference should be added, as they directly inform the paper's core argument.

3. **Whether to cut supplementary experiments**: R1 suggests cutting weaker experiments (training dynamics, recovery prompting) to deepen treatment of stronger ones. R2 suggests most supplementary experiments should move to appendix given the 4-page limit. **Resolution**: The core 4-page paper should focus on: main results (Table 1), dose-response (multi-seed if possible), qualitative failure analysis, and per-operator gradient. Scale ablation and WebShop can be appendix.

---

## Step 4: Consolidated Assessment

### Final Scores

| Dimension | R1 | R2 | Consensus | Justification |
|-----------|----|----|-----------|---------------|
| Soundness | 3 | 3 | **3/5** | Core experimental design is clean (same-source controlled comparison, multi-seed evaluation, pre-registered termination). However: single-seed dose-response, missing formal variance test for primary claim, overclaimed "constant penalty," and paper exceeds venue length. Adequate to support directional conclusions but not specific quantitative claims. |
| Excitement | 3 | 3 | **3/5** | The question is timely and the negative result is informative. The per-operator locality gradient and error echo phenomenon are genuinely interesting. But statistical power is insufficient for strong claims, the PALADIN comparison is heavily confounded, and the framework is post-hoc descriptive rather than predictive. Provides directional warnings rather than crisp boundary conditions. |
| Overall | 3 | 3 | **3/5** | Suitable for the Insights from Negative Results workshop with revisions. The core finding (error injection destabilizes embodied planning training without improving performance) is genuine and useful. The analytical depth (6 complementary experiments, hierarchical claims) goes well beyond "we tried X and it didn't work." Key revisions needed: correct taxonomy penalty overclaim, add formal variance tests, address related work gaps (especially Reflexion), discuss recovery-pairing confound explicitly, and cut to 4-page limit. |
| Confidence | — | — | **4/5** | Both reviewers are familiar with the relevant benchmarks, training methodology, and comparison papers. |

### Headline Assessment: **Borderline Accept**

The paper presents a genuine, informative negative result with a clean experimental design and honest statistical reporting. It is a natural fit for a negative results workshop. The per-operator locality gradient is a compelling micro-contribution. However, the paper needs non-trivial revisions: correcting the taxonomy penalty overclaim, adding formal variance tests, addressing related work gaps, discussing the recovery-pairing confound, and cutting to venue page limits.

### Summary of Required Revisions

**Must-fix (for acceptance)**:
1. Remove or reframe the "constant ~6.4pp taxonomy penalty" claim as coincidental rather than systematic.
2. Add formal variance test (Levene's or bootstrap) for the primary variance gradient finding.
3. Cut paper to 4 pages + references; move 3-4 supplementary experiments to appendix.
4. Fix all [?] references and expand bibliography (currently ~8 entries; add at minimum Reflexion, one adversarial training reference, and one curriculum learning reference).

**Should-fix (strengthens paper)**:
5. Explicitly discuss recovery-pairing as an alternative explanation for the PALADIN/TaxEI difference (PALADIN uses error+recovery pairs; TaxEI uses standalone errors).
6. Align title/abstract with primary finding: the variance gradient (robust) rather than mean degradation (p≈0.32).
7. Replicate dose-response across multiple seeds, or explicitly caveat all dose-response conclusions as single-seed.
8. Develop the EEF contrast into a 2×2 framework: {positive, negative signal} × {tool-use, planning}.

**Nice-to-have**:
9. Test error injection with recovery pairing in ALFWorld to disentangle task-structure vs. methodology confound.
10. Formalize the task-structural framework enough to generate testable predictions for new domains.
11. Expand detection rate discussion or remove it.

### Experiment Coverage Assessment

The paper reports 6 supplementary experiments beyond the core 3-condition comparison:

| Experiment | In Paper? | Contribution to Claims | Assessment |
|------------|-----------|----------------------|------------|
| Training Dynamics (loss decomposition) | Yes (§4.1) | Marginal — 0.02 gap not significant | Could be appendix |
| WebShop Replication | Yes (§4.2) | Moderate — confirms directional consistency | Keep in main or appendix |
| Qualitative Failure Analysis | Yes (§4.3) | High — error echoes provide mechanistic insight | Keep in main body |
| Scale Ablation (25K/50K) | Yes (§4.4) | Moderate — shows scale doesn't close gap | Appendix |
| Recovery Prompting (5-shot) | Yes (§4.5) | Moderate — isolates delivery mechanism | Appendix |
| Per-Operator Deep Dive | Yes (§4.6) | High — locality gradient is best finding | Keep in main body |

**Recommended 4-page structure**: Introduction → Method → Main Results (Table 1 + dose-response with caveats) → Qualitative Failure Analysis (error echoes) → Per-Operator Gradient (locality analysis) → Discussion (task-structural lens + limitations) → Conclusion. Move training dynamics, WebShop, scale ablation, and recovery prompting to appendix.

### Key Takeaway for the Research Team

The paper's strongest contributions are (1) the variance gradient as an empirical finding about training instability, (2) the per-operator locality gradient connecting micro-level error properties to macro-level domain effects, and (3) the qualitative error echo phenomenon. These should be the backbone of the final paper. The weaker contributions (constant taxonomy penalty, dose-response threshold location, exact mean degradation magnitude) should be presented with appropriate caveats or moved to supplementary material. The paper's honest, hierarchical framing of claims is a strength — lean into it rather than overclaiming on the weaker findings.