---
dream_id: dream_20260516T113255
tier: median
overall_score: borderline — recommend Findings
timestamp: 2026-05-16T12:11:12.244298+00:00
---

# Dream Review Report: "Strong Predictors, Weak Selectors: Why Confidence Signals Cannot Scale Structured Information Extraction"

**Venue**: EMNLP 2026 Main Conference (via ACL Rolling Review)
**Review Mode**: Full (2 Reviewers + Roundtable)
**Dream ID**: 20260516T113255

---

## Venue Calibration

EMNLP 2026 uses ACL Rolling Review with three scoring dimensions: Soundness (1–5), Excitement (1–5), Overall (1–5). Acceptance rate ~22%. Scores anchored to ARR rubric: 5=Excellent, 4=Strong, 3=Acceptable, 2=Poor, 1=Major issues.

---

## Reviewer 1 (R1): Methods and Experiments

### Summary
The paper evaluates 5 confidence signals across 3 families for structured IE (NER + RE), finding strong population-level QE (AUROC up to 0.82, ρ up to 0.45) but failure at instance-level selection (+0.6pp over greedy, p=0.39, d=0.038) despite 13pp oracle headroom. Diagnostic analysis identifies three contributing factors: instance degeneracy, LP score compression, and persistence under reduced degeneracy.

### Strengths
1. **QE-selection decoupling** is a well-executed conceptual separation. Distinguishing population-level prediction from instance-level selection is a genuine methodological insight not clearly articulated in prior TTS work for structured outputs.
2. **LoRA rank ablation** is elegantly designed. Reducing degeneracy from 21% to 7.2% while preserving QE correlation (ρ 0.360→0.365) yet still failing at selection provides strong multi-causal evidence.
3. **Honest statistical reporting**: Bootstrap CI [−3.0, +4.2]pp, p=0.39, d=0.038 for the central negative claim. The paper does not overstate a null finding.
4. **Breadth of evaluation**: 5 signals × 4 QE metrics × selection × 3 datasets × 3 models is a comprehensive matrix.
5. **Free-form decoding ablation** showing LP compression is intrinsic (constrained: 0.0206 vs free-form: 0.0199, ratio 0.97) rules out a common confound.

### Weaknesses
1. **Small effective sample sizes**: SciERC NER n=529, RE n=397 with 43–45% zero-F1; effective RE size ~220. Bootstrap CI width of 7.2pp means the negative result could reflect insufficient power rather than fundamental impossibility.
2. **"Model-agnostic" overclaimed**: Two 8B architectures (Qwen, LLaMA) + one 4B from the same Qwen family does not establish model-agnosticity. Should say "consistent across tested configurations."
3. **Missing entity-token-only LP baseline**: The paper hypothesizes LP fails because format/template tokens dilute entity-level signal but never tests the obvious fix (averaging LP only over entity-span tokens).
4. **Semantic entropy not evaluated**: The most theoretically motivated UQ signal from the LLM uncertainty literature (Kuhn et al. 2023) is discussed in related work but absent from experiments.
5. **Verifier uses oracle F1 labels**: The 8.3% gap closure is an upper bound on these 5 features, not a practical method. Only logistic regression tested — no MLP, random forest, or gradient-boosted alternative.
6. **Single RE dataset** (SciERC only): No second RE dataset (TACRED, DocRED) to validate RE-specific claims.
7. **Aggregate vs per-sample handling confused**: Paper's Eq. (1) defines SJ as per-instance aggregate, but Section 3.3 implies per-sample SJ scores exist (mean pairwise similarity of sample_i against others). If SJ can rank candidates, the "4/5 signals cannot rank" framing is misleading.

### Numerical Consistency Issues
- Abstract claims "AUROC up to 0.82" — highest in tables is 0.816 (CoNLL EM, Table 2), rounded up. Borderline acceptable but imprecise.
- Abstract claims "ρ up to 0.45" — highest reported is 0.421 (EM, Table 2). The 0.45 claim appears inflated.
- Appendix A self-audit catches 4 inconsistencies but misses the abstract-table discrepancies above.

### Reproducibility
- Model names, N, T specified. Metric equations provided.
- **Gaps**: No code/data release. LoRA hyperparameters (LR, epochs, batch size) not reported. Hungarian matching thresholds for SJ not specified. No compute budget or hardware details.

### R1 Scores
- **Soundness**: 3.0/5
- **Excitement**: 3.0/5
- **Overall**: 3.0/5

---

## Reviewer 2 (R2): Novelty and Related Work

