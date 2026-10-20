---
dream_id: dream_20260516T124139
tier: worst
overall_score: 3 — Reject
timestamp: 2026-05-16T13:20:03.929154+00:00
---


# Review Report: "Why Doesn't Symbolic Consensus Improve LLM Reasoning? A Diagnostic Study"

## Overall Assessment

**Score: 3 / 6 (Reject)**

An honest negative-result study with competent experimental execution, but the contributions do not clear the bar for a top ML venue. The diagnostic insights—C0 as a diversity metric, constraint quality as the bottleneck, reasoning model self-consistency—are either unsurprising given prior knowledge or too shallowly developed to constitute a lasting contribution. The paper would benefit from deeper analysis, broader benchmarks, and stronger comparative baselines.

---

## Summary

The paper evaluates SICA (Symbolic Invariant Consensus Aggregation), a method that extracts first-order logic constraints from LLM reasoning traces and uses weighted partial MAX-SAT to aggregate answers, against standard Self-Consistency (SC) majority voting. Across 7 models from 3 families, 2 reasoning architectures, and logic/arithmetic benchmarks, SICA shows no statistically significant improvement (+0.3pp on 804 instances, p=0.42). The paper identifies three findings: (1) the multi-candidate rate C0 distinguishes instruction models (C0>20%) from reasoning models (C0<5%); (2) LLM-extracted constraints are too shallow for MAX-SAT to exploit; (3) reasoning models exhibit structural self-consistency that nullifies any diversity-based consensus method.

---

## Strengths

**S1. Thorough negative-result framing.** The paper does not simply report failure but provides a structured diagnostic investigation. The pivot from "SICA works" to "why doesn't it work" is well-executed, and the paper is admirably transparent about its earlier small-sample pilot results being artifacts (§5.1, §6 "small-sample trap"). This intellectual honesty is commendable.

**S2. Clean tiebreak and K-sensitivity analysis (§5.2–5.3).** The demonstration that SICA's gains track tiebreak frequency rather than reasoning quality is the paper's strongest analytical contribution. Table 3 shows a clean pattern: as K increases, ties decrease, and the gap vanishes. This is a well-designed experiment with a crisp conclusion.

**S3. Constraint ablation is well-designed (§5.4).** Showing that SICA-MaxSAT ≈ SICA-CountOnly (Δ=0.1pp, p=0.48, 89% tiebreak agreement) is a clean result that isolates the failure to the extraction stage rather than the solver. This effectively decomposes the pipeline failure.

**S4. Cross-family C0 pattern.** The observation that instruction-tuned models universally show C0>20% while reasoning models show C0<5%, validated across Qwen/Mistral/LLaMA families and the controlled LLaMA-8B comparison (instruction C0=30% vs reasoning-distilled C0=5%, Table 8), is a neat empirical regularity.

**S5. Practical cautionary value.** The "small-sample trap" message—a +6.7pp gap on n=60 collapsing to +0.3pp on n=804—is a useful reminder for the community evaluating tiebreak-sensitive methods.

---

## Weaknesses

**W1. Limited novelty of core findings.** The three claimed contributions are individually thin:
- *C0 as diversity indicator*: C0 is simply "fraction of problems with >1 unique answer in K samples." The paper itself acknowledges (§5.6) that its binary classification ability is "trivial"—it distinguishes reasoning from instruction models, "a categorization available from the model card." This honesty undermines the contribution claim.
- *Constraint extraction is shallow*: This diagnoses why one specific approach fails. Without testing alternative extraction strategies (e.g., using a stronger model, structured prompting, or verified extraction), the finding is descriptive rather than prescriptive.
- *Reasoning model self-consistency*: That reasoning-trained models (QwQ, DeepSeek-R1) produce near-deterministic outputs under temperature sampling is already empirically well-known in the community. Documenting it with C0 is confirmatory, not novel.

