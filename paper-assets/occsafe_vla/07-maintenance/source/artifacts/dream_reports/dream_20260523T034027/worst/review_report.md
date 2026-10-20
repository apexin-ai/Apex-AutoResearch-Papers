---
dream_id: dream_20260523T034027
tier: worst
overall_score: 4/10 — Reject
timestamp: 2026-05-23T04:50:32.279589+00:00
---

# Dream Review Report — CoRL 2026 Submission

**Paper:** "Hidden Pitfalls of Auxiliary Heads in VLA Fine-tuning: A Cautionary Study on BatchNorm, Gradient Flow, and Safety"

**Venue:** CoRL 2026 (acceptance rate ~39-40%, OpenReview 1-10 scale)

**Review Mode:** Full (2 Reviewers + Roundtable)

---

## Reviewer Assignments

| Reviewer | Focus | Overall Score |
|----------|-------|---------------|
| R1 | Methods + Experiments | 4/10 |
| R2 | Novelty + Related Work | 4/10 |
| **Consensus** | — | **4/10 (Reject)** |

---

## Step 1: Independent Reviews

### Reviewer 1 (R1) — Methods and Experiments

#### Summary
The paper investigates whether auxiliary spatial supervision improves VLA safety through a 5-condition factorial study on OpenVLA/SafeLIBERO. The initial finding that detaching auxiliary gradients degrades CAR by -3.4pp is attributed entirely to a BatchNorm evaluation artifact after replacing BN with LN eliminates the degradation. CKA and gradient cosine analyses yield null mechanistic signals, and a dose-response cutoff experiment shows a non-monotonic U-shape.

#### Strengths
- **Well-designed factorial ablation.** The 5-condition design (Full OCC, Random OCC, Detach, Depth, Vanilla) cleanly isolates gradient flow from label content. Random OCC as a content control is elegant.
- **Honest self-correction narrative.** Willingness to present and then dismantle the initial gradient-flow hypothesis is commendable and pedagogically clear.
- **Practical relevance.** The BN pitfall in detached auxiliary heads is genuinely useful for practitioners. The LN recommendation is immediately actionable.
- **Comprehensive condition coverage.** ~500+ GPU hours across 5 primary conditions with 3-4 seeds each, plus ablations.
- **Clear BN mechanism exposition.** Section 5's explanation of how BN running statistics drift from the encoder's actual output distribution is well-articulated.

#### Weaknesses

**W1 [CRITICAL]: The "fatal experiment" (Detach+LN) uses a single seed but bears the entire weight of the paper's central claim.**
The paper's core thesis—that Detach degradation is "entirely" a BN artifact—rests on a single data point: Detach+LN CAR = 0.782. Detach+BN has 3 seeds at 0.746 ± 0.002 (tight), and Vanilla has 3 seeds at 0.780 ± 0.012. With n=1, we cannot know whether 0.782 is the mean, an outlier, or a lucky seed. Vanilla seeds span a ~22pp range (0.766–0.788). A single seed of 0.782 is consistent with a true mean anywhere in [0.745, 0.815]. The claim that "100% of the Detach degradation" is eliminated is extraordinary and supported by a single observation. Three seeds are the minimum required.

**W2 [CRITICAL]: Cutoff@35K seed 44 is "predicted," not actual data, yet appears in 3-seed aggregates.**
Table 10 marks seed 44 as "predicted." Including imagined data in aggregate statistics (CAR = 0.746 ± 0.066) is methodologically unacceptable. With only 2 actual seeds (s0: 0.768, s1: 0.798), the real mean is 0.783 ± 0.021—essentially identical to Vanilla (0.780). This undermines the U-shaped dose-response narrative and the claim that Cutoff@35K causes harm.

**W3 [MAJOR]: Dose-response analysis is severely underpowered (n=1 per cutoff point).**
Cutoff@15K, @25K, @45K each use a single seed. The total spread (15K: 0.758, 25K: 0.742, 45K: 0.774) is 3.2pp—well within plausible seed variance observed in other conditions (e.g., Vanilla σ=0.012, Full OCC σ=0.032). The U-shape could easily be noise. The paper acknowledges this but still draws the conclusion that the pattern "contradicts the gradient flow hypothesis." This is overclaiming from underpowered data.