### Novelty Assessment

**QE Contribution (A)**: The paper frames this as "confirming and extending known UQ principles to structured IE." This is an honest characterization — the signals (Jaccard, Kappa, EM, voting, logprob) are standard measures applied to structured outputs. More systematic benchmark than conceptual advance.

**Diagnostic Contribution (B)**:
- *Instance degeneracy*: Not itself novel — Snell et al. (2024) already discusses compute-optimal allocation conditioning on difficulty. The specific empirical thresholds (21–58% tied across tasks) add incremental domain-specific value but the concept is known.
- *LP compression* (0.041 nats median range): Interesting empirical observation that follows naturally from autoregressive generation for structured outputs — once the model commits to a structural template, token-level variation is minimal.
- *Persistence under reduced degeneracy* (LoRA rank=8): The most novel finding — demonstrates multi-causality. But the mechanism ("signals lack discriminative power even with headroom") restates that unsupervised heuristics are weaker than supervised verifiers, which is well-established.

**QE-Selection Decoupling**: Partially tautological. 4/5 signals produce one score per instance and trivially cannot rank candidates within an instance. The genuinely empirical content is that LP (the only per-sample signal) also fails, attributed to compression. The paper frames the definitional property as an empirical discovery.

**Capability-degeneracy correlation**: Based on 3 data points, acknowledged as "illustrative." This is speculation, not a contribution.

### Related Work Gaps
- **MBR literature**: Kumar & Byrne (2004), Freitag et al. (2022) discuss MBR failure in structured prediction — the paper's "degeneracy" explanation may be a special case of MBR failure when the reference distribution collapses.
- **Active learning / query-by-committee**: Disagreement as informativeness signal is foundational to QBC (Seung et al. 1992). Relevant parallel uncited.
- **Conformal prediction for structured outputs**: Fisch et al., Angelopoulos et al. — cited in one sentence but deeper engagement warranted for set-valued predictions.
- **Best-of-N with process reward models**: Wang et al. 2024 (Math-Shepherd), Hosseini et al. 2024 — natural comparison for "what would be needed" only mentioned in passing.

### Positioning Concerns
- **CoCoA contrast unfair**: Paper only tests linear combination of 5 signals (logistic regression), not CoCoA's actual MBR-style framework where consistency defines the utility function and confidence weights the reference. The dismissal of ensemble approaches based solely on linear combination is potentially unfair.
- **SJ vs surface matching advantage not empirically demonstrated**: EM actually outperforms SJ on CoNLL (ρ 0.421 vs 0.418) and is competitive across configs. The claimed advantage of structural metrics over Nédéllec & Xia's surface matching is task-dependent, not universal.
- **Title "Cannot" overclaims**: Evidence shows "Do Not" or "Fail To" for specific signals at 4B–8B scale. No impossibility result established.

### Writing Quality
Framing is commendably honest in the body ("confirming and extending," "contributing factors," "preliminary evidence"). Title overclaims relative to evidence. Exposition is clear and well-organized.

### R2 Scores
- **Soundness**: 3.0/5
- **Excitement**: 2.5/5
- **Overall**: 3.0/5

---

## Roundtable Discussion

### Step 2: Cross-Sharing Key Exchanges

**R1 conceded** to R2 that the QE-selection decoupling is partially tautological (4/5 signals definitionally cannot select), revising Excitement from 3.5→3.0.

**R2 conceded** to R1 that the LoRA rank ablation, while confirming known calibration phenomena, is well-designed as domain-specific causal evidence. R2 lowered Soundness from 3.5→3.0 based on R1's numerical inconsistency findings and SJ definitional confusion.

**Both agreed**: Title overclaims; cross-model validation insufficient for "model-agnostic"; missing baselines are addressable in revision but weaken current claims.

### Step 3: Convergence — Resolution of Key Disagreements

