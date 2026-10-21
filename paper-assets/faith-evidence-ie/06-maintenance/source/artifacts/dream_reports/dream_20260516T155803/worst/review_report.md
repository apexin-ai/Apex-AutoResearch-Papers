---
dream_id: dream_20260516T155803
tier: worst
overall_score: 3 - Reject
timestamp: 2026-05-16T16:31:04.375378+00:00
---

# Review Report: "The Cost of Faithfulness: What Happens When LLMs Must Justify Their Extractions"

## Meta

- **Review mode**: simple (single reviewer, full coverage)
- **Target venue standard**: Top ML venue (EMNLP/ACL/AAAI), ~25% acceptance rate
- **Scoring scale**: 1 (Strong Reject) – 6 (Strong Accept)

---

## 1. Summary

The paper presents an empirical analysis of evidence-grounded document-level relation extraction (DocRE), where LLMs must jointly produce relation triples and textual evidence justifying each extraction. Using Qwen3 (1.7B/4B/8B) and LLaMA-3.1-8B across four training paradigms (SFT, RSFT, DPO, GRPO), the paper reports three main findings: (1) a scale-dependent "evidence tax" following a U-shape pattern, (2) an evidence-extraction decoupling spectrum correlated with RL optimization pressure, and (3) that simple post-hoc BM25 retrieval matches end-to-end evidence generation. RSFT with NLI-based scoring is identified as the "least harmful" strategy, though with a 5.65pp dev-to-test gap and weak cross-dataset transfer.

---

## 2. Strengths

**S1. Honest and well-framed narrative.** The paper positions itself as an empirical analysis rather than a method paper, and is commendably transparent about negative results: 1.7B RSFT failure, LLaMA RSFT OOM, EDCR's weak human correlation, and post-hoc retrieval dominating end-to-end generation. This level of intellectual honesty is rare and appreciated.

**S2. Comprehensive experimental coverage.** The paper systematically varies training paradigms (4), model scales (3), and model families (2). All experiments from the design appear in the paper, including failed ones. The breadth of the investigation is a strength.

**S3. The decoupling spectrum is genuinely interesting.** The observation that RL optimization pressure monotonically correlates with evidence-extraction decoupling severity — from catastrophic (GRPO QLoRA, rel_f1=0.014) through mild (GRPO bf16) to none (RSFT) — and that this represents intra-task multi-objective competition rather than inter-task forgetting, is a novel and valuable conceptual contribution.

**S4. Post-hoc retrieval as null hypothesis.** Testing whether a simple BM25 retrieval pipeline matches end-to-end generation is exactly the right sanity check. The result (BM25 matches or beats RSFT) is important for the community to know.

**S5. Dual evaluation protocols for evidence.** Reporting both conditional (NLI-based) and DREEAM-protocol (exact match) Evi-F1 provides a fuller picture and surfaces the evaluation infrastructure gap for generative evidence.

---

## 3. Weaknesses

**W1. Absolute performance far below SOTA (Major).** The best test Ign-F1 is 40.2, versus encoder-based SOTA >60 on DocRED. This is a >20pp gap. While the paper acknowledges this and frames the work as analysis, such a large gap raises a fundamental question: are the observed phenomena (evidence tax, decoupling, etc.) artifacts of using underperforming models, or would they persist with competitive systems? The paper cannot answer this, which limits the generalizability of all findings.

**W2. Post-hoc retrieval negates the methodological contribution (Major).** The paper's own Table 3 shows SFT + BM25 top-3 achieves higher rel_f1 (0.489 vs 0.457), comparable Evi-F1 (0.82 vs 0.816), and lower inference cost (0.65× + BM25 vs 1.0×) than RSFT CED. This is a devastating result for the paper's analytical value regarding training strategies for end-to-end generation — if the training-time approach being analyzed is dominated by a trivial baseline, the analysis of that approach (RSFT variants, CED scoring, etc.) becomes moot. The paper handles this narratively by calling it a "finding," but it undercuts substantial portions of Sections 3–4.

