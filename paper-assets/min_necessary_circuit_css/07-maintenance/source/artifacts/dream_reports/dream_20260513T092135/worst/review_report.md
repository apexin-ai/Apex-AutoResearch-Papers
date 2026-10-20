---
dream_id: dream_20260513T092135
tier: worst
overall_score: borderline reject
timestamp: 2026-05-13T10:18:09.714559+00:00
---

# Dream Review Report: "Binary Consensus Does Not Improve Circuit Discovery"

**Dream ID**: 20260513T092135
**Venue**: EMNLP 2026 Findings
**Review Mode**: Full (2 Reviewers + Roundtable)
**Scoring Rubric**: ACL Rolling Review (Soundness / Excitement / Overall Assessment, each 1–5)

---

## Roundtable Process

### Step 1: Independent Reviews

**Reviewer 1 (R1) — Methods & Experiments Focus**
- Soundness: 3/5 | Excitement: 3/5 | Overall: 3.0/5 | Confidence: 4/5

**Reviewer 2 (R2) — Novelty & Related Work Focus**
- Soundness: 3/5 | Excitement: 2/5 | Overall: 2.5/5 | Confidence: 4/5

### Step 2: Cross-Sharing

R1 → R2: Flagged that ablation method comparison (zero vs mean) is reported only for IOI (Table 4) but not extended to other tasks. If mean ablation dramatically changes results on Arithmetic or SVA, the "0/6 universal failure" headline may be zero-ablation-specific. Also flagged asymmetric size controls — size-controlled analysis only applied to the positive case (IOI), not to failing tasks where CSS also produces fewer edges.

R2 → R1: Flagged that the "community assumption" — that practitioners actually use binary consensus — is asserted without any citations to papers performing cross-method binary consensus. Mondorf et al. (2025) does continuous averaging, CIRCUS (Parekh 2026) does within-method threshold diversity — neither is the binary cross-method consensus attacked here. If no one actually does this, the paper tests a straw man. Also flagged extremely thin related work (9 references for an EMNLP paper).

### Step 3: Convergence — Agreements and Disagreements

**Full agreement (both reviewers)**:
1. The **ACDC binarization pathology** (Failure Mode 1) is a genuinely novel, concrete, and actionable finding — CSS(1.0) ⊆ C_ACDC by construction due to isinf sparsity. This alone is a useful contribution to practitioners.
2. The **component-level scoring collapse** (Failure Mode 2) on Qwen-0.5B is the most insightful finding, with genuine implications beyond the consensus question — IFR block-voting in L0–5, ACDC node-broadcasting in L18–23, zero edge overlap.
3. The **missing continuous averaging baseline** (Mondorf et al. 2025) is a critical gap. Without testing whether continuous averaging also fails, the paper cannot distinguish "consensus fails" from "binarization fails."
4. **K≈2 effective diversity** (EAP-IG/EP Jaccard up to 0.695) is a real confound — the paper is mostly testing "ACDC vs. gradient pair" rather than genuine 3-method consensus.
5. **Bootstrap methodology** (paired BCa, B=10,000) is correctly applied. Statistical claims are properly calibrated.
6. The **size-controlled IOI analysis** (Table 3) is well-executed confound analysis — top-7 EAP-IG (CPR=0.125) exceeds CSS(1.0) (CPR=0.1095).
7. **Soundness = 3/5** — core experiments adequate, but gaps in ablation coverage and baseline completeness.

**Partial agreement**:
- Both acknowledge the paper is **intellectually honest** and **well-calibrated** in its epistemic claims. The limitations section is substantive.
- Both agree the **Jaccard diagnostic** (§5.8) is undercooked — n=6 data points, no clear pattern, appropriately demoted to "future work" in the paper itself.

**Disagreement → Resolution**:
- **Excitement**: R1 (3/5) argued the failure mode taxonomy has practical value for the interpretability community. R2 (2/5) argued the core answer is predictable from ensemble theory (intersection requires diversity + accuracy; paper shows these are unmet). **Resolved at 2/5**: R2's argument prevails — the high-level answer *is* predictable, and the individual failure mode findings (FM1, FM2) would be better served by a shorter format. The scaling degeneration insight is valuable but the overall narrative adds limited surprise.
- **Overall Assessment**: R1 (3.0) vs R2 (2.5). **Resolved at 2.5/5 (borderline reject)**: The convergence was driven by three compounding issues: (a) the straw man risk — no evidence that the community actually practices binary consensus in the form tested; (b) the missing continuous averaging baseline, which is the single most informative absent experiment; (c) the title/abstract overclaims ("fundamentally flawed," "universally fails") relative to evidence from K≈2 effective methods on 2 model scales.

