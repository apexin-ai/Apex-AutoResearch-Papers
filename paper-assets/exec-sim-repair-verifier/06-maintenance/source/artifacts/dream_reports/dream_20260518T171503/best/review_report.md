---
dream_id: dream_20260518T171503
tier: best
overall_score: weak reject
timestamp: 2026-05-18T18:01:00.999492+00:00
---

# Dream Review Report: "The Formulation Design Space for Neural Code Verification"

**Dream ID**: 20260518T171503  
**Review mode**: Full (2 reviewers, 4-step roundtable)  
**Venue standard**: Top ML venue, ~25% acceptance, 6-point scale

---

## 1. Paper Summary

This paper compares three formulations for execution-free code verification: per-test binary classification (CLS), execution output prediction (CWM), and trajectory-level scoring (TRAJ). The comparison uses LoRA fine-tuning on identical data (SWE-bench-PerTest) with two model families (Qwen3-4B, DeepSeek-R1-Qwen3-8B) at function-level and repository-level complexity. The central finding is that no single formulation dominates: at function-level the three are statistically equivalent (TOST p=0.007, ±2pp), while at repository-level CWM viability becomes model-contingent (93% unparseable on Qwen3 vs. 11.8% on DeepSeek). The paper also reports CLS/CWM error complementarity (+2.8pp oracle ensemble), releases the SWE-bench-PerTest dataset (467 instances, 89,664 labels), and presents a non-significant re-repair PoC (+4pp, p=0.18).

---

## 2. Roundtable Process

### Step 1: Independent Reviews

**R1 (Method + Experiments)** — Score: 3.5/6  
**R2 (Novelty + Related Work)** — Score: 3.0/6

### Step 2: Cross-Sharing Key Points

**R1 highlights shared with R2:**
- Strong statistical methodology (TOST equivalence testing, clustered bootstrap with ICC, design effect reporting) is a genuine differentiator
- CWM may be systematically disadvantaged: while the paper states max seq_len=8192, CWM must reserve output tokens for generation whereas CLS uses only 1 output token, creating an input-context disparity at repo level
- Repo-level results have gaps: Qwen TRAJ results are missing entirely (dashes in Table 3); DeepSeek TRAJ lacks F1 and unparseable metrics
- Multi-seed validation: DeepSeek CLS has 2 seeds (mean 81.45±0.92), but CWM appears to be single-seed (84.2). The paper's strongest claim — cross-model reversal — depends on this single-seed CWM number
- Default assignment artifact analysis (unparseable outputs defaulting to majority class) is a genuinely insightful finding

**R2 highlights shared with R1:**
- Novelty concern: the qualitative direction of findings (generation harder than classification for long outputs) is predictable from the paper's own theoretical framing ($q^L$ exponential decay)
- Missing constrained decoding discussion: the central negative finding (CWM format non-compliance) has an obvious mitigation that the paper never addresses
- Only 11 references is thin for a top venue — missing structured generation literature, broader SWE-bench ecosystem, reward modeling beyond Lightman/Uesato
- "Design space" framing is inflated for what is essentially running three existing formulations side by side; the paper does not propose new formulations or methods
- Framing mismatch: paper claims "no formulation dominates" but CLS actually wins or ties in every practical scenario (equal/better accuracy, 6-9× faster, diagnostic granularity)

### Step 3: Convergence

**Points of agreement (both reviewers):**

1. **Statistical methodology is a clear strength.** TOST equivalence testing with margin sensitivity, clustered bootstrap respecting within-problem correlation, ICC-based design effects — this is substantially more rigorous than typical empirical ML papers.

2. **Honest limitations disclosure.** The paper is transparent about single-seed constraints, the gap between its LoRA setup and the original 32B CWM, and the non-significance of the re-repair result. This builds credibility.

3. **Tokenizer-specific finding is the most novel contribution.** The 93% vs 11.8% unparseable rate across models at repo level, combined with 0% vs 0% at function level, is a striking result that genuinely advances understanding.