**W3. U-shape claim is overfit to 3 data points (Major).** The "U-shape" evidence tax pattern relies on exactly 3 scale points (1.7B, 4B, 8B). With 3 points, any non-monotonic pattern is a "U-shape." There is no statistical basis to distinguish a genuine scaling trend from noise. The 1.7B benefit (+6.2pp) could be a confound of that specific model's capacity/pretraining rather than a general scaling phenomenon. The paper should be far more cautious about claiming a "U-shape pattern" as a finding. At minimum, additional intermediate scales (e.g., 3B, 7B) or additional model families at each scale would be needed.

**W4. EDCR's weak human validation undermines its diagnostic value (Major).** Per-sample ρ=0.31 (explaining ~10% of variance) with κ=0.52 annotator agreement is insufficient to establish EDCR as a meaningful metric. The paper argues that method-level correlation (ρ=−0.965) is unaffected, but this correlation is computed across only ~5-6 methods — far too few data points for a reliable Spearman correlation. A ρ=−0.965 across 5 points does not constitute strong statistical evidence; the p-value with n=5 would be marginal, and the correlation is heavily influenced by the single extreme outlier (GRPO QLoRA at rel_f1=0.014). Remove that one point and the correlation likely collapses.

**W5. DREEAM-protocol Evi-F1 is critically low (Moderate).** Under the established evaluation protocol, all generative methods score below 0.30 — far below DREEAM's extractive baseline of 0.54. The paper argues this is a "protocol mismatch," but this argument cuts both ways: if the standard evaluation protocol cannot be used, and the paper's preferred protocol (conditional NLI-based Evi-F1) has no established validity in the literature, then the evidence quality claims rest on an unvalidated metric. The 66-72% shrinkage is not just a curiosity — it means the work cannot be placed in context with existing evidence extraction literature.

**W6. Incomplete cross-family and scaling analysis (Moderate).** LLaMA RSFT failed (OOM), 1.7B RSFT failed (low candidate quality). The RSFT conclusions thus rest on a single model family (Qwen3) at only 2 scales (4B, 8B). For a paper making broad claims about training paradigms for evidence-grounded IE, this is a narrow empirical base.

**W7. CED scoring is a non-contribution (Moderate).** CED vs flat-NLI are statistically indistinguishable (p=0.44). DeBERTa-base vs DeBERTa-large yields no significant difference (p=0.38). The specific scoring function — which constitutes the main methodological novelty in the RSFT framework — is shown to be irrelevant. Any NLI-based filter works equivalently. This is reported honestly, but it means the paper has no method contribution at all.

**W8. Cross-dataset degradation suggests overfitting, not generalizable findings (Moderate).** RSFT gains shrink from +5.5pp (DocRED) to +1.5pp (Re-DocRED). Combined with the 5.65pp dev-to-test gap on DocRED itself, this pattern suggests the development-set results that guided all experimental decisions (CED threshold, RSFT hyperparameters) are unreliable indicators of true performance. Findings derived from optimizing on these dev results inherit this unreliability.

---

## 4. Detailed Questions and Suggestions

**Q1.** The method-level EDCR correlation (ρ=−0.965) — how many data points is this computed over? If it's 5-6 methods, please report the p-value explicitly and discuss the influence of the GRPO QLoRA outlier. A leave-one-out sensitivity analysis would strengthen (or honestly weaken) this claim.

**Q2.** The 1.7B "benefit" from evidence (+6.2pp) — is this consistent across random seeds? A single SFT run could produce this by chance. How many seeds were used for the 1.7B SFT experiments?

**Q3.** For the post-hoc BM25 baseline (Table 3), was the BM25 retrieval evaluated on the same test set? The paper reports dev-set numbers in some tables and test-set in others; please clarify which split Table 3 uses.

**Q4.** The paper claims evidence generation acts as "implicit regularization" at 1.7B. What is the evidence for this interpretation beyond the performance number? Is there analysis of training dynamics (loss curves, gradient norms) that would support regularization vs. other explanations?

