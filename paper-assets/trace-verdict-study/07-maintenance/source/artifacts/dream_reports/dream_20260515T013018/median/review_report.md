---
dream_id: dream_20260515T013018
tier: median
overall_score: weak reject
timestamp: 2026-05-15T02:06:37.458791+00:00
---

# Dream Review Report: Verdict-Optimized Trace Abstraction for Code Behavior Classification

**Dream ID:** 20260515T013018
**Review Mode:** full (2 Reviewers + 4-step Roundtable)
**Date:** 2026-05-15

---

## Reviewer Assignments
- **R1:** Methods + Experiments
- **R2:** Novelty + Related Work

---

## Step 1: Independent Reviews

### Reviewer 1 (R1): Methods + Experiments

**Score: 3 (Weak Reject)**

#### Summary
The paper investigates trace-augmented SFT for binary verdict tasks and proposes VOTA, a compact ~80-token trace capturing assertion-point snapshots, exception summaries, and loop compression. The main finding is that VOTA substantially improves verdict accuracy over no-trace on CodeLlama-7B, while full execution traces cause model collapse. Ablations decompose VOTA's contribution and attribute full-trace collapse to gradient dilution + content noise.

#### Strengths
- **Comprehensive ablation design.** 8 experiments systematically probe different aspects: component ablation, label-only loss, trace length, cross-model, cross-task, calibration, and seed robustness. Thorough for an empirical study.
- **Gradient dilution diagnosis is well-designed.** Label-only loss recovery (28.4%→62%) combined with trace-length monotonic decline provides a convincing two-factor explanation.
- **Appropriate statistical methodology.** McNemar's test for paired comparison, bootstrap CIs, multi-seed validation are correct choices for binary outcomes on this sample size.
- **Component ablation reveals interpretable structure.** Showing each VOTA component's independent contribution and super-additive combination provides actionable design guidance.
- **Useful negative result.** Full-trace collapse finding with quantitative decomposition is genuinely informative.

#### Weaknesses
- **Dataset description is insufficient.** No discussion of: (a) how repositories were selected, (b) whether train/test split is repository-level (to avoid data leakage from related code), (c) overlap with base model pretraining data, (d) distribution of code complexity, (e) whether the 71.5/28.5 pass/fail ratio is natural or artificial.
- **The 60/40 gradient dilution vs. content noise decomposition assumes separability.** The two effects interact: label-only loss changes the entire optimization landscape, not just one factor. The decomposition is a useful narrative but not a rigorous causal decomposition. The paper should acknowledge this limitation.
- **Generalizability is genuinely limited.** Only two models of similar size (6.7B and 7B), two verdict tasks. VOTA lift ranges from +8pp (bug detection) to +24pp (test verdict on CodeLlama) — a 3x variation. The "design guideline" claims are not well-supported by such variable results.
- **No pairwise component ablation.** The paper tests single-component and full-VOTA conditions but not two-component combinations (e.g., actual/expected + exception). Without these, interaction effects cannot be properly quantified.
- **Missing oracle baseline.** Simply providing actual==expected as a single boolean feature would establish an upper bound for the "string matching" hypothesis and clarify VOTA's contribution beyond trivial value comparison.
- **No error analysis.** What do VOTA's ~1.5% errors look like? Systematic patterns in failures would strengthen the mechanistic understanding.
- **Only 7B models tested.** Whether larger models can extract signal from full traces without collapse (e.g., by better attention over long contexts) is important for the gradient dilution narrative.
- **LoRA hyperparameters.** Rank 16 with α=32 gives effective scaling 2.0, which is aggressive. Was this tuned, and on what data?
- **Label-only loss is a known technique** (standard in instruction tuning), but presented without proper contextualization in the loss masking literature.

#### Questions for Authors
1. Is the train/test split repository-level or random? What prevents code from the same repository appearing in both splits?
2. For label-only loss: was the no-trace baseline also retrained with label-only loss for a fair comparison, or is 75.13% from standard loss?
3. What is the actual VOTA token count distribution (mean, std, min, max)?
4. Were LoRA hyperparameters tuned, and if so, on what split?
5. What happens with VOTA + label-only loss? This would help disentangle compression vs. content quality.