4. **Incomplete three-way comparison weakens the premise.** The paper's title and framing promise a comparison of three formulations, but at repo level (where the interesting dynamics emerge), Qwen TRAJ is entirely missing, and DeepSeek TRAJ has only accuracy (no F1, no unparseable). The three-way comparison is complete only at function level.

5. **Two model families is thin for an "interaction" claim.** The formulation × model interaction is the paper's headline finding, but with n=2 models the observed pattern could reflect any of numerous confounds (vocab size, pretraining corpus, architecture differences).

6. **Small model scale limits generality.** All experiments use 4-8B LoRA-adapted models. The original CWM work (Gu et al., 2024) uses a 32B model with mid-training on execution traces. The LoRA rank 64 setup may be insufficient for CWM's harder generation task, making the comparison structurally unfair.

**Points of productive disagreement:**

- R1 emphasizes experimental design fairness (CWM disadvantaged by shared setup) while R2 emphasizes low novelty. Both concerns are valid and complementary: even if the comparison were perfectly fair, the finding's qualitative direction is predictable.
- R1 is more positive about the paper's practical value to practitioners (score 3.5); R2 finds the novelty bar unmet for a top venue main track (score 3.0). The consensus is that the paper sits between these — solid empirical work that falls short of a top venue main track but could fit Findings.

### Step 4: Consolidated Assessment

---

## 3. Strengths

1. **Rigorous statistical framework.** TOST equivalence testing (with sensitivity analysis across ±1pp to ±5pp margins), clustered bootstrap with ICC correction, and design effect reporting. This is a model for how empirical ML comparisons should be conducted.

2. **Clean controlled design.** Holding LoRA hyperparameters (rank 64, α=128, lr=1e-4, bs=16, 3 epochs, seq_len=8192), training data, and evaluation protocol constant across formulations isolates the effect of formulation choice from confounding factors.

3. **Striking cross-model CWM unparseable reversal.** The 93% (Qwen) vs 11.8% (DeepSeek) unparseable rate at repo level, against 0% vs 0% at function level (Table 4), is an order-of-magnitude difference that is hard to dismiss as noise. This provides concrete evidence that CWM failure is tokenizer-specific rather than formulation-inherent.

4. **Parseable-only accuracy analysis.** The finding that DeepSeek's parseable CWM outputs reach 88.7% accuracy (n=8,629), comparable to function-level CWM (86.8%), demonstrates that CWM verification capability transfers across complexity levels when format compliance is achieved.

5. **Practical efficiency quantification.** CLS offers 6-9× inference speedup over CWM (single token vs multi-token generation) with no accuracy penalty at function level. This is directly actionable for practitioners.

6. **Honest reporting of negative results.** The re-repair PoC (+4pp, p=0.18) is presented as a non-significant future direction rather than inflated into a contribution. The oracle ceiling (+8pp) provides honest motivation for future work.

7. **Dataset contribution.** SWE-bench-PerTest (467 instances, 89,664 per-test labels) fills a genuine gap — per-test level SWE-bench annotations did not previously exist as a public resource.

---

## 4. Weaknesses

### W1: Incomplete Three-Way Comparison at Repository Level (Major)
The paper frames itself as comparing three formulations, but at repo level — where the interesting dynamics emerge — the comparison is incomplete. Qwen TRAJ is entirely absent (dashes in Table 3), and DeepSeek TRAJ has only accuracy (75.4%) with no F1 or unparseable metrics. The three-way comparison is complete only at function level, where the finding is a null result. This gap undermines the paper's central framing.

*Impact*: The paper's premise ("the formulation design space") promises a complete map but delivers a partial one. Readers cannot assess how TRAJ behaves across models at the complexity level that matters.

### W2: CWM Single-Seed at Repository Level (Major)
DeepSeek CWM repo-level accuracy (84.2%) appears to be a single-seed result, while DeepSeek CLS reports two seeds (82.1% and 80.8%, mean 81.45±0.92). The cross-model reversal claim (CWM > CLS on DeepSeek by 2.7pp) rests on comparing a single CWM seed against the CLS mean. Given that CLS seed variance is ~1.3pp, the CWM advantage could be within single-seed noise.