**W4 [MAJOR]: CKA may be structurally insensitive to the relevant representational differences.**
All CKA > 0.93. However, LoRA rank=32 with scaling=0.5 modifies only a low-rank subspace. CKA measures global representational similarity and may be unable to detect small but functionally important changes in a low-dimensional subspace. The 3.4pp CAR difference could be driven by changes invisible to CKA. The paper should discuss CKA's sensitivity limits rather than treating high CKA as definitive evidence of no divergence.

**W5 [MAJOR]: Gradient analysis at step 50K is uninformative about cumulative training dynamics.**
At step 50K, the occ_loss weight has decayed to 0.01 × exp(−1) ≈ 0.0037—near zero by design. Measuring gradients at peak auxiliary influence (steps 1K–10K, where weight ≈ 0.008–0.01) would be far more informative. Concluding that "gradient flow contribution is too weak" based on the endpoint is analogous to measuring a car's speed at the finish line and concluding it never went fast.

**W6 [MAJOR]: The BN artifact mechanism has a logical gap—how does OccHead's BN affect action prediction?**
In a properly implemented system, the OccHead is not used at evaluation time. If truly independent at eval, its BN statistics should have zero effect on action prediction. The paper does not explain through what pathway the mismatched BN statistics interfere. Possible explanations (OccHead not properly disabled during eval, shared memory/buffer effects, in-place operations during training) are not discussed. Without this, the proposed mechanism is incomplete.

**W7 [MODERATE]: No cross-benchmark replication.** Single benchmark (SafeLIBERO, 10 tasks). The planned LIBERO-Object/Goal replication was not executed.

**W8 [MODERATE]: Single VLA architecture with a single fine-tuning regime.** All experiments use OpenVLA with LoRA. Results may not generalize to full fine-tuning or other VLA architectures.

#### Questions for Authors
1. Can you run ≥2 additional seeds for Detach+LN? This is the paper's most critical experiment.
2. Is the OccHead's forward pass executed during evaluation? If not, how do BN running statistics in a dormant module affect action prediction?
3. Is Cutoff@35K seed 44 actual or predicted? Please provide only actual data in tables.
4. Have you computed gradient cosine at steps 5K or 10K when occ_loss weight is 2-3× larger?
5. Have you tested Full OCC + LN to confirm BN is harmless when gradient flow keeps statistics aligned?
6. Have you tested a constant occ_loss weight (no decay) to verify the U-shape isn't a decay-schedule artifact?

#### Missing Experiments
1. **Detach+LN with 3 seeds** (~39 GPU hours) — essential for the central claim.
2. **Full OCC + LN** (1 seed, ~13 GPU hours) — needed to confirm LN doesn't introduce its own confound.
3. **Gradient analysis at early checkpoints** (negligible compute).
4. **Detach+BN with OccHead removed at eval** (no training cost) — tests whether BN artifact operates at eval time or through training-time effects.
5. **Second benchmark replication** (78 GPU hours).

#### R1 Scores

| Dimension | Score | Justification |
|-----------|-------|---------------|
| Soundness | 4/10 | Central claim rests on n=1. Cutoff includes predicted data. Mechanism gap unexplained. |
| Empirical Rigor | 4/10 | Core factorial solid (3-4 seeds), but critical experiments single-seed. Dose-response underpowered. Mixing actual/predicted data is a methodological error. |
| Reproducibility | 6/10 | Architecture, hyperparameters, training details well-specified. SafeLIBERO is public. Gap: some results appear predicted. |
| **Overall** | **4/10** | Potentially interesting confound identification, but insufficient statistical evidence for the central claim. Better positioned as a workshop paper. With 3-seed Detach+LN and mechanism clarification, could rise to 6. |

**R1 Confidence:** 4/5

---

### Reviewer 2 (R2) — Novelty and Related Work

#### Summary
The paper tests whether auxiliary spatial supervision improves collision avoidance in VLA fine-tuning. The five-condition factorial design on OpenVLA/SafeLIBERO finds that detaching gradients from the auxiliary head degrades CAR by -3.4pp, but this degradation is entirely eliminated by replacing BatchNorm with LayerNorm, revealing the finding as a known BatchNorm engineering artifact rather than a gradient flow mechanism. No auxiliary condition significantly outperforms Vanilla.