**Q5.** Related work is thin. Missing discussion of: (a) recent generative IE work beyond SAIS/DREEAM, (b) evidence generation in other NLP tasks (QA, fact verification), (c) multi-objective optimization in NLP more broadly. The paper would benefit from positioning the decoupling spectrum within the broader multi-objective/multi-task learning literature.

**Q6.** No qualitative error analysis is provided. Examples of generated evidence (good and bad), failure modes, and relation-type-specific patterns would substantially strengthen the paper's analytical value.

---

## 5. Experiment Coverage Assessment

Comparing against the experimental design:

| Experiment | Status in Paper | Notes |
|---|---|---|
| Test Set Evaluation | ✅ Complete | Table 1 |
| Re-DocRED Cross-Dataset | ✅ Complete | Table 6 |
| EDCR Human Validation | ✅ Complete | Table 8 |
| DREEAM-Protocol Alignment | ✅ Complete | Table 7 |
| Post-hoc BM25 Retrieval | ✅ Complete | Table 3 |
| NLI Model Ablation | ✅ Complete | Table 9 |
| 1.7B/8B RSFT Scaling | ✅ Complete | 1.7B failed, reported |
| LLaMA Cross-Family | ✅ Complete | RSFT failed (OOM), reported |

All planned experiments are reflected in the paper. Failed experiments are transparently reported. Coverage is complete.

---

## 6. Minor Issues

- Table 2: GRPO bf16 and DPO bf16 (3ep) have missing EDCR values. These should be computable and reported for completeness.
- Section 2.3: The EDCR definition is too terse. The mathematical formulation is absent — readers cannot reproduce it from the description given.
- Section 4.4: Table 4 and Table 5 could be merged for clarity.
- The paper lacks confidence intervals or standard deviations on most reported metrics, making it impossible to assess whether differences are meaningful.
- No references are provided (the PDF appears to omit the bibliography), making it impossible to verify related work claims.

---

## 7. Overall Assessment

**Score: 3 (Reject)**

**Confidence: 4 (High)**

**Justification:**

The paper asks a worthwhile question — what is the cost of requiring LLMs to justify their extractions? — and provides honest empirical answers. The intellectual honesty about negative results is commendable and the decoupling spectrum concept is interesting.

However, the paper's own findings systematically undermine its contributions:

1. The primary analytical target (RSFT with CED scoring) is dominated by a trivial baseline (BM25 post-hoc retrieval), rendering extensive analysis of RSFT variants, CED vs flat-NLI, and NLI model ablation largely academic.
2. The U-shape "scaling law" rests on 3 data points with no replication — insufficient for the claim.
3. EDCR, the proposed diagnostic metric, has weak human validation (ρ=0.31) and its method-level correlation is based on too few methods to be statistically reliable.
4. Absolute performance is 20pp below SOTA, leaving open whether findings generalize to competitive systems.
5. The RSFT analysis is limited to one model family at two scales due to failures.

The paper reads as a thorough negative-result report, which has value, but the magnitude and breadth of the negative results leave insufficient positive contribution for a top venue main conference. The findings are: (a) evidence generation is costly (not surprising), (b) RL can be unstable for multi-objective tasks (known), (c) simple baselines are hard to beat (expected), and (d) the proposed metric doesn't work well (undermining).

**Recommendation:** The decoupling spectrum finding (W/S3) and the evaluation infrastructure gap observation could form the core of a more focused Findings paper, if stripped of the method-contribution framing and if the EDCR claims are appropriately scoped. The current version tries to be both an analysis paper and a methods paper, succeeding at neither.

---

## 8. Scores Summary

| Criterion | Score (1-6) |
|---|---|
| Soundness | 3 |
| Novelty | 3 |
| Significance | 2 |
| Clarity | 4 |
| Reproducibility | 3 |
| **Overall** | **3 (Reject)** |