#### Missing Experiments
- Pairwise component ablation (2-component combinations)
- Learning curve / data scaling analysis
- Error analysis on VOTA failure cases
- Larger model evaluation (13B+)
- Oracle boolean baseline (actual==expected as single feature)
- VOTA with label-only loss

---

### Reviewer 2 (R2): Novelty + Related Work

**Score: 3 (Weak Reject)**

#### Summary
The paper studies execution trace granularity for SFT on binary code verdict tasks, proposing VOTA as a compact trace abstraction. The core finding is that task-aligned trace compression vastly outperforms both no-trace and full-trace SFT. Component ablation reveals actual/expected value pairs are the dominant signal, and label-only loss experiments decompose full-trace collapse into gradient dilution and content noise.

#### Strengths
- **Useful negative result on full-trace SFT.** The collapse finding with quantitative decomposition via label-only loss is genuinely informative, complementing DCSH's findings for generation tasks.
- **Clean experimental decomposition.** The label-only loss ablation that separates gradient dilution from content noise is a well-designed experiment with a clear interpretation.
- **Correct positioning as empirical study.** The title and framing appropriately set expectations for an empirical analysis rather than a method contribution.
- **Fills a genuine gap.** DCSH (generation), TracePile (pretraining), and TRACED (encoder classification) did not study decoder SFT for classification. This paper addresses that gap.

#### Weaknesses
- **VOTA is feature engineering, not a method contribution.** The 74.3% lift from actual/expected values means VOTA is essentially providing the model with the two values it needs to compare for the verdict. For pass/fail prediction, knowing actual vs. expected is nearly sufficient to determine the answer. Framing this as "trace abstraction" overstates the conceptual contribution when "provide actual vs. expected values as input features" is more accurate.
- **Design guideline (Claim 3) is truistic.** "Minimize irrelevant state, maximize decision-relevant signal density" is a restatement of the feature relevance principle understood since Guyon & Elisseeff (JMLR 2003). The paper provides no mechanism for identifying "decision-relevant" elements beyond manual domain knowledge.
- **Related work is severely inadequate — only 6 references.** Critical missing areas:
  - **Loss masking in SFT:** Selective loss masking is well-studied in multi-task learning and instruction tuning. The label-only loss experiment reinvents a known technique without acknowledgment.
  - **Feature selection:** VOTA is an input feature selection exercise with no connection to the extensive feature selection literature.
  - **Trace-as-CoT approaches:** NExT (Ni et al., ICML 2024), Code Execution as Grounded Supervision (Jung et al., EMNLP 2025), and ET-CoT/PyTracify are directly relevant but uncited.
  - **Prompt engineering / structured input formatting:** VOTA is a structured input design choice; this literature is unacknowledged.
  - **Verdict prediction in SE:** APPT (TSE 2024) for patch correctness, mutation-guided verdict approaches.
  - **Calibration of code LLMs:** Relevant if calibration analysis is included.
- **Information bottleneck connection is superficial.** Tishby (2000) is invoked but no information-theoretic analysis is provided — no I(trace; verdict), no rate-distortion analysis, no formal IB connection. This is name-dropping.
- **Insufficient differentiation from TRACED.** TRACED showed traces help encoder-based classification. Why is the decoder SFT distinction conceptually important, beyond an incremental "it also works here" finding?
- **Missing baseline: structured features without trace framing.** Comparing VOTA to flat key-value features (actual=X, expected=Y, exception=Z) without any trace abstraction framing is essential. If they perform comparably, the "trace abstraction" framing adds no value.
- **VOTA acronym presupposes conclusion.** "Verdict-Optimized" embeds the conclusion in the name, inappropriate for an empirical study claiming to investigate trace design.

#### Questions for Authors
1. Have you compared VOTA to providing actual/expected as flat structured features without any trace/assertion-point framing?
2. Why use instruction-format SFT (next-token prediction on "pass"/"fail") instead of a classification head? How does this architecture choice affect gradient dilution?
3. Can you provide I(VOTA; verdict) vs. I(full_trace; verdict) to substantiate the information bottleneck framing?
4. How much of VOTA's accuracy comes from trivially matchable actual==expected cases vs. cases requiring non-trivial comparison?

