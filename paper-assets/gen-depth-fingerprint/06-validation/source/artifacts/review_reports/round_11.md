---
round: 11
overall_score: 3.0 (Findings)
timestamp: 2026-05-17T17:35:19.373451+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 11 Consolidated Review Report

**Paper**: "Depth Fingerprinting: Detecting Recursive Generation Depth in LLM Text Chains"
**Target**: EMNLP 2026 (ARR May 2026 cycle, deadline 2026-05-25)
**Reviewers**: R1 (方法严谨性 + 实验设计), R2 (新颖性 + 完整性 + Related Work)

---

## Summary

The paper formulates generation depth classification (gen-0/gen-1/gen-2+) as a new task beyond binary AI text detection, identifies a "differential depth response" (DDR) where central-tendency features drift monotonically with recursive generation depth while shape features remain near-stationary, and builds a 7-feature XGBoost ensemble achieving 3-class LOGO F1=0.762 across 8 base-model generators from 5 families. A TOST equivalence test suggests detected distributional shift does not translate to downstream perplexity degradation.

---

## Strengths

1. **Novel and well-motivated task formulation**: Generation depth classification (gen-0/gen-1/gen-2+) fills a genuine gap between binary detection and source attribution. Independent convergence with two concurrent works (Broken Telephone, Markovian Chains) on ~3-class practical ceiling validates the research direction. [Unanimous]

2. **DDR is a genuine scientific insight**: The drifting vs. stationary feature decomposition provides structured, interpretable understanding of recursive generation dynamics. The location-shift-preserving-shape hypothesis has theoretical elegance and empirical support (KS statistics show 10× magnitude gap). [Unanimous]

3. **Exceptional experimental coverage**: LOGO/LOFO/cross-model/cross-reference/cross-temperature/cross-domain/cross-prompt/perturbation/length confound/classifier ablation/feature ablation/finer granularity/downstream utility — nearly every conceivable reviewer question is pre-addressed. Statistical methodology (bootstrap CI, McNemar, Bonferroni, TOST) exceeds average EMNLP standard. [Unanimous]

4. **Honest self-criticism**: Paper proactively identifies gen-0 seed sharing bias, reports instruct model failure (F1=0.338), t=1.0 degradation, and provides leak-free binary metric. Limitations section is comprehensive and candid. [Unanimous]

5. **Computational efficiency advantage**: Single 410M reference model (905 MB, 9.7 ms/text) vs. multi-detector ensembles (2 models, 2868 MB, 22.8 ms/text) with comparable binary F1. [Unanimous]

6. **Writing quality and format compliance**: No AI writing artifacts (no em-dashes, no -ing phrase abuse, no excessive paragraphing). ACL style with [review] option, anonymous, line numbers, 8-page main text, Limitations section present. [R2 confirmed]

---

## Weaknesses

### Must-Fix (影响接收决定)

**MF1** [CONSENSUS — R1-N1 + R2-N1] **TOST equivalence test methodology flawed and Contribution 3 over-packaged**

The paper's third contribution claims "depth-aware data selection yields training utility equivalent to random subsampling" (Abstract L8). This is problematic on multiple levels:
- Table 8 shows random subsampling **consistently outperforms** depth-aware (ppl 2.367 vs 2.387). Using "equivalent" is misleading when one method uniformly dominates.
- TOST with n=3 seeds produces Cohen's d = 86–120, which the paper itself acknowledges as "artificially inflated." Statistical power derives from extremely low seed-level variance, not genuine equivalence evidence.
- The ±2% margin is not justified from domain knowledge. Table 9 shows equivalence fails at ±1% margin.
- Fundamentally, this is a **null result**: the detected distributional shift has no practical downstream impact. Packaging this as a main contribution overstates its significance and paradoxically undermines the paper's data-curation motivation.

**Required action**: (1) Demote from Contribution 3 to Discussion analysis finding; (2) Replace "equivalent" with "does not substantially degrade"; (3) Acknowledge random > depth-aware honestly; (4) Caveat n=3 limitation explicitly.

