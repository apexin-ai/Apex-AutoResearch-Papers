---
dream_id: dream_20260516T155754
tier: median
overall_score: 4 - Borderline Reject
timestamp: 2026-05-16T16:29:55.184961+00:00
---

# Review Report: "When Does Symbolic Consensus Help?"

## Meta-Information
- **Review mode**: simple (single reviewer, full coverage)
- **Venue standard**: Top ML venue (e.g., EMNLP Main), ~25% acceptance rate, 6-point scale

---

## Overall Assessment

**Score: 4 / 6 (Borderline Reject)**

The paper asks a well-motivated question—"when does symbolic consensus help?"—and provides a systematic, honest answer. The framing pivot from "our method is better" to "here is the operating regime" is commendable and more scientifically rigorous than overclaiming. However, the paper suffers from three compounding weaknesses: (1) the core technical component (MAX-SAT) does not significantly outperform simple constraint counting (p=0.33), undermining the methodological contribution; (2) the only statistically significant accuracy improvement is on a single domain–model pair (FOLIO, Qwen-14B), while the combined 804-question result is not significant (p=0.089); and (3) the operating regime analysis—the paper's claimed main contribution—rests on only 14 data points. The paper is well-written and transparent, but the results do not clear the bar for a top venue main track. It would be a reasonable EMNLP Findings paper with revisions.

---

## Strengths

### S1: Honest, well-framed research question
The paper's central question "when does symbolic consensus help?" is more valuable than a blanket claim of improvement. The authors transparently report null results (ProofWriter, GSM8K, reasoning models) and negative results (Mistral), which strengthens credibility. The pivot to operating regime characterization is scientifically appropriate given the mixed results.

### S2: Systematic experimental coverage
Seven model configurations across 3 families (Qwen, LLaMA, Mistral) and 2 reasoning architectures (QwQ, DeepSeek-R1) is thorough. The inclusion of negative controls (reasoning models with C0 < 5%, GSM8K as a "too easy" task) demonstrates good experimental design. All 14 planned experiments from the design document appear to be represented in the paper.

### S3: Actionable practical contribution (C0 diagnostic)
The C0 metric as a zero-cost deployment diagnostic is genuinely useful for practitioners. The recommendation framework (C0 > 20% → use SICA; C0 < 5% → skip) is simple and actionable. The observation that C0 is task-relative rather than model-intrinsic (same 14B model: C0=0.48 on FOLIO vs. 0.10 on GSM8K) is an interesting finding.

### S4: Mechanistic analysis of tiebreaking
The K sensitivity analysis (Table 4) demonstrating that SICA's gap systematically covaries with tie rate provides clean mechanistic evidence for the "principled tiebreaker" narrative. The dual-axis relationship between K, tie rate, and SICA–SC gap is convincing.

### S5: Transparent limitation disclosure
The limitations section is unusually thorough for a submitted paper—acknowledging the quantization confound, the non-significant MAX-SAT vs. counting result, and the small sample for C0 validation.

---

## Weaknesses

### W1: MAX-SAT does not significantly outperform counting — the core technical contribution is hollow (Major)
Table 6 is the most damaging result in the paper: MAX-SAT (73.7%) vs. count-only (73.0%), p=0.33. The paper introduces a non-trivial pipeline involving FOL extraction, constraint weighting, and Z3 solving, but simple counting of constraint occurrences achieves statistically indistinguishable accuracy. The authors reframe MAX-SAT as providing "a formal framework for interpretability," but this is a post-hoc justification. If counting suffices for accuracy, the paper's technical contribution reduces to: (a) the idea of extracting constraints from traces (which could be a paragraph, not a method), and (b) the operating regime analysis (which has its own issues, see W3). The 4.3pp tie-only gap (68.1% vs. 63.8%) is suggestive but on only 47 ties and not tested for significance between these two methods.

### W2: Statistical significance achieved only on one domain–model pair (Major)
The only significant overall accuracy result is FOLIO with Qwen-14B: +3.9pp, p=0.038. Every other model configuration fails to reach significance (most on 60 questions with p > 0.19). The combined 804-question result is p=0.089—marginal and driven by ProofWriter's 75% weight diluting the FOLIO signal. ProofWriter shows essentially null effect (+0.3pp, p=0.41) across all models due to its restricted 3-class answer space. This means SICA's accuracy advantage is demonstrated convincingly only on FOLIO, a single formal logic NLI dataset. For a venue paper claiming to characterize when a method works, having it work clearly in only one domain is insufficient.

### W3: Operating regime analysis on 14 data points is underpowered (Major)
The paper claims C0 achieves "86% binary classification accuracy at a 20% threshold" for predicting SICA effectiveness—but this is 12/14 correct classifications. With 14 data points, the confidence interval for 86% accuracy is extremely wide (~57%–98% by Wilson interval). Furthermore, several of these 14 points are not independent: they share the same model (Qwen-14B appears in FOLIO, PW, and GSM8K configurations) or the same dataset. The Pearson r=0.72 on 14 points has p ≈ 0.004, which is respectable, but the binary threshold claim requires far more data points to be actionable. This is the paper's headline contribution and it rests on a very thin empirical basis.

### W4: Missing and incomplete references (Minor)
The very first citation in the paper is "[?]" (page 1, referencing Self-Consistency), indicating a broken BibTeX reference. The Related Work section mentions "Wang et al. (2023)" and "Chen et al. (2023)" in text but references appear incomplete. For a submission, all citations must be properly formatted. This suggests the paper was rushed to completion.

