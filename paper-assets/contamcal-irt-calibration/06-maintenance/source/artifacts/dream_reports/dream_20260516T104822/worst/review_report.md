---
dream_id: dream_20260516T104822
tier: worst
overall_score: 3 - Reject
timestamp: 2026-05-16T11:33:44.234866+00:00
---


# Review: The Limits of Contamination Detection and Calibration

## Summary

This paper investigates whether post-hoc contamination calibration is feasible for LLM benchmark evaluation. It proposes ContamCal, a two-stage framework combining multi-signal detection (RRF-aggregated) with contamination-augmented 4PL IRT. Through controlled SFT injection experiments across scales (0.5B–72B), model families (Qwen, Llama), and training paradigms (SFT, RL), the paper argues for three "impossibility" results: (1) only embedding similarity works reliably for detection, and Min-K++ exhibits directional reversal at small scales; (2) Fisher Information analysis requires N≥50 models for reliable γ recovery; (3) contamination effects are scale/family/paradigm-dependent, making universal calibration infeasible. The paper reframes ContamCal as a diagnostic tool rather than a calibration solution.

## Overall Assessment

**Score: 3 / 6 (Reject)**

The paper tackles a timely and important question — whether we can statistically correct for benchmark contamination — and the negative/impossibility framing is intellectually honest. The Min-K++ directional reversal is a genuinely novel empirical finding. However, the impossibility claims significantly overreach the evidence. The controlled experiments use SFT injection (fundamentally different from pretraining contamination), key intermediate scale data is missing from tables, observational experiments cannot distinguish method failure from absence of contamination, and the paper generalizes from one specific framework's limitations to sweeping claims about all post-hoc calibration. The paper would need substantial revision to properly scope its claims and fill significant experimental gaps.

---

## Strengths

### S1: Important and timely research question
The question "can we calibrate benchmark scores for contamination?" is central to LLM evaluation integrity. The negative answer, if properly supported, would be a valuable contribution redirecting community effort toward contamination-robust evaluation designs.

