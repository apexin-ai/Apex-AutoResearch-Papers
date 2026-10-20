---
dream_id: dream_20260523T034027
tier: median
overall_score: 4/10 — Weak Reject
timestamp: 2026-05-23T04:42:25.533006+00:00
---

# Dream Review Report — Consolidated

**Paper:** "Does Auxiliary Spatial Supervision Make VLAs Safer? An Empirical Investigation"
**Venue:** CoRL 2026
**Review Mode:** Full (2 Reviewers + Roundtable)
**Dream ID:** 20260523T034027

---

## Overall Assessment

**Overall Score: 4 / 10 — Weak Reject**

Both reviewers independently arrived at 4/10 (Weak Reject) with highly aligned reasoning. The paper's primary finding — that detaching auxiliary head gradients harms VLA safety (CAR −3.4pp, Glass's Δ = 2.83, p < 0.01) — is robust, well-characterized, and practically useful. However, this single strong result is insufficient for acceptance at CoRL given: (1) the core mechanistic insight (gradient flow as regularization) is a well-known prediction of multi-task learning theory, (2) the paper's mechanism analysis attempts (CKA, gradient cosine) both yield null results, and (3) the positive claims ("spatial content doesn't matter") rest on underpowered non-significant comparisons that cannot distinguish "no effect" from "undetectable effect."

---

## Reviewer 1 (R1): Methods & Experiments

### Summary
The paper presents a six-condition factorial study on SafeLIBERO-Spatial examining whether auxiliary spatial supervision improves VLA collision avoidance. The central finding is that gradient flow from the auxiliary head is necessary to prevent safety degradation, while the content of the auxiliary task is secondary. The Detach condition (no gradient flow) shows a significant 3.4pp CAR drop, while all gradient-flow conditions are indistinguishable from the no-auxiliary baseline.

### Strengths
1. **Well-structured factorial design** with appropriate controls, especially the Random OCC condition as a gradient-flow-matched content control.
2. **Sound statistical methodology for the Detach finding** — Glass's Δ = 2.83 with bootstrap CIs is rigorous and convincing.
3. **Honest reporting** — null results (CKA, gradient analysis) are transparently presented rather than hidden, and limitations are thoroughly acknowledged.
4. **Comprehensive ablation ladder** — cutoff, reverse cutoff, Detach+LayerNorm provide a thorough investigation of the gradient flow mechanism.

### Weaknesses
1. **(Major) No positive result.** No condition significantly outperforms Vanilla (all CIs overlap zero), so the paper's contribution reduces to a narrow engineering guideline: "do not detach gradients." This is a cautionary finding, not a method advancement.
2. **(Major) Critically underpowered for positive claims.** With n=3 seeds and observed variances (σ ≈ 0.012–0.037), the study can only detect effects ≥3–5pp. Claiming "spatial content doesn't matter" when the study lacks power to detect moderate effects (1–3pp) conflates statistical non-significance with absence of effect. The confidence intervals are wide (e.g., Full OCC vs Vanilla: [−1.5pp, +4.9pp]).
3. **(Major) Single benchmark, single architecture.** All experiments use SafeLIBERO-Spatial with OpenVLA + LoRA. The planned second benchmark (LIBERO-Object/Goal) was not executed. Ceiling effects on 7/10 tasks (CAR > 0.9) compress the measurable signal, and the practical guideline cannot be verified on other VLA architectures or training regimes.
4. **(Major) Dose-response analysis is inconclusive.** Three of four cutoff points use n=1, producing non-monotonic CAR values (0.762, 0.775, 0.777, 0.769) that prevent any dose-response conclusion. The reverse cutoff is confounded with the exponential decay schedule (weight already ≈ 0.005 at step 35K). The "binary switch" claim is not falsifiable with this design.
5. **(Moderate) Missing simpler baselines.** The "regularizer" interpretation is never tested against alternatives: Does L2 regularization on encoder parameters achieve the same effect? Does a random-initialized auxiliary head with gradient flow match Full OCC? These controls would sharpen the mechanistic argument.
6. **(Moderate) Forward-pass confounds in Detach.** The Detach condition adds 1.2M parameters to the forward pass that consume encoder features without contributing gradients. The degradation could partly reflect computational interference (attention, memory) rather than gradient flow absence per se. The Detach+LayerNorm control addresses BatchNorm but not this broader confound.
7. **(Minor) Per-task analysis lacks error bars.** Table 4 reports 3-seed averages but no standard deviations. Given that some per-task CARs are based on only 50 episodes × 3 seeds = 150 trials, the sampling noise on individual tasks is high.

