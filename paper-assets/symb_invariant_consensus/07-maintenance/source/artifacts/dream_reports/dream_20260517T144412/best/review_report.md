---
dream_id: dream_20260517T144412
tier: best
overall_score: 3/6 Weak Reject
timestamp: 2026-05-17T16:02:19.101234+00:00
---

---
dream_id: dream_20260517T144412
tier: best
reviewer: R2 (Novelty, Significance, Related Work, Positioning, Writing Quality)
overall_score: 3/6 Weak Reject
timestamp: 2026-05-17
---

# Review: "The Capability Trap: Why Symbolic Consensus Cannot Beat Majority Voting for LLM Reasoning"

## 1. Summary

This paper presents SICA (Symbolic Invariant Consensus Aggregation), a method that extracts FOL constraints from multiple LLM reasoning traces and uses weighted MAX-SAT to select answers, then systematically evaluates it against majority voting (Self-Consistency). The central finding is negative: across 5 model families, 3 reasoning domains, and 1,300+ problems, SICA provides no significant accuracy gain over SC. The authors diagnose this as a "capability trap" where instruction-scale models produce diverse but non-discriminative constraints (precision ~0.50), while reasoning models eliminate diversity entirely, and propose C0 (candidate disagreement rate) as a zero-cost diagnostic for practitioners.

## 2. Strengths

- **Thorough mechanism analysis.** The constraint ablation experiment (Table 3) is well-designed and convincing: MAX-SAT, count-only, and random-weight aggregation agree on 802/804 problems (McNemar p=0.99). This cleanly demonstrates that the solver's satisfiability reasoning contributes nothing beyond counting when constraints lack discriminative power. The per-problem precision analysis (n=307, mean=0.505, regression slope=0.003 against vote entropy, r^2<0.01) provides fine-grained evidence at a granularity that experiment-level correlations could not achieve.

- **Methodologically honest negative result.** The paper does not try to disguise a failed method as a success. The pivot from method development to systematic failure analysis is credible, and the authors are transparent about effect sizes, p-values, and statistical power throughout. The temperature ablation (Section 5) adds causal evidence by experimentally manipulating diversity from C0=28% to 68% while observing a persistent null gap.

- **Useful qualitative insight.** The case study analysis (Section 6.4) identifying that 78% of extracted constraints formalize shared premises rather than discriminative reasoning steps provides an intuitive explanation for why precision clusters at 0.50. This is a genuinely informative observation about the failure mode of LLM-based FOL extraction.

- **Clean experimental design for the powered experiment.** The main Qwen-14B experiment (n=804) with McNemar's test and appropriate multiple comparison handling is well-executed. Tables are consistently formatted with appropriate precision.

- **Practical overhead analysis.** Demonstrating 49% wall-time overhead for zero accuracy gain, with the solver itself contributing <0.01% of total time, provides actionable guidance: the bottleneck is extraction cost, not solver complexity.

## 3. Weaknesses

- **W1 (Major): The title and central claim far exceed what the evidence supports.** The title asserts that "Symbolic Consensus Cannot Beat Majority Voting" in general, but the paper tests exactly one pipeline: LLM self-extracted FOL constraints aggregated via MAX-SAT. This is a specific instantiation, not the entire class. Critically, the paper's own literature map (which I have access to via project files) identifies multiple neuro-symbolic methods that reportedly achieve gains on the exact same benchmarks tested here: DyLoS (EACL 2026) uses multi-paradigm solver selection on FOLIO and ProofWriter and outperforms Logic-LM; Aristotle (ACL 2025) achieves strong results on ProofWriter and FOLIO via logic-complete decomposition; FoVer (TACL 2025) uses FOL verification with positive results on ProofWriter and FOLIO; LogicAgent (2025) reports +7.05% average gain on logical reasoning benchmarks. The paper does not cite, discuss, or experimentally compare against any of these methods. The claim that symbolic consensus "cannot" beat voting is falsified by published results from other groups on the same benchmarks. What the paper actually shows is that *LLM self-extraction of FOL constraints produces non-discriminative constraints*, which is a narrower and less novel finding.

- **W2 (Major): 8 references is critically insufficient for a venue like EMNLP.** A systematic empirical study that claims to characterize a structural limitation of an entire class of methods requires thorough positioning against existing work. EMNLP papers in this space typically cite 30-60 references. The project's own literature map identifies 25+ relevant papers with "must_cite" or "should_cite" status, yet only 8 appear in the submission. Critical omissions include:
  - Loo et al. 2025 ("Reevaluating Self-Consistency Scaling in Multi-Agent Systems"), which directly contextualizes the QwQ-32B finding that strong models produce near-identical paths and SC gains plateau
  - Snell et al. 2025 (ICLR Oral on test-time compute scaling), which is foundational for understanding the diversity-capability relationship
  - DeepSeek-R1 technical report (Nature 2025), essential for characterizing the reasoning model paradigm and the distillation behavior observed with DeepSeek-R1-Distill-7B
  - DyLoS, FoVer, Aristotle, LogicAgent: methods that achieve positive results on the same benchmarks, whose existence fundamentally challenges the paper's framing
  - Taubenfeld et al. 2025 (confidence-weighted SC, ACL Findings 2025): the paper cites a 2024 paper on debate biases by the same authors, which appears to be a citation error
  - Diversity-Aware Training for Test-Time Scaling (2025), which independently identifies diversity collapse in reasoning models
  - SATBench (EMNLP 2025), LLM Meets Constraint Propagation (IJCAI 2025)
  
  The Related Work section is approximately half a page with four paragraphs. For a paper whose contribution depends on positioning at the intersection of self-consistency, neuro-symbolic reasoning, and test-time compute, this coverage is inadequate. A reviewer encountering this paper at EMNLP would immediately question the depth of the literature survey.