### Step 4: Consolidated Assessment

---

## Summary of Contributions

The paper formalizes Circuit Selection by Consensus (CSS) — taking the intersection of binarized circuits from multiple discovery methods — and tests it across 6 task×model configurations using EAP-IG, Edge Pruning, and ACDC. It finds 0/6 statistically significant positive advantages for CSS, identifies two mechanistic failure modes (ACDC binarization pathology and component-level scoring collapse at scale), and argues that binary consensus is fundamentally unsuited for current circuit discovery methods.

---

## Strengths

- **S1: Well-executed confound analysis.** The size-controlled IOI baseline (Table 3) is rigorous — constraining all circuits to 7 edges shows CSS(1.0) falls within the range of individual methods' top-7 selections. The zero-vs-mean ablation comparison (Table 4) provides a second independent line of evidence for the IOI artifact. These analyses demonstrate careful experimental thinking.

- **S2: ACDC binarization pathology is a concrete, actionable finding.** Showing that ACDC's isinf threshold produces 7–14 edges out of 32K, making CSS(1.0) ⊆ C_ACDC by construction, is useful independent of the consensus question. Any future work combining ACDC with other methods needs to account for this. The mechanistic explanation (loss-based discrete criterion vs. gradient-based continuous ranking) is clear and generalizable.

- **S3: Component-level scoring collapse provides genuine scaling insight.** The Qwen-0.5B analysis (Table 6) — IFR concentrating 95% of top-100 edges in L0–5, ACDC 85% in L18–23, zero edge overlap — demonstrates that the consensus problem is not just about binarization but about scoring granularity. The "impossible situation" framing (independent methods can't agree at edge level; agreeable methods aren't independent) is the paper's strongest conceptual contribution.

- **S4: Proper statistical methodology.** Bootstrap CIs (B=10,000), explicit p-values, paired comparisons. The paper does not overinterpret non-significant trends and correctly reports 3/6 significant *negative* effects.

- **S5: Intellectual honesty.** The progression from positive hypothesis to universal negative result is well-narrated. The paper acknowledges limitations substantively (K≈2 effective diversity, CPR-only metric, 2 model scales). The Jaccard diagnostic is appropriately demoted when it lacks calibration points.

---

## Weaknesses

- **W1 (Major): The "community assumption" is asserted without evidence.** The paper's contribution hinges on the claim that practitioners "actively use" binary consensus as informal validation. No citations are provided to papers that actually perform cross-method binary intersection of circuits. Mondorf et al. (2025) does continuous averaging; CIRCUS (Parekh 2026) does within-method threshold diversity; neither is binary cross-method consensus. If no one actually does this in the form tested, the paper attacks a straw man — testing a consensus strategy the community has already implicitly bypassed. The paper should cite specific publications, blog posts, or community standards documents where binary consensus is advocated or practiced.

- **W2 (Major): Missing continuous averaging baseline.** Mondorf et al. (2025) is the closest prior work and proposes a direct alternative to binary consensus. The paper discusses it in §6 but never tests it. This is the single most informative absent experiment: if continuous averaging also fails, the finding is "consensus in general fails" (much stronger); if it succeeds, the finding is "only the naive binary version fails, and there's a known fix" (much weaker and less publishable). Omitting this comparison leaves the paper's central claim fundamentally ambiguous.

- **W3 (Major): Incomplete ablation method comparison.** Zero vs. mean ablation is reported only for IOI (Table 4). The review context indicates mean ablation may dramatically change results on other tasks (e.g., Arithmetic CPR changes significantly under mean ablation). If the "0/6 universal failure" conclusion is specific to zero ablation, the headline finding is metric-dependent rather than robust. All 6 configurations should be evaluated under both ablation methods.

- **W4 (Moderate): K≈2 effective diversity confounds the core claim.** EAP-IG and EP have pairwise Jaccard up to 0.695, meaning the "3-method consensus" is effectively "ACDC vs. gradient pair." The paper acknowledges this in Limitations but then makes universal claims ("Binary Consensus Does Not Improve...") that are not warranted by testing with only one effectively independent method pair. Testing with a genuinely diverse third method (e.g., probing-based, causal scrubbing, or activation patching at different granularities) would substantially strengthen the claim.