### Questions for Authors
1. Could you add L2 regularization or weight decay to the Vanilla encoder and compare its CAR with the gradient-flow conditions? This would test whether any auxiliary head is needed or if simple regularization suffices.
2. What is the forward-pass computational overhead of the Detach condition? If the 1.2M-parameter head consumes meaningful encoder bandwidth, the degradation may partly be architectural rather than gradient-related.
3. The Detach CAR standard deviation (σ = 0.002) is suspiciously small — far smaller than any other condition. Is this an artifact of all three seeds converging to the same failure mode? What are the individual seed CAR values?
4. Would you expect these results to hold under full fine-tuning (not LoRA)? The conservative scaling factor (α/rank = 0.5) constrains updates — gradient flow effects might differ dramatically when the encoder is fully plastic.

### Scores (R1)
| Criterion | Score | Note |
|-----------|-------|------|
| Overall | 4/10 | Weak Reject |
| Originality | 2/5 | Factorial design is clean but not methodologically novel; the core finding is a single negative result |
| Quality | 3/5 | Statistical rigor strong for Detach finding; underpowered for all other comparisons; CKA/gradient null |
| Clarity | 4/5 | Well-organized, honest, clear tables |
| Significance | 2/5 | Narrow practical guideline; no new method or positive capability |
| Relevance | 4/5 | Core CoRL topic (robot learning safety) |
| Confidence | 4/5 | |

---

## Reviewer 2 (R2): Novelty & Related Work

### Summary
The paper conducts a factorial study crossing auxiliary task content with gradient flow configuration to investigate VLA safety during fine-tuning. The core finding is an asymmetry: gradient flow prevents safety degradation but spatial content is secondary. The paper frames this as a "mechanism analysis" but the operative mechanism is not identified — CKA and gradient analyses yield null results. The honest contribution is narrower than claimed: a cautionary finding about gradient detachment plus a reusable factorial design.

### Strengths
1. **The research question addresses a genuine gap.** The spatial-VLA literature and safety-VLA literature have developed in isolation; no prior work systematically measures collision avoidance outcomes under different auxiliary configurations.
2. **The Detach degradation is robust and well-characterized.** CAR = 0.746 ± 0.002 across 3 seeds, Glass's Δ ≈ 2.83, with corroborating TSR instability (σ = 0.163). This is a clean, high-confidence finding.
3. **Related work is well-structured and comprehensive** for the VLA safety and spatial VLA threads. The three-subsection organization correctly positions the paper at the intersection.
4. **Factorial design is methodologically sound and reusable.** The inclusion of Random OCC as a gradient-flow-matched content control is an elegant design choice.
5. **Honest calibration of claims.** The paper correctly frames the result as "gradient flow prevents degradation" rather than "gradient flow improves safety."

### Weaknesses
1. **(Major) Limited novelty given MTL theory precedents.** The observation that auxiliary gradient flow regularizes shared representations is a direct prediction of multi-task learning theory (Caruana 1997, Ruder 2017). The finding that random labels work as well as structured labels under gradient flow is also predicted by the regularization interpretation. The paper does not engage with the broader MTL gradient management literature:
   - GradNorm (Chen et al., ICML 2018) on adaptive gradient balancing
   - PCGrad (Yu et al., NeurIPS 2020) on gradient conflict in shared representations
   - CAGrad (Liu et al., NeurIPS 2021) and NashMTL (Navon et al., ICML 2022) for theoretical frameworks
   These methods provide both theoretical tools and empirical metrics (gradient cosine, conflict rates) directly applicable to this setup.

2. **(Major) No mechanistic resolution.** The paper proposes three candidate mechanisms (anti-overfitting regularization, optimization landscape smoothing, gradient diversity) but cannot distinguish between them. CKA: all values > 0.85. Gradient cosine: near zero, Full OCC ≈ Random OCC. A paper titled "Empirical Investigation" that cannot identify the operative mechanism is in an awkward position — the observation is clear, the explanation is not.