### S2: Min-K++ directional reversal is a novel, replicable finding
The discovery that Min-K++ scores reverse direction at small scales (Cohen's d = −1.2 to −2.7 at 0.5B, d = −1.4 for Llama-3.2-1B) is the paper's strongest contribution. It replicates across model families, ruling out architecture-specific artifacts, and has immediate practical implications for any contamination detection pipeline using membership inference signals. This alone is publishable.

### S3: Fisher Information analysis provides useful theoretical grounding
The derivation of identifiability conditions (N≥50, AUC≥0.55) from Fisher Information of the 4PL+γ model (Eq. 3) is a clean theoretical contribution. The explicit characterization of how CI width scales as N^{−0.48} gives practitioners concrete guidance about when IRT-based calibration is feasible.

### S4: Well-articulated "Calibration Paradox"
The insight that detection succeeds where calibration is unnecessary (large models) and calibration is needed where detection fails (small models) is elegantly stated and well-supported. The "Access Paradox" (Section 4.6) is similarly crisp — the method requires open weights but the models most needing calibration are closed-weight.

### S5: Honest self-assessment in limitations
The paper acknowledges its own internal tension (operating below its own N≥50 recommendation) and excludes 0.5B from IRT pooling due to position bias artifacts. This intellectual honesty is commendable.

### S6: Comprehensive experimental coverage
Six experiments span quality control ablation, scale bridging, cross-family validation, RL/instruct models, frontier scale, and closed-weight degradation. The experiment design is systematic and well-motivated.

---

## Weaknesses

### W1 (Major): SFT injection ≠ pretraining contamination — impossibility claims don't transfer
The entire controlled experimental program uses SFT-based injection of paraphrased benchmark items. This is a fundamentally different mechanism from pretraining contamination, where items appear among billions of tokens during initial training. The "catastrophic forgetting" and "capacity displacement" observed at 0.5B (Section 4.1) are well-known SFT artifacts — they demonstrate that SFT on small models is destructive, not that contamination detection is impossible. Similarly, the near-zero effect at 7B (Section 4.2) may simply show that SFT injection doesn't add meaningful signal to a model that already knows the content from pretraining — it does NOT prove that pretraining contamination has no effect at 7B. The paper acknowledges this in Section 5.4 ("may not perfectly replicate pretraining contamination") but then proceeds to make sweeping impossibility claims as if this caveat doesn't exist. The impossibility results should be scoped explicitly to SFT-based contamination regimes.

### W2 (Major): Missing intermediate scale data in key tables
Table 2 jumps from 0.5B directly to 7B, omitting 1.5B and 3B results. The abstract mentions "3B borderline" and the review context confirms these experiments were run. The transition region (1–3B) is exactly where the interesting behavior occurs — where contamination effects shift from catastrophic to negligible. Omitting this data from the main table while claiming "monotonic attenuation" based on only two data points is a serious presentation gap. The paper needs a complete scale × dosage table (0.5B/1.5B/3B/7B) to support its claims.

### W3 (Major): Observational experiments (Exp 4, 5) conflate method failure with absence of contamination
Experiments 4 and 5 apply ContamCal to RL-trained and frontier models where ground-truth contamination status is unknown. Finding that all γ CIs include zero could mean: (a) the method fails to detect existing contamination, OR (b) these models genuinely aren't contaminated for these benchmarks (or contamination effects are real but small). The paper assumes interpretation (a) throughout but never rules out (b). Without ground truth, these experiments cannot distinguish method failure from true negatives. The near-zero-on-clean-benchmark specificity check (mentioned in the context but underemphasized in the paper) only validates absence of false positives, not presence of false negatives.

### W4 (Major): Impossibility claims overgeneralize from one framework
The paper shows that ContamCal (4PL+γ IRT with RRF-aggregated signals) fails in various regimes, then generalizes to "post-hoc calibration is provably infeasible" and "these structural limitations are not engineering problems to be solved but fundamental constraints." This is a logical overreach. Other calibration approaches — different statistical models, different detection signals, ensemble methods, causal inference frameworks — are not ruled out. The Fisher Information bound applies specifically to the 4PL+γ parameterization; a different model could have different identifiability properties. The paper should claim "ContamCal-style calibration faces structural limitations" rather than "post-hoc calibration is provably infeasible."

### W5 (Moderate): No figures in the entire paper
For a paper about signal characterization and scale-dependent effects, the complete absence of figures is a major presentation weakness. Essential missing visualizations include:
- Forest plot of γ across scales with CIs (would immediately convey the scale-dependency story)
- Scale × dosage heatmap showing contamination effect magnitude
- AUC comparison across signals and scales
- Min-K++ score distributions showing the reversal

Tables alone cannot convey the patterns as effectively. A top-venue submission should have compelling visual storytelling.

### W6 (Moderate): S3 (ConStat/Self-Critique) listed but never computed
Section 3.1 describes four detection signals including S3 (Self-Critique), but the actual experiments only use S1, S2, and S4. The closed-weight experiment (Section 4.6) describes "2-signal mode" as S2+S4, implicitly acknowledging S3 was never implemented. This undermines the "multi-signal" framing. If only 3 signals were computed and only 1 works (S1), the honest description is "we tested 3 signals and found the pipeline is effectively single-signal." Either implement S3 or remove it from the method section.

### W7 (Moderate): Internal tension between N requirements and actual experiments not resolved
The paper establishes N≥50 as necessary for reliable γ recovery but operates with far fewer models throughout. While this is acknowledged (Section 5.4), it creates a fundamental credibility problem: the paper's own empirical γ estimates are unreliable by its own standards. The non-significant γ CIs in Experiments 2–5 could simply reflect insufficient power rather than true null effects. The paper should present power analyses showing what effect sizes could be detected at the actual N used.

### W8 (Minor): Position bias confound not adequately controlled
At 0.5B d=100%, A-option selection reaches 96% (Qwen) and 55% (Llama). This extreme position bias means the MC benchmark results at high dosage are measuring position bias, not benchmark knowledge or contamination effects. The paper excludes 0.5B from IRT pooling but still uses it to argue about "capacity regime impossibility." If the 0.5B results are too confounded to include in IRT, they're also too confounded to support impossibility claims about that regime.

---

## Experiment Coverage Assessment

Comparing against the experimental design (review_context.yaml), all 6 planned experiments are present in the paper:
1. ✅ sft_d100_qc_only → Section 4.1
2. ✅ scale_bridging_7b → Section 4.2
3. ✅ multi_family_validation → Section 4.3
4. ✅ rl_observational_case_study → Section 4.4
5. ✅ observational_72b → Section 4.5
6. ✅ closed_weight_2signal_mode → Section 4.6

However, intermediate scale data (1.5B, 3B) from the scale bridging experiment is missing from Table 2, despite being available per the experimental design. The design context shows 1.5B and 3B gamma estimates that would complete the scale-dependency picture.

---

## Questions for Authors

1. **SFT vs. pretraining**: Have you considered running a pretraining-stage contamination experiment (even at small scale) to validate that your SFT-based findings transfer? Without this, the impossibility claims rest on a potentially non-representative contamination mechanism.

2. **Missing scales in Table 2**: Why are 1.5B and 3B results omitted? These are critical for the "monotonic attenuation" claim and the identification of the capacity-to-sufficiency transition threshold.

3. **Ground truth for observational models**: For Experiment 4, could you inject known contamination into an RL-trained model (post-RL SFT on benchmark items) to establish a ground-truth positive control? This would disambiguate method failure from true negatives.

4. **Power analysis**: At your actual sample sizes (N<30), what is the minimum detectable γ effect size at 80% power? This would contextualize whether the non-significant results in Experiments 2–5 are informative null results or simply underpowered.

5. **Alternative calibration approaches**: The impossibility claims are framed as general, but the evidence is specific to 4PL+γ IRT. Have you considered whether simpler approaches (e.g., stratified scoring, propensity-weighted accuracy) might avoid some of the identified failure modes?

---

## Minor Issues

- Abstract mentions "Cohen's d = −1.2 to −2.7" but the text later uses specific values inconsistently — consolidate.
- Eq. 2: τ_i is defined as "item i's estimated exposure" but its range/distribution is not specified. Is it [0,1]? Continuous RRF scores?
- Table 2 caption says "across model scales" but only shows 2 scales.
- The paper mentions "4 detection signals" throughout but effectively uses 3 (S3 was never computed).
- Section 5.3 cites [White et al., 2024], [Zheng et al., 2023], [Liang et al., 2023] for alternatives but doesn't discuss how these avoid the identified impossibilities — a missed opportunity to strengthen the contribution.

---

## Recommendation

**Reject (3/6).** The paper identifies a genuinely important problem and produces one strong empirical finding (Min-K++ reversal). However, the impossibility claims — the paper's central contribution — are undermined by (1) the SFT-vs-pretraining confound, (2) missing intermediate scale data, (3) inability to distinguish method failure from absence of contamination in observational experiments, and (4) overgeneralization from one framework to all post-hoc calibration. A revised version should: (a) include complete scale data in all tables, (b) add figures, (c) scope impossibility claims to ContamCal-style approaches specifically, (d) implement S3 or remove it, and (e) add power analyses. The Min-K++ reversal finding could anchor a strong shorter paper.