*Impact*: The headline finding — that CWM can outperform CLS on a compatible tokenizer — has insufficient statistical backing.

### W3: Missing Constrained Decoding Discussion (Major)
The paper's central negative finding for CWM (54-93% unparseable rate at repo level) has an obvious engineering mitigation: grammar-constrained or structured decoding (Outlines, Guidance, LMQL). The paper never mentions this possibility. A reviewer will immediately ask: "If the only problem is format compliance, why not enforce it at decoding time?" Even if constrained decoding would not fully solve the problem (e.g., because the issue is also semantic content quality), the paper must engage with this objection.

*Impact*: Creates a perceived gap in the analysis. The CWM-is-broken conclusion may be engineering-contingent rather than formulation-inherent.

### W4: Thin Reference Coverage (Moderate)
Only 11 references is notably low for a top venue submission. Key gaps:
- **Structured generation / constrained decoding**: Directly relevant to the CWM parsing failure analysis
- **SWE-bench ecosystem**: SWE-bench Lite, SWE-Gym, Agentless, AutoCodeRover — none cited despite building on SWE-bench
- **Reward modeling beyond code**: GenRM, Math-Shepherd, and broader ORM/PRM literature
- **Execution prediction**: CRUXEval benchmark (Gu et al. is cited but primarily as the CWM reference, not as an execution prediction benchmark)

*Impact*: Signals insufficient literature engagement. The Related Work section, while well-structured with 4 subsections, is too sparse to convince a reviewer that the authors have thoroughly surveyed the field.

### W5: Limited Novelty — Predictable Direction of Findings (Moderate)
The qualitative finding that generation (CWM) is harder than classification (CLS) when output length increases is well-anticipated by the paper's own theoretical analysis (the $q^L$ exponential decay argument in Section 3.2/3.3). The TOST equivalence at function level is a null result. The cross-model reversal is the most novel finding, but as noted in W2, it rests on thin evidence. The "design space" framing inflates a controlled benchmark comparison — the paper does not propose new formulations, training methods, or mitigation strategies.

*Impact*: The contribution is primarily one of rigorous quantification of expected trends, which is valuable but may not meet the novelty bar for a top venue main track.

### W6: Small Scale vs. Original CWM (Moderate)
All experiments use 4-8B LoRA-adapted models. The original CWM work (Gu et al., 2024) uses a 32B model with mid-training on execution traces — a fundamentally different and likely much stronger approach than LoRA rank-64 on an 8B model. The paper acknowledges this in the Limitations section, but the disclaimer does not eliminate the concern: the observed CWM failure might be a consequence of insufficient model capacity and adaptation method rather than a formulation limitation.

*Impact*: Limits the generalizability of the "CWM fails at repo level" claim. A reviewer familiar with the original CWM work will find this gap significant.

### W7: Framing Mismatch (Minor)
The paper concludes "no single formulation dominates," but the results actually show CLS winning or tying in nearly every practical scenario: equivalent or better accuracy at function level, dramatically better on Qwen at repo level, comparable on DeepSeek (only 2.7pp behind CWM), 6-9× faster, and with diagnostic granularity. The only scenario where CWM wins is DeepSeek repo-level accuracy, and this is single-seed with a 2.7pp margin. The "design space" framing obscures what is effectively a recommendation for CLS as the safe default.

---

## 5. Questions for Authors

1. **Multi-seed CWM**: Can you provide a second seed for DeepSeek CWM at repo level? The cross-model reversal claim depends on this single number.

2. **Constrained decoding**: Have you considered grammar-constrained generation to enforce CWM output format? If the unparseable rate drops to near-zero under constrained decoding, does CWM's parseable-only accuracy (88.7%) make it clearly superior?

3. **Qwen TRAJ at repo level**: Is this result available or omitted for a reason? The three-way comparison requires it.

4. **CWM output length vs accuracy**: Can you provide a binned analysis of CWM accuracy stratified by target output length? This would directly validate the exponential-decay theoretical argument and identify the threshold where CWM begins to fail.

5. **Tokenizer analysis**: The tokenizer-specific hypothesis is central. Have you analyzed how Qwen3 vs DeepSeek tokenizers handle the specific delimiters in CWM output format (test result markers, pass/fail indicators)? A concrete tokenization example would strengthen the claim beyond correlation.