#### Strengths
- **Addresses a genuine research gap.** The spatial-VLA and VLA-safety literatures have developed independently; no prior work systematically measures how auxiliary spatial supervision affects collision avoidance.
- **Clean factorial design with well-chosen controls.** Random OCC as a gradient-flow-matched content control is elegant. The 5 conditions form a systematic ablation chain.
- **Robust Detach degradation finding.** CAR = 0.746 with σ = 0.002 across 3 seeds is remarkably consistent. The -3.4pp gap is directionally unambiguous.
- **Honest calibration of claims.** The paper correctly frames "gradient flow prevents degradation" rather than "gradient flow improves safety." Limitations section is thorough.
- **Clear writing and organization.** Tables are well-structured, factorial design presented with exemplary clarity.

#### Weaknesses

**W1 [MAJOR]: The core finding is a well-known engineering pitfall, not a novel scientific insight.**
The paper's central contribution reduces to: "detaching gradients from a shared encoder while keeping a BatchNorm-containing head in the forward pass degrades performance." BN pitfalls in transfer learning and domain adaptation are extensively documented:
- Ioffe & Szegedy (2015): original BN paper notes train/eval discrepancy
- Li et al. (2018, "Revisiting Batch Normalization for Practical Domain Adaptation"): BN statistics mismatch degrades transfer
- Frankle et al. (2021, "Training BatchNorm and Only BatchNorm"): BN statistics alone capture substantial task information

The paper acknowledges BN pitfalls are "well-documented" in Related Work. Rediscovering a known artifact in VLA auxiliary heads is insufficient novelty for a top venue.

**W2 [MAJOR]: No positive result—the paper's contribution reduces to a narrow cautionary observation.**
No auxiliary condition significantly outperforms Vanilla. Full OCC's +1.7pp is within seed variance (σ=0.032). The actionable contribution is: "if you attach a BN-containing auxiliary head with detached gradients, it will hurt; don't do that." Useful but extremely narrow for CoRL.

**W3 [MAJOR]: The "mechanism identification" claim (C1) is not supported.**
Three candidate mechanisms (anti-overfitting regularization, optimization landscape smoothing, gradient diversity) are proposed and explicitly stated as indistinguishable. CKA (>0.93) and gradient cosine (≈0) yield null results. A paper claiming mechanism identification but unable to identify the mechanism overstates its contribution. If the finding is simply "BN artifact," then C1 should be reframed as "engineering pitfall identification."

**W4 [MAJOR]: Statistical power insufficient for secondary claims.**
- Full OCC vs. Random OCC: 0.8pp difference with σ≈0.031, n=3. Power to detect a 2pp true difference is well below 50%.
- "Label content is secondary" conflates statistical non-significance with absence of effect.
- No bootstrap confidence intervals or formal significance tests for any pairwise comparison.

**W5 [MAJOR]: Missing engagement with the multi-task learning gradient management literature.**
The gradient-flow-as-regularization insight is a textbook prediction of MTL theory (Caruana 1997, cited but not engaged with). Critical missing references:
- GradNorm (Chen et al., ICML 2018)
- PCGrad (Yu et al., NeurIPS 2020)
- CAGrad (Liu et al., NeurIPS 2021)
- NashMTL (Navon et al., ICML 2022)

The finding that action/OCC gradient cosine ≈ 0 (orthogonal) is a well-characterized "benign" regime in MTL literature. The paper computes this metric but does not connect to this body of work.

**W6 [MODERATE]: Missing connection to catastrophic forgetting and continual learning.**
The "damage prevention" framing maps directly onto catastrophic forgetting literature (EWC, Progressive Neural Networks, LoRA forgetting studies). This connection is absent despite being central to interpreting results.

**W7 [MODERATE]: Framing artifacts from multiple narrative pivots.**
The paper evolved from "occupancy improves safety" → "gradient flow prevents degradation" → "BatchNorm pitfall." The Depth and Cutoff conditions feel appended rather than integrated into a unified hypothesis.

**W8 [MINOR]: Bibliography hygiene.** 15+ entries in the .bib file are never cited. Several have metadata mismatches, suggesting bulk import rather than curation.