**1. Tautology vs Empirical Finding**
*Resolved*: R2 substantially correct. The "QE-selection decoupling" conflates (a) a definitional truism (4/5 signals are per-instance aggregates that cannot discriminate among samples) with (b) a genuine empirical finding (LP compression, free-form ablation showing it's intrinsic, +2.9pp recovery on non-degenerate subset). The contribution is narrower than framed but real. The SJ definitional confusion (Eq. 1 vs Section 3.3) must be resolved.

**2. Instance Degeneracy: Rebranding vs Novel Characterization**
*Resolved*: Both partially correct. The abstract concept is known (Snell et al. 2024), but the paper provides concrete empirical thresholds specific to structured IE (60% tied at ε=0.05, task-difficulty dependence). Incremental empirical value, not "novel contribution."

**3. LoRA Rank Ablation**
*Resolved*: R1's assessment prevails. The specific experiment design — showing reduced degeneracy (21%→7.2%) with preserved QE correlation (ρ 0.360→0.365) yet failed selection — is solid domain-specific causal evidence. Worthy of inclusion, should not be framed as discovering a new phenomenon.

**4. Missing Baselines**
*Resolved*: Not fatal individually, but collectively weaken "first systematic comparison" claim. Entity-token LP and semantic entropy are addressable in revision. CoCoA MBR-style comparison is the most damaging omission — paper should discuss why it was not tested.

**5. Numerical Inconsistencies**
*Resolved*: Core table data appears internally consistent. Abstract rounding (AUROC 0.82 from 0.816, ρ 0.45 from 0.421) is sloppy but not fraudulent. Does not undermine central claims but reflects careless presentation. Requires numerical pass before publication.

---

## Step 4: Consolidated Assessment

### Consensus Scores

| Dimension | R1 | R2 | Consensus |
|---|---|---|---|
| **Soundness** | 3.0 | 3.0 | **3.0** |
| **Excitement** | 3.0 | 2.5 | **2.5–3.0** |
| **Overall** | 3.0 | 3.0 | **3.0** |
| **Confidence** | 4/5 | 4/5 | **4/5** |

### Venue Recommendation: **EMNLP 2026 Findings**

The paper identifies a practically important phenomenon with rigorous methodology, but:
- The core finding is partially definitional (4/5 signals) with one genuine empirical kernel (LP failure + diagnostics)
- No new method proposed; supervised verifier is preliminary (8.3% gap closure)
- Contribution pattern (systematic comparison + negative result + diagnostic) fits Findings better than Main
- Main would require either a stronger positive contribution (method closing more of oracle gap) or broader scope (multiple model scales, more tasks)

### Top 3 Required Revisions

**C1. Reframe contribution hierarchy.** Clearly separate the definitional layer (4/5 signals cannot select by construction — state in one sentence) from the empirical layer (LP compression diagnosis, free-form ablation, non-tied subset recovery). Currently the paper inflates the contribution by framing the definitional property as a unified empirical discovery.

**C2. Resolve SJ definitional confusion.** Eq. (1) defines SJ as per-instance aggregate, but Section 3.3 implies per-sample SJ scores. Clarify whether SJ produces per-sample rankings; if so, report SJ-based selection results. This directly affects the paper's central framing.

**C3. Scope claims to evidence.** Replace "cannot scale" with "fail to scale" in title. Replace "model-agnostic" with "consistent across tested 4B–8B configurations." Correct abstract: ρ ≤ 0.421 (not "up to 0.45"), AUROC = 0.816 (not "0.82").

### Top 3 Suggestions

**S1. Add entity-token-only LP analysis.** The paper hypothesizes LP dilution from format tokens but never tests it. Computing LP only over entity-span tokens would either confirm or falsify the hypothesis at zero additional inference cost.

**S2. Engage deeply with CoCoA.** Discuss why MBR-style fusion was not tested, and whether CoCoA's formulation would predict the correlation-selection gap for structured outputs. This strengthens the "structured IE is different" argument.

**S3. Multi-seed selection validation.** The central claim rests on p=0.39 from one configuration. Report selection results across multiple seeds for SciERC NER LP to confirm the null result is robust.

### Meta-Review

This paper investigates whether confidence signals from multi-sample LLM generation can select better structured IE outputs. The experimental scope is commendable: five signals across three datasets with multiple models, supported by rigorous statistics (bootstrap CIs, effect sizes). The central finding — that signals achieving ρ up to 0.42 and AUROC up to 0.82 at population-level QE fail at instance-level selection (+0.6pp, p=0.39, with 13pp oracle headroom) — has genuine practical value. However, both reviewers converge on a fundamental framing concern: four of five signals fail at selection by mathematical construction (they produce one scalar per instance), making the "gap" partially tautological. The true empirical contribution is narrower but real: logprob score compression, its persistence under free-form decoding, and partial recovery on non-degenerate subsets (+2.9pp, p=0.004). The LoRA rank ablation demonstrating multi-causality is the strongest experiment. Missing baselines (entity-token LP, semantic entropy, MBR-style combination) and numerical imprecision in the abstract weaken confidence. With reframing to honestly separate definitional from empirical content and claim-scope corrections, this is appropriate for EMNLP Findings as a rigorous diagnostic study.