- **W3 (Major): Self-extraction confound is not addressed.** The same model that generates reasoning traces also extracts FOL constraints from those traces. A model that commits a reasoning error will plausibly extract constraints consistent with that error, because both the reasoning and the extraction share the same internal representations and failure modes. The paper cannot distinguish between two very different conclusions: (a) "symbolic consensus over FOL constraints is fundamentally limited" (the paper's claim) vs. (b) "LLM self-extraction of FOL constraints does not produce discriminative representations" (a narrower finding about extraction methodology). FOLIO provides human-authored gold FOL annotations. An oracle experiment using gold FOL as constraints would definitively separate extraction failure from aggregation failure and is conspicuously absent. Similarly, using a stronger or separate model for extraction (e.g., 72B extracting constraints from 14B traces) would test whether the bottleneck is extraction capability rather than a structural limitation of the aggregation paradigm.

- **W4 (Major): The "capability trap" concept restates known limitations without sufficient novelty.** Logic-LM (Pan et al. 2023) and LINC (Olausson et al. 2023) already document that LLM-to-FOL translation is error-prone and that constraint quality is the binding limitation. The observation that weaker models produce more diverse but lower-quality outputs, while stronger models produce less diverse but higher-quality outputs, is a well-characterized property of LLM scaling (it is precisely the diversity-quality tradeoff documented by Loo et al. 2025 and Diversity-Aware TTS 2025). The "capability trap" label is descriptive, but the underlying phenomenon is a predictable consequence of these known properties. The paper would need to demonstrate that this specific characterization enables new research directions or practical decisions that existing understanding does not, which it does not convincingly do beyond the C0 diagnostic.

- **W5 (Moderate): Domain coverage is substantively misleading.** The paper claims "3 reasoning domains" (formal logic, commonsense, science), but SICA operates meaningfully (C0>20%) almost exclusively on formal logic (FOLIO+ProofWriter). On StrategyQA (C0=10%), ARC-Challenge (C0=5%), and GSM8K (C0=10%), the model is sufficiently capable that traces converge, making these conditions uninformative about SICA's potential. The effective experimental coverage is one domain (formal logic) with one powered model (Qwen-14B) and several underpowered conditions (n=60) for other models. This is acknowledged implicitly in the text but not reflected in how the paper frames its contributions.

- **W6 (Moderate): No figures are rendered.** The paper references F2 (hero scatter plot of per-problem constraint precision vs. vote entropy) and F4 (C0 vs. SICA-SC gap) by textual description ("Figure~\ref{fig:f2-description}" and "Figure~\ref{fig:f4-description}"), but neither figure is included in the LaTeX source. The cross-references appear broken. For a paper whose central argument is about the relationship between diversity and constraint quality, the absence of the hero visualization is a significant presentation failure.

- **W7 (Moderate): C0 as a "contribution" is questionable.** C0 is the fraction of problems with multiple candidate answers, which is trivially computed as a byproduct of standard SC. The paper's own regression analysis (slope=-0.02, r^2=0.06, p=0.40) shows C0 has no continuous predictive power for the SICA-SC gap. Its value is purely as a binary filter (C0<5% means degenerate, C0>20% means trapped), but this binary classification is effectively equivalent to asking "is this a reasoning model or an instruction model?" The C0 thresholds (<5%, >20%) are derived from a small number of conditions and their generalization is unknown.

- **W8 (Moderate): The paper attacks a method (SICA) that the authors themselves designed.** Unlike a negative result about an established community method, SICA has no prior publication, no users, and no established research line. The impact of demonstrating that a novel method does not work is inherently lower than demonstrating that an established method has overlooked limitations. The paper partially mitigates this by generalizing via the Logic-LM x K baseline (Section 6.2), but this comparison is limited to one model on one dataset.

- **W9 (Minor): The temperature ablation is labeled "causal" but is confounded.** Temperature simultaneously changes diversity (C0), trace quality (SC drops from 76.7% to 70.0%), and extraction quality (extraction rate drops from 91% to 87%). The persistent null gap at high temperature could reflect worse constraints from noisier traces rather than a structural limitation that holds regardless of diversity level. A true causal test would manipulate diversity while holding trace and extraction quality constant, which is not achievable through temperature alone.

## 4. Questions for Authors

1. How do you reconcile the claim that "symbolic consensus cannot beat majority voting" with published results from DyLoS (EACL 2026), Aristotle (ACL 2025), and FoVer (TACL 2025) achieving positive results on FOLIO and ProofWriter using symbolic reasoning methods?

2. Have you considered using FOLIO's gold FOL annotations as an oracle to separate extraction failure from aggregation failure? If gold constraints were used instead of LLM-extracted constraints, does MAX-SAT aggregation provide any value?

3. Have you tested using a stronger or separate model (e.g., GPT-4, Claude, or Qwen-72B) for constraint extraction while keeping the trace generation model constant? This would test whether the non-discriminative constraint quality is an extraction capability issue or a structural limitation.

4. The Taubenfeld et al. citation (2024) appears to reference a debate biases paper rather than the confidence-weighted SC paper (ACL Findings 2025). Is this intentional?

5. The constraint-sharing analysis (78% shared, 12% discriminative) covers only 8 problems qualitatively (Section 6.4). Has this been verified quantitatively at scale across the 307 multi-candidate problems?

6. Why is Mistral-7B referenced in the framing documents (n=60, delta=0.0) but absent from Table 1?

7. For the 5%-20% C0 gap (between "degenerate" and "trapped"): what is the predicted behavior in this range, and do any of your conditions fall there?

8. Would you consider reporting constraint precision separately for correct vs. incorrect traces? If constraints from correct traces have higher precision than those from incorrect traces, the issue is signal-to-noise ratio rather than fundamental non-discrimination.

## 5. Minor Issues

- The paper uses "5 model families" in the abstract and introduction but Table 1 shows 4 instruction-scale models plus 1 reasoning model (QwQ-32B). The QwQ-32B row reports accuracy as "--" with delta "approx 0", which is incomplete.
- Section 5 (Temperature Ablation) uses n=60, the same underpowered sample size as most non-central experiments. Running this at n=804 on the Qwen-14B FOLIO+PW dataset would substantially strengthen the causal claim.
- The paper mixes FOLIO+ProofWriter as a combined domain (n=804) and as separate domains in different sections, making it ambiguous whether this counts as 1 or 2 domains.
- "Rogers et al. 2020" (a BERT survey in TACL) is cited as precedent for "negative results in NLP" but is not itself a negative result paper. More appropriate precedents exist.
- Several paragraphs begin with "F2:" or "F4:" as inline figure descriptions, which reads as placeholder text rather than final prose.

## 6. Overall Assessment

The paper presents a well-executed empirical analysis of a specific pipeline (LLM self-extracted FOL constraints + MAX-SAT aggregation) and convincingly demonstrates that this pipeline does not outperform majority voting. The constraint ablation (Table 3) and per-problem precision analysis (Table 2) are the paper's strongest contributions and are methodologically sound.

However, the paper's framing substantially overreaches its evidence. The title implies a general impossibility result about symbolic consensus, but only one specific pipeline is tested, and multiple published methods achieve positive results on the same benchmarks using different neuro-symbolic approaches. The self-extraction confound is unaddressed: the paper cannot distinguish between "symbolic aggregation is fundamentally limited" and "LLM self-extraction produces non-discriminative constraints," which are very different conclusions with very different implications for future work. The "capability trap" concept, while clearly articulated, largely restates the known diversity-quality tradeoff in LLM scaling. The C0 diagnostic has limited incremental value beyond binary model-type classification.

The scholarship is critically thin at 8 references, missing numerous directly relevant works including methods that achieve gains on the tested benchmarks (DyLoS, Aristotle, FoVer), papers that contextualize the core findings (Loo et al. 2025, DeepSeek-R1 report), and the correct citation for Taubenfeld et al. The missing hero figures (F2, F4) further weaken the presentation.

The mechanism analysis deserves publication, but it needs to be wrapped in honest, appropriately scoped claims ("LLM self-extracted FOL constraints lack discriminative power" rather than "symbolic consensus cannot beat voting"), substantially expanded scholarship, and a clear discussion of how the findings relate to methods that do achieve gains on the same benchmarks. In its current form, the gap between claims and evidence, combined with the thin related work, places this below the acceptance bar for a top venue.

## 7. Score and Confidence

**Score: 3/6 (Weak Reject)**

Rationale: The mechanism analysis is solid empirical work, but the over-generalized claims, critically thin references (8 citations), unaddressed self-extraction confound, absence of comparison with methods that demonstrably work on the same benchmarks, and missing figures collectively place this below the acceptance threshold. The contribution is a well-executed analysis of a narrow failure mode, presented as a broad impossibility result. With narrowed claims, expanded references (30+), a gold-FOL oracle experiment, and rendered figures, this could reach borderline accept.

**Confidence: 4/5**

I am confident in this assessment. The weaknesses regarding over-generalized claims, missing related work, and the self-extraction confound are clear and well-supported by the project's own literature map, which identifies the missing citations. The one area of uncertainty is whether the EMNLP program committee would weigh the practical value of the systematic negative result more heavily than I do, potentially pushing this to borderline accept territory.