---

**MF2** [CONSENSUS — R1-N2 + R2-W2] **Gen-0 seed sharing inflates headline 3-class metric**

All 8 generators share identical ~1000 Wikipedia seeds as gen-0. In LOGO, held-out generator's gen-0 texts appear verbatim in training (via other generators' gen-0), creating direct train-test overlap. Evidence:
- Confusion matrix: gen-0 recall = 99.4% vs. gen-1 = 75.0% vs. gen-2+ = 73.7%
- 3-class macro F1 = 0.762 is upward-biased; the leak-free binary metric (gen-1 vs. gen-2+) = 0.694 is the trustworthy number
- Despite paper correctly diagnosing this issue (§4.1 L8), Abstract/Introduction/Conclusion still lead with 3-class numbers (0.809, 0.762)

**Required action**: (1) Abstract must lead with binary F1 (0.764 cross-model, 0.694 LOGO) as primary metric; (2) 3-class numbers demoted to secondary with explicit caveat; (3) Ideally: separate gen-0 seeds per generator to eliminate overlap entirely.

---

**MF3** [CONSENSUS — R1-N3 + R2-N3] **Base-model-only + temperature sensitivity = zero real-world applicability; framing mismatch**

Two independently devastating limitations stack:
- **Instruct models**: OLMo-Instruct LOGO F1 = 0.338 (≈random baseline), Qwen3-0.6B-chat = 0.667. Real-world LLM text is overwhelmingly instruction-tuned.
- **Temperature**: Cross-temperature transfer Qwen3-1.7B drops from 0.789 → 0.418. At t=1.0, entropy mean ρ collapses from -0.60 to -0.002. Many APIs default to t=1.0.
- Combined: no real deployment scenario satisfies both base-model + known-temperature constraints.

The paper's Introduction motivates with web contamination (§1 L1-5) and §4.3 uses "competitive performance at substantially lower computational cost" — language implying deployment readiness. This creates a fundamental framing mismatch with the method's actual scope.

**Required action**: (1) Reframe from "detection/classification system" to "characterizing fundamental properties of recursive generation"; (2) Remove deployment-implying language ("competitive performance"); (3) Explicit scope statement in Abstract (base models, standard decoding); (4) Deeper analysis of WHY instruction tuning destroys signal (which factor dominates: length regulation, format constraints, RLHF shaping?).

---

**MF4** [DIVERGENCE — R2-N2; R1 partial rebut] **Method novelty insufficient for main conference**

R2 argues: 7 handcrafted features + off-the-shelf XGBoost constitutes zero algorithmic innovation. QLoRA (F1=0.905) demonstrates richer signal exists. CORAL/ordinal methods provide zero improvement. The paper's own §2.1 admission ("not a new detection method") confirms method contribution is negligible.

R1 partially rebuts: (1) Paper is honestly self-positioned as task formulation + empirical finding; (2) Simple interpretable method enables DDR decomposition that neural approaches cannot; (3) EMNLP has precedent for empirical finding papers.

**Director assessment**: The divergence is legitimate. If the paper clearly positions itself as an **analysis/phenomenon paper** (emphasizing DDR insight over classification pipeline), the contribution is appropriate for Findings. For main conference, methodological novelty or deeper theoretical understanding of DDR would be needed.

---

### Should-Fix (影响评分)

**SF1** [CONSENSUS] **DDR "shape preservation" overstated**: Levene tests reject equal variance for ALL features including shape features (p < 10⁻¹⁰). "Preserving distributional shape" should be "approximately preserving shape" or quantified as "order-of-magnitude smaller drift in shape features" (CV shift <3% vs >15%).

**SF2** [CONSENSUS] **Cross-model F1=0.809 uses 5-gen subset, not 8-gen**: Mistral-7B (LOGO binary F1=0.633, lowest) excluded from cross-model evaluation. The headline 0.809 may not hold with 8 generators. Must be prominently flagged as 5-gen result or re-run with full set.