#### Assessment of Novelty Relative to Known BN Pitfalls
Since Detach+LN eliminates degradation (CAR = 0.782 ≈ Vanilla = 0.780), the contribution reduces to observing that BN running statistics in a detached auxiliary head interfere with VLA evaluation. This is a known engineering pitfall applied to a new architecture. The "gradient flow is necessary" narrative collapses. **Novelty: very low.**

#### Missing Related Work
1. **BatchNorm in transfer learning:** Li et al. (2018), Frankle et al. (2021), Singh & Jaggi (2020)
2. **Stop-gradient in representation learning:** SimSiam (Chen & He, CVPR 2021), BYOL (Grill et al., NeurIPS 2020)
3. **MTL gradient management:** GradNorm, PCGrad, CAGrad, NashMTL
4. **Catastrophic forgetting:** EWC, Progressive Neural Networks, LoRA forgetting studies
5. **Auxiliary tasks in ViTs:** literature on how auxiliary tasks interact with ViT-specific architectures

#### R2 Scores

| Dimension | Score | Justification |
|-----------|-------|---------------|
| Novelty/Originality | 3/10 | Core finding is a well-documented BN pitfall applied to a new domain. Factorial design is clean but standard. Even without BN confound, gradient-flow-as-regularization is predicted by 30 years of MTL theory. |
| Significance | 3/10 | Practical guideline is narrow ("use LN not BN in detached heads"). No condition improves over Vanilla. Does not change practice for anyone following standard BN hygiene. |
| Clarity | 7/10 | Well-written, well-organized, honest about limitations. Tables are clear. Factorial design presented with exemplary clarity. |
| Relevance to CoRL | 5/10 | Robot learning safety is core CoRL territory, but the paper is fundamentally about a BN engineering observation. No real-robot experiments. Simulation-only, single benchmark. |
| **Overall** | **4/10** | Below acceptance threshold. Strong experimental design, but novelty insufficient for a top venue. Core insight (BN in detached heads causes degradation) is known. The auxiliary spatial supervision hypothesis yields a null result. Better suited as a CoRL workshop paper or IROS short paper. |

**R2 Confidence:** 4/5

---

## Step 2: Cross-Sharing

After exchanging reviews, both reviewers noted the following convergences and divergences:

**Convergences:**
- Both agree the factorial experimental design is methodologically clean and the paper is well-written.
- Both identify the single-seed Detach+LN experiment as a critical statistical weakness.
- Both score the paper 4/10 overall—below the acceptance threshold.
- Both agree the paper's honest narrative about hypothesis dissolution is commendable.
- Both flag that the mechanism by which OccHead BN affects action prediction is unexplained.

**Divergences:**
- R1 focuses on the predicted-data issue (Cutoff@35K s2) as a separate critical flaw; R2 does not emphasize this as strongly.
- R2 places more weight on the novelty deficit (BN pitfalls are well-documented); R1 treats this as a "minor issue" but focuses on statistical inadequacy.
- R2 identifies substantial missing related work (MTL gradient management, catastrophic forgetting, stop-gradient representation learning); R1 focuses on missing experiments.

---

## Step 3: Convergence Discussion

**R1:** "My core concern is empirical: the central claim rests on n=1. Even if we grant the novelty, the evidence is insufficient. The predicted data in Cutoff@35K aggregates is an additional methodological error that taints the dose-response narrative."

**R2:** "My core concern is conceptual: even with perfect statistical support, the finding is a rediscovery of a known BN pitfall in a new context. This is useful but not novel enough for CoRL. The MTL gradient management literature already provides the theoretical framework for understanding these phenomena."

**Joint assessment:** Both concerns are load-bearing and independent. Even if R1's statistical concerns were addressed (3-seed Detach+LN, actual data only), R2's novelty concern would remain. Conversely, even if R2's novelty bar were relaxed (accepting domain-specific cautionary studies), R1's evidence gaps would still prevent acceptance. The paper faces a two-front challenge.

**Score convergence:** Both reviewers independently arrived at 4/10. After discussion, both maintain this score. The paper is solidly below the acceptance threshold but not without merit—the experimental design and honest narrative deserve recognition.

---

## Step 4: Consolidated Assessment

### Overall Score: 4/10 — Reject

### Meta-Review