3. **(Major) Positive claims are statistically unsupported.** The "spatial content doesn't matter" claim rests on non-significant comparisons with wide confidence intervals. With n=3–4 and reported variances, the ordering Full OCC > Random OCC > Depth ≈ Vanilla could easily be sampling noise. The paper should restrict conclusions to the robust Detach finding and treat gradient-flow-condition orderings as exploratory.

4. **(Major) Missing connection to catastrophic forgetting / continual learning.** The "damage prevention" framing — gradient flow prevents the encoder from losing pretrained spatial features — maps directly onto catastrophic forgetting. Relevant work (EWC, SI, LoRA-forgetting studies) is not discussed, which is a significant omission for a paper claiming mechanistic contribution.

5. **(Minor-Major) Contribution inflation.** Three contributions are claimed:
   - C1 "Mechanism identification": mechanism is not actually identified
   - C2 "Factorial ablation design": clean but standard methodology
   - C3 "Practical guideline": useful but obvious once Detach result is known
   
   More honest: (1) first empirical evidence that auxiliary spatial supervision does not improve VLA collision avoidance, and (2) detaching auxiliary gradients actively harms — a cautionary finding.

6. **(Minor) Uncited bibliography entries.** Several spatial VLA papers appear in the bibliography but are never cited in text. If the paper claims to survey 15+ spatial VLA methods, these should be cited to substantiate that claim.

### Questions for Authors
1. How do you position this work relative to PCGrad/CAGrad/NashMTL? Have you computed the gradient conflict metrics these methods propose?
2. The connection to catastrophic forgetting seems direct — does gradient flow from the auxiliary head act as an anchor preventing encoder feature drift? Have you considered EWC-style analysis?
3. With n=3 and the observed variances, what is your power to detect a true 2pp CAR difference between conditions? If power is below 50%, how do you justify the "content doesn't matter" claim?
4. Under full fine-tuning (not LoRA), would you expect the gradient flow effect to be larger or smaller? This matters for the generalizability of the practical guideline.
5. The exponential decay schedule confounds the temporal analysis. Would a constant-weight design provide cleaner temporal dynamics evidence?

### Scores (R2)
| Criterion | Score | Note |
|-----------|-------|------|
| Overall | 4/10 | Weak Reject |
| Originality | 2/5 | Domain-specific verification of well-known MTL phenomenon; incremental |
| Quality | 3/5 | Strong design, underpowered inference, null mechanism analyses |
| Clarity | 4/5 | Clear writing, honest limitations |
| Significance | 2/5 | Narrow guideline, negative result limits impact |
| Relevance | 4/5 | Directly addresses robot learning safety |
| Confidence | 4/5 | |

---

## Roundtable Synthesis

### Step 2: Cross-Sharing — Points of Agreement
Both reviewers independently converge on the same overall assessment and share four core concerns:
1. **Limited novelty**: The gradient-flow-as-regularization insight is predicted by classical MTL theory. Domain verification in VLA safety is new but incremental.
2. **Underpowered positive claims**: n=3 seeds with the observed variances cannot support the "content doesn't matter" claim. Non-significance ≠ no effect.
3. **Mechanism depth is shallow**: Both CKA and gradient analyses yield null results. The paper cannot adjudicate between its own three candidate mechanisms.
4. **Single benchmark/architecture**: Generalizability is untested; the practical guideline applies only to OpenVLA + LoRA on SafeLIBERO-Spatial.

### Step 2: Cross-Sharing — Complementary Insights
- R1 uniquely identifies: need for simpler regularization baselines (L2, weight decay), forward-pass confounds in Detach, suspiciously low Detach CAR variance (σ=0.002)
- R2 uniquely identifies: missing catastrophic forgetting literature, missing MTL gradient conflict literature (PCGrad, CAGrad), contribution inflation, uncited bibliography entries

### Step 3: Convergence
No disagreements to resolve. Both reviewers assign 4/10 with identical sub-scores on all dimensions. The convergence reflects a clear assessment: one robust negative finding (Detach harm) is necessary but not sufficient for a CoRL publication. The paper needs either (a) deeper mechanism analysis with positive results, (b) a second benchmark demonstrating generality, or (c) a method contribution (not just a finding).

### Step 4: Final Consolidated Scores