#### Missing Related Work (Priority Order)
1. Loss masking / multi-task loss weighting (Kendall et al. 2018; instruction tuning loss strategies)
2. NExT (Ni et al., ICML 2024) — trace as CoT rationale
3. Code Execution as Grounded Supervision (Jung et al., EMNLP 2025)
4. ET-CoT / PyTracify (ICML 2025 Workshop)
5. APPT (TSE 2024) — patch correctness verdict
6. Feature selection literature (Guyon & Elisseeff, JMLR 2003)
7. Program slicing / trace compression (ND-Slicer, FSE 2024)
8. Calibration of code LLMs (Spiess et al., ICSE 2025)

---

## Step 2: Cross-Sharing

### R1 response to R2's review:
**Agreement:** R2's observation that VOTA is essentially feature engineering (providing actual/expected = providing the answer) is the most important conceptual critique. This reframes the paper's contribution: VOTA's 98.45% accuracy is less impressive when you realize it's mostly pattern-matching actual vs. expected values. The missing "flat features" baseline is critical — if actual=X, expected=Y works as well without trace framing, the trace abstraction contribution is nil.

**Partial disagreement:** R2 rates the collapse diagnosis higher than I do. While the label-only loss experiment is well-designed, the 60/40 decomposition is presented as more precise than the methodology supports. The two effects are coupled, not separable.

**New concern raised:** R2's point about classification head vs. instruction-format SFT is important. The gradient dilution problem is partially an artifact of using next-token prediction for classification. A classification head would eliminate dilution by construction.

### R2 response to R1's review:
**Agreement:** R1's concerns about dataset description and repository-level splits are well-taken. Data leakage between train/test from the same repository would inflate all results. The missing error analysis and oracle boolean baseline are important gaps.

**Partial disagreement:** R1's missing experiment suggestions (pairwise ablation, larger models, data scaling) are all valid but represent a higher experimental bar than is typical. The paper's 8 experiments are already above average in quantity.

**Refinement:** R1's point about LoRA α=32 being aggressive is worth noting but unlikely to change the qualitative conclusions. The more fundamental issue is whether the task is too easy with VOTA (actual/expected essentially gives the answer).

---

## Step 3: Convergence

### Points of Agreement (Both Reviewers)
1. **The full-trace collapse diagnosis is the paper's strongest contribution.** The label-only loss experiment providing a quantitative (if approximate) decomposition into gradient dilution and content noise is genuinely informative.
2. **VOTA's core mechanism is providing the answer, not trace abstraction.** The 74.3% contribution of actual/expected values means VOTA is essentially task-specific feature engineering. The "trace abstraction" framing overstates the conceptual contribution.
3. **Generalizability is a significant limitation.** Effect sizes vary 3x across conditions (+8pp to +24pp). Only two 7B-class models and two tasks tested.
4. **Related work coverage is critically inadequate.** 6 references for an empirical study is far below venue standards. Major relevant areas (loss masking in SFT, trace-as-CoT, feature selection) are entirely absent.
5. **Dataset description is insufficient.** Repository-level splits, overlap with pretraining data, and code complexity distribution are unaddressed.
6. **The design guideline contribution is truistic.** "Use relevant features" is not a novel insight.
7. **Missing key baselines.** Flat structured features (without trace framing) and oracle boolean (actual==expected) would clarify VOTA's actual contribution.

### Points of Disagreement
1. **Severity of assessment.** R1 leans toward stronger rejection due to methodological gaps; R2 gives slightly more credit for the collapse mechanism finding.
2. **60/40 decomposition rigor.** R1 views it as fundamentally flawed (non-separable effects); R2 views it as approximate but directionally useful.

### Consensus Score: 3 (Weak Reject)
Both reviewers converge on Weak Reject after cross-sharing. The full-trace collapse diagnosis has value, but the core VOTA contribution lacks novelty (feature engineering, not method), related work is severely inadequate, generalizability is limited, and key baselines are missing.

---

## Step 4: Consolidated Assessment

### Overall Score: 3 — Weak Reject

### Meta-Review Summary

