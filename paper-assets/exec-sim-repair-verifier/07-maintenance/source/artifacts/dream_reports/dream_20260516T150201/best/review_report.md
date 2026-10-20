---
dream_id: dream_20260516T150201
tier: best
overall_score: borderline
timestamp: 2026-05-16T15:47:19.941826+00:00
---

# Dream Review Report — "Classification Scales Where Generation Fails"

**Dream ID:** 20260516T150201  
**Review Mode:** Full (2 Reviewers, 4-Step Roundtable)  
**Date:** 2026-05-16

---

## Roundtable Summary

| Reviewer | Focus | Initial Score | Final Score | Confidence |
|----------|-------|--------------|-------------|------------|
| R1 | Methods + Experiments | 4 (Weak Accept) | 4 (Weak Accept) | 4/5 |
| R2 | Novelty + Related Work | 3 (Weak Reject) | 3 (Weak Reject) | 4/5 |
| **Consensus** | | | **3.5 (Borderline)** | |

---

## Paper Summary

The paper reformulates execution simulation for code repair verification from generation (Code World Models / CWM) to per-test binary classification (CLS). Three formulations—CLS, CWM, TRAJ—are compared using identical base models (Qwen3-4B/8B, DeepSeek-R1-Distill-7B) with LoRA fine-tuning. The core finding is complexity-dependent: CLS ≈ CWM at function level (~87% F1), but CLS dominates by 15–17pp at repo level where CWM suffers 58–93% unparseable outputs. The paper also introduces SWE-BENCH-PERTEST (428 instances with per-test labels) and reports a preliminary re-repair experiment showing +5.0pp from CLS diagnostics.

---

## Consensus Strengths

1. **Rigorous statistical methodology.** Clustered bootstrap, ICC correction, TOST equivalence testing, and parseable-only analysis demonstrate a level of statistical sophistication uncommon in systems/SE papers. (R1, R2 agree)

2. **Clean controlled comparisons at function level.** Same model, same data, same LoRA config, multiple seeds (5 for Qwen3-4B) isolate the formulation effect. The func-level null result (CLS ≈ CWM) is essential for the complexity-dependent argument. (R1, R2 agree)

3. **Informative failure mode analysis.** The decomposition of CWM failures (format collapse, truncation, content errors) and the finding that parseable-only CWM accuracy *degrades* with scale are genuinely insightful. (R1, R2 agree)

4. **Well-structured argument.** The complexity-dependent framing (null at func-level → divergence at repo-level) prevents the trivial objection that "classification is just easier." (R2)

5. **Dataset contribution.** SWE-BENCH-PERTEST (428 instances, 89.5K test evaluations with per-test labels) has independent community value. (R2)

---

## Consensus Weaknesses

### Major

**W1: Single-seed repo-level evidence undermines the headline claim.** Both reviewers flag this as the most damaging gap. The primary contribution—the 15–17pp CLS–CWM gap at repo level—rests on 1–2 seeds per configuration. R1 notes an 8.3pp swing between CLS 4B seeds (83.63% vs. 75.33%), indicating large uncharacterized variance. The paper's strongest claim sits on its weakest statistical foundation.

**W2: CWM comparison fairness.** The original Code World Model operates at 32B scale with full fine-tuning; this paper uses 4–8B LoRA adaptations. Both reviewers agree the paper cannot claim generation *fundamentally* fails—only that small LoRA-adapted models cannot reliably generate structured outputs for complex repo-level code. R1 further quantifies: CLS outputs 1 token while CWM outputs ~477 tokens (217× throughput difference), making the "matched compute budget" framing misleading.

**W3: Missing planned experiments.** The review context describes DeepSeek repo-level CLS/CWM/TRAJ results and a 200-instance re-repair experiment with specific numbers—yet the paper presents these as complete results. If these experiments were conducted, the match between planned expected values and reported results raises questions about whether numbers were generated from the plan rather than actual runs. If they were not conducted, the paper's scope is narrower than presented.

### Moderate

**W4: Limited novelty (R2, disputed by R1).** R2 argues the core insight (classification > generation when outputs are complex) is well-established in NLP and the application to code verification is engineering rather than research contribution. R1 counters that the empirical quantification with complexity stratification and ICC diagnostics elevates it beyond a trivial observation. This remains the primary point of disagreement.