- **W5 (Moderate): Thin related work.** Only 9 references for an 8-page EMNLP paper on mechanistic interpretability. Notable absences include: Goldowsky-Dill et al. (2023) on path patching, Hanna et al. (2023/2024) on circuit evaluation metrics, Miller et al. (COLM 2024) on faithfulness sensitivity to ablation method (directly relevant given §5.5), Lieberum et al. on circuit benchmarks, and deeper engagement with ensemble pruning literature beyond Kuncheva & Whitaker (2003). The paper needs substantially more contextualization.

- **W6 (Moderate): Title and abstract overclaim.** "Binary Consensus Does Not Improve Circuit Discovery" and "fundamentally flawed" are universal claims based on K≈2 effective methods, 4 tasks, and 2 model scales. The evidence better supports: "Binary consensus with current methods (including ACDC's isinf binarization) does not improve circuit discovery on the tested configurations." The paper's own analysis shows that IOI *could* have been a genuine success if not for size confound — suggesting consensus might work under favorable conditions (well-characterized task, accurate individual methods), consistent with ensemble theory rather than "fundamental flaw."

- **W7 (Minor): CIRCUS comparison is superficial.** CIRCUS is claimed to produce "negative CPR on all tested tasks" but no details (tables, numbers, analysis) are provided. Without evidence of a correct implementation, this claim is unreliable and should be removed or substantiated.

- **W8 (Minor): Asymmetric size controls.** Size-controlled analysis is applied only to IOI (the positive case). Failing tasks where CSS also selects fewer edges should receive the same treatment for completeness.

---

## Questions for Authors

1. Can you cite specific papers or community documents that actually perform binary cross-method consensus for circuit validation? The paper's contribution depends on this being a real practice.

2. Why was continuous score averaging (Mondorf et al. 2025) not included as a baseline? This is the most obvious comparison and its absence is conspicuous.

3. How do results change under mean ablation for Arithmetic, SVA, Factual Recall, and Qwen configurations? Is the "0/6 universal failure" robust to ablation method choice?

4. Have you considered testing with a genuinely diverse third method (not gradient-based) to address the K≈2 confound?

5. For the failing configurations, does CSS(1.0) outperform random circuits of the same size? If so, consensus still provides signal — it just doesn't beat the best single method. This distinction affects the strength of the negative claim.

6. Was the CIRCUS comparison (§6) run with a corrected implementation? What specific numbers underlie the "negative CPR on all tested tasks" claim?

---

## Minor Issues

- GPT-2 Small edge count stated as both "~32K" and "32,491" — use consistent precision.
- The Jaccard diagnostic section (§5.8) with n=6 points and no clear pattern could be compressed to 1–2 sentences rather than a full subsection.
- No figures in the paper — a forest plot of bootstrap CIs (Table 5) or a heatmap of method failure modes (Table 6) would significantly improve readability.
- The paper lacks a scatter plot for the Jaccard-vs-CSS-advantage data (Table 7), despite this being a natural visualization.

---

## Consolidated Scores

| Dimension | R1 | R2 | Converged | Rationale |
|-----------|----|----|-----------|-----------|
| Soundness | 3/5 | 3/5 | **3/5** | Core experiments adequate; ablation coverage gap, missing continuous averaging baseline, and CIRCUS reliability reduce confidence |
| Excitement | 3/5 | 2/5 | **2/5** | High-level answer predictable from ensemble theory; FM1 and FM2 individually insightful but better suited to shorter format |
| Overall | 3.0/5 | 2.5/5 | **2.5/5** | Borderline reject — straw man risk, missing key baseline, overclaiming, thin related work compound against acceptance |
| Confidence | 4/5 | 4/5 | **4/5** | Both reviewers familiar with circuit discovery and ensemble methods |

---

## Meta-Review Summary

This paper addresses a relevant question — whether binary consensus improves circuit discovery — and provides a thorough negative answer with two mechanistic failure modes. The ACDC binarization pathology and the component-level scoring collapse are genuinely insightful findings. However, three compounding issues push the paper below the acceptance threshold for EMNLP Findings:

1. **Motivation gap**: The paper never demonstrates that anyone actually uses binary consensus in the form tested, risking a straw-man framing.
2. **Missing key baseline**: The continuous averaging approach (Mondorf et al. 2025) is the most natural comparison and its absence leaves the central claim ambiguous.
3. **Overclaiming**: Universal negative claims ("fundamentally flawed," "does not improve") are not supported by testing K≈2 effective methods on 2 model scales.

**Recommendation**: Borderline reject. The failure mode analyses are the paper's strongest contribution and could anchor a revised submission that (a) provides evidence of the community assumption, (b) includes the continuous averaging baseline, (c) extends the ablation comparison to all configurations, and (d) right-sizes the claims to the evidence scope.

**Overall Score**: 2.5/5 (borderline reject)