**W2. Most cross-model evidence is on only 60 questions.** The expanded 804-instance evaluation (the paper's headline result) is performed only on Qwen2.5-14B-Instruct. All other 6 models are evaluated on the 60-question D012 pilot—the very sample size the paper warns against in §6 ("We recommend minimum sample sizes of 200+"). This is a significant internal inconsistency. Cross-model claims (Table 5) rest on the same small-sample regime the paper critiques.

**W3. Narrow benchmark scope undermines generality claims.** The abstract says "4 benchmarks" but lists only 3 (FOLIO, ProofWriter, GSM8K). The main evaluation uses two logic-reasoning benchmarks (FOLIO + ProofWriter) that share structural similarities. GSM8K is a 30-question pilot explicitly flagged as non-definitive. No commonsense reasoning (e.g., StrategyQA, ARC), no scientific reasoning, no code generation. Claims about SICA failing "across domains" are overstated.

**W4. No comparison with other aggregation methods.** The paper positions itself as informing "future consensus methods" but only compares SICA against vanilla SC. Where is Universal Self-Consistency (Chen et al. 2023, which the paper cites)? Where are weighted voting schemes, verifier-based approaches (e.g., ORM/PRM), or debate-style aggregation? A diagnostic study of *why symbolic consensus fails* should situate the failure against methods that *do* work, to isolate what's missing.

**W5. Constraint quality analysis is too small-scale.** The 45%/35%/20% taxonomy (Table 7) is derived from only 8 representative problems. This is anecdotal, not systematic. The 30%/15%/55% exclusion outcome breakdown is more useful (computed over n=804) but the constraint categorization—the more interesting finding—is underpowered. Per-model breakdowns (Qwen vs Mistral's 12% parse error rate) are mentioned in text but not systematically tabulated.

**W6. Missing obvious ablation: extraction model ≠ generation model.** The paper uses the same model for trace generation and constraint extraction. A natural question is whether a stronger or specialized extractor (e.g., using GPT-4 or a model fine-tuned for logical analysis) would improve constraint quality. This ablation is absent, leaving the reader unsure whether the failure is fundamental to the approach or specific to self-extraction.

**W7. SICA provenance is unclear.** The paper says "SICA was proposed to address this limitation" without citation. If SICA is the authors' own prior/concurrent work, this self-critique framing matters. If it's another group's method, a citation is required. The reader cannot assess the relationship.

**W8. Redundancy in presentation.** The core finding (SICA ≈ SC) is restated with slight variations across §5.1–5.9. While each section adds a facet, the paper would benefit from tighter writing that eliminates repetitive conclusions. Several sections could be consolidated.

---

## Detailed Comments

1. **Abstract**: Claims "4 benchmarks" but parenthetically lists three: FOLIO, ProofWriter, GSM8K. Either a benchmark is missing or the count is wrong.

2. **§5.1**: The D012 pilot is referenced repeatedly without explanation. What does "D012" stand for? This should be defined at first use.

3. **Table 5**: The QwQ-32B and DeepSeek-R1-8B rows show p-value as "—" rather than a computed value. Even when the gap is 0.0, a p-value should be reported for completeness (it would be ~0.50).

4. **§5.6**: The Pearson r=0.31 is computed across only 12 data points mixing instruction and reasoning models. With n=12, this correlation analysis has essentially no statistical power. The conclusion that C0 fails as a continuous predictor is correct but the statistical framing overstates what 12 points can tell us.

5. **§5.8**: The claim that reasoning model self-consistency "persists across temperature settings (T=0.7, 0.9, 1.0)" is stated but no data is shown. A table or figure showing C0 vs temperature for QwQ-32B would strengthen this claim.

6. **Table 6**: Qwen-14B appears twice (D012 and expanded) with very different C0 values (0.53 vs 0.41). This discrepancy is not explained. Is it due to different question sets? If so, this suggests C0 is unstable across problem distributions, which weakens its utility as a diagnostic.

7. **Related work**: The survey is thin—only 8 references total. Missing: work on process reward models, outcome reward models, debate/recursive reward modeling, and other structured aggregation methods that are highly relevant comparators.

8. **Limitations section**: Appropriately identifies key gaps (narrow domains, small GSM8K pilot, 8-problem qualitative analysis, model size ceiling). However, some of these are severe enough to undermine the paper's central claims rather than being minor caveats.

---

## Experiment Coverage Assessment

Cross-referencing against the full experiment design: all 14 planned experiments are reflected in the paper (exp-001 through exp-014). Tables 1–9 cover the main results, tiebreak analysis, K-sensitivity, constraint ablation, cross-model comparison, C0 diagnostic, constraint quality, reasoning vs instruction comparison, and overhead analysis. Coverage is comprehensive in breadth. The gap is in depth—most cross-model experiments use only 60 questions.

---

## Questions for Authors

1. Have you tried using a different (stronger) model for constraint extraction? This seems like the most obvious way to test whether the failure is in the extraction approach vs. the aggregation framework.
2. Why was the 804-instance evaluation not run on at least one other model (e.g., Mistral-7B, where SICA shows negative gap)?
3. The C0 values for Qwen-14B differ substantially between D012 (0.53) and expanded (0.41). What drives this? Does C0 depend heavily on problem difficulty distribution?
4. Could you compare SICA against Universal Self-Consistency or a learned verifier to contextualize the symbolic approach's failure?

---

## Verdict

The paper is a competent and honest negative-result study. The experimental execution is solid, the analysis is well-structured, and the "small-sample trap" lesson has practical value. However, for a top ML venue, the contributions are insufficient: C0 is a trivially computable metric with limited predictive utility beyond what a model card tells you; the constraint quality analysis is too small-scale to be definitive; the cross-model evidence mostly relies on the same small-sample regime the paper warns against; and the paper lacks comparisons with other aggregation methods that would give the negative result broader significance. The work reads more as a thorough project postmortem than a venue-ready contribution to the community's understanding of reasoning aggregation.

**Recommendation**: Reject in current form. With (a) expanded evaluation of other models at 200+ instances, (b) comparison against Universal SC and verifier-based methods, (c) an ablation using a stronger extraction model, and (d) a larger-scale systematic constraint quality annotation, this could become a solid Findings paper.