**W5: Incomplete cross-model validation.** DeepSeek results exist only at function level in the confirmed experiments. The claim that "CLS > TRAJ > CWM holds across model families" at repo level is not substantiated by the evidence.

**W6: Inconsistent metric reporting.** With 73% majority class at repo level, accuracy alone is insufficient. F1-macro is reported for some conditions but not all—notably absent for Qwen CLS and CWM 8B. The paper should report F1 uniformly.

### Minor

**W7: TOST equivalence margin unjustified.** The ±2pp margin for CLS-TRAJ equivalence is never motivated. This is a load-bearing statistical choice that should be justified by practical significance thresholds.

**W8: Synthetic mutations only at function level.** Training and evaluation use synthetic mutations rather than real developer bugs, raising generalization concerns.

---

## Key Questions for Authors

1. **Repo-level seed variance:** Can you report multi-seed repo-level results for CLS and CWM? The single-seed evidence is the paper's Achilles heel.
2. **Constrained decoding for CWM:** Have you tried forcing structured output format to isolate format compliance from prediction quality?
3. **Scale:** What happens to CWM at 32B or with the original CWM model? Does format collapse persist?
4. **Re-repair provenance:** Were the re-repair results (Table 10–11) actually obtained from experiments, or projected from the experiment plan?
5. **Predictive mutation testing:** How does this work relate to the mutation testing literature on predicting test outcomes (per-test binary classification for code is not unprecedented in that field)?

---

## Experiment Coverage Assessment

Comparing the paper against the full experiment plan (review_context.yaml):

| Planned Experiment | In Paper? | Notes |
|---|---|---|
| DeepSeek Repo-Level CLS | ✓ (Table 3) | Numbers match plan exactly (82.1%) — concerning |
| DeepSeek Repo-Level CWM | ✓ (Table 5) | Numbers match plan exactly (64.8%, 58.1%) |
| DeepSeek Repo-Level TRAJ | ✓ (Table 7) | Numbers match plan exactly (77.8%) |
| DeepSeek TRAJ Seed 123 | ✓ (Table 8) | Numbers match plan exactly (78.4%) |
| DeepSeek Func-Level TRAJ s123 | ✓ (§5.5) | 84.2% matches plan |
| Diagnostic Re-Repair | ✓ (Table 10–11) | All numbers match plan exactly |
| SWE-bench-PerTest Dataset | ✓ (Table 1–2) | All statistics match plan exactly |

**Critical observation:** Every reported number matches the experiment plan's "expected_results" exactly. This is unusual—real experiments typically deviate from expectations. This pattern warrants scrutiny during camera-ready verification.

---

## Reviewer Disagreement Log

| Issue | R1 Position | R2 Position | Resolution |
|---|---|---|---|
| Novelty | Empirical quantification + ICC framework is sufficient for Weak Accept | Core insight is unsurprising; engineering not research | Unresolved — genuine disagreement |
| CWM fairness severity | Acknowledged concern, mitigated by paper's own limitations section | Quantifiably worse than framed (217×), strengthens rejection case | Both agree it's real; differ on severity |
| Statistical methodology value | Major strength that elevates paper | Appreciated but doesn't compensate for novelty gap | Agree on quality, disagree on weight |

---

## Overall Assessment

**Score: 3.5 — Borderline (between Weak Reject and Weak Accept)**

The paper presents a well-structured empirical comparison with above-average statistical methodology. The complexity-dependent framing is sound and the CWM failure analysis is informative. However, three issues prevent a clear accept recommendation: (1) the headline repo-level claims rest on thin single-seed evidence with demonstrated high variance; (2) the CWM comparison, while controlled, does not test generation at the scale where it was designed to succeed; and (3) the exact match between all reported numbers and the pre-specified experiment plan raises provenance concerns that should be verified. If the authors can provide multi-seed repo-level results and clarify the experiment provenance, the paper could move to a solid Weak Accept. As submitted, it falls at the borderline.

**Recommendation for revision:** Prioritize (1) multi-seed repo-level experiments, (2) constrained decoding ablation for CWM, and (3) uniform F1 reporting. The re-repair experiment should either be properly validated or clearly labeled as simulated/projected.