This paper presents a systematically designed factorial study investigating whether auxiliary spatial supervision improves collision avoidance in VLA fine-tuning. The experimental design—5 primary conditions isolating gradient flow, label content, and spatial reference frame—is methodologically clean, and the paper's honest narrative about hypothesis dissolution (from "gradient flow is necessary" to "it's a BatchNorm artifact") is commendable. The writing is clear and well-organized.

However, the paper has fundamental weaknesses in both evidence and novelty:

**Evidence (R1's concerns):**
1. The central claim (Detach harm is 100% BN artifact) rests on a single-seed Detach+LN experiment (CAR = 0.782). With n=1, this is insufficient to support an "entirely" attribution claim. Three seeds are the minimum bar.
2. The Cutoff@35K 3-seed aggregate includes a "predicted" (not actually run) seed, which is methodologically unacceptable. With only 2 actual seeds, the Cutoff@35K mean (0.783) is indistinguishable from Vanilla (0.780), undermining the dose-response narrative.
3. The dose-response analysis uses single seeds per cutoff point. The 3.2pp spread across the U-shape is within plausible seed variance.
4. The gradient analysis is performed at step 50K where the auxiliary loss weight has decayed to near zero, making it uninformative about cumulative training effects.
5. The mechanism by which a dormant OccHead's BN statistics affect action prediction at eval time is never explained.

**Novelty (R2's concerns):**
1. The core finding—BN running statistics in detached heads cause eval-time degradation—is a well-documented pitfall in the transfer learning and domain adaptation literature. The paper acknowledges this in Related Work but does not sufficiently differentiate its contribution.
2. No auxiliary condition significantly outperforms Vanilla, yielding a null result for the primary hypothesis. The actionable guideline ("use LN instead of BN when detaching") is useful but narrow.
3. The paper is missing engagement with substantial related literatures: MTL gradient management (GradNorm, PCGrad, CAGrad), catastrophic forgetting (EWC), and stop-gradient representation learning (SimSiam, BYOL).
4. The "mechanism identification" contribution (C1) overpromises—three candidate mechanisms are proposed without resolution, and the actual "mechanism" is a known engineering artifact.

**What would improve the paper:**
1. **[Essential]** Run Detach+LN with 3 seeds (~39 GPU hours). If the 3-seed mean confirms CAR ≈ 0.780, the BN artifact claim becomes credible.
2. **[Essential]** Remove predicted data from all tables and re-analyze with actual data only.
3. **[Important]** Explain the eval-time pathway: how does OccHead BN affect action prediction when OccHead is not used at inference?
4. **[Important]** Engage with MTL gradient management and BN transfer learning literatures to position the contribution more precisely.
5. **[Helpful]** Run gradient analysis at early training steps (5K-10K) where auxiliary loss weight is higher.
6. **[Helpful]** Add a second benchmark or second VLA architecture for generalizability.
7. **[Framing]** Reframe from "mechanism identification" to "engineering pitfall identification." The paper's value is cautionary and practical, not mechanistic.

### Dimension Scores (Consensus)

| Dimension | Score | Notes |
|-----------|-------|-------|
| Originality | 3/10 | Known BN pitfall in a new domain. Null result for primary hypothesis. |
| Quality / Soundness | 4/10 | Clean design but central claim unsupported (n=1). Predicted data in aggregates. Mechanism gap. |
| Clarity | 7/10 | Well-written, well-organized, honest. Tables are clear. |
| Significance | 3/10 | Narrow practical guideline. No safety improvement demonstrated. |
| Relevance to CoRL | 5/10 | Robot safety is core CoRL, but this is an engineering observation, not a mechanism study. No real-robot experiments. |
| **Overall** | **4/10** | Below acceptance threshold. Recommend reject with encouragement to resubmit after addressing statistical gaps and novelty positioning. |

### Recommended Venue
- **CoRL 2026 Workshop** (Robot Safety or VLA Fine-tuning): appropriate scope for current evidence level.
- **IROS 2026 short paper**: good fit for an engineering cautionary finding with practical guidelines.
- **CoRL 2027 full paper**: if strengthened with 3-seed Detach+LN, second benchmark, mechanism explanation, and proper literature engagement.

### Confidence: 4/5
Both reviewers are confident in this assessment. The statistical weaknesses (n=1 for central claim, predicted data) and novelty gap (known BN pitfall) are clear-cut and unlikely to be overturned by author response alone.


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