### W5: No comparison with other structured aggregation methods (Moderate)
The paper compares SICA only against SC variants (random, alphabetical, first-seen tiebreaking). There is no comparison with other methods that leverage trace content beyond voting, such as: Universal Self-Consistency (mentioned in Related Work but not compared against), debate-based aggregation, verifier-based reranking, or weighted voting by token probability. The absence of these baselines makes it unclear whether SICA's tiebreaking advantage comes from the FOL/MAX-SAT machinery specifically or from any method that looks inside traces.

### W6: Narrow domain where method helps creates a circular argument risk (Moderate)
SICA works on FOLIO, a dataset of first-order logic NLI problems—precisely the domain where FOL constraint extraction is naturally well-suited. The constraint extraction prompt asks the LLM to produce FOL; FOLIO problems are already designed around FOL reasoning. This raises the question: is SICA's advantage on FOLIO an artifact of the constraint representation matching the task structure, rather than a general property? The paper partially acknowledges this ("domains where formal logical structure aligns with the method's constraint extraction capability") but doesn't adequately address whether alternative constraint representations might work on other domains.

### W7: Table 1 mixes evaluation scales without adequate flagging (Minor)
Qwen2.5-14B is evaluated on 204 FOLIO questions (marked with †), while all other instruction models are on D012 (60 questions). QwQ-32B has no accuracy numbers (dashes). This heterogeneity in evaluation scale makes cross-row comparison misleading. A reader glancing at Table 1 might compare the 14B's +3.9pp on 204 questions with LLaMA's +1.7pp on 60 questions, but these are not comparable.

---

## Detailed Analysis by Section

### Method (Section 2)
The SICA pipeline is clearly described. The formalization is clean: Equation 1 for weighted partial MAX-SAT selection and Equation 2 for C0 are both simple and appropriate. One concern: the constraint weighting scheme (cross-trace agreement) is very simple—it's essentially a frequency count. The paper doesn't explore alternative weighting schemes (e.g., by trace confidence, by constraint specificity). Section 2.4 explicitly frames SICA as a tiebreaker, which is honest but also limits the claimed scope of contribution.

### Main Results (Section 3.2)
The domain decomposition analysis is well-done—the explanation of why ProofWriter shows null results (restricted 3-class answer space → few ties) is mechanistically sound. The acknowledgment that combined p=0.089 is marginal is appropriate.

### Operating Regime (Section 3.4)
Table 3 is the paper's most informative table. The Mistral anomaly is well-diagnosed (low extraction quality). The "Restricted" label for PW is appropriate. However, the 14-point scatter with 2 acknowledged anomalies and a claimed 86% binary accuracy is unconvincing for drawing strong conclusions.

### Constraint Ablation (Section 4)
This section is both the most honest and most damaging. The MAX-SAT vs. count-only comparison (p=0.33) essentially says the formal SAT machinery adds negligible accuracy over counting. The reframe to "interpretability framework" is reasonable but significantly weakens the paper's technical contribution.

---

## Experiment Coverage Assessment

Compared against the full experimental design (14 imagined experiments), the paper covers all planned experiments:
- exp-001 through exp-014: all represented in Tables 1–6 and corresponding sections
- Key figures described in the design (C0 vs gap scatter, K sensitivity, overhead breakdown) are discussed but the PDF does not appear to contain actual figures—only tables. The figure descriptions in the design document suggest figures F2, F3, F4 were planned but may not be included in this version.

**Missing figures**: The paper is entirely tables with no figures. The "hero figure" (F2: C0 vs gap scatter plot) described in the experimental design would significantly strengthen the operating regime argument. Its absence is notable.

---

## Minor Issues
1. Broken citation "[?]" on page 1
2. No figures in the paper—tables only
3. The paper has no appendix despite the design mentioning appendix tables (T_gsm8k, T_ablation)
4. The abstract says "14 model–task configurations" but Table 3 shows only 9 rows (some configurations appear merged)
5. No code/data availability statement

---

## Questions for Authors

1. Have you compared SICA against a verifier-based reranking baseline (e.g., using a separate LLM call to evaluate each tied candidate) with the same computational budget as the constraint extraction step?
2. Given that count-only achieves statistically indistinguishable accuracy from MAX-SAT, what specific interpretability insights does MAX-SAT provide that counting cannot? Can you show a concrete example?
3. The 14 data points for C0 diagnostic include non-independent observations (same model on different tasks, same task on different models). What is the effective degrees of freedom?
4. Would SICA benefit from domain-specific constraint templates rather than generic FOL extraction?

---

## Verdict

The paper has a sound experimental methodology and commendable honesty about its results. The research question is important and the operating regime framing is the right approach. However, the execution falls short of a main track publication: the method's core component (MAX-SAT) doesn't beat counting, the accuracy improvement is significant only on one dataset, and the regime analysis is severely underpowered. The contribution is real but thin—it amounts to: "extract constraints from traces and count them for tiebreaking; this helps on FOLIO with instruction models." This is a useful empirical finding but does not provide sufficient novelty or impact for a top venue main track.

**Recommendation**: Reject for main track; encourage resubmission to Findings with (a) additional domains where FOL constraints are naturally applicable, (b) larger-scale C0 validation, and (c) comparison against non-symbolic trace-content-aware baselines.

**Overall Score: 4 / 6 (Borderline Reject)**
**Confidence: 4 / 5 (Fairly confident)**