This paper investigates an interesting question: how should execution traces be designed for trace-augmented SFT on binary verdict tasks? The experimental program is comprehensive (8 experiments) and the presentation is generally clear. However, several fundamental issues prevent acceptance at a top ML venue.

### Key Strengths
1. **Full-trace collapse diagnosis.** The finding that full execution traces collapse SFT to below-majority-baseline accuracy, decomposed via label-only loss into gradient dilution (~60%) and content noise (~40%), is genuinely informative for the trace-augmented LLM community. This complements DCSH's findings for generation tasks.
2. **Systematic ablation design.** The component ablation, trace length ablation, and cross-condition experiments form a well-structured empirical investigation.
3. **Appropriate positioning.** The paper correctly frames itself as an empirical study rather than a method contribution, which is the right positioning.
4. **Statistical methodology.** Multi-seed validation, McNemar tests, and bootstrap CIs are appropriate choices.

### Key Weaknesses
1. **VOTA is feature engineering, not a generalizable insight.** The component ablation reveals that 74.3% of VOTA's lift comes from actual/expected value pairs — i.e., providing the model with the two values it needs to compare for the verdict. This is task-specific feature selection, not a trace abstraction method. The missing comparison to flat structured features (actual=X, expected=Y without trace framing) is a critical gap: if flat features perform comparably, the "trace abstraction" contribution is nil.
2. **Related work is severely inadequate.** 6 references is unacceptable for any venue. Major missing areas include: loss masking in SFT (the label-only loss experiment reinvents a known technique), trace-as-CoT approaches (NExT, Code Execution as Grounded Supervision), feature selection literature, and calibration of code LLMs. The information bottleneck invocation is superficial (no information-theoretic measurements).
3. **Limited generalizability undermines claims.** VOTA lift varies from +8pp (bug detection) to +24pp (test verdict on CodeLlama), a 3x range. Only two 7B-class models tested. The design guideline cannot be claimed as general from such limited evidence.
4. **Dataset details insufficient.** Whether train/test splits are repository-level (critical for avoiding leakage), overlap with pretraining data, and code complexity distribution are all unaddressed.
5. **60/40 decomposition lacks rigor.** Gradient dilution and content noise are coupled effects; label-only loss changes the optimization landscape, not just one factor. The decomposition is directionally useful but presented as more precise than the methodology supports.
6. **Design guideline is truistic.** "Minimize irrelevant state, maximize decision-relevant signal density" is a restatement of feature relevance principles known since the 1990s. No mechanism for identifying "decision-relevant" elements beyond manual domain engineering is provided.

### Missing Critical Elements
- **Flat feature baseline:** actual=X, expected=Y as structured input without trace abstraction framing
- **Oracle boolean baseline:** single actual==expected flag
- **Pairwise component ablation:** two-component combinations for interaction analysis
- **Error analysis:** systematic characterization of VOTA failure cases
- **Larger model evaluation:** whether gradient dilution persists at 13B+
- **Related work expansion:** at minimum 15-20 references engaging with loss masking, trace-as-CoT, feature selection, and verdict prediction literature

### Recommendation
The paper's strongest finding — full-trace collapse diagnosis with two-factor decomposition — would make a solid workshop paper or short paper (4-page Findings). For a full main conference paper, the following would be needed: (a) add the flat feature baseline and oracle boolean to clarify VOTA's actual contribution, (b) expand related work to engage with loss masking, trace-as-CoT, and feature selection literatures, (c) address dataset details (repository-level splits, pretraining overlap), (d) test on larger models and more tasks, and (e) temper the design guideline claim or provide a mechanism for automated identification of decision-relevant trace elements.

### Scores Summary
| Reviewer | Focus | Score |
|----------|-------|-------|
| R1 | Methods + Experiments | 3 (Weak Reject) |
| R2 | Novelty + Related Work | 3 (Weak Reject) |
| **Consensus** | | **3 (Weak Reject)** |

### Confidence: 4/5
Both reviewers have high confidence in their assessments. The methodological and novelty concerns are clear and specific. The main uncertainty is whether the flat feature baseline would confirm or refute the "VOTA is just feature engineering" hypothesis — if VOTA's trace framing adds substantial value beyond flat features, the paper's contribution would be stronger than currently assessed.