| Dimension | R1 | R2 | Consolidated |
|-----------|----|----|-------------|
| Overall | 4/10 | 4/10 | **4/10 (Weak Reject)** |
| Originality | 2/5 | 2/5 | 2/5 |
| Quality | 3/5 | 3/5 | 3/5 |
| Clarity | 4/5 | 4/5 | 4/5 |
| Significance | 2/5 | 2/5 | 2/5 |
| Relevance | 4/5 | 4/5 | 4/5 |

---

## Consolidated Verdict

**Score: 4/10 — Weak Reject**

The paper addresses a genuine gap at the intersection of VLA safety and spatial auxiliary supervision. The factorial design is clean, the Detach degradation finding is robust (Glass's Δ = 2.83, p < 0.01), and the writing is clear and honest. However, the contribution does not meet the CoRL acceptance threshold for three reasons:

1. **Novelty gap**: The core insight — gradient flow from auxiliary heads provides regularization, and its content matters less than its presence — is well-established in the multi-task learning literature. The paper verifies this in a new domain but does not advance understanding of the phenomenon.

2. **Mechanism analysis failure**: Despite extensive effort (CKA, gradient cosine, temporal ablation, BatchNorm control), the paper cannot identify *why* gradient detachment harms safety. The CKA and gradient analyses both yield null results. This leaves the paper's contribution as a descriptive finding without explanatory depth.

3. **Statistical limitations**: The "spatial content is secondary" claim and the "binary switch" claim both rest on underpowered non-significant comparisons (n=3, wide CIs). The dose-response analysis uses n=1 per intermediate cutoff point.

### Recommendations for Strengthening
- **Add simpler baselines**: L2 regularization, weight decay on encoder. If these match auxiliary-head gradient flow, the finding becomes cleaner (any regularization works) but also less novel. If they don't match, the auxiliary head has a specific regularization benefit worth investigating.
- **Second benchmark**: Even a reduced experiment (3 conditions × 2 seeds on LIBERO-Object) would substantially strengthen generalizability.
- **Engage MTL gradient literature**: Position explicitly against PCGrad/CAGrad framework; compute their proposed metrics.
- **Reframe contributions**: Drop "mechanism analysis" framing. Lean into "cautionary empirical study" — the honest contribution is the Detach finding plus the practical guideline.
- **Increase statistical power**: n=5 seeds per core condition would detect 2pp effects with reasonable power.

---

## 引用验证结果

**统计**: 46 篇文献 / 56 处引用 / 在线验证 46/46 篇

### 问题 (22)

- ⚠️ `kwon2026learningnudge` — 元数据不匹配: first_author: bib=kwon vs api=jin
- ⚠️ `chen2026gstvla` — 元数据不匹配: first_author: bib=chen vs api=sarowar
- ⚠️ `wu2025spatialvla` — 元数据不匹配: first_author: bib=wu vs api=qu
- ⚠️ `ranftl2022midas` — 元数据不匹配: year: bib=2022 vs api=2019
- ⚠️ `ma2026vlanext` — 元数据不匹配: first_author: bib=ma vs api=wu
- ⚠️ `yu2026safenightvla` — 在 .bib 中但正文未引用
- ⚠️ `li2026vlasafety` — 在 .bib 中但正文未引用
- ⚠️ `kwon2026learningnudge` — 在 .bib 中但正文未引用
- ⚠️ `long2025neuralcsbf` — 在 .bib 中但正文未引用
- ⚠️ `chen2026gstvla` — 在 .bib 中但正文未引用
- ⚠️ `li2025qdepthvla` — 在 .bib 中但正文未引用
- ⚠️ `abouzeid2025geoaware` — 在 .bib 中但正文未引用
- ⚠️ `lin2025evo0` — 在 .bib 中但正文未引用
- ⚠️ `tu2026sgvla` — 在 .bib 中但正文未引用
- ⚠️ `xiao2026stemvla` — 在 .bib 中但正文未引用
- ⚠️ `bhat20253dcavla` — 在 .bib 中但正文未引用
- ⚠️ `li2026corridorvla` — 在 .bib 中但正文未引用
- ⚠️ `sun2025geovla` — 在 .bib 中但正文未引用
- ⚠️ `pan2026savla` — 在 .bib 中但正文未引用
- ⚠️ `ma2026vlanext` — 在 .bib 中但正文未引用
- ⚠️ `shukor2025smolvla` — 在 .bib 中但正文未引用
- ⚠️ `choi2026vlaeval` — 在 .bib 中但正文未引用

### ✅ 通过 (41)