**SF3** [CONSENSUS] **"Competitive performance" claim**: Abstract overstates. 7-feature 3-cl F1=0.774 vs 4-det+surface 0.795 (2.1pp gap). Binary F1 difference negligible. Should say "comparable binary performance at 2.4× lower cost."

**SF4** [CONSENSUS] **Temperature section title misleading**: "Temperature robustness" paragraph actually documents a hard failure mode at t=1.0. Rename to "Temperature sensitivity" and discuss cross-temperature transfer failure prominently.

**SF5** [CONSENSUS] **Pythia-410M reference model family bias**: Pythia generators achieve highest F1 (0.718-0.724) while reference model is Pythia family. Cross-reference spread (0.013) is on 5-gen subset only. Discuss architecture overlap in main text.

**SF6** [R1 only, R2 agrees limited impact] **XGBoost hyperparameters fixed**: 200 trees depth=6 may be suboptimal for 1-dimensional single-score baselines. Report tuned results or simpler classifier sanity check.

**SF7** [R2 only, R1 partial rebut] **Ordinal classification discussion insufficient**: §3.1 frames as ordinal task but main text never discusses why ordinal methods (CORAL, Frank-Hall) provide zero improvement. This is itself an interesting finding deserving explanation.

---

### Minor Issues

- entropy_min retained "for completeness" (LOFO Δ=+0.01pp, i.e., removing slightly helps). Provide statistical justification or drop.
- Figure 3 PNG format — regenerate as PDF for print quality
- Appendix confusion matrix uses 6-gen, not aligned with Table 1 (8-gen)
- Cross-domain evaluation uses t=1.0 while main experiment uses t=0.7 — add comparability note
- "Entropy" misnomer (actually token-level NLL) clarified only in footnote — move to §3.3 opening
- Tail decay rank range 100–1000 lacks theoretical motivation
- Bonferroni correction application scope not fully specified (which comparisons, how many?)
- Table 1 caption overly long with methodological explanation
- Pythia-1B 3-class F1 > Pythia-2.8B but binary F1 reverses — undiscussed crossover
- Generation failure rate (7.4% attrition from 40K to 37K) — causes not reported
- Some bib entries missing pages/volume (stamatatos_survey, koppel_authorship)

---

## Reviewer Consensus

| Issue | R1 | R2 | Status |
|-------|----|----|--------|
| TOST misleading / Contribution 3 over-packaged | [AGREE] | [AGREE] | **Consensus** |
| Gen-0 seed sharing inflates headline | [AGREE] | [AGREE] | **Consensus** |
| Base-model + temperature = no real applicability | [AGREE] | [AGREE] | **Consensus** |
| DDR "shape preservation" overstated | [AGREE] | [AGREE] | **Consensus** |
| Cross-model 5-gen vs 8-gen inconsistency | [AGREE] | [AGREE] | **Consensus** |
| "Competitive performance" overclaim | [AGREE] | [AGREE] | **Consensus** |
| Temperature section title misleading | [AGREE] | [AGREE] | **Consensus** |
| Spearman thresholds need citation | R1 raised | R2 [REBUT] (gap self-evident) | **Minor divergence** |
| Method novelty insufficient | R1 [REBUT] partial | R2 [AGREE] critical | **Major divergence** |
| Concurrent works need experimental comparison | R1 [REBUT] (infeasible) | R2 raised | **Minor divergence** |

---

## Reviewer Divergence

**Novelty assessment** (the key divergence determining overall score):
- **R1 (3.5)**: DDR as empirical finding + task formulation constitutes sufficient EMNLP contribution. Simple interpretable method is a feature, not a bug — enables the DDR decomposition insight.
- **R2 (3.0)**: Two concurrent works (Broken Telephone, Markovian Chains) reduce novelty premium. Feature engineering + XGBoost has near-zero technical novelty. QLoRA already demonstrates superior performance. Better suited for Findings.

Both agree: if paper repositions clearly as **phenomenon characterization** (DDR analysis paper) rather than **method paper**, contribution level is appropriate for Findings acceptance.