6. **Scale sensitivity**: Do you expect the CWM failure pattern to persist at 32B scale or with full fine-tuning (not LoRA)?

---

## 6. Experiment Coverage Assessment

Comparing the paper against the review_context.yaml experiment list:

| Imagined Experiment | In Paper? | Notes |
|---|---|---|
| DeepSeek CLS Repo v5 (seed 42) | Yes | Table 3: 82.1% |
| DeepSeek CWM Repo Epoch-2 | Yes | Table 3: 84.2%, Table 4: 11.8% unparseable |
| DeepSeek CLS Repo Seed 123 | Yes | Section 4.3: 80.8%, mean 81.45±0.92 |
| SWE-bench-PerTest Construction | Yes | Table 1: 467 instances, 89,664 labels |
| Diagnostic Re-Repair PoC | Yes | Table 6: +4pp (p=0.18) |

All 5 imagined experiments are reflected in the paper. Coverage is complete.

The review_context expected an oracle ensemble of 87.0%; the paper reports 87.0% (Table 5). The expected DeepSeek CWM accuracy was 84.2%; the paper reports 84.2%. Expected unparseable rate was 11.8%; paper reports 11.8%. The paper faithfully represents all expected results.

**Missing from context but present in paper**: Function-level results (Table 2) and the tokenizer-specific analysis (Table 4, Section 4.4) are in the paper but not listed as separate imagined experiments. The re-repair oracle ceiling (+8pp) is reported as expected.

---

## 7. Scores

### R1 (Method + Experiments)
- **Score**: 3.5 / 6
- **Confidence**: 4 / 5
- **Key concern**: Incomplete repo-level comparison (missing Qwen TRAJ), single-seed CWM, potential CWM disadvantage from shared training setup

### R2 (Novelty + Related Work)
- **Score**: 3.0 / 6
- **Confidence**: 4 / 5
- **Key concern**: Predictable finding direction, inflated "design space" framing, thin references (11 total), missing constrained decoding discussion

### Consolidated Score: **3.0 / 6 (Weak Reject)**

### Justification

The paper addresses a practically relevant question with above-average statistical rigor. The TOST equivalence framework, clustered bootstrap with ICC, and the honest reporting of negative results are genuine methodological strengths that the community should adopt more broadly. The tokenizer-specific CWM failure finding (93% vs 11.8% unparseable) is the paper's most interesting and novel contribution.

However, several factors prevent recommendation for acceptance at a top venue main track:

**(a) Incomplete evidence for the headline claim.** The cross-model reversal (CWM > CLS on DeepSeek) appears to be single-seed. The three-way comparison is missing Qwen TRAJ at repo level. The paper promises "the formulation design space" but delivers a partial map.

**(b) Limited novelty.** The qualitative direction of every finding is predictable: generation harder than classification for long outputs, function-level equivalence when outputs are short, tokenizer properties affect generation quality. The contribution is in rigorous quantification, not in surprising insights.

**(c) Missing engagement with constrained decoding.** The central CWM failure finding has an obvious engineering mitigation that the paper ignores entirely. This creates a perceived analytical gap.

**(d) Thin references and small experimental scale.** 11 references is insufficient. 4-8B LoRA models are far from the original CWM setup (32B mid-training), limiting generalizability claims.

**(e) Framing overreach.** "The formulation design space" framing overpromises relative to what is a controlled benchmark of three existing methods on two models.

### Path to Improvement

The paper could strengthen significantly with:
1. Second seed for DeepSeek CWM repo-level (validate the reversal claim)
2. Qwen TRAJ at repo level (complete the three-way comparison)
3. A constrained decoding experiment or thorough discussion
4. Expanded references (target 25-30 for a top venue)
5. At minimum one additional model family (to support the "interaction" claim)
6. Narrower, more honest framing: "CLS vs CWM on two model families" rather than "the formulation design space"

With these improvements, the paper could reach 3.5-4.0 (Borderline Conference to Weak Accept) at a top venue.