---

## Questions for Authors

1. Can you report a gen-0 hold-out experiment (per-generator independent seeds) to quantify true gen-0 generalization vs. seed memorization?
2. What domain knowledge justifies the ±2% TOST margin? At what margin does equivalence first hold?
3. Does cross-model F1=0.809 survive with 8 generators (including Mistral-7B)?
4. In 8-gen setting, does a non-Pythia reference model (e.g., OLMo-2-1B) change the per-generator F1 ranking?
5. Which factor dominates instruction-tuning's destruction of depth signal: length regulation, format constraints, or RLHF distribution shaping?
6. Why do ordinal-specific methods (CORAL, Frank-Hall) provide zero improvement despite the task having ordinal structure?

---

## Missing References

- Ordinal classification: proportional odds model, ordinal SVM, unimodal regularization (if framing as ordinal task, literature should be more comprehensive)
- Multi-round LLM generation quality degradation studies beyond model collapse
- Data contamination detection methods (overlap with provenance motivation)
- R2 notes: concurrent works comparison could benefit from citing their specific experimental protocols

---

## External Review

项目未配置外部审稿（`external_review.paperreview_ai.enabled` 未设置），未请求。

---

## Overall Assessment

**Score: 3.0–3.5 (Findings to Borderline Conference)**

| Reviewer | Score | Rationale |
|----------|-------|-----------|
| R1 | 3.5 (Borderline Conference) | DDR insight + task novelty + exhaustive experiments sufficient for borderline acceptance |
| R2 | 3.0 (Findings) | No method innovation + concurrent works + base-model-only = Findings-level |

**Director's consolidated assessment: 3.0 (Findings)**

Rationale: The paper presents a genuine empirical finding (DDR) and a well-motivated task formulation. However, four factors push it below the main conference threshold:
1. **Framing inconsistency**: Paper oscillates between "practical detection system" and "phenomenon characterization" without committing to either
2. **Headline metrics inflated**: 3-class F1 biased by gen-0 leakage; Contribution 3 (TOST) is a null result over-packaged
3. **Applicability gap**: Base-model-only + temperature sensitivity means the phenomenon, while interesting, cannot translate to any practical use case currently
4. **Method contribution near zero**: Acknowledged by the paper itself (§2.1)

**Recommendation**: Accept as **Findings** if MF1–MF3 are addressed (reframe positioning, fix headline metrics, demote TOST). For main conference, would need either (a) extension to instruction-tuned models or (b) deeper theoretical understanding of DDR mechanism.

**Confidence**: 4/5 (both reviewers carefully evaluated all sections and appendices; statistical methodology scrutinized in detail)

---

## Detailed Comments by Section

**Abstract**: Leads with biased 3-class numbers; uses "equivalent" for a null result; "competitive performance" overstates. Needs restructuring with binary F1 primary, scope qualification, honest downstream framing.

**Introduction**: Web contamination motivation (§1 L1-5) creates expectation of practical tool, but scope is base-model laboratory study. Contribution 3 should be demoted. "Competitive performance at substantially lower computational cost" should be qualified.

**Method (§3)**: Solid and clearly written. Minor issues: entropy misnomer (footnote insufficient), tail_decay range unjustified, entropy_min rationale weak, ordinal framing in §3.1 not substantiated by method.

**Results (§4)**: Strong experimental design. Issues: §4.2 "Temperature robustness" title misleading; "shape preservation" language too strong given Levene results; 5-gen vs 8-gen subset mixing needs explicit explanation.

**Discussion (§5)**: Over-fragmented with \paragraph{} headers. Good content but needs consolidation into natural paragraphs. Cross-temperature transfer discussion should be more prominent.

**Limitations**: Exceptionally thorough. Could add explicit statement that method is inapplicable in any real deployment scenario currently.

**Related Work (§2)**: Well-structured with clear positioning. Ordinal classification discussion could be expanded. Concurrent works comparison is conceptual but adequate (direct experimental comparison infeasible due to different chain types).